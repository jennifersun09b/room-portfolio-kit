"""
3D ROOM PORTFOLIO KIT  -  Template: DEVELOPER HOME OFFICE
=========================================================
Builds a real-looking developer home-office corner (a sit/stand desk with two monitors on an arm, a mesh
office chair, a white drawer unit, a cube shelf, a pegboard and a cork board) and renders a 1920x1080 image.
Every piece is modelled on a real product you can buy or have seen - see REFERENCES below.

HOW TO RUN
  Option A (no Blender UI):   blender -b -P dev_office.py
  Option B (inside Blender):  Scripting tab > Open > dev_office.py > Run Script (then F12 to render)

You only need to edit the SETTINGS block below. Everything under it builds the room.
Output: output/dev_office.png and output/dev_office.blend next to this script.
"""

# REFERENCES  (product names live only here and in research/dev_office.md - never in the scene)
#   desk      IKEA IDÅSEN sit/stand desk 160x80, top 160x80x2.5 cm at 75 cm, T-legs 70 cm feet
#             https://www.ikea.com/gb/en/p/idasen-desk-sit-stand-brown-beige-s89280969/
#   cabinet   IKEA ALEX drawer unit 36x58x70 cm, 5 drawers, cut-out grips
#             https://www.ikea.com/no/en/p/alex-drawer-unit-white-00473546/
#   chair     Mesh task chair, IKEA MARKUS / Herman Miller Aeron size B type: seat 47 cm, 5-star base, twin casters
#             https://www.ikea.com/us/en/p/markus-office-chair-vissle-dark-gray-50588804
#             https://www.hermanmiller.com/products/seating/office-chairs/aeron-chair/specs/
#   monitor   2x 24-inch monitors (panel 53x30 cm) on a dual side-by-side clamp arm (Ergotron LX Dual type),
#             each screen turned in 9 degrees towards the chair
#             https://www.adorama.com/egt45491216.html
#   keyboard  Tenkeyless 87-key mechanical keyboard 36x13 cm, 19 mm key pitch, on a 80x35 cm felt desk mat
#             https://voltcave.com/keyboard-sizes/
#   lamp      IKEA TERTIAL work lamp: 17 cm shade, desk clamp, sprung arms
#             https://www.ikea.com/ee/en/p/tertial-work-lamp-white-70355455/
#   shelf     IKEA KALLAX 2x4 shelving unit 77x39x147 cm, 4 cm frame, 33.5 cm cubes, fabric boxes
#             https://www.ikea.com/no/en/p/kallax-shelving-unit-white-80275887
#   pegboard  IKEA SKÅDIS pegboard 76x56 cm with shelf, cups and hook
#             https://www.ikea.com/ch/en/p/skadis-pegboard-beige-pink-00605995
#   board     Cork notice board with pine frame 90x60 cm
#             https://backtotheoffice.co.uk/products/bi-office-cork-noticeboard-pine-wood-frame-900x600mm
#   sign      Felt letter board with oak frame 78x52 cm (name + role in white letters)
#   clock     IKEA PLUTTIS wall clock, 28 cm, black rim, white face
#             https://www.ikea.com/de/en/p/pluttis-wall-clock-black-10540847
#   wall_art  IKEA RIBBA frames with mount: 52x42 cm (landscape) and 32x42 cm
#             https://www.ikea.com/my/en/p/ribba-frame-white-00378460
#   plant     IKEA Monstera deliciosa, 24 cm pot, ~75 cm tall
#             https://www.ikea.com/gb/en/p/monstera-deliciosa-potted-plant-swiss-cheese-plant-50515493/
#   rug       Flatwoven rug 160x230 cm with striped ends and fringes (IKEA LOHALS / TIPHEDE type)
#             https://www.ikea.com/nl/en/p/lohals-rug-flatwoven-natural-50277393/
#   side tbl  IKEA LACK side table 55x55x45 cm
#             https://www.ikea.com/ee/en/p/lack-side-table-white-30449908/
#   radiator  Type 22 steel panel radiator 100x60x10 cm with thermostatic valve
#             https://www.wickes.co.uk/Type-22-Double-Panel-Compact-Radiator---White-600-x-1000mm/p/176238
#   armchair  IKEA POÄNG armchair 68x82x100 cm, seat 42 cm: bentwood birch-veneer runners, cantilevered seat
#             frame hanging from the armrest fronts, one channel-stitched cushion
#             https://www.ikea.gr/en/products/poang-armchair/19197775
#   pouffe    Hand-knitted round pouffe 45 cm x 35 cm with chunky vertical cable ribs (decor, no brand)
#   pc        White glass-side mid-tower PC case (NZXT H5 Flow type) 22.5x43x46.5 cm: PSU shroud, lit fans, GPU
#             https://support.nzxt.com/hc/en-us/articles/40225168535451-H5-Flow-2024-Specs
#   floor     Engineered oak boards 19 cm wide, staggered joints

# =====================================================================
#  SETTINGS  -  change these lines, then run the script again
# =====================================================================
ROOM_NAME = "dev_office"            # used for the output file names

ROOM_WIDTH = 4.0                    # metres, left to right
ROOM_DEPTH = 4.0                    # metres, front to back
WALL_HEIGHT = 2.8                   # metres

THEME = "daylight"                  # pick one of the colour themes below
THEMES = {                          # any hex colour works; "main" is the room's hero colour
    # The "night" theme also switches the lights (moonlight, brighter lamp and screens) - see LIGHTS below.
    # Extra keys: screen (monitor default), sky (window), metal (steel), cork, pet (cat fur),
    #             frame (desk legs + monitor arm), felt (letter board).
    "daylight": {
        "background": "#DCE7F0", "wall": "#F2EEE7", "wall_trim": "#E3D8C8", "floor": "#D2B188",
        "wood": "#C9A276", "main": "#8FB8DE", "accent_1": "#E07F5F", "accent_2": "#CFE3F5",
        "accent_3": "#F4D27A", "cream": "#F6F4EF", "plant": "#4F8F57", "dark": "#2B2F36",
        "screen": "#26303F", "sky": "#CFE3F5", "metal": "#BFC6CE", "cork": "#B98A5E", "pet": "#E2A469",
        "frame": "#E4E0D8", "felt": "#2A2A2D",
    },
    "japandi": {
        "background": "#ECE5DA", "wall": "#E5DCCF", "wall_trim": "#B8A792", "floor": "#D3BC9A",
        "wood": "#C6A27C", "main": "#D9CDB8", "accent_1": "#8A6E58", "accent_2": "#A4AD8C",
        "accent_3": "#BE9277", "cream": "#F1EADD", "plant": "#6E7F58", "dark": "#3F3A35",
        "screen": "#3F3A35", "sky": "#EDEBE2", "metal": "#A99C8C", "cork": "#B89A70", "pet": "#C9A27E",
        "frame": "#3F3A35", "felt": "#3A3631",
    },
    "night": {
        "background": "#1E2433", "wall": "#E9E2D6", "wall_trim": "#C9B9A0", "floor": "#C4A47C",
        "wood": "#B8936A", "main": "#7FA8D4", "accent_1": "#F29B7E", "accent_2": "#B9D3EE",
        "accent_3": "#F3CD7A", "cream": "#F4EFE6", "plant": "#4E8E5B", "dark": "#2A303C",
        "screen": "#1C2433", "sky": "#1B2640", "metal": "#AEB7C2", "cork": "#B58C62", "pet": "#E39C62",
        "frame": "#30343C", "felt": "#26272B",
    },
}

SUN_WARMTH = 5200                   # Kelvin: 2500 = sunset orange, 6500 = white daylight
SUN_STRENGTH = 4.0                  # afternoon sun through the window
LAMP_WARMTH = 2900                  # Kelvin of the desk lamp
LAMP_STRENGTH = 18                  # Watts
SCREEN_GLOW = 0.9                   # how brightly the two monitors shine (0.6 - 1.0 looks best in daylight)
SEED = 7                            # change to shuffle books, sticky notes, code lines and small props

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
NIGHT = THEME == "night"

STYLE = "dev_office"
KIT_VERSION = 2
W, D, H = ROOM_WIDTH, ROOM_DEPTH, WALL_HEIGHT
T = 0.15            # wall thickness
FLOOR_Z = 0.02      # top of the oak floor boards; furniture stands here
DESK_H = 0.75       # sit/stand desk at sitting height
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
    """Lighter (f > 1) or darker (f < 1) version of a hex colour."""
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


def mat(key, rough=0.6, emit=0.0, metal=0.0, color=None):
    """Material from a COLORS key (or a hex via color=)."""
    hex_color = color or COLORS[key]
    name = f"M_{key}_{rough}_{emit}_{metal}_{hex_color}"
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


def see_through(key, alpha, rough=0.7):
    """Partly transparent material (the chair's mesh back): you can see the room through it."""
    m = mat(key, rough).copy()
    m.name = f"M_{key}_mesh"
    _set(_principled(m), ["Alpha"], alpha)
    if hasattr(m, "surface_render_method"):
        m.surface_render_method = "DITHERED"
    elif hasattr(m, "blend_method"):
        m.blend_method = "HASHED"
    return m


# --------------------------------------------------------------------- mesh helpers
def _finish(o, material, bevel, coll, parent):
    o.data.materials.append(material)
    if bevel:
        mod = o.modifiers.new("Bevel", "BEVEL")
        mod.width = bevel
        mod.segments = 3 if bevel >= 0.008 else 2
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
    """Box with small rounded edges. size = (x, y, z) in metres, loc = centre."""
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=Vector(size), verts=bm.verts)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, min(bevel, min(size) * 0.45), coll, parent)


def boxes(name, items, material, bevel=0.0, loc=(0, 0, 0), rot=(0, 0, 0), coll=None, parent=None):
    """Many boxes in ONE object (key caps, floor boards, pegboard slots). items = [(size, centre), ...]."""
    bm = bmesh.new()
    for size, centre in items:
        verts = bmesh.ops.create_cube(bm, size=1.0)["verts"]
        bmesh.ops.scale(bm, vec=Vector(size), verts=verts)
        bmesh.ops.translate(bm, vec=Vector(centre), verts=verts)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, bevel, coll, parent)


def cyl(name, r, h, loc, material, r2=None, segs=32, bevel=0.003, rot=(0, 0, 0), coll=None, parent=None):
    """Cylinder (or tapered cylinder with r2). loc = centre."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=segs, radius1=r, radius2=r if r2 is None else r2, depth=h)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, bevel, coll, parent)


def ball(name, r, loc, material, scale=(1, 1, 1), coll=None, parent=None):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=24, v_segments=14, radius=r)
    o = _obj(name, bm)
    o.location, o.scale = loc, scale
    return _finish(o, material, 0, coll, parent)


def rod(name, a, b, r, material, parent=None, segs=12):
    """A thin tube from point a to point b (lamp arms, chair spokes, pens)."""
    a, b = Vector(a), Vector(b)
    o = cyl(name, r, (b - a).length, (a + b) / 2, material, segs=segs, bevel=0, parent=parent)
    o.rotation_euler = (b - a).to_track_quat("Z", "Y").to_euler()
    return o


def tube(name, pts, r, material, closed=False, segs=10, parent=None, coll=None):
    """A round tube swept along a list of points (chair back frame, cables, springs, vines)."""
    pts = [Vector(p) for p in pts]
    n = len(pts)
    bm = bmesh.new()
    rings, normal = [], None
    for i, p in enumerate(pts):
        if closed:
            tang = pts[(i + 1) % n] - pts[i - 1]
        else:
            tang = pts[min(i + 1, n - 1)] - pts[max(i - 1, 0)]
        tang.normalize()
        if normal is None:                                   # first frame, then parallel transport
            ref = Vector((0, 0, 1)) if abs(tang.z) < 0.9 else Vector((1, 0, 0))
            normal = tang.cross(ref).normalized()
        normal = (normal - tang * normal.dot(tang)).normalized()
        side = tang.cross(normal)
        rings.append([bm.verts.new(p + (normal * math.cos(a) + side * math.sin(a)) * r)
                      for a in (2 * math.pi * k / segs for k in range(segs))])
    for i in range(n if closed else n - 1):
        a, b = rings[i], rings[(i + 1) % n]
        for k in range(segs):
            bm.faces.new((a[k], a[(k + 1) % segs], b[(k + 1) % segs], b[k]))
    if not closed:
        bm.faces.new(rings[0][::-1])
        bm.faces.new(rings[-1])
    o = _obj(name, bm)
    return _finish(o, material, 0, coll, parent)


def bezier(p0, p1, p2, n=12):
    """Points on a smooth curve from p0 to p2 that bends towards p1."""
    p0, p1, p2 = Vector(p0), Vector(p1), Vector(p2)
    return [(1 - t) ** 2 * p0 + 2 * (1 - t) * t * p1 + t * t * p2 for t in (i / n for i in range(n + 1))]


def spline(pts, n=6):
    """Smooth curve through 2D points (Catmull-Rom), n points per span."""
    P = [pts[0]] + list(pts) + [pts[-1]]
    out = []
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        for k in range(n):
            t = k / n
            out.append(tuple(0.5 * (2 * p1[j] + (p2[j] - p0[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t * t
                                    + (3 * p1[j] - p0[j] - 3 * p2[j] + p3[j]) * t ** 3) for j in range(2)))
    out.append(tuple(pts[-1]))
    return out


def offset_path(pts, d):
    """Move a side-view (y, z) path sideways by d (positive = to the left of its direction of travel)."""
    out = []
    for i, (y, z) in enumerate(pts):
        (y0, z0), (y1, z1) = pts[max(i - 1, 0)], pts[min(i + 1, len(pts) - 1)]
        L = math.hypot(y1 - y0, z1 - z0) or 1.0
        out.append((y - (z1 - z0) / L * d, z + (y1 - y0) / L * d))
    return out


def ribbon(name, pts_yz, width, thick, material, x=0.0, bevel=0.004, parent=None):
    """A flat strip swept along a side-view path of (y, z) points: bent plywood, or a long cushion.
    It is `width` wide along x and `thick` thick across the path."""
    inner, outer = offset_path(pts_yz, -thick / 2), offset_path(pts_yz, thick / 2)
    bm = bmesh.new()
    rings = [[bm.verts.new((x + sx * width / 2, *(a if side < 0 else b))) for sx, side in
              ((-1, -1), (1, -1), (1, 1), (-1, 1))] for a, b in zip(inner, outer)]
    for ra, rb in zip(rings, rings[1:]):
        for k in range(4):
            bm.faces.new((ra[k], ra[(k + 1) % 4], rb[(k + 1) % 4], rb[k]))
    bm.faces.new(rings[0][::-1])
    bm.faces.new(rings[-1])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return _finish(_obj(name, bm), material, bevel, None, parent)


def flat(name, pts2d, material, loc=(0, 0, 0), rot=(0, 0, 0), parent=None, coll=None):
    """A flat shape (a leaf, a sticker) from 2D outline points in the XY plane."""
    bm = bmesh.new()
    bm.faces.new([bm.verts.new((x, y, 0)) for x, y in pts2d])
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, 0, coll, parent)


def no_shadow(*objs):
    for o in objs:
        if hasattr(o, "visible_shadow"):
            o.visible_shadow = False
    return objs


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


def slot_point(slot_name, local):
    """A point given in a slot's own frame (x = width, y = depth, z = up from its bottom) -> world."""
    s = SLOTS[slot_name]
    h = s["kit_size"][2]
    return s.location - Vector((0, 0, h / 2)) + s.rotation_euler.to_matrix() @ Vector(local)


def _matrix(o):
    return Matrix.Translation(o.location) @ o.rotation_euler.to_matrix().to_4x4()


def group(name, world_loc, world_turn, parent, tilt=0.0):
    """Empty placed in WORLD space (metres, degrees) but parented to a placeholder, so small props on a
    desk can be laid out in room coordinates and still disappear when that furniture is replaced."""
    e = bpy.data.objects.new(name, None)
    e.empty_display_size = 0.05
    e.location, e.rotation_euler = world_loc, (R(tilt), 0, R(world_turn))
    COL_FURN.objects.link(e)
    e.parent = parent
    e.matrix_parent_inverse = _matrix(parent).inverted()
    return e


# --------------------------------------------------------------------- portfolio hooks
# Hooks are where YOUR content goes. tools/build_portfolio.py fills them from profile.json:
#   picture hooks: "screen" (glows), "frame", "poster", "board", "logo"  -> project images (in order)
#   text hooks:    "name", "role", "title" (project titles), "skill"
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
    o.data.materials.append(mat(default_key, 0.4, emit=SCREEN_GLOW if glow else 0.0))
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


def deco_text(name, text, height, loc, material, rot=(R(90), 0, 0), parent=None, depth=0.006, align="CENTER"):
    """Plain 3D text that is NOT a hook (clock numbers, a label)."""
    cu = bpy.data.curves.new(name, "FONT")
    cu.body, cu.size, cu.align_x, cu.align_y = text, height, align, "CENTER"
    cu.extrude, cu.bevel_depth = depth, depth * 0.3
    o = bpy.data.objects.new(name, cu)
    o.location, o.rotation_euler = loc, rot
    o.data.materials.append(material)
    COL_ROOM.objects.link(o)
    o.parent = parent
    return o


# --------------------------------------------------------------------- shared real-world materials
def oak(rough=0.45, along="X"):
    """Oak veneer / solid oak in the theme's wood colour."""
    return surface(mat("wood", rough), "wood", along=along)


def steel(key="metal", rough=0.35):
    return surface(mat(key, rough, metal=0.8), "brushed")


def powder(key, rough=0.5):
    """Powder-coated steel (desk legs, brackets, monitor arm): matte paint over metal."""
    return surface(mat(key, rough, metal=0.15), "brushed")


def fabric(key, rough=0.9):
    return surface(mat(key, rough), "fabric")


def ceramic(key, rough=0.2):
    return surface(mat(key, rough), "ceramic")


PAPER = surface(mat("paper", 0.85, color="#F3EEE2"), "paper")      # printed pages, book edges, notes
MELAMINE = mat("cream", 0.45)                       # white flat-pack board (KALLAX, ALEX, SKÅDIS)
PLASTIC = mat("dark", 0.5)
RUBBER = mat("dark", 0.85, color=shade(COLORS["dark"], 0.8))


# =====================================================================
#  ROOM SHELL
# =====================================================================
# Diorama base slab, then engineered oak boards (19 cm wide) running front to back with staggered joints.
box("Floor_Base", (W + T, D + T, 0.2), ((W - T) / 2, (D + T) / 2, -0.1), mat("wall_trim", 0.7), bevel=0.03)
BOARD_W = 0.19
cols = math.ceil(W / BOARD_W)
tones = [[] for _ in range(3)]
for i in range(cols):
    x0, x1 = i * BOARD_W, min(W, (i + 1) * BOARD_W)
    y = -random.uniform(0.2, 1.4)                                   # stagger the end joints
    while y < D:
        L = random.uniform(1.2, 2.0)
        y0, y1 = max(0.0, y), min(D, y + L)
        if y1 - y0 > 0.05:
            tones[random.randrange(3)].append(((x1 - x0 - 0.003, y1 - y0 - 0.003, FLOOR_Z),
                                               ((x0 + x1) / 2, (y0 + y1) / 2, FLOOR_Z / 2)))
        y += L
for k, (items, f) in enumerate(zip(tones, (1.0, 0.94, 1.05))):
    m = surface(mat("floor", 0.5 + 0.02 * k, color=shade(COLORS["floor"], f)), "wood", scale=0.7, along="Y")
    boxes(f"Floor_Boards_{k}", items, m, bevel=0.0015)

# Walls: smooth painted plaster. The window is cut into the left wall.
WIN_Y = (1.5, 2.95)                 # from front to back
WIN_Z = (0.92, 2.22)                # bottom (sill height) and top
wall_m = surface(mat("wall", 0.85), "plaster", scale=3.0)       # fine, even plaster (not blotchy)
left = box("Wall_Left", (T, D + T, H), (-T / 2, (D + T) / 2, H / 2), wall_m, bevel=0.0)
cutter = box("Window_Cutter", (T * 3, WIN_Y[1] - WIN_Y[0], WIN_Z[1] - WIN_Z[0]),
             (-T / 2, sum(WIN_Y) / 2, sum(WIN_Z) / 2), wall_m, bevel=0.0)
cutter.hide_render = cutter.hide_viewport = True
boolean = left.modifiers.new("Window", "BOOLEAN")
boolean.operation, boolean.object = "DIFFERENCE", cutter
bev = left.modifiers.new("Bevel", "BEVEL")
bev.width, bev.segments, bev.limit_method = 0.006, 2, "ANGLE"
box("Wall_Back", (W + T, T, H), ((W - T) / 2, D + T / 2, H / 2), wall_m, bevel=0.006)

# Cut-away caps on top of the walls (the diorama look) and painted skirting boards with a rounded top.
cap = mat("wall_trim", 0.6)
box("Trim_Top_Back", (W + T + 0.02, T + 0.02, 0.06), ((W - T) / 2, D + T / 2, H + 0.03), cap, bevel=0.012)
box("Trim_Top_Left", (T + 0.02, D + T + 0.02, 0.06), (-T / 2, (D + T) / 2 - 0.01, H + 0.03), cap, bevel=0.012)
skirt = mat("cream", 0.35)
box("Skirting_Back", (W, 0.018, 0.12), (W / 2, D - 0.009, FLOOR_Z + 0.06), skirt, bevel=0.004)
box("Skirting_Left", (0.018, D, 0.12), (0.009, D / 2, FLOOR_Z + 0.06), skirt, bevel=0.004)
box("Skirting_Back_Ovolo", (W, 0.024, 0.016), (W / 2, D - 0.012, FLOOR_Z + 0.115), skirt, bevel=0.007)
box("Skirting_Left_Ovolo", (0.024, D, 0.016), (0.012, D / 2, FLOOR_Z + 0.115), skirt, bevel=0.007)

# Window: white timber casement (frame + two opening sashes with a handle), plastered reveal,
# a deep window board (the cat's spot), a roller blind and a panel radiator underneath.
wy, wz = sum(WIN_Y) / 2, sum(WIN_Z) / 2
ww, wh = WIN_Y[1] - WIN_Y[0], WIN_Z[1] - WIN_Z[0]
paint = mat("cream", 0.3)
FX = -T * 0.62                                                      # frame sits towards the outside
for nm, size, loc in [
    ("Head", (0.07, ww, 0.06), (FX, wy, WIN_Z[1] - 0.03)),
    ("Sill", (0.07, ww, 0.06), (FX, wy, WIN_Z[0] + 0.03)),
    ("JambF", (0.07, 0.06, wh), (FX, WIN_Y[0] + 0.03, wz)),
    ("JambB", (0.07, 0.06, wh), (FX, WIN_Y[1] - 0.03, wz)),
    ("Mullion", (0.07, 0.05, wh), (FX, wy, wz)),
]:
    box(f"Window_Frame_{nm}", size, loc, paint, bevel=0.005)
sash_w = (ww - 0.12 - 0.05) / 2
for k, sy in enumerate((WIN_Y[0] + 0.06 + sash_w / 2, WIN_Y[1] - 0.06 - sash_w / 2)):
    for nm, size, off in [("T", (0.05, sash_w, 0.05), (0, 0, wh / 2 - 0.085)),
                          ("B", (0.05, sash_w, 0.07), (0, 0, -wh / 2 + 0.095)),
                          ("F", (0.05, 0.05, wh - 0.12), (0, -sash_w / 2 + 0.025, 0)),
                          ("K", (0.05, 0.05, wh - 0.12), (0, sash_w / 2 - 0.025, 0))]:
        box(f"Window_Sash_{k}{nm}", size, (FX + 0.02, sy + off[1], wz + off[2]), paint, bevel=0.006)
    hy = sy - sash_w / 2 + 0.03 if k == 1 else sy + sash_w / 2 - 0.03
    box(f"Window_Handle_{k}", (0.02, 0.025, 0.035), (FX + 0.055, hy, wz - 0.05), steel(), bevel=0.004)
    box(f"Window_Handle_Lever_{k}", (0.018, 0.016, 0.11), (FX + 0.07, hy, wz - 0.1), steel(), bevel=0.006)
glass = box("Window_Glass", (0.006, ww - 0.08, wh - 0.08), (FX + 0.02, wy, wz),
            mat("sky", 0.08, emit=0.9 if not NIGHT else 0.6), bevel=0)
no_shadow(glass)
SILL_TOP = WIN_Z[0] + 0.025
box("Window_Board", (0.37, ww + 0.1, 0.025), (0.095, wy, SILL_TOP - 0.0125), paint, bevel=0.005)
cloud_m = mat("cloud", 0.9, emit=1.0, color="#FFFFFF" if not NIGHT else "#FFF3C4")
GX = FX - 0.03
if NIGHT:                                   # a moon and a few stars instead of clouds
    no_shadow(ball("Window_Moon", 0.07, (GX, WIN_Y[0] + ww * 0.72, WIN_Z[0] + wh * 0.78), cloud_m, scale=(0.1, 1, 1)))
    for k in range(9):
        no_shadow(ball("Window_Star", 0.008, (GX, WIN_Y[0] + random.uniform(0.1, ww - 0.1),
                                              WIN_Z[0] + random.uniform(0.3, wh - 0.1)), cloud_m, scale=(0.1, 1, 1)))
else:
    for k, (cy, cz, cr) in enumerate([(0.25, 0.8, 0.06), (0.32, 0.82, 0.08), (0.4, 0.8, 0.055),
                                       (0.7, 0.6, 0.05), (0.77, 0.62, 0.07), (0.84, 0.6, 0.045)]):
        no_shadow(ball(f"Window_Cloud_{k}", cr, (GX, WIN_Y[0] + ww * cy, WIN_Z[0] + wh * cz), cloud_m,
                       scale=(0.1, 1.4, 0.7)))
    for k in range(5):                                              # distant tree tops beyond the glass
        no_shadow(ball(f"Window_Tree_{k}", 0.11 + 0.03 * (k % 2), (GX - 0.005, WIN_Y[0] + 0.15 + k * 0.27,
                       WIN_Z[0] + 0.08), mat("tree", 0.9, emit=0.5, color=shade(COLORS["plant"], 1.25)),
                       scale=(0.1, 1.2, 1.0)))
# Roller blind: cassette, fabric pulled down a little, weighted bottom bar and a bead chain.
box("Blind_Cassette", (0.06, ww + 0.06, 0.07), (0.035, wy, WIN_Z[1] + 0.06), paint, bevel=0.012)
box("Blind_Fabric", (0.004, ww + 0.02, 0.3), (0.035, wy, WIN_Z[1] - 0.12), fabric("wall_trim", 0.95), bevel=0)
box("Blind_Bar", (0.014, ww + 0.02, 0.02), (0.035, wy, WIN_Z[1] - 0.27), paint, bevel=0.005)
tube("Blind_Chain", [(0.045, WIN_Y[1] + 0.01, WIN_Z[1] + 0.03), (0.047, WIN_Y[1] + 0.012, WIN_Z[1] - 0.55),
                     (0.045, WIN_Y[1] + 0.03, WIN_Z[1] - 0.6), (0.043, WIN_Y[1] + 0.045, WIN_Z[1] - 0.55),
                     (0.042, WIN_Y[1] + 0.045, WIN_Z[1] + 0.03)], 0.0025, steel(), segs=6)

# Type 22 panel radiator (100 x 60 x 10 cm) under the window: pressed vertical ribs, top grille, valves, pipes.
RX, RZ = 0.075, FLOOR_Z + 0.15
rad = mat("cream", 0.32)
box("Radiator_Back", (0.022, 1.0, 0.6), (RX - 0.035, wy, RZ + 0.3), rad, bevel=0.006)
box("Radiator_Front", (0.022, 1.0, 0.6), (RX + 0.035, wy, RZ + 0.3), rad, bevel=0.006)
boxes("Radiator_Ribs", [((0.006, 0.022, 0.56), (RX + 0.048, wy - 0.48 + 0.0333 * k, RZ + 0.3)) for k in range(30)],
      rad, bevel=0.0025)
boxes("Radiator_Grille", [((0.07, 0.006, 0.004), (RX, wy - 0.48 + 0.02 * k, RZ + 0.602)) for k in range(49)],
      mat("dark", 0.7, color=shade(COLORS["cream"], 0.55)))
box("Radiator_Grille_Top", (0.09, 1.0, 0.004), (RX, wy, RZ + 0.598), rad, bevel=0)
for k, sy in enumerate((wy - 0.56, wy + 0.56)):
    rod(f"Radiator_Pipe_{k}", (RX, sy, FLOOR_Z), (RX, sy, RZ + 0.04), 0.0075, steel())
    rod(f"Radiator_Tail_{k}", (RX, sy, RZ + 0.04), (RX, sy + (0.06 if k == 0 else -0.06), RZ + 0.04), 0.009, steel())
cyl("Radiator_Valve_Body", 0.014, 0.07, (RX, wy - 0.56, RZ + 0.085), steel(), bevel=0.002)
cyl("Radiator_Valve_Head", 0.026, 0.075, (RX, wy - 0.56, RZ + 0.155), rad, bevel=0.008)
boxes("Radiator_Valve_Ribs", [((0.003, 0.006, 0.05), (RX + 0.026 * math.cos(a), wy - 0.56 + 0.026 * math.sin(a),
                                                       RZ + 0.155)) for a in (k * math.pi / 8 for k in range(16))],
      rad)
cyl("Radiator_Lockshield", 0.012, 0.05, (RX, wy + 0.56, RZ + 0.07), mat("cream", 0.5), bevel=0.003)

# Floating oak shelf with two black brackets on the left wall above the desk, with a trailing pothos.
SH_Y, SH_Z = (3.12, 3.82), 1.78
box("WallShelf_Board", (0.2, SH_Y[1] - SH_Y[0], 0.02), (0.1, sum(SH_Y) / 2, SH_Z), oak(0.52, "Y"), bevel=0.003)
for k, by in enumerate((SH_Y[0] + 0.1, SH_Y[1] - 0.1)):
    box(f"WallShelf_Bracket_{k}", (0.17, 0.02, 0.004), (0.085, by, SH_Z - 0.012), powder("dark"), bevel=0.001)
    box(f"WallShelf_Bracket_Wall_{k}", (0.004, 0.02, 0.12), (0.002, by, SH_Z - 0.07), powder("dark"), bevel=0.001)
pot_m = ceramic("cream")
cyl("WallShelf_Pot", 0.06, 0.1, (0.1, SH_Y[0] + 0.12, SH_Z + 0.06), pot_m, r2=0.07, bevel=0.004)
cyl("WallShelf_Pot_Rim", 0.072, 0.014, (0.1, SH_Y[0] + 0.12, SH_Z + 0.105), pot_m, bevel=0.003)
cyl("WallShelf_Soil", 0.064, 0.01, (0.1, SH_Y[0] + 0.12, SH_Z + 0.108), mat("soil", 0.95, color="#4A3828"), bevel=0)
leaf_m = mat("plant", 0.45)


def heart_leaf(name, size, loc, rot, material):
    """A small heart-shaped leaf (pothos / ivy)."""
    pts = [(math.sin(t) ** 3 * 0.5 * size, (0.8 * math.cos(t) - 0.3 * math.cos(2 * t) - 0.1 * math.cos(3 * t)
            - 0.05 * math.cos(4 * t)) * 0.5 * size) for t in (2 * math.pi * k / 20 for k in range(20))]
    return flat(name, pts, material, loc, rot)


for v in range(4):                                                  # vines spilling over the shelf edge
    start = Vector((0.17, SH_Y[0] + 0.07 + 0.04 * v, SH_Z + 0.1))
    drop = 0.25 + 0.17 * v
    pts = bezier(start, start + Vector((0.12, 0.02 * v, 0.02)), start + Vector((0.1, 0.06 + 0.05 * v, -drop)), 10)
    tube(f"WallShelf_Vine_{v}", pts, 0.003, mat("stem", 0.6, color=shade(COLORS["plant"], 0.8)), segs=5)
    for k, p in enumerate(pts[1::2]):
        heart_leaf(f"WallShelf_Leaf_{v}_{k}", 0.055, p + Vector((0.004, 0, -0.01)),
                   (R(70 + 20 * (k % 2)), 0, R(90 + 35 * ((k + v) % 3 - 1))), leaf_m)
for k in range(6):                                                  # leaves on top of the pot
    a = k * 1.1
    heart_leaf(f"WallShelf_TopLeaf_{k}", 0.065, (0.1 + 0.05 * math.cos(a), SH_Y[0] + 0.12 + 0.05 * math.sin(a),
               SH_Z + 0.15 + 0.02 * (k % 2)), (R(35), 0, a + R(90)), leaf_m)
for k, (key, bh) in enumerate((("main", 0.21), ("accent_1", 0.19), ("dark", 0.23), ("accent_3", 0.2))):
    box(f"WallShelf_Book_{k}", (0.15, 0.028, bh), (0.09, SH_Y[1] - 0.2 + k * 0.031, SH_Z + 0.01 + bh / 2),
        mat(key, 0.7), bevel=0.003)
box("WallShelf_Bookend", (0.12, 0.004, 0.12), (0.08, SH_Y[1] - 0.22, SH_Z + 0.07), powder("dark"), bevel=0.001)

# 28 cm wall clock: black rim, white face, all twelve numbers, red seconds hand.
CK = Vector((2.6, D, 2.44))
cyl("Clock_Body", 0.14, 0.03, CK + Vector((0, -0.015, 0)), mat("dark", 0.35), rot=(R(90), 0, 0), segs=48, bevel=0.008)
cyl("Clock_Face", 0.128, 0.002, CK + Vector((0, -0.031, 0)), mat("cream", 0.6), rot=(R(90), 0, 0), segs=48, bevel=0)
tube("Clock_Rim", [CK + Vector((math.cos(a) * 0.134, -0.033, math.sin(a) * 0.134))
                   for a in (2 * math.pi * k / 48 for k in range(48))], 0.008, mat("dark", 0.35), closed=True)
for k in range(12):
    a = (k + 1) * math.pi / 6
    deco_text(f"Clock_Num_{k + 1}", str(k + 1), 0.03, CK + Vector((math.sin(a) * 0.1, -0.0325, math.cos(a) * 0.1 - 0.001)),
              mat("dark", 0.5), depth=0.0005)
for k in range(60):
    if k % 5:
        a = k * math.pi / 30
        box("Clock_Tick", (0.002, 0.001, 0.007), CK + Vector((math.sin(a) * 0.119, -0.0325, math.cos(a) * 0.119)),
            mat("dark", 0.5), bevel=0, rot=(0, a, 0))
for nm, length, width, ang, key in (("H", 0.06, 0.007, 300, "dark"), ("M", 0.095, 0.005, 60, "dark"),
                                    ("S", 0.105, 0.0018, 150, "accent_1")):
    a = R(ang)
    box(f"Clock_Hand_{nm}", (width, 0.001, length), CK + Vector((math.sin(a) * length * 0.4, -0.034 - 0.001 * len(nm),
                                                                 math.cos(a) * length * 0.4)),
        mat(key, 0.5), bevel=0, rot=(0, a, 0))
cyl("Clock_Pin", 0.006, 0.006, CK + Vector((0, -0.037, 0)), mat("dark", 0.4), rot=(R(90), 0, 0), bevel=0)

# Side table (55 x 55 x 45 cm slab top on square legs) in the front-left corner with books and a speaker.
LT = Vector((0.42, 0.5, FLOOR_Z))
lack = oak(0.4)
box("SideTable_Top", (0.55, 0.55, 0.05), LT + Vector((0, 0, 0.425)), lack, bevel=0.004)
for sx in (-1, 1):
    for sy in (-1, 1):
        box("SideTable_Leg", (0.05, 0.05, 0.4), LT + Vector((sx * 0.25, sy * 0.25, 0.2)), lack, bevel=0.003)
for k, (key, th, w_, d_, turn) in enumerate((("accent_2", 0.03, 0.24, 0.17, 8), ("dark", 0.025, 0.22, 0.16, -5),
                                            ("accent_1", 0.035, 0.2, 0.14, 14))):
    zb = 0.45 + (0.0, 0.03, 0.055)[k]
    box(f"SideTable_Book_{k}", (w_, d_, th), LT + Vector((0.05, -0.08, zb + th / 2)), mat(key, 0.7), bevel=0.003,
        rot=(0, 0, R(turn)))
    box(f"SideTable_Pages_{k}", (w_ - 0.012, d_ + 0.002, th - 0.006), LT + Vector((0.054, -0.08, zb + th / 2)),
        PAPER, bevel=0, rot=(0, 0, R(turn)))
cyl("SideTable_Speaker", 0.045, 0.17, LT + Vector((-0.14, 0.14, 0.535)), fabric("dark", 0.95), segs=32, bevel=0.01)
cyl("SideTable_Speaker_Top", 0.044, 0.006, LT + Vector((-0.14, 0.14, 0.622)), mat("dark", 0.4), bevel=0.002)

# Desktop PC (mid-tower case 21 x 45 x 47 cm) on the floor between the drawer unit and the shelf:
# white steel case, mesh front, tempered-glass side panel showing the board, graphics card and fans.
PC = Vector((2.62, 3.71, FLOOR_Z))
case = mat("cream", 0.35, color=shade(COLORS["cream"], 0.97))
inside = mat("pc_inside", 0.6, color="#22262D")
for nm, size, off in [("Top", (0.21, 0.45, 0.012), (0, 0, 0.464)), ("Bottom", (0.21, 0.45, 0.03), (0, 0, 0.03)),
                      ("Back", (0.21, 0.012, 0.46), (0, 0.219, 0.245)), ("Side", (0.012, 0.45, 0.46), (-0.099, 0, 0.245))]:
    box(f"PC_Case_{nm}", size, PC + Vector(off), case, bevel=0.004)
box("PC_Front", (0.21, 0.02, 0.46), PC + Vector((0, -0.215, 0.245)), case, bevel=0.004)
box("PC_Front_Mesh", (0.15, 0.004, 0.34), PC + Vector((0, -0.226, 0.23)), fabric("dark", 0.95), bevel=0.002)
cyl("PC_Power", 0.008, 0.004, PC + Vector((0.0, -0.226, 0.43)), mat("led", 0.3, emit=3.0, color="#FFFFFF"),
    rot=(R(90), 0, 0), bevel=0)
for sx in (-1, 1):
    for sy in (-1, 1):
        cyl("PC_Foot", 0.018, 0.012, PC + Vector((sx * 0.07, sy * 0.18, 0.006)), RUBBER)
box("PC_Board", (0.004, 0.36, 0.3), PC + Vector((-0.09, 0.03, 0.3)), inside, bevel=0)
box("PC_PSU_Shroud", (0.19, 0.44, 0.09), PC + Vector((0.0, 0.0, 0.09)), case, bevel=0.003)   # covers the PSU
box("PC_GPU", (0.12, 0.28, 0.045), PC + Vector((-0.025, -0.03, 0.21)), mat("dark", 0.4), bevel=0.004)
box("PC_GPU_Backplate", (0.12, 0.28, 0.004), PC + Vector((-0.025, -0.03, 0.234)), steel("metal", 0.3), bevel=0)
led = mat("pc_led", 0.3, emit=3.0, color=shade(COLORS["main"], 1.15))
for k, (fy, fz, ry) in enumerate(((0.19, 0.35, -0.164), (-0.19, 0.3, -0.176))):   # rear exhaust + front intake
    cyl(f"PC_Fan_{k}", 0.058, 0.025, PC + Vector((-0.01, fy, fz)), case, rot=(R(90), 0, 0), segs=24, bevel=0.002)
    cyl(f"PC_Fan_Hub_{k}", 0.02, 0.028, PC + Vector((-0.01, fy, fz)), inside, rot=(R(90), 0, 0), segs=16, bevel=0)
    ring_y = fy - 0.014 if fy > 0 else fy + 0.014                   # lit ring on the side facing the inside
    tube(f"PC_Fan_Ring_{k}", [PC + Vector((-0.01 + 0.05 * math.cos(a), ring_y, fz + 0.05 * math.sin(a)))
                              for a in (2 * math.pi * j / 24 for j in range(24))], 0.006, led, closed=True, segs=6)
box("PC_Cooler", (0.09, 0.07, 0.11), PC + Vector((-0.04, 0.07, 0.36)), case, bevel=0.004)
cyl("PC_Cooler_Top", 0.032, 0.012, PC + Vector((-0.04, 0.07, 0.42)), led, segs=24, bevel=0)
box("PC_RAM", (0.012, 0.13, 0.035), PC + Vector((-0.07, 0.14, 0.37)), mat("dark", 0.4), bevel=0.002)
box("PC_RAM_Light", (0.012, 0.13, 0.004), PC + Vector((-0.07, 0.14, 0.389)), led, bevel=0)
# Tempered-glass side: only a smoked edge band is modelled (a full see-through pane renders as noise).
glass_m = see_through("dark", 0.35, 0.05)
for nm, size, off in [("T", (0.004, 0.43, 0.012), (0, 0, 0.452)), ("B", (0.004, 0.43, 0.012), (0, 0, 0.038)),
                      ("F", (0.004, 0.012, 0.43), (0, -0.209, 0.245)), ("K", (0.004, 0.012, 0.43), (0, 0.209, 0.245))]:
    no_shadow(box(f"PC_Glass_Edge_{nm}", size, PC + Vector((0.103, 0, 0)) + Vector(off), glass_m, bevel=0))

tube("PC_Cable", bezier(PC + Vector((0, 0.226, 0.4)), PC + Vector((0, 0.3, 0.2)), PC + Vector((-0.1, 0.27, 0.0)), 8),
     0.005, PLASTIC)

# Reading corner: a bentwood armchair (IKEA POÄNG: 68 x 82 x 100 cm, seat 39 cm) turned towards the room.
# Side view: each floor runner bends up at the front into the armrest; the seat and back are ONE springy
# frame that hangs from the front of the armrests (cantilever) and carries one long channel-stitched cushion.
AC = bpy.data.objects.new("Armchair", None)
AC.location, AC.rotation_euler = (3.22, 1.22, FLOOR_Z), (0, 0, R(-28))
COL_ROOM.objects.link(AC)
birch = surface(mat("birch", 0.45, color=shade(COLORS["wood"], 1.12)), "veneer", along="Y")
runner = spline([(0.34, 0.012), (0.05, 0.012), (-0.25, 0.02), (-0.36, 0.13), (-0.355, 0.35), (-0.3, 0.5),
                 (-0.15, 0.555), (0.07, 0.55)], 6)
seat_frame = spline([(-0.31, 0.47), (-0.18, 0.37), (0.0, 0.3), (0.15, 0.32), (0.23, 0.44), (0.28, 0.68),
                     (0.33, 0.93), (0.31, 0.99)], 6)
for sx in (-1, 1):
    ribbon(f"Armchair_Runner_{sx}", runner, 0.045, 0.024, birch, x=sx * 0.315, parent=AC)
    ribbon(f"Armchair_SeatFrame_{sx}", seat_frame, 0.04, 0.024, birch, x=sx * 0.27, parent=AC)
    cyl(f"Armchair_Bolt_{sx}", 0.008, 0.05, (sx * 0.29, -0.31, 0.47), steel(), rot=(0, R(90), 0), parent=AC)
box("Armchair_Rail_Back", (0.675, 0.045, 0.024), (0, 0.32, 0.012), birch, bevel=0.004, parent=AC)
box("Armchair_Rail_Seat", (0.56, 0.04, 0.02), (0, 0.0, 0.29), birch, bevel=0.004, parent=AC)
box("Armchair_Rail_Top", (0.56, 0.035, 0.02), (0, 0.33, 0.9), birch, bevel=0.004, parent=AC)
cushion_m = fabric("main", 0.95)
cushion_path = offset_path(seat_frame[1:-1], 0.055)
cushion_path.insert(0, (cushion_path[0][0] - 0.035, cushion_path[0][1] - 0.06))   # rolls over the front edge
ribbon("Armchair_Cushion", cushion_path, 0.53, 0.09, cushion_m, bevel=0.04, parent=AC)
seam = mat("seam", 0.9, color=shade(COLORS["main"], 0.8))
seam_line = offset_path(cushion_path, 0.043)
for k in range(7, len(cushion_path) - 3, 5):                       # stitched channels across the cushion
    y, z = seam_line[k]
    rod(f"Armchair_Seam_{k}", (-0.235, y, z), (0.235, y, z), 0.005, seam, parent=AC)

# Knitted pouffe (45 cm across, 35 cm high) used as the armchair's footstool: chunky vertical cable ribs
# wrap from the floor over the top edge, like the real hand-knitted ones.
PF = Vector((2.86, 0.52, FLOOR_Z))
knit = surface(mat("accent_3", 0.95), "knit")
cyl("Pouffe", 0.205, 0.35, PF + Vector((0, 0, 0.175)), knit, segs=48, bevel=0.05)
for k in range(30):
    a = k * 2 * math.pi / 30
    prof = [(0.2, 0.025), (0.214, 0.12), (0.214, 0.25), (0.2, 0.33), (0.15, 0.352)]
    tube("Pouffe_Rib", [PF + Vector((math.cos(a) * r_, math.sin(a) * r_, z_)) for r_, z_ in spline(prof, 4)],
         0.0165, knit, segs=8)
box("Pouffe_Book", (0.17, 0.24, 0.025), PF + Vector((0.02, -0.02, 0.383)), mat("accent_1", 0.7), bevel=0.003,
    rot=(0, 0, R(25)))

# =====================================================================
#  FURNITURE SLOTS  (same names in every template)
#  size = (width, depth, height); front of the furniture faces local -Y
# =====================================================================
DESK_TOP = FLOOR_Z + DESK_H
slot("desk",     (1.6, 0.8, DESK_H),    (1.1, D - 0.42), shape="table")
slot("cabinet",  (0.36, 0.58, 0.70),    (2.14, D - 0.31), shape="cabinet")
slot("monitor",  (1.12, 0.3, 0.62),     (1.02, D - 0.2), z=DESK_TOP, kind="surface", shape="monitor")
slot("lamp",     (0.25, 0.45, 0.62),    (1.77, D - 0.245), z=DESK_TOP, kind="surface", shape="lamp")
slot("chair",    (0.66, 0.66, 1.08),    (1.06, 2.7), turn=172, shape="chair")
slot("rug",      (2.3, 1.6, 0.01),      (1.3, 2.42), kind="rug", shape="rug")
slot("shelf",    (0.77, 0.39, 1.47),    (3.45, D - 0.2), shape="shelf")
slot("wall_art", (0.72, 0.04, 0.95),    (2.62, D - 0.02), z=1.2, kind="wall", shape="frame")
slot("plant",    (0.65, 0.65, 1.0),     (3.5, 2.6), shape="plant")
slot("pet",      (0.44, 0.28, 0.24),    (0.15, WIN_Y[0] + 0.36), z=SILL_TOP, turn=90, kind="surface", shape="pet")


# =====================================================================
#  PLACEHOLDER FURNITURE  (replaced when you add your own with add_furniture.py)
# =====================================================================
def build_desk():
    """Sit/stand desk: thin oak top on two telescoping T-legs with long flat feet, a crossbeam and a control
    paddle. The desk-top props (keyboard, mouse, laptop, mug...) belong to it."""
    root, w, d, h = furniture_root("desk")
    frame = powder("frame")
    box("Desk_Top", (w, d, 0.025), (0, 0, h - 0.0125), oak(0.42), bevel=0.003, parent=root)
    for sx in (-1, 1):
        lx = sx * (w / 2 - 0.2)
        box("Desk_Foot", (0.075, 0.7, 0.03), (lx, 0, 0.022), frame, bevel=0.012, parent=root)
        for sy in (-1, 1):
            cyl("Desk_Glide", 0.012, 0.008, (lx, sy * 0.31, 0.004), RUBBER, parent=root)
        box("Desk_Leg_Lower", (0.09, 0.065, 0.36), (lx, 0.02, 0.037 + 0.18), frame, bevel=0.004, parent=root)
        box("Desk_Leg_Upper", (0.078, 0.054, h - 0.43), (lx, 0.02, 0.397 + (h - 0.43) / 2 - 0.02), frame, bevel=0.003,
            parent=root)
        box("Desk_Leg_Seam", (0.093, 0.068, 0.01), (lx, 0.02, 0.395), RUBBER, bevel=0.002, parent=root)
        box("Desk_Side_Rail", (0.05, d - 0.16, 0.035), (lx, 0, h - 0.043), frame, bevel=0.003, parent=root)
    box("Desk_Crossbeam", (w - 0.42, 0.05, 0.05), (0, 0.06, h - 0.05), frame, bevel=0.004, parent=root)
    box("Desk_Motor", (0.16, 0.08, 0.05), (-w / 2 + 0.32, 0.06, h - 0.07), frame, bevel=0.006, parent=root)
    box("Desk_Paddle", (0.11, 0.045, 0.02), (w / 2 - 0.15, -d / 2 + 0.03, h - 0.04), PLASTIC, bevel=0.006, parent=root)
    tube("Desk_Cable_Tray", bezier((-0.2, d / 2 - 0.06, h - 0.03), (0, d / 2 - 0.02, h - 0.2), (0.25, d / 2 - 0.06,
                                   h - 0.03)), 0.006, PLASTIC, parent=root)
    tube("Desk_Power_Cable", bezier((w / 2 - 0.28, d / 2 - 0.05, h - 0.05), (w / 2 - 0.2, d / 2 - 0.02, 0.2),
                                    (w / 2 - 0.1, d / 2 - 0.02, 0.0)), 0.004, PLASTIC, parent=root)

    top = DESK_TOP
    # Felt desk mat, tenkeyless mechanical keyboard and a mouse.
    box("Desk_Mat", (0.8, 0.35, 0.003), (1.08, 3.44, top + 0.0015), fabric("felt", 0.95), bevel=0.001,
        parent=root).matrix_parent_inverse = _matrix(root).inverted()
    kb = group("Desk_Keyboard", (1.0, 3.42, top + 0.003), -2, root, tilt=3)
    box("Keyboard_Case", (0.355, 0.128, 0.022), (0, 0, 0.011), mat("cream", 0.5, color=shade(COLORS["cream"], 0.93)),
        bevel=0.005, parent=kb)
    U = 0.0185
    rows = [  # (row y, [(width in units, is modifier), ... or negative width = gap])
        (0.048, [(1, 2), (-1, 0), (1, 0), (1, 0), (1, 0), (1, 0), (-0.5, 0), (1, 1), (1, 1), (1, 1), (1, 1), (-0.5, 0),
                 (1, 0), (1, 0), (1, 0), (1, 0), (-0.25, 0), (1, 1), (1, 1), (1, 1)]),
        (0.024, [(1, 0)] * 13 + [(2, 1), (-0.25, 0), (1, 1), (1, 1), (1, 1)]),
        (0.005, [(1.5, 1)] + [(1, 0)] * 12 + [(1.5, 1), (-0.25, 0), (1, 1), (1, 1), (1, 1)]),
        (-0.014, [(1.75, 1)] + [(1, 0)] * 11 + [(2.25, 2)]),
        (-0.033, [(2.25, 1)] + [(1, 0)] * 10 + [(2.75, 1), (-1.25, 0), (1, 1)]),
        (-0.052, [(1.25, 1)] * 3 + [(6.25, 0)] + [(1.25, 1)] * 4 + [(-0.25, 0), (1, 1), (1, 1), (1, 1)]),
    ]
    keys = {0: [], 1: [], 2: []}
    for ry, row in rows:
        x = -0.169
        for units, kind in row:
            if units > 0:
                keys[kind].append(((units * U - 0.0028, 0.0162, 0.011), (x + units * U / 2, ry, 0.0265)))
            x += abs(units) * U
    for kind, key in ((0, "cream"), (1, "dark"), (2, "accent_1")):
        if keys[kind]:
            boxes(f"Keyboard_Keys_{kind}", keys[kind], mat(key, 0.55), bevel=0.0018, parent=kb)
    tube("Keyboard_Cable", bezier((1.0 + 0.0, 3.42 + 0.066, top + 0.015), (1.02, 3.6, top + 0.004),
                                  (1.04, 3.72, top + 0.004), 8), 0.0025, PLASTIC, parent=root
         ).matrix_parent_inverse = _matrix(root).inverted()
    ms = group("Desk_Mouse", (1.32, 3.4, top + 0.003), -6, root)
    ball("Mouse_Body", 0.058, (0, 0, 0.0), mat("dark", 0.45), scale=(0.55, 1.0, 0.36), parent=ms)
    box("Mouse_Split", (0.0012, 0.04, 0.003), (0, 0.03, 0.02), mat("dark", 0.8, color="#111111"), bevel=0, parent=ms)
    cyl("Mouse_Wheel", 0.007, 0.004, (0, 0.028, 0.0205), RUBBER, rot=(0, R(90), 0), bevel=0, parent=ms)
    # Mug (email link): ceramic with a real loop handle, coffee inside.
    mg = group("Desk_Mug", (1.6, 3.33, top), 40, root)
    mug = ceramic("accent_1")
    hook_link(cyl("Mug_Body", 0.041, 0.095, (0, 0, 0.0475), mug, segs=40, bevel=0.003, parent=mg), "email")
    cyl("Mug_Coffee", 0.037, 0.004, (0, 0, 0.083), mat("coffee", 0.15, color="#4A3024"), bevel=0, parent=mg)
    tube("Mug_Handle", [(0.038 + 0.03 * math.sin(a), 0, 0.048 + 0.028 * math.cos(a))
                        for a in (math.pi * k / 10 for k in range(11))], 0.006, mug, parent=mg)
    # Closed laptop with a sticker or two (lid sticker = optional "logo" hook) and a phone.
    lp = group("Desk_Laptop", (0.5, 3.42, top), 12, root)
    alu = steel("metal", 0.32)
    hook_link(box("Laptop_Base", (0.304, 0.212, 0.008), (0, 0, 0.004), alu, bevel=0.003, parent=lp), "linkedin")
    box("Laptop_Lid", (0.304, 0.212, 0.006), (0, 0, 0.0115), alu, bevel=0.003, parent=lp)
    box("Laptop_Hinge", (0.24, 0.006, 0.01), (0, 0.105, 0.008), mat("dark", 0.5), bevel=0.002, parent=lp)
    for k, (sx, sy, r_, key) in enumerate([(-0.1, 0.06, 0.022, "accent_3"), (0.11, -0.065, 0.018, "plant")]):
        cyl("Laptop_Sticker", r_, 0.001, (sx, sy, 0.0148), mat(key, 0.5), segs=24, bevel=0, parent=lp)
    logo = hook_image("logo", 1, (0.07, 0.07), (0, 0, 0.0151), rot=(R(-90), 0, 0), parent=lp, default_key="dark")
    hook_default(logo, deco_text("Logo_Brackets", "</>", 0.03, (0, 0.0, 0.0156), mat("cream", 0.5), rot=(0, 0, 0),
                                 parent=lp, depth=0.0005))
    ph = group("Desk_Phone", (0.72, 3.27, top), -20, root)
    box("Phone_Body", (0.072, 0.15, 0.008), (0, 0, 0.004), mat("dark", 0.3), bevel=0.004, parent=ph)
    box("Phone_Camera", (0.025, 0.025, 0.002), (-0.018, 0.05, 0.009), mat("metal", 0.3), bevel=0.003, parent=ph)
    # Notebook with an elastic band and a pen, and a pen pot.
    nb = group("Desk_Notebook", (0.44, 3.68, top), 5, root)
    box("Notebook_Cover", (0.145, 0.21, 0.016), (0, 0, 0.008), mat("dark", 0.75, color=shade(COLORS["main"], 0.6)),
        bevel=0.003, parent=nb)
    box("Notebook_Pages", (0.14, 0.206, 0.012), (0.004, 0, 0.008), PAPER, bevel=0, parent=nb)
    box("Notebook_Band", (0.004, 0.212, 0.017), (0.055, 0, 0.0085), mat("dark", 0.6), bevel=0, parent=nb)
    rod("Notebook_Pen", (-0.03, -0.07, 0.022), (0.04, 0.08, 0.022), 0.0045, mat("dark", 0.3), parent=nb)


def build_cabinet():
    """Drawer unit 36 x 58 x 70 cm: white carcass, five flat fronts with 3 mm gaps and cut-out grips."""
    root, w, d, h = furniture_root("cabinet")
    t = 0.018
    box("Cabinet_Top", (w, d, t), (0, 0, h - t / 2), MELAMINE, bevel=0.002, parent=root)
    for sx in (-1, 1):
        box("Cabinet_Side", (t, d, h - t), (sx * (w / 2 - t / 2), 0, (h - t) / 2), MELAMINE, bevel=0.002, parent=root)
    box("Cabinet_Back", (w - 2 * t, t, h - t), (0, d / 2 - t / 2, (h - t) / 2), MELAMINE, bevel=0.001, parent=root)
    box("Cabinet_Plinth", (w - 2 * t, d - 0.04, 0.012), (0, 0.0, 0.006), MELAMINE, bevel=0.001, parent=root)
    gap = 0.003
    heights = [0.084] + [(h - t - 0.016 - 0.084 - 5 * gap) / 4] * 4
    z = h - t - gap
    fw = w - 2 * t - 2 * gap
    hole = mat("dark", 0.9, color=shade(COLORS["dark"], 0.7))
    for k, fh in enumerate(heights):
        zc = z - fh / 2
        box(f"Cabinet_Drawer_{k}", (fw, 0.016, fh), (0, -d / 2 + 0.008, zc), MELAMINE, bevel=0.0015, parent=root)
        box(f"Cabinet_Grip_{k}", (0.1, 0.004, 0.016), (0, -d / 2 - 0.0005, z - 0.018), hole, bevel=0.006, parent=root)
        z -= fh + gap
    # On top: a printer-sized storage box, a plant cutting in a glass jar and a stack of paper trays.
    box("Cabinet_Tray", (0.26, 0.34, 0.06), (0, 0.04, h + 0.03), mat("dark", 0.5, color=shade(COLORS["dark"], 1.1)),
        bevel=0.004, parent=root)
    box("Cabinet_Tray_Paper", (0.21, 0.297, 0.012), (0, 0.04, h + 0.066), surface(mat("cream", 0.85, color="#F3EEE2"),
        "paper"), bevel=0, parent=root)
    cyl("Cabinet_Jar", 0.035, 0.12, (0.0, -0.2, h + 0.06), mat("glassjar", 0.08, color="#CFE0DA"), bevel=0.004,
        parent=root)
    for k in range(4):
        a = k * 1.6
        heart_leaf(f"Cabinet_Cutting_{k}", 0.07, slot_point("cabinet", (0.025 * math.cos(a), -0.2 + 0.025 * math.sin(a),
                   h + 0.17 + 0.02 * k)), (R(50), 0, a), leaf_m).parent = root
    for o in root.children:
        if o.name.startswith("Cabinet_Cutting"):
            o.matrix_parent_inverse = _matrix(root).inverted()


PANEL = (0.53, 0.30)        # 24-inch 16:9 panel, metres
MON_X = 0.282               # each monitor's centre, left/right of the slot centre
MON_Y = -0.06               # front-back position of the casings in the slot
MON_Z = 0.40                # screen centre above the desk top
MON_TOE = R(9)              # each screen turned in towards the chair


def build_monitor():
    """Two 24-inch monitors on a dual clamp arm. The screens themselves are hooks anchored to SLOT_monitor."""
    root, w, d, h = furniture_root("monitor")
    arm = powder("frame", 0.4)
    casing = mat("dark", 0.45)
    PY = d / 2 - 0.04                                               # pole sits just in front of the desk's back edge
    box("Monitor_Clamp_Top", (0.07, 0.12, 0.012), (0, PY + 0.02, 0.006), arm, bevel=0.003, parent=root)
    box("Monitor_Clamp_Back", (0.07, 0.012, 0.07), (0, PY + 0.074, -0.03), arm, bevel=0.003, parent=root)
    cyl("Monitor_Pole", 0.017, 0.5, (0, PY, 0.26), arm, segs=24, parent=root)
    cyl("Monitor_Pole_Cap", 0.019, 0.012, (0, PY, 0.513), PLASTIC, segs=24, parent=root)
    cyl("Monitor_Collar", 0.025, 0.04, (0, PY, MON_Z), arm, segs=24, parent=root)
    for sx in (-1, 1):
        cx = sx * MON_X
        mid = Vector((sx * 0.14, PY - 0.01, MON_Z))
        rod(f"Monitor_Arm_{sx}", (0, PY, MON_Z), mid, 0.016, arm, parent=root)
        rod(f"Monitor_Arm_Fore_{sx}", mid, (cx, MON_Y + 0.06, MON_Z), 0.013, arm, parent=root)
        cyl(f"Monitor_Elbow_{sx}", 0.02, 0.04, mid, arm, segs=20, parent=root)
        cyl(f"Monitor_Tilt_Joint_{sx}", 0.018, 0.05, (cx, MON_Y + 0.058, MON_Z), arm, segs=20, parent=root)
        # Each monitor is turned in a little towards the chair, the way people set up two screens.
        head = bpy.data.objects.new(f"Monitor_Head_{sx}", None)
        head.empty_display_size = 0.05
        head.location, head.rotation_euler = (cx, MON_Y, MON_Z), (0, 0, -sx * MON_TOE)
        COL_FURN.objects.link(head)
        head.parent = root
        box(f"Monitor_VESA_{sx}", (0.1, 0.012, 0.1), (0, 0.045, 0), arm, bevel=0.003, parent=head)
        # Thin casing: 7 mm bezel on three sides and a 2 cm chin, a deeper back bump with the electronics.
        box(f"Monitor_Casing_{sx}", (PANEL[0] + 0.014, 0.018, PANEL[1] + 0.027), (0, 0, -0.0065),
            casing, bevel=0.003, parent=head)
        box(f"Monitor_Back_{sx}", (0.36, 0.03, 0.22), (0, 0.022, -0.02), casing, bevel=0.012, parent=head)
        box(f"Monitor_Panel_{sx}", (PANEL[0], 0.002, PANEL[1]), (0, -0.0095, 0), mat("dark", 0.15,
            color="#0E1116"), bevel=0, parent=head)
        box(f"Monitor_LED_{sx}", (0.004, 0.002, 0.002), (0.24, -0.0095, -PANEL[1] / 2 - 0.01),
            mat("led", 0.3, emit=3.0, color="#FFFFFF"), bevel=0, parent=head)
        if sx < 0:                                                  # clip-on webcam on the left screen
            box("Monitor_Webcam", (0.09, 0.03, 0.026), (0, 0.004, PANEL[1] / 2 + 0.02), casing, bevel=0.008,
                parent=head)
            cyl("Monitor_Webcam_Lens", 0.006, 0.003, (0, -0.012, PANEL[1] / 2 + 0.02),
                mat("lens", 0.05, color="#101820"), rot=(R(90), 0, 0), bevel=0, parent=head)
    # Soft screen glow on the keyboard (kept when the monitor is replaced).
    glow = light("Light_Monitor_Glow", "AREA", 6 if not NIGHT else 14, kelvin(7500),
                 slot_point("monitor", (0, -0.25, MON_Z)), aim=slot_point("monitor", (0, -0.9, -0.2)), size=0.7)
    glow.parent = root
    glow.matrix_parent_inverse = _matrix(root).inverted()


def build_chair():
    """Mesh-back task chair: five-star base with twin-wheel casters, gas lift, tilt mechanism, padded seat,
    see-through mesh back in a looped frame and T-shaped armrests."""
    root, w, d, h = furniture_root("chair")
    base = mat("dark", 0.4)
    for k in range(5):                                              # five tapered spokes + twin-wheel casters
        a = k * 2 * math.pi / 5 + 0.3
        c, s = math.cos(a), math.sin(a)
        box(f"Chair_Spoke_{k}", (0.3, 0.042, 0.03), (c * 0.16, s * 0.16, 0.085), base, bevel=0.008,
            rot=(0, R(6), a), parent=root)
        tip = Vector((c * 0.31, s * 0.31, 0.0))
        cyl(f"Chair_Caster_Stem_{k}", 0.008, 0.03, tip + Vector((0, 0, 0.075)), steel(), parent=root)
        box(f"Chair_Caster_Hood_{k}", (0.05, 0.035, 0.03), tip + Vector((0, 0, 0.055)), base, bevel=0.01,
            rot=(0, 0, a), parent=root)
        for side in (-1, 1):
            cyl(f"Chair_Wheel_{k}", 0.025, 0.012, tip + Vector((-s * side * 0.012, c * side * 0.012, 0.025)), RUBBER,
                rot=(R(90), 0, a), segs=20, bevel=0.003, parent=root)
    cyl("Chair_Hub", 0.045, 0.06, (0, 0, 0.1), base, bevel=0.01, parent=root)
    cyl("Chair_Gas_Cover", 0.028, 0.16, (0, 0, 0.21), base, r2=0.024, parent=root)
    cyl("Chair_Gas_Rod", 0.014, 0.12, (0, 0, 0.33), steel(rough=0.2), parent=root)
    seat_h = 0.47
    box("Chair_Mechanism", (0.2, 0.24, 0.06), (0, 0.02, seat_h - 0.1), base, bevel=0.01, parent=root)
    rod("Chair_Lever", (0.1, -0.04, seat_h - 0.1), (0.2, -0.08, seat_h - 0.11), 0.006, base, parent=root)
    cyl("Chair_Tension_Knob", 0.025, 0.05, (0, -0.12, seat_h - 0.11), base, rot=(R(90), 0, 0), parent=root)
    box("Chair_Seat_Shell", (0.5, 0.47, 0.03), (0, -0.02, seat_h - 0.06), base, bevel=0.012, parent=root)
    box("Chair_Seat_Cushion", (0.5, 0.48, 0.06), (0, -0.025, seat_h - 0.015), fabric("dark", 0.95), bevel=0.027,
        parent=root)
    box("Chair_Seat_Waterfall", (0.46, 0.06, 0.05), (0, -0.25, seat_h - 0.035), fabric("dark", 0.95), bevel=0.022,
        rot=(R(-30), 0, 0), parent=root)
    # Back: like the real mesh chairs, the back is narrow at the waist and wide at the shoulders (a rounded
    # trapezoid), curves back over the lumbar and wraps forward at the sides. A thick moulded frame holds the
    # mesh, and a U-shaped yoke carries it from the tilt mechanism.
    by, bz0, bz1 = 0.19, seat_h + 0.07, seat_h + 0.6

    def back_point(u, v):
        """u = -1..1 across, v = 0 (bottom) .. 1 (top) -> a point on the curved back."""
        half_w = 0.155 + 0.08 * math.sin(0.5 * math.pi * min(1.0, v / 0.8))   # narrow waist, wide shoulders
        lean = 0.09 * v + 0.05 * v * v - 0.025 * math.sin(math.pi * v)        # lumbar bulge, leaning back
        return Vector((u * half_w, by + lean - 0.045 * u * u, bz0 + v * (bz1 - bz0)))

    outline = []                                                    # rounded-rectangle outline in (u, v)
    for k in range(48):
        a = 2 * math.pi * k / 48
        outline.append((math.copysign(abs(math.cos(a)) ** 0.3, math.cos(a)),
                        0.5 + 0.5 * math.copysign(abs(math.sin(a)) ** 0.3, math.sin(a))))
    tube("Chair_Back_Frame", [back_point(u, v) for u, v in outline], 0.017, base, closed=True, parent=root)
    bm = bmesh.new()                                                # mesh panel: rings shrinking to the centre
    rings = [[bm.verts.new(back_point(u * s, 0.5 + (v - 0.5) * s) + Vector((0, 0.003, 0))) for u, v in outline]
             for s in (0.97, 0.66, 0.33)]
    for ra, rb in zip(rings, rings[1:]):
        for k in range(48):
            bm.faces.new((ra[k], ra[(k + 1) % 48], rb[(k + 1) % 48], rb[k]))
    mid = bm.verts.new(back_point(0, 0.5) + Vector((0, 0.003, 0)))
    for k in range(48):
        bm.faces.new((rings[-1][k], rings[-1][(k + 1) % 48], mid))
    panel = _obj("Chair_Back_Mesh", bm)
    _finish(panel, see_through("dark", 0.8, 0.85), 0, None, root)
    yoke_top = back_point(0, 0.0) + Vector((0, 0.03, -0.03))
    tube("Chair_Yoke", bezier((0, 0.1, seat_h - 0.09), (0, by + 0.04, seat_h - 0.09), yoke_top, 8), 0.02, base,
         parent=root)
    for sx in (-1, 1):
        tube(f"Chair_Yoke_Arm_{sx}", bezier(yoke_top, yoke_top + Vector((sx * 0.1, 0.0, 0.0)),
                                            back_point(sx * 0.92, 0.12) + Vector((0, 0.012, 0)), 8), 0.015, base,
             parent=root)
    for sx in (-1, 1):                                              # armrests: curved support + soft pad
        ax = sx * 0.27
        tube(f"Chair_Arm_Support_{sx}", bezier((sx * 0.12, 0.06, seat_h - 0.08), (sx * 0.31, 0.12, seat_h - 0.07),
                                               (ax, 0.05, seat_h + 0.195), 10), 0.016, base, parent=root)
        box(f"Chair_Arm_Pad_{sx}", (0.075, 0.25, 0.03), (ax, 0.01, seat_h + 0.21), mat("dark", 0.7,
            color=shade(COLORS["dark"], 1.15)), bevel=0.013, parent=root)


def build_rug():
    """Flatwoven rug 230 x 160 cm: plain field, bands of stripes at both short ends and short fringes."""
    root, w, d, h = furniture_root("rug")
    weave = fabric("cream", 0.95) if THEME != "japandi" else fabric("main", 0.95)
    box("Rug_Field", (w, d, h), (0, 0, h / 2), surface(mat("rugfield", 0.95, color=shade(COLORS["wall_trim"], 1.02)),
                                                     "fabric"), bevel=0.002, parent=root)
    for sx in (-1, 1):
        for k, (off, width, key) in enumerate(((0.1, 0.06, "main"), (0.19, 0.02, "dark"), (0.24, 0.02, "main"),
                                               (0.3, 0.04, "accent_1"))):
            box(f"Rug_Stripe_{k}", (width, d - 0.004, 0.002), (sx * (w / 2 - off), 0, h + 0.0005),
                fabric(key, 0.95), bevel=0, parent=root)
        boxes(f"Rug_Fringe_{sx}", [((0.05, 0.005, 0.003), (sx * (w / 2 + 0.024), -d / 2 + 0.02 + k * 0.025, 0.002))
                                   for k in range(int((d - 0.03) / 0.025))], weave, parent=root)


def build_lamp():
    """Clamp-on work lamp: desk clamp, two straight arms with tension springs, rounded cone shade."""
    root, w, d, h = furniture_root("lamp")
    m = powder("main", 0.35) if THEME != "japandi" else powder("dark", 0.4)
    cy = d / 2 - 0.03
    box("Lamp_Clamp_Top", (0.05, 0.07, 0.014), (0, cy, 0.007), m, bevel=0.004, parent=root)
    box("Lamp_Clamp_Jaw", (0.05, 0.016, 0.08), (0, cy + 0.035, -0.03), m, bevel=0.004, parent=root)
    cyl("Lamp_Clamp_Screw", 0.006, 0.05, (0, cy + 0.035, -0.08), steel(), parent=root)
    cyl("Lamp_Post", 0.009, 0.07, (0, cy, 0.045), m, parent=root)
    pivot = Vector((0, cy, 0.08))
    elbow = Vector((0, cy - 0.06, 0.44))
    head = Vector((0, -d / 2 + 0.08, 0.5))
    for sx in (-1, 1):                                              # twin arm bars, like the real lamp
        off = Vector((sx * 0.009, 0, 0))
        rod("Lamp_Arm_Lower", pivot + off, elbow + off, 0.0045, m, parent=root)
        rod("Lamp_Arm_Upper", elbow + off, head + off, 0.0045, m, parent=root)
    for a, b, nm in ((pivot, elbow, "Lower"), (elbow, head, "Upper")):  # coil springs running beside each arm
        axis = b - a
        n = axis.normalized()
        side = n.cross(Vector((1, 0, 0))).normalized()
        start, end = a + axis * 0.18 + side * 0.022, a + axis * 0.62 + side * 0.022
        coils = []
        for k in range(73):
            t = k / 72
            ang = t * 18 * 2 * math.pi
            coils.append(start.lerp(end, t) + Vector((math.cos(ang) * 0.005, 0, 0)) + side * math.sin(ang) * 0.005)
        tube(f"Lamp_Spring_{nm}", coils, 0.0012, steel(), segs=4, parent=root)
        rod(f"Lamp_Spring_Rod_{nm}", a + side * 0.01, start, 0.0012, steel(), parent=root)
    ball("Lamp_Elbow", 0.012, elbow, m, scale=(1.8, 1, 1), parent=root)
    ball("Lamp_Knuckle", 0.013, head, m, scale=(1.8, 1, 1), parent=root)
    shade_dir = Vector((0, -0.35, -1)).normalized()                # the shade points down and a bit forward
    rot = shade_dir.to_track_quat("-Z", "Y").to_euler()
    centre = head + shade_dir * 0.075 + Vector((0, -0.01, 0))
    sh = cyl("Lamp_Shade", 0.085, 0.11, centre, m, r2=0.035, segs=40, bevel=0.004, parent=root)
    sh.rotation_euler = rot
    ring = cyl("Lamp_Shade_Vents", 0.042, 0.012, head + shade_dir * 0.035, mat("dark", 0.6), segs=40, bevel=0,
               parent=root)
    ring.rotation_euler = rot
    cap = ball("Lamp_Shade_Cap", 0.036, head + shade_dir * 0.025, m, scale=(1, 1, 0.6), parent=root)
    cap.rotation_euler = rot
    bulb = ball("Lamp_Bulb", 0.03, head + shade_dir * 0.11, mat("bulb", 0.3, emit=6.0, color="#FFE6B8"),
                parent=root)
    no_shadow(sh, bulb)
    tube("Lamp_Cable", bezier(pivot + Vector((0.0, 0.01, -0.02)), (0.0, d / 2 + 0.01, -0.3), (0.05, d / 2, -0.7), 8),
         0.0025, PLASTIC, parent=root)


def build_shelf():
    """Cube shelf 2 x 4 (77 x 39 x 147 cm): chunky 4 cm outer frame, thin 1.6 cm dividers, no back panel,
    fabric storage boxes, books (project titles on three of them) and records."""
    root, w, d, h = furniture_root("shelf")
    hook_link(root, "github")
    o, i_ = 0.04, 0.016
    cw = (w - 2 * o - i_) / 2
    ch = (h - 2 * o - 3 * i_) / 4
    for sx in (-1, 1):
        box("Shelf_Side", (o, d, h), (sx * (w / 2 - o / 2), 0, h / 2), MELAMINE, bevel=0.002, parent=root)
    for z in (o / 2, h - o / 2):
        box("Shelf_TopBottom", (w - 2 * o, d, o), (0, 0, z), MELAMINE, bevel=0.002, parent=root)
    box("Shelf_Divider_V", (i_, d - 0.002, h - 2 * o), (0, 0, h / 2), MELAMINE, bevel=0.001, parent=root)
    for k in range(3):
        box("Shelf_Divider_H", (w - 2 * o, d - 0.002, i_), (0, 0, o + ch * (k + 1) + i_ * k + i_ / 2), MELAMINE,
            bevel=0.001, parent=root)

    def cube(col, row):
        """Bottom-centre of one cube opening in shelf coordinates."""
        return Vector(((col - 0.5) * (cw + i_), 0, o + row * (ch + i_)))

    box_cols = ["main", "accent_2"] if THEME != "japandi" else ["accent_2", "main"]
    for col in (0, 1):                                              # fabric boxes with a front pull-tab
        p = cube(col, 0)
        b = box(f"Shelf_FabricBox_{col}", (cw - 0.012, d - 0.03, ch - 0.01), p + Vector((0, -0.01, (ch - 0.01) / 2)),
                fabric(box_cols[col], 0.95), bevel=0.008, parent=root)
        box(f"Shelf_FabricBox_Tab_{col}", (0.09, 0.006, 0.03), p + Vector((0, -d / 2 + 0.003, ch * 0.7)),
            mat("dark", 0.7), bevel=0.006, parent=root)
    p = cube(0, 1)                                                  # vinyl records leaning in one cube
    for k in range(14):
        box("Shelf_Record", (0.006, 0.31, 0.31), p + Vector((-cw / 2 + 0.01 + k * 0.009, -0.01, 0.155)),
            mat(random.choice(["dark", "accent_1", "cream", "main", "accent_3"]), 0.7), bevel=0.001,
            rot=(0, R(-4 if k > 10 else 0), 0), parent=root)
    p = cube(1, 1)                                                  # project titles on three lying books
    for k, key in enumerate(("dark", "accent_1", "main")):
        bz = 0.022 + k * 0.042
        box("Shelf_TitleBook", (cw - 0.07 - k * 0.025, 0.24, 0.04), p + Vector((-0.01, -0.03, bz)), mat(key, 0.7),
            bevel=0.003, parent=root)
        box("Shelf_TitleBook_Pages", (cw - 0.08 - k * 0.025, 0.236, 0.032), p + Vector((-0.01, -0.028, bz)), PAPER,
            bevel=0, parent=root)
        hook_text("title", k + 1, ["Clean Code Notes", "My First API", "CSS Tricks"][k], 0.02,
                  p + Vector((-0.01, -0.152, bz)), material=mat("cream", 0.5) if key != "main" else mat("dark", 0.5),
                  max_width=cw - 0.1 - k * 0.025, parent=root, depth=0.001)
    cyl("Shelf_Figure_Base", 0.03, 0.02, p + Vector((0.09, -0.04, 0.142)), mat("dark", 0.4), parent=root)
    ball("Shelf_Figure", 0.035, p + Vector((0.09, -0.04, 0.185)), ceramic("accent_3"), scale=(1, 1, 1.1),
         parent=root)
    for row in (2, 3):                                              # books with varied size, colour and lean
        for col in (0, 1):
            p = cube(col, row)
            x = -cw / 2 + 0.008
            stop = cw / 2 - (0.12 if (row, col) in ((2, 1), (3, 0)) else 0.01)
            while x < stop - 0.02:
                bw = random.uniform(0.018, 0.04)
                bh = random.uniform(0.2, min(0.3, ch - 0.02))
                bd = random.uniform(0.17, 0.24)
                key = random.choice(["main", "accent_1", "accent_2", "accent_3", "cream", "dark", "plant"])
                box("Shelf_Book", (bw, bd, bh), p + Vector((x + bw / 2, -d / 2 + 0.03 + bd / 2, bh / 2)),
                    mat(key, 0.7), bevel=0.002, parent=root)
                box("Shelf_Book_Pages", (bw - 0.004, 0.002, bh - 0.01), p + Vector((x + bw / 2, -d / 2 + 0.028 + bd,
                    bh / 2)), PAPER, bevel=0, parent=root)
                x += bw + random.uniform(0.0, 0.004)
            if (row, col) == (2, 1):                                # a small succulent in the gap
                cyl("Shelf_Pot", 0.04, 0.07, p + Vector((cw / 2 - 0.06, -0.03, 0.035)), ceramic("cream"), r2=0.045,
                    parent=root)
                for k in range(7):
                    a = k * 0.9
                    ball("Shelf_Succulent", 0.022, p + Vector((cw / 2 - 0.06 + math.cos(a) * 0.02,
                         -0.03 + math.sin(a) * 0.02, 0.085 + 0.01 * (k % 2))), mat("plant", 0.5, color=shade(
                         COLORS["plant"], 1.15)), scale=(0.7, 0.7, 1.3), parent=root)
            if (row, col) == (3, 0):                                # a desk speaker / alarm clock
                box("Shelf_Speaker", (0.09, 0.12, 0.14), p + Vector((cw / 2 - 0.06, -0.04, 0.07)),
                    fabric("cream", 0.95), bevel=0.012, parent=root)
    # On top: a small storage box and a trailing plant.
    # On top: two board-game boxes and a trailing plant in a glazed pot.
    for k, (key, th, turn) in enumerate((("accent_1", 0.07, 0), ("main", 0.05, 6))):
        z0 = h + (0, 0.07)[k]
        box(f"Shelf_Game_{k}", (0.3, 0.3, th), (-w * 0.18, 0.01, z0 + th / 2), mat(key, 0.6), bevel=0.003,
            rot=(0, 0, R(turn)), parent=root)
        box(f"Shelf_Game_Lid_{k}", (0.302, 0.302, 0.003), (-w * 0.18, 0.01, z0 + th * 0.62), mat("cream", 0.6),
            bevel=0, rot=(0, 0, R(turn)), parent=root)
    tp = Vector((w * 0.25, -0.03, h))
    cyl("Shelf_TopPot", 0.06, 0.1, tp + Vector((0, 0, 0.05)), ceramic("accent_1"), r2=0.07, parent=root)
    cyl("Shelf_TopSoil", 0.064, 0.008, tp + Vector((0, 0, 0.098)), mat("soil", 0.95, color="#4A3828"), bevel=0,
        parent=root)
    for v in range(3):                                              # vines over the front edge
        st = tp + Vector((-0.03 + 0.03 * v, -0.03, 0.1))
        pts = bezier(st, st + Vector((0.02 * v, -0.1, 0.03)), st + Vector((0.03 * (v - 1), -0.2, -0.18 - 0.12 * v)), 8)
        tube(f"Shelf_Vine_{v}", pts, 0.003, mat("stem", 0.6, color=shade(COLORS["plant"], 0.8)), segs=5, parent=root)
        for k, pnt in enumerate(pts[1::2]):
            heart_leaf(f"Shelf_VineLeaf_{v}_{k}", 0.05, pnt + Vector((0, -0.005, -0.01)),
                       (R(75), 0, R(15 * ((k + v) % 3 - 1))), leaf_m).parent = root
    for k in range(6):
        a = k * 1.05
        heart_leaf(f"Shelf_TopLeaf_{k}", 0.06, tp + Vector((math.cos(a) * 0.04, math.sin(a) * 0.04, 0.14)),
                   (R(30), 0, a + R(90)), leaf_m).parent = root


def build_wall_art():
    """Two picture frames with white mounts: a 52 x 42 cm landscape frame and a 32 x 42 cm portrait one."""
    root, w, d, h = furniture_root("wall_art")
    mount = surface(mat("cream", 0.9, color="#FBFAF6"), "paper")
    frames = [(-0.09, 0.27, 0.52, 0.42, (0.39, 0.29), "accent_2", oak(0.5)),
              (0.2, 0.71, 0.3, 0.4, (0.2, 0.29), "main", powder("dark", 0.45))]
    for i, (fx, fz, fw, fh, (pw, ph), key, fmat) in enumerate(frames):
        box("Art_Frame", (fw, d, fh), (fx, 0, fz), fmat, bevel=0.003, parent=root)
        box("Art_Mount", (fw - 0.04, 0.004, fh - 0.04), (fx, -d / 2 - 0.001, fz), mount, bevel=0, parent=root)
        pic = hook_image("frame", i + 1, (pw, ph), (fx, -d / 2 - 0.004, fz), parent=root, default_key=key)
        y = -d / 2 - 0.0055
        if i == 0:                                                  # a line-art mountain print
            deco = [flat("Art_Mountain", [(-0.19, -0.14), (-0.06, 0.04), (0.0, -0.03), (0.09, 0.09), (0.19, -0.04),
                                          (0.19, -0.14)], mat("main", 0.8), (fx, y, fz), (R(90), 0, 0), root),
                    ball("Art_Sun", 0.035, (fx - 0.1, y + 0.001, fz + 0.07), mat("accent_1", 0.8), scale=(1, 0.05, 1),
                         parent=root)]
        else:                                                       # a botanical print
            deco = [tube("Art_Stem", bezier((fx, y, fz - 0.12), (fx + 0.04, y, fz), (fx - 0.01, y, fz + 0.11), 8),
                         0.002, mat("plant", 0.6), parent=root)]
            for k in range(4):
                deco.append(heart_leaf(f"Art_Leaf_{k}", 0.06, (fx + (0.03 if k % 2 else -0.025), y, fz - 0.07 + k * 0.05),
                                       (R(90), R(60 if k % 2 else -60), 0), mat("plant", 0.6)))
                deco[-1].parent = root
        hook_default(pic, *deco)


def monstera_leaf(name, size, material, rng):
    """Monstera deliciosa leaf: a broad heart (almost as wide as long, two round lobes behind the stalk) with
    4-6 deep, narrow splits per side that run in along the side veins, leaving wide lobes between them.
    Each half is tilted up a little from the midrib, so the leaf has the real shallow V-fold."""
    ctrl = [(0.0, 0.0), (0.16, -0.1), (0.36, -0.07), (0.5, 0.08), (0.55, 0.3), (0.5, 0.54), (0.38, 0.75),
            (0.2, 0.92), (0.0, 1.0)]
    edge = []
    for a, b in zip(ctrl, ctrl[1:]):                                # densify the outline
        for t in (0.0, 0.25, 0.5, 0.75):
            edge.append((a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t))
    edge.append(ctrl[-1])
    halves = []
    for side in (1, -1):
        cuts = sorted(rng.sample(range(11, len(edge) - 6, 3), k=4))
        half = []
        for k, (x, y) in enumerate(edge):
            if k in cuts:                                           # a split towards the midrib, angled to the tip
                depth = rng.uniform(0.6, 0.8)                      # side veins rise from midrib to edge
                half += [(x, y - 0.024), (x * (1 - depth), y - 0.09 * depth), (x * (1 - depth) + 0.008, y - 0.085 * depth),
                         (x, y + 0.024)]
            else:
                half.append((x, y))
        fold = R(12) * side
        pts = [(x * side * size * math.cos(fold), y * size, abs(x) * size * math.sin(abs(fold))) for x, y in half]
        bm = bmesh.new()
        vs = [bm.verts.new(p) for p in pts] + [bm.verts.new((0, y * size, 0)) for y in (0.7, 0.4)]
        if side < 0:
            vs.reverse()
        bm.faces.new(vs)
        halves.append(bm)
    bm = halves[0]                                                  # join both halves into one mesh
    me_tmp = bpy.data.meshes.new("tmp")
    halves[1].to_mesh(me_tmp)
    halves[1].free()
    bm.from_mesh(me_tmp)
    bpy.data.meshes.remove(me_tmp)
    leaf = _finish(_obj(name, bm), material, 0, None, None)
    tube(name + "_Midrib", [(0, 0.0, 0.002), (0, 0.5 * size, 0.003), (0, 0.97 * size, 0.001)], 0.0025,
         mat("stem", 0.55, color=shade(COLORS["plant"], 1.2)), segs=5).parent = leaf
    return leaf


def build_plant():
    """Monstera in a 24 cm glazed ceramic pot with a rim and saucer."""
    root, w, d, h = furniture_root("plant")
    rng = random.Random(SEED + 3)
    pot = ceramic("cream" if THEME != "japandi" else "accent_1")
    cyl("Plant_Saucer", 0.15, 0.025, (0, 0, 0.0125), pot, r2=0.16, segs=48, bevel=0.006, parent=root)
    cyl("Plant_Pot", 0.11, 0.24, (0, 0, 0.145), pot, r2=0.135, segs=48, bevel=0.006, parent=root)
    cyl("Plant_Pot_Rim", 0.142, 0.03, (0, 0, 0.255), pot, segs=48, bevel=0.008, parent=root)
    cyl("Plant_Soil", 0.128, 0.01, (0, 0, 0.262), mat("soil", 0.95, color="#4A3828"), segs=40, bevel=0, parent=root)
    cyl("Plant_Pole", 0.014, 0.55, (0.02, 0.02, 0.52), surface(mat("coir", 0.95, color="#8A6A48"), "knit"),
        parent=root)
    stem_m = mat("stem", 0.55, color=shade(COLORS["plant"], 0.85))
    leaves = [mat("plant", 0.45, color=shade(COLORS["plant"], 0.9)), mat("plant", 0.45, color=shade(COLORS["plant"], 0.75))]
    base = Vector((0, 0, 0.26))
    for k in range(9):                                              # long stalks arching out, leaves hanging off
        a = k * 2.4 + 0.5                                           # their tips like real Monstera leaves
        reach = rng.uniform(0.12, 0.2)
        rise = rng.uniform(0.3, h - 0.38)
        tip = base + Vector((math.cos(a) * reach, math.sin(a) * reach, rise))
        tube(f"Plant_Stem_{k}", bezier(base + Vector((0.01 * math.cos(a), 0.01 * math.sin(a), 0)),
                                       base + Vector((math.cos(a) * reach * 0.3, math.sin(a) * reach * 0.3, rise * 0.9)),
                                       tip, 8), 0.0065, stem_m, segs=6, parent=root)
        lf = monstera_leaf(f"Plant_Leaf_{k}", rng.uniform(0.28, 0.36), leaves[k % 2], rng)
        lf.parent = root
        lf.location = tip
        lf.rotation_euler = Euler((R(rng.uniform(-38, -12)), R(rng.uniform(-15, 15)), a - R(90)), "XYZ")


def build_pet():
    """A tabby cat curled up asleep on a seat cushion on the window board: round body, head tucked on the
    front paws, tail wrapped around the front."""
    root, w, d, h = furniture_root("pet")
    fur = mat("pet", 0.9)
    dark_fur = mat("pet_stripe", 0.9, color=shade(COLORS["pet"], 0.72))
    box("Pet_Cushion", (w - 0.02, d - 0.02, 0.045), (0, 0, 0.0225), fabric("accent_1" if THEME != "night" else "main"),
        bevel=0.018, parent=root)
    ball("Pet_Body", 0.115, (0.035, 0.02, 0.11), fur, scale=(1.25, 0.95, 0.6), parent=root)
    ball("Pet_Haunch", 0.08, (0.1, 0.035, 0.11), fur, scale=(1, 1, 0.85), parent=root)
    for k in range(3):                                              # tabby markings lying on the fur
        ball("Pet_Marking", 0.05, (0.0 + k * 0.06, 0.04, 0.16 - 0.006 * k), dark_fur, scale=(0.35, 1.3, 0.25),
             parent=root)
    head = Vector((-0.115, -0.03, 0.115))
    ball("Pet_Head", 0.06, head, fur, scale=(1.0, 1.0, 0.86), parent=root)
    ball("Pet_Cheeks", 0.04, head + Vector((-0.004, -0.03, -0.018)), fur, scale=(1.35, 0.9, 0.8), parent=root)
    ball("Pet_Muzzle", 0.018, head + Vector((-0.006, -0.056, -0.02)), mat("cream", 0.9), scale=(1.5, 0.8, 0.8),
         parent=root)
    ball("Pet_Nose", 0.006, head + Vector((-0.006, -0.068, -0.01)), mat("nose", 0.6, color="#C9786A"), parent=root)
    for sx in (-1, 1):
        ear = cyl("Pet_Ear", 0.022, 0.042, head + Vector((sx * 0.03, 0.005, 0.052)), fur, r2=0.002, segs=4, bevel=0,
                  parent=root)
        ear.rotation_euler = (R(-12), R(sx * 20), R(45))
        tube("Pet_Eye", [head + Vector((sx * 0.024 + 0.01 * math.cos(a), -0.057, 0.012 - 0.004 * math.sin(a)))
                         for a in (math.pi * k / 6 for k in range(7))], 0.0016, mat("dark", 0.5), segs=5, parent=root)
    ball("Pet_Paw", 0.024, (-0.07, -0.085, 0.07), fur, scale=(1.6, 0.9, 0.6), parent=root)
    tail = [(0.17 - 0.06 * (1 - math.cos(t)) - 0.12 * t / math.pi, -0.02 - 0.075 * math.sin(t), 0.075 - 0.01 * t)
            for t in (math.pi * k / 10 for k in range(11))]
    tube("Pet_Tail", tail, 0.019, fur, segs=10, parent=root)
    ball("Pet_Tail_Tip", 0.019, tail[-1], dark_fur, scale=(1.4, 1, 1), parent=root)


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
    "desk": build_desk, "cabinet": build_cabinet, "monitor": build_monitor, "chair": build_chair, "rug": build_rug,
    "lamp": build_lamp, "shelf": build_shelf, "wall_art": build_wall_art, "plant": build_plant, "pet": build_pet,
}
if SHOW_PLACEHOLDER_FURNITURE:
    for slot_name, build in PLACEHOLDERS.items():
        build()


# =====================================================================
#  PORTFOLIO WALL  (screens, pegboard, cork board, poster, letter board)
# =====================================================================
# Two monitor screens. They belong to SLOT_monitor (not the placeholder), so they stay
# in place even if you swap in your own monitor model.
mon_turn = SLOTS["monitor"].rotation_euler.z
screen_cols = ["accent_1", "accent_3", "main", "plant", "accent_2"]
SW, SH = PANEL
for i, sx in enumerate((-1, 1)):
    toe = -sx * MON_TOE                                             # match the turned-in monitor heads
    front = Vector((0.0115 * math.sin(toe), -0.0115 * math.cos(toe), 0))
    scr = hook_image("screen", i + 1, (SW, SH), slot_point("monitor", Vector((sx * MON_X, MON_Y, MON_Z)) + front),
                     rot=(0, 0, mon_turn + toe), glow=True, default_key="screen" if i == 0 else "cream")
    y = -0.0015
    deco = []
    if i == 0:                                                      # left screen: a code editor
        deco.append(box("Screen_Sidebar", (0.08, 0.001, SH), (-SW / 2 + 0.04, y, 0), mat("dark", 0.5, emit=0.6),
                        bevel=0, parent=scr))
        deco.append(box("Screen_Tabs", (SW - 0.08, 0.001, 0.018), (0.04, y, SH / 2 - 0.009),
                        mat("dark", 0.5, emit=0.45, color=shade(COLORS["screen"], 1.3)), bevel=0, parent=scr))
        for row in range(13):
            x = -SW / 2 + 0.1 + 0.018 * random.choice([0, 0, 1, 1, 2])
            box("Screen_LineNo", (0.008, 0.001, 0.006), (-SW / 2 + 0.09, y, SH / 2 - 0.04 - row * 0.02),
                mat("metal", 0.5, emit=0.5), bevel=0, parent=scr)
            for seg in range(random.randint(1, 3)):
                L = random.uniform(0.03, 0.1)
                if x + L > SW / 2 - 0.02:
                    break
                deco.append(box("Screen_Code", (L, 0.001, 0.007), (x + L / 2, y, SH / 2 - 0.04 - row * 0.02),
                                mat(random.choice(screen_cols), 0.4, emit=1.2), bevel=0, parent=scr))
                x += L + 0.01
        deco += [o for o in scr.children if o.name.startswith("Screen_LineNo")]
    else:                                                           # right screen: a website you are building
        deco.append(box("Screen_Nav", (SW, 0.001, 0.03), (0, y, SH / 2 - 0.015), mat("main", 0.5, emit=0.8), bevel=0,
                        parent=scr))
        deco.append(box("Screen_Hero", (SW - 0.06, 0.001, 0.1), (0, y, 0.035), mat("accent_1", 0.5, emit=0.8), bevel=0,
                        parent=scr))
        for k, key in enumerate(("accent_2", "accent_3", "accent_2")):
            deco.append(box("Screen_Card", (0.14, 0.001, 0.08), (-0.16 + k * 0.16, y, -0.085), mat(key, 0.5, emit=0.8),
                            bevel=0, parent=scr))
    hook_default(scr, *deco)

# Pegboard (76 x 56 cm, white) on its rail above the left half of the desk: staggered pill-shaped slots,
# a little shelf, two cups and a hook with over-ear headphones.
PG_X, PG_Z, PG_W, PG_H = 0.7, 1.72, 0.76, 0.56
PGY = D - 0.018
box("Pegboard_Rail", (PG_W - 0.1, 0.012, 0.05), (PG_X, D - 0.006, PG_Z + 0.1), MELAMINE, bevel=0.002)
box("Pegboard", (PG_W, 0.012, PG_H), (PG_X, PGY, PG_Z), MELAMINE, bevel=0.003)
slots_ = []
for r_ in range(int((PG_H - 0.04) / 0.028)):
    for c in range(int((PG_W - 0.04) / 0.04)):
        x = PG_X - PG_W / 2 + 0.03 + c * 0.04 + (0.02 if r_ % 2 else 0)
        if x < PG_X + PG_W / 2 - 0.02:
            slots_.append(((0.006, 0.004, 0.018), (x, PGY - 0.0045, PG_Z - PG_H / 2 + 0.035 + r_ * 0.028)))
boxes("Pegboard_Slots", slots_, mat("dark", 0.9, color=shade(COLORS["cream"], 0.35)), bevel=0.002)
pg_front = PGY - 0.006
box("Pegboard_Shelf", (0.36, 0.1, 0.008), (PG_X + 0.14, pg_front - 0.05, PG_Z + 0.06), MELAMINE, bevel=0.002)
box("Pegboard_Shelf_Lip", (0.36, 0.006, 0.025), (PG_X + 0.14, pg_front - 0.098, PG_Z + 0.072), MELAMINE, bevel=0.002)
cyl("Pegboard_Shelf_Pot", 0.035, 0.065, (PG_X + 0.04, pg_front - 0.05, PG_Z + 0.097), ceramic("accent_1"), r2=0.04)
for k in range(5):
    a = k * 1.3
    heart_leaf(f"Pegboard_Leaf_{k}", 0.05, (PG_X + 0.04 + 0.03 * math.cos(a), pg_front - 0.05 + 0.02 * math.sin(a),
               PG_Z + 0.15 + 0.01 * (k % 2)), (R(40), 0, a), leaf_m)
for k, (key, bh) in enumerate((("dark", 0.15), ("accent_3", 0.13), ("main", 0.14))):
    box(f"Pegboard_Book_{k}", (0.022, 0.09, bh), (PG_X + 0.2 + k * 0.024, pg_front - 0.05, PG_Z + 0.064 + bh / 2),
        mat(key, 0.7), bevel=0.002)
for k, cx in enumerate((PG_X - 0.27, PG_X - 0.16)):                 # cups holding pens, a ruler, scissors
    cyl(f"Pegboard_Cup_{k}", 0.035, 0.08, (cx, pg_front - 0.036, PG_Z - 0.12), MELAMINE, segs=24)
    for j, key in enumerate(("dark", "accent_1", "main")):
        rod(f"Pegboard_Pen_{k}{j}", (cx - 0.012 + 0.012 * j, pg_front - 0.036, PG_Z - 0.14),
            (cx - 0.02 + 0.02 * j, pg_front - 0.04, PG_Z - 0.03 - 0.01 * j), 0.004, mat(key, 0.4))
cyl("Pegboard_Hook", 0.004, 0.07, (PG_X + 0.16, pg_front - 0.035, PG_Z - 0.1), steel(), rot=(R(90), 0, 0))
hp = Vector((PG_X + 0.16, pg_front - 0.06, PG_Z - 0.1))             # over-ear headphones hanging on the hook
tube("Headphones_Band", [hp + Vector((math.cos(a) * 0.09, 0, math.sin(a) * 0.11 - 0.11))
                         for a in (math.pi * k / 16 for k in range(17))], 0.009, mat("dark", 0.5))
for sx in (-1, 1):
    cyl("Headphones_Cup", 0.045, 0.04, hp + Vector((sx * 0.09, 0, -0.14)), mat("dark", 0.45), rot=(0, R(90), 0),
        segs=28, bevel=0.012)
    cyl("Headphones_Pad", 0.042, 0.02, hp + Vector((sx * 0.065, 0, -0.14)), fabric("dark", 0.95), rot=(0, R(90), 0),
        segs=28, bevel=0.008)

# Cork notice board 90 x 60 cm with a pine frame: one pinned project print + sticky notes with your skills.
PB_X, PB_Z, PB_W, PB_H = 1.6, 1.72, 0.9, 0.6
pine = surface(mat("wood", 0.55, color=shade(COLORS["wood"], 1.08)), "wood")
for nm, size, loc in [("T", (PB_W, 0.022, 0.025), (PB_X, D - 0.011, PB_Z + PB_H / 2 - 0.0125)),
                      ("B", (PB_W, 0.022, 0.025), (PB_X, D - 0.011, PB_Z - PB_H / 2 + 0.0125)),
                      ("L", (0.025, 0.022, PB_H - 0.05), (PB_X - PB_W / 2 + 0.0125, D - 0.011, PB_Z)),
                      ("R", (0.025, 0.022, PB_H - 0.05), (PB_X + PB_W / 2 - 0.0125, D - 0.011, PB_Z))]:
    box(f"Corkboard_Frame_{nm}", size, loc, pine, bevel=0.003)
box("Corkboard_Cork", (PB_W - 0.04, 0.01, PB_H - 0.04), (PB_X, D - 0.006, PB_Z), surface(mat("cork", 0.95),
    "terrazzo", scale=3.0), bevel=0)
fy = D - 0.012
board = hook_image("board", 1, (0.36, 0.25), (PB_X - 0.18, fy - 0.003, PB_Z + 0.1), rot=(0, R(-2), 0),
                   default_key="accent_2")
box("Corkboard_Print_Border", (0.38, 0.002, 0.27), (PB_X - 0.18, fy - 0.0015, PB_Z + 0.1), PAPER, bevel=0,
    rot=(0, R(-2), 0))
hook_default(board,
             ball("Board_Sun", 0.03, (PB_X - 0.27, fy - 0.006, PB_Z + 0.15), mat("accent_3", 0.7), scale=(1, 0.1, 1)),
             box("Board_Wire_1", (0.22, 0.002, 0.03), (PB_X - 0.15, fy - 0.006, PB_Z + 0.07), mat("main", 0.6), bevel=0),
             box("Board_Wire_2", (0.14, 0.002, 0.05), (PB_X - 0.2, fy - 0.006, PB_Z + 0.01), mat("cream", 0.6), bevel=0))
for px, pz in ((-0.355, 0.215), (-0.005, 0.225)):
    cyl("Corkboard_Pin", 0.007, 0.012, (PB_X + px, fy - 0.009, PB_Z + pz), mat("accent_1", 0.3), rot=(R(90), 0, 0),
        segs=16, bevel=0.002)
note_spots = [(0.2, 0.17), (0.33, 0.15), (0.2, 0.03), (0.33, 0.02), (-0.28, -0.17), (0.25, -0.16)]
note_cols = ["accent_3", "accent_3", "accent_2", "accent_1", "accent_3", "cream"]
random.shuffle(note_cols)
skills = ["HTML", "CSS", "JavaScript", "Git", "UX", ""]
for k, (nx, nz) in enumerate(note_spots):                           # 10 x 10 cm sticky notes
    tilt = R(random.uniform(-5, 5))
    loc = Vector((PB_X + nx, fy - 0.0015, PB_Z + nz))
    box(f"Corkboard_Note_{k}", (0.11, 0.002, 0.11), loc, mat(note_cols[k], 0.8), bevel=0, rot=(0, tilt, 0))
    cyl(f"Corkboard_NotePin_{k}", 0.006, 0.01, loc + Vector((0, -0.006, 0.042)),
        mat("dark" if k % 2 else "accent_1", 0.3), rot=(R(90), 0, 0), segs=12, bevel=0.002)
    if skills[k]:
        hook_text("skill", k + 1, skills[k], 0.03, loc + Vector((0, -0.003, -0.008)), rot=(R(90), tilt, 0),
                  material=mat("dark", 0.6), max_width=0.095, depth=0.001)
    else:                                                           # a tiny to-do list
        for r_ in range(3):
            box("Corkboard_Todo", (0.06, 0.001, 0.007), loc + Vector((0.012, -0.0025, 0.025 - r_ * 0.025)),
                mat("dark", 0.6), bevel=0, rot=(0, tilt, 0))
            box("Corkboard_Tick", (0.01, 0.001, 0.01), loc + Vector((-0.035, -0.0025, 0.025 - r_ * 0.025)),
                mat("accent_1" if r_ < 2 else "dark", 0.6), bevel=0, rot=(0, tilt, 0))
box("Corkboard_Calendar", (0.2, 0.002, 0.15), (PB_X - 0.12, fy - 0.0015, PB_Z - 0.17), PAPER, bevel=0,
    rot=(0, R(2), 0))
boxes("Corkboard_Calendar_Grid", [((0.018, 0.001, 0.014), (PB_X - 0.2 + (k % 7) * 0.026, fy - 0.003,
                                   PB_Z - 0.14 - (k // 7) * 0.022)) for k in range(28)], mat("main", 0.7))
cyl("Corkboard_CalPin", 0.006, 0.01, (PB_X - 0.12, fy - 0.007, PB_Z - 0.105), mat("main", 0.3), rot=(R(90), 0, 0),
    segs=12, bevel=0.002)

# Poster in a thin black aluminium frame on the left wall, near the front (faces into the room, +X).
PO_Y, PO_Z, PO_W, PO_H = 0.62, 1.58, 0.5, 0.7
box("Poster_Frame", (0.02, PO_W + 0.03, PO_H + 0.03), (0.01, PO_Y, PO_Z), powder("dark", 0.4), bevel=0.002)
box("Poster_Paper", (0.003, PO_W, PO_H), (0.021, PO_Y, PO_Z), PAPER, bevel=0)
poster = hook_image("poster", 1, (PO_W - 0.06, PO_H - 0.08), (0.0235, PO_Y, PO_Z + 0.01), rot=(0, 0, R(90)),
                    default_key="accent_2")
px_ = 0.026
hook_default(poster,
             deco_text("Poster_Braces", "{ }", 0.18, (px_, PO_Y, PO_Z + 0.1), mat("main", 0.6), rot=(R(90), 0, R(90)),
                       depth=0.001),
             box("Poster_Stripe_1", (0.002, PO_W * 0.6, 0.04), (px_, PO_Y, PO_Z - 0.12), mat("accent_1", 0.6), bevel=0),
             box("Poster_Stripe_2", (0.002, PO_W * 0.42, 0.04), (px_, PO_Y - PO_W * 0.08, PO_Z - 0.19),
                 mat("accent_3", 0.6), bevel=0),
             box("Poster_Stripe_3", (0.002, PO_W * 0.5, 0.04), (px_, PO_Y + PO_W * 0.04, PO_Z - 0.26),
                 mat("dark", 0.6), bevel=0))

# Letter board above the cube shelf: oak frame, black grooved felt, white letters (your name + role).
SG_X, SG_Z, SG_W, SG_H = 3.45, 1.96, 0.8, 0.52
felt = fabric("felt", 0.95)
sign = box("Name_Sign", (SG_W, 0.02, SG_H), (SG_X, D - 0.012, SG_Z), felt, bevel=0.002)
hook_link(sign, "website")
for nm, size, loc in [("T", (SG_W + 0.03, 0.03, 0.022), (SG_X, D - 0.015, SG_Z + SG_H / 2 + 0.011)),
                      ("B", (SG_W + 0.03, 0.03, 0.022), (SG_X, D - 0.015, SG_Z - SG_H / 2 - 0.011)),
                      ("L", (0.022, 0.03, SG_H), (SG_X - SG_W / 2 - 0.004, D - 0.015, SG_Z)),
                      ("R", (0.022, 0.03, SG_H), (SG_X + SG_W / 2 + 0.004, D - 0.015, SG_Z))]:
    box(f"Name_Sign_Frame_{nm}", size, loc, oak(0.5), bevel=0.003)
boxes("Name_Sign_Grooves", [((SG_W - 0.01, 0.001, 0.0025), (SG_X, D - 0.0225, SG_Z - SG_H / 2 + 0.015 + k * 0.016))
                            for k in range(int((SG_H - 0.02) / 0.016))], mat("felt_line", 0.9,
                            color=shade(COLORS["felt"], 1.9)))
letters = mat("letters", 0.4, color="#F7F5EF")
hook_text("name", 1, "YOUR NAME", 0.11, (SG_X, D - 0.025, SG_Z + 0.08), material=letters, max_width=SG_W - 0.1,
          depth=0.003)
hook_text("role", 1, "your role", 0.065, (SG_X, D - 0.025, SG_Z - 0.08), material=mat("letters_role", 0.4,
          color="#F2C46B" if THEME != "japandi" else "#E2CDB0"), max_width=SG_W - 0.14, depth=0.003)
deco_text("Name_Sign_Code", "</>", 0.05, (SG_X, D - 0.025, SG_Z - 0.19), letters, depth=0.003)


# =====================================================================
#  LIGHTS, WORLD, CAMERA, RENDER
# =====================================================================
# Daylight: afternoon sun through the window + soft fill from the camera side + desk lamp.
# Night (THEME == "night"): a dim cool moon, much less fill, a brighter lamp and glowing screens.
sun_power, fill_mult, amb = (SUN_STRENGTH, 1.0, 0.35) if not NIGHT else (0.5, 0.22, 0.08)
light("Light_Sun", "SUN", sun_power, kelvin(SUN_WARMTH if not NIGHT else 9000), (-3, wy + 0.9, 4.0),
      aim=(0.2, wy - 0.15, 0.0), size=R(2.5))
light("Light_Fill", "AREA", 230 * (W * D / 16) * fill_mult, kelvin(6000 if not NIGHT else 8000), (W + 3, -3, H + 2.5),
      aim=(W / 2, D / 2, 0.6), size=6)
lamp_slot = SLOTS["lamp"]
light("Light_Lamp", "POINT", LAMP_STRENGTH * (1 if not NIGHT else 2.4), kelvin(LAMP_WARMTH),
      slot_point("lamp", (0, -lamp_slot["kit_size"][1] / 2 + 0.1, 0.42)), size=0.04)
light("Light_Bounce", "AREA", 30 if not NIGHT else 12, kelvin(5000 if not NIGHT else LAMP_WARMTH),
      (W / 2, D / 2, H - 0.1), aim=(W / 2, D / 2, 0), size=2.5)
if NIGHT:                                                           # warm pool on the boards + letter board
    light("Light_Wall_Wash", "AREA", 40, kelvin(LAMP_WARMTH), (2.2, D - 0.9, 2.6), aim=(2.2, D, 1.9), size=1.8)

# World: the camera sees the flat background colour; the room is lit by a soft ambient.
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
bg_amb.inputs["Color"].default_value = (*kelvin(6500 if not NIGHT else 9000), 1)
bg_amb.inputs["Strength"].default_value = amb
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
scene.view_settings.exposure = -0.15 if not NIGHT else 0.0

# Remember the style so add_furniture.py can match colours later.
scene["kit_style"] = STYLE
scene["kit_version"] = KIT_VERSION
scene["kit_palette"] = json.dumps(COLORS)
scene["kit_material_finish"] = json.dumps({"roughness": 0.6, "bevel": 0.004, "saturation": 0.7})
scene["kit_theme"] = THEME
scene["kit_bounds"] = [-T, 0.0, -0.2, W, D + T, H + 0.12]   # used to re-frame the camera for social sizes
scene["kit_furniture_colors"] = json.dumps(["main", "accent_1", "accent_2", "accent_3", "cream", "wood", "plant", "dark"])   # colours add_furniture.py may use


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
