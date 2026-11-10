"""
3D ROOM PORTFOLIO KIT  -  Template: HOME MUSIC & PODCAST STUDIO
================================================================
Builds a cosy isometric home studio from scratch and renders a 1920x1080 image:
a producer desk with rack bays and nearfield monitors, a digital piano on an X-stand, a condenser mic
on a boom stand, an acoustic guitar and a tweed combo amp, a KALLAX full of records with a turntable,
wood slat panels and a neon sign with your name.
Every piece is modelled on a real product you can buy or have seen - see REFERENCES below.
For musicians, producers, DJs, podcasters, voice actors and sound designers.

HOW TO RUN
  Option A (no Blender UI):   blender -b -P music_studio.py
  Option B (inside Blender):  Scripting tab > Open > music_studio.py > Run Script (then F12 to render)

You only need to edit the SETTINGS block below. Everything under it builds the room.
Output: output/music_studio.png and output/music_studio.blend next to this script.
"""

# REFERENCES  (product names live only here and in research/music_studio.md - never in the scene)
#   desk       Producer desk, Output Platform / Studio RTA Producer Station style: top 152x70x2.5 cm at 74 cm,
#              18 cm bridge with a 4U 19" rack bay at each end, 8U rack bay under the right side, keyboard tray
#              https://djmag.com/tech/output-launch-new-hardware-product
#              https://www.thomann.de/ie/studiorta_producer_station_cherry.htm
#   monitors   Yamaha HS5-type nearfields 17x22.2x28.5 cm, white 5" woofer, 1" tweeter
#              https://ca.yamaha.com/en/products/contents/proaudio/musicianspa/products_studio_monitor.html
#   pads       IsoAcoustics ISO-155-type isolation stands 15.5x19x7.6 cm   https://zzounds.com/item--ISOISO155
#   interface  Focusrite Scarlett 2i2-type, 18x9.9x4.55 cm, red body, halo gain knobs
#              https://www.thomann.co.uk/focusrite_scarlett_2i2_4th_generation.htm
#   screen     27-inch monitor, panel 59.8x33.6 cm, 7 mm bezel, rectangular stand
#   chair      IKEA MARKUS office chair 62x60 cm, seat 47 cm, back 129 cm, five-star base, one-piece wrap-around
#              back with built-in headrest on a black shell
#              https://www.ikea.com/fi/en/p/markus-office-chair-vissle-light-grey-10521858
#   instrument Yamaha P-45-type 88-key digital piano 132.6x29.5x15.4 cm on a double-braced X stand (KS7191 type)
#              https://usa.yamaha.com/products/musical_instruments/pianos/p_series/p-45/specs.html
#              https://www.zzounds.com/item--MUPKS7191
#   hero_prop  Rode NT1-type condenser (189x52 mm, silver finish) in a two-ring shock mount, 6" pop filter,
#              tripod boom stand tipped 10 degrees down towards a seated voice over the sofa
#              https://edge.rode.com//pdf/products/1183/NT1%205th%20GEN_Datasheet.pdf
#   headphones Audio-Technica ATH-M50x-type closed-back headphones, cups 8.5x10x4.6 cm, on a desk hook
#              https://www.crutchfield.com/S-Al0KmaQ2TXK/p_901M50X/Audio-Technica-ATH-M50x.html
#   guitar     Yamaha F310-type dreadnought: 102.9 cm long, body 50.5x41.2x10 cm, 63.4 cm scale; tripod stand
#              https://usa.yamaha.com/products/musical_instruments/guitars_basses/ac_guitars/f_fx/specs.html
#              https://herculesstands.com/products/fretted-and-bowed-instrument/guitar/single-stands/gs414b-plus
#   speaker    Fender Blues Junior-type 1x12 combo in lacquered tweed (diagonal twill), 45.7x23.3x40.6 cm
#              https://www.thomann.co.uk/fender_blues_junior_tweed.htm
#   shelf      IKEA KALLAX 77x39x77 cm, 4 cm frame, 1.6 cm dividers, LPs (31.4 cm sleeves)
#              https://www.ikea.com/qa/en/p/kallax-shelving-unit-white-20275814/
#   turntable  Technics SL-1200MK7-type direct-drive turntable 45.3x35.3x16.9 cm
#              https://technics.com/ca/products/dj-series/sl-1200mk7.html
#   sofa       IKEA LANDSKRONA 2-seat sofa, golden-brown leather, 164x89x78 cm, seat 44 cm, wooden legs
#              https://www.ikea.com/au/en/files/pdf/49/d5/49d53ff6/landskrona_fy22_oct21.pdf
#   floor_lamp IKEA HEKTAR floor lamp 181 cm, 31.5 cm cone shade, 34 cm base
#              https://www.ikea.com/gb/en/p/hektar-floor-lamp-dark-grey-60216549/
#   slats      Woodupp Akupanel 240-type slat panels 240x60 cm, 27 mm slats, 13 mm gaps, black felt
#              https://woodupp.co.uk/product/akupanel-240
#   foam       Auralex Studiofoam Wedgies-type tiles 30x30x5 cm (1 ft x 1 ft x 2 in), checkerboard ridges
#              https://www.adorama.com/aurwedgie24.html
#   ledges     IKEA MOSSLANDA picture ledge 115x12 cm holding LP sleeves (frame hooks)
#              https://www.ikea.com/no/en/p/mosslanda-picture-ledge-white-40291766/
#   posters    IKEA RIBBA frames 52x72 and 32x42 cm   https://www.ikea.com/my/en/p/ribba-frame-white-00378460
#   rug        Vintage Persian-style rug 200x140 cm: navy border, rust field with an all-over flower repeat,
#              serrated diamond medallion with end pendants, corner spandrels, fringes
#   sign       Custom LED neon sign on black acrylic 120x46 cm + generic ON AIR light box 34x11 cm
#   decor      Box cajon 30x30x48 cm, snake plant in a 22 cm pot, Type 22 radiator 80x50 cm, oak floorboards 19 cm

# =====================================================================
#  SETTINGS  -  change these lines, then run the script again
# =====================================================================
ROOM_NAME = "music_studio"          # used for the output file names

ROOM_WIDTH = 4.4                    # metres, left to right
ROOM_DEPTH = 4.2                    # metres, front to back
WALL_HEIGHT = 2.8                   # metres

THEME = "evening"                   # pick one of the colour themes below
THEMES = {                          # any hex colour works; "main" is the leather sofa colour
    # "evening" is a dusk session: low sunset light through the blinds, amber lamps, one teal LED strip.
    # "daylight" is a bright morning: white sun, dimmer lamps. The lights switch too - see LIGHTS below.
    "evening": {
        "background": "#26242C", "wall": "#76625C", "wall_trim": "#3A302E", "floor": "#8C5E40",
        "wood": "#5E3D2C", "main": "#A0582F", "accent_1": "#E8A23D", "accent_2": "#2BB3A7",
        "accent_3": "#A8402F", "cream": "#E6D6BF", "plant": "#5E8C5A", "dark": "#1C1B20",
        "foam": "#3C3A42", "metal": "#9A979E", "guitar": "#D9A462", "sky": "#F4B57E", "onair": "#E5402F",
        "kallax": "#E4DED3", "oak": "#9C7048", "speaker": "#1A191D", "tweed": "#C9A15E", "grille": "#4E2C22",
        "navy": "#26304A",
    },
    "daylight": {
        "background": "#ECE6DD", "wall": "#E3D8CA", "wall_trim": "#C7B39E", "floor": "#BD8E62",
        "wood": "#8A5E40", "main": "#B5683F", "accent_1": "#E8A23D", "accent_2": "#2BB3A7",
        "accent_3": "#B84A36", "cream": "#FBF5EA", "plant": "#6E9A5E", "dark": "#2A2930",
        "foam": "#5A6470", "metal": "#B0ACB3", "guitar": "#E0AE6C", "sky": "#DDEFFF", "onair": "#E5402F",
        "kallax": "#F4F2EE", "oak": "#C09464", "speaker": "#EDECE8", "tweed": "#D2AC6A", "grille": "#5A3427",
        "navy": "#2E3A5C",
    },
}

SUN_WARMTH = 2900                   # Kelvin: 2500 = sunset orange, 6500 = white daylight
SUN_STRENGTH = 4.5                  # light coming in through the window blinds
LAMP_WARMTH = 2400                  # Kelvin of the floor lamp and the keyboard spotlight
LAMP_STRENGTH = 70                  # Watts of the floor lamp
SPOT_STRENGTH = 1400                # Watts of the soft spotlight above the keyboard (the hero)
LED_STRENGTH = 60                   # Watts of the teal LED strip behind the desk
SEED = 7                            # change to shuffle records, gear and small props

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

STYLE = "music_studio"
KIT_VERSION = 2
W, D, H = ROOM_WIDTH, ROOM_DEPTH, WALL_HEIGHT
T = 0.15            # wall thickness
FLOOR_Z = 0.02      # top of the oak floor boards; furniture stands here
R = math.radians
DAY = THEME == "daylight"
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
    """Partly transparent material (pop filter mesh): you can see through it."""
    m = mat(key, rough).copy()
    m.name = f"M_{key}_mesh"
    _set(_principled(m), ["Alpha"], alpha)
    if hasattr(m, "surface_render_method"):
        m.surface_render_method = "DITHERED"
    elif hasattr(m, "blend_method"):
        m.blend_method = "HASHED"
    return m


# --------------------------------------------------------------------- shared real-world materials
WALNUT = surface(mat("wood", 0.42), "veneer")                         # desk, sofa legs, guitar back and sides
WALNUT_V = surface(mat("wood", 0.43), "veneer", along="Z")            # upright panels: grain runs vertically
OAK_SLAT = surface(mat("oak", 0.55), "veneer", along="Z")             # vertical acoustic slats
STEEL = surface(mat("metal", 0.3, metal=0.85), "brushed")             # stands, standoffs, rails
CHROME = mat("metal", 0.12, metal=1.0, color="#D8D8DC")
POWDER = surface(mat("dark", 0.5, metal=0.15), "brushed")             # powder-coated steel (stands, rack rails)
PLASTIC = mat("dark", 0.45)
RUBBER = mat("dark", 0.85, color=shade(COLORS["dark"], 0.8))
FELT = surface(mat("dark", 0.95, color="#151417"), "fabric")
LEATHER = surface(mat("main", 0.45), "leather")
KALLAX_M = mat("kallax", 0.45)                                        # white melamine foil board
PAPER = surface(mat("paper", 0.85, color="#F3EEE2"), "paper")
CAB = mat("speaker", 0.42)                                            # monitor cabinets (black or white)
ALU = surface(mat("metal", 0.38, metal=0.7, color="#C4C4C8"), "brushed")


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
    """Many boxes in ONE object (keys, records, slats, floor boards). items = [(size, centre[, rot]), ...]."""
    bm = bmesh.new()
    for it in items:
        verts = bmesh.ops.create_cube(bm, size=1.0)["verts"]
        bmesh.ops.scale(bm, vec=Vector(it[0]), verts=verts)
        if len(it) > 2:
            bmesh.ops.rotate(bm, verts=verts, cent=(0, 0, 0), matrix=Euler(it[2]).to_matrix())
        bmesh.ops.translate(bm, vec=Vector(it[1]), verts=verts)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, bevel, coll, parent)


def cyl(name, r, h, loc, material, r2=None, segs=32, bevel=0.003, rot=(0, 0, 0), coll=None, parent=None, caps=True):
    """Cylinder (or tapered cylinder with r2). loc = centre."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=caps, segments=segs, radius1=r, radius2=r if r2 is None else r2, depth=h)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, bevel, coll, parent)


def disc(name, r, loc, material, facing="-y", depth=0.004, segs=40, parent=None):
    """Thin flat disc (cones, knobs, records) facing -y or +x."""
    rot = (R(90), 0, 0) if facing == "-y" else (0, R(90), 0)
    return cyl(name, r, depth, loc, material, segs=segs, bevel=0, rot=rot, parent=parent)


def ball(name, r, loc, material, scale=(1, 1, 1), coll=None, parent=None):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=24, v_segments=14, radius=r)
    o = _obj(name, bm)
    o.location, o.scale = loc, scale
    return _finish(o, material, 0, coll, parent)


def rod(name, a, b, r, material, parent=None, segs=12):
    """A thin straight tube from point a to point b (stand legs, strings, cables)."""
    a, b = Vector(a), Vector(b)
    o = cyl(name, r, (b - a).length, (a + b) / 2, material, segs=segs, bevel=0, parent=parent)
    o.rotation_euler = (b - a).to_track_quat("Z", "Y").to_euler()
    return o


def tube(name, pts, r, material, closed=False, segs=10, parent=None, coll=None):
    """A round tube swept along a list of points (cables, headband, rings, piping)."""
    pts = [Vector(p) for p in pts]
    n = len(pts)
    bm = bmesh.new()
    rings, normal = [], None
    for i, p in enumerate(pts):
        tang = (pts[(i + 1) % n] - pts[i - 1]) if closed else (pts[min(i + 1, n - 1)] - pts[max(i - 1, 0)])
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


def circle(c, r, plane="XZ", n=32):
    """Points on a circle around c, in the XZ (faces -y) or YZ (faces +x) or XY (flat) plane."""
    out = []
    for k in range(n):
        a = 2 * math.pi * k / n
        u, v = math.cos(a) * r, math.sin(a) * r
        off = {"XZ": (u, 0, v), "YZ": (0, u, v), "XY": (u, v, 0)}[plane]
        out.append(Vector(c) + Vector(off))
    return out


def bezier(p0, p1, p2, n=12):
    """Points on a smooth curve from p0 to p2 that bends towards p1."""
    p0, p1, p2 = Vector(p0), Vector(p1), Vector(p2)
    return [(1 - t) ** 2 * p0 + 2 * (1 - t) * t * p1 + t * t * p2 for t in (i / n for i in range(n + 1))]


def slab(name, pts2d, depth, loc, material, rot=(0, 0, 0), bevel=0.0, parent=None):
    """A flat outline (x, z) extruded `depth` along +y (guitar body, pickguard, leaves). Front face at y = 0."""
    bm = bmesh.new()
    face = bm.faces.new([bm.verts.new((x, 0, z)) for x, z in pts2d])
    ext = bmesh.ops.extrude_face_region(bm, geom=[face])
    bmesh.ops.translate(bm, vec=(0, depth, 0), verts=[e for e in ext["geom"] if isinstance(e, bmesh.types.BMVert)])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, bevel, None, parent)


def prisms(name, items, material, segs=4, parent=None, z_up=True):
    """Many low prisms (rug diamonds, octagons) in one object. items = [(radius_x, radius_y, height, centre)]."""
    bm = bmesh.new()
    for rx, ry, h, c in items:
        m = Matrix.Translation(c) @ Matrix.Diagonal((rx, ry, 1, 1))
        bmesh.ops.create_cone(bm, cap_ends=True, segments=segs, radius1=1, radius2=1, depth=h, matrix=m)
    o = _obj(name, bm)
    return _finish(o, material, 0, None, parent)


def sub(name, loc, rot, parent):
    """An empty in the parent's local space, so a group of parts (a monitor, a turntable) can be turned."""
    e = bpy.data.objects.new(name, None)
    e.empty_display_size = 0.05
    e.location, e.rotation_euler = loc, rot
    COL_FURN.objects.link(e)
    e.parent = parent
    return e


def no_shadow(*objs):
    for o in objs:
        if hasattr(o, "visible_shadow"):
            o.visible_shadow = False
    return objs


def label(name, text, size, loc, material, rot=(R(90), 0, 0), parent=None, align="CENTER", depth=0.002):
    """Small 3D text that is NOT a hook (e.g. the words ON AIR)."""
    cu = bpy.data.curves.new(name, "FONT")
    cu.body, cu.size, cu.align_x, cu.align_y = text, size, align, "CENTER"
    cu.extrude = depth
    o = bpy.data.objects.new(name, cu)
    o.location, o.rotation_euler = loc, rot
    o.data.materials.append(material)
    (COL_ROOM if parent is None else COL_FURN).objects.link(o)
    o.parent = parent
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
    bpy.context.view_layer.update()     # so root.matrix_world is ready for lights placed in its space
    return root, w, d, h


# --------------------------------------------------------------------- portfolio hooks
# Hooks are where YOUR content goes. tools/build_portfolio.py fills them from profile.json:
#   picture hooks: "screen" (glows), "poster", "frame"  -> project images (in that order)
#   text hooks:    "name", "role" (on the neon sign)
#   link hooks:    the microphone = email, the record shelf = github, the neon sign = website
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
    if parent is not None:                  # keep the world position, follow the furniture
        bpy.context.view_layer.update()
        mw = o.matrix_world.copy()
        o.parent = parent
        o.matrix_world = mw
    return o


# =====================================================================
#  ROOM SHELL
# =====================================================================
# Diorama base slab, then engineered oak boards (19 cm wide) running front to back with staggered joints.
box("Floor_Base", (W + T, D + T, 0.2), ((W - T) / 2, (D + T) / 2, -0.1), mat("wall_trim", 0.7), bevel=0.03)
BOARD_W = 0.19
tones = [[] for _ in range(3)]
for i in range(math.ceil(W / BOARD_W)):
    x0, x1 = i * BOARD_W, min(W, (i + 1) * BOARD_W)
    y = -random.uniform(0.2, 1.4)                                   # stagger the end joints
    while y < D:
        L = random.uniform(1.2, 2.0)
        y0, y1 = max(0.0, y), min(D, y + L)
        if y1 - y0 > 0.05:
            tones[random.randrange(3)].append(((x1 - x0 - 0.003, y1 - y0 - 0.003, FLOOR_Z),
                                               ((x0 + x1) / 2, (y0 + y1) / 2, FLOOR_Z / 2)))
        y += L
for k, (items, f) in enumerate(zip(tones, (1.0, 0.93, 1.06))):
    m = surface(mat("floor", 0.4 + 0.03 * k, color=shade(COLORS["floor"], f)), "wood", scale=0.7, along="Y")
    boxes(f"Floor_Boards_{k}", items, m, bevel=0.0015)

# Walls: painted plaster. The window is cut into the front part of the left wall (sill at 90 cm).
WIN_Y = (0.45, 1.35)                # from front to back
WIN_Z = (0.9, 2.1)                  # bottom (sill height) and top
wall_m = surface(mat("wall", 0.85), "plaster", scale=3.0)
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
cap = surface(mat("wood", 0.5), "wood")
box("Trim_Top_Back", (W + T + 0.02, T + 0.02, 0.06), ((W - T) / 2, D + T / 2, H + 0.03), cap, bevel=0.012)
box("Trim_Top_Left", (T + 0.02, D + T + 0.02, 0.06), (-T / 2, (D + T) / 2 - 0.01, H + 0.03), cap, bevel=0.012)
skirt = mat("wall_trim", 0.4)
box("Skirting_Back", (W, 0.018, 0.12), (W / 2, D - 0.009, FLOOR_Z + 0.06), skirt, bevel=0.004)
box("Skirting_Left", (0.018, D, 0.12), (0.009, D / 2, FLOOR_Z + 0.06), skirt, bevel=0.004)
box("Skirting_Back_Ovolo", (W, 0.024, 0.016), (W / 2, D - 0.012, FLOOR_Z + 0.115), skirt, bevel=0.007)
box("Skirting_Left_Ovolo", (0.024, D, 0.016), (0.012, D / 2, FLOOR_Z + 0.115), skirt, bevel=0.007)

# Window: painted timber casement (frame + two sashes with handles), window board, a sunset sky outside.
wy, wz = sum(WIN_Y) / 2, sum(WIN_Z) / 2
ww, wh = WIN_Y[1] - WIN_Y[0], WIN_Z[1] - WIN_Z[0]
paint = mat("cream", 0.3)
FX = -T * 0.62
for nm, size, loc in [("Head", (0.07, ww, 0.06), (FX, wy, WIN_Z[1] - 0.03)),
                      ("Sill", (0.07, ww, 0.06), (FX, wy, WIN_Z[0] + 0.03)),
                      ("JambF", (0.07, 0.06, wh), (FX, WIN_Y[0] + 0.03, wz)),
                      ("JambB", (0.07, 0.06, wh), (FX, WIN_Y[1] - 0.03, wz)),
                      ("Mullion", (0.07, 0.05, wh), (FX, wy, wz))]:
    box(f"Window_Frame_{nm}", size, loc, paint, bevel=0.005)
sash_w = (ww - 0.12 - 0.05) / 2
for k, sy in enumerate((WIN_Y[0] + 0.06 + sash_w / 2, WIN_Y[1] - 0.06 - sash_w / 2)):
    for nm, size, off in [("T", (0.05, sash_w, 0.05), (0, wh / 2 - 0.085)), ("B", (0.05, sash_w, 0.07), (0, -wh / 2 + 0.095)),
                          ("F", (0.05, 0.05, wh - 0.12), (-sash_w / 2 + 0.025, 0)),
                          ("K", (0.05, 0.05, wh - 0.12), (sash_w / 2 - 0.025, 0))]:
        box(f"Window_Sash_{k}{nm}", size, (FX + 0.02, sy + off[0], wz + off[1]), paint, bevel=0.006)
    hy = sy - sash_w / 2 + 0.03 if k == 1 else sy + sash_w / 2 - 0.03
    box(f"Window_Handle_{k}", (0.018, 0.016, 0.1), (FX + 0.06, hy, wz - 0.08), STEEL, bevel=0.005)
glass = box("Window_Glass", (0.006, ww - 0.08, wh - 0.08), (FX + 0.02, wy, wz), mat("sky", 0.08, emit=0.9), bevel=0)
no_shadow(glass)
box("Window_Board", (0.24, ww + 0.12, 0.025), (0.06, wy, WIN_Z[0] + 0.0125), paint, bevel=0.005)
for k in range(4):                                                  # far rooftops in the sunset
    no_shadow(box(f"Window_Roof_{k}", (0.01, 0.18 + 0.05 * (k % 2), 0.12 + 0.07 * ((k * 3) % 4)),
                  (FX - 0.03, WIN_Y[0] + 0.12 + k * 0.22, WIN_Z[0] + 0.1), mat("wall_trim", 0.9, emit=0.3), bevel=0))

# Venetian blind with 25 mm aluminium slats, half lowered and tilted, so the light falls in stripes.
blind = surface(mat("cream", 0.42, metal=0.3), "brushed", along="Y")
box("Blind_Headrail", (0.035, ww + 0.04, 0.035), (0.03, wy, WIN_Z[1] + 0.02), blind, bevel=0.004)
for k in range(13):
    box(f"Blind_Slat_{k}", (0.025, ww + 0.02, 0.0015), (0.03, wy, WIN_Z[1] - 0.03 - k * 0.042), blind,
        bevel=0, rot=(0, R(38), 0))
box("Blind_Bottom_Rail", (0.03, ww + 0.02, 0.012), (0.03, wy, WIN_Z[1] - 0.58), blind, bevel=0.004)
for sy in (-1, 1):
    rod("Blind_Ladder", (0.044, wy + sy * ww * 0.32, WIN_Z[1] + 0.005), (0.044, wy + sy * ww * 0.32, WIN_Z[1] - 0.58),
        0.0012, mat("cream", 0.7), segs=5)
rod("Blind_Wand", (0.05, WIN_Y[1] - 0.04, WIN_Z[1]), (0.05, WIN_Y[1] - 0.04, WIN_Z[1] - 0.45), 0.004, blind, segs=8)

# Type 22 panel radiator (80 x 50 x 10 cm) under the window: pressed ribs, top grille, valve and pipes.
RX, RZ, RL = 0.075, FLOOR_Z + 0.16, 0.8
rad = mat("cream", 0.32)
box("Radiator_Back", (0.022, RL, 0.5), (RX - 0.035, wy, RZ + 0.25), rad, bevel=0.006)
box("Radiator_Front", (0.022, RL, 0.5), (RX + 0.035, wy, RZ + 0.25), rad, bevel=0.006)
boxes("Radiator_Ribs", [((0.006, 0.022, 0.46), (RX + 0.048, wy - RL / 2 + 0.03 + 0.0333 * k, RZ + 0.25))
                        for k in range(23)], rad, bevel=0.0025)
boxes("Radiator_Grille", [((0.07, 0.006, 0.004), (RX, wy - RL / 2 + 0.02 + 0.02 * k, RZ + 0.502)) for k in range(39)],
      mat("dark", 0.7, color=shade(COLORS["cream"], 0.55)))
for k, sy in enumerate((wy - RL / 2 - 0.06, wy + RL / 2 + 0.06)):
    rod(f"Radiator_Pipe_{k}", (RX, sy, FLOOR_Z), (RX, sy, RZ + 0.04), 0.0075, STEEL)
cyl("Radiator_Valve", 0.024, 0.07, (RX, wy - RL / 2 - 0.06, RZ + 0.09), rad, bevel=0.008)

# Acoustic slat panels behind the desk: two 240 x 60 cm panels, 27 mm veneer slats with black felt in the gaps.
SLAT_X0 = 2.98
for p in range(2):
    px = SLAT_X0 + p * 0.6
    box(f"Slat_Felt_{p}", (0.598, 0.009, 2.4), (px + 0.3, D - 0.0045, FLOOR_Z + 0.14 + 1.2), FELT, bevel=0.001)
    boxes(f"Slat_Slats_{p}", [((0.027, 0.013, 2.4), (px + 0.0135 + 0.0065 + 0.04 * k, D - 0.0155, FLOOR_Z + 0.14 + 1.2))
                              for k in range(15)], OAK_SLAT, bevel=0.0015)

# Studio foam wedge tiles (30 x 30 x 5 cm) on the left wall at the sofa end, ridges alternating like a checkerboard.
def foam_tile(name, y, z, vertical):
    """One wedge tile on the left wall (faces +x): a 1 cm base and five 4 cm triangular ridges."""
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0, matrix=Matrix.Translation((0.005, 0, 0)) @ Matrix.Diagonal((0.01, 0.3, 0.3, 1)))
    for k in range(5):
        o = -0.15 + 0.03 + k * 0.06
        pts = [(0.01, o - 0.03, -0.15), (0.01, o + 0.03, -0.15), (0.05, o, -0.15)]
        vs0 = [bm.verts.new(p) for p in pts]
        vs1 = [bm.verts.new((p[0], p[1], 0.15)) for p in pts]
        bm.faces.new(vs0[::-1])
        bm.faces.new(vs1)
        for i in range(3):
            bm.faces.new((vs0[i], vs0[(i + 1) % 3], vs1[(i + 1) % 3], vs1[i]))
    if not vertical:
        bmesh.ops.rotate(bm, verts=bm.verts, cent=(0, 0, 0), matrix=Matrix.Rotation(R(90), 3, "X"))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    o = _obj(name, bm)
    o.location = (0.0, y, z)
    return _finish(o, surface(mat("foam", 0.95), "knit", scale=2.0), 0, None, None)


for i in range(2):
    for j in range(3):
        foam_tile(f"Foam_Tile_{i}{j}", 1.88 + i * 0.302, 1.2 + j * 0.302, (i + j) % 2 == 0)


# =====================================================================
#  FURNITURE SLOTS  (same names in every template)
#  size = (width, depth, height); front of the furniture faces local -Y
# =====================================================================
slot("instrument", (1.33, 0.42, 1.15),   (2.3, 1.75), turn=25, shape="table")
slot("hero_prop",  (0.5, 0.5, 1.7),     (1.5, 2.62), turn=270, shape="lamp")
slot("desk",       (1.52, 0.7, 1.0),    (3.55, D - 0.385), shape="table")
slot("chair",      (0.62, 0.6, 1.29),   (3.45, 3.03), turn=180, shape="chair")
slot("sofa",       (1.64, 0.89, 0.78),  (0.45, 2.55), turn=90, shape="sofa")
slot("shelf",      (0.77, 0.39, 0.95),  (1.25, D - 0.2), shape="shelf")
slot("speaker",    (0.46, 0.24, 0.43),  (3.88, 1.82), turn=30, shape="box")
slot("floor_lamp", (0.4, 0.5, 1.81),   (0.33, D - 0.36), turn=45, shape="lamp")
slot("rug",        (2.0, 1.4, 0.012),   (2.15, 2.05), kind="rug", shape="rug")


# =====================================================================
#  PLACEHOLDER FURNITURE  (replaced when you add your own with add_furniture.py)
# =====================================================================
U = 0.04445                                                         # one rack unit (1U) in metres


def rack_unit(name, units, loc, style, parent):
    """One 19-inch rack device (48.3 cm wide face), front at loc (centre of the face), facing -y."""
    x, y, z = loc
    hgt = units * U - 0.001
    face = {"preamp": ALU, "power": PLASTIC, "comp": PLASTIC, "vent": PLASTIC, "blank": POWDER,
            "converter": ALU}[style]
    box(f"{name}_Face", (0.483, 0.005, hgt), (x, y, z), face, bevel=0.0015, parent=parent)
    box(f"{name}_Chassis", (0.43, 0.2, hgt - 0.004), (x, y + 0.103, z), PLASTIC, bevel=0.002, parent=parent)
    for sx in (-1, 1):                                              # rack screws in the ears
        for sz in ((-1, 1) if units > 1 else (0,)):
            cyl(f"{name}_Screw", 0.0035, 0.003, (x + sx * 0.233, y - 0.003, z + sz * (hgt / 2 - 0.012)), STEEL,
                segs=10, bevel=0, rot=(R(90), 0, 0), parent=parent)
    knob = mat("dark", 0.35, color="#0E0E10")
    fy = y - 0.0035
    if style == "preamp":                                           # two-channel tube preamp: VU meters + big knobs
        for sx in (-1, 1):
            box(f"{name}_VU", (0.07, 0.004, 0.045), (x + sx * 0.15, fy, z + 0.005),
                mat("cream", 0.4, emit=1.2, color="#F6E3B4"), bevel=0.002, parent=parent)
            rod(f"{name}_Needle", (x + sx * 0.15, fy - 0.003, z - 0.012), (x + sx * 0.15 + 0.015, fy - 0.003, z + 0.02),
                0.0008, mat("dark", 0.5), parent=parent, segs=4)
            for j, kx in enumerate((0.05, 0.09)):
                cyl(f"{name}_Knob", 0.014 if j == 0 else 0.01, 0.018, (x + sx * kx, fy - 0.009, z), knob, segs=20,
                    bevel=0.002, rot=(R(90), 0, 0), parent=parent)
            box(f"{name}_Toggle", (0.004, 0.012, 0.004), (x + sx * 0.205, fy - 0.006, z), STEEL, bevel=0, parent=parent)
    elif style == "power":                                          # power conditioner: amber read-out + switch
        box(f"{name}_Display", (0.05, 0.003, 0.018), (x, fy, z), mat("accent_1", 0.3, emit=4.0), bevel=0.001,
            parent=parent)
        box(f"{name}_Switch", (0.022, 0.006, 0.016), (x - 0.18, fy - 0.002, z), mat("onair", 0.4, emit=1.5),
            bevel=0.002, parent=parent)
        for sx in (0.12, 0.17):
            cyl(f"{name}_Lamp", 0.008, 0.012, (x + sx, fy - 0.004, z), STEEL, segs=12, bevel=0, rot=(R(90), 0, 0),
                parent=parent)
    elif style == "comp":                                           # compressor: row of knobs + LED meter
        for j in range(6):
            cyl(f"{name}_Knob", 0.008, 0.012, (x - 0.17 + j * 0.05, fy - 0.005, z), mat("cream", 0.4), segs=14,
                bevel=0.001, rot=(R(90), 0, 0), parent=parent)
        for j in range(8):
            box(f"{name}_LED", (0.006, 0.003, 0.006), (x + 0.15 + j * 0.008, fy, z),
                mat("accent_2" if j < 5 else ("accent_1" if j < 7 else "onair"), 0.3, emit=3.0 if j < 6 else 0.6),
                bevel=0, parent=parent)
    elif style == "converter":                                      # multi-channel converter: meters + screen
        for j in range(8):
            box(f"{name}_Meter", (0.006, 0.003, 0.05), (x - 0.12 + j * 0.012, fy, z), mat("dark", 0.4), bevel=0,
                parent=parent)
            box(f"{name}_MeterLit", (0.006, 0.0032, 0.012 + 0.004 * (j % 4)), (x - 0.12 + j * 0.012, fy - 0.0005,
                z - 0.019 + 0.002 * (j % 4)), mat("accent_2", 0.3, emit=3.0), bevel=0, parent=parent)
        box(f"{name}_Screen", (0.06, 0.003, 0.03), (x + 0.1, fy, z), mat("accent_2", 0.3, emit=1.5), bevel=0.001,
            parent=parent)
        cyl(f"{name}_Knob", 0.012, 0.015, (x + 0.18, fy - 0.007, z), knob, segs=18, rot=(R(90), 0, 0), parent=parent)
    elif style == "vent":                                           # vent panel: slots
        boxes(f"{name}_Slots", [((0.03, 0.003, 0.006), (x - 0.18 + j * 0.04, fy, z)) for j in range(10)],
              mat("dark", 0.8, color="#050506"), parent=parent)


def build_desk():
    """Producer desk: veneer top and side panels, a monitor bridge with two 4U rack bays, an 8U rack under
    the right side, a keyboard tray, two nearfield monitors on isolation pads, a 27-inch screen, a mini
    MIDI controller, a red audio interface, headphones on a hook and the teal LED strip."""
    root, w, d, h = furniture_root("desk")
    TOP = 0.74
    box("Desk_Top", (w, d, 0.025), (0, 0, TOP - 0.0125), WALNUT, bevel=0.003, parent=root)
    for sx in (-1, 1):
        box("Desk_Side", (0.025, d - 0.03, TOP - 0.025 - 0.012), (sx * (w / 2 - 0.0125), 0.0, (TOP - 0.025) / 2 + 0.006),
            WALNUT_V, bevel=0.003, parent=root)
        for sy in (-1, 1):
            cyl("Desk_Glide", 0.011, 0.012, (sx * (w / 2 - 0.0125), sy * (d / 2 - 0.05), 0.006), RUBBER, segs=12,
                bevel=0, parent=root)
    box("Desk_Modesty", (w - 0.05, 0.018, 0.3), (0, d / 2 - 0.05, TOP - 0.025 - 0.15), WALNUT, bevel=0.002,
        parent=root)
    # 8U rack bay under the right side (Producer Station style): rails, units, a gap and a plinth.
    bx = w / 2 - 0.025 - 0.2415
    fy = -d / 2 + 0.035
    box("Desk_Rack_Side", (0.018, d - 0.08, 0.4), (bx - 0.2505, 0.0, 0.06 + 0.2), WALNUT_V, bevel=0.002, parent=root)
    box("Desk_Rack_Bottom", (0.501, d - 0.08, 0.018), (bx - 0.009, 0.0, 0.051), WALNUT, bevel=0.002, parent=root)
    box("Desk_Rack_Plinth", (0.49, 0.018, 0.04), (bx - 0.009, fy + 0.03, 0.022), PLASTIC, bevel=0.002, parent=root)
    box("Desk_Rack_Back", (0.483, 0.01, 0.36), (bx, d / 2 - 0.06, 0.24), mat("dark", 0.7), bevel=0, parent=root)
    for sx in (-1, 1):
        box("Desk_Rack_Rail", (0.016, 0.012, 0.36), (bx + sx * 0.2335, fy + 0.006, 0.06 + 0.18), POWDER, bevel=0.001,
            parent=root)
    z = 0.06
    for k, (units, style) in enumerate([(2, "converter"), (1, "vent"), (2, "preamp"), (1, "comp"), (1, "power")]):
        rack_unit(f"Desk_LowRack_{k}", units, (bx, fy - 0.002, z + units * U / 2), style, root)
        z += units * U
    # The bridge: an 18 cm high shelf across the back with a 4U rack bay at each end.
    by, bd, bz = d / 2 - 0.135, 0.27, TOP + 4 * U
    box("Desk_Bridge", (w, bd, 0.022), (0, by, bz + 0.011), WALNUT, bevel=0.003, parent=root)
    bay_styles = {-1: [(1, "comp"), (2, "preamp"), (1, "vent")], 1: [(1, "power"), (2, "converter"), (1, "comp")]}
    for sx in (-1, 1):
        cx = sx * (w / 2 - 0.018 - 0.2415)
        for ox in (-1, 1):
            box("Desk_Bay_Side", (0.018, bd, 4 * U), (cx + ox * 0.2505, by, TOP + 2 * U), WALNUT_V, bevel=0.002,
                parent=root)
        z = TOP
        for k, (units, style) in enumerate(bay_styles[sx]):
            rack_unit(f"Desk_Bay_{sx}_{k}", units, (cx, by - bd / 2 + 0.004, z + units * U / 2), style, root)
            z += units * U
    # Keyboard tray on runners, pulled out a little, with a slim aluminium keyboard and a mouse.
    tx = -0.22
    box("Desk_Tray", (0.67, 0.3, 0.016), (tx, -d / 2 + 0.11, TOP - 0.085), WALNUT, bevel=0.002, parent=root)
    for sx in (-1, 1):
        box("Desk_Tray_Runner", (0.012, 0.42, 0.035), (tx + sx * 0.341, -d / 2 + 0.2, TOP - 0.06), POWDER, bevel=0.001,
            parent=root)
    kz = TOP - 0.077 + 0.005
    box("Desk_Keyboard", (0.28, 0.115, 0.008), (tx - 0.04, -d / 2 + 0.1, kz), ALU, bevel=0.003, parent=root)
    boxes("Desk_Keyboard_Keys", [((0.0155, 0.0155, 0.003), (tx - 0.04 - 0.13 + 0.0185 * c + 0.009 * (r % 2),
                                  -d / 2 + 0.1 - 0.042 + 0.019 * r, kz + 0.005)) for r in range(5) for c in range(14)
                                 if not (r == 0 and 3 < c < 10)] + [((0.1, 0.0155, 0.003), (tx - 0.04, -d / 2 + 0.058,
                                                                                           kz + 0.005))],
          mat("cream", 0.5, color="#F1F1F1"), bevel=0.001, parent=root)
    ball("Desk_Mouse", 0.03, (tx + 0.2, -d / 2 + 0.1, kz + 0.002), mat("cream", 0.4, color="#F1F1F1"),
         scale=(1, 1.8, 0.4), parent=root)
    # 27-inch screen on a rectangular stand in the centre gap between the bays (screen hook).
    sw, sh = 0.598, 0.336
    scz = TOP + 0.4
    box("Desk_Screen_Foot", (0.24, 0.17, 0.01), (0, 0.13, TOP + 0.005), PLASTIC, bevel=0.003, parent=root)
    box("Desk_Screen_Neck", (0.07, 0.022, 0.3), (0, 0.11, TOP + 0.16), PLASTIC, bevel=0.004, rot=(R(-6), 0, 0),
        parent=root)
    box("Desk_Screen_Body", (sw + 0.014, 0.03, sh + 0.027), (0, 0.06, scz), PLASTIC, bevel=0.004, parent=root)
    box("Desk_Screen_Back", (0.3, 0.03, 0.2), (0, 0.085, scz), PLASTIC, bevel=0.01, parent=root)
    box("Desk_Screen_LED", (0.004, 0.002, 0.002), (sw / 2 - 0.02, 0.0445, scz - sh / 2 - 0.008),
        mat("cream", 0.3, emit=4.0), bevel=0, parent=root)
    pz = scz + 0.0065
    screen = hook_image("screen", 1, (sw, sh), (0, 0.0445, pz), parent=root, glow=True, default_key="dark")
    parts = []
    for k in range(5):                                   # fake DAW: coloured clips on five tracks + a playhead
        tz = pz + sh / 2 - 0.05 - k * 0.058
        parts.append(box("DAW_Track_Name", (0.07, 0.002, 0.042), (-sw / 2 + 0.045, 0.0425, tz),
                         mat("foam", 0.5, emit=1.0), bevel=0, parent=root))
        x = -sw / 2 + 0.1
        while x < sw / 2 - 0.06:
            cw = min(random.uniform(0.06, 0.16), sw / 2 - 0.02 - x)
            key = ("accent_1", "accent_2", "accent_3", "cream", "main")[k]
            parts.append(box("DAW_Clip", (cw, 0.002, 0.042), (x + cw / 2, 0.0425, tz), mat(key, 0.5, emit=1.2),
                             bevel=0, parent=root))
            x += cw + random.uniform(0.01, 0.06)
    parts.append(box("DAW_Playhead", (0.004, 0.002, sh - 0.02), (0.05, 0.041, pz), mat("cream", 0.4, emit=3),
                     bevel=0, parent=root))
    hook_default(screen, *parts)
    light("Light_Screen_Glow", "AREA", 6, kelvin(6500), root.matrix_world @ Vector((0, -0.3, scz)),
          aim=root.matrix_world @ Vector((0, -0.8, TOP)), size=0.5, parent=root)
    # Nearfield monitors on isolation pads on the bridge, toed in towards the chair.
    for sx in (-1, 1):
        sp = sub("Desk_Monitor", (sx * 0.6, by + 0.01, bz + 0.022), (0, 0, R(sx * 12)), root)
        for py in (-1, 1):
            box("Pad_Plate", (0.155, 0.19, 0.008), (0, 0, 0.004 + (py + 1) * 0.034), POWDER, bevel=0.002, parent=sp)
        for px in (-1, 1):
            for py in (-1, 1):
                cyl("Pad_Post", 0.009, 0.06, (px * 0.06, py * 0.075, 0.038), mat("foam", 0.8), segs=12, bevel=0.002,
                    parent=sp)
        z0 = 0.076
        box("HS_Cabinet", (0.17, 0.222, 0.285), (0, 0.0, z0 + 0.1425), CAB, bevel=0.004, parent=sp)
        fy2 = -0.111
        cone = mat("cream", 0.55, color="#F2F0EA")
        disc("HS_Woofer_Trim", 0.072, (0, fy2 - 0.002, z0 + 0.1), mat("dark", 0.25, color="#101012"), depth=0.004,
             parent=sp)
        disc("HS_Woofer_Surround", 0.064, (0, fy2 - 0.004, z0 + 0.1), RUBBER, depth=0.003, parent=sp)
        cyl("HS_Woofer_Cone", 0.058, 0.012, (0, fy2 - 0.001, z0 + 0.1), cone, r2=0.02, segs=36, bevel=0,
            rot=(R(-90), 0, 0), parent=sp)
        ball("HS_Dust_Cap", 0.021, (0, fy2 - 0.009, z0 + 0.1), cone, scale=(1, 0.45, 1), parent=sp)
        disc("HS_Waveguide", 0.034, (0, fy2 - 0.002, z0 + 0.226), mat("dark", 0.3, color="#0C0C0E"), depth=0.004,
             parent=sp)
        ball("HS_Tweeter", 0.013, (0, fy2 - 0.004, z0 + 0.226), mat("dark", 0.2, color="#2A2A2E"),
             scale=(1, 0.5, 1), parent=sp)
        disc("HS_LED", 0.003, (0.06, fy2 - 0.002, z0 + 0.022), mat("cream", 0.3, emit=5.0), depth=0.002, parent=sp)
    # On the desk: mini MIDI controller, red audio interface, a mug.
    mc = sub("Desk_MiniKeys", (-0.12, -0.13, TOP), (0, 0, R(4)), root)
    box("Mini_Body", (0.318, 0.181, 0.03), (0, 0, 0.015), PLASTIC, bevel=0.006, parent=mc)
    boxes("Mini_White", [((0.0158, 0.075, 0.012), (-0.1 + 0.0167 * k, -0.045, 0.034)) for k in range(15)],
          mat("cream", 0.4, color="#F4F2EE"), bevel=0.001, parent=mc)
    blacks = [k for k in range(14) if k % 7 not in (2, 6)]
    boxes("Mini_Black", [((0.009, 0.045, 0.012), (-0.1 + 0.0167 * (k + 0.5), -0.03, 0.04)) for k in blacks],
          mat("dark", 0.35, color="#111113"), bevel=0.001, parent=mc)
    cyl("Mini_Joystick", 0.012, 0.02, (-0.135, -0.045, 0.04), RUBBER, segs=16, parent=mc)
    for k in range(8):
        px, py = -0.115 + (k % 4) * 0.038, 0.045 + (k // 4) * 0.035 - 0.017
        box("Mini_Pad", (0.032, 0.03, 0.008), (px, py, 0.033), mat("accent_3" if k == 5 else "foam", 0.6,
            emit=1.6 if k == 5 else 0.0), bevel=0.003, parent=mc)
        cyl("Mini_Knob", 0.008, 0.014, (0.05 + (k % 4) * 0.03, py, 0.037), mat("dark", 0.3, color="#0E0E10"),
            segs=14, parent=mc)
    ai = sub("Desk_Interface", (0.33, -0.07, TOP), (0, 0, R(-10)), root)
    box("AI_Body", (0.18, 0.099, 0.0455), (0, 0, 0.0228), surface(mat("accent_3", 0.32, metal=0.6), "brushed"),
        bevel=0.004, parent=ai)
    for k, kx in enumerate((-0.07, -0.035)):
        disc("AI_XLR", 0.011, (kx, -0.0505, 0.023), mat("dark", 0.4), depth=0.003, parent=ai)
        disc("AI_XLR_Hole", 0.006, (kx, -0.052, 0.023), mat("dark", 0.8, color="#000000"), depth=0.002, parent=ai)
        disc("AI_Halo", 0.012, (0.002 + k * 0.032, -0.0505, 0.023), mat("plant", 0.3, emit=3.0, color="#4CD964"),
             depth=0.002, parent=ai)
        cyl("AI_Gain", 0.0095, 0.012, (0.002 + k * 0.032, -0.056, 0.023), PLASTIC, segs=16, rot=(R(90), 0, 0),
            parent=ai)
    cyl("AI_Monitor_Knob", 0.016, 0.014, (0.062, -0.056, 0.023), PLASTIC, segs=20, rot=(R(90), 0, 0), parent=ai)
    cup = surface(mat("cream", 0.25), "ceramic")
    cyl("Desk_Mug", 0.04, 0.095, (0.56, -0.2, TOP + 0.0475), cup, bevel=0.003, parent=root)
    cyl("Desk_Mug_Coffee", 0.036, 0.004, (0.56, -0.2, TOP + 0.088), mat("wood", 0.2, color="#3A2418"), bevel=0,
        parent=root)
    tube("Desk_Mug_Handle", bezier((0.6, -0.2, TOP + 0.075), (0.64, -0.2, TOP + 0.05), (0.6, -0.2, TOP + 0.022), 8),
         0.006, cup, parent=root)
    # Closed-back headphones hanging on a hook on the right side panel.
    hx, hy, hk = w / 2 + 0.03, -0.12, 0.66               # hook height; the band rests on it
    box("Hook_Bracket", (0.035, 0.02, 0.03), (w / 2 + 0.015, hy, hk), POWDER, bevel=0.003, parent=root)
    box("Hook_Lip", (0.008, 0.02, 0.025), (w / 2 + 0.033, hy, hk + 0.02), POWDER, bevel=0.002, parent=root)
    band = mat("dark", 0.5, color="#141416")
    hz = hk - 0.08 + 0.015
    arc = [(hx, hy + 0.09 * math.cos(a), hz + 0.09 * math.sin(a)) for a in (R(t) for t in range(0, 181, 12))]
    tube("HP_Band", [(hx, hy + 0.09, hz - 0.08)] + arc + [(hx, hy - 0.09, hz - 0.08)], 0.009, band, parent=root)
    for sy in (-1, 1):
        cup_c = (hx, hy + sy * 0.1, hz - 0.15)
        rod("HP_Yoke", (hx, hy + sy * 0.09, hz - 0.08), (hx, hy + sy * 0.1, hz - 0.1), 0.004, STEEL, parent=root)
        ball("HP_Cup", 0.05, cup_c, PLASTIC, scale=(0.85, 0.46, 1.0), parent=root)
        ball("HP_Pad", 0.047, (hx, hy + sy * 0.085, hz - 0.15), surface(mat("dark", 0.55, color="#1E1D21"), "leather"),
             scale=(0.85, 0.32, 1.0), parent=root)
    tube("HP_Cable", [(hx, hy - 0.1, hz - 0.2), (hx + 0.01, hy - 0.08, hz - 0.35), (hx + 0.005, hy - 0.04, hz - 0.5),
                      (hx, hy, hz - 0.4)], 0.0025, band, parent=root)
    # Teal LED strip on the back edge of the bridge, washing the slats behind the desk.
    box("Desk_LED", (w - 0.06, 0.01, 0.008), (0, d / 2 - 0.005, bz + 0.026), mat("accent_2", 0.3, emit=10.0),
        bevel=0, parent=root)
    light("Light_LED", "AREA", LED_STRENGTH * (0.4 if DAY else 1.0), lin(COLORS["accent_2"])[:3],
          root.matrix_world @ Vector((0, d / 2 - 0.12, bz + 0.05)),
          aim=root.matrix_world @ Vector((0, d / 2 + 0.2, bz + 0.6)), size=1.3, parent=root)


def build_chair():
    """Office chair with a tall back and built-in headrest, five-star base, twin casters and loop arms."""
    root, w, d, h = furniture_root("chair")
    seat_fabric = surface(mat("foam", 0.9), "fabric")
    for k in range(5):
        a = k * 2 * math.pi / 5 + R(90)
        ex, ey = math.cos(a) * 0.3, math.sin(a) * 0.3
        box("Chair_Spoke", (0.3, 0.045, 0.03), (ex / 2, ey / 2, 0.085), PLASTIC, bevel=0.008, rot=(0, R(-6), a),
            parent=root)
        box("Chair_Caster_Fork", (0.03, 0.022, 0.03), (ex, ey, 0.06), PLASTIC, bevel=0.006, rot=(0, 0, a), parent=root)
        for side in (-1, 1):
            ox, oy = math.cos(a + R(90)) * 0.014 * side, math.sin(a + R(90)) * 0.014 * side
            cyl("Chair_Wheel", 0.026, 0.012, (ex + ox, ey + oy, 0.027), RUBBER, segs=18, bevel=0.003,
                rot=(R(90), 0, a), parent=root)
    cyl("Chair_Hub", 0.045, 0.05, (0, 0, 0.1), PLASTIC, r2=0.035, bevel=0.006, parent=root)
    cyl("Chair_Gas_Shroud", 0.03, 0.16, (0, 0, 0.2), PLASTIC, bevel=0.003, parent=root)
    cyl("Chair_Gas_Piston", 0.016, 0.12, (0, 0, 0.33), CHROME, bevel=0, parent=root)
    box("Chair_Mechanism", (0.2, 0.22, 0.05), (0, 0.02, 0.39), PLASTIC, bevel=0.008, parent=root)
    rod("Chair_Lever", (0.09, -0.02, 0.385), (0.2, -0.06, 0.37), 0.006, PLASTIC, parent=root)
    box("Chair_Seat_Shell", (0.5, 0.46, 0.025), (0, -0.01, 0.405), PLASTIC, bevel=0.008, parent=root)
    box("Chair_Seat_Cushion", (0.53, 0.47, 0.065), (0, -0.015, 0.44), seat_fabric, bevel=0.022, parent=root)
    # Back: ONE tall upholstered piece that wraps around you and narrows into the built-in headrest (the
    # MARKUS outline), on a black plastic shell joined to the mechanism by a spine.
    back = sub("Chair_Back_Pivot", (0, 0.2, 0.48), (R(-9), 0, 0), root)
    box("Chair_Spine", (0.07, 0.03, 0.42), (0, 0.075, 0.12), PLASTIC, bevel=0.01, parent=back)
    WRAP = 0.75                                          # y = -WRAP * x^2: the sides come forward

    def back_panel(name, hw, zb, shoulder, head, y0, thick, material, bevel):
        def top(x):                                      # top edge: headrest in the middle, shoulders outside
            t = min(1.0, max(0.0, (abs(x) - 0.11) / 0.06))
            return head + (shoulder - head) * t * t * (3 - 2 * t)
        nx, nz = 18, 10
        bm_ = bmesh.new()
        grid = [[[bm_.verts.new((x, y0 + dy - WRAP * x * x, zb + (top(x) - zb) * k / nz)) for k in range(nz + 1)]
                 for x in (-hw + 2 * hw * i / nx for i in range(nx + 1))] for dy in (0.0, thick)]
        f, b_ = grid
        for i in range(nx):
            for k in range(nz):
                bm_.faces.new((f[i][k], f[i + 1][k], f[i + 1][k + 1], f[i][k + 1]))
                bm_.faces.new((b_[i][k + 1], b_[i + 1][k + 1], b_[i + 1][k], b_[i][k]))
        for i in range(nx):                              # bottom and top edges
            bm_.faces.new((f[i + 1][0], f[i][0], b_[i][0], b_[i + 1][0]))
            bm_.faces.new((f[i][nz], f[i + 1][nz], b_[i + 1][nz], b_[i][nz]))
        for k in range(nz):                              # left and right edges
            bm_.faces.new((f[0][k + 1], f[0][k], b_[0][k], b_[0][k + 1]))
            bm_.faces.new((f[nx][k], f[nx][k + 1], b_[nx][k + 1], b_[nx][k]))
        bmesh.ops.recalc_face_normals(bm_, faces=bm_.faces)
        o = _obj(name, bm_)
        _finish(o, material, bevel, None, back)
        o.modifiers["Bevel"].angle_limit = R(40)
        return o
    back_panel("Chair_Back", 0.25, 0.1, 0.6, 0.81, 0.0, 0.06, seat_fabric, 0.02)
    back_panel("Chair_Back_Shell", 0.235, 0.12, 0.585, 0.795, 0.055, 0.02, PLASTIC, 0.008)
    tube("Chair_Lumbar_Seam", [(x, -0.003 - WRAP * x * x, 0.3) for x in (-0.24 + 0.04 * k for k in range(13))],
         0.003, mat("dark", 0.8), parent=back)
    tube("Chair_Head_Seam", [(x, -0.003 - WRAP * x * x, 0.62) for x in (-0.11 + 0.0275 * k for k in range(9))],
         0.003, mat("dark", 0.8), parent=back)
    for sx in (-1, 1):                                               # loop armrests
        tube("Chair_Arm", [(sx * 0.24, 0.12, 0.42), (sx * 0.27, 0.12, 0.55), (sx * 0.27, 0.06, 0.63),
                           (sx * 0.27, -0.12, 0.64), (sx * 0.26, -0.16, 0.6), (sx * 0.24, -0.1, 0.42)], 0.013,
             PLASTIC, parent=root)
        box("Chair_Arm_Pad", (0.06, 0.22, 0.025), (sx * 0.27, -0.03, 0.65), RUBBER, bevel=0.01, parent=root)


def build_instrument():
    """88-key digital piano on a double-braced X stand, with a music rest, sheet music and a sustain pedal."""
    root, w, d, h = furniture_root("instrument")
    ST = 0.71                                            # top of the stand arms
    for py in (-0.075, 0.075):                           # two parallel X frames (double braced)
        for sx in (-1, 1):
            rod("XStand_Tube", (sx * 0.36, py, 0.03), (-sx * 0.36, py, ST - 0.02), 0.014, POWDER, parent=root)
        cyl("XStand_Pivot", 0.02, 0.03, (0, py, (ST + 0.01) / 2), POWDER, segs=16, rot=(R(90), 0, 0), parent=root)
    rod("XStand_Bolt", (0, -0.1, (ST + 0.01) / 2), (0, 0.1, (ST + 0.01) / 2), 0.006, STEEL, parent=root)
    cyl("XStand_Knob", 0.032, 0.025, (0, -0.115, (ST + 0.01) / 2), PLASTIC, segs=6, bevel=0.006,
        rot=(R(90), 0, 0), parent=root)
    for sx in (-1, 1):
        box("XStand_Foot", (0.03, 0.42, 0.025), (sx * 0.36, 0, 0.0125), POWDER, bevel=0.004, parent=root)
        box("XStand_Arm", (0.03, 0.36, 0.025), (sx * 0.36, 0, ST - 0.0125), POWDER, bevel=0.004, parent=root)
        for sy in (-1, 1):
            cyl("XStand_Cap", 0.017, 0.03, (sx * 0.36, sy * 0.215, 0.015), RUBBER, segs=12, bevel=0.005,
                rot=(R(90), 0, 0), parent=root)
            box("XStand_Pad", (0.04, 0.06, 0.01), (sx * 0.36, sy * 0.1, ST + 0.005), RUBBER, bevel=0.003, parent=root)
    # The piano: 132.6 x 29.5 x 15.4 cm, keys from A0 to C8 (52 white, 36 black).
    kb = ST + 0.01
    body = surface(mat("dark", 0.5, color="#17161A"), "leather", scale=3.0)   # fine textured plastic
    box("Piano_Chassis", (1.326, 0.295, 0.07), (0, 0, kb + 0.035), body, bevel=0.012, parent=root)
    box("Piano_Rear_Panel", (1.326, 0.13, 0.06), (0, 0.0825, kb + 0.1), body, bevel=0.01, parent=root)
    for sx in (-1, 1):
        box("Piano_Cheek", (0.05, 0.17, 0.075), (sx * 0.638, -0.06, kb + 0.08), body, bevel=0.01, parent=root)
    box("Piano_Key_Slip", (1.226, 0.012, 0.03), (0, -0.142, kb + 0.072), body, bevel=0.003, parent=root)
    box("Piano_Felt", (1.222, 0.006, 0.008), (0, 0.012, kb + 0.106), surface(mat("accent_3", 0.9), "fabric"),
        bevel=0, parent=root)
    pitch = 1.222 / 52
    names = "ABCDEFG"
    whites, blacks = [], []
    for i in range(52):
        x = -0.611 + pitch * (i + 0.5)
        whites.append(((pitch - 0.0012, 0.145, 0.022), (x, -0.0655, kb + 0.094)))
        if names[i % 7] in "ACDFG" and i < 51:
            blacks.append(((0.0115, 0.09, 0.012), (x + pitch / 2, -0.038, kb + 0.11)))
    boxes("Piano_White_Keys", whites, mat("cream", 0.3, color="#F5F2EA"), bevel=0.0012, parent=root)
    boxes("Piano_Black_Keys", blacks, mat("dark", 0.25, color="#0C0C0E"), bevel=0.0015, parent=root)
    cyl("Piano_Power", 0.007, 0.005, (-0.6, 0.06, kb + 0.132), mat("metal", 0.4), segs=16, bevel=0, parent=root)
    for k in range(2):
        box("Piano_Button", (0.022, 0.012, 0.004), (-0.55 + k * 0.035, 0.06, kb + 0.132), mat("metal", 0.4), bevel=0.002,
            parent=root)
    box("Piano_Volume", (0.05, 0.006, 0.004), (-0.47, 0.06, kb + 0.132), mat("dark", 0.6, color="#050505"), bevel=0,
        parent=root)
    box("Piano_Volume_Cap", (0.008, 0.012, 0.008), (-0.48, 0.06, kb + 0.135), mat("metal", 0.4), bevel=0.002,
        parent=root)
    box("Piano_LED", (0.004, 0.004, 0.002), (-0.58, 0.06, kb + 0.133), mat("plant", 0.3, emit=5, color="#7CFF7C"),
        bevel=0, parent=root)
    mr = sub("Piano_Music_Rest", (0, 0.11, kb + 0.13), (R(-16), 0, 0), root)
    box("Rest_Board", (0.56, 0.006, 0.2), (0, 0, 0.1), mat("dark", 0.4, color="#141416"), bevel=0.003, parent=mr)
    box("Rest_Lip", (0.56, 0.03, 0.008), (0, -0.012, 0.004), mat("dark", 0.4, color="#141416"), bevel=0.002,
        parent=mr)
    for k, ox in enumerate((-0.11, 0.11)):                          # an open book of sheet music
        box("Rest_Sheet", (0.21, 0.002, 0.28), (ox, -0.005, 0.15), PAPER, bevel=0, rot=(0, 0, R(4 if k else -4)),
            parent=mr)
        boxes("Rest_Staves", [((0.17, 0.0005, 0.002), (ox, -0.0065, 0.26 - j * 0.022)) for j in range(9)],
              mat("dark", 0.8, color="#4A4A4A"), parent=mr)
    # Square sustain pedal on the floor with its cable to the back of the piano.
    pd = sub("Piano_Pedal", (0.18, -0.36, 0), (0, 0, R(-8)), root)
    box("Pedal_Base", (0.075, 0.16, 0.02), (0, 0, 0.01), RUBBER, bevel=0.005, parent=pd)
    box("Pedal_Plate", (0.07, 0.15, 0.012), (0, 0.0, 0.032), ALU, bevel=0.003, rot=(R(-7), 0, 0), parent=pd)
    tube("Pedal_Cable", [(0.18, -0.28, 0.01), (0.3, -0.05, 0.005), (0.42, 0.12, 0.01), (0.45, 0.16, kb + 0.04)],
         0.003, RUBBER, parent=root)


def build_hero_prop():
    """Large-diaphragm condenser mic in a shock mount with a pop filter, on a tripod boom stand (email link)."""
    root, w, d, h = furniture_root("hero_prop")
    hook_link(root, "email")
    for k in range(3):                                   # folding tripod with a strut collar
        a = k * 2 * math.pi / 3 + R(30)
        foot = (math.cos(a) * 0.3, math.sin(a) * 0.3, 0.012)
        rod("Mic_Leg", (math.cos(a) * 0.02, math.sin(a) * 0.02, 0.42), foot, 0.009, POWDER, parent=root)
        mid = (math.cos(a) * 0.15, math.sin(a) * 0.15, 0.22)
        rod("Mic_Strut", (math.cos(a) * 0.018, math.sin(a) * 0.018, 0.27), mid, 0.005, POWDER, parent=root)
        ball("Mic_Foot", 0.014, foot, RUBBER, scale=(1, 1, 0.7), parent=root)
    cyl("Mic_Collar_Top", 0.022, 0.05, (0, 0, 0.42), PLASTIC, segs=16, parent=root)
    cyl("Mic_Collar_Strut", 0.02, 0.03, (0, 0, 0.27), PLASTIC, segs=16, parent=root)
    rod("Mic_Tube_Lower", (0, 0, 0.1), (0, 0, 0.98), 0.0125, POWDER, parent=root)
    cyl("Mic_Clutch", 0.02, 0.045, (0, 0, 0.98), PLASTIC, segs=16, parent=root)
    rod("Mic_Clutch_Knob", (0, 0, 0.98), (0.04, 0, 0.98), 0.006, PLASTIC, parent=root)
    rod("Mic_Tube_Upper", (0, 0, 0.98), (0, 0, 1.3), 0.0095, POWDER, parent=root)
    P = Vector((0, 0, 1.32))
    BOOM = -10                                           # boom angle in degrees: tipped down towards a seated voice
    u = Vector((0, -math.cos(R(BOOM)), math.sin(R(BOOM))))
    cyl("Mic_Boom_Joint", 0.024, 0.04, P, PLASTIC, segs=16, rot=(0, R(90), 0), parent=root)
    cyl("Mic_Boom_TKnob", 0.012, 0.03, P + Vector((0.035, 0, 0)), PLASTIC, segs=6, rot=(0, R(90), 0), parent=root)
    back_end, F = P - u * 0.28, P + u * 0.52
    rod("Mic_Boom", back_end, F, 0.0085, POWDER, parent=root)
    cyl("Mic_Counterweight", 0.026, 0.09, back_end + u * 0.04, PLASTIC, segs=20, bevel=0.004,
        rot=(R(90 - BOOM), 0, 0), parent=root)
    # Shock mount (two elastic rings) and the condenser: 189 mm x 52 mm, mesh head with two rings.
    S = F + Vector((0, -0.02, -0.07))
    rod("Mic_Swivel", F, S + Vector((0, 0.06, 0)), 0.006, PLASTIC, parent=root)
    for dz in (-0.035, 0.035):
        tube("Shock_Ring", circle(S + Vector((0, 0, dz)), 0.045, "XY", 28), 0.0045, PLASTIC, closed=True, segs=8,
             parent=root)
        for k in range(4):                               # elastic cords from ring to mic body
            a = k * math.pi / 2 + R(45)
            rod("Shock_Cord", S + Vector((math.cos(a) * 0.045, math.sin(a) * 0.045, dz)),
                S + Vector((math.cos(a) * 0.027, math.sin(a) * 0.027, dz * 0.6)), 0.0015, mat("dark", 0.8), parent=root)
    rod("Shock_Arm", S + Vector((0, 0.045, -0.035)), S + Vector((0, 0.06, 0.035)), 0.005, PLASTIC, parent=root)
    body_m = surface(mat("metal", 0.32, metal=0.85, color="#C9C7C1"), "brushed", along="Z")   # the silver finish
    grille_m = surface(mat("metal", 0.5, metal=0.8, color="#B4B4B8"), "fabric", scale=0.4)
    cyl("NT_Body", 0.026, 0.115, S + Vector((0, 0, -0.035)), body_m, segs=32, bevel=0.002, parent=root)
    cyl("NT_Grille", 0.0262, 0.05, S + Vector((0, 0, 0.0475)), grille_m, segs=32, bevel=0, parent=root)
    ball("NT_Grille_Top", 0.0262, S + Vector((0, 0, 0.072)), grille_m, scale=(1, 1, 0.75), parent=root)
    for dz in (0.023, 0.072):
        cyl("NT_Ring", 0.0272, 0.004, S + Vector((0, 0, dz)), STEEL, segs=32, bevel=0, parent=root)
    disc("NT_Front_Dot", 0.004, S + Vector((0, -0.027, 0.0)), mat("accent_1", 0.4), depth=0.002, parent=root)
    cyl("NT_XLR", 0.011, 0.03, S + Vector((0, 0, -0.105)), STEEL, segs=16, bevel=0.002, parent=root)
    # 6-inch double-layer pop filter on a gooseneck clamped to the boom.
    pc = S + Vector((0, -0.12, 0.02))
    tube("Pop_Ring", circle(pc, 0.076, "XZ", 36), 0.005, PLASTIC, closed=True, segs=8, parent=root)
    no_shadow(cyl("Pop_Mesh", 0.074, 0.004, pc, see_through("dark", 0.55, 0.8), segs=36, bevel=0,
                  rot=(R(90), 0, 0), parent=root))
    g0, g1 = F - u * 0.22, pc + Vector((0, 0, -0.076))
    cyl("Pop_Clamp", 0.014, 0.03, g0, PLASTIC, segs=12, rot=(R(90 - BOOM), 0, 0), parent=root)
    tube("Pop_Gooseneck", bezier(g0, (g0 + g1) / 2 + Vector((0.05, 0.02, -0.07)), g1, 14), 0.004, PLASTIC, parent=root)
    # XLR cable: from the mic down the boom and the stand to the floor, then towards the desk.
    under = Vector((0.0, 0, -0.012))                     # runs along the underside of the boom
    tube("Mic_Cable", bezier(S + Vector((0, 0, -0.12)), S + Vector((0, 0.03, -0.24)), F - u * 0.16 + under, 10)
         + [P - u * 0.04 + under, P + Vector((0.014, 0, -0.04)), Vector((0.014, 0, 1.0)), Vector((0.015, 0, 0.5)),
            Vector((0.03, 0.02, 0.1)), Vector((0.12, 0.1, 0.006)), Vector((0.24, 0.3, 0.006))], 0.003, RUBBER,
         parent=root)


def build_sofa():
    """Two-seat leather sofa: thin track arms, two seat and two back cushions with piping, wooden legs."""
    root, w, d, h = furniture_root("sofa")
    pipe = surface(mat("main", 0.5, color=shade(COLORS["main"], 0.8)), "leather")
    for sx in (-1, 1):
        for sy in (-1, 1):
            cyl("Sofa_Leg", 0.022, 0.12, (sx * (w / 2 - 0.07), sy * (d / 2 - 0.07), 0.06), WALNUT, r2=0.017,
                bevel=0.002, parent=root)
    box("Sofa_Base", (w, d, 0.2), (0, 0, 0.22), LEATHER, bevel=0.02, parent=root)
    box("Sofa_Back_Frame", (w - 0.24, 0.16, 0.46), (0, d / 2 - 0.08, 0.32 + 0.23), LEATHER, bevel=0.03, parent=root)
    for sx in (-1, 1):
        box("Sofa_Arm", (0.12, d, 0.52), (sx * (w / 2 - 0.06), 0, 0.12 + 0.26), LEATHER, bevel=0.025, parent=root)
        tube("Sofa_Arm_Piping", [(sx * (w / 2 - 0.12 + 0.002), -d / 2 + 0.002, 0.64 - 0.006),
                                 (sx * (w / 2 - 0.12 + 0.002), d / 2 - 0.01, 0.64 - 0.006)], 0.004, pipe, parent=root)
        cx = sx * 0.351
        box("Sofa_Seat_Cushion", (0.698, 0.61, 0.12), (cx, -d / 2 + 0.305 + 0.0, 0.38), LEATHER, bevel=0.025,
            parent=root)
        rect = [(cx - 0.34, -d / 2 + 0.008, 0.437), (cx + 0.34, -d / 2 + 0.008, 0.437), (cx + 0.34, 0.1, 0.437),
                (cx - 0.34, 0.1, 0.437)]
        tube("Sofa_Seat_Piping", rect, 0.0045, pipe, closed=True, segs=6, parent=root)
        box("Sofa_Back_Cushion", (0.698, 0.17, 0.36), (cx, d / 2 - 0.235, 0.62), LEATHER, bevel=0.035,
            rot=(R(-10), 0, 0), parent=root)
    pil = surface(mat("accent_1", 0.95), "knit")
    box("Sofa_Pillow", (0.42, 0.13, 0.42), (w / 2 - 0.36, d / 2 - 0.36, 0.64), pil, bevel=0.06,
        rot=(R(-14), 0, R(-10)), parent=root)
    throw = surface(mat("cream", 0.95), "knit")             # knitted throw folded over the front arm
    ax_ = -w / 2 + 0.06
    box("Sofa_Throw_Top", (0.15, 0.42, 0.025), (ax_, -0.08, 0.652), throw, bevel=0.01, parent=root)
    box("Sofa_Throw_Out", (0.025, 0.42, 0.36), (ax_ - 0.072, -0.08, 0.48), throw, bevel=0.01, rot=(0, R(-3), 0),
        parent=root)
    box("Sofa_Throw_In", (0.025, 0.42, 0.2), (ax_ + 0.072, -0.08, 0.56), throw, bevel=0.01, rot=(0, R(4), 0),
        parent=root)
    boxes("Sofa_Throw_Fringe", [((0.004, 0.006, 0.035), (ax_ - 0.08, -0.28 + 0.02 * k, 0.285)) for k in range(21)],
          throw, parent=root)


def build_shelf():
    """KALLAX 2x2 (77 x 39 x 77 cm) full of LPs, a fabric box, and a direct-drive turntable on top. Link: github."""
    root, w, d, h = furniture_root("shelf")
    hook_link(root, "github")
    S, F, I = 0.77, 0.04, 0.016                          # outer size, frame and divider thickness
    for sx in (-1, 1):
        box("Kallax_Side", (F, d, S), (sx * (S / 2 - F / 2), 0, S / 2), KALLAX_M, bevel=0.002, parent=root)
    for z in (F / 2, S - F / 2):
        box("Kallax_TopBottom", (S - 2 * F, d, F), (0, 0, z), KALLAX_M, bevel=0.002, parent=root)
    box("Kallax_Divider_V", (I, d - 0.002, S - 2 * F), (0, 0, S / 2), KALLAX_M, bevel=0.001, parent=root)
    box("Kallax_Divider_H", (S - 2 * F, d - 0.002, I), (0, 0, S / 2), KALLAX_M, bevel=0.001, parent=root)
    cube = (S - 2 * F - I) / 2                           # 33.7 cm openings
    keys = ["dark", "cream", "accent_1", "accent_2", "accent_3", "main", "wall_trim", "plant", "navy", "foam"]
    groups = {k: [] for k in keys}
    for cxi, czi, mode in ((-1, 0, "full"), (1, 1, "lean"), (-1, 1, "full")):
        x0 = cxi * (I / 2 + cube / 2) - cube / 2 + 0.004
        zb = F if czi == 0 else S / 2 + I / 2
        end = x0 + cube - (0.01 if mode == "full" else 0.15)
        x = x0
        while x < end:
            t = random.uniform(0.0035, 0.006)
            groups[random.choice(keys)].append(((t, 0.314, 0.314), (x + t / 2, -d / 2 + 0.03 + 0.157, zb + 0.157)))
            x += t + (0.0004 if random.random() > 0.08 else 0.003)
        if mode == "lean":                               # the last few records lean over against the rest
            for j in range(4):                           # a 33.7 cm cube only lets a 31.4 cm LP lean ~5 degrees
                ang = R(3 + j * 0.6)
                groups[random.choice(keys)].append(((0.005, 0.314, 0.314), (x + 0.004 + j * 0.007 + 0.157 * math.sin(ang),
                                                    -d / 2 + 0.03 + 0.157, zb + 0.157 * (math.cos(ang) + math.sin(ang))
                                                    + 0.001), (0, -ang, 0)))
    for k, items in groups.items():
        if items:
            boxes(f"Kallax_LPs_{k}", items, surface(mat(k, 0.62), "paper"), bevel=0.0006, parent=root)
    # Fabric storage box (DRÖNA type) with a pull tab, in the bottom-right cube.
    fx = I / 2 + cube / 2
    box("Kallax_Box", (0.33, 0.37, 0.32), (fx, 0.0, F + 0.162), surface(mat("navy", 0.95), "fabric"), bevel=0.01,
        parent=root)
    box("Kallax_Box_Tab", (0.06, 0.008, 0.025), (fx, -d / 2 + 0.003, F + 0.27), mat("dark", 0.6), bevel=0.003,
        parent=root)
    # Direct-drive turntable: 45.3 x 35.3 cm plinth, platter with strobe dots, S-arm, pitch fader, big feet.
    tt = sub("Turntable", (-0.07, 0.0, S), (0, 0, R(3)), root)
    plinth = surface(mat("dark", 0.38, metal=0.5, color="#242327"), "brushed")
    for sx in (-1, 1):
        for sy in (-1, 1):
            cyl("TT_Foot", 0.035, 0.03, (sx * 0.185, sy * 0.135, 0.015), RUBBER, segs=24, bevel=0.004, parent=tt)
    box("TT_Plinth", (0.453, 0.353, 0.075), (0, 0, 0.03 + 0.0375), plinth, bevel=0.008, parent=tt)
    pz = 0.105
    cx, cy = -0.055, 0.0
    cyl("TT_Platter", 0.166, 0.022, (cx, cy, pz + 0.011), ALU, segs=64, bevel=0.002, parent=tt)
    prisms("TT_Strobe_Dots", [(0.0025, 0.0025, 0.004, (cx + math.cos(a) * 0.167, cy + math.sin(a) * 0.167, pz + 0.016))
                              for a in (2 * math.pi * k / 90 for k in range(90))], mat("cream", 0.3), segs=4,
            parent=tt)
    cyl("TT_Mat", 0.15, 0.003, (cx, cy, pz + 0.0235), RUBBER, segs=48, bevel=0, parent=tt)
    cyl("TT_Record", 0.15, 0.002, (cx, cy, pz + 0.026), mat("dark", 0.18, color="#0B0B0D"), segs=64, bevel=0,
        parent=tt)
    cyl("TT_Label", 0.05, 0.0006, (cx, cy, pz + 0.0273), mat("accent_1", 0.5), segs=32, bevel=0, parent=tt)
    cyl("TT_Spindle", 0.0035, 0.02, (cx, cy, pz + 0.035), CHROME, segs=8, bevel=0, parent=tt)
    ax, ay = 0.165, 0.11                                 # tonearm base at the right rear
    cyl("TT_Arm_Base", 0.035, 0.012, (ax, ay, pz + 0.006), ALU, segs=32, parent=tt)
    cyl("TT_Arm_Pivot", 0.016, 0.03, (ax, ay, pz + 0.025), CHROME, segs=20, parent=tt)
    cyl("TT_Counterweight", 0.016, 0.03, (ax, ay + 0.055, pz + 0.035), CHROME, segs=20, rot=(R(90), 0, 0), parent=tt)
    rod("TT_Arm_Rear", (ax, ay, pz + 0.035), (ax, ay + 0.04, pz + 0.035), 0.004, CHROME, parent=tt)
    arm = bezier((ax, ay, pz + 0.035), (ax + 0.03, ay - 0.12, pz + 0.035), (ax - 0.01, ay - 0.235, pz + 0.035), 10)
    tube("TT_Arm_S", arm, 0.0035, CHROME, parent=tt)
    box("TT_Headshell", (0.018, 0.04, 0.008), (ax - 0.014, ay - 0.25, pz + 0.033), CHROME, bevel=0.002,
        rot=(0, 0, R(-20)), parent=tt)
    box("TT_Cartridge", (0.014, 0.018, 0.014), (ax - 0.016, ay - 0.255, pz + 0.024), mat("accent_3", 0.4),
        bevel=0.002, parent=tt)
    box("TT_Arm_Rest", (0.012, 0.012, 0.025), (ax + 0.026, ay - 0.13, pz + 0.012), PLASTIC, bevel=0.002, parent=tt)
    box("TT_Pitch_Slot", (0.01, 0.1, 0.002), (0.207, -0.1, pz + 0.001), mat("dark", 0.8, color="#050506"), bevel=0,
        parent=tt)
    box("TT_Pitch_Cap", (0.018, 0.016, 0.012), (0.207, -0.115, pz + 0.007), ALU, bevel=0.003, parent=tt)
    box("TT_StartStop", (0.03, 0.03, 0.006), (-0.19, -0.145, pz + 0.002), ALU, bevel=0.003, parent=tt)
    for k in range(2):
        box("TT_Speed_Btn", (0.018, 0.012, 0.004), (-0.15 + k * 0.024, -0.152, pz + 0.002), ALU, bevel=0.002,
            parent=tt)
    cyl("TT_Strobe_Lamp", 0.012, 0.025, (-0.205, 0.15, pz + 0.012), ALU, segs=16, parent=tt)
    cyl("TT_Strobe_Glow", 0.006, 0.003, (-0.205, 0.15, pz + 0.026), mat("onair", 0.3, emit=4.0), segs=12, bevel=0,
        parent=tt)
    # A small trailing plant (pothos in a glazed pot) at the right end of the top.
    pot = surface(mat("accent_2", 0.25, color=shade(COLORS["accent_2"], 0.65)), "ceramic")
    cyl("Kallax_Pot", 0.06, 0.1, (0.28, 0.02, S + 0.05), pot, r2=0.065, bevel=0.004, parent=root)
    cyl("Kallax_Pot_Rim", 0.067, 0.012, (0.28, 0.02, S + 0.1), pot, bevel=0.003, parent=root)
    cyl("Kallax_Soil", 0.06, 0.008, (0.28, 0.02, S + 0.102), mat("wood", 0.95, color="#3E2E22"), bevel=0, parent=root)
    leaf = mat("plant", 0.45)
    for k in range(12):
        a = k * 2.4
        t = k / 11
        lx, ly = 0.28 + math.cos(a) * (0.05 + 0.06 * t), 0.02 + math.sin(a) * 0.05 - 0.04 * t
        lz = S + 0.12 - (0.28 * t if k % 3 == 0 else 0.04 * t)
        if k % 3 == 0:                                   # trailing vines down the front
            lx, ly = 0.3 + 0.02 * (k % 2), -d / 2 + 0.01
        ball("Kallax_Leaf", 0.03, (lx, ly, lz), leaf, scale=(1.1, 0.75, 0.35), parent=root).rotation_euler = (R(30), 0, a)
    tube("Kallax_Vine", [(0.29, 0.0, S + 0.105), (0.3, -d / 2 + 0.015, S + 0.08), (0.31, -d / 2 + 0.005, S - 0.12),
                         (0.3, -d / 2 + 0.005, S - 0.24)], 0.002, leaf, parent=root)


def twill(m, period=0.015, low=0.8):
    """Diagonal twill stripes on top of a surface() material (lacquered tweed). The palette colour
    stays in the KIT_BASE node; this only multiplies a stripe pattern into it."""
    nt, b = m.node_tree, _principled(m)
    src = b.inputs["Base Color"].links[0].from_socket
    coords, wave = nt.nodes.new("ShaderNodeTexCoord"), nt.nodes.new("ShaderNodeTexWave")
    wave.wave_type, wave.bands_direction = "BANDS", "DIAGONAL"
    wave.inputs["Scale"].default_value = 2 * math.pi / (10 * period)
    nt.links.new(coords.outputs["Object"], wave.inputs["Vector"])
    r = nt.nodes.new("ShaderNodeValToRGB")
    r.color_ramp.elements[0].color, r.color_ramp.elements[1].color = (low, low, low, 1), (1.04, 1.04, 1.04, 1)
    nt.links.new(wave.outputs["Fac"], r.inputs["Fac"])
    mix = nt.nodes.new("ShaderNodeMix")
    mix.data_type, mix.blend_type = "RGBA", "MULTIPLY"
    mix.inputs["Factor"].default_value = 1.0
    nt.links.new(src, mix.inputs[6])
    nt.links.new(r.outputs["Color"], mix.inputs[7])
    nt.links.new(mix.outputs[2], b.inputs["Base Color"])
    return m


def build_speaker():
    """1x12 tube combo amp in lacquered tweed: brown striped grille, chrome top panel with chicken-head knobs."""
    root, w, d, h = furniture_root("speaker")
    tweed = twill(surface(mat("tweed", 0.38), "fabric", scale=0.35))     # lacquer = a bit of gloss
    AH = 0.406
    for sx in (-1, 1):
        for sy in (-1, 1):
            cyl("Amp_Foot", 0.014, 0.012, (sx * (w / 2 - 0.04), sy * (d / 2 - 0.04), 0.006), RUBBER, segs=12,
                bevel=0.002, parent=root)
    box("Amp_Cabinet", (0.457, 0.233, AH), (0, 0, 0.012 + AH / 2), tweed, bevel=0.012, parent=root)
    gz, gh = 0.012 + 0.17, 0.27
    grille = surface(mat("grille", 0.9), "fabric", scale=0.6)
    box("Amp_Grille", (0.39, 0.006, gh), (0, -0.233 / 2 - 0.001, gz), grille, bevel=0.002, parent=root)
    boxes("Amp_Grille_Stripes", [((0.388, 0.002, 0.004), (0, -0.233 / 2 - 0.0045, gz - gh / 2 + 0.02 + 0.03 * k))
                                 for k in range(9)], mat("tweed", 0.9, color=shade(COLORS["grille"], 1.6)), parent=root)
    box("Amp_Grille_Welt", (0.398, 0.004, 0.006), (0, -0.233 / 2 - 0.003, gz + gh / 2 + 0.002), mat("cream", 0.6),
        bevel=0.001, parent=root)
    # Top-mounted chrome control panel at the rear edge (the knobs point up).
    top = 0.012 + AH
    box("Amp_Panel_Recess", (0.41, 0.075, 0.008), (0, 0.06, top - 0.002), mat("dark", 0.7), bevel=0.002, parent=root)
    box("Amp_Panel", (0.4, 0.065, 0.003), (0, 0.06, top + 0.002), CHROME, bevel=0.001, parent=root)
    for k in range(7):
        kx = -0.16 + k * 0.045
        cyl("Amp_Knob", 0.011, 0.016, (kx, 0.06, top + 0.011), mat("dark", 0.3, color="#101012"), segs=6,
            bevel=0.003, parent=root)
        box("Amp_Knob_Pointer", (0.004, 0.018, 0.004), (kx, 0.054, top + 0.0195), mat("cream", 0.4), bevel=0.001,
            rot=(0, 0, R(-30 + 20 * k)), parent=root)
    ball("Amp_Jewel", 0.009, (0.18, 0.06, top + 0.007), mat("onair", 0.2, emit=6.0), parent=root)
    box("Amp_Switch", (0.008, 0.016, 0.008), (0.155, 0.06, top + 0.008), CHROME, bevel=0.002, parent=root)
    strap = surface(mat("dark", 0.6, color="#221A16"), "leather")
    tube("Amp_Handle", bezier((-0.09, -0.01, top + 0.004), (0, -0.01, top + 0.06), (0.09, -0.01, top + 0.004), 10),
         0.009, strap, parent=root).scale = (1, 2.0, 1)
    for sx in (-1, 1):
        box("Amp_Handle_Cap", (0.03, 0.03, 0.008), (sx * 0.09, -0.01, top + 0.004), CHROME, bevel=0.003, parent=root)
    jack = Vector((0.2, 0.075, top + 0.004))              # guitar lead from the input jack, over the back edge
    tube("Amp_Cable", bezier(jack, (0.21, 0.16, top + 0.04), (0.22, 0.2, top - 0.1), 8)
         + bezier((0.22, 0.2, top - 0.12), (0.23, 0.24, 0.0), (0.05, 0.45, 0.006), 8)[1:]
         + [Vector((-0.4, 0.78, 0.006))], 0.003, RUBBER, parent=root)
    cyl("Amp_Jack_Plug", 0.006, 0.03, jack + Vector((0, 0, 0.012)), CHROME, segs=10, bevel=0, parent=root)


def build_floor_lamp():
    """Industrial floor lamp: heavy round base, thin stem and a big dark-grey cone shade on a tilting joint."""
    root, w, d, h = furniture_root("floor_lamp")
    lamp_m = surface(mat("foam", 0.45, metal=0.3, color="#3B3B40"), "brushed")
    cyl("Lamp_Base", 0.17, 0.025, (0, 0, 0.0125), lamp_m, segs=40, bevel=0.006, parent=root)
    cyl("Lamp_Base_Boss", 0.03, 0.03, (0, 0, 0.035), lamp_m, segs=20, bevel=0.004, parent=root)
    rod("Lamp_Stem", (0, 0, 0.04), (0, 0, 1.56), 0.0095, lamp_m, parent=root)
    cyl("Lamp_Switch", 0.012, 0.03, (0, 0, 1.1), PLASTIC, segs=12, parent=root)
    J = Vector((0, 0, 1.58))
    ball("Lamp_Joint", 0.018, J, lamp_m, parent=root)
    axis = Vector((0, -math.sin(R(55)), -math.cos(R(55))))      # shade axis points forward and down
    sc = J + Vector((0, -0.02, 0.06)) + axis * 0.08
    rot = axis.to_track_quat("-Z", "Y").to_euler()
    shade_o = cyl("Lamp_Shade", 0.06, 0.25, sc, lamp_m, r2=0.1575, segs=48, bevel=0, rot=rot, parent=root, caps=False)
    shade_o.rotation_euler = axis.to_track_quat("Z", "Y").to_euler()      # wide end points along the axis
    solid = shade_o.modifiers.new("Thickness", "SOLIDIFY")
    solid.thickness = 0.003
    rod("Lamp_Shade_Arm", J, sc - axis * 0.12, 0.007, lamp_m, parent=root)
    bulb = ball("Lamp_Bulb", 0.04, sc + axis * 0.04, mat("cream", 0.2, emit=6.0, color="#FFE7C2"), parent=root)
    no_shadow(bulb)
    bpy.context.view_layer.update()
    lamp_power = LAMP_STRENGTH * (0.35 if DAY else 1.0)
    tip = root.matrix_world @ (sc + axis * 0.1)
    spot = light("Light_FloorLamp", "SPOT", lamp_power * 8, kelvin(LAMP_WARMTH), tip,
                 aim=root.matrix_world @ (sc + axis * 2.0), size=0.08, parent=root)
    spot.data.spot_size, spot.data.spot_blend = R(85), 0.6
    light("Light_FloorLamp_Glow", "POINT", lamp_power * 0.6, kelvin(LAMP_WARMTH), root.matrix_world @ (J + Vector((0, 0, 0.1))),
          size=0.1, parent=root)


def build_rug():
    """Vintage Persian-style rug (200 x 140 cm): navy border, guard stripes, rust field, medallion, fringes."""
    root, w, d, h = furniture_root("rug")
    navy = surface(mat("navy", 1.0), "fabric")
    rust = surface(mat("accent_3", 1.0), "fabric")
    ivory = surface(mat("cream", 1.0, color=shade(COLORS["cream"], 0.92)), "fabric")
    gold = surface(mat("accent_1", 1.0, color=shade(COLORS["accent_1"], 0.8)), "fabric")
    box("Rug_Base", (w, d, 0.008), (0, 0, 0.004), navy, bevel=0.002, parent=root)

    def frame(name, inset, band, z, material):
        ow, od = w - 2 * inset, d - 2 * inset
        boxes(name, [((ow, band, 0.002), (0, od / 2 - band / 2, z)), ((ow, band, 0.002), (0, -od / 2 + band / 2, z)),
                     ((band, od, 0.002), (ow / 2 - band / 2, 0, z)), ((band, od, 0.002), (-ow / 2 + band / 2, 0, z))],
              material, parent=root)
    frame("Rug_Guard_Outer", 0.04, 0.02, 0.009, ivory)
    frame("Rug_Guard_Inner", 0.2, 0.015, 0.009, gold)
    motifs = []                                          # repeating diamonds along the main border
    for k in range(int((w - 0.3) / 0.09) + 1):
        x = -w / 2 + 0.15 + k * 0.09
        motifs += [(0.03, 0.03, 0.002, (x, d / 2 - 0.13, 0.009)), (0.03, 0.03, 0.002, (x, -d / 2 + 0.13, 0.009))]
    for k in range(int((d - 0.3) / 0.09) + 1):
        y = -d / 2 + 0.15 + k * 0.09
        motifs += [(0.03, 0.03, 0.002, (w / 2 - 0.13, y, 0.009)), (0.03, 0.03, 0.002, (-w / 2 + 0.13, y, 0.009))]
    prisms("Rug_Border_Motifs", motifs, rust, segs=4, parent=root)
    box("Rug_Field", (w - 0.43, d - 0.43, 0.002), (0, 0, 0.009), rust, bevel=0, parent=root)
    def lozenge(name, rx, ry, cx, z, material, teeth=0, tooth=0.0):
        """Flat diamond (Persian medallion / pendant) along the rug's long axis; `teeth` adds a stepped,
        serrated edge like the knotted outline of a real medallion."""
        corners = [Vector((cx + rx, 0)), Vector((cx, ry)), Vector((cx - rx, 0)), Vector((cx, -ry))]
        pts = []
        for i in range(4):
            a, e = corners[i], corners[(i + 1) % 4] - corners[i]
            nrm_ = Vector((e.y, -e.x)).normalized()                     # points out of the diamond
            steps = max(1, teeth * 2)
            pts += [a + e * (k / steps) + (nrm_ * tooth if k % 2 else Vector((0, 0))) for k in range(steps)]
        bm_ = bmesh.new()
        ext = bmesh.ops.extrude_face_region(bm_, geom=[bm_.faces.new([bm_.verts.new((p.x, p.y, z)) for p in pts])])
        bmesh.ops.translate(bm_, vec=(0, 0, 0.0015), verts=[e for e in ext["geom"] if isinstance(e, bmesh.types.BMVert)])
        bmesh.ops.recalc_face_normals(bm_, faces=bm_.faces)
        return _finish(_obj(name, bm_), material, 0, None, root)
    # Central medallion: a serrated navy diamond with an ivory diamond, a rust core and a gold rosette inside,
    # and a pendant (small diamond on a stem) at each end of the long axis - the classic Persian layout.
    lozenge("Rug_Medallion", 0.4, 0.27, 0, 0.0098, navy, teeth=7, tooth=0.022)
    lozenge("Rug_Medallion_Inner", 0.29, 0.19, 0, 0.0106, ivory, teeth=5, tooth=0.016)
    lozenge("Rug_Medallion_Core", 0.17, 0.11, 0, 0.0114, rust)
    prisms("Rug_Medallion_Rosette", [(0.06, 0.06, 0.002, (0, 0, 0.0132))], gold, segs=8, parent=root)
    for sx in (-1, 1):
        box("Rug_Pendant_Stem", (0.1, 0.022, 0.0015), (sx * 0.47, 0, 0.0105), navy, bevel=0, parent=root)
        lozenge("Rug_Pendant", 0.055, 0.075, sx * 0.565, 0.0098, navy, teeth=2, tooth=0.012)
        lozenge("Rug_Pendant_Inner", 0.025, 0.035, sx * 0.565, 0.0106, gold)
    fx, fy = (w - 0.43) / 2, (d - 0.43) / 2
    bm = bmesh.new()                                     # corner spandrels: triangles inside the field corners
    for sx in (-1, 1):
        for sy in (-1, 1):
            vs = [bm.verts.new((sx * fx, sy * fy, 0.0098)), bm.verts.new((sx * (fx - 0.3), sy * fy, 0.0098)),
                  bm.verts.new((sx * fx, sy * (fy - 0.22), 0.0098))]
            ext = bmesh.ops.extrude_face_region(bm, geom=[bm.faces.new(vs)])
            bmesh.ops.translate(bm, vec=(0, 0, 0.0015), verts=[e for e in ext["geom"] if isinstance(e, bmesh.types.BMVert)])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    spand = _obj("Rug_Spandrels", bm)
    _finish(spand, navy, 0, None, root)
    # The field is covered in a small repeat of flower heads (a herati-style all-over pattern), as on real rugs.
    flowers = {0: [], 1: []}
    for i in range(-6, 7):
        for j in range(-4, 5):
            x, y = i * 0.115 + (0.0575 if j % 2 else 0), j * 0.1
            inside_medallion = abs(x) / 0.48 + abs(y) / 0.34 < 1 or (abs(x) < 0.66 and abs(y) < 0.1)
            in_spandrel = (fx - abs(x)) / 0.3 + (fy - abs(y)) / 0.22 < 1.15
            if abs(x) < fx - 0.04 and abs(y) < fy - 0.04 and not inside_medallion and not in_spandrel:
                flowers[(i + j) % 2].append((0.018, 0.018, 0.002, (x, y, 0.0102)))
    prisms("Rug_Field_Flowers", flowers[0], ivory, segs=6, parent=root)
    prisms("Rug_Field_Buds", flowers[1], gold, segs=4, parent=root)
    boxes("Rug_Fringe", [((0.035, 0.005, 0.003), (sx * (w / 2 + 0.0175), -d / 2 + 0.03 + k * (d - 0.06) / 39, 0.002))
                         for sx in (-1, 1) for k in range(40)], ivory, parent=root)


PLACEHOLDERS = {
    "instrument": build_instrument, "hero_prop": build_hero_prop, "desk": build_desk, "chair": build_chair,
    "sofa": build_sofa, "shelf": build_shelf, "speaker": build_speaker, "floor_lamp": build_floor_lamp,
    "rug": build_rug,
}
if SHOW_PLACEHOLDER_FURNITURE:
    for slot_name, build in PLACEHOLDERS.items():
        build()


# =====================================================================
#  DECOR  (not slots): guitar on its stand, cajon, plant, cables
# =====================================================================
def smooth_outline(ctrl, n=6):
    """Catmull-Rom smoothing of control points (half-width profile of the guitar)."""
    out = []
    for i in range(len(ctrl) - 1):
        p0, p1, p2, p3 = (Vector(ctrl[max(i - 1, 0)]), Vector(ctrl[i]), Vector(ctrl[i + 1]),
                          Vector(ctrl[min(i + 2, len(ctrl) - 1)]))
        for k in range(n):
            t = k / n
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t * t
                              + (-p0 + 3 * p1 - 3 * p2 + p3) * t ** 3))
    out.append(Vector(ctrl[-1]))
    return out


# Dreadnought outline: (half width, height from the bottom of the body). Square shoulders, 41 cm lower bout.
GUITAR_HALF = [(0.0, 0.0), (0.12, 0.008), (0.175, 0.04), (0.2, 0.1), (0.206, 0.16), (0.198, 0.23), (0.165, 0.29),
               (0.138, 0.32), (0.14, 0.36), (0.148, 0.41), (0.145, 0.45), (0.128, 0.485), (0.085, 0.502), (0.0, 0.505)]
half = smooth_outline(GUITAR_HALF)
GUITAR_OUTLINE = [(p.x, p.y) for p in half] + [(-p.x, p.y) for p in reversed(half[1:-1])]

gtr = bpy.data.objects.new("Guitar", None)
gtr.location, gtr.rotation_euler = (3.22, 2.05, FLOOR_Z), (0, 0, R(38))
COL_ROOM.objects.link(gtr)
stand_m = POWDER
for k in range(3):                                       # tripod stand with a padded cradle and a neck yoke
    a = k * 2 * math.pi / 3 + R(90)
    rod("GStand_Leg", (0, 0.1, 0.2), (math.cos(a) * 0.2, 0.1 + math.sin(a) * 0.2, 0.01), 0.007, stand_m, parent=gtr)
rod("GStand_Post", (0, 0.1, 0.2), (0, 0.16, 0.92), 0.009, stand_m, parent=gtr)
for sx in (-1, 1):
    rod("GStand_Cradle", (0, 0.1, 0.2), (sx * 0.12, -0.03, 0.12), 0.007, stand_m, parent=gtr)
    cyl("GStand_Cradle_Pad", 0.014, 0.06, (sx * 0.12, -0.02, 0.13), RUBBER, segs=12, rot=(R(90), 0, 0), parent=gtr)
tube("GStand_Yoke", [(-0.035, 0.12, 0.96), (-0.03, 0.15, 0.92), (0, 0.16, 0.905), (0.03, 0.15, 0.92),
                     (0.035, 0.12, 0.96)], 0.007, RUBBER, parent=gtr)
body = bpy.data.objects.new("Guitar_Body_Root", None)
body.location, body.rotation_euler = (0, 0, 0.1), (R(-15), 0, 0)
body.parent = gtr
COL_ROOM.objects.link(body)
spruce = surface(mat("guitar", 0.3), "wood", scale=1.4, along="Z")
slab("Guitar_Sides", GUITAR_OUTLINE, 0.098, (0, -0.045, 0), WALNUT, bevel=0.006, parent=body)
slab("Guitar_Binding", [(x * 1.012, z * 1.006 - 0.0015) for x, z in GUITAR_OUTLINE], 0.004, (0, -0.0505, 0),
     mat("cream", 0.4), parent=body)
slab("Guitar_Top", GUITAR_OUTLINE, 0.004, (0, -0.0535, 0), spruce, bevel=0.0015, parent=body)
FY = -0.0545                                             # just in front of the top
disc("Guitar_Soundhole", 0.05, (0, FY + 0.0005, 0.335), mat("dark", 0.9, color="#0A0807"), depth=0.002, parent=body)
for r_ in (0.058, 0.064):
    tube("Guitar_Rosette", circle((0, FY, 0.335), r_, "XZ", 40), 0.0018, mat("cream", 0.5), closed=True, segs=6,
         parent=body)
guard = [(0.04, 0.29), (0.09, 0.3), (0.12, 0.34), (0.115, 0.4), (0.085, 0.43), (0.055, 0.395), (0.06, 0.35)]
slab("Guitar_Pickguard", [(x, z) for x, z in smooth_outline(guard, 3)], 0.0015, (0, FY - 0.0005, 0),
     surface(mat("wood", 0.25, color="#4A2614"), "marble"), parent=body)
box("Guitar_Bridge", (0.15, 0.008, 0.032), (0, FY - 0.003, 0.2), mat("dark", 0.5, color="#2A1A12"), bevel=0.003,
    parent=body)
box("Guitar_Saddle", (0.075, 0.004, 0.003), (0, FY - 0.0075, 0.21), mat("cream", 0.3), bevel=0, parent=body)
for k in range(6):
    cyl("Guitar_Pin", 0.0028, 0.004, (-0.03 + k * 0.012, FY - 0.008, 0.195), mat("cream", 0.3), segs=8, bevel=0,
        rot=(R(90), 0, 0), parent=body)
# Neck: 14 frets clear of the body, rosewood fingerboard with frets and dot inlays, 3+3 headstock.
SCALE, NUT = 0.634, 0.505 + 0.352
box("Guitar_Heel", (0.06, 0.07, 0.05), (0, -0.02, 0.525), WALNUT, bevel=0.01, parent=body)
neck = slab("Guitar_Neck", [(-0.028, 0.5), (0.028, 0.5), (0.022, NUT), (-0.022, NUT)], 0.022, (0, -0.045, 0),
            WALNUT, bevel=0.004, parent=body)
board = slab("Guitar_Fretboard", [(-0.028, 0.505), (0.028, 0.505), (0.022, NUT), (-0.022, NUT)], 0.005,
             (0, -0.05, 0), mat("dark", 0.6, color="#2A1A12"), parent=body)
frets = []
for n in range(1, 15):
    zf = NUT - SCALE * (1 - 2 ** (-n / 12))
    hw = 0.022 + (NUT - zf) / (NUT - 0.505) * 0.006
    frets.append(((hw * 2, 0.002, 0.0015), (0, -0.0515, zf)))
boxes("Guitar_Frets", frets, CHROME, parent=body)
for n in (3, 5, 7, 9, 12):
    zf = NUT - SCALE * (1 - 2 ** (-(n - 0.5) / 12))
    for ox in ((-0.008, 0.008) if n == 12 else (0,)):
        disc("Guitar_Inlay", 0.0035, (ox, -0.0512, zf), mat("cream", 0.3), depth=0.001, parent=body)
box("Guitar_Nut", (0.046, 0.006, 0.005), (0, -0.0515, NUT), mat("cream", 0.3), bevel=0.001, parent=body)
head = sub("Guitar_Head", (0, -0.04, NUT), (R(13), 0, 0), body)
slab("Guitar_Headstock", [(-0.024, 0.0), (0.024, 0.0), (0.04, 0.1), (0.042, 0.175), (0.0, 0.185), (-0.042, 0.175),
                          (-0.04, 0.1)], 0.016, (0, -0.008, 0), mat("dark", 0.35, color="#1C120C"), bevel=0.003,
     parent=head)
for k in range(3):
    for sx in (-1, 1):
        zz = 0.045 + k * 0.045
        cyl("Guitar_Tuner_Post", 0.004, 0.012, (sx * 0.02, -0.014, zz), CHROME, segs=8, bevel=0, rot=(R(90), 0, 0),
            parent=head)
        rod("Guitar_Tuner_Shaft", (sx * 0.04, 0.0, zz), (sx * 0.06, 0.0, zz), 0.0025, CHROME, parent=head)
        box("Guitar_Tuner_Button", (0.018, 0.006, 0.014), (sx * 0.068, 0.0, zz), CHROME, bevel=0.002, parent=head)
string_m = mat("metal", 0.25, metal=1.0, color="#E3DCCF")
for k in range(6):
    xb, xn = -0.026 + k * 0.0104, -0.019 + k * 0.0076
    rod("Guitar_String", (xb, FY - 0.009, 0.205), (xn, -0.0545, NUT), 0.0006 + 0.00012 * (5 - k), string_m,
        parent=body, segs=5)
cyl("Guitar_Endpin", 0.005, 0.01, (0, 0.004, -0.004), mat("cream", 0.3), segs=8, parent=body)

# Box cajon (30 x 30 x 48 cm): birch body, darker front plate with screws in the corners, rubber feet.
cajon = box("Cajon", (0.3, 0.3, 0.48), (1.05, 1.28, FLOOR_Z + 0.008 + 0.24), surface(mat("guitar", 0.45), "wood",
            along="Z"), bevel=0.006, rot=(0, 0, R(28)))
box("Cajon_Tapa", (0.29, 0.004, 0.47), (0, -0.152, 0), surface(mat("wood", 0.4), "veneer", along="Z"), bevel=0.002,
    parent=cajon)
for sx in (-1, 1):
    for sz in (0.215, 0.12, 0.025):
        cyl("Cajon_Screw", 0.004, 0.003, (sx * 0.13, -0.155, sz), STEEL, segs=8, bevel=0, rot=(R(90), 0, 0),
            parent=cajon)
    for sy in (-1, 1):
        cyl("Cajon_Foot", 0.012, 0.008, (sx * 0.12, sy * 0.12, -0.244), RUBBER, segs=10, bevel=0, parent=cajon)

# Snake plant in a glazed pot (22 cm) in the front-left corner, beside the radiator.
PX, PY = 0.26, 0.24
pot_m = surface(mat("cream", 0.25), "ceramic")
cyl("Plant_Pot", 0.1, 0.24, (PX, PY, FLOOR_Z + 0.12), pot_m, r2=0.11, bevel=0.006)
cyl("Plant_Pot_Rim", 0.114, 0.02, (PX, PY, FLOOR_Z + 0.24), pot_m, bevel=0.004)
cyl("Plant_Soil", 0.104, 0.01, (PX, PY, FLOOR_Z + 0.242), mat("wood", 0.95, color="#3E2E22"), bevel=0)
leaf_m = mat("plant", 0.45)
band_m = mat("plant", 0.5, color=shade(COLORS["plant"], 1.35))
for k in range(11):
    a = k * 2.4
    hgt = 0.38 + 0.28 * ((k * 7) % 5) / 4
    wd = 0.028 + 0.01 * (k % 3)
    pts = [(-wd * 0.6, 0.0), (wd * 0.6, 0.0), (wd, hgt * 0.35), (wd * 0.8, hgt * 0.75), (0.0, hgt),
           (-wd * 0.8, hgt * 0.75), (-wd, hgt * 0.35)]
    lf = slab("Plant_Leaf", pts, 0.004, (PX + math.cos(a) * 0.04, PY + math.sin(a) * 0.04, FLOOR_Z + 0.24), leaf_m,
              rot=(R(6 + 5 * (k % 3)) * math.cos(a), R(6 + 5 * (k % 3)) * math.sin(a), a + R(90)))
    lf.data.materials.append(band_m)
    for j, f in enumerate(lf.data.polygons):             # light cross-bands on the front face only
        f.material_index = 1 if (f.normal.y < -0.5 and k % 2) else 0

# Cables on the floor: the keyboard power lead and an instrument cable from the guitar corner to the desk.
for i, pts in enumerate([[(2.75, 1.95, FLOOR_Z + 0.004), (3.0, 2.3, FLOOR_Z + 0.004), (3.1, 2.8, FLOOR_Z + 0.004),
                          (3.0, 3.3, FLOOR_Z + 0.004), (2.98, 3.5, FLOOR_Z + 0.004)],
                         [(3.35, 2.2, FLOOR_Z + 0.004), (3.6, 2.45, FLOOR_Z + 0.004), (3.95, 2.7, FLOOR_Z + 0.004),
                          (4.2, 3.2, FLOOR_Z + 0.004), (4.25, 3.48, FLOOR_Z + 0.004)]]):
    tube(f"Floor_Cable_{i}", pts, 0.0035, RUBBER, segs=6)


# =====================================================================
#  PORTFOLIO WALL  (neon name sign, ON AIR light, framed gig posters, LP sleeves on picture ledges)
# =====================================================================
# Neon sign on black acrylic above the KALLAX: your NAME and ROLE glow on it. Link: website.
SIGN_X, SIGN_Z, SW_, SH_ = 1.25, 1.86, 1.2, 0.46
SY = D - 0.034
sign = box("Neon_Backboard", (SW_, 0.008, SH_), (SIGN_X, SY, SIGN_Z), mat("dark", 0.32, color="#0E0D11"), bevel=0.004)
hook_link(sign, "website")
for sx in (-1, 1):
    for sz in (-1, 1):
        cyl("Neon_Standoff", 0.011, 0.03, (SIGN_X + sx * (SW_ / 2 - 0.04), D - 0.015, SIGN_Z + sz * (SH_ / 2 - 0.04)),
            CHROME, segs=16, bevel=0.002, rot=(R(90), 0, 0))
        cyl("Neon_Standoff_Cap", 0.012, 0.006, (SIGN_X + sx * (SW_ / 2 - 0.04), SY - 0.007, SIGN_Z + sz * (SH_ / 2 - 0.04)),
            CHROME, segs=16, bevel=0.002, rot=(R(90), 0, 0))
tube("Neon_Cable", [(SIGN_X + 0.45, SY + 0.004, SIGN_Z - SH_ / 2), (SIGN_X + 0.47, D - 0.01, SIGN_Z - SH_ / 2 - 0.2),
                    (SIGN_X + 0.48, D - 0.008, 0.95), (SIGN_X + 0.45, D - 0.01, 0.8)], 0.0025,
     mat("cream", 0.3, color="#DADADA"))
hook_text("name", 1, "YOUR NAME", 0.17, (SIGN_X, SY - 0.012, SIGN_Z + 0.05),
          material=mat("accent_1", 0.3, emit=5.0, color=shade(COLORS["accent_1"], 1.08)), max_width=1.06, depth=0.005)
hook_text("role", 1, "your role", 0.09, (SIGN_X, SY - 0.012, SIGN_Z - 0.14),
          material=mat("cream", 0.3, emit=2.5, color="#FFF1DC"), max_width=1.0, depth=0.004)

# ON AIR light box (34 x 11 x 7 cm) above the sign.
OA_Z = SIGN_Z + SH_ / 2 + 0.14
box("OnAir_Housing", (0.34, 0.07, 0.11), (SIGN_X, D - 0.035, OA_Z), PLASTIC, bevel=0.006)
box("OnAir_Face", (0.31, 0.004, 0.085), (SIGN_X, D - 0.071, OA_Z), mat("onair", 0.3, emit=4.0), bevel=0.002)
label("OnAir_Text", "ON AIR", 0.06, (SIGN_X, D - 0.074, OA_Z), mat("cream", 0.3, emit=6.0, color="#FFF4EE"))

# Gig posters in two thin deep frames (52 x 72 and 32 x 42 cm) between the shelf and the desk.
POSTERS = [((2.2, 1.5), (0.48, 0.68)), ((2.66, 1.44), (0.28, 0.38))]
frame_m = surface(mat("dark", 0.45), "veneer")
for i, ((x, z), (pw, ph)) in enumerate(POSTERS):
    fw = 0.02
    box(f"Poster_Back_{i}", (pw + 2 * fw, 0.035, ph + 2 * fw), (x, D - 0.0175, z), mat("dark", 0.7), bevel=0.002)
    for nm, size, loc in [("T", (pw + 2 * fw, 0.045, fw), (x, D - 0.0225, z + ph / 2 + fw / 2)),
                          ("B", (pw + 2 * fw, 0.045, fw), (x, D - 0.0225, z - ph / 2 - fw / 2)),
                          ("L", (fw, 0.045, ph), (x - pw / 2 - fw / 2, D - 0.0225, z)),
                          ("R", (fw, 0.045, ph), (x + pw / 2 + fw / 2, D - 0.0225, z))]:
        box(f"Poster_Frame_{i}{nm}", size, loc, frame_m, bevel=0.002)
    bg, fg = (("accent_3", "cream"), ("cream", "accent_3"))[i]
    py = D - 0.036
    p = hook_image("poster", i + 1, (pw, ph), (x, py, z), default_key=bg)
    hook_default(p,
                 disc(f"Poster_Sun_{i}", pw * 0.28, (x, py - 0.001, z + ph * 0.12), mat(fg, 0.6), depth=0.001),
                 box(f"Poster_Line_{i}", (pw * 0.7, 0.001, 0.03), (x, py - 0.001, z - ph * 0.25), mat(fg, 0.6), bevel=0),
                 box(f"Poster_Line2_{i}", (pw * 0.45, 0.001, 0.02), (x, py - 0.001, z - ph * 0.34), mat(fg, 0.6),
                     bevel=0))

# LP sleeves (31.4 cm) leaning on two 115 cm picture ledges above the sofa: frame hooks 1-6.
COVER, LEAN = 0.314, R(15.5)                                # leaning back until the top touches the wall
LEDGE_Y, LEDGE_ZS = 3.03, (1.24, 1.7)
ledge_m = mat("cream", 0.4)
for j, lz in enumerate(LEDGE_ZS):
    box(f"Ledge_Board_{j}", (0.12, 1.15, 0.02), (0.06, LEDGE_Y, lz - 0.01), ledge_m, bevel=0.003)
    box(f"Ledge_Lip_{j}", (0.012, 1.15, 0.03), (0.114, LEDGE_Y, lz + 0.005), ledge_m, bevel=0.003)
    box(f"Ledge_Fascia_{j}", (0.12, 1.15, 0.06), (0.06, LEDGE_Y, lz - 0.05), ledge_m, bevel=0.003, rot=(0, 0, 0))
VINYL = [(LEDGE_Y + dy, lz) for lz in LEDGE_ZS for dy in (-0.36, 0.0, 0.36)]
ART = [("accent_1", "dark"), ("accent_2", "cream"), ("accent_3", "cream"), ("cream", "dark"), ("dark", "accent_1"),
       ("main", "cream")]
up = Vector((-math.sin(LEAN), 0, math.cos(LEAN)))           # the sleeve's "up" leans back towards the wall
nrm = Vector((math.cos(LEAN), 0, math.sin(LEAN)))           # sleeve faces into the room and a little up
for i, (y, lz) in enumerate(VINYL):
    c = Vector((0.087, y, lz)) + up * (COVER / 2)
    rot = (-LEAN, 0, R(90))
    box(f"Sleeve_Card_{i}", (COVER, 0.003, COVER), c, PAPER, bevel=0.0008, rot=rot)
    if i in (3, 5):                                          # a record slid half out of the sleeve
        disc(f"Sleeve_Record_{i}", 0.148, c + up * 0.11 - nrm * 0.002, mat("dark", 0.2, color="#0B0B0D"),
             facing="+x", depth=0.002).rotation_euler = (0, R(90) - LEAN, 0)
    bg, fg = ART[i]
    f = hook_image("frame", i + 1, (COVER, COVER), c + nrm * 0.002, rot=rot, default_key=bg)
    fc = c + nrm * 0.003
    deco = []
    if i % 3 == 0:                                       # a big circle
        d_ = disc(f"Cover_Circle_{i}", COVER * 0.28, fc + up * 0.02, mat(fg, 0.6), facing="+x", depth=0.001)
        d_.rotation_euler = (0, R(90) - LEAN, 0)
        deco.append(d_)
    elif i % 3 == 1:                                     # equaliser bars
        for k in range(5):
            bh = COVER * (0.15 + 0.12 * ((k * 3 + i) % 4))
            deco.append(box(f"Cover_Bar_{i}", (COVER * 0.1, 0.001, bh),
                            fc + Vector((0, -COVER * 0.3 + k * COVER * 0.15, 0)) + up * (-COVER * 0.3 + bh / 2),
                            mat(fg, 0.6), bevel=0, rot=rot))
    else:                                                # stripes
        for k in range(3):
            deco.append(box(f"Cover_Stripe_{i}", (COVER * 0.8, 0.001, COVER * 0.07), fc + up * (COVER * (0.2 - k * 0.15)),
                            mat(fg, 0.6), bevel=0, rot=rot))
    hook_default(f, *deco)


# =====================================================================
#  LIGHTS, WORLD, CAMERA, RENDER
# =====================================================================
# evening: low sunset sun through the blinds (a warm rim light), a dim fill, the floor lamp,
#          a soft spotlight on the keyboard and the teal LED (built with the desk).
# daylight: a brighter, whiter sun and fill; lamps, spotlight and LED turned down.
sun_k, sun_power = (5200, 3.6) if DAY else (SUN_WARMTH, SUN_STRENGTH)
fill_mult, amb, amb_k = (1.0, 0.4, 6500) if DAY else (0.38, 0.42, 9000)
light("Light_Sun", "SUN", sun_power, kelvin(sun_k), (-3, wy, 3.2), aim=(1.5, wy + 0.7, 0), size=R(2))
light("Light_Fill", "AREA", 230 * (W * D / 16) * fill_mult, kelvin(6000 if DAY else 7000), (W + 3, -3, H + 2.5),
      aim=(W / 2, D / 2, 0.6), size=6)
spot = light("Light_Spot_Keys", "SPOT", SPOT_STRENGTH * (0.35 if DAY else 1.0), kelvin(LAMP_WARMTH + 300),
             (2.4, 1.9, 3.2), aim=(2.25, 1.8, 0.6), size=0.3)
spot.data.spot_size, spot.data.spot_blend = R(55), 0.75
light("Light_Bounce", "AREA", 35 if DAY else 22, kelvin(5200 if DAY else LAMP_WARMTH), (W / 2, D / 2, H - 0.1),
      aim=(W / 2, D / 2, 0), size=2.5)
light("Light_Sign_Glow", "POINT", 4 if DAY else 9, lin(COLORS["accent_1"])[:3], (SIGN_X, D - 0.12, SIGN_Z),
      size=0.5)                                                       # the neon's own glow on the wall

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
bg_amb.inputs["Color"].default_value = (*kelvin(amb_k), 1)
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
                    ("shadow_ray_count", 2), ("use_gtao", True), ("use_soft_shadows", True),
                    ("use_bloom", True)):
    if hasattr(ee, attr):
        setattr(ee, attr, value)
if hasattr(ee, "ray_tracing_options"):
    ee.ray_tracing_options.resolution_scale = "2" if "2" in [i.identifier for i in
        type(ee.ray_tracing_options).bl_rna.properties["resolution_scale"].enum_items] else ee.ray_tracing_options.resolution_scale
scene.view_settings.view_transform = "Standard"   # keeps your hex colours exactly as typed
scene.view_settings.exposure = -0.15 if DAY else 0.0

# Remember the style so add_furniture.py can match colours later.
scene["kit_style"] = STYLE
scene["kit_version"] = KIT_VERSION
scene["kit_palette"] = json.dumps(COLORS)
scene["kit_material_finish"] = json.dumps({"roughness": 0.55, "bevel": 0.006, "saturation": 0.7})
scene["kit_theme"] = THEME
scene["kit_bounds"] = [-T, 0.0, -0.2, W, D + T, H + 0.12]   # used to re-frame the camera for social sizes
scene["kit_furniture_colors"] = json.dumps(["main", "wood", "oak", "accent_1", "accent_3", "cream", "foam", "dark",
                                            "plant", "kallax", "navy"])   # colours add_furniture.py may use


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
