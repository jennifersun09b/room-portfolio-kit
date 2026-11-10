"""
3D ROOM PORTFOLIO KIT  -  Template: GLOW NAIL & BEAUTY BAR (boutique nail, lash and brow salon)
==============================================================================================
Builds a small isometric boutique beauty bar, the kind of salon that lives on social media: a milky-pink
terrazzo floor, painted arch niches, a colour-sorted polish wall, a manicure table with an LED lamp and a
hand rest, a velvet pedicure "throne" in front of an arched boxwood hedge with a neon script sign, an arched
make-up mirror ringed with bulbs, a ring light, a fluted reception desk with a booking tablet and a velvet
waiting loveseat. It renders a 1920x1080 image.
Your name and role glow on the neon sign; your projects hang in the gold frames, the service poster and
on the booking tablet.

HOW TO RUN
  Option A (no Blender UI):   blender -b -P glow_beauty_bar.py
  Option B (inside Blender):  Scripting tab > Open > glow_beauty_bar.py > Run Script (then F12 to render)

You only need to edit the SETTINGS block below. Everything under it builds the room.
Output: output/glow_beauty_bar.png and output/glow_beauty_bar.blend next to this script.
"""
# REFERENCES  (what each piece is modelled on; product names appear only here and in research/glow_beauty_bar.md)
#   desk          salon manicure table, single (Equipro / HANS "Penelope" type): L110 D48 H76 cm, drawer pedestal,
#                 vented dust collector, towel-wrapped wrist cushion
#                 https://minervabeauty.com/blog/post/manicure-table-buying-guide
#                 https://www.purespadirect.com/Penelope-Double-Manicure-Table-White-with-Light-Wo-p/kv-972300.htm
#   LED lamp      48 W UV/LED gel nail lamp (tunnel type): 20 x 19 x 9 cm, front hand opening, timer display
#                 https://Semilac.co.uk/products/semilac-uv-led-lamp-24-48w
#   chair         velvet channel-tufted tub chair on tapered brass legs: W60 D58 H78 cm, seat 46 cm
#   stool         nail technician stool, gas lift, 5-star base on casters, seat dia 38 cm, seat 50-65 cm
#   salon_chair   pipeless pedicure spa "throne" (Continuum Echo footprint): L157 W75-88 H137 cm, seat 58 cm
#                 from the floor, fibreglass foot basin about 20 l, raised plinth + foot step
#                 https://cdn.shopify.com/s/files/1/0316/8783/5786/files/Continuum_-_Echo_1-300-0095_-_Rev_021720.pdf
#   wall_shelf    salon polish wall: 3 x 6-tier clear acrylic wall racks (each 52 x 5 x 61 cm, 90 bottles)
#                 https://gemininevada.com/products/90-spot-polish-rack
#   bottles       15 ml square glass polish bottle: 28.5 x 28.5 mm, 52 mm body, 68 mm with cap (generic shape)
#                 https://tkbtrading.com/collections/nails-packaging/products/emperor-le-barrel-nail-polish-bottle-in-black-or-white
#   counter       salon reception desk with a raised transaction ledge: W140 D60 H107 cm, work top 75 cm
#                 https://keller4salon.com/blogs/keller-international-blog/the-complete-guide-to-salon-reception-desk-sizing
#   booking tab   12.9" tablet on a swivel kiosk stand (28 x 21.5 cm screen) + countertop card reader 8 x 8 cm
#   mirror        arched "Hollywood" make-up mirror with globe bulbs: W72 H98 cm, 13 dimmable bulbs
#                 https://www.debenhams.ie/product/fascinate-15-led-hollywood-vanity-mirror-industry-chic-black-frame-dimmable-58x48cm_p-b56ebc6e-e66d-4790-8b6b-e4a96da07f21
#   vanity        Hollywood-Regency console vanity: W85 D38 H76 cm, one drawer, tapered brass legs
#   floor_lamp    18" LED ring light on a light stand (NEEWER RL-18 type): ring 46 cm OD / 36 cm ID, stand 75-190 cm
#                 https://neewer.com/products/led-ring-lights-66600024
#   sofa          velvet channel-tufted 2-seat loveseat: W138 D78 H80 cm, seat 44 cm, brass feet
#                 https://www.manomano.co.uk/p/2-seater-velvet-sofa-loveseat-tufted-seat-low-back-tuxedo-off-white-malung-81067376
#   coffee table  tulip-style round pedestal table with a marble top: dia 60 cm, H42 cm
#   tips wheel    nail-art practice / colour wheel, 20 tips, 13 x 11 cm on a stand
#                 https://www.woolworths.com.au/shop/productdetails/1118153859/oz-nails
#   hedge         artificial boxwood hedge panels (50 x 50 cm tiles) behind a neon sign, LED neon flex 8 mm tube
#   plant         dried pampas grass (about 1.1 m plumes) in a ribbed ceramic floor vase, H40 cm
#   window        arched timber casement: W74 H140 cm, sill at 0.92 m, sheer linen curtains on a brass rod
#   floor         poured terrazzo (blush base, pink / sage / gold chips) with brass divider strips at about 1.2 m

# =====================================================================
#  SETTINGS  -  change these lines, then run the script again
# =====================================================================
ROOM_NAME = "glow_beauty_bar"       # used for the output file names

ROOM_WIDTH = 4.6                    # metres, left to right (along the back wall)
ROOM_DEPTH = 4.0                    # metres, front to back (along the left wall)
WALL_HEIGHT = 2.85                  # metres

THEME = "milk_blush"                # pick one of the colour themes below
THEMES = {                          # any hex colour works; "main" is the velvet, "accent_1" the neon sign
    # "milk_blush": clean daylight - milky white, blush velvet, pink terrazzo, brushed gold, sage greens.
    "milk_blush": {
        "background": "#F4E3E1", "wall": "#F8EEEA", "wall_trim": "#EFDDD8", "floor": "#F2E2DC",
        "wood": "#E3C9AE", "main": "#E9A4B2", "accent_1": "#F2588E", "accent_2": "#F6CBCF", "accent_3": "#B4C8AC",
        "cream": "#FFFAF6", "plant": "#7F9C77", "dark": "#4B3A41",
        "gold": "#C9A66B", "lacquer": "#FFF7F4", "marble": "#F8F3F0", "glass": "#F1F6F9", "mirror": "#E8ECEF",
        "sky": "#FFF6EE", "chip_1": "#E596A6", "chip_2": "#B9CBB0", "chip_3": "#D8B98B", "hedge": "#58784A",
        "hedge_2": "#7B9A5E", "water": "#BFE7E4", "uv": "#CDB8FF", "bulb": "#FFE7C4", "towel": "#FFFFFF",
        "pampas": "#EBDBC2", "neon_white": "#FFF3F6",
    },
    # "jelly_neon": evening glam - lilac and aqua jelly finishes, deep plum walls, pink neon.
    # Lights change too: a dusky window, a weaker sky and brighter neon / bulbs (see LIGHTS below).
    "jelly_neon": {
        "background": "#241C36", "wall": "#56467E", "wall_trim": "#66558F", "floor": "#5A4C80",
        "wood": "#9C88B8", "main": "#B89BF2", "accent_1": "#FF4FA8", "accent_2": "#7563A8", "accent_3": "#7FE3D6",
        "cream": "#F4EEFF", "plant": "#6FA58C", "dark": "#1E1A2C",
        "gold": "#E0C58F", "lacquer": "#EEE7FA", "marble": "#E8E0F4", "glass": "#E3F6FF", "mirror": "#CCC6E0",
        "sky": "#7A58B0", "chip_1": "#B07099", "chip_2": "#5E9F9E", "chip_3": "#8F7EC2", "hedge": "#3E6A55",
        "hedge_2": "#5B8D6C", "water": "#8EF2E6", "uv": "#B39AFF", "bulb": "#FFE2C6", "towel": "#F7F2FF",
        "pampas": "#E9D9CE", "neon_white": "#F2FBFF",
    },
}

SUN_WARMTH = 5600                   # Kelvin: 2500 = sunset orange, 6500 = white daylight (5600 = bright midday)
SUN_STRENGTH = 3.0                  # sunlight through the arched window
LAMP_WARMTH = 2700                  # Kelvin of the globe bulbs round the make-up mirror
LAMP_STRENGTH = 14                  # Watts of the mirror's bulb glow
NEON_STRENGTH = 5.0                 # glow of the neon name sign (higher = brighter tubes)
RING_LIGHT = True                   # the ring light is switched on (cool white glow on the vanity corner)
SEED = 11                           # change to shuffle polish colours on the table, magazines and props

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
JELLY = THEME == "jelly_neon"       # evening theme: translucent jelly finishes and night lighting

STYLE = "glow_beauty_bar"
KIT_VERSION = 2
W, D, H = ROOM_WIDTH, ROOM_DEPTH, WALL_HEIGHT
T = 0.15            # wall thickness
FLOOR_Z = 0.02      # top of the terrazzo; furniture stands here
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



# The room's real materials (one place, so every piece uses the same velvet, lacquer, gold...).
VELVET = M("main", 0.85, "fabric")                 # blush (or lilac) velvet: throne, client chair, stool seat
VELVET_2 = M("accent_3", 0.86, "fabric")           # sage (or aqua) velvet: waiting loveseat, pouf
LACQUER = M("lacquer", 0.32, "plaster", scale=4)   # white satin lacquer joinery: tables, vanity, rack backs
PAINT_PINK = M("accent_2", 0.55, "plaster", scale=3)   # pastel paint: arch niches, reception flutes
PAINT_PINK_V = M("accent_2", 0.5, "plaster", scale=3.2)
MARBLE = M("marble", 0.16, "marble")               # white marble tops
GOLD = M("gold", 0.28, "brushed", metal=1.0)       # brushed brass: legs, trims, frames, standoffs
GOLD_V = M("gold", 0.3, "brushed", metal=1.0, along="Z")
CHROME = M("glass", 0.12, "brushed", metal=1.0, along="Z")   # polished chrome: stool base, ring-light stand
BLACK = M("dark", 0.45, "brushed", metal=0.6)      # black powder-coat / plastic
PLASTER = M("wall", 0.88, "plaster")
TRIM = M("wall_trim", 0.5, "plaster", scale=3)     # painted skirting, window frame, cornice
CERAMIC = M("cream", 0.25, "ceramic")
TOWEL = M("towel", 0.95, "knit", scale=2.5)        # terry towels
LINEN = M("cream", 0.9, "fabric")
PAPER = M("cream", 0.8, "paper")
OAK = M("wood", 0.5, "wood")
GLASS = mat("glass", 0.04, alpha=0.18)             # clear glass / acrylic
ACRYLIC = mat("glass", 0.1, alpha=0.26 if not JELLY else 0.16)
JELLY_AQUA = mat("accent_3", 0.08, emit=0.25 if JELLY else 0.0, alpha=0.72 if JELLY else 1.0)   # jelly acrylic
SHEER = mat("wall_trim", 0.9, alpha=0.5)              # sheer curtain
MIRROR = mat("mirror", 0.1, metal=0.85)            # mirror glass (soft reflection of the room)
WINDOW_GLASS = mat("sky", 0.05, emit=0.3 if not JELLY else 0.8, alpha=0.6)
BULB = mat("bulb", 0.2, emit=LAMP_STRENGTH * 0.15 * (1.3 if JELLY else 1.0))
NEON = mat("accent_1", 0.25, emit=NEON_STRENGTH * 0.5 * (1.5 if JELLY else 1.0))         # brand_color recolours this
NEON_WHITE = mat("neon_white", 0.25, emit=NEON_STRENGTH * 0.4 * (1.3 if JELLY else 1.0))
NEON_BACKER = mat("glass", 0.45, alpha=0.03)            # almost invisible clear acrylic behind the neon
RING_GLOW = mat("cream", 0.3, emit=(3.5 if JELLY else 2.6) if RING_LIGHT else 0.0)
UV_GLOW = mat("uv", 0.3, emit=2.5)
WATER = mat("water", 0.04, emit=0.12, alpha=0.75)
SOIL = mat("soil", 0.95, color="#3A2A20")
HEDGE = mat("hedge", 0.6)
HEDGE_2 = mat("hedge_2", 0.55)
PAMPAS = M("pampas", 0.95, "knit", scale=3)
LEAF = mat("plant", 0.55)
CHIPS = [mat(k, 0.45) for k in ("chip_1", "chip_2", "chip_3", "wood" if JELLY else "cream")]   # terrazzo aggregate
#   (jelly_neon uses lilac instead of white chips so the dark pour does not read as confetti)


def hsv_hex(h, s, v):
    """Hue/saturation/value (0..1) -> '#RRGGBB' (used for the colour-sorted polish wall)."""
    h = (h % 1.0) * 6
    i, f = int(h), h - int(h)
    p, q, t = v * (1 - s), v * (1 - s * f), v * (1 - s * (1 - f))
    r, g, b = [(v, t, p), (q, v, p), (p, v, t), (p, q, v), (t, p, v), (v, p, q)][i % 6]
    return "#%02X%02X%02X" % tuple(int(round(c * 255)) for c in (r, g, b))


def polish(hex_color):
    """Glossy nail-polish colour. In the jelly theme it is see-through like a jelly sweet."""
    if JELLY:
        return mat("polish", 0.06, emit=0.7, alpha=0.93, color=hex_color)
    return mat("polish", 0.08, color=hex_color)


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


def spline(ctrl, steps=6, closed=False):
    """Smooth Catmull-Rom curve through control points (for bentwood, cords, wands, scrolls)."""
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


def sym(half):
    """Left half of a symmetric path (ending on x = 0) -> the whole path, left to right."""
    return list(half) + [(-x, y, z) for (x, y, z) in reversed(half[:-1])]


def tube(name, pts, r, material, parent=None, segs=10, r2=None, closed=False):
    """Round tube swept along a path: bentwood, cords, rails, steam wands, iron scrolls."""
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
    """Turned shape from a (radius, height) profile: cups, cake domes, pots, lamp shades, hoppers."""
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
            # pointed oval leaf (6 points) with a slight fold along the midrib, not a flat diamond
            fold = out.cross(side).normalized() * lw * s * 0.12
            vs = [bm.verts.new(p + out * ln * s * f + side * lw * s * wd - fold * abs(wd) * 2)
                  for f, wd in ((0, 0), (0.25, 0.42), (0.62, 0.36), (1.0, 0), (0.62, -0.36), (0.25, -0.42))]
            bm.faces.new(vs)
    o = _obj(name, bm)
    o.data.materials.append(material)
    (COL_ROOM).objects.link(o)
    o.parent = parent
    return o


def label(name, body, size, loc, material, rot=(R(90), 0, 0), align="CENTER", parent=None, depth=0.003):
    """Plain 3D text that is NOT a portfolio hook (prices, window lettering)."""
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



# --------------------------------------------------------------------- extra shape helpers (arches, soft parts)
def flat(o):
    """Flat shading for big plain surfaces (walls, floor) so they do not get smooth-shading gradients."""
    o.data.polygons.foreach_set("use_smooth", [False] * len(o.data.polygons))
    return o


def soft(name, size, loc, material, parent=None, rot=(0, 0, 0), r=None):
    """Upholstered part: a box with a big round bevel (cushions, velvet channels, arms)."""
    o = box(name, size, loc, material, bevel=r if r is not None else min(size) * 0.45, rot=rot, parent=parent)
    o.modifiers["Bevel"].segments = 5
    return o


def arch_pts(w, h, n=18):
    """Outline (u, z) of an arch: straight sides and a half-circle top. Bottom at z = 0, centred on u = 0."""
    r = w / 2
    spring = max(0.0, h - r)
    return [(-r, 0.0), (r, 0.0)] + [(r * math.cos(math.pi * k / n), spring + r * math.sin(math.pi * k / n))
                                    for k in range(n + 1)]


def arch_path(w, h, n=18):
    """The arch outline without its bottom edge: up the right side, over the top, down the left side."""
    return arch_pts(w, h, n)[1:] + [(-w / 2, 0.0)]


def arch_prism(name, w, h, depth, loc, material, parent=None, rot=(0, 0, 0), bevel=0.003, n=18):
    """Arch-shaped slab facing -Y (niches, mirror, hedge panel, window glass). loc = bottom centre."""
    bm = bmesh.new()
    pts = arch_pts(w, h, n)
    front = [bm.verts.new((u, -depth / 2, z)) for u, z in pts]
    back = [bm.verts.new((u, depth / 2, z)) for u, z in pts]
    bm.faces.new(front)
    bm.faces.new(list(reversed(back)))
    for i in range(len(pts)):
        j = (i + 1) % len(pts)
        bm.faces.new((front[i], front[j], back[j], back[i]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, bevel, None, parent)


def along(path2d, step):
    """Evenly spaced points (u, z) along a 2D polyline, `step` metres apart, ends trimmed by half a step."""
    seg = [(Vector(a), Vector(b)) for a, b in zip(path2d, path2d[1:])]
    total = sum((b - a).length for a, b in seg)
    n = max(1, int(total / step))
    out, want, done = [], [(k + 0.5) * total / n for k in range(n)], 0.0
    for a, b in seg:
        L = (b - a).length
        while want and want[0] <= done + L:
            t = (want.pop(0) - done) / max(L, 1e-9)
            out.append(tuple(a.lerp(b, t)))
        done += L
    return out


def merged(name, parts, parent=None, bevel=0.0, flat_shade=False):
    """Many small boxes / cylinders as ONE mesh (polish bottles, caps, nail tips).
    parts = [("box", (sx, sy, sz), centre, material) | ("cyl", (radius, height, segments), centre, material)]"""
    bm, mats, index = bmesh.new(), [], {}
    for kind, dims, c, m in parts:
        if m.name not in index:
            index[m.name] = len(mats)
            mats.append(m)
        if kind == "box":
            res = bmesh.ops.create_cube(bm, size=1.0, matrix=Matrix.Translation(c) @ Matrix.Diagonal((*dims, 1.0)))
        else:
            r, h, segs = dims
            res = bmesh.ops.create_cone(bm, cap_ends=True, segments=segs, radius1=r, radius2=r, depth=h,
                                        matrix=Matrix.Translation(c))
        for f in {f for v in res["verts"] for f in v.link_faces}:
            f.material_index = index[m.name]
    o = _obj(name, bm)
    for m in mats:
        o.data.materials.append(m)
    if bevel:
        mod = o.modifiers.new("Bevel", "BEVEL")
        mod.width, mod.segments, mod.limit_method = bevel, 2, "ANGLE"
        try:
            mod.harden_normals = True
        except AttributeError:
            pass
    o.data.polygons.foreach_set("use_smooth", [not flat_shade] * len(o.data.polygons))
    COL_ROOM.objects.link(o)
    o.parent = parent
    return o


def flutes(name, parent, x0, x1, y, z0, z1, material, pitch=0.032):
    """Reeded (fluted) joinery: half-round battens side by side across x0..x1 at depth y."""
    n = max(1, int(round(abs(x1 - x0) / pitch)))
    p = (x1 - x0) / n
    for k in range(n):
        cyl(name, abs(p) * 0.5, z1 - z0, (x0 + p * (k + 0.5), y, (z0 + z1) / 2), material, segs=10, bevel=0.002,
            parent=parent)


def flutes_y(name, parent, y0, y1, x, z0, z1, material, pitch=0.032):
    """Fluted joinery on a face that runs along Y (the end of a desk)."""
    n = max(1, int(round(abs(y1 - y0) / pitch)))
    p = (y1 - y0) / n
    for k in range(n):
        cyl(name, abs(p) * 0.5, z1 - z0, (x, y0 + p * (k + 0.5), (z0 + z1) / 2), material, segs=10, bevel=0.002,
            parent=parent)


def brass_leg(name, parent, x, y, h, r_top=0.015, r_foot=0.009, tilt=(0, 0)):
    """Tapered brass furniture leg (Hollywood-Regency style) with a small foot cap."""
    cyl(name, r_foot, h, (x, y, h / 2), GOLD_V, r2=r_top, segs=16, bevel=0.001, rot=(tilt[0], tilt[1], 0),
        parent=parent)
    cyl(f"{name}_Cap", r_foot + 0.002, 0.012, (x, y, 0.006), GOLD, segs=16, bevel=0.002, parent=parent)


def polish_bottle(name, loc, parent, color_hex, cap=None, s=1.0):
    """15 ml square polish bottle (28 x 28 x 52 mm) with a tall round cap (generic shape, no brand)."""
    x, y, z = loc
    no_shadow(box(f"{name}_Glass", (0.03 * s, 0.03 * s, 0.054 * s), (x, y, z + 0.027 * s), GLASS, bevel=0.006 * s,
                  parent=parent))
    box(f"{name}_Lacquer", (0.026 * s, 0.026 * s, 0.046 * s), (x, y, z + 0.025 * s), polish(color_hex), bevel=0.005 * s,
        parent=parent)
    cyl(f"{name}_Cap", 0.0095 * s, 0.03 * s, (x, y, z + 0.069 * s), cap or GOLD_V, segs=14, bevel=0.002, parent=parent)


def furniture_light(root, name, kind, energy, color, local_loc, local_aim=None, size=None):
    """A light that belongs to a placeholder (ring light, polish-wall strip): parented, so it moves with it."""
    bpy.context.view_layer.update()
    mw = root.matrix_world
    loc = mw @ Vector(local_loc)
    aim = (mw @ Vector(local_aim)) if local_aim is not None else None
    o = light(name, kind, energy, color, loc, aim=aim, size=size)
    o.parent = root
    o.matrix_parent_inverse = mw.inverted()
    return o


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


# =====================================================================
#  ROOM SHELL: blush terrazzo, plaster walls, arched window, arch niches
# =====================================================================
box("Floor_Base", (W + T, D + T, 0.2), ((W - T) / 2, (D + T) / 2, -0.1), mat("wall_trim", 0.7), bevel=0.02)
flat(box("Floor_Terrazzo", (W, D, FLOOR_Z), (W / 2, D / 2, FLOOR_Z / 2), M("floor", 0.28, "terrazzo"), bevel=0.002))


def terrazzo_chips():
    """Poured terrazzo: thousands of little irregular marble chips (pink, sage, gold, white) in ONE mesh."""
    rnd = random.Random(SEED + 5)
    bm = bmesh.new()
    weights = (0.34, 0.2, 0.14, 0.32)
    for _ in range(int(W * D * 340)):          # fine aggregate (7-25 mm), dense enough to read as stone
        cx, cy = rnd.uniform(0.02, W - 0.02), rnd.uniform(0.02, D - 0.02)
        r = rnd.choice((0.0045, 0.0055, 0.007, 0.009, 0.012)) * rnd.uniform(0.8, 1.25)
        k, a0 = rnd.randint(5, 7), rnd.uniform(0, 6.3)
        vs = [bm.verts.new((cx + r * rnd.uniform(0.55, 1.0) * math.cos(a0 + 2 * math.pi * i / k),
                            cy + r * rnd.uniform(0.55, 1.0) * math.sin(a0 + 2 * math.pi * i / k), FLOOR_Z + 0.0004))
              for i in range(k)]
        f = bm.faces.new(vs)
        u, acc = rnd.random(), 0.0
        for mi, wgt in enumerate(weights):
            acc += wgt
            if u <= acc:
                f.material_index = mi
                break
    o = _obj("Floor_Terrazzo_Chips", bm)
    for m in CHIPS:
        o.data.materials.append(m)
    flat(o)
    COL_ROOM.objects.link(o)


terrazzo_chips()
for k in range(1, 4):                       # brass divider strips set into the pour (about 1.15 x 1.0 m bays)
    box("Floor_Brass_Strip_X", (0.005, D, 0.0012), (k * W / 4, D / 2, FLOOR_Z + 0.0005), GOLD, bevel=0)
    box("Floor_Brass_Strip_Y", (W, 0.005, 0.0012), (W / 2, k * D / 4, FLOOR_Z + 0.0005), GOLD, bevel=0)

# Left wall with an arched window (sill 0.92 m), back wall plain.
WIN_Y0, WIN_W, WIN_Z0, WIN_H = 1.78, 0.74, 0.92, 1.42
WIN_CY = WIN_Y0 + WIN_W / 2
left = flat(box("Wall_Left", (T, D + T, H), (-T / 2, (D + T) / 2, H / 2), PLASTER, bevel=0.0))
cutter = arch_prism("Window_Cutter", WIN_W, WIN_H, T * 3, (-T / 2, WIN_CY, WIN_Z0), mat("wall"), rot=(0, 0, R(90)),
                    bevel=0)
cutter.hide_render = cutter.hide_viewport = True
boolean = left.modifiers.new("Window", "BOOLEAN")
boolean.operation, boolean.object = "DIFFERENCE", cutter
flat(box("Wall_Back", (W + T, T, H), ((W - T) / 2, D + T / 2, H / 2), PLASTER, bevel=0.0))

# Diorama cap on top of the walls (painted cornice with a fine brass line under it).
box("Trim_Top_Back", (W + T + 0.04, T + 0.06, 0.08), ((W - T) / 2, D + T / 2, H + 0.04), TRIM, bevel=0.01)
box("Trim_Top_Left", (T + 0.06, D + T + 0.04, 0.08), (-T / 2, (D + T) / 2 - 0.02, H + 0.04), TRIM, bevel=0.01)
box("Trim_Brass_Back", (W, 0.006, 0.012), (W / 2, D - 0.003, H - 0.04), GOLD, bevel=0)
box("Trim_Brass_Left", (0.006, D, 0.012), (0.003, D / 2, H - 0.04), GOLD, bevel=0)

# Painted skirting (100 mm).
SK = 0.1
box("Skirting_Back", (W, 0.016, SK), (W / 2, D - 0.008, FLOOR_Z + SK / 2), TRIM, bevel=0.004)
box("Skirting_Left", (0.016, D - 0.016, SK), (0.008, (D - 0.016) / 2, FLOOR_Z + SK / 2), TRIM, bevel=0.004)

# Arched window: round architrave moulding, painted casement with glazing bars, glass, oak window board.
win2d = arch_path(WIN_W + 0.1, WIN_H + 0.05)
tube("Window_Architrave", [(0.012, WIN_CY + u, WIN_Z0 - 0.05 + z) for u, z in win2d], 0.028, TRIM, segs=12)
casement = arch_path(WIN_W - 0.02, WIN_H - 0.01)
tube("Window_Frame", [(-0.05, WIN_CY + u, WIN_Z0 + z) for u, z in casement], 0.024, TRIM, segs=10)
box("Window_Frame_Bottom", (0.05, WIN_W - 0.02, 0.05), (-0.05, WIN_CY, WIN_Z0 + 0.025), TRIM, bevel=0.005)
spring_z = WIN_Z0 + WIN_H - WIN_W / 2
box("Window_Mullion", (0.035, 0.03, WIN_H - 0.04), (-0.05, WIN_CY, WIN_Z0 + (WIN_H - 0.04) / 2), TRIM, bevel=0.004)
box("Window_Transom", (0.035, WIN_W - 0.04, 0.03), (-0.05, WIN_CY, spring_z), TRIM, bevel=0.004)
for a in (R(40), R(140)):                    # fanlight glazing bars, like sun rays
    rr = WIN_W / 2 - 0.02
    tube("Window_Fan_Bar", [(-0.05, WIN_CY, spring_z), (-0.05, WIN_CY + rr * math.cos(a), spring_z + rr * math.sin(a))],
         0.012, TRIM, segs=8)
no_shadow(arch_prism("Window_Glass", WIN_W - 0.03, WIN_H - 0.02, 0.006, (-0.07, WIN_CY, WIN_Z0 + 0.01), WINDOW_GLASS,
                     rot=(0, 0, R(90)), bevel=0))
box("Window_Board", (0.2, WIN_W + 0.12, 0.025), (0.07, WIN_CY, WIN_Z0 + 0.0125), MARBLE, bevel=0.004)

# Sheer linen curtains on a brass rod with rings and ball finials, pulled to each side of the window.
ROD_Z = WIN_Z0 + WIN_H + 0.14
ROD_Y0, ROD_Y1 = WIN_Y0 - 0.22, WIN_Y0 + WIN_W + 0.22
cyl("Curtain_Rod", 0.011, ROD_Y1 - ROD_Y0, (0.1, WIN_CY, ROD_Z), GOLD, rot=(R(90), 0, 0), segs=14)
for yy in (ROD_Y0 - 0.02, ROD_Y1 + 0.02):
    ball("Curtain_Finial", 0.026, (0.1, yy, ROD_Z), GOLD)
    box("Curtain_Bracket", (0.1, 0.012, 0.012), (0.05, yy + (0.04 if yy < WIN_CY else -0.04), ROD_Z), GOLD, bevel=0.002)


def curtain(name, y0, y1, folds=5, amp=0.022):
    """Sheer curtain panel: vertical folds (a sine wave in plan) from the rod to just above the floor."""
    bm = bmesh.new()
    cols, top, bot = folds * 6, ROD_Z - 0.03, FLOOR_Z + 0.03
    rows = []
    for z, flare in ((top, 0.0), (top - 0.3, 0.3), (bot + 0.4, 0.9), (bot, 1.0)):
        row = []
        for i in range(cols + 1):
            t = i / cols
            yy = y0 + (y1 - y0) * t
            row.append(bm.verts.new((0.1 + amp * (1 + 0.6 * flare) * math.sin(t * folds * 2 * math.pi), yy, z)))
        rows.append(row)
    for a, b in zip(rows, rows[1:]):
        for i in range(cols):
            bm.faces.new((a[i], a[i + 1], b[i + 1], b[i]))
    o = _obj(name, bm)
    o.data.materials.append(SHEER)
    COL_ROOM.objects.link(o)
    for k in range(folds + 1):               # curtain rings on the rod
        cyl(f"{name}_Ring", 0.019, 0.006, (0.1, y0 + (y1 - y0) * k / folds, ROD_Z), GOLD, rot=(R(90), 0, 0), segs=14,
            bevel=0)
    return o


no_shadow(curtain("Curtain_Front", ROD_Y0 + 0.02, WIN_Y0 + 0.08))
no_shadow(curtain("Curtain_Back", WIN_Y0 + WIN_W - 0.08, ROD_Y1 - 0.02))

# Painted arch niches on the back wall: one frames the polish wall, the other is a boxwood hedge (neon sign).
NICHE_X, NICHE_W, NICHE_H = 1.6, 1.7, 2.62
arch_prism("Niche_Polish", NICHE_W, NICHE_H, 0.012, (NICHE_X, D - 0.006, FLOOR_Z), PAINT_PINK, bevel=0.002)
tube("Niche_Polish_Brass", [(NICHE_X + u, D - 0.013, FLOOR_Z + z) for u, z in arch_path(NICHE_W, NICHE_H)], 0.006, GOLD,
     segs=8)
label("Niche_Label", "colour bar", 0.075, (NICHE_X, D - 0.014, 2.36), mat("gold", 0.25, metal=1.0, emit=0.1),
      depth=0.002)
for k, sx in enumerate((-1, 1)):            # tiny brass stars either side of the lettering
    ball(f"Niche_Star_{k}", 0.012, (NICHE_X + sx * 0.33, D - 0.014, 2.36), GOLD, scale=(1, 0.3, 1))

HEDGE_X, HEDGE_W, HEDGE_H, HEDGE_Z = 3.8, 1.3, 2.5, FLOOR_Z + 0.1
arch_prism("Hedge_Backing", HEDGE_W, HEDGE_H, 0.02, (HEDGE_X, D - 0.01, HEDGE_Z), HEDGE, bevel=0.002)
tube("Hedge_Brass_Frame", [(HEDGE_X + u, D - 0.03, HEDGE_Z + z) for u, z in arch_path(HEDGE_W + 0.03, HEDGE_H + 0.015)],
     0.013, GOLD, segs=10)


def hedge_wall():
    """Artificial boxwood hedge panel: thousands of small leaves filling the arch (two greens)."""
    r, spring = HEDGE_W / 2 - 0.035, HEDGE_H - HEDGE_W / 2
    clusters = []
    step = 0.075
    for i in range(int(HEDGE_W / step) + 1):
        for j in range(int(HEDGE_H / step) + 1):
            u, z = -HEDGE_W / 2 + 0.04 + i * step, 0.04 + j * step
            if abs(u) > r or (z > spring and u * u + (z - spring) ** 2 > r * r):
                continue
            clusters.append(((HEDGE_X + u, D - 0.032, HEDGE_Z + z), 0.04))
    foliage("Hedge_Leaves", clusters, 9, (0.032, 0.02), HEDGE, seed=SEED + 21, droop=0.0)
    foliage("Hedge_Leaves_Light", clusters, 5, (0.03, 0.019), HEDGE_2, seed=SEED + 22, droop=0.0)
    blooms = []                              # a few small white blossoms tucked into the lower corners
    rnd = random.Random(SEED + 23)
    for _ in range(26):
        sx = rnd.choice((-1, 1))
        u = sx * rnd.uniform(0.25, r - 0.02)
        z = rnd.uniform(0.08, 0.75) if abs(u) > 0.42 else rnd.uniform(0.05, 0.25)
        sz = rnd.uniform(0.026, 0.04)
        blooms.append(("box", (sz, 0.018, sz), (HEDGE_X + u, D - 0.08, HEDGE_Z + z),
                       rnd.choice((CERAMIC, mat("accent_2", 0.6), mat("cream", 0.6)))))
    merged("Hedge_Blooms", blooms, bevel=0.008)


hedge_wall()


# =====================================================================
#  FURNITURE SLOTS  (same names in every template)
#  size = (width, depth, height); front of the furniture faces local -Y
# =====================================================================
MANI_X, MANI_Y = NICHE_X, 3.0                       # manicure station, in front of the polish wall
THRONE_D = 1.55
slot("wall_shelf",  (1.45, 0.13, 1.25), (NICHE_X, D - 0.065), z=0.92, kind="wall", shape="shelf")
slot("desk",        (1.1, 0.48, 0.76), (MANI_X, MANI_Y), shape="table")
slot("stool",       (0.5, 0.5, 0.85), (MANI_X, MANI_Y + 0.52), shape="stool")
slot("chair",       (0.6, 0.6, 0.8), (MANI_X, MANI_Y - 0.68), turn=180, shape="chair")
slot("salon_chair", (0.95, THRONE_D, 1.45), (HEDGE_X, D - THRONE_D / 2), shape="chair")
slot("plant",       (0.42, 0.42, 1.35), (2.8, D - 0.27), shape="plant")
slot("counter",     (1.4, 0.6, 1.07), (0.85, 0.9), turn=90, shape="counter")
slot("mirror",      (0.72, 0.06, 0.98), (0.03, 3.08), z=0.94, turn=90, kind="wall", shape="frame")
slot("floor_lamp",  (0.46, 0.46, 1.75), (0.46, 3.64), turn=40, shape="lamp")   # ring faces into the room
slot("sofa",        (1.38, 0.78, 0.8), (4.15, 1.15), turn=-90, shape="sofa")


# =====================================================================
#  PLACEHOLDER FURNITURE  (replaced when you add your own with add_furniture.py)
# =====================================================================
LACQ_MAIN = M("main", 0.4, "plaster", scale=3)      # blush satin lacquer (fluted panels)
LACQ_MAIN_V = M("main", 0.42, "plaster", scale=3.3)


def polish_colour(col, row, cols, rows):
    """Colour-sorted salon wall: nudes first, then pink > red > coral > yellow > green > teal > blue > lilac.
    Top rows are pastel, bottom rows deep."""
    depth = (rows - 1 - row) / (rows - 1)            # 0 = top (pastel) .. 1 = bottom (deep)
    if col < 3:                                      # nudes and milky pinks
        return hsv_hex(0.04 + 0.015 * col, 0.12 + 0.3 * depth, 0.97 - 0.3 * depth)
    t = (col - 3) / (cols - 4)
    if JELLY:                                        # jelly-sweet shades: stronger colour on every row
        return hsv_hex(0.97 + 0.8 * t, 0.42 + 0.48 * depth, 0.95 - 0.3 * depth)
    return hsv_hex(0.97 + 0.8 * t, 0.2 + 0.62 * depth, 0.98 - 0.26 * depth)


def build_wall_shelf():
    """The polish wall: three 6-tier clear acrylic racks side by side on a white lacquer board in a brass frame,
    with seven rows of colour-sorted bottles (the middle row's feature shades follow accent_1 / brand_color)."""
    root, w, d, h = furniture_root("wall_shelf")
    by = d / 2
    board = LACQUER if not JELLY else mat("dark", 0.35)   # evening: a dark board so the jelly colours glow
    box("Polish_Board", (w, 0.016, h), (0, by - 0.008, h / 2), board, bevel=0.004, parent=root)
    for sx in (-1, 1):
        box("Polish_Frame_Side", (0.022, 0.03, h + 0.044), (sx * (w / 2 + 0.011), by - 0.015, h / 2), GOLD_V,
            bevel=0.003, parent=root)
    for zz in (-0.011, h + 0.011):
        box("Polish_Frame_Rail", (w + 0.044, 0.03, 0.022), (0, by - 0.015, zz), GOLD, bevel=0.003, parent=root)
    for sx in (-1, 1):                               # joints between the three acrylic racks
        box("Polish_Rack_Joint", (0.006, 0.012, h - 0.04), (sx * w / 6, by - 0.022, h / 2), ACRYLIC, bevel=0,
            parent=root)
    rows, cols = 7, 24
    pitch = (w - 0.08) / cols
    rnd = random.Random(SEED + 31)
    bottles, caps = [], []
    for r in range(rows):
        z = 0.075 + r * 0.163
        ly = by - 0.016 - 0.04
        box("Polish_Ledge", (w - 0.04, 0.08, 0.008), (0, ly, z - 0.004), ACRYLIC, bevel=0.002, parent=root)
        box("Polish_Lip", (w - 0.04, 0.006, 0.03), (0, ly - 0.04, z + 0.007), ACRYLIC, bevel=0.002, parent=root)
        box("Polish_Lip_Edge", (w - 0.04, 0.007, 0.003), (0, ly - 0.04, z + 0.021), GOLD, bevel=0, parent=root)
        for c in range(cols):
            if rnd.random() < 0.05:                  # a few gaps: bottles out on the tables
                continue
            x = -w / 2 + 0.04 + pitch * (c + 0.5)
            yy = ly + rnd.uniform(-0.006, 0.006)
            feature = r == 3 and 11 <= c <= 13
            m = mat("accent_1", 0.08) if feature else polish(polish_colour(c, r, cols, rows))
            bottles.append(("box", (0.03, 0.03, 0.054), (x, yy, z + 0.027), m))
            caps.append(("cyl", (0.0095, 0.03, 12), (x, yy, z + 0.069), GOLD_V if r % 2 == 0 else CERAMIC))
    merged("Polish_Bottles", bottles, parent=root, bevel=0.006)
    merged("Polish_Caps", caps, parent=root, bevel=0.002)
    box("Polish_LED", (w - 0.06, 0.012, 0.006), (0, by - 0.03, h - 0.02), mat("cream", 0.3, emit=3.0), bevel=0,
        parent=root)
    furniture_light(root, "Light_PolishWall", "AREA", 26 if not JELLY else 12, kelvin(5200),
                    (0, -0.8, h + 0.2), (0, by, h * 0.45), size=1.3)


def build_desk():
    """Single manicure table: 22 mm white marble top, blush fluted modesty panel, drawer pedestal with brass
    pulls, tapered brass legs, a vented dust collector, towel + acrylic hand rest, an LED gel lamp,
    a gooseneck task lamp, a nail-art tip wheel, polish in use and a cotton jar."""
    root, w, d, h = furniture_root("desk")
    top = h
    box("Mani_Top", (w, d, 0.022), (0, 0, top - 0.011), MARBLE, bevel=0.005, parent=root)
    px = w / 2 - 0.16                                # drawer pedestal (right hand side)
    box("Mani_Pedestal", (0.3, d - 0.04, top - 0.022 - 0.05), (px, 0, 0.05 + (top - 0.072) / 2), LACQUER, bevel=0.004,
        parent=root)
    box("Mani_Plinth", (0.28, d - 0.08, 0.05), (px, 0, 0.025), GOLD, bevel=0.003, parent=root)
    dh = (top - 0.022 - 0.05 - 0.016) / 3
    for k in range(3):                               # three drawers on the technician's side, 4 mm gaps
        z = 0.05 + 0.004 + dh * (k + 0.5)
        box("Mani_Drawer", (0.28, 0.018, dh - 0.004), (px, d / 2 - 0.02 + 0.009, z), LACQUER, bevel=0.003, parent=root)
        box("Mani_Drawer_Pull", (0.1, 0.012, 0.01), (px, d / 2 - 0.002, z + dh * 0.25), GOLD, bevel=0.003, parent=root)
    # fluted modesty panel on the client side, between the legs and the pedestal
    x0, x1 = -w / 2 + 0.04, px - 0.15
    box("Mani_Panel", (x1 - x0, 0.018, top - 0.18), ((x0 + x1) / 2, -d / 2 + 0.04, 0.16 + (top - 0.18) / 2 - 0.011),
        LACQ_MAIN, bevel=0.003, parent=root)
    flutes("Mani_Flute", root, x0 + 0.005, x1 - 0.005, -d / 2 + 0.03, 0.16, top - 0.03, LACQ_MAIN_V)
    flutes("Mani_Flute_Ped", root, px - 0.145, px + 0.145, -d / 2 + 0.02, 0.06, top - 0.03, LACQ_MAIN_V)
    box("Mani_Brass_Band", (w - 0.02, 0.004, 0.01), (0, -d / 2 + 0.011, top - 0.03), GOLD, bevel=0, parent=root)
    for sy in (-1, 1):
        brass_leg("Mani_Leg", root, -w / 2 + 0.04, sy * (d / 2 - 0.05), top - 0.022)
    cyl("Mani_Stretcher", 0.008, d - 0.1, (-w / 2 + 0.04, 0, 0.14), GOLD, rot=(R(90), 0, 0), parent=root)
    # vented dust collector in the top, under the client's hand
    box("Mani_Vent", (0.2, 0.1, 0.002), (-0.02, 0.02, top + 0.001), mat("dark", 0.6), bevel=0, parent=root)
    for k in range(6):
        box("Mani_Vent_Bar", (0.006, 0.1, 0.003), (-0.105 + k * 0.034, 0.02, top + 0.0025), GOLD, bevel=0, parent=root)
    # folded towel + acrylic hand rest with a velvet pad
    box("Mani_Towel", (0.34, 0.17, 0.014), (-0.02, -0.13, top + 0.007), TOWEL, bevel=0.005, parent=root)
    box("Mani_HandRest_Base", (0.22, 0.09, 0.03), (-0.02, -0.14, top + 0.029), ACRYLIC, bevel=0.012, parent=root)
    soft("Mani_HandRest_Pad", (0.2, 0.08, 0.04), (-0.02, -0.14, top + 0.06), VELVET, parent=root)
    box("Mani_File", (0.18, 0.02, 0.004), (0.12, -0.17, top + 0.016), mat("accent_2", 0.8), bevel=0.0015,
        rot=(0, 0, R(12)), parent=root)
    cyl("Mani_Pusher", 0.004, 0.13, (-0.2, -0.17, top + 0.018), CHROME, rot=(0, R(90), R(-8)), parent=root)
    # 48 W LED gel lamp (tunnel type), opening towards the client, with a timer display on top
    lamp = empty("Mani_LED_Lamp", (0.3, -0.06, top), rot=(0, 0, R(-8)), parent=root)
    shell = JELLY_AQUA if JELLY else LACQUER
    box("LED_Lamp_Base", (0.21, 0.19, 0.012), (0, 0, 0.006), CERAMIC, bevel=0.004, parent=lamp)
    box("LED_Lamp_Shell", (0.2, 0.18, 0.085), (0, 0.005, 0.0545), shell, bevel=0.035, parent=lamp)
    box("LED_Lamp_Opening", (0.15, 0.06, 0.05), (0, -0.07, 0.037), mat("dark", 0.5, color="#2B2333"), bevel=0.012,
        parent=lamp)
    box("LED_Lamp_Glow", (0.13, 0.004, 0.028), (0, -0.04, 0.04), UV_GLOW, bevel=0, parent=lamp)
    box("LED_Lamp_Display", (0.05, 0.02, 0.002), (0, -0.02, 0.0975), mat("dark", 0.3), bevel=0, parent=lamp)
    box("LED_Lamp_Digits", (0.03, 0.008, 0.001), (0, -0.02, 0.099), mat("water", 0.3, emit=2.0), bevel=0, parent=lamp)
    # gooseneck LED task lamp at the back-left corner
    lx, ly = -w / 2 + 0.1, d / 2 - 0.08
    cyl("TaskLamp_Base", 0.06, 0.018, (lx, ly, top + 0.009), GOLD, segs=24, parent=root)
    arm = spline([(lx, ly, top + 0.018), (lx, ly - 0.01, top + 0.25), (lx + 0.08, ly - 0.06, top + 0.38),
                  (lx + 0.2, ly - 0.12, top + 0.36)], 5)
    tube("TaskLamp_Neck", arm, 0.007, GOLD, parent=root, segs=8)
    tl = box("TaskLamp_Head", (0.15, 0.05, 0.022), (lx + 0.25, ly - 0.14, top + 0.35), CERAMIC, bevel=0.008,
             rot=(0, R(-10), R(-28)), parent=root)
    box("TaskLamp_Diffuser", (0.13, 0.035, 0.002), (0, 0, -0.012), mat("cream", 0.3, emit=4.0), bevel=0, parent=tl)
    # nail-art tip wheel on its stand: 20 tips round a clear disc (the project gallery of a nail artist)
    wh = empty("Mani_TipWheel", (-0.26, 0.1, top), rot=(0, 0, R(18)), parent=root)
    box("TipWheel_Foot", (0.08, 0.05, 0.008), (0, 0, 0.004), GOLD, bevel=0.003, parent=wh)
    cyl("TipWheel_Post", 0.004, 0.06, (0, 0, 0.035), GOLD, parent=wh)
    no_shadow(cyl("TipWheel_Disc", 0.068, 0.003, (0, 0, 0.13), ACRYLIC, rot=(R(90), 0, 0), segs=32, parent=wh))
    tips = []
    for k in range(20):
        a = 2 * math.pi * k / 20
        tips.append(("box", (0.011, 0.004, 0.02), (0.052 * math.cos(a), -0.003, 0.13 + 0.052 * math.sin(a)),
                     polish(hsv_hex(0.97 + 0.8 * k / 20, 0.45, 0.95))))
    merged("TipWheel_Tips", tips, parent=wh, bevel=0.004)
    # polish in use, cotton jar, pump bottle
    for k in range(3):
        polish_bottle(f"Mani_Polish_{k}", (0.02 + k * 0.05, 0.15, top), root,
                      polish_colour(random.randint(3, 22), random.randint(1, 5), 24, 7))
    no_shadow(cyl("Cotton_Jar", 0.04, 0.1, (-0.42, -0.11, top + 0.05), GLASS, bevel=0.006, parent=root))
    for k in range(5):
        ball("Cotton_Ball", 0.02, (-0.42 + random.uniform(-0.015, 0.015), -0.11 + random.uniform(-0.015, 0.015),
                                   top + 0.02 + k * 0.016), mat("towel", 0.95), parent=root, segs=10)
    cyl("Cotton_Jar_Lid", 0.042, 0.012, (-0.42, -0.11, top + 0.106), GOLD, parent=root)
    cyl("Pump_Bottle", 0.026, 0.13, (0.46, 0.15, top + 0.065), mat("accent_2", 0.2), bevel=0.008, parent=root)
    cyl("Pump_Head", 0.01, 0.035, (0.46, 0.15, top + 0.148), GOLD, parent=root)
    box("Pump_Nozzle", (0.035, 0.01, 0.01), (0.475, 0.15, top + 0.16), GOLD, bevel=0.003, parent=root)


def tub_shell(name, parent, r_in, r_out, a0, a1, z0, top, material, n=28):
    """Curved upholstered back of a tub chair: a thick arc of padding whose top height follows top(angle).
    Angle 0 points to local +Y (the back of the chair)."""
    bm = bmesh.new()
    rings = []
    for i in range(n + 1):
        a = a0 + (a1 - a0) * i / n
        s_, c_ = math.sin(a), math.cos(a)
        zt = top(a)
        rings.append([bm.verts.new((r * s_, r * c_, z)) for r, z in ((r_out, z0), (r_out, zt), (r_in, zt), (r_in, z0))])
    for p, q in zip(rings, rings[1:]):
        for k in range(4):
            bm.faces.new((p[k], q[k], q[(k + 1) % 4], p[(k + 1) % 4]))
    bm.faces.new(rings[0])
    bm.faces.new(list(reversed(rings[-1])))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    o = _finish(_obj(name, bm), material, 0.025, None, parent)
    o.modifiers["Bevel"].segments = 4
    return o


def build_chair():
    """Client chair: velvet channel-tufted tub chair on four tapered brass legs, seat 46 cm. The back is one
    curved padded shell with vertical channels sewn into its inside face and a soft rolled top edge."""
    root, w, d, h = furniture_root("chair")
    for sx in (-1, 1):
        for sy in (-1, 1):
            brass_leg("Chair_Leg", root, sx * 0.2, sy * 0.18, 0.21, r_top=0.014, r_foot=0.008)
    soft("Chair_Base", (0.56, 0.52, 0.2), (0, 0.0, 0.3), VELVET, parent=root, r=0.06)
    soft("Chair_Seat", (0.44, 0.4, 0.08), (0, -0.04, 0.43), VELVET, parent=root, r=0.035)
    box("Chair_Piping", (0.5, 0.004, 0.012), (0, -0.262, 0.215), GOLD, bevel=0, parent=root)
    a0, a1 = R(-112), R(112)

    def top(a):
        return 0.6 + 0.16 * math.cos(a * 0.85)
    tub_shell("Chair_Back", root, 0.215, 0.285, a0, a1, 0.36, top, VELVET)
    tube("Chair_Back_Roll", [(0.25 * math.sin(a), 0.25 * math.cos(a), top(a) - 0.005) for a in
                             (a0 + (a1 - a0) * k / 30 for k in range(31))], 0.036, VELVET, parent=root, segs=12)
    for i in range(9):                                # channels sewn into the inside face
        a = R(-96 + 192 * i / 8)
        soft("Chair_Channel", (0.075, 0.04, top(a) - 0.47), (0.205 * math.sin(a), 0.205 * math.cos(a),
                                                            (top(a) + 0.44) / 2), VELVET, rot=(0, 0, -a), parent=root,
             r=0.019)


def build_stool():
    """Technician stool: chrome 5-star base on twin-wheel casters, gas lift, velvet seat and a small back pad."""
    root, w, d, h = furniture_root("stool")
    for k in range(5):
        a = 2 * math.pi * k / 5 + R(90)
        box("Stool_Star", (0.22, 0.035, 0.022), (0.11 * math.cos(a), 0.11 * math.sin(a), 0.075), CHROME, bevel=0.008,
            rot=(0, 0, a), parent=root)
        box("Stool_Caster_Fork", (0.02, 0.025, 0.03), (0.215 * math.cos(a), 0.215 * math.sin(a), 0.05), BLACK,
            bevel=0.006, parent=root)
        cyl("Stool_Caster", 0.024, 0.03, (0.215 * math.cos(a), 0.215 * math.sin(a), 0.025), BLACK, rot=(0, R(90), a),
            segs=16, bevel=0.006, parent=root)
    cyl("Stool_Hub", 0.04, 0.05, (0, 0, 0.085), CHROME, parent=root)
    cyl("Stool_Gas_Lift", 0.026, 0.22, (0, 0, 0.2), BLACK, parent=root)
    cyl("Stool_Gas_Rod", 0.02, 0.14, (0, 0, 0.37), CHROME, parent=root)
    cyl("Stool_Seat_Plate", 0.09, 0.02, (0, 0, 0.45), BLACK, parent=root)
    cyl("Stool_Seat", 0.19, 0.08, (0, 0, 0.5), VELVET, segs=40, bevel=0.03, parent=root)
    tube("Stool_Lever", [(0.06, -0.02, 0.445), (0.17, -0.06, 0.43)], 0.005, CHROME, parent=root)
    tube("Stool_Back_Bar", spline([(0, 0.08, 0.45), (0, 0.18, 0.47), (0, 0.205, 0.6), (0, 0.205, 0.7)], 4), 0.012,
         CHROME, parent=root)
    soft("Stool_Back_Pad", (0.3, 0.05, 0.12), (0, 0.215, 0.74), VELVET, parent=root, r=0.022)


def build_salon_chair():
    """Pedicure 'throne': a velvet wing chair with an arched channel-tufted back on a raised fluted plinth with a
    marble cap and LED under-glow, a foot step with a glazed foot basin, rolled towels and a scrub jar."""
    root, w, d, h = furniture_root("salon_chair")
    PL_H, py0 = 0.34, -0.06                           # plinth height, plinth front edge
    pd = d / 2 - py0
    pcy = (py0 + d / 2) / 2
    box("Throne_Plinth", (w - 0.04, pd - 0.04, PL_H - 0.03), (0, pcy + 0.02, (PL_H - 0.03) / 2), LACQUER, bevel=0.004,
        parent=root)
    flutes("Throne_Plinth_Flute", root, -w / 2 + 0.03, w / 2 - 0.03, py0 + 0.02, 0.03, PL_H - 0.035, LACQ_MAIN_V)
    box("Throne_Plinth_Cap", (w, pd, 0.03), (0, pcy, PL_H - 0.015), MARBLE, bevel=0.004, parent=root)
    box("Throne_Plinth_LED", (w - 0.08, 0.006, 0.006), (0, py0 + 0.012, PL_H - 0.036), mat("cream", 0.3, emit=3.0),
        bevel=0, parent=root)
    sd = py0 + d / 2                                  # foot step in front
    box("Throne_Step", (w - 0.04, sd - 0.02, 0.12), (0, -d / 2 + sd / 2 + 0.01, 0.06), LACQUER, bevel=0.004,
        parent=root)
    box("Throne_Step_Cap", (w, sd, 0.025), (0, -d / 2 + sd / 2, 0.1325), MARBLE, bevel=0.004, parent=root)
    box("Throne_Step_Kick", (w - 0.06, 0.006, 0.04), (0, -d / 2 + 0.012, 0.03), GOLD, bevel=0, parent=root)
    # foot basin: a glazed bowl on a short foot, with water and a brass rim
    bx, by_, bz = 0, -d / 2 + 0.33, 0.145
    cyl("Basin_Foot", 0.13, 0.03, (bx, by_, bz + 0.015), GOLD, segs=32, parent=root)
    lathe("Basin_Bowl", [(0, 0.02), (0.15, 0.02), (0.21, 0.07), (0.24, 0.17), (0.245, 0.18), (0.228, 0.18),
                         (0.2, 0.08), (0.15, 0.045), (0, 0.045)], (bx, by_, bz), CERAMIC, segs=40, parent=root)
    tube("Basin_Rim", ring_pts(0.238, bz + 0.18, 40, bx, by_), 0.006, GOLD, parent=root, closed=True)
    cyl("Basin_Water", 0.214, 0.004, (bx, by_, bz + 0.14), WATER, segs=40, bevel=0, parent=root)
    for k, fx in enumerate((-0.07, 0.07)):           # floating rose petals
        ball(f"Basin_Petal_{k}", 0.015, (bx + fx, by_ + 0.03 * k, bz + 0.143), mat("accent_1", 0.5),
             scale=(1, 0.7, 0.2),
             parent=root, segs=10)
    for k, fy in enumerate((-0.64, -0.52)):          # rolled towels on the step
        cyl(f"Throne_Towel_{k}", 0.042, 0.26, (0.34, fy, 0.18 + 0.0), TOWEL, rot=(0, R(90), 0), segs=20, bevel=0.012,
            parent=root)
    cyl("Throne_Scrub_Jar", 0.045, 0.06, (-0.34, -0.6, 0.175), mat("accent_2", 0.25), bevel=0.01, parent=root)
    cyl("Throne_Scrub_Lid", 0.047, 0.018, (-0.34, -0.6, 0.214), GOLD, parent=root)
    # the chair on the plinth
    soft("Throne_Base", (0.86, 0.74, 0.26), (0, 0.38, PL_H + 0.13), VELVET, parent=root, r=0.03)
    box("Throne_Base_Piping", (0.86, 0.006, 0.014), (0, 0.38 - 0.372, PL_H + 0.02), GOLD, bevel=0, parent=root)
    soft("Throne_Seat", (0.6, 0.62, 0.15), (0, 0.3, PL_H + 0.26 + 0.07), VELVET, parent=root, r=0.05)
    for sx in (-1, 1):
        soft("Throne_Arm", (0.13, 0.72, 0.58), (sx * 0.365, 0.37, PL_H + 0.05 + 0.29), VELVET, parent=root, r=0.04)
        cyl("Throne_Arm_Roll", 0.078, 0.74, (sx * 0.37, 0.36, PL_H + 0.62), VELVET, rot=(R(90), 0, 0), segs=24,
            bevel=0.03, parent=root)
        cyl("Throne_Arm_Medallion", 0.05, 0.012, (sx * 0.37, 0.36 - 0.376, PL_H + 0.62), GOLD, rot=(R(90), 0, 0),
            segs=24, parent=root)
    back_z0, bw = PL_H + 0.22, 0.88
    br, bspring = bw / 2, (h - back_z0) - bw / 2
    arch_prism("Throne_Back_Shell", bw, h - back_z0, 0.09, (0, 0.72, back_z0), VELVET, parent=root, bevel=0.03)
    tube("Throne_Back_Piping", [(u, 0.674, back_z0 + z) for u, z in arch_path(bw + 0.004, h - back_z0 + 0.002)],
         0.008, GOLD, parent=root)
    for i in range(7):
        x = -0.33 + i * 0.11
        topz = back_z0 + bspring + math.sqrt(max(0.0, (br - 0.05) ** 2 - x * x)) - 0.02
        y = 0.64 + 0.0 * x
        soft("Throne_Channel", (0.108, 0.12, topz - (PL_H + 0.26)), (x, y, (topz + PL_H + 0.26) / 2), VELVET,
             parent=root, r=0.05)
    soft("Throne_Cushion", (0.36, 0.12, 0.26), (0.06, 0.5, PL_H + 0.52), mat("cream", 0.9) if not JELLY else
         VELVET_2, rot=(R(-12), 0, R(8)), parent=root, r=0.05)


def build_counter():
    """Reception desk: recessed brass kick, blush fluted front, white marble transaction ledge at 107 cm and a
    lower work top behind it, a booking tablet on a swivel stand, card reader, business cards and tulips."""
    root, w, d, h = furniture_root("counter")
    box("Desk_Kick", (w - 0.06, d - 0.1, 0.06), (0, 0.03, 0.03), GOLD, bevel=0.003, parent=root)
    fy = -d / 2 + 0.17                                # the tall front block
    box("Desk_Front_Block", (w, 0.3, h - 0.1), (0, fy, 0.06 + (h - 0.1) / 2), LACQUER, bevel=0.004, parent=root)
    flutes("Desk_Flute", root, -w / 2 + 0.02, w / 2 - 0.02, fy - 0.15, 0.07, h - 0.05, PAINT_PINK_V, pitch=0.036)
    flutes_y("Desk_Flute_End", root, fy - 0.14, fy + 0.14, -w / 2, 0.07, h - 0.05, PAINT_PINK_V, pitch=0.036)
    box("Desk_Back_Block", (w, 0.27, 0.7), (0, d / 2 - 0.135, 0.06 + 0.35), LACQUER, bevel=0.004, parent=root)
    box("Desk_Work_Top", (w, 0.3, 0.025), (0, d / 2 - 0.15, 0.7725), MARBLE, bevel=0.004, parent=root)
    box("Desk_Ledge", (w + 0.04, 0.34, 0.03), (0, fy - 0.01, h - 0.015), MARBLE, bevel=0.005, parent=root)
    box("Desk_Ledge_Brass", (w + 0.04, 0.006, 0.012), (0, fy - 0.183, h - 0.036), GOLD, bevel=0, parent=root)
    # booking tablet on a swivel kiosk stand, facing the guests
    st = empty("Tablet_Stand", (-0.3, fy - 0.04, h), parent=root)
    cyl("Tablet_Stand_Base", 0.055, 0.012, (0, 0, 0.006), GOLD, segs=24, parent=st)
    cyl("Tablet_Stand_Post", 0.011, 0.13, (0, 0, 0.075), GOLD, parent=st)
    head = empty("Tablet_Head", (0, 0, 0.15), rot=(R(-20), 0, 0), parent=st)
    tab = box("Tablet_Body", (0.3, 0.01, 0.225), (0, 0, 0.1), mat("dark", 0.35), bevel=0.006, parent=head)
    hook_link(tab, "website")                         # your online booking page or your site
    scr = hook_image("screen", 1, (0.28, 0.205), (0, -0.0055, 0.1), parent=head, glow=True, default_key="cream")
    ui = [box("Tablet_UI_Bar", (0.27, 0.002, 0.03), (0, -0.0068, 0.188), mat("accent_1", 0.5, emit=0.9), bevel=0,
              parent=head)]
    for i in range(4):                                # a little booking calendar
        for j in range(3):
            key = ("accent_2", "main", "accent_3")[(i + j) % 3] if (i * 3 + j) % 4 else "cream"
            ui.append(box("Tablet_UI_Slot", (0.055, 0.002, 0.038), (-0.1 + i * 0.065, -0.0068, 0.13 - j * 0.048),
                          mat(key, 0.5, emit=0.8), bevel=0, parent=head))
    hook_default(scr, *ui)
    box("CardReader_Dock", (0.075, 0.07, 0.018), (-0.05, fy - 0.07, h + 0.009), CERAMIC, bevel=0.006, parent=root)
    rd = box("CardReader", (0.07, 0.016, 0.085), (-0.05, fy - 0.06, h + 0.055), mat("dark", 0.4), bevel=0.008,
             rot=(R(-25), 0, 0), parent=root)
    box("CardReader_Screen", (0.05, 0.002, 0.04), (0, -0.009, 0.015), mat("cream", 0.3, emit=1.2), bevel=0, parent=rd)
    # brass business-card holder = your email
    holder = box("CardHolder", (0.1, 0.05, 0.012), (0.16, fy - 0.07, h + 0.006), GOLD, bevel=0.003, parent=root)
    hook_link(holder, "email")
    box("CardHolder_Back", (0.1, 0.006, 0.05), (0, 0.022, 0.025), GOLD, bevel=0.002, rot=(R(-10), 0, 0), parent=holder)
    for k in range(4):
        box("Business_Card", (0.09, 0.0015, 0.055), (0, 0.012 - k * 0.0025, 0.033), PAPER if k else
            mat("accent_2", 0.7), bevel=0, rot=(R(-12), 0, 0), parent=holder)
    # bud vase with pink tulips
    vx = 0.46
    no_shadow(lathe("Tulip_Vase", [(0, 0), (0.035, 0), (0.045, 0.06), (0.025, 0.13), (0.03, 0.15), (0.024, 0.15),
                                   (0, 0.01)], (vx, fy - 0.05, h), GLASS, parent=root))
    for k in range(5):
        a = R(-40 + 20 * k)
        tip = (vx + 0.09 * math.sin(a), fy - 0.05 + 0.03 * math.cos(a * 2), h + 0.3 + 0.04 * math.cos(a))
        tube("Tulip_Stem", spline([(vx, fy - 0.05, h + 0.03), (vx + 0.02 * math.sin(a), fy - 0.05, h + 0.16), tip], 4),
             0.003, LEAF, parent=root, segs=5)
        ball("Tulip_Head", 0.024, tip, mat("main", 0.5) if k % 2 else mat("accent_1", 0.55), scale=(1, 1, 1.35),
             parent=root, segs=14)
    # trailing pothos on the work top, spilling over the end of the desk
    px_, py_ = w / 2 - 0.12, d / 2 - 0.15
    lathe("Desk_Pot", [(0, 0), (0.06, 0), (0.075, 0.11), (0.08, 0.12), (0.07, 0.12), (0.06, 0.02), (0, 0.02)],
          (px_, py_, 0.785), CERAMIC, parent=root)
    cyl("Desk_Pot_Soil", 0.068, 0.01, (px_, py_, 0.785 + 0.105), SOIL, bevel=0, parent=root)
    vines = []
    for k, (dx, dy, drop) in enumerate(((0.09, -0.05, 0.45), (0.11, 0.06, 0.32), (0.03, 0.1, 0.2), (-0.06, 0.08, 0.15))):
        pts = spline([(px_, py_, 0.9), (px_ + dx * 0.8, py_ + dy, 0.92), (px_ + dx * 1.3, py_ + dy * 1.2, 0.85),
                      (px_ + dx * 1.4, py_ + dy * 1.3, 0.85 - drop)], 4)
        tube("Pothos_Vine", pts, 0.0028, LEAF, parent=root, segs=5)
        vines += [(tuple(p), 0.035) for p in pts[::2]]
    vines.append(((px_, py_, 0.95), 0.07))
    foliage("Pothos_Leaves", vines, 10, (0.05, 0.04), mat("plant", 0.5, color="#5E8C43"), parent=root, seed=SEED + 4,
            droop=0.5)


def build_mirror():
    """Arched 'Hollywood' make-up mirror: white lacquer arch frame, brass inner bead, real mirror glass
    and 13 frosted globe bulbs on brass sockets."""
    root, w, d, h = furniture_root("mirror")
    arch_prism("Mirror_Frame", w, h, 0.035, (0, d / 2 - 0.0175, 0), LACQUER, parent=root, bevel=0.006)
    arch_prism("Mirror_Glass", w - 0.13, h - 0.13, 0.006, (0, d / 2 - 0.038, 0.065), MIRROR, parent=root, bevel=0.001)
    tube("Mirror_Bead", [(u, d / 2 - 0.038, 0.06 + z) for u, z in arch_path(w - 0.12, h - 0.115)], 0.006, GOLD,
         parent=root)
    path = arch_path(w - 0.065, h - 0.065)
    length = sum((Vector(b) - Vector(a)).length for a, b in zip(path, path[1:]))
    for k, (u, z) in enumerate(along(path, length / 13)):
        cyl(f"Mirror_Socket_{k}", 0.012, 0.016, (u, d / 2 - 0.043, 0.0325 + z), GOLD, rot=(R(90), 0, 0), segs=12,
            parent=root)
        ball(f"Mirror_Bulb_{k}", 0.021, (u, d / 2 - 0.068, 0.0325 + z), BULB, parent=root, segs=14)


def build_floor_lamp():
    """18-inch LED ring light on a black light stand: tripod legs, two telescopic sections, ball head,
    a frosted diffuser ring and a phone holder in the middle."""
    root, w, d, h = furniture_root("floor_lamp")
    hub = 0.42
    for k in range(3):
        a = R(90 + 120 * k)
        tube("Ring_Leg", [(0, 0, hub), (0.2 * math.cos(a), 0.2 * math.sin(a), 0.012)], 0.009, BLACK, parent=root)
        ball("Ring_Foot", 0.014, (0.2 * math.cos(a), 0.2 * math.sin(a), 0.012), BLACK, parent=root, segs=10)
    cyl("Ring_Hub", 0.022, 0.05, (0, 0, hub), BLACK, parent=root)
    cyl("Ring_Pole_Lower", 0.014, 0.82, (0, 0, hub + 0.41), BLACK, parent=root)
    cyl("Ring_Pole_Clamp", 0.02, 0.03, (0, 0, hub + 0.82), BLACK, parent=root)
    cyl("Ring_Pole_Upper", 0.01, 0.24, (0, 0, hub + 0.94), CHROME, parent=root)
    rc = 1.5                                          # ring centre height
    ball("Ring_BallHead", 0.022, (0, 0, rc - 0.235), BLACK, parent=root, segs=12)
    ring = [(0.205 * math.cos(t), 0.0, rc + 0.205 * math.sin(t)) for t in (2 * math.pi * k / 48 for k in range(48))]
    tube("Ring_Housing", ring, 0.024, BLACK, parent=root, closed=True, segs=12)
    tube("Ring_Diffuser", [(x, -0.012, z) for x, _, z in ring], 0.018, RING_GLOW, parent=root, closed=True, segs=10)
    box("Ring_Phone_Arm", (0.012, 0.012, 0.2), (0, -0.01, rc - 0.115), BLACK, bevel=0.003, parent=root)
    box("Ring_Phone", (0.075, 0.009, 0.15), (0, -0.016, rc), mat("dark", 0.3), bevel=0.008, parent=root)
    box("Ring_Phone_Clip", (0.09, 0.014, 0.02), (0, -0.016, rc - 0.07), BLACK, bevel=0.004, parent=root)
    if RING_LIGHT:
        ld = furniture_light(root, "Light_Ring", "AREA", 26 if not JELLY else 28, kelvin(6500), (0, -0.06, rc),
                             (0, -1.0, rc - 0.12), size=0.42)      # aimed at face height, not the floor
        ld.data.shape = "DISK"
        if hasattr(ld.data, "specular_factor"):       # no sparkly hot spot mirrored in the glossy terrazzo
            ld.data.specular_factor = 0.3


def build_sofa():
    """Waiting loveseat: channel-tufted velvet back, one long seat cushion, rolled arms, brass feet."""
    root, w, d, h = furniture_root("sofa")
    for sx in (-1, 1):
        for sy in (-1, 1):
            brass_leg("Sofa_Leg", root, sx * (w / 2 - 0.08), sy * (d / 2 - 0.08), 0.12, r_top=0.016, r_foot=0.011)
    soft("Sofa_Base", (w, d - 0.02, 0.2), (0, 0, 0.22), VELVET_2, parent=root, r=0.03)
    soft("Sofa_Seat", (w - 0.26, d - 0.2, 0.13), (0, -0.06, 0.385), VELVET_2, parent=root, r=0.05)
    box("Sofa_Piping", (w - 0.04, 0.005, 0.012), (0, -d / 2 + 0.008, 0.13), GOLD, bevel=0, parent=root)
    for sx in (-1, 1):
        soft("Sofa_Arm", (0.13, d - 0.02, 0.5), (sx * (w / 2 - 0.065), 0, 0.37), VELVET_2, parent=root, r=0.04)
        cyl("Sofa_Arm_Roll", 0.07, d - 0.02, (sx * (w / 2 - 0.068), 0, 0.6), VELVET_2, rot=(R(90), 0, 0), segs=24,
            bevel=0.03, parent=root)
    n, xm = 9, w / 2 - 0.15
    for i in range(n):
        x = -xm + 2 * xm * i / (n - 1)
        top = h - 0.02 - 0.05 * (x / xm) ** 2
        soft("Sofa_Channel", (2 * xm / (n - 1) + 0.01, 0.16, top - 0.32), (x, d / 2 - 0.11, (top + 0.32) / 2), VELVET_2,
             parent=root, r=0.055)
    soft("Sofa_Pillow", (0.34, 0.13, 0.32), (-0.36, 0.1, 0.6), M("cream", 0.95, "knit", scale=1.5),
         rot=(R(-14), 0, R(10)), parent=root, r=0.06)
    soft("Sofa_Pillow_2", (0.3, 0.12, 0.28), (0.4, 0.12, 0.58), VELVET, rot=(R(-12), 0, R(-8)), parent=root, r=0.06)


def build_plant():
    """Dried pampas grass in a ribbed ceramic floor vase: tall stems with soft feathery plumes."""
    root, w, d, h = furniture_root("plant")
    lathe("Vase_Body", [(0, 0), (0.1, 0), (0.135, 0.06), (0.15, 0.17), (0.12, 0.3), (0.06, 0.38), (0.065, 0.42),
                        (0.055, 0.42), (0.05, 0.38), (0, 0.38)], (0, 0, 0), CERAMIC, segs=40, parent=root)
    for k in range(18):                               # vertical ribs round the belly
        a = 2 * math.pi * k / 18
        tube("Vase_Rib", [(0.104 * math.cos(a), 0.104 * math.sin(a), 0.01), (0.14 * math.cos(a), 0.14 * math.sin(a), 0.08),
                          (0.149 * math.cos(a), 0.149 * math.sin(a), 0.17), (0.12 * math.cos(a), 0.12 * math.sin(a), 0.29),
                          (0.065 * math.cos(a), 0.065 * math.sin(a), 0.37)], 0.006, CERAMIC, parent=root, segs=6)
    rnd = random.Random(SEED + 41)
    stem_mat = mat("pampas", 0.8, color="#BFA785")
    bm = bmesh.new()                                  # every plume's barbs in ONE mesh
    for k in range(9):
        a = 2 * math.pi * k / 9 + rnd.uniform(-0.25, 0.25)
        wallward = 1.0 - 0.7 * max(0.0, math.sin(a))  # plumes towards the back wall stay upright (no clipping)
        lean = rnd.uniform(0.12, 0.26) * wallward
        top = rnd.uniform(0.84, 1.02)
        out_dir = Vector((math.cos(a), math.sin(a), 0.0)) * wallward
        tip = Vector((lean * math.cos(a), lean * math.sin(a), top))
        stem = spline([(0, 0, 0.38), (tip.x * 0.25, tip.y * 0.25, 0.7), tuple(tip)], 5)
        tube("Pampas_Stem", stem, 0.0035, stem_mat, parent=root, segs=5)
        # the plume carries on from the stem tip and nods outwards a little
        axis = ((Vector(stem[-1]) - Vector(stem[-3])).normalized() + out_dir * 0.35).normalized()
        L = rnd.uniform(0.3, 0.38)
        side = axis.cross(Vector((0, 0, 1)))
        side = side.normalized() if side.length > 1e-4 else Vector((1, 0, 0))
        up2 = side.cross(axis).normalized()
        tube("Pampas_Rachis", [tuple(tip), tuple(tip + axis * L * 0.95)], 0.006, PAMPAS, parent=root, segs=6, r2=0.002)
        for _ in range(420):                          # soft feathery barbs: lean up the plume, fuller near the base
            t = rnd.random() ** 0.85
            rad = 0.062 * math.sin(math.pi * (0.08 + 0.88 * t)) ** 0.7 * (1.0 - 0.45 * t) * rnd.uniform(0.35, 1.0)
            ang = rnd.uniform(0, 2 * math.pi)
            radial = side * math.cos(ang) + up2 * math.sin(ang)
            base = tip + axis * (t * L) + radial * rad * 0.35
            d = (axis * 1.0 + radial * rnd.uniform(0.35, 0.8) + Vector((0, 0, -0.25))).normalized()
            ln = rnd.uniform(0.045, 0.075) * (1.0 - 0.4 * t)
            wv = d.cross(radial).normalized() * rnd.uniform(0.005, 0.009)
            vs = [bm.verts.new(v) for v in (base - wv * 0.4, base + d * ln * 0.35 - wv, base + d * ln,
                                             base + d * ln * 0.35 + wv, base + wv * 0.4)]
            bm.faces.new(vs)
    o = _obj("Pampas_Plumes", bm)
    o.data.materials.append(PAMPAS)
    COL_ROOM.objects.link(o)
    o.parent = root


PLACEHOLDERS = {
    "wall_shelf": build_wall_shelf, "desk": build_desk, "chair": build_chair, "stool": build_stool,
    "salon_chair": build_salon_chair, "counter": build_counter, "mirror": build_mirror,
    "floor_lamp": build_floor_lamp, "sofa": build_sofa, "plant": build_plant,
}

if SHOW_PLACEHOLDER_FURNITURE:
    for slot_name, build in PLACEHOLDERS.items():
        build()

# =====================================================================
#  DECORATION: vanity under the mirror, pouf, waiting-area rug and coffee table, towel trolley
# =====================================================================
van = empty("Vanity", (0.19, 3.08, FLOOR_Z), rot=(0, 0, R(90)))   # front faces +x (into the room)
VW, VD, VH = 0.85, 0.38, 0.76
box("Vanity_Top", (VW, VD, 0.025), (0, 0, VH - 0.0125), LACQUER, bevel=0.005, parent=van)
box("Vanity_Top_Brass", (VW, 0.004, 0.01), (0, -VD / 2 - 0.001, VH - 0.0125), GOLD, bevel=0, parent=van)
box("Vanity_Apron", (VW - 0.04, VD - 0.04, 0.13), (0, 0.01, VH - 0.025 - 0.065), LACQUER, bevel=0.004, parent=van)
box("Vanity_Drawer", (VW - 0.14, 0.018, 0.1), (0, -VD / 2 + 0.02, VH - 0.09), LACQ_MAIN, bevel=0.003, parent=van)
for sx in (-1, 1):
    ball("Vanity_Knob", 0.012, (sx * 0.14, -VD / 2 + 0.006, VH - 0.09), GOLD, parent=van, segs=12)
    for sy in (-1, 1):
        brass_leg("Vanity_Leg", van, sx * (VW / 2 - 0.05), sy * (VD / 2 - 0.05), VH - 0.15)
top_z = VH
no_shadow(cyl("Brush_Cup", 0.035, 0.1, (-0.28, 0.02, top_z + 0.05), GLASS, bevel=0.005, parent=van))
for k in range(5):                                   # make-up brushes: handle, ferrule, soft head
    a = R(-30 + 15 * k)
    bx_, bz_ = -0.28 + 0.06 * math.sin(a), top_z + 0.1
    tube("Brush_Handle", [(-0.28, 0.02, top_z + 0.01), (bx_, 0.02 + 0.01 * k - 0.02, bz_ + 0.06)], 0.004,
         mat("dark", 0.4) if k % 2 else mat("cream", 0.4), parent=van, segs=6)
    ball("Brush_Head", 0.012, (bx_ * 1.02 + 0.006 * math.sin(a), 0.02 + 0.01 * k - 0.02, bz_ + 0.078),
         mat("pampas", 0.95), scale=(1, 1, 1.6), parent=van, segs=10)
box("Palette_Case", (0.16, 0.1, 0.012), (-0.08, 0.0, top_z + 0.006), mat("dark", 0.4), bevel=0.004, parent=van)
for i in range(4):
    for j in range(2):
        cyl("Palette_Pan", 0.014, 0.004, (-0.13 + i * 0.033, -0.02 + j * 0.04, top_z + 0.013),
            mat("pal", 0.6, color=hsv_hex(0.02 + 0.03 * (i + j * 4), 0.35 + 0.05 * i, 0.9 - 0.08 * j)), bevel=0,
            segs=14, parent=van)
care = empty("Skincare_Trio", (0.16, 0.04, top_z), parent=van)  # little shop shelf of your own products
hook_link(care, "github")                            # no GitHub? it borrows your social or shop link
for k, (key, r_, h_) in enumerate((("accent_2", 0.034, 0.07), ("cream", 0.028, 0.11), ("accent_3", 0.03, 0.055))):
    x_ = -0.06 + k * 0.07
    cyl("Skincare_Jar", r_, h_, (x_, 0, h_ / 2), mat(key, 0.15), bevel=0.008, parent=care)
    cyl("Skincare_Lid", r_ * 1.03, 0.018, (x_, 0, h_ + 0.009), GOLD, parent=care)
    box("Skincare_Label", (r_ * 1.2, 0.002, h_ * 0.4), (x_, -r_ - 0.0005, h_ * 0.45), PAPER, bevel=0, parent=care)
lathe("Perfume", [(0, 0), (0.03, 0), (0.035, 0.05), (0.028, 0.08), (0.01, 0.085), (0, 0.085)], (0.34, 0.06, top_z),
      mat("glass", 0.05, alpha=0.5), segs=8, parent=van)
ball("Perfume_Cap", 0.016, (0.34, 0.06, top_z + 0.1), GOLD, parent=van, segs=12)

# velvet pouf in front of the vanity, with a covered button
pouf_x, pouf_y = 0.64, 3.02
cyl("Pouf", 0.2, 0.38, (pouf_x, pouf_y, FLOOR_Z + 0.04 + 0.19), VELVET_2, segs=40, bevel=0.06)
cyl("Pouf_Base", 0.17, 0.04, (pouf_x, pouf_y, FLOOR_Z + 0.02), GOLD, segs=40, bevel=0.004)
ball("Pouf_Button", 0.018, (pouf_x, pouf_y, FLOOR_Z + 0.42), VELVET_2, scale=(1, 1, 0.5), segs=12)

# waiting area: a round wool rug, a tulip-style marble coffee table with plain magazines and a candle
RUG_X, RUG_Y = 3.55, 1.15
cyl("Rug_Border", 0.93, 0.012, (RUG_X, RUG_Y, FLOOR_Z + 0.006), M("accent_2", 0.95, "knit", scale=1.2), segs=72,
    bevel=0.004)
cyl("Rug_Field", 0.84, 0.014, (RUG_X, RUG_Y, FLOOR_Z + 0.007), M("cream", 0.95, "knit", scale=1.2), segs=72,
    bevel=0.004)
tb = empty("Coffee_Table", (3.18, RUG_Y, FLOOR_Z + 0.014))
lathe("Coffee_Table_Pedestal", [(0, 0), (0.22, 0), (0.22, 0.02), (0.12, 0.08), (0.06, 0.2), (0.05, 0.32), (0.09, 0.4),
                                (0, 0.4)], (0, 0, 0), JELLY_AQUA if JELLY else LACQUER, segs=40, parent=tb)
cyl("Coffee_Table_Top", 0.3, 0.022, (0, 0, 0.411), MARBLE, segs=48, bevel=0.005, parent=tb)
for k, (key, rot_) in enumerate((("main", 8), ("accent_3", -14))):
    mg = box("Magazine", (0.21, 0.28, 0.007), (-0.06 + 0.02 * k, -0.04 + 0.02 * k, 0.4255 + 0.007 * k),
             mat(key, 0.5), bevel=0.001, rot=(0, 0, R(rot_)), parent=tb)
    box("Magazine_Band", (0.17, 0.05, 0.001), (0, 0.08, 0.004), PAPER, bevel=0, parent=mg)   # plain cover, no title
no_shadow(cyl("Candle_Glass", 0.04, 0.08, (0.14, 0.08, 0.462), GLASS, bevel=0.005, parent=tb))
cyl("Candle_Wax", 0.036, 0.05, (0.14, 0.08, 0.448), mat("cream", 0.6), bevel=0.004, parent=tb)
ball("Candle_Flame", 0.007, (0.14, 0.08, 0.485), mat("bulb", 0.3, emit=6.0), scale=(1, 1, 1.8), parent=tb, segs=8)

# two-tier brass towel trolley at the technician's right hand, between the manicure table and the pampas
# (kept clear of the pedicure basin so the throne's foot spa stays visible)
tr = empty("Trolley", (2.5, 2.72, FLOOR_Z), rot=(0, 0, R(90)))
for zz in (0.12, 0.72):
    box("Trolley_Tray", (0.38, 0.28, 0.012), (0, 0, zz), MARBLE if zz > 0.5 else LACQUER, bevel=0.003, parent=tr)
    box("Trolley_Rail", (0.38, 0.006, 0.03), (0, -0.14, zz + 0.02), GOLD, bevel=0, parent=tr)
for sx in (-1, 1):
    for sy in (-1, 1):
        cyl("Trolley_Post", 0.007, 0.74, (sx * 0.175, sy * 0.125, 0.4), GOLD_V, parent=tr)
        cyl("Trolley_Wheel", 0.022, 0.014, (sx * 0.175, sy * 0.125, 0.022), BLACK, rot=(0, R(90), 0), parent=tr)
for k in range(3):
    box("Trolley_Towel", (0.3, 0.2, 0.035), (0, 0, 0.145 + k * 0.037), TOWEL, bevel=0.012, parent=tr)
for k in range(4):
    polish_bottle(f"Trolley_Polish_{k}", (-0.12 + k * 0.08, 0.04, 0.726), tr,
                  polish_colour(random.randint(3, 22), random.randint(2, 6), 24, 7))
cyl("Trolley_Cup", 0.035, 0.08, (0.1, -0.06, 0.766), CERAMIC, bevel=0.006, parent=tr)

# =====================================================================
#  PORTFOLIO: neon name sign on the hedge, gold frames, service poster
# =====================================================================
NEON_Y = D - 0.135
no_shadow(box("Neon_Backer", (1.2, 0.008, 0.56), (HEDGE_X, D - 0.125, 1.92), NEON_BACKER, bevel=0.004))
hook_link(bpy.data.objects["Neon_Backer"], "linkedin")
for sx in (-1, 1):
    for sz in (-1, 1):
        cyl("Neon_Standoff", 0.012, 0.1, (HEDGE_X + sx * 0.54, D - 0.075, 1.92 + sz * 0.23), GOLD, rot=(R(90), 0, 0),
            segs=14)


def neon(hook, tube_r):
    """Make a text hook read as LED neon flex: italic (script-like) and with round tube edges, then fit it again."""
    cu = hook.data
    cu.shear, cu.extrude, cu.bevel_depth, cu.bevel_resolution = 0.2, 0.002, tube_r, 3
    hook.scale = (1, 1, 1)
    bpy.context.view_layer.update()
    if hook.dimensions.x > hook["kit_max_width"]:
        hook.scale = [hook["kit_max_width"] / hook.dimensions.x] * 3
    return hook


neon(hook_text("name", 1, "Your Name", 0.23, (HEDGE_X, NEON_Y, 2.02), material=NEON, max_width=1.08, depth=0.004),
     0.007)
neon(hook_text("role", 1, "your role", 0.115, (HEDGE_X, NEON_Y, 1.74), material=NEON_WHITE, max_width=0.95,
               depth=0.003), 0.004)


def framed(name, center, size, wall="back", mount=0.04, depth=0.024):
    """Brass picture frame (20 mm moulding) with a white mount. Returns the picture's location + rotation."""
    x, y, z = center
    w, h = size
    fw = 0.02
    ow, oh = w + 2 * mount + 2 * fw, h + 2 * mount + 2 * fw
    if wall == "back":
        box(f"{name}_Backing", (ow - 0.01, 0.01, oh - 0.01), (x, D - 0.005, z), PAPER, bevel=0)
        for sz in (-1, 1):
            box(f"{name}_Frame_H", (ow, depth, fw), (x, D - depth / 2, z + sz * (oh - fw) / 2), GOLD, bevel=0.003)
        for sx in (-1, 1):
            box(f"{name}_Frame_V", (fw, depth, oh - 2 * fw), (x + sx * (ow - fw) / 2, D - depth / 2, z), GOLD_V,
                bevel=0.003)
        return (x, D - 0.0115, z), (0, 0, 0)
    box(f"{name}_Backing", (0.01, ow - 0.01, oh - 0.01), (0.005, y, z), PAPER, bevel=0)
    for sz in (-1, 1):
        box(f"{name}_Frame_H", (depth, ow, fw), (depth / 2, y, z + sz * (oh - fw) / 2), GOLD, bevel=0.003)
    for sy in (-1, 1):
        box(f"{name}_Frame_V", (depth, fw, oh - 2 * fw), (depth / 2, y + sy * (ow - fw) / 2, z), GOLD_V, bevel=0.003)
    return (0.0115, y, z), (0, 0, R(90))


# Frames 1 + 2: left wall above the reception desk ("before / after" nail-art photos).
FR_Z = 1.86
loc, rot = framed("Frame1", (0, 0.58, FR_Z), (0.36, 0.46), wall="left")
f1 = hook_image("frame", 1, (0.36, 0.46), loc, rot=rot, default_key="accent_2")
nails = []
for k in range(5):                                   # a fan of five almond nails in polish colours
    a = R(-36 + 18 * k)
    nails.append(ball("Frame1_Nail", 0.05, (0.014, 0.58 + 0.12 * math.sin(a), FR_Z - 0.1 + 0.13 * math.cos(a)),
                      polish(polish_colour(4 + 4 * k, 2, 24, 7)), scale=(0.06, 0.5, 1.0), rot=(-a, 0, 0)))
    nails.append(ball("Frame1_Nail_Shine", 0.012, (0.017, 0.58 + 0.12 * math.sin(a) - 0.008,
                                                   FR_Z - 0.1 + 0.13 * math.cos(a) + 0.02), mat("cream", 0.2, emit=0.4),
                      scale=(0.1, 0.4, 1.2), rot=(-a, 0, 0)))
hook_default(f1, *nails)

loc, rot = framed("Frame2", (0, 1.22, FR_Z), (0.36, 0.46), wall="left")
f2 = hook_image("frame", 2, (0.36, 0.46), loc, rot=rot, default_key="cream")
hook_default(f2,
             arch_prism("Frame2_Arch", 0.22, 0.3, 0.003, (0.014, 1.22, FR_Z - 0.21), mat("main", 0.8),
                        rot=(0, 0, R(90)), bevel=0),
             arch_prism("Frame2_Arch_Inner", 0.12, 0.2, 0.003, (0.016, 1.22, FR_Z - 0.21), mat("accent_2", 0.8),
                        rot=(0, 0, R(90)), bevel=0),
             ball("Frame2_Sun", 0.045, (0.015, 1.22 + 0.09, FR_Z + 0.14), GOLD, scale=(0.06, 1, 1)))

# Poster: back wall between the two arches, a service menu by default.
loc, rot = framed("Poster1", (2.8, 0, 1.88), (0.42, 0.56))
p1 = hook_image("poster", 1, (0.42, 0.56), loc, rot=rot, default_key="accent_2")
px_, py_, pz_ = loc
deco = [label("Poster1_Title", "services", 0.05, (px_, py_ - 0.003, pz_ + 0.2), mat("dark", 0.6), depth=0.001)]
for k in range(5):
    deco.append(box("Poster1_Line", (0.22, 0.002, 0.012), (px_ - 0.05, py_ - 0.003, pz_ + 0.09 - k * 0.07),
                    mat("dark", 0.6), bevel=0))
    deco.append(box("Poster1_Price", (0.05, 0.002, 0.012), (px_ + 0.14, py_ - 0.003, pz_ + 0.09 - k * 0.07),
                    mat("accent_1", 0.6), bevel=0))
deco.append(arch_prism("Poster1_Arch", 0.12, 0.12, 0.002, (px_, py_ - 0.003, pz_ - 0.27), mat("main", 0.7), bevel=0))
hook_default(p1, *deco)

# =====================================================================
#  LIGHTS, WORLD, CAMERA, RENDER
# =====================================================================
# Day ("milk_blush"): bright sun through the arched window, a big soft fill from the open side, a soft
# bounce from above. Evening ("jelly_neon"): a dusky lilac sky, dimmer fill, and the neon, bulbs and
# ring light carry the room.
sun_dir = Vector((1.0, 0.3, -0.62)).normalized()
target = Vector((1.7, WIN_CY + 0.4, 0.0))
if not JELLY:
    light("Light_Sun", "SUN", SUN_STRENGTH, kelvin(SUN_WARMTH), target - sun_dir * 6, aim=target, size=R(3))
    light("Light_Fill", "AREA", 240 * (W * D / 16), kelvin(6200), (W + 3, -3, H + 2.5), aim=(W / 2, D / 2, 0.6), size=6)
    light("Light_Window", "AREA", 28, kelvin(6000), (0.7, WIN_CY, 1.9), aim=(2.2, WIN_CY, 0.8), size=0.8)
    light("Light_Bounce", "AREA", 60, kelvin(4800), (W / 2, D / 2, H - 0.1), aim=(W / 2, D / 2, 0), size=3.0)
else:
    light("Light_Sun", "SUN", SUN_STRENGTH * 0.18, (0.62, 0.52, 1.0), target - sun_dir * 6, aim=target, size=R(6))
    light("Light_Fill", "AREA", 120 * (W * D / 16), (0.7, 0.62, 1.0), (W + 3, -3, H + 2.5), aim=(W / 2, D / 2, 0.6),
          size=6)
    light("Light_Window", "AREA", 30, lin(COLORS["sky"])[:3], (0.7, WIN_CY, 1.9), aim=(2.2, WIN_CY, 0.8), size=0.8)
    light("Light_Bounce", "AREA", 55, kelvin(3000), (W / 2, D / 2, H - 0.1), aim=(W / 2, D / 2, 0), size=3.0)
neon_rgb = lin(COLORS["accent_1"])[:3]
light("Light_Neon", "AREA", 30 * (1.7 if JELLY else 1.0), neon_rgb, (HEDGE_X, D - 0.45, 2.0), aim=(HEDGE_X, 2.2, 0.9),
      size=0.9)
light("Light_Neon_Wash", "POINT", 12 * (1.1 if JELLY else 1.0), neon_rgb, (HEDGE_X, D - 0.2, 2.25), size=0.3)
mirror_glow = light("Light_Mirror", "POINT", LAMP_STRENGTH * 0.45 * (1.4 if JELLY else 1.0), kelvin(LAMP_WARMTH),
                    (0.52, 3.08, 1.38), size=0.45)
if hasattr(mirror_glow.data, "specular_factor"):    # no big bright highlight disc in the mirror glass
    mirror_glow.data.specular_factor = 0.0

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
bg_amb.inputs["Color"].default_value = (*kelvin(6200), 1) if not JELLY else (0.62, 0.55, 0.95, 1)
bg_amb.inputs["Strength"].default_value = 0.38 if not JELLY else 0.22
path = wn.new("ShaderNodeLightPath")
mix = wn.new("ShaderNodeMixShader")
wl.new(path.outputs["Is Camera Ray"], mix.inputs["Fac"])
wl.new(bg_amb.outputs[0], mix.inputs[1])
wl.new(bg_cam.outputs[0], mix.inputs[2])
wl.new(mix.outputs[0], out.inputs["Surface"])

# Orthographic camera that frames the whole room automatically.
BOUNDS = [-T, 0.0, -0.2, W, D + T, H + 0.12]
cam_data = bpy.data.cameras.new("Camera")
cam_data.type = "ORTHO"
cam = bpy.data.objects.new("Camera", cam_data)
scene.collection.objects.link(cam)
scene.camera = cam
cam.rotation_euler = Euler((R(90 - CAMERA_HEIGHT_ANGLE), 0, R(CAMERA_TURN)))
rot = cam.rotation_euler.to_matrix()
right, up, back = rot.col[0], rot.col[1], rot.col[2]
corners = [Vector((x, y, z)) for x in (BOUNDS[0], BOUNDS[3]) for y in (BOUNDS[1], BOUNDS[4])
           for z in (BOUNDS[2], BOUNDS[5])]
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
                    ("shadow_ray_count", 2), ("use_gtao", True), ("use_soft_shadows", True),
                    ("use_ssr", True), ("use_ssr_refraction", True), ("use_bloom", True)):
    if hasattr(ee, attr):
        setattr(ee, attr, value)
if hasattr(ee, "ray_tracing_options"):
    ee.ray_tracing_options.resolution_scale = "2" if "2" in [i.identifier for i in
        type(ee.ray_tracing_options).bl_rna.properties["resolution_scale"].enum_items] else ee.ray_tracing_options.resolution_scale
scene.view_settings.view_transform = "Standard"   # keeps your hex colours exactly as typed
scene.view_settings.exposure = -0.22 if not JELLY else 0.0

# Remember the style so add_furniture.py can match colours later.
scene["kit_style"] = STYLE
scene["kit_version"] = KIT_VERSION
scene["kit_palette"] = json.dumps(COLORS)
scene["kit_material_finish"] = json.dumps({"roughness": 0.55, "bevel": 0.005, "saturation": 0.7})
scene["kit_theme"] = THEME
scene["kit_bounds"] = BOUNDS
scene["kit_room_size"] = [W, D, H]
scene["kit_furniture_colors"] = json.dumps(["main", "accent_2", "accent_3", "cream", "wood", "lacquer", "gold",
                                            "plant", "dark"])   # colours add_furniture.py may use (no neon)


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
