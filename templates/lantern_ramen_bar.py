"""
3D ROOM PORTFOLIO KIT  -  Template: LANTERN ALLEY RAMEN BAR (late-night noodle counter on a rainy alley)
=======================================================================================================
Builds a little late-night ramen counter shop on a rain-wet alley corner, modelled on real Japanese
neighbourhood ramen bars: an L-shaped pale-timber counter with a raised serving ledge and six round stools,
an open kitchen with three big stock pots steaming under a stainless hood, a noodle boiler with strainer
baskets, a meal-ticket vending machine by the door, red paper lanterns hung from the counter beam, a cotton
curtain in the kitchen doorway, a row of hanging wooden menu planks, a sake-bottle shelf, an old box TV
in the corner, a little two-seat table, and outside a stone-paved alley with puddles, a city bicycle
and a standing light-box sign.
It renders a 1920x1080 image.
Your name and role are on the big signboard over the kitchen; your projects are the hanging menu planks,
the TV and the poster. The ticket machine emails you; the bottle shelf, the street sign and the bicycle
open your other links. The lantern beam carries your tagline.

HOW TO RUN
  Option A (no Blender UI):   blender -b -P lantern_ramen_bar.py
  Option B (inside Blender):  Scripting tab > Open > lantern_ramen_bar.py > Run Script (then F12 to render)

You only need to edit the SETTINGS block below. Everything under it builds the room.
Output: output/lantern_ramen_bar.png and output/lantern_ramen_bar.blend next to this script.
"""
# REFERENCES  (what each piece is modelled on; product names appear only here and in research/lantern_ramen_bar.md)
#   counter        neighbourhood ramen-bar counter, pale solid-timber top 45 mm, raised serving ledge:
#                  customer top 90 cm, ledge 108 cm, depth 60 cm, 6 seats at about 60 cm pitch
#                  https://www.restaurant-furniture.com/resources/guides/bar-stool-and-counter-stool-measurements-and-spacing-layout-selecting-the-right-dimension
#   stool          round backless wooden counter stool with a vinyl seat pad: seat dia 32 cm, seat H 66 cm
#                  https://www.superiorseating.com/round-seat-backless-restaurant-bar-stool-in-walnut
#   stove          low stock-pot range (stand 50 cm) with three 40 qt / 38 L pots: dia 40 x H 31 cm each
#                  https://www.gofoodservice.com/p/cac-stkp-40
#   noodle boiler  counter-height noodle boiler with six strainer baskets (tebo): W52 D60 H85 cm, basket dia 13 cm
#   hood           stainless canopy hood over the range: 190 x 70 cm, front 40 cm deep, 1.8 m above the floor
#   hero_prop      floor-standing meal-ticket vending machine (NEC MP-T4S-type size): W65 D30 H161 cm
#                  https://en.wikipedia.org/wiki/Shokken
#                  https://www.ipros.com/en/cg3/Touch%20panel%20slim%20ticket%20vending%20machine
#   pendant_lamp   red paper chochin lanterns, bamboo-ribbed: dia 25 x H 45 cm (izakaya size 24 x 60 cm)
#                  https://kimurakami.com/products/japanese-paper-lanterns
#                  https://nipponandco.fr/en/japanese-lanterns-chochin/4273-japanese-lantern-shokuji-red.html
#   noren          split cotton doorway curtain 85 x 150 cm (here cut to 85 x 105 cm for the kitchen door)
#                  https://japanesetaste.com/products/noren-gold-woven-doorway-curtain-japanese-flying-dragon-design-85x150cm
#   ramen bowls    21 cm donburi bowl, H 8.5 cm, about 1.3 L
#                  https://souschef.co.uk/products/blue-wave-ramen-bowl
#   wall_shelf     timber bottle shelf 115 x 22 cm; 1.8 L sake bottles (isshobin) H 40 x dia 10.5 cm
#                  https://hakushika.co.jp/en/culture/measurements.html
#   beckoning cat  generic ceramic beckoning-cat figurine (Tokoname-type size): W13.5 D11.5 H18 cm
#                  https://www.goodsfromjapan.com/products/daruma-maneki-neko
#   menu planks    hanging timber menu tags, here 34 x 62 cm (signboard proportions of old shop kanban)
#                  https://www.chairish.com/product/14039904/japanese-wooden-kanban-restaurant-sign
#   signboard      shop kanban board for the name: 190 x 46 cm (old kanban 121 x 45 cm)
#                  https://www.chairish.com/product/14578572/japanese-wooden-restaurant-signboardkanban-sushi-1950s
#   TV             14-inch box CRT TV on a wall bracket: W40 D36 H33 cm
#   bicycle        Japanese city bicycle with a front basket, 26-inch wheels: L182 W58 H100 cm, basket 31 x 22 x 24 cm
#                  https://stonetiledepot.com/products/24-26-inch-beach-cruiser-bike-with-basket-and-rear-rack
#   street sign    standing light-box sign (andon type): 34 x 34 x 130 cm on a weighted base
#   table          restaurant two-top: 24 x 24 in (61 x 61 cm) laminated timber top 29 mm, 22 x 22 in cast-iron
#                  cross base, 3 in column, H 30 in (76 cm); with two low backless stools (seat H 46 cm)
#                  https://www.webstaurantstore.com/lancaster-table-seating-24-x-24-reversible-gray-white-laminated-standard-height-table-top-and-base-kit-with-22-x-22-base/349C24SG222S.html
#   planter        black bamboo (Phyllostachys nigra) in a cedar box planter 42 x 42 x 40 cm, canes 1.5 m
#   umbrella stand clear vinyl umbrellas (60 cm canopy radius, 85 cm long) in a steel stand
#   floor          slate-grey 300 mm porcelain floor tiles; alley in granite setts 100 x 100 mm with wet puddles

# =====================================================================
#  SETTINGS  -  change these lines, then run the script again
# =====================================================================
ROOM_NAME = "lantern_ramen_bar"     # used for the output file names

ROOM_WIDTH = 4.8                    # metres, left to right (along the back wall)
ROOM_DEPTH = 4.2                    # metres, front to back (along the left wall)
WALL_HEIGHT = 2.9                   # metres

THEME = "lantern_night"             # pick one of the colour themes below
THEMES = {                          # any hex colour works; "main" is the room's hero colour (stool seats)
    # "lantern_night": pale timber and dark walnut, cream plaster, red paper lanterns, an indigo curtain,
    # a blue-black rainy alley outside.
    "lantern_night": {
        "background": "#121826", "wall": "#E6D6BB", "wall_trim": "#4A3123", "floor": "#575B63", "floor_2": "#4A4E56",
        "wood": "#DDB988", "main": "#B8322B", "accent_1": "#3D6CA6", "accent_2": "#F1B652", "accent_3": "#5E9C8F",
        "cream": "#F3EADA", "plant": "#5D8A45", "dark": "#1D1C21", "walnut": "#5A3A27", "lantern": "#D2392B",
        "glow": "#FFB45C", "steel": "#B9BDC2", "tile": "#EEEAE2", "street": "#3A4050", "sett": "#565C69",
        "puddle": "#3E5276", "sky": "#1E2A44", "broth": "#D69A4C", "noodle": "#F1D58C", "neon": "#FFB45C",
        "sign": "#F4E9D2", "rain": "#B9CCEB", "glass": "#C9D9E6", "bottle": "#3E6B4A",
    },
    # "neon_rain": a rainy cyber-noodle-bar night - magenta and cyan neon tubes, glowing holographic menu,
    # wet chrome, pink lanterns. Uses its own lights (see "LIGHTS" near the end: NEON switches the lantern,
    # kitchen, fill and street lights and turns the menu planks into glowing screens).
    "neon_rain": {
        "background": "#0C0A1A", "wall": "#3A3550", "wall_trim": "#211D30", "floor": "#2E2C3A", "floor_2": "#25232F",
        "wood": "#9C7C66", "main": "#E0399E", "accent_1": "#1FC8E0", "accent_2": "#F7D046", "accent_3": "#8C5CF0",
        "cream": "#EDE7F6", "plant": "#3E9C7A", "dark": "#141220", "walnut": "#3B2B33", "lantern": "#F0459E",
        "glow": "#FF6CC0", "steel": "#D8DCE6", "tile": "#5B5774", "street": "#22202E", "sett": "#3A3848",
        "puddle": "#3A2E66", "sky": "#1A1430", "broth": "#D9934A", "noodle": "#F1D58C", "neon": "#29E3FF",
        "sign": "#1A1726", "rain": "#9FE8FF", "glass": "#9FB4E6", "bottle": "#2E5D7A",
    },
}

SUN_WARMTH = 9000                   # Kelvin of the moonlit night sky over the alley (bigger = bluer)
SUN_STRENGTH = 0.9                  # strength of that cool night light
LAMP_WARMTH = 2200                  # Kelvin of the candle-warm bulbs inside the paper lanterns
LAMP_STRENGTH = 9                   # Watts per lantern bulb
STEAM = True                        # soft steam rising from the stock pots and the bowls
RAIN = True                         # rain streaks and ripples over the alley outside
ALLEY = True                        # stone-paved alley strip with a bicycle and a street sign in front of the shop
SEED = 5                            # change to shuffle bowls, bottles, toppings and props

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
NEON = THEME == "neon_rain"         # cyber theme: neon tubes, glowing menu, wet chrome

STYLE = "lantern_ramen_bar"
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



# The room's real materials (one place, so every piece uses the same timber, steel, glaze...).
TIMBER = M("wood", 0.42, "wood")                   # pale cypress-style timber: counter tops, planks, frames
TIMBER_V = M("wood", 0.44, "wood", along="Z")      # the same timber with vertical grain (posts, planks)
WALNUT = M("walnut", 0.5, "wood")                  # dark-stained timber: beams, counter front, stool legs
WALNUT_V = M("walnut", 0.52, "wood", along="Z")
FRAME = M("wall_trim", 0.55, "wood")               # dark structural timber: wall posts, door frames, wainscot rail
FRAME_V = M("wall_trim", 0.57, "wood", along="Z")
PLASTER = M("wall", 0.88, "plaster")
TILE = M("tile", 0.28, "square_tile")              # kitchen wall tiles (100 mm), rows along the back wall
TILE_L = M("tile", 0.29, "square_tile", along="Y") # the same tiles on the left wall
FLOOR_TILE = M("floor", 0.55, "square_tile", along="Z", scale=1 / 3)    # 300 mm slate-grey floor tiles
STEEL = M("steel", 0.12 if NEON else 0.3, "brushed", metal=1.0)         # stainless: hood, range, tables
STEEL_V = M("steel", 0.14 if NEON else 0.32, "brushed", metal=1.0, along="Z")
ALU = M("steel", 0.38, "brushed", metal=0.85, along="Z", color="#A9ADB2")   # dull aluminium stock pots
IRON = M("dark", 0.5, "brushed", metal=0.7)        # cast iron / black steel
NOREN = M("accent_1", 0.92, "fabric")              # dyed cotton curtain (follows your brand colour)
LINEN = M("cream", 0.9, "fabric")
VINYL = M("main", 0.38, "leather")                 # stool seat pads
GLAZE_OUT = M("dark", 0.22, "ceramic")             # black-glazed donburi bowls
GLAZE_IN = M("main", 0.2, "ceramic")               # red glaze inside the bowls
CERAMIC = M("cream", 0.25, "ceramic")              # white porcelain: spoons, plates, the beckoning cat
PAPER = M("cream", 0.8, "paper")
LANTERN_PAPER = mat("lantern", 0.75, emit=2.2)     # lit red paper lanterns glow from inside
LANTERN_RIB = mat("lantern", 0.7, emit=0.9, color="#8E2A22" if not NEON else "#9C2A6E")
LACQUER = mat("dark", 0.3)                         # black lacquered lantern caps
SETT = M("sett", 0.22, "square_tile", along="Z")   # wet granite setts in the alley
SETT_2 = M("street", 0.24, "square_tile", along="Z")
PUDDLE = mat("puddle", 0.03, emit=0.35, metal=0.3)  # mirror-flat rain puddles holding a little sky glow
GLASS = mat("glass", 0.05, alpha=0.22)
FROSTED = mat("sky", 0.4, emit=0.6, alpha=0.85)    # frosted door glass with the blue street glow behind it
BOTTLE_GREEN = mat("bottle", 0.08, alpha=0.8)
BOTTLE_BROWN = mat("bottle", 0.08, alpha=0.8, color="#6A3E1C")
BROTH = mat("broth", 0.12)                         # glossy pork-bone broth
NOODLE = mat("noodle", 0.45)
CHASHU = mat("chashu", 0.5, color="#C98E6E")       # rolled pork slices: pink centre, dark rim
CHASHU_RIM = mat("chashu_rim", 0.5, color="#6E3C24")
EGG = mat("egg", 0.35, color="#F6F0E2")
YOLK = mat("yolk", 0.3, color="#E88B1E")
NORI = mat("nori", 0.6, color="#1F2A22")
SCALLION = mat("scallion", 0.5, color="#79B14E")
MENMA = mat("menma", 0.5, color="#C79A57")
WATER = mat("rain", 0.05, alpha=0.35)
SOIL = mat("soil", 0.95, color="#2E241D")
FLAME = mat("flame", 0.5, emit=6.0, color="#3E8CFF")
ROOF = M("roof", 0.5, "concrete", color="#4B505B" if not NEON else "#2C2A3A")    # grey clay roof tiles


def soft_glow(key, strength, alpha):
    """Soft see-through puff (steam): it glows in the middle and fades out towards its outline."""
    m = mat(key, 0.95, emit=strength, alpha=alpha)
    if m.get("kit_soft"):
        return m
    nt, b = m.node_tree, _principled(m)
    lw = nt.nodes.new("ShaderNodeLayerWeight")
    lw.inputs["Blend"].default_value = 0.5
    inv = nt.nodes.new("ShaderNodeMath")
    inv.operation, inv.inputs[0].default_value = "SUBTRACT", 1.0
    nt.links.new(lw.outputs["Facing"], inv.inputs[1])
    pw = nt.nodes.new("ShaderNodeMath")
    pw.operation, pw.inputs[1].default_value = "POWER", 3.0
    nt.links.new(inv.outputs[0], pw.inputs[0])
    mul = nt.nodes.new("ShaderNodeMath")
    mul.operation, mul.inputs[1].default_value = "MULTIPLY", strength
    nt.links.new(pw.outputs[0], mul.inputs[0])
    nt.links.new(mul.outputs[0], b.inputs["Emission Strength"])
    _set(b, ["Specular IOR Level", "Specular"], 0.0)
    m["kit_soft"] = True
    return m


STEAM_MAT = soft_glow("cream", 2.0, 0.09)
BOWL_STEAM = soft_glow("cream", 1.2, 0.05)          # fainter wisps over the served bowls
RAIN_MAT = mat("rain", 0.2, emit=0.8, alpha=0.3)
GLOW_TXT = mat("cream", 0.5, emit=0.5)             # cream letters that stay readable at night
NEON_A = mat("neon", 0.3, emit=7.0)                # neon tube colour 1 (warm amber, or cyan in neon_rain)
NEON_B = mat("main", 0.3, emit=6.0)                # neon tube colour 2 (red, or magenta in neon_rain)
SIGN_FACE = mat("sign", 0.6, emit=1.3 if not NEON else 0.2)    # light-box face of the street sign
SCREEN_DARK = mat("dark", 0.2, emit=0.05)

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



def cloth(name, w, h, loc, material, folds=3, amp=0.012, rot=(0, 0, 0), parent=None, sway=0.0):
    """Hanging cloth panel (curtain) facing local -Y with soft vertical folds that deepen towards the hem.
    loc = centre of the TOP edge."""
    nx, nz = 24, 6
    bm = bmesh.new()
    grid = []
    for j in range(nz + 1):
        t = j / nz                                     # 0 at the rod, 1 at the hem
        row = []
        for i in range(nx + 1):
            u = i / nx
            y = amp * (0.35 + 0.65 * t) * math.sin(2 * math.pi * folds * u) + sway * t * t
            row.append(bm.verts.new(((u - 0.5) * w, y, -t * h)))
        grid.append(row)
    for j in range(nz):
        for i in range(nx):
            bm.faces.new((grid[j][i], grid[j][i + 1], grid[j + 1][i + 1], grid[j + 1][i]))
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    sol = o.modifiers.new("Thickness", "SOLIDIFY")
    sol.thickness = 0.004
    return _finish(o, material, 0, None, parent)


def flat_poly(name, pts, y, material, parent=None):
    """Flat shape in the x-z plane at depth y (a printed doodle on a sign). pts = [(x, z)]."""
    bm = bmesh.new()
    bm.faces.new([bm.verts.new((x, y, z)) for x, z in pts])
    return _finish(_obj(name, bm), material, 0, None, parent)


def bmesh_boxes(name, boxes, materials, parent=None):
    """Many small boxes in ONE mesh (setts, slats). boxes = [(cx, cy, cz, sx, sy, sz, material_index)]."""
    bm = bmesh.new()
    for cx, cy, cz, sx, sy, sz, mi in boxes:
        vs = [bm.verts.new((cx + dx * sx / 2, cy + dy * sy / 2, cz + dz * sz / 2))
              for dz in (-1, 1) for dx, dy in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
        for f in ((0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)):
            bm.faces.new([vs[i] for i in f]).material_index = mi
    o = _obj(name, bm)
    for m in materials:
        o.data.materials.append(m)
    o.data.polygons.foreach_set("use_smooth", [False] * len(o.data.polygons))
    COL_ROOM.objects.link(o)
    o.parent = parent
    bev = o.modifiers.new("Bevel", "BEVEL")
    bev.width, bev.segments, bev.limit_method = 0.004, 1, "ANGLE"
    return o


# =====================================================================
#  ROOM SHELL: slate floor tiles, plaster walls over a timber wainscot, kitchen tiles, timber frame
# =====================================================================
DOOR_Y, DOOR_TOP = (0.32, 1.22), 2.0          # sliding street door in the left wall
BACK_DOOR_X, BACK_DOOR_TOP = (0.12, 0.94), 1.9  # kitchen doorway (with the curtain) in the back wall
KITCHEN_Y = 2.75                               # the kitchen starts behind the counter
KITCHEN_X = 2.75                               # ... and ends at the counter return

box("Floor_Base", (W + T, D + T, 0.2), ((W - T) / 2, (D + T) / 2, -0.1), mat("dark", 0.8), bevel=0.02)
box("Floor_Tiles", (W, D, FLOOR_Z), (W / 2, D / 2, FLOOR_Z / 2), FLOOR_TILE, bevel=0.0)

left = box("Wall_Left", (T, D + T, H), (-T / 2, (D + T) / 2, H / 2), PLASTER, bevel=0.0)
back = box("Wall_Back", (W + T, T, H), ((W - T) / 2, D + T / 2, H / 2), PLASTER, bevel=0.0)
for wall, nm, size, loc in ((left, "Door", (T * 3, DOOR_Y[1] - DOOR_Y[0], DOOR_TOP + 0.1),
                             (-T / 2, sum(DOOR_Y) / 2, (DOOR_TOP - 0.1) / 2)),
                            (back, "BackDoor", (BACK_DOOR_X[1] - BACK_DOOR_X[0], T * 3, BACK_DOOR_TOP + 0.1),
                             (sum(BACK_DOOR_X) / 2, D + T / 2, (BACK_DOOR_TOP - 0.1) / 2))):
    cutter = box(f"{nm}_Cutter", size, loc, mat("wall"), bevel=0.0)
    cutter.hide_render = cutter.hide_viewport = True
    boolean = wall.modifiers.new(nm, "BOOLEAN")
    boolean.operation, boolean.object = "DIFFERENCE", cutter

# Dark timber cap on top of the walls, corner post and an end post at the front of the left wall.
box("Trim_Top_Back", (W + T + 0.04, T + 0.06, 0.08), ((W - T) / 2, D + T / 2, H + 0.04), FRAME, bevel=0.01)
box("Trim_Top_Left", (T + 0.06, D + T + 0.04, 0.08), (-T / 2, (D + T) / 2 - 0.02, H + 0.04), FRAME, bevel=0.01)
box("Post_Corner", (0.12, 0.12, H), (0.06, D - 0.06, H / 2), FRAME_V, bevel=0.006)
box("Post_Front", (0.1, 0.1, H), (0.05, 0.05, H / 2), FRAME_V, bevel=0.006)

# Kitchen walls: white 100 mm tiles behind the range and the prep table.
TILE_TOP = 1.72
box("Kitchen_Tiles_Back", (KITCHEN_X - BACK_DOOR_X[1] - 0.04, 0.01, TILE_TOP - FLOOR_Z),
    ((KITCHEN_X + BACK_DOOR_X[1] + 0.04) / 2, D - 0.005, (TILE_TOP + FLOOR_Z) / 2), TILE, bevel=0.0)
box("Kitchen_Tiles_Left", (0.01, D - KITCHEN_Y - 0.12, TILE_TOP - FLOOR_Z),
    (0.005, (D - 0.12 + KITCHEN_Y) / 2, (TILE_TOP + FLOOR_Z) / 2), TILE_L, bevel=0.0)
for nm, size, loc in (("Back", (KITCHEN_X - BACK_DOOR_X[1] - 0.04, 0.02, 0.02),
                       ((KITCHEN_X + BACK_DOOR_X[1] + 0.04) / 2, D - 0.01, TILE_TOP)),
                      ("Left", (0.02, D - KITCHEN_Y - 0.12, 0.02), (0.01, (D - 0.12 + KITCHEN_Y) / 2, TILE_TOP))):
    box(f"Kitchen_Tiles_Edge_{nm}", size, loc, STEEL, bevel=0.004)

# Timber wainscot (vertical boards, 95 mm, with a capping rail) in the dining part of the shop.
WS_TOP = 0.95


def wainscot(name, axis, a0, a1):
    """Run of vertical tongue-and-groove boards along a wall. axis 'x' = back wall, 'y' = left wall."""
    n = max(1, int((a1 - a0) / 0.095))
    pitch = (a1 - a0) / n
    boards = []
    for k in range(n):
        c = a0 + pitch * (k + 0.5)
        if axis == "x":
            boards.append((c, D - 0.009, (WS_TOP + FLOOR_Z) / 2, pitch - 0.004, 0.018, WS_TOP - FLOOR_Z, k % 2))
        else:
            boards.append((0.009, c, (WS_TOP + FLOOR_Z) / 2, 0.018, pitch - 0.004, WS_TOP - FLOOR_Z, k % 2))
    bmesh_boxes(name, boards, [WALNUT_V, M("walnut", 0.55, "wood", along="Z", color="#4F3322" if not NEON else
                                         "#35262E")])
    if axis == "x":
        box(f"{name}_Rail", (a1 - a0, 0.034, 0.03), ((a0 + a1) / 2, D - 0.017, WS_TOP + 0.015), FRAME, bevel=0.004)
    else:
        box(f"{name}_Rail", (0.034, a1 - a0, 0.03), (0.017, (a0 + a1) / 2, WS_TOP + 0.015), FRAME, bevel=0.004)


wainscot("Wainscot_Left_Front", "y", 0.1, DOOR_Y[0] - 0.06)
wainscot("Wainscot_Left", "y", DOOR_Y[1] + 0.06, KITCHEN_Y - 0.05)
wainscot("Wainscot_Back", "x", KITCHEN_X + 0.02, W - 0.1)

# Street door: two sliding timber-framed leaves with frosted glass panes (one leaf half open behind the other).
dy0, dy1 = DOOR_Y
dw = dy1 - dy0
for nm, size, loc in (("Head", (0.05, dw + 0.16, 0.08), (0.025, (dy0 + dy1) / 2, DOOR_TOP + 0.04)),
                      ("Jamb_Front", (0.05, 0.08, DOOR_TOP), (0.025, dy0 - 0.04, DOOR_TOP / 2)),
                      ("Jamb_Back", (0.05, 0.08, DOOR_TOP), (0.025, dy1 + 0.04, DOOR_TOP / 2)),
                      ("Track", (T, dw, 0.03), (-T / 2, (dy0 + dy1) / 2, FLOOR_Z + 0.015))):
    box(f"Door_Frame_{nm}", size, loc, FRAME, bevel=0.005)
leaf_w = dw / 2 + 0.03
for k, (lx, ly) in enumerate(((-0.05, dy0 + leaf_w / 2), (-0.1, dy1 - leaf_w / 2 - 0.12))):
    lz0, lh = FLOOR_Z + 0.03, DOOR_TOP - FLOOR_Z - 0.04
    for sy in (-1, 1):
        box("Door_Leaf_Stile", (0.035, 0.045, lh), (lx, ly + sy * (leaf_w / 2 - 0.0225), lz0 + lh / 2), TIMBER_V,
            bevel=0.004)
    for nm, hh, zz in (("Bottom", 0.36, lz0 + 0.18), ("Top", 0.06, lz0 + lh - 0.03)):
        box(f"Door_Leaf_{nm}", (0.035, leaf_w - 0.09, hh), (lx, ly, zz), TIMBER_V, bevel=0.004)
    gz0, gz1 = lz0 + 0.36, lz0 + lh - 0.06
    no_shadow(box("Door_Leaf_Glass", (0.006, leaf_w - 0.09, gz1 - gz0), (lx, ly, (gz0 + gz1) / 2), FROSTED, bevel=0))
    for j in range(1, 5):                              # horizontal glazing bars, like an old shop door
        box("Door_Leaf_Bar", (0.03, leaf_w - 0.09, 0.016), (lx, ly, gz0 + j * (gz1 - gz0) / 5), TIMBER, bevel=0.003)
    for j in range(1, 3):
        box("Door_Leaf_Bar_V", (0.028, 0.014, gz1 - gz0), (lx, ly - leaf_w / 2 + 0.045 + j * (leaf_w - 0.09) / 3,
                                                          (gz0 + gz1) / 2), TIMBER_V, bevel=0.003)
    box("Door_Leaf_Pull", (0.01, 0.02, 0.12), (lx + 0.022, ly + (leaf_w / 2 - 0.08) * (1 if k == 0 else -1), 1.0),
        IRON, bevel=0.003)
box("Door_Mat", (0.5, dw - 0.05, 0.012), (0.3, (dy0 + dy1) / 2, FLOOR_Z + 0.006), M("dark", 0.95, "knit", scale=3),
    bevel=0.003)

# Kitchen doorway in the back wall: frame, a dim back room, and the split cotton curtain on a pole.
bx0, bx1 = BACK_DOOR_X
for nm, size, loc in (("Head", (bx1 - bx0 + 0.14, 0.05, 0.07), ((bx0 + bx1) / 2, D - 0.025, BACK_DOOR_TOP + 0.035)),
                      ("Jamb_L", (0.07, 0.05, BACK_DOOR_TOP), (bx0 - 0.035, D - 0.025, BACK_DOOR_TOP / 2)),
                      ("Jamb_R", (0.07, 0.05, BACK_DOOR_TOP), (bx1 + 0.035, D - 0.025, BACK_DOOR_TOP / 2))):
    box(f"BackDoor_Frame_{nm}", size, loc, FRAME, bevel=0.005)
backroom = M("wall", 0.9, "plaster", color="#5A4A3A" if not NEON else "#2A2540")
box("Backroom_Floor", (bx1 - bx0 + 0.3, 0.8, 0.02), ((bx0 + bx1) / 2, D + T + 0.4, FLOOR_Z / 2), FLOOR_TILE, bevel=0)
box("Backroom_Wall", (bx1 - bx0 + 0.3, 0.05, BACK_DOOR_TOP + 0.2), ((bx0 + bx1) / 2, D + T + 0.8, BACK_DOOR_TOP / 2),
    backroom, bevel=0)
for sx in (bx0 - 0.15, bx1 + 0.15):
    box("Backroom_Side", (0.05, 0.8, BACK_DOOR_TOP + 0.2), (sx, D + T + 0.4, BACK_DOOR_TOP / 2), backroom, bevel=0)
box("Backroom_Top", (bx1 - bx0 + 0.3, 0.8, 0.05), ((bx0 + bx1) / 2, D + T + 0.4, BACK_DOOR_TOP + 0.1), backroom, bevel=0)
for k in range(3):                                     # sacks and boxes stacked in the store room
    box("Backroom_Box", (0.32, 0.3, 0.24), (bx0 + 0.25 + (k % 2) * 0.3, D + T + 0.55, FLOOR_Z + 0.12 + (k // 2) * 0.24),
        M("accent_2", 0.85, "paper", color="#B88C5A"), bevel=0.01)
NR_Z = BACK_DOOR_TOP - 0.02
tube("Noren_Pole", [(bx0 - 0.08, D - 0.06, NR_Z), (bx1 + 0.08, D - 0.06, NR_Z)], 0.012, TIMBER)
for sx in (bx0 - 0.08, bx1 + 0.08):
    cyl("Noren_Pole_Hook", 0.008, 0.06, (sx, D - 0.03, NR_Z), IRON, rot=(R(90), 0, 0), segs=8)
NOREN_W = (bx1 - bx0 + 0.04) / 3
for k in range(3):                                     # three panels with a little gap, cotton loops at the top
    cx_ = bx0 - 0.02 + NOREN_W * (k + 0.5)
    cloth(f"Noren_Panel_{k}", NOREN_W - 0.012, 1.05, (cx_, D - 0.07, NR_Z - 0.03), NOREN, folds=2, amp=0.01,
          sway=0.01 * (k - 1))
    for j in range(3):                                 # cotton loops round the pole
        lx = cx_ - NOREN_W * 0.33 + j * NOREN_W * 0.33
        tube("Noren_Loop", [(lx, D - 0.06 + 0.02 * math.cos(a), NR_Z + 0.02 * math.sin(a)) for a in
                            (2 * math.pi * q / 10 for q in range(10))], 0.004, NOREN, closed=True, segs=6)
# Your logo (if profile.json has one) is printed on the middle panel; by default a bowl-and-steam emblem.
logo = hook_image("logo", 1, (0.2, 0.2), (bx0 - 0.02 + NOREN_W * 1.5, D - 0.077 - 0.012, NR_Z - 0.62),
                  default_key="accent_1")
logo.data.materials[0] = NOREN                    # printed on the cotton itself
lx_, _, lz_ = logo.location
emb = mat("cream", 0.85, emit=0.15)
hook_default(logo,
             tube("Noren_Emblem_Bowl", spline([(lx_ - 0.08, D - 0.092, lz_ + 0.0), (lx_ - 0.05, D - 0.092, lz_ - 0.06),
                                               (lx_, D - 0.092, lz_ - 0.075), (lx_ + 0.05, D - 0.092, lz_ - 0.06),
                                               (lx_ + 0.08, D - 0.092, lz_ + 0.0)], 4), 0.008, emb, segs=6),
             tube("Noren_Emblem_Rim", [(lx_ - 0.09, D - 0.092, lz_ + 0.0), (lx_ + 0.09, D - 0.092, lz_ + 0.0)], 0.007,
                  emb, segs=6),
             *[tube(f"Noren_Emblem_Steam_{k}", spline([(lx_ - 0.04 + k * 0.04, D - 0.092, lz_ + 0.03),
                                                       (lx_ - 0.055 + k * 0.04, D - 0.092, lz_ + 0.06),
                                                       (lx_ - 0.035 + k * 0.04, D - 0.092, lz_ + 0.09)], 4), 0.006,
                    emb, segs=6) for k in range(3)])


# =====================================================================
#  REAL-WORLD PIECES (shared by the placeholders and the decoration)
# =====================================================================
def counter_run(root, L, d=0.6, end_left=False, end_right=True):
    """Ramen-bar counter run in root's space (front = -y): recessed plinth, vertical-slat dark front, a 45 mm
    pale timber top for the customers (90 cm) and a raised serving ledge on the kitchen side (108 cm)."""
    y_front = -d / 2
    box("Counter_Plinth", (L - 0.04, d - 0.14, 0.1), (0, 0.04, 0.05), FRAME, bevel=0.003, parent=root)
    n = max(1, int(round(L / 0.09)))
    pitch = L / n
    slats = [(-L / 2 + pitch * (k + 0.5), y_front + 0.08, 0.1 + 0.37, pitch - 0.005, 0.02, 0.74, k % 2) for k in range(n)]
    bmesh_boxes("Counter_Slats", slats, [WALNUT_V, M("walnut", 0.56, "wood", along="Z", color="#4F3322" if not NEON
                                                     else "#35262E")], parent=root)
    box("Counter_Carcass", (L - 0.02, d - 0.2, 0.76), (0, 0.06, 0.48), FRAME, bevel=0.002, parent=root)
    box("Counter_Rail", (L, 0.03, 0.04), (0, y_front + 0.075, 0.855), WALNUT, bevel=0.004, parent=root)
    box("Counter_Top", (L, 0.43, 0.045), (0, y_front + 0.215, 0.8775), TIMBER, bevel=0.005, parent=root)
    box("Counter_Upstand", (L, 0.03, 0.2), (0, y_front + 0.445, 0.95), WALNUT, bevel=0.004, parent=root)
    box("Counter_Ledge", (L, d - 0.43, 0.035), (0, y_front + 0.43 + (d - 0.43) / 2, 1.0625), TIMBER, bevel=0.005,
        parent=root)
    box("Counter_Kitchen_Back", (L, 0.02, 1.0), (0, d / 2 - 0.01, 0.53), STEEL, bevel=0.002, parent=root)
    # a soft LED strip under the lip of the top lights the slatted front from above
    strip = mat("glow", 0.4, emit=2.5) if not NEON else NEON_A
    no_shadow(box("Counter_LED", (L - 0.06, 0.008, 0.008), (0, y_front + 0.1, 0.845), strip, bevel=0, parent=root))
    for flag, sx in ((end_left, -1), (end_right, 1)):
        if flag:
            box("Counter_End", (0.03, d - 0.08, 0.76), (sx * (L / 2 - 0.015), 0.04, 0.48), WALNUT_V, bevel=0.004,
                parent=root)


def stool(root, seat_h=0.68):
    """Round backless counter stool: four splayed dark-timber legs with stretchers, a pale seat board
    and a red vinyl seat pad with piping. Seat dia 32 cm, seat height 68 cm."""
    top, foot = 0.105, 0.15

    def leg_at(sx, sy, z):
        r = top + (foot - top) * (seat_h - 0.06 - z) / (seat_h - 0.06)
        return (sx * r, sy * r, z)
    corners = ((-1, -1), (1, -1), (1, 1), (-1, 1))
    for sx, sy in corners:
        tube("Stool_Leg", [leg_at(sx, sy, 0.0), leg_at(sx, sy, seat_h - 0.05)], 0.016, WALNUT_V, parent=root, segs=10,
             r2=0.014)
    for z, rr, m_ in ((0.35 * seat_h, 0.011, IRON), (0.68 * seat_h, 0.009, WALNUT_V)):   # footrest ring, upper stretcher
        pts = [leg_at(sx, sy, z) for sx, sy in corners]
        tube("Stool_Stretcher", pts, rr, m_, parent=root, segs=8, closed=True)
    cyl("Stool_Board", 0.16, 0.03, (0, 0, seat_h - 0.045), TIMBER, segs=32, bevel=0.005, parent=root)
    cyl("Stool_Pad", 0.155, 0.05, (0, 0, seat_h - 0.005), VINYL, segs=32, bevel=0.018, parent=root)
    tube("Stool_Piping", ring_pts(0.153, seat_h - 0.03, 32), 0.005, VINYL, parent=root, closed=True, segs=6)


LANTERN_PROF = [(0.08, 0.0), (0.1, 0.025), (0.118, 0.08), (0.126, 0.16), (0.127, 0.21), (0.126, 0.26), (0.118, 0.34),
                (0.1, 0.395), (0.08, 0.42)]


def paper_lantern(name, loc, parent=None, s=1.0, paper=None, rib=None):
    """Red paper chochin lantern (dia 25 x H 42 cm): bamboo-ribbed paper barrel between black lacquered rims,
    hung on a wire hook. loc = the hanging point (top)."""
    x, y, z = loc
    paper, rib = paper or LANTERN_PAPER, rib or LANTERN_RIB
    z0 = z - 0.05 * s - 0.42 * s                     # bottom of the paper
    no_shadow(lathe(f"{name}_Paper", [(r * s, h * s) for r, h in LANTERN_PROF], (x, y, z0), paper, segs=28,
                    parent=parent))                # thin paper: the bulb inside lights the room through it
    for k in range(1, 12):                           # bamboo ribs show as fine darker rings
        hh = 0.42 * k / 12
        rr = next(r1 + (r2 - r1) * (hh - h1) / (h2 - h1) for (r1, h1), (r2, h2) in zip(LANTERN_PROF, LANTERN_PROF[1:])
                  if h1 <= hh <= h2)
        no_shadow(tube(f"{name}_Rib", ring_pts(rr * s + 0.0012, z0 + hh * s, 28, x, y), 0.0022 * s, rib, parent=parent,
                       segs=5, closed=True))
    for zz in (z0 - 0.012 * s, z0 + 0.432 * s):
        cyl(f"{name}_Rim", 0.088 * s, 0.03 * s, (x, y, zz), LACQUER, segs=24, bevel=0.004, parent=parent)
    tube(f"{name}_Hook", [(x, y, z0 + 0.447 * s), (x, y, z), (x + 0.012, y, z + 0.012)], 0.003, IRON, parent=parent,
         segs=6)
    return z0


def ramen_bowl(name, loc, parent=None, full=True, steam=True):
    """21 cm donburi bowl (H 8.5 cm), black glaze outside, red inside. Full = a served bowl of ramen: glossy
    broth, noodles, two rolled-pork slices, a soft egg, bamboo shoots, a nori sheet and scallions."""
    x, y, z = loc
    lathe(f"{name}_Bowl", [(0, 0), (0.045, 0), (0.048, 0.011), (0.07, 0.03), (0.094, 0.06), (0.105, 0.084),
                           (0.104, 0.087)], (x, y, z), GLAZE_OUT, segs=36, parent=parent)
    lathe(f"{name}_Glaze", [(0.1015, 0.0865), (0.091, 0.06), (0.067, 0.032), (0.04, 0.018), (0, 0.017)], (x, y, z),
          GLAZE_IN, segs=36, parent=parent)
    if not full:
        return
    zb = z + 0.068
    cyl(f"{name}_Broth", 0.094, 0.004, (x, y, zb), BROTH, segs=36, bevel=0, parent=parent)
    rnd = random.Random(hash(name) % 1000)
    for k in range(6):                               # noodles lifting out of the broth in loose waves
        a = rnd.uniform(0, math.pi)
        ca, sa = math.cos(a), math.sin(a)
        pts = [(x + ca * t - sa * 0.012 * math.sin(t * 60), y + sa * t + ca * 0.012 * math.sin(t * 60),
                zb + 0.003 + 0.003 * math.sin(t * 40)) for t in (q * 0.016 - 0.064 for q in range(9))]
        tube(f"{name}_Noodle", pts, 0.0028, NOODLE, parent=parent, segs=5)
    for k, (dx, dy, tilt) in enumerate(((0.035, 0.025, 18), (0.05, -0.012, 24))):
        e = empty(f"{name}_Chashu_{k}", (x + dx, y + dy, zb + 0.012), rot=(R(tilt), R(-12), R(30 * k)), parent=parent)
        cyl(f"{name}_Chashu", 0.034, 0.008, (0, 0, 0), CHASHU, segs=20, bevel=0.002, parent=e)
        tube(f"{name}_Chashu_Rim", ring_pts(0.034, 0, 20), 0.0045, CHASHU_RIM, parent=e, segs=5, closed=True)
    ball(f"{name}_Egg", 0.024, (x - 0.042, y + 0.012, zb + 0.006), EGG, scale=(1, 1.3, 0.55), parent=parent)
    ball(f"{name}_Yolk", 0.013, (x - 0.042, y + 0.012, zb + 0.016), YOLK, scale=(1, 1.25, 0.3), parent=parent)
    box(f"{name}_Nori", (0.07, 0.003, 0.08), (x - 0.01, y + 0.082, zb + 0.032), NORI, bevel=0.001, rot=(R(-14), 0, 0),
        parent=parent)
    for k in range(4):
        box(f"{name}_Menma", (0.03, 0.008, 0.006), (x - 0.01 + k * 0.006, y - 0.05 + k * 0.007, zb + 0.004 + k * 0.001),
            MENMA, bevel=0.002, rot=(0, 0, R(70 + k * 8)), parent=parent)
    for k in range(12):
        cyl(f"{name}_Scallion", 0.0045, 0.003, (x + rnd.uniform(-0.03, 0.03), y + rnd.uniform(-0.04, 0.01),
                                                zb + 0.006), SCALLION, segs=8, bevel=0, parent=parent)
    if steam and STEAM:                             # a few soft puffs drifting up off the broth
        for k in range(3):
            t = k / 2
            no_shadow(ball(f"{name}_Steam", 0.018 + 0.016 * t, (x + 0.015 * math.sin(k * 2.1 + len(name)), y - 0.01,
                                                              zb + 0.045 + 0.05 * k), BOWL_STEAM,
                           scale=(1.3, 1.0, 0.75), parent=parent, segs=14))


def chopsticks(name, loc, parent=None, turn=0.0):
    """Pair of pale timber chopsticks on a small ceramic rest."""
    e = empty(name, loc, rot=(0, 0, turn), parent=parent)
    box(f"{name}_Rest", (0.04, 0.012, 0.01), (0.06, 0, 0.005), CERAMIC, bevel=0.004, parent=e)
    for dy in (-0.006, 0.006):
        box(f"{name}_Stick", (0.21, 0.006, 0.006), (0, dy, 0.012), TIMBER, bevel=0.002, rot=(0, R(-2.5), 0), parent=e)
    return e


def water_glass(name, loc, parent=None):
    x, y, z = loc
    no_shadow(lathe(f"{name}_Glass", [(0, 0), (0.03, 0), (0.034, 0.1), (0.032, 0.1), (0.028, 0.006), (0, 0.006)],
                    (x, y, z), GLASS, segs=20, parent=parent))
    no_shadow(cyl(f"{name}_Water", 0.029, 0.07, (x, y, z + 0.042), WATER, segs=20, bevel=0, parent=parent))


def condiments(name, loc, parent=None, turn=0.0):
    """Counter caddy: soy dispenser, chilli-oil jar, pepper shaker and a box of disposable chopsticks."""
    e = empty(name, loc, rot=(0, 0, turn), parent=parent)
    box(f"{name}_Tray", (0.24, 0.1, 0.014), (0, 0, 0.007), TIMBER, bevel=0.003, parent=e)
    lathe(f"{name}_Soy", [(0, 0), (0.028, 0), (0.03, 0.07), (0.016, 0.09), (0.012, 0.1), (0, 0.1)], (-0.08, 0, 0.014),
          mat("soy", 0.08, color="#3A1C10", alpha=0.85), segs=16, parent=e)
    cyl(f"{name}_Soy_Cap", 0.014, 0.025, (-0.08, 0, 0.126), mat("main", 0.4), segs=16, parent=e)
    lathe(f"{name}_Chili", [(0, 0), (0.026, 0), (0.027, 0.06), (0.022, 0.065), (0, 0.065)], (-0.02, 0, 0.014),
          mat("chili", 0.15, color="#B8361A", alpha=0.9), segs=16, parent=e)
    cyl(f"{name}_Chili_Lid", 0.024, 0.012, (-0.02, 0, 0.085), CERAMIC, segs=16, parent=e)
    cyl(f"{name}_Pepper", 0.017, 0.06, (0.03, 0, 0.044), GLASS, segs=14, parent=e)
    cyl(f"{name}_Pepper_Cap", 0.018, 0.018, (0.03, 0, 0.083), STEEL, segs=14, parent=e)
    box(f"{name}_Chopbox", (0.07, 0.07, 0.1), (0.085, 0, 0.064), WALNUT, bevel=0.004, parent=e)
    for k in range(9):
        box(f"{name}_Chopstick", (0.006, 0.006, 0.2), (0.068 + (k % 3) * 0.017, -0.017 + (k // 3) * 0.017, 0.1),
            TIMBER, bevel=0.0015, rot=(R(random.uniform(-6, 6)), R(random.uniform(-6, 6)), 0), parent=e)
    return e


def isshobin(name, loc, parent=None, glass=None, label_key="cream"):
    """1.8 L sake bottle (H 40 x dia 10.5 cm) with a paper label and a crown cap."""
    x, y, z = loc
    lathe(f"{name}_Bottle", [(0, 0), (0.05, 0), (0.0525, 0.006), (0.0525, 0.26), (0.046, 0.295), (0.026, 0.33),
                             (0.0175, 0.35), (0.0175, 0.385), (0.019, 0.39), (0, 0.39)], (x, y, z), glass or BOTTLE_GREEN,
          segs=24, parent=parent)
    cyl(f"{name}_Label", 0.0535, 0.12, (x, y, z + 0.17), M(label_key, 0.8, "paper"), segs=24, bevel=0, parent=parent)
    box(f"{name}_Label_Mark", (0.03, 0.003, 0.08), (x, y - 0.054, z + 0.17), mat("dark", 0.6), bevel=0, parent=parent)
    cyl(f"{name}_Cap", 0.0195, 0.018, (x, y, z + 0.392), mat("accent_2", 0.35, metal=0.8), segs=16, parent=parent)


def beckoning_cat(name, loc, parent=None, turn=0.0, s=1.0):
    """Generic ceramic beckoning-cat figurine (H 18 cm): white glaze, one paw raised, red collar with a bell,
    holding a plain gold oval coin."""
    e = empty(name, loc, rot=(0, 0, turn), parent=parent)
    e.scale = (s, s, s)
    gold = mat("accent_2", 0.3, metal=0.9)
    pink = mat("pink", 0.5, color="#E9A0A0")
    ball(f"{name}_Body", 0.055, (0, 0, 0.058), CERAMIC, scale=(1, 0.85, 1.08), parent=e)
    ball(f"{name}_Head", 0.05, (0, -0.005, 0.14), CERAMIC, scale=(1.12, 0.95, 0.9), parent=e)
    for sx in (-1, 1):
        cyl(f"{name}_Ear", 0.019, 0.034, (sx * 0.033, -0.002, 0.188), CERAMIC, r2=0.003, segs=12, bevel=0,
            rot=(0, R(sx * 22), 0), parent=e)
        ball(f"{name}_EarIn", 0.01, (sx * 0.034, -0.012, 0.185), pink, scale=(0.9, 0.3, 1.2), parent=e)
        tube(f"{name}_Eye", [(sx * 0.02 - 0.009, -0.05, 0.146), (sx * 0.02, -0.052, 0.141), (sx * 0.02 + 0.009, -0.05, 0.146)],
             0.0022, mat("dark", 0.4), parent=e, segs=5)
    ball(f"{name}_Nose", 0.005, (0, -0.054, 0.133), pink, parent=e)
    tube(f"{name}_Collar", ring_pts(0.044, 0.103, 24, 0, -0.004), 0.006, mat("main", 0.35), parent=e, closed=True,
         segs=6)
    ball(f"{name}_Bell", 0.011, (0, -0.05, 0.096), gold, parent=e)
    tube(f"{name}_Arm", spline([(0.045, -0.01, 0.09), (0.062, -0.02, 0.13), (0.058, -0.03, 0.172)], 3), 0.014, CERAMIC,
         parent=e, segs=10)
    ball(f"{name}_Paw", 0.017, (0.056, -0.034, 0.18), CERAMIC, scale=(1, 0.8, 1.15), parent=e)
    box(f"{name}_Coin", (0.05, 0.008, 0.066), (-0.012, -0.05, 0.06), gold, bevel=0.012, parent=e)
    ball(f"{name}_FrontPaw", 0.014, (-0.03, -0.05, 0.04), CERAMIC, parent=e)
    tube(f"{name}_Tail", spline([(0.0, 0.045, 0.02), (0.045, 0.04, 0.025), (0.06, 0.0, 0.03)], 3), 0.008, CERAMIC,
         parent=e, segs=8)
    return e


def framed(name, center, size, wall="back", frame_mat=None, mount=0.04, depth=0.025, off=0.0):
    """Real picture frame: 22 mm moulding, a white mount (passe-partout) around the picture.
    Returns the hook location + rotation for the picture inside."""
    x, y, z = center
    w, h = size
    fw = 0.022
    ow, oh = w + 2 * mount + 2 * fw, h + 2 * mount + 2 * fw
    fm = frame_mat or TIMBER
    if wall == "back":
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


# =====================================================================
#  FURNITURE SLOTS  (same names in every template)
#  size = (width, depth, height); front of the furniture faces local -Y
# =====================================================================
COUNTER_Y = 2.45                                   # centre line of the long counter run
COUNTER_D = 0.6                                    # counter depth (customer top + serving ledge)
COUNTER_L = 3.33                                   # long run, from the left wall to the corner post
COUNTER_X1 = 0.02 + COUNTER_L                      # outer corner of the L
STOOL_Y = 1.9                                      # stools along the long run
LANTERN_Z = 2.46                                   # underside of the lantern beam
slot("counter",      (COUNTER_L, COUNTER_D, 1.1), (0.02 + COUNTER_L / 2, COUNTER_Y), shape="counter")
slot("stool",        (0.36, 0.36, 0.7), (1.95, STOOL_Y), shape="stool")
slot("stove",        (1.25, 0.62, 1.05), (1.65, D - 0.31), shape="box")
slot("pendant_lamp", (2.2, 0.3, 0.62), (1.3, COUNTER_Y), z=LANTERN_Z - 0.62, kind="hanging", shape="lamp")
slot("hero_prop",    (0.65, 0.32, 1.61), (0.18, 1.64), turn=90, shape="box")
slot("wall_shelf",   (1.1, 0.22, 0.48), (4.1, D - 0.11), z=2.37, kind="wall", shape="shelf")
slot("planter",      (0.42, 0.42, 1.6), (4.45, 0.4), shape="plant")
slot("table",        (0.61, 0.61, 0.76), (3.0, 0.95), shape="table")


# =====================================================================
#  LIGHTS helper (the lanterns carry their own bulbs)
# =====================================================================
def light(name, kind, energy, color, loc, aim=None, size=None, parent=None):
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
    if parent is not None:                 # stays where it is, but moves with its piece of furniture
        o.parent = parent
        o.matrix_parent_inverse = parent.matrix_world.inverted()
    return o


LANTERN_K = kelvin(LAMP_WARMTH) if not NEON else (1.0, 0.35, 0.75)


# =====================================================================
#  PLACEHOLDER FURNITURE  (replaced when you add your own with add_furniture.py)
# =====================================================================
def build_counter():
    """Long run of the L-shaped counter, from the left wall to the corner post."""
    root, w, d, h = furniture_root("counter")
    counter_run(root, w, d, end_left=False, end_right=True)
    return root


def build_stool():
    root, w, d, h = furniture_root("stool")
    stool(root)
    return root


def build_stove():
    """Low stock-pot range (stand 50 cm) with three 40 qt aluminium stock pots on cast-iron burners:
    a pork-bone stock, a chicken stock with a ladle, and one with its lid set ajar."""
    root, w, d, h = furniture_root("stove")
    sh = 0.5
    for sx in (-1, 1):
        for sy in (-1, 1):
            box("Range_Leg", (0.04, 0.04, sh - 0.04), (sx * (w / 2 - 0.03), sy * (d / 2 - 0.03), (sh - 0.04) / 2),
                STEEL_V, bevel=0.003, parent=root)
    box("Range_Frame", (w, d, 0.06), (0, 0, sh - 0.03), STEEL, bevel=0.004, parent=root)
    box("Range_Shelf", (w - 0.04, d - 0.06, 0.02), (0, 0, 0.12), STEEL, bevel=0.002, parent=root)
    tube("Range_Manifold", [(-w / 2 + 0.02, -d / 2 - 0.03, sh - 0.09), (w / 2 - 0.02, -d / 2 - 0.03, sh - 0.09)], 0.014,
         M("accent_2", 0.35, "brushed", metal=1.0, color="#C9A14E"), parent=root, segs=10)
    for k, px in enumerate((-0.415, 0.0, 0.415)):
        cyl("Range_Knob", 0.022, 0.03, (px, -d / 2 - 0.055, sh - 0.09), mat("dark", 0.4), rot=(R(90), 0, 0), segs=16,
            parent=root)
        tube("Range_Grate_Ring", ring_pts(0.15, sh + 0.02, 28, px, 0), 0.008, IRON, parent=root, closed=True, segs=6)
        for a in range(4):
            ca, sa = math.cos(R(45 + a * 90)), math.sin(R(45 + a * 90))
            box("Range_Grate_Prong", (0.18, 0.016, 0.03), (px + ca * 0.1, sa * 0.1, sh + 0.015), IRON, bevel=0.003,
                rot=(0, 0, R(45 + a * 90)), parent=root)
        cyl("Range_Burner", 0.06, 0.02, (px, 0, sh + 0.005), IRON, segs=20, parent=root)
        no_shadow(tube("Range_Flame", ring_pts(0.066, sh + 0.022, 20, px, 0), 0.008, FLAME, parent=root, closed=True,
                       segs=5))
        pz = sh + 0.035
        lathe("Pot", [(0, 0), (0.192, 0), (0.2, 0.008), (0.2, 0.3), (0.207, 0.308), (0.202, 0.315), (0.195, 0.306),
                      (0.195, 0.04), (0, 0.04)], (px, 0, pz), ALU, segs=40, parent=root)
        for sx in (-1, 1):
            tube("Pot_Handle", [(px + sx * 0.2, -0.05, pz + 0.26), (px + sx * 0.235, -0.05, pz + 0.265),
                                (px + sx * 0.235, 0.05, pz + 0.265), (px + sx * 0.2, 0.05, pz + 0.26)], 0.008, ALU,
                 parent=root, segs=8)
        cyl("Pot_Stock", 0.194, 0.006, (px, 0, pz + 0.27), mat("broth", 0.15, color="#E6D2A8" if k == 0 else "#D9A65A"),
            segs=40, bevel=0, parent=root)
        if k == 0:                                     # pork bones and a split onion in the pale stock
            for j in range(4):
                ball("Pot_Bone", 0.035, (px - 0.08 + j * 0.05, 0.03 * (-1) ** j, pz + 0.272), mat("bone", 0.6,
                     color="#EADFC8"), scale=(1.6, 0.8, 0.5), rot=(0, 0, R(j * 40)), parent=root)
        elif k == 1:                                   # a long-handled ladle resting in the stock
            lathe("Pot_Ladle", [(0, 0), (0.045, 0.0), (0.05, 0.03), (0.046, 0.032), (0, 0.006)], (px + 0.06, 0.02, pz + 0.25),
                  STEEL, segs=16, parent=root)
            tube("Pot_Ladle_Handle", [(px + 0.06, 0.02, pz + 0.28), (px + 0.12, -0.08, pz + 0.42), (px + 0.14, -0.1, pz + 0.47)],
                 0.007, STEEL, parent=root, segs=8)
        else:                                          # lid set ajar
            e = empty("Pot_Lid", (px, 0.02, pz + 0.322), rot=(R(-8), 0, 0), parent=root)
            lathe("Pot_Lid_Disc", [(0, 0.02), (0.06, 0.018), (0.2, 0.004), (0.21, 0.0), (0, 0)], (0, 0, 0), ALU, segs=40,
                  parent=e)
            tube("Pot_Lid_Handle", [(-0.04, 0, 0.02), (-0.04, 0, 0.045), (0.04, 0, 0.045), (0.04, 0, 0.02)], 0.007,
                 IRON, parent=e, segs=8)
    return root


def build_pendant_lamp():
    """Four red paper lanterns hung from the counter beam, each with a warm bulb inside. They stop short of the
    corner so the beam leaves a clear view onto the steaming stock pots."""
    root, w, d, h = furniture_root("pendant_lamp")
    bpy.context.view_layer.update()                    # so the bulbs can be placed in the lanterns' world space
    for k in range(4):
        px = -0.825 + k * 0.55
        z0 = paper_lantern(f"Lantern_{k}", (px, 0, h), parent=root)
        light(f"Light_Lantern_{k}", "POINT", LAMP_STRENGTH, LANTERN_K, root.matrix_world @ Vector((px, 0, z0 + 0.21)),
              size=0.08, parent=root)
    return root


def build_hero_prop():
    """Meal-ticket vending machine (W65 D30 H161 cm): plinth, cream cabinet, an illuminated header, a recessed
    grid of 20 menu buttons, a little display, coin and note slots, and the ticket tray. Click it to email you."""
    root, w, d, h = furniture_root("hero_prop")
    hook_link(root, "email")
    body = M("cream", 0.35, "ceramic")
    fy = -d / 2
    box("Ticket_Plinth", (w - 0.04, d - 0.04, 0.08), (0, 0.01, 0.04), mat("dark", 0.6), bevel=0.004, parent=root)
    hook_link(box("Ticket_Body", (w, d, h - 0.08), (0, 0, 0.08 + (h - 0.08) / 2), body, bevel=0.012, parent=root),
              "email")
    box("Ticket_Header", (w - 0.06, 0.01, 0.18), (0, fy - 0.003, h - 0.13), mat("accent_2", 0.4, emit=1.4), bevel=0.004,
        parent=root)
    label("Ticket_Header_Text", "TICKETS", 0.075, (0, fy - 0.009, h - 0.135), mat("dark", 0.5), parent=root)
    box("Ticket_Panel", (w - 0.08, 0.02, 0.6), (0, fy, 1.13), mat("dark", 0.35), bevel=0.006, parent=root)
    keys = ["main", "accent_2", "cream", "accent_3", "accent_1"]
    for r in range(5):
        for c in range(4):
            key = keys[(r + c * 2) % len(keys)] if r > 0 else "main"
            bz = 1.36 - r * 0.105
            bx = -0.2 + c * 0.133
            box("Ticket_Button", (0.115, 0.014, 0.08), (bx, fy - 0.012, bz), mat(key, 0.4, emit=0.6), bevel=0.006,
                parent=root)
            box("Ticket_Button_Line", (0.07, 0.003, 0.008), (bx, fy - 0.02, bz - 0.018), mat("dark", 0.6), bevel=0,
                parent=root)
    box("Ticket_Display", (0.22, 0.012, 0.06), (-0.13, fy - 0.006, 0.76), mat("accent_3", 0.3, emit=1.5), bevel=0.004,
        parent=root)
    for nm, size, loc in (("Coin_Slot", (0.05, 0.012, 0.012), (0.09, fy - 0.006, 0.77)),
                          ("Note_Slot", (0.18, 0.012, 0.016), (0.0, fy - 0.006, 0.66)),
                          ("Tray", (0.26, 0.02, 0.09), (-0.08, fy - 0.006, 0.36)),
                          ("Coin_Cup", (0.1, 0.02, 0.07), (0.17, fy - 0.006, 0.36))):
        box(f"Ticket_{nm}", size, loc, mat("dark", 0.5), bevel=0.004, parent=root)
    box("Ticket_Card", (0.05, 0.004, 0.075), (-0.08, fy - 0.017, 0.395), PAPER, bevel=0.001, rot=(R(-10), 0, 0),
        parent=root)
    box("Ticket_Lever", (0.03, 0.03, 0.05), (0.17, fy - 0.02, 0.78), STEEL, bevel=0.006, parent=root)
    beckoning_cat("Lucky_Cat", (0.12, 0.0, h), parent=root, turn=0.0)
    return root


def build_wall_shelf():
    """Timber bottle shelf on two black brackets: 1.8 L sake bottles, soy-sauce bottles and a stack of plates.
    Click it to open your GitHub."""
    root, w, d, h = furniture_root("wall_shelf")
    hook_link(root, "github")
    hook_link(box("Shelf_Board", (w, d, 0.028), (0, 0, 0.014), TIMBER, bevel=0.004, parent=root), "github")
    box("Shelf_Lip", (w, 0.012, 0.03), (0, -d / 2 + 0.006, 0.04), TIMBER, bevel=0.003, parent=root)
    for sx in (-1, 1):
        box("Shelf_Bracket_V", (0.025, 0.012, 0.2), (sx * (w / 2 - 0.15), d / 2 - 0.006, -0.1), IRON, bevel=0.002,
            parent=root)
        tube("Shelf_Bracket_Brace", [(sx * (w / 2 - 0.15), d / 2 - 0.01, -0.18), (sx * (w / 2 - 0.15), -d / 2 + 0.03, -0.005)],
             0.007, IRON, parent=root, segs=6)
    glasses = [BOTTLE_GREEN, BOTTLE_BROWN]
    labels = ["cream", "accent_2", "cream", "sign"]
    for k in range(5):
        isshobin(f"Shelf_Sake_{k}", (-w / 2 + 0.1 + k * 0.125, 0.01, 0.028), parent=root, glass=random.choice(glasses),
                 label_key=random.choice(labels))
    for k in range(2):                                 # small soy bottles with red caps
        x = 0.28 + k * 0.07
        lathe(f"Shelf_Soy_{k}", [(0, 0), (0.03, 0), (0.031, 0.13), (0.015, 0.16), (0.012, 0.18), (0, 0.18)], (x, 0.0, 0.028),
              mat("soy", 0.08, color="#3A1C10", alpha=0.85), segs=16, parent=root)
        cyl(f"Shelf_Soy_Cap_{k}", 0.013, 0.02, (x, 0, 0.218), mat("main", 0.4), segs=16, parent=root)
    for j in range(5):
        lathe("Shelf_Plate", [(0, 0), (0.055, 0), (0.075, 0.012), (0.072, 0.014), (0, 0.006)], (0.46, 0.0, 0.028 + j * 0.012),
              CERAMIC, segs=24, parent=root)
    return root


def build_planter():
    """Black bamboo in a slatted cedar box planter (42 x 42 x 40 cm), canes about 1.5 m tall."""
    root, w, d, h = furniture_root("planter")
    ph = 0.4
    cedar = M("wood", 0.6, "wood", along="Z", color="#9A6A45" if not NEON else "#6A4A44")
    for sx in (-1, 1):
        for sy in (-1, 1):
            box("Planter_Post", (0.04, 0.04, ph), (sx * (w / 2 - 0.02), sy * (d / 2 - 0.02), ph / 2), cedar, bevel=0.003,
                parent=root)
    for k in range(4):
        z = 0.05 + k * 0.095
        for a in range(4):
            ang = R(a * 90)
            box("Planter_Slat", (w - 0.04, 0.018, 0.085), (math.sin(ang) * (w / 2 - 0.009), -math.cos(ang) * (d / 2 - 0.009),
                                                            z + 0.0425), cedar, bevel=0.003, rot=(0, 0, ang), parent=root)
    box("Planter_Soil", (w - 0.05, d - 0.05, 0.02), (0, 0, ph - 0.03), SOIL, bevel=0, parent=root)
    cane = mat("bamboo", 0.4, color="#2C2A22" if not NEON else "#25303A")
    node = mat("bamboo_node", 0.5, color="#5C5A44")
    rnd = random.Random(SEED + 11)
    tops = []
    for k in range(7):
        bx, by = rnd.uniform(-0.12, 0.12), rnd.uniform(-0.12, 0.12)
        top_h = rnd.uniform(1.15, h - 0.1)
        lean = (bx * 0.5, by * 0.5)
        tube("Bamboo_Cane", [(bx, by, ph - 0.03), (bx + lean[0], by + lean[1], top_h)], 0.011, cane, parent=root,
             segs=10, r2=0.007)
        for j in range(1, int((top_h - ph) / 0.22)):
            t = j * 0.22 / (top_h - ph)
            tube("Bamboo_Node", ring_pts(0.0115 - 0.004 * t, ph + j * 0.22, 12, bx + lean[0] * t, by + lean[1] * t),
                 0.0025, node, parent=root, segs=4, closed=True)
        tops.append(((bx + lean[0], by + lean[1], top_h - 0.18), 0.16))
        tops.append(((bx + lean[0] * 0.7, by + lean[1] * 0.7, top_h - 0.45), 0.12))
    foliage("Bamboo_Leaves", tops, 60, (0.11, 0.018), M("plant", 0.6, "paper", scale=0.3), parent=root, seed=SEED,
            droop=0.6)
    return root


def build_table():
    """Restaurant two-top (61 x 61 cm, H 76 cm): a pale timber top with a dark edge band on a black cast-iron
    column and cross base, laid for one late-night customer."""
    root, w, d, h = furniture_root("table")
    top_t = 0.029
    box("Table_Top", (w, d, top_t), (0, 0, h - top_t / 2), TIMBER, bevel=0.004, parent=root)
    box("Table_Top_Band", (w - 0.004, d - 0.004, 0.012), (0, 0, h - top_t - 0.004), WALNUT, bevel=0.002, parent=root)
    box("Table_Spider", (0.24, 0.24, 0.02), (0, 0, h - top_t - 0.02), IRON, bevel=0.003, parent=root)
    cyl("Table_Column", 0.038, h - 0.07, (0, 0, (h - 0.07) / 2 + 0.03), IRON, segs=20, parent=root)
    cyl("Table_Collar", 0.055, 0.04, (0, 0, 0.05), IRON, segs=20, parent=root)
    for a in (45, 135):                                # 22 x 22 in cross base with levelling feet
        box("Table_Base_Arm", (0.76, 0.06, 0.035), (0, 0, 0.0325), IRON, bevel=0.006, rot=(0, 0, R(a)), parent=root)
    for a in range(4):
        ang = R(45 + a * 90)
        cyl("Table_Foot", 0.025, 0.015, (math.cos(ang) * 0.36, math.sin(ang) * 0.36, 0.0075), mat("dark", 0.6), segs=12,
            parent=root)
    ramen_bowl("Table_Bowl", (0.04, -0.1, h), parent=root)
    chopsticks("Table_Chopsticks", (0.07, -0.25, h), parent=root, turn=R(-3))
    water_glass("Table_Water", (0.21, -0.06, h), parent=root)
    condiments("Table_Caddy", (-0.02, 0.19, h), parent=root)
    return root


PLACEHOLDERS = {
    "counter": build_counter, "stool": build_stool, "stove": build_stove, "pendant_lamp": build_pendant_lamp,
    "hero_prop": build_hero_prop, "wall_shelf": build_wall_shelf, "planter": build_planter,
    "table": build_table,
}

if SHOW_PLACEHOLDER_FURNITURE:
    for slot_name, build in PLACEHOLDERS.items():
        build()

# =====================================================================
#  THE L-SHAPED COUNTER: return run, corner post, lantern beams, stools and what is on the counter
# =====================================================================
TOP_Z = FLOOR_Z + 0.9                              # customer counter top
LEDGE_Z = FLOOR_Z + 1.08                           # raised serving ledge
RET_X = COUNTER_X1 - COUNTER_D / 2                 # centre line of the return run
ret = empty("Counter_Return", (RET_X, (COUNTER_Y + COUNTER_D / 2 + D) / 2, FLOOR_Z), rot=(0, 0, R(90)))
counter_run(ret, D - COUNTER_Y - COUNTER_D / 2, COUNTER_D, end_left=False, end_right=False)

POST_X = COUNTER_X1 - 0.05
box("Corner_Post", (0.1, 0.1, LANTERN_Z + 0.14), (POST_X, COUNTER_Y, (LANTERN_Z + 0.14) / 2), WALNUT_V, bevel=0.005)
box("Lantern_Beam", (COUNTER_X1, 0.12, 0.14), (COUNTER_X1 / 2, COUNTER_Y, LANTERN_Z + 0.07), WALNUT, bevel=0.006)
box("Lantern_Beam_Return", (0.12, D - COUNTER_Y, 0.14), (POST_X, (COUNTER_Y + D) / 2, LANTERN_Z + 0.07), WALNUT,
    bevel=0.006)
# Your tagline is painted along the front of the lantern beam.
hook_text("tagline", 1, "hand-pulled noodles  .  slow-simmered broth  .  open late", 0.075,
          (1.62, COUNTER_Y - 0.0615, LANTERN_Z + 0.07), material=GLOW_TXT, max_width=2.75, depth=0.003)
for k, yy in enumerate((3.15, 3.8)):              # two more lanterns over the return
    z0 = paper_lantern(f"Lantern_Return_{k}", (POST_X, yy, LANTERN_Z))
    light(f"Light_Lantern_Return_{k}", "POINT", LAMP_STRENGTH, LANTERN_K, (POST_X, yy, z0 + 0.21), size=0.08)

STOOLS = [(0.75, STOOL_Y), (1.35, STOOL_Y), (2.55, STOOL_Y), (COUNTER_X1 + 0.27, 3.15), (COUNTER_X1 + 0.27, 3.8)]
for k, (sx_, sy_) in enumerate(STOOLS):
    stool(empty(f"Stool_{k}", (sx_, sy_, FLOOR_Z), rot=(0, 0, R(random.uniform(0, 90)))))
for k, sx_ in enumerate((2.52, 3.48)):              # two low stools (seat 46 cm) at the two-top table
    stool(empty(f"Table_Stool_{k}", (sx_, 0.95, FLOOR_Z), rot=(0, 0, R(20 + 25 * k))), seat_h=0.46)

# Served bowls, chopsticks, water and the condiment caddies along the counter.
CY = COUNTER_Y - COUNTER_D / 2 + 0.17               # where a customer's bowl sits
for k, (bx_, by_) in enumerate(((1.35, CY), (2.55, CY))):
    ramen_bowl(f"Bowl_{k}", (bx_, by_, TOP_Z))
    chopsticks(f"Chopsticks_{k}", (bx_ + 0.03, by_ - 0.12, TOP_Z), turn=R(4))
    water_glass(f"Water_{k}", (bx_ + 0.17, by_ + 0.02, TOP_Z))
ramen_bowl("Bowl_Return", (RET_X + 0.12, 3.15, TOP_Z))
e = empty("Bowl_Return_Sticks", (RET_X + 0.24, 3.15, TOP_Z), rot=(0, 0, R(90)))
chopsticks("Chopsticks_Return", (0, 0, 0), parent=e)
water_glass("Water_Return", (RET_X + 0.13, 3.34, TOP_Z))
water_glass("Water_Seat0", (0.8, CY, TOP_Z))
ramen_bowl("Bowl_Ledge", (1.95, COUNTER_Y + 0.2, LEDGE_Z))          # just ladled, waiting to be handed down
ramen_bowl("Bowl_Ledge_2", (0.55, COUNTER_Y + 0.2, LEDGE_Z), steam=False)
condiments("Caddy_0", (1.05, COUNTER_Y + 0.04, TOP_Z))
condiments("Caddy_1", (2.25, COUNTER_Y + 0.04, TOP_Z))
condiments("Caddy_2", (RET_X + 0.04, 3.5, TOP_Z), turn=R(90))
for k, (tx, ty) in enumerate(((1.62, COUNTER_Y + 0.23), (2.8, COUNTER_Y + 0.22), (0.85, COUNTER_Y + 0.24))):
    box(f"Meal_Ticket_{k}", (0.05, 0.03, 0.0015), (tx, ty, LEDGE_Z + 0.001), PAPER, bevel=0, rot=(0, 0, R(8 - 9 * k)))
for j in range(4):                                  # a stack of clean bowls at the corner of the ledge
    ramen_bowl(f"Bowl_Stack_{j}", (3.06, COUNTER_Y + 0.1, LEDGE_Z + j * 0.03), full=False)


# =====================================================================
#  OPEN KITCHEN: hood, noodle boiler, prep table and bowl shelves
# =====================================================================
HOOD_X0, HOOD_X1 = BACK_DOOR_X[1] + 0.24, KITCHEN_X   # starts clear of the doorway so the curtain stays in view
HOOD_Z, HOOD_D = 1.8, 0.62
hx, hw = (HOOD_X0 + HOOD_X1) / 2, HOOD_X1 - HOOD_X0
box("Hood_Top", (hw, HOOD_D - 0.12, 0.02), (hx, D - (HOOD_D - 0.12) / 2, HOOD_Z + 0.36), STEEL, bevel=0.003)
box("Hood_Front", (hw, 0.02, 0.24), (hx, D - HOOD_D + 0.01, HOOD_Z + 0.12), STEEL, bevel=0.004)
e = empty("Hood_Slope", (hx, D - HOOD_D + 0.01, HOOD_Z + 0.24), rot=(R(-38), 0, 0))
box("Hood_Slope_Panel", (hw, 0.02, 0.16), (0, 0, 0.08), STEEL, bevel=0.003, parent=e)
for sx in (-1, 1):
    box("Hood_Side", (0.02, HOOD_D, 0.24), (hx + sx * (hw / 2 - 0.01), D - HOOD_D / 2, HOOD_Z + 0.12), STEEL, bevel=0.003)
box("Hood_Lip", (hw + 0.02, 0.04, 0.03), (hx, D - HOOD_D, HOOD_Z), STEEL, bevel=0.006)
for k in range(4):                                  # grease filters inside the canopy
    box("Hood_Filter", (hw / 4 - 0.03, 0.4, 0.01), (HOOD_X0 + hw / 8 + k * hw / 4, D - 0.35, HOOD_Z + 0.22),
        M("dark", 0.4, "brushed", metal=0.8, color="#6B6E73"), bevel=0.002, rot=(R(-25), 0, 0))
no_shadow(box("Hood_Lightbar", (hw - 0.2, 0.05, 0.012), (hx, D - HOOD_D + 0.07, HOOD_Z + 0.01),
              mat("cream", 0.4, emit=3.0, color="#FFF4E0" if not NEON else "#E8FBFF"), bevel=0.002))

# Noodle boiler: stainless cabinet, a well of boiling water and six strainer baskets with long handles.
nb_x0, nb_x1 = 2.24, KITCHEN_X - 0.02
nbx, nbw, nbd = (nb_x0 + nb_x1) / 2, nb_x1 - nb_x0, 0.6
box("Boiler_Body", (nbw, nbd, 0.8), (nbx, D - nbd / 2, FLOOR_Z + 0.4), STEEL, bevel=0.006)
box("Boiler_Door_Seam", (nbw - 0.06, 0.004, 0.5), (nbx, D - nbd - 0.001, FLOOR_Z + 0.42), mat("dark", 0.5), bevel=0)
box("Boiler_Door", (nbw - 0.07, 0.01, 0.49), (nbx, D - nbd - 0.004, FLOOR_Z + 0.42), STEEL_V, bevel=0.004)
box("Boiler_Handle", (0.14, 0.02, 0.015), (nbx, D - nbd - 0.015, FLOOR_Z + 0.62), STEEL, bevel=0.005)
box("Boiler_Deck", (nbw + 0.02, nbd + 0.02, 0.03), (nbx, D - nbd / 2, FLOOR_Z + 0.83), STEEL, bevel=0.005)
box("Boiler_Water", (nbw - 0.07, nbd - 0.12, 0.01), (nbx, D - nbd / 2 + 0.02, FLOOR_Z + 0.835),
    mat("rain", 0.05, emit=0.25, alpha=0.8), bevel=0)
for k in range(6):
    cx_ = nb_x0 + 0.1 + (k % 2) * (nbw - 0.2)
    cy_ = D - 0.47 + (k // 2) * 0.16
    lathe(f"Tebo_{k}", [(0.0, -0.12), (0.045, -0.12), (0.062, 0.0), (0.066, 0.012), (0.06, 0.014)], (cx_, cy_, FLOOR_Z + 0.84),
          M("steel", 0.5, "fabric", metal=0.6, color="#B0B4B8"), segs=16)
    tube(f"Tebo_Handle_{k}", [(cx_, cy_ - 0.06, FLOOR_Z + 0.853), (cx_ + 0.0, cy_ - 0.2, FLOOR_Z + 0.93)], 0.007,
         STEEL, segs=6)
    if k % 2 == 0:
        tube(f"Tebo_Noodles_{k}", [(cx_ + 0.03 * math.cos(a), cy_ + 0.03 * math.sin(a), FLOOR_Z + 0.85 + 0.006 * math.sin(a * 3))
                                   for a in (q * 0.7 for q in range(14))], 0.004, NOODLE, segs=5)

# Prep table along the kitchen's left wall, with the toppings laid out, and two bowl shelves above it.
PT_Y0, PT_Y1, PT_D = KITCHEN_Y + 0.15, KITCHEN_Y + 0.85, 0.55
pty = (PT_Y0 + PT_Y1) / 2
box("Prep_Top", (PT_D, PT_Y1 - PT_Y0, 0.04), (PT_D / 2, pty, FLOOR_Z + 0.85), STEEL, bevel=0.004)
box("Prep_Upstand", (0.02, PT_Y1 - PT_Y0, 0.1), (0.01, pty, FLOOR_Z + 0.92), STEEL, bevel=0.003)
box("Prep_Shelf", (PT_D - 0.04, PT_Y1 - PT_Y0 - 0.04, 0.02), (PT_D / 2, pty, FLOOR_Z + 0.2), STEEL, bevel=0.002)
for sx in (0.03, PT_D - 0.03):
    for sy in (PT_Y0 + 0.03, PT_Y1 - 0.03):
        cyl("Prep_Leg", 0.018, 0.83, (sx, sy, FLOOR_Z + 0.415), STEEL_V, segs=12)
for k in range(3):                                  # noodle trays (shallow timber boxes) under the table
    box("Prep_Noodle_Tray", (0.42, 0.3, 0.06), (0.28, pty - 0.1 + k * 0.0, FLOOR_Z + 0.24 + k * 0.065), TIMBER, bevel=0.004)
box("Prep_Board", (0.3, 0.42, 0.025), (0.3, pty - 0.08, FLOOR_Z + 0.8825), M("wood", 0.6, "wood", along="Y", color="#E9D3B0"),
    bevel=0.004)
e = empty("Prep_Chashu_Roll", (0.32, pty - 0.12, FLOOR_Z + 0.94), rot=(R(90), 0, 0))
cyl("Prep_Chashu", 0.045, 0.2, (0, 0, 0), CHASHU_RIM, segs=20, bevel=0.01, parent=e)
for j in range(4):
    tube("Prep_Twine", ring_pts(0.0465, -0.07 + j * 0.045, 16), 0.0018, PAPER, parent=e, closed=True, segs=4)
for j in range(3):
    e = empty("Prep_Slice", (0.32, pty + 0.03 + j * 0.012, FLOOR_Z + 0.94), rot=(R(90 - 20 * j), 0, 0))
    cyl("Prep_Slice_Disc", 0.044, 0.008, (0, 0, 0), CHASHU, segs=20, bevel=0.002, parent=e)
box("Prep_Egg_Tray", (0.26, 0.18, 0.02), (0.3, pty + 0.22, FLOOR_Z + 0.88), STEEL, bevel=0.004)
for j in range(6):
    ex_, ey_ = 0.22 + (j % 3) * 0.08, pty + 0.18 + (j // 3) * 0.08
    ball("Prep_Egg", 0.024, (ex_, ey_, FLOOR_Z + 0.892), EGG, scale=(1, 1.3, 0.55))
    ball("Prep_Yolk", 0.013, (ex_, ey_, FLOOR_Z + 0.902), YOLK, scale=(1, 1.25, 0.3))
for j in range(2):
    box(f"Shelf_K_{j}", (0.28, PT_Y1 - PT_Y0, 0.02), (0.14, pty, 1.36 + j * 0.36), STEEL, bevel=0.003)
    for sx_ in (PT_Y0 + 0.05, PT_Y1 - 0.05):
        tube("Shelf_K_Bracket", [(0.0, sx_, 1.25 + j * 0.36), (0.25, sx_, 1.35 + j * 0.36)], 0.006, STEEL, segs=6)
    for c in range(3):
        for b in range(4 - j):
            ramen_bowl(f"Shelf_Bowl_{j}_{c}_{b}", (0.13, PT_Y0 + 0.13 + c * 0.22, 1.37 + j * 0.36 + b * 0.028), full=False)

# A cook's towel and two long ladles hanging from a rail on the hood.
tube("Hood_Rail", [(HOOD_X0 + 0.1, D - HOOD_D - 0.04, HOOD_Z + 0.08), (HOOD_X1 - 0.1, D - HOOD_D - 0.04, HOOD_Z + 0.08)],
     0.006, STEEL, segs=8)
for k, hx_ in enumerate((HOOD_X1 - 0.35, HOOD_X1 - 0.25)):
    tube(f"Hang_Ladle_{k}", [(hx_, D - HOOD_D - 0.04, HOOD_Z + 0.09), (hx_, D - HOOD_D - 0.05, HOOD_Z - 0.25)], 0.005, STEEL,
         segs=6)
    lathe(f"Hang_Ladle_Cup_{k}", [(0, 0), (0.03, 0.002), (0.034, 0.03), (0.03, 0.032), (0, 0.008)],
          (hx_, D - HOOD_D - 0.07, HOOD_Z - 0.28), STEEL, segs=14)
cloth("Cook_Towel", 0.24, 0.32, (HOOD_X0 + 0.3, D - HOOD_D - 0.05, HOOD_Z + 0.08), LINEN, folds=1, amp=0.008)

if STEAM:                                           # steam rising from the stock pots and the noodle boiler
    sp = SLOTS["stove"]
    for k, px in enumerate((-0.415, 0.0, 0.415)):
        base = Vector((sp.location.x + px, sp.location.y, FLOOR_Z + 0.88))
        rnd = random.Random(SEED + k)
        for j in range(6):
            t = j / 5
            p = base + Vector((0.06 * math.sin(j * 1.3 + k), -0.04 * t, 0.06 + t * (HOOD_Z - FLOOR_Z - 0.98)))
            no_shadow(ball(f"Steam_{k}_{j}", 0.07 + 0.09 * t, p, STEAM_MAT, scale=(1.2, 1.0, 0.75 + 0.2 * rnd.random()),
                           segs=16))
    for j in range(4):
        t = j / 3
        no_shadow(ball(f"Steam_Boiler_{j}", 0.06 + 0.07 * t, (nbx + 0.04 * math.sin(j * 2), D - 0.35, FLOOR_Z + 0.95 + t * 0.6),
                       STEAM_MAT, scale=(1.3, 1.0, 0.8), segs=16))


# =====================================================================
#  WALL DECOR + PORTFOLIO PICTURES
# =====================================================================
# Shop signboard over the kitchen: your name and role, lit by two little gooseneck lamps.
SB_X, SB_Z, SB_W, SB_H = hx, 2.5, 1.7, 0.44
board_mat = WALNUT if not NEON else mat("sign", 0.4)
box("Signboard", (SB_W, 0.04, SB_H), (SB_X, D - 0.022, SB_Z), board_mat, bevel=0.006)
for nm, size, loc in (("Top", (SB_W + 0.07, 0.05, 0.035), (SB_X, D - 0.027, SB_Z + SB_H / 2 + 0.0175)),
                      ("Bottom", (SB_W + 0.07, 0.05, 0.035), (SB_X, D - 0.027, SB_Z - SB_H / 2 - 0.0175))):
    box(f"Signboard_Frame_{nm}", size, loc, TIMBER, bevel=0.004)
for sx in (-1, 1):
    box("Signboard_Frame_Side", (0.035, 0.05, SB_H), (SB_X + sx * (SB_W / 2 + 0.0175), D - 0.027, SB_Z), TIMBER_V,
        bevel=0.004)
NAME_MAT = GLOW_TXT if not NEON else NEON_B
hook_text("name", 1, "YOUR NAME", 0.17, (SB_X, D - 0.0515, SB_Z + 0.06), material=NAME_MAT, max_width=SB_W - 0.24,
          depth=0.006)
hook_text("role", 1, "your role", 0.075, (SB_X, D - 0.0505, SB_Z - 0.12), material=mat("accent_2", 0.5, emit=0.6),
          max_width=SB_W - 0.7, depth=0.004)
for sx in (-1, 1):
    box("Signboard_Rule", (0.2, 0.004, 0.008), (SB_X + sx * 0.45, D - 0.044, SB_Z - 0.12), mat("accent_2", 0.5, emit=0.6),
        bevel=0)
if NEON:
    rr = [(SB_X - SB_W / 2 - 0.06, D - 0.06, SB_Z - SB_H / 2 - 0.06), (SB_X + SB_W / 2 + 0.06, D - 0.06, SB_Z - SB_H / 2 - 0.06),
          (SB_X + SB_W / 2 + 0.06, D - 0.06, SB_Z + SB_H / 2 + 0.06), (SB_X - SB_W / 2 - 0.06, D - 0.06, SB_Z + SB_H / 2 + 0.06)]
    no_shadow(tube("Neon_Signboard", rr, 0.009, NEON_A, segs=8, closed=True))
else:
    for sx in (-1, 1):                              # gooseneck sign lamps
        lx = SB_X + sx * 0.5
        tube("Sign_Lamp_Arm", spline([(lx, D, 2.86), (lx, D - 0.07, 2.88), (lx, D - 0.14, 2.86)], 4), 0.007, IRON, segs=8)
        lathe("Sign_Lamp_Shade", [(0.0, 0.0), (0.04, -0.005), (0.03, 0.035), (0.01, 0.045), (0, 0.045)],
              (lx, D - 0.15, 2.82), IRON, segs=16, rot=(R(-40), 0, 0))
        sp_ = light(f"Light_Signboard_{sx}", "SPOT", 5, kelvin(3000), (lx, D - 0.17, 2.81), aim=(SB_X + sx * 0.15, D, SB_Z - 0.15),
                    size=0.1)
        sp_.data.spot_size, sp_.data.spot_blend = R(100), 0.9

# Old box TV on a wall bracket in the corner over the kitchen door (picture hook 1: it glows).
tv = empty("TV", (0.5, D - 0.23, 2.08), rot=(R(7), 0, 0))
tv_body = M("tv", 0.4, "ceramic", color="#C8C0B2" if not NEON else "#9C98B4")
box("TV_Body", (0.4, 0.3, 0.33), (0, 0.0, 0.185), tv_body, bevel=0.02, parent=tv)
box("TV_Back", (0.3, 0.14, 0.25), (0, 0.2, 0.185), tv_body, bevel=0.02, parent=tv)
box("TV_Bezel", (0.33, 0.012, 0.255), (-0.025, -0.15, 0.2), mat("dark", 0.3), bevel=0.01, parent=tv)
for k in range(2):
    cyl("TV_Knob", 0.012, 0.015, (0.165, -0.155, 0.27 - k * 0.06), mat("dark", 0.4), rot=(R(90), 0, 0), segs=12, parent=tv)
for sx in (-1, 1):
    tube("TV_Antenna", [(0, 0.1, 0.35), (sx * 0.12, 0.12, 0.55)], 0.003, STEEL, parent=tv, segs=5)
screen = hook_image("screen", 1, (0.3, 0.225), (-0.025, -0.158, 0.2), parent=tv, glow=True, default_key="accent_3")
hook_default(screen,
             box("TV_Field", (0.3, 0.002, 0.08), (-0.025, -0.16, 0.128), mat("plant", 0.5, emit=0.8), bevel=0, parent=tv),
             ball("TV_Sun", 0.03, (0.05, -0.16, 0.25), mat("accent_2", 0.5, emit=1.0), scale=(1, 0.05, 1), parent=tv),
             box("TV_Ticker", (0.3, 0.002, 0.025), (-0.025, -0.161, 0.1), mat("main", 0.5, emit=0.8), bevel=0, parent=tv))
box("TV_Tray", (0.44, 0.36, 0.02), (0.5, D - 0.2, 2.07), IRON, bevel=0.003)
for sx in (-1, 1):
    tube("TV_Bracket", [(0.5 + sx * 0.18, D, 1.86), (0.5 + sx * 0.18, D - 0.34, 2.06)], 0.01, IRON, segs=6)
light("Light_TV", "AREA", 4, (0.6, 0.8, 1.0), (0.5, D - 0.6, 2.2), aim=(0.6, D - 1.5, 1.4), size=0.3)

# Poster on the left wall above the ticket machine (picture hook 2).
loc, rot = framed("Poster1", (0, 1.64, 2.33), (0.4, 0.56), wall="left", frame_mat=WALNUT, mount=0.035)
p1 = hook_image("poster", 1, (0.4, 0.56), loc, rot=rot, default_key="cream")
_, py_, pz_ = loc
hook_default(p1,
             box("Poster1_Sky", (0.002, 0.4, 0.3), (0.0125, py_, pz_ + 0.13), mat("accent_2", 0.8), bevel=0),
             ball("Poster1_Sun", 0.075, (0.0135, py_ + 0.08, pz_ + 0.12), mat("main", 0.7), scale=(0.04, 1, 1)),
             box("Poster1_Hill", (0.002, 0.3, 0.3), (0.014, py_ - 0.05, pz_ - 0.08), mat("accent_1", 0.8), bevel=0,
                 rot=(R(45), 0, 0)),
             box("Poster1_Sea", (0.002, 0.4, 0.2), (0.0145, py_, pz_ - 0.18), mat("accent_3", 0.8), bevel=0),
             *[tube(f"Poster1_Wave_{k}", [(0.016, py_ - 0.18, pz_ - 0.14 - k * 0.05), (0.016, py_ - 0.06, pz_ - 0.12 - k * 0.05),
                                          (0.016, py_ + 0.06, pz_ - 0.14 - k * 0.05), (0.016, py_ + 0.18, pz_ - 0.12 - k * 0.05)],
                    0.004, mat("cream", 0.6), segs=5) for k in range(2)])

# Hanging timber menu planks on the back wall: one dish per project (picture hooks 3-5 + titles).
RAIL_Z = 2.1
box("Menu_Rail", (1.26, 0.03, 0.03), (4.1, D - 0.05, RAIL_Z), WALNUT, bevel=0.004)
for sx in (3.55, 4.65):
    box("Menu_Rail_Bracket", (0.02, 0.05, 0.05), (sx, D - 0.025, RAIL_Z), IRON, bevel=0.003)
plank_mat = TIMBER_V if not NEON else mat("sign", 0.15, emit=0.25, alpha=0.85)
ink = mat("dark", 0.5) if not NEON else NEON_A
for k, cx_ in enumerate((3.68, 4.1, 4.52)):
    pz = 1.71
    box(f"Menu_Plank_{k}", (0.36, 0.025, 0.7), (cx_, D - 0.035, pz), plank_mat, bevel=0.005)
    for sx in (-1, 1):
        tube(f"Menu_Cord_{k}", [(cx_ + sx * 0.13, D - 0.04, pz + 0.35), (cx_ + sx * 0.08, D - 0.05, RAIL_Z - 0.01)], 0.003,
             mat("cream", 0.8), segs=5)
    bd = hook_image("board", k + 1, (0.3, 0.34), (cx_, D - 0.0485, pz + 0.13), glow=NEON,
                    default_key=("accent_2", "cream", "accent_3")[k])
    hook_default(bd,
                 flat_poly(f"Menu_Doodle_Bowl_{k}", [(cx_ + 0.1 * math.cos(a), pz + 0.075 - 0.07 * math.sin(a))
                                                     for a in (math.pi * q / 16 for q in range(17))], D - 0.05,
                           mat("dark", 0.5)),
                 box(f"Menu_Doodle_Foot_{k}", (0.06, 0.003, 0.014), (cx_, D - 0.05, pz - 0.0), mat("dark", 0.5), bevel=0),
                 box(f"Menu_Doodle_Rim_{k}", (0.2, 0.003, 0.012), (cx_, D - 0.052, pz + 0.075), mat("main", 0.5), bevel=0),
                 *[tube(f"Menu_Doodle_Steam_{k}_{j}", spline([(cx_ - 0.04 + j * 0.04, D - 0.051, pz + 0.1),
                                                               (cx_ - 0.055 + j * 0.04, D - 0.051, pz + 0.15),
                                                               (cx_ - 0.035 + j * 0.04, D - 0.051, pz + 0.2)], 4),
                        0.005, mat("dark", 0.6), segs=5) for j in range(3)])
    box(f"Menu_Stamp_{k}", (0.04, 0.003, 0.04), (cx_ + 0.12, D - 0.05, pz - 0.27), mat("main", 0.5, emit=0.3), bevel=0)
    hook_text("title", k + 1, f"PROJECT {('ONE', 'TWO', 'THREE')[k]}", 0.04, (cx_, D - 0.049, pz - 0.1), material=ink,
              max_width=0.31, depth=0.003)
    label(f"Menu_Number_{k}", f"No. {k + 1}", 0.032, (cx_, D - 0.049, pz - 0.21), ink if NEON else mat("main", 0.5))
    if NEON:
        no_shadow(tube(f"Neon_Plank_{k}", [(cx_ - 0.19, D - 0.05, pz - 0.36), (cx_ + 0.19, D - 0.05, pz - 0.36),
                                           (cx_ + 0.19, D - 0.05, pz + 0.36), (cx_ - 0.19, D - 0.05, pz + 0.36)], 0.005,
                       NEON_A, segs=6, closed=True))
light("Light_Menu", "AREA", 14 if not NEON else 6, kelvin(3200), (4.1, D - 1.1, 2.7), aim=(4.1, D, 1.8), size=0.8)

# Self-service water station under the menu planks: a low timber cabinet with sliding doors, a steel jug,
# stacked tumblers and a box of paper napkins.
WS_X, WS_W, WS_D, WS_H = 4.22, 0.62, 0.34, 0.82
box("Water_Cabinet", (WS_W, WS_D, WS_H - 0.06), (WS_X, D - WS_D / 2, FLOOR_Z + 0.06 + (WS_H - 0.06) / 2), WALNUT,
    bevel=0.004)
box("Water_Cabinet_Plinth", (WS_W - 0.04, WS_D - 0.04, 0.06), (WS_X, D - WS_D / 2 + 0.01, FLOOR_Z + 0.03), FRAME, bevel=0.002)
box("Water_Cabinet_Top", (WS_W + 0.02, WS_D + 0.01, 0.03), (WS_X, D - WS_D / 2, FLOOR_Z + WS_H + 0.015), TIMBER, bevel=0.004)
for sx in (-1, 1):
    box("Water_Cabinet_Door", (WS_W / 2 - 0.02, 0.012, WS_H - 0.14), (WS_X + sx * (WS_W / 4 - 0.004), D - WS_D - 0.004 - 0.008 * (sx > 0),
        FLOOR_Z + 0.06 + (WS_H - 0.06) / 2), TIMBER_V, bevel=0.003)
    box("Water_Cabinet_Pull", (0.012, 0.006, 0.08), (WS_X + sx * 0.05, D - WS_D - 0.018, FLOOR_Z + 0.5), IRON, bevel=0.002)
wt = FLOOR_Z + WS_H + 0.03
lathe("Water_Jug", [(0, 0), (0.06, 0), (0.065, 0.02), (0.065, 0.2), (0.055, 0.23), (0.035, 0.25), (0, 0.25)],
      (WS_X - 0.16, D - 0.17, wt), STEEL_V, segs=24)
tube("Water_Jug_Handle", spline([(WS_X - 0.095, D - 0.17, wt + 0.19), (WS_X - 0.06, D - 0.17, wt + 0.16),
                                 (WS_X - 0.065, D - 0.17, wt + 0.06), (WS_X - 0.095, D - 0.17, wt + 0.04)], 4), 0.008, STEEL)
box("Water_Tray", (0.26, 0.18, 0.012), (WS_X + 0.06, D - 0.17, wt + 0.006), mat("dark", 0.4), bevel=0.003)
for j in range(3):
    for i in range(2):
        no_shadow(lathe(f"Water_Tumbler_{j}_{i}", [(0, 0), (0.03, 0), (0.034, 0.09), (0.032, 0.09), (0.028, 0.006), (0, 0.006)],
                        (WS_X + 0.0 + i * 0.075, D - 0.17, wt + 0.012 + j * 0.03), GLASS, segs=16))
box("Water_Napkins", (0.12, 0.1, 0.06), (WS_X + 0.22, D - 0.17, wt + 0.03), PAPER, bevel=0.006)

# Waiting bench by the cut-away side and an umbrella stand by the door (it is raining).
bench = empty("Bench", (W - 0.3, 1.55, FLOOR_Z), rot=(0, 0, R(-90)))
box("Bench_Seat", (1.1, 0.32, 0.04), (0, 0, 0.43), TIMBER, bevel=0.005, parent=bench)
for sx in (-1, 1):
    for sy in (-1, 1):
        box("Bench_Leg", (0.045, 0.045, 0.41), (sx * 0.48, sy * 0.11, 0.205), WALNUT_V, bevel=0.004, parent=bench)
    box("Bench_Rail", (0.04, 0.22, 0.04), (sx * 0.48, 0, 0.12), WALNUT, bevel=0.003, parent=bench)
box("Bench_Stretcher", (0.92, 0.04, 0.04), (0, 0, 0.12), WALNUT, bevel=0.003, parent=bench)
box("Bench_Cushion", (0.5, 0.28, 0.05), (-0.25, 0, 0.475), M("accent_1", 0.9, "fabric"), bevel=0.018, parent=bench)
cyl("Umbrella_Stand", 0.1, 0.42, (0.24, 0.2, FLOOR_Z + 0.21), M("steel", 0.35, "brushed", metal=1.0, along="Z",
    color="#7E848C"), segs=20, bevel=0.004)
for k, (dx, dy, tilt) in enumerate(((0.03, 0.02, (R(8), R(-6), 0)), (-0.03, -0.02, (R(-6), R(-10), 0)))):
    e = empty(f"Umbrella_{k}", (0.24 + dx, 0.2 + dy, FLOOR_Z + 0.05), rot=tilt)
    no_shadow(cyl(f"Umbrella_{k}_Canopy", 0.045, 0.6, (0, 0, 0.42), mat("glass", 0.1, alpha=0.4), r2=0.012, segs=12,
                  bevel=0, parent=e))
    tube(f"Umbrella_{k}_Shaft", [(0, 0, 0.0), (0, 0, 0.86)], 0.005, STEEL, parent=e, segs=6)
    tube(f"Umbrella_{k}_Handle", spline([(0, 0, 0.84), (0, 0, 0.92), (0.035, 0, 0.95), (0.05, 0, 0.91)], 4), 0.009,
         mat("dark", 0.4), parent=e, segs=8)

# =====================================================================
#  OUTSIDE: clay-tile eave, rain-wet stone alley, puddles, a city bicycle, a standing light-box sign, rain
# =====================================================================
# Grey clay-tile eave along the street side of the shop (it "breaks the box" above the left wall).
EAVE_LEN, EAVE_SLOPE = 0.62, 25
eave_c = Vector((-T - 0.27, (D + T) / 2 - 0.02, H - 0.03))
eave_n = Vector((-math.sin(R(EAVE_SLOPE)), 0, math.cos(R(EAVE_SLOPE))))
box("Eave_Board", (EAVE_LEN, D + T + 0.2, 0.03), eave_c, FRAME, bevel=0.004, rot=(0, R(-EAVE_SLOPE), 0))
y = -0.08
while y < D + T + 0.08:
    no_shadow(cyl("Eave_Tile", 0.042, EAVE_LEN + 0.04, eave_c + eave_n * 0.03 + Vector((0, y - eave_c.y, 0)), ROOF, segs=12,
                  bevel=0.004, rot=(0, R(90 - EAVE_SLOPE), 0)))
    y += 0.115
edge = eave_c - Vector((math.cos(R(EAVE_SLOPE)), 0, math.sin(R(EAVE_SLOPE)))) * (EAVE_LEN / 2 + 0.02)
box("Eave_Fascia", (0.03, D + T + 0.2, 0.08), edge + Vector((0, 0, -0.01)), FRAME, bevel=0.004)
box("Eave_Ridge", (0.14, D + T + 0.2, 0.06), (-T / 2, (D + T) / 2 - 0.02, H + 0.1), ROOF, bevel=0.01)

PAVE_X, PAVE_Y = -T - 1.0, -1.05              # outer edges of the alley strip
ALLEY_Z = -0.02                                # top of the stone setts (one step down from the shop floor)
if ALLEY:
    base = mat("dark", 0.9)
    box("Alley_Base", (W - PAVE_X, -PAVE_Y, 0.2), ((W + PAVE_X) / 2, PAVE_Y / 2, -0.16), base, bevel=0.01)
    box("Alley_Base_Side", (-T - PAVE_X, D + T, 0.2), ((-T + PAVE_X) / 2, (D + T) / 2, -0.16), base, bevel=0.01)
    rnd = random.Random(SEED + 21)
    stones, s = [], 0.1
    yy = PAVE_Y + 0.13
    row = 0
    while yy < -0.16:                              # granite setts in running bond, laid along the alley
        xx = PAVE_X + 0.13 + (s / 2 if row % 2 else 0)
        while xx < W - 0.02:
            ww = min(s, W - xx)
            stones.append((xx + ww / 2, yy + s / 2, ALLEY_Z - 0.02 + rnd.uniform(-0.003, 0.002), ww - 0.008, s - 0.008,
                           0.04, rnd.randint(0, 1)))
            xx += s
        yy += s
        row += 1
    xx = PAVE_X + 0.13
    col = 0
    while xx < -T - 0.02:
        yy = -0.16 + (s / 2 if col % 2 else 0)
        while yy < D + T - 0.02:
            hh = min(s, D + T - yy)
            stones.append((xx + s / 2, yy + hh / 2, ALLEY_Z - 0.02 + rnd.uniform(-0.003, 0.002), s - 0.008, hh - 0.008,
                           0.04, rnd.randint(0, 1)))
            yy += s
        xx += s
        col += 1
    bmesh_boxes("Alley_Setts", stones, [SETT, SETT_2])
    kerb = M("sett", 0.4, "concrete", color="#8A8E96" if not NEON else "#4A4860")
    box("Kerb_Front", (W - PAVE_X, 0.13, 0.08), ((W + PAVE_X) / 2, PAVE_Y + 0.065, ALLEY_Z - 0.03), kerb, bevel=0.01)
    box("Kerb_Side", (0.13, D + T - PAVE_Y, 0.08), (PAVE_X + 0.065, (D + T + PAVE_Y) / 2, ALLEY_Z - 0.03), kerb, bevel=0.01)
    # Drain channel with a steel grate along the shop front.
    box("Drain_Channel", (W + T, 0.14, 0.03), ((W - T) / 2, -0.08, ALLEY_Z - 0.012), mat("dark", 0.6), bevel=0.003)
    grate = [(x0 + 0.01, -0.08, ALLEY_Z + 0.002, 0.012, 0.12, 0.008, 0) for x0 in
             (-T + 0.02 + k * 0.03 for k in range(int((W + T - 0.04) / 0.03)))]
    bmesh_boxes("Drain_Grate", grate, [IRON])
    # Rain puddles: mirror-flat, with soft reflections of the warm lights.
    PUDDLES = [(0.85, -0.55, 0.32, 0.16, 10), (2.75, -0.42, 0.42, 0.2, -8), (3.95, -0.74, 0.24, 0.12, 20),
               (-0.6, 1.4, 0.18, 0.34, 0), (-0.75, -0.62, 0.22, 0.14, 30)]
    for k, (px, py, rx, ry, a) in enumerate(PUDDLES):
        pd = cyl(f"Puddle_{k}", 1.0, 0.003, (px, py, ALLEY_Z + 0.004), PUDDLE, segs=40, bevel=0, rot=(0, 0, R(a)))
        pd.scale = (rx, ry, 1)
        if RAIN:
            for j in range(2):
                rr = no_shadow(tube(f"Puddle_Ripple_{k}_{j}", ring_pts(0.035 + j * 0.03, 0, 24), 0.0018, RAIN_MAT,
                                    closed=True, segs=4))
                rr.location = (px + (j - 0.5) * rx * 0.5, py + (0.5 - j) * ry * 0.4, ALLEY_Z + 0.007)

    # Japanese city bicycle (26-inch wheels, step-through frame, front basket, rear rack, centre stand).
    bike = empty("Bicycle", (2.35, -0.6, ALLEY_Z), rot=(0, 0, R(-4)))
    hook_link(bike, "linkedin")
    paint = M("accent_3", 0.35, "ceramic")
    rubber = mat("dark", 0.8)
    for nm, cx_ in (("Front", -0.58), ("Rear", 0.58)):
        c = Vector((cx_, 0, 0.33))
        tube(f"Bike_{nm}_Tyre", [c + Vector((0.31 * math.cos(a), 0, 0.31 * math.sin(a))) for a in
                                 (2 * math.pi * q / 40 for q in range(40))], 0.022, rubber, parent=bike, closed=True, segs=8)
        tube(f"Bike_{nm}_Rim", [c + Vector((0.29 * math.cos(a), 0, 0.29 * math.sin(a))) for a in
                                (2 * math.pi * q / 40 for q in range(40))], 0.008, STEEL, parent=bike, closed=True, segs=6)
        cyl(f"Bike_{nm}_Hub", 0.022, 0.09, c, STEEL, rot=(R(90), 0, 0), segs=12, parent=bike)
        for q in range(12):
            a = 2 * math.pi * q / 12
            tube(f"Bike_{nm}_Spoke", [c + Vector((0, 0.035 * (-1) ** q, 0)), c + Vector((0.285 * math.cos(a), 0, 0.285 * math.sin(a)))],
                 0.0016, STEEL, parent=bike, segs=4)
        a0, a1 = (R(25), R(165)) if cx_ < 0 else (R(15), R(150))
        tube(f"Bike_{nm}_Fender", [c + Vector((0.345 * math.cos(a), 0, 0.345 * math.sin(a))) for a in
                                   (a0 + (a1 - a0) * q / 14 for q in range(15))], 0.02, paint, parent=bike, segs=8)
    BB, HT, HB, ST = (0.04, 0, 0.3), (-0.42, 0, 0.86), (-0.47, 0, 0.66), (0.16, 0, 0.78)
    tube("Bike_DownTube", spline([(-0.455, 0, 0.73), (-0.32, 0, 0.45), (-0.12, 0, 0.31), BB], 5), 0.021, paint, parent=bike)
    tube("Bike_HeadTube", [HB, HT], 0.024, paint, parent=bike)
    tube("Bike_SeatTube", [BB, ST], 0.018, paint, parent=bike)
    tube("Bike_SeatPost", [ST, (0.185, 0, 0.88)], 0.012, STEEL, parent=bike)
    ball("Bike_Saddle", 0.1, (0.2, 0, 0.905), mat("walnut", 0.5, color="#3A2A22"), scale=(1.25, 0.75, 0.32), parent=bike)
    for sy in (-0.035, 0.035):
        tube("Bike_ChainStay", [(BB[0], sy, BB[2]), (0.58, sy, 0.33)], 0.011, paint, parent=bike)
        tube("Bike_SeatStay", [(0.14, sy, 0.72), (0.58, sy, 0.33)], 0.01, paint, parent=bike)
        tube("Bike_Fork", spline([(HB[0], sy, HB[2]), (-0.53, sy, 0.45), (-0.58, sy, 0.33)], 4), 0.012, paint, parent=bike)
        tube("Bike_Stand", [(0.5, sy * 1.6, 0.3), (0.6, sy * 4.2, 0.0)], 0.008, STEEL, parent=bike)
    box("Bike_ChainGuard", (0.56, 0.01, 0.11), (0.3, 0.06, 0.32), paint, bevel=0.03, parent=bike, rot=(0, R(-2), 0))
    cyl("Bike_Crank", 0.09, 0.012, (BB[0], 0.07, BB[2]), STEEL, rot=(R(90), 0, 0), segs=20, parent=bike)
    tube("Bike_Stem", [HT, (-0.4, 0, 0.98)], 0.013, STEEL, parent=bike)
    tube("Bike_Bars", spline([(-0.3, -0.29, 0.97), (-0.38, -0.16, 0.99), (-0.4, 0, 0.99), (-0.38, 0.16, 0.99),
                              (-0.3, 0.29, 0.97)], 4), 0.011, STEEL, parent=bike)
    for sy in (-1, 1):
        tube("Bike_Grip", [(-0.32, sy * 0.26, 0.975), (-0.29, sy * 0.33, 0.968)], 0.016, rubber, parent=bike)
    # wire front basket (31 x 22 x 24 cm) on struts to the front hub
    bc = Vector((-0.66, 0, 0.86))
    for zz in (0.0, 0.24):
        hw_, hd_ = (0.11, 0.155) if zz == 0 else (0.12, 0.165)
        tube("Bike_Basket_Ring", [bc + Vector((sx_ * hw_, sy_ * hd_, zz)) for sx_, sy_ in ((-1, -1), (1, -1), (1, 1), (-1, 1))],
             0.005, STEEL, parent=bike, closed=True, segs=5)
    for q in range(-3, 4):
        for sx_ in (-1, 1):
            tube("Bike_Basket_Wire", [bc + Vector((sx_ * 0.11, q * 0.044, 0)), bc + Vector((sx_ * 0.12, q * 0.047, 0.24))],
                 0.0025, STEEL, parent=bike, segs=4)
    for q in range(-2, 3):
        for sy_ in (-1, 1):
            tube("Bike_Basket_Wire", [bc + Vector((q * 0.044, sy_ * 0.155, 0)), bc + Vector((q * 0.048, sy_ * 0.165, 0.24))],
                 0.0025, STEEL, parent=bike, segs=4)
    box("Bike_Basket_Floor", (0.22, 0.31, 0.006), bc + Vector((0, 0, 0.003)), STEEL, bevel=0, parent=bike)
    for sy in (-0.03, 0.03):
        tube("Bike_Basket_Strut", [(-0.58, sy, 0.33), (-0.66, sy, 0.86)], 0.006, STEEL, parent=bike)
    box("Bike_Rack", (0.36, 0.14, 0.012), (0.56, 0, 0.7), STEEL, bevel=0.004, parent=bike)
    for sy in (-0.06, 0.06):
        tube("Bike_Rack_Strut", [(0.4, sy, 0.7), (0.58, sy, 0.34)], 0.006, STEEL, parent=bike)
    cyl("Bike_Lamp", 0.03, 0.05, (-0.62, 0, 0.74), mat("glow", 0.3, emit=3.0), rot=(0, R(90), 0), segs=14, parent=bike)
    ball("Bike_Bell", 0.022, (-0.37, 0.12, 1.01), STEEL, scale=(1, 1, 0.6), parent=bike)

    # Standing light-box street sign (34 x 34 x 130 cm): timber posts, glowing panels, the word RAMEN.
    sign = empty("Street_Sign", (-0.6, -0.58, ALLEY_Z), rot=(0, 0, R(CAMERA_TURN)))
    hook_link(sign, "website")
    box("Street_Sign_Base", (0.44, 0.44, 0.08), (0, 0, 0.04), M("dark", 0.7, "concrete", color="#4A4D55"), bevel=0.008,
        parent=sign)
    for sx in (-1, 1):
        for sy in (-1, 1):
            box("Street_Sign_Post", (0.035, 0.035, 1.24), (sx * 0.155, sy * 0.155, 0.08 + 0.62), FRAME_V, bevel=0.004,
                parent=sign)
    for a in range(4):
        ang = R(a * 90)
        face = box("Street_Sign_Panel", (0.28, 0.008, 1.08), (math.sin(ang) * 0.155, -math.cos(ang) * 0.155, 0.72), SIGN_FACE,
                   bevel=0, rot=(0, 0, ang), parent=sign)
        hook_link(face, "website")
    letters_mat = mat("main", 0.5, emit=0.25) if not NEON else NEON_B
    for k, ch in enumerate("RAMEN"):
        label(f"Street_Sign_Letter_{k}", ch, 0.17, (0, -0.162, 1.13 - k * 0.2), letters_mat, parent=sign, depth=0.004)
    box("Street_Sign_Cap", (0.42, 0.42, 0.04), (0, 0, 1.34), FRAME, bevel=0.006, parent=sign)
    cyl("Street_Sign_Roof", 0.3, 0.09, (0, 0, 1.405), ROOF, r2=0.03, segs=4, bevel=0.004, rot=(0, 0, R(45)), parent=sign)
    if NEON:
        no_shadow(tube("Neon_Street_Sign", [(-0.15, -0.165, 0.2), (0.15, -0.165, 0.2), (0.15, -0.165, 1.25),
                                            (-0.15, -0.165, 1.25)], 0.007, NEON_A, parent=sign, segs=6, closed=True))
    bpy.context.view_layer.update()
    glow_ = light("Light_Street_Sign", "SPOT", 14 if not NEON else 10, kelvin(3600) if not NEON else (1.0, 0.3, 0.8),
                  sign.matrix_world @ Vector((0, -0.3, 1.0)), aim=sign.matrix_world @ Vector((0, -0.35, 0.0)), size=0.2)
    glow_.data.spot_size, glow_.data.spot_blend = R(55), 0.8          # a pool of light on the wet setts only

    if RAIN:                                       # thin rain streaks over the alley
        rnd = random.Random(SEED + 31)
        for k in range(130):
            if k % 3:
                px, py = rnd.uniform(PAVE_X + 0.1, W - 0.05), rnd.uniform(PAVE_Y + 0.1, -0.1)
            else:
                px, py = rnd.uniform(PAVE_X + 0.1, -T - 0.08), rnd.uniform(-0.1, D)
            pz = rnd.uniform(0.15, 0.55) if k % 3 else rnd.uniform(0.15, H + 0.1)   # front: low, so it stays outside
            ln = rnd.uniform(0.14, 0.26)
            no_shadow(box(f"Rain_{k}", (0.004, 0.004, ln), (px, py, pz), RAIN_MAT, bevel=0, rot=(R(6), R(-8), 0)))

# Neon theme: a kanji-free neon pictogram (bowl and chopsticks) on the left wall and neon tubes on the wall caps.
if NEON:
    nx_, ny_, nz_ = 0.03, 0.75, 2.4
    no_shadow(tube("Neon_Bowl", spline([(nx_, ny_ - 0.2, nz_), (nx_, ny_ - 0.14, nz_ - 0.13), (nx_, ny_, nz_ - 0.18),
                                        (nx_, ny_ + 0.14, nz_ - 0.13), (nx_, ny_ + 0.2, nz_)], 5), 0.011, NEON_B, segs=8))
    no_shadow(tube("Neon_Bowl_Rim", [(nx_, ny_ - 0.23, nz_), (nx_, ny_ + 0.23, nz_)], 0.011, NEON_B, segs=8))
    for k in range(2):
        no_shadow(tube(f"Neon_Chopstick_{k}", [(nx_, ny_ + 0.02 + k * 0.06, nz_ + 0.02), (nx_, ny_ + 0.12 + k * 0.08, nz_ + 0.3)],
                       0.008, NEON_A, segs=8))
    for k in range(3):
        no_shadow(tube(f"Neon_Steam_{k}", spline([(nx_, ny_ - 0.1 + k * 0.07, nz_ + 0.05), (nx_, ny_ - 0.13 + k * 0.07, nz_ + 0.12),
                                                  (nx_, ny_ - 0.08 + k * 0.07, nz_ + 0.2)], 4), 0.007, NEON_A, segs=8))
    box("Neon_Backplate", (0.01, 0.56, 0.6), (0.006, ny_, nz_ + 0.05), mat("dark", 0.3), bevel=0.003)
    no_shadow(tube("Neon_Cap_Back", [(0.1, D - 0.04, H - 0.04), (W, D - 0.04, H - 0.04)], 0.008, NEON_B, segs=8),
              tube("Neon_Cap_Left", [(0.04, 0.0, H - 0.04), (0.04, D - 0.1, H - 0.04)], 0.008, NEON_A, segs=8))

# =====================================================================
#  LIGHTS, WORLD, CAMERA, RENDER
# =====================================================================
# Cool night sky light from over the alley, a soft fill from the camera side so the furniture keeps its shape,
# warm work light under the kitchen hood, a blue street lamp over the alley and a dim glow in the store room.
# The neon_rain theme swaps these for magenta / cyan light (NEON).
sky_k = kelvin(SUN_WARMTH) if not NEON else (0.55, 0.45, 1.0)
light("Light_Moon", "SUN", SUN_STRENGTH, sky_k, (-3, -1.5, 4.5), aim=(1.8, 1.8, 0), size=R(3))
light("Light_Fill", "AREA", 150 * (W * D / 16), kelvin(7500) if not NEON else (0.6, 0.55, 1.0), (W + 3, -3, H + 2.5),
      aim=(W / 2, D / 2, 0.6), size=6)
light("Light_Kitchen", "AREA", 70, kelvin(3800) if not NEON else (0.75, 0.95, 1.0), (hx, D - 0.36, HOOD_Z - 0.03),
      aim=(hx, D - 0.45, 0.0), size=1.5)
light("Light_Bounce", "AREA", 35, kelvin(LAMP_WARMTH + 600) if not NEON else (1.0, 0.45, 0.8), (W / 2, D / 2, H - 0.05),
      aim=(W / 2, D / 2, 0), size=2.5)
light("Light_Counter", "AREA", 40, kelvin(2600) if not NEON else (1.0, 0.4, 0.8), (1.7, COUNTER_Y - 0.5, 2.3),
      aim=(1.7, COUNTER_Y, 0.9), size=1.8)
light("Light_Street", "AREA", 90, kelvin(10000) if not NEON else (0.3, 0.9, 1.0), (1.5, -1.6, 2.9),
      aim=(1.2, -0.5, 0.0), size=2.5)
light("Light_Noren", "AREA", 18 if not NEON else 7, kelvin(3200) if not NEON else (0.5, 0.9, 1.0), (sum(BACK_DOOR_X) / 2 + 0.1, D - 0.75, 1.7),
      aim=(sum(BACK_DOOR_X) / 2, D, 1.35), size=0.4)
light("Light_Backroom", "POINT", 8, kelvin(2700), (sum(BACK_DOOR_X) / 2, D + T + 0.4, 1.6), size=0.2)
light("Light_Ticket", "AREA", 6, kelvin(4500) if not NEON else (0.4, 0.9, 1.0), (0.7, 1.64, 1.5), aim=(0.1, 1.64, 1.2),
      size=0.6)

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
bg_amb.inputs["Color"].default_value = lin(COLORS["sky"])
bg_amb.inputs["Strength"].default_value = 1.2
path = wn.new("ShaderNodeLightPath")
mix = wn.new("ShaderNodeMixShader")
wl.new(path.outputs["Is Camera Ray"], mix.inputs["Fac"])
wl.new(bg_amb.outputs[0], mix.inputs[1])
wl.new(bg_cam.outputs[0], mix.inputs[2])
wl.new(mix.outputs[0], out.inputs["Surface"])

# Orthographic camera that frames the whole room (and the alley + eave) automatically.
# kit_bounds must start at x = -T (check_room.py works out the room size from it). The alley and eave
# stick out to the left, so the box reaches further forward (-y) instead: the 45-degree camera sees that as
# the same left edge. Its bottom is raised a little so the extra reach adds no empty space under the room.
FRONT = PAVE_X + PAVE_Y + T if ALLEY else -0.6
BOUNDS = [-T, FRONT, -0.2 + 0.44 * ((PAVE_Y if ALLEY else 0.0) - FRONT), W, D + T, H + 0.12]
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
                    ("shadow_ray_count", 2), ("use_gtao", True), ("use_soft_shadows", True), ("use_bloom", True),
                    ("use_ssr", True), ("use_ssr_refraction", True)):
    if hasattr(ee, attr):
        setattr(ee, attr, value)
if hasattr(ee, "ray_tracing_options"):
    ee.ray_tracing_options.resolution_scale = "2" if "2" in [i.identifier for i in
        type(ee.ray_tracing_options).bl_rna.properties["resolution_scale"].enum_items] else ee.ray_tracing_options.resolution_scale
scene.view_settings.view_transform = "Standard"   # keeps your hex colours exactly as typed
scene.view_settings.exposure = 0.25 if not NEON else 0.3

# Remember the style so add_furniture.py can match colours later.
scene["kit_style"] = STYLE
scene["kit_version"] = KIT_VERSION
scene["kit_palette"] = json.dumps(COLORS)
scene["kit_material_finish"] = json.dumps({"roughness": 0.55, "bevel": 0.005, "saturation": 0.7})
scene["kit_theme"] = THEME
scene["kit_bounds"] = BOUNDS            # includes the alley and the eave outside the walls
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
