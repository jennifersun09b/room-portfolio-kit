"""
3D ROOM PORTFOLIO KIT  -  Template: ANIMAL CITY LOFT (a sunny apartment in a city built for every size)
=======================================================================================================
Builds a bright corner loft in a big, friendly city where residents of every size live side by side.
Signature: three doors for three sizes (a giraffe-height arched door, an ordinary door and a mouse door
with its own doormat, mailbox and lamp) under an "ALL SIZES WELCOME" sign, a height chart on the door
frame, and a big steel factory window looking out on an original city of climate districts side by side:
snowy peaks and ice-crystal towers, a sandstone desert quarter with palms, a tall downtown, and a misty
glass rainforest dome. Also: a kitchen island with a kettle, a toaster and a bowl of fruit and carrots,
cups and stools in three sizes, a step stool, a hat-and-coat board at three heights (the top hook at
giraffe height), a framed patrol-training certificate with a gold star badge and a toy patrol car, a
vintage radio and a smartphone showing a city map on an oak desk, a detective-style cork case board,
a pneumatic delivery tube, a paw-print rug, a hill-nook bed with a carrot cushion, a bamboo plant,
a mouse-scale cafe in the skirting and simple plush residents (an otter, a raccoon, a meerkat, a tortoise).
It renders a 1920x1080 image.
Your name and role are the headline of the framed newspaper; your projects are on the city billboard,
the case board photos, the newspaper photo and the transit-map poster. The delivery tube is your email.

HOW TO RUN
  Option A (no Blender UI):   blender -b -P animal_city_apartment.py
  Option B (inside Blender):  Scripting tab > Open > animal_city_apartment.py > Run Script (then F12 to render)

You only need to edit the SETTINGS block below. Everything under it builds the room.
Output: output/animal_city_apartment.png and output/animal_city_apartment.blend next to this script.
"""
# REFERENCES  (what each piece is modelled on; product names appear only here and in research/animal_city_apartment.md)
#   desk                   oak writing desk with a drawer pedestal (Garden Trading Oakworth type): W120 D60 H75 cm,
#                          25 mm top    https://www.gardentrading.co.uk/products/oakworth-desk.html
#   chair                  oak banker's swivel chair on a four-leg caster base: seat H47 cm, seat 46 x 42 cm,
#                          H86 cm      https://www.chairish.com/product/32050194/vintage-traditional-solid-wood-murphy-bankers-swivel-chair-w-casters
#   lamp                   green-glass banker's desk lamp: H36 cm, shade 24 x 13 cm, brass base 20 x 13 cm
#                          https://www.lampsplus.com/products/360-lighting-hammond-14-high-green-glass-and-brass-bankers-table-lamp__23r12.html
#   case board             cork notice board in a wooden frame: 120 x 90 cm, 15 mm frame depth
#                          https://www.esselte.com/en-nu/products/presentation--organisation/conference-products-av/esselte-standard-cork-noticeboard-wood-frame-120x90cm/
#   armchair               upholstered barrel tub chair: W80 D78 H76 cm, seat 43 cm
#                          https://www.livingspaces.com/pdp-wren-navy-blue-barrel-swivel-arm-chair-412230
#   floor_lamp             extra-tall reading floor lamp with a weighted round base (arc-lamp proportions,
#                          240 cm total height, 32 cm shade)   https://www.finnishdesignshop.com/en-us/product/arco-floor-lamp
#   bed                    single 90 x 200 cm platform / cabin bed, entry height ~50 cm, inside a built-in
#                          arched alcove (house-bed canopy type, 172 cm)  https://lifetimekidsrooms.com/products/cabin-bed
#   doors                  UK internal door 826 x 2040 x 40 mm; oversized arched pivot door 900 x 2950 mm
#                          https://www.designingbuildings.co.uk/wiki/Door_size
#   window                 W20-type steel factory window, 32 mm profile, ~40 mm sightlines, 4 x 4 panes (2.35 x 2.25 m)
#                          https://www.steelwindows.co.uk/w20-windows
#   delivery tube          hospital pneumatic tube system, 4-inch (110 mm) tube, 4-inch carrier 39 cm long
#                          https://www.kuka.com/-/media/swisslog-healthcare/documents/products-and-services/transport/translogic-pts/pts-210-translogic-pneumatic-tube-system-carriers-and-accessories.pdf
#   kitchen island         butcher-block kitchen trolley (IKEA FOERHOEJA type): W100 D43 H90 cm, 38 mm top,
#                          a drawer, a door, an open shelf, a towel rail, casters   https://www.ikea.com/gb/en/p/foerhoeja-kitchen-trolley-birch-80186575/
#   kettle / toaster       1.7 l dome kettle on a base (Smeg KLF03 type: 23 x 17 x 25 cm); 2-slice toaster
#                          (Smeg TSF01 type: 31 x 20 x 20 cm)   https://www.smeg.com/uk/products/klf03
#   stools                 tiny 25 cm milking stool, 65 cm bar stool (Tolix-type), 105 cm extra-tall stool
#                          with a footring   https://www.tolix.fr/en/stools
#   step stool             two-step wooden step stool (IKEA BEKVAEM type): H50 W43 D40 cm
#                          https://www.ikea.com/gb/en/p/bekvaem-step-stool-beech-80173948/
#   cups                   espresso cup 6 cl, mug 35 cl, a 3 l "giant" mug (jumbo novelty mug type)
#   certificate            A3 certificate in a 30 mm gilt frame (42 x 30 cm), gold foil seal and ribbon
#   badge / toy car        5-point metal star badge 16 cm on a display stand; 1:24 die-cast patrol car 20 cm
#                          https://www.maisto.com/1-24-scale-special-edition
#   smartphone             15 x 7.2 x 0.8 cm phone in a case, screen showing an original city map
#   hat-and-coat board     oak hook board with brass hooks at 0.46, 1.62 and 2.62 m and a hat shelf at 2.86 m
#   bamboo                 potted golden bamboo (Phyllostachys aurea) ~1.8 m in a 40 cm glazed pot
#                          https://www.gardenersworld.com/plants/phyllostachys-aurea/
#   paw rug                paw-print shaped wool rug, 180 x 170 cm (paw-shaped rug type)
#   carrot cushion         carrot-shaped plush bolster cushion 60 cm (food-shaped novelty cushion type)
#   welcome sign           painted timber fascia sign 150 x 18 cm, raised letters
#   suitcases              vintage hard-shell cases stacked as a bed-end table: 30" 77 x 51 x 25 cm, 21" 56 x 38 x 20 cm
#                          https://www.globe-trotter.com/collections/original
#   radio                  1950s tabletop valve radio: 33 x 16 x 19 cm   https://retroradiofarm.com/products/mint-green-vintage-1953-rca-victor-6-xd-5-tube-radio-excellent-condition-works-great
#   wall_shelf (mouse cafe) 1:12 dollhouse cafe pieces: chair 9.4 x 4 x 4 cm, cafe table set 10 x 6.5 x 9 cm
#                          https://minimumworld.com/rp18055-coffee-shop-chair.html
#   doormat                coir doormat 60 x 40 cm, 17 mm   https://relaxdays.co.uk/home/hallway/doormats/coir-doormats/coir-doormat-60x40-cm-10014666.html
#   plant                  potted golden bamboo ~180 cm (see bamboo above)
#   floor                  wide oak floorboards, 180 mm, random lengths

# =====================================================================
#  SETTINGS  -  change these lines, then run the script again
# =====================================================================
ROOM_NAME = "animal_city_apartment"   # used for the output file names

ROOM_WIDTH = 5.0                    # metres, left to right
ROOM_DEPTH = 4.4                    # metres, front to back
WALL_HEIGHT = 3.3                   # metres (a tall loft, so the giraffe-height door fits)

THEME = "sunny_downtown"            # pick one of the colour themes below
THEMES = {                          # any hex colour works; "main" is the room's hero colour
    # "sunny_downtown": white walls, teal dado, citrus orange / sunflower / lime colour blocking, midday sun.
    "sunny_downtown": {
        "background": "#DCEFEA", "wall": "#FBF8F2", "wall_trim": "#EFE3CF", "floor": "#D3A570", "floor_2": "#C59664",
        "wood": "#DDB582", "main": "#1E9E96", "accent_1": "#F5862A", "accent_2": "#F8C531", "accent_3": "#A3CC3C",
        "cream": "#FFF8EC", "plant": "#4C9A48", "dark": "#2B2D3A",
        "dado": "#22A39A", "terracotta": "#DB6A40", "hill": "#86C25A", "steel": "#33394A", "brass": "#D3A54A",
        "metal": "#C9CED3", "cork": "#C79560", "paper": "#F4EEDD", "ink": "#23242C", "red_string": "#D7322B",
        "glass": "#E4F5F6", "coir": "#B88A55", "bulb": "#FFE2B0", "pavement": "#D9D4CC",
        "sky_top": "#6FC4EA", "sky_mid": "#BDE8F1", "sky_low": "#FFE3B8", "haze": "#B9D9E6",
        "stone_light": "#F7FBFF", "deco": "#9FCDEB", "sand": "#EDC48A", "sandstone": "#DE9152", "garden": "#3E9E63",
        "leaf": "#78C257", "tower_glass": "#7FC6D3", "brick": "#C9744F", "window_glow": "#4F7F9E",
        "neon": "#FF5C9E", "otter": "#8B5E3C", "raccoon": "#8F939C", "mask": "#3A3A44", "meerkat": "#D8B07A",
        "shell": "#6FA544",
        # climate districts in the skyline + new props
        "snow": "#FFFFFF", "ice": "#8FD8F2", "ice_deep": "#4FA3D6", "peak": "#7D93C6", "dune": "#F6D9A0",
        "adobe": "#F0C98F", "dome": "#6FD9A8", "jungle": "#2E9556", "mist": "#F4FFFB", "carrot": "#F27A1E",
        "badge": "#E9B83A", "siren": "#3B7BE8",
    },
    # "neon_nightlife": the same loft at night - violet walls, teal and pink neon, the skyline lit up.
    # Night lights: see the NIGHT branches in the LIGHTS section (moonlight, brighter lamps, a billboard glow).
    "neon_nightlife": {
        "background": "#231C3D", "wall": "#A89FD8", "wall_trim": "#8378BE", "floor": "#9C7054", "floor_2": "#8E654B",
        "wood": "#BC8D64", "main": "#13B5AC", "accent_1": "#FF6B3D", "accent_2": "#FFCF3A", "accent_3": "#B5EE3A",
        "cream": "#F6EEFF", "plant": "#3E8C5C", "dark": "#1B1730",
        "dado": "#5A43A8", "terracotta": "#D45A3E", "hill": "#5DAA5A", "steel": "#2A2840", "brass": "#E0B050",
        "metal": "#BFC3D6", "cork": "#B98A58", "paper": "#ECE6F2", "ink": "#1D1B2A", "red_string": "#FF3B4A",
        "glass": "#D6E6FF", "coir": "#A57C50", "bulb": "#FFD49A", "pavement": "#6A6488",
        "sky_top": "#0D0B26", "sky_mid": "#2E1C5E", "sky_low": "#A8327E", "haze": "#3E2E73",
        "stone_light": "#D8E4FF", "deco": "#5C7FC4", "sand": "#B98458", "sandstone": "#9C5A3E", "garden": "#1F6B52",
        "leaf": "#3E9C5C", "tower_glass": "#2B6F8E", "brick": "#7A4060", "window_glow": "#FFD36B",
        "neon": "#FF4FA3", "otter": "#7E5436", "raccoon": "#868A98", "mask": "#2E2C3A", "meerkat": "#CFA470",
        "shell": "#5C9A44",
        "snow": "#CFD8F6", "ice": "#5ED2F5", "ice_deep": "#3C83C6", "peak": "#4C5592", "dune": "#B88555",
        "adobe": "#A86A48", "dome": "#44C49A", "jungle": "#1E6E4A", "mist": "#BFD0FF", "carrot": "#FF7B26",
        "badge": "#F2C14E", "siren": "#4A8BFF",
    },
}

SUN_WARMTH = 5400                   # Kelvin: 2500 = sunset orange, 6500 = white daylight (5400 = bright midday)
SUN_STRENGTH = 4.0
LAMP_WARMTH = 2700                  # Kelvin of the lamp bulbs (desk lamp, tall floor lamp, nook lights)
LAMP_STRENGTH = 8                   # Watts of the desk lamp bulb (the other lamps scale with it)
SKYLINE_GLOW = 1.0                  # brightness of the city seen through the window
STRING_LIGHTS = True                # little warm lights inside the hill nook and over the mouse cafe
SEED = 5                            # change to shuffle fruit, papers, tower windows and props

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
NIGHT = THEME == "neon_nightlife"   # night theme: lit skyline windows, neon glow, moonlight

STYLE = "animal_city_apartment"
KIT_VERSION = 2
W, D, H = ROOM_WIDTH, ROOM_DEPTH, WALL_HEIGHT
T = 0.15            # wall thickness
FLOOR_Z = 0.02      # top of the oak floorboards; furniture stands here
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


# The room's real materials (one place, so every piece uses the same oak, paint, steel...).
OAK = M("wood", 0.5, "wood")                       # light oak: desk, bed frame, shelves, picture frames
OAK_V = M("wood", 0.52, "wood", along="Z")         # vertical grain: legs, uprights
OAK_Y = M("wood", 0.51, "wood", along="Y")         # grain along Y: pieces on the left wall
PLASTER = M("wall", 0.85, "plaster")               # clean white plaster walls
DADO = M("dado", 0.62, "plaster", scale=3)         # colour-blocked painted dado (lower wall)
TRIM = M("wall_trim", 0.55, "plaster", scale=3)    # painted skirting, rails and architraves
CAP = M("terracotta", 0.5, "plaster", scale=3)     # painted cap on top of the walls
STEEL = M("steel", 0.42, "brushed", metal=0.6)     # powder-coated steel window frame
BRASS = M("brass", 0.3, "brushed", metal=1.0)
CHROME = M("metal", 0.15, "brushed", metal=1.0, along="Z")
IRON = M("dark", 0.5, "brushed", metal=0.7)
TEAL_METAL = M("main", 0.38, "plaster", scale=3)     # painted steel: delivery tube
CORK = M("cork", 0.9, "terrazzo", scale=3)
MARBLE = M("cream", 0.2, "marble")
PAPER = M("cream", 0.8, "paper")
NEWS = M("paper", 0.85, "paper")                    # newsprint
MANILA = M("sand", 0.85, "paper")                   # case-file folders
INK = mat("ink", 0.6)
BEAD = mat("ink", 0.15)                             # shiny black safety eyes on the plush
CHAIR_FAB = M("accent_1", 0.9, "fabric")            # tub chair upholstery
PIPING = M("cream", 0.88, "fabric")
LINEN = M("cream", 0.9, "fabric")
DUVET = M("accent_2", 0.9, "fabric")
THROW = M("main", 0.95, "knit")
LINING = M("accent_2", 0.93, "knit")                # soft lining inside the hill hood
CERAMIC = M("cream", 0.3, "ceramic")
BAKELITE = M("accent_2", 0.32, "ceramic")           # glossy radio cabinet
TERRA = M("terracotta", 0.8, "concrete", scale=3)   # terracotta pots
PAINT_TALL = M("accent_2", 0.45, "plaster", scale=3)  # giraffe door: sunflower
PAINT_DOOR = M("terracotta", 0.46, "plaster", scale=3)  # ordinary door: terracotta
PAINT_MINI = M("accent_3", 0.45, "plaster", scale=3)  # mouse door: lime
PAINT_TEAL = M("main", 0.44, "plaster", scale=3)
HILL = M("hill", 0.75, "plaster", scale=2)          # painted plywood "hill" over the hill-nook bed
PAVE = M("pavement", 0.8, "concrete", scale=4)
COIR = M("coir", 0.95, "knit", scale=3)
SHADE = M("accent_2", 0.3, "ceramic")               # enamel lamp shade
GLASS_SHADE = M("main", 0.15, "ceramic")            # banker's lamp glass shade
GLASS = mat("glass", 0.05, alpha=0.1)
CAPSULE = mat("glass", 0.04, alpha=0.32)
GLINT = mat("cream", 0.1, emit=0.25 if NIGHT else 0.45, alpha=0.1 if NIGHT else 0.16)   # reflections on glass
BULB = mat("bulb", 0.4, emit=6.0)
WARM_GLOW = mat("bulb", 0.4, emit=1.6)
RUBBER = mat("dark", 0.8)
SOIL = mat("soil", 0.95, color="#3A2A20")
RED = mat("red_string", 0.55)
LEAF = mat("plant", 0.55)
STEM = mat("plant", 0.6, color="#5E7F3A")
CANVAS_A = M("accent_1", 0.86, "fabric")
CANVAS_B = M("cream", 0.87, "fabric")
CANVAS_C = M("accent_3", 0.86, "fabric")
OTTER = M("otter", 0.95, "knit")
RACCOON = M("raccoon", 0.95, "knit")
MASK = M("mask", 0.95, "knit")
MEERKAT = M("meerkat", 0.95, "knit")
SHELL = M("shell", 0.95, "knit")
SKIN = M("hill", 0.94, "knit")
FLUFF = M("cream", 0.94, "knit")


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


def rod(name, a, b, r, material, parent=None, segs=12, r2=None):
    """Cylinder from point a to point b (radius r at a, r2 at b): legs, poles, spindles."""
    a, b = Vector(a), Vector(b)
    o = cyl(name, r, (b - a).length, (a + b) / 2, material, r2=r2, segs=segs, bevel=0, parent=parent)
    o.rotation_euler = (b - a).to_track_quat("Z", "Y").to_euler()
    return o


def spline(ctrl, steps=6, closed=False):
    """Smooth Catmull-Rom curve through control points (for bentwood, cords, rails, string)."""
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
    """Round tube swept along a path: rails, cords, the delivery tube, red string, tails."""
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


def lathe(name, prof, loc, material, segs=32, parent=None, rot=(0, 0, 0), scale=(1, 1, 1)):
    """Turned shape from a (radius, height) profile: pots, mugs, lamp shades, bottles."""
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


def prism(name, pts, depth, loc, material, rot=(0, 0, 0), parent=None, bevel=0.003):
    """Flat outline in the XZ plane ((x, z) pairs) extruded along Y: arched doors, shades, signs."""
    bm = bmesh.new()
    front = [bm.verts.new((x, -depth / 2, z)) for x, z in pts]
    back = [bm.verts.new((x, depth / 2, z)) for x, z in pts]
    bm.faces.new(front)
    bm.faces.new(list(reversed(back)))
    n = len(pts)
    for i in range(n):
        j = (i + 1) % n
        bm.faces.new((front[i], front[j], back[j], back[i]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, bevel, None, parent)


def arch_pts(w, h, segs=16, z0=0.0):
    """Outline of an arched door: straight sides and a half-round top, centred on x = 0. (x, z) pairs."""
    r = w / 2
    pts = [(-r, z0), (r, z0)]
    for k in range(segs + 1):
        a = math.pi * k / segs
        pts.append((r * math.cos(a), z0 + h - r + r * math.sin(a)))
    return pts


def band(name, out_r, in_r, ext, material, a0=0.0, a1=math.pi, segs=24, plane="XZ", loc=(0, 0, 0),
         rot=(0, 0, 0), parent=None, bevel=0.0):
    """Curved slab between two ellipses (radii out_r, in_r = (rx, rz)) from angle a0 to a1, extruded over
    ext = (e0, e1). plane "XZ": an arch standing up, extruded along Y (door heads, the hill hood).
    plane "XY": a horseshoe lying flat, extruded up along Z (the tub chair's back and arms)."""
    def P(rx, rz, a, e):
        u, v = rx * math.cos(a), rz * math.sin(a)
        return (u, e, v) if plane == "XZ" else (u, v, e)

    angs = [a0 + (a1 - a0) * k / segs for k in range(segs + 1)]
    bm = bmesh.new()
    rings = [([bm.verts.new(P(*out_r, a, e)) for a in angs], [bm.verts.new(P(*in_r, a, e)) for a in angs])
             for e in ext]
    (o0, i0), (o1, i1) = rings
    for k in range(segs):
        for quad in ((o0[k], o0[k + 1], o1[k + 1], o1[k]), (i0[k], i1[k], i1[k + 1], i0[k + 1]),
                     (o0[k], i0[k], i0[k + 1], o0[k + 1]), (o1[k], o1[k + 1], i1[k + 1], i1[k])):
            bm.faces.new(quad)
    bm.faces.new((o0[0], o1[0], i1[0], i0[0]))
    bm.faces.new((o0[-1], i0[-1], i1[-1], o1[-1]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, bevel, None, parent)


def mesh_obj(name, verts, faces, material, loc=(0, 0, 0), rot=(0, 0, 0), parent=None):
    me = bpy.data.meshes.new(name)
    me.from_pydata(verts, [], faces)
    me.update()
    o = bpy.data.objects.new(name, me)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, 0, None, parent)


def subsurf(o, levels=1):
    m = o.modifiers.new("Subsurf", "SUBSURF")
    m.levels = m.render_levels = levels
    return o


def puffy(name, sx, sy, thick, loc, material, rot=(0, 0, 0), parent=None, n=12, waist=0.06):
    """Pillow / duvet / cushion: two bulging faces sewn together at a pinched seam (sx, sy = flat size)."""
    verts, index, faces = [], {}, []

    def vid(i, j, side):
        edge = i in (0, n) or j in (0, n)
        key = (i, j) if edge else (i, j, side)
        if key not in index:
            u, v = -1 + 2 * i / n, -1 + 2 * j / n
            h = thick / 2 * ((1 - u * u) * (1 - v * v)) ** 0.4
            index[key] = len(verts)
            verts.append((u * sx / 2 * (1 - waist * (1 - v * v)), v * sy / 2 * (1 - waist * (1 - u * u)), side * h))
        return index[key]

    for i in range(n):
        for j in range(n):
            faces.append((vid(i, j, 1), vid(i + 1, j, 1), vid(i + 1, j + 1, 1), vid(i, j + 1, 1)))
            faces.append((vid(i, j + 1, -1), vid(i + 1, j + 1, -1), vid(i + 1, j, -1), vid(i, j, -1)))
    return subsurf(mesh_obj(name, verts, faces, material, loc, rot, parent), 1)


def torus(name, ring_r, tube_r, loc, material, parent=None, seg=32, tseg=10, rot=(0, 0, 0)):
    verts = []
    for i in range(seg):
        a = 2 * math.pi * i / seg
        for j in range(tseg):
            b = 2 * math.pi * j / tseg
            rr = ring_r + tube_r * math.cos(b)
            verts.append((rr * math.cos(a), rr * math.sin(a), tube_r * math.sin(b)))
    faces = [(i * tseg + j, ((i + 1) % seg) * tseg + j, ((i + 1) % seg) * tseg + (j + 1) % tseg, i * tseg + (j + 1) % tseg)
             for i in range(seg) for j in range(tseg)]
    return mesh_obj(name, verts, faces, material, loc, rot, parent)


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


def label(name, body, size, loc, material, rot=(R(90), 0, 0), align="CENTER", parent=None, depth=0.003):
    """Plain 3D text that is NOT a portfolio hook (shop signs, map titles, the masthead)."""
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


def disc(name, r, h, loc, normal, material, parent=None, segs=24):
    """Thin round plate facing 'normal' (buttons, dials, station dots, portholes)."""
    o = cyl(name, r, h, loc, material, segs=segs, bevel=min(0.002, h * 0.4), parent=parent)
    o.rotation_euler = Vector(normal).to_track_quat("Z", "Y").to_euler()
    return o


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
    """Mark decoration that is hidden once the hook gets a real image (e.g. a doodle on a photo)."""
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
#  ROOM SHELL: oak floorboards, white plaster, a colour-blocked dado, a steel factory window
# =====================================================================
box("Floor_Base", (W + T, D + T, 0.2), ((W - T) / 2, (D + T) / 2, -0.1), M("dado", 0.7, "concrete", scale=2),
    bevel=0.02)
box("Floor_Joints", (W, D, 0.004), (W / 2, D / 2, 0.002), mat("dark", 0.9), bevel=0)   # dark gaps between boards


def floorboards(x0, y0, x1, y1, pw=0.18, gap=0.0018):
    """Wide oak boards in random lengths, joints staggered, two slightly different tones (one mesh)."""
    rnd = random.Random(SEED + 3)
    bm = bmesh.new()
    y = y0
    while y < y1 - 1e-6:
        yb = min(y + pw, y1)
        x = x0 - rnd.uniform(0.0, 1.2)
        while x < x1 - 1e-6:
            length = rnd.uniform(0.9, 1.9)
            xa, xb = max(x, x0), min(x + length, x1)
            if xb - xa > 0.05:
                mi = rnd.randint(0, 1)
                vs = [bm.verts.new((px, py, pz)) for pz in (0.004, FLOOR_Z)
                      for px, py in ((xa + gap, y + gap), (xb - gap, y + gap), (xb - gap, yb - gap), (xa + gap, yb - gap))]
                for f in ((0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)):
                    bm.faces.new([vs[i] for i in f]).material_index = mi
            x += length
        y = yb
    o = _obj("Floor_Boards", bm)
    o.data.materials.append(M("floor", 0.42, "veneer"))
    o.data.materials.append(M("floor_2", 0.42, "veneer"))
    COL_ROOM.objects.link(o)
    return o


floorboards(0, 0, W, D)

# Left wall: a big steel factory window looking out on the city. Back wall: the three doors.
WIN_Y, WIN_Z = (0.5, 2.85), (0.85, 3.1)    # a big 4 x 4 pane factory window
wy, wz = sum(WIN_Y) / 2, sum(WIN_Z) / 2
ww, wh = WIN_Y[1] - WIN_Y[0], WIN_Z[1] - WIN_Z[0]
left = box("Wall_Left", (T, D + T, H), (-T / 2, (D + T) / 2, H / 2), PLASTER, bevel=0.0)
cutter = box("Window_Cutter", (T * 3, ww, wh), (-T / 2, wy, wz), mat("wall"), bevel=0.0)
cutter.hide_render = cutter.hide_viewport = True
boolean = left.modifiers.new("Window", "BOOLEAN")
boolean.operation, boolean.object = "DIFFERENCE", cutter
box("Wall_Back", (W + T, T, H), ((W - T) / 2, D + T / 2, H / 2), PLASTER, bevel=0.0)
box("Trim_Top_Back", (W + T + 0.04, T + 0.06, 0.08), ((W - T) / 2, D + T / 2, H + 0.04), CAP, bevel=0.01)
box("Trim_Top_Left", (T + 0.06, D + T + 0.04, 0.08), (-T / 2, (D + T) / 2 - 0.02, H + 0.04), CAP, bevel=0.01)

# Painted dado (colour block) up to a 0.8 m oak chair rail, white above; 100 mm skirting at the bottom.
DADO_H, SK = 0.8, 0.1
GIRAFFE_X = (1.15, 2.05)          # giraffe-height arched door (0.9 x 2.95 m)
DOOR_X = (2.48, 3.306)            # ordinary 826 x 2040 mm door
MOUSE_X = 2.265                   # mouse door (centre), 17 x 25 cm, between the two big doors
HOOKS_X = 3.62                    # coat-hook board at three heights
back_runs = [(0.0, GIRAFFE_X[0] - 0.07), (GIRAFFE_X[1] + 0.07, DOOR_X[0] - 0.07), (DOOR_X[1] + 0.07, W)]
skirt_runs = [(0.0, GIRAFFE_X[0] - 0.07), (GIRAFFE_X[1] + 0.07, MOUSE_X - 0.105), (MOUSE_X + 0.105, DOOR_X[0] - 0.07),
              (DOOR_X[1] + 0.07, W)]
for k, (xa, xb) in enumerate(back_runs):
    box(f"Dado_Back_{k}", (xb - xa, 0.004, DADO_H - FLOOR_Z), ((xa + xb) / 2, D - 0.002, (DADO_H + FLOOR_Z) / 2),
        DADO, bevel=0)
    box(f"Rail_Back_{k}", (xb - xa, 0.022, 0.03), ((xa + xb) / 2, D - 0.011, DADO_H), OAK, bevel=0.004)
for k, (xa, xb) in enumerate(skirt_runs):
    box(f"Skirting_Back_{k}", (xb - xa, 0.018, SK), ((xa + xb) / 2, D - 0.009 - 0.004, FLOOR_Z + SK / 2), TRIM,
        bevel=0.004)
CAFE_Y = (1.1, 2.0)               # the mouse cafe is built into the skirting under the window
box("Dado_Left", (0.004, D, DADO_H - FLOOR_Z), (0.002, D / 2, (DADO_H + FLOOR_Z) / 2), DADO, bevel=0)
box("Rail_Left", (0.022, D, 0.03), (0.011, D / 2, DADO_H), OAK_Y, bevel=0.004)
for nm, (ya, yb) in (("Front", (0.0, CAFE_Y[0])), ("Back", (CAFE_Y[1], D))):
    box(f"Skirting_Left_{nm}", (0.018, yb - ya, SK), (0.013, (ya + yb) / 2, FLOOR_Z + SK / 2), TRIM, bevel=0.004)

# Steel factory window (W20-type, 32 mm profile): perimeter frame, 3 mullions, 3 transoms = 16 panes.
XG = -0.05                                           # plane of the glass, set back in the reveal
for nm, size, loc in [("Head", (0.06, ww, 0.045), (XG, wy, WIN_Z[1] - 0.0225)),
                      ("Sill", (0.06, ww, 0.045), (XG, wy, WIN_Z[0] + 0.0225)),
                      ("Jamb_F", (0.06, 0.045, wh), (XG, WIN_Y[0] + 0.0225, wz)),
                      ("Jamb_B", (0.06, 0.045, wh), (XG, WIN_Y[1] - 0.0225, wz))]:
    box(f"Window_Frame_{nm}", size, loc, STEEL, bevel=0.004)
COLS, ROWS = 4, 4
for k in range(1, COLS):
    box("Window_Mullion", (0.045, 0.03, wh), (XG, WIN_Y[0] + ww * k / COLS, wz), STEEL, bevel=0.003)
for k in range(1, ROWS):
    box("Window_Transom", (0.045, ww, 0.03), (XG, wy, WIN_Z[0] + wh * k / ROWS), STEEL, bevel=0.003)
no_shadow(box("Window_Glass", (0.004, ww - 0.04, wh - 0.04), (XG, wy, wz), GLASS, bevel=0))
for (c, r_) in ((0, 1), (3, 2), (1, 3), (3, 0)):           # soft reflections on a few panes (not the billboard's)
    gy, gz = WIN_Y[0] + ww * (c + 0.5) / COLS, WIN_Z[0] + wh * (r_ + 0.5) / ROWS
    for dy, wdt, ln in ((-0.08, 0.05, 0.3), (0.04, 0.018, 0.2)):
        no_shadow(box("Window_Glint", (0.002, wdt, ln), (XG + 0.004, gy + dy, gz), GLINT, bevel=0, rot=(R(-38), 0, 0)))
box("Window_Board", (0.25, ww + 0.12, 0.03), (0.075, wy, WIN_Z[0] + 0.015), OAK_Y, bevel=0.004)
box("Window_Handle_Plate", (0.012, 0.02, 0.07), (XG + 0.03, WIN_Y[0] + ww / 4 - 0.05, WIN_Z[0] + wh / 2), BRASS,
    bevel=0.002)
rod("Window_Handle", (XG + 0.035, WIN_Y[0] + ww / 4 - 0.05, WIN_Z[0] + wh / 2 + 0.02),
    (XG + 0.035, WIN_Y[0] + ww / 4 - 0.05, WIN_Z[0] + wh / 2 - 0.09), 0.006, BRASS)


# =====================================================================
#  THE CITY OUTSIDE  (an original city of climate districts side by side, in a shallow light box behind the window)
#  Seen from the camera, a point d metres behind the glass shows through the window d metres further
#  back (+y) and 0.88 d lower, so everything is placed inside that visible band.
# =====================================================================
CITY_EMIT = 0.16 if NIGHT else 0.5


def city_mat(key, emit=None):
    return mat(key, 0.7, emit=CITY_EMIT if emit is None else emit)


def sky_material():
    """Tilt-shift sky: warm haze at the horizon, clear colour higher up (an emission gradient)."""
    m = bpy.data.materials.new("M_sky")
    if bpy.app.version < (5, 0, 0):
        m.use_nodes = True
    nt, b = m.node_tree, _principled(m)
    coords = nt.nodes.new("ShaderNodeTexCoord")
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    rng = nt.nodes.new("ShaderNodeMapRange")
    rng.inputs["From Min"].default_value, rng.inputs["From Max"].default_value = 0.6, 2.6
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    els = ramp.color_ramp.elements
    els[0].position, els[0].color = 0.0, lin(COLORS["sky_low"])
    els[1].position, els[1].color = 1.0, lin(COLORS["sky_top"])
    els.new(0.4).color = lin(COLORS["sky_mid"])
    nt.links.new(coords.outputs["Object"], sep.inputs[0])
    nt.links.new(sep.outputs["Z"], rng.inputs["Value"])
    nt.links.new(rng.outputs["Result"], ramp.inputs["Fac"])
    nt.links.new(ramp.outputs["Color"], b.inputs["Base Color"])
    nt.links.new(ramp.outputs["Color"], b.inputs["Emission Color" if "Emission Color" in b.inputs else "Emission"])
    _set(b, ["Emission Strength"], 1.0 * SKYLINE_GLOW)
    m.diffuse_color = lin(COLORS["sky_mid"])
    m["kit_color_key"] = "sky_mid"
    return m


BOX_X0, BOX_Y, BOX_Z = -T - 0.5, (0.5, 3.5), (-0.1, 2.74)
LID_F, LID_B = 3.14, 2.74                            # the light box lid slopes down so it never shows over the wall
bm = bmesh.new()
sx = BOX_X0 + 0.02
vs = [bm.verts.new((sx, y, z)) for y, z in ((BOX_Y[0], BOX_Z[0]), (BOX_Y[1], BOX_Z[0]), (BOX_Y[1], BOX_Z[1]),
                                              (BOX_Y[0], BOX_Z[1]))]
bm.faces.new(vs)
sky = _obj("City_Sky", bm)
sky.data.materials.append(sky_material())
COL_ROOM.objects.link(sky)
skin = mat("wall", 0.8)                              # the light box's outside, painted like the walls
bw = -T - BOX_X0
box("City_Box_Back", (0.02, BOX_Y[1] - BOX_Y[0], BOX_Z[1] - BOX_Z[0]), (BOX_X0 + 0.01, sum(BOX_Y) / 2, sum(BOX_Z) / 2),
    skin, bevel=0)
box("City_Box_Bottom", (bw, BOX_Y[1] - BOX_Y[0], 0.03), (BOX_X0 + bw / 2, sum(BOX_Y) / 2, BOX_Z[0] - 0.015), skin, bevel=0)
mesh_obj("City_Box_Lid", [(-T, BOX_Y[0], LID_F), (-T, BOX_Y[1], LID_F), (BOX_X0, BOX_Y[1], LID_B), (BOX_X0, BOX_Y[0], LID_B)],
         [(0, 1, 2, 3)], skin)
for nm, yy in (("Front", BOX_Y[0] - 0.015), ("End", BOX_Y[1] + 0.015)):
    prism(f"City_Box_{nm}", [(-T, BOX_Z[0]), (BOX_X0, BOX_Z[0]), (BOX_X0, LID_B), (-T, LID_F)], 0.03, (0, yy, 0), skin,
          bevel=0)

crnd = random.Random(SEED + 11)
WIN_LIT = mat("window_glow", 0.2, emit=2.6 if NIGHT else 0.12)
WIN_DARK = mat("window_glow", 0.25, emit=0.0, color="#2A2D4A" if NIGHT else "#5F8DAA")
WIN_PINK = mat("neon", 0.2, emit=2.2 if NIGHT else 0.0)


def bx(d):
    """x of a facade that stands d metres behind the window glass."""
    return XG - d


def wy_(yw, d):
    """World y of something d metres behind the glass that the camera sees at window position yw."""
    return yw + d


def wz_(zw, d):
    """World z of something d metres behind the glass that the camera sees at window height zw."""
    return zw - 0.88 * d


def tower(name, y, d, w, z1, key, depth=0.08, z0=0.4, emit=None):
    return box(f"City_{name}", (depth, w, z1 - z0), (bx(d) - depth / 2, y, (z0 + z1) / 2), city_mat(key, emit),
               bevel=0.004)


def wtower(name, yw, d, w, zw1, key, depth=0.08, zw0=0.9, emit=None):
    """A tower placed in WINDOW coordinates: it shows at (yw, up to zw1) in the window."""
    return tower(name, wy_(yw, d), d, w, wz_(zw1, d), key, depth, wz_(zw0, d), emit)


def windows(name, y, d, w, z0, z1, cols, rows, size=(0.03, 0.04), lit=0.6):
    for i in range(cols):
        for j in range(rows):
            yy = y - w / 2 + w * (i + 0.5) / cols
            zz = z0 + (z1 - z0) * (j + 0.5) / rows
            m = WIN_LIT if crnd.random() < lit else WIN_DARK
            if NIGHT and crnd.random() < 0.12:
                m = WIN_PINK
            box(f"City_{name}_Win", (0.006, size[0], size[1]), (bx(d) + 0.002, yy, zz), m, bevel=0)


def wwindows(name, yw, d, w, zw0, zw1, cols, rows, size=(0.03, 0.04), lit=0.6):
    windows(name, wy_(yw, d), d, w, wz_(zw0, d), wz_(zw1, d), cols, rows, size, lit)


def ridge(name, d, pts_w, key, depth=0.04, emit=None):
    """A flat silhouette (mountains, dunes, snow caps) from (yw, zw) window points, d metres behind the glass."""
    pts = [(wy_(yw, d), wz_(zw, d)) for yw, zw in pts_w]
    return prism(f"City_{name}", pts, depth, (bx(d) - depth / 2, 0, 0), city_mat(key, emit), rot=(0, 0, R(90)),
                 bevel=0)


# far, hazy towers behind everything (thin flats), mostly behind downtown
for k, (yw, w, top) in enumerate(((1.62, 0.16, 2.75), (1.98, 0.14, 2.95), (2.3, 0.2, 2.55), (2.62, 0.16, 2.35))):
    wtower(f"Haze_{k}", yw, 0.5, w, top, "haze", depth=0.02)
    wwindows(f"Haze_{k}", yw, 0.5, w * 0.8, 1.6, top - 0.08, 3, int((top - 1.6) / 0.12), size=(0.018, 0.026), lit=0.3)

# ---- SNOW DISTRICT (left): snowy peaks, ice-crystal towers, snow-roofed chalets and frosted pines ----------
MT_D = 0.54
MT = [(0.42, 1.2), (0.47, 2.05), (0.6, 2.42), (0.7, 2.26), (0.86, 2.86), (1.0, 2.5), (1.1, 2.64), (1.3, 2.12),
      (1.48, 1.7), (1.6, 1.2)]
ridge("Mountains_Far", MT_D + 0.03, [(0.42, 1.4), (0.52, 2.5), (0.66, 2.68), (0.78, 2.5), (1.18, 2.76), (1.42, 2.3),
                                      (1.62, 2.0), (1.62, 1.4)], "haze", depth=0.01)
ridge("Mountains", MT_D, MT, "peak", depth=0.03)
for k in (2, 4, 6):                                  # a snow cap on each peak with a ragged lower edge
    (y0, z0), (y1, z1), (y2, z2) = MT[k - 1], MT[k], MT[k + 1]
    f = 0.5
    a = (y1 + (y0 - y1) * f, z1 + (z0 - z1) * f)
    b = (y1 + (y2 - y1) * f, z1 + (z2 - z1) * f)
    rag = [a]
    for j in range(1, 5):
        t = j / 5
        rag.append((a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t - (0.05 if j % 2 else 0.0)))
    ridge(f"Snowcap_{k}", MT_D - 0.004, [(y1, z1)] + rag + [b], "snow", depth=0.004,
          emit=CITY_EMIT + 0.15)
ICE_D = 0.34
ICE_EMIT = 1.1 if NIGHT else 0.55
ice_m, ice_deep = city_mat("ice", ICE_EMIT), city_mat("ice_deep", ICE_EMIT * 0.8)
for k, (yw, r, top) in enumerate(((0.66, 0.055, 2.28), (0.84, 0.075, 2.7), (1.02, 0.05, 2.05))):
    cx, cy = bx(ICE_D) - r, wy_(yw, ICE_D)
    zt, zb = wz_(top, ICE_D), wz_(0.95, ICE_D)
    tip = r * 2.6
    cyl(f"City_Ice_Tower_{k}", r, zt - tip - zb, (cx, cy, (zb + zt - tip) / 2), ice_m, segs=6, bevel=0.002)
    cyl(f"City_Ice_Tip_{k}", r, tip, (cx, cy, zt - tip / 2), ice_m, r2=0.0, segs=6, bevel=0)
    for j in range(int((zt - tip - zb) / 0.16)):     # frosted floor bands and a lit facet line
        cyl(f"City_Ice_Band_{k}", r + 0.004, 0.012, (cx, cy, zb + 0.12 + j * 0.16), city_mat("snow", CITY_EMIT + 0.2),
            segs=6, bevel=0)
    box(f"City_Ice_Facet_{k}", (0.004, 0.008, zt - tip - zb - 0.1), (cx + r + 0.001, cy, (zb + zt - tip) / 2),
        ice_deep, bevel=0)
    cyl(f"City_Ice_Snow_{k}", r * 0.55, tip * 0.4, (cx, cy, zt - tip * 0.2), city_mat("snow", CITY_EMIT + 0.3), r2=0.0,
        segs=6, bevel=0)
CH_D = 0.22
for k, (yw, w, top, key) in enumerate(((0.56, 0.16, 1.42, "terracotta"), (0.76, 0.2, 1.5, "wood"),
                                       (0.98, 0.15, 1.4, "accent_1"))):
    y, zt = wy_(yw, CH_D), wz_(top, CH_D)
    zb = wz_(0.85, CH_D)
    box(f"City_Chalet_{k}", (0.06, w, zt - zb), (bx(CH_D) - 0.03, y, (zt + zb) / 2), city_mat(key), bevel=0.003)
    prism(f"City_Chalet_Roof_{k}", [(-w / 2 - 0.02, 0), (w / 2 + 0.02, 0), (0, w * 0.42)], 0.07,
          (bx(CH_D) - 0.03, y, zt), city_mat("snow", CITY_EMIT + 0.2), rot=(0, 0, R(90)), bevel=0.004)
    for j in range(2):
        box(f"City_Chalet_Win_{k}", (0.006, 0.03, 0.035), (bx(CH_D) + 0.002, y - w * 0.22 + j * w * 0.44, zt - 0.06),
            WIN_LIT, bevel=0)
PINE_D = 0.15
for k, (yw, hgt) in enumerate(((0.52, 0.3), (0.68, 0.24), (0.92, 0.34), (1.07, 0.26))):
    cx, cy, zb = bx(PINE_D) - 0.03, wy_(yw, PINE_D), wz_(1.0, PINE_D)
    rod(f"City_Pine_Trunk_{k}", (cx, cy, zb), (cx, cy, zb + 0.05), 0.006, city_mat("wood"))
    for j in range(3):
        rr, zz = 0.055 - j * 0.013, zb + 0.04 + j * hgt * 0.26
        cyl(f"City_Pine_{k}", rr, hgt * 0.42, (cx, cy, zz + hgt * 0.21), city_mat("jungle"), r2=0.0, segs=10, bevel=0)
        cyl(f"City_Pine_Snow_{k}", rr * 0.55, hgt * 0.17, (cx, cy, zz + hgt * 0.36), city_mat("snow", CITY_EMIT + 0.2),
            r2=0.0, segs=10, bevel=0)

# ---- DESERT QUARTER (left of centre): dunes, sandstone mesa towers with beam ends, a wind tower, palms -------
for k, (yw, zw, ry, rz, d) in enumerate(((1.25, 1.32, 0.3, 0.26, 0.5), (1.55, 1.28, 0.24, 0.2, 0.5),
                                         (1.22, 1.0, 0.2, 0.09, 0.14), (1.5, 0.98, 0.24, 0.08, 0.13))):
    ball(f"City_Dune_{k}", 1.0, (bx(d) - 0.02, wy_(yw, d), wz_(zw, d)), city_mat("dune" if k % 2 else "adobe"),
         scale=(0.02, ry, rz), segs=24)
MESA_D = 0.3
for k, (yw, w, top) in enumerate(((1.36, 0.3, 1.5), (1.36, 0.22, 1.7), (1.36, 0.13, 1.88))):
    wtower(f"Mesa_{k}", yw, MESA_D - 0.03 * k, w, top, ("adobe", "dune", "sandstone")[k], depth=0.07)
    d = MESA_D - 0.03 * k
    box(f"City_Mesa_Parapet_{k}", (0.075, w + 0.012, 0.018), (bx(d) - 0.035, wy_(1.36, d), wz_(top, d) + 0.004),
        city_mat("dune", CITY_EMIT + 0.1), bevel=0.006)
    for i in range(3 if k < 2 else 2):              # little square windows and wooden beam ends (vigas)
        yy = wy_(1.36, d) - w * 0.32 + w * 0.64 * i / (2 if k < 2 else 1)
        box(f"City_Mesa_Win_{k}", (0.006, 0.026, 0.03), (bx(d) + 0.002, yy, wz_(top - 0.11, d)),
            WIN_LIT if (i + k) % 2 else WIN_DARK, bevel=0)
        rod(f"City_Mesa_Beam_{k}", (bx(d), yy, wz_(top - 0.04, d)), (bx(d) + 0.025, yy, wz_(top - 0.04, d)), 0.006,
            city_mat("wood"), segs=8)
WT_D, WT_YW = 0.36, 1.17                             # wind tower: a tall slim sandstone tower with vent slots
wtower("WindTower", WT_YW, WT_D, 0.1, 2.2, "adobe", depth=0.08)
box("City_WindTower_Cap", (0.09, 0.12, 0.02), (bx(WT_D) - 0.04, wy_(WT_YW, WT_D), wz_(2.2, WT_D) + 0.01),
    city_mat("dune", CITY_EMIT + 0.1), bevel=0.004)
for i in range(3):
    box("City_WindTower_Slot", (0.006, 0.016, 0.12), (bx(WT_D) + 0.002, wy_(WT_YW, WT_D) - 0.03 + 0.03 * i,
        wz_(2.06, WT_D)), WIN_DARK, bevel=0)
ball("City_Desert_Dome", 0.07, (bx(0.28) - 0.03, wy_(1.58, 0.28), wz_(1.52, 0.28)), city_mat("accent_2"),
     scale=(0.5, 1, 0.9), segs=16)
box("City_Desert_Dome_Drum", (0.07, 0.13, 0.2), (bx(0.28) - 0.035, wy_(1.58, 0.28), wz_(1.42, 0.28)),
    city_mat("adobe"), bevel=0.004)


def mini_palm(name, base, height, seed, lean=0.0):
    """A small date palm: a ringed, gently curved trunk and drooping fronds with leaflets (one leaf mesh)."""
    rnd = random.Random(seed)
    b = Vector(base)
    top = b + Vector((0, lean, height))
    trunk = spline([b, b + Vector((0, lean * 0.2, height * 0.5)), top], 4)
    tube(f"City_{name}_Trunk", trunk, 0.011, city_mat("sandstone"), segs=8, r2=0.007)
    bm_ = bmesh.new()
    for f in range(8):
        az = 2 * math.pi * f / 8 + rnd.uniform(-0.2, 0.2)
        dvec = Vector((math.cos(az) * 0.4, math.sin(az), 0))
        L = height * rnd.uniform(0.45, 0.6)
        pts = [top + dvec * (L * t) + Vector((0, 0, L * (0.35 * t - 0.75 * t * t))) for t in (0, .2, .4, .6, .8, 1.0)]
        for i in range(1, len(pts)):
            tang = (pts[i] - pts[i - 1]).normalized()
            side = tang.cross(Vector((0, 0, 1)))
            side = side.normalized() if side.length > 1e-4 else Vector((1, 0, 0))
            ll = 0.05 * (1 - i / 7)
            for sd in (-1, 1):
                out = (side * sd + Vector((0, 0, -0.7))).normalized()
                bm_.faces.new([bm_.verts.new(pts[i - 1]), bm_.verts.new(pts[i - 1] + out * ll),
                               bm_.verts.new(pts[i] + out * ll * 0.8), bm_.verts.new(pts[i])])
    o = _obj(f"City_{name}_Fronds", bm_)
    o.data.materials.append(city_mat("leaf"))
    COL_ROOM.objects.link(o)
    return o


for k, (yw, hgt, lean) in enumerate(((1.14, 0.42, 0.03), (1.3, 0.52, -0.02), (1.46, 0.4, 0.03), (1.62, 0.48, -0.03))):
    mini_palm(f"Palm_{k}", (bx(0.15) - 0.02, wy_(yw, 0.15), wz_(0.98, 0.15)), hgt, SEED + 50 + k, lean)

# ---- DOWNTOWN (centre): a glass tower carrying the billboard (your hero project), a stepped deco tower -----
BB_D = 0.22
BB_Y, BB_Z = WIN_Y[0] + ww * 2.5 / COLS + BB_D, WIN_Z[0] + wh * 2.5 / ROWS - 0.88 * BB_D
GY, GD = BB_Y, 0.38
tower("Glass", GY, GD, 0.34, 2.8, "tower_glass", depth=0.09)
for k in range(15):
    box("City_Glass_Floor", (0.006, 0.345, 0.008), (bx(GD) + 0.003, GY, 0.75 + k * 0.13), city_mat("stone_light", 0.3),
        bevel=0)
for k in range(1, 4):
    box("City_Glass_Fin", (0.008, 0.008, 2.0), (bx(GD) + 0.004, GY - 0.17 + k * 0.085, 1.8), city_mat("stone_light", 0.3),
        bevel=0)
windows("Glass", GY, GD, 0.3, 0.9, 2.75, 5, 14, size=(0.04, 0.07), lit=0.35)
box("City_Glass_Crown", (0.1, 0.36, 0.03), (bx(GD) - 0.045, GY, 2.8), city_mat("stone_light", CITY_EMIT + 0.1),
    bevel=0.004)
SD, SYW = 0.27, 2.13
SY = wy_(SYW, SD)
for k, (w, ztop) in enumerate(((0.32, 2.2), (0.24, 2.62), (0.15, 2.98))):
    d = SD - 0.02 * k
    z1 = wz_(ztop, d)
    tower(f"Deco_{k}", SY, d, w, z1, "deco", z0=0.4 if k == 0 else z1 - 0.5)
    windows(f"Deco_{k}", SY, d, w * 0.8, z1 - 0.4, z1 - 0.06, 3, 3)
    box(f"City_Deco_Coping_{k}", (0.1, w + 0.02, 0.022), (bx(d) - 0.04, SY, z1 + 0.011),
        city_mat("stone_light", CITY_EMIT + 0.1), bevel=0.004)
    for i in range(4):                                # vertical deco piers between the window columns
        box("City_Deco_Pier", (0.008, 0.012, 0.44), (bx(d) + 0.004, SY - w * 0.4 + w * 0.8 * i / 3, z1 - 0.23),
            city_mat("stone_light", CITY_EMIT + 0.1), bevel=0)
z_sp = wz_(2.98, SD - 0.04)
rod("City_Deco_Spire", (bx(SD - 0.04) - 0.04, SY, z_sp), (bx(SD - 0.04) - 0.04, SY, z_sp + 0.16), 0.007,
    city_mat("stone_light"))
ball("City_Deco_Spire_Light", 0.013, (bx(SD - 0.04) - 0.04, SY, z_sp + 0.17), mat("neon", 0.3, emit=3.0))

# ---- RAINFOREST DOME (right): a misty glass biome dome, giant trees with vines, a tree-planted tower -------
JD, JYW = 0.5, 2.74                                  # vertical-forest tower behind the dome
JY = wy_(JYW, JD)
wtower("Planted", JYW, JD, 0.24, 2.6, "garden", depth=0.05)
wwindows("Planted", JYW, JD, 0.2, 1.8, 2.5, 3, 5, lit=0.5)
for k, zw in enumerate((1.95, 2.2, 2.45)):
    box(f"City_Planted_Balcony_{k}", (0.03, 0.26, 0.014), (bx(JD) + 0.012, JY, wz_(zw, JD)), city_mat("sandstone"),
        bevel=0.003)
foliage("City_Planted_Leaves", [((bx(JD) + 0.02, JY + dy, wz_(zw, JD) + 0.025), 0.04) for zw in (1.95, 2.2, 2.45)
                                for dy in (-0.09, 0.0, 0.09)] + [((bx(JD) - 0.02, JY, wz_(2.62, JD)), 0.08)],
        14, (0.045, 0.02), city_mat("leaf"), seed=SEED + 5, droop=0.1)
DOME_D, DOME_YW, DOME_ZW = 0.3, 2.55, 0.98
DRX, DRY, DRZ = 0.1, 0.32, 0.72
dcx, dcy, dcz = bx(DOME_D) - DRX, wy_(DOME_YW, DOME_D + DRX * 0.4), wz_(DOME_ZW, DOME_D + DRX * 0.4)


def half_dome(name, sx_, sy_, sz_, material, wire=0.0):
    """Upper half of a geodesic sphere (icosphere), scaled in the mesh so a wire frame keeps an even thickness."""
    bm_ = bmesh.new()
    bmesh.ops.create_icosphere(bm_, subdivisions=2, radius=1.0)
    bmesh.ops.delete(bm_, geom=[v for v in bm_.verts if v.co.z < -0.3], context="VERTS")
    for v in bm_.verts:                              # flatten the lowest row onto the base ring
        v.co.z = max(v.co.z, 0.0)
    bmesh.ops.scale(bm_, vec=(sx_, sy_, sz_), verts=bm_.verts)
    o = _obj(name, bm_)
    o.location = (dcx, dcy, dcz)
    o.data.materials.append(material)
    COL_ROOM.objects.link(o)
    if wire:
        mod = o.modifiers.new("Frame", "WIREFRAME")
        mod.thickness = wire
        mod.use_replace = True
    return o


DOME_EMIT = 1.0 if NIGHT else 0.3
# trees growing inside the dome (seen through the glass)
foliage("City_Dome_Canopy", [((dcx + 0.02, dcy + dy, dcz + dz), rr) for dy, dz, rr in
                             ((-0.17, 0.18, 0.09), (0.0, 0.32, 0.12), (0.16, 0.2, 0.1), (0.06, 0.45, 0.08))],
        26, (0.05, 0.03), city_mat("jungle", DOME_EMIT * 0.6), seed=SEED + 61, droop=0.2)
half_dome("City_Dome_Glass", DRX, DRY, DRZ, mat("dome", 0.15, emit=DOME_EMIT, alpha=0.92))
half_dome("City_Dome_Frame", DRX + 0.002, DRY + 0.002, DRZ + 0.002, city_mat("main", CITY_EMIT + 0.3),
          wire=0.012)
cyl("City_Dome_Ring", 1.0, 0.025, (dcx, dcy, dcz + 0.012), city_mat("stone_light", CITY_EMIT + 0.1), segs=40,
    bevel=0).scale = (DRX + 0.01, DRY + 0.01, 1)
# giant rainforest trees either side of the dome, with hanging vines
for k, (yw, top, rr) in enumerate(((2.44, 1.88, 0.16), (2.8, 2.42, 0.19), (2.6, 2.74, 0.15))):
    d = (0.4, 0.44, 0.42)[k]                          # behind the dome, so the dome reads in front
    cx, cy = bx(d) - 0.03, wy_(yw, d)
    zt, zb = wz_(top, d), wz_(1.05, d)
    rod(f"City_Jungle_Trunk_{k}", (cx, cy, zb), (cx, cy, zt - rr * 0.5), 0.02, city_mat("wood"), r2=0.012)
    for sx_ in (-1, 1):
        rod(f"City_Jungle_Bough_{k}", (cx, cy, zt - rr * 0.9), (cx, cy + sx_ * rr * 0.8, zt - rr * 0.2), 0.006,
            city_mat("wood"))
    foliage(f"City_Jungle_Canopy_{k}", [((cx, cy + dy, zt + dz), rr * s) for dy, dz, s in
                                         ((0, 0, 1.0), (-rr * 0.8, -rr * 0.35, 0.7), (rr * 0.8, -rr * 0.3, 0.7))],
            44, (0.065, 0.038), city_mat("jungle" if k != 1 else "leaf"), seed=SEED + 70 + k, droop=0.25)
    for j in range(3):
        vy = cy - rr * 0.6 + j * rr * 0.6
        tube(f"City_Jungle_Vine_{k}", spline([(cx + 0.01, vy, zt - rr * 0.3), (cx + 0.015, vy + 0.01, zt - rr - 0.08),
                                             (cx + 0.01, vy - 0.01, zt - rr - 0.2 - 0.05 * j)], 4), 0.0028,
             city_mat("leaf"), segs=5)
# mist drifting round the dome and the tree tops
MIST = mat("mist", 0.9, emit=0.6 if NIGHT else 1.0, alpha=0.32)
for k, (yw, zw, d, ry, rz) in enumerate(((2.32, 1.08, 0.1, 0.18, 0.05), (2.62, 1.05, 0.09, 0.22, 0.05),
                                         (2.84, 1.16, 0.11, 0.14, 0.05), (2.42, 1.95, 0.16, 0.15, 0.04),
                                         (2.76, 2.12, 0.15, 0.13, 0.035), (2.58, 1.5, 0.12, 0.1, 0.03))):
    ball(f"City_Mist_{k}", 1.0, (bx(d) - 0.01, wy_(yw, d), wz_(zw, d)), MIST, scale=(0.015, ry, rz), segs=20)

# ---- near rooftops: one block per district, with snow, sand, brick and a roof garden -----------------------
NR_D = 0.12
for k, (ya, yb, top, key, cap) in enumerate(((0.4, 1.12, 1.04, "peak", "snow"), (1.12, 1.66, 1.0, "adobe", "dune"),
                                             (1.66, 2.32, 1.08, "brick", "cream"), (2.32, 2.95, 1.02, "garden", "leaf"))):
    y0, y1 = wy_(ya, NR_D), wy_(yb, NR_D)
    zt = wz_(top, NR_D)
    box(f"City_Roof_{k}", (0.1, y1 - y0, zt - 0.3), (bx(NR_D) - 0.05, (y0 + y1) / 2, (zt + 0.3) / 2), city_mat(key),
        bevel=0.003)
    box(f"City_Roof_Coping_{k}", (0.11, y1 - y0, 0.02 if cap != "snow" else 0.03), (bx(NR_D) - 0.05, (y0 + y1) / 2, zt + 0.01),
        city_mat(cap, CITY_EMIT + (0.15 if cap == "snow" else 0.0)), bevel=0.006 if cap == "snow" else 0.003)
    windows(f"Roof_{k}", (y0 + y1) / 2, NR_D, y1 - y0 - 0.1, 0.6, zt - 0.06, max(2, int((y1 - y0) / 0.12)), 1,
            size=(0.04, 0.04), lit=0.5)
TANK_Y = wy_(1.98, 0.2)
for dy in (-0.05, 0.05):
    rod("City_Tank_Leg", (bx(0.2), TANK_Y + dy, wz_(1.08, 0.12)), (bx(0.2), TANK_Y + dy, wz_(1.08, 0.12) + 0.12), 0.004,
        city_mat("dark"))
cyl("City_Tank", 0.075, 0.13, (bx(0.2), TANK_Y, wz_(1.08, 0.12) + 0.185), city_mat("wood"), bevel=0.004)
cyl("City_Tank_Roof", 0.08, 0.05, (bx(0.2), TANK_Y, wz_(1.08, 0.12) + 0.275), city_mat("dark"), r2=0.0, bevel=0)
foliage("City_Roof_Garden", [((bx(0.14), wy_(2.45, 0.14), wz_(1.04, 0.14)), 0.06),
                             ((bx(0.14), wy_(2.75, 0.14), wz_(1.04, 0.14)), 0.05)], 16,
        (0.04, 0.018), city_mat("leaf"), seed=SEED + 6, droop=0.0)
for k in range(10):                                  # a string of rooftop lights
    yy = wy_(0.48, 0.1) + k * 0.27
    ball("City_String_Bulb", 0.008, (bx(0.1) + 0.005, yy, wz_(1.13, 0.1) - 0.025 * math.sin(math.pi * (k % 3) / 2)),
         mat("bulb", 0.3, emit=5.0 if NIGHT else 1.2), segs=8)

# sky: soft clouds by day (and a few snowflakes over the peaks), a moon and stars at night
if NIGHT:
    ball("City_Moon", 0.09, (BOX_X0 + 0.06, wy_(1.3, 0.54), wz_(2.92, 0.54)), mat("cream", 0.3, emit=2.5),
         scale=(0.2, 1, 1))
    for k in range(46):
        yw, zw = crnd.uniform(0.5, 2.85), crnd.uniform(2.45, 3.1)
        ball("City_Star", crnd.uniform(0.003, 0.006), (BOX_X0 + 0.04, wy_(yw, 0.56), wz_(zw, 0.56)),
             mat("cream", 0.3, emit=4.0), segs=6)
else:
    ball("City_Sun", 0.085, (BOX_X0 + 0.07, wy_(1.38, 0.53), wz_(2.72, 0.53)), mat("accent_2", 0.4, emit=2.2),
         scale=(0.15, 1, 1), segs=24)
    ball("City_Sun_Halo", 0.13, (BOX_X0 + 0.065, wy_(1.38, 0.535), wz_(2.72, 0.535)), mat("sky_low", 0.4, emit=1.2),
         scale=(0.1, 1, 1), segs=24)
    for k, (yw, zw) in enumerate(((0.75, 3.0), (1.35, 2.9), (2.0, 3.02), (2.62, 2.86))):
        for j in range(4):
            ball(f"City_Cloud_{k}", 0.06 + 0.02 * (j % 2), (BOX_X0 + 0.05, wy_(yw, 0.55) - 0.1 + j * 0.065,
                 wz_(zw, 0.55) + 0.02 * (j % 2)), mat("cream", 0.6, emit=0.9), scale=(0.15, 1.2, 0.6))
for k in range(34):                                  # gentle snowfall over the snow district only
    yw, zw, d = crnd.uniform(0.52, 1.12), crnd.uniform(1.3, 3.05), crnd.uniform(0.08, 0.3)
    ball("City_Snowflake", crnd.uniform(0.004, 0.007), (bx(d), wy_(yw, d), wz_(zw, d)),
         mat("snow", 0.3, emit=1.5 if NIGHT else 1.0), segs=6)

# THE BILLBOARD: picture hook "screen" 1, centred in a pane as seen from the camera.
BB_W, BB_H = 0.5, 0.32
box("City_Billboard_Frame", (0.025, BB_W + 0.04, BB_H + 0.04), (bx(BB_D) - 0.014, BB_Y, BB_Z), city_mat("dark", 0.1),
    bevel=0.004)
for dy in (-0.15, 0.15):
    box("City_Billboard_Bracket", (GD - BB_D, 0.015, 0.015), (bx((GD + BB_D) / 2), BB_Y + dy, BB_Z - 0.1),
        city_mat("dark", 0.1), bevel=0)
box("City_Billboard_Lamp_Bar", (0.04, BB_W, 0.012), (bx(BB_D) + 0.02, BB_Y, BB_Z + BB_H / 2 + 0.03),
    city_mat("dark", 0.1), bevel=0)
bb = hook_image("screen", 1, (BB_W, BB_H), (bx(BB_D) + 0.001, BB_Y, BB_Z), rot=(0, 0, R(90)), glow=True,
                default_key="accent_2")
bxp = bx(BB_D) + 0.003
hook_default(bb,
             ball("City_Billboard_Sun", 0.07, (bxp, BB_Y - 0.12, BB_Z + 0.02), mat("accent_1", 0.4, emit=1.2),
                  scale=(0.05, 1, 1)),
             box("City_Billboard_Hill", (0.003, BB_W, 0.09), (bxp, BB_Y, BB_Z - BB_H / 2 + 0.045),
                 mat("main", 0.4, emit=1.0), bevel=0),
             label("City_Billboard_Text", "HELLO, CITY!", 0.05, (bxp + 0.001, BB_Y + 0.08, BB_Z + 0.06),
                   mat("cream", 0.4, emit=1.2), rot=(R(90), 0, R(90)), depth=0.001),
             box("City_Billboard_Line", (0.003, 0.18, 0.012), (bxp, BB_Y + 0.08, BB_Z - 0.0),
                 mat("accent_1", 0.4, emit=1.2), bevel=0))

for o in [o for o in COL_ROOM.objects if o.name.startswith("City_")]:
    no_shadow(o)                                     # the sun shines in through the window, past the city


# =====================================================================
#  BACK WALL: three doors for three sizes of resident, coat hooks at three heights
# =====================================================================
# Giraffe-height arched door: sunflower leaf, raised panels, a fanlight, a door knob at 2.2 m.
gcx, gw = sum(GIRAFFE_X) / 2, GIRAFFE_X[1] - GIRAFFE_X[0]
GH = 2.95
SPRING = FLOOR_Z + GH - FLOOR_Z - gw / 2              # where the half-round head starts
tall = prism("Door_Tall_Leaf", arch_pts(gw - 0.02, GH - FLOOR_Z - 0.01, 20, z0=FLOOR_Z), 0.035,
             (gcx, D - 0.0225, 0), PAINT_TALL, bevel=0.004)
hook_link(tall, "linkedin")
band("Door_Tall_Architrave", (gw / 2 + 0.07, gw / 2 + 0.07), (gw / 2, gw / 2), (-0.05, 0.0), TRIM,
     loc=(gcx, D, SPRING), segs=28, bevel=0.004)
for sx in (-1, 1):
    box("Door_Tall_Jamb", (0.07, 0.05, SPRING - FLOOR_Z), (gcx + sx * (gw / 2 + 0.035), D - 0.025, (SPRING + FLOOR_Z) / 2),
        TRIM, bevel=0.004)
    for z0, z1 in ((0.14, 1.0), (1.12, 2.2)):
        box("Door_Tall_Panel", (0.3, 0.012, z1 - z0), (gcx + sx * 0.19, D - 0.046, (z0 + z1) / 2), PAINT_TALL, bevel=0.01)
FAN_R = gw / 2 - 0.09
fan_glass = mat("sky_mid", 0.1, emit=0.35)
prism("Door_Tall_Fanlight", [(FAN_R * math.cos(math.pi * k / 16), SPRING + FAN_R * math.sin(math.pi * k / 16))
                             for k in range(17)], 0.006, (gcx, D - 0.042, 0), fan_glass, bevel=0)
band("Door_Tall_Fan_Frame", (FAN_R + 0.025, FAN_R + 0.025), (FAN_R, FAN_R), (-0.05, -0.04), TRIM, loc=(gcx, D, SPRING),
     segs=20, bevel=0.002)
box("Door_Tall_Fan_Sill", (2 * FAN_R + 0.05, 0.012, 0.025), (gcx, D - 0.046, SPRING - 0.0125), TRIM, bevel=0.003)
for k in range(1, 4):
    a = math.pi * k / 4
    box("Door_Tall_Fan_Bar", (0.012, 0.01, FAN_R), (gcx + FAN_R / 2 * math.cos(a), D - 0.046, SPRING + FAN_R / 2 * math.sin(a)),
        TRIM, bevel=0, rot=(0, -(a - math.pi / 2), 0))
disc("Door_Tall_Rose", 0.03, 0.01, (gcx + 0.32, D - 0.045, 2.2), (0, -1, 0), BRASS)
ball("Door_Tall_Knob", 0.03, (gcx + 0.32, D - 0.085, 2.2), BRASS)
rod("Door_Tall_Knob_Neck", (gcx + 0.32, D - 0.045, 2.2), (gcx + 0.32, D - 0.07, 2.2), 0.01, BRASS)
box("Door_Tall_Kick", (gw - 0.12, 0.004, 0.14), (gcx, D - 0.042, FLOOR_Z + 0.09), BRASS, bevel=0.001)
for z in (0.35, 1.5, 2.55):
    box("Door_Tall_Hinge", (0.02, 0.014, 0.1), (GIRAFFE_X[0] + 0.012, D - 0.046, z), BRASS, bevel=0.002)

# Ordinary door (826 x 2040 mm): four raised panels, lever handle, kick plate.
hcx, hw = sum(DOOR_X) / 2, DOOR_X[1] - DOOR_X[0]
DOOR_TOP = FLOOR_Z + 2.04
human = box("Door_Leaf", (hw, 0.04, 2.04), (hcx, D - 0.024, FLOOR_Z + 1.02), PAINT_DOOR, bevel=0.004)
hook_link(human, "website")
for sx in (-1, 1):
    for z0, z1 in ((0.16, 0.92), (1.08, 1.92)):
        box("Door_Panel", (0.29, 0.012, z1 - z0), (hcx + sx * 0.18, D - 0.048, FLOOR_Z + (z0 + z1) / 2), PAINT_DOOR,
            bevel=0.01)
    box("Door_Architrave", (0.07, 0.05, 2.04 + 0.035), (hcx + sx * (hw / 2 + 0.035), D - 0.025, FLOOR_Z + 1.02 + 0.0175),
        TRIM, bevel=0.004)
box("Door_Architrave_Head", (hw + 0.14, 0.05, 0.07), (hcx, D - 0.025, DOOR_TOP + 0.035), TRIM, bevel=0.004)
disc("Door_Rose", 0.026, 0.01, (hcx + 0.33, D - 0.049, FLOOR_Z + 1.0), (0, -1, 0), BRASS)
rod("Door_Lever_Neck", (hcx + 0.33, D - 0.049, FLOOR_Z + 1.0), (hcx + 0.33, D - 0.1, FLOOR_Z + 1.0), 0.008, BRASS)
rod("Door_Lever", (hcx + 0.33, D - 0.1, FLOOR_Z + 1.0), (hcx + 0.21, D - 0.1, FLOOR_Z + 1.0), 0.009, BRASS)
box("Door_Kick", (hw - 0.06, 0.004, 0.16), (hcx, D - 0.046, FLOOR_Z + 0.09), BRASS, bevel=0.001)
disc("Door_Viewer", 0.009, 0.01, (hcx, D - 0.047, FLOOR_Z + 1.55), (0, -1, 0), BRASS)

# Mouse door in the skirting: a tiny arched lime door with a brass knob, a doormat, a lamp and a flower pot.
mz0 = FLOOR_Z
prism("Door_Mini_Frame", arch_pts(0.21, 0.29, 14, z0=mz0), 0.014, (MOUSE_X, D - 0.007, 0), TRIM, bevel=0.003)
mini = prism("Door_Mini_Leaf", arch_pts(0.165, 0.25, 14, z0=mz0), 0.012, (MOUSE_X, D - 0.016, 0), PAINT_MINI, bevel=0.002)
hook_link(mini, "github")
ball("Door_Mini_Knob", 0.009, (MOUSE_X + 0.05, D - 0.025, mz0 + 0.1), BRASS, segs=10)
for k in range(3):
    box("Door_Mini_Plank_Line", (0.003, 0.003, 0.2), (MOUSE_X - 0.042 + k * 0.042, D - 0.0225, mz0 + 0.1),
        mat("accent_3", 0.5, color="#7EA62E" if not NIGHT else "#8CC22E"), bevel=0)
box("Door_Mini_Mat_Border", (0.19, 0.1, 0.005), (MOUSE_X, D - 0.07, FLOOR_Z + 0.0025), mat("cream", 0.8), bevel=0.001)
box("Door_Mini_Mat", (0.165, 0.078, 0.007), (MOUSE_X, D - 0.07, FLOOR_Z + 0.0035), M("accent_1", 0.9, "knit"), bevel=0.001)
# a tiny striped awning over the mouse door (a 1:12 shop awning on two iron arms)
for i in range(6):
    box("Door_Mini_Awning", (0.04, 0.07, 0.006), (MOUSE_X - 0.1 + 0.04 * i, D - 0.045, mz0 + 0.318), 
        mat("cream" if i % 2 else "red_string", 0.6), bevel=0.001, rot=(R(-24), 0, 0))
    ball("Door_Mini_Awning_Scallop", 0.02, (MOUSE_X - 0.1 + 0.04 * i, D - 0.078, mz0 + 0.3),
         mat("cream" if i % 2 else "red_string", 0.6), scale=(1, 0.15, 0.6), segs=10)
rod("Door_Mini_Lamp_Arm", (MOUSE_X + 0.115, D - 0.003, mz0 + 0.22), (MOUSE_X + 0.115, D - 0.035, mz0 + 0.235), 0.003, IRON)
ball("Door_Mini_Lamp", 0.015, (MOUSE_X + 0.115, D - 0.038, mz0 + 0.22), mat("bulb", 0.3, emit=4.0), segs=10)
lathe("Door_Mini_Pot", [(0, 0), (0.012, 0), (0.016, 0.025), (0, 0.025)], (MOUSE_X + 0.12, D - 0.09, FLOOR_Z), TERRA,
      segs=12)
ball("Door_Mini_Flower", 0.012, (MOUSE_X + 0.12, D - 0.09, FLOOR_Z + 0.04), mat("accent_1", 0.5), segs=10)

# Coat hooks at three heights (small, standard, tall) on an oak board, with what each resident hangs there.
HB_W, HB_Z = 0.24, (0.3, 2.78)
box("Hooks_Board", (HB_W, 0.022, HB_Z[1] - HB_Z[0]), (HOOKS_X, D - 0.011, sum(HB_Z) / 2), OAK_V, bevel=0.004)
for k, (z, r, ln) in enumerate(((0.46, 0.006, 0.045), (1.62, 0.01, 0.08), (2.62, 0.014, 0.11))):
    rod(f"Hook_{k}", (HOOKS_X, D - 0.022, z), (HOOKS_X, D - 0.022 - ln, z + ln * 0.3), r, BRASS)
    ball(f"Hook_{k}_Tip", r * 1.6, (HOOKS_X, D - 0.022 - ln, z + ln * 0.3), BRASS, segs=12)
    disc(f"Hook_{k}_Plaque", 0.018 + 0.01 * k, 0.004, (HOOKS_X + 0.08, D - 0.024, z + 0.05), (0, -1, 0),
         mat("cream", 0.3))
    pr = 0.004 + 0.002 * k                           # a paw print on each plaque, sized to the hook
    ball(f"Hook_{k}_Paw", pr * 1.6, (HOOKS_X + 0.08, D - 0.027, z + 0.045), INK, scale=(1, 0.3, 0.85), segs=10)
    for t in (-1, 0, 1):
        ball(f"Hook_{k}_Toe", pr * 0.7, (HOOKS_X + 0.08 + t * pr * 1.4, D - 0.027, z + 0.045 + pr * 2.2 - abs(t) * pr * 0.5),
             INK, scale=(1, 0.3, 1), segs=8)
# tiny knitted scarf on the small hook
for k, dx in enumerate((-0.012, 0.012)):
    box("Hook_Scarf_Small", (0.02, 0.008, 0.11 - 0.02 * k), (HOOKS_X + dx, D - 0.06, 0.46 - 0.05 + 0.01 * k),
        M("accent_1", 0.95, "knit"), bevel=0.003)
# canvas tote on the standard hook
puffy("Hook_Tote", 0.28, 0.32, 0.06, (HOOKS_X, D - 0.075, 1.36), M("cream", 0.86, "fabric"), rot=(R(90), 0, 0))
for sx in (-1, 1):
    tube("Hook_Tote_Handle", spline([(HOOKS_X + sx * 0.08, D - 0.075, 1.51), (HOOKS_X + sx * 0.04, D - 0.08, 1.6),
                                    (HOOKS_X, D - 0.1, 1.645)], 4), 0.006, M("main", 0.87, "fabric"), segs=6)
box("Hook_Tote_Patch", (0.12, 0.004, 0.1), (HOOKS_X, D - 0.108, 1.36), M("accent_2", 0.86, "fabric"), bevel=0.003)
# a very long striped scarf on the tall hook
for k, (dx, bottom) in enumerate(((-0.05, 1.55), (0.05, 1.72))):
    n = int((2.6 - bottom) / 0.08)
    for i in range(n):
        box("Hook_Scarf_Long", (0.085, 0.014, 0.08), (HOOKS_X + dx * (1 - i / n * 0.3), D - 0.09 + 0.02 * (i / n),
            2.6 - 0.04 - i * 0.08), M("main", 0.95, "knit") if i % 2 == 0 else M("accent_2", 0.96, "knit"), bevel=0.004)
    for f in range(5):
        box("Hook_Scarf_Fringe", (0.006, 0.006, 0.04), (HOOKS_X + dx * 0.7 - 0.034 + f * 0.017, D - 0.071, bottom - 0.02),
            M("accent_2", 0.96, "knit"), bevel=0)

# Coir doormat in front of the door, with paw prints of three sizes.
mat_c = (hcx, D - 0.32)
box("Doormat", (0.6, 0.4, 0.017), (mat_c[0], mat_c[1], FLOOR_Z + 0.0085), COIR, bevel=0.003)
PAW = mat("coir", 0.9, color="#5A3F26")
for k, (dx, dy, s) in enumerate(((-0.17, -0.06, 1.6), (0.02, 0.07, 1.0), (0.18, -0.08, 0.55))):
    px, py = mat_c[0] + dx, mat_c[1] + dy
    ball("Doormat_Paw_Pad", 0.022 * s, (px, py, FLOOR_Z + 0.0175), PAW, scale=(1.1, 0.9, 0.05), segs=12)
    for t in (-1.5, -0.5, 0.5, 1.5):
        ball("Doormat_Paw_Toe", 0.009 * s, (px + t * 0.016 * s, py + (0.032 - abs(t) * 0.006) * s, FLOOR_Z + 0.0175),
             PAW, scale=(1, 1.2, 0.05), segs=10)


def paw(name, cx, y, cz, s, material, plane="XZ"):
    """A paw print (pad + four toes) of size s, flat on the back wall (XZ) or on the floor (XY)."""
    def P(u, v):
        return (cx + u, y, cz + v) if plane == "XZ" else (cx + u, y + v, cz)
    sc = (1.1, 0.12, 0.9) if plane == "XZ" else (1.1, 0.9, 0.12)
    parts = [ball(f"{name}_Pad", s, P(0, 0), material, scale=sc, segs=12)]
    for t in (-1.5, -0.5, 0.5, 1.5):
        parts.append(ball(f"{name}_Toe", s * 0.42, P(t * s * 0.72, s * (1.45 - abs(t) * 0.28)), material,
                          scale=(sc[0] * 0.9, sc[1], sc[2] * 1.3) if plane == "XZ" else (1, 1.2, 0.12), segs=10))
    return parts


# "ALL SIZES WELCOME": a painted timber fascia sign over the doors, with paw prints in three sizes.
WS_X, WS_Z, WS_W, WS_H = 2.2, 3.14, 1.56, 0.19
box("Welcome_Sign_Board", (WS_W, 0.025, WS_H), (WS_X, D - 0.0125, WS_Z), M("cream", 0.6, "wood"), bevel=0.005)
for sz in (-1, 1):
    box("Welcome_Sign_Rail", (WS_W, 0.008, 0.018), (WS_X, D - 0.028, WS_Z + sz * (WS_H / 2 - 0.016)), PAINT_TEAL,
        bevel=0.002)
for sx in (-1, 1):
    box("Welcome_Sign_Stile", (0.018, 0.008, WS_H - 0.014), (WS_X + sx * (WS_W / 2 - 0.016), D - 0.028, WS_Z), PAINT_TEAL,
        bevel=0.002)
label("Welcome_Sign_Text", "ALL SIZES WELCOME", 0.098, (WS_X, D - 0.03, WS_Z - 0.006), mat("accent_1", 0.45),
      depth=0.006)
for k, (sx, s) in enumerate(((-1, 0.011), (-1, 0.02), (1, 0.03))):
    px = WS_X + sx * (WS_W / 2 - 0.06) + (0.045 if k == 1 else 0) * 0 + (-0.0 if k else 0)
    if k == 0:
        px = WS_X - WS_W / 2 + 0.045
    elif k == 1:
        px = WS_X - WS_W / 2 + 0.09
    paw(f"Welcome_Paw_{k}", px, D - 0.029, WS_Z - 0.02 + (0.012 if k == 0 else 0), s, mat("main", 0.5))
for sx in (-1, 1):                                    # two iron hanging brackets
    box("Welcome_Sign_Bracket", (0.02, 0.05, 0.012), (WS_X + sx * 0.6, D - 0.025, WS_Z + WS_H / 2 + 0.006), IRON,
        bevel=0.002)

# Height chart on the tall door's frame: a painted ruler on the jamb, pencil lines, and a paw-print tag at each
# resident's height, the tags growing with the paw size (small to giraffe-tall).
RJ_X = GIRAFFE_X[1] + 0.035                          # centre of the tall door's right-hand jamb
box("HeightChart_Ruler", (0.042, 0.004, SPRING - 0.2), (RJ_X, D - 0.052, 0.1 + (SPRING - 0.2) / 2),
    mat("cream", 0.5), bevel=0.001)
for k in range(int((SPRING - 0.25) / 0.05)):
    z = 0.15 + k * 0.05
    big = k % 2 == 1
    box("HeightChart_Tick", (0.03 if big else 0.016, 0.002, 0.004), (RJ_X - 0.021 + (0.015 if big else 0.008), D - 0.0545, z),
        INK, bevel=0)
for k, (z, s, key) in enumerate(((0.42, 0.012, "accent_3"), (0.95, 0.016, "accent_1"), (1.55, 0.02, "main"),
                                 (2.12, 0.024, "accent_2"), (2.78, 0.028, "terracotta"))):
    if z < SPRING:
        box("HeightChart_Pencil", (0.05, 0.002, 0.003), (RJ_X, D - 0.0548, z), mat("ink", 0.7, color="#555560"), bevel=0)
    tx = GIRAFFE_X[1] + 0.07 + 0.075 if z < SPRING + 0.2 else GIRAFFE_X[1] + 0.09
    box("HeightChart_Tag", (0.13, 0.006, 0.075 + s), (tx, D - 0.003, z), mat(key, 0.55), bevel=0.003)
    paw(f"HeightChart_Paw_{k}", tx, D - 0.0068, z - s * 0.4, s, mat("cream", 0.5))

# Mouse door extras: a tiny post mailbox with a red flag and a little house number.
paw("Door_Mini_Mat_Paw", MOUSE_X, D - 0.075, FLOOR_Z + 0.0075, 0.011, mat("cream", 0.8), plane="XY")
mb = empty("Mouse_Mailbox", (MOUSE_X - 0.125, D - 0.11, FLOOR_Z))
rod("Mailbox_Post", (0, 0, 0), (0, 0, 0.1), 0.004, OAK_V, parent=mb)
box("Mailbox_Box", (0.032, 0.05, 0.022), (0, 0, 0.11), PAINT_TEAL, bevel=0.002, parent=mb)
cyl("Mailbox_Lid", 0.016, 0.05, (0, 0, 0.121), PAINT_TEAL, rot=(R(90), 0, 0), segs=16, bevel=0.002, parent=mb)
box("Mailbox_Flag", (0.003, 0.006, 0.03), (0.018, 0.012, 0.13), mat("red_string", 0.5), bevel=0, parent=mb)
box("Mailbox_Flag_Tip", (0.003, 0.016, 0.01), (0.018, 0.02, 0.142), mat("red_string", 0.5), bevel=0, parent=mb)
box("Mailbox_Letter", (0.022, 0.004, 0.014), (0, -0.026, 0.115), PAPER, bevel=0, rot=(0, R(8), 0), parent=mb)
disc("Door_Mini_Number_Plate", 0.014, 0.004, (MOUSE_X - 0.05, D - 0.025, FLOOR_Z + 0.2), (0, -1, 0), BRASS)
label("Door_Mini_Number", "1/2", 0.012, (MOUSE_X - 0.05, D - 0.0275, FLOOR_Z + 0.2), INK, depth=0.0005)

# Hat shelf on top of the hook board at 2.86 m, with a giant wide-brim straw sun hat for the tallest resident,
# and a tiny knitted bobble hat on the small hook.
box("Hooks_Hat_Shelf", (0.34, 0.18, 0.02), (HOOKS_X, D - 0.09, 2.86), OAK, bevel=0.004)
for sx in (-1, 1):
    prism("Hooks_Hat_Shelf_Bracket", [(0.0, 0.0), (0.0, -0.11), (0.14, 0.0)], 0.016, (HOOKS_X + sx * 0.12, D - 0.005, 2.85),
          OAK_V, rot=(0, 0, R(-90)), bevel=0.002)
hat = empty("Giant_Sun_Hat", (HOOKS_X, D - 0.1, 2.873), rot=(R(-8), 0, R(10)))
STRAW = M("sand", 0.85, "fabric")
lathe("Hat_Brim", [(0.07, 0.0), (0.24, -0.012), (0.25, -0.006), (0.075, 0.012)], (0, 0, 0), STRAW, segs=40, parent=hat)
lathe("Hat_Crown", [(0, 0.12), (0.075, 0.11), (0.09, 0.06), (0.095, 0.0), (0.0, 0.0)], (0, 0, 0), STRAW, segs=32, parent=hat)
torus("Hat_Band", 0.093, 0.012, (0, 0, 0.025), M("accent_1", 0.8, "fabric"), parent=hat, seg=32, tseg=8)
ball("Hat_Flower", 0.02, (0.07, -0.06, 0.03), mat("accent_2", 0.6), scale=(1, 1, 0.6), parent=hat)
lathe("Tiny_Bobble_Hat", [(0, 0.035), (0.016, 0.03), (0.022, 0.012), (0.022, 0.0), (0, 0)],
      (HOOKS_X, D - 0.06, 0.46 + 0.02), M("main", 0.95, "knit"), segs=16)
ball("Tiny_Bobble", 0.009, (HOOKS_X, D - 0.06, 0.46 + 0.058), M("cream", 0.95, "knit"), segs=10)

# Patrol-training certificate in a gilt frame (A3), with a floating oak shelf below holding a gold star badge
# on a little stand and a 1:24 toy patrol car. Generic: no department name, crest or logo.
CF_X, CF_Z, CF_W, CF_H = 0.48, 2.48, 0.46, 0.34
GILT = M("badge", 0.3, "brushed", metal=1.0)
for sz in (-1, 1):
    box("Certificate_Frame_H", (CF_W + 0.06, 0.03, 0.03), (CF_X, D - 0.015, CF_Z + sz * (CF_H / 2 + 0.015)), GILT,
        bevel=0.004)
for sx in (-1, 1):
    box("Certificate_Frame_V", (0.03, 0.03, CF_H + 0.06), (CF_X + sx * (CF_W / 2 + 0.015), D - 0.015, CF_Z), GILT,
        bevel=0.004)
box("Certificate_Paper", (CF_W, 0.006, CF_H), (CF_X, D - 0.01, CF_Z), M("cream", 0.85, "paper"), bevel=0)
box("Certificate_Border", (CF_W - 0.04, 0.001, CF_H - 0.04), (CF_X, D - 0.0135, CF_Z), mat("main", 0.6), bevel=0)
box("Certificate_Field", (CF_W - 0.052, 0.001, CF_H - 0.052), (CF_X, D - 0.0142, CF_Z), M("cream", 0.85, "paper"),
    bevel=0)
CY = D - 0.0152
label("Certificate_Title", "CERTIFICATE", 0.045, (CF_X, CY, CF_Z + 0.105), INK, depth=0.0006)
label("Certificate_Sub", "PATROL TRAINING  -  WITH HONOURS", 0.013, (CF_X, CY, CF_Z + 0.06), INK, depth=0.0005)
for j, wdt in enumerate((0.3, 0.24, 0.27)):
    box("Certificate_Line", (wdt, 0.001, 0.005), (CF_X, CY, CF_Z + 0.02 - j * 0.03), mat("ink", 0.8, color="#8A8A92"),
        bevel=0)
for sx in (-1, 1):
    box("Certificate_Signature_Rule", (0.1, 0.001, 0.002), (CF_X + sx * 0.12, CY, CF_Z - 0.11), INK, bevel=0)
    tube("Certificate_Signature", [(CF_X + sx * 0.12 - 0.04 + 0.016 * i, CY - 0.0005, CF_Z - 0.095 + 0.008 * math.sin(i * 1.7))
                                   for i in range(6)], 0.0012, INK, segs=4)
disc("Certificate_Seal", 0.032, 0.004, (CF_X, CY - 0.002, CF_Z - 0.1), (0, -1, 0), GILT)
for sx in (-1, 1):
    box("Certificate_Ribbon", (0.016, 0.002, 0.06), (CF_X + sx * 0.014, CY + 0.0005, CF_Z - 0.14), mat("red_string", 0.6),
        bevel=0, rot=(0, R(sx * 14), 0))


def star_pts(r_out, r_in, n=5, rot=90):
    return [((r_out if i % 2 == 0 else r_in) * math.cos(R(rot + 180 * i / n)),
             (r_out if i % 2 == 0 else r_in) * math.sin(R(rot + 180 * i / n))) for i in range(2 * n)]


SH_Z = 2.06
box("Badge_Shelf", (0.6, 0.14, 0.02), (CF_X, D - 0.07, SH_Z), OAK, bevel=0.004)
box("Badge_Shelf_Cleat", (0.56, 0.016, 0.04), (CF_X, D - 0.008, SH_Z - 0.02), OAK, bevel=0.002)
BADGE = M("badge", 0.22, "brushed", metal=1.0)
bst = empty("Star_Badge", (CF_X - 0.15, D - 0.075, SH_Z + 0.01), rot=(0, 0, R(-25)))
box("Badge_Stand_Base", (0.2, 0.08, 0.014), (0, 0, 0.007), OAK, bevel=0.003, parent=bst)
box("Badge_Stand_Back", (0.19, 0.01, 0.2), (0, 0.022, 0.11), M("main", 0.9, "fabric"), bevel=0.004,
    rot=(R(-12), 0, 0), parent=bst)
star = prism("Badge_Star", star_pts(0.08, 0.035), 0.012, (0, 0.006, 0.11), BADGE, rot=(R(-12), 0, 0), bevel=0.0015,
             parent=bst)
for i in range(5):
    a = R(90 + 72 * i)
    ball("Badge_Star_Tip", 0.01, (0.082 * math.cos(a), 0.0 - 0.082 * math.sin(a) * math.sin(R(12)), 0.11 + 0.082 * math.sin(a) * 0.98),
         BADGE, segs=10, parent=bst)
disc("Badge_Star_Boss", 0.026, 0.007, (0, -0.004, 0.11), (0, -1, 0.21), M("cream", 0.3, "brushed", metal=0.8), parent=bst)
# toy patrol car (1:24 die-cast type): two-tone body, cabin glass, light bar, wheels, a star on the door
car = empty("Toy_Patrol_Car", (CF_X + 0.11, D - 0.07, SH_Z + 0.01), rot=(0, 0, R(-12)))
CAR_A, CAR_B = M("cream", 0.25, "ceramic"), M("main", 0.25, "ceramic")
box("Car_Body", (0.2, 0.082, 0.04), (0, 0, 0.032), CAR_B, bevel=0.012, parent=car)
box("Car_Doors", (0.09, 0.084, 0.026), (0.005, 0, 0.036), CAR_A, bevel=0.006, parent=car)
box("Car_Cabin", (0.1, 0.072, 0.034), (-0.005, 0, 0.068), CAR_A, bevel=0.012, parent=car)
for sy in (-1, 1):
    box("Car_Side_Glass", (0.08, 0.002, 0.018), (-0.005, sy * 0.0365, 0.07), mat("ink", 0.1), bevel=0.002, parent=car)
    for sx in (-1, 1):
        cyl("Car_Wheel", 0.017, 0.014, (sx * 0.062, sy * 0.038, 0.017), RUBBER, rot=(R(90), 0, 0), segs=16, parent=car)
        cyl("Car_Hubcap", 0.008, 0.016, (sx * 0.062, sy * 0.038, 0.017), CHROME, rot=(R(90), 0, 0), segs=12, parent=car)
for sx in (-1, 1):
    box("Car_Screen", (0.002, 0.06, 0.022), (sx * 0.048, 0, 0.068), mat("ink", 0.1), bevel=0.002,
        rot=(0, R(sx * 22), 0), parent=car)
box("Car_Lightbar_Base", (0.026, 0.06, 0.008), (-0.005, 0, 0.088), mat("dark", 0.4), bevel=0.002, parent=car)
for sy, key in ((-1, "red_string"), (1, "siren")):
    box("Car_Light", (0.022, 0.026, 0.012), (-0.005, sy * 0.015, 0.097), mat(key, 0.3, emit=1.2), bevel=0.003,
        parent=car)
prism("Car_Door_Star", star_pts(0.011, 0.005), 0.002, (0.005, -0.043, 0.037), BADGE, bevel=0, parent=car)
for sx in (-1, 1):
    box("Car_Headlight", (0.002, 0.016, 0.008), (sx * 0.1, 0, 0.036), mat("bulb" if sx > 0 else "red_string", 0.3, emit=0.8),
        bevel=0, rot=(0, 0, R(90)), parent=car)


# =====================================================================
#  SHARED PIECES: the plush residents (simple rounded toys, not characters)
# =====================================================================
def eyes(prefix, parent, pts, r=0.008):
    for p in pts:
        ball(f"{prefix}_Eye", r, p, BEAD, parent=parent, segs=12)


def otter_plush(root, z=0.0):
    """Sitting otter plush (~34 cm): long brown body, cream face and belly, holding a pebble."""
    ball("Otter_Body", 0.1, (0, 0, z + 0.12), OTTER, scale=(0.85, 0.75, 1.3), parent=root)
    ball("Otter_Belly", 0.075, (0, -0.045, z + 0.12), FLUFF, scale=(0.8, 0.45, 1.15), parent=root)
    ball("Otter_Head", 0.07, (0, -0.01, z + 0.29), OTTER, scale=(1.1, 1, 0.95), parent=root)
    ball("Otter_Muzzle", 0.042, (0, -0.055, z + 0.272), FLUFF, scale=(1.3, 0.8, 0.8), parent=root)
    ball("Otter_Nose", 0.012, (0, -0.09, z + 0.288), BEAD, scale=(1.3, 1, 0.8), parent=root)
    eyes("Otter", root, [(sx * 0.03, -0.062, z + 0.31) for sx in (-1, 1)], r=0.009)
    for sx in (-1, 1):
        ball("Otter_Ear", 0.017, (sx * 0.06, 0.0, z + 0.338), OTTER, scale=(1, 0.6, 1), parent=root)
        ball("Otter_Arm", 0.026, (sx * 0.035, -0.08, z + 0.17), OTTER, scale=(0.8, 1.2, 0.8), parent=root)
        ball("Otter_Foot", 0.03, (sx * 0.05, -0.065, z + 0.02), OTTER, scale=(1, 1.5, 0.55), parent=root)
    ball("Otter_Pebble", 0.022, (0, -0.1, z + 0.175), mat("deco", 0.3), scale=(1.2, 0.8, 0.9), parent=root)
    rod("Otter_Tail", (0, 0.06, z + 0.05), (0.04, 0.2, z + 0.02), 0.035, OTTER, r2=0.012, parent=root)


def raccoon_plush(root, z=0.0):
    """Raccoon plush (~32 cm): grey, dark eye band, white muzzle, ringed tail curled round to the front."""
    ball("Raccoon_Body", 0.1, (0, 0, z + 0.11), RACCOON, scale=(0.95, 0.85, 1.12), parent=root)
    ball("Raccoon_Belly", 0.07, (0, -0.05, z + 0.11), FLUFF, scale=(0.8, 0.45, 1.0), parent=root)
    ball("Raccoon_Head", 0.075, (0, -0.01, z + 0.27), RACCOON, scale=(1.15, 1, 0.92), parent=root)
    ball("Raccoon_Mask", 0.072, (0, -0.03, z + 0.282), MASK, scale=(1.12, 0.62, 0.36), parent=root)
    ball("Raccoon_Muzzle", 0.036, (0, -0.07, z + 0.255), FLUFF, scale=(1.2, 0.9, 0.8), parent=root)
    ball("Raccoon_Nose", 0.011, (0, -0.104, z + 0.265), BEAD, parent=root)
    eyes("Raccoon", root, [(sx * 0.03, -0.075, z + 0.29) for sx in (-1, 1)], r=0.0085)
    for sx in (-1, 1):
        cyl("Raccoon_Ear", 0.024, 0.045, (sx * 0.055, 0.0, z + 0.345), RACCOON, r2=0.004, segs=12, bevel=0,
            rot=(0, R(sx * 18), 0), parent=root)
        ball("Raccoon_Foot", 0.03, (sx * 0.05, -0.07, z + 0.02), MASK, scale=(1, 1.4, 0.55), parent=root)
        ball("Raccoon_Paw", 0.024, (sx * 0.05, -0.085, z + 0.13), MASK, scale=(0.8, 1, 0.8), parent=root)
    path = spline([(0.06, 0.07, z + 0.04), (0.14, 0.02, z + 0.04), (0.15, -0.08, z + 0.05), (0.1, -0.14, z + 0.06)], 3)
    for k in range(len(path) - 1):
        rod("Raccoon_Tail", path[k], path[k + 1], 0.034 - 0.002 * k, RACCOON if k % 2 == 0 else MASK, parent=root)
    ball("Raccoon_Tail_Tip", 0.022, path[-1], MASK, parent=root)


def meerkat_plush(root, z=0.0):
    """Meerkat plush standing up (~30 cm): slim sandy body, dark eye patches, paws together."""
    ball("Meerkat_Body", 0.06, (0, 0, z + 0.13), MEERKAT, scale=(0.85, 0.8, 1.9), parent=root)
    ball("Meerkat_Belly", 0.045, (0, -0.025, z + 0.13), FLUFF, scale=(0.8, 0.5, 1.8), parent=root)
    ball("Meerkat_Head", 0.045, (0, -0.005, z + 0.29), MEERKAT, scale=(0.95, 1.1, 0.9), parent=root)
    rod("Meerkat_Snout", (0, -0.03, z + 0.285), (0, -0.075, z + 0.275), 0.022, MEERKAT, r2=0.01, parent=root)
    ball("Meerkat_Nose", 0.008, (0, -0.077, z + 0.276), BEAD, parent=root)
    for sx in (-1, 1):
        ball("Meerkat_Patch", 0.017, (sx * 0.022, -0.036, z + 0.305), MASK, scale=(0.8, 0.5, 1.1), parent=root)
        ball("Meerkat_Ear", 0.01, (sx * 0.042, 0.005, z + 0.31), MASK, scale=(0.6, 1, 1), parent=root)
        ball("Meerkat_Foot", 0.022, (sx * 0.03, -0.03, z + 0.012), MEERKAT, scale=(1, 1.4, 0.5), parent=root)
        rod("Meerkat_Arm", (sx * 0.035, -0.03, z + 0.215), (sx * 0.012, -0.06, z + 0.17), 0.012, MEERKAT, parent=root)
    eyes("Meerkat", root, [(sx * 0.022, -0.045, z + 0.305) for sx in (-1, 1)], r=0.0065)
    rod("Meerkat_Tail", (0, 0.04, z + 0.06), (0, 0.11, z + 0.006), 0.012, MEERKAT, r2=0.005, parent=root)


def tortoise_plush(root, z=0.0):
    """Tortoise plush (~40 cm long): a quilted dome shell, a round head and four stubby legs."""
    ball("Tortoise_Shell", 0.15, (0, 0.01, z + 0.07), SHELL, scale=(0.85, 1.0, 0.62), parent=root)
    torus("Tortoise_Rim", 0.13, 0.016, (0, 0.01, z + 0.06), FLUFF, parent=root, rot=(0, 0, 0))
    rnd = random.Random(SEED + 21)
    plate = M("leaf", 0.96, "knit")
    for k, (a, rr) in enumerate([(0, 0)] + [(2 * math.pi * i / 6, 0.075) for i in range(6)]):
        px, py = rr * math.cos(a) * 0.85, 0.01 + rr * math.sin(a)
        pz = z + 0.07 + 0.093 * math.sqrt(max(0.0, 1 - (px / 0.1275) ** 2 - ((py - 0.01) / 0.15) ** 2)) - 0.004
        ball("Tortoise_Plate", 0.034 + rnd.uniform(-0.003, 0.003), (px, py, pz), plate, scale=(1, 1, 0.3), parent=root)
    ball("Tortoise_Head", 0.05, (0, -0.16, z + 0.085), SKIN, scale=(0.95, 1.05, 0.9), parent=root)
    eyes("Tortoise", root, [(sx * 0.025, -0.2, z + 0.1) for sx in (-1, 1)], r=0.007)
    for sx in (-1, 1):
        for sy in (-1, 1):
            ball("Tortoise_Leg", 0.036, (sx * 0.095, sy * 0.085, z + 0.028), SKIN, scale=(1, 1.1, 0.7), parent=root)
    ball("Tortoise_Tail", 0.015, (0, 0.165, z + 0.04), SKIN, parent=root)


def capsule(name, loc, rot, length, cap_mat, parent=None, r=0.048):
    """Pneumatic-tube carrier: clear body, a rolled letter inside, felt wear bands and coloured end caps."""
    g = empty(name, loc, rot=rot, parent=parent)
    cyl(f"{name}_Body", r * 0.92, length - 0.06, (0, 0, 0), CAPSULE, segs=24, bevel=0, parent=g)
    cyl(f"{name}_Letter", r * 0.6, length - 0.1, (0, 0, 0), PAPER, segs=16, bevel=0.002, parent=g)
    for sz in (-1, 1):
        cyl(f"{name}_Cap", r, 0.04, (0, 0, sz * (length / 2 - 0.02)), cap_mat, segs=24, bevel=0.01, parent=g)
        cyl(f"{name}_Band", r * 1.02, 0.018, (0, 0, sz * (length / 2 - 0.07)), M("dark", 0.95, "fabric"), segs=24,
            bevel=0.004, parent=g)
    return g


# =====================================================================
#  FURNITURE SLOTS  (same names in every template)
#  size = (width, depth, height); front of the furniture faces local -Y
# =====================================================================
slot("desk",       (1.2, 0.6, 0.75), (0.31, 3.4), turn=90, shape="table")
slot("lamp",       (0.26, 0.2, 0.38), (0.19, 3.82), z=FLOOR_Z + 0.75, turn=90, kind="surface", shape="lamp")
slot("chair",      (0.56, 0.58, 0.92), (1.0, 3.2), turn=-65, shape="chair")
slot("floor_lamp", (0.38, 0.38, 2.8), (0.26, 4.2), turn=0, shape="lamp")   # giraffe-height lamp in the desk corner
slot("armchair",   (0.8, 0.78, 0.76), (2.55, 2.55), turn=35, shape="chair")
slot("rug",        (2.0, 2.0, 0.015), (2.55, 2.0), kind="rug", shape="rug")
slot("pet",        (0.3, 0.42, 0.2), (3.25, 1.45), turn=30, shape="pet")
slot("bed",        (1.06, 2.1, 1.75), (4.45, 3.33), shape="bed")
slot("plant",      (0.7, 0.7, 1.85), (0.42, 0.42), shape="plant")
slot("wall_shelf", (0.9, 0.17, 0.34), (0.085, sum(CAFE_Y) / 2), turn=90, kind="wall", shape="shelf")


# =====================================================================
#  LIGHTS helper (lamps carry their own bulbs)
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
    o.parent = parent
    return o


LAMP_K = kelvin(LAMP_WARMTH)
NIGHT_LAMPS = 1.8 if NIGHT else 1.0                  # lamps matter more at night


# =====================================================================
#  PLACEHOLDER FURNITURE  (replaced when you add your own with add_furniture.py)
# =====================================================================
def build_desk():
    """Oak writing desk: 25 mm top, a three-drawer pedestal on a plinth, tapered legs, a pencil drawer."""
    root, w, d, h = furniture_root("desk")
    box("Desk_Top", (w, d, 0.025), (0, 0, h - 0.0125), OAK, bevel=0.004, parent=root)
    px0, px1 = 0.18, w / 2 - 0.02                    # drawer pedestal (the end near the back wall)
    pcx, pw_ = (px0 + px1) / 2, px1 - px0
    for x in (px0 + 0.009, px1 - 0.009):
        box("Desk_Pedestal_Side", (0.018, d - 0.04, h - 0.085), (x, 0.0, 0.06 + (h - 0.085) / 2), OAK_V, bevel=0.002,
            parent=root)
    box("Desk_Pedestal_Back", (pw_, 0.012, h - 0.085), (pcx, d / 2 - 0.026, 0.06 + (h - 0.085) / 2), OAK, bevel=0.001,
        parent=root)
    box("Desk_Plinth", (pw_ - 0.03, d - 0.1, 0.06), (pcx, 0.02, 0.03), mat("dark", 0.7), bevel=0.002, parent=root)
    z = h - 0.025 - 0.003
    for k, dh in enumerate((0.16, 0.2, 0.25)):
        box("Desk_Drawer", (pw_ - 0.004, 0.02, dh - 0.003), (pcx, -d / 2 + 0.03, z - dh / 2), OAK, bevel=0.003,
            parent=root)
        rod("Desk_Drawer_Pull", (pcx - 0.045, -d / 2 + 0.008, z - dh / 2 + dh * 0.2),
            (pcx + 0.045, -d / 2 + 0.008, z - dh / 2 + dh * 0.2), 0.006, BRASS, parent=root)
        for sx in (-1, 1):
            rod("Desk_Pull_Post", (pcx + sx * 0.04, -d / 2 + 0.02, z - dh / 2 + dh * 0.2),
                (pcx + sx * 0.04, -d / 2 + 0.006, z - dh / 2 + dh * 0.2), 0.004, BRASS, parent=root)
        z -= dh
    lx = -w / 2 + 0.035                              # tapered legs at the open end
    for sy in (-1, 1):
        cyl("Desk_Leg", 0.022, h - 0.025, (lx, sy * (d / 2 - 0.035), (h - 0.025) / 2), OAK_V, r2=0.016, bevel=0.002,
            rot=(R(180), 0, 0), parent=root)
    box("Desk_Rail_Side", (0.022, d - 0.1, 0.09), (lx, 0, h - 0.07), OAK, bevel=0.002, parent=root)
    box("Desk_Rail_Back", (px0 - lx, 0.022, 0.09), ((px0 + lx) / 2, d / 2 - 0.035, h - 0.07), OAK, bevel=0.002,
        parent=root)
    box("Desk_Pencil_Drawer", (px0 - lx - 0.06, 0.02, 0.085), ((px0 + lx) / 2, -d / 2 + 0.035, h - 0.07), OAK,
        bevel=0.003, parent=root)
    ball("Desk_Pencil_Knob", 0.012, ((px0 + lx) / 2, -d / 2 + 0.018, h - 0.07), BRASS, parent=root)
    top = h
    # 1950s tabletop valve radio
    rx, ry = -0.38, 0.1
    box("Radio_Cabinet", (0.33, 0.16, 0.19), (rx, ry, top + 0.095), BAKELITE, bevel=0.03, parent=root)
    box("Radio_Grille", (0.17, 0.006, 0.12), (rx - 0.06, ry - 0.08, top + 0.1), mat("cream", 0.6), bevel=0.01, parent=root)
    for k in range(6):
        box("Radio_Grille_Slot", (0.15, 0.004, 0.006), (rx - 0.06, ry - 0.083, top + 0.06 + k * 0.016),
            mat("dark", 0.6), bevel=0, parent=root)
    disc("Radio_Dial", 0.045, 0.006, (rx + 0.09, ry - 0.081, top + 0.11), (0, -1, 0), mat("cream", 0.3, emit=0.3),
         parent=root)
    box("Radio_Dial_Needle", (0.004, 0.004, 0.07), (rx + 0.09, ry - 0.086, top + 0.11), mat("red_string", 0.4),
        bevel=0, rot=(0, R(25), 0), parent=root)
    for k in range(2):
        cyl("Radio_Knob", 0.016, 0.018, (rx + 0.06 + k * 0.06, ry - 0.088, top + 0.038), BRASS, rot=(R(90), 0, 0),
            parent=root)
    # case files, a magnifying glass, a mug of tea and a notepad
    for k in range(3):
        box("Desk_Case_File", (0.24, 0.31, 0.006), (-0.06 + 0.01 * k, -0.03 + 0.006 * k, top + 0.003 + k * 0.006),
            MANILA, bevel=0.001, rot=(0, 0, R(-6 + 7 * k)), parent=root)
    box("Desk_File_Label", (0.08, 0.025, 0.001), (-0.05, -0.15, top + 0.019), PAPER, bevel=0, rot=(0, 0, R(8)),
        parent=root)
    mg = empty("Desk_Magnifier", (0.0, -0.12, top + 0.026), rot=(0, 0, R(30)), parent=root)
    torus("Magnifier_Ring", 0.045, 0.006, (0, 0, 0), BRASS, parent=mg)
    cyl("Magnifier_Lens", 0.043, 0.004, (0, 0, 0), GLASS, bevel=0, parent=mg)
    rod("Magnifier_Handle", (0.05, 0, 0), (0.15, 0, -0.008), 0.009, OAK, parent=mg)
    lathe("Desk_Mug", [(0, 0), (0.038, 0), (0.04, 0.09), (0.036, 0.09), (0.034, 0.012), (0, 0.012)],
          (0.08, 0.15, top), M("accent_1", 0.3, "ceramic"), parent=root)
    torus("Desk_Mug_Handle", 0.025, 0.006, (0.12, 0.15, top + 0.048), M("accent_1", 0.3, "ceramic"), parent=root,
          rot=(R(90), 0, 0))
    cyl("Desk_Mug_Tea", 0.035, 0.004, (0.08, 0.15, top + 0.075), mat("sandstone", 0.2), bevel=0, parent=root)
    box("Desk_Notepad", (0.15, 0.2, 0.012), (-0.22, -0.16, top + 0.006), PAPER, bevel=0.002, rot=(0, 0, R(-12)),
        parent=root)
    rod("Desk_Pencil", (-0.27, -0.2, top + 0.016), (-0.14, -0.12, top + 0.016), 0.004, mat("accent_2", 0.5), parent=root)
    # smartphone in a case, its screen showing an original city map: four districts, a river, a route and a pin
    ph = empty("Desk_Phone", (0.25, -0.13, top), rot=(0, 0, R(-18)), parent=root)
    box("Phone_Case", (0.076, 0.154, 0.009), (0, 0, 0.0045), M("main", 0.5, "leather"), bevel=0.004, parent=ph)
    box("Phone_Screen", (0.066, 0.142, 0.002), (0, 0, 0.0095), mat("cream", 0.3, emit=0.9), bevel=0.001, parent=ph)
    for k, (dx, dy, key) in enumerate(((-0.017, 0.037, "snow"), (0.017, 0.037, "dune"), (-0.017, -0.033, "deco"),
                                       (0.017, -0.033, "hill"))):
        box(f"Phone_Map_District_{k}", (0.03, 0.066, 0.001), (dx, dy, 0.0107), mat(key, 0.4, emit=0.8), bevel=0,
            parent=ph)
    box("Phone_Map_River", (0.006, 0.144, 0.001), (0.0, 0.0, 0.0112), mat("sky_mid", 0.4, emit=0.9), bevel=0,
        rot=(0, 0, R(6)), parent=ph)
    for (x0, y0), (x1, y1) in (((-0.024, -0.055), (-0.024, 0.0)), ((-0.024, 0.0), (0.02, 0.0)), ((0.02, 0.0), (0.02, 0.05))):
        box("Phone_Map_Route", (abs(x1 - x0) + 0.003, abs(y1 - y0) + 0.003, 0.001), ((x0 + x1) / 2, (y0 + y1) / 2, 0.0116),
            mat("accent_1", 0.4, emit=1.0), bevel=0, parent=ph)
    ball("Phone_Map_Pin", 0.0055, (0.02, 0.05, 0.0135), mat("red_string", 0.4, emit=0.8), segs=10, parent=ph)
    box("Phone_Camera_Notch", (0.012, 0.004, 0.001), (0, 0.066, 0.0112), mat("ink", 0.4), bevel=0, parent=ph)


def build_lamp():
    """Banker's desk lamp: brass base and stem, a long teal glass shade, a pull chain."""
    root, w, d, h = furniture_root("lamp")
    box("Lamp_Base", (0.2, 0.13, 0.026), (0, 0, 0.013), BRASS, bevel=0.009, parent=root)
    rod("Lamp_Stem", (0, 0.03, 0.026), (0, 0.03, 0.27), 0.008, BRASS, parent=root)
    rod("Lamp_Yoke", (-0.06, 0.03, 0.27), (0.06, 0.03, 0.27), 0.005, BRASS, parent=root)
    shade_r = 0.065
    pts = [(shade_r * math.cos(math.pi * k / 14), shade_r * 0.75 * math.sin(math.pi * k / 14)) for k in range(15)]
    prism("Lamp_Shade", pts, 0.24, (0, 0.0, 0.258), GLASS_SHADE, rot=(0, 0, R(90)), bevel=0.003, parent=root)
    box("Lamp_Shade_Glow", (0.23, 0.12, 0.004), (0, 0.0, 0.256), mat("bulb", 0.4, emit=2.5), bevel=0, parent=root)
    rod("Lamp_Chain", (0.07, -0.04, 0.255), (0.07, -0.04, 0.18), 0.0015, BRASS, parent=root)
    ball("Lamp_Chain_Bead", 0.006, (0.07, -0.04, 0.178), BRASS, segs=10, parent=root)
    light("Light_Lamp", "POINT", LAMP_STRENGTH * NIGHT_LAMPS, LAMP_K, (0, 0.0, 0.22), size=0.05, parent=root)


def build_chair():
    """Oak banker's swivel chair: four-leg base on casters, iron spindle, saddle seat, spindle back and arms."""
    root, w, d, h = furniture_root("chair")
    for k in range(4):
        a = R(45 + 90 * k)
        tip = (0.27 * math.cos(a), 0.27 * math.sin(a), 0.06)
        rod("Chair_Base_Leg", (0, 0, 0.13), tip, 0.02, OAK_V, r2=0.015, parent=root)
        cyl("Chair_Caster", 0.025, 0.018, (tip[0], tip[1], 0.025), RUBBER, rot=(R(90), 0, a), segs=16, parent=root)
        box("Chair_Caster_Fork", (0.012, 0.03, 0.03), (tip[0], tip[1], 0.05), IRON, bevel=0.002, rot=(0, 0, a),
            parent=root)
    cyl("Chair_Hub", 0.05, 0.08, (0, 0, 0.13), IRON, parent=root)
    cyl("Chair_Spindle", 0.018, 0.26, (0, 0, 0.3), IRON, parent=root)
    cyl("Chair_Spring_Plate", 0.08, 0.015, (0, 0, 0.432), IRON, parent=root)
    cyl("Chair_Seat", 0.235, 0.04, (0, 0.0, 0.46), OAK, bevel=0.008, parent=root).scale = (1, 0.92, 1)
    for k in range(6):                                 # spindle back
        a = R(40 + 20 * k)
        rod("Chair_Spindle_Back", (0.19 * math.cos(a), 0.19 * math.sin(a) * 0.92, 0.48),
            (0.235 * math.cos(a), 0.235 * math.sin(a), 0.84), 0.008, OAK_V, parent=root)
    crest = [(0.24 * math.cos(R(a)), 0.24 * math.sin(R(a)), 0.86) for a in range(15, 170, 10)]
    tube("Chair_Crest_Rail", crest, 0.024, OAK, segs=10, parent=root)
    arm = [(0.25 * math.cos(R(a)), 0.25 * math.sin(R(a)), 0.66) for a in range(-35, 220, 15)]
    tube("Chair_Arm_Rail", arm, 0.017, OAK, segs=10, parent=root)
    for a in (-30, 210):
        rod("Chair_Arm_Post", (0.2 * math.cos(R(a)), 0.2 * math.sin(R(a)), 0.47),
            (0.25 * math.cos(R(a)), 0.25 * math.sin(R(a)), 0.66), 0.012, OAK_V, parent=root)


def build_floor_lamp():
    """Extra-tall reading lamp: weighted marble base, slim brass pole, a bent neck and an enamel dome shade."""
    root, w, d, h = furniture_root("floor_lamp")
    lathe("FloorLamp_Base", [(0, 0), (0.15, 0), (0.16, 0.012), (0.15, 0.04), (0.04, 0.05), (0, 0.05)], (0, 0.0, 0),
          MARBLE, parent=root)
    rod("FloorLamp_Pole", (0, 0.0, 0.05), (0, 0.0, 2.42), 0.012, BRASS, parent=root)
    for z in (1.0, 1.9):
        cyl("FloorLamp_Joint", 0.018, 0.04, (0, 0.0, z), BRASS, parent=root)
    neck = spline([(0, 0.0, 2.4), (0, -0.03, 2.62), (0, -0.14, 2.74), (0, -0.24, 2.73)], 5)
    tube("FloorLamp_Neck", neck, 0.012, BRASS, parent=root)
    sh = empty("FloorLamp_Head", (0, -0.26, 2.72), rot=(R(12), 0, 0), parent=root)
    lathe("FloorLamp_Shade", [(0.02, 0.03), (0.06, 0.02), (0.12, -0.04), (0.155, -0.12), (0.15, -0.125),
                              (0.115, -0.045), (0.056, 0.012), (0.018, 0.022)], (0, 0, 0), SHADE, parent=sh)
    cyl("FloorLamp_Bulb_Glow", 0.1, 0.004, (0, 0, -0.09), mat("bulb", 0.4, emit=3.0), bevel=0, parent=sh)
    spot = light("Light_FloorLamp", "SPOT", 110 * NIGHT_LAMPS, LAMP_K, (0, 0, -0.08), size=0.06, parent=sh)
    spot.data.spot_size, spot.data.spot_blend = R(95), 0.6
    rod("FloorLamp_Switch_Cord", (0, 0.0, 0.6), (0.06, -0.08, 0.3), 0.003, mat("dark", 0.7), parent=root)
    box("FloorLamp_Switch", (0.025, 0.04, 0.015), (0.06, -0.08, 0.29), mat("dark", 0.5), bevel=0.004, parent=root)


def build_armchair():
    """Barrel tub chair: a horseshoe back that flows into the arms, piped top edge, deep seat cushion, oak legs."""
    root, w, d, h = furniture_root("armchair")
    a0, a1 = R(-35), R(215)                          # open at the front (-y)
    for sx in (-1, 1):
        for sy in (-1, 1):
            cyl("Armchair_Leg", 0.022, 0.12, (sx * 0.26, sy * 0.24, 0.06), OAK_V, r2=0.016, rot=(R(180), 0, 0),
                parent=root)
    band("Armchair_Shell", (0.4, 0.39), (0.27, 0.26), (0.12, 0.74), CHAIR_FAB, a0=a0, a1=a1, segs=30, plane="XY",
         bevel=0.025, parent=root)
    cyl("Armchair_Base", 0.33, 0.2, (0, -0.01, 0.22), CHAIR_FAB, bevel=0.02, parent=root).scale = (1, 0.95, 1)
    cyl("Armchair_Cushion", 0.315, 0.11, (0, -0.03, 0.375), CHAIR_FAB, bevel=0.025, parent=root).scale = (1, 0.95, 1)
    for z, rr in ((0.74, (0.385, 0.375)), (0.12, (0.4, 0.39))):
        tube("Armchair_Piping", [(rr[0] * math.cos(a0 + (a1 - a0) * k / 40), rr[1] * math.sin(a0 + (a1 - a0) * k / 40), z)
                                 for k in range(41)], 0.009, PIPING, segs=8, parent=root)
    puffy("Armchair_Back_Cushion", 0.36, 0.26, 0.09, (0, 0.17, 0.55), M("accent_2", 0.91, "fabric"),
          rot=(R(-72), 0, 0), parent=root)
    otter = empty("Otter_Plush", (0.04, -0.06, 0.43), rot=(0, 0, R(-8)), parent=root)
    otter_plush(otter)


def build_rug():
    """Paw-print shaped wool rug (about 180 x 170 cm): a big pad and four toes, each with a cream border."""
    root, w, d, h = furniture_root("rug")
    parts = [((0.0, 0.22), (0.74, 0.6), "main")] + \
            [((x, y), (0.21, 0.26), "main") for x, y in ((-0.66, -0.34), (-0.25, -0.68), (0.25, -0.68), (0.66, -0.34))]
    for k, ((x, y), (rx, ry), key) in enumerate(parts):
        o = cyl(f"Rug_Border_{k}", 1.0, 0.008, (x, y, 0.004), M("cream", 0.97, "knit"), segs=64, bevel=0.002,
                parent=root)
        o.scale = (rx + 0.05, ry + 0.05, 1)
        o = cyl(f"Rug_Paw_{k}", 1.0, 0.009, (x, y, 0.0055), M(key, 0.96, "knit"), segs=64, bevel=0.002, parent=root)
        o.scale = (rx, ry, 1)
    o = cyl("Rug_Pad_Inner", 1.0, 0.0095, (0.0, 0.17, 0.006), M("accent_2", 0.96, "knit"), segs=64, bevel=0.002,
            parent=root)
    o.scale = (0.4, 0.3, 1)


def build_pet():
    """Tortoise plush resident on the rug (swap in your own pet)."""
    root, w, d, h = furniture_root("pet")
    tortoise_plush(root, z=0.012)


def build_bed():
    """Single platform bed (90 x 200 mattress) tucked into a hill nook: a hill-shaped arched hood with a porthole,
    grass on top, a soft lining and warm string lights inside."""
    root, w, d, h = furniture_root("bed")
    box("Bed_Plinth", (0.8, 1.98, 0.09), (0, 0.02, 0.045), mat("dark", 0.7), bevel=0.003, parent=root)
    box("Bed_Frame", (0.92, 2.06, 0.24), (0, 0.0, 0.21), OAK_Y, bevel=0.006, parent=root)
    box("Bed_Mattress", (0.86, 1.96, 0.18), (0, 0.0, 0.42), LINEN, bevel=0.025, parent=root)
    puffy("Bed_Duvet", 0.9, 1.2, 0.07, (0, -0.42, 0.53), DUVET, parent=root)
    puffy("Bed_Duvet_Fold", 0.9, 0.22, 0.06, (0, 0.24, 0.55), DUVET, parent=root)
    puffy("Bed_Pillow", 0.6, 0.36, 0.13, (0, 0.76, 0.58), LINEN, rot=(R(-14), 0, 0), parent=root)
    # carrot-shaped plush cushion (a 60 cm food-shaped bolster): tapered knit body with ridges and a leafy top
    cc = empty("Bed_Carrot_Cushion", (-0.06, -0.12, 0.645), rot=(0, R(90), R(28)), parent=root)
    carrot_k = M("carrot", 0.93, "knit")
    lathe("Carrot_Body", [(0, -0.3), (0.012, -0.29), (0.035, -0.2), (0.058, -0.05), (0.072, 0.12), (0.074, 0.2),
                          (0.06, 0.235), (0, 0.24)], (0, 0, 0), carrot_k, segs=24, parent=cc)
    for k, z in enumerate((-0.2, -0.11, -0.01, 0.09)):
        rr = 0.035 + (0.072 - 0.035) * (z + 0.2) / 0.32
        torus("Carrot_Ridge", rr + 0.002, 0.004, (0, 0, z), carrot_k, parent=cc, seg=20, tseg=6)
    for k in range(3):
        a = 2 * math.pi * k / 3
        puffy("Carrot_Leaf", 0.05, 0.16, 0.018, (0.02 * math.cos(a), 0.02 * math.sin(a), 0.31),
              M("accent_3", 0.92, "knit"), rot=(R(90 + 18 * math.cos(a)), R(18 * math.sin(a)), a), parent=cc, n=8)
    box("Bed_Throw", (0.94, 0.34, 0.025), (0, -0.82, 0.565), THROW, bevel=0.01, parent=root)
    for sx in (-1, 1):
        box("Bed_Throw_Drop", (0.02, 0.34, 0.2), (sx * 0.47, -0.82, 0.47), THROW, bevel=0.008, parent=root)
    # the hill hood: side walls up to 0.6 m, then a tall half-ellipse arch (top at 1.72 m)
    y0, y1 = 0.25, 1.05
    SPR = 0.6
    for sx in (-1, 1):
        box("Bed_Hood_Side", (0.05, y1 - y0, SPR), (sx * 0.495, (y0 + y1) / 2, SPR / 2), HILL, bevel=0.006,
            parent=root)
        box("Bed_Hood_Lining_Side", (0.012, y1 - y0 - 0.02, SPR - 0.05), (sx * 0.464, (y0 + y1) / 2 + 0.01, SPR / 2 + 0.03),
            LINING, bevel=0.004, parent=root)
    band("Bed_Hood", (0.52, 1.12), (0.47, 1.07), (y0, y1), HILL, loc=(0, 0, SPR), segs=32, bevel=0.006, parent=root)
    band("Bed_Hood_Lining", (0.47, 1.07), (0.458, 1.058), (y0 + 0.01, y1), LINING, loc=(0, 0, SPR), segs=32,
         parent=root)
    rim = [(-0.495, y0 - 0.006, 0.02)] + [(0.495 * math.cos(math.pi - math.pi * k / 30), y0 - 0.006,
                                           SPR + 1.095 * math.sin(math.pi - math.pi * k / 30)) for k in range(31)] + \
          [(0.495, y0 - 0.006, 0.02)]
    tube("Bed_Hood_Rim", rim, 0.03, OAK, segs=10, parent=root)
    # porthole on the camera side
    a = R(32)
    px, pz = 0.52 * math.cos(a), SPR + 1.12 * math.sin(a)
    nrm = Vector((math.cos(a) / 0.52, 0, math.sin(a) / 1.12)).normalized()
    pp = Vector((px, 0.66, pz)) + nrm * 0.004
    disc("Bed_Porthole_Glass", 0.085, 0.006, pp, nrm, mat("bulb", 0.3, emit=1.4), parent=root)
    ring = torus("Bed_Porthole_Ring", 0.088, 0.016, pp, OAK, parent=root)
    ring.rotation_euler = nrm.to_track_quat("Z", "Y").to_euler()
    for k in range(4):                                 # porthole bolts
        ang = math.pi / 4 + k * math.pi / 2
        q = nrm.to_track_quat("Z", "Y")
        off = q @ Vector((0.088 * math.cos(ang), 0.088 * math.sin(ang), 0.016))
        ball("Bed_Porthole_Bolt", 0.006, pp + off, BRASS, segs=8, parent=root)
    # grass and little flowers on top of the hill
    tufts = [((0.53 * math.cos(R(ang)), y + 0.04 * ((i + j) % 2), SPR + 1.13 * math.sin(R(ang))), 0.05)
             for i, ang in enumerate((58, 72, 84, 96, 108, 122)) for j, y in enumerate((0.3, 0.46, 0.62, 0.78, 0.94))]
    foliage("Bed_Hood_Grass", tufts, 16, (0.075, 0.012), mat("leaf", 0.6), parent=root, seed=SEED + 8, droop=-0.7)
    foliage("Bed_Hood_Grass_Dark", tufts[::2], 10, (0.06, 0.012), mat("plant", 0.6), parent=root, seed=SEED + 9,
            droop=-0.8)
    for k, (fx, fy, key) in enumerate(((0.06, 0.42, "accent_2"), (-0.08, 0.7, "cream"), (0.12, 0.9, "accent_1"),
                                       (-0.2, 0.55, "accent_2"), (0.26, 0.34, "cream"), (0.3, 0.74, "accent_2"),
                                       (-0.02, 0.98, "accent_1"), (0.2, 0.58, "neon"))):
        fz = SPR + 1.12 * math.sqrt(max(0.0, 1 - (fx / 0.52) ** 2))
        rod("Bed_Flower_Stem", (fx, fy, fz - 0.01), (fx, fy, fz + 0.07), 0.003, STEM, parent=root)
        for j in range(5):
            ang = 2 * math.pi * j / 5
            ball("Bed_Flower_Petal", 0.014, (fx + 0.015 * math.cos(ang), fy + 0.015 * math.sin(ang), fz + 0.075),
                 mat(key, 0.6), scale=(1, 1, 0.4), segs=8, parent=root)
        ball("Bed_Flower_Heart", 0.007, (fx, fy, fz + 0.078), mat("accent_1" if key != "accent_1" else "accent_2", 0.5),
             segs=8, parent=root)
    # string lights inside the nook
    if STRING_LIGHTS:
        pts = [(0.44 * math.cos(R(a)), y1 - 0.06, SPR + 1.03 * math.sin(R(a))) for a in range(12, 175, 12)]
        tube("Bed_String_Wire", spline(pts, 3), 0.002, mat("dark", 0.6), segs=5, parent=root)
        for k, p in enumerate(pts):
            ball("Bed_String_Bulb", 0.014, (p[0], p[1] - 0.01, p[2] - 0.03), mat("bulb", 0.3, emit=5.0), segs=10,
                 parent=root)
    light("Light_Nook", "POINT", 9 * NIGHT_LAMPS, LAMP_K, (0, 0.62, 1.1), size=0.15, parent=root)
    rc = empty("Raccoon_Plush", (0.08, -0.66, 0.58), rot=(0, 0, R(28)), parent=root)
    raccoon_plush(rc)


def build_plant():
    """Potted golden bamboo (~180 cm): ringed canes with nodes, side twigs and narrow leaves, in a glazed pot."""
    root, w, d, h = furniture_root("plant")
    lathe("Plant_Pot", [(0, 0), (0.15, 0), (0.155, 0.012), (0.19, 0.36), (0.205, 0.365), (0.207, 0.4), (0.19, 0.405),
                        (0.185, 0.38), (0.17, 0.38), (0, 0.38)], (0, 0, 0), M("main", 0.28, "ceramic"), parent=root)
    torus("Plant_Pot_Band", 0.19, 0.008, (0, 0, 0.3), M("cream", 0.3, "ceramic"), parent=root)
    cyl("Plant_Soil", 0.175, 0.01, (0, 0, 0.38), SOIL, bevel=0, parent=root)
    rnd = random.Random(SEED + 33)
    cane_m = mat("bamboo", 0.45, color="#C9C356" if not NIGHT else "#A9A64C")
    node_m = mat("bamboo_node", 0.5, color="#8E9A3A" if not NIGHT else "#76803A")
    clusters = []
    for k in range(9):
        a = 2 * math.pi * k / 9 + rnd.uniform(-0.3, 0.3)
        r0 = rnd.uniform(0.03, 0.12)
        top = rnd.uniform(1.25, 1.82)
        lean = rnd.uniform(0.04, 0.16)
        p0 = Vector((r0 * math.cos(a), r0 * math.sin(a), 0.38))
        p1 = Vector(((r0 + lean) * math.cos(a), (r0 + lean) * math.sin(a), top))
        rod(f"Plant_Cane_{k}", p0, p1, 0.011, cane_m, r2=0.007, parent=root)
        n = int((top - 0.45) / 0.22)
        for j in range(1, n + 1):
            t = j / (n + 1)
            q = p0.lerp(p1, t)
            cyl("Plant_Cane_Node", 0.0125 - 0.004 * t, 0.008, q, node_m, segs=12, bevel=0, parent=root)
            if t > 0.45:
                out = Vector((math.cos(a + (0.9 if j % 2 else -0.9)), math.sin(a + (0.9 if j % 2 else -0.9)), 0.6))
                tip = q + out.normalized() * rnd.uniform(0.12, 0.2)
                rod("Plant_Twig", q, tip, 0.003, node_m, parent=root)
                clusters.append((tuple(tip), 0.09))
        clusters.append((tuple(p1), 0.1))
    foliage("Plant_Bamboo_Leaves", clusters, 22, (0.13, 0.018), LEAF, parent=root, seed=SEED + 34, droop=0.55)
    foliage("Plant_Bamboo_Leaves_Dark", clusters[::2], 12, (0.12, 0.016), STEM, parent=root, seed=SEED + 35, droop=0.6)


def build_wall_shelf():
    """Mouse-scale cafe and market built into the skirting board (1:12 dollhouse scale)."""
    root, w, d, h = furniture_root("wall_shelf")
    by = d / 2                                       # back of the shelf = the wall
    box("Mini_Pavement", (w, d, 0.015), (0, 0, 0.0075), PAVE, bevel=0.002, parent=root)
    box("Mini_Kerb", (w, 0.012, 0.02), (0, -d / 2 + 0.006, 0.01), mat("pavement", 0.7), bevel=0.002, parent=root)
    for k, (cx_, face, awn_a, awn_b, sign) in enumerate(((-0.225, CAP, CANVAS_A, CANVAS_B, "CAFE"),
                                                        (0.225, PAINT_TALL, CANVAS_C, CANVAS_B, "MARKET"))):
        box(f"Mini_Facade_{k}", (0.43, 0.025, 0.3), (cx_, by - 0.0125, 0.165), face, bevel=0.003, parent=root)
        box(f"Mini_Cornice_{k}", (0.44, 0.035, 0.015), (cx_, by - 0.0175, 0.31), TRIM, bevel=0.002, parent=root)
        prism(f"Mini_Door_{k}", arch_pts(0.055, 0.12, 8, z0=0.015), 0.006, (cx_ - 0.13, by - 0.027, 0),
              mat("walnut", 0.5, color="#5A3A28"), bevel=0.001, parent=root)
        ball(f"Mini_Door_Knob_{k}", 0.003, (cx_ - 0.115, by - 0.032, 0.07), BRASS, segs=8, parent=root)
        box(f"Mini_Window_{k}", (0.15, 0.004, 0.09), (cx_ + 0.06, by - 0.027, 0.105), mat("bulb", 0.3, emit=1.8),
            bevel=0, parent=root)
        for dx in (-0.075, 0.0, 0.075):
            box(f"Mini_Window_Bar_{k}", (0.006, 0.008, 0.096), (cx_ + 0.06 + dx, by - 0.029, 0.105), TRIM, bevel=0,
                parent=root)
        for dz in (-0.045, 0.045):
            box(f"Mini_Window_Rail_{k}", (0.156, 0.008, 0.006), (cx_ + 0.06, by - 0.029, 0.105 + dz), TRIM, bevel=0,
                parent=root)
        for j in range(8):                           # striped awning
            box(f"Mini_Awning_{k}", (0.04, 0.07, 0.004), (cx_ - 0.14 + j * 0.04, by - 0.055, 0.19),
                awn_a if j % 2 == 0 else awn_b, bevel=0, rot=(R(-28), 0, 0), parent=root)
            ball(f"Mini_Awning_Scallop_{k}", 0.012, (cx_ - 0.14 + j * 0.04, by - 0.087, 0.172),
                 awn_a if j % 2 == 0 else awn_b, scale=(1.4, 0.15, 0.8), segs=10, parent=root)
        box(f"Mini_Sign_{k}", (0.2, 0.006, 0.045), (cx_, by - 0.029, 0.26), mat("cream", 0.5), bevel=0.002, parent=root)
        label(f"Mini_Sign_Text_{k}", sign, 0.026, (cx_, by - 0.033, 0.26), INK, parent=root, depth=0.001)
    # cafe terrace: two bistro tables and four chairs
    for t, tx in enumerate((-0.34, -0.17)):
        cyl("Mini_Table_Top", 0.022, 0.004, (tx, -0.03, 0.068), MARBLE, bevel=0, parent=root)
        rod("Mini_Table_Stem", (tx, -0.03, 0.015), (tx, -0.03, 0.066), 0.0025, IRON, parent=root)
        cyl("Mini_Table_Foot", 0.012, 0.003, (tx, -0.03, 0.0165), IRON, bevel=0, parent=root)
        cyl("Mini_Cup", 0.005, 0.008, (tx + 0.006, -0.035, 0.074), CERAMIC, bevel=0, segs=10, parent=root)
        for sx in (-1, 1):
            cx_ = tx + sx * 0.04
            box("Mini_Chair_Seat", (0.03, 0.03, 0.004), (cx_, -0.03, 0.045), IRON, bevel=0, parent=root)
            box("Mini_Chair_Back", (0.004, 0.03, 0.035), (cx_ + sx * 0.015, -0.03, 0.064), IRON, bevel=0, parent=root)
            for lx in (-1, 1):
                for ly in (-1, 1):
                    rod("Mini_Chair_Leg", (cx_ + lx * 0.012, -0.03 + ly * 0.012, 0.015),
                        (cx_ + lx * 0.012, -0.03 + ly * 0.012, 0.044), 0.0015, IRON, segs=6, parent=root)
    # market front: crates of tiny fruit and a potted tree
    for c, cx_ in enumerate((0.13, 0.2, 0.27, 0.34)):
        box("Mini_Crate", (0.055, 0.04, 0.03), (cx_, -0.025, 0.03), OAK, bevel=0.002, parent=root)
        key = ("accent_1", "accent_3", "accent_2", "terracotta")[c]
        for j in range(6):
            ball("Mini_Fruit", 0.0085, (cx_ - 0.017 + (j % 3) * 0.017, -0.035 + (j // 3) * 0.018, 0.048),
                 mat(key, 0.45), segs=8, parent=root)
    lathe("Mini_Planter", [(0, 0), (0.012, 0), (0.016, 0.03), (0, 0.03)], (0.415, -0.04, 0.015), TERRA, segs=12,
          parent=root)
    ball("Mini_Tree", 0.025, (0.415, -0.04, 0.075), LEAF, segs=12, parent=root)
    rod("Mini_Tree_Trunk", (0.415, -0.04, 0.04), (0.415, -0.04, 0.06), 0.003, OAK, parent=root)
    # a street lamp between the shops and festoon lights along the top
    rod("Mini_Lamp_Post", (0.0, -0.05, 0.015), (0.0, -0.05, 0.22), 0.0035, IRON, parent=root)
    ball("Mini_Lamp_Globe", 0.012, (0.0, -0.05, 0.228), mat("bulb", 0.3, emit=5.0), segs=10, parent=root)
    if STRING_LIGHTS:
        fest = [(-0.43 + 0.86 * k / 12, by - 0.035, 0.3 - 0.025 * math.sin(math.pi * (k % 6) / 6)) for k in range(13)]
        tube("Mini_Festoon_Wire", fest, 0.0012, mat("dark", 0.6), segs=4, parent=root)
        for k, p in enumerate(fest[1:-1]):
            ball("Mini_Festoon_Bulb", 0.0045, (p[0], p[1], p[2] - 0.006), mat("bulb", 0.3, emit=6.0), segs=8,
                 parent=root)
    light("Light_MouseCafe", "POINT", 1.4 * NIGHT_LAMPS, LAMP_K, (-0.1, -0.12, 0.2), size=0.04, parent=root)


PLACEHOLDERS = {
    "desk": build_desk, "lamp": build_lamp, "chair": build_chair, "floor_lamp": build_floor_lamp,
    "armchair": build_armchair, "rug": build_rug, "pet": build_pet, "bed": build_bed, "plant": build_plant,
    "wall_shelf": build_wall_shelf,
}

if SHOW_PLACEHOLDER_FURNITURE:
    for slot_name, build in PLACEHOLDERS.items():
        build()


# =====================================================================
#  DECOR: kitchen island, stools and cups in three sizes, window-sill residents, the delivery tube
# =====================================================================
# the mouse door's porch lamp casts a small warm pool, so the tiny door reads even in a thumbnail
light("Light_Mouse_Porch", "POINT", 1.6 * NIGHT_LAMPS, LAMP_K, (MOUSE_X + 0.115, D - 0.07, FLOOR_Z + 0.2), size=0.02)
# Kitchen island: a butcher-block kitchen trolley (100 x 43 x 90 cm) with a drawer, a door, an open shelf,
# a towel rail and casters. On top: a dome kettle, a 2-slice toaster, fruit and carrots, cups in three sizes.
ki = empty("Kitchen_Island", (2.14, 0.8, FLOOR_Z), rot=(0, 0, R(36)))
KW, KD, KH = 1.0, 0.43, 0.9
TOP_T = 0.038
PAINT_KI = M("main", 0.42, "plaster", scale=3)
BLOCK = M("wood", 0.48, "wood")
for sx in (-1, 1):                                   # side panels on a recessed plinth
    box("Island_Side", (0.018, KD - 0.02, KH - TOP_T - 0.08), (sx * (KW / 2 - 0.029), 0, 0.08 + (KH - TOP_T - 0.08) / 2),
        PAINT_KI, bevel=0.003, parent=ki)
box("Island_Divider", (0.018, KD - 0.04, KH - TOP_T - 0.1), (0.12, 0, 0.09 + (KH - TOP_T - 0.1) / 2), PAINT_KI,
    bevel=0.002, parent=ki)
box("Island_Back", (KW - 0.06, 0.012, KH - TOP_T - 0.1), (0, KD / 2 - 0.016, 0.09 + (KH - TOP_T - 0.1) / 2), PAINT_KI,
    bevel=0.002, parent=ki)
for z in (0.09, 0.45):                               # bottom and middle shelves of the open bay
    box("Island_Shelf", (KW - 0.076, KD - 0.04, 0.018), (0, 0, z), PAINT_KI, bevel=0.002, parent=ki)
box("Island_Plinth", (KW - 0.1, KD - 0.08, 0.06), (0, 0, 0.05), mat("dark", 0.6), bevel=0.002, parent=ki)
box("Island_Top", (KW, KD, TOP_T), (0, 0, KH - TOP_T / 2), BLOCK, bevel=0.004, parent=ki)
for k in range(1, 7):                                # butcher-block staves (glued strips)
    box("Island_Top_Stave", (0.0015, KD + 0.001, TOP_T - 0.004), (-KW / 2 + KW * k / 7, 0, KH - TOP_T / 2),
        mat("dark", 0.6, color="#B48552"), bevel=0, parent=ki)
# right bay: a drawer over a door (3 mm gaps), brass knobs
DX0, DX1 = 0.13, KW / 2 - 0.038
dcx_, dw_ = (DX0 + DX1) / 2, DX1 - DX0
box("Island_Drawer", (dw_ - 0.006, 0.02, 0.14), (dcx_, -KD / 2 + 0.01, KH - TOP_T - 0.075), PAINT_KI, bevel=0.003,
    parent=ki)
box("Island_Door", (dw_ - 0.006, 0.02, 0.6), (dcx_, -KD / 2 + 0.01, 0.1 + 0.3 + 0.012), PAINT_KI, bevel=0.003,
    parent=ki)
box("Island_Door_Panel", (dw_ - 0.07, 0.006, 0.52), (dcx_, -KD / 2 - 0.001, 0.412), PAINT_KI, bevel=0.006, parent=ki)
for z in (KH - TOP_T - 0.075, 0.62):
    ball("Island_Knob", 0.014, (dcx_ + (0.0 if z > 0.7 else -dw_ / 2 + 0.05), -KD / 2 - 0.012, z), BRASS, parent=ki)
# casters
for sx in (-1, 1):
    for sy in (-1, 1):
        cyl("Island_Caster", 0.025, 0.02, (sx * (KW / 2 - 0.06), sy * (KD / 2 - 0.06), 0.025), RUBBER, rot=(R(90), 0, 0),
            segs=16, parent=ki)
        box("Island_Caster_Fork", (0.02, 0.035, 0.03), (sx * (KW / 2 - 0.06), sy * (KD / 2 - 0.06), 0.045), IRON,
            bevel=0.002, parent=ki)
# towel rail on the left end, with a striped tea towel
for sy in (-1, 1):
    rod("Island_Rail_Post", (-KW / 2 - 0.0, sy * 0.15, 0.74), (-KW / 2 - 0.04, sy * 0.15, 0.74), 0.006, CHROME, parent=ki)
rod("Island_Rail", (-KW / 2 - 0.04, -0.16, 0.74), (-KW / 2 - 0.04, 0.16, 0.74), 0.007, CHROME, parent=ki)
for k in range(5):
    box("Island_Towel", (0.006, 0.2, 0.05), (-KW / 2 - 0.047, 0.0, 0.715 - k * 0.05),
        M("cream" if k % 2 else "accent_1", 0.9, "fabric"), bevel=0.002, parent=ki)
# open bay: a crate of apples and greens on the bottom shelf, cookbooks on the middle shelf
CARROT = M("carrot", 0.5, "ceramic")
CARROT_TOP = mat("accent_3", 0.6)


def carrot(name, base, direction, length, r, parent):
    """A carrot: a tapered orange root with a few green tops."""
    base, dv = Vector(base), Vector(direction).normalized()
    rod(f"{name}_Root", base, base + dv * length, r, CARROT, r2=r * 0.15, parent=parent, segs=10)
    for j in range(3):
        sp = Vector((math.cos(j * 2.1), math.sin(j * 2.1), 0)) * 0.3
        rod(f"{name}_Top", base, base + (-dv + sp).normalized() * length * 0.45, r * 0.22, CARROT_TOP, parent=parent,
            segs=5)


for sx in (-1, 1):
    box("Island_Crate_End", (0.012, 0.26, 0.12), (-0.2 + sx * 0.15, -0.01, 0.1 + 0.06), OAK, bevel=0.002, parent=ki)
for sy in (-1, 1):
    for z in (0.12, 0.18):
        box("Island_Crate_Slat", (0.3, 0.01, 0.035), (-0.2, -0.01 + sy * 0.125, z), OAK, bevel=0.002, parent=ki)
for k in range(8):
    ball(f"Island_Crate_Apple_{k}", 0.03, (-0.31 + (k % 4) * 0.072, -0.07 + 0.1 * (k // 4), 0.19 + 0.01 * (k % 2)),
         M("red_string" if k % 3 else "accent_3", 0.42, "ceramic"), parent=ki)
for k in range(2):
    puffy(f"Island_Crate_Greens_{k}", 0.09, 0.07, 0.05, (-0.27 + k * 0.15, 0.03, 0.235), M("leaf", 0.8, "fabric"),
          parent=ki)
for k, (key, wd) in enumerate((("accent_1", 0.035), ("cream", 0.03), ("accent_3", 0.04), ("accent_2", 0.028))):
    box("Island_Cookbook", (wd, 0.2, 0.24 - 0.02 * (k % 2)), (-0.4 + k * 0.042 + (0.06 if k == 3 else 0), -0.02,
        0.459 + (0.12 - 0.01 * (k % 2))), M(key, 0.7, "paper"), bevel=0.002, rot=(0, R(-14) if k == 3 else 0, 0),
        parent=ki)
# on the worktop
TOPZ = KH
kt = empty("Island_Kettle", (-0.33, 0.05, TOPZ), rot=(0, 0, R(-30)), parent=ki)
cyl("Kettle_Base", 0.085, 0.018, (0, 0, 0.009), mat("dark", 0.4), bevel=0.005, parent=kt)
lathe("Kettle_Body", [(0, 0.018), (0.08, 0.018), (0.095, 0.06), (0.095, 0.12), (0.075, 0.19), (0.04, 0.215), (0, 0.22)],
      (0, 0, 0), M("accent_2", 0.25, "ceramic"), parent=kt)
cyl("Kettle_Lid_Knob", 0.014, 0.022, (0, 0, 0.228), mat("dark", 0.4), bevel=0.005, parent=kt)
rod("Kettle_Spout", (0.0, -0.075, 0.09), (0.0, -0.135, 0.17), 0.016, M("accent_2", 0.25, "ceramic"), r2=0.009, parent=kt)
tube("Kettle_Handle", spline([(0, 0.07, 0.19), (0, 0.13, 0.17), (0, 0.13, 0.08), (0, 0.09, 0.06)], 4), 0.011,
     mat("dark", 0.4), segs=10, parent=kt)
disc("Kettle_Gauge", 0.015, 0.004, (0.07, -0.06, 0.1), (0.75, -0.65, 0), mat("cream", 0.3), parent=kt)
ts = empty("Island_Toaster", (-0.06, 0.07, TOPZ), rot=(0, 0, R(0)), parent=ki)
box("Toaster_Body", (0.26, 0.17, 0.18), (0, 0, 0.095), M("cream", 0.28, "ceramic"), bevel=0.04, parent=ts)
for sx in (-1, 1):
    box("Toaster_Foot", (0.04, 0.12, 0.008), (sx * 0.09, 0, 0.004), mat("dark", 0.5), bevel=0.002, parent=ts)
    box("Toaster_Slot", (0.18, 0.026, 0.01), (0, sx * 0.035, 0.18), mat("dark", 0.6), bevel=0.003, parent=ts)
box("Toaster_Lever", (0.03, 0.02, 0.014), (0.13, -0.02, 0.13), mat("dark", 0.4), bevel=0.004, parent=ts)
disc("Toaster_Dial", 0.016, 0.008, (0.05, -0.088, 0.08), (0, -1, 0), CHROME, parent=ts)
box("Toaster_Toast", (0.11, 0.012, 0.1), (-0.02, 0.035, 0.21), M("sand", 0.85, "paper"), bevel=0.012, parent=ts)
box("Toaster_Toast_Crust", (0.116, 0.008, 0.104), (-0.02, 0.035, 0.21), mat("sandstone", 0.8), bevel=0.012, parent=ts)
# a bowl of fruit and carrots
lathe("Island_Bowl", [(0, 0), (0.06, 0), (0.12, 0.06), (0.125, 0.065), (0.115, 0.065), (0.055, 0.008), (0, 0.008)],
      (0.27, 0.06, TOPZ), M("cream", 0.3, "ceramic"), parent=ki)
torus("Island_Bowl_Band", 0.105, 0.004, (0.27, 0.06, TOPZ + 0.05), M("accent_1", 0.3, "ceramic"), parent=ki)
frnd = random.Random(SEED + 40)
for k in range(6):
    a = 2 * math.pi * k / 6 + frnd.uniform(-0.2, 0.2)
    key = ("accent_1", "red_string", "accent_3", "accent_1", "accent_2", "red_string")[k]
    ball("Island_Fruit", 0.033, (0.27 + 0.06 * math.cos(a), 0.06 + 0.06 * math.sin(a), TOPZ + 0.055),
         M(key, 0.42, "ceramic"), scale=(1.15, 1, 1) if key == "accent_2" else (1, 1, 1), parent=ki)
for k in range(4):
    a = R(-30 + 22 * k)
    carrot(f"Island_Bowl_Carrot_{k}", (0.27 + 0.03 * math.cos(a), 0.06 + 0.03 * math.sin(a), TOPZ + 0.16),
           (math.cos(a) * 0.8, math.sin(a) * 0.8, -1.0), 0.17, 0.018, ki)
# cutting board with a cucumber and a few slices
box("Island_Board", (0.24, 0.14, 0.018), (0.25, -0.13, TOPZ + 0.009), OAK, bevel=0.004, rot=(0, 0, R(8)), parent=ki)
rod("Island_Board_Cucumber", (0.17, -0.12, TOPZ + 0.036), (0.31, -0.1, TOPZ + 0.036), 0.018, M("plant", 0.5, "ceramic"),
    parent=ki, segs=12)
for k in range(3):
    cyl("Island_Board_Slice", 0.017, 0.005, (0.34 + 0.012 * k, -0.16 + 0.018 * k, TOPZ + 0.021), mat("leaf", 0.5),
        segs=12, parent=ki)
# cups in three sizes: a 6 cl espresso cup, a 35 cl mug and a giant 3 litre mug
CUP_M = M("accent_1", 0.28, "ceramic")
for k, (x, y, r, hgt, key) in enumerate(((-0.17, -0.15, 0.022, 0.05, "cream"), (-0.08, -0.14, 0.04, 0.095, "accent_3"),
                                          (0.06, -0.11, 0.085, 0.2, "accent_1"))):
    cm = M(key, 0.28, "ceramic")
    lathe(f"Island_Cup_{k}", [(0, 0), (r * 0.92, 0), (r, hgt), (r * 0.9, hgt), (r * 0.84, hgt * 0.08), (0, hgt * 0.08)],
          (x, y, TOPZ), cm, parent=ki)
    torus(f"Island_Cup_Handle_{k}", hgt * 0.27, r * 0.15, (x + r + hgt * 0.17, y, TOPZ + hgt * 0.52), cm, parent=ki,
          rot=(R(90), 0, 0), seg=20, tseg=8)
    cyl(f"Island_Cup_Drink_{k}", r * 0.86, 0.004, (x, y, TOPZ + hgt * 0.82), mat("sandstone", 0.2), bevel=0, parent=ki)
cyl("Island_Saucer", 0.04, 0.008, (-0.17, -0.15, TOPZ + 0.002), M("cream", 0.28, "ceramic"), bevel=0.003, parent=ki)

# Stools in three sizes lined up at the island: a tiny 25 cm stool, a 65 cm bar stool and a 105 cm giant stool.
for k, (x, y, seat, r, key) in enumerate(((-0.36, -0.52, 0.25, 0.11, "wood"), (0.03, -0.55, 0.65, 0.16, "accent_1"),
                                          (0.52, -0.58, 1.05, 0.2, "accent_3"))):
    st = empty(f"Stool_{k}", (x, y, 0), parent=ki)
    sm = OAK if key == "wood" else M(key, 0.4, "brushed", metal=0.3)
    cyl(f"Stool_{k}_Seat", r, 0.03 + 0.01 * k, (0, 0, seat - 0.015 - 0.005 * k), sm, bevel=0.006, parent=st)
    nleg = 3 if k == 0 else 4
    spread = r * (1.25 if k else 1.1)
    for j in range(nleg):
        a = 2 * math.pi * j / nleg + R(45)
        rod(f"Stool_{k}_Leg", (r * 0.6 * math.cos(a), r * 0.6 * math.sin(a), seat - 0.03),
            (spread * math.cos(a), spread * math.sin(a), 0.0), 0.012 + 0.005 * k, sm if k else OAK_V, r2=0.01 + 0.004 * k,
            parent=st)
        cyl(f"Stool_{k}_Foot", 0.014 + 0.004 * k, 0.01, (spread * math.cos(a), spread * math.sin(a), 0.005), RUBBER,
            parent=st)
    for zr in ((0.3,) if k == 1 else (0.32, 0.62) if k == 2 else ()):   # footrings
        rr = r * 0.6 + (spread - r * 0.6) * (1 - zr / seat)
        torus(f"Stool_{k}_Footring", rr, 0.009, (0, 0, zr), sm, parent=st, seg=28, tseg=8)
# a little knitted cushion on the tiny stool
cyl("Stool_0_Cushion", 0.1, 0.025, (-0.36, -0.52, 0.27), M("accent_2", 0.92, "knit"), bevel=0.01, parent=ki)

# Two-step wooden step stool (50 cm) at the island's end, so smaller residents can reach the worktop.
ss = empty("Step_Stool", (-0.8, -0.16, 0), rot=(0, 0, R(-28)), parent=ki)
SSW = 0.42
for sx in (-1, 1):
    prism("StepStool_Side", [(-0.2, 0.0), (0.2, 0.0), (0.06, 0.5), (-0.06, 0.5)], 0.018, (sx * (SSW / 2 - 0.009), 0, 0),
          OAK_V, rot=(0, 0, R(90)), bevel=0.003, parent=ss)
box("StepStool_Top", (SSW, 0.2, 0.02), (0, 0.04, 0.49), OAK, bevel=0.004, parent=ss)
box("StepStool_Grip", (0.1, 0.03, 0.022), (0, 0.06, 0.49), mat("dark", 0.6), bevel=0.008, parent=ss)
box("StepStool_Step", (SSW - 0.036, 0.15, 0.02), (0, -0.09, 0.25), OAK, bevel=0.004, parent=ss)
box("StepStool_Stretcher", (SSW - 0.036, 0.018, 0.05), (0, 0.13, 0.08), OAK, bevel=0.003, parent=ss)

# A tiny tub chair (about 1:3 scale) beside the big one: chairs in three sizes, with the desk chair in between.
mc = empty("Mini_Tub_Chair", (1.98, 2.42, FLOOR_Z + 0.018), rot=(0, 0, R(20)))
MS = 0.33
for sx in (-1, 1):
    for sy in (-1, 1):
        cyl("MiniChair_Leg", 0.008, 0.04, (sx * 0.26 * MS, sy * 0.24 * MS, 0.02), OAK_V, r2=0.006, parent=mc)
band("MiniChair_Shell", (0.4 * MS, 0.39 * MS), (0.27 * MS, 0.26 * MS), (0.04, 0.25), CHAIR_FAB, a0=R(-35), a1=R(215),
     segs=24, plane="XY", bevel=0.008, parent=mc)
cyl("MiniChair_Base", 0.33 * MS, 0.07, (0, 0, 0.075), CHAIR_FAB, bevel=0.008, parent=mc)
cyl("MiniChair_Cushion", 0.31 * MS, 0.04, (0, -0.01, 0.125), M("accent_2", 0.9, "fabric"), bevel=0.01, parent=mc)
tube("MiniChair_Piping", [(0.385 * MS * math.cos(R(-35) + R(250) * k / 30), 0.375 * MS * math.sin(R(-35) + R(250) * k / 30),
                           0.25) for k in range(31)], 0.004, PIPING, segs=6, parent=mc)

# Suitcases in three sizes stacked at the foot of the bed as a bed-end table (vintage hard-shell cases:
# 30" case 77 x 51 x 25 cm, 21" case 56 x 38 x 20 cm, and an 18 x 12 x 6 cm case for a very small resident).
cases = empty("Suitcase_Stack", (4.42, 1.98, FLOOR_Z), rot=(0, 0, R(-4)))
STRAP = M("cream", 0.6, "leather")
CORNER = M("dark", 0.5, "leather")
cz = 0.0
for k, (cw, cd, ch, key, turn) in enumerate(((0.77, 0.51, 0.25, "terracotta", 0), (0.56, 0.38, 0.2, "main", 7),
                                             (0.18, 0.12, 0.06, "accent_2", -14))):
    cs = empty(f"Suitcase_{k}", (0.02 * k, -0.02 * k, cz), rot=(0, 0, R(turn)), parent=cases)
    bev = 0.02 if k < 2 else 0.008
    box("Suitcase_Body", (cw, cd, ch), (0, 0, ch / 2), M(key, 0.55, "leather"), bevel=bev, parent=cs)
    box("Suitcase_Seam", (cw + 0.004, cd + 0.004, ch * 0.06), (0, 0, ch * 0.62), mat("dark", 0.5), bevel=bev * 0.5,
        parent=cs)
    for sx in (-1, 1):
        for sy in (-1, 1):                            # leather corner guards on the lid
            ball("Suitcase_Corner", bev * 1.25, (sx * (cw / 2 - bev * 0.5), sy * (cd / 2 - bev * 0.5), ch - bev * 0.5),
                 CORNER, segs=10, parent=cs)
        # two straps over the lid and down the front and back
        box("Suitcase_Strap_Top", (cw * 0.07, cd + 0.006, 0.006), (sx * cw * 0.28, 0, ch + 0.002), STRAP, bevel=0.002,
            parent=cs)
        for sy in (-1, 1):
            box("Suitcase_Strap_Side", (cw * 0.07, 0.006, ch * 0.9), (sx * cw * 0.28, sy * (cd / 2 + 0.002), ch * 0.52),
                STRAP, bevel=0.002, parent=cs)
        box("Suitcase_Latch", (cw * 0.05, 0.01, ch * 0.12), (sx * cw * 0.14, -cd / 2 - 0.004, ch * 0.62), BRASS,
            bevel=0.002, parent=cs)
    tube("Suitcase_Handle", [(-cw * 0.09, -cd / 2 - 0.004, ch * 0.72), (-cw * 0.08, -cd / 2 - 0.03 * (cw / 0.77),
                              ch * 0.74), (cw * 0.08, -cd / 2 - 0.03 * (cw / 0.77), ch * 0.74),
                             (cw * 0.09, -cd / 2 - 0.004, ch * 0.72)], max(0.004, 0.011 * cw / 0.77), STRAP, segs=8,
         parent=cs)
    cz += ch
# a paper luggage tag on the big case
box("Suitcase_Tag", (0.05, 0.003, 0.08), (0.3, -0.262, 0.13), PAPER, bevel=0.002, rot=(0, R(8), 0), parent=cases)
box("Suitcase_Tag_Band", (0.05, 0.0035, 0.012), (0.3, -0.263, 0.155), mat("accent_1", 0.6), bevel=0, rot=(0, R(8), 0),
    parent=cases)

# A cactus and the meerkat plush on the oak window board.
SILL_Z = WIN_Z[0] + 0.03
cac = empty("Sill_Cactus", (0.09, WIN_Y[0] + 0.3, SILL_Z))
lathe("Cactus_Pot", [(0, 0), (0.05, 0), (0.06, 0.09), (0.066, 0.092), (0.066, 0.11), (0, 0.11)], (0, 0, 0), TERRA,
      parent=cac)
cyl("Cactus_Body", 0.04, 0.2, (0, 0, 0.2), mat("plant", 0.6), bevel=0.03, segs=12, parent=cac)
for sx, zz in ((1, 0.21), (-1, 0.17)):
    tube("Cactus_Arm", [(sx * 0.035, 0, zz), (sx * 0.07, 0, zz + 0.005), (sx * 0.08, 0, zz + 0.07)], 0.018,
         mat("plant", 0.6), segs=10, parent=cac)
ball("Cactus_Flower", 0.016, (0, 0, 0.305), mat("neon", 0.5), scale=(1, 1, 0.6), parent=cac)
mk = empty("Meerkat_Plush", (0.09, WIN_Y[1] - 0.35, SILL_Z), rot=(0, 0, R(-80)))
meerkat_plush(mk)
book = empty("Sill_Books", (0.09, WIN_Y[1] - 0.12, SILL_Z))
bz = 0.0
for k, (key, hh) in enumerate((("main", 0.03), ("accent_1", 0.025), ("cream", 0.028))):
    box("Sill_Book", (0.16 - 0.01 * k, 0.12, hh), (0, 0, bz + hh / 2), M(key, 0.7, "paper"), bevel=0.002,
        rot=(0, 0, R(6 * k - 6)), parent=book)
    bz += hh

# Pneumatic delivery tube: out of the wall near the ceiling, down to a wall station with a capsule tray (email).
TX, TY, TR = 0.86, D - 0.075, 0.055
tube("Tube_Pipe", spline([(TX, D + 0.02, 3.06), (TX, D - 0.03, 3.05), (TX, TY, 2.96), (TX, TY, 2.6), (TX, TY, 1.47)], 5),
     TR, TEAL_METAL, segs=20)
for z in (2.95, 2.45, 1.95, 1.55):
    cyl("Tube_Collar", TR + 0.008, 0.035, (TX, TY, z), BRASS, bevel=0.004)
    box("Tube_Clamp", (0.15, 0.02, 0.03), (TX, D - 0.01, z + 0.06), IRON, bevel=0.003)
disc("Tube_Wall_Flange", 0.085, 0.012, (TX, D - 0.006, 3.06), (0, -1, 0), BRASS)
station = box("Tube_Station", (0.27, 0.17, 0.36), (TX, D - 0.085, 1.28), PAINT_TEAL, bevel=0.02)
hook_link(station, "email")
box("Tube_Station_Back", (0.33, 0.02, 0.5), (TX, D - 0.01, 1.25), BRASS, bevel=0.004)
box("Tube_Station_Window", (0.17, 0.004, 0.24), (TX - 0.02, D - 0.172, 1.29), CAPSULE, bevel=0)
for nm, size, loc in [("Top", (0.19, 0.008, 0.012), (TX - 0.02, D - 0.174, 1.416)),
                      ("Bot", (0.19, 0.008, 0.012), (TX - 0.02, D - 0.174, 1.164)),
                      ("L", (0.012, 0.008, 0.25), (TX - 0.11, D - 0.174, 1.29)),
                      ("R", (0.012, 0.008, 0.25), (TX + 0.07, D - 0.174, 1.29))]:
    box(f"Tube_Station_Bezel_{nm}", size, loc, CHROME, bevel=0.002)
capsule("Tube_Capsule_In", (TX - 0.02, D - 0.09, 1.29), (0, 0, 0), 0.22, M("accent_1", 0.32, "ceramic"), r=0.042)
ball("Tube_Station_Lamp", 0.012, (TX + 0.1, D - 0.172, 1.42), mat("accent_3", 0.3, emit=3.0), segs=10)
cyl("Tube_Station_Button", 0.014, 0.012, (TX + 0.1, D - 0.172, 1.36), mat("red_string", 0.4), rot=(R(90), 0, 0))
box("Tube_Station_Plate", (0.07, 0.003, 0.03), (TX + 0.1, D - 0.171, 1.22), BRASS, bevel=0.001)
label("Tube_Station_Plate_Text", "MAIL", 0.018, (TX + 0.1, D - 0.1735, 1.22), INK, depth=0.0008)
# open wire tray under the station, with a capsule that just arrived
TZ = 1.0
box("Tube_Tray_Floor", (0.32, 0.18, 0.006), (TX, D - 0.1, TZ), CHROME, bevel=0.001)
for nm, size, loc in [("Front", (0.32, 0.006, 0.06), (TX, D - 0.19, TZ + 0.03)),
                      ("L", (0.006, 0.18, 0.06), (TX - 0.16, D - 0.1, TZ + 0.03)),
                      ("R", (0.006, 0.18, 0.06), (TX + 0.16, D - 0.1, TZ + 0.03))]:
    box(f"Tube_Tray_{nm}", size, loc, CHROME, bevel=0.001)
arrived = capsule("Tube_Capsule_Arrived", (TX + 0.02, D - 0.1, TZ + 0.048), (0, R(90), R(-6)), 0.3,
                  M("accent_3", 0.32, "ceramic"), r=0.042)
for c in arrived.children:
    hook_link(c, "email")
# a little wall rack of spare capsules
box("Tube_Rack", (0.2, 0.08, 0.02), (0.44, D - 0.04, 1.5), OAK, bevel=0.003)
for k, key in enumerate(("main", "accent_2")):
    capsule(f"Tube_Capsule_Spare_{k}", (0.39 + k * 0.1, D - 0.05, 1.68), (0, 0, 0), 0.34, M(key, 0.33, "ceramic"),
            r=0.04)


# =====================================================================
#  WALL DECOR + PORTFOLIO PICTURES
# =====================================================================
# THE CASE BOARD over the desk (left wall): cork in an oak frame, three photos pinned and tied with red string.
CB_Y, CB_Z, CB_W, CB_H = 3.62, 1.86, 1.2, 0.9
for nm, size, loc in (("Top", (0.03, CB_W, 0.03), (0.015, CB_Y, CB_Z + CB_H / 2 - 0.015)),
                      ("Bottom", (0.03, CB_W, 0.03), (0.015, CB_Y, CB_Z - CB_H / 2 + 0.015))):
    box(f"Board_Frame_{nm}", size, loc, OAK_Y, bevel=0.003)
for sy in (-1, 1):
    box("Board_Frame_Side", (0.03, 0.03, CB_H - 0.06), (0.015, CB_Y + sy * (CB_W / 2 - 0.015), CB_Z), OAK_V, bevel=0.003)
box("Board_Cork", (0.015, CB_W - 0.06, CB_H - 0.06), (0.0125, CB_Y, CB_Z), CORK, bevel=0)
BX = 0.02                                            # front of the cork


def on_board(u, v, x=0.0, tilt=0.0, cu=0.0, cv=0.0):
    """Point on the case board: u along the wall (+y), v up, rotated by tilt (degrees) around (cu, cv)."""
    t = R(tilt)
    du, dv = u - cu, v - cv
    return (BX + x, CB_Y + cu + du * math.cos(t) - dv * math.sin(t), CB_Z + cv + du * math.sin(t) + dv * math.cos(t))


PHOTOS = [(-0.36, 0.17, 3.0), (0.36, 0.19, -4.0), (0.0, -0.2, 2.0)]   # (u, v, tilt) of each photo
pins = []
doodles = (
    lambda c, p, t: [box("Board_Doodle_Tower", (0.002, 0.05, 0.13), on_board(c[0] - 0.06, c[1] - 0.02, 0.0075, t, *c),
                         mat("main", 0.6), bevel=0, rot=(R(t), 0, 0)),
                     box("Board_Doodle_Tower2", (0.002, 0.04, 0.09), on_board(c[0] + 0.0, c[1] - 0.04, 0.0075, t, *c),
                         mat("accent_1", 0.6), bevel=0, rot=(R(t), 0, 0)),
                     box("Board_Doodle_Tower3", (0.002, 0.04, 0.16), on_board(c[0] + 0.06, c[1] - 0.005, 0.0075, t, *c),
                         mat("accent_3", 0.6), bevel=0, rot=(R(t), 0, 0))],
    lambda c, p, t: [ball("Board_Doodle_Pad", 0.035, on_board(c[0], c[1] - 0.02, 0.0075, t, *c), mat("ink", 0.6),
                          scale=(0.05, 1.1, 0.85))] +
                    [ball("Board_Doodle_Toe", 0.014, on_board(c[0] + dx * 0.03, c[1] + 0.035 - abs(dx) * 0.008, 0.0075, t, *c),
                          mat("ink", 0.6), scale=(0.05, 1, 1.2)) for dx in (-1.5, -0.5, 0.5, 1.5)],
    lambda c, p, t: [label("Board_Doodle_Q", "?", 0.14, on_board(c[0], c[1], 0.008, t, *c), mat("red_string", 0.5),
                           rot=(R(90), 0, R(90)), depth=0.001)],
)
for k, (u, v, tilt) in enumerate(PHOTOS):
    c = (u, v)
    box(f"Board_Photo_Border_{k}", (0.003, 0.4, 0.33), on_board(u, v - 0.012, 0.0015, tilt, *c), PAPER, bevel=0,
        rot=(R(tilt), 0, 0))
    hook = hook_image("board", k + 1, (0.36, 0.26), on_board(u, v + 0.004, 0.0045, tilt, *c),
                      rot=(0, -R(tilt), R(90)), default_key=("sky_mid", "accent_2", "cream")[k])
    hook_default(hook, *doodles[k](c, None, tilt))
    pin = on_board(u, v + 0.145, 0.012, tilt, *c)
    pins.append(pin)
    ball(f"Board_Pin_{k}", 0.011, pin, RED, segs=12)
CARDS = [(-0.46, -0.27, -5.0), (0.45, -0.27, 4.0), (0.0, 0.3, -2.0)]
for k, (u, v, tilt) in enumerate(CARDS):
    c = (u, v)
    box(f"Board_Card_{k}", (0.003, 0.15, 0.1), on_board(u, v, 0.0015, tilt, *c), PAPER, bevel=0, rot=(R(tilt), 0, 0))
    box(f"Board_Card_Rule_{k}", (0.002, 0.14, 0.003), on_board(u, v + 0.03, 0.0035, tilt, *c), RED, bevel=0,
        rot=(R(tilt), 0, 0))
    for j in range(3):
        box(f"Board_Card_Line_{k}", (0.002, 0.11 - 0.02 * (j % 2), 0.0025), on_board(u - 0.01, v + 0.005 - j * 0.022, 0.0035,
            tilt, *c), mat("ink", 0.7), bevel=0, rot=(R(tilt), 0, 0))
    pin = on_board(u, v + 0.04, 0.012, tilt, *c)
    pins.append(pin)
    ball(f"Board_Pin_Card_{k}", 0.009, pin, mat("accent_2", 0.3), segs=12)
# red string: photo -> photo, photo -> card, sagging a little between the pins
for a, b in ((0, 5), (5, 1), (0, 2), (1, 2), (2, 3), (2, 4), (0, 3)):
    pa, pb = Vector(pins[a]), Vector(pins[b])
    mid = (pa + pb) / 2 + Vector((0.004, 0, -0.025))
    tube("Board_String", [pa + Vector((0.004, 0, 0)), mid, pb + Vector((0.004, 0, 0))], 0.0022, RED, segs=6)
# sticky notes carry your skills
for k, (u, v, key) in enumerate(((-0.27, -0.35, "accent_2"), (0.27, -0.35, "accent_3"), (0.08, 0.02, "neon"))):
    box(f"Board_Sticky_{k}", (0.003, 0.09, 0.09), on_board(u, v, 0.0015), mat(key, 0.7), bevel=0)
    hook_text("skill", k + 1, ("SKETCH", "CODE", "STORY")[k], 0.02, on_board(u, v, 0.005), rot=(R(90), 0, R(90)),
              material=INK, max_width=0.08, depth=0.0008)
light("Light_Board", "AREA", 6 if not NIGHT else 9, kelvin(4200), (0.75, CB_Y, CB_Z + 0.9), aim=(0, CB_Y, CB_Z),
      size=0.8)

# THE NEWSPAPER over the hill-nook bed (back wall): your name is today's headline.
NK = 1.18                                            # scale of the front page (74 x 90 cm at 1.0)
NX, NZ, NW, NH = 4.45, 2.42, 0.74 * NK, 0.9 * NK
for sz in (-1, 1):
    box("News_Frame_H", (NW + 0.06, 0.03, 0.03), (NX, D - 0.015, NZ + sz * (NH / 2 + 0.015)), mat("dark", 0.4), bevel=0.003)
for sx in (-1, 1):
    box("News_Frame_V", (0.03, 0.03, NH + 0.06), (NX + sx * (NW / 2 + 0.015), D - 0.015, NZ), mat("dark", 0.4), bevel=0.003)
box("News_Paper", (NW, 0.006, NH), (NX, D - 0.012, NZ), NEWS, bevel=0)
TYP = D - 0.017
label("News_Masthead", "THE DAILY PAW", 0.066 * NK, (NX, TYP, NZ + 0.375 * NK), INK, depth=0.0012)
for dz in (0.335, 0.418):
    box("News_Rule", (NW - 0.06, 0.002, 0.004), (NX, TYP, NZ + dz * NK), INK, bevel=0)
label("News_Dateline", "CITY EDITION  -  NEWS FOR EVERY SIZE  -  ONE COIN", 0.0145 * NK, (NX, TYP, NZ + 0.32 * NK), INK,
      depth=0.0008)
hook_text("name", 1, "YOUR NAME", 0.1 * NK, (NX, TYP, NZ + 0.235 * NK), material=INK, max_width=NW - 0.07, depth=0.003)
hook_text("role", 1, "your role", 0.072 * NK, (NX, TYP, NZ + 0.135 * NK), material=mat("red_string", 0.55),
          max_width=NW - 0.12, depth=0.002)
box("News_Rule_2", (NW - 0.06, 0.002, 0.003), (NX, TYP, NZ + 0.095 * NK), INK, bevel=0)
PH_W, PH_H = 0.38 * NK, 0.27 * NK
ph = hook_image("frame", 1, (PH_W, PH_H), (NX - 0.13 * NK, D - 0.0158, NZ - 0.075 * NK), default_key="sky_mid")
hook_default(ph,
             box("News_Photo_Tower_1", (0.06 * NK, 0.002, 0.16 * NK), (NX - 0.22 * NK, D - 0.017, NZ - 0.13 * NK),
                 mat("deco", 0.6), bevel=0),
             box("News_Photo_Tower_2", (0.07 * NK, 0.002, 0.2 * NK), (NX - 0.13 * NK, D - 0.017, NZ - 0.11 * NK),
                 mat("sandstone", 0.6), bevel=0),
             box("News_Photo_Tower_3", (0.05 * NK, 0.002, 0.12 * NK), (NX - 0.05 * NK, D - 0.017, NZ - 0.15 * NK),
                 mat("garden", 0.6), bevel=0),
             ball("News_Photo_Sun", 0.035 * NK, (NX - 0.02 * NK, D - 0.017, NZ + 0.0), mat("accent_2", 0.6),
                  scale=(1, 0.05, 1)))
for j in range(11):                                  # body text columns beside the photo
    box("News_Text", ((0.24 if j % 4 else 0.18) * NK, 0.002, 0.008), (NX + (0.2 - (0.03 if j % 4 == 0 else 0)) * NK,
        TYP, NZ + (0.05 - j * 0.023) * NK), mat("ink", 0.8, color="#7A7A80"), bevel=0)
hook_text("tagline", 1, "fresh ideas for every size", 0.026 * NK, (NX, TYP, NZ - 0.245 * NK), material=INK,
          max_width=NW - 0.08, depth=0.0012)
for col in range(3):
    for j in range(4):
        box("News_Text_Low", (0.2 * NK, 0.002, 0.007), (NX + (-0.24 + col * 0.24) * NK, TYP, NZ + (-0.29 - j * 0.02) * NK),
            mat("ink", 0.8, color="#7A7A80"), bevel=0)
box("News_Picture_Light", (0.36, 0.06, 0.03), (NX, D - 0.07, NZ + NH / 2 + 0.08), BRASS, bevel=0.01)
rod("News_Picture_Light_Arm", (NX, D - 0.005, NZ + NH / 2 + 0.06), (NX, D - 0.06, NZ + NH / 2 + 0.08), 0.008, BRASS)
light("Light_Picture", "AREA", 5 if not NIGHT else 10, LAMP_K, (NX, D - 0.12, NZ + NH / 2 + 0.06),
      aim=(NX, D, NZ - 0.1), size=0.35)

# THE TRANSIT MAP over the door (back wall): an original map, poster hook 1.
MX_, MZ_, MW_, MH_ = hcx, 2.68, 0.74, 0.5
for sz in (-1, 1):
    box("Map_Frame_H", (MW_ + 0.05, 0.025, 0.025), (MX_, D - 0.0125, MZ_ + sz * (MH_ / 2 + 0.0125)), mat("cream", 0.4),
        bevel=0.003)
for sx in (-1, 1):
    box("Map_Frame_V", (0.025, 0.025, MH_ + 0.05), (MX_ + sx * (MW_ / 2 + 0.0125), D - 0.0125, MZ_), mat("cream", 0.4),
        bevel=0.003)
mp = hook_image("poster", 1, (MW_, MH_), (MX_, D - 0.012, MZ_), default_key="cream")
map_parts = [label("Map_Title", "CITY TRANSIT", 0.032, (MX_ - MW_ / 2 + 0.04, D - 0.014, MZ_ + MH_ / 2 - 0.045),
                   mat("ink", 0.6), align="LEFT", depth=0.0008)]
LINES = [("accent_1", [(-0.32, 0.1), (-0.1, 0.1), (0.04, -0.04), (0.32, -0.04)]),
         ("main", [(-0.32, -0.16), (-0.14, -0.16), (0.06, 0.04), (0.06, 0.18)]),
         ("accent_3", [(-0.22, 0.18), (-0.22, -0.06), (0.02, -0.18), (0.3, -0.18)]),
         ("accent_2", [(0.32, 0.14), (0.18, 0.14), (0.06, 0.02), (-0.06, -0.1), (-0.3, -0.1)])]
for k, (key, pts) in enumerate(LINES):
    yy = D - 0.0135 - 0.0004 * k
    for (u0, v0), (u1, v1) in zip(pts, pts[1:]):
        ln = math.hypot(u1 - u0, v1 - v0)
        ang = math.atan2(v1 - v0, u1 - u0)
        map_parts.append(box(f"Map_Line_{k}", (ln + 0.012, 0.001, 0.012), (MX_ + (u0 + u1) / 2, yy, MZ_ + (v0 + v1) / 2),
                             mat(key, 0.6), bevel=0, rot=(0, -ang, 0)))
    for (u, v) in pts:
        map_parts.append(disc(f"Map_Station_{k}", 0.014, 0.002, (MX_ + u, D - 0.016, MZ_ + v), (0, -1, 0), mat("cream", 0.5)))
        map_parts.append(disc(f"Map_Station_Ring_{k}", 0.019, 0.0015, (MX_ + u, D - 0.0148, MZ_ + v), (0, -1, 0),
                              mat("ink", 0.6)))
map_parts.append(box("Map_River", (MW_, 0.0008, 0.035), (MX_, D - 0.0128, MZ_ - 0.03), mat("sky_mid", 0.7), bevel=0,
                     rot=(0, R(8), 0)))
hook_default(mp, *map_parts)


# =====================================================================
#  LIGHTS, WORLD, CAMERA, RENDER
# =====================================================================
# Day: a high midday sun through the factory window throws long window-grid shadows across the floor,
# a soft fill from the camera side, sky light from the window and a warm bounce from the (missing) ceiling.
# Night: cool moonlight, a teal-and-pink city glow through the window, brighter lamps, a lilac fill.
sun_dir = Vector((1.0, -0.22, -0.62)).normalized()
target = Vector((1.8, wy, 0.0))
if NIGHT:
    light("Light_Sun", "SUN", 0.6, kelvin(9000), target - sun_dir * 6, aim=target, size=R(3))
    light("Light_Fill", "AREA", 120 * (W * D / 16), (0.62, 0.56, 1.0), (W + 3, -3, H + 2.5), aim=(W / 2, D / 2, 0.6), size=6)
    light("Light_Window", "AREA", 70, (0.35, 0.85, 1.0), (0.3, wy, wz), aim=(2.4, wy, wz - 0.6), size=1.6)
    light("Light_Neon", "AREA", 35, (1.0, 0.32, 0.65), (0.25, BB_Y - 0.25, BB_Z + 0.2), aim=(2.0, 1.4, 0.6), size=0.8)
    light("Light_Bounce", "AREA", 40, (0.7, 0.55, 1.0), (W / 2, D / 2, H - 0.1), aim=(W / 2, D / 2, 0), size=2.5)
else:
    light("Light_Sun", "SUN", SUN_STRENGTH, kelvin(SUN_WARMTH), target - sun_dir * 6, aim=target, size=R(1.5))
    light("Light_Fill", "AREA", 220 * (W * D / 16), kelvin(6200), (W + 3, -3, H + 2.5), aim=(W / 2, D / 2, 0.6), size=6)
    light("Light_Window", "AREA", 60, kelvin(6800), (0.3, wy, wz), aim=(2.4, wy, wz - 0.6), size=1.6)
    light("Light_Bounce", "AREA", 50, kelvin(4200), (W / 2, D / 2, H - 0.1), aim=(W / 2, D / 2, 0), size=2.5)
light("Light_Skyline", "AREA", 40 if NIGHT else 25, kelvin(6500) if not NIGHT else (0.8, 0.5, 1.0),
      (-T - 0.02, 2.0, 2.7), aim=(-T - 0.3, 2.0, 1.3), size=1.4)

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
bg_amb.inputs["Color"].default_value = (0.42, 0.36, 0.75, 1) if NIGHT else (*kelvin(6300), 1)
bg_amb.inputs["Strength"].default_value = 0.3 if NIGHT else 0.35
path = wn.new("ShaderNodeLightPath")
mix = wn.new("ShaderNodeMixShader")
wl.new(path.outputs["Is Camera Ray"], mix.inputs["Fac"])
wl.new(bg_amb.outputs[0], mix.inputs[1])
wl.new(bg_cam.outputs[0], mix.inputs[2])
wl.new(mix.outputs[0], out.inputs["Surface"])

# Orthographic camera that frames the whole room automatically. The city light box behind the window is hidden
# behind the left wall from this camera, so the standard bounds are used; kit_room_size says the room is W x D.
BOUNDS = [-T, 0, -0.2, W, D + T, H + 0.12]
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
scene.view_settings.exposure = -0.1 if not NIGHT else 0.0

# Remember the style so add_furniture.py can match colours later.
scene["kit_style"] = STYLE
scene["kit_version"] = KIT_VERSION
scene["kit_palette"] = json.dumps(COLORS)
scene["kit_material_finish"] = json.dumps({"roughness": 0.6, "bevel": 0.005, "saturation": 0.85})
scene["kit_theme"] = THEME
scene["kit_bounds"] = BOUNDS
scene["kit_room_size"] = [W, D, H]      # the room itself (the city light box sits outside the left wall)
scene["kit_furniture_colors"] = json.dumps(["main", "accent_1", "accent_2", "accent_3", "cream", "wood", "terracotta",
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
