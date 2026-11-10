"""
3D ROOM PORTFOLIO KIT  -  ROOM CATALOGUE FOR ROOMKIT STUDIO
===========================================================
Writes tools/studio/rooms.json: every room in templates/ with its display name, colour themes,
furniture slots, preview pictures, how long a name fits on its sign, and who it suits.
RoomKit Studio runs this for you. You only need it if you add a room by hand.

HOW TO RUN
  python3 tools/make_manifest.py                 # quick scan, then asks Blender for the exact slots
  python3 tools/make_manifest.py --quick         # quick scan only (reads the template files, no Blender)
  python3 tools/make_manifest.py --blender /path/to/blender --build-missing
  blender -b -P tools/make_manifest.py           # same as the first line, all inside Blender
Options:
  --blender PATH     Blender to use (default: BLENDER env, then PATH)
  --quick            skip Blender; slots come from reading the template code
  --build-missing    build rooms that have no templates/output/<room>.blend yet into a private cache
                     (tools/studio/cache/), never into templates/output
  --force            ignore the cache and rescan every room
  --out FILE         where to write (default tools/studio/rooms.json)

The quick scan reads THEMES, ROOM_NAME and the slot(...) calls with Python's ast module, so it works
without Blender and is instant. The Blender pass opens each room's .blend and reads the real slot
boxes, picture and link hooks and the name sign's width, and makes small JPEG thumbnails.
"""

import argparse
import ast
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

try:
    import bpy                                          # present when this runs inside Blender
except ImportError:
    bpy = None

KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = os.path.join(KIT, "templates")
STUDIO = os.path.join(KIT, "tools", "studio")
DEFAULT_OUT = os.path.join(STUDIO, "rooms.json")
THUMBS = os.path.join(STUDIO, "thumbs")
CACHE = os.path.join(STUDIO, "cache")
MANIFEST_VERSION = 2

# Friendly names for rooms we know about. Other rooms get a name from their docstring.
DISPLAY_NAMES = {
    "dev_office": "Developer Office",
    "streamer_den": "Streamer Den",
    "living_lounge": "Living Lounge",
    "cozy_cafe": "Cosy Café",
    "cozy_bedroom": "Cosy Bedroom",
    "academia_library": "Academia Library",
    "design_studio": "Design Studio",
    "music_studio": "Music Studio",
    "potion_shop": "Potion Shop",
    "plant_shop": "Plant Shop",
    "fairytale_atelier": "Fairy-tale Gown Atelier",
    "hearth_cottage": "Hearth Cottage",
    "forest_spirit_cottage": "Forest Cottage",
    "wizard_school_dorm": "Wizard School Dorm",
    "tiny_planet_stargazer": "Tiny Planet Stargazer",
    "lantern_ramen_bar": "Lantern Ramen Bar",
    "glow_beauty_bar": "Glow Beauty Bar",
    "animal_city_apartment": "Animal City Apartment",
}

BLURBS = {
    "dev_office": "A bright desk setup with monitors, a pegboard and a cat.",
    "streamer_den": "Neon-lit gaming corner with a big desk and a comfy sofa.",
    "living_lounge": "A warm lounge with a sofa, records and a big TV wall.",
    "cozy_cafe": "A bakery café with a pastry case, menu board and bentwood chairs.",
    "cozy_bedroom": "A soft pastel bedroom with a letter-board sign and fairy lights.",
    "academia_library": "Tall bookcases, a reading chair and a rainy window.",
    "design_studio": "An airy studio with a big work table, easel and pin-up wall.",
    "music_studio": "Keys, speakers and acoustic panels in a warm home studio.",
    "potion_shop": "A candle-lit apothecary with jars, bottles and a shop sign.",
    "plant_shop": "Terracotta, buckets of flowers and a potting bench.",
    "fairytale_atelier": "A dressmaker's atelier with gown rails, a mirror and a vanity.",
    "hearth_cottage": "A countryside cottage with a fireplace and hand-painted charm.",
    "forest_spirit_cottage": "A woodland cottage full of plants and soft light.",
    "wizard_school_dorm": "A magic-school dorm with bunk beds, banners and a trunk.",
    "tiny_planet_stargazer": "A tiny planet with a telescope under the stars.",
    "lantern_ramen_bar": "A late-night noodle counter under paper lanterns.",
    "glow_beauty_bar": "A glowing beauty bar with salon chairs and a mirror wall.",
    "animal_city_apartment": "A bright city flat with a view of a busy animal metropolis.",
}

# Which personas (see tools/studio/personas.json) each room suits best.
PERSONAS = {
    "dev_office": ["student", "designer", "teacher"],
    "streamer_den": ["streamer"],
    "living_lounge": ["couple", "streamer", "designer"],
    "cozy_cafe": ["shop", "couple"],
    "cozy_bedroom": ["student", "artist", "couple", "teacher"],
    "academia_library": ["writer", "student", "teacher"],
    "design_studio": ["designer", "artist"],
    "music_studio": ["streamer", "artist"],
    "potion_shop": ["shop", "writer", "artist"],
    "plant_shop": ["shop", "designer"],
    "fairytale_atelier": ["shop", "designer", "couple", "artist"],
    "hearth_cottage": ["artist", "writer", "teacher", "couple"],
    "forest_spirit_cottage": ["artist", "writer", "teacher", "couple"],
    "wizard_school_dorm": ["student", "writer", "streamer"],
    "tiny_planet_stargazer": ["artist", "designer", "teacher", "writer"],
    "lantern_ramen_bar": ["shop", "streamer"],
    "glow_beauty_bar": ["shop", "artist"],
    "animal_city_apartment": ["streamer", "student", "teacher"],
}
KEYWORDS = {                                          # used for rooms not listed above
    "shop": ("shop", "café", "cafe", "bar", "boutique", "bakery", "store", "market"),
    "student": ("student", "dorm", "school", "bedroom"),
    "writer": ("library", "book", "writer", "study"),
    "designer": ("design", "studio", "atelier", "loft"),
    "artist": ("art", "paint", "illustrat", "craft", "cottage", "planet"),
    "streamer": ("stream", "gaming", "neon", "game"),
    "teacher": ("class", "teacher", "school"),
    "couple": ("lounge", "home", "living", "wedding"),
}

# Slot names in plain words (SPEC.md section 3 vocabulary).
SLOT_WORDS = {
    "desk": ("Desk", "Where you work"), "chair": ("Chair", "A seat at the desk or table"),
    "stool": ("Stool", "A stool or bar seat"), "sofa": ("Sofa", "The big comfy seat"),
    "armchair": ("Armchair", "A reading or lounge chair"), "bed": ("Bed", "The bed and bedding"),
    "table": ("Table", "A table"), "side_table": ("Side table", "Bedside or sofa-side table"),
    "counter": ("Counter", "The shop or bar counter"), "display_case": ("Display case", "Glass case for products"),
    "shelf": ("Shelf unit", "Shelving with books and boxes"), "wall_shelf": ("Wall shelf", "A shelf on the wall"),
    "cabinet": ("Cabinet", "Drawers or a cupboard"), "media_console": ("TV unit", "The low media console"),
    "workbench": ("Workbench", "A big work table"), "easel": ("Easel", "A painting easel"),
    "monitor": ("Computer screen", "The monitor on the desk"), "instrument": ("Instrument", "Your instrument"),
    "speaker": ("Speakers", "Speakers or studio monitors"), "hero_prop": ("Star piece", "The eye-catching centrepiece"),
    "lamp": ("Table lamp", "A lamp on a surface"), "floor_lamp": ("Floor lamp", "A standing lamp"),
    "pendant_lamp": ("Ceiling lamp", "A lamp hanging from the ceiling"), "plant": ("Plant", "A potted plant"),
    "hanging_plant": ("Hanging plant", "A plant hanging from above"), "rug": ("Rug", "The rug on the floor"),
    "wall_art": ("Wall art", "Pictures on the wall"), "pet": ("Pet", "Your pet (a photo works great)"),
    "clothes_rack": ("Clothes rail", "A rail of garments"), "wardrobe": ("Wardrobe", "A tall wardrobe"),
    "vanity": ("Vanity table", "A dressing table"), "mirror": ("Mirror", "A standing or wall mirror"),
    "telescope": ("Telescope", "A telescope on a tripod"), "trunk": ("Trunk", "A travel trunk"),
    "fireplace": ("Fireplace", "The fireplace"), "stove": ("Stove", "A stove or range"),
    "bookcase": ("Bookcase", "A tall bookcase"), "salon_chair": ("Salon chair", "A salon or beauty chair"),
    "bunk_bed": ("Bunk bed", "A bunk bed"), "window_seat": ("Window seat", "A cushioned window seat"),
    "planter": ("Planter", "A big planter box"),
}
KIND_WORDS = {"floor": "Stands on the floor", "surface": "Sits on another piece", "wall": "Hangs on the wall",
              "rug": "Lies on the floor", "hanging": "Hangs from above"}
SAMPLE_TEXT = "Alex Rivera Studio abcdefghij"            # used to measure the sign font's average letter width


def log(msg):
    print(f"[manifest] {msg}", flush=True)


def label(word):
    return word.replace("_", " ").replace("70s", " 70s").replace("  ", " ").strip().capitalize()


# ===================================================================== quick scan (no Blender)
def literal(node):
    try:
        return ast.literal_eval(node)
    except Exception:
        return None


def scan_template(path):
    """Read a template with ast: name, themes, default theme, slots. Never runs it."""
    with open(path, encoding="utf-8") as f:
        src = f.read()
    tree = ast.parse(src)
    room_id = os.path.splitext(os.path.basename(path))[0]
    found = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            key = node.targets[0].id
            if key in ("ROOM_NAME", "THEME", "THEMES") and key not in found:
                value = literal(node.value)
                if value is not None:
                    found[key] = value
    doc = (ast.get_docstring(tree) or "").splitlines()
    title = ""
    for line in doc[:3]:
        if "Template:" in line:
            title = line.split("Template:", 1)[1].strip().title()
    blurb = ""
    for line in doc[2:6]:
        if line.strip() and not set(line.strip()) <= {"="}:
            blurb = line.strip()
            break
    slots = []
    for node in ast.walk(tree):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "slot"
                and node.args and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str)):
            kw = {k.arg: literal(k.value) for k in node.keywords}
            size = literal(node.args[1]) if len(node.args) > 1 else None
            slots.append({"name": node.args[0].value, "kind": kw.get("kind") or "floor",
                          "shape": kw.get("shape") or "box",
                          "size": [round(float(v), 3) for v in size] if isinstance(size, (tuple, list)) else None})
    themes = found.get("THEMES") if isinstance(found.get("THEMES"), dict) else {}
    return {
        "id": found.get("ROOM_NAME") or room_id, "file_id": room_id, "doc_title": title, "doc_blurb": blurb,
        "default_theme": found.get("THEME") if isinstance(found.get("THEME"), str) else next(iter(themes), ""),
        "themes": themes, "slots": slots,
    }


def kit_rel(path):
    return os.path.relpath(path, KIT).replace(os.sep, "/")


def find_preview(room, theme, default_theme):
    names = [f"{room}__{theme}.png"] + ([f"{room}.png"] if theme == default_theme else [])
    for folder in (os.path.join(KIT, "previews"), os.path.join(TEMPLATES, "output")):
        for n in names:
            p = os.path.join(folder, n)
            if os.path.isfile(p):
                return p
    return ""


def blend_for(room_id):
    official = os.path.join(TEMPLATES, "output", f"{room_id}.blend")
    if os.path.isfile(official):
        return official
    cached = os.path.join(CACHE, room_id, "output", f"{room_id}.blend")
    return cached if os.path.isfile(cached) else ""


def signature(*paths):
    sig = []
    for p in paths:
        try:
            st = os.stat(p)
            sig.append([kit_rel(p), int(st.st_mtime), st.st_size])
        except OSError:
            sig.append([p and kit_rel(p), 0, 0])
    return sig


def personas_for(room_id, text):
    if room_id in PERSONAS:
        return PERSONAS[room_id]
    text = text.lower()
    return [pid for pid, words in KEYWORDS.items() if any(w in text for w in words)][:4]


def base_entry(path):
    info = scan_template(path)
    rid = info["file_id"]
    themes = []
    for name, colors in info["themes"].items():
        preview = find_preview(rid, name, info["default_theme"])
        themes.append({
            "id": name, "label": label(name), "default": name == info["default_theme"],
            "colors": {k: colors.get(k) for k in ("background", "wall", "floor", "wood", "main", "accent_1",
                                                  "accent_2", "accent_3", "cream", "dark") if colors.get(k)},
            "preview": kit_rel(preview) if preview else "", "thumb": "",
        })
    themes.sort(key=lambda t: (not t["default"],))
    slots = []
    for s in info["slots"]:
        words = SLOT_WORDS.get(s["name"], (label(s["name"]), ""))
        slots.append(dict(s, label=words[0], hint=words[1], where=KIND_WORDS.get(s["kind"], "")))
    blend = blend_for(rid)
    return {
        "id": rid, "name": DISPLAY_NAMES.get(rid) or info["doc_title"] or label(rid),
        "blurb": BLURBS.get(rid) or info["doc_blurb"],
        "themed": rid not in ("dev_office", "streamer_den", "living_lounge", "cozy_cafe", "cozy_bedroom",
                              "academia_library", "design_studio", "music_studio", "potion_shop", "plant_shop"),
        "default_theme": info["default_theme"], "themes": themes, "slots": slots,
        "personas": personas_for(rid, " ".join([rid, info["doc_title"], info["doc_blurb"]])),
        "name_sign": None, "role_sign": None, "hooks": None, "source": "template",
        "blend": kit_rel(blend) if blend else "",
        "sig": signature(path, blend) if blend else signature(path),
        "preview": next((t["preview"] for t in themes if t["preview"]), ""), "thumb": "",
    }


# ===================================================================== Blender pass
def bpy_extract(blend_path):
    """Open one room .blend and read slots, hooks and the sign size. Runs inside Blender."""
    bpy.ops.wm.open_mainfile(filepath=blend_path)
    scene = bpy.context.scene
    out = {"slots": [], "hooks": {"pictures": 0, "links": [], "text": []}}
    for o in scene.objects:
        if o.name.startswith("SLOT_") and "kit_slot" in o:
            size = list(o.get("kit_size", [0, 0, 0]))
            out["slots"].append({"name": o["kit_slot"], "kind": o.get("kit_kind", "floor"),
                                 "shape": o.get("kit_shape", "box"), "size": [round(float(v), 3) for v in size]})
        hook = o.get("kit_hook")
        if hook in ("screen", "frame", "poster", "canvas", "board"):
            out["hooks"]["pictures"] += 1
        elif hook:
            out["hooks"]["text"].append(hook)
        if o.get("kit_link"):
            out["hooks"]["links"].append(o["kit_link"])
        if hook in ("name", "role") and o.type == "FONT" and o.get("kit_hook_index", 1) == 1:
            o.scale = (1, 1, 1)
            o.data.body = SAMPLE_TEXT
            bpy.context.view_layer.update()
            per_char = o.dimensions.x / len(SAMPLE_TEXT)
            width = float(o.get("kit_max_width", 1.0))
            if per_char > 0:
                fit = int(width / per_char)
                out[f"{hook}_sign"] = {"fit": max(fit, 4), "max": max(int(fit / 0.6), 6),
                                       "width_m": round(width, 3), "letter_m": round(float(o.data.size), 3)}
    out["hooks"]["links"] = sorted(set(out["hooks"]["links"]))
    out["hooks"]["text"] = sorted(set(out["hooks"]["text"]))
    out["theme"] = scene.get("kit_theme", "")
    return out


def bpy_thumb(src, dst, width=960):
    """Scale a preview PNG down to a small JPEG for the room gallery."""
    img = bpy.data.images.load(src, check_existing=False)
    w, h = img.size
    if w > width:
        img.scale(width, max(1, int(h * width / w)))
    img.filepath_raw = dst
    img.file_format = "JPEG"
    try:
        bpy.context.scene.render.image_settings.quality = 82
    except Exception:
        pass
    img.save()
    bpy.data.images.remove(img)


def bpy_pass(jobs):
    """jobs = {"blends": {room: path}, "thumbs": [[src, dst], ...]} -> results dict."""
    results = {"rooms": {}, "thumbs": []}
    for src, dst in jobs.get("thumbs", []):
        try:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            bpy_thumb(src, dst)
            results["thumbs"].append(dst)
        except Exception as err:                                      # a thumbnail is nice to have, never fatal
            log(f"thumbnail skipped for {os.path.basename(src)}: {err}")
    for room, path in jobs.get("blends", {}).items():
        log(f"reading {room}")
        try:
            results["rooms"][room] = bpy_extract(path)
        except Exception as err:
            log(f"could not read {room}: {err}")
    return results


# ===================================================================== helpers for the plain-Python side
def find_blender(explicit=""):
    for cand in (explicit, os.environ.get("BLENDER", ""), shutil.which("blender") or "",
                 "/Applications/Blender.app/Contents/MacOS/Blender", "/opt/homebrew/bin/blender"):
        if cand and os.path.isfile(cand):
            return cand
    return ""


def build_missing_room(blender, template, room_id):
    """Build a room that has no .blend yet into tools/studio/cache/<room>/ (never templates/output)."""
    folder = os.path.join(CACHE, room_id)
    os.makedirs(folder, exist_ok=True)
    copy = os.path.join(folder, os.path.basename(template))
    shutil.copyfile(template, copy)
    env = dict(os.environ, ROOMKIT_BUILD_ONLY="1")
    log(f"building {room_id} once so Studio can read its slots (about 10-40 s)")
    proc = subprocess.run([blender, "-b", "--factory-startup", "-P", copy], env=env,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, errors="replace")
    blend = os.path.join(folder, "output", f"{room_id}.blend")
    if proc.returncode != 0 or not os.path.isfile(blend):
        log(f"could not build {room_id} (Studio will use the slots from its template code)")
        return ""
    return blend


def run_bpy_pass(blender, jobs):
    tmp = tempfile.mkdtemp(prefix="roomkit_manifest_")
    jin, jout = os.path.join(tmp, "in.json"), os.path.join(tmp, "out.json")
    with open(jin, "w", encoding="utf-8") as f:
        json.dump(jobs, f)
    cmd = [blender, "-b", "--factory-startup", "-P", os.path.abspath(__file__), "--", "--bpy-pass", jin, jout]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, errors="replace")
    for line in proc.stdout:
        if line.startswith("[manifest]"):
            print(line.rstrip(), flush=True)
    proc.wait()
    try:
        with open(jout, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        log("Blender pass gave no result; keeping the quick scan")
        return {"rooms": {}, "thumbs": []}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ===================================================================== main
def build_manifest(args, in_blender=False):
    old = {}
    if os.path.isfile(args.out) and not args.force:
        try:
            with open(args.out, encoding="utf-8") as f:
                prev = json.load(f)
            if prev.get("version") == MANIFEST_VERSION:
                old = {r["id"]: r for r in prev.get("rooms", [])}
        except (OSError, ValueError):
            old = {}
    templates = sorted(f for f in os.listdir(TEMPLATES) if f.endswith(".py") and not f.startswith("_"))
    rooms, need_blend, thumbs = [], {}, []
    blender = args.blender if in_blender else ("" if args.quick else find_blender(args.blender))
    for fname in templates:
        path = os.path.join(TEMPLATES, fname)
        try:
            entry = base_entry(path)
        except (SyntaxError, ValueError, OSError) as err:
            log(f"skipped {fname}: {err}")
            continue
        rid = entry["id"]
        prev = old.get(rid)
        if not entry["blend"] and args.build_missing and blender:
            built = build_missing_room(blender, path, rid)
            if built:
                entry["blend"], entry["sig"] = kit_rel(built), signature(path, built)
        if prev and prev.get("sig") == entry["sig"] and prev.get("source") == "blend":
            for key in ("slots", "name_sign", "role_sign", "hooks", "source"):    # nothing changed: reuse
                entry[key] = prev.get(key)
        elif entry["blend"] and (blender or in_blender):
            need_blend[rid] = os.path.join(KIT, entry["blend"])
        for t in entry["themes"]:                                  # thumbnails, made only when missing/stale
            if not t["preview"]:
                continue
            src = os.path.join(KIT, t["preview"])
            dst = os.path.join(THUMBS, os.path.splitext(os.path.basename(src))[0] + ".jpg")
            if os.path.isfile(dst) and os.path.getmtime(dst) >= os.path.getmtime(src):
                t["thumb"] = kit_rel(dst)
            elif blender or in_blender:
                thumbs.append([src, dst])
                t["thumb"] = kit_rel(dst)
        rooms.append(entry)

    if need_blend or thumbs:
        jobs = {"blends": need_blend, "thumbs": thumbs}
        log(f"asking Blender about {len(need_blend)} room(s), {len(thumbs)} thumbnail(s)")
        results = bpy_pass(jobs) if in_blender else run_bpy_pass(blender, jobs)
        made = set(results.get("thumbs", []))
        for entry in rooms:
            got = results.get("rooms", {}).get(entry["id"])
            if got and got["slots"]:
                words = {s["name"]: s for s in entry["slots"]}
                entry["slots"] = [dict(s, label=SLOT_WORDS.get(s["name"], (label(s["name"]), ""))[0],
                                       hint=SLOT_WORDS.get(s["name"], ("", ""))[1],
                                       where=KIND_WORDS.get(s["kind"], ""))
                                  for s in sorted(got["slots"], key=lambda s: list(words).index(s["name"])
                                                  if s["name"] in words else 99)]
                entry["name_sign"], entry["role_sign"] = got.get("name_sign"), got.get("role_sign")
                entry["hooks"], entry["source"] = got["hooks"], "blend"
            for t in entry["themes"]:
                if t["thumb"] and os.path.join(KIT, t["thumb"]) not in made and not os.path.isfile(os.path.join(KIT, t["thumb"])):
                    t["thumb"] = ""
    for entry in rooms:
        entry["thumb"] = next((t["thumb"] for t in entry["themes"] if t["thumb"]), "")
    manifest = {"version": MANIFEST_VERSION, "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "rooms": sorted(rooms, key=lambda r: (r["themed"], r["name"]))}
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    tmp = args.out + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1, ensure_ascii=False)
    os.replace(tmp, args.out)
    exact = sum(1 for r in rooms if r["source"] == "blend")
    log(f"wrote {kit_rel(args.out)}: {len(rooms)} rooms ({exact} read from Blender)")
    return manifest


def main():
    argv = sys.argv[sys.argv.index("--") + 1:] if (bpy and "--" in sys.argv) else (sys.argv[1:] if not bpy else [])
    if len(argv) >= 3 and argv[0] == "--bpy-pass":                 # internal: called by run_bpy_pass()
        with open(argv[1], encoding="utf-8") as f:
            jobs = json.load(f)
        results = bpy_pass(jobs)
        with open(argv[2], "w", encoding="utf-8") as f:
            json.dump(results, f)
        return
    p = argparse.ArgumentParser(prog="make_manifest.py", description="Write the room catalogue for RoomKit Studio.")
    p.add_argument("--blender", default="")
    p.add_argument("--quick", action="store_true")
    p.add_argument("--build-missing", action="store_true")
    p.add_argument("--force", action="store_true")
    p.add_argument("--out", default=DEFAULT_OUT)
    args = p.parse_args(argv)
    if bpy and not args.blender:
        args.blender = bpy.app.binary_path
    build_manifest(args, in_blender=bool(bpy))


if __name__ == "__main__":
    main()
