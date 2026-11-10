"""
3D ROOM PORTFOLIO KIT  -  Template: APOTHECARY & HERB SHOP ("potion shop")
=========================================================================
Builds a moonlit isometric apothecary from scratch and renders a 1920x1080 image: a wall-sized walnut
dispensing cabinet with 56 labelled drawers and a hook-on library ladder, a panelled mahogany shop counter
with a brass balance, a cast-iron cauldron hung from a tripod, a glazed crystal cabinet, dried herbs on a
pulley airer, dripping pillar candles, a wing chair beside a tarot table and a black shop cat - all modelled
on real pieces you could find in an antiques shop, an occult bookshop or IKEA.

HOW TO RUN
  Option A (no Blender UI):   blender -b -P potion_shop.py
  Option B (inside Blender):  Scripting tab > Open > potion_shop.py > Run Script (then F12 to render)

You only need to edit the SETTINGS block below. Everything under it builds the room.
Output: output/potion_shop.png and output/potion_shop.blend next to this script.

Where your portfolio goes:
  gilded fascia sign above the cabinet -> your name + role (and your website link)
  book on the oak lectern              -> project 1
  two framed botanical prints          -> projects 2 and 3 (project titles on the mounts)
  chalkboard "TODAY'S BREW"            -> project 4
  jar labels on the wall shelf         -> your skills
  crystal ball -> email link,  apothecary cabinet -> GitHub,  sealed scroll -> LinkedIn
"""
# REFERENCES  (what each piece is modelled on; real sizes in metres; details in research/potion_shop.md)
#   shelf        antique walnut apothecary / dispensing cabinet, 56 drawers: 1.90 W x 0.52 D x 2.45 H, hutch 0.32 D
#                https://www.proantic.com/en/1762933-early-20th-century-oak-apothecary-cabinet-with-42-drawers.html
#   hardware     cast brass label holder + bin (cup) pull, 0.092 x 0.054, 0.019 projection
#                https://www.houseofantiquehardware.com/brass-card-holders-bin-pull-3-5-8
#   ladder       hook-on oak library ladder, 0.41 W, 7 treads, 1in brass rail at 2.2
#                https://www.vandykes.com/quiet-glide-oak-library-ladder-8-ft-rolling-hardware-kit/p/236625/
#   counter      late-Victorian mahogany shop / haberdashery counter: 1.70 x 0.62 x 0.92, fielded panels
#                https://www.chairish.com/product/23155923/large-19th-century-english-mahogany-haberdashery-counter-1890
#   balance      Victorian brass & mahogany apothecary balance: base 0.46 x 0.20, 0.43 H, pans 0.14
#                https://www.chairish.com/product/35419336/antique-victorian-apothecary-balance-scales-in-brass-and-mahogany-with-weights-from-day-millward-18
#   hero_prop    19th-c cast-iron handled cauldron (0.38 belly, 0.30 H) on a 1.42 m camp tripod with chain
#                https://www.chairish.com/product/29049653/19th-century-cast-iron-handled-cauldron-with-stand
#   display_case Victorian oak chemist's glazed display cabinet: 0.95 x 0.45 x 1.65, glass shelves
#                https://www.vinterior.co/furniture/storage/cabinets/antique-wooden-glazed-large-apothecary-chemists-shop-dispensing-cabinet-c-1910-sku88290784
#   hanging_plant Sheila Maid 4-rail pulley airer used as a herb drying rack: 1.45 laths, 0.395 cast-iron ends
#                https://www.willowandstone.co.uk/products/sheila-maid-traditional-clothes-dryer
#   wall_shelf   deep oak plank shelf on cast-iron brackets: 0.70 x 0.26, 30 mm board
#   armchair     IKEA STRANDMON wing chair: 0.82 W x 0.96 D x 1.01 H, seat 0.45 H / 0.49 W / 0.54 D
#                https://www.ikea.com/us/en/p/strandmon-wing-chair-grann-bomstad-dark-brown-20494637
#   tarot table  1920s round walnut pedestal table 0.60 dia x 0.66 H + 0.90 velvet cloth with fringe
#                https://www.selency.nl/p/A7TJE2FF/1920-walnut-round-art-deco-side-table
#   candles      church / olive-wax pillar candles 0.07 x 0.15 (also 0.06 x 0.10, 0.07 x 0.22) with drips
#                https://eu.matildagoad.com/collections/new-in/products/olive-wax-pillar-candle-ivory
#   bottles      250 ml amber apothecary bottle 0.14 H x 0.07 dia with cork; stoppered glass shop jars 0.2-0.3 H
#                https://www.orsina.co.uk/products/apothecary-small-amber-glass-bottle
#   crystal tray 12-compartment wooden specimen tray 0.33 x 0.23 x 0.04  https://www.desertcart.ma/products/508255282
#   wall lights  brass swan-neck bracket + prismatic glass shade (Holophane-style) 0.16 dia
#                https://www.1stdibs.com/furniture/lighting/chandeliers-pendant-lights/antique-holophane-prismatic-glass-brass-church-pendant-light/id-f_41340382/
#   rug          vintage Turkish kilim flatweave 2.6 x 1.7 with warp fringes  https://www.kilim.com/detail/k0085950-vintage-turkish-kilim-rug
#   lectern      oak pedestal lectern / bible stand: desk 0.56 x 0.42 at 30 deg, 1.12 H
#   walls/floor  painted tongue-and-groove dado 1.0 H + limewash plaster; Victorian 6 in (150 mm) quarry tiles laid
#                diagonally with a straight border row + fillet  https://www.luxurytiles.co.uk/classic-victorian-quarry-black-matt-tile.html
#   till         ornate brass 1900s shop cash register (National-type), modelled 0.30 W x 0.32 D x 0.36 H, sloped keys
#                https://www.chairish.com/product/32488315/national-cash-register-1900s
#   yard measure brass yard rule let into a haberdashery counter top, 0.91 m (ticks every 4 in)
#   basket       seagrass belly basket 0.36 dia x 0.29 H with coiled rows + dried pampas (floor-size IKEA FLADIS; FLADIS itself is 0.25 dia x 0.32)
#                https://www.ikea.com/ie/en/p/fladis-basket-seagrass-60322173/
#   fairy bottle cork LED bottle light: coloured glass bottle + copper wire string of 10 warm LEDs
#   venues       Herb Garret (Old Operating Theatre Museum, London), Treadwell's / Atlantis occult bookshops

# =====================================================================
#  SETTINGS  -  change these lines, then run the script again
# =====================================================================
ROOM_NAME = "potion_shop"           # used for the output file names

ROOM_WIDTH = 4.6                    # metres, left to right
ROOM_DEPTH = 4.2                    # metres, front to back
WALL_HEIGHT = 3.0                   # metres (tall, for the big cabinet and the hanging herbs)

THEME = "moonlit"                   # pick one of the colour themes below
THEMES = {                          # any hex colour works; "main" is the room's hero colour (the velvet wing chair)
    # Lights change with the theme too (see LIGHTS below): "moonlit" = cold blue moon through the window;
    # "harvest" = a big orange harvest moon and warmer candle light (autumn / Halloween).
    # accent_1/2/3 = the brew glow and the coloured glass bottles. "floor" + "tile_dark" = the two quarry tiles
    # (moonlit = black and buff, harvest = red and black, the two classic Victorian quarry-tile pairings).
    "moonlit": {
        "background": "#17121F", "wall": "#4A3E5C", "wall_trim": "#2E4A4C", "floor": "#7C7064",
        "wood": "#5A3A26", "main": "#5E3F6E", "accent_1": "#8CE6A0", "accent_2": "#F08CC0",
        "accent_3": "#7FD8F0", "cream": "#E9DCC0", "plant": "#7D8C55", "dark": "#1C1824",
        "pet": "#25212B", "metal": "#34333A", "brass": "#C29A48", "candle": "#FFC870", "sky": "#24407A",
        "moon": "#E4EEFF", "wax": "#8E2333", "amber": "#8A4510", "tile_dark": "#3A3337", "mahogany": "#5C2A1E",
    },
    "harvest": {
        "background": "#1E120D", "wall": "#5A3B30", "wall_trim": "#3F3A26", "floor": "#A2603F",
        "wood": "#4E301C", "main": "#B5561F", "accent_1": "#FFA03A", "accent_2": "#B9F05A",
        "accent_3": "#C68CFF", "cream": "#F0DDB4", "plant": "#9A8A3E", "dark": "#1E130E",
        "pet": "#231A17", "metal": "#2F2A28", "brass": "#D0A048", "candle": "#FFB85C", "sky": "#4A2A3A",
        "moon": "#FFC27A", "wax": "#7A1E1E", "amber": "#9A5214", "tile_dark": "#3A2219", "mahogany": "#5A2616",
    },
}

SUN_WARMTH = 11000                  # Kelvin of the moonlight from the window (high = cold blue; harvest uses its own)
SUN_STRENGTH = 2.2                  # how bright the moonlight is
LAMP_WARMTH = 2200                  # Kelvin of the candles and wall lights (low = orange flame)
LAMP_STRENGTH = 5                   # Watts of each candle light
POTION_GLOW = 0.8                   # glow of the cork-LED lights inside the coloured bottles (0 = off)
CAULDRON_GLOW = 15                  # Watts of the soft light above the brew in the cauldron
CANDLES = True                      # pillar candles on the counter, sill, table, cabinet and floor
SEED = 5                            # change to shuffle jars, herbs and small props

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

STYLE = "potion_shop"
KIT_VERSION = 2
W, D, H = ROOM_WIDTH, ROOM_DEPTH, WALL_HEIGHT
T = 0.15            # wall thickness
FLOOR_Z = 0.02      # top of the floor tiles; furniture stands here
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


# Real materials used all over the room (each is a palette colour + a surface() kind).
def wood(f=1.0, rough=0.45, along="X", key="wood", kind="wood"):
    """Walnut / mahogany / oak. along = grain direction in the part's own axes (Z for uprights)."""
    tag = {"X": 0.0, "Y": 0.001, "Z": 0.002}[along]          # separate cached material per grain direction
    return surface(mat(key, round(rough + tag, 3), color=shade(COLORS[key], f) if f != 1.0 else None), kind,
                   along=along)


def brass(rough=0.3):
    return surface(mat("brass", rough, metal=0.85), "brushed")


def iron(f=1.0):
    """Cast / wrought iron: dark, slightly rough metal."""
    return surface(mat("metal", 0.62, metal=0.55, color=shade(COLORS["metal"], f) if f != 1.0 else None),
                   "brushed", scale=0.3)


def cloth(key, f=1.0, kind="fabric"):
    return surface(mat(key, 0.9, color=shade(COLORS[key], f) if f != 1.0 else None), kind)


def paper(f=1.0):
    return surface(mat("cream", 0.85, color=shade(COLORS["cream"], f) if f != 1.0 else None), "paper")


def wax(f=1.0):
    return surface(mat("cream", 0.5, color=shade(COLORS["cream"], f) if f != 1.0 else None), "ceramic", scale=0.5)


def glow(hex_color, strength):
    return mat("flame", 0.4, emit=strength, color=hex_color)


def glass(hex_color, alpha=0.3, rough=0.05, emit=0.0):
    """See-through glass (bottles, jars, cabinet panes). Low alpha = clearer."""
    name = f"G_{hex_color}_{alpha}_{rough}_{emit}"
    if name in _mats:
        return _mats[name]
    m = bpy.data.materials.new("M_glass")
    if bpy.app.version < (5, 0, 0):
        m.use_nodes = True
    b = _principled(m)
    c = lin(hex_color)
    _set(b, ["Base Color"], c)
    _set(b, ["Roughness"], rough)
    _set(b, ["Alpha"], alpha)
    _set(b, ["Specular IOR Level", "Specular"], 0.8)
    if emit:
        _set(b, ["Emission Color", "Emission"], c)
        _set(b, ["Emission Strength"], emit)
    if hasattr(m, "surface_render_method"):          # Blender 4.2+: smooth sorted transparency, no dither noise
        m.surface_render_method = "BLENDED"
    elif hasattr(m, "blend_method"):
        m.blend_method = "BLEND"
    if hasattr(m, "use_transparent_shadow"):
        m.use_transparent_shadow = True
    m.diffuse_color = (*c[:3], alpha)
    m["kit_color_key"] = "glass"
    _mats[name] = m
    return m


# --------------------------------------------------------------------- mesh helpers
def _finish(o, material, bevel, coll, parent, segs=3):
    o.data.materials.append(material)
    if bevel:
        mod = o.modifiers.new("Bevel", "BEVEL")
        mod.width = bevel
        mod.segments = segs
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
    _finish(o, material, min(bevel, min(size) * 0.45), coll, parent)
    if not bevel:                                   # sharp boxes (labels, tiles, rug stripes) stay flat-shaded
        o.data.polygons.foreach_set("use_smooth", [False] * len(o.data.polygons))
    return o


def boxes(name, parts, material, bevel=0.003, coll=None, parent=None, segs=2):
    """MANY boxes merged into one object (fast for hundreds of tiles). parts = [(size, loc, rot), ...]."""
    bm = bmesh.new()
    for size, loc, rot in parts:
        verts = bmesh.ops.create_cube(bm, size=1.0)["verts"]
        bmesh.ops.transform(bm, matrix=Matrix.LocRotScale(Vector(loc), Euler(rot), Vector(size)), verts=verts)
    o = _finish(_obj(name, bm), material, bevel, coll, parent, segs)
    if not bevel:
        o.data.polygons.foreach_set("use_smooth", [False] * len(o.data.polygons))
    return o


def cyl(name, r, h, loc, material, r2=None, segs=32, bevel=0.003, rot=(0, 0, 0), coll=None, parent=None):
    """Cylinder (or tapered cylinder with r2). loc = centre."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=segs, radius1=r, radius2=r if r2 is None else r2, depth=h)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, bevel, coll, parent)


def ball(name, r, loc, material, scale=(1, 1, 1), coll=None, parent=None, segs=24, rot=(0, 0, 0)):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=segs, v_segments=max(8, segs // 2 + 2), radius=r)
    o = _obj(name, bm)
    o.location, o.scale, o.rotation_euler = loc, scale, rot
    return _finish(o, material, 0, coll, parent)


def ring(name, big_r, r, loc, material, rot=(0, 0, 0), segs=40, coll=None, parent=None):
    """Torus (ring) lying flat in local XY."""
    bm = bmesh.new()
    rows = [[bm.verts.new(((big_r + r * math.cos(b)) * math.cos(a), (big_r + r * math.cos(b)) * math.sin(a),
                           r * math.sin(b))) for b in (2 * math.pi * j / 10 for j in range(10))]
            for a in (2 * math.pi * i / segs for i in range(segs))]
    for i in range(segs):
        r1, r2 = rows[i], rows[(i + 1) % segs]
        for j in range(10):
            bm.faces.new((r1[j], r2[j], r2[(j + 1) % 10], r1[(j + 1) % 10]))
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, 0, coll, parent)


def lathe(name, prof, loc, material, segs=32, rot=(0, 0, 0), wave=None, coll=None, parent=None, scale=(1, 1, 1)):
    """A TURNED part (bottle, candle, column, pot). prof = [(radius, z), ...] bottom to top, spun around local Z.
    wave=(count, amount) adds ribs/folds (prismatic glass, tablecloth folds); wave=(count, amount, True) makes the
    folds grow from nothing at the first ring to full size at the last ring."""
    bm = bmesh.new()
    rings = []
    for j, (r, z) in enumerate(prof):
        amt = 0.0 if not wave else wave[1] * ((j / (len(prof) - 1)) if len(wave) > 2 and wave[2] else 1.0)
        rings.append([bm.verts.new((r * (1 + amt * math.cos(wave[0] * a if wave else 0)) * math.cos(a),
                                    r * (1 + amt * math.cos(wave[0] * a if wave else 0)) * math.sin(a), z))
                      for a in (2 * math.pi * i / segs for i in range(segs))])
    for r1, r2 in zip(rings, rings[1:]):
        for i in range(segs):
            bm.faces.new((r1[i], r1[(i + 1) % segs], r2[(i + 1) % segs], r2[i]))
    if prof[0][0] > 0.0005:
        bm.faces.new(list(reversed(rings[0])))
    if prof[-1][0] > 0.0005:
        bm.faces.new(rings[-1])
    o = _obj(name, bm)
    o.location, o.rotation_euler, o.scale = loc, rot, scale
    _finish(o, material, 0, coll, parent)
    flat = [abs(p.normal.z) > 0.97 for p in o.data.polygons]        # crisp steps, smooth curves
    o.data.polygons.foreach_set("use_smooth", [not f for f in flat])
    return o


def tube(name, pts, radii, material, segs=10, coll=None, parent=None):
    """A round bar swept along a list of points (iron rods, chair legs, lamp arms, ropes, bail handles)."""
    if not isinstance(radii, (list, tuple)):
        radii = [radii] * len(pts)
    pts = [Vector(p) for p in pts]
    bm = bmesh.new()
    rings = []
    for i, p in enumerate(pts):
        t = (pts[min(i + 1, len(pts) - 1)] - pts[max(i - 1, 0)]).normalized()
        ref = Vector((0, 0, 1)) if abs(t.z) < 0.9 else Vector((1, 0, 0))
        n1 = t.cross(ref).normalized()
        n2 = t.cross(n1).normalized()
        rings.append([bm.verts.new(p + radii[i] * (math.cos(a) * n1 + math.sin(a) * n2))
                      for a in (2 * math.pi * k / segs for k in range(segs))])
    for r1, r2 in zip(rings, rings[1:]):
        for k in range(segs):
            bm.faces.new((r1[k], r1[(k + 1) % segs], r2[(k + 1) % segs], r2[k]))
    bm.faces.new(list(reversed(rings[0])))
    bm.faces.new(rings[-1])
    return _finish(_obj(name, bm), material, 0, coll, parent)


def arc_pts(center, radius, a0, a1, n=12, plane="XZ"):
    """Points on a circular arc (angles in degrees). plane 'XZ' or 'YZ' (vertical) or 'XY' (flat)."""
    cx, cy, cz = center
    out = []
    for i in range(n + 1):
        a = R(a0 + (a1 - a0) * i / n)
        u, v = radius * math.cos(a), radius * math.sin(a)
        out.append({"XZ": (cx + u, cy, cz + v), "YZ": (cx, cy + u, cz + v), "XY": (cx + u, cy + v, cz)}[plane])
    return out


def anchor(name, loc, turn=0, coll=None, parent=None):
    """Empty used as a local frame: x = across, y = depth (front = -y), z = up."""
    e = bpy.data.objects.new(name, None)
    e.empty_display_size = 0.1
    e.location, e.rotation_euler = loc, (0, 0, R(turn))
    (coll or COL_ROOM).objects.link(e)
    e.parent = parent
    return e


def no_shadow(*objs):
    for o in objs:
        if hasattr(o, "visible_shadow"):
            o.visible_shadow = False            # glowing things should not block their own light
    return objs[0] if objs else None


def deco_text(name, text, height, loc, material, rot=(R(90), 0, 0), max_width=1.0, parent=None, depth=0.003):
    """Fixed 3D text that is part of the room (not a portfolio hook)."""
    cu = bpy.data.curves.new(name, "FONT")
    cu.body, cu.size, cu.align_x, cu.align_y = text, height, "CENTER", "CENTER"
    cu.extrude = depth
    o = bpy.data.objects.new(name, cu)
    o.location, o.rotation_euler = loc, rot
    o.data.materials.append(material)
    COL_ROOM.objects.link(o)
    o.parent = parent
    bpy.context.view_layer.update()
    if o.dimensions.x > max_width:
        o.scale = [max_width / o.dimensions.x] * 3
    return o


def light(name, kind, energy, color, loc, aim=None, size=None, parent=None):
    data = bpy.data.lights.new(name, kind)
    data.energy, data.color = energy, color[:3]
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
    o.parent = parent
    return o


# --------------------------------------------------------------------- shared real-world props
def flame(name, loc, size=1.0, parent=None):
    """Teardrop candle flame (glows, casts no shadow)."""
    fr, fh = 0.0075 * size, 0.034 * size
    return no_shadow(lathe(name, [(0.0005, 0), (fr * 0.8, fh * 0.15), (fr, fh * 0.35), (fr * 0.6, fh * 0.7),
                                  (0.0005, fh)], loc, glow(COLORS["candle"], 14.0), segs=12, parent=parent))


def pillar_candle(name, loc, h=0.15, r=0.035, parent=None, lit=True, glow_light=False, plate=True):
    """Church pillar candle (e.g. 7 x 15 cm) with a sunken melt pool, a raised rim, drips and a brass plate."""
    x, y, z = loc
    if plate:
        lathe(f"{name}_Plate", [(r + 0.022, 0), (r + 0.024, 0.004), (r + 0.018, 0.008), (r + 0.004, 0.006),
                                (0.0005, 0.006)], (x, y, z), brass(0.35), segs=28, parent=parent)
        z += 0.006
    wx = wax(random.choice((0.95, 1.0, 1.03)))
    lathe(f"{name}_Wax", [(r * 0.97, 0), (r, 0.004), (r, h - 0.004), (r * 0.98, h + 0.004), (r * 0.86, h + 0.002),
                          (r * 0.55, h - 0.008), (0.0005, h - 0.011)], (x, y, z), wx, segs=28, parent=parent)
    for k in range(random.randint(3, 5)):                    # wax drips running down from the rim
        a = random.uniform(0, 2 * math.pi)
        ln = random.uniform(0.02, min(0.09, h * 0.6))
        ball(f"{name}_Drip", 0.0065, (x + math.cos(a) * r * 0.97, y + math.sin(a) * r * 0.97, z + h - ln / 2 + 0.002),
             wx, scale=(1, 1, ln / 0.013), segs=10, parent=parent)
    cyl(f"{name}_Wick", 0.0014, 0.014, (x, y, z + h - 0.006), mat("dark", 0.8), segs=6, bevel=0, parent=parent)
    if lit and CANDLES:
        flame(f"{name}_Flame", (x, y, z + h + 0.0), size=1.0, parent=parent)
        if glow_light:
            light(f"Light_{name}", "POINT", LAMP_STRENGTH, kelvin(LAMP_WARMTH), (x, y, z + h + 0.09), size=0.04,
                  parent=parent)


def label(name, loc, w, h, parent=None, rot=(0, 0, 0), ink_lines=2):
    """Paper label with a ruled border and a couple of hand-written lines (no readable brand text)."""
    x, y, z = loc
    box(name, (w, 0.0015, h), (x, y, z), paper(0.97), bevel=0, rot=rot, parent=parent)
    ink = mat("ink", 0.8, color=shade(COLORS["wood"], 0.55))
    lines = [((w * random.uniform(0.45, 0.75), 0.001, 0.0035), (x, y - 0.0012, z + h * (0.18 - 0.36 * k)), rot)
             for k in range(ink_lines)]
    boxes(f"{name}_Ink", lines, ink, bevel=0, parent=parent)


def herb_fills():
    """Real dried-herb colours for the shop jars, nudged towards the theme palette."""
    return [mix_hex(COLORS["cream"], "#D8B040", 0.55),       # chamomile flowers
            mix_hex(COLORS["wax"], "#C46A78", 0.5),          # rose buds
            shade(COLORS["plant"], 0.75),                    # nettle / peppermint leaf
            mix_hex(COLORS["main"], "#8A76B0", 0.55),        # lavender
            mix_hex(COLORS["amber"], "#E08A2A", 0.6),        # calendula petals
            shade(COLORS["wax"], 0.95),                      # hibiscus / rosehip
            shade(COLORS["wood"], 1.1)]                      # cut roots, black tea


def shop_jar(name, x, y, z, r, h, fill_hex, parent, with_label=True):
    """Clear glass pharmacy jar with a ground-glass mushroom stopper, dried contents and a paper label."""
    g = glass("#E4EEEA", 0.12)
    lathe(f"{name}_Glass", [(r * 0.92, 0), (r, 0.006), (r, h * 0.8), (r * 0.8, h * 0.9), (r * 0.56, h * 0.94),
                            (r * 0.56, h)], (x, y, z), g, segs=28, parent=parent)
    fill = surface(mat("herbs", 0.9, color=fill_hex), "terrazzo", scale=0.6)       # chips = dried flower bits
    fh = h * random.uniform(0.5, 0.72)
    cyl(f"{name}_Fill", r * 0.9, fh, (x, y, z + 0.004 + fh / 2), fill, segs=20, bevel=0.008, parent=parent)
    lathe(f"{name}_Stopper", [(r * 0.5, 0), (r * 0.56, 0.008), (r * 0.25, 0.016), (r * 0.22, 0.03), (r * 0.6, 0.042),
                              (r * 0.55, 0.055), (0.0005, 0.06)], (x, y, z + h - 0.004), g, segs=24, parent=parent)
    if with_label:
        label(f"{name}_Label", (x, y - r - 0.0015, z + h * 0.42), r * 1.15, h * 0.26, parent=parent)


def amber_bottle(name, x, y, z, s, parent, key="amber", with_label=True, glowing=False):
    """250 ml Boston-round apothecary bottle (14 x 7 cm) with a cork and a paper label."""
    r, h = 0.034 * s, 0.13 * s
    col = COLORS[key] if key in COLORS else key
    if glowing:                                     # real coloured glass (cobalt, rose, green) is deep, not pastel
        col = mix_hex(col, COLORS["dark"], 0.35)
    g = glass(col, 0.6 if glowing else 0.82, 0.08, emit=0.25 * POTION_GLOW if glowing else 0.0)
    lathe(f"{name}_Glass", [(r * 0.94, 0), (r, 0.005), (r, h * 0.66), (r * 0.82, h * 0.78), (r * 0.34, h * 0.86),
                            (r * 0.32, h * 0.95), (r * 0.36, h * 0.97), (r * 0.33, h)], (x, y, z), g, segs=24,
          parent=parent)
    cyl(f"{name}_Cork", r * 0.34, 0.02 * s, (x, y, z + h + 0.006 * s), wood(1.7, 0.85, key="wood"), r2=r * 0.38,
        segs=12, bevel=0.002, parent=parent)
    if glowing:                                     # cork-LED fairy light: a coil of tiny warm-white LEDs on wire
        coil = lambda t: Vector((math.cos(t * 15.7) * r * 0.6, math.sin(t * 15.7) * r * 0.6, 0.012 + t * h * 0.6))
        bm = bmesh.new()
        for k in range(10):
            ico = bmesh.ops.create_icosphere(bm, subdivisions=1, radius=0.0032 * s)["verts"]
            bmesh.ops.translate(bm, vec=coil(k / 9), verts=ico)
        leds = _finish(_obj(f"{name}_LEDs", bm), glow(COLORS["candle"], 6.0 * POTION_GLOW + 0.01), 0, None, parent)
        leds.location = (x, y, z)
        no_shadow(leds)
        tube(f"{name}_Wire", [Vector((x, y, z)) + coil(k / 40) for k in range(41)] + [(x, y, z + h)],
             0.0007, mat("wire", 0.4, metal=1.0, color="#B87333"), segs=4, parent=parent)
    elif with_label:
        label(f"{name}_Label", (x, y - r - 0.0015, z + h * 0.36), r * 1.4, h * 0.3, parent=parent)
    return 2 * r


def crock(name, x, y, z, r, h, parent):
    """Two-tone salt-glazed stoneware crock (cream body, brown dipped shoulder) with a lid."""
    body = surface(mat("cream", 0.3, color=shade(COLORS["cream"], 0.92)), "ceramic")
    dip = surface(mat("wood", 0.25, color=shade(COLORS["amber"], 0.8)), "ceramic")
    lathe(f"{name}_Body", [(r * 0.9, 0), (r, 0.01), (r * 1.02, h * 0.6)], (x, y, z), body, segs=28, parent=parent)
    lathe(f"{name}_Shoulder", [(r * 1.02, 0), (r * 0.96, h * 0.25), (r * 0.8, h * 0.35), (r * 0.8, h * 0.4)],
          (x, y, z + h * 0.6), dip, segs=28, parent=parent)
    lathe(f"{name}_Lid", [(r * 0.84, 0), (r * 0.84, 0.01), (r * 0.5, 0.025), (r * 0.18, 0.03), (r * 0.2, 0.045),
                          (0.0005, 0.05)], (x, y, z + h), dip, segs=24, parent=parent)


def crystal(name, loc, r, h, material, tilt=(0, 0), parent=None):
    """One quartz / amethyst point: six-sided prism with a pointed termination."""
    o = lathe(name, [(r * 0.9, 0), (r, 0.002), (r, h * 0.72), (0.0005, h)], loc, material, segs=6,
              rot=(R(tilt[0]), R(tilt[1]), R(random.uniform(0, 60))), parent=parent)
    o.data.polygons.foreach_set("use_smooth", [False] * len(o.data.polygons))
    return o


def cluster(name, loc, key, n=6, size=1.0, parent=None):
    """Crystal cluster on a grey matrix rock (amethyst / clear quartz geode piece)."""
    x, y, z = loc
    rock = surface(mat("metal", 0.9, color=mix_hex(COLORS["metal"], "#8A8A8A", 0.4)), "concrete")
    ball(f"{name}_Matrix", 0.05 * size, (x, y, z + 0.015 * size), rock, scale=(1.3, 1.0, 0.5), segs=12, parent=parent)
    m = glass(mix_hex(COLORS[key], "#FFFFFF", 0.25), 0.75, 0.05, emit=0.25)
    for k in range(n):
        a = k * 2 * math.pi / n + random.uniform(-0.3, 0.3)
        d = random.uniform(0.0, 0.035) * size
        crystal(f"{name}_Point", (x + math.cos(a) * d, y + math.sin(a) * d, z + 0.02 * size),
                random.uniform(0.008, 0.014) * size, random.uniform(0.05, 0.1) * size, m,
                tilt=(math.sin(a) * -25 * d / 0.035, math.cos(a) * 25 * d / 0.035), parent=parent)


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
#   picture hooks: "screen" (glows), "frame", "poster", "board", "logo"  -> project images (in order)
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
    """Mark decoration that is hidden once the hook gets a real image (e.g. a drawing on a print)."""
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


# =====================================================================
#  ROOM SHELL
# =====================================================================
# Floor: Victorian 6 in (150 mm) unglazed quarry tiles, the classic shop / hallway floor. The field is laid
# diagonally in two colours; a border of square tiles and a narrow fillet strip run straight round the edge.
# Every fired-clay tile is a slightly different shade, so the floor reads as clay, not as a chessboard.
box("Floor_Base", (W + T, D + T, 0.2), ((W - T) / 2, (D + T) / 2, -0.1),
    surface(mat("dark", 0.9, color=mix_hex(COLORS["tile_dark"], COLORS["floor"], 0.45)), "concrete"), bevel=0.02)
TS, GAP = 0.15, 0.004                            # tile size, grout joint
BORDER, FILLET = 0.15, 0.04                      # straight border row + fillet strip round the field
B_IN = BORDER + FILLET
tile_mats = {(c, k): surface(mat(c, 0.5 + 0.01 * k, color=shade(COLORS[c], f)), "concrete", scale=3)
             for c in ("floor", "tile_dark") for k, f in enumerate((0.9, 1.0, 1.1))}
cutter = box("Floor_Cutter", (W - 2 * B_IN, D - 2 * B_IN, 1.0), (W / 2, D / 2, 0), mat("floor"), bevel=0)
cutter.hide_render = cutter.hide_viewport = True
s2 = math.sqrt(0.5)
tile_parts = {key: [] for key in tile_mats}
for i in range(-2, int((W + D) * s2 / TS) + 3):
    for j in range(-int(W * s2 / TS) - 3, int(D * s2 / TS) + 3):
        u, v = (i + 0.5) * TS, (j + 0.5) * TS
        x, y = (u - v) * s2, (u + v) * s2
        if B_IN - 0.15 < x < W - B_IN + 0.15 and B_IN - 0.15 < y < D - B_IN + 0.15:
            key = (("floor", "tile_dark")[(i + j) % 2], random.randrange(3))
            tile_parts[key].append(((TS - GAP, TS - GAP, FLOOR_Z), (u, v, FLOOR_Z / 2), (0, 0, 0)))
for (c, k), parts in tile_parts.items():
    t = boxes(f"Floor_Tiles_{c}_{k}", parts, tile_mats[(c, k)], bevel=0.0015, segs=1)
    t.rotation_euler = (0, 0, R(45))
    cut = t.modifiers.new("Room", "BOOLEAN")
    cut.operation, cut.object = "INTERSECT", cutter
border = {key: [] for key in tile_mats}


def tile_run(a0, a1, fixed, width, along_x, colour):
    """A straight row of tiles from a0 to a1 (the last one cut short), centred on `fixed` across the row."""
    a = a0
    while a < a1 - 0.01:
        ln = min(TS, a1 - a)
        size = (ln - GAP, width - GAP, FLOOR_Z) if along_x else (width - GAP, ln - GAP, FLOOR_Z)
        loc = (a + ln / 2, fixed, FLOOR_Z / 2) if along_x else (fixed, a + ln / 2, FLOOR_Z / 2)
        border[(colour, random.randrange(3))].append((size, loc, (0, 0, 0)))
        a += ln


for along_x, length, (f0, f1) in ((True, W, (BORDER / 2, D - BORDER / 2)), (False, D, (BORDER / 2, W - BORDER / 2))):
    for fixed in (f0, f1):                                         # border row on all four edges (corners once)
        tile_run(0.0 if along_x else BORDER, length if along_x else length - BORDER, fixed, BORDER, along_x,
                 "tile_dark")
    for fixed in (BORDER + FILLET / 2, (D if along_x else W) - BORDER - FILLET / 2):
        inset = BORDER if along_x else B_IN
        tile_run(inset, length - inset, fixed, FILLET, along_x, "floor")        # buff fillet strip
for key, parts in border.items():
    if parts:
        boxes(f"Floor_Border_{key[0]}_{key[1]}", parts, tile_mats[key], bevel=0.0015, segs=1)

# Walls: dark limewash plaster. A timber shop window in the left wall.
WIN_Y = (1.8, 2.85)                 # from front to back
WIN_Z = (1.05, 2.35)                # the sill sits on the dado rail, like a real shop window
plaster = surface(mat("wall", 0.92), "plaster")
left = box("Wall_Left", (T, D + T, H), (-T / 2, (D + T) / 2, H / 2), plaster, bevel=0.0)
win_cut = box("Window_Cutter", (T * 3, WIN_Y[1] - WIN_Y[0], WIN_Z[1] - WIN_Z[0]),
              (-T / 2, sum(WIN_Y) / 2, sum(WIN_Z) / 2), mat("wall"), bevel=0.0)
win_cut.hide_render = win_cut.hide_viewport = True
boolean = left.modifiers.new("Window", "BOOLEAN")
boolean.operation, boolean.object = "DIFFERENCE", win_cut
box("Wall_Back", (W + T, T, H), ((W - T) / 2, D + T / 2, H / 2),
    surface(mat("wall", 0.92, color=shade(COLORS["wall"], 1.08)), "plaster"), bevel=0.0)
cap = wood(0.7, 0.5)
box("Trim_Top_Back", (W + T + 0.04, T + 0.04, 0.08), ((W - T) / 2, D + T / 2, H + 0.04), cap, bevel=0.008)
box("Trim_Top_Left", (T + 0.04, D + T + 0.04, 0.08), (-T / 2, (D + T) / 2 - 0.02, H + 0.04),
    wood(0.7, 0.5, along="Y"), bevel=0.008)
cornice = surface(mat("wall", 0.8, color=shade(COLORS["wall"], 1.3)), "plaster")
for i, (dd, hh) in enumerate(((0.05, 0.03), (0.03, 0.05))):          # two-step plaster cornice
    z = H - 0.08 + (0.0 if i else 0.05) + hh / 2 - (0.0 if i else 0.02)
    box(f"Cornice_Back_{i}", (W, dd, hh), (W / 2, D - dd / 2, z), cornice, bevel=0.006)
    box(f"Cornice_Left_{i}", (dd, D, hh), (dd / 2, D / 2, z), cornice, bevel=0.006)

# Painted tongue-and-groove dado (1.0 m) with a moulded rail and a 15 cm skirting board.
DADO, SKIRT = 1.0, 0.15
tg = surface(mat("wall_trim", 0.55), "wood", along="Z")
tg_y = surface(mat("wall_trim", 0.551), "wood", along="Z")
groove = mat("wall_trim", 0.8, color=shade(COLORS["wall_trim"], 0.55))
rail_m = surface(mat("wall_trim", 0.45, color=shade(COLORS["wall_trim"], 1.15)), "wood")
rail_y = surface(mat("wall_trim", 0.451, color=shade(COLORS["wall_trim"], 1.15)), "wood", along="Y")


def dado_run(axis, a0, a1, top=DADO):
    """Tongue-and-groove boards on the back wall (axis 'x') or the left wall (axis 'y') between a0 and a1."""
    L = a1 - a0
    if L < 0.05:
        return
    mid = (a0 + a1) / 2
    if axis == "x":
        P = lambda nm, sx, sz, a, z, dy, mt: box(nm, (sx, dy, sz), (a, D - dy / 2, z), mt, bevel=0.003)
        G = lambda a, z, sz: ((0.006, 0.004, sz), (a, D - 0.019, z), (0, 0, 0))
    else:
        P = lambda nm, sx, sz, a, z, dy, mt: box(nm, (dy, sx, sz), (dy / 2, a, z), mt, bevel=0.003)
        G = lambda a, z, sz: ((0.004, 0.006, sz), (0.019, a, z), (0, 0, 0))
    P("Dado_Boards", L, top, mid, top / 2, 0.018, tg if axis == "x" else tg_y)
    gz = SKIRT + (top - SKIRT) / 2
    boxes("Dado_Grooves", [G(a0 + 0.095 * (k + 1), gz, top - SKIRT) for k in range(int(L / 0.095))], groove, bevel=0)
    rm = rail_m if axis == "x" else rail_y
    P("Dado_Rail", L, 0.035, mid, top + 0.0175, 0.045, rm)
    P("Dado_RailBead", L, 0.02, mid, top - 0.01, 0.03, rm)
    P("Skirting", L, SKIRT, mid, SKIRT / 2, 0.028, rm)
    P("Skirting_Top", L, 0.02, mid, SKIRT - 0.01, 0.036, rm)


dado_run("x", 0.0, W)
dado_run("y", 0.0, WIN_Y[0] - 0.08)
dado_run("y", WIN_Y[1] + 0.08, D)
dado_run("y", WIN_Y[0] - 0.08, WIN_Y[1] + 0.08, top=WIN_Z[0] - 0.05)

# Shop window: 3 x 4 small panes (Georgian shopfront), painted frame, deep window board, night sky outside.
wy, wz = sum(WIN_Y) / 2, sum(WIN_Z) / 2
ww, wh = WIN_Y[1] - WIN_Y[0], WIN_Z[1] - WIN_Z[0]
frame_paint = surface(mat("wall_trim", 0.45, color=shade(COLORS["wall_trim"], 1.25)), "wood", along="Z")
for nm, size, loc in (("Top", (T, ww, 0.02), (-T / 2, wy, WIN_Z[1] - 0.01)),
                      ("Front", (T, 0.02, wh), (-T / 2, WIN_Y[0] + 0.01, wz)),
                      ("Back", (T, 0.02, wh), (-T / 2, WIN_Y[1] - 0.01, wz))):
    box(f"Window_Lining_{nm}", size, loc, frame_paint, bevel=0.002)
for nm, size, loc in (("Top", (0.025, ww + 0.18, 0.08), (0.0125, wy, WIN_Z[1] + 0.04)),
                      ("Front", (0.025, 0.08, wh), (0.0125, WIN_Y[0] - 0.04, wz)),
                      ("Back", (0.025, 0.08, wh), (0.0125, WIN_Y[1] + 0.04, wz))):
    box(f"Window_Architrave_{nm}", size, loc, frame_paint, bevel=0.005)
box("Window_Board", (T + 0.08, ww + 0.16, 0.03), (-T / 2 + 0.04, wy, WIN_Z[0] - 0.015), wood(1.0, 0.4, along="Y"),
    bevel=0.005)
fx = -0.09                                       # the glazed frame sits in the middle of the wall
bars = [((0.05, 0.05, wh), (fx, WIN_Y[0] + 0.025, wz), (0, 0, 0)), ((0.05, 0.05, wh), (fx, WIN_Y[1] - 0.025, wz), (0, 0, 0)),
        ((0.05, ww, 0.05), (fx, wy, WIN_Z[1] - 0.025), (0, 0, 0)), ((0.05, ww, 0.07), (fx, wy, WIN_Z[0] + 0.035), (0, 0, 0))]
gy0, gy1, gz0, gz1 = WIN_Y[0] + 0.05, WIN_Y[1] - 0.05, WIN_Z[0] + 0.07, WIN_Z[1] - 0.05
bars += [((0.03, 0.02, gz1 - gz0), (fx, gy0 + (gy1 - gy0) * k / 3, (gz0 + gz1) / 2), (0, 0, 0)) for k in (1, 2)]
bars += [((0.03, gy1 - gy0, 0.02), (fx, wy, gz0 + (gz1 - gz0) * k / 4), (0, 0, 0)) for k in (1, 2, 3)]
boxes("Window_Frame", bars, frame_paint, bevel=0.003)
no_shadow(box("Window_Glass", (0.004, ww, wh), (fx - 0.005, wy, wz), glass("#B8CCE0", 0.12), bevel=0))
sky = no_shadow(box("Window_Sky", (0.01, ww + 0.4, wh + 0.4), (-T - 0.25, wy, wz), mat("sky", 0.2, emit=1.2), bevel=0))
no_shadow(cyl("Window_Moon", 0.13, 0.01, (-T - 0.24, wy + 0.2, wz + 0.3), mat("moon", 0.3, emit=4.0), segs=40,
              bevel=0, rot=(0, R(90), 0)))
roofs = [((0.01, random.uniform(0.18, 0.4), random.uniform(0.2, 0.55)), (-T - 0.235, WIN_Y[0] + 0.1 + k * 0.17,
          WIN_Z[0] + 0.1), (0, 0, 0)) for k in range(7)]
no_shadow(boxes("Window_Rooftops", roofs, mat("skyline", 0.9, color=shade(COLORS["sky"], 0.45)), bevel=0))
for k, (dy, dz) in enumerate([(-0.35, 0.45), (-0.15, 0.55), (0.38, 0.05), (-0.3, 0.2), (0.05, 0.45)]):
    no_shadow(ball(f"Window_Star_{k}", 0.008, (-T - 0.238, wy + dy, wz + dz), mat("moon", 0.3, emit=5.0),
                   scale=(0.3, 1, 1), segs=8))

# Brass swan-neck wall lights with small prismatic glass shades (Holophane-style), back wall.
SCONCES = [(2.43, 2.32), (3.6, 2.42)]
prism = glass(mix_hex(COLORS["candle"], "#FFFFFF", 0.55), 0.7, 0.1, emit=1.6)
for k, (sx, sz) in enumerate(SCONCES):
    lathe(f"Sconce_Plate_{k}", [(0.045, 0), (0.045, 0.01), (0.03, 0.02), (0.012, 0.03)], (sx, D, sz + 0.12),
          brass(), rot=(R(90), 0, 0), segs=24)
    tube(f"Sconce_Arm_{k}", [(sx, D - 0.03, sz + 0.12), (sx, D - 0.1, sz + 0.16), (sx, D - 0.17, sz + 0.13),
                             (sx, D - 0.2, sz + 0.07)], 0.008, brass())
    lathe(f"Sconce_Gallery_{k}", [(0.012, 0), (0.035, 0.0), (0.04, 0.025), (0.03, 0.03)], (sx, D - 0.2, sz + 0.035),
          brass(), segs=24, rot=(R(180), 0, 0))
    no_shadow(lathe(f"Sconce_Shade_{k}", [(0.035, 0), (0.06, -0.03), (0.08, -0.08), (0.06, -0.11), (0.0005, -0.12)],
                    (sx, D - 0.2, sz + 0.035), prism, segs=36, wave=(18, 0.05)))
    light(f"Light_Sconce_{k}", "POINT", 14, kelvin(LAMP_WARMTH + 300), (sx, D - 0.22, sz - 0.03), size=0.06)


# =====================================================================
#  FURNITURE SLOTS  (same names in every template)
#  size = (width, depth, height); front of the furniture faces local -Y
# =====================================================================
slot("shelf",         (1.9, 0.52, 2.45),  (1.1, D - 0.26), shape="shelf")
slot("counter",       (1.7, 0.62, 0.92),  (3.6, D - 0.31), shape="counter")
slot("display_case",  (0.95, 0.45, 1.65), (0.255, 0.92), turn=90, shape="cabinet")
slot("wall_shelf",    (0.7, 0.26, 0.45),  (0.13, 3.27), z=1.35, turn=90, kind="wall", shape="shelf")
slot("hanging_plant", (1.45, 0.38, 0.75), (0.42, 0.95), z=2.05, turn=90, kind="hanging", shape="plant")
slot("hero_prop",     (1.1, 1.1, 1.45),   (2.15, 2.2), shape="box")
slot("armchair",      (0.82, 0.96, 1.01), (3.95, 1.45), turn=-30, shape="chair")
slot("rug",           (2.6, 1.7, 0.012),  (2.2, 1.75), kind="rug", shape="rug")
slot("pet",           (0.3, 0.46, 0.4),   (1.35, 1.3), z=FLOOR_Z + 0.012, turn=25, shape="pet")


# =====================================================================
#  PLACEHOLDER FURNITURE  (replaced when you add your own with add_furniture.py)
# =====================================================================
HERB_FILLS = herb_fills()


def drawer_bank(prefix, root, x0, x1, z0, z1, rows, y_front, veneer, parent_parts):
    """A grid of small apothecary drawers: 18 mm fronts with 3 mm gaps, a brass card frame + cup pull each."""
    cols = 8
    cw, rh = (x1 - x0) / cols, (z1 - z0) / rows
    fronts, frames, cups, cards, inks = [], [], [], [], []
    for r_ in range(rows):
        for c in range(cols):
            cx, cz = x0 + (c + 0.5) * cw, z0 + (r_ + 0.5) * rh
            fronts.append(((cw - 0.006, 0.018, rh - 0.006), (cx, y_front + 0.009, cz), (0, 0, 0)))
            fy = y_front - 0.002
            lz = cz + rh * 0.18
            fw, fh = min(0.075, cw * 0.4), 0.032
            frames += [((fw, 0.004, 0.004), (cx, fy, lz + fh / 2), (0, 0, 0)),
                       ((fw, 0.004, 0.004), (cx, fy, lz - fh / 2), (0, 0, 0)),
                       ((0.004, 0.004, fh), (cx - fw / 2, fy, lz), (0, 0, 0)),
                       ((0.004, 0.004, fh), (cx + fw / 2, fy, lz), (0, 0, 0))]
            cards.append(((fw - 0.006, 0.0015, fh - 0.006), (cx, y_front - 0.0008, lz), (0, 0, 0)))
            inks.append(((fw * random.uniform(0.45, 0.7), 0.001, 0.005), (cx, y_front - 0.0017, lz), (0, 0, 0)))
            pz = cz - rh * 0.17
            cups += [((0.07, 0.004, 0.024), (cx, y_front - 0.002, pz), (0, 0, 0)),          # back plate
                     ((0.062, 0.016, 0.006), (cx, y_front - 0.01, pz - 0.011), (0, 0, 0)),   # lip of the cup
                     ((0.062, 0.004, 0.02), (cx, y_front - 0.017, pz - 0.003), (R(-25), 0, 0))]
    boxes(f"{prefix}_Fronts", fronts, veneer, bevel=0.003, parent=root)
    boxes(f"{prefix}_LabelFrames", frames, brass(0.3), bevel=0.0, parent=root)
    boxes(f"{prefix}_Cups", cups, brass(0.28), bevel=0.0015, parent=root)
    boxes(f"{prefix}_Cards", cards, paper(0.95), bevel=0, parent=root)
    boxes(f"{prefix}_CardInk", inks, mat("ink", 0.8, color=shade(COLORS["wood"], 0.55)), bevel=0, parent=root)


def fill_shelf(prefix, root, x0, x1, y, z, max_h):
    """Stand a row of real shop bottles and jars on a shelf between x0 and x1."""
    x = x0
    k = 0
    while x < x1 - 0.06:
        roll = random.random()
        nm = f"{prefix}_{k}"
        if roll < 0.38 and max_h > 0.24:
            r = random.uniform(0.045, 0.055)
            if x + 2 * r > x1:
                break
            shop_jar(nm, x + r, y + random.uniform(-0.02, 0.02), z, r, random.uniform(0.17, min(0.22, max_h - 0.07)),
                     random.choice(HERB_FILLS), root)
            x += 2 * r + random.uniform(0.012, 0.03)
        elif roll < 0.72:
            s = random.uniform(0.85, 1.2)
            glowing = random.random() < 0.3
            key = random.choice(("accent_1", "accent_2", "accent_3")) if glowing else \
                random.choice(("amber", "amber", "amber", shade(COLORS["sky"], 1.1), "#2D4A2A"))
            x += amber_bottle(nm, x + 0.034 * s, y + random.uniform(-0.03, 0.03), z, s, root, key=key,
                              glowing=glowing) + random.uniform(0.01, 0.025)
        elif roll < 0.86:
            r = random.uniform(0.04, 0.05)
            if x + 2 * r > x1:
                break
            crock(nm, x + r, y, z, r, random.uniform(0.09, 0.12), root)
            x += 2 * r + 0.02
        else:                                                    # a few old books lying flat or upright
            for b in range(random.randint(2, 4)):
                bw = random.uniform(0.025, 0.04)
                bh = random.uniform(0.16, min(0.24, max_h - 0.03))
                if x + bw > x1:
                    break
                box(f"{nm}_Book_{b}", (bw, random.uniform(0.15, 0.2), bh), (x + bw / 2, y, z + bh / 2),
                    surface(mat("book", 0.7, color=random.choice([COLORS["wax"], COLORS["wall_trim"], COLORS["main"],
                            shade(COLORS["wood"], 1.3), shade(COLORS["plant"], 0.7)])), "leather"),
                    bevel=0.003, parent=root)
                x += bw + 0.002
            x += 0.02
        k += 1


def build_shelf():
    """Antique walnut apothecary cabinet: 32-drawer base + worktop, 24-drawer hutch, open shelves of jars,
    stepped cornice, tongue-and-groove back and a hook-on library ladder on a brass rail."""
    root, w, d, h = furniture_root("shelf")
    hook_link(root, "github")
    side, flat, veneer = wood(1.0, 0.4, along="Z"), wood(1.0, 0.4), wood(1.1, 0.38, kind="veneer")
    dark = wood(0.45, 0.7)
    BASE_H, DH = 0.92, 0.32                      # worktop height, hutch depth
    yf = -d / 2                                  # front of the base
    # Base carcass.
    for sx in (-1, 1):
        box("Cab_Side", (0.025, d, BASE_H - 0.03), (sx * (w / 2 - 0.0125), 0, (BASE_H - 0.03) / 2), side, parent=root)
    box("Cab_Plinth", (w - 0.04, 0.02, 0.085), (0, yf + 0.035, 0.0425), dark, parent=root)
    box("Cab_Inside", (w - 0.05, d - 0.03, BASE_H - 0.115), (0, 0.015, 0.085 + (BASE_H - 0.115) / 2), dark,
        bevel=0, parent=root)
    box("Cab_Worktop", (w + 0.03, d + 0.02, 0.03), (0, -0.01, BASE_H - 0.015), flat, bevel=0.005, parent=root)
    drawer_bank("Cab_Base", root, -w / 2 + 0.025, w / 2 - 0.025, 0.088, BASE_H - 0.032, 4, yf + 0.002, veneer, None)
    # Hutch.
    yh = d / 2 - DH                              # front of the hutch
    top = h - 0.1                                # underside of the cornice
    for sx in (-1, 1):
        box("Hutch_Side", (0.025, DH, top - BASE_H), (sx * (w / 2 - 0.0125), d / 2 - DH / 2, (BASE_H + top) / 2),
            side, parent=root)
    back = wood(0.7, 0.5, along="Z", kind="veneer")
    box("Hutch_Back", (w - 0.05, 0.012, top - BASE_H), (0, d / 2 - 0.006, (BASE_H + top) / 2), back, bevel=0,
        parent=root)
    boxes("Hutch_Back_Grooves", [((0.004, 0.004, top - 1.36), (-w / 2 + 0.025 + 0.1 * (k + 1), d / 2 - 0.013,
                                  (1.36 + top) / 2), (0, 0, 0)) for k in range(int((w - 0.05) / 0.1))],
          mat("dark", 0.8), bevel=0, parent=root)
    DZ = 1.36                                    # top of the hutch drawers
    box("Hutch_DrawerBox", (w - 0.05, DH - 0.03, DZ - BASE_H), (0, d / 2 - DH / 2 + 0.01, (BASE_H + DZ) / 2), dark,
        bevel=0, parent=root)
    drawer_bank("Cab_Hutch", root, -w / 2 + 0.025, w / 2 - 0.025, BASE_H + 0.004, DZ - 0.004, 3, yh + 0.002, veneer,
                None)
    levels = [DZ, 1.68, 2.0]
    for z in levels + [top]:
        box("Hutch_Shelf", (w - 0.05, DH - 0.015, 0.02), (0, d / 2 - DH / 2 - 0.004, z + 0.01), flat, parent=root)
        box("Hutch_ShelfLip", (w - 0.05, 0.012, 0.03), (0, yh + 0.006, z + 0.012), wood(1.15, 0.38), parent=root)
    for sx in (-1, 1):                            # two uprights divide the open shelves into three bays
        box("Hutch_Divider", (0.02, DH - 0.02, top - DZ), (sx * w / 6, d / 2 - DH / 2, (DZ + top) / 2), side,
            parent=root)
    for i, (dw, dd, hh) in enumerate(((0.02, 0.02, 0.035), (0.05, 0.035, 0.03), (0.09, 0.06, 0.035))):
        box(f"Cornice_{i}", (w + dw, DH + dd, hh), (0, d / 2 - (DH + dd) / 2, top + 0.005 + i * 0.032 + hh / 2),
            flat, bevel=0.006, parent=root)
    # Bottles and jars on the three open levels (three bays each).
    bay = (w - 0.05 - 0.04) / 3
    for li, z in enumerate(levels):
        clear = (levels + [top])[li + 1] - z - 0.02
        for b in range(3):
            bx0 = -w / 2 + 0.025 + b * (bay + 0.02) + 0.02
            fill_shelf(f"Shelf_L{li}B{b}", root, bx0, bx0 + bay - 0.02, d / 2 - DH / 2 - 0.02, z + 0.02, clear)
    # Brass ladder rail on three brackets and a hook-on oak library ladder.
    RAIL_Z, RAIL_Y = 2.2, yh - 0.06
    b = brass(0.25)
    cyl("Ladder_Rail", 0.0125, w - 0.1, (0, RAIL_Y, RAIL_Z), b, rot=(0, R(90), 0), segs=16, parent=root)
    for bx in (-w / 2 + 0.12, 0, w / 2 - 0.12):
        box("Ladder_RailBracket", (0.02, 0.07, 0.03), (bx, yh - 0.03, RAIL_Z), b, bevel=0.004, parent=root)
    LX, foot_y = w / 2 - 0.42, yf - 0.62
    top_pt, foot_pt = Vector((0, RAIL_Y - 0.01, RAIL_Z - 0.04)), Vector((0, foot_y, 0.0))
    v = top_pt - foot_pt
    L, tilt = v.length, -math.atan2(v.y, v.z)
    oak = wood(1.45, 0.45, along="Z")
    for sx in (-1, 1):
        box("Ladder_Stile", (0.025, 0.06, L), (LX + sx * 0.205, (foot_y + top_pt.y) / 2, L * math.cos(tilt) / 2),
            oak, rot=(tilt, 0, 0), parent=root)
        tube("Ladder_Hook", [(LX + sx * 0.205, RAIL_Y + 0.0, RAIL_Z - 0.06), (LX + sx * 0.205, RAIL_Y + 0.02,
                             RAIL_Z + 0.01), (LX + sx * 0.205, RAIL_Y, RAIL_Z + 0.025),
                             (LX + sx * 0.205, RAIL_Y - 0.02, RAIL_Z + 0.01)], 0.006, b, parent=root)
        box("Ladder_Foot", (0.03, 0.07, 0.02), (LX + sx * 0.205, foot_y + 0.01, 0.01), mat("dark", 0.9), parent=root)
    for k in range(7):                                   # flat treads that sit level when the ladder leans
        t = (k + 1) / 8
        p = foot_pt + v * t
        box("Ladder_Tread", (0.41, 0.09, 0.022), (LX, p.y + 0.02, p.z), wood(1.45, 0.45), parent=root)
    # A few things on the worktop: a mortar and pestle, a tray of amber bottles and a pillar candle.
    stone = surface(mat("cream", 0.6, color=mix_hex(COLORS["cream"], "#9A9A9A", 0.4)), "marble")
    lathe("Mortar", [(0.05, 0), (0.065, 0.02), (0.07, 0.07), (0.062, 0.075), (0.045, 0.03), (0.0005, 0.025)],
          (-0.62, yf + 0.14, BASE_H), stone, segs=28, parent=root)
    tube("Pestle", [(-0.62, yf + 0.14, BASE_H + 0.04), (-0.58, yf + 0.16, BASE_H + 0.15)], [0.016, 0.01], stone,
         parent=root)
    for k in range(4):
        amber_bottle(f"Worktop_Bottle_{k}", -0.25 + k * 0.08, yf + 0.12, BASE_H, 0.85, root)
    pillar_candle("Candle_Worktop", (0.25, yf + 0.11, BASE_H), 0.15, 0.035, parent=root, glow_light=True)


def build_counter():
    """Late-Victorian mahogany shop counter with fielded panels, a brass balance, crystals and a service bell."""
    root, w, d, h = furniture_root("counter")
    mah = lambda f=1.0, al="X": wood(f, 0.32, along=al, key="mahogany")
    box("Counter_Plinth", (w - 0.06, d - 0.06, 0.09), (0, 0.01, 0.045), mah(0.5), parent=root)
    box("Counter_Body", (w - 0.02, d - 0.04, h - 0.125), (0, 0.01, 0.09 + (h - 0.125) / 2), mah(0.85, "Z"),
        parent=root)
    yf = -d / 2 + 0.01
    box("Counter_BaseMould", (w, d - 0.02, 0.03), (0, 0.0, 0.105), mah(1.0), bevel=0.008, parent=root)
    frame = [((w - 0.04, 0.02, 0.07), (0, yf - 0.01, h - 0.07), (0, 0, 0)),
             ((w - 0.04, 0.02, 0.08), (0, yf - 0.01, 0.16), (0, 0, 0))]
    frame += [((0.08, 0.02, h - 0.31), (-w / 2 + 0.06 + k * (w - 0.12) / 3, yf - 0.01, 0.2 + (h - 0.31) / 2), (0, 0, 0))
              for k in range(4)]
    boxes("Counter_FrontFrame", frame, mah(1.0, "Z"), bevel=0.004, parent=root)
    pw = (w - 0.12) / 3 - 0.08
    for k in range(3):                                   # raised fields with a bevelled edge
        px = -w / 2 + 0.06 + (k + 0.5) * (w - 0.12) / 3
        box("Counter_Field", (pw - 0.01, 0.022, h - 0.33), (px, yf - 0.006, 0.2 + (h - 0.31) / 2), mah(1.08, "Z"),
            bevel=0.012, parent=root)
        box("Counter_Bead", (pw + 0.01, 0.008, h - 0.31), (px, yf - 0.002, 0.2 + (h - 0.31) / 2), mah(0.7),
            bevel=0.002, parent=root)
    box("Counter_Top", (w + 0.04, d + 0.03, 0.035), (0, -0.005, h - 0.0175), mah(1.15), bevel=0.012, parent=root)
    b = brass(0.28)
    # Brass balance on a mahogany base with a drawer, stepped weights and pans on three chains.
    sx, sy = -w / 2 + 0.33, 0.05
    box("Balance_Base", (0.46, 0.2, 0.07), (sx, sy, h + 0.035), mah(1.2), bevel=0.006, parent=root)
    box("Balance_Drawer", (0.18, 0.004, 0.04), (sx, sy - 0.101, h + 0.035), mah(1.0), bevel=0.002, parent=root)
    ball("Balance_Knob", 0.007, (sx, sy - 0.107, h + 0.035), b, segs=10, parent=root)
    top = h + 0.07
    lathe("Balance_Pillar", [(0.03, 0), (0.03, 0.01), (0.012, 0.03), (0.009, 0.3), (0.016, 0.31), (0.016, 0.33),
                             (0.0005, 0.345)], (sx, sy, top), b, segs=20, parent=root)
    BZ = top + 0.33
    box("Balance_Beam", (0.42, 0.01, 0.014), (sx, sy, BZ), b, bevel=0.002, parent=root)
    box("Balance_Pointer", (0.004, 0.004, 0.12), (sx, sy - 0.012, BZ - 0.065), b, bevel=0, parent=root)
    for side in (-1, 1):
        ex = sx + side * 0.2
        pz = top + 0.09
        ball("Balance_EndKnob", 0.008, (ex, sy, BZ), b, segs=10, parent=root)
        for a in (90, 210, 330):
            tube("Balance_Chain", [(ex, sy, BZ - 0.006), (ex + math.cos(R(a)) * 0.065, sy + math.sin(R(a)) * 0.065,
                                                          pz + 0.012)], 0.0012, b, segs=5, parent=root)
        lathe("Balance_Pan", [(0.0005, 0), (0.05, 0.004), (0.068, 0.012), (0.07, 0.014), (0.066, 0.012),
                              (0.0005, 0.004)], (ex, sy, pz), b, segs=28, parent=root)
    for k, s in enumerate((1.0, 0.8, 0.65, 0.5, 0.4)):    # stepped brass weights in a row
        lathe(f"Balance_Weight_{k}", [(0.016 * s, 0), (0.016 * s, 0.03 * s), (0.008 * s, 0.033 * s),
                                      (0.008 * s, 0.04 * s), (0.011 * s, 0.045 * s), (0.0005, 0.048 * s)],
              (sx - 0.12 + k * 0.035, sy + 0.06, top), b, segs=16, parent=root)
    # Wooden specimen tray with 12 cells of tumbled stones and two quartz points.
    tx, ty = -0.12, -0.12
    tray = wood(1.5, 0.5)
    box("Tray_Base", (0.33, 0.23, 0.01), (tx, ty, h + 0.005), tray, parent=root)
    walls = [((0.33, 0.008, 0.035), (tx, ty + sy_ * 0.111, h + 0.0175), (0, 0, 0)) for sy_ in (-1, 1)]
    walls += [((0.008, 0.23, 0.035), (tx + sx_ * 0.161, ty, h + 0.0175), (0, 0, 0)) for sx_ in (-1, 1)]
    walls += [((0.005, 0.22, 0.028), (tx - 0.165 + 0.0825 * k, ty, h + 0.014), (0, 0, 0)) for k in (1, 2, 3)]
    walls += [((0.32, 0.005, 0.028), (tx, ty - 0.115 + 0.0767 * k, h + 0.014), (0, 0, 0)) for k in (1, 2)]
    boxes("Tray_Dividers", walls, tray, bevel=0.0015, parent=root)
    stone_keys = ("accent_3", "accent_2", "cream", "plant", "main", "wax", "amber", "tile_dark", "accent_1")
    for i in range(4):
        for j in range(3):
            m = surface(mat("stone", 0.25, color=mix_hex(COLORS[stone_keys[(i * 3 + j) % len(stone_keys)]],
                                                         "#FFFFFF", 0.2)), "marble")
            cx, cy = tx - 0.124 + i * 0.0825, ty - 0.077 + j * 0.0767
            for s in range(3):
                ball(f"Tray_Stone_{i}{j}{s}", random.uniform(0.011, 0.015), (cx + random.uniform(-0.018, 0.018),
                     cy + random.uniform(-0.016, 0.016), h + 0.018), m, scale=(1.25, 1, 0.65), segs=12,
                     rot=(0, 0, random.uniform(0, 3)), parent=root)
    crystal("Counter_Quartz", (tx + 0.24, ty + 0.03, h), 0.02, 0.14, glass("#F2F6FF", 0.6, emit=0.15), parent=root)
    cluster("Counter_Amethyst", (tx + 0.26, ty + 0.13, h), "main", n=7, size=1.1, parent=root)
    # Crystal ball on a brass stand = your EMAIL link (a real 13 cm clear quartz sphere).
    cx = 0.32
    lathe("Crystal_Stand", [(0.05, 0), (0.052, 0.006), (0.035, 0.012), (0.03, 0.03), (0.042, 0.04), (0.038, 0.045)],
          (cx, 0.0, h), b, segs=28, parent=root)
    orb = ball("Crystal_Ball", 0.065, (cx, 0.0, h + 0.105), glass(COLORS["accent_3"], 0.55, 0.02, emit=0.5),
               segs=32, parent=root)
    hook_link(orb, "email")
    no_shadow(orb)
    no_shadow(ball("Crystal_Mist", 0.032, (cx + 0.01, -0.01, h + 0.1), glow(COLORS["moon"], 1.5), segs=16,
                   parent=root))
    light("Light_Crystal", "POINT", 3, lin(COLORS["accent_3"]), (cx, -0.15, h + 0.15), size=0.05, parent=root)
    # A sealed parchment scroll = your LINKEDIN link.
    scroll = cyl("Scroll", 0.022, 0.26, (0.56, -0.17, h + 0.022), paper(0.93), segs=20, bevel=0.004,
                 rot=(0, R(90), R(-12)), parent=root)
    hook_link(scroll, "linkedin")
    cyl("Scroll_Ribbon", 0.024, 0.02, (0.56, -0.17, h + 0.022), mat("wax", 0.6), segs=20, bevel=0.002,
        rot=(0, R(90), R(-12)), parent=root)
    cyl("Scroll_Seal", 0.016, 0.006, (0.552, -0.193, h + 0.024), mat("wax", 0.35), segs=16, bevel=0.002,
        rot=(R(90), 0, R(-12)), parent=root)
    # Service bell, two stoppered jars at the back and a pillar candle.
    lathe("Bell_Base", [(0.04, 0), (0.04, 0.012), (0.034, 0.016)], (0.78, -0.2, h), mat("dark", 0.4), segs=24,
          parent=root)
    lathe("Bell_Dome", [(0.034, 0), (0.033, 0.012), (0.026, 0.032), (0.012, 0.042), (0.0005, 0.044)],
          (0.78, -0.2, h + 0.016), b, segs=28, parent=root)
    cyl("Bell_Plunger", 0.004, 0.014, (0.78, -0.2, h + 0.065), b, segs=8, bevel=0, parent=root)
    for k, fk in enumerate((HERB_FILLS[2], HERB_FILLS[1])):
        shop_jar(f"Counter_Jar_{k}", 0.05 + k * 0.14, 0.2, h, 0.05, 0.2, fk, root)
    pillar_candle("Candle_Counter", (0.36, 0.22, h), 0.18, 0.035, parent=root, glow_light=True)
    # Brass yard measure let into the front edge of the top: the signature of a real haberdashery counter.
    box("Counter_Measure", (0.92, 0.014, 0.0012), (0.0, -d / 2 - 0.004, h + 0.0004), b, bevel=0, parent=root)
    boxes("Counter_MeasureTicks", [((0.0015, 0.006, 0.0008), (-0.46 + k * 0.0254 * 4, -d / 2 - 0.008, h + 0.001),
                                    (0, 0, 0)) for k in range(10)], mat("dark", 0.5), bevel=0, parent=root)
    # Antique brass cash register (ornate 1900s shop till, ~30 x 32 x 36 cm): drawer, sloped key bank, top display.
    rx, ry = 0.62, 0.07
    reg = brass(0.32)
    box("Till_Drawer", (0.3, 0.32, 0.08), (rx, ry, h + 0.04), mah(1.1), bevel=0.005, parent=root)
    box("Till_DrawerPull", (0.08, 0.012, 0.012), (rx, ry - 0.166, h + 0.045), reg, bevel=0.003, parent=root)
    box("Till_Body", (0.28, 0.18, 0.2), (rx, ry + 0.06, h + 0.18), reg, bevel=0.008, parent=root)
    tilt = R(35)
    box("Till_KeyBed", (0.28, 0.16, 0.03), (rx, ry - 0.08, h + 0.13), reg, bevel=0.006, rot=(tilt, 0, 0),
        parent=root)
    keys = []
    for r_ in range(3):
        for c in range(7):
            v = Vector((-0.11 + c * 0.0367, -0.05 + r_ * 0.045, 0.02))
            v.rotate(Euler((tilt, 0, 0)))
            keys.append(((0.018, 0.018, 0.012), (rx + v.x, ry - 0.08 + v.y, h + 0.13 + v.z), (tilt, 0, 0)))
    boxes("Till_Keys", keys, surface(mat("cream", 0.3, color=shade(COLORS["cream"], 1.05)), "ceramic"), bevel=0.004,
          parent=root)
    box("Till_Display", (0.2, 0.06, 0.08), (rx, ry + 0.06, h + 0.32), reg, bevel=0.006, parent=root)
    box("Till_Window", (0.15, 0.004, 0.04), (rx, ry + 0.028, h + 0.32), mat("dark", 0.2), bevel=0, parent=root)
    lathe("Till_Crest", [(0.05, 0), (0.05, 0.01), (0.02, 0.03), (0.006, 0.05), (0.0005, 0.055)], (rx, ry + 0.06, h + 0.36),
          reg, segs=6, scale=(1, 0.3, 1), parent=root)
    tube("Till_Crank", [(rx + 0.14, ry + 0.06, h + 0.18), (rx + 0.18, ry + 0.06, h + 0.18), (rx + 0.18, ry - 0.02,
                        h + 0.12)], 0.006, reg, parent=root)
    ball("Till_CrankKnob", 0.012, (rx + 0.18, ry - 0.02, h + 0.12), mat("dark", 0.4), segs=10, parent=root)


def build_display_case():
    """Victorian oak chemist's display cabinet: drawer base, glazed doors and sides, glass shelves, crystals."""
    root, w, d, h = furniture_root("display_case")
    oak, oak_z = wood(1.25, 0.4), wood(1.25, 0.4, along="Z")
    BASE = 0.42
    box("Case_Plinth", (w - 0.04, d - 0.04, 0.08), (0, 0.01, 0.04), wood(0.6, 0.6), parent=root)
    box("Case_Base", (w, d, BASE - 0.08), (0, 0, 0.08 + (BASE - 0.08) / 2), oak_z, parent=root)
    for sx in (-1, 1):
        box("Case_Drawer", (w / 2 - 0.04, 0.018, 0.13), (sx * w / 4, -d / 2 - 0.009, BASE - 0.1), oak, parent=root)
        ball("Case_Knob", 0.012, (sx * w / 4, -d / 2 - 0.024, BASE - 0.1), brass(), segs=12, parent=root)
        box("Case_Panel", (w / 2 - 0.06, 0.012, 0.13), (sx * w / 4, -d / 2 - 0.006, 0.17), oak, bevel=0.008,
            parent=root)
    box("Case_Waist", (w + 0.02, d + 0.02, 0.03), (0, -0.005, BASE + 0.015), oak, bevel=0.005, parent=root)
    G0, G1 = BASE + 0.03, h - 0.09
    box("Case_Back", (w - 0.04, 0.015, G1 - G0), (0, d / 2 - 0.0075, (G0 + G1) / 2), wood(0.55, 0.6, along="Z",
        kind="veneer"), bevel=0, parent=root)
    posts = [((0.035, 0.035, G1 - G0), (sx * (w / 2 - 0.0175), sy * (d / 2 - 0.0175), (G0 + G1) / 2), (0, 0, 0))
             for sx in (-1, 1) for sy in (-1, 1)]
    boxes("Case_Posts", posts, oak_z, parent=root)
    pane = glass("#EEF4F2", 0.05, 0.02)                  # clear window glass, barely tinted
    for sx in (-1, 1):                                   # glass side panels
        no_shadow(box("Case_SideGlass", (0.004, d - 0.07, G1 - G0 - 0.02), (sx * (w / 2 - 0.0175), 0, (G0 + G1) / 2),
                      pane, bevel=0, parent=root))
    for sx in (-1, 1):                                   # two glazed doors
        dx = sx * (w / 4 - 0.004)
        dw = w / 2 - 0.035
        door = [((0.035, 0.022, G1 - G0), (dx - dw / 2 + 0.0175, -d / 2 + 0.011, (G0 + G1) / 2), (0, 0, 0)),
                ((0.035, 0.022, G1 - G0), (dx + dw / 2 - 0.0175, -d / 2 + 0.011, (G0 + G1) / 2), (0, 0, 0)),
                ((dw, 0.022, 0.05), (dx, -d / 2 + 0.011, G0 + 0.025), (0, 0, 0)),
                ((dw, 0.022, 0.04), (dx, -d / 2 + 0.011, G1 - 0.02), (0, 0, 0))]
        boxes("Case_Door", door, oak_z, bevel=0.003, parent=root)
        no_shadow(box("Case_DoorGlass", (dw - 0.06, 0.004, G1 - G0 - 0.08), (dx, -d / 2 + 0.012, (G0 + G1) / 2 + 0.005),
                      pane, bevel=0, parent=root))
        box("Case_Escutcheon", (0.012, 0.004, 0.03), (dx - sx * (dw / 2 - 0.0175), -d / 2 - 0.002, (G0 + G1) / 2),
            brass(), bevel=0.001, parent=root)
    for i, (dw_, dd, hh) in enumerate(((0.02, 0.02, 0.03), (0.05, 0.04, 0.025), (0.08, 0.06, 0.035))):
        box(f"Case_Cornice_{i}", (w + dw_, d + dd, hh), (0, -dd / 2 + 0.01 * i, G1 + 0.005 + i * 0.028 + hh / 2), oak,
            bevel=0.005, parent=root)
    shelf_z = [G0, 0.85, 1.2]
    sg, edge = glass("#E2EEEA", 0.12, 0.02), glass("#5E9C84", 0.7, 0.05)    # float glass: clear face, green edge
    for z in shelf_z[1:]:
        no_shadow(box("Case_Shelf", (w - 0.08, d - 0.07, 0.008), (0, 0.0, z), sg, bevel=0.001, parent=root))
        no_shadow(box("Case_ShelfEdge", (w - 0.08, 0.003, 0.008), (0, -(d - 0.07) / 2 - 0.0015, z), edge, bevel=0,
                      parent=root))
        for sx in (-1, 1):                               # brass shelf studs
            for sy in (-1, 1):
                ball("Case_ShelfStud", 0.005, (sx * (w / 2 - 0.042), sy * (d / 2 - 0.06), z - 0.007), brass(),
                     segs=8, parent=root)
    # Crystals: amethyst and quartz clusters, rose quartz, a selenite tower and a split geode on each level.
    for li, z in enumerate(shelf_z):
        zb = z + (0.004 if li else 0.0)
        cluster(f"Case_Cluster_{li}", (-w / 4, 0.02, zb), ("main", "moon", "accent_2")[li], n=7, parent=root)
        crystal(f"Case_Point_{li}", (0.02, -0.03, zb), 0.016, 0.12, glass("#F0F4FF", 0.55, emit=0.2), parent=root)
        if li == 1:
            lathe("Case_Selenite", [(0.022, 0), (0.022, 0.16), (0.0005, 0.2)], (w / 4 + 0.05, 0.03, zb),
                  glass("#FFF8EE", 0.8, emit=0.3), segs=6, parent=root)
        else:
            ball(f"Case_RoseQuartz_{li}", 0.04, (w / 4 + 0.04, 0.0, zb + 0.025),
                 glass(mix_hex(COLORS["accent_2"], "#FFFFFF", 0.5), 0.8, 0.2, emit=0.15), scale=(1.2, 1, 0.7),
                 segs=12, parent=root)
        if li == 0:                                           # an amethyst geode half, open face forward
            lathe("Case_Geode", [(0.0005, 0), (0.07, 0.01), (0.09, 0.05), (0.075, 0.09), (0.06, 0.09),
                                 (0.0005, 0.06)], (0.05, 0.05, zb + 0.09), surface(mat("metal", 0.8, color="#6A6A6A"),
                                                                                   "concrete"),
                  segs=20, rot=(R(-80), 0, 0), parent=root)
            for k in range(9):
                a = k * 0.7
                crystal("Case_GeodeTooth", (0.05 + math.cos(a) * 0.04, 0.0, zb + 0.09 + math.sin(a) * 0.04), 0.008,
                        0.025, glass(COLORS["main"], 0.8, emit=0.25), tilt=(90, 0), parent=root)
    # Top shelf: two amber bottles behind the rose quartz.
    for k in range(2):
        amber_bottle(f"Case_Bottle_{k}", w / 4 - 0.06 + k * 0.08, 0.1, shelf_z[2] + 0.004, 0.9, root)
    light("Light_Case", "POINT", 4, kelvin(3600), (0, -0.05, G1 - 0.06), size=0.12, parent=root)
    # On top: a stack of old books and a pillar candle.
    for k in range(3):
        box("Case_TopBook", (0.26 - k * 0.02, 0.19, 0.04), (w / 4 - 0.05, 0.0, h + 0.02 + k * 0.04),
            surface(mat("book", 0.7, color=(COLORS["wax"], COLORS["wall_trim"], shade(COLORS["wood"], 1.4))[k]),
                    "leather"), bevel=0.004, rot=(0, 0, R(random.uniform(-8, 8))), parent=root)
    pillar_candle("Candle_Case", (-w / 4, 0.0, h), 0.13, 0.032, parent=root)


def build_wall_shelf():
    """Deep oak plank shelf on cast-iron brackets with three big stoppered jars (skill labels) and amber bottles."""
    root, w, d, h = furniture_root("wall_shelf")
    box("WallShelf_Plank", (w, d, 0.03), (0, 0, 0.045), wood(1.3, 0.42), parent=root)
    ir = iron()
    for sx in (-1, 1):
        bx = sx * (w / 2 - 0.12)
        box("WallShelf_BracketTop", (0.012, d - 0.03, 0.02), (bx, 0.015, 0.02), ir, bevel=0.003, parent=root)
        box("WallShelf_BracketWall", (0.012, 0.02, 0.2), (bx, d / 2 - 0.01, -0.07), ir, bevel=0.003, parent=root)
        tube("WallShelf_Scroll", arc_pts((bx, d / 2 - 0.02, 0.01), 0.16, 180, 270, 10, plane="YZ"), 0.006, ir,
             parent=root)
    for k in range(3):                                   # skill jars with paper labels
        jx = -w / 2 + 0.16 + k * (w - 0.32) / 2
        shop_jar(f"WallShelf_Jar_{k}", jx, 0.0, 0.06, 0.065, 0.24, HERB_FILLS[(2, 3, 0)[k]], root,
                 with_label=False)
        box(f"WallShelf_Label_{k}", (0.13, 0.002, 0.065), (jx, -0.067, 0.17), paper(0.97), bevel=0, parent=root)
        hook_text("skill", k + 1, ("Herbs", "Hexes", "Tonics")[k], 0.036, (jx, -0.069, 0.17),
                  material=mat("ink", 0.6, color=shade(COLORS["wood"], 0.5)), max_width=0.115, parent=root,
                  depth=0.002)
    for k, x in enumerate((-w / 2 + 0.035, w / 2 - 0.035)):
        amber_bottle(f"WallShelf_Bottle_{k}", x, 0.02, 0.06, 0.9, root)


def herb_bundle(name, x, y, z, kind, parent, length):
    """A bundle of dried herbs hanging head-down: twine loop, tie, stems and leaves or flower spikes."""
    twine = mat("twine", 0.9, color=shade(COLORS["cream"], 0.8))
    tube(f"{name}_Loop", [(x, y - 0.014, z - 0.05), (x, y - 0.016, z), (x, y, z + 0.016), (x, y + 0.016, z),
                          (x, y + 0.014, z - 0.05)], 0.002, twine, segs=5, parent=parent)
    tie = z - 0.055
    cyl(f"{name}_Tie", 0.011, 0.012, (x, y, tie), twine, segs=10, bevel=0.002, parent=parent)
    stem_col = mat("stem", 0.9, color=mix_hex(COLORS["plant"], COLORS["wood"], 0.5))
    stems = []
    for k in range(9):
        a = k * 0.7
        sp = random.uniform(0.006, 0.02)
        stems.append(((0.003, 0.003, length * 0.55), (x + math.cos(a) * sp * 0.5, y + math.sin(a) * sp * 0.5,
                                                       tie + 0.01 - length * 0.27), (math.sin(a) * 0.08, math.cos(a) * 0.08, 0)))
    boxes(f"{name}_Stems", stems, stem_col, bevel=0, parent=parent)
    cols = {"lavender": mix_hex(COLORS["main"], COLORS["cream"], 0.25), "sage": mix_hex(COLORS["plant"], "#A9B09A", 0.35),
            "rosemary": shade(COLORS["plant"], 0.62), "yarrow": mix_hex(COLORS["cream"], COLORS["amber"], 0.25)}
    m = surface(mat("herb", 0.9, color=cols[kind]), "fabric", scale=0.2)
    if kind in ("lavender", "yarrow"):                 # stems first, then flower heads at the bottom
        for k in range(34):
            a = random.uniform(0, 2 * math.pi)
            sp = 0.008 + 0.04 * random.random() ** 0.7
            zz = tie - length * random.uniform(0.7, 1.0)
            if kind == "lavender":
                ball(f"{name}_Spike", 0.0065, (x + math.cos(a) * sp, y + math.sin(a) * sp, zz), m, scale=(1, 1, 5),
                     segs=8, parent=parent)
            else:
                ball(f"{name}_Head", 0.013, (x + math.cos(a) * sp, y + math.sin(a) * sp, zz), m, scale=(1, 1, 0.6),
                     segs=8, parent=parent)
    else:                                              # leafy herbs: a dense cone of leaves widening downwards
        for k in range(44):
            t = random.uniform(0.15, 1.0)
            a = random.uniform(0, 2 * math.pi)
            sp = (0.008 + 0.05 * t) * random.uniform(0.6, 1.0)
            ball(f"{name}_Leaf", 0.016 if kind == "sage" else 0.011,
                 (x + math.cos(a) * sp, y + math.sin(a) * sp, tie - 0.02 - length * t), m,
                 scale=(0.8, 0.3, 2.4), segs=8, rot=(math.sin(a) * 0.5, -math.cos(a) * 0.5, a), parent=parent)


def build_hanging_plant():
    """Sheila Maid pulley airer (cast-iron ends, four pine laths) used as a herb drying rack, roped to a wall cleat."""
    root, w, d, h = furniture_root("hanging_plant")
    ir, pine = iron(), wood(1.9, 0.6, key="wood")
    LZ = 0.5                                             # lath height
    lath_y = (-0.135, -0.045, 0.045, 0.135)
    for ly in lath_y:
        cyl("Airer_Lath", 0.013, w, (0, ly, LZ), pine, rot=(0, R(90), 0), segs=14, bevel=0.002, parent=root)
    for ex in (-w / 2 + 0.08, w / 2 - 0.08):            # the two cast-iron ends
        tube("Airer_End_Bar", [(ex, -0.18, LZ), (ex, 0.18, LZ)], 0.008, ir, parent=root)
        arch = [(ex, 0.18 * math.cos(R(a)), LZ + 0.1 * math.sin(R(a))) for a in range(180, -1, -15)]
        tube("Airer_End_Arch", arch, 0.007, ir, parent=root)            # low cast arch over the four lath eyes
        for ly in lath_y:
            ring("Airer_End_Eye", 0.018, 0.005, (ex, ly, LZ), ir, rot=(0, R(90), 0), segs=16, parent=root)
        for sy in (-1, 1):                                              # scroll ornaments inside the arch
            ring("Airer_End_Scroll", 0.025, 0.004, (ex, sy * 0.07, LZ + 0.05), ir, rot=(0, R(90), 0), segs=16,
                 parent=root)
        ring("Airer_End_Top", 0.015, 0.005, (ex, 0, LZ + 0.115), ir, rot=(0, R(90), 0), segs=16, parent=root)
        # Rope up to a pulley on an iron bracket that comes out of the wall (local +y = towards the wall).
        rope = mat("twine", 0.95, color=shade(COLORS["cream"], 0.85))
        tube("Airer_Rope", [(ex, 0, LZ + 0.13), (ex, 0, 0.78)], 0.004, rope, segs=6, parent=root)
        box("Airer_WallArm", (0.02, 0.44, 0.02), (ex, 0.2, 0.83), ir, bevel=0.003, parent=root)
        box("Airer_WallPlate", (0.06, 0.01, 0.1), (ex, 0.415, 0.83), ir, bevel=0.002, parent=root)
        ring("Airer_Pulley", 0.025, 0.006, (ex, 0, 0.8), ir, rot=(0, R(90), 0), segs=16, parent=root)
    # The rope runs along the arms, then down the wall to a cleat beside the window.
    ex0 = -w / 2 + 0.08
    tube("Airer_RopeRun", [(w / 2 - 0.08, 0.405, 0.81), (ex0, 0.405, 0.81), (ex0 - 0.04, 0.405, 0.7),
                           (ex0 - 0.04, 0.405, -0.42)], 0.004, mat("twine", 0.95, color=shade(COLORS["cream"], 0.85)),
         segs=6, parent=root)
    box("Airer_Cleat", (0.1, 0.02, 0.02), (ex0 - 0.04, 0.4, -0.45), brass(), bevel=0.005, parent=root)
    # Dried herb bundles hanging head-down from the laths.
    kinds = ("lavender", "sage", "rosemary", "yarrow")
    n = 16                                               # a well-stocked rack: a bundle every 7 cm
    for k in range(n):
        bx = -w / 2 + 0.2 + k * (w - 0.4) / (n - 1)
        ly = lath_y[k % 2 * 3 if k % 4 < 2 else 1 + k % 2]
        herb_bundle(f"Herbs_{k}", bx, ly, LZ - 0.013, random.choice(kinds) if k > 1 else kinds[k], root,
                    random.uniform(0.34, 0.46))


def build_hero_prop():
    """Cast-iron handled cauldron hung by a chain from a three-legged camp tripod, warm brew, candles beneath."""
    root, w, d, h = furniture_root("hero_prop")
    ir = iron()
    TOP = h - 0.03
    feet = [(math.cos(R(a)) * 0.5, math.sin(R(a)) * 0.5, 0.0) for a in (90, 210, 330)]
    for k, f in enumerate(feet):
        tube(f"Tripod_Leg_{k}", [f, (f[0] * 0.04, f[1] * 0.04, TOP - 0.02), (-f[0] * 0.05, -f[1] * 0.05, TOP + 0.02)],
             0.011, ir, parent=root)
        box(f"Tripod_Foot_{k}", (0.04, 0.04, 0.008), (f[0], f[1], 0.004), ir, bevel=0.002, parent=root)
    ring("Tripod_Collar", 0.022, 0.008, (0, 0, TOP - 0.03), ir, segs=16, parent=root)
    POT_Z = 0.22                                       # bottom of the pot
    RIM = POT_Z + 0.3
    BAIL = RIM + 0.2
    z = TOP - 0.05
    k = 0
    while z > BAIL + 0.05:                             # chain of alternating links
        ring(f"Chain_Link_{k}", 0.016, 0.0035, (0, 0, z), ir, rot=(R(90), 0, R(90 * (k % 2))), segs=12, parent=root)
        z -= 0.026
        k += 1
    tube("Chain_SHook", [(0, 0, z + 0.02), (0.015, 0, z + 0.005), (0, 0, z - 0.01), (-0.015, 0, z - 0.025),
                         (0, 0, BAIL - 0.004)], 0.004, ir, parent=root)
    pot = iron(0.75)
    lathe("Cauldron_Pot", [(0.06, 0), (0.12, 0.012), (0.17, 0.05), (0.19, 0.11), (0.188, 0.17), (0.172, 0.23),
                           (0.155, 0.27), (0.152, 0.285), (0.168, 0.295), (0.17, 0.3), (0.155, 0.302), (0.142, 0.285),
                           (0.155, 0.23), (0.16, 0.15), (0.13, 0.06), (0.0005, 0.03)], (0, 0, POT_Z), pot, segs=40,
          parent=root)
    for a in (90, 210, 330):                           # three stub feet cast on the base
        cyl("Cauldron_Foot", 0.016, 0.05, (math.cos(R(a)) * 0.1, math.sin(R(a)) * 0.1, POT_Z - 0.012), pot, r2=0.011,
            segs=10, parent=root)
    for side in (-1, 1):
        ring("Cauldron_Lug", 0.016, 0.006, (side * 0.163, 0, RIM - 0.02), pot, rot=(R(90), 0, 0), segs=14,
             parent=root)
    tube("Cauldron_Bail", arc_pts((0, 0, RIM - 0.02), 0.163, 0, 180, 18, plane="XZ")[:1] +
         [(math.cos(R(a)) * 0.163, 0, RIM - 0.02 + math.sin(R(a)) * (BAIL - RIM + 0.02)) for a in range(10, 171, 10)] +
         [(-0.163, 0, RIM - 0.02)], 0.005, ir, parent=root)
    brew_m = mat("accent_1", 0.08, emit=0.35, color=mix_hex(COLORS["accent_1"], COLORS["dark"], 0.55))  # herbal brew
    no_shadow(cyl("Cauldron_Brew", 0.152, 0.01, (0, 0, POT_Z + 0.262), brew_m, segs=40, bevel=0, parent=root))
    for k, (bx, by, br) in enumerate([(0.06, -0.05, 0.022), (-0.07, 0.03, 0.016), (0.0, 0.08, 0.012)]):
        no_shadow(ball(f"Cauldron_Bubble_{k}", br, (bx, by, POT_Z + 0.266), mat("accent_1", 0.1, emit=0.9),
                       scale=(1, 1, 0.5), segs=12, parent=root))
    for k in range(5):                                 # floating herb leaves
        a = random.uniform(0, 6.28)
        ball("Cauldron_Leaf", 0.014, (math.cos(a) * 0.09, math.sin(a) * 0.09, POT_Z + 0.268), mat("plant", 0.8),
             scale=(1, 0.5, 0.15), rot=(0, 0, a), segs=8, parent=root)
    spoon = wood(1.5, 0.6, along="Z")
    tube("Cauldron_Spoon", [(0.06, 0.04, POT_Z + 0.2), (0.2, 0.14, POT_Z + 0.62)], [0.012, 0.01], spoon, parent=root)
    ball("Cauldron_SpoonBowl", 0.03, (0.05, 0.035, POT_Z + 0.2), spoon, scale=(1, 0.5, 1.3), segs=12, parent=root)
    # Slate hearth plate with three pillar candles keeping the brew warm.
    box("Hearth_Slate", (0.56, 0.56, 0.02), (0, 0, 0.01), surface(mat("tile_dark", 0.5, color=shade(COLORS["tile_dark"],
        1.25)), "concrete"), bevel=0.004, rot=(0, 0, R(15)), parent=root)
    for k, a in enumerate((30, 150, 270)):
        pillar_candle(f"Candle_Hearth_{k}", (math.cos(R(a)) * 0.09, math.sin(R(a)) * 0.09, 0.02), 0.1, 0.03,
                      parent=root, plate=False)
    light("Light_Cauldron", "POINT", CAULDRON_GLOW, lin(mix_hex(COLORS["accent_1"], "#FFFFFF", 0.3)),
          (0, -0.12, RIM + 0.45), size=0.3, parent=root)
    light("Light_Hearth", "POINT", 6, kelvin(LAMP_WARMTH), (0, -0.2, 0.15), size=0.08, parent=root)


def build_armchair():
    """IKEA STRANDMON-style wing chair: splayed legs, upholstered base, loose seat cushion, rolled arms, wings."""
    root, w, d, h = furniture_root("armchair")
    fab, fab_lt = cloth("main"), cloth("main", 1.12)
    leg = wood(0.55, 0.35, along="Z")
    for sx in (-1, 1):
        for sy in (-1, 1):
            top = (sx * (w / 2 - 0.08), sy * (d / 2 - 0.12), 0.18)
            tube("Armchair_Leg", [(top[0] + sx * 0.02, top[1] + sy * 0.03 * (sy > 0), 0.0), top], [0.016, 0.022], leg,
                 segs=12, parent=root)
    box("Armchair_Base", (w - 0.04, d - 0.18, 0.2), (0, -0.04, 0.27), fab, bevel=0.025, parent=root)
    box("Armchair_Cushion", (0.5, 0.58, 0.1), (0, -0.1, 0.42), fab_lt, bevel=0.03, parent=root)
    box("Armchair_CushionPiping", (0.505, 0.585, 0.008), (0, -0.1, 0.42), fab, bevel=0.003, parent=root)
    for sx in (-1, 1):
        ax = sx * (w / 2 - 0.08)
        box("Armchair_ArmPanel", (0.13, d - 0.26, 0.36), (ax, -0.05, 0.44), fab, bevel=0.02, parent=root)
        cyl("Armchair_ArmRoll", 0.065, d - 0.24, (ax + sx * 0.01, -0.06, 0.63), fab, segs=24, bevel=0.012,
            rot=(R(90), 0, 0), parent=root)
        cyl("Armchair_ArmFace", 0.066, 0.012, (ax + sx * 0.01, -d / 2 + 0.065, 0.63), fab_lt, segs=24, bevel=0.004,
            rot=(R(90), 0, 0), parent=root)
        box("Armchair_ArmFront", (0.13, 0.03, 0.3), (ax, -d / 2 + 0.075, 0.45), fab_lt, bevel=0.012, parent=root)
        # The wing: one curved panel that sweeps from the arm roll up and back to the top of the backrest.
        wing = [(d / 2 - 0.1, 0.6), (d / 2 - 0.1, h - 0.03), (d / 2 - 0.24, h), (d / 2 - 0.36, h - 0.04),
                (d / 2 - 0.45, h - 0.12), (d / 2 - 0.52, h - 0.24), (d / 2 - 0.56, 0.6)]
        bm = bmesh.new()
        face = bm.faces.new([bm.verts.new((-0.05, y, z)) for y, z in wing])
        ext = bmesh.ops.extrude_face_region(bm, geom=[face])
        bmesh.ops.translate(bm, vec=(0.1, 0, 0), verts=[v for v in ext["geom"] if isinstance(v, bmesh.types.BMVert)])
        bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
        wo = _finish(_obj("Armchair_Wing", bm), fab, 0.03, None, root)
        wo.location, wo.rotation_euler = (ax + sx * 0.012, 0, 0), (0, 0, R(-sx * 5))
    box("Armchair_Back", (w - 0.16, 0.16, 0.68), (0, d / 2 - 0.14, 0.72), fab, bevel=0.04, rot=(R(-10), 0, 0),
        parent=root)
    box("Armchair_BackCushion", (w - 0.3, 0.1, 0.5), (0, d / 2 - 0.25, 0.7), fab_lt, bevel=0.035, rot=(R(-12), 0, 0),
        parent=root)
    # A chunky knit throw over one arm (a separate soft part).
    throw = cloth("amber", 1.5, kind="knit")
    tx = w / 2 - 0.07                                    # folded throw: lies over the arm roll, hangs down the side
    box("Armchair_Throw", (0.15, 0.36, 0.02), (tx - 0.01, -0.12, 0.703), throw, bevel=0.008, rot=(0, R(8), 0),
        parent=root)
    cyl("Armchair_ThrowFold", 0.024, 0.36, (tx + 0.065, -0.12, 0.68), throw, segs=16, bevel=0.004,
        rot=(R(90), 0, 0), parent=root)
    box("Armchair_ThrowDrop", (0.02, 0.36, 0.28), (tx + 0.085, -0.12, 0.53), throw, bevel=0.008, rot=(0, R(-4), 0),
        parent=root)
    boxes("Armchair_ThrowTassels", [((0.008, 0.008, 0.04), (tx + 0.088, -0.29 + k * 0.034, 0.375), (0, 0, 0))
                                    for k in range(11)], throw, bevel=0, parent=root)


def build_rug():
    """Vintage Turkish kilim: banded border, three stepped diamond medallions, warp fringes at both ends."""
    root, w, d, h = furniture_root("rug")
    red = cloth("wax", 1.15)
    navy = cloth("wall_trim", 0.9)
    ivory = cloth("cream", 0.95)
    ochre = cloth("amber", 1.35)
    box("Rug_Ground", (w, d, h * 0.5), (0, 0, h * 0.25), red, bevel=0.002, parent=root)
    band = [((w - 0.06, 0.07, h * 0.2), (0, sy * (d / 2 - 0.08), h * 0.55), (0, 0, 0)) for sy in (-1, 1)]
    band += [((0.07, d - 0.09, h * 0.2), (sx * (w / 2 - 0.08), 0, h * 0.55), (0, 0, 0)) for sx in (-1, 1)]
    boxes("Rug_Border", band, navy, bevel=0, parent=root)
    small = [((0.045, 0.045, h * 0.2), (x, sy * (d / 2 - 0.08), h * 0.65), (0, 0, R(45)))
             for sy in (-1, 1) for x in [-w / 2 + 0.16 + i * 0.12 for i in range(int((w - 0.3) / 0.12))]]
    boxes("Rug_BorderMotifs", small, ivory, bevel=0, parent=root)
    STEP = 0.04                                                    # kilims weave diamonds as stepped stripes
    for k, mx in enumerate((-w / 3 + 0.05, 0, w / 3 - 0.05)):
        for j, (n_, m) in enumerate(((13, navy), (10, ivory), (7, ochre), (4, red), (1, ivory))):
            rows = [((STEP * 0.7 * (2 * (n_ - abs(r_)) + 1), STEP, h * 0.2), (mx, r_ * STEP, h * (0.55 + 0.1 * j)),
                     (0, 0, 0)) for r_ in range(-n_, n_ + 1)]
            boxes(f"Rug_Lozenge_{k}_{j}", rows, m, bevel=0, parent=root)
        for sx in (-1, 1):                                         # hooked arms off the sides
            for r_ in (-1, 1):
                box(f"Rug_Hook_{k}", (0.05, STEP, h * 0.2), (mx + sx * (STEP * 0.7 * 13.5 + 0.03), r_ * STEP * 2,
                    h * 0.6), ivory, bevel=0, parent=root)
    fringe = [((0.004, 0.045, 0.003), (-w / 2 + 0.02 + i * 0.03, sy * (d / 2 + 0.022), 0.0015), (0, 0, random.uniform(-0.15, 0.15)))
              for sy in (-1, 1) for i in range(int((w - 0.04) / 0.03) + 1)]
    boxes("Rug_Fringe", fringe, ivory, bevel=0, parent=root)


def build_pet():
    """Black domestic shorthair cat sitting with its tail curled round its paws (about 25 cm at the shoulder)."""
    root, w, d, h = furniture_root("pet")
    fur = surface(mat("pet", 0.75), "fabric", scale=0.4)
    ball("Cat_Haunch", 0.1, (0, 0.06, 0.1), fur, scale=(1.05, 1.25, 1.0), parent=root)
    ball("Cat_Chest", 0.075, (0, -0.04, 0.17), fur, scale=(0.95, 0.9, 1.35), parent=root)
    head = Vector((0, -0.07, 0.31))
    ball("Cat_Head", 0.065, head, fur, scale=(1.08, 0.95, 0.9), parent=root)
    ball("Cat_Muzzle", 0.028, head + Vector((0, -0.055, -0.022)), fur, scale=(1.3, 0.8, 0.75), parent=root)
    ball("Cat_Nose", 0.006, head + Vector((0, -0.077, -0.01)), mat("nose", 0.5, color="#3A2A30"), segs=8, parent=root)
    for sx in (-1, 1):
        lathe("Cat_Ear", [(0.026, 0), (0.0005, 0.05)], head + Vector((sx * 0.036, 0.008, 0.042)), fur, segs=12,
              rot=(R(-5), R(sx * 20), 0), scale=(1, 0.45, 1), parent=root)
        no_shadow(ball("Cat_Eye", 0.012, head + Vector((sx * 0.026, -0.058, 0.01)), mat("accent_1", 0.2, emit=1.5),
                       scale=(0.9, 0.4, 0.7), segs=12, parent=root))
        tube("Cat_Foreleg", [(sx * 0.03, -0.07, 0.17), (sx * 0.03, -0.09, 0.03)], [0.02, 0.016], fur, parent=root)
        ball("Cat_Paw", 0.02, (sx * 0.03, -0.105, 0.015), fur, scale=(1, 1.3, 0.75), segs=12, parent=root)
    tube("Cat_Tail", [(0.06, 0.15, 0.03), (0.11, 0.05, 0.02), (0.1, -0.07, 0.018), (0.04, -0.13, 0.018),
                      (-0.03, -0.14, 0.02)], [0.02, 0.019, 0.017, 0.015, 0.012], fur, segs=10, parent=root)


PLACEHOLDERS = {
    "shelf": build_shelf, "counter": build_counter, "display_case": build_display_case,
    "wall_shelf": build_wall_shelf, "hanging_plant": build_hanging_plant, "hero_prop": build_hero_prop,
    "armchair": build_armchair, "rug": build_rug, "pet": build_pet,
}
if SHOW_PLACEHOLDER_FURNITURE:
    for slot_name, build in PLACEHOLDERS.items():
        build()


# =====================================================================
#  PORTFOLIO PIECES  (fascia sign, botanical prints, chalkboard, lectern book)
# =====================================================================
# Gilded fascia sign above the apothecary cabinet: your NAME + ROLE, click = website.
SIGN_X, SIGN_Z, SIGN_W, SIGN_H = 1.1, 2.69, 1.72, 0.38
sign_paint = surface(mat("dark", 0.35, color=shade(COLORS["dark"], 1.1)), "wood")
sign = box("Name_Sign", (SIGN_W, 0.03, SIGN_H), (SIGN_X, D - 0.015, SIGN_Z), sign_paint, bevel=0.006)
hook_link(sign, "website")
gold = mat("brass", 0.3, emit=0.6, metal=0.6)
edge = [((SIGN_W - 0.05, 0.006, 0.012), (SIGN_X, D - 0.033, SIGN_Z + sz * (SIGN_H / 2 - 0.03)), (0, 0, 0)) for sz in (-1, 1)]
edge += [((0.012, 0.006, SIGN_H - 0.05), (SIGN_X + sx * (SIGN_W / 2 - 0.03), D - 0.033, SIGN_Z), (0, 0, 0)) for sx in (-1, 1)]
boxes("Name_Sign_Gilt", edge, gold, bevel=0.0)
box("Name_Sign_Moulding", (SIGN_W + 0.04, 0.04, 0.03), (SIGN_X, D - 0.02, SIGN_Z + SIGN_H / 2 + 0.015), wood(0.7),
    bevel=0.006)
hook_text("name", 1, "YOUR NAME", 0.17, (SIGN_X, D - 0.034, SIGN_Z + 0.045), material=gold, max_width=SIGN_W - 0.3,
          depth=0.004)
hook_text("role", 1, "your role", 0.075, (SIGN_X, D - 0.034, SIGN_Z - 0.105), material=mat("cream", 0.5, emit=0.6),
          max_width=SIGN_W - 0.4, depth=0.003)

# Two framed botanical prints above the counter: projects 2 and 3, with their titles on the mounts.
ink = mat("ink", 0.8, color=shade(COLORS["wood"], 0.55))
frame_oak = wood(0.8, 0.4)
for i, px in enumerate((3.22, 3.98)):
    p = anchor(f"Print_{i + 1}", (px, D, 1.82))
    FW_, FH_, M = 0.52, 0.68, 0.035                    # frame outer size, moulding width
    rails = [((FW_, 0.03, M), (0, -0.015, sz * (FH_ / 2 - M / 2)), (0, 0, 0)) for sz in (-1, 1)]
    rails += [((M, 0.03, FH_ - 2 * M), (sx * (FW_ / 2 - M / 2), -0.015, 0), (0, 0, 0)) for sx in (-1, 1)]
    boxes("Print_Frame", rails, frame_oak, bevel=0.005, parent=p)
    box("Print_Mount", (FW_ - 2 * M, 0.006, FH_ - 2 * M), (0, -0.01, 0), paper(1.02), bevel=0, parent=p)
    ball("Print_Nail", 0.006, (0, -0.004, FH_ / 2 + 0.05), brass(), segs=8, parent=p)
    tube("Print_Wire", [(-0.15, -0.006, FH_ / 2 - 0.06), (0, -0.006, FH_ / 2 + 0.05), (0.15, -0.006, FH_ / 2 - 0.06)],
         0.0012, brass(), segs=4, parent=p)
    hook = hook_image("poster", i + 1, (0.36, 0.46), (0, -0.0135, 0.03), parent=p)
    hook.data.materials[0] = paper(0.92)
    # Projects fill picture hooks as frame_1, poster_1, poster_2, board_1, so the titles are 2 and 3.
    hook_text("title", i + 2, ("Elixir of Focus", "Draught of Dreams")[i], 0.026, (0, -0.0145, -0.245),
              material=ink, max_width=0.34, parent=p, depth=0.0015)
    green = mat("plant", 0.8, color=shade(COLORS["plant"], 0.85))
    petal = mat("print", 0.8, color=(mix_hex(COLORS["main"], COLORS["cream"], 0.35), shade(COLORS["wax"], 1.3))[i])
    drawing = [box("Print_Stem", (0.006, 0.002, 0.34), (0, -0.016, -0.02), green, bevel=0, parent=p)]
    for k in range(4):
        side = -1 if k % 2 else 1
        drawing.append(ball("Print_Leaf", 0.03, (side * 0.035, -0.016, -0.14 + k * 0.07), green, scale=(1.4, 0.05, 0.55),
                            rot=(0, R(side * 30), 0), segs=12, parent=p))
    for k in range(5 + i):
        a = k * 2 * math.pi / (5 + i)
        drawing.append(ball("Print_Petal", 0.03, (math.cos(a) * 0.035, -0.017, 0.17 + math.sin(a) * 0.035), petal,
                            scale=(1.0, 0.05, 0.55), rot=(0, -a, 0), segs=12, parent=p))
    drawing.append(ball("Print_Centre", 0.016, (0, -0.018, 0.17), mat("amber", 0.6), scale=(1, 0.05, 1), segs=10, parent=p))
    hook_default(hook, *drawing)

# Slate chalkboard "TODAY'S BREW" in an oak frame between the cabinet and the counter: project 4.
BX, BZ = 2.43, 1.58
box("Board_Frame", (0.62, 0.035, 0.86), (BX, D - 0.0175, BZ), wood(0.9, 0.45), bevel=0.006)
slate = surface(mat("slate", 0.85, color=mix_hex(COLORS["dark"], COLORS["wall_trim"], 0.3)), "concrete", scale=2)
box("Board_Slate", (0.54, 0.01, 0.78), (BX, D - 0.038, BZ), slate, bevel=0.002)
chalk = mat("chalk", 0.9, emit=0.25, color=shade(COLORS["cream"], 1.05))
deco_text("Board_Title", "TODAY'S BREW", 0.05, (BX, D - 0.044, BZ + 0.31), chalk, max_width=0.44, depth=0.001)
board = hook_image("board", 1, (0.48, 0.36), (BX, D - 0.044, BZ + 0.04))
board.data.materials[0] = slate
for k in range(3):
    box("Board_Chalk_Line", (0.36 - k * 0.08, 0.002, 0.01), (BX, D - 0.044, BZ - 0.21 - k * 0.04), chalk, bevel=0)
hook_default(board,
             ring("Board_Doodle_Pot", 0.09, 0.005, (BX, D - 0.046, BZ + 0.02), chalk, rot=(R(90), 0, 0), segs=32),
             box("Board_Doodle_Rim", (0.22, 0.002, 0.012), (BX, D - 0.046, BZ + 0.11), chalk, bevel=0))
box("Board_Ledge", (0.6, 0.05, 0.02), (BX, D - 0.06, BZ - 0.44), wood(0.9, 0.45), bevel=0.004)
for k in range(2):
    box("Board_Chalk", (0.05, 0.01, 0.01), (BX - 0.1 + k * 0.07, D - 0.065, BZ - 0.425), chalk, bevel=0.003,
        rot=(0, 0, R(10 * k)))

# Oak pedestal lectern with an open herbal: project 1. Turned to face the camera.
lect = anchor("Lectern", (0.98, 0.72, FLOOR_Z), turn=45)
lw, lw_z = wood(1.3, 0.42), wood(1.3, 0.42, along="Z")
for a in (0, 90, 180, 270):                             # cross feet
    box("Lectern_Foot", (0.04, 0.24, 0.05), (math.sin(R(a)) * 0.11, math.cos(R(a)) * 0.11, 0.025), lw,
        rot=(0, 0, R(a)), parent=lect)
lathe("Lectern_Column", [(0.05, 0.05), (0.05, 0.08), (0.035, 0.1), (0.03, 0.3), (0.04, 0.45), (0.03, 0.6),
                         (0.028, 0.85), (0.045, 0.88), (0.045, 0.92)], (0, 0, 0), lw_z, segs=20, parent=lect)
TILT = 30                                               # desk slope in degrees
n = Vector((0, -math.sin(R(TILT)), math.cos(R(TILT))))  # the desk's "up" direction
up = Vector((0, math.cos(R(TILT)), math.sin(R(TILT))))  # up the slope
top = Vector((0, 0.0, 1.0))
box("Lectern_Desk", (0.56, 0.42, 0.022), top, lw, rot=(R(TILT), 0, 0), parent=lect)
box("Lectern_Lip", (0.56, 0.025, 0.04), top - up * 0.2 + n * 0.02, lw, rot=(R(TILT), 0, 0), parent=lect)
box("Lectern_Bracket", (0.06, 0.12, 0.12), (0, 0.0, 0.93), lw, rot=(R(TILT / 2), 0, 0), parent=lect)
box("Book_Cover", (0.6, 0.4, 0.012), top + n * 0.017, surface(mat("main", 0.7, color=shade(COLORS["main"], 0.65)),
    "leather"), bevel=0.004, rot=(R(TILT), 0, 0), parent=lect)
for sx in (-1, 1):                                      # page blocks rise towards the spine like a real open book
    box("Book_Pages", (0.275, 0.37, 0.022), top + Vector((sx * 0.142, 0, 0)) + n * 0.03, paper(0.97),
        bevel=0.008, rot=(R(TILT), R(-sx * 4), 0), parent=lect)
    box("Book_PageEdge", (0.004, 0.37, 0.016), top + Vector((sx * 0.281, 0, 0)) + n * 0.026, paper(0.8),
        bevel=0, rot=(R(TILT), 0, 0), parent=lect)
box("Book_Gutter", (0.012, 0.37, 0.004), top + n * 0.044, mat("ink", 0.9, color=shade(COLORS["cream"], 0.55)), bevel=0,
    rot=(R(TILT), 0, 0), parent=lect)
book = hook_image("frame", 1, (0.5, 0.31), top + n * 0.053, rot=(R(TILT - 90), 0, 0), parent=lect)
book.data.materials[0] = paper(0.95)
doodles = [ring("Book_Circle", 0.055, 0.003, top + n * 0.0545 + Vector((0.13, 0, 0)), ink, rot=(R(TILT), 0, 0), segs=32,
                parent=lect)]
for k in range(6):
    doodles.append(box("Book_Line", (0.17 - 0.04 * (k % 2), 0.008, 0.002),
                       top + n * 0.0545 + Vector((-0.13, 0, 0)) + up * (0.11 - k * 0.042), ink, bevel=0,
                       rot=(R(TILT), 0, 0), parent=lect))
hook_default(book, *doodles)
box("Book_Ribbon", (0.012, 0.004, 0.14), top - up * 0.19 + n * 0.03 + Vector((0.02, -0.02, -0.07)), mat("wax", 0.6),
    bevel=0, parent=lect)


# =====================================================================
#  EXTRA PROPS  (tarot table, besom broom, crates, candles, window sill, seasonal pumpkins)
# =====================================================================
# Tarot reading table: 1920s round walnut pedestal table under a fringed velvet cloth, three-card spread.
tab = anchor("TarotTable", (3.35, 0.62, FLOOR_Z), turn=-20)
TZ = 0.66
lathe("Tarot_Column", [(0.04, 0.05), (0.05, 0.08), (0.03, 0.12), (0.025, 0.4)], (0, 0, 0), wood(1.0, 0.4, along="Z"),
      segs=20, parent=tab)
for a in (90, 210, 330):
    tube("Tarot_Foot", [(0, 0, 0.1), (math.cos(R(a)) * 0.14, math.sin(R(a)) * 0.14, 0.06),
                        (math.cos(R(a)) * 0.22, math.sin(R(a)) * 0.22, 0.01)], [0.025, 0.02, 0.014],
         wood(1.0, 0.4), parent=tab)
velvet = surface(mat("wall_trim", 0.85, color=shade(COLORS["wall_trim"], 1.1)), "fabric")
lathe("Tarot_Cloth", [(0.0005, TZ + 0.004), (0.3, TZ + 0.004), (0.315, TZ - 0.01), (0.36, TZ - 0.12), (0.4, TZ - 0.24),
                      (0.405, TZ - 0.245)], (0, 0, 0), velvet, segs=48, wave=(11, 0.07, True), parent=tab)
fringe = [((0.006, 0.006, 0.04), (math.cos(a) * 0.405 * (1 + 0.07 * math.cos(11 * a)),
           math.sin(a) * 0.405 * (1 + 0.07 * math.cos(11 * a)), TZ - 0.26), (0, 0, a))
          for a in (2 * math.pi * k / 120 for k in range(120))]
boxes("Tarot_Fringe", fringe, mat("brass", 0.6, color=COLORS["brass"]), bevel=0, parent=tab)
card_back = mat("card", 0.6, color=shade(COLORS["main"], 0.6))
for k in range(3):
    box(f"Tarot_Card_{k}", (0.07, 0.12, 0.002), (-0.09 + k * 0.09, -0.04, TZ + 0.006), paper(1.0), bevel=0.001,
        rot=(0, 0, R(random.uniform(-3, 3))), parent=tab)
    box(f"Tarot_CardArt_{k}", (0.054, 0.1, 0.001), (-0.09 + k * 0.09, -0.04, TZ + 0.0075),
        mat("cardart", 0.7, color=(COLORS["wax"], COLORS["wall_trim"], COLORS["amber"])[k]), bevel=0, parent=tab)
for k in range(6):
    box("Tarot_Deck", (0.07, 0.12, 0.004), (0.15, 0.1, TZ + 0.006 + k * 0.004), card_back, bevel=0.001,
        rot=(0, 0, R(18 + k)), parent=tab)
pillar_candle("Candle_Tarot", (-0.14, 0.12, TZ + 0.004), 0.12, 0.03, parent=tab, glow_light=True)
cluster("Tarot_Amethyst", (0.02, 0.14, TZ + 0.004), "main", n=5, size=0.9, parent=tab)

# Seagrass belly basket (36 dia x 29 cm, a floor-size IKEA FLADIS) of dried pampas and eucalyptus.
bk = anchor("Basket", (0.46, 0.24, FLOOR_Z))
weave = surface(mat("seagrass", 0.85, color=mix_hex(COLORS["cream"], "#8C7444", 0.7)), "knit", scale=0.5)
prof = [(0.12, 0), (0.15, 0.03), (0.18, 0.12), (0.17, 0.22), (0.15, 0.27), (0.155, 0.285), (0.14, 0.29), (0.13, 0.27)]
lathe("Basket_Body", prof, (0, 0, 0), weave, segs=40, parent=bk)
coil = surface(mat("seagrass", 0.86, color=mix_hex(COLORS["cream"], "#7A6438", 0.75)), "knit", scale=0.5)
for k in range(1, 14):                                  # the coiled seagrass rope rows that make it read as woven
    zc = k * 0.02
    rc = next(r0 + (r1 - r0) * (zc - z0) / (z1 - z0) for (r0, z0), (r1, z1) in zip(prof, prof[1:]) if z0 <= zc <= z1)
    ring("Basket_Coil", rc, 0.0055, (0, 0, zc), coil, segs=40, parent=bk)
for side in (-1, 1):                                    # two rope handles
    tube("Basket_Handle", arc_pts((side * 0.15, 0, 0.255), 0.035, 0, 180, 8, plane="YZ"), 0.007, coil, parent=bk)
pampas = surface(mat("pampas", 0.95, color=mix_hex(COLORS["cream"], "#C8B48C", 0.5)), "fabric", scale=0.3)
stalk = mat("stem", 0.9, color=mix_hex(COLORS["plant"], COLORS["wood"], 0.5))
for k in range(7):                                      # pampas plumes: fluffy, drooping, on bare stalks
    a, lean = k * 0.9, 0.1 + 0.05 * (k % 3)
    base = Vector((math.cos(a) * 0.03, math.sin(a) * 0.03, 0.1))
    tip = Vector((math.cos(a) * lean, math.sin(a) * lean, 0.9 + 0.12 * math.sin(k * 1.7)))
    tube("Basket_Stalk", [base, tip], 0.004, stalk, segs=6, parent=bk)
    axis = (tip - base).normalized()
    bm = bmesh.new()
    for j in range(16):
        t = j / 15
        bend = Vector((math.cos(a), math.sin(a), 0)) * 0.05 * t * t      # plumes droop outwards at the tip
        jit = Vector([random.uniform(-0.012, 0.012) for _ in range(3)])
        rad = 0.022 * (1.0 - 0.6 * t) * (0.5 + 1.2 * min(1.0, t * 4))
        ico = bmesh.ops.create_icosphere(bm, subdivisions=1, radius=rad)["verts"]
        bmesh.ops.translate(bm, vec=tip + axis * (0.27 * t) + bend + jit, verts=ico)
    _finish(_obj("Basket_Plume", bm), pampas, 0, None, bk)
for k in range(4):                                      # silver-dollar eucalyptus sprigs
    a = 0.4 + k * 1.6
    pts = [(0, 0, 0.12), (math.cos(a) * 0.12, math.sin(a) * 0.12, 0.45), (math.cos(a) * 0.2, math.sin(a) * 0.2, 0.62)]
    tube("Basket_Euca", pts, 0.003, stalk, segs=5, parent=bk)
    for j in range(5):
        p = Vector(pts[1]).lerp(Vector(pts[2]), j / 4) + Vector((0, 0, -0.03 * j))
        ball("Basket_EucaLeaf", 0.025, p, mat("euca", 0.7, color=mix_hex(COLORS["plant"], "#9AB0A4", 0.5)),
             scale=(1, 0.12, 0.9), rot=(0, 0, a + j), segs=10, parent=bk)

# Birch besom broom leaning on the left wall.
BROOM_FOOT, BROOM_TOP = Vector((0.4, 1.58, FLOOR_Z + 0.01)), Vector((0.03, 1.6, 1.6))
bd = (BROOM_TOP - BROOM_FOOT).normalized()
tube("Broom_Handle", [BROOM_FOOT + bd * 0.2, BROOM_TOP], 0.015, wood(1.6, 0.6, along="Z"))
twigs = mat("twig", 0.9, color=mix_hex(COLORS["wood"], COLORS["cream"], 0.15))
lathe("Broom_Head", [(0.075, 0), (0.08, 0.06), (0.065, 0.25), (0.04, 0.42), (0.032, 0.48)], BROOM_FOOT,
      surface(twigs, "wood", along="Z"), segs=28, rot=bd.to_track_quat("Z", "Y").to_euler(), wave=(28, 0.12))
for k in (0.3, 0.42):
    cyl("Broom_Binding", 0.04, 0.012, BROOM_FOOT + bd * k, mat("twine", 0.9, color=shade(COLORS["cream"], 0.8)), segs=16,
        bevel=0.002, rot=bd.to_track_quat("Z", "Y").to_euler())

# Two stacked wooden apple crates (50 x 30 x 26 cm) of container candles by the counter: an Etsy candle stall.
crate_wood = wood(1.6, 0.7)
for c, (cx, cy, cz, turn) in enumerate(((4.3, 2.75, FLOOR_Z, 90), (4.28, 2.77, FLOOR_Z + 0.26, 86))):
    cr = anchor(f"Crate_{c}", (cx, cy, cz), turn=turn)
    slats = []
    for sz in (0.03, 0.12, 0.21):
        slats += [((0.5, 0.012, 0.07), (0, sy * 0.144, sz + 0.02), (0, 0, 0)) for sy in (-1, 1)]
    slats += [((0.018, 0.3, 0.26), (sx * 0.241, 0, 0.13), (0, 0, 0)) for sx in (-1, 1)]
    slats += [((0.5, 0.29, 0.012), (0, 0, 0.006), (0, 0, 0))]
    boxes("Crate_Slats", slats, crate_wood, bevel=0.002, parent=cr)
for k in range(4):                                      # amber-glass container candles on the top crate
    x, y = 4.22 + (k % 2) * 0.13, 2.6 + (k // 2) * 0.17
    lathe(f"JarCandle_{k}", [(0.035, 0), (0.04, 0.005), (0.04, 0.09), (0.038, 0.095)], (x, y, FLOOR_Z + 0.52),
          glass(COLORS["amber"], 0.6, 0.1), segs=24)
    cyl(f"JarCandle_Wax_{k}", 0.036, 0.05, (x, y, FLOOR_Z + 0.55), wax(), segs=20, bevel=0)
    if CANDLES and k % 2 == 0:
        flame(f"JarCandle_Flame_{k}", (x, y, FLOOR_Z + 0.575), 0.8)
    box(f"JarCandle_Label_{k}", (0.045, 0.002, 0.035), (x, y - 0.041, FLOOR_Z + 0.57), paper(), bevel=0)
light("Light_Crates", "POINT", LAMP_STRENGTH, kelvin(LAMP_WARMTH), (4.28, 2.68, FLOOR_Z + 0.75), size=0.05)

# A wooden wine crate of amber bottles under the chalkboard.
wc = anchor("BottleCrate", (2.43, D - 0.26, FLOOR_Z), turn=-3)
boxes("BottleCrate_Box", [((0.5, 0.012, 0.22), (0, sy * 0.164, 0.11), (0, 0, 0)) for sy in (-1, 1)] +
      [((0.015, 0.34, 0.22), (sx * 0.243, 0, 0.11), (0, 0, 0)) for sx in (-1, 1)] +
      [((0.5, 0.34, 0.012), (0, 0, 0.006), (0, 0, 0))], crate_wood, bevel=0.002, parent=wc)
for k in range(6):
    amber_bottle(f"Crate_Bottle_{k}", -0.16 + (k % 3) * 0.16, -0.07 + (k // 3) * 0.14, 0.012, 1.25, wc,
                 with_label=k < 3)

# Pillar candles: a cluster on the floor beside the cabinet and two on the window board.
if CANDLES:
    for k, (cx, cy, ch, cr_) in enumerate([(2.72, 3.36, 0.22, 0.04), (2.84, 3.28, 0.15, 0.035), (2.66, 3.22, 0.1, 0.035)]):
        pillar_candle(f"Candle_Floor_{k}", (cx, cy, FLOOR_Z), ch, cr_, glow_light=(k == 0))
    for k, dy in enumerate((-0.32, 0.3)):
        pillar_candle(f"Candle_Sill_{k}", (0.06, wy + dy, WIN_Z[0]), 0.1 + 0.05 * k, 0.03, glow_light=(k == 0))
# A potted rosemary in a terracotta pot on the window board (pot with a rim, soil and needles).
terracotta = surface(mat("pot", 0.8, color=mix_hex(COLORS["amber"], "#C0603A", 0.6)), "ceramic")
lathe("Sill_Pot", [(0.045, 0), (0.06, 0.1), (0.068, 0.1), (0.068, 0.125), (0.058, 0.125), (0.0005, 0.11)],
      (0.06, wy, WIN_Z[0]), terracotta, segs=24)
cyl("Sill_Soil", 0.056, 0.01, (0.06, wy, WIN_Z[0] + 0.115), mat("soil", 0.95, color="#3A2A20"), segs=20, bevel=0)
for k in range(10):
    a = k * 0.63
    tube("Sill_Rosemary", [(0.06, wy, WIN_Z[0] + 0.115), (0.06 + math.cos(a) * 0.04, wy + math.sin(a) * 0.04,
                                                         WIN_Z[0] + 0.3 + 0.03 * math.sin(3 * a))], [0.006, 0.003],
         mat("plant", 0.85, color=shade(COLORS["plant"], 0.75)), segs=6)

if THEME == "harvest":                                  # seasonal decoration: real pumpkins with ribs and stalks
    def pumpkin(name, loc, r):
        lathe(f"{name}_Body", [(0.0005, 0), (r * 0.7, r * 0.08), (r, r * 0.45), (r * 0.9, r * 0.85), (r * 0.25, r * 1.02),
                               (0.0005, r * 0.95)], loc, surface(mat("main", 0.6), "ceramic"), segs=48, wave=(10, 0.06))
        tube(f"{name}_Stalk", [(loc[0], loc[1], loc[2] + r * 0.95), (loc[0] + r * 0.06, loc[1], loc[2] + r * 1.22)],
             [r * 0.1, r * 0.07], mat("plant", 0.8, color=shade(COLORS["plant"], 0.6)), segs=8)
    pumpkin("Pumpkin_A", (3.05, 3.35, FLOOR_Z), 0.16)
    pumpkin("Pumpkin_B", (2.95, 3.12, FLOOR_Z), 0.1)
    pumpkin("Pumpkin_C", (4.32, 2.4, FLOOR_Z), 0.12)


# =====================================================================
#  LIGHTS, WORLD, CAMERA, RENDER
# =====================================================================
# Moonlight through the shop window, a soft fill from the camera side and a dim bounce from above.
# The harvest theme uses a warm orange moon instead of the cold blue one.
moon_k = SUN_WARMTH if THEME != "harvest" else 3200
fill_k = 9500 if THEME != "harvest" else 4200
light("Light_Moon", "SUN", SUN_STRENGTH, kelvin(moon_k), (-3, wy + 0.4, 3.9), aim=(1.6, wy - 0.2, 0), size=R(2))
light("Light_Fill", "AREA", 200 * (W * D / 16), kelvin(fill_k), (W + 3, -3, H + 2.5), aim=(W / 2, D / 2, 0.6), size=6)
light("Light_Bounce", "AREA", 30, lin(mix_hex(COLORS["wall"], "#FFFFFF", 0.5)), (W / 2, D / 2, H - 0.1),
      aim=(W / 2, D / 2, 0), size=3.0)
light("Light_Sign", "AREA", 8, kelvin(2800), (SIGN_X, D - 0.6, SIGN_Z + 0.4), aim=(SIGN_X, D, SIGN_Z), size=1.2)

# World: the camera sees the flat background colour; the room gets a dim ambient tinted like the night.
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
bg_amb.inputs["Color"].default_value = (*kelvin(fill_k), 1)
bg_amb.inputs["Strength"].default_value = 0.3
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
                    ("shadow_ray_count", 2), ("use_gtao", True), ("use_soft_shadows", True), ("use_bloom", True)):
    if hasattr(ee, attr):
        setattr(ee, attr, value)
if hasattr(ee, "ray_tracing_options"):
    ee.ray_tracing_options.resolution_scale = "2" if "2" in [i.identifier for i in
        type(ee.ray_tracing_options).bl_rna.properties["resolution_scale"].enum_items] else ee.ray_tracing_options.resolution_scale
scene.view_settings.view_transform = "Standard"   # keeps your hex colours exactly as typed
scene.view_settings.exposure = 0.2

# Remember the style so add_furniture.py can match colours later.
scene["kit_style"] = STYLE
scene["kit_version"] = KIT_VERSION
scene["kit_palette"] = json.dumps(COLORS)
scene["kit_material_finish"] = json.dumps({"roughness": 0.6, "bevel": 0.004, "saturation": 0.6})
scene["kit_theme"] = THEME
scene["kit_bounds"] = [-T, 0.0, -0.2, W, D + T, H + 0.12]   # used to re-frame the camera for social sizes
scene["kit_furniture_colors"] = json.dumps(["main", "wood", "mahogany", "cream", "wall_trim", "plant", "dark", "wax",
                                            "brass"])   # colours add_furniture.py may use


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
