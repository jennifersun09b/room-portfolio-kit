"""
3D ROOM PORTFOLIO KIT  -  Template: COZY CORNER CAFE (neighbourhood bakery-cafe)
================================================================================
Builds a little isometric bakery-cafe in early-morning sun, modelled on real London / Copenhagen
bakery-cafes: a fluted dark-oak counter with a marble top, a curved-glass patisserie cabinet, a two-group
espresso machine and grinder, bread shelves with wicker baskets, white metro tiles, enamel pendants,
bentwood chairs, marble bistro tables, a channel-back banquette, a shop window with gold-leaf lettering,
a canvas awning and an A-board on the pavement. It renders a 1920x1080 image.
Your name and role are on the letter-board menu; your projects are the menu items and the pictures.

HOW TO RUN
  Option A (no Blender UI):   blender -b -P cozy_cafe.py
  Option B (inside Blender):  Scripting tab > Open > cozy_cafe.py > Run Script (then F12 to render)

You only need to edit the SETTINGS block below. Everything under it builds the room.
Output: output/cozy_cafe.png and output/cozy_cafe.blend next to this script.
"""
# REFERENCES  (what each piece is modelled on; brand names appear only here and in research/cozy_cafe.md)
#   chair (+ decor chairs) Thonet No.14 bentwood cafe chair: W43 D50 H89 cm, seat 46 cm, seat dia 40 cm
#                          https://www.monologuelondon.com/products/n14-chair
#   stool                  Thonet-style bentwood counter stool: seat dia 36 cm, seat height 65 cm
#                          https://www.chairish.com/product/17502425/antique-chair-model-no-14-from-thonet
#   table (+ decor tables) French marble bistro table on a cast-iron tripod: dia 60 cm, H 75 cm, 2 cm marble
#                          https://www.blumfeldt.co.uk/Garden-furniture/Patras-Pearl-Bistro-Table-Art-Nouveau-Marble-60-cm-H-75-cm-Cast-Iron-White.html
#   hero_prop              La Marzocco Linea Classic S 2-group espresso machine (shape only): W69 D56 H53 cm
#                          https://www.matthewalgie.com/machines/details/la-marzocco-linea-classic-2-group
#   grinder (decor)        Mazzer Super Jolly doser grinder: W24 D41 H60 cm
#                          https://www.wholelattelove.com/products/mazzer-super-jolly-grinder-in-black
#   display_case           curved-glass patisserie counter 900 mm (Sterling Pro EVO90 type): W90 D75 H130 cm
#                          https://ceonline.co.uk/sterling-pro-evo90-chilled-patisserie-counter-curved-glass.html
#   counter                GAIL's / Ole & Steen-style bespoke fluted-oak counter, marble top: L160 D68 H92 cm
#                          https://weberindustries.com/projects/gails-bakery
#   cake domes             glass cake stand with dome (Nkuku Banjara type): dia 30 cm, H 38 cm
#                          https://nkuku.com/products/banjara-glass-dome-cake-stand-bs11
#   card reader            SumUp Solo-style countertop reader on a dock: 83 x 83 x 18 mm
#                          https://www.mobiletransaction.org/sumup-solo-review/
#   bread wall (decor)     bakery bread shelving + wicker display baskets: shelf D38 cm, basket 38 x 30 x 10 cm
#                          https://www.mandai-design.com/products/shelving-system-ceres-bakery-style1
#                          https://www.gadsby.co.uk/prod/101/sloping-display-basket-50
#   menu (letter board)    black felt letter board with an oak frame (George & Willy type), custom 136 x 98 cm
#                          https://www.georgeandwilly.com/products/felt-board
#   wall tiles             white bevelled metro tile 150 x 75 mm, half bond
#                          https://www.clayandrock.co.uk/im-0003718-brilliant-white-metro-bevelled-tile
#   pendant_lamp           enamel dome factory pendant: dia 36 cm, 16 cm shade, hung about 0.8 m above the counter
#                          https://archipro.com.au/product/workshop-black-370mm-loftmotif
#   banquette (decor)      contract channel-back banquette: seat H45 D50 cm, back 42 cm above the seat
#                          https://dimensions.com/element/banquette-seating-clearances
#   A-board (email)        wooden A-frame chalkboard: 61 x 107 cm, chalk area 51 x 89 cm
#                          https://www.majisign.co.uk/product/standard-wooden-a-boards/
#   wall_shelf             oak shelf on black steel brackets (IKEA BERGSHULT / PERSHULT type): 80 x 20 cm, 2 cm board
#                          https://www.ikea.com/gb/en/p/bergshult-shelf-white-60292117/
#   plant                  olive tree in a fibre-clay planter: pot dia 38 x 36 cm, tree about 1.45 m
#   floor                  oak herringbone parquet with a border: 70 x 350 mm blocks

# =====================================================================
#  SETTINGS  -  change these lines, then run the script again
# =====================================================================
ROOM_NAME = "cozy_cafe"             # used for the output file names

ROOM_WIDTH = 4.4                    # metres, left to right
ROOM_DEPTH = 4.0                    # metres, front to back
WALL_HEIGHT = 2.9                   # metres

THEME = "morning"                   # pick one of the colour themes below
THEMES = {                          # any hex colour works; "main" is the room's hero colour
    # "morning": dark-stained oak and white marble, sage banquette, heritage-green shopfront, terracotta awning.
    "morning": {
        "background": "#EFE4D6", "wall": "#F1E9DC", "wall_trim": "#E4D6C2", "floor": "#B48F69", "floor_2": "#A4815D",
        "wood": "#C29F78", "main": "#8EA58C", "accent_1": "#C8653E", "accent_2": "#F1D7A6", "accent_3": "#C9A45C",
        "cream": "#F6F1E8", "plant": "#71895A", "dark": "#2A2725", "walnut": "#4B3324", "joinery": "#34463C",
        "chalk": "#FBF7EE", "pavement": "#CFC7BB", "glass": "#E3F1EE", "sky": "#FFF1D8", "metal": "#C9CBCB",
        "bread": "#CB975C", "crust": "#8D5634", "tile": "#F7F5EF", "marble": "#F2EFEA", "brass": "#C9A45C",
        "wicker": "#C39459", "machine": "#C9CBCB",
    },
    # "bakery": a pastel patisserie - pink shopfront and espresso machine, mint banquette, whitewashed oak.
    # Same lights as "morning".
    "bakery": {
        "background": "#F8E6E8", "wall": "#FCF0EF", "wall_trim": "#F2D5D9", "floor": "#D9BB98", "floor_2": "#CCAA86",
        "wood": "#E0B48E", "main": "#A9DCC7", "accent_1": "#F28DA6", "accent_2": "#FFE2B3", "accent_3": "#B9A4E0",
        "cream": "#FFFAF4", "plant": "#7DBE8C", "dark": "#4A3A42", "walnut": "#B9805E", "joinery": "#E9A3B4",
        "chalk": "#FFF3F5", "pavement": "#E3D9D6", "glass": "#E6F6F2", "sky": "#FFF3E6", "metal": "#D6D3D4",
        "bread": "#E3A866", "crust": "#B7703A", "tile": "#FFF8F6", "marble": "#FBF4F2", "brass": "#D8B26A",
        "wicker": "#D9B07A", "machine": "#F4B9C7",
    },
}

SUN_WARMTH = 4000                   # Kelvin: 2500 = sunset orange, 6500 = white daylight (4000 = early morning)
SUN_STRENGTH = 3.6
LAMP_WARMTH = 2400                  # Kelvin of the bulbs in the enamel pendants over the counter
LAMP_STRENGTH = 17                  # Watts per pendant bulb
AWNING = True                       # striped canvas awning outside the shop window (it "breaks the box")
PAVEMENT = True                     # strip of pavement with an A-board in front of the cafe
SEED = 7                            # change to shuffle pastries, breads, jars and props

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
BAKERY_PROPS = THEME == "bakery"    # patisserie theme: macarons and tarts in the cabinet

STYLE = "cozy_cafe"
KIT_VERSION = 2
W, D, H = ROOM_WIDTH, ROOM_DEPTH, WALL_HEIGHT
T = 0.15            # wall thickness
FLOOR_Z = 0.02      # top of the oak parquet; furniture stands here
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


# The room's real materials (one place, so every piece uses the same oak, marble, steel...).
OAK = M("wood", 0.5, "wood")                       # light oak: shelves, frames, bread racks, picture frames
OAK_V = M("wood", 0.52, "wood", along="Z")         # light oak with vertical grain (uprights)
DARK_OAK = M("walnut", 0.45, "wood")               # dark-stained oak: counter carcass, back bar, bentwood
DARK_OAK_V = M("walnut", 0.47, "wood", along="Z")  # vertical grain: counter flutes, chair legs
MARBLE = M("marble", 0.18, "marble")               # Carrara-style marble: counter and table tops
STEEL = M("machine", 0.3, "brushed", metal=1.0) if COLORS["machine"] == COLORS["metal"] else \
    M("machine", 0.32, "ceramic")                  # espresso machine body (stainless, or enamel paint)
INOX = M("metal", 0.28, "brushed", metal=1.0)      # stainless: drip tray, cabinet deck, jugs
CHROME = M("metal", 0.1, "brushed", metal=1.0, along="Z")
IRON = M("dark", 0.5, "brushed", metal=0.7)        # cast iron / black steel
BRASS = M("brass", 0.3, "brushed", metal=1.0)
GOLD_LEAF = mat("brass", 0.2, metal=1.0, emit=0.15)
FABRIC = M("main", 0.9, "fabric")                  # banquette upholstery
CANE = M("wicker", 0.7, "knit", scale=2.0)         # woven cane seats
WICKER = M("wicker", 0.75, "knit")                 # bread baskets
WICKER_DARK = M("wicker", 0.8, "knit", color="#9C7240" if not BAKERY_PROPS else "#BE915C")   # darker woven rods
LINEN = M("cream", 0.9, "fabric")
CERAMIC = M("cream", 0.3, "ceramic")
PAINT = M("joinery", 0.5, "plaster", scale=3)      # painted shopfront joinery (door, window frames)
TRIM = M("wall_trim", 0.55, "plaster", scale=3)    # painted skirting and architraves
PLASTER = M("wall", 0.85, "plaster")
TILE = M("tile", 0.2, "subway_tile")
FELT = M("dark", 0.95, "fabric")
PAPER = M("cream", 0.8, "paper")
KRAFT = M("accent_2", 0.85, "paper")
POT_CLAY = M("pavement", 0.8, "concrete")          # fibre-clay planters
GLASS = mat("glass", 0.05, alpha=0.16)
DOME_GLASS = mat("glass", 0.02, alpha=0.3)
BREAD = M("bread", 0.6, "plaster", scale=5)        # golden laminated dough, softly mottled
CRUST = M("crust", 0.55, "concrete", scale=5)      # well-baked crust: uneven, blistered colour
LOAF = M("loaf", 0.75, "concrete", scale=6, color="#7A4524" if not BAKERY_PROPS else "#8A5230")  # dark sourdough crust
GLAZE = mat("glaze", 0.3, color="#A97340" if not BAKERY_PROPS else "#C08549")   # egg-washed pastry top (shiny)
FLOUR = M("cream", 0.95, "paper", scale=0.5)
DUST = M("dust", 0.95, "paper", scale=0.5, color="#D9C3A2")    # thin flour dusting: crust colour shows through
SHOP_GLASS = mat("sky", 0.05, emit=0.4, alpha=0.55)     # shop window: bright street seen through clear glass
GLINT = mat("chalk", 0.1, emit=0.9, alpha=0.35)         # soft reflection streaks across the glass
CHOC = mat("walnut", 0.4, color="#3B2418")
SOIL = mat("soil", 0.95, color="#3A2A20")
PLINTH = M("dark", 0.7, "plaster", scale=3)        # painted plinths / kick boards
SLATE = M("dark", 0.85, "concrete", scale=3)       # chalkboard


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


# =====================================================================
#  ROOM SHELL: oak herringbone floor, plaster walls, metro tiles, shopfront
# =====================================================================
box("Floor_Base", (W + T, D + T, 0.2), ((W - T) / 2, (D + T) / 2, -0.1), mat("wall_trim", 0.7), bevel=0.02)
box("Floor_Joints", (W, D, 0.004), (W / 2, D / 2, 0.002), mat("crust", 0.9), bevel=0)   # dark gaps between blocks


def herringbone(x0, y0, x1, y1, L=0.35, w=0.07, gap=0.0015):
    """Oak parquet blocks laid at 45 degrees, clipped to a rectangle. Two objects (one per block direction)
    so the wood grain runs along every block."""
    c = Vector(((x0 + x1) / 2, (y0 + y1) / 2, 0))
    reach = math.hypot(x1 - x0, y1 - y0) / 2 + L
    rnd = random.Random(SEED + 3)
    for nm, ang, vertical in (("A", 45, False), ("B", 135, True)):
        rot = Matrix.Rotation(R(45), 3, "Z")
        bm = bmesh.new()
        for m in range(-int(reach / L) - 2, int(reach / L) + 3):
            for k in range(-int(2 * reach / w) - 2, int(2 * reach / w) + 3):
                u, v = k * w + m * L, k * w - m * L
                if vertical:
                    rect = (u, u + w, v + w, v + w + L)
                else:
                    rect = (u, u + L, v, v + w)
                pts = [c + rot @ Vector((px, py, 0)) for px in rect[:2] for py in rect[2:]]
                if max(p.x for p in pts) < x0 or min(p.x for p in pts) > x1 or \
                        max(p.y for p in pts) < y0 or min(p.y for p in pts) > y1:
                    continue
                ux0, ux1, vy0, vy1 = rect[0] + gap, rect[1] - gap, rect[2] + gap, rect[3] - gap
                vs = [bm.verts.new(c + rot @ Vector((px, py, 0)) + Vector((0, 0, pz)))
                      for pz in (0.004, FLOOR_Z) for px, py in ((ux0, vy0), (ux1, vy0), (ux1, vy1), (ux0, vy1))]
                mi = rnd.randint(0, 1)
                for f in ((0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)):
                    bm.faces.new([vs[i] for i in f]).material_index = mi
        for co, no in (((x1, 0, 0), (1, 0, 0)), ((x0, 0, 0), (-1, 0, 0)), ((0, y1, 0), (0, 1, 0)), ((0, y0, 0), (0, -1, 0))):
            bmesh.ops.bisect_plane(bm, geom=bm.verts[:] + bm.edges[:] + bm.faces[:], plane_co=co, plane_no=no,
                                   clear_outer=True)
        bmesh.ops.translate(bm, vec=-c, verts=bm.verts)            # object origin in the middle, X along the blocks
        bmesh.ops.rotate(bm, verts=bm.verts, cent=(0, 0, 0), matrix=Matrix.Rotation(-R(ang), 3, "Z"))
        o = _obj(f"Floor_Herringbone_{nm}", bm)
        o.location, o.rotation_euler = c, (0, 0, R(ang))
        o.data.materials.append(M("floor", 0.42, "veneer"))
        o.data.materials.append(M("floor_2", 0.42, "veneer"))
        o.data.polygons.foreach_set("use_smooth", [False] * len(o.data.polygons))
        COL_ROOM.objects.link(o)


BORDER = 0.075
herringbone(BORDER, BORDER, W - BORDER, D - BORDER)
for nm, size, loc, along in (("Front", (W, BORDER, FLOOR_Z - 0.004), (W / 2, BORDER / 2, 0.011), "X"),
                             ("Back", (W, BORDER, FLOOR_Z - 0.004), (W / 2, D - BORDER / 2, 0.011), "X"),
                             ("Left", (BORDER, D - 2 * BORDER - 0.004, FLOOR_Z - 0.004), (BORDER / 2, D / 2, 0.011), "Y"),
                             ("Right", (BORDER, D - 2 * BORDER - 0.004, FLOOR_Z - 0.004), (W - BORDER / 2, D / 2, 0.011), "Y")):
    box(f"Floor_Border_{nm}", size, loc, M("floor_2", 0.43 if along == "X" else 0.44, "veneer", along=along), bevel=0.0015)

# Left wall = the street side: a glazed shop door at the front and a big shop window in the middle.
DOOR_Y, DOOR_TOP = (0.2, 1.1), 2.1
WIN_Y, WIN_Z = (1.4, 3.0), (0.92, 2.42)
left = box("Wall_Left", (T, D + T, H), (-T / 2, (D + T) / 2, H / 2), PLASTER, bevel=0.0)
for nm, (ys, zs) in (("Door", (DOOR_Y, (-0.1, DOOR_TOP))), ("Window", (WIN_Y, WIN_Z))):
    cutter = box(f"{nm}_Cutter", (T * 3, ys[1] - ys[0], zs[1] - zs[0]), (-T / 2, sum(ys) / 2, sum(zs) / 2),
                 mat("wall"), bevel=0.0)
    cutter.hide_render = cutter.hide_viewport = True
    boolean = left.modifiers.new(nm, "BOOLEAN")
    boolean.operation, boolean.object = "DIFFERENCE", cutter
box("Wall_Back", (W + T, T, H), ((W - T) / 2, D + T / 2, H / 2), PLASTER, bevel=0.0)

# Diorama cap on top of the walls (dark oak, like a cornice).
box("Trim_Top_Back", (W + T + 0.04, T + 0.06, 0.08), ((W - T) / 2, D + T / 2, H + 0.04), DARK_OAK, bevel=0.01)
box("Trim_Top_Left", (T + 0.06, D + T + 0.04, 0.08), (-T / 2, (D + T) / 2 - 0.02, H + 0.04), DARK_OAK, bevel=0.01)

# White metro tiles (150 x 75 mm, half bond) behind the bread wall, with a slim bullnose edge on top.
BB_X0, BB_D = 1.78, 0.5                      # back bar: where it starts (x) and how deep it is
TILE_TOP = H - 0.12
box("Wall_Tiles", (W - BB_X0 + 0.02, 0.012, TILE_TOP - FLOOR_Z), ((W + BB_X0 - 0.02) / 2, D - 0.006,
    (TILE_TOP + FLOOR_Z) / 2), TILE, bevel=0.0)
box("Wall_Tiles_Edge", (W - BB_X0 + 0.02, 0.018, 0.014), ((W + BB_X0 - 0.02) / 2, D - 0.009, TILE_TOP + 0.007),
    TILE, bevel=0.005)

# Painted skirting (120 mm) and architraves (70 mm) around the door and window.
SK = 0.12
for nm, size, loc in (("Back", (BB_X0, 0.018, SK), (BB_X0 / 2, D - 0.009, FLOOR_Z + SK / 2)),
                      ("Left_Front", (0.018, DOOR_Y[0] - 0.07, SK), (0.009, (DOOR_Y[0] - 0.07) / 2, FLOOR_Z + SK / 2)),
                      ("Left_Back", (0.018, D - DOOR_Y[1] - 0.07, SK), (0.009, (D + DOOR_Y[1] + 0.07) / 2, FLOOR_Z + SK / 2))):
    box(f"Skirting_{nm}", size, loc, TRIM, bevel=0.004)
for nm, (ys, z0, z1) in (("Door", (DOOR_Y, FLOOR_Z, DOOR_TOP)), ("Window", (WIN_Y, WIN_Z[0], WIN_Z[1]))):
    for sy, yy in ((-1, ys[0] - 0.035), (1, ys[1] + 0.035)):
        box(f"Architrave_{nm}", (0.02, 0.07, z1 - z0 + 0.07), (0.01, yy, (z0 + z1 + 0.07) / 2), TRIM, bevel=0.004)
    box(f"Architrave_{nm}_Head", (0.02, ys[1] - ys[0] + 0.14, 0.07), (0.01, sum(ys) / 2, z1 + 0.035), TRIM, bevel=0.004)

# Shop window: painted timber frame, a centre mullion, a transom with two fanlights, an oak window board.
wy, wz = sum(WIN_Y) / 2, sum(WIN_Z) / 2
ww, wh = WIN_Y[1] - WIN_Y[0], WIN_Z[1] - WIN_Z[0]
TRANSOM = WIN_Z[1] - 0.42
FX = -T / 2
for nm, size, loc in [
    ("Head", (T + 0.02, ww, 0.08), (FX, wy, WIN_Z[1] - 0.04)),
    ("Sill", (T + 0.06, ww, 0.07), (FX - 0.02, wy, WIN_Z[0] + 0.035)),
    ("Jamb_Front", (T + 0.02, 0.08, wh), (FX, WIN_Y[0] + 0.04, wz)),
    ("Jamb_Back", (T + 0.02, 0.08, wh), (FX, WIN_Y[1] - 0.04, wz)),
    ("Mullion", (0.07, 0.05, wh), (FX, wy, wz)),
    ("Transom", (0.07, ww, 0.05), (FX, wy, TRANSOM)),
    ("Fanlight_Bar_1", (0.05, 0.03, 0.4), (FX, WIN_Y[0] + ww / 4, TRANSOM + 0.2)),
    ("Fanlight_Bar_2", (0.05, 0.03, 0.4), (FX, WIN_Y[0] + 3 * ww / 4, TRANSOM + 0.2)),
]:
    box(f"Window_Frame_{nm}", size, loc, PAINT, bevel=0.006)
no_shadow(box("Window_Glass", (0.006, ww - 0.1, wh - 0.1), (FX - 0.01, wy, wz), SHOP_GLASS, bevel=0))


def glints(name, x, cy, cz, n=2):
    """Two soft diagonal reflection streaks, the way real plate glass catches the light."""
    for k, (dy, wdt, ln) in enumerate(((-0.06, 0.07, 0.5), (0.07, 0.025, 0.4))[:n]):
        no_shadow(box(f"{name}_Glint_{k}", (0.002, wdt, ln), (x, cy + dy, cz), GLINT, bevel=0, rot=(R(-38), 0, 0)))


for cy_ in (WIN_Y[0] + ww / 4, WIN_Y[0] + 3 * ww / 4):
    glints("Window", FX - 0.005, cy_, WIN_Z[0] + 0.5)
box("Window_Board", (0.24, ww + 0.1, 0.025), (0.08, wy, WIN_Z[0] + 0.0125), OAK, bevel=0.004)
# Gold-leaf lettering is gilded on the inside of the glass to read from the street, so from in here it is mirrored.
gx = FX - 0.004
for k, sy in enumerate((-1, 1)):
    cy_ = wy + sy * ww / 4
    label(f"Window_Gilt_{k}", "BAKERY" if k == 0 else "& COFFEE", 0.11 if k == 0 else 0.085,
          (gx, cy_, TRANSOM - 0.2), GOLD_LEAF, rot=(R(90), 0, R(-90)), depth=0.001)
    box(f"Window_Gilt_Rule_{k}", (0.002, 0.42, 0.006), (gx, cy_, TRANSOM - 0.29), GOLD_LEAF, bevel=0)
    label(f"Window_Gilt_Small_{k}", "fresh daily" if k == 0 else "since 2026", 0.04, (gx, cy_, TRANSOM - 0.34),
          GOLD_LEAF, rot=(R(90), 0, R(-90)), depth=0.001)

# Glazed shop door: stiles and rails, a solid kick panel, brass push bar and kick plate, and a shop bell.
dy0, dy1 = DOOR_Y
dcy, dw = (dy0 + dy1) / 2, dy1 - dy0
for nm, size, loc in [("Head", (T + 0.02, dw + 0.02, 0.06), (FX, dcy, DOOR_TOP - 0.03)),
                      ("Jamb_Front", (T + 0.02, 0.05, DOOR_TOP), (FX, dy0 + 0.025, DOOR_TOP / 2)),
                      ("Jamb_Back", (T + 0.02, 0.05, DOOR_TOP), (FX, dy1 - 0.025, DOOR_TOP / 2))]:
    box(f"Door_Frame_{nm}", size, loc, PAINT, bevel=0.006)
LX, leaf_w, leaf_h = -0.03, dw - 0.1, DOOR_TOP - 0.06 - FLOOR_Z - 0.005
lz0 = FLOOR_Z + 0.005
door = box("Door_Leaf_Bottom_Rail", (0.045, leaf_w, 0.24), (LX, dcy, lz0 + 0.12), PAINT, bevel=0.005)
hook_link(door, "linkedin")
for nm, h_, z_ in (("Lock_Rail", 0.12, lz0 + 0.95), ("Top_Rail", 0.1, lz0 + leaf_h - 0.05)):
    box(f"Door_Leaf_{nm}", (0.045, leaf_w, h_), (LX, dcy, z_), PAINT, bevel=0.005)
for sy in (-1, 1):
    box("Door_Leaf_Stile", (0.045, 0.1, leaf_h), (LX, dcy + sy * (leaf_w / 2 - 0.05), lz0 + leaf_h / 2), PAINT, bevel=0.005)
box("Door_Leaf_Panel", (0.035, leaf_w - 0.2, 0.65), (LX, dcy, lz0 + 0.24 + 0.325), PAINT, bevel=0.012)
gl_h = leaf_h - 1.01 - 0.1
no_shadow(box("Door_Glass", (0.006, leaf_w - 0.2, gl_h), (LX, dcy, lz0 + 1.01 + gl_h / 2), SHOP_GLASS, bevel=0))
glints("Door", LX + 0.006, dcy, lz0 + 1.01 + gl_h / 2)
box("Door_Kick_Plate", (0.004, leaf_w - 0.02, 0.2), (LX + 0.024, dcy, lz0 + 0.11), BRASS, bevel=0.001)
tube("Door_Push_Bar", [(LX + 0.03, dy1 - 0.17, 0.85), (LX + 0.065, dy1 - 0.17, 0.87), (LX + 0.065, dy1 - 0.17, 1.33),
                       (LX + 0.03, dy1 - 0.17, 1.35)], 0.012, BRASS)
tube("Door_Bell_Spring", spline([(0.0, dy1 - 0.08, DOOR_TOP + 0.08), (0.06, dy1 - 0.1, DOOR_TOP + 0.06),
                                 (0.1, dy1 - 0.16, DOOR_TOP - 0.0)], 5), 0.004, IRON)
lathe("Door_Bell", [(0, -0.05), (0.03, -0.05), (0.025, -0.03), (0.016, 0.0), (0.006, 0.01), (0, 0.012)],
      (0.1, dy1 - 0.16, DOOR_TOP - 0.01), BRASS, segs=20)
box("Door_Mat", (0.55, dw, 0.012), (0.3, dcy, FLOOR_Z + 0.006), M("wicker", 0.95, "knit", scale=3), bevel=0.003)


# =====================================================================
#  REAL-WORLD PIECES (shared by the placeholders and the decoration)
# =====================================================================
def make_cup(name, loc, parent, key="cream", saucer=True, size=1.0, latte=True):
    """Flat-white cup and saucer (cup dia 8.5 cm), with a latte-art heart."""
    x, y, z = loc
    cup_mat = CERAMIC if key == "cream" else M(key, 0.31, "ceramic")
    if saucer:
        lathe(f"{name}_Saucer", [(0, 0), (0.045, 0), (0.07, 0.009), (0.072, 0.013), (0.066, 0.012), (0.03, 0.006),
                                 (0, 0.006)], (x, y, z), CERAMIC, parent=parent)
        z += 0.006
    s = size
    lathe(f"{name}_Cup", [(0, 0), (0.024 * s, 0), (0.03 * s, 0.005 * s), (0.042 * s, 0.05 * s), (0.044 * s, 0.058 * s),
                          (0.041 * s, 0.058 * s), (0.039 * s, 0.05 * s), (0.026 * s, 0.008 * s), (0, 0.008 * s)],
          (x, y, z), cup_mat, parent=parent)
    if latte:
        cyl(f"{name}_Coffee", 0.0395 * s, 0.002, (x, y, z + 0.05 * s), mat("crust", 0.3, color="#8A5A36"), bevel=0,
            parent=parent)
        ball(f"{name}_Art", 0.016 * s, (x, y, z + 0.051 * s), mat("cream", 0.4, color="#F3E3CC"), scale=(1, 1.2, 0.08),
             parent=parent)
    tube(f"{name}_Handle", spline([(x + 0.04 * s, y, z + 0.045 * s), (x + 0.062 * s, y, z + 0.04 * s),
                                   (x + 0.06 * s, y, z + 0.02 * s), (x + 0.036 * s, y, z + 0.016 * s)], 4),
         0.004 * s, cup_mat, parent=parent, segs=8)


def croissant(name, loc, parent, turn=0.0, s=1.0, mats=None):
    """Crescent of 7 rolled ridges, biggest in the middle, darker tips curling inwards."""
    body, tips = mats or (GLAZE, CRUST)
    e = empty(name, loc, rot=(0, 0, turn), parent=parent)
    for i in range(7):
        t = -1 + 2 * i / 6
        a = t * R(74)
        rad = 0.026 * s * (1 - 0.5 * t * t)
        arc = 0.045 * s * (1 - 0.12 * t * t)              # tips pull in towards each other, like a real crescent
        ball(f"{name}_Ridge", rad, (math.sin(a) * arc, -math.cos(a) * arc + 0.03 * s, rad * 0.75),
             body if abs(t) < 0.5 else tips, scale=(0.95, 1.3, 0.8), rot=(0, 0, a), parent=e, segs=14)
    return e


def pain_au_chocolat(name, loc, parent, turn=0.0):
    """Rolled laminated rectangle (10 x 7 cm): a puffed, egg-washed block with the lapped seam on top,
    flaky layers and the two chocolate batons showing at each open end."""
    e = empty(name, loc, rot=(0, 0, turn), parent=parent)
    box(f"{name}_Base", (0.104, 0.068, 0.012), (0, 0, 0.006), BREAD, bevel=0.005, parent=e)        # pale baked base
    box(f"{name}_Body", (0.1, 0.066, 0.03), (0, 0, 0.019), GLAZE, bevel=0.012, parent=e)          # puffed, egg-washed
    box(f"{name}_Seam", (0.094, 0.005, 0.004), (0, 0.012, 0.034), CRUST, bevel=0.0015, parent=e)  # lapped dough edge
    for sx in (-1, 1):
        for zz in (0.012, 0.024):                       # laminated layers showing at the open ends
            box(f"{name}_Layer", (0.003, 0.05, 0.0025), (sx * 0.0505, 0, zz), BREAD, bevel=0, parent=e)
        for yy in (-0.012, 0.012):
            box(f"{name}_Choc", (0.004, 0.012, 0.007), (sx * 0.0505, yy, 0.018), CHOC, bevel=0.001, parent=e)
    return e


def cinnamon_bun(name, loc, parent, turn=0.0):
    """Swirled bun: dough round + a darker cinnamon spiral + a sugar glaze drizzle."""
    e = empty(name, loc, rot=(0, 0, turn), parent=parent)
    cyl(f"{name}_Dough", 0.042, 0.04, (0, 0, 0.02), BREAD, bevel=0.012, segs=20, parent=e)
    sp = [(math.cos(a) * (0.036 - a * 0.0024), math.sin(a) * (0.036 - a * 0.0024), 0.041) for a in
          (k * 0.35 for k in range(36))]
    tube(f"{name}_Swirl", sp, 0.0045, CRUST, parent=e, segs=6)
    return e


def tart(name, loc, parent, key="accent_2"):
    lathe(f"{name}_Shell", [(0, 0), (0.044, 0), (0.048, 0.022), (0.044, 0.024), (0.04, 0.016), (0, 0.016)], loc,
          BREAD, segs=24, parent=parent)
    x, y, z = loc
    cyl(f"{name}_Filling", 0.041, 0.006, (x, y, z + 0.019), mat(key, 0.35), bevel=0.002, segs=24, parent=parent)
    for k in range(5):
        a = k * 2 * math.pi / 5
        ball(f"{name}_Berry", 0.009, (x + math.cos(a) * 0.022, y + math.sin(a) * 0.022, z + 0.025),
             mat("berry", 0.3, color="#8E2340"), parent=parent, segs=10)


def macaron(name, loc, parent, key):
    x, y, z = loc
    for zz in (0.006, 0.02):
        cyl(f"{name}_Shell", 0.021, 0.011, (x, y, z + zz), mat(key, 0.6), bevel=0.005, segs=18, parent=parent)
    cyl(f"{name}_Filling", 0.018, 0.006, (x, y, z + 0.013), mat("cream", 0.5), bevel=0.001, segs=18, parent=parent)


def boule(name, loc, parent, r=0.085):
    """Round sourdough loaf proved in a cane banneton: dark caramel crust with the basket's spiral of flour
    rings, and one long curved score that opened in the oven into a golden cut with a raised crusty 'ear'."""
    x, y, z = loc
    c = z + r * 0.5
    ball(f"{name}_Loaf", r, (x, y, c), LOAF, scale=(1, 1, 0.6), parent=parent, segs=28)
    a = random.uniform(0, math.pi)
    ca, sa = math.cos(a), math.sin(a)

    def top(u, v, lift):                             # a point on the crust, lifted a little off it
        zl = 0.6 * r * math.sqrt(max(0.0, 1 - (u * u + v * v) / (r * r)))
        return (x + ca * u - sa * v, y + sa * u + ca * v, c + zl + lift)
    for k, rr in enumerate((0.38, 0.6, 0.8)):        # flour rings left by the banneton
        tube(f"{name}_Ring_{k}", [top(rr * r * math.cos(t), rr * r * math.sin(t), 0.0) for t in
                                  (2 * math.pi * q / 28 for q in range(28))], 0.017 * r, DUST, parent=parent,
             segs=5, closed=True)
    cut = [(t * r, 0.16 * r * (1 - (t / 0.62) ** 2)) for t in (k * 0.124 - 0.62 for k in range(11))]
    tube(f"{name}_Score", [top(u, v, 0.01 * r) for u, v in cut], 0.07 * r, GLAZE, parent=parent, segs=6)
    tube(f"{name}_Ear", [top(u, v + 0.075 * r, 0.04 * r) for u, v in cut[1:-1]], 0.04 * r, CRUST, parent=parent,
         segs=6)


def bloomer(name, loc, parent, turn=0.0, length=0.28):
    """Bloomer: a long, deep-golden loaf with five diagonal slashes that opened up pale in the oven."""
    e = empty(name, loc, rot=(0, 0, turn), parent=parent)
    ball(f"{name}_Loaf", 0.06, (0, 0, 0.04), CRUST, scale=(length / 0.12, 1, 0.75), parent=e, segs=28)
    for k in range(5):
        u = -length * 0.32 + k * length * 0.16
        zt = 0.04 + 0.045 * math.sqrt(max(0.0, 1 - (u / (length / 2)) ** 2))
        ball(f"{name}_Slash", 0.03, (u, 0, zt - 0.003), DUST, scale=(0.22, 1.05, 0.12), rot=(0, 0, R(35)), parent=e,
             segs=12)
    return e


def baguette(name, loc, parent, rot=(0, 0, 0), length=0.6):
    e = empty(name, loc, rot=rot, parent=parent)
    ball(f"{name}_Stick", 0.03, (0, 0, 0), CRUST, scale=(length / 0.06, 1, 0.85), parent=e, segs=16)
    for k in range(5):
        ball(f"{name}_Slash", 0.03, (-length * 0.33 + k * length * 0.165, 0, 0.019), BREAD, scale=(1, 0.22, 0.25),
             rot=(0, 0, R(18)), parent=e, segs=12)
    return e


def pastry(name, loc, parent, kind=None, turn=None):
    """One item from the patisserie, picked by theme + SEED when kind is empty."""
    pool = (["macaron", "tart", "cinnamon", "croissant"] if BAKERY_PROPS
            else ["croissant", "pain", "cinnamon", "tart"])
    kind = kind or random.choice(pool)
    turn = random.uniform(-0.3, 0.3) if turn is None else turn
    if kind == "croissant":
        croissant(name, loc, parent, turn)
    elif kind == "pain":
        pain_au_chocolat(name, loc, parent, turn)
    elif kind == "cinnamon":
        cinnamon_bun(name, loc, parent, turn)
    elif kind == "tart":
        tart(name, loc, parent, random.choice(["accent_2", "cream"]))
    else:
        macaron(name, loc, parent, random.choice(["accent_1", "main", "accent_3", "accent_2"]))


def cake_dome(name, loc, parent=None, chocolate=False):
    """Footed white cake stand (dia 30 cm) with a layer cake under a glass bell dome (H 38 cm in all)."""
    x, y, z = loc
    lathe(f"{name}_Stand", [(0, 0), (0.06, 0), (0.055, 0.01), (0.022, 0.03), (0.02, 0.085), (0.15, 0.09),
                            (0.152, 0.097), (0, 0.097)], loc, CERAMIC, parent=parent)
    cz = z + 0.097
    # Victoria sponge: two golden sponges, a layer of whipped cream and jam, icing sugar on top
    # chocolate: dark sponge, ganache filling and a glossy ganache top with a ring of cocoa-dusted truffles
    sponge = mat("sponge", 0.7, color=("#5B3626" if chocolate else "#C08048" if not BAKERY_PROPS else "#D3955A"))
    filling = mat("cream", 0.6, color="#3E2419" if chocolate else "#EADBC2")
    cyl(f"{name}_Sponge", 0.1, 0.045, (x, y, cz + 0.0225), sponge, bevel=0.008, parent=parent)
    cyl(f"{name}_Cream", 0.097, 0.014, (x, y, cz + 0.052), filling, bevel=0.005, parent=parent)
    if not chocolate:
        cyl(f"{name}_Jam", 0.092, 0.006, (x, y, cz + 0.062), mat("berry", 0.3, color="#9E2238"), bevel=0.002,
            parent=parent)
    cyl(f"{name}_Sponge_Top", 0.1, 0.042, (x, y, cz + 0.086), sponge, bevel=0.01, parent=parent)
    if chocolate:
        cyl(f"{name}_Ganache", 0.101, 0.006, (x, y, cz + 0.106), mat("ganache", 0.2, color="#2E1A12"), bevel=0.003,
            parent=parent)
        for k in range(8):
            a = k * math.pi / 4
            ball(f"{name}_Truffle", 0.011, (x + 0.075 * math.cos(a), y + 0.075 * math.sin(a), cz + 0.118), CHOC,
                 parent=parent, segs=10)
    else:
        cyl(f"{name}_Sugar", 0.088, 0.003, (x, y, cz + 0.1075), DUST, bevel=0.0015, parent=parent)
    no_shadow(lathe(f"{name}_Dome", [(0.142, 0.0), (0.14, 0.12), (0.12, 0.2), (0.07, 0.25), (0.02, 0.262),
                                     (0.018, 0.29), (0.0, 0.295)], (x, y, cz), DOME_GLASS, segs=40, parent=parent))
    ball(f"{name}_Knob", 0.022, (x, y, cz + 0.29), DOME_GLASS, parent=parent)


def bentwood_chair(root, seat_h=0.46):
    """Vienna No.14-style cafe chair: one bent piece forms the back legs and back hoop, plus an inner loop,
    a caned seat ring, four splayed legs and a leg ring. Built in root's space, front = -y. W43 D50 H89 cm."""
    wood = DARK_OAK_V
    cy = -0.01
    cyl("Chair_Seat_Rim", 0.205, 0.04, (0, cy, seat_h - 0.02), wood, bevel=0.006, segs=40, parent=root)
    cyl("Chair_Seat_Cane", 0.182, 0.006, (0, cy, seat_h + 0.002), CANE, bevel=0.001, segs=40, parent=root)
    tube("Chair_Seat_Ring", ring_pts(0.195, seat_h + 0.002, 40, 0, cy), 0.013, wood, parent=root, closed=True)
    for sx in (-1, 1):
        tube("Chair_Front_Leg", spline([(sx * 0.155, -0.205, 0.0), (sx * 0.14, -0.175, 0.22),
                                        (sx * 0.125, -0.15, seat_h - 0.03)], 4), 0.0135, wood, parent=root, r2=0.016)
        tube("Chair_Brace", spline([(sx * 0.13, -0.16, seat_h - 0.12), (sx * 0.1, -0.12, seat_h - 0.05),
                                    (sx * 0.05, -0.12, seat_h - 0.035)], 4), 0.007, wood, parent=root)
    back = sym([(-0.15, 0.25, 0.0), (-0.132, 0.17, 0.3), (-0.125, 0.14, seat_h), (-0.14, 0.155, 0.6),
                (-0.156, 0.18, 0.74), (-0.145, 0.2, 0.83), (-0.088, 0.215, 0.877), (0.0, 0.22, 0.89)])
    tube("Chair_Back_Hoop", spline(back, 5), 0.0155, wood, parent=root)
    inner = sym([(-0.075, 0.15, seat_h), (-0.094, 0.165, 0.6), (-0.088, 0.182, 0.72), (-0.042, 0.19, 0.768),
                 (0.0, 0.192, 0.772)])
    tube("Chair_Inner_Loop", spline(inner, 5), 0.0105, wood, parent=root)
    tube("Chair_Leg_Ring", ring_pts(0.222, 0.2, 40, 0, 0.012), 0.0095, wood, parent=root, closed=True)


def bistro_table(root, h=0.75, top_r=0.3):
    """Marble-top bistro table: 2 cm veined top, cast-iron column with collars and three curled feet."""
    cyl("Table_Top", top_r, 0.02, (0, 0, h - 0.01), MARBLE, segs=56, bevel=0.005, parent=root)
    cyl("Table_Spider", 0.11, 0.012, (0, 0, h - 0.026), IRON, segs=24, bevel=0.003, parent=root)
    lathe("Table_Column", [(0, 0.1), (0.04, 0.1), (0.045, 0.13), (0.024, 0.16), (0.02, 0.4), (0.032, 0.44),
                           (0.02, 0.48), (0.018, h - 0.07), (0.03, h - 0.05), (0.03, h - 0.032), (0, h - 0.032)],
          (0, 0, 0), IRON, segs=20, parent=root)
    for k in range(3):
        a = R(90 + k * 120)
        ca, sa = math.cos(a), math.sin(a)
        pts = [(ca * rr, sa * rr, zz) for rr, zz in ((0.03, 0.14), (0.1, 0.11), (0.2, 0.05), (0.26, 0.018), (0.29, 0.02))]
        tube("Table_Foot", spline(pts, 4), 0.017, IRON, parent=root, r2=0.012)
        cyl("Table_Foot_Pad", 0.022, 0.012, (ca * 0.28, sa * 0.28, 0.006), IRON, segs=12, parent=root)


def wicker_basket(name, size, loc, parent, rot=(0, 0, 0)):
    """Rectangular bakery display basket: woven walls, a rolled rim, a linen liner."""
    w, d, h = size
    e = empty(name, loc, rot=rot, parent=parent)
    box(f"{name}_Bottom", (w, d, 0.012), (0, 0, 0.006), WICKER, bevel=0.004, parent=e)
    for sx in (-1, 1):
        box(f"{name}_End", (0.012, d, h), (sx * (w / 2 - 0.006), 0, h / 2), WICKER, bevel=0.004, parent=e)
    for sy in (-1, 1):
        box(f"{name}_Side", (w, 0.012, h * (0.7 if sy < 0 else 1)), (0, sy * (d / 2 - 0.006), h * (0.35 if sy < 0 else 0.5)),
            WICKER, bevel=0.004, parent=e)
    tube(f"{name}_Rim", [(-w / 2, -d / 2, h * 0.7), (w / 2, -d / 2, h * 0.7), (w / 2, d / 2, h), (-w / 2, d / 2, h)],
         0.008, WICKER, parent=e, closed=True, segs=6)
    o = 0.0035                                           # woven rows (the "rods" of a willow basket) proud of the walls
    for f in (0.28, 0.52):
        tube(f"{name}_Weave", [(-w / 2 - o, -d / 2 - o, h * 0.7 * f), (w / 2 + o, -d / 2 - o, h * 0.7 * f),
                               (w / 2 + o, d / 2 + o, h * f), (-w / 2 - o, d / 2 + o, h * f)],
             0.0045, WICKER_DARK, parent=e, closed=True, segs=5)
    box(f"{name}_Linen", (w - 0.03, d - 0.03, 0.008), (0, 0, 0.016), LINEN, bevel=0.003, parent=e)
    return e


def banquette(y0, y1, depth=0.56, seat_h=0.45):
    """Channel-back banquette along the left wall: recessed plinth, separate seat cushion, vertical channels."""
    L, cy = y1 - y0, (y0 + y1) / 2
    box("Banquette_Plinth", (depth - 0.08, L - 0.04, 0.1), ((depth - 0.08) / 2, cy, FLOOR_Z + 0.05), DARK_OAK, bevel=0.003)
    box("Banquette_Base", (depth, L, seat_h - 0.22), (depth / 2, cy, FLOOR_Z + 0.1 + (seat_h - 0.22) / 2), FABRIC,
        bevel=0.01)
    box("Banquette_Seat", (depth - 0.12, L - 0.02, 0.12), (0.12 + (depth - 0.12) / 2, cy, FLOOR_Z + seat_h - 0.06),
        FABRIC, bevel=0.03)
    n = int(L / 0.15)
    for k in range(n):
        yy = y0 + L * (k + 0.5) / n
        box("Banquette_Channel", (0.11, L / n - 0.008, 0.44), (0.07, yy, FLOOR_Z + seat_h + 0.2), FABRIC, bevel=0.045,
            rot=(0, R(-8), 0))
    box("Banquette_End", (depth, 0.04, seat_h + 0.05), (depth / 2, y1 - 0.02, FLOOR_Z + (seat_h + 0.05) / 2), FABRIC,
        bevel=0.012)


# =====================================================================
#  BACK BAR + BREAD WALL (decoration behind the counter)
# =====================================================================
BB_H = 0.9
bb_w = W - BB_X0 - 0.02
bbx, bby = BB_X0 + bb_w / 2, D - BB_D / 2
box("BackBar_Plinth", (bb_w, BB_D - 0.08, 0.1), (bbx, bby + 0.04, FLOOR_Z + 0.05), PLINTH, bevel=0.003)
box("BackBar_Carcass", (bb_w, BB_D - 0.02, BB_H - 0.13), (bbx, bby + 0.01, FLOOR_Z + 0.1 + (BB_H - 0.13) / 2),
    DARK_OAK_V, bevel=0.003)
box("BackBar_Worktop", (bb_w + 0.01, BB_D, 0.03), (bbx, bby, FLOOR_Z + BB_H - 0.015), OAK, bevel=0.003)
mods = 4
mw = bb_w / mods
for k in range(mods):                              # drawer banks and door pairs with 3 mm gaps and bar handles
    mx = BB_X0 + mw * (k + 0.5)
    fy = D - BB_D - 0.008
    if k % 2 == 0:
        for j, (zb, hh) in enumerate(((0.105, 0.26), (0.37, 0.2), (0.575, 0.18))):
            box("BackBar_Drawer", (mw - 0.006, 0.02, hh - 0.004), (mx, fy, FLOOR_Z + zb + hh / 2), DARK_OAK_V, bevel=0.002)
            tube("BackBar_Handle", [(mx - 0.08, fy - 0.011, FLOOR_Z + zb + hh - 0.05), (mx - 0.08, fy - 0.03,
                 FLOOR_Z + zb + hh - 0.05), (mx + 0.08, fy - 0.03, FLOOR_Z + zb + hh - 0.05),
                 (mx + 0.08, fy - 0.011, FLOOR_Z + zb + hh - 0.05)], 0.006, BRASS, segs=8)
    else:
        for sx in (-1, 1):
            dx = mx + sx * mw / 4
            box("BackBar_Door", (mw / 2 - 0.004, 0.02, 0.645), (dx, fy, FLOOR_Z + 0.105 + 0.3225), DARK_OAK_V, bevel=0.002)
            tube("BackBar_Handle", [(dx - sx * (mw / 4 - 0.04), fy - 0.011, FLOOR_Z + 0.58),
                                    (dx - sx * (mw / 4 - 0.04), fy - 0.03, FLOOR_Z + 0.6),
                                    (dx - sx * (mw / 4 - 0.04), fy - 0.03, FLOOR_Z + 0.72),
                                    (dx - sx * (mw / 4 - 0.04), fy - 0.011, FLOOR_Z + 0.74)], 0.006, BRASS, segs=8)

# Bread shelving on the worktop: oak uprights, two sloped shelves with a front lip, a flat top shelf.
TOP_Z = FLOOR_Z + BB_H
RACK_D = 0.38
ry = D - RACK_D / 2 - 0.01
bays = 3
bay_w = bb_w / bays
for k in range(bays + 1):
    ux = BB_X0 + 0.015 + k * (bb_w - 0.03) / bays
    box("BreadRack_Upright", (0.028, RACK_D, 0.64), (ux, ry, TOP_Z + 0.32), OAK_V, bevel=0.003)
box("BreadRack_Top", (bb_w, RACK_D, 0.024), (bbx, ry, TOP_Z + 0.64), OAK, bevel=0.003)
SLOPE = R(12)
for lvl, z_front in enumerate((TOP_Z + 0.05, TOP_Z + 0.33)):
    sh = empty("BreadRack_Shelf", (bbx, ry, z_front + math.sin(SLOPE) * RACK_D / 2), rot=(SLOPE, 0, 0))
    box("BreadRack_Board", (bb_w - 0.06, RACK_D, 0.02), (0, 0, 0), OAK, bevel=0.003, parent=sh)
    box("BreadRack_Lip", (bb_w - 0.06, 0.018, 0.06), (0, -RACK_D / 2 + 0.009, 0.03), OAK, bevel=0.003, parent=sh)
    for b in range(bays):
        bxc = -bb_w / 2 + bay_w * (b + 0.5)
        for j in (-1, 1):                              # little slate price tags clipped to the shelf lip
            box("BreadRack_Tag", (0.08, 0.004, 0.05), (bxc + j * bay_w / 4, -RACK_D / 2 - 0.002, 0.03), SLATE,
                bevel=0.001, parent=sh)
            box("BreadRack_Tag_Chalk", (0.05, 0.002, 0.006), (bxc + j * bay_w / 4, -RACK_D / 2 - 0.0045, 0.036),
                mat("chalk", 0.8, emit=0.3), bevel=0, parent=sh)
            box("BreadRack_Tag_Chalk", (0.03, 0.002, 0.005), (bxc + j * bay_w / 4, -RACK_D / 2 - 0.0045, 0.022),
                mat("chalk", 0.8, emit=0.3), bevel=0, parent=sh)
        if lvl == 0:                                  # lower level: wicker baskets of rolls and boules
            for j, sx in enumerate((-1, 1)):
                bk = wicker_basket(f"Basket_{b}_{j}", (bay_w / 2 - 0.05, 0.3, 0.1), (bxc + sx * bay_w / 4, 0.0, 0.01), sh)
                for q in range(2):
                    if (b + j) % 2:
                        boule(f"Basket_Boule_{b}_{j}_{q}", ((q - 0.5) * 0.15, 0.0, 0.02), bk, r=0.07)
                    else:
                        bloomer(f"Basket_Bloomer_{b}_{j}_{q}", (0, (q - 0.5) * 0.12, 0.02), bk, length=0.26)
        else:                                          # upper level: loaves straight on the board
            for q in range(3):
                qx = bxc + (q - 1) * bay_w / 3
                if random.random() < 0.5:
                    boule(f"Shelf_Boule_{b}_{q}", (qx, 0.02, 0.01), sh, r=random.uniform(0.07, 0.085))
                else:
                    bloomer(f"Shelf_Bloomer_{b}_{q}", (qx, 0.02, 0.01), sh, turn=R(90), length=0.22)
# On the top shelf: stacked plates, a jar of biscotti and kraft paper bags.
for k in range(4):
    cyl("Top_Plate", 0.11, 0.012, (BB_X0 + 0.3, ry, TOP_Z + 0.66 + k * 0.013), CERAMIC, bevel=0.003)
for k in range(6):
    box("Top_Paper_Bag", (0.16, 0.1, 0.012), (BB_X0 + 0.75, ry - 0.02, TOP_Z + 0.658 + k * 0.012), KRAFT, bevel=0.002,
        rot=(0, 0, R(random.uniform(-6, 6))))
# Tall baguette basket standing at the end of the counter run.
bgx, bgy = 4.2, 3.27
lathe("Baguette_Basket", [(0, 0), (0.1, 0), (0.12, 0.45), (0.13, 0.46), (0.115, 0.47), (0.105, 0.03), (0, 0.03)],
      (bgx, bgy, FLOOR_Z), WICKER, segs=28)
for k in range(7):
    a = k * 2.4
    baguette(f"Basket_Baguette_{k}", (bgx + math.cos(a) * 0.05, bgy + math.sin(a) * 0.05, FLOOR_Z + 0.36 + (k % 3) * 0.04),
             None, rot=(0, R(-90 + random.uniform(-9, 9)), a), length=0.62)


# =====================================================================
#  OUTSIDE: pavement, awning, A-board, bracket sign, box balls
# =====================================================================
PAVE_X, PAVE_Y = -T - 0.95, -0.7           # outer edges of the pavement strip
if PAVEMENT:
    box("Pavement_Base", (W - PAVE_X, -PAVE_Y, 0.18), ((W + PAVE_X) / 2, PAVE_Y / 2, -0.15), mat("dark", 0.9),
        bevel=0.01)
    box("Pavement_Base_Side", (-T - PAVE_X, D + T, 0.18), ((-T + PAVE_X) / 2, (D + T) / 2, -0.15), mat("dark", 0.9),
        bevel=0.01)
    pav = M("pavement", 0.85, "concrete")
    step = 0.45                                             # 450 mm concrete flags
    x = PAVE_X + 0.15
    while x < W - 0.01:
        pw = min(step, W - x)
        for y0, y1 in ((PAVE_Y + 0.15, PAVE_Y / 2 + 0.07), (PAVE_Y / 2 + 0.07, 0.0)):
            box("Paver", (pw - 0.008, y1 - y0 - 0.008, 0.05), (x + pw / 2, (y0 + y1) / 2, -0.065), pav, bevel=0.004)
        x += step
    y = 0.0
    while y < D + T - 0.01:
        ph = min(step, D + T - y)
        for x0, x1 in ((PAVE_X + 0.15, (PAVE_X - T) / 2), ((PAVE_X - T) / 2, -T)):
            box("Paver", (x1 - x0 - 0.008, ph - 0.008, 0.05), ((x0 + x1) / 2, y + ph / 2, -0.065), pav, bevel=0.004)
        y += step
    curb = M("cream", 0.8, "concrete")
    box("Curb_Front", (W - PAVE_X, 0.15, 0.09), ((W + PAVE_X) / 2, PAVE_Y + 0.075, -0.05), curb, bevel=0.012)
    box("Curb_Side", (0.15, D + T - PAVE_Y, 0.09), (PAVE_X + 0.075, (D + T + PAVE_Y) / 2, -0.05), curb, bevel=0.012)

    # A-board (61 x 107 cm) on the pavement - click it to email you.
    af = empty("AFrame", (-0.3, -0.36, -0.04), rot=(0, 0, R(45)))
    for side, tilt in ((-1, R(-12)), (1, R(12))):
        leg = empty("AFrame_Side", (0, side * 0.11, 0.52), rot=(tilt, 0, 0), parent=af)
        for sx in (-1, 1):
            box("AFrame_Rail", (0.045, 0.028, 1.07), (sx * 0.2825, 0, 0), OAK_V, bevel=0.004, parent=leg)
        for sz in (-1, 1):
            box("AFrame_Rail", (0.52, 0.028, 0.045 if sz > 0 else 0.08), (0, 0, sz * (0.5 if sz > 0 else 0.4)), OAK,
                bevel=0.004, parent=leg)
        slate = box("AFrame_Slate", (0.52, 0.012, 0.86), (0, 0, 0.04), SLATE,
                    bevel=0.002, parent=leg)
        if side < 0:
            hook_link(slate, "email")
            chalk = mat("chalk", 0.8, emit=0.5)
            label("AFrame_Text_1", "say hi!", 0.1, (0, -0.012, 0.33), chalk, parent=leg)
            box("AFrame_Rule", (0.3, 0.002, 0.006), (0, -0.008, 0.24), chalk, bevel=0, parent=leg)
            for k, t in enumerate(("flat white", "sourdough", "cinnamon buns", "& good ideas")):
                label(f"AFrame_Text_{k + 2}", t, 0.046, (0, -0.012, 0.16 - k * 0.075), chalk, parent=leg)
            cup = [(-0.07, -0.008, -0.2), (-0.06, -0.008, -0.29), (-0.03, -0.008, -0.33), (0.03, -0.008, -0.33),
                   (0.06, -0.008, -0.29), (0.07, -0.008, -0.2)]
            tube("AFrame_Chalk_Cup", spline(cup, 4), 0.005, chalk, parent=leg, segs=5)
            tube("AFrame_Chalk_Handle", spline([(0.065, -0.008, -0.22), (0.1, -0.008, -0.23), (0.095, -0.008, -0.27),
                                                (0.055, -0.008, -0.28)], 4), 0.005, chalk, parent=leg, segs=5)
            tube("AFrame_Chalk_Saucer", [(-0.11, -0.008, -0.35), (0.11, -0.008, -0.35)], 0.005, chalk, parent=leg, segs=5)
            for k in range(3):
                tube("AFrame_Chalk_Steam", spline([(-0.03 + k * 0.03, -0.008, -0.17), (-0.04 + k * 0.03, -0.008, -0.14),
                                                   (-0.02 + k * 0.03, -0.008, -0.11)], 4), 0.004, chalk, parent=leg, segs=5)
    for sx in (-1, 1):
        tube("AFrame_Chain", [(sx * 0.24, -0.03, 0.3), (sx * 0.24, 0.0, 0.26), (sx * 0.24, 0.03, 0.3)], 0.003, IRON,
             parent=af, segs=5)
    # A clipped box ball in a square fibre-clay planter by the corner of the shop.
    for k, (px, py) in enumerate(((-0.86, -0.4),)):
        box("Planter", (0.36, 0.36, 0.36), (px, py, 0.14), POT_CLAY, bevel=0.01)
        cyl("Planter_Soil", 0.15, 0.01, (px, py, 0.315), SOIL, bevel=0)
        foliage("BoxBall", [((px, py, 0.5), 0.17)], 900, (0.03, 0.016), mat("plant", 0.6, color="#4E6B3A"),
                seed=k + 3, droop=0.0)
        ball("BoxBall_Core", 0.15, (px, py, 0.5), mat("plant", 0.8, color="#3A5230"))

# Canvas shop awning over the door and window: roller box, striped canvas, scalloped valance, folding arms.
if AWNING:
    AW_Y0, AW_Y1, AW_LEN, AW_SLOPE = 0.05, WIN_Y[1] + 0.15, 0.95, 18
    stripes = 14
    sw = (AW_Y1 - AW_Y0) / stripes
    z0, x0 = H - 0.12, -T - 0.08
    xo, zo = x0 - AW_LEN * math.cos(R(AW_SLOPE)), z0 - AW_LEN * math.sin(R(AW_SLOPE))
    for i in range(stripes):
        cm = M("accent_1", 0.85, "fabric") if i % 2 == 0 else M("cream", 0.86, "fabric")
        cy_ = AW_Y0 + sw * (i + 0.5)
        no_shadow(
            box(f"Awning_Stripe_{i}", (AW_LEN, sw + 0.001, 0.008), ((x0 + xo) / 2, cy_, (z0 + zo) / 2), cm, bevel=0.002,
                rot=(0, R(-AW_SLOPE), 0)),
            box(f"Awning_Valance_{i}", (0.008, sw + 0.001, 0.16), (xo - 0.005, cy_, zo - 0.075), cm, bevel=0.002),
            ball(f"Awning_Scallop_{i}", sw * 0.5, (xo - 0.005, cy_, zo - 0.155), cm, scale=(0.02, 1, 0.5)))
    no_shadow(box("Awning_FrontBar", (0.03, AW_Y1 - AW_Y0, 0.03), (xo, (AW_Y0 + AW_Y1) / 2, zo + 0.005), IRON, bevel=0.004),
              box("Awning_RollerBox", (0.14, AW_Y1 - AW_Y0 + 0.06, 0.14), (-T - 0.07, (AW_Y0 + AW_Y1) / 2, z0 + 0.03),
                  PAINT, bevel=0.01))
    for yy in (AW_Y0 + 0.1, AW_Y1 - 0.1):              # folding lateral arms with an elbow
        a, b = Vector((-T, yy, z0 - 0.45)), Vector((xo + 0.03, yy, zo))
        elbow = (a + b) / 2 + Vector((0.05, 0, -0.12))
        no_shadow(tube("Awning_Arm", [a, elbow, b], 0.012, IRON, segs=8))
        no_shadow(cyl("Awning_Arm_Bracket", 0.025, 0.04, (-T - 0.02, yy, z0 - 0.45), IRON, rot=(0, R(90), 0), segs=12))

# Iron bracket sign at the corner of the shop - click it to open your website.
bracket_y = -0.09
sign_x = -T - 0.4
tube("BracketSign_Arm", [(-T, bracket_y, 2.45), (-T - 0.72, bracket_y, 2.45)], 0.012, IRON, segs=8)
tube("BracketSign_Scroll", spline([(-T, bracket_y, 2.2), (-T - 0.2, bracket_y, 2.3), (-T - 0.35, bracket_y, 2.42),
                                   (-T - 0.5, bracket_y, 2.45)], 5), 0.009, IRON, segs=8)
tube("BracketSign_Curl", [(-T - 0.1 + (0.045 - a * 0.005) * math.cos(a), bracket_y,
                          2.31 + (0.045 - a * 0.005) * math.sin(a)) for a in (k * 0.4 for k in range(16))], 0.006, IRON,
     segs=6)
for k in (-1, 1):
    tube("BracketSign_Hanger", [(sign_x + k * 0.2, bracket_y, 2.44), (sign_x + k * 0.2, bracket_y, 2.37)], 0.004, IRON,
         segs=6)
blade = box("BracketSign", (0.5, 0.035, 0.36), (sign_x, bracket_y, 2.18), PAINT, bevel=0.008)
hook_link(blade, "website")
for side in (-1, 1):
    box("BracketSign_Border", (0.44, 0.004, 0.3), (sign_x, bracket_y + side * 0.019, 2.18), GOLD_LEAF, bevel=0.0)
    box("BracketSign_Field", (0.42, 0.004, 0.28), (sign_x, bracket_y + side * 0.021, 2.18), PAINT, bevel=0.0)
    emblem = croissant(f"BracketSign_Croissant_{side}", (sign_x, bracket_y + side * 0.02, 2.22), None, s=2.0,
                       mats=(GOLD_LEAF, BRASS))
    emblem.rotation_euler, emblem.scale = (R(-90 * side), R(180), 0), (1, 1, 0.4)   # carved, gilded, horns down


# =====================================================================
#  FURNITURE SLOTS  (same names in every template)
#  size = (width, depth, height); front of the furniture faces local -Y
# =====================================================================
COUNTER_Y = 2.6                                     # centre line of the service counter
COUNTER_H = 0.92                                    # real counter height
slot("display_case", (0.9, 0.75, 1.3), (2.25, COUNTER_Y), shape="cabinet")
slot("counter",      (1.6, 0.68, COUNTER_H), (3.56, COUNTER_Y), shape="counter")
slot("hero_prop",    (0.69, 0.56, 0.53), (3.92, COUNTER_Y + 0.02), z=FLOOR_Z + COUNTER_H, kind="surface",
     shape="box")
slot("pendant_lamp", (1.5, 0.4, 1.12), (3.56, COUNTER_Y), z=H - 1.12, kind="hanging", shape="lamp")
slot("stool",        (0.95, 0.4, 0.66), (3.85, 1.98), shape="stool")
slot("table",        (0.62, 0.62, 0.75), (0.92, 2.85), shape="table")
slot("chair",        (0.44, 0.5, 0.9), (1.5, 2.85), turn=-90, shape="chair")
slot("wall_shelf",   (0.8, 0.22, 0.6), (1.25, D - 0.11), z=1.62, kind="wall", shape="shelf")
slot("plant",        (0.5, 0.5, 1.6), (1.45, 3.62), shape="plant")


# =====================================================================
#  LIGHTS helper (the pendants carry their own bulbs)
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


# =====================================================================
#  PLACEHOLDER FURNITURE  (replaced when you add your own with add_furniture.py)
# =====================================================================
def fluted_front(name, root, x0, x1, y, z0, z1, axis="x"):
    """Reeded joinery: half-round dark-oak battens (34 mm pitch) side by side."""
    n = max(1, int(round(abs(x1 - x0) / 0.034)))
    pitch = (x1 - x0) / n
    for k in range(n):
        c = x0 + pitch * (k + 0.5)
        loc = (c, y, (z0 + z1) / 2) if axis == "x" else (y, c, (z0 + z1) / 2)
        cyl(name, abs(pitch) * 0.5, z1 - z0, loc, DARK_OAK_V, segs=10, bevel=0.002, parent=root)


def build_counter():
    """Bespoke bakery counter: recessed plinth, fluted dark-oak front and end, 30 mm marble top."""
    root, w, d, h = furniture_root("counter")
    box("Counter_Plinth", (w - 0.04, d - 0.1, 0.1), (0, 0.04, 0.05), PLINTH, bevel=0.003, parent=root)
    box("Counter_Carcass", (w, d - 0.04, h - 0.13), (0, 0.02, 0.1 + (h - 0.13) / 2), DARK_OAK, bevel=0.003, parent=root)
    fluted_front("Counter_Flute", root, -w / 2 + 0.01, w / 2 - 0.01, -d / 2 + 0.03, 0.12, h - 0.04)
    fluted_front("Counter_Flute_End", root, -d / 2 + 0.04, d / 2 - 0.02, w / 2 - 0.0, 0.12, h - 0.04, axis="y")
    box("Counter_Top", (w + 0.05, d + 0.04, 0.03), (0.0, -0.01, h - 0.015), MARBLE, bevel=0.004, parent=root)
    top = h
    # left end: cake under a glass dome, card reader on its dock, tablet till, paper-cup stack
    cake_dome("Counter_Cake", (-w / 2 + 0.16, -0.06, top), parent=root)
    rx, ry_ = -w / 2 + 0.38, -d / 2 + 0.1
    box("CardReader_Dock", (0.09, 0.08, 0.03), (rx, ry_, top + 0.015), mat("cream", 0.4), bevel=0.012, parent=root)
    rd = empty("CardReader", (rx, ry_ + 0.01, top + 0.03), rot=(R(-58), 0, R(-10)), parent=root)
    box("CardReader_Body", (0.083, 0.018, 0.083), (0, 0, 0.04), mat("dark", 0.35), bevel=0.008, parent=rd)
    box("CardReader_Screen", (0.066, 0.002, 0.05), (0, -0.0095, 0.05), mat("cream", 0.3, emit=0.6, color="#CFE3E8"),
        bevel=0, parent=rd)
    tx, ty = -w / 2 + 0.3, d / 2 - 0.14
    cyl("Till_Base", 0.07, 0.014, (tx, ty, top + 0.007), mat("cream", 0.4), bevel=0.004, parent=root)
    cyl("Till_Neck", 0.014, 0.12, (tx, ty, top + 0.07), INOX, segs=12, parent=root)
    tb = empty("Till_Tablet", (tx, ty, top + 0.15), rot=(R(-70), 0, R(180)), parent=root)
    box("Till_Tablet_Body", (0.25, 0.008, 0.175), (0, 0, 0), mat("dark", 0.3), bevel=0.006, parent=tb)
    box("Till_Tablet_Screen", (0.23, 0.002, 0.155), (0, -0.005, 0), mat("cream", 0.3, emit=0.5, color="#E8F0F3"),
        bevel=0, parent=tb)
    for s in range(6):                                   # takeaway cups with lids, stacked
        lathe("Counter_Paper_Cup", [(0, 0), (0.028, 0), (0.042, 0.11), (0.04, 0.11), (0.026, 0.004), (0, 0.004)],
              (-w / 2 + 0.07, d / 2 - 0.08, top + s * 0.018), PAPER, segs=20, parent=root)
    cyl("Counter_Cup_Lid", 0.044, 0.012, (-w / 2 + 0.07, d / 2 - 0.08, top + 0.205), mat("cream", 0.4), parent=root)
    # grinder (Super Jolly style) beside the machine, a knock box and milk jugs
    g = empty("Grinder", (-w / 2 + 0.55, -0.05, top), parent=root)
    box("Grinder_Base", (0.2, 0.3, 0.03), (0, 0.02, 0.015), CHROME, bevel=0.008, parent=g)
    box("Grinder_Body", (0.16, 0.22, 0.26), (0, 0.04, 0.16), CHROME, bevel=0.03, parent=g)
    cyl("Grinder_Burrs", 0.07, 0.05, (0, 0.04, 0.315), CHROME, bevel=0.008, parent=g)
    no_shadow(cyl("Grinder_Doser", 0.055, 0.09, (0, -0.1, 0.22), mat("glass", 0.05, alpha=0.35), bevel=0.004, parent=g))
    box("Grinder_Lever", (0.015, 0.09, 0.015), (0.07, -0.12, 0.2), mat("dark", 0.4), bevel=0.004, rot=(0, 0, R(-20)),
        parent=g)
    box("Grinder_Fork", (0.06, 0.06, 0.008), (0, -0.12, 0.12), CHROME, bevel=0.002, parent=g)
    no_shadow(lathe("Grinder_Hopper", [(0.03, 0.34), (0.1, 0.56), (0.105, 0.57), (0.0, 0.57)], (0, 0.04, 0),
                    mat("glass", 0.1, alpha=0.4, color="#9A8A7A"), parent=g))
    lathe("Grinder_Beans", [(0.0, 0.35), (0.032, 0.35), (0.075, 0.47), (0.0, 0.48)], (0, 0.04, 0), CHOC, parent=g)
    cyl("Grinder_Lid", 0.108, 0.02, (0, 0.04, 0.58), mat("dark", 0.4), bevel=0.006, parent=g)
    kx, ky = -w / 2 + 0.71, -d / 2 + 0.12
    lathe("Counter_KnockBox", [(0, 0), (0.06, 0), (0.065, 0.09), (0.058, 0.09), (0.05, 0.02), (0, 0.02)], (kx, ky, top),
          mat("dark", 0.6), segs=24, parent=root)
    cyl("Counter_KnockBar", 0.008, 0.12, (kx, ky, top + 0.08), mat("dark", 0.4), rot=(0, R(90), 0), segs=10, parent=root)
    for k in range(2):                                   # 350 ml steaming pitchers: belly, pinched spout, C handle
        jx, jy = w / 2 - 0.045, d / 2 - 0.06 - k * 0.11
        lathe("Counter_Milk_Jug", [(0, 0), (0.036, 0), (0.04, 0.035), (0.036, 0.075), (0.031, 0.1), (0.029, 0.1),
                                   (0.034, 0.075), (0.037, 0.035), (0.033, 0.004), (0, 0.004)], (jx, jy, top), INOX,
              segs=24, parent=root)
        box("Counter_Milk_Jug_Spout", (0.03, 0.022, 0.006), (jx - 0.034, jy, top + 0.099), INOX, bevel=0.002,
            rot=(0, R(-20), 0), parent=root)
        tube("Counter_Milk_Jug_Handle", spline([(jx + 0.031, jy, top + 0.088), (jx + 0.055, jy, top + 0.075),
                                                (jx + 0.05, jy, top + 0.03), (jx + 0.036, jy, top + 0.022)], 4),
             0.0045, INOX, parent=root, segs=8)


def build_display_case():
    """Curved-glass patisserie cabinet: fluted base, stainless deck, two stepped glass shelves, LED canopy."""
    root, w, d, h = furniture_root("display_case")
    box("Case_Plinth", (w - 0.04, d - 0.12, 0.1), (0, 0.05, 0.05), PLINTH, bevel=0.003, parent=root)
    box("Case_Body", (w, d - 0.06, 0.74), (0, 0.03, 0.47), DARK_OAK, bevel=0.003, parent=root)
    fluted_front("Case_Flute", root, -w / 2 + 0.01, w / 2 - 0.01, -d / 2 + 0.06, 0.12, 0.82)
    deck_z = 0.86
    box("Case_Deck", (w, d - 0.02, 0.02), (0, 0.0, deck_z - 0.01), INOX, bevel=0.003, parent=root)
    box("Case_Rail", (w, 0.03, 0.03), (0, -d / 2 + 0.02, deck_z - 0.01), INOX, bevel=0.004, parent=root)
    # curved front glass: a quarter ellipse from the front of the deck up to the canopy
    gy0, gz_top = -d / 2 + 0.02, h - 0.02
    yc, ry_, rz_ = gy0 + 0.3, 0.3, gz_top - deck_z
    bm = bmesh.new()
    cols = []
    for i in range(13):
        a = R(90) * i / 12
        yy, zz = yc - ry_ * math.cos(a), deck_z + rz_ * math.sin(a)
        cols.append([bm.verts.new((sx * (w / 2 - 0.01), yy, zz)) for sx in (-1, 1)])
    for a_, b_ in zip(cols, cols[1:]):
        bm.faces.new((a_[0], a_[1], b_[1], b_[0]))
    glass = _obj("Case_Glass_Front", bm)
    no_shadow(_finish(glass, GLASS, 0, None, root))
    for sx in (-1, 1):                                  # end glass + stainless end profile following the curve
        prof = [(sx * (w / 2 - 0.01), yc - ry_ * math.cos(R(90) * i / 12), deck_z + rz_ * math.sin(R(90) * i / 12))
                for i in range(13)]
        bm = bmesh.new()
        vs = [bm.verts.new(p) for p in prof + [(sx * (w / 2 - 0.01), d / 2 - 0.02, gz_top),
                                                (sx * (w / 2 - 0.01), d / 2 - 0.02, deck_z)]]
        bm.faces.new(vs)
        no_shadow(_finish(_obj("Case_Glass_End", bm), GLASS, 0, None, root))
        tube("Case_End_Profile", prof, 0.008, INOX, parent=root, segs=8)
    no_shadow(box("Case_Glass_Back", (w - 0.02, 0.006, gz_top - deck_z), (0, d / 2 - 0.02, (deck_z + gz_top) / 2), GLASS,
                  bevel=0, parent=root))
    box("Case_Canopy", (w, d / 2 + 0.04, 0.025), (0, yc + (d / 2 + 0.04) / 2 - 0.03, h - 0.0125), INOX, bevel=0.004,
        parent=root)
    box("Case_LED", (w - 0.06, 0.02, 0.004), (0, yc + 0.02, h - 0.028), mat("chalk", 0.3, emit=1.6), bevel=0,
        parent=root)
    shelves = ((deck_z + 0.16, yc - 0.12, d / 2 - 0.03), (deck_z + 0.3, yc + 0.0, d / 2 - 0.03))
    for k, (sz, sy0, sy1) in enumerate(shelves):
        no_shadow(box("Case_Shelf", (w - 0.04, sy1 - sy0, 0.008), (0, (sy0 + sy1) / 2, sz), GLASS, bevel=0, parent=root))
        for sx in (-1, 1):
            box("Case_Shelf_Bracket", (0.012, sy1 - sy0, 0.02), (sx * (w / 2 - 0.025), (sy0 + sy1) / 2, sz - 0.014),
                INOX, bevel=0.002, parent=root)
    # trays: oak boards on the deck and shelves, each with one kind of pastry in rows (like a real cabinet)
    trays = [(deck_z, -0.07), (deck_z, 0.12), (shelves[0][0] + 0.004, (shelves[0][1] + shelves[0][2]) / 2),
             (shelves[1][0] + 0.004, (shelves[1][1] + shelves[1][2]) / 2)]
    n = 0
    for tz, ty in trays:
        for tx in (-w / 4 + 0.01, w / 4 - 0.01):
            box("Case_Tray", (w / 2 - 0.06, 0.15, 0.012), (tx, ty, tz + 0.006), OAK, bevel=0.002, parent=root)
            kind = random.choice(["croissant", "pain", "cinnamon", "tart"] if not BAKERY_PROPS else
                                 ["macaron", "tart", "cinnamon", "croissant"])
            per = {"croissant": 3, "pain": 3, "tart": 3, "cinnamon": 4, "macaron": 6}[kind]
            rows = (-0.035, 0.035) if kind in ("pain", "cinnamon", "macaron") else (0.0,)   # packed like a real tray
            for i in range(per):
                for dy in rows:
                    px = tx - (w / 2 - 0.1) / 2 + (w / 2 - 0.1) * (i + 0.5) / per + dy * 0.3
                    pastry(f"Case_Pastry_{n}", (px, ty + dy, tz + 0.012), root, kind=kind)
                    n += 1
            if tz == deck_z:                               # little price tag on a pick
                box("Case_Tag", (0.05, 0.003, 0.03), (tx, ty - 0.085, tz + 0.06), mat("chalk", 0.6), bevel=0,
                    rot=(R(-20), 0, 0), parent=root)
    cake_dome("Case_Top_Cake", (w / 2 - 0.2, 0.12, h), parent=root, chocolate=True)    # cake stand on the cabinet top


def build_hero_prop():
    """Two-group commercial espresso machine (Linea Classic proportions, no logo): W69 D56 H53 cm."""
    root, w, d, h = furniture_root("hero_prop")
    fy = -d / 2 + 0.1                                    # front face of the body
    for sx in (-1, 1):
        for sy in (-1, 1):
            cyl("Espresso_Foot", 0.018, 0.08, (sx * (w / 2 - 0.06), sy * (d / 2 - 0.08) + 0.04, 0.04), CHROME, segs=12,
                parent=root)
    box("Espresso_Body", (w, d - 0.1, 0.38), (0, 0.05, 0.27), STEEL, bevel=0.006, parent=root)
    for sx in (-1, 1):
        box("Espresso_Side_Panel", (0.004, d - 0.14, 0.32), (sx * (w / 2 + 0.002), 0.05, 0.27), STEEL, bevel=0.002,
            parent=root)
    box("Espresso_Front_Band", (w - 0.02, 0.006, 0.12), (0, fy - 0.003, 0.4), INOX, bevel=0.002, parent=root)
    box("Espresso_DripTray", (w - 0.08, 0.2, 0.035), (0, fy - 0.06, 0.1), INOX, bevel=0.004, parent=root)
    for k in range(9):
        box("Espresso_Grate", (0.006, 0.18, 0.004), (-w / 2 + 0.07 + k * (w - 0.14) / 8, fy - 0.06, 0.12), CHROME,
            bevel=0, parent=root)
    for gi, sx in enumerate((-1, 1)):
        gx = sx * 0.17
        # saturated group: a round chrome neck out of the front panel, a vertical group with a flange,
        # then the portafilter (chrome basket ring, black handle, twin spouts) locked in underneath
        gy = fy - 0.06
        cyl("Espresso_Group_Neck", 0.03, 0.07, (gx, fy - 0.03, 0.315), CHROME, rot=(R(90), 0, 0), segs=20, parent=root)
        lathe("Espresso_Group", [(0, 0.0), (0.046, 0.0), (0.048, 0.008), (0.04, 0.012), (0.04, 0.06), (0.036, 0.075),
                                 (0.022, 0.085), (0, 0.087)], (gx, gy, 0.272), CHROME, segs=28, parent=root)
        lathe("Espresso_Portafilter", [(0, 0.0), (0.03, 0.0), (0.042, 0.008), (0.045, 0.024), (0.0, 0.024)],
              (gx, gy, 0.245), CHROME, segs=24, parent=root)
        tube("Espresso_Handle_Arm", [(gx, gy - 0.04, 0.257), (gx + sx * 0.012, gy - 0.075, 0.255)], 0.009, CHROME,
             parent=root, segs=10)
        tube("Espresso_Handle", [(gx + sx * 0.012, gy - 0.075, 0.255), (gx + sx * 0.03, gy - 0.15, 0.243),
                                 (gx + sx * 0.045, gy - 0.2, 0.236)], 0.0135, mat("dark", 0.35), parent=root, segs=12,
             r2=0.0165)
        for k in (-1, 1):
            cyl("Espresso_Spout", 0.006, 0.025, (gx + k * 0.012, gy, 0.234), CHROME, segs=10, bevel=0.001, parent=root)
        make_cup(f"Espresso_Shot_{gi}", (gx, gy, 0.122), root, saucer=False, size=0.75, latte=False)
        kp = box("Espresso_Keypad", (0.09, 0.006, 0.045), (gx, fy - 0.007, 0.415), mat("dark", 0.3), bevel=0.003,
                 parent=root)
        for b in range(4):
            cyl("Espresso_Key", 0.007, 0.004, (gx - 0.03 + b * 0.02, fy - 0.011, 0.418), mat("chalk", 0.4, emit=0.4),
                rot=(R(90), 0, 0), segs=10, bevel=0, parent=root)
        wx = sx * (w / 2 - 0.05)                                  # steam wands + valve knobs at both corners
        cyl("Espresso_Steam_Knob", 0.022, 0.035, (wx, fy - 0.02, 0.4), mat("dark", 0.35), rot=(R(90), 0, 0), segs=16,
            parent=root)
        tube("Espresso_Steam_Wand", spline([(wx, fy - 0.01, 0.33), (wx + sx * 0.02, fy - 0.07, 0.31),
                                            (wx + sx * 0.03, fy - 0.09, 0.22), (wx + sx * 0.03, fy - 0.08, 0.15)], 4),
             0.007, CHROME, parent=root, segs=8)
    cyl("Espresso_Gauge_Bezel", 0.04, 0.02, (0, fy - 0.01, 0.4), CHROME, rot=(R(90), 0, 0), segs=28, parent=root)
    cyl("Espresso_Gauge_Face", 0.033, 0.004, (0, fy - 0.021, 0.4), mat("chalk", 0.3), rot=(R(90), 0, 0), segs=28,
        bevel=0, parent=root)
    box("Espresso_Gauge_Needle", (0.026, 0.002, 0.004), (0.006, fy - 0.024, 0.405), mat("accent_1", 0.4), bevel=0,
        rot=(0, R(-30), 0), parent=root)
    tube("Espresso_Water_Spout", [(0, fy - 0.01, 0.33), (0, fy - 0.06, 0.31), (0, fy - 0.07, 0.24)], 0.006, CHROME,
         parent=root, segs=8)
    box("Espresso_Cup_Tray", (w - 0.04, d - 0.14, 0.012), (0, 0.05, 0.466), INOX, bevel=0.003, parent=root)
    rail = [(-w / 2 + 0.03, fy + 0.02, 0.5), (-w / 2 + 0.03, d / 2 - 0.04, 0.5), (w / 2 - 0.03, d / 2 - 0.04, 0.5),
            (w / 2 - 0.03, fy + 0.02, 0.5)]
    tube("Espresso_Cup_Rail", rail, 0.006, CHROME, parent=root, segs=8)
    for sx in (-1, 1):
        for sy in (-1, 1):
            cyl("Espresso_Rail_Post", 0.005, 0.03, (sx * (w / 2 - 0.03), (fy + 0.02) if sy < 0 else (d / 2 - 0.04), 0.485),
                CHROME, segs=8, parent=root)
    for k in range(6):                                     # cups on the cup warmer
        make_cup(f"Espresso_Top_Cup_{k}", (-w / 2 + 0.12 + (k % 3) * 0.2, 0.0 + (k // 3) * 0.13, 0.472), root,
                 saucer=False, size=0.8, latte=False)


def build_pendant_lamp():
    """Three enamel dome pendants (dia 36 cm): dark enamel outside, white inside, a bulb and a ceiling rose."""
    root, w, d, h = furniture_root("pendant_lamp")
    enamel = M("joinery", 0.25, "ceramic") if not BAKERY_PROPS else M("cream", 0.24, "ceramic")
    inner = mat("cream", 0.4, emit=0.35)
    bulb = mat("bulb", 0.2, emit=12.0, color="#FFE2B0")
    for k, px in enumerate((-0.55, 0.0, 0.55)):
        drop = h - 0.12
        tube("Pendant_Cord", [(px, 0, h + 0.1), (px, 0, h - drop + 0.06)], 0.0035, mat("dark", 0.5), parent=root, segs=6)
        sz = h - drop
        cyl("Pendant_Holder", 0.02, 0.06, (px, 0, sz + 0.07), BRASS, segs=14, parent=root)
        lathe("Pendant_Shade", [(0.18, -0.12), (0.176, -0.11), (0.14, -0.05), (0.07, 0.01), (0.03, 0.04), (0.03, 0.05),
                                (0.0, 0.05)], (px, 0, sz), enamel, segs=40, parent=root)
        no_shadow(lathe("Pendant_Shade_Inner", [(0.172, -0.118), (0.136, -0.054), (0.067, 0.004), (0.0, 0.03)],
                        (px, 0, sz - 0.004), inner, segs=40, parent=root))
        no_shadow(ball("Pendant_Bulb", 0.045, (px, 0, sz - 0.07), bulb, scale=(1, 1, 1.2), parent=root))
        lamp = light(f"Light_Pendant_{k}", "POINT", LAMP_STRENGTH, kelvin(LAMP_WARMTH), (0, 0, 0), size=0.04)
        lamp.parent = root
        lamp.location = (px, 0, sz - 0.08)


def build_stool():
    """Two bentwood counter stools: caned seat at 65 cm, four splayed legs, a foot ring and a seat apron ring."""
    root, w, d, h = furniture_root("stool")
    wood = DARK_OAK_V
    for k, sx in enumerate((-w / 4, w / 4)):
        sh = h - 0.01
        cyl("Stool_Seat_Rim", 0.18, 0.035, (sx, 0, sh - 0.0175), wood, bevel=0.005, segs=36, parent=root)
        cyl("Stool_Seat_Cane", 0.16, 0.006, (sx, 0, sh + 0.002), CANE, bevel=0.001, segs=36, parent=root)
        tube("Stool_Seat_Ring", ring_pts(0.17, sh + 0.002, 36, sx, 0), 0.011, wood, parent=root, closed=True)
        for a in range(4):
            ang = R(45 + a * 90)
            ca, sa = math.cos(ang), math.sin(ang)
            tube("Stool_Leg", [(sx + ca * 0.19, sa * 0.19, 0.0), (sx + ca * 0.12, sa * 0.12, sh - 0.035)], 0.014, wood,
                 parent=root, r2=0.016, segs=10)
        tube("Stool_Foot_Ring", ring_pts(0.152, 0.24, 36, sx, 0), 0.01, wood, parent=root, closed=True)
        tube("Stool_Apron_Ring", ring_pts(0.128, sh - 0.12, 36, sx, 0), 0.008, wood, parent=root, closed=True)


def build_table():
    root, w, d, h = furniture_root("table")
    bistro_table(root, h, top_r=0.3)
    # 15-inch laptop facing the chair (towards +x / the camera), a flat white and a croissant
    lap = empty("Laptop", (0.02, 0.0, h), rot=(0, 0, R(90)), parent=root)
    alu = M("metal", 0.35, "brushed", metal=0.9, along="Y")
    box("Laptop_Base", (0.35, 0.24, 0.015), (0, -0.03, 0.0075), alu, bevel=0.004, parent=lap)
    box("Laptop_Keys", (0.28, 0.1, 0.002), (0, -0.0, 0.0155), mat("dark", 0.5), bevel=0, parent=lap)
    box("Laptop_Trackpad", (0.12, 0.07, 0.001), (0, -0.1, 0.0152), alu, bevel=0, parent=lap)
    lid = empty("Laptop_Lid", (0, 0.09, 0.015), rot=(R(-12), 0, 0), parent=lap)
    box("Laptop_Lid_Back", (0.35, 0.007, 0.235), (0, 0.004, 0.1175), alu, bevel=0.004, parent=lid)
    box("Laptop_Bezel", (0.34, 0.002, 0.225), (0, -0.0005, 0.1175), mat("dark", 0.3), bevel=0, parent=lid)
    screen = hook_image("screen", 1, (0.32, 0.2), (0, -0.002, 0.12), parent=lid, glow=True, default_key="main")
    hook_default(screen,
                 box("Laptop_UI_Bar", (0.3, 0.002, 0.025), (0, -0.0035, 0.205), mat("cream", 0.5, emit=0.8), bevel=0,
                     parent=lid),
                 box("Laptop_UI_Card", (0.13, 0.002, 0.11), (-0.075, -0.0035, 0.11), mat("accent_2", 0.5, emit=0.8),
                     bevel=0, parent=lid),
                 box("Laptop_UI_Card", (0.13, 0.002, 0.11), (0.075, -0.0035, 0.11), mat("accent_1", 0.5, emit=0.8),
                     bevel=0, parent=lid))
    make_cup("Table_Latte", (0.17, -0.17, h), root)
    lathe("Table_Plate", [(0, 0), (0.07, 0), (0.09, 0.012), (0.085, 0.013), (0.06, 0.006), (0, 0.006)], (0.17, 0.17, h),
          CERAMIC, parent=root)
    croissant("Table_Croissant", (0.17, 0.17, h + 0.006), root, turn=R(30))


def build_chair():
    root, w, d, h = furniture_root("chair")
    bentwood_chair(root)


def build_wall_shelf():
    """Two oak shelves on black steel brackets: retail coffee pouches, glass jars, cups and a trailing plant."""
    root, w, d, h = furniture_root("wall_shelf")
    hook_link(root, "github")
    by = d / 2 - 0.105
    for k, z in enumerate((0.06, 0.36)):
        box("WallShelf_Board", (w, 0.2, 0.02), (0, by, z), OAK, bevel=0.003, parent=root)
        for sx in (-1, 1):
            box("WallShelf_Bracket_Wall", (0.025, 0.005, 0.13), (sx * (w / 2 - 0.12), d / 2 - 0.0025, z - 0.075), IRON,
                bevel=0.001, parent=root)
            box("WallShelf_Bracket_Arm", (0.025, 0.17, 0.005), (sx * (w / 2 - 0.12), by + 0.01, z - 0.0125), IRON,
                bevel=0.001, parent=root)
    zb = 0.07
    for k in range(3):                                    # stand-up coffee pouches with a crimped top + label
        px = -w / 2 + 0.1 + k * 0.13
        pz = random.uniform(0.17, 0.2)
        box("Coffee_Pouch", (0.11, 0.06, pz), (px, by, zb + pz / 2), KRAFT if k != 1 else mat("dark", 0.6), bevel=0.012,
            parent=root)
        box("Coffee_Pouch_Crimp", (0.11, 0.03, 0.02), (px, by, zb + pz + 0.006), KRAFT if k != 1 else mat("dark", 0.6),
            bevel=0.003, parent=root)
        box("Coffee_Pouch_Label", (0.075, 0.002, 0.07), (px, by - 0.031, zb + pz * 0.45), PAPER, bevel=0, parent=root)
        cyl("Coffee_Pouch_Valve", 0.008, 0.003, (px, by - 0.031, zb + pz * 0.8), mat("dark", 0.4), rot=(R(90), 0, 0),
            segs=10, bevel=0, parent=root)
    for k in range(2):                                    # glass jars with oak lids (biscotti / beans)
        jx = w / 2 - 0.22 + k * 0.12
        jh = 0.18 - k * 0.03
        no_shadow(cyl("Jar_Glass", 0.05, jh, (jx, by, zb + jh / 2), GLASS, bevel=0.006, parent=root))
        cyl("Jar_Fill", 0.044, jh * 0.7, (jx, by, zb + jh * 0.35 + 0.003), CHOC if k else BREAD, bevel=0.004,
            parent=root)
        cyl("Jar_Lid", 0.052, 0.025, (jx, by, zb + jh + 0.012), OAK, bevel=0.004, parent=root)
    zt = 0.37
    for s in range(4):                                    # stacked cups
        lathe("Shelf_Cup", [(0, 0), (0.026, 0), (0.042, 0.06), (0.039, 0.06), (0.024, 0.004), (0, 0.004)],
              (-w / 2 + 0.12, by, zt + s * 0.022), CERAMIC, segs=20, parent=root)
    for k in range(3):                                    # small glass bottles of syrup
        no_shadow(cyl("Syrup_Bottle", 0.03, 0.2, (-0.08 + k * 0.075, by, zt + 0.1), mat("glass", 0.05, alpha=0.4),
                      bevel=0.008, parent=root))
        cyl("Syrup_Fill", 0.026, 0.15, (-0.08 + k * 0.075, by, zt + 0.076), mat(("crust", "accent_1", "bread")[k], 0.3),
            bevel=0.006, parent=root)
        cyl("Syrup_Cap", 0.012, 0.05, (-0.08 + k * 0.075, by, zt + 0.225), mat("dark", 0.4), parent=root)
    px = w / 2 - 0.16                                     # trailing pothos in a glazed pot
    lathe("Shelf_Pot", [(0, 0), (0.055, 0), (0.07, 0.11), (0.074, 0.115), (0.066, 0.115), (0.055, 0.02), (0, 0.02)],
          (px, by, zt), M("cream", 0.32, "ceramic"), parent=root)
    vines = []
    for k, (dx, dy, drop) in enumerate(((-0.06, -0.1, 0.2), (0.04, -0.12, 0.27), (0.08, -0.09, 0.15))):
        pts = spline([(px, by, zt + 0.11), (px + dx * 1.3, by + dy, zt + 0.1), (px + dx * 1.6, by + dy * 1.4, zt - drop * 0.5),
                      (px + dx * 1.4, by + dy * 1.3, zt - drop)], 4)
        tube("Pothos_Vine", pts, 0.003, mat("plant", 0.6), parent=root, segs=5)
        vines += [(tuple(p), 0.035) for p in pts[::2]]
    vines.append(((px, by, zt + 0.16), 0.07))
    foliage("Pothos_Leaves", vines, 10, (0.05, 0.04), mat("plant", 0.55, color="#5C8A3E"), parent=root, seed=11,
            droop=0.5)


def build_plant():
    """Olive tree in a fibre-clay planter: thin twisting trunk, small narrow silvery leaves."""
    root, w, d, h = furniture_root("plant")
    pot_h = 0.36
    lathe("Plant_Pot", [(0, 0), (0.15, 0), (0.18, pot_h - 0.02), (0.19, pot_h), (0.175, pot_h), (0.165, 0.04), (0, 0.04)],
          (0, 0, 0), POT_CLAY, segs=36, parent=root)
    cyl("Plant_Soil", 0.17, 0.01, (0, 0, pot_h - 0.025), SOIL, bevel=0, parent=root)
    bark = M("crust", 0.85, "wood", along="Z", color="#6E5B48")
    trunk = [(0, 0, pot_h - 0.03), (0.02, 0.01, pot_h + 0.25), (-0.015, 0.0, pot_h + 0.55), (0.01, -0.01, pot_h + 0.75)]
    tube("Plant_Trunk", spline(trunk, 4), 0.024, bark, parent=root, r2=0.012, segs=10)
    tips = []
    for k, (dx, dy, dz) in enumerate(((0.16, 0.04, 0.95), (-0.15, 0.06, 0.92), (0.03, -0.14, 1.0), (-0.02, 0.12, 1.06),
                                      (0.05, 0.0, 1.1))):
        start = Vector(trunk[-1]) - Vector((0, 0, 0.1 * (k % 2)))
        end = Vector((dx, dy, pot_h + dz))
        tube("Plant_Branch", spline([start, (start + end) / 2 + Vector((0, 0, 0.05)), end], 3), 0.01, bark, parent=root,
             r2=0.005, segs=6)
        tips.append((tuple(end), 0.17))
    tips.append(((0, 0, pot_h + 1.0), 0.2))
    foliage("Plant_Leaves", tips, 170, (0.06, 0.012), mat("plant", 0.55), parent=root, seed=SEED, droop=0.4)
    foliage("Plant_Leaves_Silver", tips, 60, (0.055, 0.011), mat("plant", 0.5, color="#A9B49A"), parent=root,
            seed=SEED + 1, droop=0.4)


PLACEHOLDERS = {
    "counter": build_counter, "display_case": build_display_case, "hero_prop": build_hero_prop,
    "pendant_lamp": build_pendant_lamp, "stool": build_stool, "table": build_table, "chair": build_chair,
    "wall_shelf": build_wall_shelf, "plant": build_plant,
}

if SHOW_PLACEHOLDER_FURNITURE:
    for slot_name, build in PLACEHOLDERS.items():
        build()

# Banquette under the shop window, a second marble table + chair at it, and a two-top near the door.
banquette(1.3, 3.4)
tb = empty("TableB", (0.92, 1.8, FLOOR_Z))
bistro_table(tb)
make_cup("TableB_Cup", (0.1, -0.12, 0.75), tb, key="main")
lathe("TableB_Plate", [(0, 0), (0.07, 0), (0.09, 0.012), (0.085, 0.013), (0.06, 0.006), (0, 0.006)], (-0.1, 0.1, 0.75),
      CERAMIC, parent=tb)
cinnamon_bun("TableB_Bun", (-0.1, 0.1, 0.756), tb)
bentwood_chair(empty("TableB_Chair", (1.5, 1.8, FLOOR_Z), rot=(0, 0, R(-90))))
tc = empty("TableC", (2.75, 0.85, FLOOR_Z))
bistro_table(tc)
make_cup("TableC_Cup_1", (-0.12, -0.06, 0.75), tc)
make_cup("TableC_Cup_2", (0.12, 0.08, 0.75), tc, key="accent_1")
lathe("TableC_Plate", [(0, 0), (0.07, 0), (0.09, 0.012), (0.085, 0.013), (0.06, 0.006), (0, 0.006)], (0.0, -0.15, 0.75),
      CERAMIC, parent=tc)
pain_au_chocolat("TableC_Pain", (0.0, -0.15, 0.756), tc, turn=R(20))
for cx_, turn in ((2.18, 90), (3.32, -90)):
    bentwood_chair(empty("TableC_Chair", (cx_, 0.85, FLOOR_Z), rot=(0, 0, R(turn))))

# =====================================================================
#  WALL DECOR + PORTFOLIO PICTURES
# =====================================================================
# Letter-board menu over the counter: your name, your role, and your projects as menu items.
MB_X, MB_Z, MB_W, MB_H = 3.6, 2.12, 1.36, 0.98
for nm, size, loc in (("Top", (MB_W + 0.06, 0.035, 0.03), (MB_X, D - 0.0175, MB_Z + MB_H / 2 + 0.015)),
                      ("Bottom", (MB_W + 0.06, 0.035, 0.03), (MB_X, D - 0.0175, MB_Z - MB_H / 2 - 0.015))):
    box(f"Menu_Frame_{nm}", size, (loc[0], loc[1] - 0.012, loc[2]), OAK, bevel=0.003)
for sx in (-1, 1):
    box("Menu_Frame_Side", (0.03, 0.035, MB_H), (MB_X + sx * (MB_W / 2 + 0.015), D - 0.0295, MB_Z), OAK_V, bevel=0.003)
menu = box("Menu_Felt", (MB_W, 0.012, MB_H), (MB_X, D - 0.018, MB_Z), FELT, bevel=0)
for k in range(int(MB_H / 0.028)):                 # the grooves that hold the push-in letters
    box("Menu_Groove", (MB_W - 0.01, 0.002, 0.003), (MB_X, D - 0.0245, MB_Z - MB_H / 2 + 0.014 + k * 0.028),
        mat("dark", 0.9, color="#4A4542"), bevel=0)
letters = mat("chalk", 0.5, emit=0.35)
TY = D - 0.028
hook_text("name", 1, "YOUR NAME", 0.13, (MB_X, TY, MB_Z + 0.36), material=letters, max_width=MB_W - 0.2, depth=0.004)
hook_text("role", 1, "your role", 0.07, (MB_X, TY, MB_Z + 0.22), material=letters, max_width=MB_W - 0.3, depth=0.004)
label("Menu_Dash", "- - -   MENU   - - -", 0.045, (MB_X, TY, MB_Z + 0.12), mat("accent_2", 0.5, emit=0.35))
for k in range(4):                                  # project titles = menu items, prices are decoration
    zz = MB_Z + 0.02 - k * 0.1
    hook_text("title", k + 1, f"PROJECT {('ONE', 'TWO', 'THREE', 'FOUR')[k]}", 0.055,
              (MB_X - MB_W / 2 + 0.1, TY, zz), material=letters, max_width=0.85, align="LEFT", depth=0.004)
    label(f"Menu_Price_{k}", f"{random.choice((3, 4, 5))}.{random.choice((20, 50, 80))}", 0.05,
          (MB_X + MB_W / 2 - 0.1, TY, zz), letters, align="RIGHT")
label("Menu_Footer", "SOURDOUGH . PASTRIES . COFFEE", 0.036, (MB_X, TY, MB_Z - MB_H / 2 + 0.06),
      mat("accent_2", 0.5, emit=0.35))


def framed(name, center, size, wall="back", frame_mat=None, mount=0.05, depth=0.025, off=0.0):
    """Real picture frame: 22 mm moulding, a white mount (passe-partout) around the picture.
    Returns the hook location + rotation for the picture inside."""
    x, y, z = center
    w, h = size
    fw = 0.022
    ow, oh = w + 2 * mount + 2 * fw, h + 2 * mount + 2 * fw
    fm = frame_mat or OAK
    if wall == "back":                                  # off = how far the wall surface sits in front of y = D (tiles)
        box(f"{name}_Backing", (ow - 0.01, 0.01, oh - 0.01), (x, D - off - 0.005, z), PAPER, bevel=0)
        for sz in (-1, 1):
            box(f"{name}_Frame_H", (ow, depth, fw), (x, D - off - depth / 2, z + sz * (oh - fw) / 2), fm, bevel=0.003)
        for sx in (-1, 1):
            box(f"{name}_Frame_V", (fw, depth, oh - 2 * fw), (x + sx * (ow - fw) / 2, D - off - depth / 2, z), fm,
                bevel=0.003)
        return (x, D - off - 0.0115, z), (0, 0, 0)
    box(f"{name}_Backing", (0.01, ow - 0.01, oh - 0.01), (0.005, y, z), PAPER, bevel=0)
    for sz in (-1, 1):
        box(f"{name}_Frame_H", (depth, ow, fw), (depth / 2, y, z + sz * (oh - fw) / 2), fm, bevel=0.003)
    for sy in (-1, 1):
        box(f"{name}_Frame_V", (depth, fw, oh - 2 * fw), (depth / 2, y + sy * (ow - fw) / 2, z), fm, bevel=0.003)
    return (0.0115, y, z), (0, 0, R(90))


# Poster 1: back wall corner, above the end of the banquette (black frame, white mount).
loc, rot = framed("Poster1", (0.36, 0, 1.68), (0.36, 0.5), frame_mat=mat("dark", 0.4))
p1 = hook_image("poster", 1, (0.36, 0.5), loc, rot=rot, default_key="accent_2")
px_, _, pz_ = loc
hook_default(p1,
             ball("Poster1_Bread", 0.1, (px_, D - 0.014, pz_ - 0.04), CRUST, scale=(1.3, 0.05, 0.65)),
             *[box("Poster1_Score", (0.09, 0.004, 0.012), (px_ - 0.06 + k * 0.06, D - 0.016, pz_ - 0.0), BREAD, bevel=0,
                   rot=(0, R(35), 0)) for k in range(3)],
             box("Poster1_Line", (0.22, 0.003, 0.01), (px_, D - 0.014, pz_ + 0.17), mat("crust", 0.6), bevel=0))

# Poster 2: back wall above the patisserie cabinet, oak frame.
loc, rot = framed("Poster2", (2.25, 0, 2.02), (0.46, 0.62), mount=0.04, off=0.012)
p2 = hook_image("poster", 2, (0.46, 0.62), loc, rot=rot, default_key="accent_1")
px_, _, pz_ = loc
hook_default(p2,
             ball("Poster2_Sun", 0.08, (px_ + 0.1, D - 0.026, pz_ + 0.15), mat("accent_2", 0.8), scale=(1, 0.05, 1)),
             box("Poster2_Hill", (0.46, 0.003, 0.16), (px_, D - 0.026, pz_ - 0.23), mat("main", 0.8), bevel=0),
             box("Poster2_Hill2", (0.3, 0.003, 0.1), (px_ + 0.08, D - 0.028, pz_ - 0.12), mat("cream", 0.8), bevel=0,
                 rot=(0, R(8), 0)))

# Frame 1: left wall between the window and the back corner, over the end of the banquette.
loc, rot = framed("Frame1", (0, 3.6, 1.62), (0.42, 0.54), wall="left", mount=0.05)
f1 = hook_image("frame", 1, (0.42, 0.54), loc, rot=rot, default_key="main")
hook_default(f1,
             *[ball("Frame1_Leaf", 0.045, (0.014, 3.6 + math.sin(k) * 0.05, 1.47 + k * 0.07), mat("plant", 0.7),
                    scale=(0.05, 1.4, 0.6)) for k in range(5)],
             box("Frame1_Stem", (0.003, 0.006, 0.34), (0.013, 3.6, 1.62), mat("crust", 0.7), bevel=0))

# =====================================================================
#  LIGHTS, WORLD, CAMERA, RENDER
# =====================================================================
# Low morning sun raking in through the shop window and door, a soft fill from the camera side,
# the window's own sky glow, and a warm bounce under the (missing) ceiling.
sun_dir = Vector((1.0, -0.32, -0.6)).normalized()
target = Vector((1.6, wy - 0.3, 0.0))
light("Light_Sun", "SUN", SUN_STRENGTH, kelvin(SUN_WARMTH), target - sun_dir * 6, aim=target, size=R(2.5))
light("Light_Fill", "AREA", 230 * (W * D / 16), kelvin(5800), (W + 3, -3, H + 2.5), aim=(W / 2, D / 2, 0.6), size=6)
light("Light_Window", "AREA", 60, kelvin(5200), (0.25, wy, wz), aim=(2.0, wy, wz - 0.4), size=1.4)
light("Light_Bounce", "AREA", 45, kelvin(LAMP_WARMTH + 400), (W / 2, D / 2, H - 0.1), aim=(W / 2, D / 2, 0), size=2.5)
light("Light_Street", "AREA", 60, kelvin(5600), (-1.2, -1.6, 2.6), aim=(-0.6, -0.3, 0.3), size=2.0)
light("Light_Case", "AREA", 3.5, kelvin(4200), (2.25, COUNTER_Y + 0.05, 1.26), aim=(2.25, COUNTER_Y, 0.8), size=0.6)

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

# Orthographic camera that frames the whole room (and the pavement + awning) automatically.
# kit_bounds must start at x = -T (check_room.py works out the room size from it). The pavement and awning
# stick out to the left, so the box reaches further forward (-y) instead: the 45-degree camera sees that as
# the same left edge. Its bottom is raised a little so the extra reach adds no empty space under the room.
FRONT = PAVE_X + PAVE_Y + T if (PAVEMENT or AWNING) else 0.0
BOUNDS = [-T, FRONT, -0.2 + 0.44 * (PAVE_Y - FRONT), W, D + T, H + 0.12]
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
scene.view_settings.exposure = -0.15

# Remember the style so add_furniture.py can match colours later.
scene["kit_style"] = STYLE
scene["kit_version"] = KIT_VERSION
scene["kit_palette"] = json.dumps(COLORS)
scene["kit_material_finish"] = json.dumps({"roughness": 0.6, "bevel": 0.005, "saturation": 0.75})
scene["kit_theme"] = THEME
scene["kit_bounds"] = BOUNDS            # includes the pavement and awning outside the walls
scene["kit_room_size"] = [W, D, H]      # the room itself, for check_room.py
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
