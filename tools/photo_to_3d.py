"""
3D ROOM PORTFOLIO KIT  -  PHOTO TO 3D MODEL (AI)
================================================
Turns one photo of a piece of furniture, a product or a pet into a textured 3D model (.glb)
using an online AI service. add_furniture.py then puts that model into a room slot.

  python3 tools/photo_to_3d.py --photo my_chair.jpg --out my_chair.glb
  python3 tools/photo_to_3d.py --photo my_chair.jpg --out my_chair.glb --provider meshy --yes

Normally you don't run this yourself - add --ai to add_furniture.py:
  blender -b room.blend -P tools/add_furniture.py -- --slot chair --photo my_chair.jpg --ai auto

Providers (--provider):
  auto      (default) the first one you have a key for: meshy, then fal, then the free hf route
  meshy     Meshy.ai - best results. Needs MESHY_API_KEY (paid Meshy plan). About $0.30-$0.60 a model.
  fal       fal.ai TRELLIS - pay as you go. Needs FAL_KEY. About $0.02 (draft) - $0.30 (standard) a model.
  hf        free TRELLIS demo on Hugging Face. No key needed (a free HF_TOKEN gives more daily quota).
            Best effort: 1-2 models a day, and it can be busy or asleep.
  sample    offline practice run: returns samples/sample_armchair.glb after a short wait. Costs nothing.
Options:
  --quality draft|standard   draft = cheaper/faster, fewer polygons (good for small props)
  --yes                      allow a paid provider to spend money without asking
  --timeout SECONDS          give up waiting after this long (default 600). Run again to pick the job up.
  --dry-run                  show exactly what would be sent (and the cost) without sending anything
  --no-cache                 always make a new model (normally the same photo is never paid for twice)

Keys: environment variables (MESHY_API_KEY, FAL_KEY, HF_TOKEN) or ~/.roomkit/keys.json, e.g.
  {"MESHY_API_KEY": "msy_...", "FAL_KEY": "...", "HF_TOKEN": "hf_..."}
Never put keys in profile.json - that file often ends up on the web.

Exit codes: 0 ok, 2 bad input (photo/arguments), 3 no provider available or all failed
            (add_furniture.py then builds the free blocky version), 4 timed out.
Pure Python standard library: runs with python3 and with Blender's own Python.
"""

import argparse
import base64
import hashlib
import json
import os
import shutil
import ssl
import struct
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
import uuid

KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAMPLE_GLB = os.path.join(KIT, "samples", "sample_armchair.glb")
HOME = os.path.abspath(os.path.expanduser(os.environ.get("ROOMKIT_HOME") or "~/.roomkit"))
CACHE = os.path.join(HOME, "cache")
JOBS = os.path.join(HOME, "jobs.json")
KEYS_FILE = os.path.join(HOME, "keys.json")

OK, BAD_INPUT, NO_PROVIDER, TIMED_OUT = 0, 2, 3, 4
AUTO_ORDER = ("meshy", "fal", "hf")
KEY_NAMES = {"meshy": "MESHY_API_KEY", "fal": "FAL_KEY", "hf": "HF_TOKEN"}

# What each provider/quality costs (estimates, Nov 2026 - see the research brief / provider pricing pages).
MESHY_URL = "https://api.meshy.ai/openapi/v1/image-to-3d"
FAL_QUEUE = "https://queue.fal.run/"
HF_SPACE = os.environ.get("ROOMKIT_HF_SPACE", "https://trellis-community-trellis.hf.space")
PLANS = {
    ("meshy", "standard"): {"model": "meshy-7.1 (latest), 2K PBR texture, 20k triangles", "cost": 0.60,
                            "credits": "30 credits", "minutes": "about 2-3 minutes"},
    ("meshy", "draft"): {"model": "meshy-6-lite, 2K texture, 8k triangles", "cost": 0.30,
                         "credits": "15 credits", "minutes": "about 1-2 minutes"},
    ("fal", "standard"): {"model": "fal-ai/trellis-2 (1024, 30k triangles, 2K texture)", "cost": 0.30,
                          "credits": "", "minutes": "about 1-2 minutes"},
    ("fal", "draft"): {"model": "fal-ai/trellis (v1, 1K texture)", "cost": 0.02, "credits": "",
                       "minutes": "under a minute"},
    ("hf", "standard"): {"model": "TRELLIS on a free Hugging Face Space", "cost": 0.0, "credits": "",
                         "minutes": "about 1-3 minutes plus queue time"},
    ("hf", "draft"): {"model": "TRELLIS on a free Hugging Face Space (512 texture)", "cost": 0.0, "credits": "",
                      "minutes": "about 1-3 minutes plus queue time"},
    ("sample", "standard"): {"model": "offline sample armchair", "cost": 0.0, "credits": "", "minutes": "a moment"},
    ("sample", "draft"): {"model": "offline sample armchair", "cost": 0.0, "credits": "", "minutes": "a moment"},
}


def say(msg):
    print(f"[photo-to-3d] {msg}", flush=True)


class Stop(Exception):
    """Ends the run with an exit code and a plain-language message."""

    def __init__(self, code, msg):
        super().__init__(msg)
        self.code = code


class ProviderFailed(Exception):
    """This provider did not work; auto mode tries the next one."""


class TimedOut(Exception):
    pass


# ===================================================================== keys, cache, jobs
def load_keys():
    keys = {}
    try:
        with open(KEYS_FILE, encoding="utf-8") as f:
            data = json.load(f)
        for prov, env in KEY_NAMES.items():
            v = data.get(env) or data.get(prov) or data.get(prov.upper())
            if v:
                keys[prov] = str(v).strip()
    except FileNotFoundError:
        pass
    except (OSError, ValueError) as err:
        say(f"note: could not read {KEYS_FILE} ({err}); using environment variables only")
    for prov, env in KEY_NAMES.items():                 # environment wins over the file
        if os.environ.get(env, "").strip():
            keys[prov] = os.environ[env].strip()
    return keys


def read_jobs():
    try:
        with open(JOBS, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def write_jobs(jobs):
    os.makedirs(HOME, exist_ok=True)
    tmp = JOBS + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=1)
    os.replace(tmp, JOBS)


def remember_job(key, job):
    jobs = read_jobs()
    jobs[key] = dict(job, saved=time.time())
    write_jobs(jobs)


def forget_job(key):
    jobs = read_jobs()
    if jobs.pop(key, None) is not None:
        write_jobs(jobs)


def cache_key(photo_bytes, provider, quality):
    h = hashlib.sha256(photo_bytes)
    h.update(f"|{provider}|{quality}".encode())
    return h.hexdigest()


# ===================================================================== photo checks + conversion
def sniff(data):
    """Image type from the file's first bytes (file extensions lie, e.g. HEIC saved as .jpg)."""
    if data[:3] == b"\xff\xd8\xff":
        return "jpeg"
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return "png"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "webp"
    if data[4:8] == b"ftyp":
        brand = data[8:12]
        if brand in (b"heic", b"heix", b"hevc", b"hevx", b"mif1", b"msf1", b"heim", b"heis"):
            return "heic"
        if brand in (b"avif", b"avis"):
            return "avif"
    if data[:2] in (b"II", b"MM") and data[2:4] in (b"*\x00", b"\x00*"):
        return "tiff"
    if data[:2] == b"BM":
        return "bmp"
    if data[:6] in (b"GIF87a", b"GIF89a"):
        return "gif"
    return ""


def image_size(data, kind):
    """(width, height) for jpeg/png/webp using only the file header, or None."""
    try:
        if kind == "png":
            return struct.unpack(">II", data[16:24])
        if kind == "webp":
            chunk = data[12:16]
            if chunk == b"VP8X":
                w = int.from_bytes(data[24:27], "little") + 1
                h = int.from_bytes(data[27:30], "little") + 1
                return w, h
            if chunk == b"VP8L":
                b = int.from_bytes(data[21:25], "little")
                return (b & 0x3FFF) + 1, ((b >> 14) & 0x3FFF) + 1
            if chunk == b"VP8 ":
                w, h = struct.unpack("<HH", data[26:30])
                return w & 0x3FFF, h & 0x3FFF
        if kind == "jpeg":
            i = 2
            while i < len(data) - 9:
                if data[i] != 0xFF:
                    i += 1
                    continue
                marker = data[i + 1]
                if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
                    i += 2
                    continue
                length = struct.unpack(">H", data[i + 2:i + 4])[0]
                if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                    h, w = struct.unpack(">HH", data[i + 5:i + 9])
                    return w, h
                i += 2 + length
    except (struct.error, IndexError):
        pass
    return None


def convert_with_sips(src, dst, max_side=None):
    """macOS built-in image tool: any format -> JPEG, optionally shrunk."""
    if not shutil.which("sips"):
        return False
    cmd = ["sips", "-s", "format", "jpeg", "-s", "formatOptions", "90"]
    if max_side:
        cmd += ["-Z", str(max_side)]
    cmd += [src, "--out", dst]
    try:
        r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
    except (OSError, subprocess.TimeoutExpired):
        return False
    return r.returncode == 0 and os.path.isfile(dst) and os.path.getsize(dst) > 0


def convert_with_blender(src, dst, max_side=None):
    """Inside Blender: load, shrink and save as JPEG with bpy (no PIL needed). HEIC is not supported by Blender."""
    try:
        import bpy                                      # noqa: F401  (only available inside Blender)
    except ImportError:
        return False
    try:
        img = bpy.data.images.load(src)
        w, h = img.size
        if not w or not h:
            return False
        if max_side and max(w, h) > max_side:
            k = max_side / max(w, h)
            img.scale(max(1, round(w * k)), max(1, round(h * k)))
        img.filepath_raw = dst
        img.file_format = "JPEG"
        img.save()
        bpy.data.images.remove(img)
        return os.path.isfile(dst)
    except Exception:                                   # noqa: BLE001
        return False


def prepare_photo(path, work_dir=None, max_side=2048):
    """Checks a photo and returns (path_to_send, kind, bytes). Converts HEIC/TIFF/BMP/GIF/AVIF to JPEG and
    shrinks very big photos. Raises Stop(BAD_INPUT, message) with a plain-language reason when it can't."""
    path = os.path.abspath(os.path.expanduser(path or ""))
    if not os.path.isfile(path):
        raise Stop(BAD_INPUT, f"Photo not found: {path}")
    with open(path, "rb") as f:
        data = f.read()
    if not data:
        raise Stop(BAD_INPUT, f"The photo file is empty: {path}")
    kind = sniff(data)
    if not kind:
        raise Stop(BAD_INPUT, "That file doesn't look like a photo. Use a .jpg, .png, .webp or iPhone .heic image.")
    size = image_size(data, kind) if kind in ("jpeg", "png", "webp") else None
    too_big = len(data) > 8 * 1024 * 1024 or (size is not None and max(size) > max_side)
    if kind in ("jpeg", "png", "webp") and not too_big:
        if size and min(size) < 64:
            raise Stop(BAD_INPUT, f"The photo is tiny ({size[0]}x{size[1]} pixels). Use one at least 256 pixels wide.")
        if size and min(size) < 256:
            say(f"note: the photo is small ({size[0]}x{size[1]}); a bigger one gives a better model")
        return path, kind, data
    work_dir = work_dir or tempfile.mkdtemp(prefix="roomkit_photo_")
    os.makedirs(work_dir, exist_ok=True)
    dst = os.path.join(work_dir, os.path.splitext(os.path.basename(path))[0] + "_prepared.jpg")
    what = "shrinking the big photo" if kind in ("jpeg", "png", "webp") else f"converting the {kind.upper()} photo to JPEG"
    say(what)
    if convert_with_sips(path, dst, max_side) or (kind != "heic" and convert_with_blender(path, dst, max_side)):
        with open(dst, "rb") as f:
            out = f.read()
        return dst, "jpeg", out
    if kind in ("jpeg", "png", "webp") and len(data) <= 20 * 1024 * 1024:
        say("note: could not shrink the photo on this computer; sending it as it is")
        return path, kind, data
    if kind in ("heic", "avif"):
        raise Stop(BAD_INPUT, f"This computer can't convert {kind.upper()} photos (iPhone format). Open the photo and "
                              "export or share it as JPEG, or on iPhone choose Settings > Camera > Formats > "
                              "Most Compatible, then try again.")
    raise Stop(BAD_INPUT, f"Can't read this {kind.upper()} image here. Save it as a .jpg or .png and try again.")


def data_uri(kind, data):
    return f"data:image/{kind};base64," + base64.b64encode(data).decode("ascii")


# ===================================================================== HTTP (urllib only)
def ssl_context():
    try:
        import certifi                                   # Blender bundles it; python.org Pythons may lack root certs
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


SSL = ssl_context()


class HttpError(Exception):
    def __init__(self, code, body, headers=None):
        super().__init__(f"HTTP {code}")
        self.code, self.body, self.headers = code, body, headers or {}


def http(method, url, headers=None, body=None, timeout=60):
    """-> (status, headers, bytes). body may be bytes or a JSON-able object."""
    h = dict(headers or {})
    if body is not None and not isinstance(body, (bytes, bytearray)):
        body = json.dumps(body).encode()
        h.setdefault("Content-Type", "application/json")
    h.setdefault("User-Agent", "RoomKit-photo-to-3d/1.0")
    req = urllib.request.Request(url, data=body, headers=h, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=SSL) as r:
            return r.status, dict(r.headers), r.read()
    except urllib.error.HTTPError as err:
        raise HttpError(err.code, err.read().decode("utf-8", "replace")[:600], dict(err.headers or {})) from None
    except (urllib.error.URLError, OSError) as err:
        if isinstance(err, ssl.SSLCertVerificationError) or isinstance(getattr(err, "reason", None),
                                                                      ssl.SSLCertVerificationError):
            raise ProviderFailed("this Python can't check secure web certificates. On a Mac run "
                                 "'Install Certificates.command' from your Python folder, or use Blender's Python.")
        raise ProviderFailed(f"could not reach {url.split('/')[2]} ({getattr(err, 'reason', err)}). "
                             "Check your internet connection.")


def http_json(method, url, headers=None, body=None, timeout=60):
    _, _, raw = http(method, url, headers, body, timeout)
    return json.loads(raw.decode("utf-8") or "{}")


def download(url, out, headers=None, timeout=300):
    _, _, raw = http("GET", url, headers, None, timeout)
    if raw[:4] != b"glTF":
        raise ProviderFailed("the service sent back something that is not a .glb model")
    tmp = out + ".part"
    with open(tmp, "wb") as f:
        f.write(raw)
    os.replace(tmp, out)
    return out


def explain(provider, err):
    """HTTP error -> plain language."""
    body = (err.body or "").lower()
    if err.code == 401 or err.code == 403 and "quota" not in body:
        return f"{provider}: the API key was refused. Check {KEY_NAMES.get(provider, 'the key')} (copy it again from the website)."
    if err.code == 402 or "credit" in body or "balance" in body:
        return f"{provider}: not enough credits on your account. Top up on the provider's website."
    if err.code == 429:
        return f"{provider}: the service is busy (too many requests). Try again in a minute."
    if err.code == 400 or "moderation" in body:
        return f"{provider}: the photo was rejected ({err.body[:160]}). Try a different photo: one object, plain background."
    if err.code >= 500:
        return f"{provider}: the service has a problem right now (HTTP {err.code}). Try again later."
    return f"{provider}: HTTP {err.code} {err.body[:200]}"


class Clock:
    def __init__(self, seconds):
        self.end = time.time() + seconds

    def left(self):
        return self.end - time.time()

    def sleep(self, s):
        if self.left() <= 0:
            raise TimedOut()
        time.sleep(max(0.0, min(s, self.left())))
        if self.left() <= 0:
            raise TimedOut()


# ===================================================================== providers
def meshy_body(uri, quality):
    body = {"image_url": uri, "should_texture": True, "should_remesh": True, "topology": "triangle",
            "remove_lighting": True, "target_formats": ["glb"], "origin_at": "bottom"}
    if quality == "draft":
        body.update(ai_model="meshy-6-lite", target_polycount=8000, enable_pbr=False)
    else:
        body.update(ai_model="latest", target_polycount=20000, enable_pbr=True, texture_resolution="2k")
    return body


def fal_request(uri, quality):
    if quality == "draft":
        return "fal-ai/trellis", {"image_url": uri, "texture_size": "1024", "mesh_simplify": 0.95}
    return "fal-ai/trellis-2", {"image_url": uri, "resolution": "1024", "texture_size": "2048",
                                "decimation_target": 30000, "remesh": True}


def run_meshy(key, uri, quality, out, clock, job_key):
    H = {"Authorization": "Bearer " + key}
    job = read_jobs().get(job_key)
    task = job.get("task") if job and job.get("provider") == "meshy" else None
    if task:
        say(f"picking up the Meshy job started earlier ({task})")
    else:
        try:
            task = http_json("POST", MESHY_URL, H, meshy_body(uri, quality), timeout=90)["result"]
        except HttpError as err:
            raise ProviderFailed(explain("meshy", err))
        except (KeyError, ValueError):
            raise ProviderFailed("meshy: unexpected answer from the service")
        remember_job(job_key, {"provider": "meshy", "task": task})
        say(f"Meshy job started ({task})")
    last, wait = -1, 5
    while True:
        try:
            status, headers, raw = http("GET", f"{MESHY_URL}/{task}", H, timeout=30)
            t = json.loads(raw.decode("utf-8"))
            wait = float(headers.get("Retry-After") or 5)
        except HttpError as err:
            if err.code == 404:
                forget_job(job_key)
                raise ProviderFailed("meshy: the earlier job has expired. Run again to start a new one.")
            if err.code in (429, 500, 502, 503, 504):
                clock.sleep(10)                         # busy: not a failure, ask again later
                continue
            raise ProviderFailed(explain("meshy", err))
        except ProviderFailed:
            clock.sleep(10)                             # a short network blip while waiting
            continue
        st = t.get("status", "")
        if st == "SUCCEEDED":
            url = (t.get("model_urls") or {}).get("glb")
            if not url:
                raise ProviderFailed("meshy: finished, but no .glb was returned")
            say("Meshy finished - downloading the model")
            download(url, out)
            forget_job(job_key)
            return {"model": t.get("ai_model") or "meshy", "task": task}
        if st in ("FAILED", "CANCELED", "EXPIRED"):
            forget_job(job_key)
            msg = (t.get("task_error") or {}).get("message") if isinstance(t.get("task_error"), dict) else t.get("task_error")
            raise ProviderFailed(f"meshy: the job {st.lower()} ({msg or 'no reason given'}). Failed jobs are refunded.")
        p = int(t.get("progress") or 0)
        if p != last:
            say(f"Meshy: {st.lower().replace('_', ' ') or 'waiting'} {p}%")
            last = p
        clock.sleep(max(2.0, min(wait, 15)))


def run_fal(key, uri, quality, out, clock, job_key):
    H = {"Authorization": "Key " + key}
    model, body = fal_request(uri, quality)
    job = read_jobs().get(job_key)
    if job and job.get("provider") == "fal" and job.get("status_url"):
        sub = job
        say("picking up the fal.ai job started earlier")
    else:
        try:
            sub = http_json("POST", FAL_QUEUE + model, H, body, timeout=90)
        except HttpError as err:
            raise ProviderFailed(explain("fal", err))
        if not sub.get("status_url"):
            raise ProviderFailed("fal: unexpected answer from the service")
        remember_job(job_key, {"provider": "fal", "status_url": sub["status_url"], "response_url": sub["response_url"],
                               "request_id": sub.get("request_id", "")})
        say(f"fal.ai job started ({model})")
    last = None
    while True:
        try:
            s = http_json("GET", sub["status_url"], H, timeout=30)
        except HttpError as err:
            if err.code in (404, 410):
                forget_job(job_key)
                raise ProviderFailed("fal: the earlier job has expired. Run again to start a new one.")
            if err.code in (429, 500, 502, 503, 504):
                clock.sleep(6)
                continue
            raise ProviderFailed(explain("fal", err))
        except ProviderFailed:
            clock.sleep(6)
            continue
        st = s.get("status", "")
        if st == "COMPLETED":
            if s.get("error"):
                forget_job(job_key)
                raise ProviderFailed(f"fal: the job failed ({s['error']})")
            try:
                res = http_json("GET", sub["response_url"], H, timeout=60)
            except HttpError as err:
                forget_job(job_key)
                raise ProviderFailed(explain("fal", err))
            mesh = res.get("model_glb") or res.get("model_mesh") or {}
            if not mesh.get("url"):
                forget_job(job_key)
                raise ProviderFailed("fal: finished, but no .glb was returned")
            say("fal.ai finished - downloading the model")
            download(mesh["url"], out)
            forget_job(job_key)
            return {"model": model, "task": sub.get("request_id", "")}
        msg = f"fal.ai: in queue (position {s.get('queue_position')})" if st == "IN_QUEUE" else f"fal.ai: {st.lower().replace('_', ' ')}"
        if msg != last:
            say(msg)
            last = msg
        clock.sleep(3)


def _multipart(field, filename, mime, data):
    b = uuid.uuid4().hex
    body = (f'--{b}\r\nContent-Disposition: form-data; name="{field}"; filename="{filename}"\r\n'
            f"Content-Type: {mime}\r\n\r\n").encode() + data + f"\r\n--{b}--\r\n".encode()
    return body, "multipart/form-data; boundary=" + b


def run_hf(token, photo_path, kind, data, quality, out, clock):
    """Free TRELLIS Space through Gradio's raw queue protocol (no gradio_client needed)."""
    H = {"Authorization": "Bearer " + token} if token else {}
    root = HF_SPACE.rstrip("/")
    try:
        cfg = http_json("GET", root + "/config", H, timeout=30)
    except HttpError as err:
        raise ProviderFailed(f"hf: the free Space is not answering (HTTP {err.code}); it may be asleep or moved.")
    api = root + (cfg.get("api_prefix") or "")
    deps = cfg.get("dependencies", [])
    fns = {d.get("api_name"): (d.get("id", i), d) for i, d in enumerate(deps)}
    need = ("start_session", "preprocess_image", "generate_and_extract_glb")
    if not all(n in fns for n in need) or len(fns["generate_and_extract_glb"][1].get("inputs", [])) != 11:
        raise ProviderFailed("hf: the free Space has changed and this kit can't drive it any more. "
                             "Use Meshy or fal.ai, or the free blocky version.")
    session = uuid.uuid4().hex[:11]

    def call(name, payload):
        fn, dep = fns[name]
        trig = (dep.get("targets") or [[None]])[0][0]
        try:
            j = http_json("POST", api + "/queue/join", H, {"data": payload, "event_data": None, "fn_index": fn,
                                                          "trigger_id": trig, "session_hash": session}, timeout=60)
        except HttpError as err:
            raise ProviderFailed(f"hf: the Space refused the job (HTTP {err.code})")
        event = j.get("event_id")
        req = urllib.request.Request(f"{api}/queue/data?session_hash={session}", headers=dict(H, Accept="text/event-stream"))
        try:
            with urllib.request.urlopen(req, timeout=max(30, clock.left()), context=SSL) as stream:
                for line in stream:
                    if clock.left() <= 0:
                        raise TimedOut()
                    if not line.startswith(b"data:"):
                        continue
                    try:
                        m = json.loads(line[5:])
                    except ValueError:
                        continue
                    if event and m.get("event_id") not in (None, event):
                        continue
                    kind_ = m.get("msg")
                    if kind_ == "estimation" and m.get("rank") is not None:
                        say(f"hf: in queue (place {m.get('rank', 0) + 1}, about {round(m.get('rank_eta') or 0)} s)")
                    elif kind_ == "process_starts":
                        say(f"hf: {name.replace('_', ' ')} started")
                    elif kind_ == "process_completed":
                        if not m.get("success"):
                            err = str((m.get("output") or {}).get("error") or "unknown error")
                            if "quota" in err.lower():
                                raise ProviderFailed("hf: the free daily GPU quota is used up. Add a free Hugging Face "
                                                     "token (HF_TOKEN) for more, or try again tomorrow.")
                            raise ProviderFailed(f"hf: the Space failed ({err[:200]})")
                        return (m.get("output") or {}).get("data") or []
                    elif kind_ == "close_stream":
                        break
        except TimedOut:
            raise
        except (urllib.error.URLError, OSError) as err:
            if clock.left() <= 0:
                raise TimedOut()
            raise ProviderFailed(f"hf: lost the connection to the Space ({err})")
        raise ProviderFailed("hf: the Space closed the connection without a result")

    say("hf: connecting to the free TRELLIS Space (best effort)")
    call("start_session", [])
    body, ctype = _multipart("files", os.path.basename(photo_path), f"image/{kind}", data)
    try:
        paths = http_json("POST", api + f"/upload?upload_id={uuid.uuid4().hex[:10]}", dict(H, **{"Content-Type": ctype}),
                          body, timeout=120)
    except HttpError as err:
        raise ProviderFailed(f"hf: photo upload failed (HTTP {err.code})")
    img = {"path": paths[0], "orig_name": os.path.basename(photo_path), "mime_type": f"image/{kind}",
           "meta": {"_type": "gradio.FileData"}}
    cut = call("preprocess_image", [img])                 # removes the background, like the web page does
    img = cut[0] if cut and cut[0] else img
    tex = 512 if quality == "draft" else 1024
    res = call("generate_and_extract_glb", [img, [], None, 0, 7.5, 12, 3.0, 12, "stochastic", 0.95, tex])
    glb = None
    for item in (res[3:4] + res[2:3]) if len(res) >= 3 else []:
        item = item.get("value", item) if isinstance(item, dict) else item
        if isinstance(item, dict) and (item.get("url") or item.get("path")):
            glb = item
            break
    if not glb:
        raise ProviderFailed("hf: finished, but no .glb came back")
    url = glb.get("url") or f"{api}/file={glb['path']}"
    say("hf: finished - downloading the model")
    download(url, out, H)
    return {"model": "TRELLIS (Hugging Face Space)", "task": session}


def run_sample(out, clock):
    if not os.path.isfile(SAMPLE_GLB):
        raise ProviderFailed(f"sample: {SAMPLE_GLB} is missing")
    for p in (25, 60, 100):
        say(f"sample: working {p}%")
        clock.sleep(0.5)
    shutil.copyfile(SAMPLE_GLB, out)
    return {"model": "sample armchair (offline)", "task": "sample"}


# ===================================================================== main
def confirm_cost(provider, quality, yes):
    plan = PLANS[(provider, quality)]
    if plan["cost"] <= 0:
        return True
    extra = f" ({plan['credits']})" if plan["credits"] else ""
    say(f"{provider} will make this model with {plan['model']}.")
    say(f"Estimated cost: about ${plan['cost']:.2f}{extra}, {plan['minutes']}. Failed jobs are not charged.")
    if yes:
        return True
    if sys.stdin is not None and sys.stdin.isatty():
        try:
            say("Spend this? Type y and press Enter:")      # own line, so it shows even when output is piped
            answer = input().strip().lower()
        except EOFError:
            answer = ""
        return answer in ("y", "yes")
    say(f"Not spending money without permission: add --yes to allow {provider}.")
    return False


def dry_run(provider, quality, keys, kind, data, path):
    uri = data_uri(kind, data)
    short = uri[:48] + f"...<{len(uri)} characters>"
    mask = lambda k: (k[:4] + "..." + k[-2:]) if k and len(k) > 8 else ("<not set>" if not k else "***")
    if provider == "meshy":
        body = meshy_body(short, quality)
        req = {"method": "POST", "url": MESHY_URL, "headers": {"Authorization": "Bearer " + mask(keys.get("meshy"))},
               "json": body, "then": f"poll GET {MESHY_URL}/<task id> until SUCCEEDED, download model_urls.glb"}
    elif provider == "fal":
        model, body = fal_request(short, quality)
        req = {"method": "POST", "url": FAL_QUEUE + model, "headers": {"Authorization": "Key " + mask(keys.get("fal"))},
               "json": body, "then": "poll status_url until COMPLETED, GET response_url, download model_glb.url"}
    elif provider == "hf":
        req = {"method": "POST", "url": HF_SPACE + "/gradio_api/queue/join",
               "steps": ["GET /config", "start_session", "POST /upload (photo)", "preprocess_image",
                         "generate_and_extract_glb", "download GLB"],
               "headers": {"Authorization": "Bearer " + mask(keys.get("hf"))} if keys.get("hf") else {}}
    else:
        req = {"copy": SAMPLE_GLB}
    plan = PLANS[(provider, quality)]
    say(f"DRY RUN - nothing is sent. Photo: {path} ({kind}, {len(data) // 1024} KB)")
    say(f"provider {provider}, {plan['model']}, estimated cost ${plan['cost']:.2f}")
    print(json.dumps(req, indent=1), flush=True)


def main(argv=None):
    p = argparse.ArgumentParser(prog="photo_to_3d.py", description="Turn a photo into a 3D model (.glb) with AI.")
    p.add_argument("--photo", required=True, help="photo of one object (.jpg, .png, .webp, .heic)")
    p.add_argument("--out", required=True, help="where to save the model, e.g. my_chair.glb")
    p.add_argument("--provider", default="auto", choices=["auto", "meshy", "fal", "hf", "sample"])
    p.add_argument("--quality", default="standard", choices=["draft", "standard"])
    p.add_argument("--yes", action="store_true", help="allow paid providers to spend money without asking")
    p.add_argument("--timeout", type=float, default=600, help="seconds to wait (default 600)")
    p.add_argument("--dry-run", action="store_true", help="show the request and cost, send nothing")
    p.add_argument("--no-cache", action="store_true", help="always make a new model")
    a = p.parse_args(argv)

    out = os.path.abspath(os.path.expanduser(a.out))
    try:
        if not out.lower().endswith(".glb"):
            raise Stop(BAD_INPUT, "--out must end in .glb, e.g. --out my_chair.glb")
        if a.timeout <= 0:
            raise Stop(BAD_INPUT, "--timeout must be more than 0 seconds")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        photo, kind, data = prepare_photo(a.photo, os.path.join(HOME, "tmp"))
        keys = load_keys()
        if a.provider == "auto":
            order = [pv for pv in AUTO_ORDER if pv == "hf" or keys.get(pv)]
            say(f"auto: trying {', '.join(order)}" + ("" if keys.get("meshy") or keys.get("fal") else
                " (no MESHY_API_KEY or FAL_KEY found, so using the free route)"))
        else:
            order = [a.provider]
        if a.dry_run:
            for pv in order:
                dry_run(pv, a.quality, keys, kind, data, photo)
            return OK

        clock, errors = Clock(a.timeout), []
        for pv in order:
            if pv in ("meshy", "fal") and not keys.get(pv):
                errors.append(f"{pv}: no API key. Set {KEY_NAMES[pv]} or add it to {KEYS_FILE}.")
                say(errors[-1])
                continue
            key = cache_key(data, pv, a.quality)
            cached = os.path.join(CACHE, key + ".glb")
            if pv != "sample" and not a.no_cache and os.path.isfile(cached):
                shutil.copyfile(cached, out)
                say(f"using the model made earlier from this photo ({pv}) - no new cost")
                print(f"GLB: {out}", flush=True)
                return OK
            resuming = pv in ("meshy", "fal") and read_jobs().get(key, {}).get("provider") == pv
            if not resuming and not confirm_cost(pv, a.quality, a.yes):
                errors.append(f"{pv}: not confirmed")
                continue
            say(f"using {pv} ({PLANS[(pv, a.quality)]['model']}), usually {PLANS[(pv, a.quality)]['minutes']}")
            try:
                if pv == "meshy":
                    info = run_meshy(keys["meshy"], data_uri(kind, data), a.quality, out, clock, key)
                elif pv == "fal":
                    info = run_fal(keys["fal"], data_uri(kind, data), a.quality, out, clock, key)
                elif pv == "hf":
                    info = run_hf(keys.get("hf"), photo, kind, data, a.quality, out, clock)
                else:
                    info = run_sample(out, clock)
            except ProviderFailed as err:
                errors.append(str(err))
                say(str(err))
                continue
            except TimedOut:
                if pv in ("meshy", "fal"):
                    say(f"Still working after {a.timeout:.0f} s. The job keeps running online: run the same command "
                        "again to pick it up (no extra cost).")
                else:
                    say(f"Gave up waiting after {a.timeout:.0f} s.")
                return TIMED_OUT
            if pv != "sample":
                os.makedirs(CACHE, exist_ok=True)
                shutil.copyfile(out, cached)
                with open(os.path.join(CACHE, key + ".json"), "w", encoding="utf-8") as f:
                    json.dump(dict(info, provider=pv, quality=a.quality, photo=os.path.basename(a.photo),
                                   date=time.strftime("%Y-%m-%d")), f)
            say(f"done: {os.path.getsize(out) / 1e6:.1f} MB model from {pv} ({info['model']})")
            print(f"GLB: {out}", flush=True)
            return OK
        say("No AI model could be made: " + " | ".join(errors) if errors else "No AI provider is available.")
        return NO_PROVIDER
    except Stop as err:
        say(str(err))
        return err.code
    except KeyboardInterrupt:
        say("stopped")
        return TIMED_OUT


if __name__ == "__main__":
    sys.exit(main())
