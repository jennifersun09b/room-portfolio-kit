"""
3D ROOM PORTFOLIO KIT  -  Template: PLANT SHOP (independent London plant shop & florist)
========================================================================================
Builds a little isometric plant shop in soft late-morning daylight, modelled on real independent
plant shops (Conservatory Archives, Prick, Grow London, Bloomist style): painted brick walls, a steel
shop window, a polished concrete floor, galvanised greenhouse shelving with grow-light bars, a stepped
stand of galvanised florist buckets full of cut stems, a potting bench with a metal top and a soil bin,
a timber shop counter with a tablet till, card reader and kraft-paper roll, macrame hangers, pendant
grow lights, a pine display table of succulents and real-looking plants (Strelitzia, monstera,
fiddle-leaf fig, olive, pothos, cacti) in real terracotta and glazed pots. It renders a 1920x1080 image.
Your name and role are chalked on the shop's chalkboard, your projects hang as framed botanical prints
and glow on the till tablet. The A-board outside is your email link.

HOW TO RUN
  Option A (no Blender UI):   blender -b -P plant_shop.py
  Option B (inside Blender):  Scripting tab > Open > plant_shop.py > Run Script (then F12 to render)

You only need to edit the SETTINGS block below. Everything under it builds the room.
Output: output/plant_shop.png and output/plant_shop.blend next to this script.
"""
# REFERENCES  (what each piece is modelled on; brand names appear only here and in research/plant_shop.md)
#   shelf               IKEA HYLLIS shelving unit, galvanised: W60 D27 H140 cm, 4 shelves (+ LED grow bars)
#                       https://www.ikea.com/gb/en/p/hyllis-shelving-unit-in-outdoor-galvanised-00278578/
#   workbench           Outsunny-type potting bench, galvanised top: W103 D53 H162 cm, worktop 90 cm, top shelf 12 cm
#                       https://www.diy.com/departments/outsunny-potting-bench-table-workstation-w-galvanized-tabletop-storage-shelf/5056534581954_BQ.prd
#   soil bin            galvanised steel bin with lid, 30 L: dia 32 x H50 cm
#                       https://www.diy.com/departments/30l-steel-bin-with-lid-smooth-sided-strong-metal-ash-bin-log-bin-or-animal-feed-bin-50cm/5060875444656_BQ.prd
#   hero_prop           Haws-style metal watering can, 1 gallon: L50 x H30 cm (8.8 L Warley Fall is L80.5 x H33)
#                       https://bonsaischule.de/en/accessories/others/watering-equipment/1146-8.8-G/haws-watering-can-galvanized-8.8-l
#   counter             painted tongue-and-groove timber shop counter, oak top: L120 D60 H92 cm, 30 mm top
#                       https://theshopkeepers.com/conservatory-archives
#   ribbon reel         florist's 20 m reel of 25 mm satin ribbon: dia 10 x W 3.6 cm
#                       https://www.tinyboxcompany.co.uk/rose-gold-double-faced-satin-ribbon-20m-x-25mm-rose-gold-ds20rg25
#   compost sack        part-used peat-free compost bag stood upright: ~30 x 19 x 35 cm (full 40 L bag 54 x 38 x 16 cm)
#                       https://www.sure-green.com/melcourt-all-purpose-peat-free-compost-50l.html
#   tablet till         12.9" tablet on a swivel stand: 28.1 x 21.5 cm (screen hook 26 x 19.5 cm)
#                       https://support.apple.com/kb/SP785
#   card reader         SumUp Air-type reader on a cradle (shape only): 84 x 84 x 23 mm
#                       https://sumup.ie/blog/the-air-your-latest-card-reader-our-best-design-so-far-a-learning-achievement/
#   kraft roll          Bulman A500-24-type paper dispenser/cutter: 61 cm roll, dia 15 cm
#                       https://www.webstaurantstore.com/bulman-a500-24-24-paper-cutter/43324PC.html
#   table               IKEA LERHAMN table, solid pine, antique-stain top / white-stain legs: 118 x 74 x 75 cm
#                       https://www.dimensions.com/element/ikea-lerhamn-table-rectangular
#   stool               IKEA BEKVAM step stool: W43 D39 H50 cm, step at 25 cm, hand-hold slot
#                       https://www.ikea.com/nl/en/p/bekvam-step-stool-aspen-10225589
#   bucket stand        3-tier florist bucket display stand: 150 x 56 x 70 cm (metal versions 100 x 50 x 110 cm)
#                       https://www.ebay.com/itm/198220516634
#   florist buckets     galvanised flower buckets with ring handles: dia 24 x H30, dia 18 x H31 cm
#                       https://www.waitrosegarden.com/product/_/galvanised-flower-bucket/classid.2000031500/
#   terracotta pots     classic Italian standard pot (dia 9-31.5 x H8.4-27.6 cm) and long tom (dia 17 x H23 cm)
#                       https://www.waitrosegarden.com/product/_/terracotta-standard-pot-white-5-sizes/classid.2000044659
#   glazed pots         IKEA CHIAFRON-type glazed pot: dia 27 x H26 cm
#                       https://www.ikea.com/es/en/p/chiafron-plant-pot-in-outdoor-green-10606150
#   hanging_plant       100 cm cotton macrame hangers, pot 15 cm, sits ~65 cm below the hook
#                       https://hortology.co.uk/products/plant-pot-macrame-hanger-with-bar-ivory
#   grow lights         Soltech Aspect-type pendant grow light (shape only): dia 9 x H16 cm
#                       https://soltech.com/products/aspect-plant-light
#   A-board (email)     small wooden-frame chalk A-board: 50 x 80 cm boards
#                       https://www.smartuk.net/blackboards-and-chalkboard-menu-signs/wooden-frame-chalkboard-a-board/
#   prints (frames)     IKEA RIBBA frame 40x50, black, white mount: outer 42 x 52 x 4 cm, opening 29 x 39 cm
#                       https://mgmt.ikea.gr/en/products/ribba-frame-40x50-cm/60378457
#   plant               Strelitzia nicolai, 180 cm, in a 40 cm terracotta pot (fan of paddle leaves)
#   floor plants        fiddle-leaf fig 140 cm in a 34 cm pot, olive standard 130 cm, monstera 80 cm in a 30 cm glazed pot
#                       https://patchplants.com/products/plants-fiddle-leaf-fig/
#   shell               painted London stock brick 215 x 65 mm, polished concrete with saw cuts, steel shop window
#                       https://www.gardenista.com/posts/cactus-succulents-prick-london-shoppers-diary

# =====================================================================
#  SETTINGS  -  change these lines, then run the script again
# =====================================================================
ROOM_NAME = "plant_shop"            # used for the output file names

ROOM_WIDTH = 4.4                    # metres, left to right
ROOM_DEPTH = 4.0                    # metres, front to back
WALL_HEIGHT = 2.9                   # metres

THEME = "morning"                   # pick one of the colour themes below
THEMES = {                          # any hex colour works; "main" is the room's hero colour (terracotta pots)
    # "morning": fresh 5600K daylight, painted white brick, three greens against terracotta and zinc.
    "morning": {
        "background": "#EEF2E6", "wall": "#F4F2EC", "wall_trim": "#8FAE9C", "floor": "#D6D3CB",
        "wood": "#C99A6B", "main": "#C2653D", "accent_1": "#E3C9A2", "accent_2": "#9DB8A8",
        "accent_3": "#E9B949", "cream": "#F7F3EA", "plant": "#4A7A45", "dark": "#2F3B35",
        "plant_light": "#86B07A", "plant_dark": "#2C4F31", "succulent": "#93B8A8", "flower": "#EE8E8C",
        "floor_alt": "#AFABA3", "steel": "#3A4541", "glass": "#E4F2EC", "soil": "#4B372B", "chalk": "#F4F1E6",
        "galv": "#B8BEBC", "brass": "#C8A15A", "glaze": "#3E6F74", "olive": "#8EA083", "kraft": "#C49B6C",
        "grow": "#FFF2E4", "rose": "#F6E7DA",
    },
    # "golden_hour": the same shop at the end of the day. The code switches the sun to a low, orange
    # 3100K beam and turns the barn lights up (see "golden_hour" under LIGHTS).
    "golden_hour": {
        "background": "#F4E3CF", "wall": "#F6ECDF", "wall_trim": "#A3AE8C", "floor": "#DCD0C0",
        "wood": "#C08A5A", "main": "#C2653D", "accent_1": "#E7C49A", "accent_2": "#AFC0A0",
        "accent_3": "#F0B84E", "cream": "#FFF7EC", "plant": "#52804A", "dark": "#33362C",
        "plant_light": "#97B96E", "plant_dark": "#2F5233", "succulent": "#9DBB9A", "flower": "#F09A8A",
        "floor_alt": "#B7A994", "steel": "#3E3F36", "glass": "#FFE0B5", "soil": "#4A3426", "chalk": "#FBF3E2",
        "galv": "#C4BFB5", "brass": "#CFA45A", "glaze": "#4F6E5C", "olive": "#97A07E", "kraft": "#C79A66",
        "grow": "#FFE8CC", "rose": "#FBE4D2",
    },
}

SUN_WARMTH = 5600                   # Kelvin: 2500 = sunset orange, 6500 = white daylight
SUN_STRENGTH = 4.5
LAMP_WARMTH = 2900                  # Kelvin of the two barn lights over the chalkboard
LAMP_STRENGTH = 18                  # Watts per barn light
WINDOW_GLOW = 1.0                   # brightness of the daylight coming in through the shop window
HANGING_POTS = 3                    # macrame pots on the rail in front of the window (1-4)
GROW_LIGHTS = True                  # warm LED grow bars on the shelving and pendants over the table
SEED = 7                            # change to shuffle which plants grow where

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

STYLE = "plant_shop"
KIT_VERSION = 2
W, D, H = ROOM_WIDTH, ROOM_DEPTH, WALL_HEIGHT
T = 0.15            # wall thickness
FLOOR_Z = 0.03      # top of the floor slab; furniture stands here
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


def mix_hex(a, b, t):
    """Blend two '#RRGGBB' colours (t = 0 -> a, 1 -> b)."""
    ca, cb = (int(a[i:i + 2], 16) for i in (1, 3, 5)), (int(b[i:i + 2], 16) for i in (1, 3, 5))
    return "#" + "".join(f"{round(x + (y - x) * t):02X}" for x, y in zip(ca, cb))


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


# Real-material shortcuts. Each surfaced material has its own roughness so it never shares a cache
# entry with a plain (un-textured) use of the same colour key.
def oak():          return surface(mat("wood", 0.5), "wood")                        # solid oak / pine
def pine():         return surface(mat("wood", 0.62), "wood", scale=0.8)            # rougher garden softwood
def galv(along="X"): return surface(mat("galv", 0.46, metal=0.6), "brushed", along=along)    # galvanised zinc
def terracotta():   return surface(mat("main", 0.86), "plaster", scale=2.0)         # matt unglazed clay
def kraft():        return surface(mat("kraft", 0.9), "paper")
def cotton():       return surface(mat("cream", 0.93), "knit", scale=2.5)           # macrame cord


def glazed(key):
    return surface(mat(key, 0.28), "ceramic")


def painted_brick():
    """Painted London stock brick: one coat of paint over bricks and mortar alike, so the kit's two-tone
    brick pattern is toned down to a faint brick-to-brick variation with slightly shadowed mortar joints."""
    m = surface(mat("wall", 0.9), "brick", along="X")
    br = next(n for n in m.node_tree.nodes if n.type == "TEX_BRICK")
    for name, v in (("Color1", 1.0), ("Color2", 0.97), ("Mortar", 0.82)):
        br.inputs[name].default_value = (v, v, v, 1)
    return m


def painted(key):
    """Painted timber: satin paint with the faint mottling of a brushed finish."""
    return surface(mat(key, 0.47), "plaster", scale=3.0)


# --------------------------------------------------------------------- mesh helpers
def _finish(o, material, bevel, coll, parent, smooth=True):
    o.data.materials.append(material)
    if bevel:
        mod = o.modifiers.new("Bevel", "BEVEL")
        mod.width = bevel
        mod.segments = 3
        mod.limit_method = "ANGLE"
        try:
            mod.harden_normals = True
        except AttributeError:
            pass
    if smooth:
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
    bevel = min(bevel, min(size) * 0.45)
    return _finish(o, material, bevel, coll, parent, smooth=bevel > 0)


def cyl(name, r, h, loc, material, r2=None, segs=32, bevel=0.003, rot=(0, 0, 0), coll=None, parent=None):
    """Cylinder (or tapered cylinder with r2 at the top). loc = centre."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=segs, radius1=r, radius2=r if r2 is None else r2, depth=h)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, min(bevel, r * 0.4, h * 0.4), coll, parent)


def ball(name, r, loc, material, scale=(1, 1, 1), coll=None, parent=None, segs=24):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=segs, v_segments=max(8, segs // 2), radius=r)
    o = _obj(name, bm)
    o.location, o.scale = loc, scale
    return _finish(o, material, 0, coll, parent)


def rod(name, a, b, r, material, parent=None, segs=10, r2=None):
    """Thin cylinder from point a to point b (cords, legs, brackets, spouts)."""
    a, b = Vector(a), Vector(b)
    o = cyl(name, r, (b - a).length, (a + b) / 2, material, r2=r2, segs=segs, bevel=0, parent=parent)
    o.rotation_euler = (b - a).to_track_quat("Z", "Y").to_euler()
    return o


def ring(name, r_ring, r_tube, loc, material, rot=(0, 0, 0), arc=1.0, parent=None, segs=24):
    """Donut (bucket rims, macrame rings, handles). arc=0.5 gives a half ring."""
    bm, rings, sides = bmesh.new(), [], 8
    n = segs if arc >= 1 else segs + 1
    for i in range(n):
        a = 2 * math.pi * arc * i / segs
        rings.append([bm.verts.new((math.cos(a) * (r_ring + r_tube * math.cos(b)),
                                    math.sin(a) * (r_ring + r_tube * math.cos(b)), r_tube * math.sin(b)))
                      for b in (2 * math.pi * j / sides for j in range(sides))])
    for i in range(n if arc >= 1 else n - 1):
        r1, r2 = rings[i], rings[(i + 1) % n]
        for j in range(sides):
            bm.faces.new((r1[j], r1[(j + 1) % sides], r2[(j + 1) % sides], r2[j]))
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, 0, None, parent)


def lathe(name, prof, loc, material, segs=32, rot=(0, 0, 0), scale=(1, 1, 1), parent=None):
    """Revolve a list of (radius, z) points around Z: pots, buckets, bins, lamp shades.
    Points with radius 0 close the shape (a pot's base, a shade's top)."""
    bm, rings = bmesh.new(), []
    for r, z in prof:
        if r <= 1e-6:
            rings.append([bm.verts.new((0, 0, z))])
        else:
            rings.append([bm.verts.new((r * math.cos(2 * math.pi * i / segs), r * math.sin(2 * math.pi * i / segs), z))
                          for i in range(segs)])
    for a, b in zip(rings, rings[1:]):
        if len(a) == 1 and len(b) == 1:
            continue
        for i in range(segs):
            j = (i + 1) % segs
            if len(a) == 1:
                bm.faces.new((a[0], b[j], b[i]))
            elif len(b) == 1:
                bm.faces.new((a[i], a[j], b[0]))
            else:
                bm.faces.new((a[i], a[j], b[j], b[i]))
    o = _obj(name, bm)
    o.location, o.rotation_euler, o.scale = loc, rot, scale
    return _finish(o, material, 0, None, parent)


def prism(name, pts, depth, loc, material, rot=(0, 0, 0), parent=None, bevel=0.003):
    """Flat board cut to an outline of (x, z) points, `depth` thick along Y (side panels, brackets)."""
    bm = bmesh.new()
    front = [bm.verts.new((x, -depth / 2, z)) for x, z in pts]
    back = [bm.verts.new((x, depth / 2, z)) for x, z in pts]
    bm.faces.new(front)
    bm.faces.new(list(reversed(back)))
    for i in range(len(pts)):
        j = (i + 1) % len(pts)
        bm.faces.new((front[i], front[j], back[j], back[i]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, bevel, None, parent, smooth=bevel > 0)


def empty(name, loc, rot=(0, 0, 0), parent=None):
    """Invisible handle; build things in its local space (x = along, -y = out of the wall)."""
    e = bpy.data.objects.new(name, None)
    e.empty_display_size = 0.15
    e.location, e.rotation_euler = loc, rot
    COL_ROOM.objects.link(e)
    e.parent = parent
    return e


def label(name, body, size, loc, material, rot=(R(90), 0, 0), align="CENTER", parent=None, depth=0.004):
    """Plain 3D text that is NOT a hook (chalk headings, doodles)."""
    cu = bpy.data.curves.new(name, "FONT")
    cu.body, cu.size, cu.align_x, cu.align_y = body, size, align, "CENTER"
    cu.extrude = depth
    o = bpy.data.objects.new(name, cu)
    o.location, o.rotation_euler = loc, rot
    o.data.materials.append(material)
    COL_ROOM.objects.link(o)
    o.parent = parent
    return o


def no_shadow(*objs):
    for o in objs:
        if hasattr(o, "visible_shadow"):
            o.visible_shadow = False


# =====================================================================
#  PLANT LIBRARY  -  real leaf outlines (split monstera, violin fig, heart pothos, paddle Strelitzia)
#  Each plant is ONE mesh (fast) with up to 3 greens. Build it around (0,0,0) = soil centre.
# =====================================================================
def greens():
    return [mat("plant_dark", 0.5), mat("plant", 0.45), mat("plant_light", 0.45)]


def vein():
    """Pale yellow-green of a midrib (fiddle-leaf fig, Strelitzia)."""
    return mat("vein", 0.5, color=mix_hex(COLORS["plant_light"], COLORS["cream"], 0.35))


def dirv(yaw):
    return Vector((-math.sin(yaw), math.cos(yaw), 0))


def spread(n, arc=None, jitter=0.25):
    """n leaf directions (yaw). arc = (from, to) compass degrees (0 = +X, 90 = +Y) keeps leaves off walls."""
    if arc is None:
        return [k * 2.39996 + random.uniform(-jitter, jitter) for k in range(n)]
    out = [R(arc[0] + (k + 0.5) / n * (arc[1] - arc[0])) - R(90) + random.uniform(-jitter, jitter) for k in range(n)]
    random.shuffle(out)
    return out


HEART = lambda u: math.sin(math.pi * min(1.0, 0.16 + 0.84 * u)) ** 0.6                      # pothos, philodendron
FIDDLE = lambda u: (u ** 0.55) * ((1 - u) ** 0.3) * 1.9 * (1 - 0.16 * math.exp(-((u - 0.4) / 0.12) ** 2))
PADDLE = lambda u: math.sin(math.pi * u) ** 0.55                                             # Strelitzia, banana
SWORD = lambda u: ((1 - u) ** 0.55) * min(1.0, 0.45 + u * 5)                                 # snake plant
ROUND = lambda u: math.sin(math.pi * u) ** 0.5                                               # eucalyptus coins


class Greens:
    """Collects leaves, stems and blobs into one mesh object."""

    def __init__(self, name):
        self.name, self.bm, self.mats = name, bmesh.new(), []

    def _mi(self, material):
        if material not in self.mats:
            self.mats.append(material)
        return self.mats.index(material)

    def _tag(self, verts, material):
        mi = self._mi(material)
        for f in {f for v in verts for f in v.link_faces}:
            f.material_index = mi

    def leaf_m(self, m, length, width, material, droop=0.25, fold=0.3, shape=0.8, nu=7, profile=None, notch=0.0,
               rib=None, wave=0.0):
        """One leaf along local +Y: an outline (profile), a folded midrib and a droop toward the tip.
        Five points across give a soft curved (not faceted) cross-section. notch pulls the base corners
        back into heart-shaped lobes, rib = material for a raised pale midrib, wave = wavy leaf margin."""
        rows, cols = [], (-1, -0.5, 0, 0.5, 1)
        for i in range(nu + 1):
            u = i / nu
            p = profile(u) if profile else math.sin(math.pi * u) ** shape
            half = 0.5 * width * p
            vs = (0,) if half < 1e-4 else cols
            rows.append([self.bm.verts.new(m @ Vector((v * half, u * length - notch * length * abs(v) * (1 - u) ** 3,
                                                       -droop * length * u * u + fold * half * abs(v) ** 1.6
                                                       + wave * half * abs(v) ** 2 * math.sin(u * 17 + v * 2))))
                         for v in vs])
        mi = self._mi(material)
        for a, b in zip(rows, rows[1:]):
            if len(a) == 1 and len(b) == 1:
                continue
            if len(a) == 1:
                faces = [(a[0], b[j + 1], b[j]) for j in range(len(b) - 1)]
            elif len(b) == 1:
                faces = [(a[j], a[j + 1], b[0]) for j in range(len(a) - 1)]
            else:
                faces = [(a[j], a[j + 1], b[j + 1], b[j]) for j in range(len(a) - 1)]
            for f in faces:
                self.bm.faces.new(f).material_index = mi
        if rib is not None:                                   # pale midrib standing just proud of the blade
            pts = [m @ Vector((0, u * length, -droop * length * u * u + 0.0015)) for u in (0, 0.2, 0.4, 0.6, 0.8, 0.93)]
            for k, (a, b) in enumerate(zip(pts, pts[1:])):
                self.stem(a, b, max(0.0015, width * 0.018) * (1 - 0.15 * k), rib, segs=5)

    def leaf(self, base, length, width, yaw, pitch, material, roll=0.0, **kw):
        """Leaf starting at base, pointing toward yaw, lifted pitch radians above horizontal."""
        m = (Matrix.Translation(Vector(base)) @ Matrix.Rotation(yaw, 4, "Z") @ Matrix.Rotation(pitch, 4, "X")
             @ Matrix.Rotation(roll, 4, "Y"))
        self.leaf_m(m, length, width, material, **kw)

    def split_leaf(self, m, length, width, material, lobes=6, droop=0.3, fold=0.08, solid=0.34, holes=True,
                   profile=HEART, notch=0.2, curl=0.25):
        """Monstera deliciosa leaf: a heart-shaped blade with deep slits cut in from the edge, swept toward the
        tip. The slits stop short of the midrib (a solid band of `solid` x half-width) and a row of small
        oval holes runs beside it. solid ~0 + holes=False gives Strelitzia's wind tears that reach the midrib.
        curl bends the blade edges down, so the leaf is a soft dome rather than a flat card."""
        cols = [-1, -0.74, -0.5, -solid, -solid * 0.45, 0, solid * 0.45, solid, 0.5, 0.74, 1]

        def P(s, v):
            out = max(0.0, abs(v) - solid) / (1 - solid)
            u = min(1.0, s + 0.12 * out * min(1, s / 0.15) * min(1, (1 - s) / 0.15))   # slits sweep forward
            half = 0.5 * width * profile(u)
            y = u * length - notch * length * abs(v) * (1 - u) ** 3
            z = -droop * length * u * u + fold * half * abs(v) - curl * half * v * v
            return Vector((v * half, y, z)), half

        L, g = 0.78 / lobes, 0.022                                     # lobe length and slit width (fractions)
        rows, gaps, hole_rows = {0.0, 0.04, 0.88, 0.95, 1.0}, {-1: [], 1: []}, {-1: [], 1: []}
        for side, off in ((-1, 0.0), (1, 0.45)):                       # the two halves are offset, like a real leaf
            for k in range(lobes):
                s0 = 0.07 + (k + off) * L
                s1 = min(0.86, s0 + L)
                rows.update((s0, s1 - g, s1, s0 + L * 0.5))
                if s1 < 0.86:
                    gaps[side].append((s1 - g - 1e-6, s1 - 1e-6))
                if holes and 0 < k < lobes - 1:
                    rows.update((s0 + L * 0.15, s0 + L * 0.42))
                    hole_rows[side].append((s0 + L * 0.15 - 1e-6, s0 + L * 0.42 - 1e-6))
        rows = sorted(rows)
        inside = lambda s, spans: any(a <= s < b for a, b in spans)
        grid = []
        for s in rows:
            pts = [P(s, v) for v in cols]
            if pts[0][1] < 1e-4:
                grid.append([self.bm.verts.new(m @ pts[len(cols) // 2][0])])
            else:
                grid.append([self.bm.verts.new(m @ p) for p, _ in pts])
        mi = self._mi(material)
        for i, (a, b) in enumerate(zip(grid, grid[1:])):
            s_key = rows[i]
            if len(a) == 1 or len(b) == 1:                             # pointed base or tip
                for j in range(len(cols) - 1):
                    f = (a[0], b[j + 1], b[j]) if len(a) == 1 else (a[j], a[j + 1], b[0])
                    if len(set(f)) == 3:
                        self.bm.faces.new(f).material_index = mi
                continue
            for j in range(len(cols) - 1):
                vm = (cols[j] + cols[j + 1]) / 2
                side = -1 if vm < 0 else 1
                if abs(vm) > solid and inside(s_key, gaps[side]):
                    continue                                           # a slit
                if solid * 0.45 < abs(vm) < solid and inside(s_key, hole_rows[side]):
                    continue                                           # a fenestration hole beside the midrib
                self.bm.faces.new((a[j], a[j + 1], b[j + 1], b[j])).material_index = mi

    def stem(self, a, b, r, material, r2=None, segs=8):
        a, b = Vector(a), Vector(b)
        v = b - a
        m = Matrix.Translation((a + b) / 2) @ v.to_track_quat("Z", "Y").to_matrix().to_4x4()
        ret = bmesh.ops.create_cone(self.bm, cap_ends=True, segments=segs, radius1=r,
                                    radius2=r if r2 is None else r2, depth=max(v.length, 1e-4), matrix=m)
        self._tag(ret["verts"], material)

    def blob(self, center, r, material, scale=(1, 1, 1), segs=12):
        m = Matrix.Translation(Vector(center)) @ Matrix.Diagonal((*scale, 1))
        ret = bmesh.ops.create_uvsphere(self.bm, u_segments=segs, v_segments=max(6, segs * 2 // 3), radius=r, matrix=m)
        self._tag(ret["verts"], material)

    def ribbed(self, base, r, h, material, ribs=8, depth=0.12, rows=12, prof=None):
        """Ribbed cactus body (column or barrel): radius r, height h, `ribs` vertical ridges."""
        base, segs = Vector(base), ribs * 4
        prof = prof or (lambda t: (0.86 + 0.14 * min(1, t * 6)) * (1 if t < 1 - r / h else
                        math.sqrt(max(0.0, 1 - ((t - (1 - r / h)) / (r / h)) ** 2))))
        rings = []
        for i in range(rows + 1):
            t = i / rows
            rr = r * prof(t)
            rings.append([self.bm.verts.new(base + Vector((math.cos(a) * rr * (1 - depth + depth * math.cos(ribs * a) ** 2),
                                                           math.sin(a) * rr * (1 - depth + depth * math.cos(ribs * a) ** 2),
                                                           h * t)))
                          for a in (2 * math.pi * j / segs for j in range(segs))])
        top = self.bm.verts.new(base + Vector((0, 0, h)))
        mi = self._mi(material)
        for a, b in zip(rings, rings[1:]):
            for j in range(segs):
                self.bm.faces.new((a[j], a[(j + 1) % segs], b[(j + 1) % segs], b[j])).material_index = mi
        for j in range(segs):
            self.bm.faces.new((rings[-1][j], rings[-1][(j + 1) % segs], top)).material_index = mi

    def build(self, parent=None, loc=(0, 0, 0)):
        o = _obj(self.name, self.bm)
        for m in self.mats:
            o.data.materials.append(m)
        o.data.polygons.foreach_set("use_smooth", [True] * len(o.data.polygons))
        o.location = loc
        COL_ROOM.objects.link(o)
        o.parent = parent
        return o


def sp_bird_of_paradise(g, size, r, arc=None):
    """Strelitzia nicolai: two clumps of long upright petioles, each fanned out roughly in one plane and
    ending in a long paddle leaf; the older outer leaves lean out, droop and are often split."""
    G = greens()
    fan = R(((arc[0] + arc[1]) / 2) if arc else random.uniform(0, 180))          # direction the fan spreads along
    F, N = Vector((math.cos(fan), math.sin(fan), 0)), Vector((-math.sin(fan), math.cos(fan), 0))
    for c, (off, n) in enumerate(((-0.07, 6), (0.08, 5))):
        base = F * off + N * random.uniform(-0.03, 0.03)
        leans = [R(random.uniform(48, 88)) for _ in range(n)]
        for k, lean in enumerate(leans):
            side = -1 if (k + c) % 2 else 1
            d = (F * side + N * random.uniform(-0.35, 0.35)).normalized()
            pl = size * random.uniform(0.32, 0.55) * (0.7 + 0.3 * math.sin(lean))
            top = base + (d * math.cos(lean) + Vector((0, 0, math.sin(lean)))) * pl
            g.stem(base, top, 0.013, G[0], r2=0.008)
            yaw = math.atan2(-d.x, d.y)
            m = (Matrix.Translation(top) @ Matrix.Rotation(yaw, 4, "Z") @ Matrix.Rotation(lean - R(random.uniform(6, 22)), 4, "X")
                 @ Matrix.Rotation(R(random.uniform(60, 95)) * side, 4, "Y"))
            L, Wd = size * random.uniform(0.3, 0.4), size * random.uniform(0.11, 0.14)
            if lean < R(62):                                              # old leaves tear along their veins
                g.split_leaf(m, L, Wd, G[(k + c) % 2], lobes=4, droop=0.12, fold=0.05, solid=0.04, holes=False,
                             profile=PADDLE, notch=0.0, curl=0.12)
            else:
                g.leaf_m(m, L, Wd, G[(k + c) % 2], droop=0.1, fold=0.2, profile=PADDLE, nu=8, rib=vein())
        g.stem(base - Vector((0, 0, 0.01)), base + Vector((0, 0, 0.2)), 0.03, G[0], r2=0.014, segs=12)  # leaf sheaths


def sp_monstera(g, size, r, arc=None):
    """Monstera deliciosa: arching petioles holding big split heart-shaped leaves."""
    G = greens()
    for k, yaw in enumerate(spread(8, arc)):
        d, reach = dirv(yaw), size * random.uniform(0.2, 0.4)
        top = Vector((0, 0, size * random.uniform(0.38, 0.8))) + d * reach
        mid = d * reach * 0.3 + Vector((0, 0, top.z * 0.72))           # petioles rise steeply, then arch out
        g.stem((0, 0, 0), mid, 0.008, G[2], r2=0.006)
        g.stem(mid, top, 0.006, G[2], r2=0.005)
        m = (Matrix.Translation(top) @ Matrix.Rotation(yaw + random.uniform(-0.3, 0.3), 4, "Z")
             @ Matrix.Rotation(R(random.uniform(-32, -8)), 4, "X") @ Matrix.Rotation(random.uniform(-0.35, 0.35), 4, "Y"))
        L = size * random.uniform(0.36, 0.46)                           # adult leaves are about as wide as long
        g.split_leaf(m, L, L * random.uniform(0.9, 1.0), G[k % 2], lobes=5 + k % 3, droop=0.3, fold=0.1)


def sp_snake(g, size, r, arc=None):
    """Sansevieria: stiff upright sword leaves, dark and mid green."""
    G = greens()
    for k, yaw in enumerate(spread(10, arc, jitter=0.6)):
        g.leaf(dirv(yaw) * random.uniform(0.0, r * 0.45), size * random.uniform(0.6, 1.0), size * 0.13, yaw,
               R(random.uniform(78, 89)), G[0] if k % 3 else G[1], droop=0.02, fold=0.45, profile=SWORD, nu=6)


def sp_pothos(g, size, r, arc=None):
    """Golden pothos: heart-shaped leaves on vines that spill over the pot rim (size = how far they hang)."""
    G = greens()
    for yaw in spread(6, arc, jitter=0.4):
        d = dirv(yaw)
        prev = None
        steps = 7
        for s in range(steps + 1):
            t = s / steps
            p = d * (r * (0.5 + 0.7 * min(1.0, t * 3)) + 0.03 * t) + Vector((0, 0, 0.04 - size * max(0.0, t - 0.15) ** 1.2))
            if prev is not None:
                g.stem(prev, p, 0.003, G[2], segs=5)
            g.leaf(p, random.uniform(0.06, 0.08), 0.055, yaw + random.uniform(-1.2, 1.2), R(random.uniform(-25, 30)),
                   random.choice(G[1:]), droop=0.2, fold=0.15, profile=HEART, notch=0.12, nu=5)
            prev = p
    for yaw in spread(5):
        g.leaf((0, 0, 0.01), 0.085, 0.065, yaw, R(45), G[1], droop=0.3, fold=0.2, profile=HEART, notch=0.12, nu=5)


def sp_fern(g, size, r, arc=None):
    """Boston fern: arching fronds made of many small leaflets."""
    G = greens()
    for k, yaw in enumerate(spread(9, arc)):
        d, lift, L = dirv(yaw), random.uniform(0.5, 1.0), size * random.uniform(0.8, 1.0)
        prev, npts = None, 8
        for i in range(npts + 1):
            t = i / npts
            p = d * L * t * 0.85 + Vector((0, 0, L * (lift * t - (lift + 0.2) * t * t)))
            if prev is not None:
                g.stem(prev, p, 0.003, G[2], segs=5)
            if 0 < i < npts:
                ll = L * 0.24 * (1 - t * 0.6)
                for side in (-1, 1):
                    g.leaf(p, ll, ll * 0.3, yaw + side * R(70), R(15 - 30 * t), G[(k + i) % 2 + 1],
                           droop=0.25, fold=0.2, nu=4)
            prev = p


def sp_rosette(g, size, r, arc=None):
    """Echeveria succulent: rings of fat leaves, the inner ones more upright."""
    m = mat("succulent", 0.45)
    for n, f, pitch in ((9, 1.0, 18), (7, 0.75, 38), (6, 0.5, 58), (4, 0.3, 76)):
        off = random.uniform(0, 1)
        for k in range(n):
            g.leaf((0, 0, 0.004), size * f, size * f * 0.75, (k + off) * 2 * math.pi / n, R(pitch), m,
                   droop=-0.15, fold=0.7, shape=0.7, nu=5)


def sp_cactus(g, size, r, arc=None):
    """Column cactus (Cereus): an 8-ribbed column with one ribbed arm."""
    m = mat("plant", 0.55)
    rr = min(r * 0.55, size * 0.16)
    g.ribbed((0, 0, -0.01), rr, size, m, ribs=8)
    side = random.choice((-1, 1))
    ax, az = side * rr * 2.1, size * 0.42
    g.stem((side * rr * 0.6, 0, az - rr * 0.6), (ax, 0, az - rr * 0.6), rr * 0.5, m, segs=10)
    g.ribbed((ax, 0, az - rr * 0.9), rr * 0.62, size * 0.35, m, ribs=7)


def sp_barrel(g, size, r, arc=None):
    """Golden barrel cactus: a squat ribbed sphere."""
    g.ribbed((0, 0, -0.01), size * 0.5, size * 0.85, mat("plant", 0.55), ribs=14, depth=0.1, rows=10,
             prof=lambda t: math.sin(math.pi * (0.22 + 0.78 * t)) ** 0.55)
    g.blob((0, 0, size * 0.83), size * 0.1, mat("accent_3", 0.6), scale=(1, 1, 0.4))     # woolly yellow crown


def sp_fiddle(g, size, r, arc=None):
    """Fiddle-leaf fig standard: a slim trunk with big violin-shaped leaves on the top 60 %."""
    G = greens()
    top = Vector((random.uniform(-0.03, 0.03), random.uniform(-0.03, 0.03), size * 0.95))
    g.stem((0, 0, 0), top, 0.016, mat("bark", 0.85, color=mix_hex(COLORS["soil"], COLORS["galv"], 0.3)), r2=0.009)
    n = 22
    for k, yaw in enumerate(spread(n, arc)):
        t = 0.4 + 0.6 * (k / (n - 1)) ** 0.8
        g.leaf(top * t, size * (0.24 - 0.05 * t), size * (0.17 - 0.03 * t), yaw, R(random.uniform(10, 40) + 25 * t),
               G[k % 2], droop=0.25, fold=0.18, profile=FIDDLE, roll=random.uniform(-0.4, 0.4), nu=8,
               rib=vein(), wave=0.12)


def sp_olive(g, size, r, arc=None):
    """Olive standard: a gnarled grey trunk and a dense round crown of narrow grey-green leaves."""
    bark = mat("bark", 0.85, color=mix_hex(COLORS["soil"], COLORS["galv"], 0.3))
    leafs = [mat("olive", 0.6), mat("olive_lt", 0.6, color=mix_hex(COLORS["olive"], COLORS["cream"], 0.35)),
             mat("olive_dk", 0.6, color=mix_hex(COLORS["olive"], COLORS["plant_dark"], 0.4))]
    pts = [Vector((0, 0, 0))]
    for k in range(1, 5):
        pts.append(Vector((random.uniform(-0.035, 0.035), random.uniform(-0.035, 0.035), size * 0.6 * k / 4)))
    for a, b in zip(pts, pts[1:]):
        g.stem(a, b, 0.024, bark)
        g.blob(b, 0.026, bark, segs=8)                                        # knobbly joints
    crown, cr = Vector((0, 0, size * 0.8)), size * 0.21
    for k, yaw in enumerate(spread(9)):
        tip = crown + dirv(yaw) * cr * 0.85 + Vector((0, 0, random.uniform(-0.6, 0.8) * cr))
        g.stem(pts[-1], tip, 0.01, bark, r2=0.004)
        for j in range(72):                                              # dense clipped crown of narrow leaves
            p = pts[-1].lerp(tip, random.uniform(0.5, 1.0)) + Vector([random.uniform(-1, 1) * cr * 0.34 for _ in range(3)])
            g.leaf(p, 0.065, 0.02, random.uniform(0, 6.28), R(random.uniform(-40, 60)), leafs[j % 3],
                   droop=0.1, fold=0.3, nu=3)


def sp_flowers(g, size, r, arc=None):
    """Kalanchoe / florist pot plant: a leafy bush with clusters of small blooms."""
    G, fm = greens(), mat("flower", 0.6)
    for yaw in spread(10, arc):
        g.leaf((0, 0, 0), size * 0.5, size * 0.25, yaw, R(random.uniform(25, 60)), G[1], droop=0.3, fold=0.3)
    for yaw in spread(6, arc, jitter=0.5):
        top = dirv(yaw) * size * random.uniform(0.05, 0.25) + Vector((0, 0, size * random.uniform(0.55, 0.9)))
        g.stem((0, 0, 0), top, 0.003, G[2], segs=5)
        for _ in range(4):
            g.blob(top + Vector([random.uniform(-0.015, 0.015) for _ in range(3)]), size * 0.035, fm, segs=8)


SPECIES = {"fiddle": sp_fiddle, "bird": sp_bird_of_paradise, "monstera": sp_monstera, "snake": sp_snake,
           "pothos": sp_pothos, "fern": sp_fern, "rosette": sp_rosette, "cactus": sp_cactus, "barrel": sp_barrel,
           "olive": sp_olive, "flowers": sp_flowers}
SMALL_SPECIES = ["fern", "pothos", "rosette", "cactus", "barrel", "snake", "flowers", "monstera"]
POT_KEYS = ["main", "main", "main", "cream", "glaze"]      # terracotta most often, then white and glazed


def pot(name, loc, d, h, key="main", parent=None, style=None):
    """A real pot from a revolved profile; d = top outside diameter. Returns the soil centre.
    style: 'standard' (Italian terracotta, rim band), 'glazed' (round shoulder), 'nursery' (thin plastic)."""
    style = style or ("standard" if key == "main" else "glazed")
    Rr, (x, y, z) = d / 2, loc
    if style == "standard":
        band = max(0.016, h * 0.16)
        prof = [(0, 0), (Rr * 0.7, 0), (Rr * 0.72, 0.005), (Rr * 0.9, h - band), (Rr, h - band + 0.004), (Rr, h - 0.004),
                (Rr * 0.98, h), (Rr * 0.87, h), (Rr * 0.85, h - band * 0.7), (Rr * 0.8, h - band * 1.8)]
        material = terracotta() if key == "main" else glazed(key)
    elif style == "nursery":
        prof = [(0, 0), (Rr * 0.76, 0), (Rr * 0.95, h - 0.01), (Rr, h - 0.008), (Rr, h), (Rr * 0.95, h), (Rr * 0.93, h - 0.03)]
        material = mat("dark", 0.55)
    else:
        prof = [(0, 0), (Rr * 0.6, 0), (Rr * 0.66, 0.01), (Rr * 0.93, h * 0.35), (Rr, h * 0.72), (Rr * 0.97, h - 0.005),
                (Rr * 0.92, h), (Rr * 0.86, h), (Rr * 0.84, h - 0.03)]
        material = glazed(key)
    lathe(f"{name}_Pot", prof, (x, y, z), material, segs=28, parent=parent)
    soil_z = h - max(0.012, h * 0.08)
    cyl(f"{name}_Soil", Rr * 0.85, 0.008, (x, y, z + soil_z - 0.004), mat("soil", 0.95), segs=20, bevel=0, parent=parent)
    return Vector((x, y, z + soil_z))


def potted(name, species, loc, d, h, size, key="main", parent=None, arc=None, style=None):
    """A pot plus one plant from the library. loc = bottom centre of the pot."""
    top = pot(name, loc, d, h, key, parent, style)
    g = Greens(f"{name}_Plant")
    SPECIES[species](g, size, d / 2, arc)
    return g.build(parent, top)


# --------------------------------------------------------------------- cut flowers (florist buckets)
def cut_stems(g, kind, n, length, spread_r):
    """A bunch of cut stems rising from (0,0,0): tulips, roses, sunflowers, eucalyptus or gypsophila."""
    G = greens()
    for k in range(n):
        a = k * 2.39996 + random.uniform(-0.3, 0.3)
        lean = Vector((math.cos(a), math.sin(a), 0)) * spread_r * random.uniform(0.4, 1.0)
        top = lean * 2.2 + Vector((0, 0, length * random.uniform(0.85, 1.05)))
        base = lean * 0.3
        if kind == "eucalyptus":
            g.stem(base, top, 0.0025, mat("olive", 0.6), segs=5)
            for j in range(9):
                p = base.lerp(top, 0.3 + 0.7 * j / 9)
                for s in (0, math.pi):
                    g.leaf(p, 0.034, 0.034, a + s + j * 0.6, R(10), mat("succulent", 0.6), droop=0.1, fold=0.1,
                           profile=ROUND, nu=4)
            continue
        g.stem(base, top, 0.003, G[1], segs=5)
        if kind == "tulip":
            for j in range(5):
                g.leaf(top - Vector((0, 0, 0.012)), 0.05, 0.034, j * 1.2566 + a, R(78), mat("flower", 0.5),
                       droop=-0.12, fold=-0.25, nu=4)
            if k % 2 == 0:
                g.leaf(base + (top - base) * 0.55, length * 0.3, 0.03, a, R(55), G[2], droop=0.35, fold=0.4, nu=4)
        elif kind == "rose":                    # a tight cup of petals round a bud, on a green calyx
            rm = mat("rose", 0.6)
            g.blob(top + Vector((0, 0, 0.006)), 0.014, rm, scale=(1, 1, 1.25), segs=10)
            for ring_k, (n_p, pl, pitch) in enumerate(((5, 0.026, 72), (5, 0.03, 52))):
                for j in range(n_p):
                    g.leaf(top - Vector((0, 0, 0.004 + 0.004 * ring_k)), pl, 0.03, j * 1.2566 + a + ring_k * 0.63,
                           R(pitch), rm, droop=-0.45, fold=0.5, nu=4)
            for j in range(5):
                g.leaf(top - Vector((0, 0, 0.01)), 0.022, 0.008, j * 1.2566 + a + 0.3, R(-35), G[0], droop=0.1,
                       fold=0.2, nu=3)
        elif kind == "sunflower":
            nrm = (top - base).normalized().lerp(Vector((math.cos(a), math.sin(a), 0)), 0.55).normalized()
            g.stem(top, top + nrm * 0.014, 0.038, mat("soil", 0.8), segs=14)
            frame = Matrix.Translation(top + nrm * 0.007) @ nrm.to_track_quat("Z", "Y").to_matrix().to_4x4()
            for j in range(14):
                g.leaf_m(frame @ Matrix.Rotation(j * 2 * math.pi / 14, 4, "Z") @ Matrix.Translation((0, 0.034, 0)),
                         0.045, 0.018, mat("accent_3", 0.55), droop=0.05, fold=0.1, nu=3)
        elif kind == "gyp":
            for j in range(10):
                g.blob(top + Vector([random.uniform(-0.05, 0.05) for _ in range(2)] + [random.uniform(-0.04, 0.02)]),
                       0.008, mat("cream", 0.7), segs=6)


def flower_bucket(name, loc, d, h, kind, n, length, parent=None):
    """Galvanised florist bucket: tapered zinc body, pressed bands, rolled rim, ring handles, cut stems."""
    x, y, z = loc
    Rr, wall = d / 2, 0.0025
    rb = Rr * 0.74                                                      # base is about 3/4 of the rim
    r_at = lambda t: rb + (Rr - rb) * t                                 # one smooth straight taper
    prof = [(0, 0.002), (rb - 0.006, 0.002), (rb - 0.002, 0.0), (rb, 0.006), (r_at(1) , h - 0.002),
            (r_at(1) - wall, h - 0.002), (rb - wall, 0.012), (0, 0.012)]
    lathe(f"{name}_Bucket", prof, (x, y, z), galv("Z"), segs=36, parent=parent)
    ring(f"{name}_Rim", Rr + 0.001, 0.0045, (x, y, z + h - 0.003), galv("Z"), parent=parent, segs=36)   # rolled rim
    for t in (0.1, 0.17):                                              # two pressed beads low on the body
        ring(f"{name}_Bead", r_at(t) + 0.0005, 0.002, (x, y, z + h * t), galv("Z"), parent=parent, segs=36)
    cyl(f"{name}_Water", r_at(0.55) - wall - 0.001, 0.003, (x, y, z + h * 0.55), mat("water", 0.05,
        color=mix_hex(COLORS["galv"], COLORS["dark"], 0.55)), segs=32, bevel=0, parent=parent)
    for s in (-1, 1):                                                  # riveted lugs with drop-ring handles
        rx = x + s * (r_at(0.8) + 0.004)
        box(f"{name}_Lug", (0.008, 0.02, 0.026), (rx, y, z + h * 0.8), galv("Z"), bevel=0.002, parent=parent)
        ring(f"{name}_Handle", 0.02, 0.0028, (rx + s * 0.004, y, z + h * 0.8 - 0.018), galv("Z"),
             rot=(0, R(90) - s * R(25), 0), parent=parent)
    g = Greens(f"{name}_Stems")
    cut_stems(g, kind, n, length, Rr * 0.5)
    return g.build(parent, (x, y, z + h * 0.6))


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
#  ROOM SHELL  -  polished concrete floor, painted London stock brick, steel shop window
# =====================================================================
box("Floor_Base", (W + T, D + T, 0.2), ((W - T) / 2, (D + T) / 2, -0.1), mat("wall_trim", 0.7), bevel=0.04)
box("Floor_Concrete", (W, D, FLOOR_Z), (W / 2, D / 2, FLOOR_Z / 2), surface(mat("floor", 0.32), "concrete"),
    bevel=0.004)
joint = mat("floor_alt", 0.8)
for x in (1.1, 2.2, 3.3):                       # saw-cut control joints every 1.1 m
    box("Floor_SawCut", (0.006, D, 0.001), (x, D / 2, FLOOR_Z + 0.0003), joint, bevel=0)
for y in (1.0, 2.0, 3.0):
    box("Floor_SawCut", (W, 0.006, 0.001), (W / 2, y, FLOOR_Z + 0.0003), joint, bevel=0)

WIN_X = (0.95, 3.45)                # shop window, from left to right
WIN_Z = (0.92, 2.45)
wx, wz = sum(WIN_X) / 2, sum(WIN_Z) / 2
ww, wh = WIN_X[1] - WIN_X[0], WIN_Z[1] - WIN_Z[0]
back = box("Wall_Back", (W + T, T, H), ((W - T) / 2, D + T / 2, H / 2),
           painted_brick(), bevel=0.0)
cutter = box("Window_Cutter", (ww, T * 3, wh), (wx, D + T / 2, wz), mat("wall"), bevel=0.0)
cutter.hide_render = cutter.hide_viewport = True
boolean = back.modifiers.new("Window", "BOOLEAN")
boolean.operation, boolean.object = "DIFFERENCE", cutter
# The left wall is built like the back wall and turned 90 degrees, so the brick courses run along it.
box("Wall_Left", (D + T, T, H), (-T / 2, (D + T) / 2, H / 2), painted_brick(), bevel=0.0, rot=(0, 0, R(90)))

# Sage cap on top of the walls (the kit's "diorama" edge) and painted timber skirting with a top bevel.
trim = mat("wall_trim", 0.5)
box("Trim_Top_Back", (W + T + 0.06, T + 0.08, 0.12), ((W - T) / 2, D + T / 2, H + 0.06), trim, bevel=0.03)
box("Trim_Top_Left", (T + 0.08, D + T + 0.06, 0.12), (-T / 2, (D + T) / 2 - 0.03, H + 0.06), trim, bevel=0.03)
skirt = painted("wall_trim")
box("Skirting_Back", (W, 0.018, 0.12), (W / 2, D - 0.009, FLOOR_Z + 0.06), skirt, bevel=0.004)
box("Skirting_Left", (0.018, D, 0.12), (0.009, D / 2, FLOOR_Z + 0.06), skirt, bevel=0.004)

# Steel shop window (Crittall style): slim outer frame, 5 x 3 panes with 25 mm glazing bars, timber window board.
steel = mat("steel", 0.4, metal=0.5)
for nm, size, loc in [
    ("Top", (ww + 0.1, 0.06, 0.05), (wx, D + 0.03, WIN_Z[1] + 0.025)),
    ("Bottom", (ww + 0.1, 0.06, 0.05), (wx, D + 0.03, WIN_Z[0] - 0.025)),
    ("Left", (0.05, 0.06, wh), (WIN_X[0] - 0.025, D + 0.03, wz)),
    ("Right", (0.05, 0.06, wh), (WIN_X[1] + 0.025, D + 0.03, wz)),
]:
    box(f"Window_Frame_{nm}", size, loc, steel, bevel=0.004)
for k in range(1, 5):
    box("Window_Bar_V", (0.025, 0.04, wh), (WIN_X[0] + k * ww / 5, D + 0.04, wz), steel, bevel=0.003)
for k in (1, 2):
    box("Window_Bar_H", (ww, 0.04, 0.025), (wx, D + 0.04, WIN_Z[0] + k * wh / 3), steel, bevel=0.003)
box("Window_Handle", (0.015, 0.03, 0.09), (WIN_X[0] + 3 * ww / 5 + 0.03, D + 0.01, WIN_Z[0] + wh / 3 + 0.12),
    mat("dark", 0.3, metal=0.8), bevel=0.004)
box("Window_Board", (ww + 0.16, 0.2, 0.028), (wx, D - 0.05, WIN_Z[0] - 0.064), painted("cream"), bevel=0.005)
for nm, size, loc in [                                   # plastered reveal lining the opening (no brick ends)
    ("Head", (ww, T, 0.012), (wx, D + T / 2, WIN_Z[1] - 0.006)),
    ("Left", (0.012, T, wh), (WIN_X[0] + 0.006, D + T / 2, wz)),
    ("Right", (0.012, T, wh), (WIN_X[1] - 0.006, D + T / 2, wz)),
    ("Sill", (ww, T, 0.012), (wx, D + T / 2, WIN_Z[0] + 0.006)),
]:
    box(f"Window_Reveal_{nm}", size, loc, surface(mat("wall", 0.85), "plaster"), bevel=0)
glass_m = mat("glass", 0.04)                                # clear float glass: mostly see-through, a faint sheen
_set(_principled(glass_m), ["Alpha"], 0.12)
_set(_principled(glass_m), ["Specular IOR Level", "Specular"], 0.8)
if hasattr(glass_m, "surface_render_method"):
    glass_m.surface_render_method = "BLENDED"
elif hasattr(glass_m, "blend_method"):
    glass_m.blend_method = "BLEND"
glass = box("Window_Glass", (ww, 0.006, wh), (wx, D + 0.065, wz), glass_m, bevel=0)
no_shadow(glass)


# With CAMERA_TURN = 45 a point's left-right place in the picture is x + y, so ground cut to the window's
# x + y range (plus a margin) shows only through the glass and never past the end of the back wall.
SEEN = (WIN_X[0] + D - 0.3, WIN_X[1] + D + 0.3)


def outside_quad(name, y0, y1, material, z=0.0):
    """A strip of street between y0 and y1, cut on the diagonal to the SEEN range (see above)."""
    bm = bmesh.new()
    s0, s1 = SEEN
    vs = [bm.verts.new(v) for v in ((s0 - y0, y0, z), (s1 - y0, y0, z), (s1 - y1, y1, z), (s0 - y1, y1, z))]
    bm.faces.new(vs)
    o = _obj(name, bm)
    return _finish(o, material, 0, None, None, smooth=False)


# The street outside (seen only through the window): York-stone paving, a granite kerb, tarmac and a
# street tree in a tree pit with a cast-iron grille.
KERB_Y = D + 2.1
pave = surface(mat("paving", 0.85, color=mix_hex(COLORS["floor_alt"], COLORS["cream"], 0.35)), "square_tile",
               scale=1 / 6, along="Z")                              # 0.6 m slabs
outside_quad("Outside_Pavement", D + T, KERB_Y, pave, z=FLOOR_Z)
outside_quad("Outside_Kerb", KERB_Y, KERB_Y + 0.15, surface(mat("kerb", 0.8, color=COLORS["floor_alt"]), "concrete"),
             z=FLOOR_Z + 0.002)
outside_quad("Outside_Road", KERB_Y + 0.15, D + 3.2, surface(mat("tarmac", 0.9, color=mix_hex(COLORS["dark"],
             COLORS["floor_alt"], 0.35)), "concrete", scale=3), z=FLOOR_Z - 0.1)
tree_xy = Vector((1.0, D + 1.6))                                     # x + y inside SEEN, behind the glass
box("Outside_Tree_Grille", (0.7, 0.7, 0.02), (*tree_xy, FLOOR_Z + 0.01), mat("grille", 0.7, color=mix_hex(
    COLORS["steel"], COLORS["floor_alt"], 0.5)), bevel=0.004)
# The trunk stops at 1.4 m: only its foot shows through the window, and it never rises above the back wall.
cyl("Outside_Tree_Trunk", 0.11, 1.4, (*tree_xy, FLOOR_Z + 0.7), surface(mat("bark", 0.85, color=mix_hex(
    COLORS["olive"], COLORS["galv"], 0.4)), "concrete", scale=4), r2=0.1, segs=16, bevel=0)

# Light switch by the counter (standard 86 x 86 mm UK plate).
box("Switch_Plate", (0.01, 0.086, 0.086), (0.005, 1.62, 1.2), mat("cream", 0.35), bevel=0.003)
box("Switch_Rocker", (0.008, 0.02, 0.035), (0.012, 1.62, 1.2), mat("cream", 0.3), bevel=0.002)

# =====================================================================
#  FURNITURE SLOTS  (same names in every template)
#  size = (width, depth, height); front of the furniture faces local -Y
# =====================================================================
slot("shelf",         (0.6, 0.27, 1.4),   (3.95, D - 0.16), shape="shelf")               # HYLLIS, right of the window
slot("hanging_plant", (2.3, 0.3, 0.95),   (wx, D - 0.26), z=1.75, kind="hanging", shape="plant")
slot("plant",         (0.7, 0.7, 1.85),   (0.55, D - 0.55), shape="plant")               # Strelitzia in the corner
slot("workbench",     (1.03, 0.53, 0.9),  (0.285, 2.25), turn=90, shape="table")         # potting bench
slot("hero_prop",     (0.5, 0.2, 0.32),   (0.4, 2.46), z=FLOOR_Z + 0.9, turn=90, kind="surface", shape="box")
slot("stool",         (0.43, 0.39, 0.5),  (1.2, 2.8), turn=60, shape="stool")           # BEKVAM step stool
slot("counter",       (1.2, 0.6, 0.92),   (0.75, 0.85), turn=90, shape="counter")
slot("table",         (1.18, 0.74, 0.75), (2.5, 1.85), shape="table")                    # LERHAMN display table


# =====================================================================
#  PLACEHOLDER FURNITURE  (replaced when you add your own with add_furniture.py)
# =====================================================================
def build_shelf():
    """IKEA HYLLIS-style galvanised shelving: L-section posts, ribbed shelf trays with lips, grow bars."""
    root, w, d, h = furniture_root("shelf")
    zinc = galv("Z")
    for sx in (-1, 1):
        for sy in (-1, 1):
            x, y = sx * (w / 2 - 0.015), sy * (d / 2 - 0.015)
            box("Shelving_Post", (0.03, 0.003, h), (x, sy * (d / 2 - 0.0015), h / 2), zinc, bevel=0.001, parent=root)
            box("Shelving_Post", (0.003, 0.03, h), (sx * (w / 2 - 0.0015), y, h / 2), zinc, bevel=0.001, parent=root)
            cyl("Shelving_Foot", 0.012, 0.012, (x, y, 0.006), mat("dark", 0.6), segs=12, parent=root)
    shelf_z = [0.08, 0.52, 0.96, h - 0.015]
    flat = galv("X")
    for i, z in enumerate(shelf_z):
        box("Shelving_Shelf", (w - 0.006, d - 0.006, 0.003), (0, 0, z), flat, bevel=0.001, parent=root)
        for sy in (-1, 1):
            box("Shelving_Lip", (w, 0.003, 0.03), (0, sy * (d / 2 - 0.0015), z - 0.014), flat, bevel=0.001, parent=root)
            box("Shelving_Rib", (w - 0.08, 0.014, 0.004), (0, sy * 0.06, z + 0.003), flat, bevel=0.002, parent=root)
        for sx in (-1, 1):
            box("Shelving_Lip", (0.003, d, 0.03), (sx * (w / 2 - 0.0015), 0, z - 0.014), flat, bevel=0.001, parent=root)
        if GROW_LIGHTS and i > 0:                     # clip-on LED grow bar under the shelf above each level
            box("Grow_Bar_Housing", (w - 0.12, 0.026, 0.012), (0, -0.02, z - 0.024), mat("galv", 0.3, metal=0.9),
                bevel=0.003, parent=root)
            bar = box("Grow_Bar_LED", (w - 0.14, 0.018, 0.003), (0, -0.02, z - 0.031),
                      mat("grow", 0.4, emit=4.0), bevel=0, parent=root)
            no_shadow(bar)
            ld = bpy.data.lights.new("Light_Grow_Bar", "AREA")
            ld.energy, ld.color, ld.size = 4.0, kelvin(3500), 0.45
            lo = bpy.data.objects.new("Light_Grow_Bar", ld)
            lo.location, lo.parent = (0, -0.02, z - 0.04), root
            COL_LIGHT.objects.link(lo)
    for a, b in (((-1, 0.1), (1, 0.95)), ((1, 0.1), (-1, 0.95))):   # X-brace across the back
        rod("Shelving_Brace", (a[0] * (w / 2 - 0.02), d / 2 - 0.004, a[1]), (b[0] * (w / 2 - 0.02), d / 2 - 0.004, b[1]),
            0.003, zinc, parent=root, segs=6)
    # Stock: terracotta, glazed and black nursery pots of real sizes (9-20 cm).
    stock = [
        [("fern", 0.2, 0.17, 0.34, "main", "standard", -0.16), ("monstera", 0.18, 0.16, 0.36, "glaze", None, 0.15)],
        [("snake", 0.13, 0.12, 0.32, "main", "standard", -0.19), ("barrel", 0.12, 0.1, 0.11, "main", "standard", 0.0),
         ("cactus", 0.11, 0.1, 0.26, "cream", None, 0.18)],
        [("rosette", 0.1, 0.08, 0.07, "main", "standard", -0.2), ("flowers", 0.12, 0.11, 0.2, "dark", "nursery", -0.05),
         ("rosette", 0.09, 0.08, 0.06, "glaze", None, 0.09), ("cactus", 0.09, 0.09, 0.2, "main", "standard", 0.21)],
        [("pothos", 0.15, 0.13, 0.45, "main", "standard", -0.15), ("pothos", 0.14, 0.12, 0.4, "cream", None, 0.15)],
    ]
    for z, row in zip(shelf_z, stock):
        for sp, pd, ph, size, key, style, x in row:
            potted("Shelving_Pot", sp, (x, -0.01, z + 0.0015), pd, ph, size, key, parent=root, style=style,
                   arc=(-160, -20) if sp == "pothos" else None)


def build_hanging_plant():
    """Steel rail hung from the ceiling, with 100 cm cotton macrame hangers holding 15 cm pots."""
    root, w, d, h = furniture_root("hanging_plant")
    rail_z, cord = h - 0.05, cotton()
    rail_m = mat("steel", 0.35, metal=0.6)
    cyl("Rail", 0.014, w, (0, 0, rail_z), rail_m, segs=16, bevel=0, rot=(0, R(90), 0), parent=root)
    for x in (-w / 2 + 0.08, w / 2 - 0.08):                       # drop rods up to the ceiling joists
        rod("Rail_Drop", (x, 0, rail_z), (x, 0, H - SLOTS["hanging_plant"].location.z + h / 2), 0.008, rail_m,
            parent=root)
        cyl("Rail_Clamp", 0.02, 0.03, (x, 0, rail_z), rail_m, segs=12, parent=root)
    n = max(1, min(4, HANGING_POTS))
    for k in range(n):
        x = (k - (n - 1) / 2) * (w - 0.5) / max(1, n - 1) if n > 1 else 0
        top_z = rail_z - random.uniform(0.5, 0.62)                  # pot rim height
        pr, ph = 0.075, 0.13
        ring("Macrame_Ring", 0.028, 0.005, (x, 0, rail_z - 0.035), mat("wood", 0.5), rot=(R(90), 0, 0), parent=root)
        gather = Vector((x, 0, rail_z - 0.09))
        cyl("Macrame_Gather", 0.011, 0.035, gather, cord, segs=10, parent=root)
        bottom = Vector((x, 0, top_z - ph - 0.03))
        for c in range(4):                                          # four cord pairs: square knots, then a net
            a = c * math.pi / 2 + 0.6
            rim = Vector((x + math.cos(a) * pr * 1.04, math.sin(a) * pr * 1.04, top_z - 0.02))
            knot = gather.lerp(rim, 0.55)
            for s in (-0.012, 0.012):
                off = Vector((-math.sin(a) * s, math.cos(a) * s, 0))
                rod("Macrame_Cord", gather, knot + off, 0.0022, cord, parent=root, segs=5)
            for t in (0.0, 0.06, 0.12):                             # a run of square-knot bumps
                ball("Macrame_Knot", 0.008, knot + (rim - knot) * t, cord, parent=root, segs=8)
            for s in (-1, 1):                                       # each pair splits and meets its neighbour
                b_ = c * math.pi / 2 + 0.6 + s * math.pi / 4
                cross = Vector((x + math.cos(b_) * pr * 1.06, math.sin(b_) * pr * 1.06, top_z - ph * 0.5))
                rod("Macrame_Net", knot, cross, 0.0022, cord, parent=root, segs=5)
                rod("Macrame_Net", cross, bottom, 0.0022, cord, parent=root, segs=5)
        cyl("Macrame_Bottom_Knot", 0.012, 0.03, bottom, cord, segs=10, parent=root)
        for t in range(7):                                           # tassel
            a = t * 0.9
            rod("Macrame_Tassel", bottom, bottom + Vector((math.cos(a) * 0.012, math.sin(a) * 0.012, -0.13)),
                0.002, cord, parent=root, segs=4)
        species = ["pothos", "pothos", "fern", "pothos"][k]
        potted("Hanging", species, (x, 0, top_z - ph), pr * 2, ph, 0.6 if species == "pothos" else 0.3,
               ["cream", "main", "main", "glaze"][k], parent=root)


def build_plant():
    """Statement Strelitzia nicolai (bird of paradise) in a 40 cm terracotta pot."""
    root, w, d, h = furniture_root("plant")
    potted("Hero_Plant", "bird", (0, 0, 0), 0.4, 0.36, h * 0.92, "main", parent=root, arc=(45, 45))


def build_workbench():
    """Potting bench: fir frame, galvanised worktop tray with upstands, slatted back with tool hooks,
    narrow top shelf, slatted lower shelf with a galvanised soil bin and a compost bag."""
    root, w, d, h = furniture_root("workbench")
    fir, zinc = pine(), galv("X")
    for sx in (-1, 1):
        box("Bench_Leg_Front", (0.045, 0.045, h - 0.02), (sx * (w / 2 - 0.025), -(d / 2 - 0.025), (h - 0.02) / 2),
            fir, bevel=0.004, parent=root)
        box("Bench_Leg_Back", (0.045, 0.045, 1.591), (sx * (w / 2 - 0.025), d / 2 - 0.025, 0.7955), fir,
            bevel=0.004, parent=root)
        box("Bench_Apron_Side", (0.02, d - 0.09, 0.07), (sx * (w / 2 - 0.025), 0, h - 0.075), fir, bevel=0.003,
            parent=root)
        box("Bench_Rail_Side", (0.02, d - 0.09, 0.045), (sx * (w / 2 - 0.025), 0, 0.15), fir, bevel=0.003, parent=root)
    for sy in (-1, 1):
        box("Bench_Apron", (w - 0.09, 0.02, 0.07), (0, sy * (d / 2 - 0.025), h - 0.075), fir, bevel=0.003, parent=root)
    box("Bench_Board", (w, d, 0.018), (0, 0, h - 0.013), fir, bevel=0.003, parent=root)
    box("Bench_Tray", (w + 0.004, d + 0.004, 0.004), (0, 0, h - 0.002), zinc, bevel=0.001, parent=root)
    box("Bench_Upstand_Back", (w + 0.004, 0.004, 0.1), (0, d / 2, h + 0.05), zinc, bevel=0.001, parent=root)
    for sx in (-1, 1):
        box("Bench_Upstand_Side", (0.004, d + 0.004, 0.1), (sx * (w / 2 + 0.002), 0, h + 0.05), zinc, bevel=0.001,
            parent=root)
    box("Bench_Lip_Front", (w + 0.004, 0.004, 0.022), (0, -d / 2, h - 0.008), zinc, bevel=0.001, parent=root)
    for k, z in enumerate((1.06, 1.18, 1.3, 1.42)):                       # slatted back between the rear legs
        box("Bench_Back_Slat", (w - 0.09, 0.016, 0.09), (0, d / 2 - 0.02, z), fir, bevel=0.003, parent=root)
    box("Bench_Top_Shelf", (w, 0.12, 0.018), (0, d / 2 - 0.085, 1.6), fir, bevel=0.003, parent=root)
    for sx in (-1, 1):
        prism("Bench_Bracket", [(0, 0), (0.1, 0), (0, -0.08)], 0.016, (sx * (w / 2 - 0.06), d / 2 - 0.047, 1.591),
              fir, rot=(0, 0, R(90)), parent=root)
    for k in range(5):                                                    # slatted lower shelf
        box("Bench_Shelf_Slat", (w - 0.08, (d - 0.06) / 5 - 0.012, 0.018), (0, -d / 2 + 0.03 + (k + 0.5) * (d - 0.06) / 5,
            0.18), fir, bevel=0.003, parent=root)
    # tools on hooks: trowel, hand fork, secateurs
    steel_m, grip = mat("galv", 0.3, metal=0.9), mat("main", 0.45)
    for k, x in enumerate((-0.42, -0.3)):
        rod("Hook", (x, d / 2 - 0.03, 1.36), (x, d / 2 - 0.06, 1.37), 0.003, steel_m, parent=root, segs=6)
        rod("Tool_Handle", (x, d / 2 - 0.045, 1.35), (x, d / 2 - 0.045, 1.24), 0.012, oak(), parent=root, segs=10)
        rod("Tool_Shank", (x, d / 2 - 0.045, 1.24), (x, d / 2 - 0.045, 1.21), 0.005, steel_m, parent=root, segs=6)
        if k == 0:
            box("Trowel_Blade", (0.06, 0.006, 0.13), (x, d / 2 - 0.045, 1.145), steel_m, bevel=0.003, parent=root)
        else:
            for t in (-0.018, 0, 0.018):
                box("Fork_Tine", (0.006, 0.006, 0.1), (x + t, d / 2 - 0.045, 1.16), steel_m, bevel=0.002, parent=root)
    for s in (-1, 1):                                                     # secateurs hanging open on a hook
        rod("Secateur_Grip", (-0.17, d / 2 - 0.04, 1.33), (-0.17 + s * 0.03, d / 2 - 0.04, 1.2), 0.008, grip,
            parent=root, segs=8)
    box("Secateur_Blade", (0.016, 0.005, 0.06), (-0.17, d / 2 - 0.04, 1.36), steel_m, bevel=0.002, parent=root)
    # worktop: a seed tray of seedlings and a stack of small terracotta pots
    tx, ty = -0.27, -0.04
    box("Seed_Tray", (0.36, 0.22, 0.05), (tx, ty, h + 0.025), mat("dark", 0.65), bevel=0.004, parent=root)
    box("Seed_Tray_Soil", (0.34, 0.2, 0.01), (tx, ty, h + 0.045), mat("soil", 0.95), bevel=0, parent=root)
    sprouts = Greens("Seed_Tray_Sprouts")
    for i in range(6):
        for j in range(4):
            p = Vector((tx - 0.15 + i * 0.06, ty - 0.075 + j * 0.05, h + 0.05))
            sprouts.stem(p, p + Vector((0, 0, 0.035)), 0.002, mat("plant_light", 0.5), segs=4)
            for yaw in (random.uniform(0, 3), random.uniform(3, 6)):
                sprouts.leaf(p + Vector((0, 0, 0.035)), 0.025, 0.018, yaw, R(20), mat("plant_light", 0.45), nu=3)
    sprouts.build(root)
    for s in range(4):                                                    # nested 9 cm pots
        lathe("Pot_Stack", [(0.031, 0), (0.045, 0.075), (0.047, 0.08), (0.044, 0.08)], (-0.02, 0.14, h + s * 0.018),
              terracotta(), segs=20, parent=root)
    # top shelf: trailing plants and a tin of twine
    for k, (x, sp) in enumerate(((-0.38, "pothos"), (-0.05, "rosette"), (0.33, "pothos"))):
        potted("Bench_Shelf_Pot", sp, (x, d / 2 - 0.085, 1.609), 0.1, 0.085, 0.4 if sp == "pothos" else 0.06,
               ["main", "glaze", "cream"][k], parent=root, arc=(-150, -30))
    cyl("Twine_Tin", 0.035, 0.07, (0.14, d / 2 - 0.085, 1.644), galv("Z"), segs=20, parent=root)
    cyl("Twine_Ball", 0.03, 0.03, (0.14, d / 2 - 0.085, 1.68), mat("kraft", 0.95), segs=16, bevel=0.01, parent=root)
    # lower shelf: galvanised soil bin and a bag of compost
    sb = Vector((-0.24, 0.0, 0.189))
    prof = [(0, 0), (0.146, 0), (0.151, 0.003), (0.152, 0.012)]           # extra points keep the edges crisp
    for z in (0.08, 0.2, 0.32):                                          # pressed ribs
        prof += [(0.152 + z * 0.03, z - 0.012), (0.163 + z * 0.03, z), (0.152 + z * 0.03, z + 0.012)]
    prof += [(0.164, 0.426), (0.169, 0.431), (0.169, 0.44), (0.16, 0.44), (0.158, 0.2)]
    lathe("Soil_Bin", prof, sb, galv("Z"), segs=32, parent=root)
    lathe("Soil_Bin_Lid", [(0.174, 0), (0.175, 0.004), (0.175, 0.016), (0.17, 0.021),
          (0.15, 0.028), (0.08, 0.04), (0, 0.044)], sb + Vector((0, 0, 0.432)),
          galv("Z"), segs=32, parent=root)
    ring("Soil_Bin_Lid_Handle", 0.035, 0.005, sb + Vector((0, 0, 0.474)), galv("Z"), rot=(R(90), 0, 0), arc=0.5, parent=root)
    for s in (-1, 1):
        ring("Soil_Bin_Handle", 0.03, 0.005, sb + Vector((s * 0.17, 0, 0.36)), galv("Z"), rot=(R(-90), 0, R(90)),
             arc=0.5, parent=root)
    sack = empty("Compost_Sack", (0.25, 0.0, 0.189), rot=(0, 0, R(8)), parent=root)     # kraft sack, top rolled
    box("Sack_Body", (0.3, 0.17, 0.33), (0, 0, 0.165), kraft(), bevel=0.06, parent=sack).scale = (1, 1.12, 1)
    box("Sack_Roll", (0.27, 0.06, 0.05), (0, 0.01, 0.345), kraft(), bevel=0.024, rot=(R(-12), 0, 0), parent=sack)
    box("Sack_Label", (0.16, 0.004, 0.13), (0, -0.095, 0.15), mat("cream", 0.8), bevel=0.002, parent=sack)
    cyl("Sack_Label_Leaf", 0.035, 0.003, (0, -0.098, 0.17), mat("plant", 0.7), segs=20, bevel=0,
        rot=(R(90), 0, 0), parent=sack).scale = (0.6, 1, 1)
    box("Sack_Label_Band", (0.16, 0.005, 0.026), (0, -0.0975, 0.105), mat("plant", 0.7), bevel=0, parent=sack)


def build_hero_prop():
    """Signature object: a Haws-style 1 gallon watering can, heritage green with a brass rose."""
    root, w, d, h = furniture_root("hero_prop")
    paint, brass = mat("dark", 0.32, metal=0.3), mat("brass", 0.3, metal=1.0)
    bx = 0.1                                                             # body centre (back of the can)
    lathe("Can_Body", [(0, 0), (0.088, 0), (0.092, 0.008), (0.092, 0.17), (0.084, 0.2), (0.06, 0.218), (0, 0.222)],
          (bx, 0, 0), paint, segs=32, scale=(1, 0.72, 1), parent=root)
    ring("Can_Foot", 0.09, 0.004, (bx, 0, 0.004), paint, parent=root).scale = (1, 0.72, 1)
    lathe("Can_Filler", [(0.032, 0), (0.032, 0.03), (0.036, 0.034), (0.03, 0.034), (0.028, 0.01)], (bx - 0.03, 0, 0.205),
          brass, segs=20, parent=root)
    a, b = Vector((bx - 0.08, 0, 0.03)), Vector((-0.2, 0, 0.255))     # long spout from the base
    rod("Can_Spout", a, b, 0.012, paint, parent=root, segs=12, r2=0.007)
    rose = lathe("Can_Rose", [(0.008, 0), (0.026, 0.03), (0.028, 0.034), (0, 0.036)], b, brass, segs=20, parent=root)
    rose.rotation_euler = (b - a).to_track_quat("Z", "Y").to_euler()
    for p, q in (((bx - 0.03, 0, 0.24), (bx + 0.06, 0, 0.29)), ((bx + 0.06, 0, 0.29), (bx + 0.11, 0, 0.21)),
                 ((bx + 0.11, 0, 0.21), (bx + 0.095, 0, 0.08))):        # top bar handle down the back
        rod("Can_Handle", p, q, 0.009, paint, parent=root, segs=10)
    box("Can_Stay", (0.006, 0.01, 0.05), (bx - 0.12, 0, 0.09), paint, bevel=0.002, rot=(0, R(-40), 0), parent=root)


def build_stool():
    """IKEA BEKVAM-style step stool: stepped side panels, two steps, a hand-hold slot, a back stretcher."""
    root, w, d, h = furniture_root("stool")
    beech = surface(mat("wood", 0.48, color=mix_hex(COLORS["wood"], COLORS["cream"], 0.3)), "wood")
    side = [(-0.195, 0), (0.195, 0), (0.15, 0.482), (-0.03, 0.482), (-0.045, 0.232), (-0.17, 0.232)]
    for sx in (-1, 1):
        prism("StepStool_Side", side, 0.018, (sx * (w / 2 - 0.009), 0, 0), beech, rot=(0, 0, R(90)), parent=root)
    box("StepStool_Top", (w, 0.22, 0.018), (0, 0.055, h - 0.009), beech, bevel=0.004, parent=root)
    box("StepStool_Slot", (0.11, 0.032, 0.019), (0, 0.1, h - 0.009), mat("dark", 0.8), bevel=0.012, parent=root)
    box("StepStool_Step", (w, 0.15, 0.018), (0, -0.105, 0.241), beech, bevel=0.004, parent=root)
    box("StepStool_Stretcher", (w - 0.036, 0.018, 0.08), (0, 0.15, 0.13), beech, bevel=0.003, parent=root)
    box("StepStool_Step_Rail", (w - 0.036, 0.018, 0.06), (0, -0.04, 0.2), beech, bevel=0.003, parent=root)


def build_counter():
    """Painted tongue-and-groove shop counter with an oak top: tablet till, card reader, kraft-paper roll
    on a steel cutter with a wrapped bouquet, business cards, twine and a bud vase."""
    root, w, d, h = furniture_root("counter")
    paint, top_t = painted("accent_2"), 0.03
    box("Counter_Plinth", (w - 0.06, d - 0.1, 0.1), (0, 0.02, 0.05), mat("dark", 0.7), bevel=0.003, parent=root)
    box("Counter_Carcass", (w - 0.02, d - 0.04, h - top_t - 0.1), (0, 0.01, 0.1 + (h - top_t - 0.1) / 2), paint,
        bevel=0.003, parent=root)
    n = 12                                                            # V-groove boards with 3 mm gaps
    bw = (w - 0.03) / n
    fy = -(d - 0.04) / 2 + 0.01 - 0.007
    for k in range(n):
        box("Counter_TG_Board", (bw - 0.003, 0.014, h - top_t - 0.17), (-w / 2 + 0.015 + (k + 0.5) * bw, fy,
            0.1 + (h - top_t - 0.17) / 2), paint, bevel=0.003, parent=root)
    box("Counter_Frieze", (w - 0.01, 0.02, 0.06), (0, fy - 0.003, h - top_t - 0.035), paint, bevel=0.004, parent=root)
    box("Counter_Kick_Rail", (w - 0.01, 0.02, 0.025), (0, fy - 0.003, 0.112), paint, bevel=0.004, parent=root)
    for sx in (-1, 1):                                                # framed end panels
        ex = sx * (w / 2 - 0.004)
        for nm, sz, lc in (("Stile", (0.012, 0.06, h - top_t - 0.1), (ex, -d / 2 + 0.05, 0.1 + (h - top_t - 0.1) / 2)),
                           ("Stile", (0.012, 0.06, h - top_t - 0.1), (ex, d / 2 - 0.05, 0.1 + (h - top_t - 0.1) / 2)),
                           ("Rail", (0.012, d - 0.1, 0.07), (ex, 0, h - top_t - 0.035)),
                           ("Rail", (0.012, d - 0.1, 0.07), (ex, 0, 0.135))):
            box(f"Counter_End_{nm}", sz, lc, paint, bevel=0.004, parent=root)
    box("Counter_Top", (w + 0.05, d + 0.04, top_t), (0, 0, h - top_t / 2), oak(), bevel=0.004, parent=root)
    # the shop's own square oak sign plaque on the counter front (your logo goes here)
    box("Logo_Plaque", (0.19, 0.012, 0.19), (0, fy - 0.013, 0.58), oak(), bevel=0.004, parent=root)
    logo = hook_image("logo", 1, (0.15, 0.15), (0, fy - 0.0195, 0.58), parent=root, default_key="cream")
    hook_default(logo, cyl("Logo_Leaf", 0.035, 0.002, (0, fy - 0.021, 0.58), mat("plant", 0.6), segs=24, bevel=0,
                           rot=(R(90), 0, 0), parent=root))
    # tablet till on a swivel stand, turned toward the customer (and the camera)
    tab = empty("Counter_Tablet", (0.28, -0.04, h), rot=(0, 0, R(-45)), parent=root)
    cyl("Tablet_Base", 0.06, 0.012, (0, 0.03, 0.006), mat("galv", 0.3, metal=0.9), segs=28, parent=tab)
    rod("Tablet_Neck", (0, 0.03, 0.012), (0, 0.04, 0.1), 0.012, mat("galv", 0.3, metal=0.9), parent=tab)
    lean = R(-16)
    box("Tablet_Body", (0.281, 0.007, 0.215), (0, 0.035, 0.2), mat("dark", 0.3, metal=0.3), bevel=0.006,
        rot=(lean, 0, 0), parent=tab)
    ny, nz = math.cos(lean), math.sin(lean)                           # tablet normal points along local -y, tipped back
    normal, tup = Vector((0, -ny, -nz)), Vector((0, -nz, ny))
    face = Vector((0, 0.035, 0.2)) + normal * 0.0042
    scr = hook_image("screen", 1, (0.26, 0.195), face, rot=(lean, 0, 0), parent=tab, glow=True, default_key="cream")
    ui = []
    for nm, size, off, key in (("Header", (0.23, 0.028), (0, 0.072), "plant"), ("Card_1", (0.068, 0.08), (-0.08, -0.01), "plant_light"),
                               ("Card_2", (0.068, 0.08), (0, -0.01), "flower"), ("Card_3", (0.068, 0.08), (0.08, -0.01), "succulent"),
                               ("Button", (0.09, 0.024), (0.065, -0.074), "main")):
        p = face + normal * 0.0015 + Vector((off[0], 0, 0)) + tup * off[1]
        ui.append(box(f"Tablet_UI_{nm}", (size[0], 0.002, size[1]), p, mat(key, 0.5, emit=0.6), bevel=0,
                      rot=(lean, 0, 0), parent=tab))
    hook_default(scr, *ui)
    # card reader on its cradle
    cr = empty("Card_Reader", (0.5, -0.17, h), rot=(0, 0, R(-35)), parent=root)
    box("Reader_Cradle", (0.09, 0.07, 0.016), (0, 0, 0.008), mat("cream", 0.35), bevel=0.006, parent=cr)
    box("Reader_Body", (0.084, 0.023, 0.084), (0, 0.006, 0.055), mat("cream", 0.3), bevel=0.008, rot=(R(-28), 0, 0),
        parent=cr)
    box("Reader_Screen", (0.06, 0.002, 0.028), (0, -0.009, 0.077), mat("dark", 0.2, emit=0.3), bevel=0,
        rot=(R(-28), 0, 0), parent=cr)
    for i in range(3):
        for j in range(3):
            box("Reader_Key", (0.014, 0.002, 0.007), ((i - 1) * 0.02, 0.0 + j * 0.005, 0.034 + j * 0.0105),
                mat("dark", 0.5), bevel=0, rot=(R(-28), 0, 0), parent=cr)
    # kraft-paper roll on a steel cutter (staff side), with a sheet pulled out and a wrapped bouquet
    pr = empty("Paper_Roll", (-0.27, 0.13, h), parent=root)
    steel_m = mat("galv", 0.35, metal=0.9)
    for sx in (-1, 1):
        prism("Roll_Bracket", [(-0.09, 0), (0.09, 0), (0.05, 0.2), (-0.03, 0.2)], 0.006, (sx * 0.33, 0, 0), steel_m,
              rot=(0, 0, R(90)), parent=pr)
    cyl("Roll_Paper", 0.07, 0.6, (0, 0.0, 0.13), kraft(), segs=32, rot=(0, R(90), 0), parent=pr)
    cyl("Roll_Bar", 0.012, 0.67, (0, 0.0, 0.13), steel_m, segs=12, rot=(0, R(90), 0), parent=pr)
    box("Roll_Cutter", (0.66, 0.012, 0.03), (0, -0.09, 0.05), steel_m, bevel=0.002, parent=pr)
    box("Roll_Base", (0.66, 0.18, 0.006), (0, 0, 0.003), steel_m, bevel=0.002, parent=pr)
    box("Roll_Sheet_Drop", (0.58, 0.0015, 0.09), (0, -0.075, 0.09), kraft(), bevel=0, rot=(R(-20), 0, 0), parent=pr)
    box("Roll_Sheet", (0.58, 0.26, 0.0015), (0, -0.23, 0.0075), kraft(), bevel=0, parent=pr)
    bq = empty("Bouquet", (-0.25, -0.12, h + 0.06), rot=(0, 0, R(12)), parent=root)
    cyl("Bouquet_Wrap", 0.012, 0.3, (0, 0, 0), kraft(), r2=0.07, segs=20, bevel=0, rot=(0, R(-90), 0), parent=bq)
    heads = Greens("Bouquet_Heads")
    cut_stems(heads, "tulip", 6, 0.06, 0.03)
    hb = heads.build(bq, (-0.15, 0, 0))
    hb.rotation_euler = (0, R(-80), 0)
    # business-card stand (LinkedIn), twine cone and a bud vase
    cards = box("Card_Stand", (0.1, 0.06, 0.03), (0.1, -0.2, h + 0.015), oak(), bevel=0.004, rot=(0, 0, R(-20)),
                parent=root)
    hook_link(cards, "linkedin")
    box("Card_Stand_Cards", (0.09, 0.006, 0.055), (0.1, -0.195, h + 0.05), mat("cream", 0.6), bevel=0.001,
        rot=(R(-12), 0, R(-20)), parent=root)
    rl = Vector((-0.52, -0.17, h + 0.05))                              # florist's reel of satin ribbon, on edge
    for sx in (-1, 1):
        cyl("Ribbon_Reel_Flange", 0.05, 0.004, rl + Vector((sx * 0.016, 0, 0)), mat("cream", 0.5), segs=32,
            bevel=0.001, rot=(0, R(90), 0), parent=root)
    cyl("Ribbon_Reel_Ribbon", 0.041, 0.028, rl, mat("flower", 0.3), segs=32, bevel=0.001, rot=(0, R(90), 0), parent=root)
    cyl("Ribbon_Reel_Hub", 0.012, 0.037, rl, mat("dark", 0.5), segs=16, bevel=0, rot=(0, R(90), 0), parent=root)
    box("Ribbon_Tail", (0.026, 0.12, 0.001), (-0.52, -0.25, h + 0.001), mat("flower", 0.3), bevel=0, parent=root)
    lathe("Bud_Vase", [(0, 0), (0.03, 0), (0.035, 0.04), (0.014, 0.1), (0.016, 0.12), (0.012, 0.12)],
          (0.5, 0.15, h), glazed("glaze"), segs=24, parent=root)
    bv = Greens("Bud_Vase_Stems")
    cut_stems(bv, "rose", 2, 0.2, 0.02)
    bv.build(root, (0.5, 0.15, h + 0.1))


def build_table():
    """IKEA LERHAMN-style pine table (antique-stain top, white-stain tapered legs, apron rail) with seed
    trays of succulents and cacti, slate price stakes, and apple crates of terracotta pots underneath."""
    root, w, d, h = furniture_root("table")
    top_m, leg_m = oak(), surface(mat("cream", 0.57), "wood")
    for k in range(4):                                                # four glued planks
        box("Table_Plank", (w, d / 4 - 0.002, 0.025), (0, -d / 2 + (k + 0.5) * d / 4, h - 0.0125), top_m,
            bevel=0.003, parent=root)
    for sy in (-1, 1):
        box("Table_Apron", (w - 0.14, 0.02, 0.08), (0, sy * (d / 2 - 0.06), h - 0.065), leg_m, bevel=0.003, parent=root)
    for sx in (-1, 1):
        box("Table_Apron", (0.02, d - 0.14, 0.08), (sx * (w / 2 - 0.06), 0, h - 0.065), leg_m, bevel=0.003, parent=root)
        for sy in (-1, 1):
            cyl("Table_Leg", 0.028, h - 0.025, (sx * (w / 2 - 0.06), sy * (d / 2 - 0.06), (h - 0.025) / 2), leg_m,
                r2=0.039, segs=4, bevel=0.003, rot=(0, 0, R(45)), parent=root)     # square leg, tapered to the foot
    tray_m = mat("dark", 0.65)
    for tx in (-0.3, 0.28):                                           # black seed trays of 7 cm pots
        box("Tray", (0.4, 0.26, 0.045), (tx, -0.06, h + 0.0225), tray_m, bevel=0.004, parent=root)
        for i in range(4):
            for j in range(2):
                sp = random.choice(["rosette", "rosette", "cactus", "barrel", "flowers"])
                potted("Tray_Pot", sp, (tx - 0.135 + i * 0.09, -0.12 + j * 0.115, h + 0.01), 0.075, 0.07,
                       {"rosette": 0.06, "cactus": 0.13, "barrel": 0.07, "flowers": 0.13}[sp], "main", parent=root)
        stake = box("Price_Stake", (0.08, 0.004, 0.045), (tx + 0.15, -0.205, h + 0.1), mat("dark", 0.9), bevel=0.002,
                    rot=(R(-12), 0, 0), parent=root)                    # slate tag on a stick, chalked price
        rod("Price_Stick", (tx + 0.15, -0.2, h + 0.045), (tx + 0.15, -0.2, h + 0.078), 0.002, pine(), parent=root, segs=5)
        label("Price", "£4.50", 0.022, (0, -0.0025, 0.0), mat("chalk", 0.95), parent=stake)
    for k, (x, sp, key) in enumerate(((-0.38, "pothos", "cream"), (0.0, "monstera", "glaze"), (0.38, "fern", "main"))):
        potted("Table_Pot", sp, (x, 0.22, h), 0.14, 0.13, 0.3 if sp != "monstera" else 0.36, key, parent=root)
    # two apple crates under the table, full of nested terracotta pots
    for cx in (-0.28, 0.28):
        for sx in (-1, 1):
            box("Crate_End", (0.018, 0.3, 0.25), (cx + sx * 0.241, 0, 0.125), pine(), bevel=0.003, parent=root)
        for sy in (-1, 1):
            for z in (0.035, 0.125, 0.215):
                box("Crate_Slat", (0.5, 0.012, 0.06), (cx, sy * 0.144, z), pine(), bevel=0.002, parent=root)
        box("Crate_Base", (0.48, 0.28, 0.012), (cx, 0, 0.012), pine(), bevel=0.002, parent=root)
        for px in (-0.11, 0.11):
            for s in range(4):
                lathe("Crate_Pots", [(0.052, 0), (0.075, 0.12), (0.078, 0.125), (0.072, 0.125)],
                      (cx + px, 0, 0.018 + s * 0.03), terracotta(), segs=20, parent=root)


PLACEHOLDERS = {
    "shelf": build_shelf, "hanging_plant": build_hanging_plant, "plant": build_plant, "workbench": build_workbench,
    "hero_prop": build_hero_prop, "stool": build_stool, "counter": build_counter, "table": build_table,
}
if SHOW_PLACEHOLDER_FURNITURE:
    for slot_name, build in PLACEHOLDERS.items():
        build()

# =====================================================================
#  WALL DECOR AND PORTFOLIO
# =====================================================================
chalk = mat("chalk", 0.95)

# Shop chalkboard on the left wall behind the counter: your name, role and project titles.
board = empty("Chalkboard", (0.0, 0.85, 1.9), rot=(0, 0, R(90)))       # local -y points into the room (+x)
bw_, bh_, fw = 1.2, 0.86, 0.05
frame_m = oak()
frame_parts = [box("Chalkboard_Frame", (bw_, 0.03, fw), (0, -0.015, s * (bh_ / 2 - fw / 2)), frame_m, bevel=0.005,
                   parent=board) for s in (-1, 1)]
frame_parts += [box("Chalkboard_Frame", (fw, 0.03, bh_ - 2 * fw), (s * (bw_ / 2 - fw / 2), -0.015, 0), frame_m,
                    bevel=0.005, parent=board) for s in (-1, 1)]
hook_link(frame_parts[0], "website")
box("Chalkboard_Slate", (bw_ - 2 * fw + 0.01, 0.012, bh_ - 2 * fw + 0.01), (0, -0.012, 0),
    surface(mat("dark", 0.86), "plaster", scale=1.5), bevel=0, parent=board)
box("Chalk_Ledge", (bw_ * 0.9, 0.06, 0.018), (0, -0.045, -bh_ / 2 - 0.004), frame_m, bevel=0.004, parent=board)
for k, x in enumerate((-0.3, -0.24, 0.35)):
    rod("Chalk_Stick", (x, -0.05, -bh_ / 2 + 0.012), (x + 0.07, -0.05, -bh_ / 2 + 0.012), 0.005,
        [chalk, mat("flower", 0.9), chalk][k], parent=board)
fy = -0.02
hook_text("name", 1, "YOUR NAME", 0.16, (0, fy, 0.24), material=chalk, max_width=1.0, parent=board)
hook_text("role", 1, "your role", 0.085, (0, fy, 0.085), material=chalk, max_width=1.0, parent=board)
box("Chalk_Line", (0.8, 0.003, 0.01), (0, fy, 0.0), chalk, bevel=0, parent=board)
label("Chalk_Picks", "~ fresh in this week ~", 0.042, (0, fy, -0.07), chalk, parent=board)
for i, title in enumerate(("Monstera", "Fiddle Leaf Fig", "String of Pearls")):
    zz = -0.15 - i * 0.085
    hook_text("title", i + 1, title, 0.05, (-0.38, fy, zz), material=chalk, max_width=0.62, parent=board,
              align="LEFT", depth=0.004)
    ball("Chalk_Bullet", 0.012, (-0.43, fy, zz), chalk, scale=(1, 0.3, 1), parent=board)
doodle = Greens("Chalk_Doodle")
for k in range(5):
    m = (Matrix.Translation((0.4, fy - 0.002, -0.24)) @ Matrix.Rotation(R(-50 + k * 25), 4, "Y")
         @ Matrix.Rotation(R(90), 4, "X"))
    doodle.leaf_m(m, 0.11, 0.045, chalk, droop=0, fold=0, nu=5, profile=HEART, notch=0.1)
doodle.build(board)
cyl("Chalk_Doodle_Pot", 0.045, 0.06, (0.4, fy, -0.28), chalk, r2=0.055, segs=16, bevel=0, parent=board).scale = (1, 0.06, 1)

# Two gooseneck barn wall lights over the chalkboard (25 cm enamel dome shades).
LAMP_SPOTS = []
for k, y in enumerate((0.45, 1.25)):
    lamp = empty("Barn_Light", (0.0, y, 2.76), rot=(0, 0, R(90)))
    sm = mat("steel", 0.3, metal=0.4)
    cyl("Barn_Plate", 0.06, 0.02, (0, -0.01, 0), sm, segs=24, rot=(R(90), 0, 0), parent=lamp)
    pts = [Vector(p) for p in ((0, -0.02, 0), (0, -0.09, 0.04), (0, -0.17, 0.05), (0, -0.23, 0.02), (0, -0.25, -0.03))]
    for a, b in zip(pts, pts[1:]):
        rod("Barn_Gooseneck", a, b, 0.008, sm, parent=lamp)
    tip = pts[-1]
    lathe("Barn_Shade", [(0.014, 0.0), (0.03, -0.006), (0.08, -0.04), (0.118, -0.09), (0.125, -0.1), (0.12, -0.1),
                         (0.11, -0.09), (0.075, -0.045), (0.025, -0.012)], tip, sm, segs=32, parent=lamp)
    lathe("Barn_Shade_Inside", [(0.11, -0.089), (0.075, -0.044), (0.026, -0.013)], tip - Vector((0, 0, 0.002)),
          mat("cream", 0.4), segs=32, parent=lamp)
    bulb = ball("Barn_Bulb", 0.028, tip + Vector((0, 0, -0.05)), mat("bulb", 0.3, emit=8.0, color="#FFE2A8"),
                parent=lamp)
    no_shadow(bulb)
    LAMP_SPOTS.append((0.25, y, 2.66))

# Three framed botanical prints above the potting bench (RIBBA-type 40x50 black frames, white mounts).
prints = empty("Botanical_Prints", (0.0, 2.25, 2.17), rot=(0, 0, R(90)))
fw2, fh2, rail = 0.42, 0.52, 0.022
for i, px in enumerate((-0.46, 0.0, 0.46)):
    for s in (-1, 1):
        box("Print_Frame", (fw2, 0.04, rail), (px, -0.02, s * (fh2 / 2 - rail / 2)), mat("dark", 0.4), bevel=0.003,
            parent=prints)
        box("Print_Frame", (rail, 0.04, fh2 - 2 * rail), (px + s * (fw2 / 2 - rail / 2), -0.02, 0), mat("dark", 0.4),
            bevel=0.003, parent=prints)
    box("Print_Mount", (fw2 - 0.03, 0.004, fh2 - 0.03), (px, -0.03, 0), mat("cream", 0.8), bevel=0, parent=prints)
    pic = hook_image("frame", i + 1, (0.29, 0.39), (px, -0.0335, 0), parent=prints, default_key="cream")
    art = Greens(f"Print_Art_{i}")
    ink = [mat("plant", 0.7), mat("plant_light", 0.7), mat("main", 0.7)][i]
    base = Vector((px, -0.036, -0.15))
    if i == 1:                                   # a monstera leaf study
        mm = Matrix.Translation(base + Vector((0, 0, 0.02))) @ Matrix.Rotation(R(90), 4, "X")
        art.split_leaf(mm, 0.28, 0.26, ink, lobes=6, droop=0, fold=0, curl=0)
    else:                                        # a single stem with alternating leaves
        art.stem(base, base + Vector((0, 0, 0.3)), 0.003, ink)
        for s in range(5):
            p = base + Vector((0, 0, 0.04 + s * 0.055))
            side = 1 if s % 2 else -1
            mm = (Matrix.Translation(p) @ Matrix.Rotation(R(side * 50), 4, "Y") @ Matrix.Rotation(R(90), 4, "X"))
            art.leaf_m(mm, 0.1 - s * 0.01, 0.05, ink, droop=0, fold=0, nu=5)
        art.blob(base + Vector((0, 0, 0.31)), 0.02, mat("flower", 0.7), scale=(1, 0.2, 1))
    hook_default(pic, art.build(prints))

# Three-tier florist bucket stand under the shop window, full of cut stems.
stand = empty("Bucket_Stand", (wx, D - 0.33, FLOOR_Z))
sw, tiers = 1.5, ((-0.19, 0.22), (0.0, 0.44), (0.19, 0.66))        # (y, top height) front to back
for sx in (-1, 0, 1):
    xx = sx * (sw / 2 - 0.02) if sx else 0
    prism("Stand_Side", [(-0.28, 0), (0.28, 0), (0.28, 0.66), (0.1, 0.66), (0.1, 0.44), (-0.09, 0.44), (-0.09, 0.22),
                         (-0.28, 0.22)], 0.03, (xx, 0, 0), pine(), rot=(0, 0, R(90)), parent=stand)
for ty, tz in tiers:
    for k in (-1, 1):
        box("Stand_Plank", (sw, 0.088, 0.02), (0, ty + k * 0.046, tz - 0.01), pine(), bevel=0.003, parent=stand)
bucket_plan = [   # (x, tier, diameter, height, stems, count, stem length)
    (-0.5, 0, 0.24, 0.3, "tulip", 14, 0.32), (0.0, 0, 0.24, 0.3, "sunflower", 6, 0.4), (0.5, 0, 0.24, 0.3, "rose", 10, 0.3),
    (-0.42, 1, 0.2, 0.26, "eucalyptus", 7, 0.5), (0.1, 1, 0.2, 0.26, "gyp", 9, 0.4), (0.55, 1, 0.2, 0.26, "tulip", 12, 0.34),
    (-0.2, 2, 0.18, 0.31, "eucalyptus", 6, 0.55), (0.32, 2, 0.18, 0.31, "rose", 9, 0.36),
]
for k, (bx_, tier, bd, bh, kind, cnt, ln) in enumerate(bucket_plan):
    ty, tz = tiers[tier]
    flower_bucket(f"Flower_Bucket_{k}", (bx_, ty, tz), bd, bh, kind, cnt, ln, parent=stand)
flower_bucket("Floor_Bucket", (3.28, D - 0.45, FLOOR_Z), 0.24, 0.3, "eucalyptus", 8, 0.7)

# Small wooden-frame chalk A-board by the door (click it to email you).
ab = empty("A_Board", (2.95, 0.32, FLOOR_Z), rot=(0, 0, R(45)))
L, a = 0.8, R(11)
for s in (-1, 1):
    side_e = empty("A_Board_Side", (0, s * L / 2 * math.sin(a), L / 2 * math.cos(a)), rot=(s * a, 0, 0), parent=ab)
    if s > 0:
        side_e.rotation_euler = (-a, 0, R(180))
    parts = [box("A_Board_Frame", (0.5, 0.02, 0.035), (0, 0, z), oak(), bevel=0.004, parent=side_e)
             for z in (-L / 2 + 0.0175, L / 2 - 0.0175)]
    parts += [box("A_Board_Frame", (0.035, 0.02, L - 0.07), (x, 0, 0), oak(), bevel=0.004, parent=side_e)
              for x in (-0.2325, 0.2325)]
    panel = box("A_Board_Chalk", (0.44, 0.01, L - 0.06), (0, 0.002, 0), surface(mat("dark", 0.86), "plaster", scale=1.5),
                bevel=0, parent=side_e)
    if s < 0:
        hook_link(panel, "email")
        for nm, txt, sz, z in (("A_Title", "PLANTS", 0.075, 0.25), ("A_Title2", "& FLOWERS", 0.05, 0.16),
                               ("A_Line", "~ come in ~", 0.03, 0.08), ("A_Mail", "say hello", 0.045, -0.1)):
            label(nm, txt, sz, (0, -0.008, z), chalk, parent=side_e)
        box("A_Envelope", (0.12, 0.003, 0.08), (0, -0.008, -0.22), chalk, bevel=0, parent=side_e)
        box("A_Envelope_In", (0.105, 0.004, 0.065), (0, -0.0085, -0.22), mat("dark", 0.86), bevel=0, parent=side_e)
        for sx in (-1, 1):
            box("A_Envelope_V", (0.07, 0.004, 0.007), (sx * 0.028, -0.009, -0.205), chalk, bevel=0,
                rot=(0, R(sx * 32), 0), parent=side_e)
rod("A_Board_Chain", (-0.18, -0.12, 0.25), (-0.18, 0.12, 0.25), 0.002, mat("galv", 0.3, metal=0.9), parent=ab, segs=4)

# Floor-standing grow light over the display table (arched pendant stand with a black LED can).
GROW_SPOTS = []
if GROW_LIGHTS:
    black, base_xy = mat("dark", 0.5), Vector((3.28, 2.42))
    cyl("Grow_Stand_Base", 0.14, 0.014, (*base_xy, FLOOR_Z + 0.007), black, segs=32, bevel=0.004).scale = (1, 1.25, 1)
    arm = [Vector((*base_xy, FLOOR_Z + 0.014)), Vector((*base_xy, 1.85)), Vector((3.18, 2.33, 1.98)),
           Vector((2.92, 2.12, 2.02)), Vector((2.6, 1.9, 1.96))]
    for a, b in zip(arm, arm[1:]):
        rod("Grow_Stand_Pole", a, b, 0.011, black, segs=12)
    tip = arm[-1]
    rod("Grow_Cord", tip, tip - Vector((0, 0, 0.3)), 0.003, black, segs=6)
    cyl("Grow_Can", 0.045, 0.16, tip - Vector((0, 0, 0.38)), black, segs=28, bevel=0.004)
    dif = cyl("Grow_Diffuser", 0.038, 0.004, tip - Vector((0, 0, 0.461)), mat("grow", 0.3, emit=6.0), segs=24, bevel=0)
    no_shadow(dif)
    GROW_SPOTS.append(tuple(tip - Vector((0, 0, 0.49))))

# Floor plants: real sizes in real pots.
potted("Floor_Olive", "olive", (4.05, 1.5, FLOOR_Z), 0.35, 0.31, 1.3, "main")
potted("Floor_Fiddle", "fiddle", (4.05, 2.85, FLOOR_Z), 0.34, 0.32, 1.4, "cream")
potted("Floor_Monstera", "monstera", (4.0, 0.5, FLOOR_Z), 0.3, 0.28, 0.8, "glaze", arc=(60, 300))
potted("Floor_Snake", "snake", (1.75, 0.3, FLOOR_Z), 0.22, 0.2, 0.6, "main")
potted("Floor_Corner_Fern", "fern", (1.18, D - 0.5, FLOOR_Z), 0.26, 0.24, 0.42, "cream")

# =====================================================================
#  LIGHTS, WORLD, CAMERA, RENDER
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


# Sun shining in through the shop window from behind the room; a soft sky panel at the window;
# a big soft fill from the camera side; two warm barn lights on the chalkboard; grow-light pools.
sun_warm, sun_power, lamp_power, sky_k = SUN_WARMTH, SUN_STRENGTH, LAMP_STRENGTH, 7000
sun_from = (wx - 2.0, D + 6.0, 6.2)                         # about 38 degrees high
if THEME == "golden_hour":                                  # low orange evening sun, barn lights turned up
    sun_warm, sun_power, lamp_power, sky_k = 3100, SUN_STRENGTH * 1.6, LAMP_STRENGTH * 1.8, 4200
    sun_from = (wx + 3.0, D + 6.5, 3.9)                     # about 24 degrees high
light("Light_Sun", "SUN", sun_power, kelvin(sun_warm), sun_from, aim=(wx - 0.4, D - 2.2, 0), size=R(2.5))
light("Light_Window", "AREA", 160 * WINDOW_GLOW, kelvin(sky_k), (wx, D - 0.12, wz), aim=(wx, 0, wz - 1.0), size=ww)
light("Light_Fill", "AREA", 250 * (W * D / 16), kelvin(6000), (W + 3, -3, H + 2.5), aim=(W / 2, D / 2, 0.6), size=6)
light("Light_Bounce", "AREA", 35, kelvin(5000), (W / 2, D / 2, H - 0.1), aim=(W / 2, D / 2, 0), size=2.5)
for k, p in enumerate(LAMP_SPOTS):
    light(f"Light_Barn_{k + 1}", "POINT", lamp_power, kelvin(LAMP_WARMTH), p, size=0.04)
for k, p in enumerate(GROW_SPOTS):
    light(f"Light_Grow_{k + 1}", "SPOT", 12, kelvin(3500), p, aim=(p[0], p[1], 0), size=0.03).data.spot_size = R(70)

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
bg_amb.inputs["Color"].default_value = (*kelvin(6500 if THEME != "golden_hour" else 4500), 1)
bg_amb.inputs["Strength"].default_value = 0.4
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
scene["kit_material_finish"] = json.dumps({"roughness": 0.6, "bevel": 0.004, "saturation": 0.75})
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
