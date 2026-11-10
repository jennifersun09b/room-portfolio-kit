"""
3D ROOM PORTFOLIO KIT  -  Template: DESIGN & ART STUDIO
=======================================================
Builds a real-looking illustrator / designer studio and renders a 1920x1080 image: a slim steel-framed
window with a column radiator, a split-top drafting table with an all-in-one computer and a pen tablet, a
clamp-on spring-arm lamp, a wooden A1 plan chest under a cork moodboard, a pegboard of tools, a pine
shelving unit, a steel stool, a paint trolley and a wooden H-frame easel on a paint-splattered drop cloth.
Every piece is modelled on a real product you can buy or have seen - see REFERENCES below.

HOW TO RUN
  Option A (no Blender UI):   blender -b -P design_studio.py
  Option B (inside Blender):  Scripting tab > Open > design_studio.py > Run Script (then F12 to render)

You only need to edit the SETTINGS block below. Everything under it builds the room.
Output: output/design_studio.png and output/design_studio.blend next to this script.

Your projects appear on: the computer screen (screen_1), the easel canvas (canvas_1), the canvas hanging
by the window (canvas_2) and the three A3 prints pinned to the moodboard (board_1..3).
"""

# REFERENCES  (product names live only here and in research/design_studio.md - never in the scene)
#   workbench Split-top maple drafting table (Hann split-top / Studio Designs Graphix II type), 165x76x92 cm,
#             tilting part 89x76 cm at 16 deg, fixed side widened to 75 cm for the computer
#             https://www.dickblick.com/products/hann-basic-drafting-table/
#             https://joann.com/studio-designs-graphix-ii-pro-line-drafting-desk-white/17008434.html
#   monitor   24-inch all-in-one computer (iMac 24 type) 54.7x46.1 cm, 11.5 mm body, stand 13x14.7 cm
#             https://support.apple.com/en-gb/117733
#   tablet    Medium pen tablet (Wacom Intuos Pro M type) 33.8x21.9x0.8 cm, express keys + touch ring
#             https://www.wexphotovideo.com/wacom-intuos-pro-medium-1616875/
#   keyboard  Slim aluminium keyboard (Magic Keyboard type) 27.9x11.5 cm wedge
#   lamp      Anglepoise Type 75 with desk clamp: 14 cm bell shade, twin arms, 3 springs, ~66 cm reach
#             https://architonic.com/en/product/anglepoise-type-75-with-desk-clamp/1472373
#   cabinet   Wooden A1 plan chest, 6 drawers, 100x72.5x71 cm, label frames and D-handles
#             https://www.shocfurniture.co.uk/?p=292672
#   shelf     IKEA IVAR shelving unit, pine, 89x30x179 cm, shelves 83x30x1.8 cm, steel X-brace
#             https://www.ikea.com/gb/en/p/ivar-shelving-unit-s99572571
#   easel     Beechwood H-frame studio easel (SoHo / Blick light-duty type), base 53x56 cm, 183 cm high
#             https://www.jerrysartarama.com/soho-urban-artist-h-frame-studio-easel-wooden-87223
#   stool     Tolix H65 steel stool, seat 64.5 cm, footprint 40x40 cm, footrest ring
#             https://tolix.com/international/products/tabouret-h65-75-exterieur
#   trolley   IKEA RÅSKOG trolley 35x45x78 cm, 3 trays, castors
#             https://www.ikea.com.tr/en/p90443135
#   pegboard  IKEA SKÅDIS pegboard 76x56 cm with shelf 28x9 cm, container, hooks, clip
#             https://www.ikea.com/ie/en/p/skadis-pegboard-beige-pink-00605995
#   wall_art  Pine-framed cork notice board 120x90 cm with A3 prints, swatch strips, index cards
#             https://backtotheoffice.co.uk/products/bi-office-cork-noticeboard-pine-wood-frame-900x600mm
#   window    Steel window (Crittall W20 type): 32-40 mm frame, ~20 mm glazing bars, casement lever handle
#             https://www.crittall-windows.co.uk/products/w20
#   radiator  4-column cast-iron-style radiator, 60 cm high, 14 cm deep, 16 sections at 62 mm
#             https://www.victorianplumbing.co.uk/keswick-cast-iron-style-traditional-4-column-white-radiator-600-x-636mm
#   plant     IKEA FICUS LYRATA fiddle-leaf fig, 21 cm pot, ~100 cm tall
#             https://www.ikea.com/sg/en/p/ficus-lyrata-potted-plant-fiddle-leaf-fig-40578570
#   rug       Cotton duck painter's drop cloth (9x12 ft, folded to 180x140 cm)
#             https://www.tarpsnow.com/10-oz-painters-drop-cloth-canvas-tarps-0912.html
#   canvases  Stretched canvases 76x61x3.8 cm (30x24 in) with pine stretcher bars
#   armchair  IKEA POÄNG armchair, birch veneer frame + cushion, 68x82x97 cm (decor, not a slot)
#             https://www.ikea.gr/en/products/poang-armchair-frame/20069852
#   tray tbl  IKEA GLADOM tray table, 45 cm diameter x 53 cm, powder-coated steel (decor)
#             https://www.ikea.com/ie/en/p/gladom-tray-table-black-50411990
#   floor     Pine floorboards 18 cm wide, staggered joints; back wall painted brick 215x65 mm

# =====================================================================
#  SETTINGS  -  change these lines, then run the script again
# =====================================================================
ROOM_NAME = "design_studio"         # used for the output file names

ROOM_WIDTH = 4.4                    # metres, left to right
ROOM_DEPTH = 4.0                    # metres, front to back
WALL_HEIGHT = 2.9                   # metres

THEME = "airy"                      # pick one of the colour themes below
THEMES = {                          # any hex colour works; "main" is the room's hero colour
    # "airy" = bright north-window daylight. "studio_night" = same room after dark: the code below
    # switches the sun to cool moonlight and turns up the desk lamp and the monitor glow.
    # Extra keys: cork (moodboard), cloth (drop cloth, canvas), sky (window glass), steel (window frame),
    # vinyl (drafting board cover), brass (handles and label frames).
    # The four paint colours are real artists' pigments (cobalt blue, cadmium red, yellow ochre, viridian),
    # slightly muted like gouache, so the room reads as paint and not as a tech brand's colours.
    "airy": {
        "background": "#E4EAF1", "wall": "#F4F1EC", "wall_trim": "#E3DACB", "floor": "#D7BD96",
        "wood": "#CFAE82", "main": "#3A68A8", "accent_1": "#D25A3F", "accent_2": "#DDA43F",
        "accent_3": "#3F8C7E", "cream": "#FBF9F4", "plant": "#4A8A4E", "dark": "#2A2C31",
        "cork": "#C79A66", "cloth": "#E4D9C4", "sky": "#DCE7F2", "steel": "#34383D", "vinyl": "#DDE6DD",
        "brass": "#B8924F",
    },
    "studio_night": {
        "background": "#1B2032", "wall": "#3A4262", "wall_trim": "#2B3149", "floor": "#8A6E52",
        "wood": "#B39472", "main": "#5E8FD6", "accent_1": "#E9735A", "accent_2": "#EDBA5A",
        "accent_3": "#4FB0A0", "cream": "#F1ECE3", "plant": "#3F8A55", "dark": "#1C1E27",
        "cork": "#A97F52", "cloth": "#CFC5B2", "sky": "#2A3A66", "steel": "#23262D", "vinyl": "#B9C4BC",
        "brass": "#C29A55",
    },
}

SUN_WARMTH = 5600                   # Kelvin of the daylight: 2500 = sunset orange, 6500 = white daylight
SUN_STRENGTH = 5.5                  # how bright the sun patch on the floor is
LAMP_WARMTH = 3000                  # Kelvin of the desk lamp
LAMP_STRENGTH = 14                  # Watts of the desk lamp (night theme uses 4x)
PAINT_SPLATS = 36                   # paint stains, mostly on the drop cloth round the easel (20-50 looks good)
SEED = 7                            # change to shuffle paint splats, shelf supplies and props

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
NIGHT = THEME == "studio_night"

STYLE = "design_studio"
KIT_VERSION = 2
W, D, H = ROOM_WIDTH, ROOM_DEPTH, WALL_HEIGHT
T = 0.15            # wall thickness
FLOOR_Z = 0.03      # top of the floorboards; furniture stands here
R = math.radians
random.seed(SEED)
PAINTS = ["main", "accent_1", "accent_2", "accent_3"]


# --------------------------------------------------------------------- colour helpers
def lin(hex_color):
    """'#RRGGBB' -> linear RGBA, the colour space Blender shaders use."""
    h = hex_color.lstrip("#")
    out = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return (*out, 1.0)


def kelvin(k):
    """Colour temperature -> linear RGB (Tanner Helland approximation)."""
    t = k / 100.0
    r = 255 if t <= 66 else 329.698727446 * ((t - 60) ** -0.1332047592)
    g = 99.4708025861 * math.log(t) - 161.1195681661 if t <= 66 else 288.1221695283 * ((t - 60) ** -0.0755148492)
    b = 255 if t >= 66 else (0 if t <= 19 else 138.5177312231 * math.log(t - 10) - 305.0447927307)
    rgb = [max(0.0, min(255.0, v)) / 255 for v in (r, g, b)]
    return tuple(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb)


def shade(key, f):
    """A darker (f < 1) or lighter (f > 1) version of a COLORS key, as hex."""
    h = COLORS[key].lstrip("#")
    rgb = [int(h[i:i + 2], 16) for i in (0, 2, 4)]
    rgb = [min(255, int(c * f)) if f <= 1 else int(c + (255 - c) * (f - 1)) for c in rgb]
    return "#%02X%02X%02X" % tuple(rgb)


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
    """Box with small rounded edges (real furniture: 2-8 mm). size = (x, y, z) in metres, loc = centre."""
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=Vector(size), verts=bm.verts)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, min(bevel, min(size) * 0.45), coll, parent)


def boxes(name, items, material, bevel=0.0, loc=(0, 0, 0), rot=(0, 0, 0), coll=None, parent=None):
    """Many boxes in ONE object (key caps, floorboards, pegboard slots). items = [(size, centre), ...]."""
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


def rod(name, a, b, r, material, parent=None, segs=12, coll=None):
    """A thin round bar from point a to point b (lamp arms, pipes, pencils, brush handles)."""
    a, b = Vector(a), Vector(b)
    o = cyl(name, r, (b - a).length, (a + b) / 2, material, segs=segs, bevel=0, parent=parent, coll=coll)
    o.rotation_euler = (b - a).to_track_quat("Z", "Y").to_euler()
    return o


def beam(name, a, b, size, material, bevel=0.003, roll=0.0, parent=None, coll=None):
    """A rectangular bar from point a to point b. size = (width, thickness); roll turns it around its length."""
    a, b = Vector(a), Vector(b)
    o = box(name, (size[0], size[1], (b - a).length), (a + b) / 2, material, bevel=bevel, parent=parent, coll=coll)
    m = (b - a).to_track_quat("Z", "Y").to_matrix() @ Matrix.Rotation(roll, 3, "Z")
    o.rotation_euler = m.to_euler()
    return o


def tube(name, pts, r, material, closed=False, segs=10, parent=None, coll=None):
    """A round tube swept along a list of points (trolley handles, springs, cords, mug handles)."""
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


def ring_pts(centre, r, n=20, axis="Z", start=0.0, end=2 * math.pi):
    """Points on a circle (or an arc) around centre, in the plane normal to axis."""
    cx, cy, cz = centre
    out = []
    for k in range(n + 1 if end - start < 2 * math.pi - 1e-6 else n):
        a = start + (end - start) * k / n
        c, s = math.cos(a) * r, math.sin(a) * r
        out.append({"Z": (cx + c, cy + s, cz), "Y": (cx + c, cy, cz + s), "X": (cx, cy + c, cz + s)}[axis])
    return out


def flat(name, pts2d, material, loc=(0, 0, 0), rot=(0, 0, 0), parent=None, coll=None, thick=0.0):
    """A flat shape (a leaf, a palette) from 2D outline points in the XY plane, optionally with thickness."""
    bm = bmesh.new()
    face = bm.faces.new([bm.verts.new((x, y, 0)) for x, y in pts2d])
    if thick:
        ext = bmesh.ops.extrude_face_region(bm, geom=[face])
        bmesh.ops.translate(bm, vec=(0, 0, thick), verts=[v for v in ext["geom"] if isinstance(v, bmesh.types.BMVert)])
        bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, 0, coll, parent)


def lathe(name, profile, material, loc=(0, 0, 0), rot=(0, 0, 0), segs=32, parent=None, coll=None):
    """A round shape spun from a side profile [(radius, height), ...] around local Z (lamp shades)."""
    bm = bmesh.new()
    rings = [[bm.verts.new((r * math.cos(a), r * math.sin(a), z)) for a in (2 * math.pi * k / segs for k in range(segs))]
             for r, z in profile]
    for a, b in zip(rings, rings[1:]):
        for k in range(segs):
            bm.faces.new((a[k], a[(k + 1) % segs], b[(k + 1) % segs], b[k]))
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, 0, coll, parent)


def no_shadow(*objs):
    for o in objs:
        if hasattr(o, "visible_shadow"):
            o.visible_shadow = False
    return objs


def mix_hex(a, b, t):
    """Blend two hex colours (t = 0 gives a, 1 gives b)."""
    ca, cb = [[int(h.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)] for h in (a, b)]
    return "#%02X%02X%02X" % tuple(round(x + (y - x) * t) for x, y in zip(ca, cb))


def blob_pts(r, n=18, rough=0.35):
    """An irregular round outline (a paint stain, not a perfect disc)."""
    k1, k2, p1, p2 = random.randint(2, 4), random.randint(5, 7), random.uniform(0, 6.28), random.uniform(0, 6.28)
    out = []
    for i in range(n):
        a = 2 * math.pi * i / n
        f = 1 + rough * 0.6 * math.sin(k1 * a + p1) + rough * 0.4 * math.sin(k2 * a + p2)
        out.append((math.cos(a) * r * f, math.sin(a) * r * f))
    return out


def splat(name, loc, r, key, parent=None, rot=(0, 0, 0)):
    """A dried paint stain: a flat irregular blob soaked into the cloth (matte, slightly muted),
    with a few flat satellite drops thrown off to one side, like real splatter."""
    m = mat(key + "_stain", 0.55, color=mix_hex(COLORS[key], COLORS["cloth"], 0.22))
    s = flat(name, blob_pts(r), m, loc=loc, rot=rot, parent=parent, thick=0.0006)
    a0 = random.uniform(0, 6.28)
    for k in range(random.randint(1, 4)):                  # drops flung in one direction
        a = a0 + random.uniform(-0.5, 0.5)
        d = r * random.uniform(1.4, 2.8)
        flat(name + "_Drop", blob_pts(r * random.uniform(0.12, 0.28), 10, 0.2), m,
             loc=(loc[0] + math.cos(a) * d, loc[1] + math.sin(a) * d, loc[2]), rot=rot, parent=parent, thick=0.0006)
    return s


def ribbon(name, pts, width, thick, material, side=(1, 0, 0), parent=None, coll=None):
    """A flat strip of bent plywood swept along points (the bent-birch frame of a lounge chair).
    width runs along `side`; thick is the plywood thickness."""
    s = Vector(side).normalized()
    pts = [Vector(p) for p in pts]
    bm = bmesh.new()
    rings = []
    for i, p in enumerate(pts):
        t = (pts[min(i + 1, len(pts) - 1)] - pts[max(i - 1, 0)]).normalized()
        n = s.cross(t).normalized()
        rings.append([bm.verts.new(p + s * sx * width / 2 + n * sn * thick / 2)
                      for sx, sn in ((-1, -1), (1, -1), (1, 1), (-1, 1))])
    for a, b in zip(rings, rings[1:]):
        for k in range(4):
            bm.faces.new((a[k], a[(k + 1) % 4], b[(k + 1) % 4], b[k]))
    bm.faces.new(rings[0][::-1])
    bm.faces.new(rings[-1])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    o = _obj(name, bm)
    _finish(o, material, 0, coll, parent)
    o.data.polygons.foreach_set("use_smooth", [False] * len(o.data.polygons))
    return o


def cactus(name, loc, r, h, parent=None, ribs=9):
    """A ribbed column cactus (golden barrel / cereus type): deep ribs, a domed top and rows of pale spines."""
    green = mat("cactus", 0.55, color=shade("plant", 0.85))
    bm = bmesh.new()
    segs, levels = ribs * 4, 12
    rings = []
    for j in range(levels + 1):
        t = j / levels
        prof = math.sin(math.acos(max(-1.0, min(1.0, (t - 0.55) / 0.45)))) if t > 0.55 else 1.0   # domed top
        prof = max(prof, 0.06) * (0.92 + 0.08 * math.sin(t * math.pi))
        rings.append([bm.verts.new((math.cos(a) * r * prof * (1 + 0.13 * math.cos(ribs * a)),
                                    math.sin(a) * r * prof * (1 + 0.13 * math.cos(ribs * a)), h * t))
                      for a in (2 * math.pi * k / segs for k in range(segs))])
    for a, b in zip(rings, rings[1:]):
        for k in range(segs):
            bm.faces.new((a[k], a[(k + 1) % segs], b[(k + 1) % segs], b[k]))
    bm.faces.new(rings[-1])
    o = _obj(name, bm)
    o.location = loc
    _finish(o, green, 0, None, parent)
    spines = []
    for k in range(ribs):                                       # areoles with spines along each rib edge
        a = 2 * math.pi * k / ribs
        for j in range(2, levels - 2, 2):
            t = j / levels
            prof = math.sin(math.acos((t - 0.55) / 0.45)) if t > 0.55 else 1.0
            rr = r * prof * 1.13 + 0.002
            spines.append(((0.004, 0.004, 0.004), (math.cos(a) * rr, math.sin(a) * rr, h * t)))
    boxes(name + "_Spines", spines, mat("spine", 0.6, color="#EFE6C8"), loc=loc, parent=parent)
    return o


def rag(name, loc, size, material, turn=0.0, parent=None, lift=0.03):
    """A crumpled cotton rag lying on a surface: an irregular sheet with lumpy folds."""
    sx, sy = size
    nx, ny = 10, 8
    bm = bmesh.new()
    p1, p2 = random.uniform(0, 6), random.uniform(0, 6)
    grid = []
    for j in range(ny + 1):
        row = []
        for i in range(nx + 1):
            u, v = i / nx - 0.5, j / ny - 0.5
            edge = 1 - max(abs(u), abs(v)) * 2                          # 0 at the edge, 1 in the middle
            z = lift * (0.15 + 0.85 * edge) * (0.55 + 0.45 * math.sin(u * 9 + p1) * math.cos(v * 7 + p2))
            wob = 0.06 * math.sin(v * 8 + p1) * (1 - edge)
            row.append(bm.verts.new(((u + wob) * sx, (v + 0.05 * math.sin(u * 7 + p2)) * sy, max(0.001, z))))
        grid.append(row)
    for j in range(ny):
        for i in range(nx):
            bm.faces.new((grid[j][i], grid[j][i + 1], grid[j + 1][i + 1], grid[j + 1][i]))
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, (0, 0, R(turn))
    sol = o.modifiers.new("Thickness", "SOLIDIFY")
    sol.thickness = 0.002
    return _finish(o, material, 0, None, parent)


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
#   picture hooks: "screen" (glows), "frame", "poster", "canvas", "board", "logo"  -> project images (in order)
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


def default_art(hook, w, h, loc, rot, parent, style, name=None, glow=0.0):
    """Default artwork on a picture (hidden once a real image is applied to the hook). Each style is a kind
    of work you really see pinned up in an illustrator's studio, painted flat like gouache or screen print:
      landscape  - a landscape painting: layered hills, cypress trees, a ploughed field and a low sun
      still_life - a potted plant in front of an arch (a classic illustration print)
      poster     - a Swiss-style poster: two overlapping circles and lines of type
      pattern    - a surface-pattern repeat of leaves and dots
      thumbs     - a sheet of six thumbnail sketches
    glow > 0 makes the paint self-lit, for artwork shown on a screen."""
    C = COLORS
    rm = Euler(rot).to_matrix()
    face = (rm @ Matrix.Rotation(R(90), 3, "X")).to_euler()       # flat() draws in XY; stand it in the picture
    parts = []

    def shape(pts, color, layer=1):
        """A flat painted shape. pts are (across, up) in metres from the picture centre; layers stack forward."""
        pts = [(max(-w / 2, min(w / 2, x)), max(-h / 2, min(h / 2, z))) for x, z in pts]    # never past the edge
        if sum(x0 * z1 - x1 * z0 for (x0, z0), (x1, z1) in zip(pts, pts[1:] + pts[:1])) < 0:
            pts = pts[::-1]                                             # anticlockwise = faces the viewer
        parts.append(flat(f"{name or hook.name}_Art", pts, mat("art", 0.8, emit=glow, color=color), parent=parent, rot=face,
                          loc=Vector(loc) + rm @ Vector((0, -0.0004 * layer, 0))))

    def rect(x0, z0, x1, z1, color, layer=1):
        shape([(x0, z0), (x1, z0), (x1, z1), (x0, z1)], color, layer)

    def disc(cx, cz, rx, rz, color, layer=1, n=28):
        shape([(cx + rx * math.cos(2 * math.pi * k / n), cz + rz * math.sin(2 * math.pi * k / n)) for k in range(n)],
              color, layer)

    def leaf2d(cx, cz, length, width, angle, color, layer):
        a, n = R(angle), 10
        side = [(t * length, width * math.sin(math.pi * t) * (1 - 0.3 * t)) for t in (k / n for k in range(n + 1))]
        pts = side + [(x, -y) for x, y in side[-2:0:-1]]
        shape([(cx + x * math.cos(a) - y * math.sin(a), cz + x * math.sin(a) + y * math.cos(a)) for x, y in pts],
              color, layer)

    def hill_z(k, top, amp, waves, phase, n=24):
        return top + amp * math.sin(waves * math.pi * k / n + phase) + amp * 0.35 * math.sin(k * 1.3 + phase)

    def hills(top, amp, waves, phase, color, layer):
        pts = [(-w / 2 + w * k / 24, hill_z(k, top, amp, waves, phase)) for k in range(25)]
        shape(pts + [(w / 2, -h / 2), (-w / 2, -h / 2)], color, layer)

    if style == "landscape":
        rect(-w / 2, -h * 0.1, w / 2, h * 0.16, mix_hex(C["sky"], C["accent_2"], 0.35), 1)        # warm horizon
        disc(w * 0.23, h * 0.14, w * 0.055, w * 0.055, mix_hex(C["accent_2"], C["cream"], 0.3), 2)
        hills(h * 0.0, h * 0.05, 2.2, 0.5, mix_hex(C["main"], C["sky"], 0.45), 3)                  # far hills
        hills(-h * 0.15, h * 0.06, 1.6, 2.0, mix_hex(C["accent_3"], C["plant"], 0.4), 4)           # mid hills
        field = mix_hex(C["accent_2"], C["accent_1"], 0.2)
        hills(-h * 0.3, h * 0.035, 1.1, 4.0, field, 5)                                             # near field
        for k in range(5):                                                                         # furrows
            z = -h * (0.36 + 0.03 * k)
            rect(-w / 2, z, w / 2, z + 0.004 + 0.0015 * k, shade("accent_2", 0.8), 6)
        for k, tall in ((5, 0.17), (6, 0.12), (14, 0.15), (15, 0.1)):                             # cypress trees
            base = hill_z(k, -h * 0.15, h * 0.06, 1.6, 2.0) - h * 0.025                            # on the mid hill
            disc(-w / 2 + w * k / 24, base + h * tall / 2, w * 0.017, h * tall / 2, shade("accent_3", 0.5), 6, 16)
    elif style == "still_life":
        shape([(-w * 0.3, -h * 0.3), (w * 0.3, -h * 0.3)] + [(math.cos(a) * w * 0.3, h * 0.12 + math.sin(a) * w * 0.3)
              for a in (math.pi * k / 16 for k in range(17))], mix_hex(C["accent_1"], C["cream"], 0.55), 1)  # arch
        rect(-w / 2, -h / 2, w / 2, -h * 0.28, mix_hex(C["wood"], C["accent_1"], 0.25), 2)         # table top
        shape([(-w * 0.1, -h * 0.4), (w * 0.1, -h * 0.4), (w * 0.13, -h * 0.17), (-w * 0.13, -h * 0.17)],
              C["accent_1"], 3)                                                                     # pot
        rect(-w * 0.15, -h * 0.17, w * 0.15, -h * 0.13, shade("accent_1", 0.85), 4)                 # pot rim
        greens = (C["plant"], shade("plant", 0.72), C["accent_3"])
        for k, (ang, ln) in enumerate(((95, 0.36), (60, 0.3), (125, 0.32), (40, 0.22), (145, 0.24), (78, 0.27),
                                       (110, 0.26))):
            leaf2d(0, -h * 0.13, h * ln, h * 0.06, ang, greens[k % 3], 5 + k % 3)
    elif style == "poster":
        disc(w * 0.16, h * 0.12, h * 0.36, h * 0.36, C["accent_1"], 1, 40)
        disc(-w * 0.06, -h * 0.02, h * 0.22, h * 0.22, C["main"], 2, 36)
        z = -h * 0.24
        for ln, th in ((0.55, 0.06), (0.4, 0.06), (0.3, 0.016), (0.34, 0.016), (0.22, 0.016)):  # lines of type
            rect(-w * 0.44, z - th * h, -w * 0.44 + w * ln, z, C["dark"], 3)
            z -= th * h + h * 0.025
        rect(w * 0.3, h * 0.38, w * 0.44, h * 0.42, C["dark"], 3)
    elif style == "pattern":
        rect(-w / 2, -h / 2, w / 2, h / 2, mix_hex(C["accent_3"], C["cream"], 0.72), 1)
        for i in range(7):
            for j in range(5):
                x, z = -w / 2 + w * (i + 0.5 + 0.5 * (j % 2)) / 7, -h / 2 + h * (j + 0.5) / 5
                if (i + j) % 2:
                    leaf2d(x - w * 0.03, z - h * 0.03, h * 0.16, h * 0.04, 40 + 50 * (j % 2), C["accent_3"], 2)
                else:
                    disc(x, z, h * 0.025, h * 0.025, C["accent_2"], 2, 12)
    elif style == "thumbs":
        for i in range(3):
            for j in range(2):
                cx, cz = -w / 3 + i * w / 3, h * 0.22 - j * h * 0.44
                fw, fh = w * 0.27, h * 0.33
                rect(cx - fw / 2, cz - fh / 2, cx + fw / 2, cz + fh / 2, mix_hex(C["sky"], C["cream"], 0.3), 1)
                top = cz - fh * (0.1 - 0.12 * ((i + j) % 2))
                shape([(cx - fw / 2, cz - fh / 2), (cx + fw / 2, cz - fh / 2), (cx + fw / 2, top),
                       (cx + fw * 0.1, top + fh * 0.18), (cx - fw / 2, top - fh * 0.05)],
                      (C["accent_3"], C["main"], C["accent_2"])[(i + 2 * j) % 3], 2)
                for x0, z0, x1, z1 in ((-1, -1, 1, -0.93), (-1, 0.93, 1, 1), (-1, -1, -0.96, 1), (0.96, -1, 1, 1)):
                    rect(cx + x0 * fw / 2, cz + z0 * fh / 2, cx + x1 * fw / 2, cz + z1 * fh / 2, C["dark"], 3)
    if hook is not None:
        hook_default(hook, *parts)
    return parts


# --------------------------------------------------------------------- shared real-world materials
def wood(key="wood", rough=0.45, along="X", color=None):
    """Solid wood / veneer (maple, beech, pine) in a palette colour, with real grain."""
    return surface(mat(key, rough, color=color), "wood", along=along)


def powder(key, rough=0.45, along="X"):
    """Powder-coated or painted steel (window, trolley, stool, brackets)."""
    return surface(mat(key, rough, metal=0.35), "brushed", along=along)


def ceramic(key, rough=0.2, color=None):
    return surface(mat(key, rough, color=color), "ceramic")


MAPLE = wood("wood", 0.42)                                                # drafting table, easel
MAPLE_V = wood("wood", 0.43, along="Z")                                   # same wood, grain running up
PINE = wood("pine", 0.5, color=shade("wood", 1.18))                       # IVAR, stretchers, frames
PINE_V = wood("pine", 0.51, along="Z", color=shade("wood", 1.18))
PAPER = surface(mat("paper", 0.85, color="#F5F1E8"), "paper")
KRAFT = surface(mat("kraft", 0.8, color="#B98E5E"), "paper")
STEEL = surface(mat("metal", 0.3, metal=0.85, color="#B9BDC2"), "brushed")
BRASS = surface(mat("brass", 0.3, metal=0.9), "brushed")
PLASTIC = mat("dark", 0.5)
RUBBER = mat("rubber", 0.85, color=shade("dark", 0.7))
GRAPHITE = mat("graphite", 0.6, color="#5B5E66")
TERRACOTTA = ceramic("terracotta", 0.7, color="#C46A45")
GLASS = mat("glass", 0.05, color="#EEF4F6")
# Real clear glass (jam jars, ink bottles): light passes through, so the paint and water inside show.
_g = _principled(GLASS)
_set(_g, ["Transmission Weight", "Transmission"], 1.0)
_set(_g, ["IOR"], 1.45)
for _attr in ("use_raytrace_refraction", "use_screen_refraction"):
    if hasattr(GLASS, _attr):
        setattr(GLASS, _attr, True)


def tape_m():
    """Masking tape (cream crepe paper)."""
    return mat("tape", 0.8, color="#EFE3B8")


def mug(name, loc, material, r=0.04, h=0.095, turn=0.0, parent=None, coffee=True):
    """A ceramic mug with a real loop handle."""
    x, y, z = loc
    cyl(name, r, h, (x, y, z + h / 2), material, segs=28, parent=parent)
    a = R(turn)
    hx, hy = x + math.cos(a) * (r + 0.012), y + math.sin(a) * (r + 0.012)
    pts = [(hx + math.cos(a) * 0.012 * math.sin(t), hy + math.sin(a) * 0.012 * math.sin(t),
            z + h * 0.5 + math.cos(t) * h * 0.3) for t in (k * math.pi / 10 for k in range(11))]
    tube(name + "_Handle", pts, 0.0055, material, parent=parent)
    if coffee:
        cyl(name + "_Coffee", r - 0.004, 0.003, (x, y, z + h - 0.012), mat("coffee", 0.15, color="#4A3124"),
            bevel=0, parent=parent)


def paint_tube(name, loc, key, turn=0.0, length=0.11, parent=None):
    """An artist's paint tube lying flat: round body, crimped flat end, black screw cap."""
    a = R(turn)
    d = Vector((math.cos(a), math.sin(a), 0))
    p = Vector(loc)
    body = cyl(name, 0.013, length * 0.72, p, mat("tube_alu", 0.35, metal=0.7, color="#E9E9E6"), r2=0.011, segs=16,
               bevel=0, parent=parent)
    body.rotation_euler = d.to_track_quat("Z", "Y").to_euler()
    band = cyl(name + "_Label", 0.0135, length * 0.36, p - d * 0.006, mat(key, 0.5), r2=0.0125, segs=16, bevel=0,
               parent=parent)
    band.rotation_euler = body.rotation_euler
    crimp = box(name + "_Crimp", (0.026, 0.004, length * 0.16), p - d * length * 0.42, mat("tube_alu", 0.35, metal=0.7,
                color="#E9E9E6"), bevel=0.001, parent=parent)
    crimp.rotation_euler = body.rotation_euler
    cap = cyl(name + "_Cap", 0.008, 0.016, p + d * length * 0.44, PLASTIC, segs=12, bevel=0.002, parent=parent)
    cap.rotation_euler = body.rotation_euler


def brush(name, a, b, key, parent=None, r=0.0035):
    """A paintbrush from handle end a to bristle tip b: wooden handle, metal ferrule, coloured tip."""
    a, b = Vector(a), Vector(b)
    v = b - a
    rod(name, a, a + v * 0.72, r, mat("brush_handle", 0.4, color="#B4373A" if key == "accent_1" else "#2E2A26"),
        parent=parent, segs=8)
    rod(name + "_Ferrule", a + v * 0.72, a + v * 0.88, r * 1.15, STEEL, parent=parent, segs=8)
    rod(name + "_Tip", a + v * 0.88, b, r * 1.1, mat(key, 0.6), parent=parent, segs=8)


def pencil(name, a, b, parent=None, key="accent_2"):
    """A hexagonal pencil with a sharpened tip."""
    a, b = Vector(a), Vector(b)
    v = b - a
    rod(name, a, a + v * 0.9, 0.0035, mat(key, 0.5), parent=parent, segs=6)
    tip = cyl(name + "_Tip", 0.0035, v.length * 0.1, a + v * 0.95, mat("pine_raw", 0.7, color="#E2C49A"), r2=0.0006,
              segs=6, bevel=0, parent=parent)
    tip.rotation_euler = v.to_track_quat("Z", "Y").to_euler()


# =====================================================================
#  ROOM SHELL
# =====================================================================
# Floor: a base slab plus 18 cm pine floorboards running front to back with staggered end joints.
box("Floor_Base", (W + T, D + T, 0.2), ((W - T) / 2, (D + T) / 2, -0.1), mat("wall_trim", 0.7), bevel=0.01)
board_mats = [wood("floor", 0.5, along="Y", color=c) for c in (shade("floor", 0.95), COLORS["floor"],
                                                                 shade("floor", 1.05))]
BOARD = 0.18
for i in range(int(W / BOARD) + 1):
    x0 = i * BOARD
    bw = min(BOARD, W - x0)
    if bw < 0.03:
        break
    y = -random.uniform(0.2, 1.8)
    while y < D:
        length = random.uniform(1.2, 2.6)
        y0, y1 = max(y, 0.0), min(y + length, D)
        y += length
        if y1 - y0 < 0.05:                     # a board that would end before the front edge: skip it
            continue
        box(f"Floor_Board_{i}", (bw - 0.003, y1 - y0 - 0.003, FLOOR_Z), (x0 + bw / 2, (y0 + y1) / 2, FLOOR_Z / 2),
            board_mats[random.randrange(3)], bevel=0.002)

# Walls: painted brick at the back, plaster on the window wall.
WIN_Y = (1.25, 3.15)                # steel window opening, front to back
WIN_Z = (0.9, 2.55)                 # sill at 0.9 m (real sill height 0.8-0.9 m)
wy, wz = sum(WIN_Y) / 2, sum(WIN_Z) / 2
ww, wh = WIN_Y[1] - WIN_Y[0], WIN_Z[1] - WIN_Z[0]
left = box("Wall_Left", (T, D + T, H), (-T / 2, (D + T) / 2, H / 2), surface(mat("wall", 0.85), "plaster"), bevel=0.0)
cutter = box("Window_Cutter", (T * 3, ww, wh), (-T / 2, wy, wz), mat("wall"), bevel=0.0)
cutter.hide_render = cutter.hide_viewport = True
boolean = left.modifiers.new("Window", "BOOLEAN")
boolean.operation, boolean.object = "DIFFERENCE", cutter
bev = left.modifiers.new("Bevel", "BEVEL")
bev.width, bev.segments, bev.limit_method = 0.006, 2, "ANGLE"
box("Wall_Back", (W + T, T, H), ((W - T) / 2, D + T / 2, H / 2), surface(mat("wall", 0.86), "brick", along="X"),
    bevel=0.004)

# Wall caps (the cut-away edge of the walls) and 15 cm skirting boards with a rounded top.
TRIM = mat("wall_trim", 0.55)
box("Trim_Top_Back", (W + T + 0.02, T + 0.02, 0.06), ((W - T) / 2, D + T / 2, H + 0.03), TRIM, bevel=0.006)
box("Trim_Top_Left", (T + 0.02, D + T + 0.02, 0.06), (-T / 2, (D + T) / 2, H + 0.03), TRIM, bevel=0.006)
box("Skirting_Back", (W, 0.018, 0.14), (W / 2, D - 0.009, FLOOR_Z + 0.07), TRIM, bevel=0.003)
cyl("Skirting_Back_Bead", 0.009, W, (W / 2, D - 0.012, FLOOR_Z + 0.14), TRIM, segs=12, rot=(0, R(90), 0), bevel=0)
box("Skirting_Left", (0.018, D, 0.14), (0.009, D / 2, FLOOR_Z + 0.07), TRIM, bevel=0.003)
cyl("Skirting_Left_Bead", 0.009, D, (0.012, D / 2, FLOOR_Z + 0.14), TRIM, segs=12, rot=(R(90), 0, 0), bevel=0)

# Steel window: slim dark frame near the outside face, 6 x 4 small panes, heavier mullions and transom,
# an opening middle casement with a lever handle, a deep plaster reveal and a timber window board.
STEEL_WIN = powder("steel", 0.42, along="Z")
FX = -0.11                                   # x of the frame (the reveal in front of it is 11 cm deep)
bars = []
for z in (WIN_Z[0] + 0.02, WIN_Z[1] - 0.02):                                 # outer frame
    bars.append(((0.035, ww, 0.04), (FX, wy, z)))
for y in (WIN_Y[0] + 0.02, WIN_Y[1] - 0.02):
    bars.append(((0.035, 0.04, wh), (FX, y, wz)))
TRANSOM_Z = WIN_Z[0] + wh * 0.76
bars.append(((0.035, ww, 0.045), (FX, wy, TRANSOM_Z)))                        # transom
for k in range(1, 6):                                                        # mullions (k = 2, 4) and bars
    y = WIN_Y[0] + ww * k / 6
    bars.append(((0.03 if k % 2 else 0.035, 0.02 if k % 2 else 0.045, wh), (FX, y, wz)))
for k in (1, 2):                                                             # glazing bars below the transom
    bars.append(((0.03, ww, 0.02), (FX, wy, WIN_Z[0] + (TRANSOM_Z - WIN_Z[0]) * k / 3)))
cy0, cy1 = WIN_Y[0] + ww * 2 / 6, WIN_Y[0] + ww * 4 / 6                      # opening casement outline
for z in (WIN_Z[0] + 0.045, TRANSOM_Z - 0.035):
    bars.append(((0.012, cy1 - cy0 - 0.03, 0.026), (FX + 0.022, (cy0 + cy1) / 2, z)))
for y in (cy0 + 0.028, cy1 - 0.028):
    bars.append(((0.012, 0.026, TRANSOM_Z - WIN_Z[0] - 0.08), (FX + 0.022, y, (WIN_Z[0] + TRANSOM_Z) / 2)))
boxes("Window_Steel", bars, STEEL_WIN, bevel=0.002)
hz = WIN_Z[0] + (TRANSOM_Z - WIN_Z[0]) * 0.5
box("Window_Handle_Boss", (0.012, 0.03, 0.05), (FX + 0.034, cy0 + 0.028, hz), STEEL_WIN, bevel=0.003)
beam("Window_Handle", (FX + 0.045, cy0 + 0.028, hz + 0.01), (FX + 0.05, cy0 + 0.03, hz - 0.11), (0.014, 0.008),
     STEEL_WIN, bevel=0.003)
rod("Window_Stay", (FX + 0.03, cy1 - 0.03, WIN_Z[0] + 0.05), (FX + 0.03, cy1 - 0.24, WIN_Z[0] + 0.05), 0.005, STEEL_WIN)
glass = box("Window_Glass", (0.006, ww, wh), (FX - 0.004, wy, wz), mat("sky", 0.4, emit=0.25 if NIGHT else 0.7),
            bevel=0)
no_shadow(glass)
box("Window_Board", (0.16, ww + 0.1, 0.025), (FX + 0.08 - 0.01, wy, WIN_Z[0] - 0.0125), wood("wood", 0.5, along="Y"),
    bevel=0.004)
# Window board props: a terracotta pot with a small cactus and a glass jar of brushes.
cyl("Sill_Pot", 0.055, 0.09, (-0.03, WIN_Y[1] - 0.22, WIN_Z[0] + 0.045), TERRACOTTA, r2=0.065, segs=24)
cyl("Sill_Pot_Rim", 0.068, 0.018, (-0.03, WIN_Y[1] - 0.22, WIN_Z[0] + 0.083), TERRACOTTA, segs=24)
cyl("Sill_Soil", 0.058, 0.004, (-0.03, WIN_Y[1] - 0.22, WIN_Z[0] + 0.091), mat("soil", 0.95, color="#3B2A20"))
cactus("Sill_Cactus", (-0.03, WIN_Y[1] - 0.22, WIN_Z[0] + 0.088), 0.038, 0.13)
cyl("Sill_Jar", 0.04, 0.12, (-0.03, WIN_Y[0] + 0.25, WIN_Z[0] + 0.06), GLASS, segs=24)
for k in range(4):
    a = k * 1.6
    brush(f"Sill_Brush_{k}", (-0.03 + math.cos(a) * 0.012, WIN_Y[0] + 0.25 + math.sin(a) * 0.012, WIN_Z[0] + 0.01),
          (-0.03 + math.cos(a) * 0.035, WIN_Y[0] + 0.25 + math.sin(a) * 0.03, WIN_Z[0] + 0.25 + 0.02 * k), PAINTS[k])

# 4-column cast-iron-style radiator under the window: 16 sections at 62 mm, 60 cm high, valves and pipes.
RAD_Y0, RAD_N, RAD_P = wy - 16 * 0.062 / 2, 16, 0.062
RAD_Z0, RAD_H = FLOOR_Z + 0.1, 0.6
cols = []
for s in range(RAD_N):
    y = RAD_Y0 + RAD_P * (s + 0.5)
    for cx in (0.06, 0.094, 0.128, 0.162):                    # four round-edged tubes per section
        cols.append(((0.026, 0.03, RAD_H - 0.08), (cx, y, RAD_Z0 + RAD_H / 2)))
    for z in (RAD_Z0 + 0.03, RAD_Z0 + RAD_H - 0.03):           # hubs: sections screw together here
        cols.append(((0.13, RAD_P - 0.003, 0.055), (0.111, y, z)))
RAD_M = powder("cream", 0.4, along="Z")
boxes("Radiator", cols, RAD_M, bevel=0.009)
for y in (RAD_Y0 + 0.08, RAD_Y0 + RAD_N * RAD_P - 0.08):
    box("Radiator_Foot", (0.15, 0.05, 0.1), (0.111, y, FLOOR_Z + 0.05), RAD_M, bevel=0.006)
for k, y in enumerate((RAD_Y0 - 0.03, RAD_Y0 + RAD_N * RAD_P + 0.03)):
    cyl(f"Radiator_Valve_{k}", 0.016, 0.06, (0.111, y, RAD_Z0 + 0.03), BRASS, rot=(R(90), 0, 0), segs=16)
    rod(f"Radiator_Pipe_{k}", (0.111, y + (-0.02 if k == 0 else 0.02), RAD_Z0 + 0.03),
        (0.111, y + (-0.02 if k == 0 else 0.02), FLOOR_Z - 0.01), 0.011, RAD_M)
cyl("Radiator_TRV", 0.024, 0.07, (0.111, RAD_Y0 - 0.05, RAD_Z0 + 0.09), mat("cream", 0.4), segs=20)


# =====================================================================
#  FURNITURE SLOTS  (same names in every template)
#  size = (width, depth, height); front of the furniture faces local -Y
# =====================================================================
TABLE_H = 0.92                      # drafting height, works with a 65 cm stool
TABLE_W, TABLE_D = 1.65, 0.76
TABLE_X, TABLE_Y = 3.275, D - 0.4   # against the back wall
WING_X = 0.075                      # local x where the tilting board ends and the fixed side starts
slot("workbench",  (TABLE_W, TABLE_D, TABLE_H), (TABLE_X, TABLE_Y), shape="table")
slot("monitor",    (0.56, 0.18, 0.47),    (TABLE_X + 0.535, TABLE_Y + 0.27), z=FLOOR_Z + TABLE_H, kind="surface",
     shape="monitor")
slot("lamp",       (0.16, 0.16, 0.62),    (TABLE_X + 0.165, TABLE_Y + 0.29), z=FLOOR_Z + TABLE_H, kind="surface",
     shape="lamp")
slot("stool",      (0.4, 0.4, 0.65),      (TABLE_X - 0.375, 2.86), shape="stool")
slot("easel",      (0.56, 0.56, 1.85),    (2.1, 1.65), turn=40, shape="box")
slot("rug",        (1.8, 1.4, 0.02),      (1.85, 1.6), turn=6, kind="rug", shape="rug")
slot("cabinet",    (1.0, 0.725, 0.71),    (1.3, D - 0.3725 - 0.01), shape="cabinet")
slot("wall_art",   (1.2, 0.04, 0.9),      (1.3, D - 0.02), z=1.12, kind="wall", shape="frame")
slot("shelf",      (0.89, 0.3, 1.79),     (0.165, 0.62), turn=90, shape="shelf")
slot("plant",      (0.5, 0.5, 1.2),       (0.34, 3.62), shape="plant")


# =====================================================================
#  PLACEHOLDER FURNITURE  (replaced when you add your own with add_furniture.py)
# =====================================================================
def build_workbench():
    """Split-top maple drafting table: end frames with sledge feet, a tilting board with a vinyl cover,
    pencil ledge, tilt brackets and a parallel rule, and a fixed side with a drawer for the computer."""
    root, w, d, h = furniture_root("workbench")
    TOP = 0.025
    rail_z = h - TOP - 0.035
    for sx in (-1, 1):                                                       # end frames
        x = sx * (w / 2 - 0.035)
        for sy in (-1, 1):
            box("Drafting_Leg", (0.045, 0.045, h - TOP - 0.05), (x, sy * (d / 2 - 0.06), 0.05 + (h - TOP - 0.05) / 2),
                MAPLE_V, parent=root)
            cyl("Drafting_Glide", 0.014, 0.01, (x, sy * (d / 2 - 0.04), 0.005), RUBBER, segs=12, parent=root)
        box("Drafting_Foot", (0.05, d - 0.04, 0.045), (x, 0, 0.0325), MAPLE, bevel=0.005, parent=root)
        box("Drafting_EndRail", (0.028, d - 0.16, 0.07), (x, 0, rail_z), MAPLE, parent=root)
    for sy in (-1, 1):                                                       # aprons
        box("Drafting_Apron", (w - 0.12, 0.022, 0.07), (0, sy * (d / 2 - 0.06), rail_z), MAPLE, parent=root)
    box("Drafting_Divider", (0.028, d - 0.16, 0.07), (WING_X, 0, rail_z), MAPLE, parent=root)
    box("Drafting_Footrest", (w - 0.11, 0.035, 0.035), (0, -(d / 2 - 0.06), 0.24), MAPLE, parent=root)
    box("Drafting_Stretcher", (w - 0.11, 0.03, 0.06), (0, d / 2 - 0.06, 0.14), MAPLE, parent=root)

    # fixed side: 25 mm top with a shallow drawer under it
    wing_w = w / 2 - WING_X
    wing_cx = WING_X + wing_w / 2
    box("Drafting_FixedTop", (wing_w, d, TOP), (wing_cx, 0, h - TOP / 2), MAPLE, parent=root)
    box("Drafting_DrawerGap", (0.47, 0.004, 0.058), (wing_cx, -(d / 2 - 0.06) - 0.012, rail_z),
        mat("shadow", 0.9, color=shade("dark", 0.6)), bevel=0, parent=root)
    box("Drafting_Drawer", (0.462, 0.014, 0.052), (wing_cx, -(d / 2 - 0.06) - 0.019, rail_z), MAPLE, parent=root)
    ball("Drafting_DrawerKnob", 0.011, (wing_cx, -(d / 2 - 0.06) - 0.031, rail_z), BRASS, parent=root)

    # tilting board, hinged at its front edge and propped at 16 degrees
    tilt = R(16)
    bw = WING_X + w / 2 - 0.012
    bx = -w / 2 + bw / 2
    hinge = Vector((bx, -d / 2, h - TOP))
    rm = Matrix.Rotation(tilt, 3, "X")

    def on_board(u, v, up=0.0):
        return hinge + rm @ Vector((u, v, TOP + up))
    box("Drafting_Board", (bw, d, TOP), hinge + rm @ Vector((0, d / 2, TOP / 2)), MAPLE, rot=(tilt, 0, 0), parent=root)
    box("Drafting_BoardCover", (bw - 0.02, d - 0.05, 0.0015), on_board(0, d / 2 + 0.015, 0.0008),
        mat("vinyl", 0.55), bevel=0, rot=(tilt, 0, 0), parent=root)
    box("Drafting_Ledge", (bw, 0.03, 0.022), on_board(0, 0.015, 0.011), MAPLE, rot=(tilt, 0, 0), parent=root)
    for sx in (-1, 1):                                                       # slotted tilt brackets + knobs
        x = bx + sx * (bw / 2 - 0.05)
        top = on_board(sx * (bw / 2 - 0.05), d - 0.1, -TOP)
        foot = Vector((x, d / 2 - 0.09, rail_z + 0.035))
        beam("Drafting_Bracket", foot, top, (0.006, 0.03), powder("dark", 0.45), roll=R(90), parent=root)
        cyl("Drafting_TiltKnob", 0.017, 0.02, foot.lerp(top, 0.45) + Vector((sx * 0.015, 0, 0)), PLASTIC,
            rot=(0, R(90), 0), segs=16, parent=root)
    # A2 drawing held with masking tape, and a pencil sketch on it
    pw, ph = 0.594, 0.42
    pv = 0.36
    box("Drafting_Paper", (pw, ph, 0.0008), on_board(-0.02, pv, 0.002), PAPER, bevel=0, rot=(tilt, 0, 0), parent=root)
    tape = tape_m()
    for cx in (-1, 1):
        for cz in (-1, 1):
            o = box("Drafting_Tape", (0.055, 0.02, 0.0006), on_board(-0.02 + cx * pw / 2, pv + cz * ph / 2, 0.0026),
                    tape, bevel=0, parent=root)
            o.rotation_euler = (rm @ Matrix.Rotation(R(45 * cx * cz), 3, "Z")).to_euler()
    for k, (u, v, sw, sh) in enumerate(((-0.17, 0.43, 0.16, 0.2), (0.0, 0.43, 0.12, 0.2), (0.14, 0.43, 0.12, 0.2))):
        for du, dv, lw, lh in ((0, sh / 2, sw, 0.002), (0, -sh / 2, sw, 0.002), (-sw / 2, 0, 0.002, sh),
                               (sw / 2, 0, 0.002, sh)):
            box("Drafting_Sketch", (lw, lh, 0.0004), on_board(u + du, v + dv, 0.003), GRAPHITE, bevel=0,
                rot=(tilt, 0, 0), parent=root)
        box("Drafting_Wash", (sw * 0.8, sh * 0.35, 0.0004), on_board(u, v + sh * 0.18, 0.0031),
            mat(PAINTS[k + 1], 0.7, color=shade(PAINTS[k + 1], 1.35)), bevel=0, rot=(tilt, 0, 0), parent=root)
    # parallel rule running on cords down both sides of the board
    box("Drafting_ParallelRule", (bw - 0.05, 0.045, 0.012), on_board(0, 0.13, 0.007), STEEL, bevel=0.002,
        rot=(tilt, 0, 0), parent=root)
    box("Drafting_RuleEdge", (bw - 0.05, 0.012, 0.004), on_board(0, 0.1, 0.003), GLASS, bevel=0, rot=(tilt, 0, 0),
        parent=root)
    for sx in (-1, 1):
        rod("Drafting_Cord", on_board(sx * (bw / 2 - 0.018), 0.03, 0.004), on_board(sx * (bw / 2 - 0.018), d - 0.03, 0.004),
            0.0012, PLASTIC, parent=root, segs=6)
        cyl("Drafting_Pulley", 0.012, 0.008, on_board(sx * (bw / 2 - 0.018), d - 0.03, 0.004), STEEL,
            rot=(tilt, 0, 0), segs=16, parent=root)
    for k in range(3):                                                       # pencils + eraser on the ledge
        pencil("Drafting_Pencil", on_board(-0.32 + k * 0.05, 0.028, 0.025), on_board(-0.15 + k * 0.05, 0.03, 0.025),
               parent=root, key=("accent_2", "dark", "accent_3")[k])
    box("Drafting_Eraser", (0.05, 0.02, 0.012), on_board(0.2, 0.03, 0.028), mat("eraser", 0.7, color="#F2EEE6"),
        bevel=0.002, rot=(tilt, 0, 0), parent=root)

    # fixed side: pen tablet, keyboard and a mug
    top = h
    tab = Vector((WING_X + 0.2, -0.17, top))
    tab_turn = R(-6)
    trm = Matrix.Rotation(tab_turn, 3, "Z")

    def on_tab(x, y, z):
        return tab + trm @ Vector((x, y, z))
    box("Tablet_Body", (0.338, 0.219, 0.008), on_tab(0, 0, 0.004), mat("dark", 0.35), bevel=0.003,
        rot=(0, 0, tab_turn), parent=root)
    box("Tablet_Area", (0.224, 0.148, 0.0006), on_tab(0.04, 0, 0.0082), mat("tablet_area", 0.55, color="#3A3C42"),
        bevel=0, rot=(0, 0, tab_turn), parent=root)
    marks = []
    for cx in (-1, 1):
        for cy in (-1, 1):
            marks.append(((0.012, 0.0015, 0.0004), (0.04 + cx * 0.106, cy * 0.074, 0.0086)))
            marks.append(((0.0015, 0.012, 0.0004), (0.04 + cx * 0.112, cy * 0.068, 0.0086)))
    for k in range(8):
        marks.append(((0.018, 0.012, 0.002), (-0.142, 0.07 - k * 0.02 - (0.025 if k > 3 else 0), 0.009)))
    boxes("Tablet_Keys", marks, mat("tablet_key", 0.5, color="#55585F"), loc=tab, rot=(0, 0, tab_turn), parent=root)
    tube("Tablet_Ring", ring_pts(on_tab(-0.142, 0.0, 0.009), 0.016, 20), 0.0025, mat("tablet_key", 0.5,
         color="#55585F"), closed=True, parent=root)
    rod("Tablet_Pen", on_tab(0.06, -0.135, 0.006), on_tab(0.2, -0.125, 0.006), 0.0055, mat("dark", 0.3), parent=root)
    rod("Tablet_PenGrip", on_tab(0.06, -0.135, 0.006), on_tab(0.1, -0.132, 0.006), 0.006, RUBBER, parent=root)
    kb = Vector((WING_X + 0.56, -0.08, top))
    box("Keyboard_Body", (0.279, 0.115, 0.007), kb + Vector((0, 0, 0.005)), STEEL, bevel=0.003, rot=(R(-2.5), 0, 0),
        parent=root)
    keys = []
    for row in range(5):
        y = -0.042 + row * 0.019
        n = 13 if row else 14
        kw = 0.264 / n
        for k in range(n):
            if row == 0 and 3 < k < 9:
                continue
            kh = 0.009 if row == 4 else 0.016
            keys.append(((kw - 0.003, kh, 0.002), (-0.132 + kw * (k + 0.5), y, 0.0105 + row * 0.0008)))
        if row == 0:
            keys.append(((0.1, 0.016, 0.002), (-0.132 + kw * 6.5, y, 0.0105)))           # space bar
    boxes("Keyboard_Keys", keys, mat("cream", 0.45), bevel=0.0008, loc=kb, parent=root)
    mug("Drafting_Mug", (WING_X + 0.71, -0.29, top), ceramic("cream", 0.25), turn=-60, parent=root)


def build_monitor():
    """24-inch all-in-one computer: thin coloured body, white bezel, pastel chin and a bent-plate stand."""
    root, w, d, h = furniture_root("monitor")
    back = surface(mat("main", 0.35, metal=0.5), "brushed")
    chin = surface(mat("main", 0.35, metal=0.5, color=shade("main", 1.45)), "brushed")
    bezel = mat("cream", 0.25)
    bw, bh, bd = 0.547, 0.39, 0.0115
    z0 = h - bh                                      # bottom of the body (the stand lifts it 8 cm)
    box("Monitor_Foot", (0.13, 0.147, 0.006), (0, 0.025, 0.003), back, bevel=0.002, parent=root)
    beam("Monitor_Stand", (0, 0.095, 0.004), (0, 0.012, z0 + 0.2), (0.13, 0.006), back, bevel=0.002, parent=root)
    box("Monitor_Back", (bw, bd - 0.002, bh), (0, 0.001, z0 + bh / 2), back, bevel=0.004, parent=root)
    box("Monitor_Chin", (bw, 0.003, 0.068), (0, -bd / 2 + 0.0005, z0 + 0.034), chin, bevel=0.0015, parent=root)
    box("Monitor_Bezel", (bw - 0.002, 0.002, bh - 0.068), (0, -bd / 2 + 0.0005, z0 + 0.068 + (bh - 0.068) / 2), bezel,
        bevel=0.001, parent=root)
    sw, sh = 0.521, 0.293
    sz = z0 + 0.068 + 0.013 + sh / 2
    sy = -bd / 2 - 0.0012
    scr = hook_image("screen", 1, (sw, sh), (0, sy, sz), parent=root, glow=True, default_key="cream")
    # default "design tool" UI: toolbar, layer panel, properties panel, an artboard with a hero and cards
    yy = sy - 0.0008
    ui = [
        box("UI_Toolbar", (sw, 0.0006, 0.02), (0, yy, sz + sh / 2 - 0.01), mat("dark", 0.5, emit=0.6), bevel=0,
            parent=root),
        box("UI_Left", (0.085, 0.0006, sh - 0.02), (-sw / 2 + 0.0425, yy, sz - 0.01),
            mat("ui_panel", 0.5, emit=0.6, color="#E9ECF2"), bevel=0, parent=root),
        box("UI_Right", (0.085, 0.0006, sh - 0.02), (sw / 2 - 0.0425, yy, sz - 0.01),
            mat("ui_panel", 0.5, emit=0.6, color="#E9ECF2"), bevel=0, parent=root),
        box("UI_Canvas", (sw - 0.17, 0.0006, sh - 0.02), (0, yy, sz - 0.01), mat("ui_canvas", 0.5, emit=0.6,
            color="#C9CDD4"), bevel=0, parent=root),
        box("UI_Artboard", (0.3, 0.0006, 0.24), (0, yy - 0.0004, sz - 0.01), mat("sky", 0.5, emit=0.8), bevel=0,
            parent=root),
    ]
    # the artboard holds the same landscape that is on the easel, as if it was scanned in for retouching
    ui += default_art(None, 0.3, 0.24, (0, yy - 0.0006, sz - 0.01), (0, 0, 0), root, "landscape", name="UI",
                      glow=0.8)
    for k, key in enumerate(PAINTS + ["dark", "cream"]):                 # colour swatches in the right panel
        ui.append(box("UI_Swatch", (0.02, 0.0006, 0.02), (sw / 2 - 0.07 + (k % 3) * 0.0275, yy - 0.0008,
                      sz + 0.08 - (k // 3) * 0.0275), mat(key, 0.5, emit=0.9), bevel=0, parent=root))
    for k in range(6):
        ui.append(box("UI_Layer", (0.06, 0.0006, 0.01), (-sw / 2 + 0.0425, yy - 0.0008, sz + 0.1 - k * 0.032),
                      mat("ui_line", 0.5, emit=0.6, color="#B9C0CC"), bevel=0, parent=root))
    hook_default(scr, *ui)
    glow = light("Light_Monitor", "AREA", 10 if NIGHT else 2.5, kelvin(7500), (0, -0.12, sz), size=0.5)
    glow.parent = root
    glow.rotation_euler = (R(-90), 0, 0)


LAMP_LIGHT_AT = []                                   # filled by build_lamp(): bulb position and aim


def build_lamp():
    """Spring-arm desk lamp with a desk clamp: twin arm rods, three base springs, knuckle and bell shade."""
    root, w, d, h = furniture_root("lamp")
    body = powder("accent_1", 0.35)
    edge_y = 0.09                                    # the table's back edge, in this slot's frame
    box("Lamp_ClampTop", (0.05, 0.08, 0.014), (0, edge_y - 0.035, 0.007), body, bevel=0.003, parent=root)
    box("Lamp_ClampBack", (0.05, 0.016, 0.1), (0, edge_y + 0.008, -0.04), body, bevel=0.003, parent=root)
    box("Lamp_ClampJaw", (0.05, 0.06, 0.012), (0, edge_y - 0.02, -0.084), body, bevel=0.003, parent=root)
    rod("Lamp_ClampScrew", (0, edge_y - 0.03, -0.078), (0, edge_y - 0.03, -0.05), 0.005, STEEL, parent=root)
    cyl("Lamp_ClampKnob", 0.016, 0.012, (0, edge_y - 0.03, -0.095), PLASTIC, segs=16, parent=root)
    cyl("Lamp_Column", 0.012, 0.08, (0, edge_y - 0.04, 0.054), body, segs=16, parent=root)
    pivot = Vector((0, edge_y - 0.04, 0.1))
    elbow = Vector((-0.16, -0.02, 0.43))
    head = Vector((-0.34, -0.17, 0.42))
    box("Lamp_Swivel", (0.04, 0.03, 0.03), pivot, body, bevel=0.006, parent=root)
    side = (elbow - pivot).cross(Vector((0, 0, 1))).normalized() * 0.011
    for s in (-1, 1):                                                        # twin parallel arms
        rod("Lamp_ArmLow", pivot + side * s, elbow + side * s, 0.0045, body, parent=root, segs=8)
        rod("Lamp_ArmHigh", elbow + side * s, head + side * s, 0.0045, body, parent=root, segs=8)
    for k in range(3):                                                       # the three springs
        off = Vector((0.018 * (k - 1), 0.016, 0))
        a, b = pivot + off + Vector((0, 0, 0.005)), pivot + off + (elbow - pivot) * 0.42
        axis = (b - a).normalized()
        perp = axis.cross(Vector((1, 0, 0))).normalized()
        perp2 = axis.cross(perp)
        pts = [a + (b - a) * (i / 90) + (perp * math.cos(i * 0.9) + perp2 * math.sin(i * 0.9)) * 0.0045
               for i in range(91)]
        tube("Lamp_Spring", pts, 0.0011, STEEL, segs=5, parent=root)
    ball("Lamp_Knuckle", 0.014, elbow, body, parent=root)
    ball("Lamp_HeadJoint", 0.012, head, body, parent=root)
    aim = Vector((-0.15, -0.2, -1)).normalized()
    # bell shade: a rounded crown that opens to a 14 cm rim, 19 cm long overall with the knuckle
    prof = [(0.004, -0.01), (0.022, -0.006), (0.036, 0.008), (0.048, 0.035), (0.058, 0.075), (0.066, 0.11),
            (0.07, 0.125), (0.071, 0.128)]
    shade_o = lathe("Lamp_Shade", prof, body, loc=head + aim * 0.02, rot=aim.to_track_quat("Z", "Y").to_euler(),
                    parent=root)
    inner = lathe("Lamp_ShadeInner", [(r - 0.002, z) for r, z in prof[2:]], mat("cream", 0.4),
                  loc=head + aim * 0.02, rot=shade_o.rotation_euler, parent=root)
    bulb = ball("Lamp_Bulb", 0.026, head + aim * 0.1, mat("bulb", 0.3, emit=6.0, color="#FFE2B0"), parent=root)
    no_shadow(shade_o, inner, bulb)
    LAMP_LIGHT_AT[:] = [root.location + head + aim * 0.08, aim]         # Light_Lamp sits inside the shade


def build_easel():
    """Beechwood H-frame studio easel: base with castors, two uprights, centre mast, canvas tray, top clamp."""
    root, w, d, h = furniture_root("easel")
    bw = 0.53
    for y in (-0.24, 0.24):                                                  # base: front + back feet
        box("Easel_BaseRail", (bw, 0.06, 0.05), (0, y, 0.065), MAPLE, parent=root)
        for x in (-bw / 2 + 0.04, bw / 2 - 0.04):
            cyl("Easel_Castor", 0.02, 0.016, (x, y, 0.02), RUBBER, rot=(0, R(90), 0), segs=16, parent=root)
            box("Easel_CastorFork", (0.03, 0.03, 0.02), (x, y, 0.035), STEEL, bevel=0.003, parent=root)
    for x in (-0.19, 0.19):
        box("Easel_SideRail", (0.045, 0.54, 0.045), (x, 0, 0.1), MAPLE, parent=root)
        box("Easel_Upright", (0.045, 0.045, 1.3), (x, -0.03, 0.12 + 0.65), MAPLE_V, parent=root)
        beam("Easel_Brace", (x, 0.22, 0.12), (x, -0.01, 0.8), (0.035, 0.03), MAPLE, parent=root)
    for z in (0.32, 1.4):                                                    # the H crossbars
        box("Easel_Cross", (0.34, 0.04, 0.05), (0, -0.03, z), MAPLE, parent=root)
    mast_y = -0.06
    box("Easel_Mast", (0.045, 0.035, h - 0.34), (0, mast_y, 0.34 + (h - 0.34) / 2), MAPLE_V, parent=root)
    box("Easel_StorageTray", (0.44, 0.34, 0.012), (0, 0.0, 0.135), MAPLE, parent=root)
    # canvas tray (with a lip) on two T-knobs, and the canvas resting on it
    tray_z = 0.74
    box("Easel_Tray", (0.6, 0.1, 0.025), (0, mast_y - 0.06, tray_z), MAPLE, parent=root)
    box("Easel_TrayLip", (0.6, 0.012, 0.03), (0, mast_y - 0.104, tray_z + 0.025), MAPLE, parent=root)
    box("Easel_TrayBlock", (0.06, 0.04, 0.12), (0, mast_y - 0.005, tray_z - 0.04), MAPLE, parent=root)
    for x in (-0.19, 0.19):
        cyl("Easel_TKnob", 0.014, 0.03, (x, -0.06, tray_z - 0.03), PLASTIC, rot=(R(90), 0, 0), segs=12, parent=root)
    for k, key in enumerate(("accent_1", "main", "accent_2", "accent_3")):    # paint tubes in the tray
        paint_tube(f"Easel_Tube_{k}", (-0.24 + k * 0.05, mast_y - 0.065, tray_z + 0.026), key, turn=80 + 8 * k,
                   parent=root)
    cw, ch, cd = 0.76, 0.61, 0.038
    cz = tray_z + 0.0125 + ch / 2
    cy = mast_y - 0.04 - cd / 2
    box("Easel_Canvas", (cw, cd, ch), (0, cy, cz), surface(mat("cloth", 0.9), "fabric"), bevel=0.004, parent=root)
    canvas = hook_image("canvas", 1, (cw - 0.006, ch - 0.006), (0, cy - cd / 2 - 0.0008, cz), parent=root,
                        default_key="sky")
    default_art(canvas, cw - 0.006, ch - 0.006, (0, cy - cd / 2 - 0.0008, cz), (0, 0, 0), root, "landscape")
    clamp_z = cz + ch / 2 + 0.02
    box("Easel_Clamp", (0.1, 0.08, 0.04), (0, mast_y - 0.03, clamp_z), MAPLE, parent=root)
    cyl("Easel_ClampKnob", 0.016, 0.03, (0, mast_y + 0.03, clamp_z), PLASTIC, rot=(R(90), 0, 0), segs=12, parent=root)
    cyl("Easel_MastKnob", 0.018, 0.035, (0, 0.0, 1.4), PLASTIC, rot=(R(90), 0, 0), segs=12, parent=root)


def build_stool():
    """Tolix H65-style steel stool: rolled-rim round seat, four splayed angle-section legs, footrest ring."""
    root, w, d, h = furniture_root("stool")
    steel = surface(mat("accent_2", 0.5, metal=0.2), "brushed")             # lacquered sheet steel
    top_r, foot = 0.125, 0.255             # real H65: 28 cm seat, legs splay out to a 40 x 40 cm footprint
    feet = []
    a_arm, t_arm = 0.026, 0.0025          # folded angle-section legs: two 26 mm flanges of 2.5 mm steel
    L_shape = [(0, 0), (-a_arm * 0.707, a_arm * 0.707), (-a_arm * 0.707 - t_arm * 0.707, a_arm * 0.707 - t_arm * 0.707),
               (-t_arm * 1.414, 0), (-a_arm * 0.707 - t_arm * 0.707, -a_arm * 0.707 + t_arm * 0.707),
               (-a_arm * 0.707, -a_arm * 0.707)]
    for k in range(4):
        a = R(45 + 90 * k)
        c, s = math.cos(a), math.sin(a)
        p0 = Vector((c * foot, s * foot, 0.012))
        p1 = Vector((c * top_r, s * top_r, h - 0.012))
        feet.append((p0, p1))
        zax = (p1 - p0).normalized()                                         # leg frame: corner points outward
        xax = (Vector((c, s, 0)) - zax * Vector((c, s, 0)).dot(zax)).normalized()
        frame = Matrix((xax, zax.cross(xax), zax)).transposed()
        flat("Stool_Leg", L_shape, steel, loc=p0, rot=frame.to_euler(), parent=root, thick=(p1 - p0).length)
        cyl("Stool_Foot", 0.012, 0.012, (p0.x - c * 0.008, p0.y - s * 0.008, 0.006), RUBBER, segs=12, parent=root)
    ring_z = 0.25
    for k in range(4):                                                       # flat-bar footrest ring
        a0, a1 = feet[k], feet[(k + 1) % 4]
        t = ring_z / (h - 0.032)
        pa, pb = a0[0].lerp(a0[1], t), a1[0].lerp(a1[1], t)
        beam("Stool_Ring", pa, pb, (0.025, 0.004), steel, bevel=0.001, roll=0, parent=root)
    cyl("Stool_Seat", 0.14, 0.012, (0, 0, h - 0.008), steel, segs=40, bevel=0.003, parent=root)
    tube("Stool_SeatRim", ring_pts((0, 0, h - 0.014), 0.138, 40), 0.009, steel, closed=True, parent=root)
    cyl("Stool_SeatSkirt", 0.132, 0.03, (0, 0, h - 0.03), steel, segs=40, bevel=0.002, parent=root)   # pressed apron
    cyl("Stool_Hole", 0.008, 0.002, (0, 0, h - 0.0015), mat("shadow", 0.9, color=shade("dark", 0.6)), segs=12,
        bevel=0, parent=root)


def build_cabinet():
    """Wooden A1 plan chest: six shallow drawers with 4 mm gaps, brass label frames and D-handles, on a plinth.
    On top: a cutting mat, paper stacks, a sketchbook (email link), a brush jar and a mug."""
    root, w, d, h = furniture_root("cabinet")
    oak = wood("oak", 0.4, color=shade("wood", 0.8))                        # darker oak than the maple table
    oak_side = wood("oak", 0.41, along="Z", color=shade("wood", 0.8))        # grain runs up the side panels
    box("Chest_Plinth", (w - 0.06, d - 0.06, 0.05), (0, 0.02, 0.025), mat("dark", 0.6), bevel=0.003, parent=root)
    box("Chest_Body", (w, d - 0.02, h - 0.075), (0, 0.01, 0.05 + (h - 0.075) / 2), oak_side, parent=root)
    box("Chest_Top", (w + 0.02, d + 0.01, 0.025), (0, 0.0, h - 0.0125), oak, parent=root)
    n, gap = 6, 0.004
    zone0, zone1 = 0.055, h - 0.03
    dh = (zone1 - zone0) / n
    front_y = -d / 2 + 0.008
    for i in range(n):
        z = zone0 + dh * (i + 0.5)
        box("Chest_Drawer", (w - 0.03, 0.018, dh - gap), (0, front_y - 0.006, z), oak, bevel=0.002, parent=root)
        box("Chest_LabelFrame", (0.09, 0.004, 0.042), (0, front_y - 0.017, z + 0.01), BRASS, bevel=0.001, parent=root)
        box("Chest_Label", (0.078, 0.002, 0.03), (0, front_y - 0.019, z + 0.01), PAPER, bevel=0, parent=root)
        for x in (-0.33, 0.33):
            rod("Chest_Handle", (x - 0.055, front_y - 0.033, z - 0.012), (x + 0.055, front_y - 0.033, z - 0.012), 0.005,
                BRASS, parent=root, segs=10)
            for dx in (-0.05, 0.05):
                rod("Chest_HandlePost", (x + dx, front_y - 0.015, z - 0.012), (x + dx, front_y - 0.034, z - 0.012),
                    0.004, BRASS, parent=root, segs=8)
    top = h
    # self-healing A2 cutting mat with a printed grid
    box("Chest_CuttingMat", (0.6, 0.45, 0.003), (-0.17, -0.08, top + 0.0015), mat("mat", 0.75, color="#2F7D60"),
        bevel=0.001, parent=root)
    grid = [((0.0012, 0.43, 0.0004), (-0.46 + k * 0.05, -0.08, top + 0.0032)) for k in range(12)]
    grid += [((0.58, 0.0012, 0.0004), (-0.17, -0.29 + k * 0.05, top + 0.0032)) for k in range(9)]
    boxes("Chest_MatGrid", grid, mat("mat_line", 0.7, color="#8FCFB2"), parent=root)
    rod("Chest_Knife", (-0.02, -0.22, top + 0.008), (0.1, -0.25, top + 0.008), 0.0045, mat("accent_1", 0.45),
        parent=root, segs=8)
    for i in range(6):                                                       # stack of cartridge paper
        box("Chest_Paper", (0.42, 0.3, 0.003), (-0.22, 0.12, top + 0.0045 + i * 0.0032), PAPER, bevel=0.0005,
            rot=(0, 0, R(random.uniform(-3, 3))), parent=root)
    book = box("Chest_Sketchbook", (0.21, 0.297, 0.018), (0.2, -0.06, top + 0.009), mat("dark", 0.55), bevel=0.003,
               rot=(0, 0, R(8)), parent=root)
    hook_link(book, "email")
    box("Chest_SketchbookBand", (0.008, 0.3, 0.02), (0.27, -0.05, top + 0.0095), mat("accent_1", 0.5), bevel=0.001,
        rot=(0, 0, R(8)), parent=root)
    cyl("Chest_Jar", 0.045, 0.13, (0.36, 0.2, top + 0.065), GLASS, segs=24, parent=root)
    cyl("Chest_JarWater", 0.042, 0.06, (0.36, 0.2, top + 0.032), mat("water", 0.1, color="#A9C2D9"), segs=24,
        bevel=0, parent=root)
    for k in range(6):
        a = k * 1.05
        brush(f"Chest_Brush_{k}", (0.36 + math.cos(a) * 0.012, 0.2 + math.sin(a) * 0.012, top + 0.01),
              (0.36 + math.cos(a) * 0.05, 0.2 + math.sin(a) * 0.04, top + 0.27 + 0.025 * (k % 3)), PAINTS[k % 4],
              parent=root)
    mug("Chest_Mug", (0.42, -0.22, top), ceramic("accent_3", 0.25), turn=30, parent=root)
    cyl("Chest_TapeRoll", 0.035, 0.018, (0.05, 0.22, top + 0.009), tape_m(), segs=24, parent=root)


def build_shelf():
    """IKEA IVAR-style pine shelving: ladder side units with drilled holes, five shelves, steel X-brace.
    Filled with art books, magazine files, kraft boxes, jars and rolled paper."""
    root, w, d, h = furniture_root("shelf")
    hook_link(root, "github")
    for sx in (-1, 1):                                                       # side units (ladders)
        x = sx * (w / 2 - 0.012)
        for sy in (-1, 1):
            box("Shelf_Post", (0.024, 0.044, h), (x, sy * (d / 2 - 0.022), h / 2), PINE_V, bevel=0.003, parent=root)
        holes = [((0.0005, 0.006, 0.006), (x - sx * 0.0122, -(d / 2 - 0.022), 0.1 + k * 0.032)) for k in range(52)]
        boxes("Shelf_Holes", holes, mat("shadow", 0.9, color=shade("wood", 0.55)), parent=root)
        for z in (0.06, h - 0.04):
            box("Shelf_Rung", (0.02, d - 0.08, 0.035), (x, 0, z), PINE, parent=root)
    for s in (-1, 1):                                                        # galvanised X-brace at the back
        beam("Shelf_Brace", (-w / 2 + 0.03, d / 2 - 0.004, 0.08 if s > 0 else h - 0.08),
             (w / 2 - 0.03, d / 2 - 0.004, h - 0.08 if s > 0 else 0.08), (0.018, 0.0015), STEEL, bevel=0, parent=root)
    levels = [0.12, 0.5, 0.88, 1.26, 1.64]
    inner = w - 0.048
    for i, z in enumerate(levels):
        box("Shelf_Shelf", (inner, d, 0.018), (0, 0, z), PINE, bevel=0.003, parent=root)
        box("Shelf_ShelfBatten", (inner, 0.02, 0.03), (0, -d / 2 + 0.01, z - 0.024), PINE, parent=root)
    base = [z + 0.009 for z in levels]
    x0, x1 = -inner / 2 + 0.02, inner / 2 - 0.02
    # bottom: two kraft storage boxes with hand holes
    for k in range(2):
        cx = x0 + 0.2 + k * 0.4
        box("Shelf_Box", (0.37, 0.27, 0.24), (cx, 0.0, base[0] + 0.12), KRAFT, bevel=0.004, parent=root)
        box("Shelf_BoxHole", (0.09, 0.004, 0.03), (cx, -0.136, base[0] + 0.19), mat("shadow", 0.9,
            color=shade("dark", 0.6)), bevel=0.012, parent=root)
    # shelf 1: art books of varied height and thickness, leaning bookend
    x = x0
    while x < x1 - 0.05:
        t = random.uniform(0.018, 0.045)
        bh = random.uniform(0.21, 0.31)
        key = random.choice(PAINTS + ["cream", "dark", "wood"])
        bd = random.uniform(0.2, 0.25)
        box("Shelf_Book", (t, bd, bh), (x + t / 2, -0.02, base[1] + bh / 2), mat(key, 0.7), bevel=0.002, parent=root)
        ink = "cream" if key in ("dark", "main", "accent_3") else "dark"   # spine title block + head/tail bands
        spine_y = -0.02 - bd / 2 - 0.0004
        for z, sh in ((bh * random.uniform(0.62, 0.78), 0.035), (bh * 0.1, 0.006), (bh * 0.9, 0.006)):
            box("Shelf_BookSpine", (t * 0.7, 0.001, sh), (x + t / 2, spine_y, base[1] + z), mat(ink, 0.6), bevel=0,
                parent=root)
        x += t + 0.002
    # shelf 2: magazine files and a jar of pencils
    # magazine files (IKEA TJENA / FLYTTBAR type, 10 x 25 x 30 cm): tall at the back, cut away in a long
    # slope to a low front, so you see the papers inside. Profile points are (-z, y); extruded along x.
    prof = [(0, -0.12), (0, 0.12), (-0.3, 0.12), (-0.3, 0.035), (-0.11, -0.12)]
    for k in range(4):
        key = ("cream", "main", "cream", "accent_3")[k]
        fx, fw = x0 + 0.005 + k * 0.095, 0.085
        fm = mat(key, 0.6)
        for sx in (0, fw - 0.003):                                           # the two cut-away side walls
            flat("Shelf_MagFile", prof, fm, loc=(fx + sx, -0.01, base[2]), rot=(0, R(90), 0), parent=root,
                 thick=0.003)
        box("Shelf_MagFileBack", (fw, 0.003, 0.3), (fx + fw / 2, 0.1085, base[2] + 0.15), fm, bevel=0.001, parent=root)
        box("Shelf_MagFileFront", (fw, 0.003, 0.11), (fx + fw / 2, -0.1285, base[2] + 0.055), fm, bevel=0.001,
            parent=root)
        box("Shelf_MagFileBase", (fw, 0.24, 0.003), (fx + fw / 2, -0.01, base[2] + 0.0015), fm, bevel=0, parent=root)
        for j in range(3):                                                   # papers and catalogues inside
            flat("Shelf_MagPaper", [(0, -0.11), (0, 0.11), (-0.27 + j * 0.02, 0.11), (-0.25 + j * 0.02, 0.02),
                                    (-0.14 + j * 0.01, -0.11)],
                 mat("mag_" + str(j), 0.7, color=("#F2EEE6", COLORS[PAINTS[(k + j) % 4]], "#D9D2C4")[j]),
                 loc=(fx + 0.01 + j * 0.022, -0.012, base[2] + 0.003), rot=(0, R(90), 0), parent=root, thick=0.018)
    cyl("Shelf_PencilPot", 0.04, 0.1, (x1 - 0.12, -0.03, base[2] + 0.05), ceramic("accent_1", 0.3), segs=24,
        parent=root)
    for k in range(5):
        a = k * 1.25
        pencil("Shelf_Pencil", (x1 - 0.12 + math.cos(a) * 0.012, -0.03 + math.sin(a) * 0.012, base[2] + 0.02),
               (x1 - 0.12 + math.cos(a) * 0.03, -0.03 + math.sin(a) * 0.03, base[2] + 0.18), parent=root,
               key=PAINTS[k % 4])
    # shelf 3: glass jars of paint with coloured lids and a small cactus
    for k in range(5):
        jx = x0 + 0.05 + k * 0.1
        key = PAINTS[(k + SEED) % 4]
        cyl("Shelf_Jar", 0.04, 0.11, (jx, -0.03, base[3] + 0.055), GLASS, segs=20, parent=root)
        cyl("Shelf_JarPaint", 0.036, 0.07, (jx, -0.03, base[3] + 0.037), mat(key, 0.35), segs=20, bevel=0, parent=root)
        cyl("Shelf_JarLid", 0.041, 0.018, (jx, -0.03, base[3] + 0.119), powder(key, 0.4), segs=20, parent=root)
    cyl("Shelf_CactusPot", 0.05, 0.08, (x1 - 0.1, -0.02, base[3] + 0.04), TERRACOTTA, r2=0.058, segs=20, parent=root)
    cactus("Shelf_Cactus", (x1 - 0.1, -0.02, base[3] + 0.076), 0.042, 0.1, parent=root, ribs=12)
    # top shelf: rolls of paper, a kraft box and a trailing pothos
    for k in range(3):
        cyl("Shelf_Roll", 0.035, 0.6, (-0.1 + 0.0, -0.06 + k * 0.07, base[4] + 0.035 + (k == 1) * 0.06),
            mat(("cream", "sky", "cloth")[k], 0.8), rot=(0, R(90), R(3 * k)), segs=20, parent=root)
    box("Shelf_TopBox", (0.24, 0.22, 0.16), (x1 - 0.14, 0.0, base[4] + 0.08), KRAFT, bevel=0.004, parent=root)
    cyl("Shelf_PlantPot", 0.06, 0.1, (x0 + 0.08, -0.04, base[4] + 0.05), ceramic("cream", 0.3), segs=24, parent=root)
    for k in range(6):                                                       # trailing vines over the edge
        a = k * 1.05
        start = Vector((x0 + 0.08 + math.cos(a) * 0.03, -0.04 + math.sin(a) * 0.03, base[4] + 0.1))
        end = start + Vector((math.cos(a) * 0.05, -0.12 - 0.03 * (k % 2), -0.2 - 0.12 * (k % 3)))
        pts = bezier(start, start + Vector((0, -0.1, 0.03)), end, 8)
        tube("Shelf_Vine", pts, 0.002, mat("plant", 0.5), parent=root, segs=5)
        for p in pts[2::2]:
            ball("Shelf_Leaf", 0.017, p, mat("plant", 0.5, color=shade("plant", 1.12)), scale=(1, 0.5, 0.8),
                 parent=root)


LEAF_PROFILE = [(0.0, 0.0), (0.08, 0.13), (0.25, 0.21), (0.42, 0.2), (0.6, 0.27), (0.78, 0.3), (0.92, 0.24),
                (1.0, 0.0)]                 # fiddle-leaf fig: narrow stalk end, slight waist, wide rounded tip


def leaf_width(t):
    """Half-width of a fiddle-leaf at t (0 = stalk, 1 = tip), smoothly through LEAF_PROFILE."""
    for (t0, w0), (t1, w1) in zip(LEAF_PROFILE, LEAF_PROFILE[1:]):
        if t <= t1:
            f = (t - t0) / (t1 - t0)
            f = f * f * (3 - 2 * f)                                          # ease between profile points
            return w0 + (w1 - w0) * f
    return 0.0


def leaf(name, length, material, loc, rot, parent=None):
    """A leathery fiddle-leaf: dense smooth mesh, raised along the midrib, edges cupped down and slightly
    wavy, the tip curling down - big and stiff like the real plant."""
    bm = bmesh.new()
    rows, cols = 16, 6
    grid = []
    for j in range(rows + 1):
        t = j / rows
        hw = max(leaf_width(t), 0.004) * length
        y, sag = t * length, -0.18 * length * t * t
        row = []
        for i in range(cols + 1):
            s = i / cols * 2 - 1                                              # -1 edge .. 0 midrib .. 1 edge
            wave = 0.012 * length * math.sin(t * 14 + s * 2) * abs(s)
            z = sag + 0.05 * length * math.sin(math.pi * min(1.0, t * 1.1)) * (1 - s * s) + wave
            row.append(bm.verts.new((s * hw, y, z)))
        grid.append(row)
    for a, b in zip(grid, grid[1:]):
        for i in range(cols):
            bm.faces.new((a[i], a[i + 1], b[i + 1], b[i]))
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, 0, None, parent)


def build_plant():
    """Fiddle-leaf fig in a glazed pot: woody stem and big violin-shaped leaves with a pale midrib."""
    root, w, d, h = furniture_root("plant")
    pot = ceramic("cream", 0.25, color=shade("wall_trim", 0.88))
    cyl("Plant_Pot", 0.115, 0.22, (0, 0, 0.11), pot, r2=0.125, segs=32, parent=root)
    tube("Plant_PotRim", ring_pts((0, 0, 0.22), 0.124, 32), 0.008, pot, closed=True, parent=root)
    cyl("Plant_Soil", 0.115, 0.01, (0, 0, 0.205), mat("soil", 0.95, color="#3B2A20"), bevel=0, parent=root)
    trunk = mat("trunk", 0.7, color="#7A5E45")
    stem = bezier((0, 0, 0.2), (0.04, 0.0, 0.6), (-0.01, 0.02, h - 0.12), 10)
    tube("Plant_Stem", stem, 0.013, trunk, parent=root, segs=10)
    greens = [mat("plant", 0.32, color=shade("plant", 0.9)), mat("plant_dark", 0.32, color=shade("plant", 0.72)),
              mat("plant_light", 0.32, color=shade("plant", 1.05))]          # waxy, glossy leaves
    rib = mat("rib", 0.5, color=shade("plant", 1.35))
    n = 18
    for k in range(n):
        t = 0.25 + 0.75 * k / (n - 1)
        p = stem[min(10, int(t * 10))]
        a = k * 2.4
        length = 0.2 + 0.1 * math.sin(k * 0.7 + 1) ** 2 + (0.04 if k < 6 else 0)
        pitch = R(random.uniform(20, 45) if k < n - 3 else random.uniform(55, 75))
        base = Vector(p) + Vector((math.cos(a) * 0.05, math.sin(a) * 0.05, 0))
        rod("Plant_Petiole", p, base, 0.004, trunk, parent=root, segs=6)
        rot = (pitch, 0, a - math.pi / 2)
        leaf("Plant_Leaf", length, greens[k % 3], base, rot, parent=root)
        m = Euler(rot).to_matrix()
        rib_pts = [base + m @ Vector((0, t * length, -0.18 * length * t * t
                                      + 0.05 * length * math.sin(math.pi * min(1.0, t * 1.1)) + 0.0012))
                   for t in (i / 8 * 0.9 for i in range(9))]
        tube("Plant_Midrib", rib_pts, 0.0022, rib, parent=root, segs=5)


def build_rug():
    """Cotton duck drop cloth folded double: soft wrinkles, a hem, a turned-back corner and paint splatter."""
    root, w, d, h = furniture_root("rug")
    nx, ny = 36, 28

    def cloth_z(x, y):
        z = 0.004 + 0.006 * (math.sin(x * 9.0 + y * 4.0) * math.sin(y * 6.0 - x * 3.0)) ** 2
        z += 0.018 * max(0.0, 1 - abs(y - 0.35 + 0.2 * x) / 0.07) ** 2                # long soft folds
        z += 0.012 * max(0.0, 1 - abs(x + 0.45 - 0.3 * y) / 0.06) ** 2
        return max(0.002, z)
    bm = bmesh.new()
    verts = []
    for j in range(ny + 1):
        row = []
        for i in range(nx + 1):
            x, y = -w / 2 + w * i / nx, -d / 2 + d * j / ny
            row.append(bm.verts.new((x, y, cloth_z(x, y))))
        verts.append(row)
    for j in range(ny):
        for i in range(nx):
            bm.faces.new((verts[j][i], verts[j][i + 1], verts[j + 1][i + 1], verts[j + 1][i]))
    cloth_m = surface(mat("cloth", 0.95), "fabric", scale=0.5)
    _finish(_obj("DropCloth", bm), cloth_m, 0, None, root)
    box("DropCloth_Hem", (w, 0.03, 0.004), (0, -d / 2 + 0.015, 0.006), cloth_m, bevel=0.001, parent=root)
    flat("DropCloth_Corner", [(0, 0), (0.32, 0), (0, 0.26)], cloth_m, loc=(w / 2 - 0.005, -d / 2 + 0.005, 0.01),
         rot=(0, 0, R(90)), parent=root)
    # Real splatter collects under the work: most stains sit round the easel, a few stray drips elsewhere.
    # Stains are kept off the folds and follow the cloth surface.
    easel_local = Matrix.Rotation(-root.rotation_euler.z, 3, "Z") @ (SLOTS["easel"].location - root.location)
    placed = 0
    while placed < PAINT_SPLATS * 3 // 4:
        if random.random() < 0.75:
            x, y = random.gauss(easel_local.x, 0.32), random.gauss(easel_local.y - 0.1, 0.28)
        else:
            x, y = random.uniform(-w / 2 + 0.1, w / 2 - 0.1), random.uniform(-d / 2 + 0.1, d / 2 - 0.1)
        if abs(x) > w / 2 - 0.08 or abs(y) > d / 2 - 0.08 or cloth_z(x, y) > 0.0095:
            continue
        r = random.uniform(0.008, 0.03) if random.random() < 0.8 else random.uniform(0.03, 0.05)
        splat("DropCloth_Splat", (x, y, cloth_z(x, y) + 0.0004), r, random.choice(PAINTS), parent=root)
        placed += 1
    # a one-litre paint tin with a wire handle and a drip, and a rag
    tin = (-0.65, -0.45)
    cyl("PaintTin", 0.055, 0.12, (tin[0], tin[1], 0.07), STEEL, segs=28, parent=root)
    cyl("PaintTin_Label", 0.0555, 0.07, (tin[0], tin[1], 0.065), mat("main", 0.6), segs=28, bevel=0, parent=root)
    cyl("PaintTin_Lid", 0.056, 0.008, (tin[0], tin[1], 0.134), STEEL, segs=28, parent=root)
    tube("PaintTin_Handle", bezier((tin[0] - 0.055, tin[1], 0.11), (tin[0], tin[1] - 0.02, 0.2),
                                   (tin[0] + 0.055, tin[1], 0.11), 10), 0.0015, STEEL, parent=root)
    rod("PaintTin_Drip", (tin[0] - 0.05, tin[1] - 0.025, 0.13), (tin[0] - 0.052, tin[1] - 0.026, 0.06), 0.005,
        mat("main", 0.3), parent=root)
    rag("Rag", (-0.42, 0.42, 0.009), (0.3, 0.24), surface(mat("rag", 0.95, color=mix_hex(COLORS["cloth"],
        COLORS["accent_1"], 0.25)), "fabric"), turn=25, parent=root)


def build_wall_art():
    """The moodboard: a pine-framed 120x90 cork board with three A3 prints, swatch strips and index cards."""
    root, w, d, h = furniture_root("wall_art")
    frame_w = 0.025
    box("Moodboard_Cork", (w - 2 * frame_w, 0.01, h - 2 * frame_w), (0, d / 2 - 0.012, h / 2),
        surface(mat("cork", 0.95), "terrazzo", scale=8), bevel=0.0, parent=root)
    box("Moodboard_Back", (w, 0.008, h), (0, d / 2 - 0.004, h / 2), mat("dark", 0.8), bevel=0.0, parent=root)
    for nm, size, loc, m in [("Top", (w, 0.028, frame_w), (0, d / 2 - 0.014, h - frame_w / 2), PINE),
                             ("Bottom", (w, 0.028, frame_w), (0, d / 2 - 0.014, frame_w / 2), PINE),
                             ("L", (frame_w, 0.028, h), (-w / 2 + frame_w / 2, d / 2 - 0.014, h / 2), PINE_V),
                             ("R", (frame_w, 0.028, h), (w / 2 - frame_w / 2, d / 2 - 0.014, h / 2), PINE_V)]:
        box(f"Moodboard_Frame_{nm}", size, loc, m, bevel=0.003, parent=root)
    front = d / 2 - 0.017                               # front face of the cork

    def pin(loc, key):
        ball("Moodboard_Pin", 0.007, Vector(loc) + Vector((0, -0.008, 0)), mat(key, 0.3), parent=root)
    prints = [  # (x, z centre, tilt, default colour, default artwork)  - A3 landscape 42 x 29.7 cm
        (-0.27, 0.635, -1.5, "cream", "poster"),
        (0.25, 0.65, 1.2, "cloth", "pattern"),
        (-0.29, 0.245, 1.0, "cream", "thumbs"),
    ]
    pw, ph = 0.42, 0.297
    for i, (x, z, tilt, key, style) in enumerate(prints):
        rot = (0, R(tilt), 0)
        box("Moodboard_PrintPaper", (pw, 0.0008, ph), (x, front - 0.0006, z), PAPER, bevel=0.0, rot=rot, parent=root)
        loc = Vector((x, front - 0.0016, z))
        pic = hook_image("board", i + 1, (pw - 0.024, ph - 0.024), loc, rot=rot, parent=root, default_key=key)
        default_art(pic, pw - 0.024, ph - 0.024, loc, rot, root, style)
        rm = Euler(rot).to_matrix()
        for cx in (-1, 1):
            pin(loc + rm @ Vector((cx * (pw / 2 - 0.02), 0, ph / 2 - 0.015)), PAINTS[(i + cx) % 4])
    # paint sample strips (5 tones of one colour each)
    for k, ck in enumerate(("main", "accent_1", "accent_3")):
        x = 0.05 + k * 0.065
        box("Moodboard_Strip", (0.05, 0.0008, 0.2), (x, front - 0.0006, 0.27), PAPER, bevel=0.0, parent=root)
        for j in range(5):
            box("Moodboard_Chip", (0.042, 0.0008, 0.03), (x, front - 0.0014, 0.34 - j * 0.035),
                mat(ck, 0.6, color=shade(ck, 1.0 + 0.16 * j)), bevel=0.0, parent=root)
        pin((x, front, 0.36), "dark")
    # index cards with your skills (5 x 3 in)
    for k in range(4):
        x, z = 0.32 + (k % 2) * 0.14, 0.34 - (k // 2) * 0.1
        tilt = R((-3, 2, 4, -2)[k])
        box("Moodboard_Card", (0.127, 0.0008, 0.076), (x, front - 0.0006, z), PAPER, bevel=0.0, rot=(0, tilt, 0),
            parent=root)
        box("Moodboard_CardLine", (0.11, 0.0008, 0.003), (x, front - 0.0012, z + 0.026), mat(PAINTS[k], 0.6),
            bevel=0.0, rot=(0, tilt, 0), parent=root)
        hook_text("skill", k + 1, ["Illustration", "UI / UX", "Branding", "Typography"][k], 0.022,
                  (x, front - 0.002, z - 0.008), rot=(R(90), tilt, 0), material=mat("dark", 0.6), max_width=0.105,
                  parent=root, depth=0.0008)
        pin((x, front, z + 0.03), PAINTS[(k + 2) % 4])
    # two instant photos
    for k, (x, z, tilt) in enumerate(((0.42, 0.13, -4), (0.11, 0.08, 3))):
        rot = (0, R(tilt), 0)
        box("Moodboard_Photo", (0.088, 0.0008, 0.107), (x, front - 0.0006, z), mat("cream", 0.5), bevel=0.0, rot=rot,
            parent=root)
        box("Moodboard_PhotoImg", (0.079, 0.0008, 0.079), (x, front - 0.0012, z + 0.008),
            mat(("accent_3", "accent_2")[k], 0.5, color=shade(("accent_3", "accent_2")[k], 0.8)), bevel=0.0, rot=rot,
            parent=root)


PLACEHOLDERS = {
    "workbench": build_workbench, "monitor": build_monitor, "lamp": build_lamp, "easel": build_easel,
    "stool": build_stool, "cabinet": build_cabinet, "shelf": build_shelf, "plant": build_plant, "rug": build_rug,
    "wall_art": build_wall_art,
}


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


if SHOW_PLACEHOLDER_FURNITURE:
    for slot_name, build in PLACEHOLDERS.items():
        build()

# A few small stray drips on the bare boards just in front of the drop cloth, where you step off it.
for k in range(PAINT_SPLATS - PAINT_SPLATS * 3 // 4):
    x, y = random.uniform(1.3, 2.6), random.uniform(0.55, 0.82)
    splat("Floor_Splat", (x, y, FLOOR_Z + 0.0003), random.uniform(0.006, 0.016), random.choice(PAINTS))

# Studio name board above the shelf: a painted 18 mm birch-plywood panel with its layered edge showing.
SIGN_Y, SIGN_Z, SIGN_W, SIGN_H = 0.62, 2.27, 0.9, 0.42
BIRCH = wood("birch", 0.5, along="Y", color="#E3CFA8")
sign = box("Name_Sign", (0.018, SIGN_W, SIGN_H), (0.011, SIGN_Y, SIGN_Z), BIRCH, bevel=0.002)
hook_link(sign, "website")
box("Name_Sign_Paint", (0.001, SIGN_W - 0.004, SIGN_H - 0.004), (0.0205, SIGN_Y, SIGN_Z), mat("cream", 0.5), bevel=0)
plies = []
for k in range(1, 5):                                                        # dark glue lines in the ply edge
    x = 0.002 + k * 0.0036
    plies.append(((0.0006, 0.001, SIGN_H), (x, SIGN_Y - SIGN_W / 2 - 0.0002, SIGN_Z)))
    plies.append(((0.0006, SIGN_W, 0.001), (x, SIGN_Y, SIGN_Z + SIGN_H / 2 + 0.0002)))
boxes("Name_Sign_Plies", plies, mat("ply_line", 0.6, color=shade("wood", 0.6)))
for y in (SIGN_Y - 0.3, SIGN_Y + 0.3):
    cyl("Name_Sign_Screw", 0.007, 0.004, (0.022, y, SIGN_Z + 0.16), BRASS, rot=(0, R(90), 0), segs=12, bevel=0)
for k, key in enumerate(("accent_1", "accent_2", "main")):                   # three paint dabs as a little mark
    ball("Name_Sign_Dab", 0.022, (0.022, SIGN_Y - 0.36 + k * 0.036, SIGN_Z + 0.14 - (k % 2) * 0.012), mat(key, 0.4),
         scale=(0.15, 1, 1))
box("Name_Sign_Stroke", (0.001, 0.4, 0.014), (0.0215, SIGN_Y, SIGN_Z - 0.06), mat("accent_1", 0.5), bevel=0.0)
side = (R(90), 0, R(90))                                                     # text facing into the room (+X)
hook_text("name", 1, "YOUR NAME", 0.13, (0.022, SIGN_Y, SIGN_Z + 0.04), rot=side, material=mat("dark", 0.5),
          max_width=0.8, depth=0.004)
hook_text("role", 1, "your role", 0.075, (0.022, SIGN_Y, SIGN_Z - 0.13), rot=side, material=mat("dark", 0.5),
          max_width=0.76, depth=0.004)

# A finished 24x30 in canvas hung on the window wall above the plant (canvas_2).
c2w, c2h, c2y, c2z = 0.61, 0.76, 3.6, 1.98
box("Hung_Canvas", (c2w, 0.038, c2h), (0.019, c2y, c2z), surface(mat("cloth", 0.9), "fabric"), bevel=0.004,
    rot=(0, 0, R(90)))
loc2 = Vector((0.0388, c2y, c2z))
pic2 = hook_image("canvas", 2, (c2w - 0.006, c2h - 0.006), loc2, rot=(0, 0, R(90)), default_key="cloth")
default_art(pic2, c2w - 0.006, c2h - 0.006, loc2, (0, 0, R(90)), None, "still_life")

# Two blank canvases leaning against the back wall with their pine stretcher bars showing.
lean = R(10)
for k, (cx, cw, ch) in enumerate(((2.12, 0.5, 0.7), (2.15, 0.4, 0.5))):
    rot = (-lean, 0, 0)
    rm = Euler(rot).to_matrix()
    base = Vector((cx, D - 0.03 - ch * math.sin(lean) - 0.045 * k, FLOOR_Z))
    centre = base + rm @ Vector((0, 0.01, ch / 2))
    box(f"Lean_Canvas_{k}", (cw, 0.004, ch), centre + rm @ Vector((0, 0.017, 0)), surface(mat("cloth", 0.9), "fabric"),
        bevel=0.002, rot=rot)
    bars = [((cw, 0.036, 0.045), (0, 0, ch / 2 - 0.0225)), ((cw, 0.036, 0.045), (0, 0, -ch / 2 + 0.0225)),
            ((0.045, 0.036, ch), (-cw / 2 + 0.0225, 0, 0)), ((0.045, 0.036, ch), (cw / 2 - 0.0225, 0, 0)),
            ((0.04, 0.02, ch - 0.08), (0, 0.008, 0))]
    boxes(f"Lean_Stretcher_{k}", bars, PINE_V, bevel=0.002, loc=centre, rot=rot)

# A pegboard (76 x 56 cm) above the drawing board with real accessories.
PB_X, PB_Z, PB_Y = 2.9, 1.62, D - 0.018
pegboard = box("Pegboard", (0.76, 0.012, 0.56), (PB_X, PB_Y, PB_Z), mat("cream", 0.6), bevel=0.003)
slots_ = []
for row in range(13):
    for col in range(18):
        x = PB_X - 0.34 + col * 0.04 + (0.02 if row % 2 else 0)
        if x > PB_X + 0.355:
            continue
        slots_.append(((0.005, 0.001, 0.015), (x, PB_Y - 0.0062, PB_Z - 0.24 + row * 0.04)))
boxes("Pegboard_Slots", slots_, mat("shadow", 0.9, color=shade("dark", 0.6)), bevel=0)
for x in (PB_X - 0.3, PB_X + 0.3):
    box("Pegboard_Spacer", (0.03, 0.012, 0.03), (x, D - 0.006, PB_Z + 0.24), mat("cream", 0.6))
fy = PB_Y - 0.006
box("Peg_Shelf", (0.28, 0.09, 0.008), (PB_X + 0.2, fy - 0.045, PB_Z - 0.08), mat("cream", 0.5), bevel=0.002)
box("Peg_ShelfLip", (0.28, 0.006, 0.03), (PB_X + 0.2, fy - 0.088, PB_Z - 0.07), mat("cream", 0.5), bevel=0.002)
for k, key in enumerate(("dark", "main", "accent_1", "dark")):                # ink bottles on the shelf
    x = PB_X + 0.1 + k * 0.065
    cyl("Peg_Ink", 0.022, 0.06, (x, fy - 0.045, PB_Z - 0.046), GLASS, segs=16)
    cyl("Peg_InkFill", 0.02, 0.035, (x, fy - 0.045, PB_Z - 0.056), mat(key, 0.2), segs=16, bevel=0)
    cyl("Peg_InkCap", 0.013, 0.02, (x, fy - 0.045, PB_Z - 0.006), PLASTIC, segs=12)
box("Peg_Container", (0.075, 0.09, 0.08), (PB_X - 0.25, fy - 0.045, PB_Z - 0.14), mat("cream", 0.5), bevel=0.004)
for k in range(5):                                                           # pens and markers in the container
    rod("Peg_Marker", (PB_X - 0.27 + k * 0.01, fy - 0.045, PB_Z - 0.15),
        (PB_X - 0.28 + k * 0.014, fy - 0.05 + 0.004 * k, PB_Z - 0.03 + 0.012 * (k % 2)), 0.005,
        mat(PAINTS[k % 4], 0.45) if k % 2 else PLASTIC, segs=8)
for x in (PB_X - 0.1, PB_X + 0.0, PB_X - 0.2):                               # hooks
    rod("Peg_Hook", (x, fy, PB_Z + 0.16), (x, fy - 0.05, PB_Z + 0.16), 0.003, STEEL)
box("Peg_Ruler", (0.03, 0.002, 0.3), (PB_X - 0.1, fy - 0.004, PB_Z + 0.02), STEEL, bevel=0.001)
ruler_marks = [((0.008 if k % 5 else 0.014, 0.0005, 0.0012), (PB_X - 0.111, fy - 0.0055, PB_Z + 0.16 - k * 0.01))
               for k in range(29)]
boxes("Peg_RulerMarks", ruler_marks, PLASTIC)
tube("Peg_ScissorRing_A", ring_pts((PB_X + 0.0, fy - 0.01, PB_Z + 0.13), 0.022, 16, axis="Y"), 0.004,
     mat("accent_1", 0.4), closed=True)
tube("Peg_ScissorRing_B", ring_pts((PB_X + 0.038, fy - 0.012, PB_Z + 0.13), 0.022, 16, axis="Y"), 0.004,
     mat("accent_1", 0.4), closed=True)
beam("Peg_ScissorBlade", (PB_X + 0.02, fy - 0.014, PB_Z + 0.105), (PB_X + 0.022, fy - 0.014, PB_Z - 0.02),
     (0.014, 0.002), STEEL, bevel=0.001)
cyl("Peg_Tape", 0.036, 0.02, (PB_X - 0.2, fy - 0.03, PB_Z + 0.13), tape_m(), rot=(R(90), 0, 0), segs=24)
cyl("Peg_TapeCore", 0.022, 0.021, (PB_X - 0.2, fy - 0.03, PB_Z + 0.13), KRAFT, rot=(R(90), 0, 0), segs=20)
box("Peg_Clip", (0.04, 0.012, 0.02), (PB_X + 0.25, fy - 0.006, PB_Z + 0.2), mat("dark", 0.4), bevel=0.002)
box("Peg_Swatch", (0.1, 0.001, 0.14), (PB_X + 0.25, fy - 0.004, PB_Z + 0.12), PAPER, bevel=0)
for j, key in enumerate(PAINTS):
    box("Peg_SwatchChip", (0.085, 0.0008, 0.025), (PB_X + 0.25, fy - 0.005, PB_Z + 0.165 - j * 0.03), mat(key, 0.6),
        bevel=0)

# A three-tier steel trolley of art supplies parked by the easel (35 x 45 x 78 cm).
cart = bpy.data.objects.new("Art_Trolley", None)
cart.location, cart.rotation_euler = (1.25, 1.2, FLOOR_Z), (0, 0, R(70))
COL_ROOM.objects.link(cart)
cart_m = powder("main", 0.42, along="Z")
CW, CD = 0.45, 0.35
post_x, post_y = CW / 2 - 0.012, CD / 2 - 0.012
for sx in (-1, 1):
    for sy in (-1, 1):
        rod("Trolley_Post", (sx * post_x, sy * post_y, 0.07), (sx * post_x, sy * post_y, 0.74), 0.009, cart_m,
            parent=cart, segs=12)
        cyl("Trolley_CastorWheel", 0.024, 0.018, (sx * post_x, sy * post_y, 0.024), RUBBER, rot=(0, R(90), 0), segs=16,
            parent=cart)
        box("Trolley_CastorFork", (0.026, 0.03, 0.03), (sx * post_x, sy * post_y, 0.05), STEEL, bevel=0.003,
            parent=cart)
    tube("Trolley_Handle", bezier((sx * post_x, -post_y, 0.74), (sx * post_x, 0, 0.82), (sx * post_x, post_y, 0.74), 12),
         0.009, cart_m, parent=cart)
for k, z in enumerate((0.1, 0.38, 0.64)):                                    # three deep trays
    box("Trolley_TrayBottom", (CW - 0.01, CD - 0.01, 0.004), (0, 0, z), cart_m, bevel=0.002, parent=cart)
    for sy in (-1, 1):
        box("Trolley_TrayWall", (CW - 0.01, 0.006, 0.09), (0, sy * (CD / 2 - 0.008), z + 0.045), cart_m, bevel=0.003,
            parent=cart)
    for sx in (-1, 1):
        box("Trolley_TrayWall", (0.006, CD - 0.01, 0.09), (sx * (CW / 2 - 0.008), 0, z + 0.045), cart_m, bevel=0.003,
            parent=cart)
        box("Trolley_Grip", (0.004, 0.09, 0.022), (sx * (CW / 2 - 0.0115), 0, z + 0.06),
            mat("shadow", 0.9, color=shade("dark", 0.6)), bevel=0.008, parent=cart)
tz = 0.644
pal = flat("Trolley_Palette", [(0.16 * math.cos(a) * (1 - 0.18 * math.cos(a * 2 + 0.6)), 0.11 * math.sin(a))
                               for a in (k * math.pi / 14 for k in range(28))], wood("wood", 0.5),
           loc=(-0.06, 0.0, tz + 0.004), parent=cart, thick=0.006)
cyl("Trolley_PaletteHole", 0.016, 0.0065, (-0.17, 0.02, tz + 0.0075), mat("shadow", 0.9, color=shade("dark", 0.6)),
    segs=16, bevel=0, parent=cart)
for k, key in enumerate(PAINTS + ["cream", "dark"]):
    a = R(30 + k * 40)
    ball("Trolley_Dab", 0.017, (-0.04 + math.cos(a) * 0.1, math.sin(a) * 0.07, tz + 0.012), mat(key, 0.25),
         scale=(1, 0.85, 0.35), parent=cart)
for k, key in enumerate(("accent_2", "accent_3", "dark")):
    paint_tube(f"Trolley_Tube_{k}", (0.15, -0.1 + k * 0.06, tz + 0.02), key, turn=90 + 10 * k, parent=cart)
cyl("Trolley_BrushPot", 0.035, 0.1, (0.15, 0.11, tz + 0.05), ceramic("cream", 0.3), segs=20, parent=cart)
for k in range(5):
    a = k * 1.25
    brush(f"Trolley_Brush_{k}", (0.15 + math.cos(a) * 0.01, 0.11 + math.sin(a) * 0.01, tz + 0.01),
          (0.15 + math.cos(a) * 0.04, 0.11 + math.sin(a) * 0.035, tz + 0.27 + 0.02 * (k % 2)), PAINTS[k % 4],
          parent=cart)
for k in range(6):                                                           # gouache jars on the middle tray
    key = PAINTS[k % 4]
    jx, jy = -0.15 + (k % 3) * 0.075, -0.06 + (k // 3) * 0.075
    cyl("Trolley_Jar", 0.028, 0.05, (jx, jy, 0.38 + 0.027), GLASS, segs=16, parent=cart)
    cyl("Trolley_JarPaint", 0.025, 0.035, (jx, jy, 0.38 + 0.02), mat(key, 0.3), segs=16, bevel=0, parent=cart)
    cyl("Trolley_JarLid", 0.029, 0.012, (jx, jy, 0.38 + 0.058), PLASTIC, segs=16, parent=cart)
for k, key in enumerate(("main", "accent_1", "cream")):                      # sketchbooks on the middle tray
    box("Trolley_Book", (0.15, 0.21, 0.015), (0.12, 0.0, 0.392 + k * 0.016), mat(key, 0.7), bevel=0.002,
        rot=(0, 0, R(4 * k - 3)), parent=cart)
cyl("Trolley_Tin", 0.055, 0.11, (-0.1, 0.0, 0.1 + 0.057), STEEL, segs=24, parent=cart)
cyl("Trolley_TinLabel", 0.0555, 0.06, (-0.1, 0.0, 0.1 + 0.05), mat("accent_3", 0.6), segs=24, bevel=0, parent=cart)
rag("Trolley_Rag", (0.11, 0.0, 0.103), (0.18, 0.16), surface(mat("cloth", 0.95), "fabric"), turn=-10,
    parent=cart, lift=0.04)

# Reading corner: an IKEA POÄNG-style armchair (68 x 82 x 100 cm, seat 42 cm) in bent birch veneer, with
# its thick cushion and a knit throw over the back. Each side frame is ONE bent strip: a floor runner that
# curves up at the front into the leg and back into the armrest; the seat/back shell hangs between them.
chair = bpy.data.objects.new("Reading_Chair", None)
chair.location, chair.rotation_euler = (3.72, 1.0, FLOOR_Z), (0, 0, R(-28))
COL_ROOM.objects.link(chair)
birch = wood("birch_chair", 0.45, color=shade("wood", 1.12))
side_path = (bezier((0, 0.34, 0.028), (0, 0.0, 0.028), (0, -0.28, 0.03), 6)[:-1]
             + bezier((0, -0.28, 0.03), (0, -0.4, 0.04), (0, -0.37, 0.24), 6)[:-1]
             + bezier((0, -0.37, 0.24), (0, -0.34, 0.6), (0, -0.16, 0.58), 8)[:-1]
             + bezier((0, -0.16, 0.58), (0, 0.08, 0.57), (0, 0.27, 0.49), 6))
for sx in (-1, 1):
    ribbon("Chair_SideFrame", [p + Vector((sx * 0.315, 0, 0)) for p in side_path], 0.026, 0.05, birch, parent=chair)
for y, z in ((-0.36, 0.3), (0.33, 0.06)):                                    # front and rear cross rails
    box("Chair_CrossRail", (0.6, 0.04, 0.05), (0, y, z), birch, parent=chair)
for sx in (-1, 1):                                                           # where the arms bolt to the back
    box("Chair_Joint", (0.05, 0.05, 0.045), (sx * 0.29, 0.262, 0.47), birch, parent=chair)
shell = bezier((0, -0.32, 0.44), (0, -0.05, 0.37), (0, 0.17, 0.39), 8)[:-1] + \
    bezier((0, 0.17, 0.39), (0, 0.34, 0.5), (0, 0.42, 0.98), 10)
for sx in (-1, 1):                                                           # seat / back rails
    ribbon("Chair_ShellRail", [p + Vector((sx * 0.27, 0, -0.03)) for p in shell], 0.022, 0.045, birch, parent=chair)
cushion_m = surface(mat("cushion", 0.9, color=mix_hex(COLORS["cloth"], COLORS["dark"], 0.18)), "fabric")
pad = ribbon("Chair_Cushion", [p + Vector((0, 0, 0.03)) for p in shell], 0.55, 0.075, cushion_m, parent=chair)
pbev = pad.modifiers.new("Bevel", "BEVEL")
pbev.width, pbev.segments, pbev.limit_method = 0.022, 3, "ANGLE"
pad.data.polygons.foreach_set("use_smooth", [True] * len(pad.data.polygons))
seam_m = mat("seam", 0.9, color=mix_hex(COLORS["cloth"], COLORS["dark"], 0.35))
for i in (8, 12, 15):                                                         # quilted cross seams on the pad
    p, q = Vector(shell[i]), Vector(shell[i + 1])
    nrm = Vector((1, 0, 0)).cross(q - p).normalized()
    c = p + Vector((0, 0, 0.03)) + nrm * 0.039
    rod("Chair_Seam", c - Vector((0.25, 0, 0)), c + Vector((0.25, 0, 0)), 0.004, seam_m, parent=chair, segs=8)
# A folded knit throw hung over the top of the back: it lies on the cushion's front face, wraps round the
# top edge and hangs down behind, following the pad instead of standing off it.
pad_pts, pad_nrm = [], []
for i in range(12, len(shell)):
    t = (Vector(shell[min(i + 1, len(shell) - 1)]) - Vector(shell[i - 1])).normalized()
    pad_pts.append(Vector(shell[i]) + Vector((0, 0, 0.03)))
    pad_nrm.append(Vector((1, 0, 0)).cross(t).normalized())          # points out of the cushion's front
top_t = (pad_pts[-1] - pad_pts[-2]).normalized()
off = 0.0375 + 0.007                                                  # half the pad + half the throw
throw_path = [p + n * off for p, n in zip(pad_pts, pad_nrm)]
throw_path += [pad_pts[-1] + pad_nrm[-1] * off * math.cos(a) + top_t * off * math.sin(a)
               for a in (math.pi * k / 6 for k in range(1, 6))]       # round the top edge
throw_path += [p - n * off for p, n in zip(pad_pts[::-1], pad_nrm[::-1])][:5]
throw = ribbon("Chair_Throw", throw_path, 0.42, 0.012, surface(mat("throw", 0.95, color=shade("accent_2", 0.85)),
               "knit"), parent=chair)
throw.location.x = -0.06
tbev = throw.modifiers.new("Bevel", "BEVEL")
tbev.width, tbev.segments, tbev.limit_method = 0.005, 2, "ANGLE"
throw.data.polygons.foreach_set("use_smooth", [True] * len(throw.data.polygons))

# A steel tray table beside the armchair, at its back corner (IKEA GLADOM type: 45 cm tray with a 4 cm rim, 53 cm high, four
# tube legs that splay out to the floor), holding a coffee and a couple of art books.
tt = bpy.data.objects.new("Tray_Table", None)
tt.location = (4.15, 1.5, FLOOR_Z)
COL_ROOM.objects.link(tt)
tray_m = powder("dark", 0.4)
TR, TZ = 0.225, 0.49
cyl("TrayTable_Tray", TR, 0.004, (0, 0, TZ + 0.002), tray_m, segs=40, bevel=0.0015, parent=tt)
lathe("TrayTable_Rim", [(TR - 0.002, TZ), (TR, TZ + 0.04)], tray_m, segs=40, parent=tt)
tube("TrayTable_RimBead", ring_pts((0, 0, TZ + 0.04), TR, 40), 0.004, tray_m, closed=True, parent=tt)
for k in range(4):
    a = R(45 + 90 * k)
    top, foot = Vector((math.cos(a) * 0.14, math.sin(a) * 0.14, TZ)), Vector((math.cos(a) * 0.2, math.sin(a) * 0.2, 0.01))
    rod("TrayTable_Leg", foot, top, 0.009, tray_m, parent=tt)
    cyl("TrayTable_Foot", 0.011, 0.01, foot - Vector((0, 0, 0.005)), RUBBER, segs=12, parent=tt)
tube("TrayTable_Ring", ring_pts((0, 0, TZ - 0.012), 0.141, 32), 0.006, tray_m, closed=True, parent=tt)
for k, (key, t) in enumerate((("accent_3", 0.022), ("cream", 0.016))):
    box("TrayTable_Book", (0.2, 0.26, t), (-0.04, 0.01, TZ + 0.004 + t / 2 + k * 0.022), mat(key, 0.7),
        bevel=0.002, rot=(0, 0, R(12 - 20 * k)), parent=tt)
mug("TrayTable_Mug", (0.13, -0.1, TZ + 0.004), ceramic("accent_1", 0.25), turn=-90, parent=tt)

# A tall bin of rolled paper in the corner beside the drafting table.
cyl("PaperBin", 0.11, 0.42, (4.25, D - 0.16, FLOOR_Z + 0.21), powder("dark", 0.5, along="Z"), segs=28)
for k in range(6):
    a = k * 1.05
    top = Vector((4.25 + math.cos(a) * 0.07, D - 0.16 + math.sin(a) * 0.05, FLOOR_Z + 0.7 + 0.1 * (k % 3)))
    rod("PaperRoll", (4.25 + math.cos(a) * 0.05, D - 0.16 + math.sin(a) * 0.04, FLOOR_Z + 0.05), top, 0.03,
        mat(["cream", "sky", "cloth", "accent_2", "cream", "cloth"][k], 0.8), segs=16)

# A framed print with a white mount on the brick wall above the computer (30 x 40 cm frame).
fr_x, fr_z = 3.82, 2.12
box("Frame_Print", (0.3, 0.02, 0.4), (fr_x, D - 0.01, fr_z), mat("dark", 0.5), bevel=0.003)
box("Frame_Mount", (0.26, 0.002, 0.36), (fr_x, D - 0.021, fr_z), mat("cream", 0.7), bevel=0)
box("Frame_Art", (0.18, 0.002, 0.25), (fr_x, D - 0.0225, fr_z), mat("cream", 0.8), bevel=0)
default_art(None, 0.18, 0.25, (fr_x, D - 0.0235, fr_z), (0, 0, 0), None, "still_life", name="Frame_Print")


# =====================================================================
#  LIGHTS, WORLD, CAMERA, RENDER
# =====================================================================
# Daylight through the north window, a big soft window glow, a fill from the camera side and the
# desk lamp. In the "studio_night" theme the sun becomes dim moonlight and the lamp does the work.
sun_k = 9000 if NIGHT else SUN_WARMTH
sun_dir = Vector((1.0, -0.45, -0.55))               # low sun: only the window lets it in, so the
sun_aim = Vector((3.0, 0.82, 0.0))                   # window grid draws a slanted patch on the floor
light("Light_Sun", "SUN", SUN_STRENGTH * (0.25 if NIGHT else 1.0), kelvin(sun_k), sun_aim - sun_dir * 6,
      aim=sun_aim, size=R(1.5))
light("Light_Window", "AREA", 50 if NIGHT else 95, kelvin(9000 if NIGHT else 6500), (0.25, wy, wz),
      aim=(2.2, wy - 0.3, 0.2), size=1.6)            # aimed down at the easel so it does not wash the brick wall
light("Light_Fill", "AREA", (70 if NIGHT else 180) * (W * D / 16), kelvin(5000 if NIGHT else 6000),
      (W + 3, -3, H + 2.5), aim=(W / 2, D / 2, 0.6), size=6)
lamp_slot = SLOTS["lamp"]
# The desk lamp is a wide spot inside the shade, so it pools light on the board instead of burning the wall.
lamp_at, lamp_aim = LAMP_LIGHT_AT or (lamp_slot.location + Vector((0, 0, lamp_slot["kit_size"][2] * 0.3)),
                                      Vector((0, 0, -1)))
lamp_light = light("Light_Lamp", "SPOT", LAMP_STRENGTH * (4 if NIGHT else 1.2), kelvin(LAMP_WARMTH), lamp_at,
                   aim=lamp_at + lamp_aim, size=0.04)
lamp_light.data.spot_size, lamp_light.data.spot_blend = R(120), 0.7
light("Light_Bounce", "AREA", 70 if NIGHT else 40, kelvin(3200 if NIGHT else 6000), (W / 2, D / 2, H - 0.1),
      aim=(W / 2, D / 2, 0), size=2.5)

# World: the camera sees the flat background colour; the room is lit by a soft cool ambient.
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
bg_amb.inputs["Color"].default_value = (*kelvin(8000 if NIGHT else 6500), 1)
bg_amb.inputs["Strength"].default_value = 0.2 if NIGHT else 0.4
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
                    ("shadow_ray_count", 2), ("use_gtao", True), ("gtao_distance", 0.4),
                    ("use_soft_shadows", True)):
    if hasattr(ee, attr):
        setattr(ee, attr, value)
if hasattr(ee, "ray_tracing_options"):
    ee.ray_tracing_options.resolution_scale = "2" if "2" in [i.identifier for i in
        type(ee.ray_tracing_options).bl_rna.properties["resolution_scale"].enum_items] else ee.ray_tracing_options.resolution_scale
scene.view_settings.view_transform = "Standard"   # keeps your hex colours exactly as typed
scene.view_settings.exposure = 0.0 if NIGHT else -0.3

# Remember the style so add_furniture.py can match colours later.
scene["kit_style"] = STYLE
scene["kit_version"] = KIT_VERSION
scene["kit_palette"] = json.dumps(COLORS)
scene["kit_material_finish"] = json.dumps({"roughness": 0.5, "bevel": 0.004, "saturation": 0.8})
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
