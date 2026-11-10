"""
3D ROOM PORTFOLIO KIT  -  ADD YOUR OWN FURNITURE
================================================
Puts a piece of furniture into a room made with one of the templates.

  * Have a 3D model (.glb / .gltf / .obj / .fbx / .stl), e.g. from Meshy, Tripo, Rodin, Hunyuan3D?
      -> it is imported, scaled to fit the slot, placed, and recoloured to match the room.
  * Only have a photo (.jpg / .png / .webp / iPhone .heic)?
      -> add --ai auto and an online AI service turns it into a real 3D model (see photo_to_3d.py), or
      -> without --ai, a simple version is built from basic shapes, using the photo's proportions and colours.

HOW TO RUN (command line, no Blender UI needed):
  blender -b output/cozy_bedroom.blend -P add_furniture.py -- --slot chair --model my_chair.glb
  blender -b output/cozy_bedroom.blend -P add_furniture.py -- --slot chair --photo my_chair.jpg
  blender -b output/cozy_bedroom.blend -P add_furniture.py -- --slot chair --photo my_chair.jpg --ai auto
  blender -b output/cozy_bedroom.blend -P add_furniture.py -- --list-slots
Options:
  --slot NAME        any slot in the room, e.g. desk, chair, sofa, counter, shelf, plant, pet
                     (run with a wrong name to see the list for your room)
  --model FILE       3D model to import
  --photo FILE       photo (used when there is no model; for wall_art the photo becomes the picture)
  --ai PROVIDER      with --photo: make a real 3D model from the photo with AI first
                     auto | meshy | fal | hf | sample  (if it can't, the simple blocky version is built instead)
  --quality Q        for --ai: draft (cheaper, fewer polygons) | standard (default)
  --yes              for --ai: allow a paid AI service to spend money without asking
  --timeout SECONDS  for --ai: how long to wait for the AI model (default 600)
  --list-slots       print this room's slots as JSON ([{slot, kind, shape, size}]) and stop
  --scale FACTOR     make the piece a little smaller or bigger after fitting (0.5 - 1.5, default 1)
  --shape NAME       for --photo: chair, sofa, stool, table, counter, bed, shelf, cabinet, monitor, lamp,
                     plant, rug, frame, pet, box (default: the slot's own shape)
  --colors MODE      match (default: keep detail, pull colours toward the room palette)
                     palette (flat room colour, cleanest toy look) | original (leave as is)
  --turn DEGREES     rotate the model if it faces the wrong way (90, 180, 270)
  --fit MODE         inside (default, keeps proportions) | stretch (fill the slot exactly)
  --no-render        just save the .blend
  --save FILE        save to another .blend instead of overwriting the room

OR inside Blender: open the room .blend, Scripting tab > Open > add_furniture.py,
fill in the SETTINGS below, and press Run Script.
"""

# =====================================================================
#  SETTINGS  (only used when you press Run Script inside Blender)
# =====================================================================
SLOT = "chair"
MODEL_FILE = ""          # e.g. "/Users/me/Downloads/chair.glb"
PHOTO_FILE = ""          # e.g. "/Users/me/Downloads/chair.jpg"
SHAPE = ""               # "" = guess from the slot name
COLORS_MODE = "match"    # match / palette / original
TURN = 0
FIT = "inside"
AI = ""                  # "" = no AI; or auto / meshy / fal / hf / sample (needs PHOTO_FILE)
SCALE = 1.0              # 0.5 - 1.5: fine-tune the size after it is fitted to the slot
# =====================================================================

import argparse
import json
import math
import os
import subprocess
import shutil
import sys

import bmesh
import bpy
import numpy as np
bpy.context.preferences.filepaths.save_version = 0      # no .blend1 backup files
from mathutils import Matrix, Vector

R = math.radians


# --------------------------------------------------------------------- arguments
def read_args():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else None
    if argv is None:                                   # Run Script inside Blender
        return argparse.Namespace(slot=SLOT, model=MODEL_FILE, photo=PHOTO_FILE, shape=SHAPE, colors=COLORS_MODE,
                                  turn=TURN, fit=FIT, no_render=True, save="", ai=AI, quality="standard", yes=False,
                                  timeout=600, list_slots=False, scale=SCALE)
    p = argparse.ArgumentParser(prog="add_furniture.py")
    p.add_argument("--slot", default="")
    p.add_argument("--model", default="")
    p.add_argument("--photo", default="")
    p.add_argument("--shape", default="")
    p.add_argument("--colors", default="match", choices=["match", "palette", "original"])
    p.add_argument("--turn", type=float, default=0)
    p.add_argument("--fit", default="inside", choices=["inside", "stretch"])
    p.add_argument("--no-render", action="store_true")
    p.add_argument("--save", default="")
    p.add_argument("--ai", default="", choices=["", "auto", "meshy", "fal", "hf", "sample"])
    p.add_argument("--quality", default="standard", choices=["draft", "standard"])
    p.add_argument("--yes", action="store_true")
    p.add_argument("--timeout", type=float, default=600)
    p.add_argument("--list-slots", action="store_true")
    p.add_argument("--scale", type=float, default=1.0)
    return p.parse_args(argv)


args = read_args()
scene = bpy.context.scene
if "kit_style" not in scene:
    sys.exit("[RoomKit] This .blend was not made by a Room Kit template. Open/run a template first.")

SHAPE_FROM_SLOT = {"bed": "bed", "side_table": "cabinet", "lamp": "lamp", "desk": "table", "chair": "chair",
                   "shelf": "shelf", "plant": "plant", "rug": "rug", "wall_art": "frame"}
ALL_SLOTS = sorted((o for o in bpy.data.objects if o.name.startswith("SLOT_") and o.get("kit_slot")),
                   key=lambda o: o["kit_slot"])
if args.list_slots:                                     # for the Studio app and the curious: what can go where
    listing = [{"slot": o["kit_slot"], "kind": o.get("kit_kind", "floor"),
                "shape": o.get("kit_shape") or SHAPE_FROM_SLOT.get(o["kit_slot"], "box"),
                "size": [round(float(v), 3) for v in (o.get("kit_size") or [2 * s for s in o.scale])]}
               for o in ALL_SLOTS]
    print(json.dumps(listing), flush=True)
    sys.exit(0)
if not args.slot:
    sys.exit("[RoomKit] Give a --slot (run with --list-slots to see this room's slots).")
if not (args.model or args.photo):
    sys.exit("[RoomKit] Give a --model or a --photo.")
if args.ai and not args.photo:
    sys.exit("[RoomKit] --ai needs a --photo of the piece, e.g. --photo my_chair.jpg --ai auto")
if args.ai and args.model:
    sys.exit("[RoomKit] Use either --model (you already have a 3D file) or --photo with --ai, not both.")
if not 0.5 <= args.scale <= 1.5:
    sys.exit("[RoomKit] --scale must be between 0.5 and 1.5 (1 = fits the slot exactly).")

slot_name = args.slot.replace("SLOT_", "")
slot = bpy.data.objects.get(f"SLOT_{slot_name}")
if slot is None:
    names = [o["kit_slot"] for o in ALL_SLOTS]
    sys.exit(f"[RoomKit] No slot '{slot_name}'. This room has: {', '.join(names)}")

TOOLS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS)
try:
    import photo_to_3d                                  # photo checks + HEIC conversion (standard library only)
except ImportError:
    photo_to_3d = None


def python_for_tools():
    """Blender's own Python (sys.executable) runs the AI step; fall back to python3 on the PATH."""
    exe = sys.executable or ""
    if "python" in os.path.basename(exe).lower() and os.path.isfile(exe):
        return exe
    return shutil.which("python3") or shutil.which("python") or exe


def make_ai_model(photo, slot_name):
    """Runs photo_to_3d.py in its own process (a slow service never freezes Blender).
    Returns the .glb path, or "" when no AI model could be made (then we build the blocky version)."""
    home = photo_to_3d.HOME if photo_to_3d else os.path.expanduser("~/.roomkit")
    stem = os.path.splitext(os.path.basename(photo))[0]
    out = os.path.join(home, "models", f"{stem}_{args.ai}_{args.quality}.glb")
    cmd = [python_for_tools(), os.path.join(TOOLS, "photo_to_3d.py"), "--photo", photo, "--out", out,
           "--provider", args.ai, "--quality", args.quality, "--timeout", str(args.timeout)]
    if args.yes:
        cmd.append("--yes")
    print(f"[RoomKit] making a 3D model of your photo with AI ({args.ai}) for the {slot_name} slot...", flush=True)
    glb = ""
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
        for line in proc.stdout:                        # show progress as it happens
            line = line.rstrip()
            print(line, flush=True)
            if line.startswith("GLB: "):
                glb = line[5:].strip()
        code = proc.wait()
    except OSError as err:
        print(f"[RoomKit] could not start the AI step ({err})")
        code = 3
    if code == 0 and glb and os.path.isfile(glb):
        return glb
    if code == 2:
        sys.exit("[RoomKit] The photo can't be used (see the message above). Nothing was changed.")
    why = "it took too long" if code == 4 else "no AI service was available or it failed"
    print(f"[RoomKit] No AI model this time ({why}). Building the free blocky version from your photo instead.",
          flush=True)
    if code == 4:
        print("[RoomKit] Tip: run the same command again later - the AI job keeps running online and is picked up "
              "without paying twice.", flush=True)
    return ""


ai_used = ""
if args.ai:
    if (args.shape or slot.get("kit_shape")) in ("frame", "rug"):
        print(f"[RoomKit] note: in the {slot_name} slot the photo is used flat, so --ai is skipped")
    else:
        found = make_ai_model(os.path.abspath(os.path.expanduser(args.photo)), slot_name)
        if found:
            args.model, ai_used = found, args.ai

PALETTE = json.loads(scene["kit_palette"])
FINISH = json.loads(scene.get("kit_material_finish", '{"roughness": 0.65, "saturation": 0.75}'))
SKIP_KEYS = {"background", "wall", "wall_trim", "floor", "sky"}   # don't paint furniture the colour of the walls
FURNITURE_KEYS = set(json.loads(scene["kit_furniture_colors"])) if "kit_furniture_colors" in scene else None


# --------------------------------------------------------------------- colour helpers
def hex_to_srgb(h):
    h = h.lstrip("#")
    return np.array([int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)])


def to_linear(c):
    c = np.asarray(c, dtype=float)
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def to_srgb(c):
    c = np.clip(np.asarray(c, dtype=float), 0, 1)
    return np.where(c <= 0.0031308, c * 12.92, 1.055 * c ** (1 / 2.4) - 0.055)


def nearest_palette(srgb):
    """Closest room colour (weighted RGB distance) -> (key, srgb)."""
    best = None
    for key, hx in PALETTE.items():
        if key in SKIP_KEYS or (FURNITURE_KEYS and key not in FURNITURE_KEYS):
            continue
        p = hex_to_srgb(hx)
        d = np.sum(((p - srgb) * (0.3, 0.59, 0.11)) ** 2)
        if best is None or d < best[0]:
            best = (d, key, p)
    return best[1], best[2]


def styled(srgb, amount=0.45):
    """Pull a colour toward the room palette and soften its saturation (the 'match' look)."""
    _, target = nearest_palette(srgb)
    c = srgb * (1 - amount) + target * amount
    grey = c.mean()
    return grey + (c - grey) * FINISH.get("saturation", 0.75)


def image_pixels(img, max_side=160):
    """Image -> (h, w, 4) float array in sRGB, downsampled."""
    w, h = img.size
    px = np.empty(w * h * 4, dtype=np.float32)
    img.pixels.foreach_get(px)
    px = px.reshape(h, w, 4)
    step = max(1, max(w, h) // max_side)
    px = px[::step, ::step].copy()
    if img.colorspace_settings.name.lower() in ("linear", "linear rec.709", "non-color"):
        px[..., :3] = to_srgb(px[..., :3])
    return px


def principled(m):
    return next((n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED"), None) if m and m.node_tree else None


def new_material(name, srgb, rough=None, image=None):
    m = bpy.data.materials.new(name)
    if bpy.app.version < (5, 0, 0):
        m.use_nodes = True
    b = principled(m)
    rgba = (*to_linear(srgb), 1.0)
    b.inputs["Base Color"].default_value = rgba
    b.inputs["Roughness"].default_value = FINISH.get("roughness", 0.65) if rough is None else rough
    if image is not None:
        tex = m.node_tree.nodes.new("ShaderNodeTexImage")
        tex.image = image
        m.node_tree.links.new(tex.outputs["Color"], b.inputs["Base Color"])
    m.diffuse_color = rgba
    return m


# --------------------------------------------------------------------- remove what's in the slot now
def remove_tree(o):
    for c in list(o.children):
        remove_tree(c)
    bpy.data.objects.remove(o, do_unlink=True)


kept_lights, kept_links, lost_hooks = [], [], []        # accent lights stay; links move to the new piece
for o in [o for o in bpy.data.objects if o.get("kit_slot") == slot_name and o.get("kit_role") in ("placeholder", "furniture")]:
    if o.name not in bpy.data.objects:
        continue
    for c in [o] + list(o.children_recursive):
        if c.get("kit_link"):
            kept_links.append(c["kit_link"])
        if c.get("kit_hook"):
            lost_hooks.append(c.name)
    for c in o.children_recursive:
        if c.type == "LIGHT":
            mw = c.matrix_world.copy()
            c.parent = None
            c.matrix_world = mw
            kept_lights.append(c)
    remove_tree(o)

furn_coll = bpy.data.collections.get("Furniture") or scene.collection
w, d, h = (2 * s for s in slot.scale)                # slot box size (the slot empty is scaled to half its size)
slot_rot = slot.matrix_world.to_euler().z
bottom_pose = Matrix.Translation(slot.matrix_world.translation - Vector((0, 0, h / 2))) @ Matrix.Rotation(slot_rot, 4, "Z")

root = bpy.data.objects.new(f"FURN_{slot_name}", None)
root.empty_display_size = 0.2
root["kit_slot"], root["kit_role"] = slot_name, "furniture"
furn_coll.objects.link(root)
if kept_links:
    root["kit_link"] = kept_links[0]                   # e.g. your new shelf still opens GitHub on the site
if lost_hooks:
    print(f"[RoomKit] note: the old {slot_name} carried portfolio spots that are now gone: {', '.join(lost_hooks)}")


# =====================================================================
#  A) IMPORT A 3D MODEL
# =====================================================================
def import_model(path):
    path = os.path.abspath(os.path.expanduser(path))
    if not os.path.isfile(path):
        sys.exit(f"[RoomKit] Model not found: {path}")
    before = set(bpy.data.objects)
    ext = os.path.splitext(path)[1].lower()
    if ext in (".glb", ".gltf"):
        bpy.ops.import_scene.gltf(filepath=path)
    elif ext == ".obj":
        bpy.ops.wm.obj_import(filepath=path, forward_axis="NEGATIVE_Z", up_axis="Y")
    elif ext == ".fbx":
        bpy.ops.import_scene.fbx(filepath=path)
    elif ext == ".stl":
        bpy.ops.wm.stl_import(filepath=path)
    else:
        sys.exit(f"[RoomKit] Unsupported model type {ext}. Use .glb, .gltf, .obj, .fbx or .stl")
    new = [o for o in bpy.data.objects if o not in before]
    for o in new:                                      # move into the Furniture collection
        for c in list(o.users_collection):
            c.objects.unlink(o)
        furn_coll.objects.link(o)
    for o in new:
        if o.parent is None:
            mw = o.matrix_world.copy()
            o.parent = root
            o.matrix_world = mw
        o["kit_slot"] = slot_name
    meshes = [o for o in new if o.type == "MESH"]
    if not meshes:
        sys.exit("[RoomKit] The file has no mesh in it.")
    faces = sum(len(o.data.polygons) for o in meshes)
    if faces > 80000:                                  # AI models are often huge; keep the scene light
        for o in meshes:
            dec = o.modifiers.new("RoomKit_Decimate", "DECIMATE")
            dec.ratio = max(0.05, 80000 / faces)
        print(f"[RoomKit] model had {faces} faces, decimated to about 80k")
    return meshes


def restyle_model_materials(meshes, mode):
    if mode == "original":
        return
    done = {}
    for o in meshes:
        for i, ms in enumerate(o.material_slots):
            m = ms.material
            if m is None or m.name in done:
                if m is not None:
                    ms.material = done[m.name]
                continue
            b = principled(m)
            avg, tex_node = np.array([0.8, 0.8, 0.8]), None
            if b is not None:
                link = next((l for l in m.node_tree.links if l.to_socket == b.inputs["Base Color"]), None)
                if link and link.from_node.type == "TEX_IMAGE" and link.from_node.image:
                    tex_node = link.from_node
                    px = image_pixels(tex_node.image)
                    keep = px[..., 3] > 0.5
                    avg = px[..., :3][keep].mean(axis=0) if keep.any() else px[..., :3].reshape(-1, 3).mean(axis=0)
                else:
                    avg = to_srgb(b.inputs["Base Color"].default_value[:3])
            if mode == "palette" or b is None or tex_node is None:
                color = nearest_palette(avg)[1] if mode == "palette" else styled(avg)
                new = new_material(f"FURN_{slot_name}_{m.name}", color)
            else:                                       # match: keep texture, soften + pull toward palette
                new = m.copy()
                new.name = f"FURN_{slot_name}_{m.name}"
                nt, b2 = new.node_tree, principled(new)
                tex = next(l.from_node for l in nt.links if l.to_socket == b2.inputs["Base Color"])
                hs = nt.nodes.new("ShaderNodeHueSaturation")
                hs.inputs["Saturation"].default_value = FINISH.get("saturation", 0.75)
                mix = nt.nodes.new("ShaderNodeMix")
                mix.data_type = "RGBA"
                fac = next(s for s in mix.inputs if s.type == "VALUE" and s.enabled)
                a_in, b_in = [s for s in mix.inputs if s.type == "RGBA" and s.enabled][:2]
                fac.default_value = 0.4
                b_in.default_value = (*to_linear(nearest_palette(avg)[1]), 1)
                nt.links.new(tex.outputs["Color"], hs.inputs["Color"])
                nt.links.new(hs.outputs["Color"], a_in)
                nt.links.new(next(s for s in mix.outputs if s.type == "RGBA" and s.enabled), b2.inputs["Base Color"])
                b2.inputs["Roughness"].default_value = FINISH.get("roughness", 0.65)
                for name in ("Metallic", "Specular IOR Level"):
                    if name in b2.inputs and not b2.inputs[name].is_linked:
                        b2.inputs[name].default_value = 0.0 if name == "Metallic" else 0.3
                new.diffuse_color = (*to_linear(styled(avg)), 1)
            done[m.name] = new
            ms.material = new


def fit_into_slot(meshes, turn_deg, fit):
    """Scale + place everything under root so it sits in the slot (front of model faces slot front)."""
    dg = bpy.context.evaluated_depsgraph_get()
    dg.update()
    turn = Matrix.Rotation(R(turn_deg), 4, "Z")
    pts = []
    for o in meshes:
        ev = o.evaluated_get(dg)
        mw = turn @ ev.matrix_world
        pts += [mw @ Vector(c) for c in ev.bound_box]
    lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    size = hi - lo
    size = Vector((max(size.x, 1e-4), max(size.y, 1e-4), max(size.z, 1e-4)))
    if fit == "stretch":
        scale = Matrix.Diagonal((w / size.x, d / size.y, h / size.z, 1))
    else:
        flat = slot.get("kit_kind") == "rug"         # rugs: fit the footprint, ignore height
        s = min(w / size.x, d / size.y) if flat else min(w / size.x, d / size.y, h / size.z)
        scale = Matrix.Scale(s, 4)
    base = Vector(((lo.x + hi.x) / 2, (lo.y + hi.y) / 2, lo.z))
    if slot.get("kit_kind") == "wall":                 # hang against the wall: back of model on the slot's back face
        base.y = hi.y
        bottom = bottom_pose @ Matrix.Translation((0, d / 2, 0))
    else:
        bottom = bottom_pose
    root.matrix_world = bottom @ scale @ Matrix.Translation(-base) @ turn


# =====================================================================
#  B) BUILD FROM A PHOTO (fallback when there is no 3D model)
# =====================================================================
def analyse_photo(path):
    """Returns (aspect = width/height of the object, [colours by area], image)."""
    path = os.path.abspath(os.path.expanduser(path))
    if not os.path.isfile(path):
        sys.exit(f"[RoomKit] Photo not found: {path}")
    if photo_to_3d is not None:                       # iPhone HEIC etc. -> JPEG that Blender can read
        try:
            path = photo_to_3d.prepare_photo(path, max_side=4096)[0]
        except photo_to_3d.Stop as err:
            sys.exit(f"[RoomKit] {err}")
    img = bpy.data.images.load(path, check_existing=True)
    px = image_pixels(img)
    rgb, alpha = px[..., :3], px[..., 3]
    if (alpha < 0.5).mean() > 0.05:                    # cut-out PNG: use transparency
        mask = alpha > 0.5
    else:                                              # plain background: compare with the border colour
        border = np.concatenate([rgb[0], rgb[-1], rgb[:, 0], rgb[:, -1]])
        bg = np.median(border, axis=0)
        mask = np.linalg.norm(rgb - bg, axis=-1) > 0.12
    if mask.sum() < 20:
        mask[:] = True
    ys, xs = np.nonzero(mask)
    aspect = (xs.max() - xs.min() + 1) / (ys.max() - ys.min() + 1)
    pix = rgb[mask].reshape(-1, 3)
    # small k-means for the 3 main colours
    rng = np.random.default_rng(1)
    centres = pix[rng.choice(len(pix), 3, replace=len(pix) < 3)]
    for _ in range(10):
        lab = np.argmin(((pix[:, None] - centres[None]) ** 2).sum(-1), axis=1)
        centres = np.array([pix[lab == k].mean(0) if (lab == k).any() else centres[k] for k in range(3)])
    order = np.argsort([-(lab == k).sum() for k in range(3)])
    return float(aspect), [centres[k] for k in order], img


def _part(name, bm, loc, material, bevel, rot=(0, 0, 0)):
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    o = bpy.data.objects.new(name, me)
    o.location, o.rotation_euler = loc, rot
    o.data.materials.append(material)
    if bevel:
        mod = o.modifiers.new("Bevel", "BEVEL")
        mod.width, mod.segments, mod.limit_method = bevel, 4, "ANGLE"
        try:
            mod.harden_normals = True
        except AttributeError:
            pass
    o.data.polygons.foreach_set("use_smooth", [True] * len(o.data.polygons))
    furn_coll.objects.link(o)
    o.parent = root
    o["kit_slot"] = slot_name
    return o


def box(name, size, loc, material, bevel=0.03, rot=(0, 0, 0)):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=Vector(size), verts=bm.verts)
    return _part(name, bm, loc, material, min(bevel, min(size) * 0.45), rot)


def cyl(name, r, height, loc, material, r2=None, segs=32, bevel=0.01):
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=segs, radius1=r, radius2=r if r2 is None else r2, depth=height)
    return _part(name, bm, loc, material, bevel)


def ball(name, r, loc, material, scale=(1, 1, 1)):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=24, v_segments=14, radius=r)
    o = _part(name, bm, loc, material, 0)
    o.scale = scale
    return o


def build_from_photo(shape, aspect, colors, img, mode):
    """Builds in the slot's local frame (x = width, y = depth, front = -y, z = up), then places root."""
    if mode == "original":
        cols = colors
    elif mode == "palette":
        cols = [nearest_palette(c)[1] for c in colors]
    else:
        cols = [styled(c) for c in colors]
    main, second, third = (new_material(f"FURN_{slot_name}_{i}", c) for i, c in enumerate(cols))
    # Object size: use the full slot height, and the photo's width/height ratio for the width.
    hh = h
    ww = hh * aspect
    if ww > w:
        ww, hh = w, w / aspect
    if shape in ("rug", "frame", "table", "bed", "sofa", "shelf", "cabinet", "counter"):
        ww, hh = w, h                                  # wide furniture fills the slot; photos taken at an angle mislead
    dd = d * (ww / w) if shape not in ("bed", "rug", "frame", "shelf", "cabinet", "counter") else d
    if shape == "chair" or shape == "sofa":
        seat = hh * 0.5
        leg = seat - 0.12
        for sx in (-1, 1):
            for sy in (-1, 1):
                cyl("Leg", 0.025, leg, (sx * (ww / 2 - 0.06), sy * (dd / 2 - 0.06), leg / 2), third)
        box("Seat", (ww, dd, 0.14), (0, 0, seat - 0.05), main, 0.05)
        box("Back", (ww, 0.14, hh - seat + 0.04), (0, dd / 2 - 0.07, (seat + hh) / 2), main, 0.06)
        if shape == "sofa" or aspect > 1.1:
            for sx in (-1, 1):
                box("Arm", (0.14, dd, hh * 0.25), (sx * (ww / 2 - 0.07), 0, seat + hh * 0.08), main, 0.06)
        box("Cushion", (ww * 0.5, 0.1, hh * 0.22), (0, dd / 2 - 0.18, seat + hh * 0.17), second, 0.05)
    elif shape == "stool":
        cyl("Seat", min(ww, dd) * 0.5, 0.07, (0, 0, hh - 0.035), main)
        for k in range(3):
            a = k * 2.094
            leg = cyl("Leg", 0.018, hh - 0.07, (math.cos(a) * ww * 0.3, math.sin(a) * dd * 0.3, (hh - 0.07) / 2), third)
            leg.rotation_euler = (math.sin(a) * R(6), -math.cos(a) * R(6), 0)
    elif shape == "counter":
        box("Body", (ww, dd, hh - 0.05), (0, 0, (hh - 0.05) / 2), main, 0.03)
        box("Top", (ww + 0.04, dd + 0.04, 0.05), (0, 0, hh - 0.025), second, 0.02)
        box("Kick", (ww - 0.04, 0.02, 0.08), (0, -dd / 2 + 0.03, 0.04), third, 0.01)
    elif shape == "monitor":
        box("Foot", (ww * 0.35, dd * 0.6, 0.02), (0, 0, 0.01), third, 0.008)
        box("Neck", (0.04, 0.03, hh * 0.35), (0, 0.02, hh * 0.18), third, 0.008)
        box("Screen", (ww, 0.035, hh * 0.62), (0, 0, hh * 0.65), main, 0.012)
    elif shape == "pet":
        r = min(ww, dd) * 0.36
        ball("Body", r, (0, 0.02, r * 0.62), main, scale=(1.2, 0.95, 0.62))
        ball("Head", r * 0.55, (-ww * 0.2, -dd * 0.16, r * 0.62 + 0.05), main)
        for sx in (-1, 1):
            cyl("Ear", r * 0.18, r * 0.35, (-ww * 0.2 + sx * r * 0.25, -dd * 0.16, r * 0.62 + 0.05 + r * 0.55), second,
                r2=0.003, segs=12, bevel=0)
        ball("Tail", r * 0.25, (ww * 0.1, -dd * 0.24, r * 0.3), second, scale=(2.6, 0.7, 0.6))
    elif shape == "table":
        box("Top", (ww, dd, 0.05), (0, 0, hh - 0.025), main, 0.02)
        for sx in (-1, 1):
            for sy in (-1, 1):
                cyl("Leg", 0.025, hh - 0.05, (sx * (ww / 2 - 0.06), sy * (dd / 2 - 0.06), (hh - 0.05) / 2), second)
    elif shape == "bed":
        box("Frame", (ww, dd, hh * 0.25), (0, 0, hh * 0.15), main, 0.05)
        box("Mattress", (ww - 0.06, dd - 0.1, hh * 0.2), (0, -0.04, hh * 0.36), second, 0.07)
        box("Blanket", (ww + 0.03, dd * 0.6, hh * 0.1), (0, -dd * 0.2, hh * 0.47), third, 0.05)
        box("Headboard", (ww, 0.1, hh), (0, dd / 2 - 0.05, hh / 2), main, 0.08)
    elif shape in ("shelf", "cabinet"):
        box("Body", (ww, dd, hh), (0, 0, hh / 2), main, 0.03)
        n = 4 if shape == "shelf" else 2
        for i in range(n):
            z = hh * (i + 0.5) / n
            box("Front", (ww - 0.08, 0.02, hh / n - 0.06), (0, -dd / 2, z), second if shape == "cabinet" else third, 0.01)
    elif shape == "lamp":
        cyl("Base", ww * 0.3, 0.04, (0, 0, 0.02), second)
        cyl("Stem", 0.015, hh * 0.6, (0, 0, hh * 0.3), third)
        cyl("Shade", ww * 0.5, hh * 0.4, (0, 0, hh * 0.8), main, r2=ww * 0.3)
    elif shape == "plant":
        cyl("Pot", ww * 0.3, hh * 0.3, (0, 0, hh * 0.15), second, r2=ww * 0.38)
        for k in range(9):
            a = k * 2.4
            ball("Leaf", ww * 0.18, (math.cos(a) * ww * 0.15, math.sin(a) * ww * 0.15, hh * (0.45 + 0.055 * k)), main,
                 scale=(1.3, 0.8, 0.5)).rotation_euler = (R(20), 0, a)
    elif shape == "rug":
        o = cyl("Rug", 0.5, 0.02, (0, 0, 0.01), main, segs=48, bevel=0)
        o.scale = (ww, dd, 1)
        o2 = cyl("Rug_Inner", 0.5, 0.02, (0, 0, 0.012), second, segs=48, bevel=0)
        o2.scale = (ww * 0.75, dd * 0.7, 1)
    elif shape == "frame":                             # the photo itself becomes the picture
        ar = img.size[0] / max(1, img.size[1])
        fw, fh = (ww, ww / ar) if ww / ar <= hh else (hh * ar, hh)
        box("Frame", (fw, d, fh), (0, 0, fh / 2), new_material("FURN_frame", hex_to_srgb(PALETTE.get("wood", "#C8A27A"))), 0.012)
        bm = bmesh.new()
        bmesh.ops.create_grid(bm, x_segments=1, y_segments=1, size=0.5)
        uv = bm.loops.layers.uv.new()
        for f in bm.faces:
            for loop in f.loops:
                loop[uv].uv = (loop.vert.co.x + 0.5, loop.vert.co.y + 0.5)
        pic = _part("Picture", bm, (0, -d / 2 - 0.002, fh / 2), new_material("FURN_picture", (1, 1, 1), 0.8, img), 0,
                    rot=(R(90), 0, 0))
        pic.scale = (fw - 0.07, fh - 0.07, 1)
    else:                                              # generic rounded block
        box("Block", (ww, dd, hh), (0, 0, hh / 2), main, 0.05)
        box("Top", (ww + 0.02, dd + 0.02, 0.04), (0, 0, hh), second, 0.02)
    # Place: slot bottom-centre, slot rotation; wall pieces sit on the wall.
    root.matrix_world = bottom_pose


def fine_scale(factor):
    """--scale: shrink/grow the fitted piece around its foot (wall pieces: around the point on the wall)."""
    if abs(factor - 1) < 1e-6:
        return
    pivot = bottom_pose @ Matrix.Translation((0, d / 2, 0)) if slot.get("kit_kind") == "wall" else bottom_pose
    root.matrix_world = pivot @ Matrix.Scale(factor, 4) @ pivot.inverted() @ root.matrix_world
    print(f"[RoomKit] scaled to {factor:g}x the slot fit")


# =====================================================================
#  RUN
# =====================================================================
if args.model:
    meshes = import_model(args.model)
    restyle_model_materials(meshes, args.colors)
    fit_into_slot(meshes, args.turn, args.fit)
    root["kit_source"] = os.path.basename(args.photo if ai_used else args.model)
    if ai_used:
        root["kit_ai"] = ai_used                       # which AI service made it (for credits / licence notes)
        print(f"[RoomKit] placed the AI model of {os.path.basename(args.photo)} in SLOT_{slot_name}")
    else:
        print(f"[RoomKit] placed {args.model} in SLOT_{slot_name}")
else:
    shape = args.shape or slot.get("kit_shape") or SHAPE_FROM_SLOT.get(slot_name, "box")   # templates tag each slot with a shape
    aspect, colors, img = analyse_photo(args.photo)
    build_from_photo(shape, aspect, colors, img, args.colors)
    root["kit_source"] = os.path.basename(args.photo)
    hexes = ["#%02X%02X%02X" % tuple(int(v * 255) for v in c) for c in colors]
    print(f"[RoomKit] built a '{shape}' from the photo (width/height {aspect:.2f}, colours {', '.join(hexes)})")
fine_scale(args.scale)

# Keep the bedside lamp's light on top of whatever lamp is in the lamp slot.
lamp_light = bpy.data.objects.get("Light_Lamp")
if slot_name == "lamp" and lamp_light:
    lamp_light.location = slot.matrix_world.translation + Vector((0, 0, h * 0.3))
    for o in root.children_recursive:              # a closed lamp shade would otherwise block its own light
        if o.type == "MESH" and hasattr(o, "visible_shadow"):
            o.visible_shadow = False

if bpy.app.background:
    out = os.path.abspath(args.save) if args.save else bpy.data.filepath
    if args.photo and args.slot.replace("SLOT_", "") == "wall_art":
        bpy.ops.file.pack_all()                       # keep the picture inside the .blend
    bpy.ops.wm.save_as_mainfile(filepath=out)
    print(f"[RoomKit] saved {out}")
    if not args.no_render:
        folder = os.path.dirname(out)
        room = os.path.splitext(os.path.basename(out))[0]
        scene.render.filepath = os.path.join(folder, f"{room}.png")
        bpy.ops.render.render(write_still=True)
        print(f"[RoomKit] rendered {scene.render.filepath}")
else:
    print("[RoomKit] done - press F12 to render, File > Save to keep it")
