"""
3D ROOM PORTFOLIO KIT  -  ROOM CHECKER
Checks that a room .blend follows the kit rules (slots, hooks, settings), so every tool works with it.

  blender -b templates/output/cozy_bedroom.blend -P tools/check_room.py
"""
import json
import sys

import bpy
from mathutils import Vector

SLOT_NAMES = {
    "desk", "chair", "stool", "sofa", "armchair", "bed", "table", "side_table", "counter", "display_case", "shelf",
    "wall_shelf", "cabinet", "media_console", "workbench", "easel", "monitor", "instrument", "speaker", "hero_prop",
    "lamp", "floor_lamp", "pendant_lamp", "plant", "hanging_plant", "rug", "wall_art", "pet",
    # kit v4 (themed rooms)
    "clothes_rack", "wardrobe", "vanity", "mirror", "telescope", "trunk", "fireplace", "stove", "bookcase",
    "salon_chair", "bunk_bed", "window_seat", "planter",
}
SHAPES = {"chair", "sofa", "stool", "table", "counter", "bed", "shelf", "cabinet", "monitor", "lamp", "plant", "rug",
          "frame", "pet", "box"}
KINDS = {"floor", "surface", "wall", "rug", "hanging"}
COLOR_KEYS = {"background", "wall", "wall_trim", "floor", "wood", "main", "accent_1", "accent_2", "accent_3", "cream",
              "plant", "dark"}
PICTURES = {"screen", "frame", "poster", "canvas", "board"}

scene = bpy.context.scene
problems, notes = [], []


def need(ok, msg):
    if not ok:
        problems.append(msg)


for key in ("kit_style", "kit_version", "kit_palette", "kit_material_finish", "kit_furniture_colors", "kit_theme",
            "kit_bounds"):
    need(key in scene, f"scene['{key}'] is missing")
if problems:
    print("\n".join("[RoomKit check] FAIL " + p for p in problems))
    sys.exit(1)
need(scene["kit_version"] >= 2, "kit_version must be 2")
palette = json.loads(scene["kit_palette"])
need(COLOR_KEYS <= set(palette), f"colours missing: {sorted(COLOR_KEYS - set(palette))}")
need((scene.render.resolution_x, scene.render.resolution_y) == (1920, 1080), "render must be 1920x1080")
need("EEVEE" in scene.render.engine, "render engine must be Eevee")

b = scene["kit_bounds"]
if "kit_room_size" in scene:                      # rooms with things outside the walls (awnings) set this
    W, D = scene["kit_room_size"][0], scene["kit_room_size"][1]
else:
    T, W, D = -b[0], b[3], b[4] + b[0]
slots = [o for o in scene.objects if o.name.startswith("SLOT_")]
need(6 <= len(slots) <= 10, f"{len(slots)} slots (need 6-10)")


def aabb(o):
    pts = [o.matrix_world @ Vector((x, y, z)) for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)]
    return [min(p[i] for p in pts) for i in range(3)], [max(p[i] for p in pts) for i in range(3)]


boxes = {}
for s in slots:
    name = s.get("kit_slot", "")
    need(name in SLOT_NAMES, f"slot '{name}' is not in the shared slot vocabulary")
    need(s.get("kit_shape") in SHAPES, f"slot '{name}' has shape '{s.get('kit_shape')}' (allowed: {sorted(SHAPES)})")
    need(s.get("kit_kind") in KINDS, f"slot '{name}' has kind '{s.get('kit_kind')}'")
    need(any(o.get("kit_slot") == name and o.get("kit_role") == "placeholder" for o in scene.objects),
         f"slot '{name}' has no placeholder furniture")
    lo, hi = aabb(s)
    boxes[name] = (lo, hi, s.get("kit_kind"))
    need(lo[0] >= -0.01 and lo[1] >= -0.01 and hi[0] <= W + 0.01 and hi[1] <= D + 0.01,
         f"slot '{name}' sticks out of the room ({[round(v, 2) for v in lo]} - {[round(v, 2) for v in hi]})")
names = sorted(boxes)
for i, a in enumerate(names):
    for c in names[i + 1:]:
        (alo, ahi, ak), (clo, chi, ck) = boxes[a], boxes[c]
        if "rug" in (ak, ck):
            continue
        overlap = [min(ahi[k], chi[k]) - max(alo[k], clo[k]) for k in range(3)]
        if all(v > 0.02 for v in overlap):
            problems.append(f"slots '{a}' and '{c}' overlap by {[round(v, 2) for v in overlap]} m")

hooks = [o for o in scene.objects if o.get("kit_hook")]
kinds = [o["kit_hook"] for o in hooks]
links = {o["kit_link"] for o in scene.objects if o.get("kit_link")}
need("name" in kinds, "no 'name' text hook")
need("role" in kinds, "no 'role' text hook")
need(sum(k in PICTURES for k in kinds) >= 3, f"only {sum(k in PICTURES for k in kinds)} picture hooks (need 3+)")
need("email" in links and len(links) >= 2, f"link hooks {sorted(links)} (need email + one more)")
for o in hooks:
    if o["kit_hook"] in PICTURES:
        w, h = o["kit_hook_size"]
        if max(w, h) < 0.2:
            notes.append(f"{o.name} is small ({w:.2f} x {h:.2f} m) - projects may be hard to see")

print(f"[RoomKit check] room '{scene['kit_style']}' theme '{scene['kit_theme']}': {len(slots)} slots "
      f"({', '.join(names)}), hooks {sorted(set(kinds))}, links {sorted(links)}")
for n in notes:
    print("[RoomKit check] NOTE " + n)
for p in problems:
    print("[RoomKit check] FAIL " + p)
print("[RoomKit check] " + ("PASS" if not problems else f"{len(problems)} problem(s)"))
