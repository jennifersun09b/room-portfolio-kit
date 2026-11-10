"""
3D ROOM PORTFOLIO KIT  -  Template: HILLSIDE HEARTH COTTAGE (hand-painted countryside cottage)
=============================================================================================
Builds a little timber-and-plaster cottage kitchen sitting in a mossy hillside meadow: an inglenook hearth with a
cast-iron stove and a copper kettle, herbs drying from the oak beam, a scrubbed-pine breakfast table under a paper
lantern, a round window with lace curtains and a window seat, a ladder up to a loft bed with a patchwork quilt,
an old tree growing up through the corner, a shingle roof edge covered in moss, and laundry blowing on a line
outside. It renders a 1920x1080 image.
Your name and role are burnt into the sign-board over the hearth; your projects are the framed watercolours on the
chimney breast, the picture by the door and the open sketchbook on the table. The letterbox emails you.

HOW TO RUN
  Option A (no Blender UI):   blender -b -P hearth_cottage.py
  Option B (inside Blender):  Scripting tab > Open > hearth_cottage.py > Run Script (then F12 to render)

You only need to edit the SETTINGS block below. Everything under it builds the room.
Output: output/hearth_cottage.png and output/hearth_cottage.blend next to this script.
"""
# REFERENCES  (what each piece is modelled on; brand names appear only here and in research/hearth_cottage.md)
#   stove          Morsø 1410-type small cast-iron box stove (plain sides): W39 D37 H55 cm, 125 mm flue
#                  https://morsoe.com/en/product/indoor/multifuel/p1410_uk
#   kettle         2.1 L stovetop whistling kettle (Traditional kettle proportions), in copper: L27 W21 H25 cm
#                  https://prezola.com/product/le-creuset-kettle-504959
#   hearth         inglenook: limewashed breast 140 x 52 cm, opening 100 x 112 cm, oak bressummer 156 x 27 x 22 cm
#   table          scrubbed-pine farmhouse table (Karup pine table / Derwent): L120 W75 H76 cm, 35 mm top
#                  https://www.karupdesign.com/en/product/611
#                  https://funky-chunky-furniture.co.uk/products/derwent-dining-table
#   chair          bow-back spindle Windsor side chair: W46 D50 H90 cm, seat 45 cm
#                  https://www.dutchcrafters.com/Amish-Econo-Solid-Wood-Windsor-Dining-Chair/p/62135
#   ladder-back    painted rush-seat ladder-back country chair (decor): W46 D44 H98 cm, seat 45 cm
#   window_seat    built-in window seat with lift-up lid: L130 D50 H48 cm
#                  https://designingidea.com/window-seat-dimensions
#   pendant_lamp   rice-paper globe lantern (IKEA REGOLIT type): dia 45 cm, about 0.75 m above the table
#                  https://www.ikea.com/ca/en/p/regolit-pendant-lamp-shade-white-handmade-70103410
#   bed            UK single mattress 90 x 190 x 18 cm on a low pine platform, patchwork quilt 135 x 200 cm
#                  https://www.silentnight.co.uk/guides/bed-mattress-size-guide
#   loft ladder    fixed loft ladder: 40 cm wide, rungs 28 cm apart, deck at 1.95 m
#                  https://www.fakro.ca/att/LOCAL/products/LWT.pdf
#   wall_shelf     pine jar shelf 80 x 24 x 72 cm; Weck 580 ml mould jar H10.5 dia 10 cm; jam jars dia 7 H9 cm
#                  https://admin.drinkstuff.com/products/ehint.asp?ID=35615
#   sink (decor)   fireclay Belfast butler sink 595 x 455 x 255 mm in a 90 cm painted base unit
#                  https://www.victorianplumbing.co.uk/reginox-butler-classic-600-ceramic-kitchen-sink
#   rug            oval hand-braided rag rug 120 x 180 cm
#                  https://www.wayfair.co.uk/rugs/pdp/bay-isle-home-gemini-hand-braided-beige-jute-rug-u003163329.html
#   door (decor)   cottage stable door, framed ledged & braced: 2032 x 813 x 44 mm
#                  https://travisperkins.co.uk/external-softwood-doors/plaut-redwood-framed-ledged-braced-door-2032-x-813-x-44mm/p/362101
#   letterbox      post-mounted wooden letterbox, box 36 x 26 x 24 cm on a 1.05 m post (email link)
#                  https://www.diy.com/departments/burg-wachter-aire-wall-mounted-black-lockable-weatherproof-post-box-37x36x11cm/5016567024019_BQ.prd
#   washing line   timber posts, line about 1.8 m high
#                  https://www.theclotheslinestore.com.au/blogs/news/how-high-to-install-a-clothesline
#   pet            ginger tabby asleep in a round wicker basket (dia 48 cm)
#   floor          wide pine floorboards, 18 cm boards in random lengths
#   name board     carved pine kitchen sign-board 124 x 40 x 2.8 cm on two iron hooks (name + role hooks)
#   rag rug        striped hand-woven cotton rag rug with tassels, 80 x 150 cm (decor)
#                  https://beliani.no/cotton-area-rug-80-x-150-cm-multicolour-hisarli.html
#   apple crate    slatted wooden fruit / apple crate 50 x 40 x 30 cm (decor)
#                  https://www.heavins.ie/products/natural-fruit-crate-50x40x30cm-apple-crate
#   lavender pot   'Hidcote' lavender in a 37 cm terracotta pot (H 32 cm), plant about 45 cm tall
#                  https://www.burford.co.uk/collections/lavender/products/lavender-ang-hidcote-26cm

# =====================================================================
#  SETTINGS  -  change these lines, then run the script again
# =====================================================================
ROOM_NAME = "hearth_cottage"        # used for the output file names

ROOM_WIDTH = 4.6                    # metres, left to right (along the back wall)
ROOM_DEPTH = 4.0                    # metres, front to back (along the left wall)
WALL_HEIGHT = 3.0                   # metres, from the meadow to the top of the walls

THEME = "summer_afternoon"          # pick one of the colour themes below
THEMES = {                          # any hex colour works; "main" is the room's hero colour (sage)
    # "summer_afternoon": cream limewash, honey pine, sage paint, tomato-red and sky-blue cloth, bright meadow.
    "summer_afternoon": {
        "background": "#BFDCEA", "wall": "#F4ECDA", "wall_trim": "#E6D8BD", "floor": "#C8975E", "floor_2": "#B8884F",
        "wood": "#E0B57A", "main": "#9AB48A", "accent_1": "#D2664A", "accent_2": "#F0C45C", "accent_3": "#7FB0D8",
        "cream": "#FBF5E8", "plant": "#6E9B45", "dark": "#2F2B29", "timber": "#7E5638", "chimney": "#F0E5CF",
        "brick": "#B86B4B", "stone": "#BDB6A6", "slate": "#5E6367", "copper": "#C77A45", "brass": "#C9A14E",
        "clay": "#C9774F", "sky": "#D2ECF7", "grass": "#8CBF4E", "moss": "#6E9A3A", "earth": "#7A5638",
        "leaf": "#5E9A3E", "bark": "#6B5442", "shingle": "#8C6F55", "cloud": "#FFFFFF", "lantern": "#FFF1D6",
        "fire": "#FF8A2A", "cat": "#E08A3E", "glass": "#E8F4F6",
    },
    # "rainy_lantern": a rainy blue evening - the stove glows, the paper lantern and fairy lights are lit.
    # Uses its own lights (see "LIGHTS" near the end: RAINY switches sun, fill, lantern and stove).
    "rainy_lantern": {
        "background": "#33435A", "wall": "#EADDC3", "wall_trim": "#D6C5A5", "floor": "#B5875A", "floor_2": "#A47A4E",
        "wood": "#D4A56C", "main": "#88A27C", "accent_1": "#C85E46", "accent_2": "#E8B653", "accent_3": "#6F9CC4",
        "cream": "#F6EEDD", "plant": "#5E8A40", "dark": "#2A2726", "timber": "#6E4B32", "chimney": "#E4D7BE",
        "brick": "#A85E43", "stone": "#9EA0A0", "slate": "#4F555B", "copper": "#C27443", "brass": "#C69B48",
        "clay": "#B96C48", "sky": "#5C7594", "grass": "#5E8C45", "moss": "#557D35", "earth": "#5E4430",
        "leaf": "#487A3A", "bark": "#594637", "shingle": "#6E5A49", "cloud": "#8E9CB0", "lantern": "#FFD9A0",
        "fire": "#FF7A1E", "cat": "#D9823A", "glass": "#B9CBDA",
    },
}

SUN_WARMTH = 4600                   # Kelvin: 2500 = sunset orange, 6500 = white daylight (4600 = warm afternoon)
SUN_STRENGTH = 4.2                  # the rainy theme uses a dim, cool sky instead
LAMP_WARMTH = 2300                  # Kelvin of the paper lantern, the fairy lights and the candles
LAMP_STRENGTH = 30                  # Watts in the paper lantern (rainy theme; it is only softly lit in summer)
STOVE_GLOW = 1.0                    # 0 = stove out, 1 = normal fire, 2 = roaring
FAIRY_LIGHTS = True                 # string of warm lights along the loft railing
LAUNDRY = True                      # washing line with a sheet and tea towels outside the cottage
CLOUDS = True                       # soft cumulus clouds in the background sky
SEED = 11                           # change to shuffle jars, herbs, quilt squares, grass and flowers

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
RAINY = THEME == "rainy_lantern"    # evening theme: rain outside, lantern + stove + candles lit

STYLE = "hearth_cottage"
KIT_VERSION = 2
W, D, H = ROOM_WIDTH, ROOM_DEPTH, WALL_HEIGHT
T = 0.15            # wall thickness
FLOOR_Z = 0.16      # top of the floorboards (the cottage stands on a stone plinth above the meadow)
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


def kelvin(k):
    """Colour temperature -> linear RGB (Tanner Helland approximation)."""
    t = k / 100.0
    r = 255 if t <= 66 else 329.698727446 * ((t - 60) ** -0.1332047592)
    g = 99.4708025861 * math.log(t) - 161.1195681661 if t <= 66 else 288.1221695283 * ((t - 60) ** -0.0755148492)
    b = 255 if t >= 66 else (0 if t <= 19 else 138.5177312231 * math.log(t - 10) - 305.0447927307)
    rgb = [max(0.0, min(255.0, v)) / 255 for v in (r, g, b)]
    return tuple(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb)


def shade(hex_color, f):
    """Lighter (f > 1) or darker (f < 1) version of a hex colour."""
    h = hex_color.lstrip("#")
    return "#" + "".join(f"{max(0, min(255, round(int(h[i:i + 2], 16) * f))):02X}" for i in (0, 2, 4))


def mix_hex(a, b, t):
    """Blend two hex colours (t = 0 -> a, t = 1 -> b)."""
    a, b = a.lstrip("#"), b.lstrip("#")
    return "#" + "".join(f"{round(int(a[i:i + 2], 16) * (1 - t) + int(b[i:i + 2], 16) * t):02X}" for i in (0, 2, 4))


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


def mat(key, rough=0.6, emit=0.0, metal=0.0, color=None, alpha=1.0):
    """Material from a COLORS key (or a hex via color=). alpha < 1 makes see-through glass."""
    hex_color = color or COLORS[key]
    name = f"M_{key}_{rough}_{emit}_{metal}_{hex_color}_{alpha}"
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
    if alpha < 1.0:                      # glass: simple transparency works in every Eevee version
        _set(b, ["Alpha"], alpha)
        if hasattr(m, "surface_render_method"):
            m.surface_render_method = "BLENDED"
        elif hasattr(m, "blend_method"):
            m.blend_method = "BLEND"
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


def M(key, rough, kind=None, along="X", scale=1.0, **kw):
    """Palette material + real surface detail. Different 'along' needs a different roughness (cache key)."""
    m = mat(key, rough, **kw)
    return surface(m, kind, scale=scale, along=along) if kind else m


def gingham(key, check=0.009):
    """Gingham check cloth: stripes of the colour in both directions over cream, so there are three tones like
    real gingham (white, half and full colour). The colour stays in KIT_BASE so themes and brand_color work."""
    m = mat(key, 0.913)
    if m.get("kit_surface"):
        return m
    nt, b = m.node_tree, _principled(m)
    base = nt.nodes.new("ShaderNodeRGB")
    base.name = base.label = "KIT_BASE"
    base.outputs[0].default_value = lin(COLORS[key])
    co, sep = nt.nodes.new("ShaderNodeTexCoord"), nt.nodes.new("ShaderNodeSeparateXYZ")
    nt.links.new(co.outputs["Object"], sep.inputs[0])

    def op(kind, a, b_):
        n = nt.nodes.new("ShaderNodeMath")
        n.operation = kind
        for i, v in enumerate((a, b_)):
            if isinstance(v, (int, float)):
                n.inputs[i].default_value = v
            else:
                nt.links.new(v, n.inputs[i])
        return n.outputs[0]

    def stripe(v):
        return op("GREATER_THAN", op("FRACT", op("MULTIPLY", v, 1 / (2 * check)), 0), 0.5)
    tone = op("MULTIPLY", op("ADD", stripe(sep.outputs["X"]), stripe(op("ADD", sep.outputs["Y"], sep.outputs["Z"]))),
              0.5)
    mix = nt.nodes.new("ShaderNodeMix")
    mix.data_type, mix.blend_type = "RGBA", "MIX"
    nt.links.new(tone, mix.inputs[0])
    mix.inputs[6].default_value = lin(COLORS["cream"])
    nt.links.new(base.outputs[0], mix.inputs[7])
    nt.links.new(mix.outputs[2], b.inputs["Base Color"])
    b.inputs["Roughness"].default_value = 0.9
    m["kit_surface"] = "gingham"
    return m


# The cottage's real materials (one place, so every piece uses the same pine, oak, iron, copper...).
PINE = M("wood", 0.55, "wood")                      # honey pine: shelves, bed, ladder, frames
PINE_V = M("wood", 0.56, "wood", along="Z")         # vertical grain: legs, uprights, spindles
PINE_Y = M("wood", 0.57, "wood", along="Y")         # grain along y
SCRUB = M("scrub", 0.8, "wood", color=mix_hex(COLORS["wood"], COLORS["cream"], 0.35))   # scrubbed pale table top
TIMBER = M("timber", 0.7, "wood")                   # old oak beams and posts
TIMBER_V = M("timber", 0.71, "wood", along="Z")
TIMBER_Y = M("timber", 0.72, "wood", along="Y")
FLOOR_A = M("floor", 0.62, "wood")                  # floorboards (two tones)
FLOOR_B = M("floor_2", 0.62, "wood")
PLASTER = M("wall", 0.92, "plaster")                # limewashed walls
LIME = M("chimney", 0.9, "plaster", scale=1.5)      # limewashed chimney breast
TRIM = M("wall_trim", 0.6, "plaster", scale=3)      # painted window frame and seat
SAGE_PAINT = M("main", 0.55, "plaster", scale=3)    # painted kitchen base and ladder-back chair
DOOR_PAINT = M("accent_3", 0.5, "wood", along="Z")  # painted door boards (grain shows through)
BRICK_X = M("brick", 0.85, "brick", along="X")      # brick-lined inglenook (back), chimney stack
BRICK_Y = M("brick", 0.86, "brick", along="Y")      # brick-lined inglenook (sides)
STONE_X = M("stone", 0.85, "brick", scale=0.5, along="X")   # rubble-stone plinth (big blocks)
STONE_Y = M("stone", 0.86, "brick", scale=0.5, along="Y")
FLAG = M("slate", 0.7, "concrete", scale=2)         # flagstone hearth, stepping stones
IRON = M("dark", 0.55, "brushed", metal=0.6)        # cast iron
COPPER = M("copper", 0.25, "brushed", metal=1.0)
BRASS = M("brass", 0.3, "brushed", metal=1.0)
LINEN = M("cream", 0.9, "fabric")
FABRIC = M("main", 0.9, "fabric")                   # sage window-seat cushion
KNIT = M("cream", 0.95, "knit")
KNIT_HONEY = M("accent_2", 0.95, "knit")
RUSH = M("rush", 0.9, "knit", scale=2, color=mix_hex(COLORS["accent_2"], COLORS["wood"], 0.6))   # woven rush / wicker
CERAMIC = M("cream", 0.3, "ceramic")
CLAY = M("clay", 0.8, "concrete", scale=3)          # terracotta pots, chimney pot
PAPER = M("cream", 0.8, "paper")
LACE = surface(mat("lace", 0.9, color=COLORS["cream"], alpha=0.8), "fabric")
GLASS = mat("glass", 0.05, alpha=0.2)
WIN_GLASS = mat("glass", 0.04, alpha=0.1)
SOIL = mat("soil", 0.95, color="#3A2A20")
EARTH = M("earth", 0.95, "concrete", scale=2)
TURF = M("grass", 0.9, "knit", scale=0.4)
GRASS = mat("grass", 0.75)
GRASS_DARK = mat("grass", 0.76, color=shade(COLORS["grass"], 0.72))
MOSS = M("moss", 0.95, "knit", scale=0.6)
MOSS_LIGHT = M("moss", 0.96, "knit", scale=0.6, color=mix_hex(COLORS["moss"], COLORS["grass"], 0.55))
BARK = M("bark", 0.9, "wood", along="Z", scale=0.6)
LEAF_1 = mat("leaf", 0.7)
LEAF_2 = mat("leaf", 0.71, color=mix_hex(COLORS["leaf"], COLORS["grass"], 0.5))
LEAF_3 = mat("leaf", 0.72, color=shade(COLORS["leaf"], 0.72))
SHINGLE = M("shingle", 0.85, "wood")
CAT = M("cat", 0.95, "knit", scale=0.4)
CAT_STRIPE = mat("cat", 0.96, color=shade(COLORS["cat"], 0.68))
FIRE = mat("fire", 0.5, emit=6.0 * max(STOVE_GLOW, 0.05))
EMBER = mat("ember", 0.5, emit=10.0 * max(STOVE_GLOW, 0.05), color="#FFD27A")
LANTERN = M("lantern", 0.8, "paper", emit=1.5 if RAINY else 0.1)
BULB = mat("bulb", 0.3, emit=14.0 if RAINY else 3.0, color="#FFD58A")
CANDLE = mat("cream", 0.5, color=mix_hex(COLORS["cream"], "#F3E2B8", 0.5))
FLAME = mat("flame", 0.3, emit=14.0, color="#FFC870")
INK = mat("dark", 0.7, color=shade(COLORS["timber"], 0.45))   # burnt-in letters, pencil lines


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
    """Box with a small real-furniture bevel. size = (x, y, z) in metres, loc = centre."""
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=Vector(size), verts=bm.verts)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, min(bevel, min(size) * 0.45), coll, parent)


def boxes(name, parts, material, bevel=0.003, parent=None, segs=2):
    """MANY boxes merged into one object (fast for floorboards, shingles, stems). parts = [(size, loc, rot)]."""
    bm = bmesh.new()
    for size, loc, rot in parts:
        verts = bmesh.ops.create_cube(bm, size=1.0)["verts"]
        bmesh.ops.transform(bm, matrix=Matrix.LocRotScale(Vector(loc), Euler(rot), Vector(size)), verts=verts)
    o = _finish(_obj(name, bm), material, bevel, None, parent, segs)
    if not bevel:
        o.data.polygons.foreach_set("use_smooth", [False] * len(o.data.polygons))
    return o


def cyl(name, r, h, loc, material, r2=None, segs=32, bevel=0.003, rot=(0, 0, 0), coll=None, parent=None):
    """Cylinder (or tapered cylinder with r2). loc = centre."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=segs, radius1=r, radius2=r if r2 is None else r2, depth=h)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, min(bevel, h * 0.45), coll, parent)


def ball(name, r, loc, material, scale=(1, 1, 1), rot=(0, 0, 0), parent=None, segs=20):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=segs, v_segments=max(8, segs // 2), radius=r)
    o = _obj(name, bm)
    o.location, o.scale, o.rotation_euler = loc, scale, rot
    return _finish(o, material, 0, None, parent)


def blobs(name, parts, material, parent=None, segs=12):
    """Many soft spheres merged into one object: leaves, moss cushions, clouds, smoke, cat stripes.
    parts = [(radius, centre, scale, rotation)]."""
    bm = bmesh.new()
    for r, loc, scl, rot in parts:
        verts = bmesh.ops.create_uvsphere(bm, u_segments=segs, v_segments=max(6, segs // 2), radius=r)["verts"]
        bmesh.ops.transform(bm, matrix=Matrix.LocRotScale(Vector(loc), Euler(rot), Vector(scl)), verts=verts)
    return _finish(_obj(name, bm), material, 0, None, parent)


def spline(ctrl, steps=6, closed=False):
    """Smooth Catmull-Rom curve through control points (for bentwood, cords, roots, handles)."""
    P = [Vector(c) for c in ctrl]
    m, out = len(P), []
    for i in range(m if closed else m - 1):
        p0 = P[i - 1] if (closed or i > 0) else P[i]
        p1, p2 = P[i], P[(i + 1) % m]
        p3 = P[(i + 2) % m] if (closed or i + 2 < m) else p2
        for s in range(steps):
            t = s / steps
            out.append(0.5 * (2 * p1 + (p2 - p0) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t * t
                              + (3 * p1 - p0 - 3 * p2 + p3) * t ** 3))
    if not closed:
        out.append(P[-1])
    return out


def tube(name, pts, r, material, parent=None, segs=10, r2=None, closed=False):
    """Round tube swept along a path: spindles, cords, roots, handles, washing line, braided rug rounds."""
    pts = [Vector(p) for p in pts]
    n, bm, rings, nrm = len(pts), bmesh.new(), [], None
    for i, p in enumerate(pts):
        tang = (pts[(i + 1) % n] - pts[i - 1]) if closed else (pts[min(i + 1, n - 1)] - pts[max(i - 1, 0)])
        tang.normalize()
        if nrm is None:
            ref = Vector((0, 0, 1)) if abs(tang.z) < 0.9 else Vector((1, 0, 0))
            nrm = tang.cross(ref).normalized()
        else:                                               # parallel transport: no twisting
            nrm = (nrm - tang * nrm.dot(tang)).normalized()
        bi = tang.cross(nrm)
        rr = r if r2 is None else r + (r2 - r) * i / (n - 1)
        rings.append([bm.verts.new(p + (nrm * math.cos(a) + bi * math.sin(a)) * rr)
                      for a in (2 * math.pi * k / segs for k in range(segs))])
    for i in range(n if closed else n - 1):
        a, b = rings[i], rings[(i + 1) % n]
        for k in range(segs):
            bm.faces.new((a[k], b[k], b[(k + 1) % segs], a[(k + 1) % segs]))
    if not closed:
        bm.faces.new(list(reversed(rings[0])))
        bm.faces.new(rings[-1])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return _finish(_obj(name, bm), material, 0, None, parent)


def ring_pts(r, z=0.0, n=40, cx=0.0, cy=0.0):
    return [(cx + r * math.cos(2 * math.pi * k / n), cy + r * math.sin(2 * math.pi * k / n), z) for k in range(n)]


def lathe(name, prof, loc, material, segs=32, parent=None, rot=(0, 0, 0), scale=(1, 1, 1)):
    """Turned shape from a (radius, height) profile: jars, pots, kettle, lantern, table legs."""
    bm, rings = bmesh.new(), []
    for r, z in prof:
        if r < 1e-6:
            rings.append([bm.verts.new((0, 0, z))])
        else:
            rings.append([bm.verts.new((r * math.cos(2 * math.pi * k / segs), r * math.sin(2 * math.pi * k / segs), z))
                          for k in range(segs)])
    for a, b in zip(rings, rings[1:]):
        if len(a) == 1 and len(b) == 1:
            continue
        for k in range(segs):
            if len(a) == 1:
                bm.faces.new((a[0], b[k], b[(k + 1) % segs]))
            elif len(b) == 1:
                bm.faces.new((a[k], a[(k + 1) % segs], b[0]))
            else:
                bm.faces.new((a[k], a[(k + 1) % segs], b[(k + 1) % segs], b[k]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    o = _obj(name, bm)
    o.location, o.rotation_euler, o.scale = loc, rot, scale
    return _finish(o, material, 0, None, parent)


def sheet(name, nu, nv, fn, material, parent=None):
    """A cloth surface from a function fn(u, v) -> (x, y, z), u and v in 0..1: curtains, laundry, quilt drops."""
    bm = bmesh.new()
    grid = [[bm.verts.new(fn(i / nu, j / nv)) for j in range(nv + 1)] for i in range(nu + 1)]
    for i in range(nu):
        for j in range(nv):
            bm.faces.new((grid[i][j], grid[i + 1][j], grid[i + 1][j + 1], grid[i][j + 1]))
    return _finish(_obj(name, bm), material, 0, None, parent)


def foliage(name, clusters, n, leaf, material, parent=None, seed=1, droop=0.3):
    """Many small real leaves in ONE mesh. clusters = [(centre, radius)], leaf = (length, width)."""
    rnd = random.Random(seed)
    bm = bmesh.new()
    ln, lw = leaf
    for c, rad in clusters:
        c = Vector(c)
        for _ in range(n):
            d = Vector((rnd.gauss(0, 1), rnd.gauss(0, 1), rnd.gauss(0, 1) * 0.8)).normalized()
            p = c + d * rad * (0.55 + 0.45 * rnd.random())
            out = (d + Vector((rnd.uniform(-.6, .6), rnd.uniform(-.6, .6), -droop))).normalized()
            side = out.cross(Vector((0, 0, 1)))
            side = side.normalized() if side.length > 1e-4 else Vector((1, 0, 0))
            side = (side + out.cross(side) * rnd.uniform(-0.5, 0.5)).normalized()
            s = rnd.uniform(0.75, 1.2)
            fold = out.cross(side).normalized() * lw * s * 0.12
            vs = [bm.verts.new(p + out * ln * s * f + side * lw * s * wd - fold * abs(wd) * 2)
                  for f, wd in ((0, 0), (0.25, 0.42), (0.62, 0.36), (1.0, 0), (0.62, -0.36), (0.25, -0.42))]
            bm.faces.new(vs)
    o = _obj(name, bm)
    o.data.materials.append(material)
    COL_ROOM.objects.link(o)
    o.parent = parent
    return o


def grass(name, tufts, material, seed=1, parent=None):
    """Tufts of tall meadow grass in ONE mesh: thin tapering blades that lean out and bend over at the tip.
    tufts = [(x, y, z, radius, height, blades)]."""
    rnd = random.Random(seed)
    bm = bmesh.new()
    for cx, cy, cz, rad, hgt, n in tufts:
        for _ in range(n):
            a = rnd.uniform(0, 2 * math.pi)
            d = rad * math.sqrt(rnd.random())
            base = Vector((cx + math.cos(a) * d, cy + math.sin(a) * d, cz))
            lean = Vector((math.cos(a), math.sin(a), 0)) * rnd.uniform(0.15, 0.55) + \
                Vector((rnd.gauss(0, 0.15), rnd.gauss(0, 0.15), 0))
            h = hgt * rnd.uniform(0.5, 1.0)
            wd = rnd.uniform(0.006, 0.013)
            sa = rnd.uniform(0, math.pi)
            side = Vector((math.cos(sa), math.sin(sa), 0))
            prev = None
            for k in range(5):
                t = k / 4
                p = base + Vector((0, 0, h * t)) + lean * h * t * t
                ww = wd * (1 - t) + 0.0006
                v1, v2 = bm.verts.new(p - side * ww), bm.verts.new(p + side * ww)
                if prev:
                    bm.faces.new((prev[0], prev[1], v2, v1))
                prev = (v1, v2)
    o = _obj(name, bm)
    o.data.materials.append(material)
    o.data.polygons.foreach_set("use_smooth", [True] * len(o.data.polygons))
    COL_ROOM.objects.link(o)
    o.parent = parent
    return o


def label(name, body, size, loc, material, rot=(R(90), 0, 0), align="CENTER", parent=None, depth=0.002):
    """Plain 3D text that is NOT a portfolio hook (jar labels, a house number)."""
    cu = bpy.data.curves.new(name, "FONT")
    cu.body, cu.size, cu.align_x, cu.align_y = body, size, align, "CENTER"
    cu.extrude = depth
    o = bpy.data.objects.new(name, cu)
    o.location, o.rotation_euler = loc, rot
    o.data.materials.append(material)
    COL_ROOM.objects.link(o)
    o.parent = parent
    return o


def empty(name, loc, rot=(0, 0, 0), parent=None):
    """An invisible handle to build a group of parts in its own local space."""
    e = bpy.data.objects.new(name, None)
    e.empty_display_size = 0.1
    e.location, e.rotation_euler = loc, rot
    COL_ROOM.objects.link(e)
    e.parent = parent
    return e


def no_shadow(*objs):
    for o in objs:
        if hasattr(o, "visible_shadow"):
            o.visible_shadow = False
    return objs[0]


def tilted(name, size, a, b, material, bevel=0.004, parent=None):
    """A straight member (box) from point a to point b: braces, ladder rails, roof rafters.
    size = (thickness, width); the long axis runs from a to b."""
    a, b = Vector(a), Vector(b)
    d = b - a
    q = d.to_track_quat("Z", "Y")
    return box(name, (size[0], size[1], d.length), (a + b) / 2, material, bevel=bevel, rot=q.to_euler(), parent=parent)


def flame(name, loc, parent=None, s=1.0):
    """Teardrop candle flame (glows, casts no shadow)."""
    return no_shadow(lathe(name, [(0.0005, 0), (0.006 * s, 0.006 * s), (0.0075 * s, 0.013 * s), (0.0045 * s, 0.025 * s),
                                  (0.0005, 0.036 * s)], loc, FLAME, segs=12, parent=parent))


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
    """Mark decoration that is hidden once the hook gets a real image (e.g. a default watercolour)."""
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


def circle_yz(x, cy, cz, r, n=48):
    """Points on a circle standing in the y-z plane (the left wall): round window rings."""
    return [(x, cy + r * math.cos(2 * math.pi * k / n), cz + r * math.sin(2 * math.pi * k / n)) for k in range(n)]


# =====================================================================
#  HILLSIDE BASE: an earth slab with a meadow turf top, the cottage on a stone plinth
# =====================================================================
YARD_X, YARD_Y = -1.55, -0.8       # outer edges of the meadow around the cottage (left and front)
GROUND = -0.02                     # top of the turf
yard_cx, yard_cy = (W + YARD_X) / 2, (D + T + YARD_Y) / 2
box("Hill_Earth", (W - YARD_X, D + T - YARD_Y, 0.42), (yard_cx, yard_cy, GROUND - 0.25), EARTH, bevel=0.07)
box("Hill_Turf", (W - YARD_X + 0.03, D + T - YARD_Y + 0.03, 0.06), (yard_cx, yard_cy, GROUND - 0.03), TURF,
    bevel=0.03)
rnd = random.Random(SEED + 2)
rocks = []                                         # field stones poking out of the cut earth (front and right faces)
for k in range(14):
    if k < 9:
        p = (rnd.uniform(YARD_X + 0.2, W - 0.2), YARD_Y - 0.02, GROUND - rnd.uniform(0.12, 0.34))
    else:
        p = (W + 0.02, rnd.uniform(YARD_Y + 0.3, D), GROUND - rnd.uniform(0.12, 0.34))
    rr = rnd.uniform(0.04, 0.08)
    rocks.append((rr, p, (1.3, 1.0, 0.75), (0, 0, rnd.uniform(0, 3))))
blobs("Hill_Rocks", rocks, FLAG, segs=10)
roots_ = []                                        # fine roots hanging out of the turf edge
for k in range(16):
    x0 = rnd.uniform(YARD_X + 0.1, W - 0.1)
    roots_.append((0.006, (x0, YARD_Y - 0.03, GROUND - 0.07 - rnd.uniform(0, 0.04)), (1, 1, rnd.uniform(5, 9)),
                   (rnd.uniform(-0.2, 0.2), 0, 0)))
blobs("Hill_Fine_Roots", roots_, mat("bark", 0.9, color=shade(COLORS["earth"], 0.7)), segs=6)

# Rubble-stone plinth (16 cm) under the whole cottage, and wide pine floorboards on top.
box("Plinth_Stone", (W + T, D + T, FLOOR_Z - 0.02 - GROUND), ((W - T) / 2, (D + T) / 2, (FLOOR_Z - 0.02 + GROUND) / 2),
    STONE_X, bevel=0.008)
box("Plinth_Stone_Right", (0.006, D + T - 0.01, FLOOR_Z - 0.03 - GROUND), (W + 0.003, (D + T) / 2,
    (FLOOR_Z - 0.02 + GROUND) / 2), STONE_Y, bevel=0)
box("Floor_Joints", (W, D, 0.004), (W / 2, D / 2, FLOOR_Z - 0.018), mat("dark", 0.9, color="#4A3624"), bevel=0)
BOARD = 0.18
rows = int(D / BOARD)
pitch = D / rows
parts_a, parts_b = [], []
rnd = random.Random(SEED + 5)
for r_ in range(rows):
    x, k = -rnd.uniform(0.0, 1.4), 0
    while x < W:
        ln = rnd.uniform(1.2, 2.4)
        xa, xb = max(0.0, x), min(W, x + ln)
        if xb - xa > 0.05:
            (parts_a if (r_ + k) % 2 == 0 else parts_b).append(
                ((xb - xa - 0.004, pitch - 0.004, 0.02), ((xa + xb) / 2, r_ * pitch + pitch / 2, FLOOR_Z - 0.01), (0, 0, 0)))
        x += ln
        k += 1
boxes("Floor_Boards_A", parts_a, FLOOR_A, bevel=0.0018)
boxes("Floor_Boards_B", parts_b, FLOOR_B, bevel=0.0018)

# =====================================================================
#  WALLS: limewashed plaster, a stable door and a round window in the left wall
# =====================================================================
DOOR_Y, DOOR_TOP = (0.28, 1.2), FLOOR_Z + 2.04
WIN_Y, WIN_Z, WIN_R = 2.55, FLOOR_Z + 1.42, 0.46
WALL_Z0 = FLOOR_Z - 0.02
left = box("Wall_Left", (T, D + T, H - WALL_Z0), (-T / 2, (D + T) / 2, (H + WALL_Z0) / 2), PLASTER, bevel=0.0)
door_cut = box("Door_Cutter", (T * 3, DOOR_Y[1] - DOOR_Y[0], DOOR_TOP - FLOOR_Z + 0.2),
               (-T / 2, sum(DOOR_Y) / 2, (DOOR_TOP + FLOOR_Z - 0.2) / 2), mat("wall"), bevel=0.0)
win_cut = cyl("Window_Cutter", WIN_R, T * 3, (-T / 2, WIN_Y, WIN_Z), mat("wall"), segs=64, bevel=0, rot=(0, R(90), 0))
for nm, cutter in (("Door", door_cut), ("Window", win_cut)):
    cutter.hide_render = cutter.hide_viewport = True
    boolean = left.modifiers.new(nm, "BOOLEAN")
    boolean.operation, boolean.object = "DIFFERENCE", cutter
box("Wall_Back", (W + T, T, H - WALL_Z0), ((W - T) / 2, D + T / 2, (H + WALL_Z0) / 2), PLASTER, bevel=0.0)

# Exposed oak frame: wall plates along the top, posts at the wall ends, by the door and beside the chimney.
PLATE = 0.16
box("Beam_WallPlate_Back", (W, 0.13, PLATE), (W / 2, D - 0.065, H - PLATE / 2), TIMBER, bevel=0.008)
box("Beam_WallPlate_Left", (0.13, D, PLATE), (0.065, D / 2, H - PLATE / 2), TIMBER_Y, bevel=0.008)
for nm, x in (("Chimney", 2.44), ("End", W - 0.065)):
    box(f"Post_Back_{nm}", (0.13, 0.12, H - PLATE - FLOOR_Z), (x, D - 0.06, (H - PLATE + FLOOR_Z) / 2), TIMBER_V,
        bevel=0.008)
for nm, y in (("End", 0.065), ("Door", 1.32)):
    box(f"Post_Left_{nm}", (0.12, 0.13, H - PLATE - FLOOR_Z), (0.06, y, (H - PLATE + FLOOR_Z) / 2), TIMBER_V,
        bevel=0.008)
box("Beam_Door_Lintel", (0.12, 1.2, 0.15), (0.06, 0.67, DOOR_TOP + 0.075), TIMBER_Y, bevel=0.008)
tilted("Brace_Left", (0.1, 0.08), (0.05, 0.13, H - PLATE - 0.02), (0.05, 0.62, DOOR_TOP + 0.15), TIMBER_V, bevel=0.006)
tilted("Brace_Left_2", (0.1, 0.08), (0.05, 1.25, H - PLATE - 0.02), (0.05, 0.78, DOOR_TOP + 0.15), TIMBER_V,
       bevel=0.006)
SK = 0.1                                           # pine skirting boards
for nm, size, loc in (("Back_1", (0.4, 0.018, SK), (0.75, D - 0.009, FLOOR_Z + SK / 2)),
                      ("Back_2", (0.9, 0.018, SK), (2.95, D - 0.009, FLOOR_Z + SK / 2)),
                      ("Left_1", (0.018, 0.56, SK), (0.009, 1.66, FLOOR_Z + SK / 2))):
    box(f"Skirting_{nm}", size, loc, PINE, bevel=0.003)

# Stable (Dutch) door: two leaves of V-jointed boards, ledges and braces on the inside, thumb latch and bolt.
dy0, dy1 = DOOR_Y
dcy, dw = (dy0 + dy1) / 2, dy1 - dy0
for nm, size, loc in (("Jamb_Front", (T + 0.03, 0.055, DOOR_TOP - FLOOR_Z), (-T / 2, dy0 + 0.0275, (DOOR_TOP + FLOOR_Z) / 2)),
                      ("Jamb_Back", (T + 0.03, 0.055, DOOR_TOP - FLOOR_Z), (-T / 2, dy1 - 0.0275, (DOOR_TOP + FLOOR_Z) / 2)),
                      ("Head", (T + 0.03, dw, 0.06), (-T / 2, dcy, DOOR_TOP - 0.03))):
    box(f"Door_Frame_{nm}", size, loc, TIMBER_V, bevel=0.005)
box("Door_Sill", (T + 0.04, dw, 0.04), (-T / 2, dcy, FLOOR_Z - 0.015), TIMBER_Y, bevel=0.005)
box("Door_Step", (0.36, dw + 0.12, 0.1), (-T - 0.17, dcy, GROUND + 0.05), FLAG, bevel=0.02)
LW = dw - 0.11 - 0.004                             # leaf width (an 813 mm leaf in a 920 mm opening)
LX = -0.04                                         # leaf centre (44 mm thick, set inside the frame)
leaves = (("Bottom", FLOOR_Z + 0.008, FLOOR_Z + 1.03), ("Top", FLOOR_Z + 1.036, DOOR_TOP - 0.064))
door_parts = []
for nm, z0, z1 in leaves:
    nb = 6
    for k in range(nb):
        yy = dcy - LW / 2 + LW * (k + 0.5) / nb
        door_parts.append(((0.044, LW / nb - 0.005, z1 - z0), (LX, yy, (z0 + z1) / 2), (0, 0, 0)))
door = boxes("Door_Boards", door_parts, DOOR_PAINT, bevel=0.004)
hook_link(door, "linkedin")
lx_in = LX + 0.022 + 0.011                         # ledges sit on the inside face
for nm, z0, z1 in leaves:
    za, zb = z0 + 0.1, z1 - 0.1
    for zz in (za, zb):
        box(f"Door_Ledge_{nm}", (0.022, LW - 0.06, 0.11), (lx_in, dcy, zz), DOOR_PAINT, bevel=0.004)
    tilted(f"Door_Brace_{nm}", (0.022, 0.1), (lx_in, dy1 - 0.12, za + 0.05), (lx_in, dy0 + 0.12, zb - 0.05), DOOR_PAINT)
box("Door_Latch_Bar", (0.012, 0.16, 0.018), (lx_in + 0.02, dy0 + 0.14, FLOOR_Z + 1.0), IRON, bevel=0.003)
box("Door_Latch_Keep", (0.03, 0.025, 0.05), (lx_in + 0.02, dy0 + 0.06, FLOOR_Z + 1.0), IRON, bevel=0.004)
tube("Door_Latch_Grip", spline([(lx_in + 0.012, dy0 + 0.1, FLOOR_Z + 1.1), (lx_in + 0.05, dy0 + 0.1, FLOOR_Z + 1.06),
                                (lx_in + 0.05, dy0 + 0.1, FLOOR_Z + 0.94), (lx_in + 0.012, dy0 + 0.1, FLOOR_Z + 0.9)], 4),
     0.008, IRON, segs=8)
box("Door_Bolt", (0.014, 0.12, 0.022), (lx_in + 0.02, dy0 + 0.2, FLOOR_Z + 1.06), IRON, bevel=0.003)

# Round (oeil-de-boeuf) window: painted ring frame with cross bars, oak architrave, deep sill shelf.
tube("Window_Frame_Ring", circle_yz(-0.075, WIN_Y, WIN_Z, WIN_R - 0.035, 64), 0.035, TRIM, segs=10, closed=True)
box("Window_Bar_H", (0.035, 2 * WIN_R - 0.08, 0.032), (-0.075, WIN_Y, WIN_Z), TRIM, bevel=0.004)
box("Window_Bar_V", (0.035, 0.032, 2 * WIN_R - 0.08), (-0.075, WIN_Y, WIN_Z), TRIM, bevel=0.004)
no_shadow(cyl("Window_Glass", WIN_R - 0.03, 0.004, (-0.085, WIN_Y, WIN_Z), WIN_GLASS, segs=48, bevel=0,
              rot=(0, R(90), 0)))
tube("Window_Architrave", circle_yz(0.014, WIN_Y, WIN_Z, WIN_R + 0.04, 64), 0.03, TIMBER, segs=10, closed=True)
SILL_Z = WIN_Z - WIN_R - 0.01
box("Window_Sill", (0.22, 0.74, 0.03), (0.06, WIN_Y, SILL_Z - 0.015), PINE, bevel=0.004)
for sy in (-1, 1):
    box("Window_Sill_Bracket", (0.12, 0.025, 0.1), (0.06, WIN_Y + sy * 0.28, SILL_Z - 0.08), PINE_V, bevel=0.003)


def herb_pot(name, x, y, z, kind):
    """Terracotta pot (dia 12 cm) with soil and a kitchen herb: basil, rosemary or thyme."""
    lathe(f"{name}_Pot", [(0, 0), (0.045, 0), (0.058, 0.09), (0.064, 0.092), (0.064, 0.11), (0.056, 0.11),
                          (0.052, 0.095), (0, 0.095)], (x, y, z), CLAY, segs=24)
    cyl(f"{name}_Soil", 0.05, 0.01, (x, y, z + 0.098), SOIL, bevel=0, segs=16)
    top = (x, y, z + 0.17)
    if kind == "basil":
        foliage(f"{name}_Basil", [(top, 0.07), ((x, y, z + 0.22), 0.05)], 34, (0.045, 0.03),
                mat("plant", 0.55, color=shade(COLORS["plant"], 1.15)), seed=SEED + 21, droop=0.15)
    elif kind == "rosemary":
        for k in range(7):
            a = k * 0.9
            tip = (x + math.cos(a) * 0.04, y + math.sin(a) * 0.04, z + 0.25 + 0.05 * math.sin(k))
            tube(f"{name}_Stem", [(x, y, z + 0.1), tip], 0.0025, mat("bark", 0.8), segs=5)
        foliage(f"{name}_Needles", [((x, y, z + 0.21), 0.06)], 90, (0.025, 0.004), mat("plant", 0.6, color=shade(
            COLORS["plant"], 0.7)), seed=SEED + 22, droop=-0.4)
    else:
        foliage(f"{name}_Thyme", [((x, y, z + 0.14), 0.065)], 140, (0.012, 0.007),
                mat("plant", 0.6, color=mix_hex(COLORS["plant"], "#9AA88A", 0.4)), seed=SEED + 23, droop=0.6)


for k, (dy, kind) in enumerate(((-0.22, "rosemary"), (0.0, "basil"), (0.22, "thyme"))):
    herb_pot(f"Sill_Herb_{k}", 0.075, WIN_Y + dy, SILL_Z, kind)

# Lace curtains on an iron pole, tied back at the sides so the round window stays open.
POLE_Z = WIN_Z + WIN_R + 0.1
tube("Curtain_Pole", [(0.07, WIN_Y - 0.66, POLE_Z), (0.07, WIN_Y + 0.66, POLE_Z)], 0.011, IRON, segs=10)
for sy in (-1, 1):
    ball("Curtain_Pole_Finial", 0.022, (0.07, WIN_Y + sy * 0.68, POLE_Z), IRON)
    box("Curtain_Pole_Bracket", (0.07, 0.015, 0.03), (0.035, WIN_Y + sy * 0.6, POLE_Z), IRON, bevel=0.003)


def lace_panel(name, y_out, s):
    """One gathered lace curtain: full width under the pole, pinched in by a tie-back, loose below it."""
    top, bot, tie = POLE_Z - 0.02, WIN_Z - WIN_R - 0.12, WIN_Z - 0.14
    full = 0.52

    def span(z):
        if z >= tie:
            t = (top - z) / (top - tie)
            e = t * t * (3 - 2 * t)
            return full * (1 - e) + 0.1 * e
        return 0.1 + 0.1 * (tie - z) / (tie - bot)

    def fn(u, v):
        z = top - v * (top - bot)
        sp = span(z)
        amp = 0.01 + 0.03 * (1 - sp / full)
        return (0.06 + amp * (0.5 + 0.5 * math.sin(u * 2 * math.pi * 6)), y_out + s * u * sp, z)
    no_shadow(sheet(name, 40, 26, fn, LACE))
    tube(f"{name}_Tie", [(0.04, y_out + s * 0.02, tie + 0.01), (0.1, y_out + s * 0.06, tie),
                         (0.1, y_out + s * 0.12, tie - 0.01), (0.04, y_out + s * 0.13, tie)], 0.008,
         gingham("accent_1"), segs=6)


lace_panel("Curtain_Left", WIN_Y - 0.62, 1)
lace_panel("Curtain_Right", WIN_Y + 0.62, -1)

# =====================================================================
#  INGLENOOK HEARTH: limewashed chimney breast, brick-lined opening, oak bressummer, flagstone hearth
# =====================================================================
CB_X0, CB_X1, CB_D = 0.95, 2.35, 0.52               # chimney breast: from, to (x) and depth
CB_CX = (CB_X0 + CB_X1) / 2
OPEN_X0, OPEN_X1, OPEN_TOP = 1.15, 2.15, FLOOR_Z + 1.12
BEAM_H = 0.22
CB_FRONT = D - CB_D
for nm, x0, x1 in (("Left", CB_X0, OPEN_X0), ("Right", OPEN_X1, CB_X1)):
    box(f"Chimney_Pier_{nm}", (x1 - x0, CB_D, OPEN_TOP - FLOOR_Z + 0.02), ((x0 + x1) / 2, D - CB_D / 2,
        (OPEN_TOP + FLOOR_Z - 0.02) / 2), LIME, bevel=0.012)
box("Chimney_Breast", (CB_X1 - CB_X0, CB_D, H - OPEN_TOP - BEAM_H), (CB_CX, D - CB_D / 2, (H + OPEN_TOP + BEAM_H) / 2),
    LIME, bevel=0.012)
box("Chimney_Behind_Beam", (OPEN_X1 - OPEN_X0, CB_D - 0.25, BEAM_H), (CB_CX, D - (CB_D - 0.25) / 2,
    OPEN_TOP + BEAM_H / 2), BRICK_X, bevel=0)
box("Chimney_Soot", (OPEN_X1 - OPEN_X0 - 0.02, CB_D - 0.26, 0.006), (CB_CX, D - (CB_D - 0.25) / 2, OPEN_TOP - 0.002),
    mat("dark", 0.95, color="#1E1A18"), bevel=0)
box("Inglenook_Back", (OPEN_X1 - OPEN_X0, 0.03, OPEN_TOP - FLOOR_Z), (CB_CX, D - 0.015, (OPEN_TOP + FLOOR_Z) / 2),
    BRICK_X, bevel=0)
for sx, x in ((1, OPEN_X0 + 0.015), (-1, OPEN_X1 - 0.015)):
    box("Inglenook_Cheek", (0.03, CB_D - 0.01, OPEN_TOP - FLOOR_Z), (x, D - CB_D / 2 - 0.005, (OPEN_TOP + FLOOR_Z) / 2),
        BRICK_Y, bevel=0)
beam = box("Bressummer", (CB_X1 - CB_X0 + 0.16, 0.27, BEAM_H), (CB_CX, CB_FRONT + 0.115, OPEN_TOP + BEAM_H / 2), TIMBER,
           bevel=0.014)
for k in range(5):                                 # adze marks on the old beam's face
    box("Bressummer_Adze", (0.12, 0.004, 0.012), (CB_X0 + 0.15 + k * 0.29, CB_FRONT - 0.019, OPEN_TOP + 0.06 + (k % 2) * 0.09),
        mat("timber", 0.8, color=shade(COLORS["timber"], 0.8)), bevel=0.002, rot=(0, R(8 - k * 4), 0))
HEARTH_Z = FLOOR_Z + 0.035
box("Hearth_Flag_Front", (CB_X1 - CB_X0 + 0.1, 0.46, 0.035), (CB_CX, CB_FRONT - 0.23, FLOOR_Z + 0.0175), FLAG, bevel=0.006)
box("Hearth_Flag_Inside", (OPEN_X1 - OPEN_X0 - 0.06, CB_D - 0.04, 0.035), (CB_CX, D - CB_D / 2 - 0.01, FLOOR_Z + 0.0175),
    FLAG, bevel=0.004)

# Split logs stacked in the left of the inglenook (ends towards the room).
LOG_END = M("wood", 0.85, "wood", color=mix_hex(COLORS["wood"], COLORS["cream"], 0.4))
k = 0
for row, n in enumerate((3, 2, 1)):
    for j in range(n):
        lx = OPEN_X0 + 0.09 + j * 0.1 + row * 0.05
        lz = HEARTH_Z + 0.045 + row * 0.085
        ln = random.uniform(0.34, 0.4)
        cyl(f"Log_{k}", 0.045, ln, (lx, D - 0.05 - ln / 2, lz), BARK, segs=10, bevel=0.008, rot=(R(90), 0, 0))
        cyl(f"Log_End_{k}", 0.039, 0.004, (lx, D - 0.05 - ln - 0.001, lz), LOG_END, segs=10, bevel=0, rot=(R(90), 0, 0))
        k += 1

# Cast-iron skillet hanging on a hook on the right pier.
sk = empty("Skillet", (CB_X1 - 0.1, CB_FRONT - 0.012, FLOOR_Z + 0.62), rot=(R(90), 0, 0))
lathe("Skillet_Pan", [(0, 0), (0.11, 0), (0.125, 0.045), (0.118, 0.045), (0.105, 0.008), (0, 0.008)], (0, 0, 0), IRON,
      parent=sk, segs=28)
box("Skillet_Handle", (0.028, 0.16, 0.014), (0, 0.19, 0.035), IRON, bevel=0.005, parent=sk)
tube("Skillet_Hook", [(CB_X1 - 0.1, CB_FRONT - 0.01, FLOOR_Z + 0.96), (CB_X1 - 0.1, CB_FRONT - 0.04, FLOOR_Z + 0.94),
                      (CB_X1 - 0.1, CB_FRONT - 0.04, FLOOR_Z + 0.9)], 0.004, IRON, segs=6)


def herb_bundle(name, x, y, z, kind, length=0.22):
    """A bundle of herbs drying head-down from the beam: twine loop, tie, stems and leaves (all merged)."""
    twine = mat("twine", 0.9, color=shade(COLORS["cream"], 0.78))
    tube(f"{name}_Twine", [(x, y, z), (x, y, z - 0.06)], 0.002, twine, segs=5)
    tie = z - 0.06
    cyl(f"{name}_Tie", 0.01, 0.012, (x, y, tie), twine, segs=10, bevel=0.002)
    rr = random.Random(SEED + sum(map(ord, name)))
    stems = [((0.003, 0.003, length * 0.55), (x + rr.uniform(-0.01, 0.01), y + rr.uniform(-0.01, 0.01),
             tie - length * 0.25), (rr.uniform(-0.15, 0.15), rr.uniform(-0.15, 0.15), 0)) for _ in range(8)]
    boxes(f"{name}_Stems", stems, mat("stem", 0.9, color=mix_hex(COLORS["plant"], COLORS["wood"], 0.5)), bevel=0)
    cols = {"lavender": mix_hex("#9C8CC8", COLORS["cream"], 0.15), "sage": mix_hex(COLORS["plant"], "#A9B09A", 0.45),
            "rosemary": shade(COLORS["plant"], 0.62), "yarrow": mix_hex(COLORS["cream"], COLORS["accent_2"], 0.35)}
    m = mat("herb", 0.9, color=cols[kind])
    parts = []
    for _ in range(46):
        t = rr.uniform(0.15, 1.0)
        a = rr.uniform(0, 2 * math.pi)
        sp = (0.006 + 0.05 * t) * rr.uniform(0.6, 1.0)
        p = (x + math.cos(a) * sp, y + math.sin(a) * sp, tie - 0.015 - length * t)
        if kind == "lavender":
            parts.append((0.006, p, (1, 1, 5), (0, 0, 0)))
        elif kind == "yarrow":
            parts.append((0.014, p, (1, 1, 0.55), (0, 0, 0)))
        else:
            parts.append((0.014 if kind == "sage" else 0.01, p, (0.8, 0.3, 2.4), (math.sin(a) * 0.5, -math.cos(a) * 0.5, a)))
    blobs(f"{name}_Leaves", parts, m, segs=8)


def garlic_braid(name, x, y, z, n=7):
    """Plaited garlic hung from a nail: a twine loop and bulbs alternating down the plait."""
    tube(f"{name}_Loop", [(x, y, z), (x, y, z - 0.05)], 0.003, mat("twine", 0.9, color=shade(COLORS["cream"], 0.78)), segs=5)
    parts, stems = [], []
    for k in range(n):
        side = -1 if k % 2 else 1
        p = (x + side * 0.018, y - 0.01, z - 0.07 - k * 0.04)
        parts.append((0.026, p, (1, 1, 0.85), (0, 0, 0)))
        parts.append((0.008, (p[0], p[1], p[2] - 0.028), (1, 1, 1.2), (0, 0, 0)))
        stems.append(((0.008, 0.008, 0.06), (x, y - 0.005, z - 0.06 - k * 0.04), (0, side * 0.5, 0)))
    blobs(f"{name}_Bulbs", parts, mat("garlic", 0.6, color=mix_hex(COLORS["cream"], "#E8D7E0", 0.4)), segs=10)
    boxes(f"{name}_Plait", stems, mat("twine", 0.9, color=shade(COLORS["cream"], 0.78)), bevel=0)


hy = CB_FRONT - 0.005
for k, (hx, kind) in enumerate(((CB_X0 + 0.02, "sage"), (CB_X0 + 0.19, "lavender"), (CB_X0 + 0.36, "rosemary"),
                                (OPEN_X1 + 0.02, "yarrow"), (CB_X1 + 0.03, "lavender"))):
    herb_bundle(f"Herbs_{k}", hx, hy, OPEN_TOP, kind, length=random.uniform(0.18, 0.24))
garlic_braid("Garlic", OPEN_X1 - 0.1, hy, OPEN_TOP)
# On the beam: a pair of brass candlesticks and a stoneware jug of wooden spoons.
BEAM_TOP = OPEN_TOP + BEAM_H
for k, cx in enumerate((CB_X0 + 0.12, CB_X1 - 0.12)):
    lathe(f"Candlestick_{k}", [(0, 0), (0.04, 0), (0.042, 0.008), (0.012, 0.02), (0.01, 0.1), (0.022, 0.11),
                               (0.022, 0.118), (0, 0.118)], (cx, CB_FRONT + 0.1, BEAM_TOP), BRASS, segs=20)
    cyl(f"Candle_{k}", 0.011, 0.16, (cx, CB_FRONT + 0.1, BEAM_TOP + 0.198), CANDLE, segs=12, bevel=0.002)
    if RAINY:
        flame(f"Candle_Flame_{k}", (cx, CB_FRONT + 0.1, BEAM_TOP + 0.281))
lathe("Beam_Jug", [(0, 0), (0.05, 0), (0.062, 0.05), (0.055, 0.11), (0.042, 0.135), (0.046, 0.15), (0.04, 0.15),
                   (0.036, 0.135), (0, 0.13)], (CB_CX + 0.18, CB_FRONT + 0.12, BEAM_TOP), M("accent_3", 0.32, "ceramic"),
      segs=24)
for k in range(3):
    a = R(-14 + k * 14)
    tube("Beam_Spoon", [(CB_CX + 0.18, CB_FRONT + 0.12, BEAM_TOP + 0.05),
                        (CB_CX + 0.18 + math.sin(a) * 0.08, CB_FRONT + 0.12, BEAM_TOP + 0.24)], 0.006, PINE, segs=6)
    ball("Beam_Spoon_Bowl", 0.02, (CB_CX + 0.18 + math.sin(a) * 0.085, CB_FRONT + 0.12, BEAM_TOP + 0.255), PINE,
         scale=(1, 0.5, 1.4), rot=(0, a, 0))


# =====================================================================
#  SLEEPING LOFT (back-right corner) with a ladder, and a sink counter underneath
# =====================================================================
LOFT_X0, LOFT_Y0 = 3.4, 2.0                         # front-left corner of the loft deck
LOFT_Z = FLOOR_Z + 1.95                             # top of the deck boards
JOIST = 0.17
deck = []
nb = int((D - LOFT_Y0) / 0.15)
for k in range(nb):
    yy = LOFT_Y0 + (D - LOFT_Y0) * (k + 0.5) / nb
    deck.append(((W - LOFT_X0, (D - LOFT_Y0) / nb - 0.004, 0.025), ((W + LOFT_X0) / 2, yy, LOFT_Z - 0.0125), (0, 0, 0)))
boxes("Loft_Deck", deck, PINE, bevel=0.002)
box("Loft_Beam_Front", (W - LOFT_X0, 0.12, JOIST), ((W + LOFT_X0) / 2, LOFT_Y0 + 0.06, LOFT_Z - 0.025 - JOIST / 2), TIMBER,
    bevel=0.008)
box("Loft_Beam_Side", (0.12, D - LOFT_Y0 - 0.12, JOIST), (LOFT_X0 + 0.06, (D + LOFT_Y0 + 0.12) / 2,
    LOFT_Z - 0.025 - JOIST / 2), TIMBER_Y, bevel=0.008)
box("Loft_Ledger", (W - LOFT_X0 - 0.12, 0.08, 0.14), ((W + LOFT_X0 + 0.12) / 2, D - 0.04, LOFT_Z - 0.025 - 0.07), TIMBER,
    bevel=0.006)
for jx in (3.78, 4.16):
    box("Loft_Joist", (0.06, D - LOFT_Y0 - 0.2, 0.14), (jx, (D + LOFT_Y0) / 2 + 0.02, LOFT_Z - 0.025 - 0.07), TIMBER_Y,
        bevel=0.005)
RAIL_H = 0.42
for nm, (px, py) in (("Front_Left", (LOFT_X0 + 0.05, LOFT_Y0 + 0.05)), ("Front_Right", (W - 0.05, LOFT_Y0 + 0.05))):
    box(f"Loft_Post_{nm}", (0.1, 0.1, LOFT_Z + RAIL_H - FLOOR_Z), (px, py, (LOFT_Z + RAIL_H + FLOOR_Z) / 2), TIMBER_V,
        bevel=0.008)
    ball(f"Loft_Post_{nm}_Cap", 0.045, (px, py, LOFT_Z + RAIL_H + 0.03), TIMBER, scale=(1, 1, 0.7))


def railing(name, a, b, along):
    """Spindle railing between two points on the deck edge: top rail, bottom rail, turned balusters."""
    a, b = Vector(a), Vector(b)
    ln = (b - a).length
    c = (a + b) / 2
    size_t = (ln, 0.05, 0.045) if along == "X" else (0.05, ln, 0.045)
    box(f"{name}_Top", size_t, (c.x, c.y, LOFT_Z + RAIL_H - 0.02), PINE if along == "X" else PINE_Y, bevel=0.006)
    size_b = (ln, 0.04, 0.03) if along == "X" else (0.04, ln, 0.03)
    box(f"{name}_Bottom", size_b, (c.x, c.y, LOFT_Z + 0.03), PINE if along == "X" else PINE_Y, bevel=0.004)
    n = max(2, int(ln / 0.11))
    for k in range(1, n):
        p = a + (b - a) * k / n
        lathe(f"{name}_Baluster", [(0, 0), (0.014, 0), (0.014, 0.03), (0.02, 0.08), (0.011, 0.16), (0.016, 0.26),
                                   (0.012, 0.33), (0.014, RAIL_H - 0.085), (0, RAIL_H - 0.085)], (p.x, p.y, LOFT_Z + 0.045),
              PINE_V, segs=12)


railing("Loft_Rail_Front", (LOFT_X0 + 0.1, LOFT_Y0 + 0.05), (W - 0.1, LOFT_Y0 + 0.05), "X")
railing("Loft_Rail_Side_A", (LOFT_X0 + 0.05, LOFT_Y0 + 0.1), (LOFT_X0 + 0.05, 2.43), "Y")
railing("Loft_Rail_Side_B", (LOFT_X0 + 0.05, 2.92), (LOFT_X0 + 0.05, D - 0.05), "Y")
box("Loft_Post_Ladder", (0.07, 0.07, RAIL_H), (LOFT_X0 + 0.05, 2.92, LOFT_Z + RAIL_H / 2), TIMBER_V, bevel=0.006)

# Fixed ladder: two pine rails and round rungs 28 cm apart, leaning up to the side of the loft.
LAD_Y = (2.47, 2.87)
LAD_BOTTOM_X, LAD_TOP = 2.92, Vector((LOFT_X0 + 0.03, 0, LOFT_Z + 0.36))
for k, yy in enumerate(LAD_Y):
    tilted(f"Ladder_Rail_{k}", (0.065, 0.032), (LAD_BOTTOM_X, yy, FLOOR_Z), (LAD_TOP.x, yy, LAD_TOP.z), PINE_V, bevel=0.005)
rise = LAD_TOP.z - FLOOR_Z
for k in range(1, int((LOFT_Z - FLOOR_Z) / 0.28) + 1):
    t = k * 0.28 / rise
    x_ = LAD_BOTTOM_X + (LAD_TOP.x - LAD_BOTTOM_X) * t
    cyl("Ladder_Rung", 0.016, LAD_Y[1] - LAD_Y[0] + 0.02, (x_, sum(LAD_Y) / 2, FLOOR_Z + rise * t), PINE_Y, segs=12,
        rot=(R(90), 0, 0), bevel=0.002)

if FAIRY_LIGHTS:                                    # a sagging string of warm bulbs along the loft railing
    pts = spline([(LOFT_X0 + 0.05, LOFT_Y0 + 0.04, LOFT_Z + RAIL_H - 0.01), (3.8, LOFT_Y0 + 0.03, LOFT_Z + RAIL_H - 0.11),
                  (4.2, LOFT_Y0 + 0.03, LOFT_Z + RAIL_H - 0.03), (W - 0.05, LOFT_Y0 + 0.04, LOFT_Z + RAIL_H - 0.12)], 10)
    tube("Fairy_Wire", pts, 0.0018, mat("dark", 0.5), segs=5)
    no_shadow(blobs("Fairy_Bulbs", [(0.011, tuple(p - Vector((0, 0.005, 0.012))), (1, 1, 1.3), (0, 0, 0))
                                    for p in pts[1::2]], BULB, segs=8))

# Sink counter under the loft: painted base unit, butcher-block top, a Belfast sink, a gingham curtain skirt.
KX0, KD, KH = LOFT_X0 + 0.07, 0.6, 0.9
kx_c, ky_c = (W + KX0) / 2, D - KD / 2
box("Kitchen_Plinth", (W - KX0, KD - 0.08, 0.1), (kx_c, ky_c + 0.04, FLOOR_Z + 0.05), mat("dark", 0.8), bevel=0.003)
box("Kitchen_Base", (W - KX0, KD - 0.02, KH - 0.14), (kx_c, ky_c + 0.01, FLOOR_Z + 0.1 + (KH - 0.14) / 2), SAGE_PAINT,
    bevel=0.004)
SINK_X, SINK_W = 4.17, 0.595
for nm, x0, x1 in (("L", KX0, SINK_X - SINK_W / 2), ("R", SINK_X + SINK_W / 2, W)):
    box(f"Kitchen_Top_{nm}", (x1 - x0, KD + 0.02, 0.04), ((x0 + x1) / 2, ky_c - 0.01, FLOOR_Z + KH - 0.02), PINE, bevel=0.004)
box("Kitchen_Top_Back", (SINK_W, 0.12, 0.04), (SINK_X, D - 0.06, FLOOR_Z + KH - 0.02), PINE, bevel=0.004)
sy0 = D - KD - 0.015
box("Sink_Body", (SINK_W, 0.455, 0.255), (SINK_X, sy0 + 0.2275, FLOOR_Z + KH - 0.1275), CERAMIC, bevel=0.02)
box("Sink_Basin", (SINK_W - 0.07, 0.385, 0.012), (SINK_X, sy0 + 0.2275, FLOOR_Z + KH - 0.004),
    mat("cream", 0.3, color=shade(COLORS["cream"], 0.82)), bevel=0.004)
tap_y = D - 0.06
for sx in (-1, 1):
    cyl("Tap_Pillar", 0.016, 0.07, (SINK_X + sx * 0.1, tap_y, FLOOR_Z + KH + 0.035), BRASS, segs=14)
    cyl("Tap_Head", 0.026, 0.02, (SINK_X + sx * 0.1, tap_y, FLOOR_Z + KH + 0.08), BRASS, segs=6, bevel=0.004)
tube("Tap_Bridge", [(SINK_X - 0.1, tap_y, FLOOR_Z + KH + 0.06), (SINK_X + 0.1, tap_y, FLOOR_Z + KH + 0.06)], 0.012, BRASS)
tube("Tap_Spout", spline([(SINK_X, tap_y, FLOOR_Z + KH + 0.06), (SINK_X, tap_y - 0.02, FLOOR_Z + KH + 0.2),
                          (SINK_X, tap_y - 0.12, FLOOR_Z + KH + 0.22), (SINK_X, tap_y - 0.16, FLOOR_Z + KH + 0.15)], 5),
     0.011, BRASS)
cx0, cx1 = KX0 + 0.01, SINK_X - SINK_W / 2 - 0.01


def skirt(u, v):
    """Gathered gingham curtain on a wire under the worktop."""
    z = FLOOR_Z + KH - 0.05 - v * (KH - 0.16)
    return (cx0 + u * (cx1 - cx0), sy0 - 0.012 - 0.02 * (0.5 + 0.5 * math.sin(u * 2 * math.pi * 7)) * (0.6 + 0.4 * v), z)


sheet("Kitchen_Curtain", 50, 6, skirt, gingham("accent_1"))
# Plate rack on the wall above the sink: two side boards, a drip shelf, dowel rails and plates on edge.
PR_X, PR_Z = 4.0, FLOOR_Z + 1.16
for sx in (-1, 1):
    box("PlateRack_Side", (0.02, 0.22, 0.45), (PR_X + sx * 0.32, D - 0.11, PR_Z + 0.225), PINE_V, bevel=0.003)
box("PlateRack_Shelf", (0.66, 0.24, 0.02), (PR_X, D - 0.12, PR_Z), PINE, bevel=0.003)
box("PlateRack_Top", (0.68, 0.24, 0.02), (PR_X, D - 0.12, PR_Z + 0.46), PINE, bevel=0.003)
for yy, zz in ((D - 0.2, PR_Z + 0.08), (D - 0.04, PR_Z + 0.22), (D - 0.2, PR_Z + 0.3)):
    cyl("PlateRack_Dowel", 0.006, 0.64, (PR_X, yy, zz), PINE, rot=(0, R(90), 0), segs=8, bevel=0)
plate_rim = M("accent_3", 0.3, "ceramic")
for k in range(6):
    px_ = PR_X - 0.25 + k * 0.1
    cyl("Rack_Plate", 0.11, 0.012, (px_, D - 0.12, PR_Z + 0.125), CERAMIC, rot=(R(78), 0, R(90)), segs=28, bevel=0.003)
    tube("Rack_Plate_Rim", [(px_ - 0.004, D - 0.12 + 0.105 * math.cos(a), PR_Z + 0.125 + 0.105 * math.sin(a))
                            for a in (2 * math.pi * q / 28 for q in range(28))], 0.004, plate_rim, segs=5, closed=True)
for k in range(3):                                   # three cups on the drip shelf
    lathe("Rack_Cup", [(0, 0), (0.03, 0), (0.04, 0.07), (0.037, 0.07), (0.028, 0.004), (0, 0.004)],
          (PR_X - 0.2 + k * 0.08, D - 0.12, PR_Z + 0.31), M("accent_2", 0.3, "ceramic") if k == 1 else CERAMIC, segs=18)
lathe("Kitchen_Crock", [(0, 0), (0.07, 0), (0.08, 0.06), (0.075, 0.17), (0.08, 0.18), (0.07, 0.18), (0, 0.17)],
      (KX0 + 0.12, D - 0.17, FLOOR_Z + KH), M("cream", 0.31, "ceramic", color=mix_hex(COLORS["cream"], COLORS["accent_2"], 0.35)),
      segs=24)
for k in range(4):
    a = R(-20 + k * 13)
    tube("Crock_Utensil", [(KX0 + 0.12, D - 0.17, FLOOR_Z + KH + 0.1),
                           (KX0 + 0.12 + math.sin(a) * 0.1, D - 0.17 + 0.02 * k - 0.03, FLOOR_Z + KH + 0.34)], 0.006, PINE,
         segs=6)
# Copper pans on S-hooks under the loft beam.
PAN_Y = LOFT_Y0 + 0.06
for k, (px_, kind) in enumerate(((3.62, "pot"), (3.92, "pan"), (4.22, "ladle"), (4.46, "pot"))):
    hz = LOFT_Z - 0.025 - JOIST
    tube(f"Pan_Hook_{k}", spline([(px_, PAN_Y, hz + 0.01), (px_, PAN_Y - 0.03, hz - 0.03), (px_, PAN_Y, hz - 0.07),
                                  (px_, PAN_Y + 0.02, hz - 0.1)], 3), 0.003, IRON, segs=6)
    top = hz - 0.1
    if kind == "pot":
        r_ = 0.07 if k == 0 else 0.06
        tube(f"Pan_Handle_{k}", [(px_, PAN_Y + 0.0, top), (px_, PAN_Y, top - 0.17)], 0.008, COPPER, segs=8)
        lathe(f"Pan_Pot_{k}", [(0, 0), (r_, 0), (r_ + 0.004, 0.09), (r_ - 0.003, 0.09), (r_ - 0.005, 0.006), (0, 0.006)],
              (px_, PAN_Y + 0.0 + r_ + 0.01, top - 0.17 - r_), COPPER, rot=(R(90), 0, 0), segs=28)
    elif kind == "pan":
        tube(f"Pan_Handle_{k}", [(px_, PAN_Y, top), (px_, PAN_Y, top - 0.18)], 0.009, BRASS, segs=8)
        lathe(f"Pan_Fry_{k}", [(0, 0), (0.1, 0), (0.115, 0.035), (0.11, 0.035), (0.095, 0.006), (0, 0.006)],
              (px_, PAN_Y + 0.02, top - 0.29), COPPER, rot=(R(90), 0, 0), segs=28)
    else:
        tube(f"Pan_Ladle_{k}", [(px_, PAN_Y, top), (px_, PAN_Y, top - 0.26)], 0.005, COPPER, segs=6)
        ball(f"Pan_Ladle_Bowl_{k}", 0.04, (px_, PAN_Y - 0.01, top - 0.29), COPPER, scale=(1, 1, 0.7))


# =====================================================================
#  FURNITURE SLOTS  (same names in every template)
#  size = (width, depth, height); front of the furniture faces local -Y
# =====================================================================
slot("stove",        (0.39, 0.37, 0.82), (CB_CX + 0.07, D - 0.265), z=HEARTH_Z, shape="box")
slot("wall_shelf",   (0.8, 0.24, 0.72), (2.94, D - 0.12), z=FLOOR_Z + 1.12, kind="wall", shape="shelf")
slot("pet",          (0.5, 0.5, 0.32), (2.32, 1.18), turn=90, shape="pet")   # by the rocking chair, facing the room
slot("table",        (1.2, 0.75, 0.76), (1.2, WIN_Y), turn=90, shape="table")
slot("chair",        (0.46, 0.5, 0.9), (1.95, 2.25), turn=-90, shape="chair")
slot("window_seat",  (1.3, 0.5, 0.48), (0.25, WIN_Y), turn=90, shape="sofa")
slot("rug",          (1.8, 1.2, 0.012), (1.3, WIN_Y), turn=90, kind="rug", shape="rug")
slot("pendant_lamp", (0.45, 0.45, 0.8), (1.2, WIN_Y), z=FLOOR_Z + 1.5, kind="hanging", shape="lamp")
slot("bed",          (0.9, 1.9, 0.45), (4.07, LOFT_Y0 + 1.02), z=LOFT_Z, kind="surface", shape="bed")


# =====================================================================
#  LIGHTS helper (the stove and the lantern carry their own lights)
# =====================================================================
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


light("Light_UnderLoft", "POINT", 14 if RAINY else 6, kelvin(LAMP_WARMTH + 400), (4.0, D - 0.8, LOFT_Z - 0.35), size=0.2)


# =====================================================================
#  PLACEHOLDER FURNITURE  (replaced when you add your own with add_furniture.py)
# =====================================================================
def build_stove():
    """Small cast-iron box stove (Morsø 1410 proportions, plain sides): legs, ribbed firebox, glazed door with
    a coil handle, top plate with a cooking ring, flue pipe, and a copper whistling kettle on top."""
    root, w, d, h = furniture_root("stove")
    for sx in (-1, 1):
        for sy in (-1, 1):
            lathe("Stove_Leg", [(0, 0), (0.024, 0), (0.018, 0.03), (0.026, 0.07), (0.03, 0.08), (0, 0.08)],
                  (sx * (w / 2 - 0.04), sy * (d / 2 - 0.04), 0), IRON, segs=12, parent=root)
    box("Stove_Base", (w, d, 0.03), (0, 0, 0.095), IRON, bevel=0.006, parent=root)
    bw, bd = w - 0.03, d - 0.03
    box("Stove_Body", (bw, bd, 0.36), (0, 0, 0.29), IRON, bevel=0.01, parent=root)
    for k in range(7):                                  # cast cooling ribs along both sides
        for sx in (-1, 1):
            box("Stove_Rib", (0.012, bd - 0.07, 0.014), (sx * (bw / 2 + 0.004), 0.01, 0.15 + k * 0.045), IRON,
                bevel=0.003, parent=root)
    box("Stove_Top", (w + 0.02, d + 0.02, 0.03), (0, 0, 0.485), IRON, bevel=0.008, parent=root)
    tube("Stove_Hob_Ring", ring_pts(0.075, 0.503, 32, -0.05, -0.03), 0.006, IRON, parent=root, closed=True, segs=6)
    cyl("Stove_Flue_Collar", 0.072, 0.05, (0, 0.08, 0.525), IRON, segs=24, parent=root)
    top = OPEN_TOP - HEARTH_Z + 0.02
    cyl("Stove_Flue_Pipe", 0.0625, top - 0.55, (0, 0.08, (top + 0.55) / 2), IRON, segs=24, bevel=0.002, parent=root)
    cyl("Stove_Flue_Damper", 0.008, 0.05, (0.085, 0.08, 0.72), BRASS, rot=(0, R(90), 0), segs=10, parent=root)
    fy = -bd / 2                                        # front face of the firebox
    box("Stove_Fire_Back", (bw - 0.1, 0.004, 0.16), (0, fy - 0.002, 0.295), mat("dark", 0.9, color="#1B1210"),
        bevel=0, parent=root)
    if STOVE_GLOW > 0:
        box("Stove_Embers", (bw - 0.12, 0.012, 0.022), (0, fy - 0.008, 0.226), EMBER, bevel=0.004, parent=root)
        for k in range(2):
            cyl("Stove_Fire_Log", 0.014, bw - 0.14, (0, fy - 0.009, 0.243 + k * 0.022), mat("bark", 0.9, color="#3A2A20"),
                rot=(0, R(90), R(k * 6)), segs=8, parent=root)
        rf = random.Random(SEED + 7)
        for k, (fx, fh, lean) in enumerate(((-0.075, 0.6, 0.25), (-0.03, 1.0, -0.1), (0.02, 1.25, 0.12), (0.055, 0.8, -0.2),
                                            (0.09, 0.55, 0.3), (-0.005, 0.7, 0.35))):
            fl = lathe(f"Stove_Flame_{k}", [(0.0005, 0), (0.016, 0.01), (0.02, 0.025), (0.013, 0.05), (0.0005, 0.08)],
                       (fx, fy - 0.011 - 0.002 * (k % 2), 0.235), FIRE if k % 3 else EMBER, segs=10,
                       rot=(R(rf.uniform(-5, 5)), R(lean * 40), 0), scale=(1, 0.35, fh), parent=root)
            no_shadow(fl)
    dz0, dz1 = 0.19, 0.4
    for nm, size, loc in (("Top", (bw - 0.06, 0.022, 0.05), (0, fy - 0.011, dz1 - 0.025)),
                          ("Bottom", (bw - 0.06, 0.022, 0.05), (0, fy - 0.011, dz0 + 0.025)),
                          ("Left", (0.04, 0.022, dz1 - dz0), (-(bw / 2 - 0.05), fy - 0.011, (dz0 + dz1) / 2)),
                          ("Right", (0.04, 0.022, dz1 - dz0), ((bw / 2 - 0.05), fy - 0.011, (dz0 + dz1) / 2))):
        box(f"Stove_Door_{nm}", size, loc, IRON, bevel=0.004, parent=root)
    no_shadow(box("Stove_Door_Glass", (bw - 0.16, 0.004, dz1 - dz0 - 0.09), (0, fy - 0.014, (dz0 + dz1) / 2),
                  mat("glass", 0.05, alpha=0.22, color="#2A2422"), bevel=0, parent=root))
    hx0 = bw / 2 - 0.12                                 # coil-spring door handle (stays cool)
    tube("Stove_Handle_Coil", [(hx0 + 0.07 * t, fy - 0.032 + 0.009 * math.cos(t * 2 * math.pi * 6),
                                0.3 + 0.009 * math.sin(t * 2 * math.pi * 6)) for t in (q / 72 for q in range(73))],
         0.0025, mat("metal", 0.3, metal=1.0, color="#C9CBCB"), parent=root, segs=5)
    box("Stove_Handle_Stem", (0.012, 0.02, 0.012), (hx0 - 0.004, fy - 0.022, 0.3), IRON, bevel=0.002, parent=root)
    box("Stove_Air_Slider", (0.16, 0.01, 0.026), (0, fy - 0.006, 0.145), IRON, bevel=0.003, parent=root)
    ball("Stove_Air_Knob", 0.009, (0.03, fy - 0.014, 0.145), BRASS, parent=root)
    box("Stove_Ash_Lip", (w - 0.02, 0.05, 0.012), (0, fy - 0.02, 0.118), IRON, bevel=0.003, parent=root)
    # copper whistling kettle (2.1 L): turned body, domed lid, swan spout with a whistle, arched handle
    kx, ky, kz = -0.04, -0.03, 0.5
    lathe("Kettle_Body", [(0, 0), (0.085, 0), (0.1, 0.01), (0.104, 0.04), (0.098, 0.08), (0.08, 0.115), (0.05, 0.14),
                          (0.035, 0.145), (0, 0.145)], (kx, ky, kz), COPPER, segs=40, parent=root)
    lathe("Kettle_Lid", [(0, 0), (0.042, 0), (0.042, 0.008), (0.014, 0.022), (0.016, 0.032), (0, 0.036)],
          (kx, ky, kz + 0.14), COPPER, segs=28, parent=root)
    ball("Kettle_Knob", 0.014, (kx, ky, kz + 0.186), TIMBER, parent=root)
    tube("Kettle_Spout", spline([(kx + 0.08, ky, kz + 0.04), (kx + 0.13, ky, kz + 0.08), (kx + 0.16, ky, kz + 0.15),
                                 (kx + 0.172, ky, kz + 0.17)], 4), 0.018, COPPER, parent=root, r2=0.008, segs=12)
    cyl("Kettle_Whistle", 0.012, 0.024, (kx + 0.176, ky, kz + 0.178), BRASS, rot=(0, R(55), 0), segs=12, parent=root)
    tube("Kettle_Handle", spline([(kx - 0.06, ky, kz + 0.115), (kx - 0.055, ky, kz + 0.2), (kx, ky, kz + 0.24),
                                  (kx + 0.055, ky, kz + 0.2), (kx + 0.06, ky, kz + 0.115)], 5), 0.006, COPPER,
         parent=root, segs=8)
    tube("Kettle_Grip", spline([(kx - 0.035, ky, kz + 0.225), (kx, ky, kz + 0.24), (kx + 0.035, ky, kz + 0.225)], 4),
         0.013, TIMBER, parent=root, segs=10)
    no_shadow(blobs("Kettle_Steam", [(0.02 + 0.01 * k, (kx + 0.19 + 0.02 * k, ky, kz + 0.22 + 0.06 * k), (1, 1, 0.8),
                                      (0, 0, 0)) for k in range(3)],
                    mat("steam", 0.9, color="#FFFFFF", alpha=0.35, emit=0.3), parent=root, segs=10))
    # the fire's glow inside, and on the hearth in front of the stove
    glow = STOVE_GLOW * (3.5 if RAINY else 1.0)
    fire = light("Light_Stove_Fire", "POINT", 9 * glow, kelvin(1700), (0, 0, 0), size=0.05)
    fire.parent, fire.location = root, (0, fy - 0.06, 0.3)
    spill = light("Light_Stove_Glow", "AREA", 10 * glow, kelvin(1800), (0, 0, 0), size=0.25)
    spill.parent, spill.location = root, (0, fy - 0.12, 0.3)
    spill.rotation_euler = (R(-75), 0, 0)               # facing out of the door and down onto the hearth


def jam_jar(name, x, y, z, parent, fill_hex, cover, r=0.035, h=0.09, word=""):
    """Jam jar with a gingham cloth cover tied with twine, and a paper label."""
    no_shadow(cyl(f"{name}_Glass", r, h, (x, y, z + h / 2), GLASS, bevel=0.006, parent=parent, segs=20))
    cyl(f"{name}_Fill", r - 0.004, h * 0.8, (x, y, z + h * 0.4 + 0.003), mat("jam", 0.35, color=fill_hex), bevel=0.004,
        parent=parent, segs=20)
    cyl(f"{name}_Lid", r + 0.002, 0.012, (x, y, z + h + 0.004), mat("metal", 0.4, metal=1.0, color="#B9B7B0"),
        parent=parent, segs=20)
    lathe(f"{name}_Cover", [(0, h + 0.016), (r * 0.7, h + 0.015), (r + 0.01, h + 0.008), (r + 0.016, h - 0.01),
                            (r + 0.018, h - 0.022), (0, h - 0.022)], (x, y, z), gingham(cover), segs=14, parent=parent)
    tube(f"{name}_Twine", ring_pts(r + 0.005, z + h - 0.003, 20, x, y), 0.002,
         mat("twine", 0.9, color=shade(COLORS["cream"], 0.78)), parent=parent, segs=4, closed=True)
    box(f"{name}_Label", (r * 1.3, 0.002, h * 0.36), (x, y - r - 0.001, z + h * 0.45), PAPER, bevel=0, parent=parent)
    if word:
        label(f"{name}_Word", word, 0.016, (x, y - r - 0.003, z + h * 0.45), INK, parent=parent, depth=0.0005)


def toadstool(name, x, y, z, parent, s=1.0, cap="accent_1"):
    """Felted toadstool figurine: a cream stem and a domed cap with white spots."""
    lathe(f"{name}_Stem", [(0, 0), (0.02 * s, 0), (0.016 * s, 0.03 * s), (0.014 * s, 0.05 * s), (0, 0.05 * s)], (x, y, z),
          KNIT, parent=parent, segs=16)
    lathe(f"{name}_Cap", [(0, 0.045 * s), (0.04 * s, 0.045 * s), (0.038 * s, 0.06 * s), (0.026 * s, 0.078 * s),
                          (0, 0.084 * s)], (x, y, z), M(cap, 0.95, "knit", scale=0.5), parent=parent, segs=20)
    blobs(f"{name}_Spots", [(0.006 * s, (x + math.cos(a) * 0.024 * s, y + math.sin(a) * 0.024 * s, z + 0.073 * s),
                             (1, 1, 0.5), (0, 0, 0)) for a in (0.3, 1.6, 2.7, 3.9, 5.1)], KNIT, parent=parent, segs=8)


def build_wall_shelf():
    """Pine jar shelf: shaped end boards, three shelves with plate rails, jam jars with gingham covers,
    honey, a big jar of pickled plums, and felt toadstool figurines with a little wooden hedgehog on top."""
    root, w, d, h = furniture_root("wall_shelf")
    hook_link(root, "website")
    for sx in (-1, 1):
        box("JarShelf_End", (0.018, d, h - 0.12), (sx * (w / 2 - 0.009), 0, 0.12 + (h - 0.12) / 2), PINE_V, bevel=0.003,
            parent=root)
        box("JarShelf_End_Foot", (0.018, d * 0.55, 0.12), (sx * (w / 2 - 0.009), d * 0.225, 0.06), PINE_V, bevel=0.004,
            parent=root)
    levels = (0.12, 0.38, h - 0.02)
    for k, z in enumerate(levels):
        box("JarShelf_Board", (w - 0.036 if k < 2 else w + 0.03, d - 0.01, 0.02), (0, 0.005, z), PINE, bevel=0.003,
            parent=root)
        if k < 2:
            tube("JarShelf_Rail", [(-w / 2 + 0.02, -d / 2 + 0.02, z + 0.06), (w / 2 - 0.02, -d / 2 + 0.02, z + 0.06)], 0.005,
                 PINE, parent=root, segs=8)
    box("JarShelf_Back_Rail", (w - 0.036, 0.012, 0.06), (0, d / 2 - 0.006, 0.06), PINE, bevel=0.002, parent=root)
    z0 = levels[0] + 0.01
    jam = [("#9E2238", "accent_1", "jam"), ("#D8962E", "accent_3", "honey"), ("#6E2846", "accent_1", "jam"),
           ("#E3A43A", "main", "")]
    for k, (col, cov, word) in enumerate(jam):
        jam_jar(f"Jar_{k}", -w / 2 + 0.09 + k * 0.105, -0.02, z0, root, col, cov, word=word)
    no_shadow(cyl("Honey_Pot_Glass", 0.04, 0.09, (w / 2 - 0.12, -0.01, z0 + 0.045), GLASS, bevel=0.01, parent=root, segs=6))
    cyl("Honey_Pot_Fill", 0.035, 0.07, (w / 2 - 0.12, -0.01, z0 + 0.038), mat("honey", 0.2, color="#E8A53A", emit=0.1),
        bevel=0.006, parent=root, segs=6)
    lathe("Honey_Dipper", [(0, 0), (0.006, 0), (0.006, 0.1), (0.014, 0.11), (0.016, 0.13), (0.014, 0.15), (0.006, 0.155),
                           (0.006, 0.2), (0, 0.2)], (w / 2 - 0.12, -0.01, z0 + 0.03), PINE, parent=root, segs=10)
    z1 = levels[1] + 0.01
    px_, py_ = -w / 2 + 0.13, 0.0                        # Weck-style mould jar of pickled plums (H10.5 dia 10 cm)
    no_shadow(lathe("Plum_Jar_Glass", [(0, 0), (0.05, 0), (0.055, 0.105), (0.05, 0.105), (0.0, 0.105)], (px_, py_, z1), GLASS,
                    parent=root, segs=28))
    blobs("Plum_Jar_Plums", [(0.02, (px_ + math.cos(a) * rr_, py_ + math.sin(a) * rr_, z1 + 0.02 + 0.03 * (k // 5)),
                              (1, 1, 1), (0, 0, 0)) for k, (a, rr_) in enumerate(
        [(q * 1.3, 0.026 if q % 5 else 0.0) for q in range(14)])], mat("plum", 0.35, color="#7A2340"), parent=root, segs=10)
    cyl("Plum_Jar_Lid", 0.056, 0.008, (px_, py_, z1 + 0.11), GLASS, parent=root, segs=28)
    for sx in (-1, 1):
        box("Plum_Jar_Clip", (0.006, 0.004, 0.04), (px_ + sx * 0.055, py_, z1 + 0.09), mat("metal", 0.3, metal=1.0,
            color="#C9CBCB"), bevel=0.001, parent=root)
    label("Plum_Jar_Word", "plums", 0.016, (px_, py_ - 0.056, z1 + 0.05), INK, parent=root, depth=0.0005)
    box("Plum_Jar_Label", (0.07, 0.002, 0.028), (px_, py_ - 0.053, z1 + 0.05), PAPER, bevel=0, parent=root)
    for k in range(3):                                   # stacked stoneware bowls
        lathe("Shelf_Bowl", [(0, 0), (0.04, 0), (0.07, 0.04), (0.066, 0.042), (0.037, 0.005), (0, 0.005)],
              (0.07, 0.0, z1 + k * 0.022), M("accent_3", 0.3, "ceramic") if k == 1 else CERAMIC, parent=root, segs=24)
    for k in range(2):
        jam_jar(f"Jar_Top_{k}", w / 2 - 0.2 + k * 0.1, -0.01, z1, root, ("#C5502E", "#8FAE4E")[k], ("accent_2", "main")[k],
                r=0.03, h=0.075)
    z2 = levels[2] + 0.01
    toadstool("Toadstool_A", -0.25, -0.01, z2, root, s=1.1)
    toadstool("Toadstool_B", -0.17, 0.03, z2, root, s=0.75, cap="accent_2")
    toadstool("Toadstool_C", -0.11, -0.03, z2, root, s=0.55)
    hx, hy = 0.08, -0.01                                 # carved wooden hedgehog: body, darker spiny back, nose
    ball("Hedgehog_Body", 0.04, (hx, hy, z2 + 0.03), PINE, scale=(1.4, 1, 0.8), parent=root)
    blobs("Hedgehog_Spines", [(0.012, (hx + 0.01 + 0.04 * math.cos(a) * 0.9, hy + 0.032 * math.sin(a) * 0.9,
                                       z2 + 0.045 + 0.012 * math.sin(b)), (1, 1, 1.5), (0, 0, 0))
                              for a in (q * 0.75 for q in range(9)) for b in (0, 1.5)],
          M("timber", 0.73, "wood", along="Z"), parent=root, segs=6)
    ball("Hedgehog_Nose", 0.008, (hx - 0.058, hy, z2 + 0.027), mat("dark", 0.4), parent=root)
    lathe("Shelf_Vase", [(0, 0), (0.03, 0), (0.04, 0.05), (0.02, 0.1), (0.024, 0.12), (0, 0.115)], (0.26, 0.0, z2),
          M("main", 0.31, "ceramic"), parent=root, segs=20)
    for k in range(5):
        a = k * 1.25
        top = (0.26 + math.cos(a) * 0.05, math.sin(a) * 0.03, z2 + 0.22 + 0.03 * math.sin(k))
        tube("Shelf_Vase_Stem", [(0.26, 0.0, z2 + 0.1), top], 0.002, mat("plant", 0.7), parent=root, segs=4)
        ball("Shelf_Vase_Flower", 0.014, top, mat("flower", 0.6, color=("#FFFFFF", COLORS["accent_2"])[k % 2]),
             scale=(1, 1, 0.5), parent=root)


def build_pet():
    """A ginger tabby asleep in a round wicker basket on a cushion."""
    root, w, d, h = furniture_root("pet")
    lathe("Pet_Basket", [(0, 0), (0.2, 0), (0.235, 0.1), (0.245, 0.12), (0.23, 0.125), (0.215, 0.105), (0.18, 0.02),
                         (0, 0.02)], (0, 0, 0), RUSH, segs=36, parent=root)
    tube("Pet_Basket_Rim", ring_pts(0.238, 0.122, 36), 0.014, RUSH, parent=root, closed=True, segs=8)
    cyl("Pet_Cushion", 0.2, 0.06, (0, 0, 0.06), gingham("accent_3"), bevel=0.025, segs=32, parent=root)
    cz = 0.09
    ball("Cat_Body", 0.15, (0.02, 0.01, cz + 0.08), CAT, scale=(1.2, 0.95, 0.62), parent=root)
    ball("Cat_Chest", 0.07, (-0.09, -0.06, cz + 0.06), KNIT, scale=(1, 1, 0.8), parent=root)
    hx, hy, hz = -0.11, -0.07, cz + 0.11                 # head tucked in on the front paws, facing the room
    ball("Cat_Head", 0.072, (hx, hy, hz), CAT, scale=(1.05, 0.95, 0.85), parent=root)
    ball("Cat_Muzzle", 0.03, (hx - 0.02, hy - 0.055, hz - 0.02), KNIT, scale=(1.3, 0.8, 0.8), parent=root)
    ball("Cat_Nose", 0.006, (hx - 0.022, hy - 0.08, hz - 0.006), mat("nose", 0.5, color="#D9837A"), parent=root)
    for sx in (-1, 1):
        lathe("Cat_Ear", [(0, 0), (0.028, 0), (0, 0.05)], (hx + sx * 0.045, hy + 0.01, hz + 0.045), CAT, segs=3,
              rot=(R(-12), R(sx * 18), R(30)), parent=root)
        tube("Cat_Eye", spline([(hx + sx * 0.03 - 0.022, hy - 0.06, hz + 0.012), (hx + sx * 0.03 - 0.012, hy - 0.066,
                                hz + 0.006), (hx + sx * 0.03, hy - 0.064, hz + 0.012)], 3), 0.0025, mat("dark", 0.5),
             parent=root, segs=5)
    for k in range(2):
        ball("Cat_Paw", 0.026, (-0.17 + k * 0.05, -0.12 + k * 0.01, cz + 0.035), KNIT, scale=(1.3, 1, 0.7), parent=root)
    tail = spline([(0.18, 0.05, cz + 0.05), (0.15, -0.1, cz + 0.04), (0.02, -0.16, cz + 0.035), (-0.12, -0.15, cz + 0.035)], 6)
    tube("Cat_Tail", tail, 0.026, CAT, parent=root, r2=0.02, segs=10)
    stripes = [(0.03, (0.02 + 0.16 * math.cos(a) * 0.9, 0.01 + 0.12 * math.sin(a) * 0.9, cz + 0.13), (0.5, 1.6, 0.35),
                (0, 0, a)) for a in (q * 0.5 + 0.3 for q in range(7))]
    stripes += [(0.012, (hx + 0.01 + k * 0.02, hy + 0.01, hz + 0.06), (0.6, 2.0, 0.4), (0, 0, 0.3)) for k in range(3)]
    blobs("Cat_Stripes", stripes, CAT_STRIPE, parent=root, segs=10)


def turned_leg(name, x, y, h, parent, mat_=None):
    """Turned table leg with a square block at the top (where the apron joins)."""
    lathe(name, [(0, 0), (0.022, 0), (0.026, 0.03), (0.02, 0.07), (0.024, 0.2), (0.03, 0.34), (0.022, 0.42),
                 (0.026, 0.46), (0.02, h - 0.2), (0.026, h - 0.15), (0, h - 0.15)], (x, y, 0), mat_ or PINE_V, segs=16,
          parent=parent)
    box(f"{name}_Block", (0.055, 0.055, 0.14), (x, y, h - 0.105), mat_ or PINE_V, bevel=0.004, parent=parent)


def build_table():
    """Scrubbed-pine farmhouse table: three top boards with bread-board ends, apron with a drawer,
    turned legs. On it: the open sketchbook (your hero project), paints, a brush jar, a teapot, cups, a posy."""
    root, w, d, h = furniture_root("table")
    top = h - 0.035
    for k in range(3):
        box("Table_Board", (w - 0.1, d / 3 - 0.004, 0.035), (0, -d / 3 + k * d / 3, top + 0.0175), SCRUB, bevel=0.003,
            parent=root)
    for sx in (-1, 1):
        box("Table_Breadboard_End", (0.05, d, 0.035), (sx * (w / 2 - 0.025), 0, top + 0.0175),
            M("scrub", 0.81, "wood", along="Y", color=mix_hex(COLORS["wood"], COLORS["cream"], 0.35)), bevel=0.003,
            parent=root)
    for sy in (-1, 1):
        box("Table_Apron", (w - 0.2, 0.022, 0.1), (0, sy * (d / 2 - 0.07), top - 0.05), PINE, bevel=0.003, parent=root)
    for sx in (-1, 1):
        box("Table_Apron_End", (0.022, d - 0.2, 0.1), (sx * (w / 2 - 0.12), 0, top - 0.05), PINE_Y, bevel=0.003, parent=root)
    box("Table_Drawer", (0.42, 0.024, 0.08), (0.12, -(d / 2 - 0.07) - 0.006, top - 0.05), PINE, bevel=0.003, parent=root)
    ball("Table_Drawer_Knob", 0.014, (0.12, -(d / 2 - 0.07) - 0.025, top - 0.05), TIMBER, parent=root)
    for sx in (-1, 1):
        for sy in (-1, 1):
            turned_leg("Table_Leg", sx * (w / 2 - 0.12), sy * (d / 2 - 0.07), top, root)
    # open A4 sketchbook turned towards the camera: the right page is a picture hook
    sb = empty("Sketchbook", (-0.14, -0.08, h), rot=(0, 0, R(-45)), parent=root)
    box("Sketchbook_Cover", (0.45, 0.31, 0.005), (0, 0, 0.0025), M("accent_3", 0.85, "fabric"), bevel=0.002, parent=sb)
    for sx in (-1, 1):
        box("Sketchbook_Pages", (0.215, 0.297, 0.01), (sx * 0.11, 0, 0.01), PAPER, bevel=0.002, rot=(0, R(sx * 2.5), 0),
            parent=sb)
    box("Sketchbook_Spine", (0.012, 0.3, 0.008), (0, 0, 0.012), mat("dark", 0.6), bevel=0.002, parent=sb)
    pic = hook_image("board", 1, (0.19, 0.27), (0.112, 0, 0.0205), rot=(R(-90), R(2.5), 0), parent=sb,
                     default_key="cream")
    wc = [((0.075, (0.112, 0.06, 0.0222), (1.2, 0.9, 0.03), (0, 0, 0)), "accent_3"),
          ((0.06, (0.08, -0.06, 0.0224), (1.5, 0.75, 0.03), (0, 0, 0)), "main"),
          ((0.05, (0.15, -0.07, 0.0226), (1.3, 0.7, 0.03), (0, 0, 0)), "plant"),
          ((0.025, (0.16, 0.08, 0.0228), (1, 1, 0.03), (0, 0, 0)), "accent_2")]
    hook_default(pic, *[blobs(f"Sketchbook_Wash_{k}", [p], mat(key, 0.9), parent=sb, segs=12)
                        for k, (p, key) in enumerate(wc)],
                 box("Sketchbook_Cottage", (0.03, 0.025, 0.002), (0.1, -0.03, 0.0232), mat("cream", 0.6), bevel=0,
                     parent=sb),
                 box("Sketchbook_Roof", (0.036, 0.012, 0.002), (0.1, -0.012, 0.0233), mat("accent_1", 0.6), bevel=0,
                     parent=sb))
    for k in range(5):                                   # pencil studies on the left page
        box("Sketchbook_Pencil_Line", (0.12 - 0.02 * (k % 3), 0.0015, 0.0005), (-0.11, 0.08 - k * 0.035, 0.0205), INK,
            bevel=0, rot=(0, R(-2.5), 0), parent=sb)
    tube("Sketchbook_Pencil", [(-0.06, -0.12, 0.022), (0.08, -0.17, 0.022)], 0.0035, mat("accent_2", 0.5), parent=sb, segs=6)
    # watercolour tin with 12 pans, a jar of brushes in tinted water
    tin = empty("Paint_Tin", (0.26, -0.18, h), rot=(0, 0, R(-20)), parent=root)
    box("Paint_Tin_Base", (0.17, 0.08, 0.014), (0, 0, 0.007), mat("dark", 0.4, metal=0.6), bevel=0.003, parent=tin)
    pans = ["#C8463A", "#E58A3A", "#EBC64A", "#86B04A", "#3F8A5A", "#4E86C4", "#2E4E8E", "#8A5AA6", "#7A4A2E", "#C9A07A",
            "#2E2B29", "#F1E6D2"]
    for k, c in enumerate(pans):
        box("Paint_Pan", (0.022, 0.026, 0.004), (-0.07 + (k % 6) * 0.028, -0.017 + (k // 6) * 0.034, 0.015),
            mat("paint", 0.4, color=c), bevel=0.001, parent=tin)
    jx, jy = 0.42, 0.14
    no_shadow(cyl("Brush_Jar", 0.035, 0.1, (jx, jy, h + 0.05), GLASS, bevel=0.005, parent=root, segs=20))
    no_shadow(cyl("Brush_Water", 0.031, 0.06, (jx, jy, h + 0.032), mat("water", 0.1, color="#9FB7C9", alpha=0.5),
                  bevel=0.003, parent=root, segs=20))
    for k in range(3):
        a = R(-12 + k * 12)
        tube("Brush", [(jx, jy, h + 0.01), (jx + math.sin(a) * 0.06, jy + 0.01 * k, h + 0.21)], 0.004,
             mat("brush", 0.4, color=("#C8463A", "#2E2B29", "#E0B57A")[k]), parent=root, segs=6)
        cyl("Brush_Ferrule", 0.0045, 0.02, (jx + math.sin(a) * 0.063, jy + 0.01 * k, h + 0.22),
            mat("metal", 0.3, metal=1.0, color="#C9CBCB"), rot=(0, a, 0), segs=8, parent=root)
    # glazed teapot on a cork trivet and two cups
    tx, ty = 0.33, 0.16
    cyl("Teapot_Trivet", 0.09, 0.008, (tx - 0.18, ty, h + 0.004), RUSH, segs=24, parent=root)
    tpx = tx - 0.18
    pot = M("accent_3", 0.29, "ceramic")
    lathe("Teapot_Body", [(0, 0), (0.06, 0), (0.085, 0.04), (0.088, 0.07), (0.075, 0.11), (0.045, 0.13), (0, 0.13)],
          (tpx, ty, h + 0.008), pot, segs=32, parent=root)
    lathe("Teapot_Lid", [(0, 0), (0.045, 0), (0.03, 0.02), (0.012, 0.028), (0.014, 0.04), (0, 0.045)], (tpx, ty, h + 0.135),
          pot, segs=24, parent=root)
    tube("Teapot_Spout", spline([(tpx + 0.075, ty, h + 0.05), (tpx + 0.12, ty, h + 0.09), (tpx + 0.135, ty, h + 0.13)], 4),
         0.016, pot, parent=root, r2=0.008, segs=10)
    tube("Teapot_Handle", spline([(tpx - 0.075, ty, h + 0.11), (tpx - 0.13, ty, h + 0.09), (tpx - 0.12, ty, h + 0.04),
                                  (tpx - 0.08, ty, h + 0.03)], 4), 0.008, pot, parent=root, segs=8)
    for k, (cx, cy) in enumerate(((0.06, 0.24), (-0.36, 0.2))):
        cm = CERAMIC if k == 0 else M("main", 0.3, "ceramic")
        lathe("Table_Cup", [(0, 0), (0.03, 0), (0.042, 0.07), (0.039, 0.07), (0.028, 0.006), (0, 0.006)], (cx, cy, h), cm,
              segs=22, parent=root)
        cyl("Table_Cup_Tea", 0.037, 0.002, (cx, cy, h + 0.058), mat("tea", 0.2, color="#8A4E26"), bevel=0, parent=root)
        tube("Table_Cup_Handle", spline([(cx + 0.04, cy, h + 0.055), (cx + 0.06, cy, h + 0.045), (cx + 0.058, cy, h + 0.02),
                                         (cx + 0.035, cy, h + 0.015)], 4), 0.004, cm, parent=root, segs=6)
    # a posy of meadow flowers in a jam jar at the window end
    px_, py_ = -0.48, 0.15
    no_shadow(cyl("Posy_Jar", 0.032, 0.09, (px_, py_, h + 0.045), GLASS, bevel=0.005, parent=root, segs=18))
    flowers = []
    for k in range(9):
        a = k * 0.7
        tip = (px_ + math.cos(a) * 0.05, py_ + math.sin(a) * 0.05, h + 0.2 + 0.04 * math.sin(k * 1.7))
        tube("Posy_Stem", [(px_, py_, h + 0.04), tip], 0.002, mat("plant", 0.7), parent=root, segs=4)
        flowers.append((0.016, tip, (1, 1, 0.35), (0, 0, 0)))
    blobs("Posy_Daisies", flowers[::2], mat("flower", 0.6, color="#FFFFFF"), parent=root, segs=10)
    blobs("Posy_Buttercups", flowers[1::2], mat("buttercup", 0.5, color=COLORS["accent_2"]), parent=root, segs=10)


def windsor_chair(root, seat_h=0.45, wood=None):
    """Bow-back Windsor side chair: saddle seat, four splayed legs with an H-stretcher, steam-bent bow and
    six spindles. Built in root's space, front = -y. W46 D50 H90 cm."""
    wood = wood or PINE_V
    box("Windsor_Seat", (0.44, 0.42, 0.04), (0, 0, seat_h - 0.02), PINE, bevel=0.014, parent=root)
    legs = {}
    for sx in (-1, 1):
        for sy in (-1, 1):
            topp = (sx * 0.15, sy * 0.13, seat_h - 0.04)
            foot = (sx * 0.2, sy * 0.19, 0.0)
            legs[(sx, sy)] = (Vector(foot), Vector(topp))
            tube("Windsor_Leg", [foot, topp], 0.014, wood, parent=root, r2=0.019, segs=10)
    for sx in (-1, 1):
        a, b = legs[(sx, -1)], legs[(sx, 1)]
        pa, pb = a[0].lerp(a[1], 0.4), b[0].lerp(b[1], 0.4)
        tube("Windsor_Side_Stretcher", [pa, pb], 0.011, wood, parent=root, segs=8)
    mid = [legs[(sx, -1)][0].lerp(legs[(sx, -1)][1], 0.4).lerp(legs[(sx, 1)][0].lerp(legs[(sx, 1)][1], 0.4), 0.5)
           for sx in (-1, 1)]
    tube("Windsor_Mid_Stretcher", mid, 0.011, wood, parent=root, segs=8)

    def bow(phi):
        return Vector((-0.18 * math.cos(phi), 0.17 + 0.05 * math.sin(phi), seat_h + 0.45 * math.sin(phi)))
    tube("Windsor_Bow", [bow(math.pi * q / 24) for q in range(25)], 0.014, wood, parent=root, segs=10)
    for k in range(6):
        phi = math.pi * (k + 1) / 7
        t = bow(phi)
        tube("Windsor_Spindle", [(t.x * 0.85, 0.15, seat_h), (t.x, t.y, t.z - 0.01)], 0.0075, wood, parent=root, segs=8)


def ladderback_chair(root, seat_h=0.45):
    """Painted rush-seat ladder-back chair (decor): turned back posts with finials, three curved slats, rush seat."""
    for sx in (-1, 1):
        cyl("Ladderback_Back_Post", 0.017, 0.98, (sx * 0.2, 0.18, 0.49), SAGE_PAINT, segs=12, bevel=0.003, parent=root)
        ball("Ladderback_Finial", 0.022, (sx * 0.2, 0.18, 0.99), SAGE_PAINT, scale=(1, 1, 1.3), parent=root)
        cyl("Ladderback_Front_Leg", 0.017, seat_h, (sx * 0.21, -0.19, seat_h / 2), SAGE_PAINT, segs=12, bevel=0.003,
            parent=root)
        for zz in (0.14, 0.26):
            cyl("Ladderback_Side_Stretcher", 0.01, 0.37, (sx * 0.205, 0.0, zz), SAGE_PAINT, rot=(R(90), 0, 0), segs=8,
                parent=root)
    for zz in (0.18,):
        cyl("Ladderback_Front_Stretcher", 0.01, 0.42, (0, -0.19, zz), SAGE_PAINT, rot=(0, R(90), 0), segs=8, parent=root)
    box("Ladderback_Rush_Seat", (0.42, 0.38, 0.03), (0, 0.0, seat_h - 0.01), RUSH, bevel=0.01, parent=root)
    for k, zz in enumerate((0.62, 0.76, 0.9)):
        tube("Ladderback_Slat", spline([(-0.19, 0.18, zz), (0, 0.205, zz), (0.19, 0.18, zz)], 6), 0.012, SAGE_PAINT,
             parent=root, segs=6)
        box("Ladderback_Slat_Board", (0.36, 0.012, 0.06), (0, 0.2, zz), SAGE_PAINT, bevel=0.004, parent=root)


def build_chair():
    root, w, d, h = furniture_root("chair")
    windsor_chair(root)


def build_window_seat():
    """Built-in window seat: plinth, panelled painted front, pine lift-up lid, piped sage cushion, two cushions."""
    root, w, d, h = furniture_root("window_seat")
    box("WindowSeat_Plinth", (w, d - 0.06, 0.08), (0, 0.03, 0.04), mat("dark", 0.8), bevel=0.003, parent=root)
    box("WindowSeat_Carcass", (w, d - 0.02, h - 0.105), (0, 0.01, 0.08 + (h - 0.105) / 2), TRIM, bevel=0.004, parent=root)
    fy = -d / 2 + 0.002
    for k in range(3):                                   # three fielded panels in a frame
        px_ = -w / 2 + w * (k + 0.5) / 3
        box("WindowSeat_Panel", (w / 3 - 0.1, 0.012, h - 0.25), (px_, fy - 0.004, 0.08 + (h - 0.105) / 2), TRIM, bevel=0.01,
            parent=root)
    box("WindowSeat_Lid", (w + 0.02, d + 0.02, 0.025), (0, 0.0, h - 0.0125), PINE, bevel=0.004, parent=root)
    box("WindowSeat_Cushion", (w - 0.04, d - 0.06, 0.07), (0, 0.02, h + 0.035), FABRIC, bevel=0.022, parent=root)
    tube("WindowSeat_Piping", [(-w / 2 + 0.03, -d / 2 + 0.015, h + 0.06), (w / 2 - 0.03, -d / 2 + 0.015, h + 0.06)],
         0.006, M("main", 0.91, "fabric", color=shade(COLORS["main"], 0.8)), parent=root, segs=6)
    for k, (px_, m_, tilt) in enumerate(((-0.33, gingham("accent_1"), -8), (0.3, KNIT_HONEY, 10))):
        box("WindowSeat_Pillow", (0.4, 0.13, 0.36), (px_, d / 2 - 0.1, h + 0.22), m_, bevel=0.05,
            rot=(R(-14), 0, R(tilt)), parent=root)
    # woven picnic hamper (40 x 28 x 20 cm) tucked at the end of the seat, on the floor
    hp = empty("Hamper", (-w / 2 - 0.12, -d / 2 - 0.12, 0), rot=(0, 0, R(-25)), parent=root)
    box("Hamper_Body", (0.4, 0.28, 0.2), (0, 0, 0.1), RUSH, bevel=0.012, parent=hp)
    box("Hamper_Lid", (0.41, 0.29, 0.03), (0, 0, 0.21), RUSH, bevel=0.01, parent=hp)
    for sx in (-1, 1):
        box("Hamper_Strap", (0.03, 0.3, 0.012), (sx * 0.1, 0, 0.226), mat("leather", 0.5, color=shade(COLORS["timber"], 0.9)),
            bevel=0.003, parent=hp)
    tube("Hamper_Handle", spline([(-0.12, 0, 0.226), (-0.06, 0, 0.3), (0.06, 0, 0.3), (0.12, 0, 0.226)], 4), 0.01,
         RUSH, parent=hp, segs=8)
    sheet("Hamper_Cloth", 8, 4, lambda u, v: (-0.18 + u * 0.16, -0.145 - 0.02 * v, 0.2 - v * 0.08), gingham("accent_1"),
          parent=hp)


def build_rug():
    """Oval braided rag rug (120 x 180 cm): 13 braided rounds around a centre line, in alternating colours."""
    root, w, d, h = furniture_root("rug")
    c = (w - d) / 2                                    # half-length of the straight centre line
    keys = ["accent_1", "cream", "main", "accent_2", "cream", "accent_3", "accent_1", "main", "cream", "accent_2",
            "accent_3", "cream", "accent_1"]
    n = 13
    for k in range(n):
        rr = 0.035 + k * (d / 2 - 0.06) / (n - 1)
        pts = []
        for q in range(48):
            a = 2 * math.pi * q / 48
            cx = c if math.cos(a) >= 0 else -c
            pts.append((cx + rr * math.cos(a), rr * math.sin(a), 0))
        o = tube(f"Rug_Braid_{k}", pts, 0.021, M(keys[k], 0.97, "knit", scale=1.5), parent=root, segs=8, closed=True)
        o.scale, o.location = (1, 1, 0.3), (0, 0, 0.007)


def build_pendant_lamp():
    """Rice-paper globe lantern (dia 45 cm) on a cloth flex from the iron swing-arm, with a warm bulb inside."""
    root, w, d, h = furniture_root("pendant_lamp")
    cz, r = 0.25, 0.225
    prof = []
    for q in range(41):
        z = -r + 2 * r * q / 40
        rr = math.sqrt(max(0.0, r * r - z * z)) * (0.985 if q % 2 else 1.0)    # the paper sits in and out of the ribs
        prof.append((max(rr, 0.0), z * 0.92))
    prof[0], prof[-1] = (0.05, prof[0][1] + 0.01), (0.045, prof[-1][1] - 0.01)
    no_shadow(lathe("Lantern_Paper", prof, (0, 0, cz), LANTERN, segs=48, parent=root))
    for sz in (-1, 1):
        tube("Lantern_Collar", ring_pts(0.05 if sz < 0 else 0.045, cz + sz * (r * 0.92 - 0.012), 20), 0.004,
             mat("dark", 0.5), parent=root, closed=True, segs=5)
    tube("Lantern_Flex", [(0, 0, cz + r * 0.9), (0, 0, ARM_Z - FLOOR_Z - 1.5 - 0.02)], 0.004, mat("cream", 0.6), parent=root,
         segs=6)
    lamp = light("Light_Lantern", "POINT", LAMP_STRENGTH if RAINY else 4, kelvin(LAMP_WARMTH), (0, 0, 0), size=0.12)
    lamp.parent, lamp.location = root, (0, 0, cz)


def build_bed():
    """Loft bed: low pine platform and headboard, single mattress, patchwork quilt, pillows and a knit throw."""
    root, w, d, h = furniture_root("bed")
    box("Bed_Platform", (w, d, 0.1), (0, 0, 0.05), PINE_Y, bevel=0.005, parent=root)
    box("Bed_Headboard", (w, 0.035, 0.36), (0, d / 2 - 0.0175, 0.18), PINE, bevel=0.012, parent=root)
    mz = 0.1 + 0.09
    box("Bed_Mattress", (w - 0.04, d - 0.06, 0.18), (0, -0.01, mz), LINEN, bevel=0.03, parent=root)
    qz = mz + 0.09
    cols, rows_ = 6, 8
    qw, ql = w + 0.04, d - 0.38
    sq_w, sq_l = qw / cols, ql / rows_
    pal = ["accent_1", "accent_2", "accent_3", "main", "cream"]
    rr = random.Random(SEED + 9)
    patches = {k: [] for k in pal}
    gpatch = []
    y0 = -d / 2 + 0.02
    for i in range(cols):
        for j in range(rows_):
            key = rr.choice(pal)
            part = ((sq_w - 0.006, sq_l - 0.006, 0.02), (-qw / 2 + sq_w * (i + 0.5), y0 + sq_l * (j + 0.5), qz + 0.008), (0, 0, 0))
            (gpatch if rr.random() < 0.15 else patches[key]).append(part)
    for key, parts in patches.items():
        if parts:
            boxes(f"Quilt_Patches_{key}", parts, M(key, 0.93, "fabric"), bevel=0.004, parent=root)
    if gpatch:
        boxes("Quilt_Patches_Gingham", gpatch, gingham("accent_1"), bevel=0.004, parent=root)
    box("Quilt_Backing", (qw, ql, 0.014), (0, y0 + ql / 2, qz - 0.002), M("main", 0.94, "fabric"), bevel=0.004, parent=root)
    for sx in (-1, 1):                                   # the quilt drops over both sides and the foot
        box("Quilt_Drop", (0.014, ql, 0.15), (sx * (qw / 2 + 0.001), y0 + ql / 2, qz - 0.07), M("main", 0.94, "fabric"),
            bevel=0.005, parent=root)
    box("Quilt_Drop_Foot", (qw, 0.014, 0.15), (0, y0 - 0.001, qz - 0.07), M("main", 0.94, "fabric"), bevel=0.005, parent=root)
    for k, sx in enumerate((-0.2, 0.2)):
        box("Bed_Pillow", (0.4, 0.27, 0.12), (sx, d / 2 - 0.2, qz + 0.04), LINEN if k == 0 else gingham("accent_3"),
            bevel=0.05, rot=(R(-12), 0, R(4 - 8 * k)), parent=root)
    box("Bed_Throw", (w - 0.12, 0.28, 0.05), (0, -d / 2 + 0.24, qz + 0.035), KNIT_HONEY, bevel=0.02, parent=root)
    box("Bed_Book", (0.15, 0.21, 0.025), (0.22, -0.15, qz + 0.03), M("accent_1", 0.7, "paper"), bevel=0.003,
        rot=(0, 0, R(20)), parent=root)


PLACEHOLDERS = {
    "stove": build_stove, "wall_shelf": build_wall_shelf, "pet": build_pet, "table": build_table, "chair": build_chair,
    "window_seat": build_window_seat, "rug": build_rug, "pendant_lamp": build_pendant_lamp, "bed": build_bed,
}

ARM_Z = FLOOR_Z + 2.48                              # the lantern's wrought-iron swing-arm on the left wall
if SHOW_PLACEHOLDER_FURNITURE:
    for slot_name, build in PLACEHOLDERS.items():
        build()

# A second, mismatched chair at the front end of the table: a painted ladder-back, turned a little.
# (It stands clear of the hearth so the stove and the kettle stay in view.)
ladderback_chair(empty("Chair_Ladderback", (1.16, 1.58, FLOOR_Z), rot=(0, 0, R(172))))
def rocking_chair(root, seat_h=0.42):
    """Windsor rocking chair (decor): legs set into two curved rockers, a tall bow back with spindles, arms,
    and a knitted throw over the back. Built in root's space, front = -y."""
    wood = PINE_V
    box("Rocker_Seat", (0.46, 0.44, 0.04), (0, 0, seat_h - 0.02), PINE, bevel=0.014, parent=root)
    for sx in (-1, 1):
        run = [(sx * 0.21, -0.42, 0.09), (sx * 0.21, -0.2, 0.02), (sx * 0.21, 0.1, 0.03), (sx * 0.21, 0.36, 0.11)]
        tube("Rocker_Runner", spline(run, 6), 0.016, PINE_Y, parent=root, segs=8)
        for sy, zf in ((-1, 0.025), (1, 0.035)):
            tube("Rocker_Leg", [(sx * 0.21, sy * 0.17, zf), (sx * 0.17, sy * 0.15, seat_h - 0.04)], 0.016, wood,
                 parent=root, r2=0.019, segs=10)
        tube("Rocker_Arm", spline([(sx * 0.22, 0.18, seat_h + 0.25), (sx * 0.25, -0.05, seat_h + 0.24),
                                   (sx * 0.24, -0.2, seat_h + 0.22)], 5), 0.017, PINE, parent=root, segs=8)
        tube("Rocker_Arm_Post", [(sx * 0.2, -0.17, seat_h), (sx * 0.24, -0.18, seat_h + 0.22)], 0.012, wood,
             parent=root, segs=8)

    def bow(phi):
        return Vector((-0.2 * math.cos(phi), 0.2 + 0.07 * math.sin(phi), seat_h + 0.62 * math.sin(phi)))
    tube("Rocker_Bow", [bow(math.pi * q / 24) for q in range(25)], 0.015, wood, parent=root, segs=10)
    for k in range(7):
        t = bow(math.pi * (k + 1) / 8)
        tube("Rocker_Spindle", [(t.x * 0.85, 0.17, seat_h), (t.x, t.y, t.z - 0.01)], 0.0075, wood, parent=root, segs=8)
    box("Rocker_Cushion", (0.42, 0.4, 0.05), (0, -0.01, seat_h + 0.025), gingham("accent_3"), bevel=0.02, parent=root)
    sheet("Rocker_Throw", 10, 12, lambda u, v: (-0.17 + 0.34 * u, 0.245 + 0.03 * math.sin(v * 3) + 0.01 * math.sin(u * 9),
                                                seat_h + 0.62 - v * 0.5), KNIT_HONEY, parent=root)


# A rocking chair by the hearth with a basket of knitting beside it.
rocking_chair(empty("Chair_Rocking", (3.05, 1.35, FLOOR_Z), rot=(0, 0, R(-55))))
yb = (3.55, 1.05)
lathe("Yarn_Basket", [(0, 0), (0.15, 0), (0.18, 0.2), (0.19, 0.21), (0.175, 0.21), (0.14, 0.02), (0, 0.02)],
      (yb[0], yb[1], FLOOR_Z), RUSH, segs=28)
blobs("Yarn_Balls", [(0.065, (yb[0] - 0.05, yb[1] + 0.03, FLOOR_Z + 0.2), (1, 1, 1), (0, 0, 0)),
                     (0.06, (yb[0] + 0.06, yb[1] - 0.02, FLOOR_Z + 0.21), (1, 1, 1), (0, 0, 0))],
      M("accent_1", 0.95, "knit", scale=2), segs=16)
ball("Yarn_Ball_Blue", 0.055, (yb[0] + 0.01, yb[1] + 0.1, FLOOR_Z + 0.22), M("accent_3", 0.95, "knit", scale=2))
for k in range(2):
    tube("Knitting_Needle", [(yb[0] - 0.08 + k * 0.03, yb[1] - 0.05, FLOOR_Z + 0.2),
                             (yb[0] - 0.02 + k * 0.05, yb[1] + 0.12, FLOOR_Z + 0.45)], 0.004, PINE, segs=6)

# By the door: a coir doormat and a pair of wellington boots. By the rocking chair: a pot of lavender.
box("Doormat", (0.42, 0.66, 0.015), (0.25, dcy, FLOOR_Z + 0.0075), M("rush", 0.95, "knit", scale=3,
    color=mix_hex(COLORS["accent_2"], COLORS["timber"], 0.45)), bevel=0.004)
welly = M("accent_2", 0.35, "leather")
for k, (bx, by, turn) in enumerate(((0.22, dy1 + 0.2, 10), (0.36, dy1 + 0.17, -15))):
    bt = empty(f"Welly_{k}", (bx, by, FLOOR_Z), rot=(0, 0, R(turn)))
    lathe("Welly_Shaft", [(0, 0.03), (0.05, 0.03), (0.052, 0.3), (0.056, 0.36), (0.05, 0.36), (0.046, 0.06), (0, 0.06)],
          (0, 0.04, 0), welly, segs=20, parent=bt)
    box("Welly_Foot", (0.095, 0.22, 0.08), (0, -0.02, 0.04), welly, bevel=0.035, parent=bt)
    box("Welly_Sole", (0.1, 0.23, 0.02), (0, -0.02, 0.01), mat("dark", 0.8), bevel=0.008, parent=bt)
lav = (4.3, 1.12)                                     # a big terracotta pot of lavender beside the fireside corner
lathe("Lavender_Pot", [(0, 0), (0.13, 0), (0.17, 0.27), (0.185, 0.29), (0.185, 0.32), (0.17, 0.32), (0.15, 0.05),
                       (0, 0.05)], (lav[0], lav[1], FLOOR_Z), CLAY, segs=32)
cyl("Lavender_Soil", 0.16, 0.01, (lav[0], lav[1], FLOOR_Z + 0.3), SOIL, bevel=0, segs=24)
rl = random.Random(SEED + 91)
mound = [(rl.uniform(0.07, 0.1), (lav[0] + rl.uniform(-0.09, 0.09), lav[1] + rl.uniform(-0.09, 0.09),
                                   FLOOR_Z + 0.34 + rl.uniform(0, 0.05)), (1.2, 1.2, 0.8), (0, 0, 0)) for _ in range(9)]
blobs("Lavender_Leaves", mound, mat("sage_leaf", 0.8, color=mix_hex(COLORS["main"], COLORS["plant"], 0.4)), segs=12)
spikes, stalk_mat = [], mat("stalk", 0.8, color=mix_hex(COLORS["main"], COLORS["plant"], 0.6))
for k in range(34):
    a, lean = rl.uniform(0, 2 * math.pi), rl.uniform(0.05, 0.5)
    ln = rl.uniform(0.3, 0.44)
    base = Vector((lav[0] + math.cos(a) * 0.05, lav[1] + math.sin(a) * 0.05, FLOOR_Z + 0.36))
    tip = base + Vector((math.cos(a) * math.sin(lean), math.sin(a) * math.sin(lean), math.cos(lean))) * ln
    tube("Lavender_Stalk", [tuple(base), tuple(tip)], 0.0028, stalk_mat, segs=4)
    spikes.append((0.016, tuple(tip), (1, 1, 3.2), (0, lean, a)))
blobs("Lavender_Flowers", spikes, M("lavender", 0.85, "knit", scale=3, color=mix_hex("#9C83C9", COLORS["accent_3"], 0.2)),
      segs=8)
# Fireside corner: a striped hand-woven cotton rag rug (80 x 150 cm) under the rocking chair and the cat,
# woven in bands of the palette colours with a knotted fringe at each end.
RR_C, RR_L, RR_W = (2.8, 1.2), 1.5, 0.8
bands = ["cream", "accent_1", "cream", "main", "accent_2", "cream", "accent_3", "cream", "accent_2", "main", "cream",
         "accent_1", "cream"]
widths = [0.16, 0.05, 0.1, 0.12, 0.04, 0.22, 0.1, 0.22, 0.04, 0.12, 0.1, 0.05, 0.16]
scale_ = RR_L / sum(widths)
xx = RR_C[0] - RR_L / 2
for k, (key, bw) in enumerate(zip(bands, widths)):
    bw *= scale_
    box(f"RagRug_Band_{k}", (bw + 0.001, RR_W, 0.008), (xx + bw / 2, RR_C[1], FLOOR_Z + 0.004),
        M(key, 0.97, "knit", scale=2.5, color=mix_hex(COLORS[key], COLORS["cream"], 0.15)), bevel=0.002)
    xx += bw
fringe = []
for sx in (-1, 1):
    for q in range(22):
        yy = RR_C[1] - RR_W / 2 + 0.02 + q * (RR_W - 0.04) / 21
        fringe.append(((0.05, 0.006, 0.003), (RR_C[0] + sx * (RR_L / 2 + 0.024), yy, FLOOR_Z + 0.002), (0, 0, R(sx * 6))))
boxes("RagRug_Fringe", fringe, M("cream", 0.97, "knit", scale=3), bevel=0)

# By the table: a slatted wooden apple crate (50 x 40 x 30 cm) full of apples, one rolled out onto the floor.
ac = empty("Apple_Crate", (1.55, 0.62, FLOOR_Z), rot=(0, 0, R(18)))
CRATE = M("wood", 0.75, "wood", color=mix_hex(COLORS["wood"], COLORS["cream"], 0.25))
for sx in (-1, 1):
    box("Crate_End", (0.018, 0.4, 0.3), (sx * 0.241, 0, 0.15), CRATE, bevel=0.003, parent=ac)
    box("Crate_Handle", (0.02, 0.1, 0.03), (sx * 0.241, 0, 0.25), mat("dark", 0.8), bevel=0.006, parent=ac)
    for k in range(3):
        box("Crate_Slat", (0.464, 0.01, 0.065), (0, sx * 0.195, 0.04 + k * 0.105), CRATE, bevel=0.002, parent=ac)
for k in range(4):
    box("Crate_Bottom", (0.464, 0.08, 0.01), (0, -0.15 + k * 0.1, 0.012), CRATE, bevel=0.002, parent=ac)
ra = random.Random(SEED + 95)
red, green = [], []
for q in range(18):
    p = (ra.uniform(-0.18, 0.18), ra.uniform(-0.14, 0.14), 0.25 + ra.uniform(0, 0.06) + 0.04 * (1 - abs(q % 5 - 2) / 2))
    (green if q % 4 == 0 else red).append((ra.uniform(0.036, 0.042), p, (1, 1, 0.9), (0, 0, 0)))
APPLE_R = M("accent_1", 0.4, "ceramic", color=mix_hex(COLORS["accent_1"], "#B8322A", 0.4))
APPLE_G = M("plant", 0.45, "ceramic", color=mix_hex(COLORS["plant"], COLORS["accent_2"], 0.45))
blobs("Crate_Apples_Red", red, APPLE_R, parent=ac, segs=14)
blobs("Crate_Apples_Green", green, APPLE_G, parent=ac, segs=14)
ball("Apple_Floor", 0.04, (0.05, -0.35, 0.037), APPLE_R, scale=(1, 1, 0.9), parent=ac)
for o_ in [(0.05, -0.35, 0.075)] + [(p[0], p[1], p[2] + r_ * 0.85) for r_, p, _, _ in red[:6]]:
    tube("Apple_Stalk", [o_, (o_[0] + 0.004, o_[1], o_[2] + 0.014)], 0.0022, mat("bark", 0.8), parent=ac, segs=4)

# Wrought-iron swing-arm for the lantern: wall plate, arm, a scrolled brace and a hook at the end.
ARM_Y, ARM_X1 = WIN_Y, 1.2
box("Arm_Wall_Plate", (0.012, 0.06, 0.36), (0.006, ARM_Y, ARM_Z - 0.12), IRON, bevel=0.003)
tube("Arm_Bar", [(0.01, ARM_Y, ARM_Z), (ARM_X1 + 0.02, ARM_Y, ARM_Z)], 0.011, IRON, segs=8)
tube("Arm_Brace", spline([(0.01, ARM_Y, ARM_Z - 0.28), (0.25, ARM_Y, ARM_Z - 0.14), (0.55, ARM_Y, ARM_Z - 0.03),
                          (0.75, ARM_Y, ARM_Z)], 5), 0.008, IRON, segs=8)
tube("Arm_Scroll", [(0.18 + (0.05 - a * 0.006) * math.cos(a), ARM_Y, ARM_Z - 0.1 + (0.05 - a * 0.006) * math.sin(a))
                    for a in (k * 0.45 for k in range(16))], 0.005, IRON, segs=6)
tube("Arm_Hook", spline([(ARM_X1, ARM_Y, ARM_Z), (ARM_X1, ARM_Y, ARM_Z - 0.04), (ARM_X1 + 0.02, ARM_Y, ARM_Z - 0.05)], 3),
     0.004, IRON, segs=6)


# =====================================================================
#  PORTFOLIO: the name board over the hearth, a wreath on the door and the framed watercolours
# =====================================================================
# Carved pine kitchen sign-board (124 x 40 cm) hung on two iron hooks at the top of the chimney breast,
# with your name and role burnt in. It faces the camera, so a long name and role stay readable.
SB_W, SB_H, SB_T = 1.24, 0.40, 0.028
SB_Z = FLOOR_Z + 2.45
SB_Y = CB_FRONT - 0.012 - SB_T / 2                    # hangs just off the limewash
SIGN_WOOD = M("plaque", 0.6, "wood", color=mix_hex(COLORS["wood"], COLORS["cream"], 0.5))   # pale, so the letters stand out
box("Sign_Board", (SB_W, SB_T, SB_H), (CB_CX, SB_Y, SB_Z), SIGN_WOOD, bevel=0.012)
SB_F = SB_Y - SB_T / 2                                # front face of the board
for sz in (-1, 1):                                    # routed border groove
    box("Sign_Border", (SB_W - 0.08, 0.003, 0.008), (CB_CX, SB_F - 0.001, SB_Z + sz * (SB_H / 2 - 0.04)), INK, bevel=0)
for sx in (-1, 1):
    box("Sign_Border", (0.008, 0.003, SB_H - 0.08), (CB_CX + sx * (SB_W / 2 - 0.04), SB_F - 0.001, SB_Z), INK, bevel=0)
    hx_ = CB_CX + sx * (SB_W / 2 - 0.14)
    cyl("Sign_Hook_Plate", 0.018, 0.008, (hx_, CB_FRONT - 0.004, SB_Z + SB_H / 2 + 0.1), IRON, rot=(R(90), 0, 0), segs=12)
    tube("Sign_Hook", spline([(hx_, CB_FRONT - 0.008, SB_Z + SB_H / 2 + 0.1), (hx_, SB_Y - 0.004, SB_Z + SB_H / 2 + 0.085),
                              (hx_, SB_Y, SB_Z + SB_H / 2 - 0.005)], 3), 0.0045, IRON, segs=6)
    # a carved sprig at each end of the board, inside the border
    sp = (CB_CX + sx * (SB_W / 2 - 0.085), SB_F - 0.003)
    tube("Sign_Sprig_Stem", [(sp[0], sp[1], SB_Z - 0.1), (sp[0] + sx * 0.008, sp[1], SB_Z + 0.1)], 0.0025, INK, segs=5)
    blobs("Sign_Sprig_Leaf", [(0.016, (sp[0] + sx * 0.004 + (0.014 if q % 2 else -0.014), sp[1], SB_Z - 0.07 + q * 0.04),
                               (1.5, 0.25, 0.6), (0, R(35 if q % 2 else -35), 0)) for q in range(5)],
          mat("plant", 0.6, color=shade(COLORS["plant"], 0.9)), segs=10)
hook_text("name", 1, "YOUR NAME", 0.16, (CB_CX, SB_F - 0.002, SB_Z + 0.055), material=INK, max_width=SB_W - 0.3,
          depth=0.004)
hook_text("role", 1, "your role", 0.095, (CB_CX, SB_F - 0.002, SB_Z - 0.1), material=INK, max_width=SB_W - 0.3,
          depth=0.003)

# A dried-flower wreath (35 cm) on the top leaf of the stable door: a straw ring, wheat ears, lavender and a bow.
WR_X, WR_Z, WR_R = lx_in + 0.03, FLOOR_Z + 1.62, 0.15
cyl("Wreath_Nail", 0.006, 0.03, (WR_X - 0.01, dcy, WR_Z + WR_R + 0.03), IRON, rot=(0, R(90), 0), segs=8)
tube("Wreath_Ring", circle_yz(WR_X, dcy, WR_Z, WR_R, 40), 0.028, RUSH, segs=10, closed=True)
rw = random.Random(SEED + 33)
wheat, lav_buds, wleaf = [], [], []
for k in range(26):
    a = 2 * math.pi * k / 26 + rw.uniform(-0.08, 0.08)
    c = Vector((WR_X + 0.02, dcy + math.cos(a) * WR_R, WR_Z + math.sin(a) * WR_R))
    tang = Vector((0, -math.sin(a), math.cos(a)))
    if k % 3 == 0:
        lav_buds.append((0.011, tuple(c + tang * 0.03), (1, 1, 1), (0, 0, 0)))
        lav_buds.append((0.01, tuple(c + tang * 0.05 + Vector((0.004, 0, 0))), (1, 1, 1), (0, 0, 0)))
    elif k % 3 == 1:
        wheat.append((0.012, tuple(c + tang * 0.035), (1.0, 0.8, 2.4), (a, 0, 0)))
    else:
        wleaf.append((0.022, tuple(c + Vector((0.004, 0, 0))), (0.35, 1.6, 0.7), (a, 0, 0)))
blobs("Wreath_Wheat", wheat, M("accent_2", 0.85, "knit", scale=3, color=mix_hex(COLORS["accent_2"], COLORS["cream"], 0.35)),
      segs=8)
blobs("Wreath_Lavender", lav_buds, M("lavender", 0.85, "knit", scale=3, color=mix_hex("#9C83C9", COLORS["accent_3"], 0.2)),
      segs=8)
blobs("Wreath_Leaves", wleaf, mat("sage_leaf", 0.8, color=mix_hex(COLORS["main"], COLORS["plant"], 0.4)), segs=8)
bow_m = gingham("accent_1")
for sy in (-1, 1):
    blobs("Wreath_Bow_Loop", [(0.035, (WR_X + 0.035, dcy + sy * 0.035, WR_Z - WR_R + 0.005), (0.35, 1.2, 0.7),
                               (R(sy * 20), 0, 0))], bow_m, segs=12)
    tube("Wreath_Bow_Tail", [(WR_X + 0.035, dcy + sy * 0.008, WR_Z - WR_R - 0.005),
                             (WR_X + 0.03, dcy + sy * 0.03, WR_Z - WR_R - 0.09)], 0.008, bow_m, segs=6, r2=0.006)
ball("Wreath_Bow_Knot", 0.016, (WR_X + 0.04, dcy, WR_Z - WR_R + 0.005), bow_m)

def framed(name, x, y, z, size, wall="back", frame_mat=None, mount=0.045, depth=0.024):
    """Real picture frame: 22 mm moulding around a cream mount (passe-partout).
    wall="back": hung on a surface facing -y at y; wall="left": on a surface facing +x at x.
    Returns the hook location + rotation for the picture inside."""
    w, h = size
    fw = 0.022
    ow, oh = w + 2 * mount + 2 * fw, h + 2 * mount + 2 * fw
    fm = frame_mat or PINE
    if wall == "back":
        box(f"{name}_Mount", (ow - 0.01, 0.008, oh - 0.01), (x, y - 0.004, z), PAPER, bevel=0)
        for sz in (-1, 1):
            box(f"{name}_Frame_H", (ow, depth, fw), (x, y - depth / 2, z + sz * (oh - fw) / 2), fm, bevel=0.003)
        for sx in (-1, 1):
            box(f"{name}_Frame_V", (fw, depth, oh - 2 * fw), (x + sx * (ow - fw) / 2, y - depth / 2, z), fm, bevel=0.003)
        return (x, y - 0.0115, z), (0, 0, 0)
    box(f"{name}_Mount", (0.008, ow - 0.01, oh - 0.01), (x + 0.004, y, z), PAPER, bevel=0)
    for sz in (-1, 1):
        box(f"{name}_Frame_H", (depth, ow, fw), (x + depth / 2, y, z + sz * (oh - fw) / 2), fm, bevel=0.003)
    for sy in (-1, 1):
        box(f"{name}_Frame_V", (depth, fw, oh - 2 * fw), (x + depth / 2, y + sy * (ow - fw) / 2, z), fm, bevel=0.003)
    return (x + 0.0115, y, z), (0, 0, R(90))


def wash(name, parts, key, hook, wall="back"):
    """Default watercolour: soft flattened blobs of colour laid on the picture (hidden once a project image is set)."""
    out = []
    for k, (r, (a, b), sc) in enumerate(parts):
        hx, hy, hz = hook.location
        if wall == "back":
            loc, scl = (hx + a, hy - 0.0015 - 0.0004 * k, hz + b), (sc[0], 0.03, sc[1])
        else:
            loc, scl = (hx + 0.0015 + 0.0004 * k, hy + a, hz + b), (0.03, sc[0], sc[1])
        out.append(blobs(f"{name}_{k}", [(r, loc, scl, (0, 0, 0))], mat(key[k] if isinstance(key, list) else key, 0.9),
                         segs=14))
    hook_default(hook, *out)


# Two watercolours over the hearth, on the chimney breast (under the name board).
FR_Z = FLOOR_Z + 1.75
loc, rot = framed("Frame1", CB_CX - 0.31, CB_FRONT, FR_Z, (0.4, 0.52))
f1 = hook_image("frame", 1, (0.4, 0.52), loc, rot=rot, default_key="sky")
wash("Frame1_Wash", [(0.2, (-0.05, -0.16), (1.2, 0.45)), (0.17, (0.1, -0.2), (1.3, 0.4)), (0.06, (0.08, 0.12), (1, 1)),
                     (0.05, (-0.07, -0.08), (0.6, 0.45))], ["main", "plant", "accent_2", "cream"], f1)
loc, rot = framed("Frame2", CB_CX + 0.31, CB_FRONT, FR_Z, (0.4, 0.52))
f2 = hook_image("frame", 2, (0.4, 0.52), loc, rot=rot, default_key="cream")
wash("Frame2_Wash", [(0.12, (0.0, -0.16), (1.6, 0.3)), (0.07, (0.0, 0.06), (1, 1)), (0.04, (-0.07, 0.0), (1.4, 0.5)),
                     (0.04, (0.07, -0.05), (1.4, 0.5)), (0.012, (0.0, -0.06), (0.6, 9.0))],
     ["accent_3", "accent_1", "plant", "plant", "plant"], f2)
# A third picture on the left wall between the door and the window.
loc, rot = framed("Frame3", 0.0, 1.69, FLOOR_Z + 1.5, (0.4, 0.5), wall="left", frame_mat=TIMBER_V, mount=0.04)
f3 = hook_image("frame", 3, (0.4, 0.5), loc, rot=rot, default_key="accent_2")
wash("Frame3_Wash", [(0.15, (0.0, -0.13), (1.3, 0.5)), (0.055, (0.06, 0.08), (1, 1)), (0.1, (-0.05, -0.06), (1.0, 0.4))],
     ["plant", "cream", "main"], f3, wall="left")
# Shaker peg rail under the picture: a straw sun hat and a market basket.
box("PegRail", (0.022, 0.5, 0.07), (0.011, 1.68, FLOOR_Z + 1.06), PINE_Y, bevel=0.004)
for k in range(3):
    cyl("PegRail_Peg", 0.011, 0.07, (0.055, 1.52 + k * 0.16, FLOOR_Z + 1.06), PINE, rot=(0, R(80), 0), segs=10)
lathe("Sun_Hat", [(0, 0.06), (0.06, 0.06), (0.075, 0.035), (0.08, 0.0), (0.17, -0.005), (0.18, -0.012), (0, -0.012)],
      (0.08, 1.52, FLOOR_Z + 0.98), RUSH, rot=(0, R(70), 0), segs=32)
hat_rot = Matrix.Rotation(R(70), 3, "Y")             # a ribbon band round the crown, in the hat's own tilt
tube("Sun_Hat_Ribbon", [tuple(Vector((0.08, 1.52, FLOOR_Z + 0.98)) + hat_rot @ Vector((0.079 * math.cos(a), 0.079 * math.sin(a),
                                                                                      0.03)))
                        for a in (2 * math.pi * q / 24 for q in range(24))], 0.007, M("accent_1", 0.9, "fabric"),
     segs=5, closed=True)

# =====================================================================
#  OUTSIDE: stepping stones, letterbox, washing line, hollyhocks, meadow grass and flowers
# =====================================================================
stones = [(0.15, (-0.48, 0.72, GROUND), (1.1, 0.9, 0.12), (0, 0, 0.3)), (0.13, (-0.86, 0.42, GROUND), (1.0, 1.1, 0.12),
          (0, 0, 1.0)), (0.14, (-1.08, 0.0, GROUND), (1.2, 0.9, 0.12), (0, 0, 0.2)),
          (0.12, (-1.02, -0.42, GROUND), (1.0, 1.0, 0.12), (0, 0, 0.7))]
blobs("Stepping_Stones", stones, FLAG, segs=16)

# Wooden cottage letterbox on a post, turned towards the lane - click it to email you.
mb = empty("Letterbox", (-0.5, -0.5, GROUND), rot=(0, 0, R(45)))
box("Letterbox_Post", (0.075, 0.075, 1.05), (0, 0.04, 0.525), TIMBER_V, bevel=0.006, parent=mb)
box("Letterbox_Bracket", (0.2, 0.2, 0.03), (0, 0.02, 1.065), TIMBER, bevel=0.004, parent=mb)
body = box("Letterbox_Body", (0.36, 0.26, 0.24), (0, 0, 1.2), M("accent_1", 0.55, "wood", along="Z"), bevel=0.012, parent=mb)
hook_link(body, "email")
for sx in (-1, 1):
    box("Letterbox_Roof", (0.22, 0.3, 0.018), (sx * 0.095, 0, 1.36), SHINGLE, bevel=0.004, rot=(0, R(sx * -33), 0), parent=mb)
box("Letterbox_Gable", (0.34, 0.014, 0.09), (0, -0.124, 1.345), M("accent_1", 0.56, "wood", along="Z"), bevel=0.004,
    parent=mb)
box("Letterbox_Slot", (0.18, 0.006, 0.022), (0, -0.131, 1.25), mat("dark", 0.7), bevel=0.002, parent=mb)
box("Letterbox_Letter", (0.14, 0.004, 0.07), (0.01, -0.133, 1.268), PAPER, bevel=0.001, rot=(0, R(6), 0), parent=mb)
ball("Letterbox_Knob", 0.012, (0, -0.135, 1.14), BRASS, parent=mb)
label("Letterbox_Number", "7", 0.05, (-0.12, -0.132, 1.16), mat("cream", 0.6), parent=mb)
box("Letterbox_Flag_Arm", (0.012, 0.012, 0.16), (0.186, 0.02, 1.26), M("accent_2", 0.5), bevel=0.002, parent=mb)
box("Letterbox_Flag", (0.006, 0.07, 0.05), (0.188, 0.05, 1.32), M("accent_2", 0.5), bevel=0.002, parent=mb)

# Washing line on two timber posts, a billowing linen sheet and two tea towels pegged out.
LINE_X, LINE_Y0, LINE_Y1, LINE_Z = -1.25, -0.64, 1.2, GROUND + 1.86
for yy in (LINE_Y0, LINE_Y1):
    box("Line_Post", (0.07, 0.07, 1.95), (LINE_X, yy, GROUND + 0.975), TIMBER_V, bevel=0.006)
    box("Line_Post_Cap", (0.09, 0.09, 0.025), (LINE_X, yy, GROUND + 1.96), TIMBER, bevel=0.005)


def line_z(y):
    t = (y - LINE_Y0) / (LINE_Y1 - LINE_Y0)
    return LINE_Z - 0.12 * math.sin(math.pi * t)


tube("Washing_Line", [(LINE_X + 0.04, LINE_Y0 + (LINE_Y1 - LINE_Y0) * q / 20, line_z(LINE_Y0 + (LINE_Y1 - LINE_Y0) * q / 20))
                      for q in range(21)], 0.003, mat("cream", 0.8), segs=5)
if LAUNDRY:
    def hung(name, y0, wdt, drop, m_, bill, seed):
        def fn(u, v):
            y = y0 + u * wdt
            z = line_z(y) - 0.01 - v * drop * (1 - 0.12 * v)
            x = LINE_X + 0.045 + bill * math.sin(math.pi * u) * (0.35 + 0.65 * v) + 0.18 * bill * v * v + \
                0.018 * math.sin(3 * math.pi * u + 2.5 * v + seed)
            return (x, y, z)
        sheet(name, 26, 16, fn, m_)
        for u in (0.03, 0.5, 0.97) if wdt > 0.5 else (0.06, 0.94):
            y = y0 + u * wdt
            box(f"{name}_Peg", (0.012, 0.012, 0.06), (LINE_X + 0.045, y, line_z(y) - 0.01), PINE_V, bevel=0.002)
    hung("Laundry_Sheet", -0.44, 0.86, 0.98, LINEN, 0.16, 0.0)
    hung("Laundry_Towel", 0.5, 0.36, 0.55, gingham("accent_1"), 0.1, 1.3)
    hung("Laundry_Cloth", 0.92, 0.22, 0.4, M("accent_3", 0.9, "fabric"), 0.08, 2.2)


def hollyhock(name, x, y, height, col, seed):
    """Cottage-garden hollyhock: tall stem, big round leaves at the base, open flowers up the top half."""
    rr = random.Random(seed)
    stem = [(x, y, GROUND), (x + rr.uniform(-0.03, 0.03), y + rr.uniform(-0.03, 0.03), GROUND + height * 0.5),
            (x + rr.uniform(-0.06, 0.06), y + rr.uniform(-0.06, 0.06), GROUND + height)]
    pts = spline(stem, 8)
    tube(f"{name}_Stem", pts, 0.009, mat("plant", 0.7), r2=0.004, segs=6)
    leaves = [(0.07, (x + math.cos(a) * 0.1, y + math.sin(a) * 0.1, GROUND + 0.12 + 0.07 * (k % 3)), (1, 1, 0.25),
               (rr.uniform(-0.4, 0.4), rr.uniform(-0.4, 0.4), a)) for k, a in enumerate(q * 1.1 for q in range(8))]
    blobs(f"{name}_Leaves", leaves, mat("plant", 0.6, color=shade(COLORS["plant"], 0.9)), segs=10)
    fl, buds = [], []
    for k, p in enumerate(pts[len(pts) // 2:]):
        a = k * 2.2
        q = (p.x + math.cos(a) * 0.035, p.y + math.sin(a) * 0.035, p.z)
        (fl if k < len(pts) // 2 - 2 else buds).append((0.034 if k < len(pts) // 2 - 2 else 0.014, q,
                                                       (1, 1, 0.45), (math.sin(a) * 0.8, math.cos(a) * 0.8, 0)))
    blobs(f"{name}_Flowers", fl, mat("hollyhock", 0.7, color=col), segs=12)
    blobs(f"{name}_Buds", buds, mat("plant", 0.6, color=mix_hex(COLORS["plant"], col, 0.3)), segs=8)


for k, (hx, hy, hh, col) in enumerate(((-0.3, -0.26, 1.6, "#E99AB2"), (-0.62, -0.06, 1.35, "#F4E6D8"),
                                       (-0.16, -0.58, 1.25, "#C9506E"), (-0.95, -0.72, 1.1, "#E99AB2"))):
    hollyhock(f"Hollyhock_{k}", hx, hy, hh, col, SEED + k)

# Meadow grass: low along the front of the cottage, tall at the sides and outside the round window.
rnd = random.Random(SEED + 31)
tufts = []
x = YARD_X + 0.05
while x < W - 0.05:                                   # along the front edge of the turf
    tall = x < -0.05
    tufts.append((x, YARD_Y + 0.08 + rnd.uniform(-0.03, 0.03), GROUND, 0.07, rnd.uniform(0.35, 0.6) if tall else 0.1, 14))
    x += rnd.uniform(0.12, 0.22)
y = YARD_Y + 0.15
while y < 1.5:                                        # along the left edge
    tufts.append((YARD_X + 0.08, y, GROUND, 0.08, rnd.uniform(0.45, 0.8), 16))
    y += rnd.uniform(0.12, 0.2)
for _ in range(22):                                   # seen through the round window
    tufts.append((rnd.uniform(-1.5, -0.3), rnd.uniform(2.3, D + 0.15), GROUND, 0.12, rnd.uniform(0.75, 1.25), 18))
for px_, py_ in ((LINE_X, LINE_Y0), (LINE_X, LINE_Y1), (-0.5, -0.5), (-0.3, -0.26), (-0.62, -0.06), (-0.16, -0.58),
                 (-0.95, -0.72), (-0.25, 0.1), (-1.3, 0.55), (-0.7, -0.35)):
    tufts.append((px_, py_, GROUND, 0.1, rnd.uniform(0.3, 0.55), 18))
half = len(tufts) // 2
grass("Meadow_Grass", tufts[:half], GRASS, seed=SEED + 32)
grass("Meadow_Grass_Dark", tufts[half:], GRASS_DARK, seed=SEED + 33)
flowers_w, flowers_y = [], []
for k in range(46):
    if k < 30:
        p = (rnd.uniform(YARD_X + 0.1, -0.2), rnd.uniform(YARD_Y + 0.1, 0.9))
        p = p if p[1] < -p[0] else (p[0], -p[0] - 0.05)
    else:
        p = (rnd.uniform(-1.4, -0.35), rnd.uniform(2.4, D))
    z = GROUND + (rnd.uniform(0.1, 0.35) if k < 30 else rnd.uniform(0.55, 0.95))
    (flowers_w if k % 3 else flowers_y).append((0.016 if k % 3 else 0.012, (p[0], p[1], z), (1, 1, 0.35), (0, 0, 0)))
blobs("Meadow_Daisies", flowers_w, mat("flower", 0.6, color="#FFFFFF"), segs=10)
blobs("Meadow_Buttercups", flowers_y, mat("buttercup", 0.5, color=COLORS["accent_2"]), segs=10)

# =====================================================================
#  THE OLD TREE growing up through the corner, with roots across the floor and a canopy above the roof
# =====================================================================
trunk = [(0.02, D - 0.02, GROUND - 0.05), (0.05, D - 0.06, 1.2), (0.0, D - 0.02, 2.4), (0.06, D - 0.08, 3.25),
         (0.03, D - 0.04, 3.6)]
tube("Tree_Trunk", spline(trunk, 6), 0.6, BARK, r2=0.34, segs=28)
for k, path in enumerate((
        [(0.3, D - 0.3, FLOOR_Z + 0.65), (0.6, D - 0.42, FLOOR_Z + 0.12), (0.92, D - 0.48, FLOOR_Z + 0.02)],
        [(0.42, D - 0.12, FLOOR_Z + 0.45), (0.72, D - 0.1, FLOOR_Z + 0.08), (0.9, D - 0.06, FLOOR_Z + 0.02)],
        [(0.22, D - 0.42, FLOOR_Z + 0.55), (0.42, D - 0.68, FLOOR_Z + 0.1), (0.62, D - 0.84, FLOOR_Z + 0.02)])):
    tube(f"Tree_Root_{k}", spline(path, 6), 0.13 - 0.02 * k, BARK, r2=0.025, segs=14)
for k in range(9):                                    # vertical bark ridges on the room side of the trunk
    a = R(-95 + k * 11)
    rad = 0.58
    tube("Tree_Bark_Ridge", spline([(0.02 + math.cos(a) * rad, D - 0.02 + math.sin(a) * rad, FLOOR_Z),
                                    (0.04 + math.cos(a) * (rad - 0.08), D - 0.05 + math.sin(a) * (rad - 0.08), 1.5),
                                    (0.02 + math.cos(a) * (rad - 0.2), D - 0.03 + math.sin(a) * (rad - 0.2), H - 0.1)], 5),
         0.03, BARK, segs=6)
moss_t = []
for k in range(26):                                   # moss cushions low on the trunk, where it stays damp
    a = R(rnd.uniform(-80, -5))
    z = rnd.uniform(FLOOR_Z, 0.6) ** 1.0
    rad = 0.6 - 0.26 * (z / 3.75) - 0.02
    moss_t.append((rnd.uniform(0.04, 0.075), (0.03 + math.cos(a) * rad, D - 0.03 + math.sin(a) * rad, z), (1.2, 1, 0.6),
                   (0, R(90), a)))
blobs("Tree_Moss", moss_t, MOSS, segs=16)
limbs = [[(0.05, D - 0.05, 3.25), (-0.4, D + 0.3, 3.6), (-0.95, D + 0.6, 3.75)],
         [(0.08, D - 0.08, 3.3), (0.45, D - 0.35, 3.55), (0.9, D - 0.6, 3.65)],
         [(0.03, D, 3.35), (-0.1, D + 0.6, 3.7), (-0.2, D + 1.0, 3.85)],
         [(0.05, D - 0.05, 3.4), (0.15, D - 0.15, 3.65), (0.1, D - 0.1, 3.8)]]
for k, lb in enumerate(limbs):
    tube(f"Tree_Limb_{k}", spline(lb, 6), 0.2, BARK, r2=0.05, segs=14)
# A wide, low dome of many leafy clumps (light green on top, mid green around, dark green underneath), each clump
# covered in real leaves that stand proud of it, so the crown has a soft, broken outline instead of smooth balls.
rc = random.Random(SEED + 40)
canopy = []
for k in range(46):
    a, e = rc.uniform(0, 2 * math.pi), rc.uniform(0.0, 1.0) ** 0.7
    c = (-0.15 + 1.25 * math.cos(a) * (1 - 0.5 * e), D + 0.15 + 1.05 * math.sin(a) * (1 - 0.5 * e), 3.52 + 0.42 * e)
    if c[0] > 1.15 or (c[0] > 0.6 and c[1] < D - 0.75):
        continue                                      # keep the chimney stack clear
    canopy.append((c, rc.uniform(0.22, 0.34)))
tiers = ([], [], [])
for c, r_ in canopy:
    tier = 0 if c[2] > 3.8 else (1 if c[2] > 3.62 else 2)
    tiers[tier].append((r_, c, (1.2, 1.2, 0.82), (0, 0, rc.uniform(0, 3))))
for mi, (m_, parts) in enumerate(zip((LEAF_2, LEAF_1, LEAF_3), tiers)):
    if parts:
        blobs(f"Tree_Canopy_{mi}", parts, m_, segs=20)
foliage("Tree_Leaves", [(c, r_ * 1.38) for c, r_ in canopy if c[2] > 3.62], 70, (0.12, 0.075), LEAF_2,
        seed=SEED + 41, droop=0.1)
foliage("Tree_Leaves_Mid", [(c, r_ * 1.35) for c, r_ in canopy], 45, (0.12, 0.075), LEAF_1, seed=SEED + 43, droop=0.2)
foliage("Tree_Leaves_Dark", [(c, r_ * 1.3) for c, r_ in canopy if c[2] <= 3.75], 50, (0.12, 0.075), LEAF_3,
        seed=SEED + 42, droop=0.35)

# =====================================================================
#  ROOF EDGE: a cut-away shingle eave on both walls with moss cushions, and the chimney stack
# =====================================================================
SLOPE = R(20)
box("Wall_Cap_Left", (T + 0.06, D + T + 0.02, 0.08), (-T / 2 + 0.01, (D + T) / 2 - 0.01, H + 0.04), TIMBER_Y, bevel=0.008)
box("Wall_Cap_Back", (W + T + 0.02, T + 0.06, 0.08), ((W - T) / 2 - 0.01, D + T / 2 - 0.01, H + 0.04), TIMBER, bevel=0.008)


def eave(name, wall):
    """Four staggered courses of cedar shingles on sheathing, falling away from the room at 20 degrees."""
    rr = random.Random(SEED + (51 if wall == "left" else 52))
    if wall == "left":
        p0, dirv, nrm, along = Vector((0.05, 0, H + 0.13)), Vector((-math.cos(SLOPE), 0, -math.sin(SLOPE))), \
            Vector((-math.sin(SLOPE), 0, math.cos(SLOPE))), (-0.04, D + T + 0.02)
        rot = (0, -SLOPE, 0)
    else:
        p0, dirv, nrm, along = Vector((0, D - 0.05, H + 0.13)), Vector((0, math.cos(SLOPE), -math.sin(SLOPE))), \
            Vector((0, math.sin(SLOPE), math.cos(SLOPE))), (-T - 0.04, W)
        rot = (-SLOPE, 0, 0)
    ln = 0.6
    parts = []
    for j in range(4):
        s = 0.1 + 0.15 * j
        t = along[0] + (0.08 if j % 2 else 0.0)
        while t < along[1]:
            sw = rr.uniform(0.12, 0.18)
            c = p0 + dirv * s + nrm * (0.012 * (3 - j) + 0.01)
            c = c + (Vector((0, t + sw / 2, 0)) if wall == "left" else Vector((t + sw / 2, 0, 0)))
            jit = rr.uniform(-0.04, 0.04)
            size = (0.24, sw - 0.006, 0.016) if wall == "left" else (sw - 0.006, 0.24, 0.016)
            parts.append((size, tuple(c), (rot[0], rot[1], jit)))
            t += sw
    boxes(f"{name}_Shingles", parts, SHINGLE, bevel=0.002)
    span = along[1] - along[0]
    mid = (along[0] + along[1]) / 2
    sheath_c = p0 + dirv * (ln / 2) - nrm * 0.005
    fascia_c = p0 + dirv * (ln + 0.01) - nrm * 0.03
    if wall == "left":
        box(f"{name}_Sheathing", (ln, span, 0.025), (sheath_c.x, mid, sheath_c.z), TIMBER_Y, bevel=0.003, rot=rot)
        box(f"{name}_Fascia", (0.025, span, 0.11), (fascia_c.x, mid, fascia_c.z), TIMBER_Y, bevel=0.004)
    else:
        box(f"{name}_Sheathing", (span, ln, 0.025), (mid, sheath_c.y, sheath_c.z), TIMBER, bevel=0.003, rot=rot)
        box(f"{name}_Fascia", (span, 0.025, 0.11), (mid, fascia_c.y, fascia_c.z), TIMBER, bevel=0.004)
    moss, moss2, tf = [], [], []
    t = along[0] + rr.uniform(0.05, 0.25)
    while t < along[1] - 0.1:                          # domed moss cushions, thickest low down where the rain runs off
        s0 = rr.uniform(0.3, 0.5) if rr.random() < 0.65 else rr.uniform(0.08, 0.3)
        big = rr.uniform(0.75, 1.25)
        c = p0 + dirv * s0 + nrm * 0.06                 # sits on top of the shingles (they reach about 0.055)
        c = c + (Vector((0, t, 0)) if wall == "left" else Vector((t, 0, 0)))
        for q in range(rr.randint(6, 10)):             # one cushion = a tight heap of soft mounds, highest in the middle
            off = Vector((rr.gauss(0, 0.045), rr.gauss(0, 0.045), 0)) * big
            off = Vector((0, off.x, 0)) + dirv * off.y if wall == "left" else Vector((off.x, 0, 0)) + dirv * off.y
            rad = rr.uniform(0.028, 0.045) * big * (1.15 - min(off.length / (0.1 * big), 1.0) * 0.4)
            (moss if rr.random() < 0.55 else moss2).append((rad, tuple(c + off), (1.15, 1.15, 0.95),
                                                           (rot[0], rot[1], rr.uniform(0, 3))))
        if rr.random() < 0.45:
            tf.append((c.x, c.y, c.z + 0.03, 0.05, 0.14, 8))
        t += rr.uniform(0.32, 0.6)
    blobs(f"{name}_Moss", moss, MOSS, segs=16)
    blobs(f"{name}_Moss_Light", moss2, MOSS_LIGHT, segs=16)
    if tf:
        grass(f"{name}_Moss_Grass", tf, GRASS, seed=rr.randint(0, 999))


eave("Eave_Left", "left")
eave("Eave_Back", "back")
# Brick chimney stack on the back wall with a stone cap, a terracotta pot and a curl of woodsmoke.
STACK_X, STACK_Y = CB_CX, D + 0.06
box("Chimney_Stack", (0.6, 0.46, 0.9), (STACK_X, STACK_Y, H + 0.45), BRICK_X, bevel=0.006)
box("Chimney_Cap", (0.7, 0.56, 0.07), (STACK_X, STACK_Y, H + 0.935), M("stone", 0.85, "concrete"), bevel=0.01)
lathe("Chimney_Pot", [(0, 0), (0.1, 0), (0.085, 0.2), (0.09, 0.28), (0.1, 0.3), (0.08, 0.3), (0.07, 0.29), (0, 0.29)],
      (STACK_X, STACK_Y, H + 0.97), CLAY, segs=24)
blobs("Chimney_Moss", [(0.07, (STACK_X - 0.25, STACK_Y - 0.15, H + 0.98), (1.3, 1.2, 0.5), (0, 0, 0)),
                       (0.05, (STACK_X + 0.27, STACK_Y + 0.12, H + 0.98), (1.3, 1.2, 0.5), (0, 0, 0))], MOSS, segs=10)
smoke = []                                           # a thin wisp that widens as it drifts away from the tree
rs = random.Random(SEED + 45)
for k in range(9):
    t = k / 8
    pc = Vector((STACK_X + 0.5 * t + 0.25 * t * t, STACK_Y + 0.1 * t, H + 1.32 + 0.75 * t))
    rad = 0.05 + 0.13 * t
    for q in range(2):
        smoke.append((rad * rs.uniform(0.8, 1.0), tuple(pc + Vector((rs.uniform(-1, 1) * rad * 0.4, 0.0,
                                                                         rs.uniform(-1, 1) * rad * 0.25))),
                      (1.35, 1.1, 0.8), (0, 0, rs.uniform(0, 3))))
smoke_o = blobs("Chimney_Smoke", smoke, mat("smoke", 0.9, color=mix_hex(COLORS["cloud"], COLORS["background"], 0.45),
                                            alpha=0.3, emit=0.05), segs=16)
remesh = smoke_o.modifiers.new("Merge", "REMESH")    # one smooth shell, so the puffs show no seams where they overlap
remesh.mode, remesh.voxel_size = "VOXEL", 0.03
smoke_o.modifiers.new("Soften", "SMOOTH").iterations = 6
no_shadow(smoke_o)


# =====================================================================
#  LIGHTS, WORLD, CAMERA, RENDER
# =====================================================================
# summer_afternoon: a warm high sun from the open front of the diorama, a low "sunbeam" through the round window
# that pools on the table, a soft sky fill from the camera side and a warm bounce.
# rainy_lantern: a dim blue sky, the stove, the paper lantern, the candles and the fairy lights do the work.
sun_dir = Vector((-0.38, 0.78, -0.62)).normalized()
centre = Vector((W / 2, D / 2, 0.8))
if RAINY:
    light("Light_Sun", "SUN", 0.55, kelvin(9000), centre - sun_dir * 6, aim=centre, size=R(8))
    light("Light_Fill", "AREA", 110 * (W * D / 16), kelvin(8500), (W + 3, -3, H + 2.5), aim=(W / 2, D / 2, 0.6), size=7)
    light("Light_Window", "AREA", 18, kelvin(9500), (0.3, WIN_Y, WIN_Z), aim=(2.0, WIN_Y, WIN_Z - 0.4), size=1.0)
    light("Light_Bounce", "AREA", 30, kelvin(2600), (W / 2, D / 2, H - 0.1), aim=(W / 2, D / 2, 0), size=2.5)
    light("Light_Outside", "AREA", 60, kelvin(9000), (-1.6, -1.6, 2.8), aim=(-0.8, -0.2, 0.6), size=2.5)
else:
    light("Light_Sun", "SUN", SUN_STRENGTH, kelvin(SUN_WARMTH), centre - sun_dir * 6, aim=centre, size=R(4))
    light("Light_Fill", "AREA", 190 * (W * D / 16), kelvin(6800), (W + 3, -3, H + 2.5), aim=(W / 2, D / 2, 0.6), size=7)
    light("Light_Window", "AREA", 45, kelvin(5600), (0.3, WIN_Y, WIN_Z), aim=(2.0, WIN_Y, WIN_Z - 0.4), size=1.0)
    light("Light_Bounce", "AREA", 40, kelvin(LAMP_WARMTH + 1500), (W / 2, D / 2, H - 0.1), aim=(W / 2, D / 2, 0), size=2.5)
    # the sunbeam: a spot outside the round window, aimed through it onto the table and the rug
    beam_target = Vector((1.35, 2.35, FLOOR_Z + 0.76))
    beam_dir = (beam_target - Vector((0, WIN_Y, WIN_Z))).normalized()
    light("Light_Meadow", "AREA", 160, kelvin(5600), (-0.9, 3.3, 2.6), aim=(-0.9, 3.3, 0), size=1.6)   # grass outside
    spot = light("Light_Sunbeam", "SPOT", 1500, kelvin(SUN_WARMTH - 300), tuple(Vector((0, WIN_Y, WIN_Z)) - beam_dir * 2.6),
                 aim=beam_target, size=0.05)
    spot.data.spot_size, spot.data.spot_blend = R(22), 0.35
    # a faint shaft of light in the air with a few dust motes caught in it
    shaft_len = (beam_target - Vector((0, WIN_Y, WIN_Z))).length + 0.1
    q = beam_dir.to_track_quat("Z", "Y").to_euler()
    no_shadow(cyl("Sunbeam_Shaft", WIN_R * 0.82, shaft_len, tuple(Vector((0, WIN_Y, WIN_Z)) + beam_dir * shaft_len / 2),
                  mat("beam", 0.9, color="#FFF2D2", emit=0.6, alpha=0.05), r2=WIN_R * 0.95, segs=40, bevel=0, rot=q))
    motes = []
    rm = random.Random(SEED + 61)
    for _ in range(28):
        t = rm.uniform(0.1, 0.9)
        p = Vector((0, WIN_Y, WIN_Z)) + beam_dir * shaft_len * t + Vector((rm.gauss(0, 0.12), rm.gauss(0, 0.12),
                                                                           rm.gauss(0, 0.12)))
        motes.append((0.004, tuple(p), (1, 1, 1), (0, 0, 0)))
    no_shadow(blobs("Sunbeam_Motes", motes, mat("mote", 0.5, color="#FFF6DC", emit=3.0), segs=6))

# World: the camera sees the flat background colour; the room is lit by a soft ambient sky.
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
bg_amb.inputs["Color"].default_value = (*kelvin(9000 if RAINY else 7000), 1)
bg_amb.inputs["Strength"].default_value = 0.22 if RAINY else 0.45
path = wn.new("ShaderNodeLightPath")
mix = wn.new("ShaderNodeMixShader")
wl.new(path.outputs["Is Camera Ray"], mix.inputs["Fac"])
wl.new(bg_amb.outputs[0], mix.inputs[1])
wl.new(bg_cam.outputs[0], mix.inputs[2])
wl.new(mix.outputs[0], out.inputs["Surface"])

# Orthographic camera that frames the cottage, the meadow and the tree canopy automatically.
# kit_bounds covers the meadow around the cottage (left and front) and the canopy above the roof, so
# kit_room_size tells check_room.py the size of the room itself.
BOUNDS = [YARD_X, YARD_Y, GROUND - 0.46, W, D + T, H + 1.0]
cam_data = bpy.data.cameras.new("Camera")
cam_data.type = "ORTHO"
cam = bpy.data.objects.new("Camera", cam_data)
scene.collection.objects.link(cam)
scene.camera = cam
cam.rotation_euler = Euler((R(90 - CAMERA_HEIGHT_ANGLE), 0, R(CAMERA_TURN)))
rot = cam.rotation_euler.to_matrix()
right, up, back = rot.col[0], rot.col[1], rot.col[2]
corners = [Vector((x, y, z)) for x in (BOUNDS[0], BOUNDS[3]) for y in (BOUNDS[1], BOUNDS[4]) for z in (BOUNDS[2], BOUNDS[5])]
xs = [c.dot(right) for c in corners]
ys = [c.dot(up) for c in corners]
aspect = RESOLUTION[0] / RESOLUTION[1]
cam_data.ortho_scale = max(max(xs) - min(xs), (max(ys) - min(ys)) * aspect) * 1.06
center = right * (max(xs) + min(xs)) / 2 + up * (max(ys) + min(ys)) / 2
cam.location = center + back * 30
cam_data.clip_end = 100

# Soft cumulus clouds in the sky behind the cottage (placed by where they appear in the picture).
if CLOUDS:
    cloud_m = mat("cloud", 0.95, emit=0.55 if not RAINY else 0.2)
    room_mid = Vector((W / 2, D / 2, H / 2))
    depth = (room_mid - cam.location).dot(-back) + 5.0
    half_w = cam_data.ortho_scale / 2
    rc = random.Random(SEED + 71)
    for k, (sx, sy, s) in enumerate(((-0.78, 0.62, 1.0), (0.62, 0.7, 0.8), (0.86, 0.32, 0.6), (-0.5, 0.8, 0.55))):
        c = cam.location + right * sx * half_w + up * sy * half_w / aspect - back * depth
        parts = []
        for q in range(7):
            off = (q - 3) * 0.32 * s
            rr_ = (0.42 - 0.07 * abs(q - 3)) * s * rc.uniform(0.85, 1.15)
            parts.append((rr_, tuple(c + right * off + up * rr_ * 0.35), (1.15, 1.15, 0.85), (0, 0, 0)))
        parts.append((0.5 * s, tuple(c + up * 0.32 * s), (1.2, 1.2, 0.9), (0, 0, 0)))
        no_shadow(blobs(f"Cloud_{k}", parts, cloud_m, segs=18))

# Rain (rainy theme): fine streaks over the meadow outside the cottage and beyond the round window.
if RAINY:
    rr = random.Random(SEED + 81)
    drops = []
    for _ in range(420):
        x_ = rr.uniform(YARD_X, -0.2)
        y_ = rr.uniform(YARD_Y, D + 0.2) if rr.random() < 0.6 else rr.uniform(YARD_Y, 0.0)
        drops.append(((0.003, 0.003, rr.uniform(0.12, 0.22)), (x_, y_, rr.uniform(GROUND + 0.1, H + 0.6)), (0, R(8), 0)))
    no_shadow(boxes("Rain", drops, mat("rain", 0.2, color="#CFE0F0", emit=0.6, alpha=0.45), bevel=0))
    no_shadow(blobs("Puddles", [(0.22, (-0.75, 0.15, GROUND + 0.002), (1.4, 1.0, 0.01), (0, 0, 0.4)),
                                (0.16, (-1.2, -0.3, GROUND + 0.002), (1.2, 1.0, 0.01), (0, 0, 1.2))],
                    mat("puddle", 0.05, color=shade(COLORS["sky"], 0.8), metal=0.3), segs=20))

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
                    ("shadow_ray_count", 2), ("use_gtao", True), ("use_soft_shadows", True),
                    ("use_ssr", True), ("use_ssr_refraction", True)):
    if hasattr(ee, attr):
        setattr(ee, attr, value)
if hasattr(ee, "ray_tracing_options"):
    ee.ray_tracing_options.resolution_scale = "2" if "2" in [i.identifier for i in
        type(ee.ray_tracing_options).bl_rna.properties["resolution_scale"].enum_items] else ee.ray_tracing_options.resolution_scale
scene.view_settings.view_transform = "Standard"   # keeps your hex colours exactly as typed
scene.view_settings.exposure = 0.05 if RAINY else -0.12

# Remember the style so add_furniture.py can match colours later.
scene["kit_style"] = STYLE
scene["kit_version"] = KIT_VERSION
scene["kit_palette"] = json.dumps(COLORS)
scene["kit_material_finish"] = json.dumps({"roughness": 0.65, "bevel": 0.005, "saturation": 0.8})
scene["kit_theme"] = THEME
scene["kit_bounds"] = BOUNDS            # includes the meadow, laundry and tree canopy outside the walls
scene["kit_room_size"] = [W, D, H]      # the room itself, for check_room.py
scene["kit_furniture_colors"] = json.dumps(["main", "accent_1", "accent_2", "accent_3", "cream", "wood", "timber",
                                            "copper", "plant", "dark"])   # colours add_furniture.py may use


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
