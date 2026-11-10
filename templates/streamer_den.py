"""
3D ROOM PORTFOLIO KIT  -  Template: STREAMER & GAME-DEV DEN
===========================================================
Builds an isometric streamer / gamer room at night (rainy city window, LED strip tape, a neon sign with YOUR
name, L-desk battlestation, ring light, boom mic, arcade cabinet, KALLAX TV bench) and renders a 1920x1080 image.
Every piece is modelled on a real product you could buy (see REFERENCES below and research/streamer_den.md).
Set THEME = "clean" for a bright white daytime version of the same set.

HOW TO RUN
  Option A (no Blender UI):   blender -b -P streamer_den.py
  Option B (inside Blender):  Scripting tab > Open > streamer_den.py > Run Script (then F12 to render)

You only need to edit the SETTINGS block below. Everything under it builds the room.
Output: output/streamer_den.png and output/streamer_den.blend next to this script.
"""
# REFERENCES  (real products each piece is modelled on - names only here, never in the scene)
#   desk        L-shaped carbon-texture gaming desk (REKT R-Desk 160L style): 160 x 110 x 75 cm, 25 mm top,
#               steel sled legs, LED strip under the front lip       https://ldlc.com/en/product/PB00447859.html
#   chair       Secretlab TITAN Evo (Regular): seat 51 cm, backrest 86 x 54 cm, 5-star alu base, 4D arms
#               https://www.3dtested.com/peripherals/gaming-chairs/secretlab-titan-evo-nanogen-review
#   PC tower    Lian Li O11 Dynamic EVO: 28.5 x 46.5 x 45.9 cm, pillar-less glass front + side, 6 RGB fans
#               https://www.bhphotovideo.com/c/product/1690347-REG/lian_li_o11dex_o11_dynamic_evo_atx.html
#   mic + arm   RODE PSA1-style spring boom (2 x 40 cm) + Shure SM7B-style broadcast mic (19 cm)
#               https://help.elgato.com/hc/en-us/articles/4404867182093-Elgato-Wave-Mic-Arm-Specifications
#   monitor     34" 21:9 ultrawide (80 x 33.5 cm panel, V-foot) + 24" in portrait (53 x 30 cm), clip webcam
#               https://www.aoc.com/uk/gaming/products/monitors/g2790vxa/specification
#   speaker     Edifier R1280T bookshelf speakers: 14.6 x 19.6 x 23.4 cm each, wood + black baffle
#               https://www.bhphotovideo.com/c/product/1503870-REG/edifier_4001345_r1280t_r1280t_bookshelf_speakers_wood.html
#   stream deck Elgato Stream Deck MK.2: 11.8 x 8.4 x 2.5 cm, 15 lit keys
#               https://help.elgato.com/hc/en-us/articles/18208816152333-Elgato-Stream-Deck-MK-2-Technical-Specifications
#   floor_lamp  NEEWER 18" ring light on a light stand: 46 cm ring, 1.75 m high, phone holder
#               https://neewer.com/collections/ring-lights/products/led-ring-lights-66600024
#   hex lights  Nanoleaf Shapes Hexagons (no brand shown): 23 x 20 x 1 cm panels
#               https://cdn.shopify.com/s/files/1/0573/3207/2636/files/Nanoleaf_Shapes_-_Hexagons_-_SKUs_spec_sheet_EN.pdf
#   foam        30 x 30 x 5 cm studio wedge foam tiles, checkerboard
#               https://gear4music.com/Recording-and-Computers/Acoustic-Gear-30x30x5cm-Wedge-4-Pack/43US
#   hero_prop   Arcade1Up cabinet + 1 ft riser: 50.5 x 50.2 x 153.7 cm, T-moulding, 17" screen
#               https://thebrick.com/products/arcade1up-dragon-s-lair-arcade-cabinet-with-riser
#   sofa        IKEA KLIPPAN loveseat: 180 x 88 x 66 cm, seat 43 cm, 11 cm under the frame
#               https://www.ikea.com/us/en/p/klippan-loveseat-vissle-green-s09561666/
#   shelf       IKEA KALLAX 2x4 on its side as a TV bench: 147 x 39 x 77 cm, 33 cm cubes, no back
#               https://www.ikea.gr/en/products/kallax-shelving-unit-77x147-cm/40346924/
#   TV          65" 4K TV on a flat wall bracket: 144.9 x 83.4 x 2.6 cm  https://www.wepc.com/tv/65-inch-tv-dimensions/
#   wall_art    IKEA RIBBA frames 50x70 and 30x40 with white mount   https://www.ikea.com/my/en/p/ribba-frame-black-50301618
#   side table  IKEA LACK side table: 55 x 55 x 45 cm, 5 cm top     https://www.ikea.com/de/en/p/lack-side-table-white-30449908
#   rug         IKEA TIPHEDE-style flat-woven cotton rug: 155 x 220 cm, striped ends, knotted fringe
#               https://www.ikea.com/gb/en/search/?q=tiphede
#   pouffe      chunky hand-knitted wool pouffe: 50 cm across, 38 cm high, braided stitch columns
#               https://www.ikea.com/gb/en/search/?q=knitted%20pouffe
#   throw       chunky knit throw 130 x 170 cm, folded in three over the sofa arm, tassel ends
#   plant       snake plant (Sansevieria) ~70 cm in a 30 cm glazed pot; vinyl figures ~9.5 cm on the KALLAX
#   floor/walls oak-laminate planks 19 x 122 cm, painted plaster walls, satin skirting, uPVC casement window

# =====================================================================
#  SETTINGS  -  change these lines, then run the script again
# =====================================================================
ROOM_NAME = "streamer_den"          # used for the output file names

ROOM_WIDTH = 4.4                    # metres, left to right
ROOM_DEPTH = 4.0                    # metres, front to back
WALL_HEIGHT = 2.8                   # metres

THEME = "neon"                      # "neon" = the den at night | "clean" = white daytime set
THEMES = {                          # any hex colour works; "main" is the room's hero colour (the sofa fabric)
    # "clean" is a DAY theme: it swaps the lights for daylight (see DAY_THEMES / DAY_LIGHTS below).
    "neon": {
        "background": "#0F1124", "wall": "#252B50", "wall_trim": "#1A1E38", "floor": "#6B5140",
        "wood": "#2F2926", "main": "#3C3F52", "accent_1": "#9D4DFF", "accent_2": "#22D3EE",
        "accent_3": "#FF4FA3", "cream": "#E6E3DC", "plant": "#3E8E5A", "dark": "#17181E",
        "desk": "#1D1E25",            # desk top (carbon-texture laminate)
        "sky": "#1B2E6B",             # the rainy city sky outside the window
        "neon_1": "#A24BFF", "neon_2": "#1FD6FF", "neon_3": "#FF4FA3",   # LED strip colours
    },
    "clean": {
        "background": "#ECEEF3", "wall": "#F1EFEA", "wall_trim": "#DDD9D2", "floor": "#C9A47A",
        "wood": "#EAE3D8", "main": "#C9C5BE", "accent_1": "#8A5CFF", "accent_2": "#3CCFE0",
        "accent_3": "#FF7FB6", "cream": "#FFFFFF", "plant": "#4F9A5E", "dark": "#2A2C33",
        "desk": "#F4F4F2", "sky": "#A9D4FF",
        "neon_1": "#A07BFF", "neon_2": "#3CCFE0", "neon_3": "#FF8CBF",
    },
}

SUN_WARMTH = 9500                   # Kelvin of the window light: 9500 = cold blue moonlight
SUN_STRENGTH = 0.8                  # moonlight is weak; the room brightness follows this value
LAMP_WARMTH = 6200                  # Kelvin of the ring light (cool white, like a real streaming light)
LAMP_STRENGTH = 70                  # Watts of the ring light that lights the chair
NEON_STRENGTH = 1.0                 # brightness of all LED strips and neon signs (0 = off, 2 = very bright)
RAIN = True                         # rain streaks on the window (night themes only)
DAY_THEMES = ("clean",)             # themes lit as daytime ...
DAY_LIGHTS = {"SUN_WARMTH": 5800, "SUN_STRENGTH": 3.0, "LAMP_STRENGTH": 25, "NEON_STRENGTH": 0.1}   # ... with these
SEED = 7                            # change to shuffle games, figures, the city and small props

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

import colorsys
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

STYLE = "streamer_den"
KIT_VERSION = 2
W, D, H = ROOM_WIDTH, ROOM_DEPTH, WALL_HEIGHT
T = 0.15            # wall thickness
FLOOR_Z = 0.03      # top of the floor planks; furniture stands here
R = math.radians
random.seed(SEED)

NIGHT = THEME not in DAY_THEMES
if not NIGHT:                       # daytime: brighter sun, softer ring light, LEDs as small accents
    SUN_WARMTH, SUN_STRENGTH = DAY_LIGHTS["SUN_WARMTH"], DAY_LIGHTS["SUN_STRENGTH"]
    LAMP_STRENGTH, NEON_STRENGTH = DAY_LIGHTS["LAMP_STRENGTH"], DAY_LIGHTS["NEON_STRENGTH"]
DAYLIGHT = min(1.0, SUN_STRENGTH / 3.0)    # 1 = bright room, small = night


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


def hue_hex(h):
    """Hue 0..1 -> bright '#RRGGBB' (for the RGB keyboard)."""
    return "#%02X%02X%02X" % tuple(int(c * 255) for c in colorsys.hsv_to_rgb(h % 1.0, 0.85, 1.0))


def shade(hex_color, f):
    """A lighter (f > 1) or darker (f < 1) version of a hex colour."""
    h = hex_color.lstrip("#")
    return "#%02X%02X%02X" % tuple(max(0, min(255, int(int(h[i:i + 2], 16) * f))) for i in (0, 2, 4))


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


LED_EMIT = 3.0 * max(NEON_STRENGTH, 0.4)   # how hard the LED strips glow


def neon(n, power=1.0):
    """Glowing LED material: n = 1, 2 or 3 (the theme's neon_1 / neon_2 / neon_3 colours)."""
    key = f"neon_{n}"
    return mat(key, 0.3, emit=round(LED_EMIT * power, 2), color=COLORS[key])


def neon_rgb(n):
    return lin(COLORS[f"neon_{n}"])[:3]


def glass(key="glass", alpha=0.07, color="#E4ECF4"):
    """Clear tempered glass (window panes; the PC uses a slightly tinted, more visible version)."""
    m = mat(key, 0.03, color=color)
    if not m.get("kit_glass"):
        _set(_principled(m), ["Alpha"], alpha)
        for attr, value in (("surface_render_method", "BLENDED"), ("blend_method", "BLEND")):
            if hasattr(m, attr):                      # Blender 4.2+ / older Eevee: smooth (not grainy) blending
                try:
                    setattr(m, attr, value)
                    break
                except TypeError:
                    pass
        m["kit_glass"] = True
    return m


# Shared real-world materials. Each (key, roughness, metal) combination is used for ONE kind of surface,
# because surface() changes the cached material in place.
STEEL = surface(mat("dark", 0.4, metal=0.7), "brushed") if NIGHT else surface(mat("cream", 0.4, metal=0.25), "brushed")
ALU = surface(mat("alu", 0.3, metal=1.0, color="#A3A7AF"), "brushed")          # polished aluminium (chair base)
CHROME = mat("chrome", 0.15, metal=1.0, color="#C9CDD4")
PLASTIC = mat("dark", 0.5)                                                      # matt black plastic parts
SCREEN_BLACK = mat("dark", 0.25)                                                # monitor / TV housings
WOOD = surface(mat("wood", 0.5), "veneer" if NIGHT else "paper", scale=3.0)   # KALLAX / LACK foil: black-brown oak
#                                                     at night, plain white matt foil (no visible grain) by day


# --------------------------------------------------------------------- mesh helpers
def _finish(o, material, bevel, coll, parent):
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
    o.data.polygons.foreach_set("use_smooth", [True] * len(o.data.polygons))
    (coll or (COL_FURN if parent is not None else COL_ROOM)).objects.link(o)
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


def merged(name, parts, material, bevel=0.0, coll=None, parent=None):
    """Many boxes in ONE object (floor planks, keycaps...). parts = [(size, centre), ...]."""
    bm = bmesh.new()
    for size, loc in parts:
        vs = bmesh.ops.create_cube(bm, size=1.0)["verts"]
        bmesh.ops.scale(bm, vec=Vector(size), verts=vs)
        bmesh.ops.translate(bm, vec=Vector(loc), verts=vs)
    o = _obj(name, bm)
    return _finish(o, material, bevel, coll, parent)


def cyl(name, r, h, loc, material, r2=None, segs=32, bevel=0.002, rot=(0, 0, 0), coll=None, parent=None):
    """Cylinder (or tapered cylinder with r2). loc = centre."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=segs, radius1=r, radius2=r if r2 is None else r2, depth=h)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, bevel, coll, parent)


def ball(name, r, loc, material, scale=(1, 1, 1), coll=None, parent=None, rot=(0, 0, 0)):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=24, v_segments=14, radius=r)
    o = _obj(name, bm)
    o.location, o.scale, o.rotation_euler = loc, scale, rot
    return _finish(o, material, 0, coll, parent)


def tube(name, p1, p2, r, material, parent=None, segs=12, coll=None):
    """Round rod from point p1 to point p2 (in the parent's space)."""
    a, b = Vector(p1), Vector(p2)
    o = cyl(name, r, (b - a).length, (a + b) / 2, material, segs=segs, bevel=0, parent=parent, coll=coll)
    o.rotation_euler = (b - a).to_track_quat("Z", "Y").to_euler()
    return o


def polyline(name, pts, r, material, parent=None, segs=10):
    """Bent rod through a list of points (cables, T-moulding, piping)."""
    pts = [Vector(p) for p in pts]
    for a, b in zip(pts, pts[1:]):
        tube(name, a, b, r, material, parent=parent, segs=segs)
    for p in pts[1:-1]:
        ball(name + "_Joint", r, p, material, parent=parent)


def pillow(name, size, loc, material, rot=(0, 0, 0), parent=None):
    """Scatter cushion: square front, puffed middle, thin pinched edges (a squashed 'super-sphere')."""
    w, t, h = size
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=20, radius=1.0)
    for v in bm.verts:
        x, y, z = v.co
        sx, sz = math.copysign(abs(x) ** 0.3, x), math.copysign(abs(z) ** 0.3, z)
        edge = max(abs(sx), abs(sz)) ** 6                 # 0 in the middle, 1 at the seam
        v.co = (sx * w / 2, y * t / 2 * (1 - 0.8 * edge), sz * h / 2)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, 0, None, parent)


def torus(name, radius, thickness, loc, material, rot=(0, 0, 0), parent=None, segs=48, rsegs=12):
    """Ring standing up and facing -Y (mug handles)."""
    bm = bmesh.new()
    rings = []
    for i in range(segs):
        a = 2 * math.pi * i / segs
        rings.append([bm.verts.new((math.cos(a) * (radius + math.cos(b) * thickness), math.sin(b) * thickness,
                                    math.sin(a) * (radius + math.cos(b) * thickness)))
                      for b in (2 * math.pi * j / rsegs for j in range(rsegs))])
    for i in range(segs):
        r1, r2 = rings[i], rings[(i + 1) % segs]
        for j in range(rsegs):
            bm.faces.new((r1[j], r2[j], r2[(j + 1) % rsegs], r1[(j + 1) % rsegs]))
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, 0, None, parent)


def ring_disc(name, r_out, r_in, depth, loc, material, rot=(0, 0, 0), parent=None, segs=64, bevel=0.0):
    """Flat ring (washer) facing -Y: a ring light, a speaker trim, a fan's RGB ring."""
    bm = bmesh.new()
    angles = [2 * math.pi * i / segs for i in range(segs)]
    fo, fi, bo, bi = ([bm.verts.new((math.cos(a) * r, y, math.sin(a) * r)) for a in angles]
                      for y, r in ((-depth / 2, r_out), (-depth / 2, r_in), (depth / 2, r_out), (depth / 2, r_in)))
    for i in range(segs):
        j = (i + 1) % segs
        bm.faces.new((fo[i], fo[j], fi[j], fi[i]))
        bm.faces.new((bo[i], bi[i], bi[j], bo[j]))
        bm.faces.new((fo[i], bo[i], bo[j], fo[j]))
        bm.faces.new((fi[i], fi[j], bi[j], bi[i]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, bevel, None, parent)


def extrude(name, pts, axis, t0, t1, material, bevel=0.004, parent=None, coll=None):
    """A flat outline (2D points, in order) pushed out along an axis.
    axis "X": points are (y, z) | "Y": points are (x, z) | "Z": points are (x, y)."""
    def v3(p, t):
        return {"X": (t, p[0], p[1]), "Y": (p[0], t, p[1]), "Z": (p[0], p[1], t)}[axis]
    bm = bmesh.new()
    a = [bm.verts.new(v3(p, t0)) for p in pts]
    b = [bm.verts.new(v3(p, t1)) for p in pts]
    n = len(pts)
    bm.faces.new(a)
    bm.faces.new(list(reversed(b)))
    for i in range(n):
        bm.faces.new((a[i], a[(i + 1) % n], b[(i + 1) % n], b[i]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    o = _obj(name, bm)
    return _finish(o, material, bevel, coll, parent)


def spring(name, p1, p2, radius, turns, wire, material, parent=None):
    """Coil spring from p1 to p2 (the exposed springs on a boom arm)."""
    a, b = Vector(p1), Vector(p2)
    cu = bpy.data.curves.new(name, "CURVE")
    cu.dimensions, cu.bevel_depth, cu.bevel_resolution = "3D", wire, 2
    sp = cu.splines.new("POLY")
    n = int(turns * 10)
    sp.points.add(n)
    for i in range(n + 1):
        t = i / n
        ang = t * turns * 2 * math.pi
        sp.points[i].co = (math.cos(ang) * radius, math.sin(ang) * radius, t * (b - a).length, 1)
    o = bpy.data.objects.new(name, cu)
    o.location, o.rotation_euler = a, (b - a).to_track_quat("Z", "Y").to_euler()
    o.data.materials.append(material)
    COL_FURN.objects.link(o)
    o.parent = parent
    return o


def group(name, loc, parent, rot=(0, 0, 0)):
    """Empty used as a pivot, e.g. a monitor turned towards the chair. Parts parented to it move with it."""
    e = bpy.data.objects.new(name, None)
    e.empty_display_size = 0.05
    e.location, e.rotation_euler = loc, rot
    (COL_FURN if parent is not None else COL_ROOM).objects.link(e)
    e.parent = parent
    return e


def no_shadow(o):
    if hasattr(o, "visible_shadow"):
        o.visible_shadow = False              # glowing parts and glass let light through
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


def deco_text(name, text, size, loc, material, parent=None, rot=(R(90), 0, 0), depth=0.003):
    """Small 3D text that is just decoration (not filled from profile.json)."""
    cu = bpy.data.curves.new(name, "FONT")
    cu.body, cu.size, cu.align_x, cu.align_y = text, size, "CENTER", "CENTER"
    cu.extrude, cu.bevel_depth = depth, depth * 0.4
    o = bpy.data.objects.new(name, cu)
    o.location, o.rotation_euler = loc, rot
    o.data.materials.append(material)
    (COL_FURN if parent is not None else COL_ROOM).objects.link(o)
    o.parent = parent
    return o


# --------------------------------------------------------------------- lights
def light(name, kind, energy, color, loc, aim=None, size=None, parent=None):
    """Light. With parent=, loc/aim are in the parent's local space (the light stays when that furniture is replaced)."""
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


def led_bar(name, length, loc, n, power, parent, along="X", light_aim=None, watts=0.0, light_at=None):
    """A thin glowing LED strip (and optionally a strip-shaped area light next to it, so it lights the room)."""
    size = {"X": (length, 0.012, 0.004), "Y": (0.012, length, 0.004)}[along]
    no_shadow(box(name, size, loc, neon(n, power), bevel=0.001, parent=parent))
    if watts and NEON_STRENGTH > 0:
        lo = light(f"Light_{name}", "AREA", watts * NEON_STRENGTH, neon_rgb(n), light_at or loc, aim=light_aim,
                   parent=parent)
        lo.data.shape = "RECTANGLE"
        lo.data.size, lo.data.size_y = length * 0.85, 0.06     # aimed lights keep their local X along the strip


# =====================================================================
#  ROOM SHELL
# =====================================================================
# Floor: a base slab plus oak-laminate planks (19 cm x 1.22 m) with staggered joints, in three tones.
box("Floor_Base", (W + T, D + T, 0.2), ((W - T) / 2, (D + T) / 2, -0.1), mat("wall_trim", 0.7), bevel=0.01)
PLANK_W, PLANK_L = 0.19, 1.22
# scale=3.6 keeps the oak grain fine, like real laminate (coarser values look smeared)
plank_mats = [surface(mat("floor", 0.42 + 0.05 * k, color=shade(COLORS["floor"], f)), "wood", scale=3.6, along="Y")
              for k, f in enumerate((1.0, 0.94, 1.06))]        # subtle plank-to-plank variation, like real laminate
rows = round(W / PLANK_W)
pw = W / rows
plank_parts = [[], [], []]
for i in range(rows):
    y = -random.uniform(0.1, PLANK_L - 0.1)           # each row starts at a different joint
    while y < D:
        y0, y1 = max(y, 0.0), min(y + PLANK_L, D)
        if y1 - y0 > 0.04:
            plank_parts[random.randrange(3)].append(((pw - 0.003, y1 - y0 - 0.003, FLOOR_Z),
                                                     (pw * (i + 0.5), (y0 + y1) / 2, FLOOR_Z / 2)))
        y += PLANK_L
for k, parts in enumerate(plank_parts):
    merged(f"Floor_Planks_{k}", parts, plank_mats[k], bevel=0.0015)

# Walls: painted plaster. A casement window opening in the left wall (above the sofa).
WIN_Y = (0.9, 2.2)                  # from front to back
WIN_Z = (0.95, 2.3)                 # real sill height ~0.9 m
wall_m = surface(mat("wall", 0.9), "plaster", scale=14)    # fine scale: smooth emulsion paint, not blotchy stucco
left = box("Wall_Left", (T, D + T, H), (-T / 2, (D + T) / 2, H / 2), wall_m, bevel=0.0)
cutter = box("Window_Cutter", (T * 3, WIN_Y[1] - WIN_Y[0], WIN_Z[1] - WIN_Z[0]),
             (-T / 2, sum(WIN_Y) / 2, sum(WIN_Z) / 2), wall_m, bevel=0.0)
cutter.hide_render = cutter.hide_viewport = True
boolean = left.modifiers.new("Window", "BOOLEAN")
boolean.operation, boolean.object = "DIFFERENCE", cutter
bev = left.modifiers.new("Bevel", "BEVEL")
bev.width, bev.segments, bev.limit_method = 0.006, 2, "ANGLE"
box("Wall_Back", (W + T, T, H), ((W - T) / 2, D + T / 2, H / 2), wall_m, bevel=0.006)

# Cut-away trim on top of the walls (the "diorama" edge) and real skirting boards with a top bead.
box("Trim_Top_Back", (W + T + 0.04, T + 0.04, 0.06), ((W - T) / 2, D + T / 2, H + 0.03), mat("wall_trim", 0.5), bevel=0.01)
box("Trim_Top_Left", (T + 0.04, D + T + 0.04, 0.06), (-T / 2, (D + T) / 2 - 0.02, H + 0.03), mat("wall_trim", 0.5), bevel=0.01)
skirt = mat("wall_trim", 0.45) if NIGHT else mat("cream", 0.45)
box("Skirting_Back", (W, 0.014, 0.09), (W / 2, D - 0.007, FLOOR_Z + 0.045), skirt, bevel=0.002)
box("Skirting_Back_Bead", (W, 0.008, 0.014), (W / 2, D - 0.016, FLOOR_Z + 0.083), skirt, bevel=0.003)
box("Skirting_Left", (0.014, D, 0.09), (0.007, D / 2, FLOOR_Z + 0.045), skirt, bevel=0.002)
box("Skirting_Left_Bead", (0.008, D, 0.014), (0.016, D / 2, FLOOR_Z + 0.083), skirt, bevel=0.003)

# uPVC casement window: outer frame, centre mullion, two sashes with glass, a lever handle and a window board.
wy, wz = sum(WIN_Y) / 2, sum(WIN_Z) / 2
ww, wh = WIN_Y[1] - WIN_Y[0], WIN_Z[1] - WIN_Z[0]
pvc = mat("dark", 0.41) if NIGHT else mat("cream", 0.41)      # anthracite at night, white by day
FX = -T / 2 - 0.015
for nm, size, loc in [
    ("Top", (0.07, ww, 0.06), (FX, wy, WIN_Z[1] - 0.03)),
    ("Bottom", (0.07, ww, 0.06), (FX, wy, WIN_Z[0] + 0.03)),
    ("Front", (0.07, 0.06, wh), (FX, WIN_Y[0] + 0.03, wz)),
    ("Back", (0.07, 0.06, wh), (FX, WIN_Y[1] - 0.03, wz)),
    ("Mullion", (0.07, 0.07, wh), (FX, wy, wz)),
]:
    box(f"Window_Frame_{nm}", size, loc, pvc, bevel=0.004)
for s, (y0, y1) in enumerate(((WIN_Y[0] + 0.06, wy - 0.035), (wy + 0.035, WIN_Y[1] - 0.06))):
    sy, sw = (y0 + y1) / 2, y1 - y0
    z0, z1 = WIN_Z[0] + 0.06, WIN_Z[1] - 0.06
    for nm, size, loc in [("T", (0.05, sw, 0.055), (FX + 0.02, sy, z1 - 0.0275)),
                          ("B", (0.05, sw, 0.07), (FX + 0.02, sy, z0 + 0.035)),
                          ("F", (0.05, 0.055, z1 - z0), (FX + 0.02, y0 + 0.0275, (z0 + z1) / 2)),
                          ("K", (0.05, 0.055, z1 - z0), (FX + 0.02, y1 - 0.0275, (z0 + z1) / 2))]:
        box(f"Window_Sash{s}_{nm}", size, loc, pvc, bevel=0.004)
    no_shadow(box(f"Window_Glass_{s}", (0.006, sw - 0.1, z1 - z0 - 0.11), (FX + 0.02, sy, (z0 + z1) / 2 + 0.005),
                  glass(), bevel=0))
handle_m = mat("cream", 0.3) if not NIGHT else mat("handle", 0.3, metal=0.8, color="#B9BCC2")
box("Window_Handle_Base", (0.012, 0.03, 0.075), (FX + 0.051, wy + 0.065, wz), handle_m, bevel=0.004)
box("Window_Handle_Lever", (0.016, 0.018, 0.11), (FX + 0.064, wy + 0.065, wz - 0.045), handle_m, bevel=0.006)
box("Window_Board", (T / 2 + 0.04, ww + 0.1, 0.025), ((-T / 2 + 0.04) / 2, wy, WIN_Z[0] - 0.0125),
    mat("cream", 0.35), bevel=0.003)
# Roller blind, a third of the way down: cassette, fabric, bottom bar and a bead chain.
blind_m = surface(mat("cream", 0.93), "fabric", scale=5) if not NIGHT else \
    surface(mat("main", 0.93, color="#474B63"), "fabric", scale=5)            # scale 5: even blackout fabric
drop = wh * 0.3
box("Blind_Cassette", (0.05, ww - 0.01, 0.055), (-0.035, wy, WIN_Z[1] - 0.0275), pvc, bevel=0.008)
box("Blind_Fabric", (0.003, ww - 0.04, drop), (-0.03, wy, WIN_Z[1] - 0.055 - drop / 2), blind_m, bevel=0)
box("Blind_BottomBar", (0.012, ww - 0.04, 0.02), (-0.03, wy, WIN_Z[1] - 0.055 - drop - 0.008), pvc, bevel=0.003)
tube("Blind_Chain", (-0.02, WIN_Y[1] - 0.035, WIN_Z[1] - 0.06), (-0.02, WIN_Y[1] - 0.035, WIN_Z[1] - 0.8), 0.002,
     CHROME, segs=6)

# The view outside: sky, a row of city buildings with lit windows and (at night) rain.
SKY_X = -T - 0.45
box("Outside_Sky", (0.02, ww + 0.8, wh + 0.6), (SKY_X, wy + 0.3, wz - 0.25), mat("sky", 1.0, emit=1.0 if NIGHT else 0.6), bevel=0)
city = mat("city", 0.9, color="#0B0E22" if NIGHT else "#D9DFE8")
lit = [mat("lit", 0.5, emit=2.5, color=c) for c in ("#FFD27A", "#7FE8FF", "#C99BFF", "#FF8CC6")]
x_city = SKY_X + 0.12
y = WIN_Y[0] - 0.1
while y < WIN_Y[1] + 0.6:
    bw, bh = random.uniform(0.12, 0.24), random.uniform(0.3, 0.85)
    box("Outside_Building", (0.03, bw, bh), (x_city, y + bw / 2, WIN_Z[0] - 0.4 + bh / 2), city, bevel=0)
    if NIGHT:
        for wx in range(int(bw / 0.05)):
            for wz_ in range(int(bh / 0.07)):
                if random.random() < 0.3:
                    box("Outside_LitWindow", (0.005, 0.022, 0.03),
                        (x_city + 0.018, y + 0.025 + wx * 0.05, WIN_Z[0] - 0.4 + 0.05 + wz_ * 0.07),
                        random.choice(lit), bevel=0)
    y += bw + 0.01
if NIGHT and RAIN:
    drop_m = mat("rain", 0.2, emit=1.4, color="#9FC8FF")
    for k in range(60):                                       # slanted rain streaks just outside the glass
        dy, dz = random.uniform(WIN_Y[0] + 0.08, WIN_Y[1] - 0.08), random.uniform(WIN_Z[0] + 0.1, WIN_Z[1] - 0.1)
        box("Outside_Rain", (0.003, 0.003, random.uniform(0.05, 0.11)), (-T - 0.06, dy, dz), drop_m, bevel=0,
            rot=(R(-12), 0, 0))

# LED strip tape along the top of both walls: purple on the back wall, cyan on the left wall.
COVE_WATTS = 160 if NIGHT else 40          # by day the strips barely light the wall (no hot band)
led_bar("LED_Cove_Back", W - 0.1, (W / 2, D - 0.008, H - 0.06), 1, 1.0, None, "X",
        light_at=(W / 2, D - 0.3, H - 0.12), light_aim=(W / 2, D, H - 1.4), watts=COVE_WATTS)
led_bar("LED_Cove_Left", D - 0.1, (0.008, D / 2, H - 0.06), 2, 1.0, None, "Y",
        light_at=(0.3, D / 2, H - 0.12), light_aim=(0, D / 2, H - 1.4), watts=COVE_WATTS)

# Hexagon light panels (23 x 20 cm, pointy-top) in an organic cluster on the left wall, above the arcade.
HEX_R = 0.115                                       # centre to corner
HEX_FLAT = HEX_R * math.sqrt(3) + 0.006             # centre-to-centre distance of neighbours
hex_body = mat("hexbody", 0.35, color="#D9DBE2")
for k, (q, r) in enumerate([(0, 0), (1, 0), (0, 1), (-1, 1), (1, -1), (2, -1), (-1, 2)]):
    hy = 2.95 + (q + r / 2 - 0.5) * HEX_FLAT
    hz = 2.05 + (r - 0.5) * 1.5 * HEX_R * 1.03
    cyl("Wall_HexPanel", HEX_R, 0.008, (0.004, hy, hz), hex_body, segs=6, bevel=0.002, rot=(0, R(90), 0))
    no_shadow(cyl("Wall_HexPanel_Glow", HEX_R - 0.014, 0.002, (0.009, hy, hz), neon(1 + (k * 2) % 3, 0.6), segs=6,
                  bevel=0, rot=(0, R(90), 0)))
if NEON_STRENGTH > 0:
    light("Light_HexPanels", "POINT", 14 * NEON_STRENGTH, neon_rgb(3), (0.3, 2.95, 2.05), size=0.35)

# Acoustic wedge foam (30 x 30 x 5 cm tiles, 12 wedges each) behind the desk, ridges alternating like a checkerboard.
DESK_X = W - 0.05 - 0.8                       # the desk sits on the right part of the back wall
foam_a = surface(mat("dark", 0.97), "concrete") if NIGHT else surface(mat("main", 0.97), "concrete")
foam_b = surface(mat("accent_1", 0.97, color=shade(COLORS["accent_1"], 0.55)), "concrete") if NIGHT \
    else surface(mat("cream", 0.97), "concrete")
saw = [(0, 0), (0.3, 0), (0.3, 0.012)]
for k in range(11, -1, -1):
    saw += [(k * 0.025 + 0.0125, 0.05), (k * 0.025, 0.012)]
for c in range(5):
    for r in range(2):
        x0, z0 = DESK_X - 0.75 + c * 0.3, 0.98 + r * 0.3
        m = foam_a if (c + r) % 2 else foam_b
        if (c + r) % 2:                                       # vertical wedges
            extrude("Wall_Foam", [(x0 + u, D - v) for u, v in saw], "Z", z0, z0 + 0.3, m, bevel=0)
        else:                                                 # horizontal wedges
            extrude("Wall_Foam", [(D - v, z0 + u) for u, v in saw], "X", x0, x0 + 0.3, m, bevel=0)

# =====================================================================
#  FURNITURE SLOTS  (names from the shared vocabulary in SPEC.md)
#  size = (width, depth, height); front of the furniture faces local -Y. Real product sizes.
# =====================================================================
slot("desk",       (1.6, 1.1, 0.75),   (DESK_X, D - 0.02 - 0.55), shape="table")             # 160 x 110 L-desk
slot("monitor",    (1.15, 0.34, 0.65), (DESK_X, D - 0.21), z=FLOOR_Z + 0.75, kind="surface", shape="monitor")
slot("speaker",    (0.15, 0.2, 0.24),  (DESK_X - 0.71, D - 0.16), z=FLOOR_Z + 0.75, kind="surface", shape="box")
slot("chair",      (0.7, 0.7, 1.36),   (DESK_X - 0.22, 2.53), turn=180, shape="chair")      # pulled up, facing the screens
slot("floor_lamp", (0.6, 0.6, 1.75),   (2.3, 2.8), turn=68, shape="lamp")                    # ring light aimed at the chair
slot("sofa",       (1.8, 0.88, 0.66),  (0.47, 1.55), turn=90, shape="sofa")                  # KLIPPAN under the window
slot("hero_prop",  (0.51, 0.52, 1.54), (0.29, 2.98), turn=90, shape="cabinet")               # arcade cabinet + riser
slot("shelf",      (1.47, 0.39, 0.77), (0.835, D - 0.205), shape="shelf")                    # KALLAX 2x4 on its side
slot("wall_art",   (0.9, 0.05, 1.0),   (2.17, D - 0.025), z=1.05, kind="wall", shape="frame")
slot("rug",        (2.2, 1.55, 0.012), (3.2, 2.3), kind="rug", shape="rug")                  # 155 x 220 flatweave


# =====================================================================
#  PLACEHOLDER FURNITURE  (replaced when you add your own with add_furniture.py)
# =====================================================================
def bookshelf_speaker(name, parent, loc, turn, knobs=False):
    """Powered bookshelf speaker (Edifier R1280T-style, 14.6 x 19.6 x 23.4 cm): wood box, black baffle."""
    g = group(name, loc, parent, rot=(0, 0, R(turn)))
    sw, sd, sh = 0.146, 0.196, 0.234
    wood_m = surface(mat("speaker_wood", 0.5, color="#7A4C30" if NIGHT else "#EFEBE4"), "veneer")
    baffle = mat("baffle", 0.6, color="#1B1B1F" if NIGHT else "#DCDCE0")
    trim = mat("trim", 0.25, metal=1.0, color="#B4B8BF")
    cone = mat("cone", 0.7, color="#141417")
    box(name + "_Cabinet", (sw, sd, sh), (0, 0, sh / 2), wood_m, bevel=0.003, parent=g)
    box(name + "_Baffle", (sw - 0.002, 0.005, sh - 0.002), (0, -sd / 2 - 0.0015, sh / 2), baffle, bevel=0.002, parent=g)
    yf = -sd / 2 - 0.004
    ring_disc(name + "_WooferTrim", 0.057, 0.047, 0.004, (0, yf, 0.085), trim, parent=g)
    cyl(name + "_WooferCone", 0.047, 0.004, (0, yf + 0.002, 0.085), cone, rot=(R(90), 0, 0), parent=g)
    ball(name + "_DustCap", 0.017, (0, yf, 0.085), cone, scale=(1, 0.35, 1), parent=g)
    ring_disc(name + "_TweeterTrim", 0.022, 0.011, 0.004, (0, yf, 0.183), trim, parent=g)
    ball(name + "_Tweeter", 0.011, (0, yf, 0.183), trim, scale=(1, 0.5, 1), parent=g)
    if knobs:                                                       # volume / treble / bass on the side
        for k, z in enumerate((0.055, 0.095, 0.135)):
            cyl(name + "_Knob", 0.011, 0.012, (sw / 2 + 0.006, 0.03, z), mat("dark", 0.35), rot=(0, R(90), 0), parent=g)
    return g


def keyboard(parent, loc, rz):
    """Tenkeyless mechanical keyboard (36 x 13 cm): real key rows, Esc gap, arrow cluster, RGB under-glow at night."""
    kb = group("Desk_Keyboard", loc, parent, rot=(0, 0, rz))
    box("Keyboard_Case", (0.357, 0.132, 0.024), (0, 0, 0.012), mat("dark", 0.44) if NIGHT else mat("cream", 0.44),
        bevel=0.004, parent=kb)
    U = 0.019
    rows = [[1, -1, 1, 1, 1, 1, -0.5, 1, 1, 1, 1, -0.5, 1, 1, 1, 1, -0.5, 1, 1, 1],
            [1] * 13 + [2, -0.5, 1, 1, 1],
            [1.5] + [1] * 12 + [1.5, -0.5, 1, 1, 1],
            [1.75] + [1] * 11 + [2.25],
            [2.25] + [1] * 10 + [2.75, -1.5, 1],
            [1.25] * 3 + [6.25] + [1.25] * 4 + [-0.5, 1, 1, 1]]
    caps, mods = [], []
    for r, row in enumerate(rows):
        x = -18.5 * U / 2
        y = 0.052 if r == 0 else 0.0285 - (r - 1) * U
        for kw in row:
            if kw > 0:
                part = ((kw * U - 0.003, U - 0.003, 0.009), (x + kw * U / 2, y, 0.029))
                (caps if kw == 1 and r > 0 else mods).append(part)
            x += abs(kw) * U
    merged("Keyboard_Keys", caps, mat("dark", 0.56) if NIGHT else mat("cream", 0.56), bevel=0.0015, parent=kb)
    merged("Keyboard_Mods", mods, mat("keymod", 0.56, color="#2C2E36" if NIGHT else "#C3C7CF"), bevel=0.0015, parent=kb)
    if NIGHT:                                                       # light bleeding between the black keycaps
        for b in range(6):
            no_shadow(box("Keyboard_Glow", (0.057, 0.118, 0.002), (-0.1475 + b * 0.059, 0, 0.0245),
                          mat("key", 0.4, emit=1.8, color=hue_hex(0.55 + b / 6 * 0.9)), bevel=0, parent=kb))
    return kb


def pc_tower(parent, loc):
    """Dual-chamber glass PC case (Lian Li O11 Dynamic EVO-style, 28.5 x 46.5 x 45.9 cm): pillar-less glass front +
    side, brushed aluminium rails, 6 RGB fans, horizontal GPU, AIO pump and RAM with light bars."""
    pc = group("Desk_PC", loc, parent)
    tw, td, th = 0.285, 0.465, 0.459
    shell = surface(mat("dark", 0.38, metal=0.8), "brushed") if NIGHT else surface(mat("cream", 0.38, metal=0.3), "brushed")
    inner = mat("dark", 0.62) if NIGHT else mat("pc_inner", 0.62, color="#E4E4E7")
    pcb = mat("pcb", 0.5, color="#202229")
    box("PC_Bottom", (tw, td, 0.045), (0, 0, 0.0225), shell, bevel=0.004, parent=pc)
    box("PC_Top", (tw, td, 0.03), (0, 0, th - 0.015), shell, bevel=0.004, parent=pc)
    merged("PC_TopVents", [((tw - 0.08, 0.004, 0.002), (0.01, -td / 2 + 0.05 + k * 0.012, th + 0.0005)) for k in range(31)],
           mat("vent", 0.7, color="#141418" if NIGHT else "#9A9CA3"), parent=pc)     # fine slots of the vented top
    box("PC_Back", (tw, 0.012, th - 0.075), (0, td / 2 - 0.006, th / 2), shell, bevel=0.002, parent=pc)
    box("PC_SidePanel", (0.012, td, th - 0.075), (-tw / 2 + 0.006, 0, th / 2), shell, bevel=0.002, parent=pc)
    for sx, sy in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
        box("PC_Foot", (0.04, 0.06, 0.012), (sx * (tw / 2 - 0.03), sy * (td / 2 - 0.05), -0.006), PLASTIC, bevel=0.003,
            parent=pc)
    # Inside: motherboard tray (rear chamber behind it), board, RAM, AIO pump with hoses, GPU, fans.
    xt = -tw / 2 + 0.07
    box("PC_Tray", (0.006, td - 0.03, th - 0.08), (xt, 0, th / 2), inner, bevel=0, parent=pc)
    mz = th - 0.05 - 0.122
    box("PC_Motherboard", (0.004, 0.305, 0.244), (xt + 0.005, 0.04, mz), pcb, bevel=0, parent=pc)
    for k in range(4):
        box("PC_RAM", (0.03, 0.007, 0.12), (xt + 0.022, -0.045 + k * 0.011, mz + 0.03), PLASTIC, bevel=0.001, parent=pc)
        no_shadow(box("PC_RAM_Light", (0.006, 0.0075, 0.118), (xt + 0.039, -0.045 + k * 0.011, mz + 0.03),
                      neon(1 + k % 2, 0.9), bevel=0, parent=pc))
    pump = Vector((xt + 0.022, 0.07, mz + 0.03))
    cyl("PC_Pump", 0.034, 0.03, pump, PLASTIC, rot=(0, R(90), 0), parent=pc)
    no_shadow(ring_disc("PC_Pump_Ring", 0.034, 0.024, 0.003, pump + Vector((0.016, 0, 0)), neon(2, 1.0),
                        rot=(0, 0, R(90)), parent=pc))
    for dy in (-0.012, 0.012):
        polyline("PC_Hose", [pump + Vector((0.0, dy, 0.03)), pump + Vector((0.03, dy, 0.09)),
                             Vector((xt + 0.1, 0.12 + dy, th - 0.06))], 0.006, PLASTIC, parent=pc)
    gz = mz - 0.122 + 0.05
    box("PC_GPU", (0.13, 0.31, 0.055), (xt + 0.072, -0.0, gz), mat("dark", 0.45) if NIGHT else mat("cream", 0.45),
        bevel=0.004, parent=pc)
    no_shadow(box("PC_GPU_Light", (0.003, 0.25, 0.008), (xt + 0.1385, -0.02, gz + 0.012), neon(2, 1.0), bevel=0, parent=pc))
    fan_x = (xt + tw / 2) / 2 + 0.003
    for k in range(3):
        for z, tilt in ((0.06, R(-90)), (th - 0.055, R(90))):         # 3 intake fans at the bottom, 3 on the radiator
            fy = -0.145 + k * 0.145
            side = 1 if tilt < 0 else -1                            # +1: fan faces up (bottom intake)
            box("PC_Fan_Frame", (0.12, 0.12, 0.008), (fan_x, fy, z - side * 0.009), mat("fan", 0.5, color="#2A2C33" if NIGHT
                else "#F2F2F4"), bevel=0.003, parent=pc)
            no_shadow(ring_disc("PC_Fan_Ring", 0.058, 0.05, 0.016, (fan_x, fy, z + side * 0.004),
                                neon(1 + (k + (z > 0.2)) % 2, 1.0), rot=(tilt, 0, 0), parent=pc))
            cyl("PC_Fan_Hub", 0.02, 0.027, (fan_x, fy, z), PLASTIC, parent=pc)
            for b in range(7):                                      # seven pitched blades (translucent at night)
                a = 2 * math.pi * b / 7 + k
                box("PC_Fan_Blade", (0.028, 0.02, 0.002), (fan_x + math.cos(a) * 0.034, fy + math.sin(a) * 0.034, z),
                    mat("blade", 0.4, color="#3A3550" if NIGHT else "#FFFFFF"), bevel=0.0008, rot=(R(28), 0, a),
                    parent=pc)
    # VRM heatsinks, the sleeved 24-pin cable and a GPU backplate, so the build reads through the glass.
    hs_m = surface(mat("heatsink", 0.35, metal=1.0, color="#8E939C" if NIGHT else "#D6D8DC"), "brushed")
    box("PC_VRM_Heatsink", (0.02, 0.1, 0.03), (xt + 0.016, 0.06, mz + 0.105), hs_m, bevel=0.003, parent=pc)
    box("PC_VRM_Heatsink2", (0.02, 0.03, 0.09), (xt + 0.016, 0.155, mz + 0.06), hs_m, bevel=0.003, parent=pc)
    box("PC_Chipset", (0.012, 0.07, 0.07), (xt + 0.012, 0.12, mz - 0.085), hs_m, bevel=0.003, parent=pc)
    box("PC_24Pin", (0.022, 0.014, 0.1), (xt + 0.018, -0.115, mz - 0.01), mat("sleeve", 0.7, color="#2B2D34" if NIGHT
        else "#F0F0F2"), bevel=0.005, parent=pc)
    box("PC_GPU_Backplate", (0.13, 0.31, 0.003), (xt + 0.072, 0.0, gz + 0.029), hs_m, bevel=0.001, parent=pc)
    # Pillar-less tempered glass on the front and the right side, slightly tinted, with the black silk-screened
    # border real glass panels have along the top and bottom (no pillar where the two panes meet).
    pc_glass = glass("pc_glass", 0.2, "#B9C3D0")
    gh = th - 0.075
    no_shadow(box("PC_Glass_Side", (0.004, td - 0.004, gh), (tw / 2 - 0.002, 0, th / 2), pc_glass, bevel=0.001, parent=pc))
    no_shadow(box("PC_Glass_Front", (tw - 0.014, 0.004, gh), (0.005, -td / 2 + 0.002, th / 2), pc_glass, bevel=0.001,
                  parent=pc))
    ink = mat("glass_ink", 0.2, color="#0B0B0E")
    for z in (th / 2 - gh / 2 + 0.008, th / 2 + gh / 2 - 0.008):
        box("PC_Glass_Border", (0.0015, td - 0.004, 0.016), (tw / 2 - 0.0045, 0, z), ink, bevel=0, parent=pc)
        box("PC_Glass_Border", (tw - 0.014, 0.0015, 0.016), (0.005, -td / 2 + 0.0045, z), ink, bevel=0, parent=pc)
    box("PC_Glass_Border", (0.0015, 0.016, gh), (tw / 2 - 0.0045, td / 2 - 0.01, th / 2), ink, bevel=0, parent=pc)
    box("PC_Glass_Border", (0.016, 0.0015, gh), (-tw / 2 + 0.02, -td / 2 + 0.0045, th / 2), ink, bevel=0, parent=pc)
    light("Light_PC", "POINT", 10 * NEON_STRENGTH, neon_rgb(1), (0.03, -0.05, th * 0.5), size=0.08, parent=pc)
    light("Light_PC_Glow", "POINT", 8 * NEON_STRENGTH, neon_rgb(1), (0.35, -0.35, th * 0.4), size=0.2, parent=pc)
    return pc


def build_desk():
    """L-shaped gaming desk (160 x 110 x 75 cm, 25 mm carbon-texture top on black steel sled legs, LED strip under
    the front lip) with the whole battlestation: desk mat, TKL keyboard, mouse, stream deck, headset stand, mug,
    spring boom arm + broadcast mic, right-hand speaker and a glass PC tower on the return."""
    root, w, d, h = furniture_root("desk")
    MAIN_D, RET_W, TOP = 0.6, 0.5, 0.025
    top_m = surface(mat("desk", 0.46), "fabric", scale=0.08) if NIGHT else surface(mat("desk", 0.46), "veneer")
    main_y, ret_len = d / 2 - MAIN_D / 2, d - MAIN_D
    box("Desk_Top_Main", (w, MAIN_D, TOP), (0, main_y, h - TOP / 2), top_m, bevel=0.003, parent=root)
    box("Desk_Top_Return", (RET_W, ret_len - 0.002, TOP), (w / 2 - RET_W / 2, -d / 2 + ret_len / 2 - 0.001, h - TOP / 2),
        top_m, bevel=0.003, parent=root)
    fz = h - TOP                                                    # underside of the top

    def sled(name, x, y, along, length):
        """Steel leg: square post, a foot bar on the floor with levelling glides and a bar under the top."""
        bar = (0.05, length, 0.03) if along == "Y" else (length, 0.05, 0.03)
        box(name + "_Post", (0.06, 0.06, fz - 0.06), (x, y, fz / 2), STEEL, bevel=0.004, parent=root)
        box(name + "_Foot", bar, (x, y, 0.025), STEEL, bevel=0.004, parent=root)
        box(name + "_TopBar", bar, (x, y, fz - 0.015), STEEL, bevel=0.004, parent=root)
        for s in (-1, 1):
            dx, dy = ((0, s * (length / 2 - 0.03)) if along == "Y" else (s * (length / 2 - 0.03), 0))
            cyl(name + "_Glide", 0.016, 0.01, (x + dx, y + dy, 0.005), PLASTIC, parent=root)

    sled("Desk_LegLeft", -w / 2 + 0.07, main_y, "Y", MAIN_D - 0.06)
    sled("Desk_LegRight", w / 2 - 0.07, 0, "Y", d - 0.06)
    sled("Desk_LegReturn", w / 2 - RET_W + 0.06, -d / 2 + 0.07, "X", 0.2)
    box("Desk_BackBeam", (w - 0.2, 0.03, 0.07), (0, d / 2 - 0.06, fz - 0.05), STEEL, bevel=0.003, parent=root)
    box("Desk_ReturnBeam", (0.03, ret_len, 0.05), (w / 2 - RET_W + 0.06, -d / 2 + ret_len / 2 + 0.03, fz - 0.04), STEEL,
        bevel=0.003, parent=root)
    led_bar("LED_Desk_Under", w - RET_W - 0.1, (-RET_W / 2, d / 2 - MAIN_D + 0.02, fz - 0.003), 3, 0.9, root, "X",
            light_aim=(-RET_W / 2, d / 2 - MAIN_D - 0.1, 0), watts=40)
    led_bar("LED_Desk_Return", ret_len - 0.1, (w / 2 - RET_W + 0.02, -d / 2 + ret_len / 2, fz - 0.003), 3, 0.9, root, "Y")

    # Desk mat (90 x 40 cm) with a stitched, glowing edge; keyboard, mouse, stream deck, mug.
    box("Desk_Mat_Edge", (0.9, 0.4, 0.003), (-0.14, 0.16, h + 0.0015), neon(2, 0.45) if NIGHT else mat("dark", 0.62),
        bevel=0, parent=root)
    box("Desk_Mat", (0.89, 0.39, 0.004), (-0.14, 0.16, h + 0.002), surface(mat("dark", 0.93), "fabric"), bevel=0.001,
        parent=root)
    keyboard(root, (-0.22, 0.17, h + 0.004), R(-3))
    ball("Desk_Mouse", 0.033, (0.13, 0.15, h + 0.024), mat("dark", 0.35) if NIGHT else mat("cream", 0.35),
         scale=(1, 1.9, 0.6), parent=root)
    cyl("Desk_Mouse_Wheel", 0.008, 0.006, (0.13, 0.12, h + 0.044), PLASTIC, rot=(0, R(90), 0), parent=root)
    if NIGHT:
        no_shadow(box("Desk_Mouse_Light", (0.03, 0.006, 0.004), (0.13, 0.208, h + 0.026), neon(2, 0.8), bevel=0, parent=root))
    sd_ = group("Desk_StreamDeck", (0.36, 0.06, h), root, rot=(0, 0, R(-14)))
    box("StreamDeck_Stand", (0.1, 0.07, 0.02), (0, 0.01, 0.01), PLASTIC, bevel=0.004, parent=sd_)
    tilt = Matrix.Rotation(R(40), 3, "X")
    centre = Vector((0, 0, 0.05))
    box("StreamDeck_Body", (0.118, 0.084, 0.025), centre, PLASTIC, bevel=0.005, rot=(R(40), 0, 0), parent=sd_)
    for c in range(5):
        for r in range(3):
            p = centre + tilt @ Vector((-0.044 + c * 0.022, -0.022 + r * 0.022, 0.013))
            box("StreamDeck_Key", (0.016, 0.016, 0.004), p, neon(1 + (c * 3 + r) % 3, 0.6), bevel=0.0015,
                rot=(R(40), 0, 0), parent=sd_)
    mug = Vector((-0.66, -0.01, h))
    cyl("Desk_Mug", 0.04, 0.095, mug + Vector((0, 0, 0.0475)), surface(mat("cream", 0.2), "ceramic"), segs=28,
        parent=root)
    cyl("Desk_Mug_Coffee", 0.036, 0.004, mug + Vector((0, 0, 0.083)), mat("coffee", 0.2, color="#3A2418"), parent=root)
    torus("Desk_Mug_Handle", 0.024, 0.006, mug + Vector((0.045, 0, 0.05)), surface(mat("cream", 0.2), "ceramic"),
          parent=root, segs=20, rsegs=8)
    # Headset on a stand at the left end of the desk.
    hs = Vector((-0.66, 0.2, h))
    cyl("HeadsetStand_Base", 0.055, 0.012, hs + Vector((0, 0, 0.006)), STEEL, parent=root)
    tube("HeadsetStand_Post", hs + Vector((0, 0, 0.01)), hs + Vector((0, 0, 0.28)), 0.009, STEEL, parent=root)
    box("HeadsetStand_Saddle", (0.13, 0.03, 0.016), hs + Vector((0, 0, 0.288)), STEEL, bevel=0.006, parent=root)
    band = [hs + Vector((math.cos(a) * 0.08, 0, 0.215 + math.sin(a) * 0.085)) for a in
            (R(0), R(30), R(60), R(90), R(120), R(150), R(180))]
    polyline("Headset_Band", band, 0.012, mat("dark", 0.45), parent=root)
    for sx in (-1, 1):
        cyl("Headset_Cup", 0.045, 0.035, hs + Vector((sx * 0.085, 0, 0.17)), mat("dark", 0.45), rot=(0, R(90), 0),
            parent=root)
        cyl("Headset_Cushion", 0.042, 0.02, hs + Vector((sx * 0.06, 0, 0.17)), surface(mat("dark", 0.92), "knit"),
            rot=(0, R(90), 0), parent=root)

    # Spring boom arm clamped to the back edge, and a broadcast dynamic mic swung toward the chair.
    p0 = Vector((-0.6, d / 2 - 0.035, h))
    box("MicArm_Clamp_Top", (0.05, 0.07, 0.02), p0 + Vector((0, 0, 0.01)), STEEL, bevel=0.004, parent=root)
    box("MicArm_Clamp_Spine", (0.05, 0.014, 0.09), p0 + Vector((0, 0.042, -0.025)), STEEL, bevel=0.003, parent=root)
    box("MicArm_Clamp_Jaw", (0.05, 0.06, 0.012), p0 + Vector((0, 0.01, -TOP - 0.03)), STEEL, bevel=0.003, parent=root)
    p1 = p0 + Vector((0, 0, 0.12))
    p2 = p1 + Vector((0.06, -0.13, 0.33))
    p3 = p2 + Vector((0.16, -0.36, -0.13))
    tube("MicArm_Post", p0, p1, 0.011, STEEL, parent=root)
    cyl("MicArm_Swivel", 0.02, 0.04, p1 - Vector((0, 0, 0.01)), STEEL, parent=root)
    spring_m = mat("spring", 0.35, metal=1.0, color="#BFC3CA")
    for a, b in ((p1, p2), (p2, p3)):
        dv = (b - a).normalized()
        side = dv.cross(Vector((0, 0, 1))).normalized()
        up = side.cross(dv).normalized()
        for s in (-1, 1):                                           # the two parallel rods of each section
            tube("MicArm_Rod", a + up * 0.012 * s, b + up * 0.012 * s, 0.0055, STEEL, parent=root, segs=8)
        spring("MicArm_Spring", a + dv * 0.06 + side * 0.016, b - dv * 0.1 + side * 0.016, 0.006, 16, 0.0013, spring_m,
               parent=root)
        cyl("MicArm_Knuckle", 0.018, 0.03, b, STEEL, rot=side.to_track_quat("Z", "Y").to_euler(), parent=root)
    mic = group("Desk_Mic", p3, root, rot=(0, 0, R(-24)))
    hook_link(mic, "email")                                         # click the mic to e-mail you
    mic_m = mat("dark", 0.42, metal=0.3)
    tube("Mic_Mount", (0, 0, 0), (0, 0, -0.03), 0.006, STEEL, parent=mic)
    box("Mic_Yoke_Top", (0.1, 0.022, 0.008), (0, 0, -0.034), mic_m, bevel=0.003, parent=mic)
    for sx in (-1, 1):
        box("Mic_Yoke_Side", (0.008, 0.022, 0.06), (sx * 0.046, 0, -0.064), mic_m, bevel=0.003, parent=mic)
        cyl("Mic_Yoke_Knob", 0.012, 0.012, (sx * 0.056, 0, -0.085), PLASTIC, rot=(0, R(90), 0), parent=mic)
    cyl("Mic_Body", 0.031, 0.12, (0, 0.02, -0.085), mic_m, rot=(R(90), 0, 0), bevel=0.004, parent=mic)
    foam = surface(mat("dark", 0.95), "knit")
    cyl("Mic_Windscreen", 0.037, 0.07, (0, -0.072, -0.085), foam, rot=(R(90), 0, 0), bevel=0.01, parent=mic)
    ball("Mic_Windscreen_Front", 0.037, (0, -0.107, -0.085), foam, scale=(1, 0.45, 1), parent=mic)
    cyl("Mic_XLR", 0.022, 0.02, (0, 0.088, -0.085), STEEL, rot=(R(90), 0, 0), parent=mic)
    polyline("Mic_Cable", [p3 + Vector((0.005, 0.03, -0.09)), p2 + Vector((0, 0.01, -0.02)), p1 + Vector((0.015, 0, 0)),
                           p0 + Vector((0.015, 0, 0.02))], 0.003, PLASTIC, parent=root)

    bookshelf_speaker("Desk_Speaker_R", root, (w / 2 - 0.13, d / 2 - 0.14, h), -18, knobs=True)
    pc_tower(root, (w / 2 - 0.025 - 0.1425, -d / 2 + 0.235 + 0.01, h))


def build_monitor():
    """34" ultrawide (80 x 33.5 cm panel) on a V-foot stand with a clip-on webcam, plus a 24" monitor in portrait."""
    root, w, d, h = furniture_root("monitor")
    stand = STEEL
    # Main ultrawide: the stream preview (a game scene, your webcam box and a LIVE badge).
    mon = group("Monitor_Main", (-0.18, 0.02, 0), root)
    # V-shaped foot: the apex sits under the column at the back, the two arms reach forward and outward under the
    # screen (how real ultrawide stands look from above).
    apex = Vector((0, 0.085, 0.011))                                # 4 mm above the desk: it stands on the desk mat
    for s in (-1, 1):
        tip = Vector((s * 0.22, -0.07, 0.011))
        arm = tip - apex
        box("Monitor_Foot", (arm.length, 0.036, 0.014), (apex + tip) / 2, stand, bevel=0.005,
            rot=(0, 0, math.atan2(arm.y, arm.x)), parent=mon)
        cyl("Monitor_FootPad", 0.012, 0.004, (tip.x, tip.y, 0.006), PLASTIC, parent=mon)
    cyl("Monitor_FootHub", 0.04, 0.016, (0, 0.085, 0.012), stand, segs=24, parent=mon)
    box("Monitor_Column", (0.06, 0.03, 0.34), (0, 0.075, 0.17), stand, bevel=0.006, parent=mon)
    box("Monitor_Back", (0.42, 0.05, 0.2), (0, 0.04, 0.38), SCREEN_BLACK, bevel=0.02, parent=mon)
    box("Monitor_Housing", (0.812, 0.018, 0.365), (0, 0.0, 0.38), SCREEN_BLACK, bevel=0.004, parent=mon)
    box("Monitor_Chin", (0.812, 0.02, 0.018), (0, 0.0, 0.38 - 0.1825 - 0.009), SCREEN_BLACK, bevel=0.004, parent=mon)
    box("Monitor_Webcam", (0.094, 0.03, 0.03), (0, 0.004, 0.578), PLASTIC, bevel=0.012, parent=mon)
    box("Monitor_Webcam_Clip", (0.04, 0.05, 0.008), (0, 0.02, 0.564), PLASTIC, bevel=0.003, parent=mon)
    ball("Monitor_Webcam_Lens", 0.009, (0, -0.011, 0.578), mat("lens", 0.1, color="#0A0D18"), parent=mon)
    s1 = hook_image("screen", 1, (0.796, 0.335), (0, -0.0095, 0.384), parent=mon, glow=True, default_key="dark")
    y_ui = -0.0105
    parts = []
    for k, key in enumerate(("accent_1", "accent_3", "accent_2")):  # sunset game sky in bands
        parts.append(box("Screen_GameSky", (0.78, 0.001, 0.09), (0, y_ui, 0.505 - k * 0.09),
                         mat(key, 0.4, emit=1.0 + 0.3 * k), bevel=0, parent=mon))
    for k, (x, bh) in enumerate([(-0.3, 0.08), (-0.16, 0.13), (0.02, 0.07), (0.2, 0.11)]):   # platforms
        parts.append(box("Screen_Platform", (0.12, 0.001, bh), (x, y_ui - 0.0005, 0.23 + bh / 2),
                         mat("dark", 0.5, emit=0.3), bevel=0, parent=mon))
    parts.append(box("Screen_Webcam_Box", (0.15, 0.001, 0.1), (0.3, y_ui - 0.001, 0.27), mat("cream", 0.4, emit=1.6),
                     bevel=0, parent=mon))
    parts.append(ball("Screen_Webcam_Face", 0.026, (0.3, y_ui - 0.002, 0.275), mat("accent_1", 0.5, emit=1.2),
                      scale=(1, 0.05, 1), parent=mon))
    parts.append(box("Screen_Live_Badge", (0.07, 0.001, 0.03), (-0.34, y_ui - 0.001, 0.525),
                     mat("live", 0.4, emit=2.5, color="#FF3B5C"), bevel=0, parent=mon))
    hook_default(s1, *parts)
    # 24" monitor turned to portrait on a round-base stand: the live chat.
    side = group("Monitor_Chat", (0.41, 0.03, 0), root, rot=(0, 0, R(-20)))
    cyl("Chat_Base", 0.09, 0.012, (0, 0.03, 0.006), stand, parent=side)
    box("Chat_Column", (0.045, 0.025, 0.2), (0, 0.06, 0.1), stand, bevel=0.005, parent=side)
    box("Chat_Housing", (0.312, 0.018, 0.545), (0, 0.0, 0.355), SCREEN_BLACK, bevel=0.004, parent=side)
    s2 = hook_image("screen", 2, (0.296, 0.528), (0, -0.0095, 0.357), parent=side, glow=True, default_key="dark")
    ui = [mat(k, 0.4, emit=1.6) for k in ("accent_2", "accent_1", "accent_3", "cream")]
    bubbles = []
    for r in range(10):
        L = random.uniform(0.08, 0.2)
        x = -0.12 + L / 2
        bubbles.append(box("Chat_Name", (0.03, 0.001, 0.014), (-0.125, -0.0105, 0.585 - r * 0.048), random.choice(ui[:3]),
                           bevel=0, parent=side))
        bubbles.append(box("Chat_Line", (L, 0.001, 0.014), (x + 0.03, -0.0105, 0.585 - r * 0.048), ui[3], bevel=0,
                           parent=side))
    hook_default(s2, *bubbles)
    # Bias light behind the monitors and the cool glow they throw at the chair.
    led_bar("LED_Monitor_Bias", 0.7, (-0.18, 0.075, 0.5), 3, 1.0, root, "X", light_aim=(-0.18, d / 2 + 0.3, 0.6), watts=40)
    light("Light_Screens", "AREA", 18 * max(NEON_STRENGTH, 0.4), lin("#8FB8FF")[:3], (0, -0.25, 0.4),
          aim=(0, -1.6, 0.35), size=0.8, parent=root)


def build_speaker():
    """Left bookshelf speaker (Edifier R1280T-style), toed in toward the chair."""
    root, w, d, h = furniture_root("speaker")
    bookshelf_speaker("Speaker_L", root, (0, 0, 0), 12)


def build_chair():
    """Racing-style gaming chair (Secretlab TITAN Evo-like): flared backrest with harness slots, side bolsters with
    piping, magnetic head pillow, 4D armrests, recline-hinge covers, aluminium 5-star base, twin-wheel casters."""
    root, w, d, h = furniture_root("chair")
    if NIGHT:
        shell = surface(mat("dark", 0.52), "leather")
        inner = surface(mat("chair_in", 0.6, color="#26272F"), "leather")
    else:
        shell = surface(mat("cream", 0.52), "leather")
        inner = surface(mat("chair_in", 0.6, color="#ECEBE7"), "leather")
    pipe = mat("accent_1", 0.5)
    for k in range(5):                                              # 5-star base with twin-wheel casters
        a = R(90 + k * 72)
        ca, sa = math.cos(a), math.sin(a)
        box("Chair_BaseLeg", (0.29, 0.05, 0.032), (ca * 0.17, sa * 0.17, 0.1), ALU, bevel=0.008, rot=(0, R(6), a),
            parent=root)
        box("Chair_CasterFork", (0.03, 0.035, 0.04), (ca * 0.31, sa * 0.31, 0.065), PLASTIC, bevel=0.008, rot=(0, 0, a),
            parent=root)
        cyl("Chair_Wheel", 0.03, 0.036, (ca * 0.325, sa * 0.325, 0.03), PLASTIC, rot=(R(90), 0, a), bevel=0.006,
            parent=root)
    cyl("Chair_Hub", 0.05, 0.06, (0, 0, 0.11), ALU, parent=root)
    cyl("Chair_GasCover", 0.036, 0.13, (0, 0, 0.2), PLASTIC, r2=0.03, parent=root)
    cyl("Chair_GasLift", 0.022, 0.12, (0, 0, 0.3), CHROME, parent=root)
    box("Chair_Mechanism", (0.26, 0.26, 0.05), (0, 0.02, 0.375), PLASTIC, bevel=0.008, parent=root)
    tube("Chair_Lever", (0.12, -0.02, 0.37), (0.24, -0.06, 0.38), 0.006, PLASTIC, parent=root)
    # Seat: flat centre with raised side bolsters and piping.
    box("Chair_SeatShell", (0.5, 0.48, 0.035), (0, -0.01, 0.415), PLASTIC, bevel=0.01, parent=root)
    box("Chair_Seat", (0.38, 0.49, 0.075), (0, -0.02, 0.465), inner, bevel=0.02, parent=root)
    for sx in (-1, 1):
        box("Chair_SeatBolster", (0.075, 0.49, 0.1), (sx * 0.228, -0.02, 0.475), shell, bevel=0.025, parent=root)
        tube("Chair_Piping", (sx * 0.19, -0.255, 0.502), (sx * 0.19, 0.215, 0.502), 0.004, pipe, parent=root, segs=6)
        cyl("Chair_HingeCover", 0.055, 0.03, (sx * 0.272, 0.2, 0.47), PLASTIC, rot=(0, R(90), 0), bevel=0.008, parent=root)
        # 4D armrest: steel bracket under the seat, post and a flat pad.
        box("Chair_ArmBracket", (0.12, 0.05, 0.02), (sx * 0.23, 0.04, 0.39), STEEL, bevel=0.003, parent=root)
        box("Chair_ArmPost", (0.045, 0.07, 0.29), (sx * 0.29, 0.04, 0.53), PLASTIC, bevel=0.008, parent=root)
        box("Chair_ArmPad", (0.095, 0.26, 0.03), (sx * 0.29, 0.0, 0.69), PLASTIC, bevel=0.012, parent=root)
    # Backrest: real outline (narrow waist, wide shoulders, rounded head), reclined a little.
    back = group("Chair_BackPivot", (0, 0.22, 0.46), root, rot=(R(-8), 0, 0))
    # The racing-seat silhouette: wide shoulder wings at ~60 % height, then a clear notch in to a narrower head
    # section with a rounded top (the shape that tells a racing chair from an office chair).
    half = [(0.21, 0.0), (0.235, 0.06), (0.235, 0.28), (0.25, 0.42), (0.272, 0.56), (0.272, 0.64), (0.25, 0.68),
            (0.19, 0.71), (0.17, 0.74), (0.17, 0.82), (0.15, 0.86), (0.1, 0.878)]
    outline = half + [(-x, z) for x, z in reversed(half)]
    extrude("Chair_Back", outline, "Y", -0.065, 0.06, shell, bevel=0.018, parent=back)
    half_in = [(0.13, 0.05), (0.14, 0.3), (0.155, 0.5), (0.155, 0.62), (0.12, 0.69), (0.115, 0.74), (0.115, 0.8),
               (0.09, 0.84)]
    inner_outline = half_in + [(-x, z) for x, z in reversed(half_in)]
    extrude("Chair_BackPanel", inner_outline, "Y", -0.082, -0.06, inner, bevel=0.008, parent=back)
    # Side wings: the padded bolsters that wrap forward around your ribs and shoulders (the racing-seat look).
    wing = [(0.21, 0.0), (0.235, 0.06), (0.235, 0.28), (0.25, 0.42), (0.272, 0.56), (0.272, 0.64), (0.25, 0.68),
            (0.19, 0.66), (0.175, 0.5), (0.16, 0.3), (0.15, 0.05)]
    for sx in (-1, 1):
        extrude("Chair_BackWing", [(sx * x, z) for x, z in wing], "Y", -0.125, -0.06, shell, bevel=0.016, parent=back)
        polyline("Chair_BackPiping", [(sx * x, -0.083, z) for x, z in half_in], 0.004, pipe, parent=back, segs=6)
        box("Chair_HarnessSlot", (0.03, 0.012, 0.08), (sx * 0.15, -0.064, 0.705), mat("slot", 0.8, color="#08080A"),
            bevel=0.01, parent=back)
    rear = [(x * 0.86, 0.05 + z * 0.88) for x, z in outline]        # stitched rear cover panel (seen from behind)
    extrude("Chair_BackRear", rear, "Y", 0.058, 0.066, inner, bevel=0.004, parent=back)
    polyline("Chair_RearStitch", [(x, 0.067, z) for x, z in rear + rear[:1]], 0.0028, pipe, parent=back, segs=6)
    box("Chair_Lumbar", (0.26, 0.03, 0.13), (0, -0.088, 0.2), inner, bevel=0.014, parent=back)
    box("Chair_HeadPillow", (0.22, 0.07, 0.11), (0, -0.105, 0.79), shell, bevel=0.028, parent=back)


def build_floor_lamp():
    """18" LED ring light (46 cm flat diffused ring) on a light stand with tripod legs, a ball-head bracket and a
    phone holder in the middle. Its area light points at the chair."""
    root, w, d, h = furniture_root("floor_lamp")
    stand = surface(mat("dark", 0.39, metal=0.6), "brushed")
    housing = mat("dark", 0.45) if NIGHT else mat("cream", 0.45)
    hub = Vector((0, 0, 0.42))
    collar = Vector((0, 0, 0.2))
    for k in range(3):                                              # tripod legs with braces
        a = R(90 + k * 120)
        foot = Vector((math.cos(a) * 0.27, math.sin(a) * 0.27, 0.012))
        tube("RingLight_Leg", hub, foot, 0.0085, stand, parent=root)
        tube("RingLight_Brace", collar, hub.lerp(foot, 0.55), 0.005, stand, parent=root, segs=8)
        ball("RingLight_Foot", 0.014, foot, PLASTIC, parent=root)
    RING_Z = h - 0.27
    cyl("RingLight_Hub", 0.02, 0.07, hub, PLASTIC, parent=root)
    cyl("RingLight_Collar", 0.016, 0.03, collar, PLASTIC, parent=root)
    tube("RingLight_Column", (0, 0, 0.18), (0, 0, 1.05), 0.014, stand, parent=root)
    tube("RingLight_Column2", (0, 0, 1.05), (0, 0, RING_Z - 0.3), 0.011, stand, parent=root)
    for z in (0.42 + 0.06, 1.05):
        cyl("RingLight_Lock", 0.02, 0.035, (0, 0, z), PLASTIC, parent=root)
        cyl("RingLight_LockKnob", 0.008, 0.03, (0.025, 0, z), PLASTIC, rot=(0, R(90), 0), parent=root)
    head = group("RingLight_Head", (0, 0, RING_Z), root, rot=(R(-6), 0, 0))
    ring_disc("RingLight_Housing", 0.232, 0.168, 0.03, (0, 0.004, 0), housing, parent=head, bevel=0.004)
    no_shadow(ring_disc("RingLight_Diffuser", 0.226, 0.175, 0.004, (0, -0.013, 0),
                        mat("ring", 0.3, emit=6.0 if NIGHT else 3.0, color="#F4F7FF"), parent=head))
    box("RingLight_Mount", (0.05, 0.035, 0.05), (0, 0.01, -0.255), PLASTIC, bevel=0.006, parent=head)
    ball("RingLight_BallHead", 0.02, (0, 0.01, -0.29), stand, parent=head)
    tube("RingLight_PhoneRod", (0, -0.005, -0.23), (0, -0.02, -0.02), 0.005, stand, parent=head, segs=8)
    box("RingLight_PhoneClamp", (0.09, 0.014, 0.022), (0, -0.024, 0.0), PLASTIC, bevel=0.004, parent=head)
    box("RingLight_Phone", (0.072, 0.008, 0.152), (0, -0.034, 0.03), mat("dark", 0.2), bevel=0.006, parent=head)
    box("RingLight_PhoneScreen", (0.066, 0.001, 0.145), (0, -0.0385, 0.03), mat("phone", 0.2, emit=0.6, color="#3A4B7A"),
        bevel=0, parent=head)
    lo = light("Light_RingLight", "AREA", LAMP_STRENGTH, kelvin(LAMP_WARMTH), (0, -0.06, RING_Z),
               aim=(0, -1.2, 1.0), size=0.42, parent=root)
    lo.data.shape = "DISK"
    if hasattr(lo.data, "specular_factor"):
        lo.data.specular_factor = 0.35            # keeps its reflection on the floor small


def build_sofa():
    """2-seat sofa (IKEA KLIPPAN-style, 180 x 88 x 66 cm): boxy frame with arms as high as the back, one long seat
    cushion at 43 cm, short dark feet, two scatter cushions, a knit throw and a controller."""
    root, w, d, h = furniture_root("sofa")
    fabric = surface(mat("main", 0.9), "fabric", scale=3)        # even woven cover (no cloudy patches)
    seam = mat("main", 0.95, color=shade(COLORS["main"], 0.75))
    LEG, ARM, BACK = 0.09, 0.17, 0.2
    for sx in (-1, 1):
        for sy in (-1, 1):
            cyl("Sofa_Foot", 0.022, LEG, (sx * (w / 2 - 0.08), sy * (d / 2 - 0.08), LEG / 2), mat("dark", 0.47), r2=0.018,
                segs=16, parent=root)
    box("Sofa_Base", (w - 2 * ARM + 0.02, d - 0.02, 0.23), (0, 0, LEG + 0.115), fabric, bevel=0.02, parent=root)
    for sx in (-1, 1):
        box("Sofa_Arm", (ARM, d, h - LEG), (sx * (w / 2 - ARM / 2), 0, LEG + (h - LEG) / 2), fabric, bevel=0.04, parent=root)
        tube("Sofa_ArmSeam", (sx * (w / 2 - ARM / 2), -d / 2 - 0.001, LEG + 0.04), (sx * (w / 2 - ARM / 2), -d / 2 - 0.001,
             h - 0.05), 0.003, seam, parent=root, segs=6)
    box("Sofa_Back", (w - 2 * ARM + 0.02, BACK, h - LEG), (0, d / 2 - BACK / 2, LEG + (h - LEG) / 2), fabric, bevel=0.04,
        parent=root)
    seat_d = d - BACK - 0.015
    box("Sofa_SeatCushion", (w - 2 * ARM - 0.01, seat_d, 0.12), (0, -d / 2 + seat_d / 2, LEG + 0.23 + 0.055), fabric,
        bevel=0.022, parent=root)
    tube("Sofa_SeatPiping", (-w / 2 + ARM + 0.02, -d / 2 - 0.002, LEG + 0.285), (w / 2 - ARM - 0.02, -d / 2 - 0.002,
         LEG + 0.285), 0.004, seam, parent=root, segs=6)
    for sx, key, tw in ((-1, "accent_3", 10), (1, "accent_2", -8)):   # scatter cushions leaning on the back
        pillow("Sofa_Cushion", (0.44, 0.15, 0.44), (sx * 0.4, d / 2 - BACK - 0.08, LEG + 0.35 + 0.2),
               surface(mat(key, 0.91), "fabric", scale=3), rot=(R(-14), 0, R(tw)), parent=root)
    throw = surface(mat("throw", 0.95, color="#5E5A7C" if NIGHT else "#D8D0E8"), "knit")   # heather chunky knit
    # Chunky knit throw, folded in three and laid over the far arm (how it sits in a showroom), tassels at one end.
    fold = group("Sofa_Throw", (w / 2 - ARM / 2, 0.06, h), root, rot=(0, 0, R(5)))
    for k in range(3):                                              # three folded layers, each a little offset
        box("Sofa_Throw_Layer", (0.215 - 0.008 * k, 0.4 - 0.01 * k, 0.026), (0.004 * k, 0.006 * k, 0.012 + k * 0.024),
            throw, bevel=0.011, parent=fold)
    cyl("Sofa_Throw_Fold", 0.024, 0.39, (-0.098, 0.005, 0.036), throw, rot=(R(90), 0, 0), segs=16, bevel=0, parent=fold)
    merged("Sofa_Throw_Tassels", [((0.005, 0.005, 0.06), (0.11, -0.18 + k * 0.03, -0.01)) for k in range(13)],
           throw, parent=fold)
    pad = group("Sofa_Controller", (-0.32, -0.12, LEG + 0.345), root, rot=(0, 0, R(25)))
    gamepad(pad, mat("dark", 0.4) if NIGHT else mat("cream", 0.4))


def gamepad(parent, body_m):
    """A generic game controller: body, two grips, two sticks, a d-pad and four face buttons."""
    box("Controller_Body", (0.12, 0.06, 0.028), (0, 0.005, 0.016), body_m, bevel=0.01, parent=parent)
    for sx in (-1, 1):
        ball("Controller_Grip", 0.03, (sx * 0.055, -0.022, 0.015), body_m, scale=(1, 1.3, 0.6), parent=parent)
        cyl("Controller_Stick", 0.009, 0.01, (sx * 0.025, -0.012, 0.034), PLASTIC, parent=parent)
    box("Controller_DPad", (0.016, 0.005, 0.003), (-0.045, 0.01, 0.031), PLASTIC, bevel=0.001, parent=parent)
    box("Controller_DPad", (0.005, 0.016, 0.003), (-0.045, 0.01, 0.031), PLASTIC, bevel=0.001, parent=parent)
    for k, (dx, dy) in enumerate(((0, 0.007), (0, -0.007), (0.007, 0), (-0.007, 0))):
        cyl("Controller_Button", 0.0035, 0.004, (0.045 + dx, 0.01 + dy, 0.031), mat(("accent_2", "accent_3", "accent_1",
            "cream")[k], 0.4), segs=10, parent=parent)


def build_hero_prop():
    """Arcade cabinet on a 1 ft riser (Arcade1Up-style, 51 x 52 x 154 cm): 18 mm side panels with coloured T-moulding
    and side-art stripes, leaning 17" screen, angled control panel, lit marquee and a coin door."""
    root, w, d, h = furniture_root("hero_prop")
    RISER, PANEL = 0.3, 0.018
    body_m = surface(mat("dark", 0.46), "veneer")
    side_m = surface(mat("arcade_side", 0.46, color="#1C1D26" if NIGHT else "#F2F0EC"), "veneer" if NIGHT else "paper")
    tmould = mat("accent_3", 0.4) if NIGHT else mat("accent_1", 0.4)
    # Riser box with matching stripes.
    box("Arcade_Riser", (w, d - 0.06, RISER), (0, 0.03, RISER / 2), body_m, bevel=0.003, parent=root)
    for sx in (-1, 1):
        box("Arcade_RiserStripe", (0.002, d - 0.08, 0.03), (sx * (w / 2 + 0.001), 0.03, RISER * 0.6), tmould, bevel=0,
            parent=root)
    # Side panels (profile seen from the side: y = front/back, z = up) and the body between them.
    side = [(0.26, 0), (-0.21, 0), (-0.21, 0.56), (-0.26, 0.62), (-0.26, 0.68), (-0.2, 1.06), (-0.2, 1.24), (0.26, 1.24)]
    body = [(0.25, 0), (-0.2, 0), (-0.2, 0.56), (-0.25, 0.615), (-0.25, 0.67), (-0.13, 0.71), (-0.05, 1.04),
            (-0.19, 1.06), (-0.19, 1.235), (0.25, 1.235)]
    side = [(y, z + RISER) for y, z in side]
    body = [(y, z + RISER) for y, z in body]
    for sx in (-1, 1):
        x0, x1 = sx * (w / 2 - PANEL), sx * w / 2
        extrude("Arcade_Side", side, "X", min(x0, x1), max(x0, x1), side_m, bevel=0.002, parent=root)
        polyline("Arcade_TMoulding", [(sx * (w / 2 - PANEL / 2), y, z) for y, z in side[1:]], 0.0105, tmould, parent=root,
                 segs=8)
        xs = sx * (w / 2 + 0.0008)                                  # side art: two diagonal stripes
        for k, key in enumerate(("accent_1", "accent_2")):
            o = 0.16 * k
            stripe = [(-0.19, RISER + 0.12 + o), (0.24, RISER + 0.55 + o), (0.24, RISER + 0.62 + o),
                      (-0.19, RISER + 0.19 + o)]
            extrude("Arcade_SideArt", stripe, "X", min(xs, sx * w / 2), max(xs, sx * w / 2) + 0.0008, mat(key, 0.5),
                    bevel=0, parent=root)
    extrude("Arcade_Body", body, "X", -w / 2 + PANEL, w / 2 - PANEL, body_m, bevel=0.003, parent=root)
    # Screen leaning back, with its bezel.
    lo_, hi_ = Vector((-0.13, 0.71 + RISER)), Vector((-0.05, 1.04 + RISER))
    up = (hi_ - lo_).normalized()
    nrm = Vector((-up.y, up.x))                                     # outward normal (points to -y and up)
    tilt = math.atan2(hi_.x - lo_.x, hi_.y - lo_.y)
    mid = (lo_ + hi_) / 2

    def on_screen(du, dx=0.0, out=0.002):
        p = mid + up * du + nrm * out
        return (dx, p.x, p.y)

    box("Arcade_Bezel", (w - 2 * PANEL - 0.01, 0.006, (hi_ - lo_).length - 0.01), on_screen(0, out=0.002),
        mat("bezel", 0.3, color="#0E0E12"), bevel=0.002, rot=(-tilt, 0, 0), parent=root)
    s3 = hook_image("screen", 3, (0.34, 0.255), on_screen(0.0, out=0.0055), rot=(-tilt, 0, 0), parent=root, glow=True,
                    default_key="dark")
    pix = [box("Arcade_Invader", (0.028, 0.002, 0.028), on_screen(0.05 - r * 0.032, -0.1 + c * 0.032, 0.0075),
               neon(2, 0.8), bevel=0, rot=(-tilt, 0, 0), parent=root)
           for r, row in enumerate(("0110110", "1111111", "1011101", "0100010")) for c, ch in enumerate(row) if ch == "1"]
    pix.append(box("Arcade_Score", (0.2, 0.002, 0.02), on_screen(0.1, 0, 0.0075), neon(3, 0.9), bevel=0,
                   rot=(-tilt, 0, 0), parent=root))
    pix.append(box("Arcade_Ground", (0.3, 0.002, 0.014), on_screen(-0.105, 0, 0.0075), neon(1, 0.9), bevel=0,
                   rot=(-tilt, 0, 0), parent=root))
    hook_default(s3, *pix)
    # Control panel: ball-top joystick, 2 rows of 3 buttons and two start buttons.
    cp_a, cp_b = Vector((-0.25, 0.67 + RISER)), Vector((-0.13, 0.71 + RISER))
    cp_dir = (cp_b - cp_a).normalized()
    cp_n = Vector((-cp_dir.y, cp_dir.x))
    cp_rot = (math.atan2(cp_b.y - cp_a.y, cp_b.x - cp_a.x), 0, 0)

    def on_panel(t, dx, out):
        p = cp_a + cp_dir * t + cp_n * out
        return (dx, p.x, p.y)

    box("Arcade_PanelTop", (w - 2 * PANEL - 0.004, (cp_b - cp_a).length, 0.006), on_panel((cp_b - cp_a).length / 2, 0, 0.003),
        mat("panel_art", 0.4, color="#24253A" if NIGHT else "#E9E6F2"), bevel=0.001, rot=cp_rot, parent=root)
    tube("Arcade_Stick", on_panel(0.06, -0.12, 0.0), on_panel(0.06, -0.12, 0.06), 0.004, CHROME, parent=root)
    ball("Arcade_StickBall", 0.017, on_panel(0.06, -0.12, 0.072), mat("accent_3", 0.3), parent=root)
    cyl("Arcade_StickDust", 0.02, 0.004, on_panel(0.06, -0.12, 0.007), PLASTIC, rot=cp_rot, parent=root)
    for k in range(6):
        col, row = k % 3, k // 3
        cyl("Arcade_Button", 0.0135, 0.012, on_panel(0.045 + row * 0.04, 0.0 + col * 0.04 + row * 0.006, 0.009),
            mat(("accent_2", "accent_3", "accent_1")[col], 0.25, emit=0.6 if NIGHT else 0.0), rot=cp_rot, parent=root)
    for k in range(2):
        cyl("Arcade_Start", 0.008, 0.01, on_panel(0.1, -0.04 + k * 0.035, 0.008), mat("cream", 0.3), rot=cp_rot, parent=root)
    # Marquee (back-lit acrylic) and speaker grilles under it.
    mz = RISER + (1.06 + 1.235) / 2
    no_shadow(box("Arcade_Marquee", (w - 2 * PANEL - 0.01, 0.006, 0.15), (0, -0.193, mz),
                  mat("marquee", 0.4, emit=2.0 * max(NEON_STRENGTH, 0.5), color=COLORS["neon_3"]), bevel=0.002,
                  parent=root))
    # Marquee art like a real game cabinet (no title text): a pixel-art ship flying between two speed bands.
    ship = ("0001000", "0011100", "0111110", "1101011", "1111111", "0100010")
    merged("Arcade_Marquee_Ship", [((0.0095, 0.002, 0.0095), (-0.13 + c * 0.01, -0.1975, mz + 0.03 - r * 0.01))
                                   for r, row in enumerate(ship) for c, ch in enumerate(row) if ch == "1"],
           mat("dark", 0.4), parent=root)
    for k, key in enumerate(("accent_2", "accent_1")):
        box("Arcade_Marquee_Band", (0.27, 0.002, 0.014), (0.07, -0.1975, mz + 0.012 - k * 0.03), mat(key, 0.4),
            bevel=0, parent=root)
    for sx in (-1, 1):
        cyl("Arcade_SpeakerGrille", 0.025, 0.004, on_screen(0.155, sx * 0.15, 0.006), mat("grille", 0.6, color="#2A2A30"),
            rot=(R(90) - tilt, 0, 0), parent=root)
    # Coin door on the lower front with two lit coin entries.
    cz = RISER + 0.3
    box("Arcade_CoinDoor", (0.22, 0.008, 0.26), (0, -0.204, cz), surface(mat("dark", 0.36, metal=0.6), "brushed"),
        bevel=0.004, parent=root)
    for sx in (-1, 1):
        box("Arcade_CoinEntry", (0.026, 0.006, 0.042), (sx * 0.05, -0.209, cz + 0.06),       # small lit coin inserts
            mat("coin", 0.3, emit=2.0, color="#FF5A3C"), bevel=0.002, parent=root)
        box("Arcade_CoinSlot", (0.003, 0.002, 0.026), (sx * 0.05, -0.2125, cz + 0.06), mat("slot", 0.8, color="#08080A"),
            bevel=0, parent=root)
        cyl("Arcade_CoinReject", 0.008, 0.006, (sx * 0.05, -0.21, cz - 0.02), CHROME, rot=(R(90), 0, 0), parent=root)
    cyl("Arcade_Lock", 0.01, 0.006, (0, -0.21, cz - 0.09), CHROME, rot=(R(90), 0, 0), parent=root)
    light("Light_Arcade", "POINT", 12 * max(NEON_STRENGTH, 0.4), neon_rgb(2), (0, -0.55, RISER + 1.0), size=0.15,
          parent=root)


def build_shelf():
    """IKEA KALLAX 2x4 laid on its side as a TV bench (147 x 39 x 77 cm, 39 mm outer frame, 16 mm dividers, no back):
    fabric boxes, upright game cases, boxed figures, a console and controller; a soundbar and a pothos on top."""
    root, w, d, h = furniture_root("shelf")
    hook_link(root, "github")                                       # click the games shelf for your GitHub
    O, I = 0.039, 0.016
    cw, ch = (w - 2 * O - 3 * I) / 4, (h - 2 * O - I) / 2
    box("CubeShelf_Top", (w, d, O), (0, 0, h - O / 2), WOOD, bevel=0.002, parent=root)
    box("CubeShelf_Bottom", (w, d, O), (0, 0, O / 2), WOOD, bevel=0.002, parent=root)
    for sx in (-1, 1):
        box("CubeShelf_Side", (O, d, h - 2 * O), (sx * (w / 2 - O / 2), 0, h / 2), WOOD, bevel=0.002, parent=root)
    for k in range(3):
        box("CubeShelf_Divider", (I, d, h - 2 * O), (-w / 2 + O + cw * (k + 1) + I * k + I / 2, 0, h / 2), WOOD, bevel=0.0015,
            parent=root)
    box("CubeShelf_Shelf", (w - 2 * O, d, I), (0, 0, O + ch + I / 2), WOOD, bevel=0.0015, parent=root)

    def cell(c, r):
        return -w / 2 + O + cw / 2 + c * (cw + I), O + r * (ch + I)        # centre x, floor z of a cube

    fy = -d / 2                                                    # front face
    contents = ["boxes", "games", "figures", "console", "games", "figures", "boxes", "games"]
    random.shuffle(contents)
    box_cols = ["accent_1", "accent_2", "cream", "main"]
    for i, kind in enumerate(contents):
        x, z = cell(i % 4, i // 4)
        if kind == "boxes":                                         # fabric storage box with a hand hole
            key = box_cols[i % len(box_cols)]
            box("CubeShelf_FabricBox", (cw - 0.012, d - 0.03, ch - 0.012), (x, 0.0, z + (ch - 0.012) / 2),
                surface(mat(key, 0.92, color=shade(COLORS[key], 0.85)), "fabric", scale=3), bevel=0.006, parent=root)
            box("CubeShelf_FabricBox_Handle", (0.1, 0.004, 0.03), (x, fy + 0.013, z + ch - 0.06),
                mat("hole", 0.9, color="#0C0C0F"), bevel=0.012, parent=root)
        elif kind == "games":                                       # upright game cases, spines out
            n = random.randint(9, 15)
            gx = x - cw / 2 + 0.012
            for k in range(n):
                col = random.choice(["#1F4FA8", "#1F4FA8", "#1C1C22", "#E8E8EC", "#2E8B57", "#B8282E"])
                box("CubeShelf_Game", (0.014, 0.135, 0.17), (gx + 0.007, fy + 0.03 + 0.0675, z + 0.085),
                    mat("game", 0.45, color=col), bevel=0.0015, parent=root)
                box("CubeShelf_Game_Label", (0.0145, 0.002, 0.03), (gx + 0.007, fy + 0.0295, z + 0.14),
                    mat("label", 0.5, color="#F2F2F2"), bevel=0, parent=root)
                gx += 0.0155
            if n < 13:                                              # a leaning case at the end of the row
                box("CubeShelf_Game", (0.014, 0.135, 0.17), (gx + 0.04, fy + 0.0975, z + 0.08),
                    mat("game", 0.45, color="#1F4FA8"), bevel=0.0015, rot=(0, R(-20), 0), parent=root)
        elif kind == "figures":                                     # boxed vinyl figures with a window
            for k in range(2):
                bx = x - 0.07 + k * 0.135
                key = random.choice(["accent_1", "accent_2", "accent_3"])
                box("CubeShelf_FigureBox", (0.115, 0.09, 0.16), (bx, fy + 0.075, z + 0.08), mat(key, 0.55), bevel=0.003,
                    parent=root)
                box("CubeShelf_FigureBox_Window", (0.085, 0.002, 0.095), (bx, fy + 0.0295, z + 0.072),
                    mat("window", 0.15, color="#1A1C24"), bevel=0, parent=root)
                ball("CubeShelf_Figure_Head", 0.026, (bx, fy + 0.045, z + 0.09), mat("cream", 0.5), scale=(1, 0.6, 0.9),
                     parent=root)
                box("CubeShelf_FigureBox_Top", (0.115, 0.002, 0.03), (bx, fy + 0.0295, z + 0.14), mat("cream", 0.5),
                    bevel=0, parent=root)
        else:                                                       # games console lying flat + a controller
            cm = mat("console", 0.4, color="#1A1A1F" if NIGHT else "#F4F4F6")
            box("CubeShelf_Console", (0.27, 0.3, 0.06), (x, 0.02, z + 0.03), cm, bevel=0.008, parent=root)
            box("CubeShelf_Console_Slot", (0.12, 0.002, 0.004), (x - 0.04, fy + 0.0445, z + 0.04),
                mat("slot", 0.8, color="#08080A"), bevel=0, parent=root)
            box("CubeShelf_Console_LED", (0.01, 0.002, 0.003), (x + 0.1, fy + 0.0445, z + 0.03),
                mat("led", 0.3, emit=3.0, color="#5AC8FF"), bevel=0, parent=root)
            pad = group("CubeShelf_Controller", (x, fy + 0.12, z + 0.06), root, rot=(0, 0, R(-10)))
            gamepad(pad, mat("dark", 0.4) if NIGHT else mat("cream", 0.4))
    # On top: a fabric-fronted soundbar under the TV, a pothos in a glazed pot and a small figure.
    box("CubeShelf_Soundbar", (0.89, 0.1, 0.065), (0, -0.04, h + 0.0325), PLASTIC, bevel=0.012, parent=root)
    box("CubeShelf_Soundbar_Grille", (0.87, 0.003, 0.05), (0, -0.0915, h + 0.0325), surface(mat("dark", 0.94), "fabric"),
        bevel=0.002, parent=root)
    px = w / 2 - 0.1
    cyl("Plant_Pot", 0.065, 0.12, (px, 0, h + 0.06), surface(mat("cream", 0.22), "ceramic"), r2=0.075, segs=28,
        parent=root)
    cyl("Plant_PotRim", 0.077, 0.012, (px, 0, h + 0.115), surface(mat("cream", 0.22), "ceramic"), segs=28, parent=root)
    cyl("Plant_Soil", 0.068, 0.006, (px, 0, h + 0.112), mat("soil", 0.95, color="#3B2A20"), segs=24, parent=root)
    leaf = mat("plant", 0.55)
    for k in range(16):                                             # trailing pothos leaves
        a = k * 2.4
        rr = 0.03 + 0.012 * (k % 4)
        dz = 0.14 - 0.022 * k if k > 6 else 0.13 + 0.02 * (k % 3)
        lx = px + math.cos(a) * (rr + 0.04 * (k > 6))
        ball("Plant_Leaf", 0.03, (lx, -0.05 if k > 6 else math.sin(a) * rr, h + dz), leaf, scale=(1.1, 0.45, 0.85),
             rot=(R(20), 0, a), parent=root)
    # Two collectible vinyl figures (the big-square-head kind, ~9.5 cm) standing out of their boxes.
    for k, (fx, body_key) in enumerate(((-w / 2 + 0.09, "accent_2"), (-w / 2 + 0.19, "accent_3"))):
        fg = group("CubeShelf_TopFigure", (fx, -0.02, h), root, rot=(0, 0, R(-15 + 25 * k)))
        cyl("Figure_Base", 0.026, 0.006, (0, 0, 0.003), PLASTIC, parent=fg)
        box("Figure_Body", (0.036, 0.026, 0.036), (0, 0, 0.024), mat(body_key, 0.45), bevel=0.008, parent=fg)
        box("Figure_Head", (0.058, 0.05, 0.052), (0, -0.002, 0.068), mat("cream", 0.4), bevel=0.014, parent=fg)
        box("Figure_Hair", (0.06, 0.052, 0.014), (0, 0.0, 0.092), mat("dark", 0.5), bevel=0.006, parent=fg)
        for sx in (-1, 1):
            ball("Figure_Eye", 0.0065, (sx * 0.013, -0.027, 0.066), mat("dark", 0.2), scale=(1, 0.4, 1), parent=fg)


def build_rug():
    """Flat-woven cotton rug (IKEA TIPHEDE-style, 155 x 220 cm): plain woven field, bands of thin stripes
    near both short ends and a knotted fringe."""
    root, w, d, h = furniture_root("rug")
    body = w - 0.1                                                  # the last 5 cm at each end is fringe
    field_hex = shade(COLORS["main"], 0.62) if NIGHT else shade(COLORS["cream"], 0.93)
    box("Rug_Base", (body, d, h * 0.8), (0, 0, h * 0.4), surface(mat("main", 0.98, color=field_hex), "knit", scale=5),
        bevel=0.003, parent=root)
    band_m = surface(mat("rug_band", 0.98, color="#2A2C36" if NIGHT else "#3A3D47"), "knit", scale=5)
    tone_m = surface(mat("rug_tone", 0.98, color=shade(COLORS["accent_1"], 0.45 if NIGHT else 0.9)), "knit", scale=5)
    for s in (-1, 1):                                               # stripe bands: thick, thin, thin, thick
        for k, (off, bw, m) in enumerate(((0.12, 0.06, band_m), (0.2, 0.02, tone_m), (0.24, 0.02, band_m),
                                          (0.3, 0.035, tone_m))):
            box("Rug_Stripe", (bw, d - 0.002, h * 0.04), (s * (body / 2 - off), 0, h * 0.82), m, bevel=0, parent=root)
        merged("Rug_Fringe", [((0.05, 0.006, 0.003), (s * (body / 2 + 0.025), -d / 2 + 0.02 + k * 0.025, 0.0015))
                              for k in range(int((d - 0.03) / 0.025))], mat("cream", 0.95), parent=root)


def build_wall_art():
    """IKEA RIBBA-style deep box frames with white mounts (50x70 and 30x40) and an ON AIR light box."""
    root, w, d, h = furniture_root("wall_art")
    back_y = d / 2
    frame_m = mat("dark", 0.43) if NIGHT else surface(mat("wood", 0.44), "veneer")
    mount = mat("cream", 0.85)
    for idx, x, z, fw, fh, pw_, ph_ in ((1, -0.2, 0.5, 0.52, 0.72, 0.38, 0.56), (2, 0.29, 0.33, 0.32, 0.42, 0.21, 0.3)):
        fd, fb = 0.045, 0.022                                       # frame depth, face width
        yc = back_y - fd / 2
        for nm, size, loc in (("Top", (fw, fd, fb), (x, yc, z + fh / 2 - fb / 2)), ("Bottom", (fw, fd, fb), (x, yc, z - fh / 2 + fb / 2)),
                              ("L", (fb, fd, fh), (x - fw / 2 + fb / 2, yc, z)), ("R", (fb, fd, fh), (x + fw / 2 - fb / 2, yc, z))):
            box(f"Poster_Frame_{nm}", size, loc, frame_m, bevel=0.002, parent=root)
        box("Poster_Mount", (fw - 2 * fb, 0.003, fh - 2 * fb), (x, back_y - fd + 0.012, z), mount, bevel=0, parent=root)
        hook = hook_image("poster", idx, (pw_, ph_), (x, back_y - fd + 0.0098, z), parent=root,
                          default_key="accent_1" if idx == 1 else "dark")
        yd = back_y - fd + 0.0092
        if idx == 1:                                                # game key art: sun, ground, title
            deco = [box("Poster_Sun", (0.15, 0.001, 0.15), (x, yd, z + 0.06), mat("accent_3", 0.6, emit=0.6), bevel=0.0,
                        parent=root, rot=(0, R(45), 0)),
                    box("Poster_Ground", (pw_, 0.0015, 0.16), (x, yd - 0.0005, z - ph_ / 2 + 0.08), mat("dark", 0.6),
                        bevel=0, parent=root),
                    box("Poster_Title", (pw_ - 0.1, 0.0015, 0.04), (x, yd - 0.001, z + ph_ / 2 - 0.06),
                        mat("cream", 0.5, emit=0.5), bevel=0, parent=root)]
        else:                                                       # pixel heart
            heart = ("0110110", "1111111", "1111111", "0111110", "0011100", "0001000")
            deco = [box("Poster_Pixel", (0.024, 0.0015, 0.024), (x - 0.081 + c * 0.027, yd, z + 0.07 - r * 0.027),
                        mat("accent_3", 0.5, emit=1.0), bevel=0, parent=root)
                    for r, row in enumerate(heart) for c, ch in enumerate(row) if ch == "1"]
        hook_default(hook, *deco)
    # ON AIR light box above the small frame.
    box("OnAir_Box", (0.3, 0.05, 0.1), (0.29, back_y - 0.025, 0.78), mat("dark", 0.4), bevel=0.02, parent=root)
    no_shadow(box("OnAir_Face", (0.27, 0.004, 0.075), (0.29, back_y - 0.051, 0.78),
                  mat("onair", 0.3, emit=2.0 * max(NEON_STRENGTH, 0.5), color="#FF3B5C"), bevel=0.01, parent=root))
    deco_text("OnAir_Text", "ON AIR", 0.05, (0.29, back_y - 0.055, 0.777), mat("cream", 0.3, emit=2.0), parent=root)


PLACEHOLDERS = {
    "desk": build_desk, "monitor": build_monitor, "speaker": build_speaker, "chair": build_chair,
    "floor_lamp": build_floor_lamp, "sofa": build_sofa, "hero_prop": build_hero_prop, "shelf": build_shelf,
    "rug": build_rug, "wall_art": build_wall_art,
}
if SHOW_PLACEHOLDER_FURNITURE:
    for slot_name, build in PLACEHOLDERS.items():
        build()

# =====================================================================
#  ROOM DECOR  (not slots): 65" TV on the wall, LACK side table, neon name sign
# =====================================================================
# 65" TV (144.9 x 83.4 x 2.6 cm) on a flat wall bracket above the KALLAX bench: the 4th project screen.
TV_X, TV_Z = SLOTS["shelf"].location.x, FLOOR_Z + 0.77 + 0.3 + 0.417
box("TV_Bracket", (0.42, 0.03, 0.28), (TV_X, D - 0.015, TV_Z), STEEL, bevel=0.003)
box("TV_Panel", (1.449, 0.026, 0.834), (TV_X, D - 0.043, TV_Z), SCREEN_BLACK, bevel=0.003)
tv = hook_image("screen", 4, (1.43, 0.804), (TV_X, D - 0.0565, TV_Z + 0.004), glow=True, default_key="dark")
yt = D - 0.0575
tv_deco = [box("TV_Sky", (1.43, 0.001, 0.27), (TV_X, yt, TV_Z + 0.27), mat("accent_1", 0.4, emit=0.9), bevel=0),
           box("TV_Sky2", (1.43, 0.001, 0.27), (TV_X, yt, TV_Z), mat("accent_3", 0.4, emit=1.1), bevel=0),
           box("TV_Ground", (1.43, 0.001, 0.265), (TV_X, yt, TV_Z - 0.268), mat("dark", 0.5, emit=0.3), bevel=0),
           box("TV_Sun", (0.2, 0.001, 0.2), (TV_X + 0.3, yt - 0.0005, TV_Z + 0.05), mat("cream", 0.4, emit=1.5), bevel=0,
               rot=(0, R(45), 0)),
           box("TV_Menu", (0.36, 0.001, 0.44), (TV_X - 0.45, yt - 0.001, TV_Z - 0.05), mat("dark", 0.5, emit=0.2), bevel=0)]
for k in range(4):
    tv_deco.append(box("TV_MenuItem", (0.28 if k else 0.3, 0.001, 0.045), (TV_X - 0.45, yt - 0.0015, TV_Z + 0.11 - k * 0.09),
                       mat("cream" if k else "accent_2", 0.4, emit=1.4), bevel=0))
hook_default(tv, *tv_deco)
led_bar("LED_TV_Backlight", 1.2, (TV_X, D - 0.022, TV_Z + 0.36), 1, 1.0, None, "X",
        light_at=(TV_X, D - 0.03, TV_Z), light_aim=(TV_X, D + 1, TV_Z), watts=60)   # TV bias light glows on the wall
if NEON_STRENGTH > 0:
    light("Light_TV", "AREA", 30 * max(NEON_STRENGTH, 0.4), lin("#B48CFF")[:3], (TV_X, D - 0.35, TV_Z), aim=(TV_X, 1.0, 0.5),
          size=1.2)

# IKEA LACK side table (55 x 55 x 45 cm, 5 cm slab top, 5 x 5 cm legs) by the sofa, with a mug and a controller.
LX, LY = 0.34, 0.34
box("SideTable_Top", (0.55, 0.55, 0.05), (LX, LY, FLOOR_Z + 0.425), WOOD, bevel=0.003)
for sx in (-1, 1):
    for sy in (-1, 1):
        box("SideTable_Leg", (0.05, 0.05, 0.4), (LX + sx * 0.25, LY + sy * 0.25, FLOOR_Z + 0.2), WOOD, bevel=0.002)
cyl("SideTable_Mug", 0.04, 0.095, (LX - 0.1, LY + 0.1, FLOOR_Z + 0.4975), surface(mat("accent_2", 0.2), "ceramic"), segs=28)
torus("SideTable_Mug_Handle", 0.024, 0.006, (LX - 0.055, LY + 0.1, FLOOR_Z + 0.5), surface(mat("accent_2", 0.2), "ceramic"),
      segs=20, rsegs=8)
pad2 = group("SideTable_Controller", (LX + 0.08, LY - 0.06, FLOOR_Z + 0.45), None, rot=(0, 0, R(-30)))
gamepad(pad2, mat("dark", 0.4) if NIGHT else mat("cream", 0.4))
for o in pad2.children:                       # decor lives in the Room collection
    for c in o.users_collection:
        c.objects.unlink(o)
    COL_ROOM.objects.link(o)

# Snake plant (Sansevieria laurentii, ~70 cm) in a glazed floor pot against the back wall, between the TV bench and
# the desk: lance-shaped upright leaves with pale cross-bands and the typical yellow margin.
PX, PY = 1.86, D - 0.24
pot_m = surface(mat("cream", 0.23), "ceramic")
cyl("FloorPlant_Pot", 0.13, 0.3, (PX, PY, FLOOR_Z + 0.15), pot_m, r2=0.15, segs=32)
cyl("FloorPlant_PotRim", 0.158, 0.022, (PX, PY, FLOOR_Z + 0.289), pot_m, segs=32, bevel=0.006)
cyl("FloorPlant_Soil", 0.14, 0.01, (PX, PY, FLOOR_Z + 0.292), mat("soil", 0.95, color="#3B2A20"), segs=24)


def banded_leaf():
    """The plant colour with the pale zig-zag cross-bands of a snake plant leaf (bands run across the leaf)."""
    m = mat("plant", 0.45, color=shade(COLORS["plant"], 0.8))
    if not m.get("kit_bands"):
        nt = m.node_tree
        wave = nt.nodes.new("ShaderNodeTexWave")
        wave.wave_type, wave.bands_direction = "BANDS", "Z"
        wave.inputs["Scale"].default_value, wave.inputs["Distortion"].default_value = 8.0, 9.0
        coords = nt.nodes.new("ShaderNodeTexCoord")
        nt.links.new(coords.outputs["Object"], wave.inputs["Vector"])
        mix = nt.nodes.new("ShaderNodeMix")
        mix.data_type = "RGBA"
        mix.inputs[6].default_value = lin(shade(COLORS["plant"], 0.68))
        mix.inputs[7].default_value = lin(shade(COLORS["plant"], 1.04))
        ramp = nt.nodes.new("ShaderNodeValToRGB")
        ramp.color_ramp.elements[0].position, ramp.color_ramp.elements[1].position = 0.6, 0.85
        nt.links.new(wave.outputs["Fac"], ramp.inputs["Fac"])
        nt.links.new(ramp.outputs["Color"], mix.inputs["Factor"])
        nt.links.new(mix.outputs[2], _principled(m).inputs["Base Color"])
        m["kit_bands"] = True
    return m


snake = banded_leaf()
margin = mat("leaf_margin", 0.5, color="#C9C25A")
for k in range(11):                                                 # upright lance-shaped leaves
    a = k * 2.39
    lh = random.uniform(0.42, 0.66)
    shape = [(-0.012, 0), (0.012, 0), (0.03, lh * 0.35), (0.027, lh * 0.72), (0, lh), (-0.027, lh * 0.72),
             (-0.03, lh * 0.35)]
    for part, (scale_w, t, m) in enumerate(((1.0, 0.004, margin), (0.8, 0.0065, snake))):   # yellow rim, banded face
        leaf = extrude("FloorPlant_Leaf", [(x * scale_w, z * (1 if part == 0 else 0.97)) for x, z in shape], "Y",
                       -t, t, m, bevel=0.0015)
        leaf.location = (PX + math.cos(a) * 0.06, PY + math.sin(a) * 0.06, FLOOR_Z + 0.28)
        leaf.rotation_euler = (math.sin(a) * R(12), -math.cos(a) * R(12), a + R(90))

# Chunky hand-knitted pouffe (the braided-wool kind, 50 x 38 cm) in front of the sofa: a footrest / extra seat.
# Real chunky knit is columns of "V" stitches: each stitch is two fat loops leaning towards each other.
FX_, FY_ = 1.45, 1.5
pouf_m = surface(mat("pouf", 0.95, color="#56617F" if NIGHT else "#E6DECF"), "knit", scale=3)
cyl("Pouf_Body", 0.22, 0.36, (FX_, FY_, FLOOR_Z + 0.18), pouf_m, segs=36, bevel=0.05)
ball("Pouf_Top", 0.215, (FX_, FY_, FLOOR_Z + 0.355), pouf_m, scale=(1, 1, 0.16))
bm = bmesh.new()
COLS, ROWS, PR = 26, 9, 0.222
for c in range(COLS):
    a = 2 * math.pi * c / COLS
    for r in range(ROWS):
        for side in (-1, 1):                                        # left and right loop of one V stitch
            loop = (Matrix.Translation((math.cos(a) * PR, math.sin(a) * PR, 0.045 + r * 0.035))
                    @ Matrix.Rotation(a, 4, "Z") @ Matrix.Translation((0, side * 0.012, 0))
                    @ Matrix.Rotation(R(side * 32), 4, "X") @ Matrix.Diagonal((0.016, 0.013, 0.026, 1)))
            bmesh.ops.create_uvsphere(bm, u_segments=8, v_segments=6, radius=1.0, matrix=loop)
stitches = _obj("Pouf_Stitches", bm)
stitches.location = (FX_, FY_, FLOOR_Z)
_finish(stitches, pouf_m, 0, None, None)

# Neon name sign above the desk: LED neon flex on a tinted acrylic board with four metal stand-offs.
SIGN_X, SIGN_Z = DESK_X, 2.2
SIGN_W, SIGN_H = 1.45, 0.56
board_m = mat("acrylic", 0.35, color="#14152A") if NIGHT else mat("acrylic", 0.35, color="#FBFBFD")   # satin: no glare
sign = box("Name_Sign", (SIGN_W, 0.008, SIGN_H), (SIGN_X, D - 0.03, SIGN_Z), board_m, bevel=0.004)
hook_link(sign, "website")
for sx in (-1, 1):
    for sz in (-1, 1):
        cyl("Sign_Standoff", 0.01, 0.03, (SIGN_X + sx * (SIGN_W / 2 - 0.04), D - 0.02, SIGN_Z + sz * (SIGN_H / 2 - 0.04)),
            CHROME, rot=(R(90), 0, 0))
if NIGHT:                                                           # glowing neon letters on a dark board
    name_m = mat("accent_1", 0.3, emit=round(LED_EMIT * 0.85, 2))
    role_m = mat("accent_2", 0.3, emit=round(LED_EMIT * 0.6, 2))
else:                                                               # by day: strong colours on a white board
    name_m = mat("accent_1", 0.3, emit=0.35)
    role_m = mat("dark", 0.5)
hook_text("name", 1, "YOUR NAME", 0.2, (SIGN_X, D - 0.042, SIGN_Z + 0.07), material=name_m, max_width=1.3, depth=0.008)
hook_text("role", 1, "your role", 0.11, (SIGN_X, D - 0.04, SIGN_Z - 0.17), material=role_m, max_width=1.2, depth=0.006)
if NEON_STRENGTH > 0:
    light("Light_Sign", "POINT", 26 * NEON_STRENGTH, neon_rgb(1), (SIGN_X, D - 0.45, SIGN_Z), size=0.4)


# =====================================================================
#  LIGHTS, WORLD, CAMERA, RENDER
# =====================================================================
# Moonlight (or daylight) through the window, a soft fill from the camera side, a soft bounce from above.
light("Light_Sun", "SUN", SUN_STRENGTH, kelvin(SUN_WARMTH), (-3, wy, 4), aim=(1.2, wy - 0.6, 0), size=R(3))
fill_color = kelvin(5600) if not NIGHT else lin("#7C86FF")[:3]
light("Light_Fill", "AREA", 250 * (W * D / 16) * max(DAYLIGHT, 0.2), fill_color, (W + 3, -3, H + 2.5),
      aim=(W / 2, D / 2, 0.6), size=6)
light("Light_Bounce", "AREA", 40 * max(DAYLIGHT, 0.4), kelvin(6500) if not NIGHT else lin("#8A6BFF")[:3],
      (W / 2, D / 2, H - 0.1), aim=(W / 2, D / 2, 0), size=2.5)
# Weak fill lights over the seats, so furniture built from photos never turns flat black at night.
for seat, (ox, oy) in (("sofa", (0.8, 0.0)), ("chair", (0.2, -0.5))):    # kept away from the walls (no hot spots)
    s = SLOTS[seat]
    fl = light(f"Light_Fill_{seat}", "AREA", 12, kelvin(5200), (s.location.x + ox, s.location.y + oy, H - 0.25),
               aim=(s.location.x, s.location.y, 0.4), size=1.0)
    if hasattr(fl.data, "specular_factor"):
        fl.data.specular_factor = 0.0             # no bright reflection spot on the floor

# World: the camera sees the flat background colour; the room gets a soft ambient (dim and blue at night).
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
bg_amb.inputs["Color"].default_value = (*kelvin(6000), 1) if not NIGHT else lin("#5560B0")
bg_amb.inputs["Strength"].default_value = 0.35 * max(DAYLIGHT, 0.35)
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
                    ("shadow_ray_count", 2), ("use_gtao", True), ("use_soft_shadows", True), ("use_fast_gi", True),
                    ("use_bloom", True)):
    if hasattr(ee, attr):
        setattr(ee, attr, value)
if hasattr(ee, "ray_tracing_options"):
    ee.ray_tracing_options.resolution_scale = "2" if "2" in [i.identifier for i in
        type(ee.ray_tracing_options).bl_rna.properties["resolution_scale"].enum_items] else ee.ray_tracing_options.resolution_scale
scene.view_settings.view_transform = "Standard"   # keeps your hex colours exactly as typed
scene.view_settings.exposure = 0.25 if NIGHT else -0.35


def add_glow(strength):
    """Soft bloom around the bright LEDs (compositor Glare node). Skipped quietly if this Blender differs."""
    try:
        if hasattr(scene, "compositing_node_group"):                # Blender 5+
            tree = bpy.data.node_groups.new("RoomKit_Glow", "CompositorNodeTree")
            tree.interface.new_socket("Image", in_out="OUTPUT", socket_type="NodeSocketColor")
            scene.compositing_node_group = tree
            out_node = tree.nodes.new("NodeGroupOutput")
        else:                                                       # Blender 4.x
            scene.use_nodes = True
            tree = scene.node_tree
            tree.nodes.clear()
            out_node = tree.nodes.new("CompositorNodeComposite")
        rl = tree.nodes.new("CompositorNodeRLayers")
        g = tree.nodes.new("CompositorNodeGlare")
        if "Type" in g.inputs:                                      # newer Blender: options are inputs
            g.inputs["Type"].default_value = "Bloom"
            g.inputs["Threshold"].default_value = 0.9
            g.inputs["Strength"].default_value = strength
            g.inputs["Size"].default_value = 0.6
        else:                                                       # Blender 4.2 - 4.4
            types = [i.identifier for i in g.bl_rna.properties["glare_type"].enum_items]
            g.glare_type = "BLOOM" if "BLOOM" in types else "FOG_GLOW"
            g.threshold, g.size = 0.9, 8
            if hasattr(g, "mix"):
                g.mix = -1 + min(1.0, strength) * 0.6
        tree.links.new(rl.outputs["Image"], g.inputs["Image"])
        tree.links.new(g.outputs["Image"], out_node.inputs[0])
    except Exception as err:
        print(f"[RoomKit] glow effect skipped ({err})")


add_glow(0.8 if NIGHT else 0.3)

# Remember the style so add_furniture.py can match colours later.
scene["kit_style"] = STYLE
scene["kit_version"] = KIT_VERSION
scene["kit_palette"] = json.dumps(COLORS)
scene["kit_material_finish"] = json.dumps({"roughness": 0.5, "bevel": 0.015, "saturation": 0.85 if NIGHT else 0.7})
scene["kit_theme"] = THEME
scene["kit_bounds"] = [-T, 0.0, -0.2, W, D + T, H + 0.12]   # used to re-frame the camera for social sizes
scene["kit_furniture_colors"] = json.dumps(["main", "wood", "cream", "dark", "desk", "plant", "accent_1", "accent_2",
                                            "accent_3"])   # colours add_furniture.py may use (no neon / sky)


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
