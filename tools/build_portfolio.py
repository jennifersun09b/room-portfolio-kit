"""
3D ROOM PORTFOLIO KIT  -  BUILD MY PORTFOLIO (one command)
==========================================================
Reads your profile.json (name, role, projects, links), puts it into a room, and exports:
  hero.png        1920x1080 portfolio image
  og.png          1200x630  link preview (LinkedIn / X / Slack)
  instagram.png   1080x1350 portrait post
  banner.png      1584x396  LinkedIn / X header
  (more sizes with --exports: behance 808x632, dribbble 1600x1200, story 1080x1920, obs4k 3840x2160)
  index.html      a clickable one-page portfolio site (click the screens, frames and sign)
  room.blend      the personalised room, ready for more editing

HOW TO RUN
  blender -b -P tools/build_portfolio.py -- --profile profile.json
  blender -b -P tools/build_portfolio.py -- --profile profile.json --room dev_office --theme night
  blender -b -P tools/build_portfolio.py -- --profile profile.json --blend templates/output/cozy_bedroom.blend
Options:
  --profile FILE  your profile.json, or the folder that holds it
  --room NAME     template to build (default: "room" in profile.json)
  --theme NAME    colour theme of that template (default: "theme" in profile.json, else the template's)
  --seed N        shuffle books/props
  --blend FILE    use a room you already made (e.g. after add_furniture.py) instead of building one
  --out FOLDER    where to write everything (default: portfolio_<room> next to profile.json)
  --fast          quick preview: hero image only (plus any --exports you name), fewer samples
  --exports LIST  which images to make, comma separated (default: hero,og,instagram,banner)
                  also: behance (808x632 cover), dribbble (1600x1200 shot), story (1080x1920 Instagram/TikTok
                  story), obs4k (3840x2160 stream background). hero.png is always made (the site uses it).
  --web           also make room3d.html: an interactive 3D version of the room (turn, zoom, click)
                  (bakes the lighting with Cycles - adds about 2-3 minutes on a recent GPU)
  --separate-files  with --web: keep the 3D files next to room3d.html instead of inside it
                  (by default room3d.html is one self-contained file you can double-click)
Links in profile.json can also include behance, dribbble, instagram, etsy, kofi, twitch and youtube
(a full link or just your @handle). If the room has no object for a link, it borrows a spare one.
"""

import argparse
import html
import json
import os
import re
import runpy
import shutil
import sys
import tempfile

import bpy
bpy.context.preferences.filepaths.save_version = 0              # no .blend1 backup files
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Vector

KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIZES = {"hero": (1920, 1080), "og": (1200, 630), "instagram": (1080, 1350), "banner": (1584, 396),
         "behance": (808, 632), "dribbble": (1600, 1200), "story": (1080, 1920), "obs4k": (3840, 2160)}
DEFAULT_EXPORTS = "hero,og,instagram,banner"
LINK_NAMES = {"email": "Email", "github": "GitHub", "linkedin": "LinkedIn", "website": "Website", "behance": "Behance",
              "dribbble": "Dribbble", "instagram": "Instagram", "etsy": "Etsy", "kofi": "Ko-fi", "twitch": "Twitch",
              "youtube": "YouTube"}
HOTSPOT_LABELS = {"email": "Email me", "github": "GitHub", "linkedin": "LinkedIn", "website": "About me",
                  "behance": "Behance", "dribbble": "Dribbble", "instagram": "Instagram", "etsy": "My Etsy shop",
                  "kofi": "Support me on Ko-fi", "twitch": "Watch on Twitch", "youtube": "YouTube"}
EXTRA_LINKS = ("behance", "dribbble", "instagram", "etsy", "kofi", "twitch", "youtube")
HANDLE_URLS = {"github": "https://github.com/{}", "linkedin": "https://www.linkedin.com/in/{}",
               "behance": "https://www.behance.net/{}", "dribbble": "https://dribbble.com/{}",
               "instagram": "https://www.instagram.com/{}", "etsy": "https://www.etsy.com/shop/{}",
               "kofi": "https://ko-fi.com/{}", "twitch": "https://www.twitch.tv/{}", "youtube": "https://www.youtube.com/@{}"}
PICTURE_HOOKS = ("screen", "frame", "poster", "canvas", "board")


# --------------------------------------------------------------------- arguments + profile
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
p = argparse.ArgumentParser(prog="build_portfolio.py")
p.add_argument("--profile", required=True)
p.add_argument("--room", default="")
p.add_argument("--theme", default="")
p.add_argument("--seed", default="")
p.add_argument("--blend", default="")
p.add_argument("--out", default="")
p.add_argument("--fast", action="store_true")
p.add_argument("--exports", default=None)
p.add_argument("--web", action="store_true")
p.add_argument("--separate-files", action="store_true")
args = p.parse_args(argv)

wanted = [x.strip().lower() for x in (args.exports or DEFAULT_EXPORTS).split(",") if x.strip()]
unknown = [x for x in wanted if x not in SIZES]
if unknown:
    sys.exit(f"[RoomKit] unknown export '{', '.join(unknown)}'. Choose from: {', '.join(SIZES)}")
if args.fast and args.exports is None:
    wanted = ["hero"]
renders = ["hero"] + [x for x in dict.fromkeys(wanted) if x != "hero"]      # hero first: the site's clickable spots

profile_path = os.path.abspath(os.path.expanduser(args.profile))
if os.path.isdir(profile_path):                                 # a folder (e.g. made by RoomKit Studio)
    profile_path = os.path.join(profile_path, "profile.json")
if not os.path.isfile(profile_path):
    sys.exit(f"[RoomKit] profile not found: {profile_path}")
with open(profile_path, encoding="utf-8") as f:
    profile = json.load(f)
base = os.path.dirname(profile_path)


def here(path):
    """Paths in profile.json are relative to the profile file."""
    return path if not path else os.path.abspath(os.path.join(base, os.path.expanduser(path)))


projects = [dict(pr, image=here(pr.get("image", ""))) for pr in profile.get("projects", [])]
for pr in projects:
    if pr["image"] and not os.path.isfile(pr["image"]):
        print(f"[RoomKit] WARNING image not found, skipped: {pr['image']}")
        pr["image"] = ""


def link_url(kind, value):
    """Full URL for a link: emails get mailto:, '@handle' or 'handle' becomes the site's profile URL."""
    v = str(value or "").strip()
    if not v:
        return ""
    if kind == "email":
        return v if v.startswith("mailto:") else "mailto:" + v
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", v):              # already https://, mailto:, tel: ...
        return v
    if kind in HANDLE_URLS and "/" not in v and " " not in v and (v.startswith("@") or "." not in v):
        return HANDLE_URLS[kind].format(v.lstrip("@"))
    return "https://" + v.lstrip("/")


links = {k: link_url(k, v) for k, v in (profile.get("links") or {}).items() if isinstance(v, str) and v.strip()}

# --------------------------------------------------------------------- build or open the room
if args.blend:
    bpy.ops.wm.open_mainfile(filepath=os.path.abspath(args.blend))
    room = bpy.context.scene.get("kit_style", "room")
else:
    room = args.room or profile.get("room", "cozy_bedroom")
    template = os.path.join(KIT, "templates", f"{room}.py")
    if not os.path.isfile(template):
        rooms = sorted(f[:-3] for f in os.listdir(os.path.join(KIT, "templates")) if f.endswith(".py"))
        sys.exit(f"[RoomKit] no template '{room}'. Choose one of: {', '.join(rooms)}")
    os.environ["ROOMKIT_BUILD_ONLY"] = "1"
    if args.theme or profile.get("theme"):
        os.environ["ROOMKIT_THEME"] = args.theme or profile.get("theme")
    if args.seed:
        os.environ["ROOMKIT_SEED"] = str(args.seed)
    # Run a copy of the template from a temporary folder: a template saves output/<room>.blend next to itself,
    # and the shipped templates/output files must stay exactly as they are.
    build_dir = tempfile.mkdtemp(prefix="roomkit_build_")
    shutil.copyfile(template, os.path.join(build_dir, f"{room}.py"))
    runpy.run_path(os.path.join(build_dir, f"{room}.py"), run_name="__main__")
scene = bpy.context.scene
if "kit_style" not in scene:
    sys.exit("[RoomKit] this .blend was not made by a Room Kit template")

out = os.path.abspath(args.out) if args.out else os.path.join(base, f"portfolio_{room}")
os.makedirs(os.path.join(out, "img"), exist_ok=True)


# --------------------------------------------------------------------- fill the hooks
def principled(m):
    return next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")


def srgb_to_linear(hex_color):
    h = hex_color.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c] + [1.0]


def image_material(hook, path):
    img = bpy.data.images.load(path, check_existing=True)
    w, h = hook["kit_hook_size"]
    iw, ih = img.size
    m = bpy.data.materials.new(f"{hook.name}_image")
    if bpy.app.version < (5, 0, 0):
        m.use_nodes = True
    nt = m.node_tree
    b = principled(m)
    tex = nt.nodes.new("ShaderNodeTexImage")
    tex.image, tex.extension = img, "EXTEND"
    coords, mapping = nt.nodes.new("ShaderNodeTexCoord"), nt.nodes.new("ShaderNodeMapping")
    ia, ha = iw / max(ih, 1), w / h
    sx, sy = (ha / ia, 1.0) if ia > ha else (1.0, ia / ha)      # "cover" crop: fill the surface, keep proportions
    mapping.inputs["Scale"].default_value = (sx, sy, 1)
    mapping.inputs["Location"].default_value = ((1 - sx) / 2, (1 - sy) / 2, 0)
    nt.links.new(coords.outputs["UV"], mapping.inputs["Vector"])
    nt.links.new(mapping.outputs["Vector"], tex.inputs["Vector"])
    nt.links.new(tex.outputs["Color"], b.inputs["Base Color"])
    b.inputs["Roughness"].default_value = 0.45
    if hook.get("kit_hook_glow"):
        nt.links.new(tex.outputs["Color"], b.inputs["Emission Color" if "Emission Color" in b.inputs else "Emission"])
        b.inputs["Emission Strength"].default_value = 0.9
    return m


def set_text(hook, text):
    hook.data.body = text
    hook.scale = (1, 1, 1)
    bpy.context.view_layer.update()
    limit = hook.get("kit_max_width", 1.0)
    if hook.dimensions.x > limit:
        hook.scale = [limit / hook.dimensions.x] * 3


def put_image(hook, path):
    hook.data.materials.clear()
    hook.data.materials.append(image_material(hook, path))
    for o in scene.objects:                                    # hide the default doodle / fake UI
        if o.get("kit_hook_default") == hook.name:
            o.hide_render = o.hide_viewport = True


hooks = sorted((o for o in scene.objects if o.get("kit_hook")), key=lambda o: (o["kit_hook"], o.get("kit_hook_index", 1)))
picture_hooks = sorted((o for o in hooks if o["kit_hook"] in PICTURE_HOOKS),     # screens get project #1
                       key=lambda o: (PICTURE_HOOKS.index(o["kit_hook"]), o.get("kit_hook_index", 1)))
text_values = {
    "name": [profile.get("name", "")], "role": [profile.get("role", "")], "tagline": [profile.get("tagline", "")],
    "title": [pr.get("title", "") for pr in projects], "skill": profile.get("skills", []),
}
hotspots = []
with_images = [pr for pr in projects if pr["image"]]
for i, hook in enumerate(picture_hooks):                      # project images, in order, repeating if needed
    if not with_images:
        break
    pr = with_images[i % len(with_images)]
    put_image(hook, pr["image"])
    hotspots.append((hook, pr.get("title", ""), pr.get("url", ""), "project", projects.index(pr)))
for hook in hooks:
    kind = hook["kit_hook"]
    if kind == "logo" and profile.get("logo") and os.path.isfile(here(profile["logo"])):
        put_image(hook, here(profile["logo"]))
    elif kind in text_values and hook.type == "FONT":
        values = [v for v in text_values[kind] if v]
        idx = hook.get("kit_hook_index", 1) - 1
        if values:
            set_text(hook, values[idx % len(values)])
        else:
            hook.hide_render = hook.hide_viewport = True        # no value -> hide the placeholder text
# Clickable link objects. A room object whose link is missing from the profile (e.g. the GitHub bookshelf for a
# designer with no GitHub) borrows a spare link instead (Behance, Etsy, Ko-fi...), and finally the website.
link_objects = sorted((o for o in scene.objects if o.get("kit_link")), key=lambda o: o.name)
room_kinds = {o["kit_link"] for o in link_objects}
spare = [k for k in list(EXTRA_LINKS) + [k for k in links if k not in LINK_NAMES]
         if links.get(k) and k not in room_kinds]
borrowed = {}
for o in link_objects:
    kind = o["kit_link"]
    if not links.get(kind) and kind != "email" and kind not in borrowed:
        borrowed[kind] = spare.pop(0) if spare else ("website" if links.get("website") else "")
        if borrowed[kind]:
            print(f"[RoomKit] the room's {kind} object links to your {LINK_NAMES.get(borrowed[kind], borrowed[kind])}")
    use = kind if links.get(kind) else borrowed.get(kind, "")
    if use:
        hotspots.append((o, HOTSPOT_LABELS.get(use, use.replace("_", " ").title()), links[use], "link", -1))

# Brand colour: replaces the room's first accent colour.
if profile.get("brand_color"):
    for m in bpy.data.materials:
        if m.get("kit_color_key") == "accent_1" and m.node_tree:
            b = principled(m)
            b.inputs["Base Color"].default_value = srgb_to_linear(profile["brand_color"])
            kit_base = m.node_tree.nodes.get("KIT_BASE")                # textured materials keep their colour here
            if kit_base:
                kit_base.outputs[0].default_value = srgb_to_linear(profile["brand_color"])
            emit = b.inputs.get("Emission Color") or b.inputs.get("Emission")
            if emit and not emit.is_linked and b.inputs["Emission Strength"].default_value > 0:
                emit.default_value = srgb_to_linear(profile["brand_color"])     # neon signs glow in your colour


# --------------------------------------------------------------------- camera framing + renders
cam = scene.camera


def frame(width, height, margin=1.06):
    scene.render.resolution_x, scene.render.resolution_y = width, height
    b = scene["kit_bounds"]
    rot = cam.rotation_euler.to_matrix()
    right, up, back = rot.col[0], rot.col[1], rot.col[2]
    corners = [Vector((x, y, z)) for x in (b[0], b[3]) for y in (b[1], b[4]) for z in (b[2], b[5])]
    xs, ys = [c.dot(right) for c in corners], [c.dot(up) for c in corners]
    ex, ey, aspect = max(xs) - min(xs), max(ys) - min(ys), width / height
    cam.data.ortho_scale = (max(ex, ey * aspect) if aspect >= 1 else max(ex / aspect, ey)) * margin
    cam.location = right * (max(xs) + min(xs)) / 2 + up * (max(ys) + min(ys)) / 2 + back * 30


def screen_box(obj):
    """Object -> (left, top, width, height) in % of the image."""
    meshes = [obj] + list(obj.children_recursive)
    dg = bpy.context.evaluated_depsgraph_get()
    pts = []
    for o in meshes:
        if o.type in ("MESH", "FONT") and not o.hide_render:
            ev = o.evaluated_get(dg)
            pts += [world_to_camera_view(scene, cam, ev.matrix_world @ Vector(c)) for c in ev.bound_box]
    if not pts:
        return None
    x0, x1 = min(p.x for p in pts), max(p.x for p in pts)
    y0, y1 = min(p.y for p in pts), max(p.y for p in pts)
    pad_x, pad_y = max(0.0, 0.03 - (x1 - x0)) / 2, max(0.0, 0.045 - (y1 - y0)) / 2   # small things get a bigger target
    x0, x1, y0, y1 = x0 - pad_x, x1 + pad_x, y0 - pad_y, y1 + pad_y
    return [round(100 * x0, 2), round(100 * (1 - y1), 2), round(100 * (x1 - x0), 2), round(100 * (y1 - y0), 2)]


if args.fast:
    for attr in ("taa_render_samples",):
        if hasattr(scene.eevee, attr):
            setattr(scene.eevee, attr, 16)
spots = []
for name in renders:
    frame(*SIZES[name], margin=1.06 if name != "banner" else 1.02)
    if name == "hero":
        bpy.context.view_layer.update()
        for obj, label, url, kind, _ in hotspots:
            box = screen_box(obj)
            if box and url:
                spots.append({"box": box, "label": label, "url": url, "kind": kind})
    scene.render.filepath = os.path.join(out, f"{name}.png")
    bpy.ops.render.render(write_still=True)
    print(f"[RoomKit] rendered {scene.render.filepath}")
frame(*SIZES["hero"])
# What the 3D web page needs: which objects are clickable, and the profile (export_web.py reads these).
for obj, label, url, kind, index in hotspots:
    obj["kit_web"] = json.dumps({"label": label, "url": url, "kind": kind, "project": index})
scene["kit_profile"] = json.dumps({
    "name": profile.get("name", ""), "role": profile.get("role", ""), "tagline": profile.get("tagline", ""),
    "brand_color": profile.get("brand_color", ""), "skills": profile.get("skills", []),
    "links": dict(links),
    "projects": [{"title": pr.get("title", ""), "description": pr.get("description", ""), "url": pr.get("url", ""),
                  "image": ("img/" + os.path.basename(pr["image"])) if pr["image"] else ""} for pr in projects]})
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(out, "room.blend"))
if not args.blend:
    shutil.rmtree(build_dir, ignore_errors=True)                 # the temporary template copy is no longer needed

# --------------------------------------------------------------------- one-page site
palette = json.loads(scene["kit_palette"])
def brightness(hex_color):
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return (0.299 * r + 0.587 * g + 0.114 * b) / 255


accent = profile.get("brand_color") or palette.get("accent_1", "#7C6CF2")
bg = palette.get("background", "#F5F2EE")
dark_room = brightness(bg) < 0.43
ink, card = ("#F1F1F6", "rgba(255,255,255,.07)") if dark_room else ("#24212B", "rgba(255,255,255,.72)")
if not dark_room and brightness(accent) > 0.62:            # pastel accents are unreadable as text
    accent = palette.get("dark", "#3A3340")
if dark_room and brightness(accent) < 0.45:                # deep accents vanish on a dark page
    accent = max((palette.get(k, accent) for k in ("accent_1", "accent_2", "accent_3", "cream")), key=brightness)
e = html.escape

cards = []
for pr in projects:
    img = ""
    if pr["image"]:
        dst = os.path.join("img", os.path.basename(pr["image"]))
        shutil.copyfile(pr["image"], os.path.join(out, dst))
        img = f'<img src="{e(dst)}" alt="{e(pr.get("title", ""))}">'
    title = e(pr.get("title", ""))
    title = f'<a href="{e(pr["url"])}" target="_blank" rel="noopener">{title}</a>' if pr.get("url") else title
    cards.append(f'<article class="card">{img}<h3>{title}</h3><p>{e(pr.get("description", ""))}</p></article>')
link_html = " · ".join(
    f'<a href="{e(v)}" target="_blank" rel="noopener">{e(LINK_NAMES.get(k, k.replace("_", " ").title()))}</a>'
    for k, v in links.items() if v)
spot_html = "\n".join(
    f'<a class="spot {s["kind"]}" href="{e(s["url"])}" target="_blank" rel="noopener" '
    f'style="left:{s["box"][0]}%;top:{s["box"][1]}%;width:{s["box"][2]}%;height:{s["box"][3]}%">'
    f'<span>{e(s["label"])}</span></a>' for s in spots)
skills = "".join(f"<li>{e(s)}</li>" for s in profile.get("skills", []))
page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(profile.get("name", "Portfolio"))} · {e(profile.get("role", ""))}</title>
<meta property="og:title" content="{e(profile.get("name", ""))} · {e(profile.get("role", ""))}">
<meta property="og:description" content="{e(profile.get("tagline", ""))}"><meta property="og:image" content="og.png">
<style>
:root{{--bg:{bg};--ink:{ink};--accent:{accent};--card:{card};--on:{"#1d1b22" if brightness(accent) > 0.6 else "#fff"}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 ui-rounded,"SF Pro Rounded",system-ui,sans-serif}}
header{{max-width:1100px;margin:auto;padding:40px 20px 8px}}h1{{margin:0;font-size:clamp(28px,5vw,46px)}}
.role{{color:var(--accent);font-weight:700;margin:2px 0 6px}}.links a{{color:var(--ink);font-weight:600}}
.room{{position:relative;max-width:1100px;margin:16px auto;padding:0 20px}}.room img{{width:100%;display:block;border-radius:18px}}
.stage{{position:relative}}.spot{{position:absolute;border-radius:12px;outline:2px solid transparent;transition:.2s}}
.spot:hover,.spot:focus{{outline-color:var(--accent);background:rgba(255,255,255,.12)}}
.spot span{{position:absolute;left:50%;bottom:100%;transform:translate(-50%,-6px);white-space:nowrap;background:var(--accent);
color:var(--on);font-size:13px;font-weight:700;padding:4px 10px;border-radius:99px;opacity:0;transition:.2s;pointer-events:none}}
.spot:hover span,.spot:focus span{{opacity:1}}.spot::after{{content:'';position:absolute;left:calc(50% - 5px);top:calc(50% - 5px);width:10px;height:10px;border-radius:50%;background:var(--accent);box-shadow:0 0 0 0 var(--accent);animation:pulse 2s infinite}}@keyframes pulse{{0%{{box-shadow:0 0 0 0 var(--accent);opacity:.9}}70%{{box-shadow:0 0 0 10px transparent;opacity:.6}}100%{{box-shadow:0 0 0 0 transparent;opacity:.9}}}}@media (prefers-reduced-motion:reduce){{.spot::after{{animation:none}}}}.hint{{text-align:center;opacity:.65;font-size:14px}}
.skills{{display:flex;flex-wrap:wrap;gap:8px;list-style:none;padding:0}}.skills li{{background:var(--card);padding:4px 12px;border-radius:99px}}
main{{max-width:1100px;margin:auto;padding:8px 20px 40px}}.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:18px}}
.card{{background:var(--card);border-radius:16px;overflow:hidden;padding-bottom:6px}}.card img{{width:100%;aspect-ratio:16/10;object-fit:cover;display:block}}
.go3d{{float:right;background:var(--accent);color:var(--on);font-weight:700;text-decoration:none;padding:8px 16px;border-radius:99px;margin-top:8px}}
.card h3,.card p{{margin:10px 14px 0}}.card a{{color:var(--ink)}}footer{{text-align:center;opacity:.5;font-size:13px;padding:24px}}
</style></head><body>
<header>{'<a class="go3d" href="room3d.html">Explore my room in 3D →</a>' if args.web else ""}<h1>{e(profile.get("name", ""))}</h1><div class="role">{e(profile.get("role", ""))}</div>
<p>{e(profile.get("tagline", ""))}</p><div class="links">{link_html}</div></header>
<section class="room"><div class="stage"><img src="hero.png" alt="3D room of {e(profile.get("name", ""))}">
{spot_html}
</div><p class="hint">Tip: click the screens, pictures and objects in the room.</p></section>
<main>{"<ul class='skills'>" + skills + "</ul>" if skills else ""}<h2>Projects</h2><div class="grid">{"".join(cards)}</div></main>
<footer>Made with the 3D Room Portfolio Kit</footer>
</body></html>"""
with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
    f.write(page)
print(f"[RoomKit] portfolio ready: {os.path.join(out, 'index.html')}  ({len(spots)} clickable spots)")

if args.web:                                                    # interactive 3D version (bakes lighting with Cycles)
    sys.path.insert(0, os.path.join(KIT, "tools"))
    import export_web
    export_web.export(out, size=2048 if args.fast else 4096, samples=16 if args.fast else 32,
                      single=not args.separate_files)
