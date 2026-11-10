"""
3D ROOM PORTFOLIO KIT  -  INTERACTIVE 3D WEB EXPORT
===================================================
Turns a personalised room into a real 3D web page (Three.js) that visitors can turn, zoom and click:
  room3d.html     the 3D portfolio page. By default it is ONE self-contained file: the room, its lighting and
                  your project images are inside it, so double-clicking it works (it only needs internet for
                  the 3D engine, Three.js, from the jsDelivr CDN). Upload it anywhere as it is.
  3d/room.glb     the room geometry (compressed)                      } spare copies; room3d.html only
  3d/light.webp   the lighting, baked once with Cycles like the render } reads them with --separate-files

Normally you don't run this yourself - add --web to build_portfolio.py:
  blender -b -P tools/build_portfolio.py -- --profile profile.json --web

On its own (uses the room.blend that build_portfolio.py saved):
  blender -b portfolio_dev_office/room.blend -P tools/export_web.py
Options:
  --out FOLDER     where to write (default: the .blend's folder)
  --size N         lighting texture size in pixels (default 4096; 2048 for a quicker, softer bake)
  --samples N      bake quality (default 32; the bake is denoised afterwards)
  --fast           quick test: --size 2048 --samples 16
  --no-draco       uncompressed room.glb (bigger, but needs no decoder from the CDN)
  --separate-files room3d.html loads the files in 3d/ and img/ instead of carrying them inside
                   (smaller page for big rooms; then preview it through a web server:
                   cd portfolio_dev_office && python3 -m http.server 8000 -> http://localhost:8000/room3d.html)
"""

import argparse
import base64
import html
import json
import math
import os
import shutil
import sys
import tempfile
import time

import bmesh
import bpy
import numpy as np
bpy.context.preferences.filepaths.save_version = 0
from mathutils import Matrix, Vector

KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PICTURE_HOOKS = ("screen", "frame", "poster", "canvas", "board", "logo")
THREE = "0.169.0"                                   # pinned Three.js version (CDN)
SINGLE_FILE_BUDGET = 6.0                            # MB: warn when a self-contained room3d.html is bigger
MIME = {".glb": "model/gltf-binary", ".webp": "image/webp", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
        ".png": "image/png", ".gif": "image/gif"}


def log(msg):
    print(f"[RoomKit web] {msg}", flush=True)


def to_yup(v):
    """Blender is Z-up, glTF / Three.js are Y-up."""
    return [round(v.x, 5), round(v.z, 5), round(-v.y, 5)]


# ===================================================================== 1. geometry
def render_visible(o):
    if o.hide_render or o.type not in ("MESH", "FONT", "CURVE"):
        return False
    return not any(c.hide_render for c in o.users_collection)


def web_owner(o):
    """The nearest object (itself or a parent) that is clickable on the page."""
    while o is not None:
        if o.get("kit_web"):
            return o
        o = o.parent
    return None


def is_picture(o):
    return o.get("kit_hook") in PICTURE_HOOKS and o.get("kit_web") and o.type == "MESH"


def alpha_of(o):
    """Lowest material opacity on the object (glass, display cases); 1.0 = solid."""
    lowest = 1.0
    for slot in o.material_slots:
        m = slot.material
        if m and m.node_tree:
            b = next((n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED"), None)
            if b and "Alpha" in b.inputs and not b.inputs["Alpha"].is_linked:
                lowest = min(lowest, b.inputs["Alpha"].default_value)
    return round(lowest, 2)


VIS = ("visible_camera", "visible_diffuse", "visible_glossy", "visible_transmission", "visible_shadow")


def make_world_mesh(o, dg, name, nudge=0.0):
    """Evaluated copy (modifiers applied, text turned into mesh) with the transform baked in.
    nudge: push the surface out by a fraction of a millimetre. Touching, same-level surfaces of two objects
    (e.g. two wall trims) would otherwise shadow each other in the bake and flicker on the page."""
    ev = o.evaluated_get(dg)
    me = bpy.data.meshes.new_from_object(ev, preserve_all_data_layers=False, depsgraph=dg)
    me.transform(o.matrix_world)
    if o.matrix_world.determinant() < 0:
        me.flip_normals()
    if nudge and len(me.vertices):
        co, nor = np.empty(len(me.vertices) * 3), np.empty(len(me.vertices) * 3)
        me.vertices.foreach_get("co", co)
        me.vertex_normals.foreach_get("vector", nor) if hasattr(me, "vertex_normals") else me.vertices.foreach_get("normal", nor)
        me.vertices.foreach_set("co", co + nor * nudge)
        me.update()
    n = bpy.data.objects.new(name, me)
    for a in VIS:
        if hasattr(o, a):
            setattr(n, a, getattr(o, a))
    if not me.materials:
        for slot in o.material_slots:
            me.materials.append(slot.material)
    if not any(me.materials):                         # the bake needs a material on every face
        me.materials.clear()
        me.materials.append(bpy.data.materials.get("KIT_plain") or bpy.data.materials.new("KIT_plain"))
    return n


def view_dirs(scene):
    """Directions the visitor can look from (the page limits turning to about +-30 degrees)."""
    back = scene.camera.rotation_euler.to_matrix().col[2]
    dirs = []
    for turn in (-0.6, 0.0, 0.6):
        for tilt in (-0.4, 0.0, 0.3):
            d = Matrix.Rotation(turn, 3, "Z") @ back
            side = d.cross(Vector((0, 0, 1)))
            if side.length > 1e-6:
                d = Matrix.Rotation(tilt, 3, side.normalized()) @ d
            dirs.append(d.normalized())
    return dirs


def cull_hidden_faces(o, dirs):
    """Drop faces nobody can ever see (backs of walls, undersides) - more texture for the visible ones."""
    bm = bmesh.new()
    bm.from_mesh(o.data)
    dead = [f for f in bm.faces if max(f.normal.dot(d) for d in dirs) < 0.03 and all(e.is_manifold for e in f.edges)]
    bmesh.ops.delete(bm, geom=dead, context="FACES")
    bm.to_mesh(o.data)
    bm.free()
    return len(dead)


def join(objs, name):
    if len(objs) > 1:
        bpy.ops.object.select_all(action="DESELECT")
        for o in objs:
            o.select_set(True)
        bpy.context.view_layer.objects.active = objs[0]
        bpy.ops.object.join()
    clash = bpy.data.objects.get(name)                 # the page finds meshes by these exact names
    if clash is not None and clash is not objs[0]:
        clash.name = name + "_orig"
    objs[0].name = name
    return objs[0]


# ===================================================================== 2. bake
def setup_cycles(scene, samples):
    scene.render.engine = "CYCLES"
    scene.cycles.samples = samples
    scene.cycles.use_denoising = False
    if hasattr(scene.cycles, "max_bounces"):
        scene.cycles.max_bounces = 6
    try:                                              # use the GPU when there is one (Metal / CUDA / OptiX / HIP)
        prefs = bpy.context.preferences.addons["cycles"].preferences
        for kind in ("METAL", "OPTIX", "CUDA", "HIP", "ONEAPI"):
            try:
                prefs.compute_device_type = kind
            except TypeError:
                continue
            prefs.get_devices()
            gpus = [d for d in prefs.devices if d.type != "CPU"]
            if gpus:
                for d in prefs.devices:
                    d.use = True
                scene.cycles.device = "GPU"
                log(f"baking on GPU ({kind}: {', '.join(d.name for d in gpus)})")
                return
        log("no GPU found - baking on CPU (slower)")
    except Exception as err:                          # noqa: BLE001
        log(f"GPU setup skipped ({err}) - baking on CPU")


def add_bake_target(objs, image):
    """Every material on these objects writes into `image` (the active image node is the bake target)."""
    done = set()
    for o in objs:
        for m in o.data.materials:
            if m is None or m.name in done:
                continue
            done.add(m.name)
            nt = m.node_tree
            node = nt.nodes.new("ShaderNodeTexImage")
            node.name = node.label = "KIT_BAKE"
            node.image = image
            for n in nt.nodes:
                n.select = False
            node.select = True
            nt.nodes.active = node


def bake(objs, margin):
    bpy.ops.object.select_all(action="DESELECT")
    for o in objs:
        o.select_set(True)
    bpy.context.view_layer.objects.active = objs[0]
    bpy.ops.object.bake(type="COMBINED", pass_filter={"EMIT", "DIRECT", "INDIRECT", "DIFFUSE", "TRANSMISSION"},
                        margin=margin, margin_type="EXTEND", use_clear=True)


def set_format(settings, path, quality):
    try:
        settings.file_format = "WEBP"
    except TypeError:
        settings.file_format = "JPEG"
        path = path.rsplit(".", 1)[0] + ".jpg"
    settings.quality = quality
    if hasattr(settings, "color_mode"):
        settings.color_mode = "RGB"
    return path


def save_denoised(image, path, scene, quality=90):
    """Remove bake noise (Open Image Denoise in the compositor) and save with the room's colour
    management (Standard view, exposure), so the web page matches the renders."""
    tmp = bpy.data.scenes.new("KIT_denoise")
    try:
        tmp.render.resolution_x, tmp.render.resolution_y = image.size
        tmp.render.resolution_percentage = 100
        for a in ("view_transform", "look", "exposure", "gamma"):
            setattr(tmp.view_settings, a, getattr(scene.view_settings, a))
        tmp.display_settings.display_device = scene.display_settings.display_device
        try:
            tmp.render.engine = "BLENDER_WORKBENCH"
        except TypeError:
            pass
        cam = bpy.data.objects.new("KIT_denoise_cam", bpy.data.cameras.new("KIT_denoise_cam"))
        tmp.collection.objects.link(cam)
        tmp.camera = cam
        if hasattr(tmp, "compositing_node_group"):                         # Blender 5+
            ng = bpy.data.node_groups.new("KIT_denoise", "CompositorNodeTree")
            tmp.compositing_node_group = ng
            ng.interface.new_socket(name="Image", in_out="OUTPUT", socket_type="NodeSocketColor")
            out = ng.nodes.new("NodeGroupOutput")
        else:                                                              # Blender 4.x
            tmp.use_nodes = True
            ng = tmp.node_tree
            ng.nodes.clear()
            out = ng.nodes.new("CompositorNodeComposite")
        src = ng.nodes.new("CompositorNodeImage")
        src.image = image
        dn = ng.nodes.new("CompositorNodeDenoise")
        ng.links.new(src.outputs[0], dn.inputs[0])
        ng.links.new(dn.outputs[0], out.inputs[0])
        path = set_format(tmp.render.image_settings, path, quality)
        tmp.render.filepath = path
        bpy.ops.render.render(write_still=True, scene=tmp.name)
    except Exception as err:                                               # noqa: BLE001
        log(f"denoise skipped ({err}); saving the raw bake")
        s = scene.render.image_settings
        path = set_format(s, path, quality)
        image.save_render(path, scene=scene)
    finally:
        bpy.data.scenes.remove(tmp)
    return path


# ===================================================================== 3. main export
def export(out, size=4096, samples=32, page=True, draco=True, single=True):
    t0 = time.time()
    scene = bpy.context.scene
    if "kit_style" not in scene:
        sys.exit("[RoomKit web] this .blend was not made by a Room Kit template")
    os.makedirs(os.path.join(out, "3d"), exist_ok=True)
    if bpy.context.object and bpy.context.object.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")
    dg = bpy.context.evaluated_depsgraph_get()
    coll = bpy.data.collections.new("WebExport")
    scene.collection.children.link(coll)

    # -- convert everything that renders into plain world-space meshes, sorted into groups:
    #    "static" (the room), one group per clickable object, one per project picture.
    sources = [o for o in scene.objects if render_visible(o)]
    owners, pictures, parts, glass = {}, [], {}, {}
    dirs, culled = view_dirs(scene), 0
    for i, o in enumerate(sources):
        n = make_world_mesh(o, dg, f"tmp_{o.name}", 0.0016 if is_picture(o) else 0.0002 * (1 + i % 7))
        if not is_picture(o):
            culled += cull_hidden_faces(n, dirs)
        if len(n.data.polygons) == 0:
            bpy.data.objects.remove(n)
            continue
        coll.objects.link(n)
        if is_picture(o):
            pictures.append((o, n))
            continue
        owner = web_owner(o)
        group = "static"
        if owner is not None:
            group = owners.setdefault(owner.name, f"click_{len(owners)}")
        elif alpha_of(o) < 0.98:                       # see-through glass gets its own mesh + opacity
            a = alpha_of(o)
            group = glass.setdefault(a, f"glass_{len(glass)}")
        flags = tuple(getattr(n, a, True) for a in VIS)
        parts.setdefault((group, flags), []).append(n)
    for o in sources:                                  # the copies stand in for the originals from now on
        o.hide_render = True

    bake_objs = [join(objs, f"bake_{i}") for i, objs in enumerate(parts.values())]
    groups = {}                                         # bake object -> final group name
    for (group, _), o in zip(parts.keys(), bake_objs):
        groups[o.name] = group
    tris = sum(len(o.data.polygons) for o in bake_objs)
    log(f"{len(sources)} objects -> {len(bake_objs)} bake meshes, {len(owners)} clickable, {len(pictures)} pictures, "
        f"{tris} faces ({culled} hidden faces dropped)")

    # -- one shared lightmap UV layout for the whole room
    for o in bake_objs:
        uvs = o.data.uv_layers
        lm = uvs.new(name="Lightmap")
        uvs.active = lm                               # bake target; textures keep reading their own UVs
    bpy.ops.object.select_all(action="DESELECT")
    for o in bake_objs:
        o.select_set(True)
    bpy.context.view_layer.objects.active = bake_objs[0]
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.uv.smart_project(angle_limit=math.radians(60), island_margin=0.0015, area_weight=0.0,
                             correct_aspect=True, scale_to_bounds=False)
    try:                                              # tighter packing = sharper lighting
        bpy.ops.uv.pack_islands(rotate=True, margin=0.0015)
    except Exception:                                 # noqa: BLE001
        pass
    bpy.ops.object.mode_set(mode="OBJECT")

    log(f"lightmap UVs ready ({time.time() - t0:.0f}s)")

    # -- bake the room's light into one texture. Project pictures stay sharp: the page shows the real images.
    setup_cycles(scene, samples)
    atlas = bpy.data.images.new("KIT_light", size, size, float_buffer=True)
    add_bake_target(bake_objs, atlas)
    log(f"baking lighting ({size}px, {samples} samples) - this takes a few minutes...")
    bake(bake_objs, margin=max(4, size // 256))
    log(f"baked ({time.time() - t0:.0f}s), denoising...")
    light_path = save_denoised(atlas, os.path.join(out, "3d", "light.webp"), scene)
    pics = []
    for src, _ in pictures:
        m = src.data.materials[0] if src.data.materials else None
        mapping = next((nd for nd in m.node_tree.nodes if nd.type == "MAPPING"), None) if m else None
        sx, sy = (mapping.inputs["Scale"].default_value[:2] if mapping else (1.0, 1.0))
        tex = next((nd for nd in m.node_tree.nodes if nd.type == "TEX_IMAGE" and nd.image), None) if m else None
        pics.append({"image": "img/" + os.path.basename(tex.image.filepath) if tex else "",
                     "repeat": [round(sx, 5), round(sy, 5)], "glow": bool(src.get("kit_hook_glow"))})

    # -- final objects: room, clickables, pictures; clean UVs; pivots at their centres (for hover pop)
    final = {}
    for o in bake_objs:
        final.setdefault(groups[o.name], []).append(o)
    exported = []
    for group, objs in final.items():
        o = join(objs, group)
        exported.append(o)
    for i, (src, n) in enumerate(pictures):
        exported.append(join([n], f"pic_{i}"))
    for o in exported:
        keep = "Lightmap" if not o.name.startswith("pic_") else o.data.uv_layers[0].name
        for uv in [u for u in o.data.uv_layers if u.name != keep]:
            o.data.uv_layers.remove(uv)
        o.data.materials.clear()
        if o.name != "static":
            c = sum((Vector(v) for v in o.bound_box), Vector()) / 8
            o.data.transform(Matrix.Translation(-c))
            o.location = c

    # -- clickable info for the page
    info = {}
    for name, group in owners.items():
        info[group] = json.loads(scene.objects[name]["kit_web"])
    for i, (src, _) in enumerate(pictures):
        info[f"pic_{i}"] = json.loads(src["kit_web"])

    bpy.ops.object.select_all(action="DESELECT")
    for o in exported:
        o.select_set(True)
    glb = os.path.join(out, "3d", "room.glb")
    kw = dict(filepath=glb, export_format="GLB", use_selection=True, export_normals=False, export_materials="NONE",
              export_apply=False, export_yup=True)
    try:
        if not draco:
            raise RuntimeError("turned off with --no-draco")
        bpy.ops.export_scene.gltf(**kw, export_draco_mesh_compression_enable=True,
                                  export_draco_mesh_compression_level=6)
    except Exception as err:                          # noqa: BLE001  (Draco missing on some builds)
        log("exporting uncompressed (--no-draco)" if not draco else f"Draco compression unavailable ({err}); exporting uncompressed")
        bpy.ops.export_scene.gltf(**kw)
    log(f"room.glb {os.path.getsize(glb) / 1e6:.1f} MB, light map {os.path.getsize(light_path) / 1e6:.1f} MB")

    # -- camera (same isometric view as the renders) + room extents for responsive framing
    cam = scene.camera
    rot = cam.rotation_euler.to_matrix()
    right, up, back = rot.col[0], rot.col[1], rot.col[2]
    b = scene["kit_bounds"]
    corners = [Vector((x, y, z)) for x in (b[0], b[3]) for y in (b[1], b[4]) for z in (b[2], b[5])]
    xs, ys = [c.dot(right) for c in corners], [c.dot(up) for c in corners]
    center = right * (max(xs) + min(xs)) / 2 + up * (max(ys) + min(ys)) / 2
    mid = sum(corners, Vector()) / 8
    target = center + (-back) * (mid - center).dot(-back)          # point on the view axis nearest the room centre
    view = {"target": to_yup(target), "dir": to_yup(back), "up": to_yup(up),
            "extent": [round(max(xs) - min(xs), 4), round(max(ys) - min(ys), 4)]}
    data = {"view": view, "clicks": info, "pictures": pics, "glass": {g: a for a, g in glass.items()},
            "light": os.path.basename(light_path), "style": scene["kit_style"]}
    with open(os.path.join(out, "3d", "scene.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1)
    if page:
        write_page(out, scene, data, single)
    log(f"done in {time.time() - t0:.0f}s -> {os.path.join(out, 'room3d.html')}")
    return data


# ===================================================================== 4. the web page
def web_image(path, max_side=1600, quality=85):
    """Project image -> bytes small enough to carry inside the page (big photos are shrunk with Blender)."""
    with open(path, "rb") as f:
        raw = f.read()
    ext = os.path.splitext(path)[1].lower()
    if len(raw) < 350_000 and ext in MIME:
        return raw, MIME[ext]
    tmp_dir = tempfile.mkdtemp(prefix="roomkit_web_")
    try:
        img = bpy.data.images.load(path)
        w, h = img.size
        if w and h and max(w, h) > max_side:
            k = max_side / max(w, h)
            img.scale(max(1, round(w * k)), max(1, round(h * k)))
        for fmt, suffix in (("WEBP", ".webp"), ("JPEG", ".jpg")):
            try:
                img.filepath_raw = os.path.join(tmp_dir, "pic" + suffix)
                img.file_format = fmt
                try:
                    img.save(quality=quality)
                except TypeError:                                   # older Blender: no quality argument
                    img.save()
                with open(img.filepath_raw, "rb") as f:
                    small = f.read()
                bpy.data.images.remove(img)
                if len(small) < len(raw) or ext not in MIME:
                    return small, MIME[suffix]
                return raw, MIME[ext]
            except (RuntimeError, TypeError):
                continue
        bpy.data.images.remove(img)
    except Exception as err:                                        # noqa: BLE001
        log(f"could not shrink {os.path.basename(path)} ({err}); embedding it as it is")
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)
    return raw, MIME.get(ext, "application/octet-stream")


def embedded_files(out, data, profile):
    """Every file the page loads -> data: URI, so room3d.html works on its own (even from file://)."""
    wanted = ["3d/room.glb", "3d/" + data["light"]]
    wanted += [p["image"] for p in data["pictures"] if p.get("image")]
    wanted += [pr["image"] for pr in profile.get("projects", []) if pr.get("image")]
    embed, sizes = {}, {}
    for rel in dict.fromkeys(wanted):
        path = os.path.join(out, rel)
        if not os.path.isfile(path):
            log(f"note: {rel} not found, the page will try to load it from the folder")
            continue
        if rel.startswith("img/"):
            raw, mime = web_image(path)
        else:
            with open(path, "rb") as f:
                raw = f.read()
            mime = MIME.get(os.path.splitext(rel)[1].lower(), "application/octet-stream")
        embed[rel] = f"data:{mime};base64," + base64.b64encode(raw).decode("ascii")
        sizes[rel] = len(raw)
    return embed, sizes


def write_page(out, scene, data, single=True):
    profile = json.loads(scene.get("kit_profile", "{}"))
    palette = json.loads(scene["kit_palette"])

    def brightness(hex_color):
        h = hex_color.lstrip("#")
        r, g, bl = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        return (0.299 * r + 0.587 * g + 0.114 * bl) / 255

    bg = palette.get("background", "#F5F2EE")
    accent = profile.get("brand_color") or palette.get("accent_1", "#7C6CF2")
    dark = brightness(bg) < 0.43
    if not dark and brightness(accent) > 0.62:
        accent = palette.get("dark", "#3A3340")
    if dark and brightness(accent) < 0.45:           # deep accents vanish on a dark page: use the brightest one
        accent = max((palette.get(k, accent) for k in ("accent_1", "accent_2", "accent_3", "cream")), key=brightness)
    with open(os.path.join(KIT, "tools", "web", "viewer.html"), encoding="utf-8") as f:
        page = f.read()
    config = {"three": THREE, "bg": bg, "accent": accent, "dark": dark, "profile": profile, "scene": data,
              "single": bool(single)}
    embed, sizes = embedded_files(out, data, profile) if single else ({}, {})
    e = html.escape
    page = (page.replace("{{TITLE}}", e(f"{profile.get('name', 'My room')} · {profile.get('role', '')}"))
                .replace("{{DESCRIPTION}}", e(profile.get("tagline", "")))
                .replace("{{THREE}}", THREE)
                .replace("{{CONFIG}}", json.dumps(config).replace("</", "<\\/"))
                .replace("{{EMBED}}", json.dumps(embed)))
    path = os.path.join(out, "room3d.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(page)
    mb = os.path.getsize(path) / 1e6
    if single:
        parts = ", ".join(f"{os.path.basename(k)} {v / 1e6:.2f} MB" for k, v in sizes.items())
        log(f"room3d.html is self-contained: {mb:.1f} MB ({parts}) - double-click it to open")
        if mb > SINGLE_FILE_BUDGET:
            log(f"note: that is over {SINGLE_FILE_BUDGET:.0f} MB and may load slowly on phones. Try --fast (smaller "
                "light map), smaller project images, or --separate-files.")
    else:
        log(f"room3d.html {mb:.2f} MB + the 3d/ and img/ folders (open it through a web server)")


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    p = argparse.ArgumentParser(prog="export_web.py")
    p.add_argument("--out", default="")
    p.add_argument("--size", type=int, default=4096)
    p.add_argument("--samples", type=int, default=32)
    p.add_argument("--fast", action="store_true")
    p.add_argument("--no-draco", action="store_true", help="bigger room.glb that needs no decoder download "
                   "(for hosts that block loading code from a CDN)")
    p.add_argument("--separate-files", action="store_true", help="room3d.html loads 3d/ and img/ files instead "
                   "of carrying them inside (needs a web server to preview)")
    a = p.parse_args(argv)
    if a.fast:
        a.size, a.samples = 2048, 16
    folder = os.path.abspath(a.out) if a.out else os.path.dirname(bpy.data.filepath) or os.getcwd()
    export(folder, a.size, a.samples, draco=not a.no_draco, single=not a.separate_files)
