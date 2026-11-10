"""
3D ROOM PORTFOLIO KIT  -  Template: LIVING ROOM / MEDIA LOUNGE
==============================================================
Builds a real-looking, cosy Scandinavian living room in isometric miniature and renders a 1920x1080 image.
Every piece is modelled on furniture you can buy (real sizes, real construction), so the room reads as a
friend's flat rather than a toy. The wall-mounted TV plays your showreel, the frame wall over the sofa and
the record sleeves on the picture ledge show your projects, and the letter board carries your name.

HOW TO RUN
  Option A (no Blender UI):   blender -b -P living_lounge.py
  Option B (inside Blender):  Scripting tab > Open > living_lounge.py > Run Script (then F12 to render)

You only need to edit the SETTINGS block below. Everything under it builds the room.
Output: output/living_lounge.png and output/living_lounge.blend next to this script.
"""
# REFERENCES (real products this room is modelled on; names live only in comments, never in the scene)
#   sofa          IKEA SOEDERHAMN 3-seat sofa w/ armrests, 198x99x83 cm, seat h 40, 6 cm arms
#                 https://www.ikea.com/th/en/p/soederhamn-compact-3-seat-sofa-tonerud-grey-s39485001
#   armchair      IKEA POAENG armchair, 68x82x100 cm, seat h 42, bent layer-glued birch cantilever frame
#                 https://www.ikea.gr/en/products/poang-armchair/19197780
#   table         IKEA LACK coffee table, 90x55x45 cm, 5 cm top, 5x5 cm legs, magazine shelf
#                 https://www.ikea.com/gb/en/p/lack-coffee-table-white-stained-oak-effect-50319029/
#   media_console IKEA BESTA TV bench with drawers and door, 180x42x39 cm (3 x 60 cm sections), oak-veneer fronts
#                 https://www.ikea.com/gb/en/p/besta-tv-bench-with-drawers-and-door-white-hedeviken-oak-veneer-s69435887
#   TV            generic 55" LED TV, 123x71x6 cm, 8 mm bezel, flat wall mount
#                 https://en.tab-tv.com/55-inch-tv-dimensions
#   floor_lamp    IKEA HEKTAR floor lamp, 181 cm, shade dia 31.5 cm, base dia 34 cm
#                 https://www.ikea.com/sg/en/p/hektar-floor-lamp-dark-grey-00215307/
#   rug           IKEA STOCKHOLM rug, flatwoven, handmade, striped, 170x240 cm, 6 mm
#                 https://www.ikea.com/gb/en/p/stockholm-rug-flatwoven-handmade-striped-black-off-white-80104862/
#   wall_art      IKEA RIBBA frames 50x70 (40x50 mount) + 30x40 / 40x50, salon hang
#                 https://www.ikea.com/my/en/p/ribba-frame-black-50301618
#   wall_shelf    IKEA MOSSLANDA picture ledge 115x12 cm holding 31.5 cm LP sleeves
#                 https://www.ikea.com/ie/en/p/mosslanda-picture-ledge-black-70292104
#   bookcase      IKEA BILLY bookcase 80x28x106 cm (decor, GitHub link)
#                 https://www.ikea.com/se/en/p/billy-bookcase-white-30263844/
#   plant         FICUS LYRATA fiddle-leaf fig, ~150 cm in a 30 cm ceramic pot
#                 https://www.ikea.com/ca/en/p/ficus-lyrata-potted-plant-fiddle-leaf-fig-90399175
#   snake plant   SANSEVIERIA in a 22 cm pot (decor)
#                 https://www.ikea.com/gb/en/p/sansevieria-potted-plant-with-pot-snake-plant-assorted-colours-30402034
#   curtains      IKEA HUGAD curtain rod 28 mm + rings 38 mm, linen panels
#                 https://www.ikea.com/de/en/p/raecka-hugad-double-curtain-rod-combination-black-s69399587/
#   radiator      Type 22 double-panel convector radiator 600x800x100 mm (Stelrad-style)
#                 https://www.wickes.co.uk/Compact-Type-22-Double-Panel-Double-Convector-Radiator---600mm-x-1000mm/p/176238
#   letter board  felt letter board in an oak frame, 80x55 cm (generic product type)
#   pouffe        IKEA SANDARED pouffe (cable-knit cover), dia 45 x 33 cm
#                 https://www.ikea.com/nl/en/p/sandared-pouffe-beige-00385314
#   side table    IKEA GLADOM tray table, dia 45 x 53 cm, powder-coated steel, three tube legs + ring
#                 https://www.ikea.com/ie/en/p/gladom-tray-table-white-70337819
#   basket        coiled seagrass belly basket, dia 40 x 35 cm, rope handles (generic product type)
#   dog bed       round 'donut' bolster pet bed, dia 70 cm (generic product type)
#   See research/living_lounge.md for the full table.

# =====================================================================
#  SETTINGS  -  change these lines, then run the script again
# =====================================================================
ROOM_NAME = "living_lounge"         # used for the output file names

ROOM_WIDTH = 4.6                    # metres, left to right
ROOM_DEPTH = 4.2                    # metres, front to back
WALL_HEIGHT = 2.8                   # metres

THEME = "smooth"                    # pick one of the colour themes below
THEMES = {                          # any hex colour works; "main" is the sofa fabric colour
    # "smooth": warm plaster walls, oak floor, sage cotton sofa, terracotta + dusty blue, late-afternoon sun
    "smooth": {
        "background": "#EDE4D8", "wall": "#F1E9DE", "wall_trim": "#F7F3EC", "floor": "#CBAD8C",
        "wood": "#D2AD82", "main": "#A3B394", "accent_1": "#D98F6C", "accent_2": "#7F9BB8",
        "accent_3": "#E9CB8E", "cream": "#F6F2EA", "plant": "#5E8A4E", "dark": "#2F2D2B",
        "walnut": "#6E4E38", "pet": "#E2BF93", "curtain": "#E4DCCD", "rug": "#EEE6D8", "screen": "#6F8FB0",
    },
    # "retro70s": mustard sofa, teal chair, burnt-orange rug and walnut panelling on the back wall.
    # It uses a slightly cooler, softer sun (see LIGHTS) so the warm colours do not go muddy.
    "retro70s": {
        "background": "#F4EAD6", "wall": "#F1E2C4", "wall_trim": "#E9D8B8", "floor": "#B88454",
        "wood": "#B57E48", "main": "#D4A137", "accent_1": "#CF6A2E", "accent_2": "#2F8A86",
        "accent_3": "#EBCB7E", "cream": "#F6ECD9", "plant": "#5F8240", "dark": "#33251C",
        "walnut": "#6B4128", "pet": "#C98B55", "curtain": "#E2B35A", "rug": "#C8642C", "screen": "#3F8F8A",
        "panel": "#7B4D2E",          # only themes with a "panel" colour get wood panelling
    },
}

SUN_WARMTH = 3800                   # Kelvin: 2500 = sunset orange, 6500 = white daylight
SUN_STRENGTH = 3.2
LAMP_WARMTH = 2700                  # Kelvin of the reading floor lamp
LAMP_STRENGTH = 60                  # Watts (the bulb sits inside a dark metal dome, so it needs a bit more)
TV_GLOW = 12                        # Watts of soft light coming off the TV screen
GALLERY_FRAMES = 5                  # frames in the gallery wall over the sofa (3 to 5)
SEED = 7                            # change to shuffle books, records, leaves and small props

SHOW_PLACEHOLDER_FURNITURE = True   # simple built-in furniture inside each slot
SHOW_SLOT_BOXES = True              # wireframe slot boxes in the viewport (never rendered)

CAMERA_HEIGHT_ANGLE = 32            # degrees above the floor (35 = true isometric)
CAMERA_TURN = 45                    # degrees around the room
RESOLUTION = (1920, 1080)
RENDER_SAMPLES = 64
OUTPUT_FOLDER = ""                  # "" = an "output" folder next to this script
# =====================================================================
#  END OF SETTINGS
# =====================================================================

import json
import math
import os
import random

import bmesh
import bpy
from mathutils import Euler, Matrix, Vector

THEME = os.environ.get("ROOMKIT_THEME") or THEME          # build_portfolio.py can pick the theme
SEED = int(os.environ.get("ROOMKIT_SEED") or SEED)
if THEME not in THEMES:
    raise SystemExit(f"[RoomKit] THEME must be one of: {', '.join(THEMES)}")
COLORS = THEMES[THEME]

STYLE = "living_lounge"
KIT_VERSION = 2
W, D, H = ROOM_WIDTH, ROOM_DEPTH, WALL_HEIGHT
T = 0.15            # wall thickness
FLOOR_Z = 0.03      # top of the floor boards; furniture stands here
PANEL = "panel" in COLORS
PANEL_T = 0.014     # thickness of the wood panelling (retro theme)
BACK = D - (PANEL_T if PANEL else 0.0)     # front face of the back wall (things hang here)
R = math.radians
random.seed(SEED)


# --------------------------------------------------------------------- colour helpers
def lin(hex_color):
    """'#RRGGBB' -> linear RGBA, the colour space Blender shaders use."""
    h = hex_color.lstrip("#")
    out = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return (*out, 1.0)


def shade(hex_color, f):
    """A darker (f < 1) or lighter (f > 1) version of a hex colour, e.g. for stitching or a leaf margin."""
    h = hex_color.lstrip("#")
    return "#" + "".join(f"{max(0, min(255, round(int(h[i:i + 2], 16) * f))):02X}" for i in (0, 2, 4))


def kelvin(k):
    """Colour temperature -> linear RGB (Tanner Helland approximation)."""
    t = k / 100.0
    r = 255 if t <= 66 else 329.698727446 * ((t - 60) ** -0.1332047592)
    g = 99.4708025861 * math.log(t) - 161.1195681661 if t <= 66 else 288.1221695283 * ((t - 60) ** -0.0755148492)
    b = 255 if t >= 66 else (0 if t <= 19 else 138.5177312231 * math.log(t - 10) - 305.0447927307)
    rgb = [max(0.0, min(255.0, v)) / 255 for v in (r, g, b)]
    return tuple(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb)


# --------------------------------------------------------------------- scene reset
def clear_scene():
    for o in list(bpy.data.objects):
        bpy.data.objects.remove(o, do_unlink=True)
    for coll in (bpy.data.meshes, bpy.data.materials, bpy.data.lights, bpy.data.cameras, bpy.data.curves):
        for block in list(coll):
            if block.users == 0:
                coll.remove(block)
    for c in list(bpy.data.collections):
        bpy.data.collections.remove(c)


clear_scene()
scene = bpy.context.scene


def collection(name):
    c = bpy.data.collections.new(name)
    scene.collection.children.link(c)
    return c


COL_ROOM = collection("Room")
COL_FURN = collection("Furniture")
COL_SLOTS = collection("Slots")
COL_LIGHT = collection("Lights")
COL_HOOKS = collection("Portfolio")


# --------------------------------------------------------------------- materials
_mats = {}


def _principled(m):
    return next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")


def _set(node, names, value):
    for n in names:
        if n in node.inputs:
            node.inputs[n].default_value = value
            return


def mat(key, rough=0.6, emit=0.0, metal=0.0, color=None, tag=""):
    """Material from a COLORS key (or a hex via color=). tag keeps differently-finished copies apart."""
    hex_color = color or COLORS[key]
    name = f"M_{key}_{rough}_{emit}_{metal}_{hex_color}_{tag}"
    if name in _mats:
        return _mats[name]
    m = bpy.data.materials.new(f"M_{key}")
    if bpy.app.version < (5, 0, 0):      # Blender 5+ materials always use nodes
        m.use_nodes = True
    b = _principled(m)
    c = lin(hex_color)
    _set(b, ["Base Color"], c)
    _set(b, ["Roughness"], rough)
    _set(b, ["Metallic"], metal)
    if emit:
        _set(b, ["Emission Color", "Emission"], c)
        _set(b, ["Emission Strength"], emit)
    m.diffuse_color = c
    m["kit_color_key"] = key
    _mats[name] = m
    return m


# --- KIT SURFACES (copy this block verbatim into a room template, right after mat()) -------------
# Real-world surface detail on top of a flat palette material: wood grain, oak/veneer, fabric weave,
# knit, leather, marble, terrazzo, brushed metal, ceramic glaze, paper, plaster, concrete, brick.
# The palette colour stays in an RGB node named "KIT_BASE", so themes and brand_color keep working.
# Patterns use object coordinates in metres, so a grain/weave has real-world size on any piece.
#
#   oak = surface(mat("wood", 0.5), "wood")            # plank / solid wood, grain along X
#   top = surface(mat("cream", 0.3), "marble")
#   sofa = surface(mat("main", 0.9), "fabric")
#   frame = surface(mat("dark", 0.35, metal=1), "brushed")
#
# Materials are shared by key, so surface() works on the cached material and only adds nodes once.
SURFACE_KINDS = ("wood", "veneer", "fabric", "knit", "leather", "marble", "terrazzo", "brushed", "ceramic",
                 "paper", "plaster", "concrete", "brick", "subway_tile", "square_tile")
# brick / subway_tile / square_tile draw real mortar joints; use along="X" for walls facing -Y/+Y (back wall)
# and along="Y" for walls facing +X (left wall), so the rows run along the wall.


def surface(m, kind, scale=1.0, along="X"):
    """Add real-world surface detail to material m (in place) and return it."""
    if m.get("kit_surface"):
        return m
    nt = m.node_tree
    b = _principled(m)
    base_in = b.inputs["Base Color"]
    base = nt.nodes.new("ShaderNodeRGB")
    base.name = base.label = "KIT_BASE"
    base.outputs[0].default_value = tuple(base_in.default_value)
    coords = nt.nodes.new("ShaderNodeTexCoord")
    mapping = nt.nodes.new("ShaderNodeMapping")
    nt.links.new(coords.outputs["Object"], mapping.inputs["Vector"])

    def tex(kind_, **kw):
        n = nt.nodes.new(kind_)
        for k, v in kw.items():
            if k in n.inputs:
                n.inputs[k].default_value = v
            else:
                setattr(n, k, v)
        nt.links.new(mapping.outputs["Vector"], n.inputs["Vector"])
        return n

    def ramp(src, a, b_, a_pos=0.0, b_pos=1.0):
        r = nt.nodes.new("ShaderNodeValToRGB")
        r.color_ramp.elements[0].position, r.color_ramp.elements[0].color = a_pos, (a, a, a, 1)
        r.color_ramp.elements[1].position, r.color_ramp.elements[1].color = b_pos, (b_, b_, b_, 1)
        nt.links.new(src, r.inputs["Fac"])
        return r.outputs["Color"]

    def tint(value, strength=1.0):
        """Base colour multiplied by a 0..~1.2 pattern value."""
        mix = nt.nodes.new("ShaderNodeMix")
        mix.data_type, mix.blend_type = "RGBA", "MULTIPLY"
        mix.inputs["Factor"].default_value = strength
        nt.links.new(base.outputs[0], mix.inputs[6])
        nt.links.new(value, mix.inputs[7])
        nt.links.new(mix.outputs[2], base_in)

    def bump(height, strength):
        bp = nt.nodes.new("ShaderNodeBump")
        bp.inputs["Strength"].default_value = strength
        bp.inputs["Distance"].default_value = 0.002
        nt.links.new(height, bp.inputs["Height"])
        nt.links.new(bp.outputs["Normal"], b.inputs["Normal"])

    stretch = {"X": (0.12, 1, 1), "Y": (1, 0.12, 1), "Z": (1, 1, 0.12)}[along]   # long grain / brushing direction
    if kind in ("wood", "veneer"):
        mapping.inputs["Scale"].default_value = [s * scale * (2.2 if kind == "wood" else 3.5) for s in stretch]
        wave = tex("ShaderNodeTexWave", wave_type="RINGS", rings_direction="SPHERICAL",
                   Scale=1.2, Distortion=7.0, Detail=4.0, **{"Detail Scale": 1.5})
        noise = tex("ShaderNodeTexNoise", Scale=24.0, Detail=6.0)
        mix = nt.nodes.new("ShaderNodeMix")
        mix.data_type, mix.blend_type = "FLOAT", "MIX"
        mix.inputs["Factor"].default_value = 0.35
        nt.links.new(wave.outputs["Fac"], mix.inputs[2])
        nt.links.new(noise.outputs["Fac"], mix.inputs[3])
        tint(ramp(mix.outputs[0], 0.78, 1.1, 0.25, 0.85))
        bump(mix.outputs[0], 0.06)
    elif kind in ("fabric", "knit"):
        mapping.inputs["Scale"].default_value = [scale * (900 if kind == "fabric" else 260)] * 3
        weave = tex("ShaderNodeTexWave", wave_type="BANDS", bands_direction="DIAGONAL", Scale=1.0, Distortion=0.6)
        noise = tex("ShaderNodeTexNoise", Scale=0.02, Detail=3.0)      # large soft colour variation (pilling, light)
        tint(ramp(noise.outputs["Fac"], 0.88, 1.06, 0.3, 0.7))
        bump(weave.outputs["Fac"], 0.25 if kind == "fabric" else 0.55)
        b.inputs["Roughness"].default_value = max(b.inputs["Roughness"].default_value, 0.85)
        if "Sheen Weight" in b.inputs:
            b.inputs["Sheen Weight"].default_value = 0.3
    elif kind == "leather":
        mapping.inputs["Scale"].default_value = [scale * 60] * 3
        cells = tex("ShaderNodeTexVoronoi", Scale=1.0)
        noise = tex("ShaderNodeTexNoise", Scale=0.15, Detail=2.0)
        tint(ramp(noise.outputs["Fac"], 0.82, 1.08, 0.3, 0.75))
        bump(cells.outputs["Distance"], 0.15)
    elif kind in ("marble", "terrazzo"):
        mapping.inputs["Scale"].default_value = [scale * (2.5 if kind == "marble" else 30)] * 3
        if kind == "marble":
            noise = tex("ShaderNodeTexNoise", Scale=1.5, Detail=8.0, Distortion=4.0)
            r = nt.nodes.new("ShaderNodeValToRGB")                          # thin grey veins where noise ~ 0.5
            els = r.color_ramp.elements
            els[0].position, els[0].color = 0.0, (1.04, 1.04, 1.04, 1)
            els[1].position, els[1].color = 1.0, (1.04, 1.04, 1.04, 1)
            for pos, v in ((0.485, 1.04), (0.5, 0.68), (0.515, 1.04)):
                e = els.new(pos)
                e.color = (v, v, v, 1)
            nt.links.new(noise.outputs["Fac"], r.inputs["Fac"])
            veins = r.outputs["Color"]
        else:
            vor = tex("ShaderNodeTexVoronoi", Scale=1.0)
            veins = ramp(vor.outputs["Distance"], 0.55, 1.03, 0.06, 0.12)    # chips
        tint(veins)
    elif kind == "brushed":
        mapping.inputs["Scale"].default_value = [s * scale * 400 for s in stretch]
        noise = tex("ShaderNodeTexNoise", Scale=1.0, Detail=2.0)
        nt.links.new(ramp(noise.outputs["Fac"], 0.25, 0.45), b.inputs["Roughness"])
        tint(ramp(noise.outputs["Fac"], 0.92, 1.05))
    elif kind == "ceramic":
        mapping.inputs["Scale"].default_value = [scale * 8] * 3
        noise = tex("ShaderNodeTexNoise", Scale=3.0, Detail=4.0)
        tint(ramp(noise.outputs["Fac"], 0.9, 1.05, 0.35, 0.65))
        b.inputs["Roughness"].default_value = min(b.inputs["Roughness"].default_value, 0.25)
    elif kind in ("brick", "subway_tile", "square_tile"):
        w, h = {"brick": (0.215, 0.065), "subway_tile": (0.15, 0.075), "square_tile": (0.1, 0.1)}[kind]
        rot = {"X": (math.pi / 2, 0, 0), "Y": (math.pi / 2, 0, math.pi / 2), "Z": (0, 0, 0)}[along]
        mapping.inputs["Rotation"].default_value = rot              # rows run along the wall
        mapping.inputs["Scale"].default_value = (scale, scale, scale)
        br = tex("ShaderNodeTexBrick", Scale=1.0, **{"Brick Width": w, "Row Height": h,
                 "Mortar Size": 0.012 if kind == "brick" else 0.003, "Mortar Smooth": 0.2,
                 "Color1": (1.05, 1.05, 1.05, 1), "Color2": (0.86, 0.86, 0.86, 1),
                 "Mortar": (1.3, 1.3, 1.3, 1) if kind == "brick" else (1.12, 1.12, 1.12, 1)})
        br.offset = 0.5 if kind != "square_tile" else 0.0
        tint(br.outputs["Color"])
        bump(br.outputs["Fac"], 0.35 if kind == "brick" else 0.2)
        if kind != "brick":
            b.inputs["Roughness"].default_value = min(b.inputs["Roughness"].default_value, 0.3)
    else:                                   # paper, plaster, concrete: soft mottling + fine bump
        size = {"paper": 40, "plaster": 6, "concrete": 4}.get(kind, 6)
        mapping.inputs["Scale"].default_value = [scale * size] * 3
        noise = tex("ShaderNodeTexNoise", Scale=2.0, Detail=8.0)
        fine = tex("ShaderNodeTexNoise", Scale=60.0, Detail=2.0)
        tint(ramp(noise.outputs["Fac"], 0.86 if kind == "concrete" else 0.93, 1.05, 0.3, 0.7))
        bump(fine.outputs["Fac"], 0.08 if kind != "concrete" else 0.18)
    m["kit_surface"] = kind
    return m
# --- END KIT SURFACES ----------------------------------------------------------------------------------


def smat(key, kind, rough=0.6, along="X", scale=1.0, metal=0.0, strength=None):
    """Palette material with a real surface (wood grain, weave...). One material per key + finish.
    strength < 1 tones the pattern down (quiet oak boards, fine birch veneer)."""
    m = surface(mat(key, rough, metal=metal, tag=f"{kind}{along}{scale}{strength}"), kind, scale, along)
    b = _principled(m)
    if kind in ("fabric", "knit") and "Sheen Weight" in b.inputs:
        b.inputs["Sheen Weight"].default_value = 0.08    # a little sheen; more washes colours out from above
    if kind in ("fabric", "knit"):
        _set(b, ["Specular IOR Level", "Specular"], 0.15)  # woven cotton has almost no gloss (no grey glare on top)
        if strength is None:
            strength = 0.5                               # soft colour variation, not a blotchy "crushed velvet"
    if strength is not None:
        for n in m.node_tree.nodes:
            if n.type == "MIX" and getattr(n, "blend_type", "") == "MULTIPLY":
                n.inputs["Factor"].default_value = strength
    return m


# --------------------------------------------------------------------- mesh helpers
def _finish(o, material, bevel, coll, parent, segments=3):
    o.data.materials.append(material)
    if bevel:
        mod = o.modifiers.new("Bevel", "BEVEL")
        mod.width = bevel
        mod.segments = segments
        mod.limit_method = "ANGLE"
        try:
            mod.harden_normals = True
        except AttributeError:
            pass
    o.data.polygons.foreach_set("use_smooth", [True] * len(o.data.polygons))
    (coll or COL_ROOM).objects.link(o)
    if parent is not None:
        o.parent = parent
    return o


def _obj(name, bm):
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    return bpy.data.objects.new(name, me)


def box(name, size, loc, material, bevel=0.004, rot=(0, 0, 0), coll=None, parent=None):
    """Box with small real-furniture bevels. size = (x, y, z) in metres, loc = centre."""
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=Vector(size), verts=bm.verts)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, min(bevel, min(size) * 0.45), coll, parent)


def cyl(name, r, h, loc, material, r2=None, segs=32, bevel=0.003, rot=(0, 0, 0), coll=None, parent=None):
    """Cylinder (or tapered cylinder with r2). loc = centre."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=segs, radius1=r, radius2=r if r2 is None else r2, depth=h)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, bevel, coll, parent)


def rod(name, p0, p1, r, material, segs=12, parent=None):
    """Thin round bar from point p0 to point p1 (legs, stems, tubes)."""
    p0, p1 = Vector(p0), Vector(p1)
    v = p1 - p0
    o = cyl(name, r, v.length, (p0 + p1) / 2, material, segs=segs, bevel=0, parent=parent)
    o.rotation_euler = v.to_track_quat("Z", "Y").to_euler()
    return o


def ball(name, r, loc, material, scale=(1, 1, 1), coll=None, parent=None):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=24, v_segments=14, radius=r)
    o = _obj(name, bm)
    o.location, o.scale = loc, scale
    return _finish(o, material, 0, coll, parent)


def torus(name, big_r, small_r, loc, material, rot=(0, 0, 0), segs=24, segs2=8, parent=None, big_r_y=None):
    """Ring (curtain rings, mug handles, a dog-bed bolster). Lies flat in local XY.
    big_r_y makes an oval ring whose tube stays round (an oval bolster)."""
    bm = bmesh.new()
    rings = []
    ry = big_r_y or big_r
    for i in range(segs):
        a = 2 * math.pi * i / segs
        n = Vector((ry * math.cos(a), big_r * math.sin(a))).normalized()
        rings.append([bm.verts.new((big_r * math.cos(a) + n.x * small_r * math.cos(b),
                                    ry * math.sin(a) + n.y * small_r * math.cos(b), small_r * math.sin(b)))
                      for b in (2 * math.pi * j / segs2 for j in range(segs2))])
    for i in range(segs):
        a0, a1 = rings[i], rings[(i + 1) % segs]
        for j in range(segs2):
            bm.faces.new((a0[j], a1[j], a1[(j + 1) % segs2], a0[(j + 1) % segs2]))
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, 0, None, parent)


def lathe(name, profile, loc, material, segs=32, rot=(0, 0, 0), thick=0.0, parent=None):
    """Turned shape (pots, vases, lamp shades): profile = [(radius, z), ...] spun around local Z."""
    bm = bmesh.new()
    rings = []
    for r, z in profile:
        if r < 1e-4:
            rings.append([bm.verts.new((0, 0, z))])
        else:
            rings.append([bm.verts.new((r * math.cos(2 * math.pi * i / segs), r * math.sin(2 * math.pi * i / segs), z))
                          for i in range(segs)])
    for a, b in zip(rings, rings[1:]):
        for i in range(segs):
            if len(a) == 1:
                bm.faces.new((a[0], b[i], b[(i + 1) % segs]))
            elif len(b) == 1:
                bm.faces.new((a[i], a[(i + 1) % segs], b[0]))
            else:
                bm.faces.new((a[i], a[(i + 1) % segs], b[(i + 1) % segs], b[i]))
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    if thick:
        sol = o.modifiers.new("Thickness", "SOLIDIFY")
        sol.thickness = thick
    return _finish(o, material, 0, None, parent)


def smooth_path(ctrl, n=6):
    """Catmull-Rom curve through control points -> list of Vectors (bent wood, cushions, drapes)."""
    P = [Vector(c) for c in ctrl]
    P = [P[0]] + P + [P[-1]]
    pts = []
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        for k in range(n):
            t = k / n
            pts.append(0.5 * (2 * p1 + (p2 - p0) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t * t
                              + (3 * p1 - p0 - 3 * p2 + p3) * t ** 3))
    pts.append(P[-2])
    return pts


def cut_path(pts, f0, f1):
    """The part of a path between two fractions of its length (for quilted cushion channels)."""
    lens = [0.0]
    for a, b in zip(pts, pts[1:]):
        lens.append(lens[-1] + (b - a).length)
    total = lens[-1]

    def at(f):
        d = f * total
        for i in range(len(pts) - 1):
            if lens[i + 1] >= d:
                t = (d - lens[i]) / max(lens[i + 1] - lens[i], 1e-9)
                return pts[i].lerp(pts[i + 1], t)
        return pts[-1]
    return [at(f0)] + [p for p, ln in zip(pts, lens) if f0 * total < ln < f1 * total] + [at(f1)]


def sweep(name, pts, width, thick, material, side=(1, 0, 0), bevel=0.004, parent=None, offset=0.0):
    """A strip of rectangular section swept along a path: bent plywood, a cushion, a draped throw.
    width runs along `side`; thick is measured across the path (offset shifts it to one side)."""
    side = Vector(side)
    bm = bmesh.new()
    rings = []
    for i, p in enumerate(pts):
        tan = (pts[min(i + 1, len(pts) - 1)] - pts[max(i - 1, 0)]).normalized()
        nrm = side.cross(tan).normalized()
        c = p + nrm * offset
        rings.append([bm.verts.new(c + side * sx * width / 2 + nrm * sn * thick / 2)
                      for sx, sn in ((-1, -1), (1, -1), (1, 1), (-1, 1))])
    for a, b in zip(rings, rings[1:]):
        for k in range(4):
            bm.faces.new((a[k], a[(k + 1) % 4], b[(k + 1) % 4], b[k]))
    bm.faces.new(list(reversed(rings[0])))
    bm.faces.new(rings[-1])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return _finish(_obj(name, bm), material, bevel, None, parent)


def tube(name, pts, r, material, r_end=None, sides=10, parent=None):
    """A smooth round tube along a path (tapering from r to r_end): plant trunks, lamp arms, cables, a dog's tail.
    r can also be a list with one radius per path point (a dog's body). Unlike a chain of rods it has no joints."""
    pts = [Vector(p) for p in pts]
    n = len(pts)
    bm = bmesh.new()
    rings, nrm = [], None
    for i, p in enumerate(pts):
        tan = (pts[min(i + 1, n - 1)] - pts[max(i - 1, 0)]).normalized()
        if nrm is None:
            nrm = tan.cross(Vector((0, 0, 1)) if abs(tan.z) < 0.9 else Vector((1, 0, 0))).normalized()
        else:                                                # carry the ring orientation along (no twisting)
            nrm = (nrm - tan * nrm.dot(tan)).normalized()
        bi = tan.cross(nrm)
        if isinstance(r, (list, tuple)):
            rr = r[min(i, len(r) - 1)]
        else:
            rr = r if r_end is None else r + (r_end - r) * i / (n - 1)
        rings.append([bm.verts.new(p + (nrm * math.cos(a) + bi * math.sin(a)) * rr)
                      for a in (2 * math.pi * k / sides for k in range(sides))])
    for a, b in zip(rings, rings[1:]):
        for k in range(sides):
            bm.faces.new((a[k], a[(k + 1) % sides], b[(k + 1) % sides], b[k]))
    bm.faces.new(list(reversed(rings[0])))
    bm.faces.new(rings[-1])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return _finish(_obj(name, bm), material, 0, None, parent)


def leaf(name, length, width, material, shape, loc, rot, fold=0.18, droop=0.12, parent=None, rib=None, edge=None,
         wave=0.0):
    """A real leaf outline (shape(t) = half-width 0..1 along the leaf), V-folded along the midrib and drooping
    towards the tip. The leaf grows along local +Y from its stalk.
    rib  = material for a pale midrib strip (fiddle-leaf fig), edge = material for a coloured margin (snake plant),
    wave = how much the margin ripples (the wavy edge of a fiddle-leaf)."""
    bm = bmesh.new()
    n = 20
    cols = (-1.0, -0.86, -0.07, 0.07, 0.86, 1.0)           # across the leaf: margin | blade | midrib | blade | margin
    strip_mat = (2, 0, 1, 0, 2) if edge else (0, 0, 1, 0, 0)
    rows = []
    for i in range(n + 1):
        t = i / n
        hw = width / 2 * shape(t) * (1 + wave * math.sin(t * 31.0))
        y, z = t * length, -droop * length * t * t
        rib_w = min(0.0025 + 0.003 * (1 - t), hw * 0.3) if hw > 1e-5 else 0.0
        row = []
        for c in cols:
            x = math.copysign(rib_w, c) if abs(c) < 0.1 else c * hw
            row.append(bm.verts.new((x, y, z - fold * abs(x) + (0.0015 if abs(c) < 0.1 else 0.0))))
        rows.append(row)
    for a, b in zip(rows, rows[1:]):
        for k in range(len(cols) - 1):
            f = bm.faces.new((a[k], a[k + 1], b[k + 1], b[k]))
            f.material_index = strip_mat[k] if (rib or edge) else 0
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-5)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    _finish(o, material, 0, None, parent)
    if rib or edge:
        o.data.materials.append(rib or material)
        o.data.materials.append(edge or material)
    return o


def soft(o, levels=1):
    """Subdivision on top of the bevel: only for soft things (cushions, pillows, a pouffe)."""
    mod = o.modifiers.new("Smooth", "SUBSURF")
    mod.levels, mod.render_levels = levels, levels
    return o


def pillow(name, w, h, t, loc, material, rot=(0, 0, 0), square=2.0, pinch=0.06, parent=None, n=12):
    """A stuffed cushion: two fabric faces sewn together at a seam, fat in the middle, with the edges pulled in
    between the corners (the 'ears' every real scatter cushion has). square > 2 gives a boxier sofa back cushion.
    w = width (x), h = height (z), t = thickness at the middle (y)."""
    bm = bmesh.new()
    faces = {}
    for side in (-1, 1):
        for i in range(n + 1):
            for j in range(n + 1):
                u, v = -1 + 2 * i / n, -1 + 2 * j / n
                puff = ((1 - abs(u) ** square) * (1 - abs(v) ** square)) ** (1 / square)
                x = u * w / 2 * (1 - pinch * (1 - v * v))
                z = v * h / 2 * (1 - pinch * (1 - u * u))
                faces[side, i, j] = bm.verts.new((x, side * (t / 2 * puff + 0.003), z))
    for side in (-1, 1):
        for i in range(n):
            for j in range(n):
                q = [faces[side, i, j], faces[side, i + 1, j], faces[side, i + 1, j + 1], faces[side, i, j + 1]]
                bm.faces.new(q if side > 0 else q[::-1])
    for i in range(n):                                       # the thin seam band where the two faces meet
        for a, b in (((i, 0), (i + 1, 0)), ((n, i), (n, i + 1)), ((i + 1, n), (i, n)), ((0, i + 1), (0, i))):
            bm.faces.new((faces[-1, a[0], a[1]], faces[-1, b[0], b[1]], faces[1, b[0], b[1]], faces[1, a[0], a[1]]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return soft(_finish(o, material, 0, None, parent))


# --------------------------------------------------------------------- furniture slots
SLOTS = {}


def slot(name, size, center_xy, z=FLOOR_Z, turn=0, kind="floor", shape="box"):
    """An empty box where furniture goes.
    size  = (width, depth, height) in the furniture's own frame; its FRONT faces local -Y.
    turn  = rotation in degrees (0 = faces the camera side / -Y, 90 = faces +X).
    z     = height of the slot's bottom.
    shape = what add_furniture.py builds here from a photo (chair, table, shelf, lamp, pet...)."""
    w, d, h = size
    e = bpy.data.objects.new(f"SLOT_{name}", None)
    e.empty_display_type = "CUBE"
    e.empty_display_size = 1.0
    e.location = (center_xy[0], center_xy[1], z + h / 2)
    e.rotation_euler = (0, 0, R(turn))
    e.scale = (w / 2, d / 2, h / 2)
    e.hide_render = True
    e.hide_viewport = not SHOW_SLOT_BOXES
    e["kit_slot"] = name
    e["kit_kind"] = kind            # floor / wall / surface / rug / hanging
    e["kit_size"] = [w, d, h]
    e["kit_shape"] = shape
    COL_SLOTS.objects.link(e)
    SLOTS[name] = e
    return e


def furniture_root(slot_name):
    """Empty at the slot's bottom-centre, rotated like the slot. Build placeholder parts
    in its local space: x = width, y = depth (front = -y), z = up from the floor."""
    s = SLOTS[slot_name]
    w, d, h = s["kit_size"]
    root = bpy.data.objects.new(f"{slot_name.capitalize()}_placeholder", None)
    root.empty_display_size = 0.2
    root.location = s.location - Vector((0, 0, h / 2))
    root.rotation_euler = s.rotation_euler
    root["kit_slot"] = slot_name
    root["kit_role"] = "placeholder"
    COL_FURN.objects.link(root)
    return root, w, d, h


# --------------------------------------------------------------------- portfolio hooks
# Hooks are where YOUR content goes. tools/build_portfolio.py fills them from profile.json:
#   picture hooks: "screen" (glows), "frame", "poster", "logo"  -> project images (in order)
#   text hooks:    "name", "role", "tagline", "title" (project titles), "skill"
#   link hooks:    any object with hook_link(obj, "email" | "github" | "linkedin" | "website")
def hook_image(kind, index, size, loc, rot=(0, 0, 0), parent=None, glow=False, default_key="cream"):
    """Flat picture surface facing local -Y. size = (width, height)."""
    w, h = size
    bm = bmesh.new()
    vs = [bm.verts.new(v) for v in ((-w / 2, 0, -h / 2), (w / 2, 0, -h / 2), (w / 2, 0, h / 2), (-w / 2, 0, h / 2))]
    face = bm.faces.new(vs)
    uv = bm.loops.layers.uv.new("UVMap")
    for loop, co in zip(face.loops, ((0, 0), (1, 0), (1, 1), (0, 1))):
        loop[uv].uv = co
    o = _obj(f"HOOK_{kind}_{index}", bm)
    o.location, o.rotation_euler = loc, rot
    o.data.materials.append(mat(default_key, 0.4, emit=0.8 if glow else 0.0))
    COL_HOOKS.objects.link(o)
    o.parent = parent
    o["kit_hook"], o["kit_hook_index"], o["kit_hook_size"], o["kit_hook_glow"] = kind, index, [w, h], glow
    return o


def hook_default(hook, *objs):
    """Mark decoration that is hidden once the hook gets a real image (e.g. a fake UI on a screen)."""
    for o in objs:
        o["kit_hook_default"] = hook.name
    return objs


def hook_text(kind, index, text, height, loc, rot=(R(90), 0, 0), material=None, max_width=1.0, parent=None,
              align="CENTER", depth=0.008):
    """3D text (faces -Y with the default rot). It is shrunk to fit max_width metres."""
    cu = bpy.data.curves.new(f"HOOK_{kind}_{index}", "FONT")
    cu.body, cu.size, cu.align_x, cu.align_y = text, height, align, "CENTER"
    cu.extrude, cu.bevel_depth = depth, depth * 0.4
    o = bpy.data.objects.new(f"HOOK_{kind}_{index}", cu)
    o.location, o.rotation_euler = loc, rot
    o.data.materials.append(material or mat("dark", 0.6))
    COL_HOOKS.objects.link(o)
    o.parent = parent
    o["kit_hook"], o["kit_hook_index"], o["kit_max_width"] = kind, index, max_width
    bpy.context.view_layer.update()
    if o.dimensions.x > max_width:
        o.scale = [max_width / o.dimensions.x] * 3
    return o


def hook_link(obj, link):
    """Make an object clickable on the exported web page (email, github, linkedin, website)."""
    obj["kit_link"] = link
    return obj


# --------------------------------------------------------------------- shared real-world props
BOOK_KEYS = ("accent_1", "accent_2", "accent_3", "cream", "main", "walnut", "dark")


def books(prefix, x0, x1, y, z, parent=None, max_h=0.27, lean_last=True):
    """A row of real books standing on a shelf from x0 to x1: varied height, thickness and colour,
    a pale page block at the top, and the last book leaning on its neighbour."""
    x = x0
    k = 0
    while x < x1 - 0.03:
        t = random.uniform(0.018, 0.045)
        h = random.uniform(0.6, 1.0) * max_h
        d = random.uniform(0.15, 0.2)
        if x + t > x1:
            break
        key = random.choice(BOOK_KEYS)
        bk = box(f"{prefix}_Book_{k}", (t, d, h), (x + t / 2, y + (0.2 - d) / 2, z + h / 2),
                 smat(key, "paper", 0.75), bevel=0.002, parent=parent)
        box(f"{prefix}_Pages_{k}", (t * 0.8, d * 0.96, 0.002), (0, 0, h / 2 + 0.0005),
            mat("cream", 0.9), bevel=0, parent=bk)
        x += t + 0.002
        k += 1
        if random.random() < 0.12:
            x += random.uniform(0.02, 0.05)        # small gaps, like a real shelf
    if lean_last and x < x1 - 0.06:
        t, h = 0.03, 0.8 * max_h
        a = R(14)
        box(f"{prefix}_Book_Lean", (t, 0.18, h), (x + math.sin(a) * h / 2 + t / 2, y, z + math.cos(a) * h / 2),
            smat(random.choice(BOOK_KEYS), "paper", 0.75), bevel=0.002, rot=(0, a, 0), parent=parent)


def fiddle_shape(t):
    """Fiddle-leaf fig outline: narrow stalk end, a 'waist' a third of the way up, broad rounded top."""
    t = min(max(t, 0.0), 1.0)
    return (math.sin(math.pi * t) ** 0.55) * (0.75 + 0.35 * t) * (1 - 0.15 * math.exp(-((t - 0.28) / 0.08) ** 2))


def sword_shape(t):
    """Snake-plant leaf outline: a long strap that narrows to a point."""
    return min(1.0, 5 * t) * (1 - t ** 3)


# =====================================================================
#  ROOM SHELL
# =====================================================================
# Floor: a base slab plus 18 cm engineered-oak boards running left to right, with staggered end joints.
box("Floor_Base", (W + T, D + T, 0.2), ((W - T) / 2, (D + T) / 2, -0.1), mat("wall_trim", 0.7), bevel=0.02)
board_mats = [smat("floor", "wood", r, scale=3.2, strength=0.42) for r in (0.42, 0.5, 0.58)]
rows = max(8, round(D / 0.18))
for j in range(rows):
    rw = D / rows
    x, k = 0.0, 0
    while x < W - 0.01:
        length = min(random.uniform(0.9, 2.1) if k else random.uniform(0.3, 1.6), W - x)
        if W - x - length < 0.35:
            length = W - x                          # no tiny offcuts at the end of a row
        box(f"Floor_Board_{j}_{k}", (length - 0.004, rw - 0.004, FLOOR_Z), (x + length / 2, rw * (j + 0.5), FLOOR_Z / 2),
            board_mats[(j * 2 + k) % 3], bevel=0.002)
        x += length
        k += 1

# Walls: smooth painted plaster. A casement window in the left wall (the late-afternoon sun comes in here).
WIN_Y = (2.4, 3.4)                  # from front to back
WIN_Z = (0.9, 2.25)
wall_mat = smat("wall", "plaster", 0.85, scale=0.25)        # very soft, large-scale paint variation
left = box("Wall_Left", (T, D + T, H), (-T / 2, (D + T) / 2, H / 2), wall_mat, bevel=0.0)
cutter = box("Window_Cutter", (T * 3, WIN_Y[1] - WIN_Y[0], WIN_Z[1] - WIN_Z[0]),
             (-T / 2, sum(WIN_Y) / 2, sum(WIN_Z) / 2), mat("wall"), bevel=0.0)
cutter.hide_render = cutter.hide_viewport = True
boolean = left.modifiers.new("Window", "BOOLEAN")
boolean.operation, boolean.object = "DIFFERENCE", cutter
bev = left.modifiers.new("Bevel", "BEVEL")
bev.width, bev.segments, bev.limit_method = 0.006, 2, "ANGLE"
box("Wall_Back", (W + T, T, H), ((W - T) / 2, D + T / 2, H / 2), wall_mat, bevel=0.006)

# Chunky oak trim on top of the walls (the kit's diorama look) and real 12 cm painted skirting boards.
oak_trim = smat("wood", "wood", 0.5, scale=1.5, strength=0.6)
box("Trim_Top_Back", (W + T + 0.06, T + 0.08, 0.12), ((W - T) / 2, D + T / 2, H + 0.06), oak_trim, bevel=0.03)
box("Trim_Top_Left", (T + 0.08, D + T + 0.06, 0.12), (-T / 2, (D + T) / 2 - 0.03, H + 0.06), oak_trim, bevel=0.03)
skirt = mat("wall_trim", 0.45)
box("Skirting_Back", (W, 0.018, 0.12), (W / 2, BACK - 0.009, FLOOR_Z + 0.06), skirt, bevel=0.003)
box("Skirting_Back_Bead", (W, 0.01, 0.012), (W / 2, BACK - 0.02, FLOOR_Z + 0.114), skirt, bevel=0.004)
box("Skirting_Left", (0.018, D, 0.12), (0.009, D / 2, FLOOR_Z + 0.06), skirt, bevel=0.003)
box("Skirting_Left_Bead", (0.01, D, 0.012), (0.02, D / 2, FLOOR_Z + 0.114), skirt, bevel=0.004)

# Retro theme: vertical walnut tongue-and-groove panelling on the back wall.
if PANEL:
    slats = round(W / 0.12)
    sw = W / slats
    for i in range(slats):
        box(f"Panel_Slat_{i}", (sw - 0.006, PANEL_T, H - FLOOR_Z), (sw * (i + 0.5), D - PANEL_T / 2, (H + FLOOR_Z) / 2),
            smat("panel", "wood", 0.45 + 0.1 * (i % 2), along="Z"), bevel=0.003)
    box("Panel_Groove_Back", (W, 0.004, H - FLOOR_Z), (W / 2, D - 0.002, (H + FLOOR_Z) / 2), mat("dark", 0.8), bevel=0)

# A wall socket and a light switch (small things that make a wall feel lived-in).
for nm, loc in (("Socket", (0.006, 2.2, FLOOR_Z + 0.3)), ("Switch", (0.006, 0.18, 1.15))):
    box(f"Wall_{nm}", (0.01, 0.086, 0.086), loc, mat("cream", 0.35, tag="plastic"), bevel=0.003)
    box(f"Wall_{nm}_Rocker", (0.006, 0.03 if nm == "Switch" else 0.05, 0.04), (0.012, loc[1], loc[2]),
        mat("cream", 0.3, tag="plastic"), bevel=0.002)

# Window: frame set into the wall, two side-hung casements under a top light, glass, a deep sill board.
wy, wz = sum(WIN_Y) / 2, sum(WIN_Z) / 2
ww, wh = WIN_Y[1] - WIN_Y[0], WIN_Z[1] - WIN_Z[0]
frame = mat("wall_trim", 0.4, tag="frame")
FX = -0.07                                           # the frame sits in the middle of the wall thickness
for nm, size, loc in [
    ("Head", (0.07, ww, 0.06), (FX, wy, WIN_Z[1] - 0.03)),
    ("Foot", (0.07, ww, 0.06), (FX, wy, WIN_Z[0] + 0.03)),
    ("Jamb_F", (0.07, 0.06, wh), (FX, WIN_Y[0] + 0.03, wz)),
    ("Jamb_B", (0.07, 0.06, wh), (FX, WIN_Y[1] - 0.03, wz)),
    ("Mullion", (0.07, 0.05, WIN_Z[1] - 1.85 - 0.06), (FX, wy, (WIN_Z[0] + 1.85) / 2 + 0.03)),
    ("Transom", (0.07, ww - 0.1, 0.05), (FX, wy, 1.85)),
]:
    box(f"Window_Frame_{nm}", size, loc, frame, bevel=0.004)
for side in (-1, 1):                                 # the two opening casements (sash frames)
    cy = wy + side * (ww / 4 - 0.006)
    sw_, sh_ = ww / 2 - 0.085, 1.85 - WIN_Z[0] - 0.11
    for nm, size, loc in [("T", (0.05, sw_, 0.045), (FX + 0.012, cy, 1.85 - 0.05)),
                          ("B", (0.05, sw_, 0.055), (FX + 0.012, cy, WIN_Z[0] + 0.085)),
                          ("S1", (0.05, 0.045, sh_), (FX + 0.012, cy - sw_ / 2 + 0.022, (1.85 + WIN_Z[0]) / 2 + 0.005)),
                          ("S2", (0.05, 0.045, sh_), (FX + 0.012, cy + sw_ / 2 - 0.022, (1.85 + WIN_Z[0]) / 2 + 0.005))]:
        box(f"Window_Sash_{nm}", size, loc, frame, bevel=0.004)
    box("Window_Handle", (0.03, 0.012, 0.08), (FX + 0.05, cy - side * (sw_ / 2 - 0.03), 1.35),
        mat("cream", 0.25, metal=0.6, tag="handle"), bevel=0.004)
box("Window_Sill", (0.13, ww + 0.1, 0.03), (-0.025, wy, WIN_Z[0] - 0.015), mat("cream", 0.4, tag="sill"), bevel=0.004)
glass = box("Window_Glass", (0.006, ww - 0.08, wh - 0.08), (FX, wy, wz), mat("sky", 0.1, emit=0.6, color="#DDEFFF"),
            bevel=0)
if hasattr(glass, "visible_shadow"):
    glass.visible_shadow = False

# Type 22 panel radiator under the window: fluted front, top grille, valves and pipes into the floor.
RAD_W, RAD_Z0, RAD_H = 0.8, FLOOR_Z + 0.15, 0.6
rad = mat("cream", 0.35, tag="radiator")
box("Radiator_Panel", (0.1, RAD_W, RAD_H), (0.09, wy, RAD_Z0 + RAD_H / 2), rad, bevel=0.008)
box("Radiator_Grille", (0.085, RAD_W - 0.04, 0.004), (0.09, wy, RAD_Z0 + RAD_H + 0.001), mat("dark", 0.6, tag="grille"),
    bevel=0)
for i in range(int(RAD_W / 0.05)):
    box(f"Radiator_Flute_{i}", (0.004, 0.006, RAD_H - 0.05), (0.141, wy - RAD_W / 2 + 0.025 + i * 0.05, RAD_Z0 + RAD_H / 2),
        mat("cream", 0.5, tag="flute"), bevel=0)
for side in (-1, 1):
    vy = wy + side * (RAD_W / 2 + 0.035)
    cyl("Radiator_Valve", 0.016, 0.07, (0.09, vy, RAD_Z0 + 0.03), rad)
    cyl("Radiator_Valve_Cap", 0.02, 0.03, (0.09, vy, RAD_Z0 + 0.08), mat("cream", 0.3, tag="valve"))
    cyl("Radiator_Pipe", 0.008, RAD_Z0 - FLOOR_Z, (0.09, vy, (RAD_Z0 + FLOOR_Z) / 2), smat("dark", "brushed", 0.3, metal=1),
        segs=12, bevel=0)

# Curtain pole (28 mm) on two brackets with ball finials, rings, and two gathered linen curtains.
ROD_Z, ROD_X = WIN_Z[1] + 0.16, 0.09
rod_len = ww + 0.6
pole = smat("dark", "brushed", 0.35, along="Y", metal=1)
cyl("Curtain_Rod", 0.014, rod_len, (ROD_X, wy, ROD_Z), pole, rot=(R(90), 0, 0), bevel=0)
for end in (-1, 1):
    ball("Curtain_Finial", 0.025, (ROD_X, wy + end * (rod_len / 2 + 0.02), ROD_Z), pole)
    rod("Curtain_Bracket", (0.0, wy + end * (rod_len / 2 - 0.08), ROD_Z), (ROD_X, wy + end * (rod_len / 2 - 0.08), ROD_Z),
        0.008, pole)
    cyl("Curtain_Bracket_Rose", 0.025, 0.01, (0.005, wy + end * (rod_len / 2 - 0.08), ROD_Z), pole, rot=(0, R(90), 0))
linen = smat("curtain", "fabric", 0.95)
for nm, y0, hem_dir in (("Front", wy - rod_len / 2 + 0.03, -1), ("Back", wy + rod_len / 2 - 0.37, 1)):
    cw, folds = 0.34, 7                     # a gathered panel, pushed open: 34 cm wide at the rings, 7 folds
    top_z, hem_z = ROD_Z - 0.03, FLOOR_Z + 0.008
    # every fold is a little different (real linen never hangs like a perfect wave)
    amps = [random.uniform(0.7, 1.25) for _ in range(folds)]
    phase2 = random.uniform(0, 6.28)
    bm = bmesh.new()
    nu, nv = folds * 10, 14
    grid = []
    for v in range(nv + 1):
        f = v / nv                                           # 0 = hem, 1 = heading
        z = hem_z + (top_z - hem_z) * f
        spread = 1 + 0.12 * (1 - f) ** 1.5                   # the panel fans out a little towards the hem
        row = []
        for u in range(nu + 1):
            s = u / nu
            k = min(int(s * folds), folds - 1)
            depth = (0.024 + 0.018 * (1 - f)) * amps[k]       # deep soft folds below, tight pleats under the rings
            x = ROD_X + 0.004 + depth * (0.5 + 0.5 * math.sin(2 * math.pi * folds * s - math.pi / 2))
            x += 0.006 * (1 - f) * math.sin(2 * math.pi * 2.3 * s + phase2)
            if f < 0.04:
                x += 0.012                                    # the hem just kisses the floor and kicks out
            y = y0 + cw / 2 + (s - 0.5) * cw * spread + hem_dir * 0.03 * (1 - f) ** 2
            row.append(bm.verts.new((x, y, z)))
        grid.append(row)
    for a, b in zip(grid, grid[1:]):
        for u in range(nu):
            bm.faces.new((a[u], a[u + 1], b[u + 1], b[u]))
    cur = _finish(_obj(f"Curtain_{nm}", bm), linen, 0, None, None)
    cur.modifiers.new("Thickness", "SOLIDIFY").thickness = 0.004
    for k in range(folds + 1):
        ry = y0 + cw * k / folds
        torus(f"Curtain_Ring_{nm}_{k}", 0.019, 0.003, (ROD_X, ry, ROD_Z), pole, rot=(R(90), 0, 0), segs=16, segs2=6)
        rod(f"Curtain_Hook_{nm}_{k}", (ROD_X + 0.004, ry, ROD_Z - 0.019), (ROD_X + 0.012, ry, top_z), 0.0018, pole, segs=6)

# 55" TV on a flat wall mount over the media console (your showreel plays here).
TV_Y, TV_Z, TV_W, TV_H = 1.15, 1.13, 1.23, 0.71
box("TV_Mount", (0.03, 0.4, 0.3), (0.015, TV_Y, TV_Z), mat("dark", 0.5, tag="mount"), bevel=0.003)
box("TV_Body", (0.045, TV_W, TV_H), (0.052, TV_Y, TV_Z), mat("dark", 0.3, tag="tv"), bevel=0.004)
box("TV_Bezel_Chin", (0.004, 0.06, 0.006), (0.076, TV_Y, TV_Z - TV_H / 2 + 0.006), mat("cream", 0.3, emit=0.4), bevel=0)
tv_screen = hook_image("screen", 1, (TV_W - 0.016, TV_H - 0.016), (0.0755, TV_Y, TV_Z), rot=(0, 0, R(90)), glow=True,
                       default_key="screen")
FACE_X = Matrix(((0, 0, 1), (0, 1, 0), (-1, 0, 0))).to_euler()   # a flat triangle facing +X, pointing +Y
hook_default(
    tv_screen,
    cyl("TV_UI_Play", 0.07, 0.004, (0.078, TV_Y + 0.015, TV_Z + 0.03), mat("cream", 0.4, emit=1.2), segs=3, bevel=0,
        rot=FACE_X),
    box("TV_UI_Bar", (0.003, TV_W - 0.3, 0.012), (0.078, TV_Y, TV_Z - TV_H / 2 + 0.09), mat("cream", 0.4, emit=0.6), bevel=0),
    box("TV_UI_Progress", (0.004, (TV_W - 0.3) * 0.38, 0.016),
        (0.079, TV_Y - (TV_W - 0.3) * 0.31, TV_Z - TV_H / 2 + 0.09), mat("accent_1", 0.4, emit=1.5), bevel=0),
    box("TV_UI_Title", (0.003, 0.32, 0.03), (0.078, TV_Y - TV_W / 2 + 0.25, TV_Z + TV_H / 2 - 0.09),
        mat("cream", 0.4, emit=0.9), bevel=0),
)

# =====================================================================
#  FURNITURE SLOTS  (same names in every template)
#  size = (width, depth, height); front of the furniture faces local -Y
# =====================================================================
slot("sofa",          (1.98, 0.99, 0.83), (1.78, D - 0.5), shape="sofa")
slot("armchair",      (0.68, 0.82, 1.0),  (3.72, 2.8), turn=-40, shape="chair")
slot("media_console", (1.8, 0.42, 0.49),  (0.21, TV_Y), turn=90, shape="cabinet")
slot("table",         (0.9, 0.55, 0.45),  (1.8, 2.45), shape="table")
slot("floor_lamp",    (0.36, 0.36, 1.85), (4.33, D - 0.27), turn=-30, shape="lamp")
slot("plant",         (0.6, 0.6, 1.6),    (0.38, D - 0.35), shape="plant")
slot("rug",           (2.4, 1.7, 0.012),  (1.85, 2.55), kind="rug", shape="rug")
slot("wall_art",      (1.75, 0.04, 1.0),  (1.78, BACK - 0.02), z=1.1, kind="wall", shape="frame")
slot("wall_shelf",    (1.15, 0.12, 0.36), (3.35, BACK - 0.06), z=1.93, kind="wall", shape="shelf")
slot("pet",           (0.7, 0.7, 0.3),    (2.6, 1.1), z=FLOOR_Z + 0.002, turn=10, shape="pet")


# =====================================================================
#  PLACEHOLDER FURNITURE  (replaced when you add your own with add_furniture.py)
# =====================================================================
def build_sofa():
    """Low, deep 3-seater (SOEDERHAMN): 6 cm slab arms, one long seat cushion, three loose back cushions."""
    root, w, d, h = furniture_root("sofa")
    cover = smat("main", "fabric", 0.92)
    legs = mat("dark", 0.5, tag="plastic_leg")
    leg_h, arm_w, arm_top = 0.05, 0.07, 0.58
    wi = w - 2 * arm_w                                       # width between the arms
    for sx in (-1, 1):
        for sy in (-1, 1):
            cyl("Sofa_Leg", 0.022, leg_h, (sx * (w / 2 - 0.1), sy * (d / 2 - 0.1), leg_h / 2), legs, r2=0.018,
                parent=root)
        box("Sofa_Arm", (arm_w, d, arm_top - leg_h), (sx * (w / 2 - arm_w / 2), 0, leg_h + (arm_top - leg_h) / 2),
            cover, bevel=0.018, parent=root)
    box("Sofa_Base", (wi, d - 0.01, 0.18), (0, 0, leg_h + 0.09), cover, bevel=0.015, parent=root)
    back_d, back_top = 0.17, 0.66
    box("Sofa_BackFrame", (wi, back_d, back_top - leg_h - 0.18), (0, d / 2 - back_d / 2, (back_top + leg_h + 0.18) / 2),
        cover, bevel=0.02, parent=root)
    seat_z0, seat_t = leg_h + 0.18, 0.17                     # seat cushion top = 40 cm, like the real sofa
    seat_d = d - back_d
    seat = box("Sofa_SeatCushion", (wi - 0.01, seat_d, seat_t), (0, -d / 2 + seat_d / 2, seat_z0 + seat_t / 2),
               cover, bevel=0.025, parent=root)
    soft(seat)
    for sz in (seat_z0 + 0.012, seat_z0 + seat_t - 0.012):  # piping along the front edges
        cyl("Sofa_Piping", 0.006, wi - 0.04, (0, -d / 2 + 0.006, sz), cover, rot=(0, R(90), 0), segs=8, bevel=0,
            parent=root)
    bw = wi / 3
    for i in (-1, 0, 1):                                     # three big, plump loose back cushions leaning on the frame
        pillow("Sofa_BackCushion", bw - 0.012, 0.5, 0.22, (i * bw, d / 2 - back_d - 0.075, seat_z0 + seat_t + 0.235),
               cover, rot=(R(-14), 0, 0), square=4.0, pinch=0.025, parent=root)
    # two 50x50 feather scatter cushions (one leaning into the corner) and a knitted throw over the right arm
    for sx, key, tilt, lean in ((-0.6, "accent_1", 12, -20), (0.56, "cream", -9, -24)):
        pillow("Sofa_Pillow", 0.48, 0.46, 0.15, (sx, d / 2 - back_d - 0.25, seat_z0 + seat_t + 0.2),
               smat(key, "fabric", 0.93), rot=(R(lean), 0, R(tilt)), parent=root)
    ax = w / 2 - arm_w / 2
    drape = smooth_path([(ax - 0.36, -0.12, seat_z0 + seat_t + 0.008), (ax - 0.12, -0.12, seat_z0 + seat_t + 0.01),
                         (ax - arm_w / 2 - 0.012, -0.12, arm_top - 0.02), (ax, -0.12, arm_top + 0.012),
                         (ax + arm_w / 2 + 0.012, -0.12, arm_top - 0.03), (ax + arm_w / 2 + 0.018, -0.12, 0.26)])
    throw = smat("accent_3", "knit", 0.96)
    sweep("Sofa_Throw", drape, 0.52, 0.018, throw, side=(0, -1, 0), bevel=0.006, parent=root)
    for k in range(13):                                       # knotted fringe along the hanging edge
        rod("Sofa_Throw_Fringe", (ax + arm_w / 2 + 0.02, -0.36 + k * 0.04, 0.26), (ax + arm_w / 2 + 0.024, -0.36 + k * 0.04, 0.2),
            0.004, throw, segs=6, parent=root)


def build_armchair():
    """POAENG: a cantilevered bent-birch frame (each side a 'C' from floor runner up into the armrest),
    a thin bent plywood seat shell hung inside it and one long tufted cushion over seat and back."""
    root, w, d, h = furniture_root("armchair")
    birch = smat("wood", "veneer", 0.4, along="Y", scale=4.5, strength=0.32)
    fx = w / 2 - 0.0275                                      # centre of each 5.5 cm wide side frame
    side_path = (
        [Vector((0, y, 0.014)) for y in (0.37, 0.1, -0.2)]
        + [Vector((0, -0.2 + 0.2 * math.cos(a), 0.214 + 0.2 * math.sin(a))) for a in (R(-110), R(-135), R(-160), R(-180))]
        + [Vector((0, -0.4, 0.3))]
        + [Vector((0, -0.22 + 0.18 * math.cos(a), 0.3 + 0.18 * math.sin(a))) for a in (R(160), R(135), R(110), R(90))]
        + [Vector((0, y, 0.48 + (y + 0.22) * 0.19)) for y in (0.0, 0.24)]
    )
    for sx in (-1, 1):
        sweep("Armchair_SideFrame", [p + Vector((sx * fx, 0, 0)) for p in side_path], 0.055, 0.028, birch,
              bevel=0.005, parent=root)
    rod("Armchair_FrontRail", (-fx, -0.375, 0.27), (fx, -0.375, 0.27), 0.014, birch, parent=root)
    box("Armchair_RearRail", (2 * fx, 0.045, 0.024), (0, 0.34, 0.03), birch, bevel=0.004, parent=root)
    shell_ctrl = [(0, -0.37, 0.27), (0, -0.33, 0.335), (0, -0.25, 0.36), (0, -0.08, 0.33), (0, 0.07, 0.29),
                  (0, 0.15, 0.33), (0, 0.22, 0.5), (0, 0.3, 0.72), (0, 0.355, 0.9), (0, 0.37, 0.97), (0, 0.355, 1.0)]
    shell = smooth_path(shell_ctrl, n=6)
    sweep("Armchair_Shell", shell, 0.56, 0.012, birch, bevel=0.003, parent=root)
    for sx in (-1, 1):                                       # armrest ends bolted to the back of the shell
        box("Armchair_Bolt", (0.06, 0.04, 0.04), (sx * (fx - 0.03), 0.245, 0.555), birch, bevel=0.004, parent=root)
    # one thick cushion in six quilted channels. Like the real one it covers the whole shell: it rolls over the
    # front lip (no bare plywood at the knees) and runs up to the top, where the headrest flap folds over.
    cushion = smat("accent_2", "fabric", 0.93)
    pad = smooth_path([(0, -0.392, 0.255)] + shell_ctrl[1:], n=8)
    cuts = (0.0, 0.17, 0.34, 0.51, 0.67, 0.83, 1.0)
    for i, (f0, f1) in enumerate(zip(cuts, cuts[1:])):     # channels overlap a little, so they read as one
        part = cut_path(pad, max(0.0, f0 - 0.012), min(1.0, f1 + 0.012))   # stitched cushion, not separate blocks
        soft(sweep(f"Armchair_Cushion_{i}", part, 0.55, 0.085, cushion, offset=0.046, bevel=0.035, parent=root), 2)
    soft(box("Armchair_Headrest", (0.5, 0.07, 0.17), (0, 0.235, 0.9), cushion, bevel=0.025, rot=(R(-17), 0, 0),
             parent=root))                                   # the folded-over headrest flap
    seam = mat("accent_2", 0.95, color=shade(COLORS["accent_2"], 0.72), tag="seam")
    lens = [0.0]
    for a, b in zip(pad, pad[1:]):
        lens.append(lens[-1] + (b - a).length)
    for f in cuts[1:-1]:                                     # sunken stitch lines between the quilted channels
        i = next(k for k, ln in enumerate(lens) if ln >= f * lens[-1])
        tan = (pad[min(i + 1, len(pad) - 1)] - pad[max(i - 1, 0)]).normalized()
        p = pad[i] + Vector((1, 0, 0)).cross(tan).normalized() * 0.084
        rod("Armchair_Seam", p + Vector((-0.25, 0, 0)), p + Vector((0.25, 0, 0)), 0.004, seam, segs=8, parent=root)


def build_media_console():
    """BESTA TV bench 180x42x39: white carcass on short legs, three 60 cm sections with oak-veneer fronts
    (door / two drawers / door), 4 mm gaps and slim bar handles. Soundbar, books and a vase on top."""
    root, w, d, h = furniture_root("media_console")
    carcass = mat("walnut" if PANEL else "cream", 0.35, tag="melamine")
    front = smat("wood", "veneer", 0.45, along="Z", scale=5.0, strength=0.4)     # oak veneer, grain runs up the fronts
    steel = smat("dark", "brushed", 0.35, metal=1)
    leg_h, body_h = 0.1, 0.39
    for sx in (-1, 1):
        for sy in (-1, 1):
            box("Console_Leg", (0.035, 0.035, leg_h), (sx * (w / 2 - 0.06), sy * (d / 2 - 0.07), leg_h / 2),
                smat("wood", "wood", 0.46, along="Z"), bevel=0.003, parent=root)
    box("Console_Carcass", (w, d - 0.02, body_h), (0, 0.01, leg_h + body_h / 2), carcass, bevel=0.003, parent=root)
    fy = -d / 2 + 0.008                                       # fronts sit proud of the carcass
    sec = w / 3
    gap = 0.004
    for i, kind in ((-1, "door"), (0, "drawers"), (1, "door")):
        cx = i * sec
        fw = sec - gap
        if kind == "door":
            box("Console_Door", (fw, 0.018, body_h - gap), (cx, fy, leg_h + body_h / 2), front, bevel=0.002, parent=root)
            hx = cx - i * (fw / 2 - 0.04)                     # handle on the opening edge, near the middle
            rod("Console_Handle", (hx, fy - 0.03, leg_h + body_h / 2 - 0.07), (hx, fy - 0.03, leg_h + body_h / 2 + 0.07),
                0.006, steel, parent=root)
            for hz in (-0.06, 0.06):
                rod("Console_Handle_Post", (hx, fy - 0.009, leg_h + body_h / 2 + hz), (hx, fy - 0.03, leg_h + body_h / 2 + hz),
                    0.004, steel, parent=root)
        else:
            dh = (body_h - 3 * gap) / 2
            for k in range(2):
                dz = leg_h + gap + dh / 2 + k * (dh + gap)
                box("Console_Drawer", (fw, 0.018, dh), (cx, fy, dz), front, bevel=0.002, parent=root)
                rod("Console_Handle", (cx - 0.07, fy - 0.03, dz + dh / 2 - 0.04), (cx + 0.07, fy - 0.03, dz + dh / 2 - 0.04),
                    0.006, steel, parent=root)
                for hx in (-0.06, 0.06):
                    rod("Console_Handle_Post", (cx + hx, fy - 0.009, dz + dh / 2 - 0.04),
                        (cx + hx, fy - 0.03, dz + dh / 2 - 0.04), 0.004, steel, parent=root)
    top = leg_h + body_h
    # soundbar under the TV (fabric grille), books, a ceramic vase with eucalyptus and a small bowl
    box("Soundbar", (0.9, 0.095, 0.06), (0, 0.04, top + 0.03), mat("dark", 0.5, tag="soundbar"), bevel=0.015,
        parent=root)
    box("Soundbar_Grille", (0.86, 0.004, 0.044), (0, -0.0085, top + 0.03), smat("dark", "fabric", 0.95),
        bevel=0.002, parent=root)
    for i, key in enumerate(("accent_2", "cream", "walnut")):
        box("Console_Book", (0.24 - i * 0.02, 0.17, 0.028), (-w / 2 + 0.24, 0.0, top + 0.014 + i * 0.029),
            smat(key, "paper", 0.75), bevel=0.002, rot=(0, 0, R(-6 + i * 7)), parent=root)
    lathe("Console_Bowl", [(0.0, 0.0), (0.04, 0.0), (0.07, 0.025), (0.08, 0.05), (0.075, 0.05), (0.065, 0.028),
                           (0.0, 0.01)], (-w / 2 + 0.24, 0.0, top + 0.087), smat("accent_1", "ceramic", 0.3),
          parent=root)
    vx = w / 2 - 0.2
    lathe("Console_Vase", [(0.0, 0.0), (0.05, 0.0), (0.065, 0.06), (0.06, 0.14), (0.03, 0.2), (0.028, 0.22),
                           (0.024, 0.22), (0.0, 0.2)], (vx, 0.02, top), smat("cream", "ceramic", 0.3), parent=root)
    for k in range(5):                                       # eucalyptus stems with little round leaves
        a = k * 1.3
        tip = (vx + math.cos(a) * 0.11, 0.02 + math.sin(a) * 0.08, top + 0.42 + 0.04 * math.sin(k * 2.1))
        rod("Console_Stem", (vx, 0.02, top + 0.2), tip, 0.003, mat("plant", 0.7), parent=root)
        for j in range(4):
            f = 0.35 + j * 0.18
            p = Vector((vx, 0.02, top + 0.2)).lerp(Vector(tip), f)
            ball("Console_Leaf", 0.018, p, mat("leaf_sage", 0.6, color="#8FA88C"), scale=(1, 0.3, 0.8), parent=root)


def build_table():
    """LACK coffee table 90x55x45: a thick 5 cm board top, 5x5 cm legs flush with the corners, a magazine shelf."""
    root, w, d, h = furniture_root("table")
    top_m = smat("wood", "wood", 0.42, scale=2.0, strength=0.5)
    legs = smat("wood", "wood", 0.43, along="Z", scale=2.0, strength=0.5)
    box("Table_Top", (w, d, 0.05), (0, 0, h - 0.025), top_m, bevel=0.003, parent=root)
    for sx in (-1, 1):
        for sy in (-1, 1):
            box("Table_Leg", (0.05, 0.05, h - 0.05), (sx * (w / 2 - 0.025), sy * (d / 2 - 0.025), (h - 0.05) / 2),
                legs, bevel=0.003, parent=root)
    box("Table_Shelf", (w - 0.1, d - 0.1, 0.022), (0, 0, 0.14), top_m, bevel=0.002, parent=root)
    # magazines on the shelf
    for i, key in enumerate(("accent_2", "cream", "accent_1")):
        box("Table_Magazine", (0.21, 0.28, 0.006), (-0.15 + i * 0.03, 0.0, 0.154 + i * 0.006), smat(key, "paper", 0.7),
            bevel=0.001, rot=(0, 0, R(80 + i * 8)), parent=root)
    # on top: a stack of books, a wooden tray with a candle, a remote and a mug (click it to email you)
    for i, key in enumerate(("walnut", "accent_3")):
        box("Table_Book", (0.26 - i * 0.03, 0.2, 0.03), (-0.2, 0.06, h + 0.015 + i * 0.031), smat(key, "paper", 0.74),
            bevel=0.002, rot=(0, 0, R(-8 + i * 12)), parent=root)
    box("Table_Tray", (0.3, 0.18, 0.012), (0.17, 0.08, h + 0.006), smat("walnut", "wood", 0.5), bevel=0.003, parent=root)
    for sx in (-1, 1):
        box("Table_Tray_Rim", (0.012, 0.18, 0.03), (0.17 + sx * 0.144, 0.08, h + 0.02), smat("walnut", "wood", 0.5),
            bevel=0.003, parent=root)
    lathe("Table_Candle_Jar", [(0.0, 0.0), (0.04, 0.0), (0.042, 0.08), (0.0, 0.07)], (0.1, 0.08, h + 0.012),
          smat("accent_3", "ceramic", 0.3), parent=root)
    box("Table_Remote", (0.045, 0.17, 0.018), (0.26, -0.15, h + 0.009), mat("dark", 0.45, tag="remote"), bevel=0.006,
        rot=(0, 0, R(18)), parent=root)
    mug = lathe("Table_Mug", [(0.0, 0.0), (0.038, 0.0), (0.042, 0.004), (0.042, 0.095), (0.037, 0.095), (0.036, 0.01),
                              (0.0, 0.01)], (0.0, -0.13, h), smat("accent_1", "ceramic", 0.3), parent=root)
    hook_link(mug, "email")
    torus("Table_Mug_Handle", 0.026, 0.0065, (0.045, -0.13, h + 0.05), smat("accent_1", "ceramic", 0.3),
          rot=(R(90), 0, 0), segs=16, parent=root)
    cyl("Table_Mug_Coffee", 0.035, 0.002, (0.0, -0.13, h + 0.08), mat("walnut", 0.2, tag="coffee"), bevel=0, parent=root)


def build_floor_lamp():
    """HEKTAR: 181 cm, heavy 34 cm base, thin pole, a bent arm and a 31.5 cm dark metal dome tilted forward."""
    root, w, d, h = furniture_root("floor_lamp")
    metal = smat("dark", "brushed", 0.45, metal=0.7, along="Z")
    lathe("FloorLamp_Base", [(0.0, 0.0), (0.168, 0.0), (0.17, 0.012), (0.15, 0.03), (0.03, 0.04), (0.0, 0.04)],
          (0, 0, 0), metal, segs=40, parent=root)
    pole_top = 1.6
    rod("FloorLamp_Pole", (0, 0, 0.04), (0, 0, pole_top), 0.011, metal, parent=root)
    cyl("FloorLamp_Switch", 0.016, 0.04, (0, 0, 1.05), metal, parent=root)
    arm = smooth_path([(0, 0, pole_top), (0, -0.03, pole_top + 0.1), (0, -0.12, pole_top + 0.17), (0, -0.2, pole_top + 0.16)])
    tube("FloorLamp_Arm", arm, 0.009, metal, sides=12, parent=root)
    hinge = Vector((0, -0.2, pole_top + 0.16))
    cyl("FloorLamp_Hinge", 0.018, 0.05, hinge, metal, rot=(0, R(90), 0), parent=root)
    shade_rot = (R(-28), 0, 0)
    shade = lathe("FloorLamp_Shade", [(0.03, 0.04), (0.04, 0.0), (0.075, -0.03), (0.11, -0.09), (0.135, -0.17),
                                      (0.15, -0.24), (0.1575, -0.27)],
                  hinge + Vector((0, -0.01, -0.02)), metal, segs=40, rot=shade_rot, thick=0.0025, parent=root)
    shade.name = "FloorLamp_Shade"
    bulb_at = hinge + Euler(shade_rot).to_matrix() @ Vector((0, 0, -0.1)) + Vector((0, -0.01, -0.02))
    bulb = ball("FloorLamp_Bulb", 0.04, bulb_at, mat("glow", 0.3, emit=6.0, color="#FFE6BC"), parent=root)
    if hasattr(bulb, "visible_shadow"):
        bulb.visible_shadow = False
    lamp = light("Light_FloorLamp", "POINT", LAMP_STRENGTH, kelvin(LAMP_WARMTH), bulb_at, size=0.05)
    lamp.parent = root                           # add_furniture.py keeps this light if you replace the lamp
    lamp.location = bulb_at
    cable = smooth_path([(0.0, 0.05, 0.03), (0.03, 0.12, 0.004), (0.02, 0.2, 0.004), (-0.05, 0.16, 0.004)])
    tube("FloorLamp_Cable", cable, 0.003, mat("dark", 0.6, tag="cable"), sides=8, parent=root)


def build_plant():
    """Fiddle-leaf fig (FICUS LYRATA): one upright trunk, big violin-shaped leaves, a glazed pot with soil."""
    root, w, d, h = furniture_root("plant")
    pot_h, pot_r = 0.3, 0.15
    lathe("Plant_Pot", [(0.0, 0.0), (pot_r - 0.03, 0.0), (pot_r - 0.02, 0.012), (pot_r, pot_h - 0.02), (pot_r + 0.008, pot_h),
                        (pot_r - 0.008, pot_h), (pot_r - 0.012, pot_h - 0.04), (0.0, pot_h - 0.04)],
          (0, 0, 0), smat("cream" if PANEL else "accent_1", "ceramic", 0.35), segs=40, parent=root)
    cyl("Plant_Soil", pot_r - 0.012, 0.01, (0, 0, pot_h - 0.025), smat("dark", "concrete", 0.95), bevel=0, parent=root)
    bark = smat("walnut", "wood", 0.7, along="Z")
    trunk = smooth_path([(0, 0, pot_h - 0.03), (0.01, 0.0, 0.6), (-0.015, 0.01, 1.0), (0.0, -0.01, 1.42)], n=5)
    tube("Plant_Trunk", trunk, 0.017, bark, r_end=0.008, parent=root)       # one smooth stem, thinner at the top
    branch = smooth_path([(0.01, 0.0, 0.8), (0.12, -0.05, 0.98), (0.18, -0.08, 1.15)], n=4)
    tube("Plant_Branch", branch, 0.01, bark, r_end=0.006, parent=root)
    # thick, glossy, dark leaves with a pale yellow-green midrib: the fiddle-leaf fig's signature
    greens = [smat("plant", "leather", 0.3, scale=0.4),
              mat("leaf_dark", 0.32, color="#3F6E3A" if THEME == "smooth" else "#4A6A31")]
    rib = mat("leaf_rib", 0.45, color="#93AE6C" if THEME == "smooth" else "#9AAA5E")
    n = 34
    for s in range(n):
        u = s / (n - 1)
        on_branch = s % 5 == 3
        path = branch if on_branch else trunk
        f = 0.3 + 0.7 * u if not on_branch else 0.4 + 0.6 * u
        p = cut_path(path, 0.0, max(0.05, min(1.0, f)))[-1]
        heading = s * 2.4 + random.uniform(-0.3, 0.3)              # golden-angle spiral so leaves do not stack
        elev = R(random.uniform(10, 45) + 15 * u)
        size = random.uniform(0.24, 0.34) * (0.85 + 0.25 * (1 - abs(u - 0.6)))
        out = Vector((math.cos(heading), math.sin(heading), 0))
        rod("Plant_Petiole", p, p + out * 0.04 + Vector((0, 0, 0.02)), 0.004, greens[0], parent=root)
        leaf("Plant_Leaf", size, size * 0.68, greens[s % 2], fiddle_shape, p + out * 0.04 + Vector((0, 0, 0.02)),
             (elev, random.uniform(-0.3, 0.3), heading - R(90)), fold=0.22, droop=0.18, parent=root, rib=rib,
             wave=0.035)


def build_rug():
    """STOCKHOLM-style flatweave: 6 mm thick, groups of thin stripes and wide plain bands, bound edges."""
    root, w, d, h = furniture_root("rug")
    base_key = "rug"
    stripe_key = "dark" if THEME == "smooth" else "cream"
    weave = smat(base_key, "fabric", 1.0, scale=0.4)
    stripe = smat(stripe_key, "fabric", 0.99, scale=0.4)
    box("Rug_Base", (w, d, 0.006), (0, 0, 0.003), weave, bevel=0.002, parent=root)
    group = [(0.035, 0.045), (0.012, 0.03), (0.06, 0.03), (0.012, 0.045), (0.035, 0.2)]   # (stripe, gap) widths
    x = -w / 2 + 0.12
    k = 0
    while x < w / 2 - 0.12:
        sw, gap = group[k % len(group)]
        sw = min(sw, w / 2 - 0.12 - x)
        box("Rug_Stripe", (sw, d - 0.02, 0.0012), (x + sw / 2, 0, 0.0062), stripe, bevel=0, parent=root)
        x += sw + gap
        k += 1
    for sy in (-1, 1):                                         # bound selvedge along the long edges
        box("Rug_Edge", (w, 0.012, 0.0014), (0, sy * (d / 2 - 0.006), 0.0062), stripe, bevel=0, parent=root)


def picture(prefix, index, fx, fz, fw, fh, frame_key, pic_key, mount, root, d, deco):
    """A real picture frame: four thin bars, a backing board, a white mount (passe-partout) and the picture."""
    bar, depth = 0.022, 0.03
    fmat = smat(frame_key, "wood", 0.45) if frame_key in ("wood", "walnut") else mat(frame_key, 0.4, tag="frame")
    y = -depth / 2 + d / 2
    box(f"{prefix}_Back", (fw - 0.01, 0.006, fh - 0.01), (fx, d / 2 - 0.004, fz), mat("dark", 0.9, tag="backing"),
        bevel=0, parent=root)
    for nm, size, loc in (("T", (fw, depth, bar), (fx, y, fz + fh / 2 - bar / 2)), ("B", (fw, depth, bar), (fx, y, fz - fh / 2 + bar / 2)),
                          ("L", (bar, depth, fh), (fx - fw / 2 + bar / 2, y, fz)), ("R", (bar, depth, fh), (fx + fw / 2 - bar / 2, y, fz))):
        box(f"{prefix}_Bar{nm}", size, loc, fmat, bevel=0.003, parent=root)
    face_y = d / 2 - depth + 0.012
    box(f"{prefix}_Mount", (fw - 2 * bar, 0.003, fh - 2 * bar), (fx, face_y, fz), smat("cream", "paper", 0.85),
        bevel=0, parent=root)
    pw, ph = fw - 2 * bar - 2 * mount, fh - 2 * bar - 2 * mount
    pic = hook_image("frame", index, (pw, ph), (fx, face_y - 0.002, fz), parent=root, default_key=pic_key)
    y2 = face_y - 0.004
    if deco == "landscape":                                  # a simple sun-and-hills print
        objs = (ball(f"{prefix}_Sun", pw * 0.11, (fx + pw * 0.18, y2, fz + ph * 0.15), mat("cream", 0.8), scale=(1, 0.04, 1),
                     parent=root),
                ball(f"{prefix}_Hill", pw * 0.42, (fx - pw * 0.12, y2, fz - ph * 0.42), mat("main" if pic_key != "main" else "cream", 0.8),
                     scale=(1, 0.04, 0.45), parent=root))
    elif deco == "arch":                                     # a mid-century arch print
        objs = (ball(f"{prefix}_Arch", min(pw, ph) * 0.26, (fx, y2, fz - ph * 0.06), mat("cream", 0.8), scale=(1, 0.04, 1),
                     parent=root),
                box(f"{prefix}_Line", (pw * 0.6, 0.003, 0.012), (fx, y2 - 0.002, fz - ph * 0.32), mat("dark", 0.8), bevel=0,
                    parent=root))
    else:                                                    # a line-drawn leaf
        objs = tuple(box(f"{prefix}_Stroke", (0.006, 0.003, ph * 0.5), (fx + (k - 1) * pw * 0.12, y2, fz),
                         mat("dark", 0.8), bevel=0, rot=(0, R((k - 1) * 25), 0), parent=root) for k in range(3))
    hook_default(pic, *objs)


def build_wall_art():
    """Salon-style frame wall over the sofa: one 50x70 frame with a 40x50 mount in the middle, four smaller frames
    around it on shared edge lines, in black, white and oak (RIBBA-type frames)."""
    root, w, d, h = furniture_root("wall_art")
    # (centre x, centre z, outer width, outer height, frame colour, picture colour, mount width, print)
    layout = [(0.0, 0.5, 0.53, 0.73, "dark", "accent_2", 0.045, "landscape"),
              (-0.585, 0.71, 0.52, 0.42, "wood", "accent_1", 0.04, "arch"),
              (0.485, 0.7, 0.32, 0.42, "cream", "main", 0.028, "leaf"),
              (-0.585, 0.25, 0.42, 0.32, "cream", "accent_3", 0.032, "leaf"),
              (0.585, 0.26, 0.52, 0.42, "wood", "accent_1", 0.04, "landscape")][:max(3, min(5, GALLERY_FRAMES))]
    for i, (fx, fz, fw, fh, fkey, pkey, mount, deco) in enumerate(layout):
        picture(f"Art_{i + 1}", i + 1, fx, fz, fw, fh, fkey, pkey, mount, root, d, deco)


def build_wall_shelf():
    """MOSSLANDA picture ledge, 115x12 cm with a front lip, holding three 31.5 cm LP sleeves (your projects)."""
    root, w, d, h = furniture_root("wall_shelf")
    ledge = mat("cream" if PANEL else "dark", 0.4, tag="ledge")
    box("Shelf_Ledge", (w, d - 0.01, 0.018), (0, 0.005, 0.009), ledge, bevel=0.002, parent=root)
    box("Shelf_Back", (w, 0.012, 0.05), (0, d / 2 - 0.006, 0.025), ledge, bevel=0.002, parent=root)
    box("Shelf_Lip", (w, 0.012, 0.035), (0, -d / 2 + 0.006, 0.0175), ledge, bevel=0.002, parent=root)
    sz = 0.315                                                # a real 12" record sleeve
    tilt = (R(-8), 0, 0)
    for i in range(3):
        cx = -w / 2 + 0.04 + sz / 2 + i * (sz + 0.035)
        cz = 0.018 + sz / 2 * math.cos(R(8))
        cy = d / 2 - 0.035 - sz / 2 * math.sin(R(8))
        key = ("accent_2", "accent_1", "main")[i]
        if i == 1:                  # a record peeking out of the middle sleeve
            cyl("Shelf_Vinyl", 0.15, 0.003, (cx + 0.06, cy + 0.008, cz + 0.02), mat("dark", 0.25, tag="vinyl"),
                rot=(R(90 - 8), 0, 0), bevel=0, segs=48, parent=root)
        box("Shelf_Sleeve", (sz, 0.004, sz), (cx, cy, cz), smat(key, "paper", 0.7), bevel=0.001, rot=tilt, parent=root)
        off = Euler(tilt).to_matrix() @ Vector((0, -0.0028, 0))
        pic = hook_image("frame", 6 + i, (sz - 0.015, sz - 0.015), (cx + off.x, cy + off.y, cz + off.z), rot=tilt,
                         parent=root, default_key=key)
        o2 = Euler(tilt).to_matrix() @ Vector((0, -0.0045, 0))
        hook_default(pic, ball("Sleeve_Disc", sz * 0.26, (cx + o2.x, cy + o2.y, cz + o2.z), mat("cream", 0.6),
                               scale=(1, 0.03, 1), parent=root))


def build_pet():
    """A small beagle-type dog asleep, curled nose-to-tail, in a 70 cm round 'donut' bolster bed."""
    root, w, d, h = furniture_root("pet")
    fur, ear = mat("pet", 0.9), mat("walnut", 0.85, tag="ear")
    muzzle = mat("pet", 0.9, color=shade(COLORS["pet"], 1.14), tag="muzzle")
    bed_key = "accent_2" if THEME == "smooth" else "accent_3"
    bed = smat(bed_key, "fabric", 0.96)
    rb = w / 2                                                 # bed radius (35 cm)
    soft(cyl("Pet_Bed_Base", rb - 0.05, 0.05, (0, 0, 0.025), bed, segs=48, bevel=0.015, parent=root))
    soft(torus("Pet_Bed_Bolster", rb - 0.075, 0.075, (0, 0, 0.075), bed, segs=48, segs2=12, parent=root))
    spin = R(-35)                                              # turn the whole dog so its face looks at the camera

    def at(a_deg, rad, z):
        a = math.radians(a_deg) + spin
        return Vector((rad * math.cos(a), rad * math.sin(a), z))

    # body: the spine curls round the bed from the hips to the shoulders; the neck carries on to the head
    angles = [15 + k * 21 for k in range(12)]                  # 15 .. 246 degrees
    spine = [at(a, 0.12, 0.125) for a in angles]
    radii = [0.07, 0.085, 0.092, 0.095, 0.095, 0.094, 0.092, 0.09, 0.086, 0.08, 0.072, 0.064]
    tube("Pet_Body", spine, radii, fur, sides=16, parent=root)
    for cap, rr in ((spine[0], radii[0]), (spine[-1], radii[-1])):
        ball("Pet_Body_End", rr, cap, fur, parent=root)
    ball("Pet_Haunch", 0.075, at(40, 0.13, 0.16), fur, scale=(1.15, 1.0, 0.75), parent=root)   # the folded hind leg
    head = at(292, 0.15, 0.17)
    fwd = Vector((math.cos(R(292 + 90) + spin), math.sin(R(292 + 90) + spin), 0))         # nose tucks towards the tail
    side = Vector((-fwd.y, fwd.x, 0))
    up = Vector((0, 0, 1))
    heading = math.atan2(fwd.y, fwd.x)
    ball("Pet_Head", 0.072, head, fur, scale=(1.1, 0.95, 0.9), parent=root).rotation_euler = (0, 0, heading)
    tube("Pet_Muzzle", [head + fwd * 0.03 - up * 0.012, head + fwd * 0.08 - up * 0.022, head + fwd * 0.118 - up * 0.03],
         0.044, muzzle, r_end=0.028, sides=14, parent=root)
    ball("Pet_Muzzle_Tip", 0.028, head + fwd * 0.118 - up * 0.03, muzzle, parent=root)
    ball("Pet_Nose", 0.014, head + fwd * 0.142 - up * 0.022, mat("dark", 0.35), parent=root)
    for sx in (-1, 1):                                         # long floppy ears, closed sleepy eyes
        e = ball("Pet_Ear", 0.05, head + side * sx * 0.066 - fwd * 0.012 - up * 0.03, ear, scale=(0.75, 0.22, 1.15),
                 parent=root)
        e.rotation_euler = (R(sx * 8), 0, heading)
        lid = ball("Pet_Eye", 0.011, head + fwd * 0.058 + side * sx * 0.036 + up * 0.03, mat("dark", 0.5, tag="eye"),
                   scale=(0.5, 1.3, 0.25), parent=root)
        lid.rotation_euler = (0, 0, heading)
        paw0 = at(250, 0.115, 0.07) + side * sx * 0.03
        paw1 = head + fwd * 0.05 + side * sx * 0.045 - up * 0.1
        tube("Pet_Leg", [paw0, paw0.lerp(paw1, 0.5) + up * 0.01, paw1], 0.026, fur, r_end=0.021, sides=10, parent=root)
        ball("Pet_Paw", 0.026, paw1 + fwd * 0.012, muzzle, scale=(1.3, 1.0, 0.7), parent=root).rotation_euler = (0, 0, heading)
    tail = [at(14, 0.12, 0.13), at(2, 0.18, 0.13), at(-12, 0.215, 0.135), at(-26, 0.225, 0.14), at(-38, 0.215, 0.145)]
    tube("Pet_Tail", smooth_path(tail, n=4), 0.026, fur, r_end=0.009, sides=10, parent=root)
    neck = spine[-1].lerp(head, 0.45)                         # a collar round the neck, between shoulders and head
    tan = (head - spine[-1]).normalized()
    torus("Pet_Collar", 0.064, 0.007, neck, mat("accent_1", 0.5, tag="collar"), rot=tan.to_track_quat("Z", "Y").to_euler(),
          segs=24, parent=root)
    ball("Pet_Tag", 0.012, neck - up * 0.068, smat("accent_3", "brushed", 0.3, metal=1), scale=(1, 0.3, 1), parent=root)


# --------------------------------------------------------------------- lights helper (used by the floor lamp too)
def light(name, kind, energy, color, loc, aim=None, size=None):
    data = bpy.data.lights.new(name, kind)
    data.energy, data.color = energy, color
    if size is not None:
        if kind == "AREA":
            data.size = size
        elif kind == "SUN":
            data.angle = size
        else:
            data.shadow_soft_size = size
    o = bpy.data.objects.new(name, data)
    o.location = loc
    if aim is not None:
        o.rotation_euler = (Vector(aim) - Vector(loc)).to_track_quat("-Z", "Y").to_euler()
    COL_LIGHT.objects.link(o)
    return o


PLACEHOLDERS = {
    "sofa": build_sofa, "armchair": build_armchair, "media_console": build_media_console, "table": build_table,
    "floor_lamp": build_floor_lamp, "plant": build_plant, "rug": build_rug, "wall_art": build_wall_art,
    "wall_shelf": build_wall_shelf, "pet": build_pet,
}
if SHOW_PLACEHOLDER_FURNITURE:
    for slot_name, build in PLACEHOLDERS.items():
        build()


# =====================================================================
#  ROOM DECOR (not slots): low bookcase, letter board, snake plant, pouffe
# =====================================================================
# BILLY 80x28x106 bookcase against the back wall: 16 mm panels, plinth, fixed + adjustable shelf,
# shelf-pin holes and a thin back panel. Click it for your GitHub.
BC_X, BC_W, BC_D, BC_H = 3.35, 0.8, 0.28, 1.06
bookcase = bpy.data.objects.new("Bookcase", None)
bookcase.location = (BC_X, BACK - BC_D / 2, FLOOR_Z)
COL_ROOM.objects.link(bookcase)
hook_link(bookcase, "github")
bc_mat = smat("wood", "veneer", 0.4, along="Z") if PANEL else mat("cream", 0.35, tag="melamine")
bc_mat_h = smat("wood", "veneer", 0.41) if PANEL else bc_mat
pt = 0.016
for sx in (-1, 1):
    box("Bookcase_Side", (pt, BC_D, BC_H), (sx * (BC_W / 2 - pt / 2), 0, BC_H / 2), bc_mat, bevel=0.002, parent=bookcase)
    for k in range(9):                                        # shelf-pin holes
        box("Bookcase_PinHole", (0.002, 0.005, 0.005), (sx * (BC_W / 2 - pt - 0.0008), -BC_D / 2 + 0.04, 0.2 + k * 0.08),
            mat("dark", 0.9, tag="hole"), bevel=0, parent=bookcase)
box("Bookcase_Top", (BC_W, BC_D, pt), (0, 0, BC_H - pt / 2), bc_mat_h, bevel=0.002, parent=bookcase)
box("Bookcase_Plinth", (BC_W - 2 * pt, pt, 0.06), (0, -BC_D / 2 + 0.03, 0.03), bc_mat_h, bevel=0.002, parent=bookcase)
box("Bookcase_Bottom", (BC_W - 2 * pt, BC_D - 0.01, pt), (0, 0, 0.06 + pt / 2), bc_mat_h, bevel=0.002, parent=bookcase)
SHELF_Z = 0.55
box("Bookcase_Shelf", (BC_W - 2 * pt - 0.002, BC_D - 0.02, pt), (0, -0.005, SHELF_Z), bc_mat_h, bevel=0.002,
    parent=bookcase)
box("Bookcase_BackPanel", (BC_W - 0.004, 0.003, BC_H - 0.01), (0, BC_D / 2 - 0.0015, BC_H / 2), mat("cream", 0.6, tag="hdf"),
    bevel=0, parent=bookcase)
books("Bookcase_Low", -BC_W / 2 + pt + 0.01, BC_W / 2 - pt - 0.02, -0.02, 0.06 + pt, parent=bookcase, max_h=0.32)
books("Bookcase_Mid", -BC_W / 2 + pt + 0.01, BC_W / 2 - pt - 0.18, -0.02, SHELF_Z + pt / 2, parent=bookcase, max_h=0.27)
for i, key in enumerate(("accent_1", "cream", "accent_2")):  # a few books lying flat with a ceramic pot on top
    box("Bookcase_FlatBook", (0.17, 0.22, 0.03), (BC_W / 2 - pt - 0.095, -0.02, SHELF_Z + pt / 2 + 0.015 + i * 0.031),
        smat(key, "paper", 0.74), bevel=0.002, rot=(0, 0, R(3 - i * 4)), parent=bookcase)
lathe("Bookcase_Pot", [(0.0, 0.0), (0.04, 0.0), (0.055, 0.09), (0.0, 0.08)],
      (BC_W / 2 - pt - 0.095, -0.02, SHELF_Z + pt / 2 + 0.093), smat("cream", "ceramic", 0.3), parent=bookcase)
for k in range(6):                                            # a little trailing pothos
    a = k * 1.05
    leaf("Bookcase_Pothos", 0.07, 0.05, mat("plant", 0.5), fiddle_shape,
         (BC_W / 2 - pt - 0.095 + math.cos(a) * 0.03, -0.02 + math.sin(a) * 0.03, SHELF_Z + pt / 2 + 0.18),
         (R(-30 - 10 * (k % 2)), 0, a - R(90)), parent=bookcase)
# on top of the bookcase: a small stack of books and a candle (kept low so the letter board stays clear)
for i, key in enumerate(("main", "walnut")):
    box("Bookcase_TopBook", (0.2, 0.15, 0.03), (-0.22, -0.03, BC_H + 0.015 + i * 0.031), smat(key, "paper", 0.73),
        bevel=0.002, rot=(0, 0, R(5 - i * 9)), parent=bookcase)
lathe("Bookcase_Candle", [(0.0, 0.0), (0.035, 0.0), (0.036, 0.1), (0.0, 0.095)], (0.25, -0.02, BC_H),
      smat("accent_3", "ceramic", 0.3), parent=bookcase)

# Felt letter board in an oak frame on the wall above the bookcase (your name + role). Click it for your website.
LB_X, LB_Z, LB_W, LB_H = BC_X, 1.5, 0.8, 0.55
lb_frame = smat("wood", "wood", 0.44, scale=2.0, strength=0.6)
board = box("LetterBoard_Frame", (LB_W, 0.03, LB_H), (LB_X, BACK - 0.015, LB_Z), lb_frame, bevel=0.004)
hook_link(board, "website")
box("LetterBoard_Felt", (LB_W - 0.05, 0.004, LB_H - 0.05), (LB_X, BACK - 0.032, LB_Z), smat("dark", "fabric", 0.97),
    bevel=0)
for k in range(17):                                            # the ribbed grooves letters slot into
    box("LetterBoard_Groove", (LB_W - 0.06, 0.002, 0.003), (LB_X, BACK - 0.0345, LB_Z - LB_H / 2 + 0.04 + k * 0.028),
        mat("dark", 1.0, tag="groove"), bevel=0)
hook_text("name", 1, "YOUR NAME", 0.12, (LB_X, BACK - 0.04, LB_Z + 0.07), material=mat("cream", 0.5, emit=0.15),
          max_width=LB_W - 0.12, depth=0.004)
hook_text("role", 1, "your role", 0.07, (LB_X, BACK - 0.04, LB_Z - 0.11), material=mat("accent_3", 0.5, emit=0.1),
          max_width=LB_W - 0.14, depth=0.004)

# Snake plant (SANSEVIERIA) in a cylinder pot by the end of the TV bench.
SP_X, SP_Y = 0.3, 2.24
lathe("SnakePlant_Pot", [(0.0, 0.0), (0.1, 0.0), (0.11, 0.24), (0.1, 0.24), (0.098, 0.2), (0.0, 0.2)], (SP_X, SP_Y, FLOOR_Z),
      smat("dark" if THEME == "smooth" else "cream", "ceramic", 0.35), segs=36)
cyl("SnakePlant_Soil", 0.098, 0.01, (SP_X, SP_Y, FLOOR_Z + 0.215), smat("dark", "concrete", 0.95), bevel=0)
snake = [smat("plant", "leather", 0.4, scale=0.3), mat("snake_dark", 0.4, color="#3F6B3A" if THEME == "smooth" else "#466430")]
snake_edge = mat("snake_edge", 0.45, color="#D8CB78")           # the yellow margin of the common 'Laurentii' form
for k in range(9):
    a = k * 2.4
    rr = 0.02 + 0.05 * random.random()
    length = random.uniform(0.38, 0.62)
    leaf("SnakePlant_Leaf", length, 0.06, snake[k % 2], sword_shape,
         (SP_X + math.cos(a) * rr, SP_Y + math.sin(a) * rr, FLOOR_Z + 0.215),
         (R(90 - random.uniform(2, 14)), 0, a - R(90)), fold=-0.25, droop=0.02, edge=snake_edge)

# A chunky knitted pouffe (SANDARED-type, 45 x 33 cm) used as a footrest in front of the armchair: a soft drum
# with a domed top. The cable-knit braids are part of the surface: they bulge out round the middle, wiggle like
# a twisted cable and flatten into the top and bottom seams, like the real hand-knitted cover.
PF_X, PF_Y = 3.22, 2.2
knit = smat("cream" if THEME == "smooth" else "accent_1", "knit", 0.98)
pf_profile = [(0.19, 0.0), (0.215, 0.02), (0.225, 0.08), (0.226, 0.26), (0.215, 0.32), (0.19, 0.35), (0.12, 0.365)]
pf_profile = smooth_path([(r, 0, z) for r, z in pf_profile], n=12)       # many rows so the braids wiggle smoothly
bm = bmesh.new()
segs, cables = 144, 14
pf_rings = []
for p in pf_profile:
    r0, z = p.x, p.z
    lift = max(0.0, math.sin(math.pi * min(1.0, z / 0.33))) ** 0.7       # braids fade into the seams
    ring = []
    for i in range(segs):
        a = 2 * math.pi * i / segs
        a2 = a + 0.03 * math.sin(z * 70)                                 # the twist of a cable stitch
        bulge = 0.024 * lift * max(0.0, math.cos(cables * a2)) ** 1.2 - 0.006 * lift
        ring.append(bm.verts.new(((r0 + bulge) * math.cos(a), (r0 + bulge) * math.sin(a), z)))
    pf_rings.append(ring)
bottom, top = bm.verts.new((0, 0, 0)), bm.verts.new((0, 0, 0.37))
for a, b in zip(pf_rings, pf_rings[1:]):
    for i in range(segs):
        bm.faces.new((a[i], a[(i + 1) % segs], b[(i + 1) % segs], b[i]))
for i in range(segs):
    bm.faces.new((pf_rings[0][(i + 1) % segs], pf_rings[0][i], bottom))
    bm.faces.new((pf_rings[-1][i], pf_rings[-1][(i + 1) % segs], top))
bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
pouf = _finish(_obj("Pouf", bm), knit, 0, None, None)
pouf.location = (PF_X, PF_Y, FLOOR_Z)
pouf.scale.z = 0.33 / 0.37                                             # the real one is 33 cm high

# A round metal tray side table (GLADOM-type, 45 cm across, 53 cm high) by the armchair, with a book and a vase.
GT_X, GT_Y, GT_H = 4.28, 2.25, 0.53
tray_m = smat("cream" if THEME == "smooth" else "accent_2", "brushed", 0.4, metal=0.25)
lathe("SideTable_Tray", [(0.0, 0.0), (0.215, 0.0), (0.225, 0.004), (0.225, 0.045), (0.219, 0.045), (0.21, 0.008),
                         (0.0, 0.008)], (GT_X, GT_Y, FLOOR_Z + GT_H - 0.045), tray_m, segs=48)
for k in range(3):                                             # three splayed tube legs joined by a ring
    a = R(30 + 120 * k)
    top_p = (GT_X + 0.14 * math.cos(a), GT_Y + 0.14 * math.sin(a), FLOOR_Z + GT_H - 0.045)
    foot = (GT_X + 0.19 * math.cos(a), GT_Y + 0.19 * math.sin(a), FLOOR_Z)
    rod("SideTable_Leg", foot, top_p, 0.009, tray_m)
torus("SideTable_Ring", 0.155, 0.005, (GT_X, GT_Y, FLOOR_Z + 0.2), tray_m)
gt_top = FLOOR_Z + GT_H - 0.037
box("SideTable_Book", (0.15, 0.21, 0.025), (GT_X - 0.04, GT_Y - 0.03, gt_top + 0.0125), smat("accent_1", "paper", 0.74),
    bevel=0.002, rot=(0, 0, R(22)))
lathe("SideTable_Vase", [(0.0, 0.0), (0.03, 0.0), (0.04, 0.04), (0.03, 0.09), (0.014, 0.12), (0.016, 0.135),
                         (0.012, 0.135), (0.0, 0.12)], (GT_X + 0.09, GT_Y + 0.07, gt_top), smat("cream", "ceramic", 0.3))
for k in range(3):                                             # a few dried grass stems
    tip = (GT_X + 0.09 + 0.06 * math.cos(k * 2.1), GT_Y + 0.07 + 0.05 * math.sin(k * 2.1), gt_top + 0.34 + 0.03 * k)
    rod("SideTable_Stem", (GT_X + 0.09, GT_Y + 0.07, gt_top + 0.12), tip, 0.002, mat("accent_3", 0.8, tag="grass"))
    ball("SideTable_Seedhead", 0.012, tip, mat("accent_3", 0.9, tag="grass"), scale=(0.6, 0.6, 2.2))

# A coiled seagrass belly basket (40 cm, the kind sold for blankets and toys) holding two rolled throws,
# parked beside the reading corner.
SB_X, SB_Y = 4.22, 1.62
grass = smat("wood", "knit", 0.9, scale=0.7)
belly = [(0.15, 0.012), (0.18, 0.05), (0.2, 0.11), (0.205, 0.17), (0.2, 0.23), (0.19, 0.29), (0.18, 0.34)]
belly = smooth_path([(r, 0, z) for r, z in belly], n=4)
cyl("Basket_Bottom", 0.15, 0.012, (SB_X, SB_Y, FLOOR_Z + 0.006), grass, segs=40, bevel=0.004)
for k, p in enumerate(belly):                                  # one coil of rope per row
    torus(f"Basket_Coil_{k}", p.x, 0.011, (SB_X, SB_Y, FLOOR_Z + p.z), grass, segs=40, segs2=8)
lathe("Basket_Inside", [(0.0, 0.02), (0.17, 0.02), (0.185, 0.33)], (SB_X, SB_Y, FLOOR_Z), mat("walnut", 0.9, tag="basket"),
      segs=40)
for sx in (-1, 1):                                             # rope loop handles
    torus("Basket_Handle", 0.045, 0.009, (SB_X + sx * 0.18, SB_Y, FLOOR_Z + 0.34), grass, rot=(R(90), 0, R(90)), segs=20)
for k, (key, tilt, dz) in enumerate((("accent_1", 9, 0.0), ("cream", -7, 0.04))):   # standing up, leaning apart
    roll = soft(cyl(f"Basket_Throw_{k}", 0.068, 0.42, (SB_X - 0.07 + k * 0.13, SB_Y + 0.03 - k * 0.05, FLOOR_Z + 0.25 + dz),
                    smat(key, "knit", 0.97), segs=24, bevel=0.02, rot=(R(tilt), R(-12 + 24 * k), 0)))
    roll.name = f"Basket_Throw_{k}"


# =====================================================================
#  LIGHTS, WORLD, CAMERA, RENDER
# =====================================================================
# Light values per theme: retro70s gets a slightly cooler, softer sun so mustard/orange/teal stay clean.
sun_k, sun_s = (SUN_WARMTH, SUN_STRENGTH) if THEME == "smooth" else (SUN_WARMTH + 600, SUN_STRENGTH * 0.85)
# Low late-afternoon sun through the window, a big soft fill from the camera side, the TV glow, a warm bounce.
light("Light_Sun", "SUN", sun_s, kelvin(sun_k), (-3, wy + 0.9, 3.2), aim=(1.6, wy - 0.9, 0), size=R(3))
light("Light_Fill", "AREA", 250 * (W * D / 16), kelvin(5600), (W + 3, -3, H + 2.5), aim=(W / 2, D / 2, 0.6), size=6)
light("Light_TV", "AREA", TV_GLOW, lin(COLORS["screen"])[:3], (0.3, TV_Y, TV_Z), aim=(2.0, TV_Y, TV_Z - 0.4),
      size=1.0)
light("Light_Bounce", "AREA", 45, kelvin(LAMP_WARMTH), (W / 2, D / 2, H - 0.1), aim=(W / 2, D / 2, 0), size=2.5)

# World: the camera sees the flat background colour; the room is lit by a soft warm ambient.
world = bpy.data.worlds.get("RoomKit_World") or bpy.data.worlds.new("RoomKit_World")
scene.world = world
if bpy.app.version < (5, 0, 0):
    world.use_nodes = True
wn, wl = world.node_tree.nodes, world.node_tree.links
wn.clear()
out = wn.new("ShaderNodeOutputWorld")
bg_cam = wn.new("ShaderNodeBackground")
bg_cam.inputs["Color"].default_value = lin(COLORS["background"])
bg_cam.inputs["Strength"].default_value = 1.0
bg_amb = wn.new("ShaderNodeBackground")
bg_amb.inputs["Color"].default_value = (*kelvin(6000), 1)
bg_amb.inputs["Strength"].default_value = 0.35
path = wn.new("ShaderNodeLightPath")
mix = wn.new("ShaderNodeMixShader")
wl.new(path.outputs["Is Camera Ray"], mix.inputs["Fac"])
wl.new(bg_amb.outputs[0], mix.inputs[1])
wl.new(bg_cam.outputs[0], mix.inputs[2])
wl.new(mix.outputs[0], out.inputs["Surface"])

# Orthographic camera that frames the whole room automatically.
cam_data = bpy.data.cameras.new("Camera")
cam_data.type = "ORTHO"
cam = bpy.data.objects.new("Camera", cam_data)
scene.collection.objects.link(cam)
scene.camera = cam
cam.rotation_euler = Euler((R(90 - CAMERA_HEIGHT_ANGLE), 0, R(CAMERA_TURN)))
rot = cam.rotation_euler.to_matrix()
right, up, back = rot.col[0], rot.col[1], rot.col[2]
corners = [Vector((x, y, z)) for x in (-T, W) for y in (0, D + T) for z in (-0.2, H + 0.12)]
xs = [c.dot(right) for c in corners]
ys = [c.dot(up) for c in corners]
aspect = RESOLUTION[0] / RESOLUTION[1]
cam_data.ortho_scale = max(max(xs) - min(xs), (max(ys) - min(ys)) * aspect) * 1.06
center = right * (max(xs) + min(xs)) / 2 + up * (max(ys) + min(ys)) / 2
cam.location = center + back * 30
cam_data.clip_end = 100

# Render settings (Eevee). Engine names differ between Blender versions, so try each.
for engine in ("BLENDER_EEVEE_NEXT", "BLENDER_EEVEE"):
    try:
        scene.render.engine = engine
        break
    except TypeError:
        continue
scene.render.resolution_x, scene.render.resolution_y = RESOLUTION
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = "PNG"
ee = scene.eevee
for attr, value in (("taa_render_samples", RENDER_SAMPLES), ("use_raytracing", True), ("use_shadows", True),
                    ("shadow_ray_count", 2), ("use_gtao", True), ("use_soft_shadows", True)):
    if hasattr(ee, attr):
        setattr(ee, attr, value)
if hasattr(ee, "ray_tracing_options"):
    ee.ray_tracing_options.resolution_scale = "2" if "2" in [i.identifier for i in
        type(ee.ray_tracing_options).bl_rna.properties["resolution_scale"].enum_items] else ee.ray_tracing_options.resolution_scale
scene.view_settings.view_transform = "Standard"   # keeps your hex colours exactly as typed
scene.view_settings.exposure = -0.15

# Remember the style so add_furniture.py can match colours later.
scene["kit_style"] = STYLE
scene["kit_version"] = KIT_VERSION
scene["kit_palette"] = json.dumps(COLORS)
scene["kit_material_finish"] = json.dumps({"roughness": 0.75, "bevel": 0.006, "saturation": 0.7})
scene["kit_theme"] = THEME
scene["kit_bounds"] = [-T, 0.0, -0.2, W, D + T, H + 0.12]   # used to re-frame the camera for social sizes
scene["kit_furniture_colors"] = json.dumps(["main", "accent_1", "accent_2", "accent_3", "cream", "wood", "walnut",
                                            "plant", "dark"])   # colours add_furniture.py may use


# =====================================================================
#  SAVE AND RENDER
# =====================================================================
def output_folder():
    if OUTPUT_FOLDER:
        return os.path.expanduser(OUTPUT_FOLDER)
    here = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else ""
    if here and os.path.isdir(here) and os.access(here, os.W_OK):
        return os.path.join(here, "output")
    return os.path.join(os.path.expanduser("~"), "RoomKit_output")


folder = output_folder()
os.makedirs(folder, exist_ok=True)
scene.render.filepath = os.path.join(folder, f"{ROOM_NAME}.png")
blend_path = os.path.join(folder, f"{ROOM_NAME}.blend")

if bpy.app.background:
    bpy.ops.wm.save_as_mainfile(filepath=blend_path)
    print(f"[RoomKit] saved {blend_path}")
    if os.environ.get("ROOMKIT_BUILD_ONLY") != "1":          # build_portfolio.py renders by itself
        bpy.ops.render.render(write_still=True)
        print(f"[RoomKit] rendered {scene.render.filepath}")
else:
    for area in bpy.context.screen.areas:          # show the room through the camera
        if area.type == "VIEW_3D":
            space = area.spaces.active
            space.region_3d.view_perspective = "CAMERA"
            space.shading.type = "MATERIAL"
    print("[RoomKit] room built - press F12 to render, then Image > Save As")
