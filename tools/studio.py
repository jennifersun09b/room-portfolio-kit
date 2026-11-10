#!/usr/bin/env python3
"""
3D ROOM PORTFOLIO KIT  -  ROOMKIT STUDIO
========================================
A visual builder for your 3D room portfolio that runs in your web browser. No terminal, no JSON,
no Blender know-how needed: Studio finds Blender, runs it in the background and shows the progress.

HOW TO START
  Double-click Start.command (Mac), Start.bat (Windows) or start.sh (Linux), or run:
    python3 tools/studio.py
Options:
  --port N          first port to try (default 8765; the next free one is used)
  --workspace DIR   where projects are kept (default: ~/RoomKit Projects)
  --no-browser      don't open the browser automatically
  --blender PATH    use exactly this Blender (the BLENDER environment variable is also checked)

Everything stays on your computer. The server only listens on 127.0.0.1 and every request from the
page carries a secret token, so other websites can't talk to it. API keys for AI 3D models are kept in
~/.roomkit/keys.json (only readable by you), never inside a project folder.

Python 3.9+ standard library only - nothing to install.
"""

import sys

if sys.version_info < (3, 9):
    print("RoomKit Studio needs Python 3.9 or newer. Get it free from https://www.python.org/downloads/")
    sys.exit(1)

import argparse
import glob
import hashlib
import http.server
import json
import mimetypes
import os
import platform
import re
import secrets
import shutil
import signal
import socket
import subprocess
import threading
import time
import traceback
import urllib.parse
import uuid
import webbrowser
import zipfile

KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(KIT, "tools")
UI = os.path.join(TOOLS, "studio")
ROOMS_JSON = os.path.join(UI, "rooms.json")
HOME = os.path.expanduser(os.environ.get("ROOMKIT_HOME") or os.path.join("~", ".roomkit"))
KEYS_FILE = os.path.join(HOME, "keys.json")
SETTINGS_FILE = os.path.join(HOME, "studio.json")
DEFAULT_WORKSPACE = os.path.join(os.path.expanduser("~"), "RoomKit Projects")
MIN_BLENDER = (4, 2)
BLENDER_DOWNLOAD = "https://www.blender.org/download/"
BLENDER_LTS = "https://www.blender.org/download/lts/4-2/"
WINDOWS = os.name == "nt"
MAC = sys.platform == "darwin"

KEY_NAMES = {"meshy": "MESHY_API_KEY", "fal": "FAL_KEY", "hf": "HF_TOKEN"}
IMAGE_TYPES = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"}
MODEL_TYPES = {".glb", ".gltf", ".obj", ".fbx", ".stl"}
ALL_EXPORTS = ["hero", "og", "instagram", "banner", "behance", "dribbble", "story", "obs4k"]
CLASSIC_EXPORTS = ["hero", "og", "instagram", "banner"]          # what build_portfolio.py makes without --exports
DEFAULT_TIMES = {                                                 # seconds, refined from real runs on this computer
    "room": 20, "furniture_photo": 12, "furniture_model": 15, "furniture_ai": 150,
    "render_quick": 25, "render_final": 45, "web_quick": 120, "web_final": 360,
}

mimetypes.add_type("model/gltf-binary", ".glb")
mimetypes.add_type("model/gltf+json", ".gltf")
mimetypes.add_type("image/webp", ".webp")
mimetypes.add_type("text/javascript", ".js")
mimetypes.add_type("application/wasm", ".wasm")


def log(msg):
    print(f"[studio] {msg}", flush=True)


# ===================================================================== small file helpers
_settings_lock = threading.Lock()


def read_json(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def write_json(path, data, private=False):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = f"{path}.{uuid.uuid4().hex[:6]}.tmp"
    if private:
        fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=1, ensure_ascii=False)
    else:
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=1, ensure_ascii=False)
    os.replace(tmp, path)
    if private and not WINDOWS:
        os.chmod(path, 0o600)


def settings():
    with _settings_lock:
        return read_json(SETTINGS_FILE, {})


def update_settings(**changes):
    with _settings_lock:
        data = read_json(SETTINGS_FILE, {})
        data.update(changes)
        write_json(SETTINGS_FILE, data)
        return data


def inside(base, path):
    base, path = os.path.realpath(base), os.path.realpath(path)
    return path == base or path.startswith(base + os.sep)


def safe_filename(name, default="file"):
    stem, ext = os.path.splitext(os.path.basename(name or ""))
    stem = re.sub(r"[^A-Za-z0-9._-]+", "_", stem).strip("._-")[:60] or default
    return stem + re.sub(r"[^a-z0-9.]", "", ext.lower())[:6]


def safe_project_name(name):
    name = re.sub(r'[\\/:*?"<>|\x00-\x1f]+', " ", name or "").strip(" .")
    return re.sub(r"\s+", " ", name)[:60]


# ===================================================================== finding Blender
def parse_version(text):
    m = re.search(r"Blender\s+(\d+)\.(\d+)(?:\.(\d+))?", text or "")
    return tuple(int(x or 0) for x in m.groups()) if m else None


def blender_candidates():
    seen, out = set(), []

    def add(path, where):
        if path and path not in seen:
            seen.add(path)
            out.append((path, where))

    if os.environ.get("ROOMKIT_BLENDER_ONLY"):                      # studio.py --blender PATH: use exactly that one
        p = os.environ["ROOMKIT_BLENDER_ONLY"]
        return [(p, "--blender option")] if os.path.isfile(p) else []
    add(settings().get("blender", ""), "chosen in Studio")
    add(os.environ.get("BLENDER", ""), "BLENDER setting")
    add(shutil.which("blender") or "", "your PATH")
    home = os.path.expanduser("~")
    if MAC:
        for app in ["/Applications/Blender.app", os.path.join(home, "Applications", "Blender.app")] + \
                sorted(glob.glob("/Applications/Blender*.app"), reverse=True):
            add(os.path.join(app, "Contents", "MacOS", "Blender"), "Applications")
        add(os.path.join(home, "Library", "Application Support", "Steam", "steamapps", "common", "Blender",
                         "Blender.app", "Contents", "MacOS", "Blender"), "Steam")
        add("/opt/homebrew/bin/blender", "Homebrew")
        add("/usr/local/bin/blender", "Homebrew")
    elif WINDOWS:
        roots = [os.environ.get(k, "") for k in ("ProgramFiles", "ProgramFiles(x86)", "ProgramW6432")]
        roots += [os.path.join(os.environ.get("LOCALAPPDATA", ""), "Programs")]
        for root in filter(None, roots):
            for exe in sorted(glob.glob(os.path.join(root, "Blender Foundation", "Blender*", "blender.exe")), reverse=True):
                add(exe, "Program Files")
            add(os.path.join(root, "Steam", "steamapps", "common", "Blender", "blender.exe"), "Steam")
        for drive in ("C:", "D:", "E:"):
            add(os.path.join(drive + os.sep, "SteamLibrary", "steamapps", "common", "Blender", "blender.exe"), "Steam")
    else:
        for p in ["/usr/bin/blender", "/usr/local/bin/blender", "/snap/bin/blender",
                  os.path.join(home, ".steam", "steam", "steamapps", "common", "Blender", "blender"),
                  os.path.join(home, ".local", "share", "Steam", "steamapps", "common", "Blender", "blender")]:
            add(p, "system")
        for p in sorted(glob.glob(os.path.join(home, "blender*", "blender")) + glob.glob("/opt/blender*/blender") +
                        glob.glob(os.path.join(home, "Applications", "blender*", "blender")), reverse=True):
            add(p, "home folder")
    return [(p, w) for p, w in out if os.path.isfile(p)]


def blender_version(path):
    try:
        r = subprocess.run([path, "--version"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                           errors="replace", timeout=90, **no_window())
        return parse_version(r.stdout)
    except (OSError, subprocess.SubprocessError):
        return None


class BlenderInfo:
    """Finds Blender in the background so the page opens instantly."""

    def __init__(self):
        self.lock = threading.Lock()
        self.state, self.path, self.version, self.where, self.too_old = "checking", "", None, "", []
        self.features = {}

    def detect(self):
        with self.lock:
            self.state = "checking"
        found, too_old = None, []
        for path, where in blender_candidates():
            v = blender_version(path)
            if not v:
                continue
            if v[:2] >= MIN_BLENDER:
                found = (path, v, where)
                break
            too_old.append({"path": path, "version": ".".join(map(str, v))})
        with self.lock:
            self.too_old = too_old
            if found:
                self.path, self.version, self.where = found
                self.state = "ok"
            else:
                self.path, self.version, self.state = "", None, ("too_old" if too_old else "missing")
        if found:
            log(f"Blender {'.'.join(map(str, found[1]))} found ({found[2]}): {found[0]}")
            self.features = detect_features(found[0])
        else:
            log("Blender 4.2+ not found - the page will show how to install it")
        return self.status()

    def status(self):
        with self.lock:
            return {"state": self.state, "path": self.path, "where": self.where,
                    "version": ".".join(map(str, self.version)) if self.version else "",
                    "too_old": self.too_old, "min": ".".join(map(str, MIN_BLENDER)),
                    "download": BLENDER_DOWNLOAD, "lts": BLENDER_LTS}


def no_window():
    return {"creationflags": 0x08000000} if WINDOWS else {}          # CREATE_NO_WINDOW: no console pop-ups


def tool_help(cmd):
    try:
        r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, errors="replace",
                           timeout=120, cwd=KIT, **no_window())
        return r.stdout
    except (OSError, subprocess.SubprocessError):
        return ""


def detect_features(blender):
    """Ask each kit tool what it can do (the tools are updated separately from Studio)."""
    feats = {"photo_to_3d": False, "providers": [], "furniture_scale": False, "furniture_ai": False,
             "list_slots": False, "exports": False}
    p3d = os.path.join(TOOLS, "photo_to_3d.py")
    if os.path.isfile(p3d):
        text = tool_help([sys.executable, p3d, "--help"])
        feats["photo_to_3d"] = "--photo" in text
        feats["providers"] = [p for p in ("auto", "meshy", "fal", "hf", "sample") if p in text] or ["auto"]
    text = tool_help([blender, "-b", "--factory-startup", "-P", os.path.join(TOOLS, "add_furniture.py"), "--", "--help"])
    feats["furniture_scale"] = "--scale" in text
    feats["furniture_ai"] = "--ai" in text
    feats["list_slots"] = "--list-slots" in text
    text = tool_help([blender, "-b", "--factory-startup", "-P", os.path.join(TOOLS, "build_portfolio.py"), "--", "--help"])
    feats["exports"] = "--exports" in text
    log(f"kit tools: {json.dumps(feats)}")
    return feats


BLENDER = BlenderInfo()


# ===================================================================== room catalogue
class Rooms:
    def __init__(self):
        self.lock = threading.Lock()
        self.scanning = False
        self.scanned = False                                          # one full Blender scan per session is enough
        self.last_error = ""

    def stale(self):
        if not os.path.isfile(ROOMS_JSON):
            return True
        t = os.path.getmtime(ROOMS_JSON)
        watch = glob.glob(os.path.join(KIT, "templates", "*.py")) + glob.glob(os.path.join(KIT, "templates", "output", "*")) \
            + glob.glob(os.path.join(KIT, "previews", "*.png"))
        data = read_json(ROOMS_JSON, {})
        known = {r.get("id") for r in data.get("rooms", [])}
        ids = {os.path.splitext(os.path.basename(p))[0] for p in glob.glob(os.path.join(KIT, "templates", "*.py"))}
        return ids != known or any(os.path.getmtime(p) > t for p in watch) or \
            (not self.scanned and any(r.get("source") != "blend" for r in data.get("rooms", [])))

    def refresh(self, force=False):
        with self.lock:
            if self.scanning:
                return
            self.scanning = True
        threading.Thread(target=self._scan, args=(force,), daemon=True).start()

    def _scan(self, force):
        try:
            script = os.path.join(TOOLS, "make_manifest.py")
            subprocess.run([sys.executable, script, "--quick"], cwd=KIT, stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT, timeout=120, **no_window())
            while BLENDER.state == "checking":
                time.sleep(0.5)
            if BLENDER.path:
                cmd = [sys.executable, script, "--blender", BLENDER.path, "--build-missing"] + (["--force"] if force else [])
                r = subprocess.run(cmd, cwd=KIT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                                   errors="replace", timeout=1800, **no_window())
                for line in r.stdout.splitlines()[-30:]:
                    if line.startswith("[manifest]"):
                        log(line)
        except Exception as err:                                      # never take the server down
            self.last_error = str(err)
            log(f"room scan problem: {err}")
        finally:
            self.scanned = bool(BLENDER.path)
            self.scanning = False

    def get(self):
        data = read_json(ROOMS_JSON, {"rooms": []})
        data["scanning"] = self.scanning
        return data

    def find(self, room_id):
        return next((r for r in self.get().get("rooms", []) if r["id"] == room_id), None)


ROOMS = Rooms()


# ===================================================================== keys (never stored in a project)
def load_keys():
    return read_json(KEYS_FILE, {})


def save_key(provider, key):
    if provider not in KEY_NAMES:
        raise UserError("Unknown service.")
    keys = load_keys()
    if key:
        keys[KEY_NAMES[provider]] = key.strip()
    else:
        keys.pop(KEY_NAMES[provider], None)
    os.makedirs(HOME, exist_ok=True)
    if not WINDOWS:
        os.chmod(HOME, 0o700)
    write_json(KEYS_FILE, keys, private=True)


def keys_status():
    keys = load_keys()
    out = {}
    for provider, env in KEY_NAMES.items():
        value = keys.get(env) or os.environ.get(env, "")
        out[provider] = {"set": bool(value), "hint": ("…" + value[-4:]) if len(value) > 8 else ("set" if value else ""),
                         "from": "keys.json" if keys.get(env) else ("environment" if value else "")}
    return out


def key_env():
    env = dict(os.environ)
    for name, value in load_keys().items():
        if name.isupper() and isinstance(value, str) and value and not env.get(name):
            env[name] = value
    env["ROOMKIT_KEYS_FILE"] = KEYS_FILE
    env["PYTHONUNBUFFERED"] = "1"
    return env


# ===================================================================== projects
class UserError(Exception):
    """An error with a message that is fine to show as it is."""

    def __init__(self, message, status=400):
        super().__init__(message)
        self.status = status


class Workspace:
    def __init__(self, root):
        self.root = os.path.abspath(os.path.expanduser(root))
        self.lock = threading.Lock()

    def ensure(self):
        os.makedirs(self.root, exist_ok=True)

    def path(self, pid):
        name = safe_project_name(pid)
        if not name or name != pid:
            raise UserError("That project name isn't valid.", 404)
        p = os.path.join(self.root, name)
        if not os.path.isfile(os.path.join(p, "studio.json")):
            raise UserError("That project doesn't exist (it may have been moved or renamed).", 404)
        return p

    def list(self):
        self.ensure()
        items = []
        for name in os.listdir(self.root):
            p = os.path.join(self.root, name)
            state = os.path.join(p, "studio.json")
            if os.path.isfile(state):
                st = read_json(state, {})
                prof = read_json(os.path.join(p, "profile.json"), {})
                hero = os.path.join(p, "output", "hero.png")
                items.append({"id": name, "name": name, "updated": os.path.getmtime(state),
                              "room": st.get("room") or prof.get("room", ""), "person": prof.get("name", ""),
                              "hero": f"/p/{urllib.parse.quote(name)}/output/hero.png?v={int(os.path.getmtime(hero))}"
                              if os.path.isfile(hero) else ""})
        return sorted(items, key=lambda i: -i["updated"])

    def create(self, name):
        self.ensure()
        name = safe_project_name(name) or "My portfolio"
        base, n = name, 2
        while os.path.exists(os.path.join(self.root, name)):
            name, n = f"{base} {n}", n + 1
        p = os.path.join(self.root, name)
        for sub in ("images", "furniture", "output"):
            os.makedirs(os.path.join(p, sub), exist_ok=True)
        write_json(os.path.join(p, "profile.json"), {"name": "", "role": "", "tagline": "", "room": "", "theme": "",
                                                     "brand_color": "", "links": {}, "skills": [], "projects": []})
        write_json(os.path.join(p, "studio.json"), {"created": time.time(), "step": "persona", "persona": "",
                                                    "room": "", "theme": "", "seed": 1, "swaps": [],
                                                    "build": {"quality": "quick", "web": True, "exports": ["hero"]}})
        with open(os.path.join(p, "README.txt"), "w", encoding="utf-8") as f:
            f.write("This folder is a RoomKit Studio project.\n\n"
                    "profile.json  your details (Studio writes this; you can also edit it by hand)\n"
                    "images/       your project pictures\nfurniture/    photos and 3D models of your own furniture\n"
                    "output/       your finished portfolio website and pictures (upload this folder)\n")
        return name

    def load(self, pid):
        p = self.path(pid)
        outputs = list_outputs(p)
        return {"id": pid, "name": pid, "folder": p, "profile": read_json(os.path.join(p, "profile.json"), {}),
                "studio": read_json(os.path.join(p, "studio.json"), {}), "outputs": outputs}

    def save(self, pid, profile, studio):
        p = self.path(pid)
        with self.lock:
            if profile is not None:
                old = read_json(os.path.join(p, "profile.json"), {})
                old.update(clean_profile(profile, p))
                write_json(os.path.join(p, "profile.json"), old)
            if studio is not None:
                old = read_json(os.path.join(p, "studio.json"), {})
                for k in ("step", "persona", "room", "theme", "seed", "swaps", "build", "touched", "link_order", "brand_on"):
                    if k in studio:
                        old[k] = studio[k]
                old["saved"] = time.time()
                write_json(os.path.join(p, "studio.json"), old)
        return True


def clean_profile(prof, folder):
    def s(v, n=200):
        return str(v or "").strip()[:n]

    links = {}
    for k, v in (prof.get("links") or {}).items():
        k = re.sub(r"[^a-z0-9_]", "", str(k).lower())[:24]
        if k and s(v):
            links[k] = s(v, 500)
    projects = []
    for pr in (prof.get("projects") or [])[:24]:
        img = s(pr.get("image"), 300).replace("\\", "/")
        if img and (img.startswith("/") or ".." in img.split("/") or not os.path.isfile(os.path.join(folder, img))):
            img = ""
        projects.append({"title": s(pr.get("title"), 80), "image": img, "url": s(pr.get("url"), 500),
                         "description": s(pr.get("description"), 400)})
    color = s(prof.get("brand_color"), 7)
    return {"name": s(prof.get("name"), 60), "role": s(prof.get("role"), 80), "tagline": s(prof.get("tagline"), 160),
            "room": s(prof.get("room"), 60), "theme": s(prof.get("theme"), 60),
            "brand_color": color if re.fullmatch(r"#[0-9A-Fa-f]{6}", color) else "",
            "links": links, "skills": [s(x, 40) for x in (prof.get("skills") or []) if s(x)][:12],
            "projects": projects}


def list_outputs(folder):
    out = os.path.join(folder, "output")
    files = {}
    if os.path.isdir(out):
        for name in ALL_EXPORTS + ["index", "room3d"]:
            for ext in (".png", ".html"):
                f = os.path.join(out, name + ext)
                if os.path.isfile(f):
                    files[name] = {"file": name + ext, "size": os.path.getsize(f), "mtime": int(os.path.getmtime(f))}
    return files


def sniff(data):
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return ".png"
    if data[:3] == b"\xff\xd8\xff":
        return ".jpg"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return ".webp"
    if data[4:12] in (b"ftypheic", b"ftypheix", b"ftypmif1", b"ftyphevc", b"ftypheim", b"ftypheis", b"ftypavif"):
        return ".heic"
    if data[:6] in (b"GIF87a", b"GIF89a"):
        return ".gif"
    if data[:2] == b"BM":
        return ".bmp"
    if data[:4] in (b"II*\x00", b"MM\x00*"):
        return ".tif"
    if data[:4] == b"glTF":
        return ".glb"
    return ""


def store_upload(folder, kind, filename, data):
    """Save a dropped file into the project. Returns its path relative to the project folder."""
    if not data:
        raise UserError("That file is empty.")
    ext = os.path.splitext(filename or "")[1].lower()
    found = sniff(data[:32])
    sub = "images" if kind == "images" else "furniture"
    if kind == "images" or (kind == "furniture" and ext not in MODEL_TYPES):
        if len(data) > 40 * 1024 * 1024:
            raise UserError("That picture is bigger than 40 MB. Please use a smaller one.")
        if found in (".heic", ".gif") or (not found and ext in (".heic", ".heif", ".gif")):
            return convert_image(folder, sub, filename, data)
        if found not in IMAGE_TYPES:
            raise UserError("That file isn't a picture we can read. Please use JPG, PNG or WebP"
                            + (", or a 3D model (.glb, .obj, .fbx, .stl)." if kind == "furniture" else "."))
        ext = ".jpg" if found == ".jpg" else found
    else:
        if len(data) > 300 * 1024 * 1024:
            raise UserError("That 3D model is bigger than 300 MB. Try exporting it with fewer polygons.")
        if ext == ".gltf":
            raise UserError("A .gltf file usually needs extra files next to it. Please export it as a single .glb file.")
    digest = hashlib.sha256(data).hexdigest()[:8]
    name = safe_filename(os.path.splitext(filename or "")[0] + ext, default="picture" if sub == "images" else "model")
    stem, e2 = os.path.splitext(name)
    dest_dir = os.path.join(folder, sub)
    os.makedirs(dest_dir, exist_ok=True)
    target = os.path.join(dest_dir, f"{stem}{e2}")
    if os.path.exists(target):
        with open(target, "rb") as f:
            if hashlib.sha256(f.read()).hexdigest()[:8] == digest:
                return f"{sub}/{stem}{e2}"
        target = os.path.join(dest_dir, f"{stem}-{digest}{e2}")
    with open(target, "wb") as f:
        f.write(data)
    return f"{sub}/{os.path.basename(target)}"


def convert_image(folder, sub, filename, data):
    """iPhone HEIC photos and GIFs: convert to JPG/PNG with the tools the computer already has."""
    tmp_dir = os.path.join(folder, ".studio", "tmp")
    os.makedirs(tmp_dir, exist_ok=True)
    src = os.path.join(tmp_dir, "upload" + (sniff(data[:32]) or ".heic"))
    with open(src, "wb") as f:
        f.write(data)
    stem = os.path.splitext(safe_filename(filename, "photo"))[0]
    dst = os.path.join(folder, sub, f"{stem}-{hashlib.sha256(data).hexdigest()[:8]}.jpg")
    ok = False
    if MAC and shutil.which("sips"):
        r = subprocess.run(["sips", "-s", "format", "jpeg", src, "--out", dst], stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
        ok = r.returncode == 0 and os.path.isfile(dst)
    elif BLENDER.path and not src.endswith(".heic"):
        code = ("import bpy,sys;i=bpy.data.images.load(sys.argv[-2]);i.filepath_raw=sys.argv[-1];"
                "i.file_format='JPEG';i.save()")
        subprocess.run([BLENDER.path, "-b", "--factory-startup", "--python-expr", code, "--", src, dst],
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120, **no_window())
        ok = os.path.isfile(dst)
    try:
        os.remove(src)
    except OSError:
        pass
    if not ok:
        raise UserError("We couldn't convert that photo. On an iPhone, go to Settings → Camera → Formats → "
                        "Most Compatible, or export the photo as JPG first.")
    return f"{sub}/{os.path.basename(dst)}"


# ===================================================================== jobs (builds run here)
class Cancelled(Exception):
    pass


class StepFailed(Exception):
    def __init__(self, title, message, hint=""):
        super().__init__(message)
        self.title, self.message, self.hint = title, message, hint


FRIENDLY = [   # (pattern in the log, title, message, hint) - shown instead of a traceback
    (r"No slot '([^']+)'", "That furniture spot isn't in this room",
     "This room has no spot called “{0}”.", "Go to Make it yours and choose the spot again."),
    (r"no template '([^']+)'", "Room not found", "We couldn't find the room “{0}” in your kit.",
     "Pick a room in the Room step."),
    (r"profile not found", "Profile missing", "Your profile file is missing.", "Go back to the Profile step and save it again."),
    (r"No space left on device", "Your disk is full", "There isn't enough free space to save the pictures.",
     "Free up a few GB and try again."),
    (r"Permission denied|Operation not permitted", "Folder is locked",
     "RoomKit wasn't allowed to write to your project folder.",
     "Make sure the folder isn't read-only, then try again."),
    (r"MemoryError|[Oo]ut of memory|GPU memory|CUDA error", "Your computer ran out of memory",
     "Blender needed more memory than was free.", "Close other apps, or choose Quick preview."),
    (r"Failed to import|import failed|Unsupported (file|format)|Cannot import|not a valid glTF",
     "That 3D model couldn't be loaded", "Blender couldn't read one of your 3D models.",
     "Export it again as a .glb file, or use a photo instead."),
    (r"Cannot read file|not a blend file|Unable to open", "A file couldn't be opened",
     "Blender couldn't open a file it needed.", "Try building again. If it keeps happening, rebuild with Final quality off."),
    (r"Couldn't load image|Error: Cannot load image|Unsupported image", "A picture couldn't be read",
     "One of your pictures couldn't be read.", "Use JPG or PNG pictures."),
]


def explain_failure(lines, step_label, code):
    text = "\n".join(lines[-400:])
    for pattern, title, message, hint in FRIENDLY:
        m = re.search(pattern, text)
        if m:
            return StepFailed(title, message.format(*m.groups()), hint)
    if code is not None and (code < 0 or code in (134, 137, 139, 3221225477)):
        return StepFailed("Blender closed unexpectedly", f"Blender stopped while {step_label.lower()}.",
                          "This usually means it ran out of memory. Close other apps or choose Quick preview, then try again.")
    m = re.findall(r"\[RoomKit\][^\n]*(?:WARNING|error|Error)[^\n]*", text)
    detail = f" ({m[-1].split(']', 1)[1].strip()})" if m else ""
    return StepFailed("The build stopped", f"Something went wrong while {step_label.lower()}{detail}.",
                      "Try again. If it keeps happening, open Details and share the log with support.")


class Job:
    def __init__(self, kind, project):
        self.id = uuid.uuid4().hex[:10]
        self.kind, self.project = kind, project
        self.state, self.started, self.finished = "running", time.time(), None
        self.steps, self.current = [], -1
        self.lines, self.warnings = [], []
        self.detail, self.error, self.result = "", None, None
        self.proc, self.cancelled = None, False
        self.sub = 0.0
        self.step_started = time.time()
        self.lock = threading.Lock()

    def add_step(self, sid, label, est):
        self.steps.append({"id": sid, "label": label, "status": "pending", "est": float(est), "took": None})

    def start_step(self, sid, detail=""):
        with self.lock:
            if 0 <= self.current < len(self.steps) and self.steps[self.current]["status"] == "running":
                self.steps[self.current]["status"] = "done"
                self.steps[self.current]["took"] = round(time.time() - self.step_started, 1)
            self.current = next(i for i, s in enumerate(self.steps) if s["id"] == sid)
            self.steps[self.current]["status"] = "running"
            self.step_started, self.sub, self.detail = time.time(), 0.0, detail

    def finish_step(self):
        with self.lock:
            if 0 <= self.current < len(self.steps):
                st = self.steps[self.current]
                st["status"], st["took"] = "done", round(time.time() - self.step_started, 1)
                return st
        return None

    def line(self, text):
        text = text.rstrip("\n")
        with self.lock:
            self.lines.append(text)
            if len(self.lines) > 30000:
                del self.lines[:5000]

    def progress(self):
        total = sum(s["est"] for s in self.steps) or 1
        done = sum(s["est"] for s in self.steps if s["status"] in ("done", "skipped"))
        remaining = sum(s["est"] for s in self.steps if s["status"] == "pending")
        if 0 <= self.current < len(self.steps) and self.steps[self.current]["status"] == "running":
            st = self.steps[self.current]
            elapsed = time.time() - self.step_started
            frac = max(self.sub, min(0.95, elapsed / max(st["est"], 1)))
            done += st["est"] * frac
            remaining += max(st["est"] * (1 - frac), st["est"] - elapsed, 0)
        if self.state != "running":
            return (1.0 if self.state == "done" else done / total), 0
        return min(done / total, 0.99), int(remaining)

    def snapshot(self, since=0):
        frac, eta = self.progress()
        with self.lock:
            since = max(0, min(int(since), len(self.lines)))
            return {"id": self.id, "kind": self.kind, "project": self.project, "state": self.state,
                    "steps": self.steps, "current": self.current, "progress": round(frac, 4), "eta": eta,
                    "elapsed": int((self.finished or time.time()) - self.started), "detail": self.detail,
                    "lines": self.lines[since:since + 4000], "next": min(len(self.lines), since + 4000),
                    "warnings": self.warnings, "error": self.error, "result": self.result}

    def cancel(self):
        self.cancelled = True
        kill_tree(self.proc)


def kill_tree(proc):
    if not proc or proc.poll() is not None:
        return
    try:
        if WINDOWS:
            subprocess.run(["taskkill", "/PID", str(proc.pid), "/T", "/F"], stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, **no_window())
        else:
            os.killpg(proc.pid, signal.SIGTERM)
            for _ in range(30):
                if proc.poll() is not None:
                    return
                time.sleep(0.1)
            os.killpg(proc.pid, signal.SIGKILL)
    except (OSError, ProcessLookupError):
        try:
            proc.kill()
        except OSError:
            pass


def run_proc(job, cmd, env=None, on_line=None):
    """Run one Blender / Python step, streaming its output into the job log."""
    if job.cancelled:
        raise Cancelled()
    job.line("$ " + " ".join(f'"{c}"' if " " in c else c for c in cmd))
    kw = dict(stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL, text=True,
              encoding="utf-8", errors="replace", bufsize=1, cwd=KIT, env=env or key_env())
    if WINDOWS:
        kw["creationflags"] = 0x00000200 | 0x08000000                 # new process group, no console window
    else:
        kw["start_new_session"] = True                                # so Cancel can stop Blender and its children
    try:
        proc = subprocess.Popen(cmd, **kw)
    except OSError as err:
        raise StepFailed("Couldn't start Blender", f"Blender couldn't be started ({err.strerror or err}).",
                         "Open Settings and check the Blender location.")
    job.proc = proc
    for raw in proc.stdout:
        job.line(raw)
        if on_line:
            try:
                on_line(raw.rstrip("\n"))
            except Exception:                                          # progress parsing must never break a build
                pass
    code = proc.wait()
    job.proc = None
    if job.cancelled:
        raise Cancelled()
    return code


class Builder:
    """One build at a time: Blender is heavy, and two at once would only make both slow."""

    def __init__(self, workspace):
        self.ws = workspace
        self.jobs = {}
        self.current = None
        self.lock = threading.Lock()

    def start(self, pid, options):
        with self.lock:
            if self.current and self.current.state == "running":
                raise UserError("A build is already running. Wait for it to finish or cancel it.", 409)
            if BLENDER.state != "ok":
                raise UserError("RoomKit needs Blender 4.2 or newer to build. Open Settings to set it up.", 409)
            job = Job("build", pid)
            self.jobs[job.id] = job
            self.current = job
        threading.Thread(target=self._run, args=(job, options), daemon=True).start()
        return job

    def _run(self, job, options):
        t0 = time.time()
        try:
            self.build(job, options)
            job.state = "done"
        except Cancelled:
            job.state, job.detail = "cancelled", "Cancelled. Your previous results are still there."
        except StepFailed as err:
            job.state = "error"
            job.error = {"title": err.title, "message": err.message, "hint": err.hint}
        except UserError as err:
            job.state = "error"
            job.error = {"title": "Can't build yet", "message": str(err), "hint": ""}
        except Exception:                                              # unexpected: plain words up front, details in the log
            job.line(traceback.format_exc())
            job.state = "error"
            job.error = {"title": "The build stopped", "message": "Something unexpected went wrong inside Studio.",
                         "hint": "Try again. If it keeps happening, open Details and share the log with support."}
        finally:
            job.finished = time.time()
            for st in job.steps:
                if st["status"] == "running":
                    st["status"] = "done" if job.state == "done" else ("cancelled" if job.state == "cancelled" else "failed")
            job.line(f"[studio] finished: {job.state} after {job.finished - t0:.0f}s")
            try:
                folder = self.ws.path(job.project)
                with open(os.path.join(folder, ".studio", "last_build.log"), "w", encoding="utf-8") as f:
                    f.write("\n".join(job.lines))
            except Exception:
                pass

    # ------------------------------------------------------------------ the build itself
    def build(self, job, options):
        folder = self.ws.path(job.project)
        studio = read_json(os.path.join(folder, "studio.json"), {})
        profile = read_json(os.path.join(folder, "profile.json"), {})
        room_id = studio.get("room") or profile.get("room") or ""
        template = os.path.join(KIT, "templates", f"{room_id}.py")
        if not room_id or not os.path.isfile(template):
            raise UserError("Pick a room first (step 4).")
        room = ROOMS.find(room_id) or {}
        theme = studio.get("theme") or profile.get("theme") or room.get("default_theme", "")
        seed = int(studio.get("seed") or 1)
        quick = options.get("quality", "quick") != "final"
        web = bool(options.get("web"))
        feats = BLENDER.features
        exports = [e for e in options.get("exports") or [] if e in ALL_EXPORTS]
        if "hero" not in exports:
            exports.insert(0, "hero")
        if not feats.get("exports"):
            exports = ["hero"] if quick else CLASSIC_EXPORTS
        elif quick:
            exports = ["hero"]
        swaps = [s for s in studio.get("swaps") or [] if s.get("file") and s.get("slot")]
        known = {s.get("name") for s in room.get("slots") or [] if s.get("name")}
        if known:                                                      # e.g. a swap left over from another room
            for sw in [s for s in swaps if s["slot"] not in known]:
                job.warnings.append(f"This room has no spot for your {sw['slot'].replace('_', ' ')}, so it was left out.")
            swaps = [s for s in swaps if s["slot"] in known]
        timings = settings().get("timings", {})

        def est(key, n=1):
            return timings.get(key, DEFAULT_TIMES[key]) * n

        job.add_step("room", "Preparing your room", est("room"))
        for i, sw in enumerate(swaps):
            label = sw.get("label") or sw["slot"].replace("_", " ")
            kind = "furniture_model" if sw.get("kind") == "model" else (
                "furniture_ai" if sw.get("method") == "ai" else "furniture_photo")
            job.add_step(f"swap{i}", f"Adding your {label.lower()}", est(kind) + (est("furniture_model") if kind == "furniture_ai" else 0))
        render_key = "render_quick" if quick else "render_final"
        job.add_step("render", "Adding your details and taking the pictures", est(render_key, len(exports)))
        if web:
            job.add_step("web", "Making your 3D website", est("web_quick" if quick else "web_final"))
        job.add_step("finish", "Finishing up", 2)

        blender = BLENDER.path
        private = os.path.join(folder, ".studio")
        work = os.path.join(private, "work")
        staging = os.path.join(private, "staging")
        for d in (work, staging):
            shutil.rmtree(d, ignore_errors=True)
            os.makedirs(d, exist_ok=True)

        # 1. the room itself, built from a private copy of the template (never touches templates/output)
        job.start_step("room", f"{room.get('name', room_id)}, {theme.replace('_', ' ')} theme")
        st = os.stat(template)
        key = hashlib.sha256(f"{room_id}|{theme}|{seed}|{st.st_mtime}|{st.st_size}".encode()).hexdigest()[:10]
        base = os.path.join(private, "cache", f"{room_id}__{theme or 'default'}__{seed}__{key}.blend")
        if os.path.isfile(base):
            job.line(f"[studio] using the room built earlier: {base}")
            job.steps[job.current]["est"] = 1
        else:
            tpl_dir = os.path.join(work, "template")
            os.makedirs(tpl_dir, exist_ok=True)
            copy = os.path.join(tpl_dir, os.path.basename(template))
            shutil.copyfile(template, copy)
            env = key_env()
            env.update(ROOMKIT_BUILD_ONLY="1", ROOMKIT_SEED=str(seed))
            if theme:
                env["ROOMKIT_THEME"] = theme
            code = run_proc(job, [blender, "-b", "--factory-startup", "-P", copy], env=env)
            built = os.path.join(tpl_dir, "output", f"{room_id}.blend")
            if code != 0 or not os.path.isfile(built):
                raise explain_failure(job.lines, "preparing your room", code)
            os.makedirs(os.path.dirname(base), exist_ok=True)
            for old in glob.glob(os.path.join(private, "cache", f"{room_id}__*.blend")):
                if os.path.getmtime(old) < time.time() - 14 * 86400:
                    os.remove(old)                                     # keep the cache small
            shutil.move(built, base)
            self.learn("room", job.finish_step())
        current = base

        # 2. furniture swaps, one after the other
        for i, sw in enumerate(swaps):
            current = self.swap(job, folder, work, current, i, sw, feats, blender)

        # 3. profile -> hooks -> renders (-> 3D website)
        job.start_step("render", "Putting your name, links and projects into the room")
        renders_needed = len(exports)
        rendered = []

        def on_render_line(line):
            if "[RoomKit] rendered" in line:
                rendered.append(os.path.basename(line.split("rendered", 1)[1].strip()))
                job.sub = len(rendered) / max(renders_needed, 1)
                job.detail = f"Took picture {len(rendered)} of {renders_needed}"
            elif "portfolio ready" in line:
                st_done = job.finish_step()
                self.learn(render_key, st_done, per=renders_needed)
                if web:
                    job.start_step("web", "Getting the room ready for the web")
            elif line.startswith("[RoomKit web]"):
                msg = line.split("]", 1)[1].strip()
                for marker, frac, words in (("bake meshes", 0.08, "Preparing the 3D model"),
                                            ("lightmap UVs ready", 0.25, "Preparing the lighting"),
                                            ("baking lighting", 0.3, "Baking the lighting (the slow part)"),
                                            ("baked", 0.85, "Smoothing the lighting"),
                                            ("room.glb", 0.95, "Compressing the 3D files"),
                                            ("done in", 1.0, "3D website ready")):
                    if marker in msg:
                        job.sub, job.detail = frac, words
                if "baking on" in msg or "baking on CPU" in msg:
                    job.line("[studio] " + msg)
            elif "WARNING" in line and "[RoomKit]" in line:
                job.warnings.append(line.split("WARNING", 1)[1].strip(" :"))

        cmd = [blender, "-b", "--factory-startup", "-P", os.path.join(TOOLS, "build_portfolio.py"), "--",
               "--profile", os.path.join(folder, "profile.json"), "--blend", current, "--out", staging]
        if quick:
            cmd.append("--fast")
        if web:
            cmd.append("--web")
        if feats.get("exports") and not quick:
            cmd += ["--exports", ",".join(exports)]
        code = run_proc(job, cmd, on_line=on_render_line)
        if code != 0 or not os.path.isfile(os.path.join(staging, "index.html")):
            label = job.steps[job.current]["label"] if job.current >= 0 else "building"
            raise explain_failure(job.lines, label, code)
        if web:
            st_web = job.finish_step()
            if os.path.isfile(os.path.join(staging, "room3d.html")):
                self.learn("web_quick" if quick else "web_final", st_web)
            else:
                job.warnings.append("The 3D website couldn't be made this time; the 2D site and pictures are ready.")

        # 4. swap the new results in (the old ones stay until now, so a failed build loses nothing)
        job.start_step("finish", "Saving your website")
        out = os.path.join(folder, "output")
        previous = os.path.join(private, "previous_output")
        shutil.rmtree(previous, ignore_errors=True)
        if os.path.isdir(out):
            os.replace(out, previous)
        os.replace(staging, out)
        for z in glob.glob(os.path.join(private, "*.zip")):
            os.remove(z)
        job.finish_step()
        files = list_outputs(folder)
        result = {"when": time.time(), "quality": "quick" if quick else "final", "web": web and "room3d" in files,
                  "exports": exports, "files": files, "seconds": int(time.time() - job.started),
                  "room": room_id, "theme": theme, "warnings": job.warnings}
        job.result = result
        state = read_json(os.path.join(folder, "studio.json"), {})
        state["last_build"] = result
        write_json(os.path.join(folder, "studio.json"), state)
        job.detail = "Your portfolio is ready"

    def swap(self, job, folder, work, current, i, sw, feats, blender):
        job.start_step(f"swap{i}")
        path = os.path.join(folder, sw["file"])
        if not inside(folder, path) or not os.path.isfile(path):
            job.warnings.append(f"The file for your {sw['slot'].replace('_', ' ')} is missing, so the room's own piece was kept.")
            job.steps[job.current]["status"] = "skipped"
            return current
        model = path if sw.get("kind") == "model" else ""
        photo = "" if model else path
        if photo and sw.get("method") == "ai":
            model = self.ai_model(job, folder, photo, sw, feats)
            if model:
                photo = ""
            left = settings().get("timings", {}).get("furniture_model" if model else "furniture_photo",
                                                     DEFAULT_TIMES["furniture_model" if model else "furniture_photo"])
            job.steps[job.current]["est"] = (time.time() - job.step_started) + left     # the AI part is over
        nxt = os.path.join(work, f"step{i + 1}.blend")
        cmd = [blender, "-b", "--factory-startup", current, "-P", os.path.join(TOOLS, "add_furniture.py"), "--",
               "--slot", sw["slot"]]
        cmd += ["--model", model] if model else ["--photo", photo]
        turn = float(sw.get("turn") or 0)
        if turn:
            cmd += ["--turn", f"{turn:g}"]
        scale = float(sw.get("scale") or 1)
        if abs(scale - 1) > 0.01:
            if feats.get("furniture_scale"):
                cmd += ["--scale", f"{scale:g}"]
            else:
                job.warnings.append("Resizing furniture needs a newer kit; your piece was fitted to its spot instead.")
        if sw.get("colors") in ("match", "palette", "original"):
            cmd += ["--colors", sw["colors"]]
        cmd += ["--no-render", "--save", nxt]
        job.detail = "Placing it in the room"
        t0 = time.time()
        code = run_proc(job, cmd)
        if code != 0 or not os.path.isfile(nxt):
            raise explain_failure(job.lines, f"adding your {sw['slot'].replace('_', ' ')}", code)
        st = job.finish_step()
        self.learn("furniture_model" if model else "furniture_photo", dict(st or {}, took=time.time() - t0))
        return nxt

    def ai_model(self, job, folder, photo, sw, feats):
        """Photo -> AI 3D model with tools/photo_to_3d.py. Returns a .glb path, or "" to fall back to blocky."""
        slot_words = sw["slot"].replace("_", " ")
        if not feats.get("photo_to_3d"):
            job.warnings.append(f"AI 3D models arrive with the next kit update, so your {slot_words} was built as a quick blocky version.")
            return ""
        provider = sw.get("provider") or "auto"
        with open(photo, "rb") as f:
            digest = hashlib.sha256(f.read() + provider.encode()).hexdigest()[:12]
        out = os.path.join(folder, "furniture", "ai", f"{sw['slot']}-{digest}.glb")
        if os.path.isfile(out):
            job.line(f"[studio] reusing the AI model made earlier: {out}")
            return out
        os.makedirs(os.path.dirname(out), exist_ok=True)
        job.detail = "Sending your photo to the AI service"
        found = []

        def on_line(line):
            if line.startswith("GLB:"):
                found.append(line[4:].strip())
            elif line.startswith("[photo-to-3d]"):
                msg = line.split("]", 1)[1].strip()
                m = re.search(r"(\d{1,3})\s*%", msg)
                if m:
                    job.sub = min(int(m.group(1)), 100) / 100 * 0.8
                job.detail = msg[:120]

        t0 = time.time()
        code = run_proc(job, [sys.executable, os.path.join(TOOLS, "photo_to_3d.py"), "--photo", photo, "--out", out,
                              "--provider", provider, "--yes"], on_line=on_line)
        glb = found[-1] if found and os.path.isfile(found[-1]) else (out if os.path.isfile(out) else "")
        if code == 0 and glb:
            self.learn("furniture_ai", {"took": time.time() - t0})
            return glb
        why = {3: "no AI service is set up (add a Meshy or fal key in Settings)",
               4: "the AI service took too long"}.get(code, "the AI service didn't return a model")
        job.warnings.append(f"Your {slot_words} was built as a quick blocky version because {why}.")
        return ""

    def learn(self, key, step, per=1):
        """Remember how long steps take on this computer, so the time estimates get better."""
        if not step or not step.get("took") or key not in DEFAULT_TIMES:
            return
        took = float(step["took"]) / max(per, 1)
        t = settings().get("timings", {})
        old = t.get(key)
        t[key] = round(took if old is None else old * 0.6 + took * 0.4, 1)
        update_settings(timings=t)


# ===================================================================== zip + open folder
def make_zip(folder):
    out = os.path.join(folder, "output")
    if not os.path.isfile(os.path.join(out, "index.html")):
        raise UserError("Build your portfolio first.", 404)
    z = os.path.join(folder, ".studio", f"{os.path.basename(folder)} website.zip")
    if not os.path.isfile(z):
        os.makedirs(os.path.dirname(z), exist_ok=True)
        tmp = z + ".tmp"
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zf:
            for root, _, files in os.walk(out):
                for name in files:
                    if name.endswith((".blend", ".blend1")) or name.startswith("."):
                        continue
                    full = os.path.join(root, name)
                    zf.write(full, os.path.relpath(full, out))
        os.replace(tmp, z)
    return z


def reveal(path):
    if MAC:
        subprocess.Popen(["open", path])
    elif WINDOWS:
        os.startfile(path)                                             # noqa: S606 (opens Explorer)
    else:
        subprocess.Popen(["xdg-open", path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


# ===================================================================== HTTP server
class Server(http.server.ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = False


class Handler(http.server.BaseHTTPRequestHandler):
    server_version = "RoomKitStudio/1.0"
    protocol_version = "HTTP/1.1"
    app = None                                                         # set in main()

    def log_message(self, fmt, *args):
        if self.app.verbose:
            sys.stderr.write("[http] " + (fmt % args) + "\n")

    # ------------------------------------------------------------------ plumbing
    def send(self, status, body=b"", ctype="application/json; charset=utf-8", headers=None):
        if isinstance(body, (dict, list)):
            body = json.dumps(body).encode("utf-8")
        elif isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def fail(self, status, message):
        self.send(status, {"error": message})

    def body(self, limit=320 * 1024 * 1024):
        n = int(self.headers.get("Content-Length") or 0)
        if n > limit:
            raise UserError("That file is too big.", 413)
        data = b""
        while len(data) < n:
            chunk = self.rfile.read(min(1 << 20, n - len(data)))
            if not chunk:
                break
            data += chunk
        return data

    def json_body(self):
        try:
            return json.loads(self.body(8 * 1024 * 1024) or b"{}")
        except ValueError:
            raise UserError("The page sent something we couldn't read. Reload the page and try again.")

    def host_ok(self):
        host = (self.headers.get("Host") or "").lower()
        return host in self.app.hosts

    def token_ok(self, query):
        token = self.headers.get("X-RoomKit-Token") or (query.get("token") or [""])[0]
        return secrets.compare_digest(token, self.app.token)

    def file(self, path, cache=False):
        if not os.path.isfile(path):
            return self.fail(404, "Not found")
        ctype = mimetypes.guess_type(path)[0] or "application/octet-stream"
        if ctype.startswith("text/") or ctype in ("application/json", "text/javascript"):
            ctype += "; charset=utf-8"
        size = os.path.getsize(path)
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(size))
        self.send_header("Cache-Control", "max-age=3600" if cache else "no-cache")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        if self.command == "HEAD":
            return
        with open(path, "rb") as f:
            shutil.copyfileobj(f, self.wfile, 1 << 20)

    def do_GET(self):
        self.route("GET")

    def do_HEAD(self):
        self.route("GET")

    def do_POST(self):
        self.route("POST")

    def do_PUT(self):
        self.route("PUT")

    def do_DELETE(self):
        self.route("DELETE")

    def route(self, method):
        if not self.host_ok():
            return self.fail(403, "RoomKit Studio only answers on this computer.")
        url = urllib.parse.urlsplit(self.path)
        path = urllib.parse.unquote(url.path)
        query = urllib.parse.parse_qs(url.query)
        try:
            if path.startswith("/api/"):
                if not self.token_ok(query):
                    return self.fail(403, "Please reload RoomKit Studio.")
                return self.api(method, path[5:], query)
            if method != "GET":
                return self.fail(405, "Not allowed")
            return self.static(path)
        except UserError as err:
            return self.fail(err.status, str(err))
        except (BrokenPipeError, ConnectionResetError):
            return None
        except Exception:
            traceback.print_exc()
            return self.fail(500, "Something went wrong inside Studio. Try again.")

    # ------------------------------------------------------------------ files
    def static(self, path):
        if path in ("/", "/index.html"):
            with open(os.path.join(UI, "index.html"), encoding="utf-8") as f:
                page = f.read().replace("__ROOMKIT_TOKEN__", self.app.token)
            return self.send(200, page, "text/html; charset=utf-8",
                             {"Content-Security-Policy": "default-src 'self'; img-src 'self' data: blob:; "
                              "style-src 'self' 'unsafe-inline'; script-src 'self'; connect-src 'self'; "
                              "frame-src 'self'; frame-ancestors 'none'"})
        if path.startswith("/kit/"):                                   # room previews + sample files (read only)
            rel = path[5:]
            allowed = ("previews/", "templates/output/", "samples/", "tools/studio/thumbs/")
            full = os.path.join(KIT, *rel.split("/"))
            if not rel.startswith(allowed) or not inside(KIT, full) or rel.endswith((".blend", ".py")):
                return self.fail(404, "Not found")
            return self.file(full, cache=True)
        if path.startswith("/p/"):                                     # a project's files (pictures, the built site)
            parts = path[3:].split("/", 1)
            if len(parts) < 2:
                return self.fail(404, "Not found")
            folder = self.app.ws.path(parts[0])
            full = os.path.join(folder, *parts[1].split("/"))
            if not inside(folder, full) or "/.studio/" in "/" + parts[1] or full.endswith((".blend", ".blend1")):
                return self.fail(404, "Not found")
            if os.path.isdir(full):
                full = os.path.join(full, "index.html")
            return self.file(full)
        rel = path.lstrip("/")
        full = os.path.join(UI, *rel.split("/"))
        if rel and inside(UI, full) and os.path.splitext(full)[1] in (".js", ".css", ".svg", ".png", ".jpg", ".json", ".ico", ".woff2"):
            return self.file(full)
        return self.fail(404, "Not found")

    # ------------------------------------------------------------------ API
    def api(self, method, path, query):
        app = self.app
        parts = [p for p in path.split("/") if p]
        if method == "GET" and parts == ["status"]:
            return self.send(200, {"blender": BLENDER.status(), "features": BLENDER.features, "keys": keys_status(),
                                   "workspace": app.ws.root, "keys_file": KEYS_FILE, "kit": KIT,
                                   "platform": platform.system(), "python": platform.python_version(),
                                   "timings": dict(DEFAULT_TIMES, **settings().get("timings", {})),
                                   "rooms_scanning": ROOMS.scanning,
                                   "job": app.builder.current.snapshot(10 ** 9) if app.builder.current else None})
        if parts == ["blender"] and method == "POST":
            data = self.json_body()
            path_in = os.path.expanduser((data.get("path") or "").strip().strip('"'))
            if path_in:
                if MAC and path_in.endswith(".app"):
                    path_in = os.path.join(path_in, "Contents", "MacOS", "Blender")
                if os.path.isdir(path_in):
                    exe = os.path.join(path_in, "blender.exe" if WINDOWS else "blender")
                    path_in = exe if os.path.isfile(exe) else path_in
                v = blender_version(path_in) if os.path.isfile(path_in) else None
                if not v:
                    raise UserError("That doesn't look like Blender. Choose the Blender app (or blender.exe).")
                if v[:2] < MIN_BLENDER:
                    raise UserError(f"That's Blender {'.'.join(map(str, v))}. RoomKit needs {MIN_BLENDER[0]}.{MIN_BLENDER[1]} or newer.")
                update_settings(blender=path_in)
                os.environ.pop("ROOMKIT_BLENDER_ONLY", None)            # the page's choice wins from now on
            elif data.get("reset"):
                update_settings(blender="")
                os.environ.pop("ROOMKIT_BLENDER_ONLY", None)
            status = BLENDER.detect()
            if status["state"] == "ok" and ROOMS.stale():
                ROOMS.refresh()
            return self.send(200, status)
        if parts == ["rooms"] and method == "GET":
            if ROOMS.stale() and not ROOMS.scanning:
                ROOMS.refresh()
            return self.send(200, ROOMS.get())
        if parts == ["rooms", "refresh"] and method == "POST":
            ROOMS.refresh(force=True)
            return self.send(200, {"ok": True})
        if parts == ["personas"] and method == "GET":
            return self.send(200, read_json(os.path.join(UI, "personas.json"), {}))
        if parts == ["keys"]:
            if method == "GET":
                return self.send(200, keys_status())
            if method == "POST":
                data = self.json_body()
                save_key(data.get("provider", ""), data.get("key", ""))
                return self.send(200, keys_status())
        if parts == ["projects"]:
            if method == "GET":
                return self.send(200, app.ws.list())
            if method == "POST":
                pid = app.ws.create(self.json_body().get("name", ""))
                update_settings(last_project=pid)
                return self.send(200, app.ws.load(pid))
        if len(parts) >= 2 and parts[0] == "projects":
            pid = parts[1]
            rest = parts[2:]
            folder = app.ws.path(pid)
            if not rest and method == "GET":
                update_settings(last_project=pid)
                return self.send(200, app.ws.load(pid))
            if not rest and method == "PUT":
                data = self.json_body()
                app.ws.save(pid, data.get("profile"), data.get("studio"))
                return self.send(200, {"ok": True, "saved": time.time()})
            if rest == ["upload"] and method == "POST":
                kind = (query.get("kind") or ["images"])[0]
                name = (query.get("name") or ["upload"])[0]
                rel = store_upload(folder, "furniture" if kind == "furniture" else "images", name, self.body())
                return self.send(200, {"path": rel, "url": f"/p/{urllib.parse.quote(pid)}/{urllib.parse.quote(rel)}"})
            if rest == ["sample"] and method == "POST":
                return self.send(200, load_sample(app.ws, pid))
            if rest == ["build"] and method == "POST":
                job = app.builder.start(pid, self.json_body())
                return self.send(200, job.snapshot())
            if rest == ["open"] and method == "POST":
                what = self.json_body().get("what", "output")
                target = os.path.join(folder, "output") if what == "output" else folder
                reveal(target if os.path.isdir(target) else folder)
                return self.send(200, {"ok": True})
            if rest == ["zip"] and method == "GET":
                z = make_zip(folder)
                fname = re.sub(r"[^A-Za-z0-9 _-]", "", os.path.basename(z)) or "website.zip"
                size = os.path.getsize(z)
                self.send_response(200)
                self.send_header("Content-Type", "application/zip")
                self.send_header("Content-Length", str(size))
                self.send_header("Content-Disposition", f'attachment; filename="{fname}"')
                self.end_headers()
                with open(z, "rb") as f:
                    shutil.copyfileobj(f, self.wfile, 1 << 20)
                return None
        if len(parts) >= 2 and parts[0] == "jobs":
            job = app.builder.jobs.get(parts[1])
            if not job:
                raise UserError("That build isn't running any more.", 404)
            if len(parts) == 2 and method == "GET":
                return self.send(200, job.snapshot((query.get("since") or ["0"])[0]))
            if parts[2:] == ["cancel"] and method == "POST":
                job.cancel()
                return self.send(200, {"ok": True})
        if parts == ["quit"] and method == "POST":
            self.send(200, {"ok": True})
            threading.Thread(target=app.stop, daemon=True).start()
            return None
        raise UserError("Not found", 404)


def load_sample(ws, pid):
    """Fill a project with the kit's sample profile (handy to see how everything works)."""
    folder = ws.path(pid)
    sample = read_json(os.path.join(KIT, "profile.json"), {})
    projects = []
    for pr in sample.get("projects", []):
        src = os.path.join(KIT, pr.get("image", ""))
        rel = ""
        if pr.get("image") and os.path.isfile(src):
            rel = f"images/{os.path.basename(src)}"
            shutil.copyfile(src, os.path.join(folder, rel))
        projects.append(dict(pr, image=rel))
    profile = dict(sample, projects=projects)
    ws.save(pid, profile, None)
    return ws.load(pid)


class App:
    def __init__(self, args):
        self.ws = Workspace(args.workspace)
        self.ws.ensure()
        self.builder = Builder(self.ws)
        self.token = secrets.token_urlsafe(24)
        self.verbose = args.verbose
        self.httpd, self.port, self.hosts = None, 0, set()

    def serve(self, first_port):
        for port in range(first_port, first_port + 100):
            try:
                self.httpd = Server(("127.0.0.1", port), Handler)
                self.port = port
                break
            except OSError:
                continue
        if not self.httpd:
            raise SystemExit("RoomKit Studio couldn't find a free port. Close other copies of Studio and try again.")
        self.hosts = {f"127.0.0.1:{self.port}", f"localhost:{self.port}"}
        Handler.app = self
        return f"http://127.0.0.1:{self.port}/"

    def stop(self):
        time.sleep(0.3)
        job = self.builder.current
        if job and job.state == "running":
            job.cancel()
        self.httpd.shutdown()


def main():
    p = argparse.ArgumentParser(prog="studio.py", description="RoomKit Studio: build your 3D room portfolio in the browser.")
    p.add_argument("--port", type=int, default=int(os.environ.get("ROOMKIT_PORT") or 8765))
    p.add_argument("--workspace", default=os.environ.get("ROOMKIT_PROJECTS") or DEFAULT_WORKSPACE)
    p.add_argument("--no-browser", action="store_true")
    p.add_argument("--blender", default="")
    p.add_argument("--verbose", action="store_true")
    args = p.parse_args()
    if args.blender:
        exe = os.path.abspath(os.path.expanduser(args.blender))
        if MAC and exe.endswith(".app"):
            exe = os.path.join(exe, "Contents", "MacOS", "Blender")
        os.environ["BLENDER"] = os.environ["ROOMKIT_BLENDER_ONLY"] = exe
    app = App(args)
    url = app.serve(args.port)
    threading.Thread(target=BLENDER.detect, daemon=True).start()
    if ROOMS.stale():
        ROOMS.refresh()
    print("")
    print("  RoomKit Studio is running.")
    print(f"  Open {url} in your browser if it doesn't open by itself.")
    print(f"  Your projects are saved in: {app.ws.root}")
    print("  Keep this window open while you work. Close it (or press Ctrl+C) to stop Studio.")
    print("", flush=True)
    if not args.no_browser:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        app.httpd.serve_forever(poll_interval=0.3)
    except KeyboardInterrupt:
        pass
    finally:
        job = app.builder.current
        if job and job.state == "running":
            job.cancel()
        app.httpd.server_close()
        print("RoomKit Studio stopped. See you soon!")


if __name__ == "__main__":
    main()
