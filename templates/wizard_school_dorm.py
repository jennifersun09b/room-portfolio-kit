"""
3D ROOM PORTFOLIO KIT  -  Template: WIZARD SCHOOL TOWER DORM (themed room, kit v4)
================================================================================
Builds the top room of a round stone tower at an invented boarding academy, cut away like a doll's house:
coursed blue-grey ashlar walls with battlements and a chimney stack, a painted starry vault round the top of the
walls with candles floating beneath it, a tall lancet window with leaded diamond panes looking out over a moonlit
loch, snowy peaks and a pine forest, a round leaded oculus, two single four-poster beds with plum velvet curtains
tied back with gold tassels, a steamer trunk at the foot of each bed (one with your name plate and an open wand
box, one with a chess game and sealed scrolls), a Tudor-arch stone fireplace with a crackling fire and a glowing
cauldron on a trivet, a fireside wing chair, an oak writing table with a brass orrery, quill and wax-seal set, a
Windsor chair, a bookcase of old leather books, a barn owl in a brass domed cage on a stand by the window, a brass
telescope on the window board, a besom on wall hooks, plain black hooded robes on a bentwood coat stand, a striped
knitted scarf, gilt portraits and a spiral stair coming up through the oak floor. It renders a 1920x1080 image.
The room only evokes the general "magic school" feeling: every colour and prop is original (no crests or emblems).
Your name and role are on the cloth banner over the fireplace (and your name on the trunk's brass plate); your
projects are the three paintings on the chimney breast, the two gilt portraits (with title plaques) and the cork
timetable board above the bookcase. The letter rack on the desk is your email, the bookcase your GitHub, the
orrery your website and the trunk at the foot of the bed your LinkedIn (CV).

HOW TO RUN
  Option A (no Blender UI):   blender -b -P wizard_school_dorm.py
  Option B (inside Blender):  Scripting tab > Open > wizard_school_dorm.py > Run Script (then F12 to render)

You only need to edit the SETTINGS block below. Everything under it builds the room.
Output: output/wizard_school_dorm.png and output/wizard_school_dorm.blend next to this script.
"""
# REFERENCES  (what each piece is modelled on; brand and dealer names appear only here and in
#              research/wizard_school_dorm.md)
#   bed (+ decor bed)      single four-poster with an open tester (Vipack Pino / Birlea Farringdon single):
#                          L208 x W97 x H190 cm; modelled 210 x 104 x 222 cm, mattress 90 x 200, top at 55 cm
#                          https://www.cuckooland.com/brand/cuckooland/pino-four-poster-single-bed
#                          https://www.mybespokeroom.com/home-products/products/farringdon-single-metal-4-poster-bed
#   trunk (+ decor trunk)  Victorian / Edwardian flat-top steamer trunk: W86 x D48 x H56 cm, oak slats, brass
#                          corners, two leather straps, hasp, leather end handles
#                          https://www.chairish.com/product/36662661/antique-wood-travel-trunk-with-leather-straps-and-original-hardware
#                          https://www.ebth.com/items/7466299-antique-wood-and-brass-steamer-trunk
#   fireplace              Victorian Gothic / Tudor-arch stone fire surround: W130 cm, opening 86 x 82 cm,
#                          shelf at 1.45 m, on a 1.6 m chimney breast; cast-iron fireback, fire basket, andirons
#                          https://www.1stdibs.com/furniture/building-garden/fireplaces-mantels/antique-victorian-gothic-stone-fireplace-surround/id-f_2596922/
#   armchair               Queen Anne-style walnut wing armchair: W78 x D84 x H106 cm, seat 47 cm, cabriole legs
#                          https://vinterior.co/furniture/seating/armchairs/wonderful-queen-anne-design-walnut-wing-armchair-c-1880-sku97509561
#   desk                   Victorian oak two-drawer writing table on turned legs: W100 x D55 x H75 cm,
#                          22 mm top with a tooled leather inset
#                          https://lapada.org/art-and-antiques/victorian-oak-two-drawer-writing-table/
#   chair                  English hoop-back (stick-back) Windsor chair: W50 x D52 x H92 cm, seat 45 cm
#                          https://www.chairish.com/product/32493362/antique-windsor-stick-and-hoop-back-kitchen-chair
#   orrery (website link)  19th-century brass desk orrery: H26 x dia 30 cm, turned base, brass arms
#                          https://1stdibs.com/furniture/more-furniture-collectibles/collectibles-curiosities/scientific-instruments/19th-century-astronomical-brass-orrery/id-f_940334
#   writing set + letters  glass inkwell, feather quill, 25 mm brass wax seal, letter rack (email link)
#                          https://www.gathered.how/papercraft/best-wax-seal-kits
#   bookcase (github link) narrow open bookcase, stained walnut, IKEA BILLY 40 cm proportions + cornice:
#                          W62 x D32 x H175 cm, 18 mm shelves
#                          https://www.ikea.com/gb/en/cat/billy-bookcases-19243/
#   pet                    barn owl (Tyto alba) 34 cm tall in a Victorian brass domed bird cage (dia 44 cm, H 66 cm)
#                          hanging from a 1.9 m wrought-iron cage stand with tripod feet and a crook top
#                          https://dimensions.com/element/barn-owl-tyto-alba
#                          https://en.wikipedia.org/wiki/Birdcage
#   cauldron (hearth)      cast cauldron on a three-legged trivet: dia 42 cm, H 40 cm, lugs and a bail handle
#                          https://en.wikipedia.org/wiki/Cauldron
#   besom                  traditional birch besom with a hazel handle: L127 cm, head about 19 cm wide, on two
#                          forged-iron wall hooks  https://www.reading.ac.uk/adlib/Details/collect/15599
#   coat stand + robes     Thonet No. 11-type bentwood hat-and-coat stand: H190 cm, four bent feet, six hooks;
#                          plain black academic gowns with hoods and bell sleeves, about 125 cm long on the hook
#                          https://en.wikipedia.org/wiki/Thonet
#   scarf                  hand-knitted striped wool scarf: 15 x 160 cm, oatmeal with 5 cm teal and rust stripes
#   chess set (trunk 2)    folding wooden board 30 cm (34 mm squares), turned pieces 3-6 cm
#   scrolls, letters       rolled parchment 22-24 cm with ribbon ties and wax-seal tags; sealed envelopes
#   telescope (window)     Victorian brass table telescope on a tripod: tube L33 cm, dia 4-5 cm
#   wand box               lidded walnut pen box 36 x 8.5 x 4.5 cm with a satin lining, a carved wooden rod 31 cm
#   goblets (mantel)       plain pewter goblets: H15 cm, dia 7.5 cm
#   portraits              gilt frames 38 x 48 / 34 x 42 cm with brass title plaques; faceless painterly studies
#   painted vault          plaster frieze painted as a night sky (gilt stars, constellations, crescents) on the
#                          top 52 cm of the wall, gilt bead below; floating candles 11-20 cm under it
#   windows                medieval single-light lancet with a splayed reveal and leaded quarries: glass 50 cm
#                          wide, 82 cm inside, sill 1.0 m, springing 1.95 m (Aberdour Castle window head type)
#                          https://en.wikipedia.org/wiki/Lancet_window
#   rug                    round wool rug, dia 190 cm, bordered with a star medallion
#   spiral stair           medieval newel stair: well dia 1.0 m, rise 15 cm, oak handrail on turned balusters
#                          https://en.wikipedia.org/wiki/Spiral_stairs
#   walls / floor          coursed sandstone ashlar (30 cm wall, 22-32 cm courses, lime mortar); 180 mm oak boards
#                          https://en.wikipedia.org/wiki/Ashlar

# =====================================================================
#  SETTINGS  -  change these lines, then run the script again
# =====================================================================
ROOM_NAME = "wizard_school_dorm"    # used for the output file names

ROOM_WIDTH = 5.6                    # metres: inside diameter of the round tower room (left to right)
ROOM_DEPTH = 5.6                    # metres: keep equal to ROOM_WIDTH (the room is round)
WALL_HEIGHT = 3.2                   # metres, floor to the top of the wall (battlements sit on top)

THEME = "candlelit_night"           # pick one of the colour themes below
THEMES = {                          # any hex colour works; "main" is the room's hero colour (the bed velvet)
    # Lights change with the theme too (see LIGHTS below): "candlelit_night" = indigo moonlight in the windows,
    # warm candles and a big fire; "autumn_term" = golden afternoon sun, trees turning outside, the fire low.
    # "wall" = the coursed stone, "wall_trim" = the smoother dressed stone round windows, fireplace and coping.
    # "vault" / "vault_star" = the painted night-sky band round the top of the wall; "robe" = the plain black
    # school robes on the coat stand; "brew" = the faint glow in the cauldron by the hearth.
    "candlelit_night": {
        "background": "#1D2346", "wall": "#8C93A6", "wall_trim": "#B9BBC2", "floor": "#8A6444",
        "wood": "#6A442C", "main": "#6B3B66", "accent_1": "#2D7C7A", "accent_2": "#D9A84E",
        "accent_3": "#B5583A", "cream": "#F0E4CB", "plant": "#5F7C4E", "dark": "#211B22",
        "brass": "#C99E4E", "iron": "#2C2A2E", "leather": "#6A3B26", "copper": "#BC6C3E", "mortar": "#C9C6BC",
        "flame": "#FFB24A", "sky": "#2A3B7C", "sky_low": "#5A6FB0", "hills": "#141B38", "lake": "#3C5596",
        "moon": "#F4EED8", "owl": "#C8A066", "owl_face": "#F4EEE2", "cork": "#B98A57", "snow": "#EEF2FA",
        "glass": "#C9D6F0", "tree_1": "#1C2A3A", "tree_2": "#24324A",
        "vault": "#1A2152", "vault_star": "#F4D88E", "robe": "#1F1D24", "pewter": "#8D9098", "brew": "#7FE3B4",
    },
    "autumn_term": {
        "background": "#F2E3CB", "wall": "#A1A2A6", "wall_trim": "#CBC6BA", "floor": "#A27A52",
        "wood": "#78502F", "main": "#6E3E66", "accent_1": "#2F8783", "accent_2": "#DCAB4C",
        "accent_3": "#BF6136", "cream": "#F5ECD8", "plant": "#7C8A4C", "dark": "#2A2224",
        "brass": "#CFA552", "iron": "#332F30", "leather": "#74432A", "copper": "#C4743F", "mortar": "#D6D0C2",
        "flame": "#FFB24A", "sky": "#F1D3A0", "sky_low": "#F8E6C4", "hills": "#9A8C76", "lake": "#BCCBD2",
        "moon": "#FFF6E0", "owl": "#C8A066", "owl_face": "#F4EEE2", "cork": "#BE8F5A", "snow": "#F4F4F0",
        "glass": "#F3E7CC", "tree_1": "#B8532A", "tree_2": "#D9A23A",
        "vault": "#2E3A78", "vault_star": "#F6DC96", "robe": "#25222A", "pewter": "#9A9CA2", "brew": "#9FDDB0",
    },
}

SUN_WARMTH = 9000                   # Kelvin of the light outside: 9000 = cold blue moonlight (autumn uses 3300)
SUN_STRENGTH = 0.9                  # how bright the moonlight / sunlight through the windows is
LAMP_WARMTH = 2000                  # Kelvin of the candle flames (low = orange)
LAMP_STRENGTH = 4                   # Watts of each candle light
FIRE_STRENGTH = 90                  # Watts of the fire in the grate (the autumn theme banks it down)
CANDLES = True                      # candles on the mantel, desk, window boards and in the stair lantern
FLOATING_CANDLES = 34               # candles drifting under the painted starry vault (0 = none)
STARS = True                        # moon and stars in the sky behind the tower (night theme only)
SEED = 11                           # change to shuffle stones, floorboards, books and small props

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
NIGHT = THEME != "autumn_term"      # night lighting (moon, candles lit, big fire) unless it is the autumn theme

STYLE = "wizard_school_dorm"
KIT_VERSION = 2
W, D, H = ROOM_WIDTH, ROOM_WIDTH, WALL_HEIGHT
CX, CY = W / 2, D / 2               # centre of the round room
RI = W / 2                          # inside face of the tower wall
T = 0.3                             # wall thickness (real tower walls are thick)
RO = RI + T                         # outside face
FLOOR_Z = 0.02                      # top of the oak boards; furniture stands here
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
    tag = {"X": 0.0, "Y": 0.001, "Z": 0.002}[along]
    m = mat(key, round(rough + tag, 3), **kw)
    return surface(m, kind, scale=scale, along=along) if kind else m


def wood(f=1.0, rough=0.45, along="X", key="wood"):
    """Walnut / oak furniture wood. f = lighter or darker; along = grain direction (Z for legs and posts)."""
    return M(key, rough, "wood", along=along, color=shade(COLORS[key], f) if f != 1.0 else None)


def cloth(key, f=1.0, kind="fabric", rough=0.9):
    return M(key, rough, kind, color=shade(COLORS[key], f) if f != 1.0 else None)


def glow(hex_color, strength):
    return mat("flame", 0.4, emit=strength, color=hex_color)


# The room's real materials (one place, so every piece uses the same stone, oak, brass, velvet...).
STONE_TINTS = [M("wall", 0.88, "concrete", scale=1.5, color=shade(mix_hex(COLORS["wall"], tint_, mix_), f))
               for tint_, mix_, f in (("#8C8478", 0.0, 0.93), ("#8C8478", 0.25, 1.0), ("#7E8CA8", 0.2, 1.06),
                                      ("#9C9282", 0.35, 0.98))]
MORTAR = M("mortar", 0.95, "plaster", scale=4)
DRESSED = M("wall_trim", 0.75, "plaster", scale=2.5)         # smooth dressed stone: surrounds, coping, kerbs
DRESSED_DK = M("wall_trim", 0.78, "plaster", scale=2.5, color=shade(COLORS["wall_trim"], 0.86))
OAK_FLOOR = [M("floor", 0.55, "wood", color=shade(COLORS["floor"], f)) for f in (0.92, 1.0, 1.08)]
WOOD = wood()                                                # stained walnut furniture
WOOD_V = wood(along="Z")
WOOD_DK = wood(0.75)
WOOD_DK_V = wood(0.75, along="Z")
OAK = wood(1.35, 0.5)                                        # pale oak: trunk slats, frames, rack
OAK_V = wood(1.35, 0.5, along="Z")
VELVET = cloth("main")                                       # bed curtains, quilt, banner
VELVET_DK = cloth("main", 0.78)
VELVET_LT = cloth("main", 1.18)
TEAL = cloth("accent_1")
TEAL_KNIT = cloth("accent_1", 1.1, kind="knit")
GOLD_CLOTH = M("accent_2", 0.55, "fabric", metal=0.3)         # gold thread trim and fringes
LINEN = cloth("cream")
LINEN_DK = cloth("cream", 0.9)
LEATHER = M("leather", 0.55, "leather")
LEATHER_DK = M("leather", 0.6, "leather", color=shade(COLORS["leather"], 0.7))
LEATHER_RED = M("accent_3", 0.55, "leather")
BRASS = M("brass", 0.32, "brushed", metal=0.9)
GILT = M("accent_2", 0.35, "brushed", metal=0.85)            # gilded picture frames
IRON = M("iron", 0.55, "brushed", metal=0.6, scale=0.3)
COPPER = M("copper", 0.3, "brushed", metal=0.9)
PAPER = M("cream", 0.85, "paper")
PARCHMENT = M("cream", 0.85, "paper", color=mix_hex(COLORS["cream"], "#D9BE8C", 0.45))
CORK = M("cork", 0.95, "concrete", scale=6)
WAX = M("cream", 0.5, "ceramic", scale=0.5, color=mix_hex(COLORS["cream"], "#FFFFFF", 0.3))
SEAL_WAX = mat("accent_3", 0.35, color=shade(COLORS["accent_3"], 0.85))
SOOT = M("dark", 0.95, "concrete", scale=3)
TERRACOTTA = M("accent_3", 0.85, "concrete", scale=3, color=mix_hex(COLORS["accent_3"], "#B87A5A", 0.5))
ROPE = M("cream", 0.95, "knit", scale=2.0, color=mix_hex(COLORS["cream"], "#B89A6A", 0.5))
TWIGS = M("wood", 0.8, "wood", along="Z", color=mix_hex(COLORS["wood"], "#C2A06A", 0.72))
GLASS = mat("glass", 0.05, alpha=0.1)
INK = mat("dark", 0.15, color="#141420")


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


def boxes(name, parts, material, bevel=0.003, coll=None, parent=None, segs=2):
    """MANY boxes merged into one object (fast for hundreds of stones). parts = [(size, loc, rot), ...]."""
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
    return _finish(o, material, min(bevel, h * 0.45), coll, parent)


def ball(name, r, loc, material, scale=(1, 1, 1), rot=(0, 0, 0), parent=None, segs=20):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=segs, v_segments=max(8, segs // 2), radius=r)
    o = _obj(name, bm)
    o.location, o.scale, o.rotation_euler = loc, scale, rot
    return _finish(o, material, 0, None, parent)


def ring(name, big_r, r, loc, material, rot=(0, 0, 0), segs=40, parent=None):
    """Torus (ring) lying flat in local XY."""
    bm = bmesh.new()
    rows = [[bm.verts.new(((big_r + r * math.cos(b)) * math.cos(a), (big_r + r * math.cos(b)) * math.sin(a),
                           r * math.sin(b))) for b in (2 * math.pi * j / 8 for j in range(8))]
            for a in (2 * math.pi * i / segs for i in range(segs))]
    for i in range(segs):
        r1, r2 = rows[i], rows[(i + 1) % segs]
        for j in range(8):
            bm.faces.new((r1[j], r2[j], r2[(j + 1) % 8], r1[(j + 1) % 8]))
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, 0, None, parent)


def spline(ctrl, steps=6, closed=False):
    """Smooth Catmull-Rom curve through control points (for cabriole legs, hoops, cords, quills)."""
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
    """Round bar swept along a path: legs, spindles, hoops, rails, cords, scrolls."""
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
    """Turned shape from a (radius, height) profile: posts, finials, candlesticks, kettle, pots, inkwell."""
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
    if len(rings[0]) > 1:
        bm.faces.new(list(reversed(rings[0])))
    if len(rings[-1]) > 1:
        bm.faces.new(rings[-1])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    o = _obj(name, bm)
    o.location, o.rotation_euler, o.scale = loc, rot, scale
    return _finish(o, material, 0, None, parent)


def prism(name, pts, depth, material, loc=(0, 0, 0), rot=(0, 0, 0), parent=None, bevel=0.0):
    """Flat outline (list of (x, z) points) extruded `depth` along local Y: arches, banners, shields."""
    bm = bmesh.new()
    front = [bm.verts.new((x, -depth / 2, z)) for x, z in pts]
    back = [bm.verts.new((x, depth / 2, z)) for x, z in pts]
    n = len(pts)
    bm.faces.new(front)
    bm.faces.new(list(reversed(back)))
    for i in range(n):
        j = (i + 1) % n
        bm.faces.new((front[i], back[i], back[j], front[j]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    o = _finish(o, material, bevel, None, parent)
    o.data.polygons.foreach_set("use_smooth", [False] * len(o.data.polygons))
    return o


def flat_polys(name, polys, y, material, parent=None):
    """Many flat outlines (lists of (x, z)) in one object at depth y, facing -Y: painted or distant shapes."""
    bm = bmesh.new()
    for poly in polys:
        bm.faces.new([bm.verts.new((x, y, z)) for x, z in poly])
    o = _obj(name, bm)
    o.data.materials.append(material)
    COL_ROOM.objects.link(o)
    o.parent = parent
    return o


def label(name, body, size, loc, material, rot=(R(90), 0, 0), align="CENTER", parent=None, depth=0.003,
          max_width=None):
    """Plain 3D text that is NOT a portfolio hook (engraved plates, the timetable heading)."""
    cu = bpy.data.curves.new(name, "FONT")
    cu.body, cu.size, cu.align_x, cu.align_y = body, size, align, "CENTER"
    cu.extrude = depth
    o = bpy.data.objects.new(name, cu)
    o.location, o.rotation_euler = loc, rot
    o.data.materials.append(material)
    COL_ROOM.objects.link(o)
    o.parent = parent
    if max_width:
        bpy.context.view_layer.update()
        if o.dimensions.x > max_width:
            o.scale = [max_width / o.dimensions.x] * 3
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
            o.visible_shadow = False            # glowing things should not block their own light
    return objs[0]


# --------------------------------------------------------------------- round-room geometry
def P(r, a, z=0.0):
    """Point at distance r from the room centre, at angle a (degrees, 0 = +X, 90 = back, 180 = left)."""
    return Vector((CX + r * math.cos(R(a)), CY + r * math.sin(R(a)), z))


def at_wall(name, a, r=RI, z=0.0, parent=None):
    """Local frame on the curved wall at angle a: local x runs along the wall (to the right when you face it),
    local -y points into the room, z is up. Things built in it face the room centre."""
    return empty(name, P(r, a, z), rot=(0, 0, R(a - 90)), parent=parent)


def arc_block(bm, r0, r1, a0, a1, z0, z1, mi=0, seg=3.0, cx=None, cy=None):
    """Curved block (a ring sector) from radius r0 to r1, angle a0 to a1 (degrees), height z0 to z1."""
    cx = CX if cx is None else cx
    cy = CY if cy is None else cy
    n = max(1, math.ceil(abs(a1 - a0) / seg))
    rings = []
    for i in range(n + 1):
        a = R(a0 + (a1 - a0) * i / n)
        c, s = math.cos(a), math.sin(a)
        rings.append([bm.verts.new((cx + r * c, cy + r * s, z)) for r, z in ((r0, z0), (r1, z0), (r1, z1), (r0, z1))])
    faces = []
    for A, B in zip(rings, rings[1:]):
        for k in range(4):
            faces.append(bm.faces.new((A[k], B[k], B[(k + 1) % 4], A[(k + 1) % 4])))
    faces.append(bm.faces.new(list(reversed(rings[0]))))
    faces.append(bm.faces.new(rings[-1]))
    for f in faces:
        f.material_index = mi
    return faces


def mesh_from(name, bm, materials, bevel=0.0, coll=None, parent=None, smooth=False):
    """bmesh with several material slots -> object."""
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    o = _obj(name, bm)
    for m in materials:
        o.data.materials.append(m)
    if bevel:
        mod = o.modifiers.new("Bevel", "BEVEL")
        mod.width, mod.segments, mod.limit_method = bevel, 2, "ANGLE"
    o.data.polygons.foreach_set("use_smooth", [smooth] * len(o.data.polygons))
    (coll or COL_ROOM).objects.link(o)
    o.parent = parent
    return o


def split_run(length, lo=0.38, hi=0.72, first=None):
    """Cut a course of `length` metres into stones of random length (running bond). Returns [(start, end)]."""
    cuts, pos = [0.0], first if first is not None else random.uniform(lo * 0.5, hi)
    while pos < length - lo * 0.6:
        cuts.append(pos)
        pos += random.uniform(lo, hi)
    cuts.append(length)
    return list(zip(cuts, cuts[1:]))


def lancet(hw, z_sill, z_spring, n=24):
    """Outline of an equilateral pointed-arch window (x, z), anticlockwise from the bottom right."""
    pts = [(hw, z_sill), (hw, z_spring)]
    for i in range(1, n + 1):                                  # right arc: centre (-hw, spring), radius 2 hw
        a = R(60 * i / n)
        pts.append((-hw + 2 * hw * math.cos(a), z_spring + 2 * hw * math.sin(a)))
    for i in range(n - 1, -1, -1):                             # left arc mirrors it
        a = R(60 * i / n)
        pts.append((hw - 2 * hw * math.cos(a), z_spring + 2 * hw * math.sin(a)))
    pts.append((-hw, z_sill))
    return pts


def ray_hit(p0, d, poly):
    """Nearest point where the ray p0 + t d (t > 0) crosses a closed polygon outline."""
    best = None
    for i in range(len(poly)):
        ax, az = poly[i]
        bx, bz = poly[(i + 1) % len(poly)]
        ex, ez = bx - ax, bz - az
        den = d[0] * ez - d[1] * ex
        if abs(den) < 1e-12:
            continue
        t = ((ax - p0[0]) * ez - (az - p0[1]) * ex) / den
        s = ((ax - p0[0]) * d[1] - (az - p0[1]) * d[0]) / den
        if t > 1e-9 and -1e-9 <= s <= 1 + 1e-9 and (best is None or t < best):
            best = t
    return (p0[0] + d[0] * best, p0[1] + d[1] * best)


def clip_line(p, q, poly):
    """Part of segment p-q inside a convex anticlockwise polygon (Cyrus-Beck), or None."""
    t0, t1 = 0.0, 1.0
    dx, dz = q[0] - p[0], q[1] - p[1]
    for i in range(len(poly)):
        ax, az = poly[i]
        bx, bz = poly[(i + 1) % len(poly)]
        nx, nz = -(bz - az), bx - ax                           # inward normal for an anticlockwise outline
        num = nx * (p[0] - ax) + nz * (p[1] - az)
        den = nx * dx + nz * dz
        if abs(den) < 1e-12:
            if num < 0:
                return None
            continue
        t = -num / den
        if den > 0:
            t0 = max(t0, t)
        else:
            t1 = min(t1, t)
        if t0 > t1:
            return None
    return (p[0] + dx * t0, p[1] + dz * t0), (p[0] + dx * t1, p[1] + dz * t1)


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
    """Mark decoration that is hidden once the hook gets a real image (e.g. a painted scene in a frame)."""
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


# --------------------------------------------------------------------- lights
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


# --------------------------------------------------------------------- small shared props
def flame(name, loc, size=1.0, parent=None):
    """Teardrop candle flame (glows, casts no shadow)."""
    fr, fh = 0.0075 * size, 0.034 * size
    return no_shadow(lathe(name, [(0.0, 0), (fr * 0.8, fh * 0.15), (fr, fh * 0.35), (fr * 0.6, fh * 0.7),
                                  (0.0, fh)], loc, glow(COLORS["flame"], 14.0), segs=12, parent=parent))


def candle(name, loc, h=0.16, r=0.02, parent=None, light_w=None, flame_size=1.0, halo=False, magic=False):
    """Ivory church candle with a melt pool, a couple of drips, a wick and (if CANDLES) a flame + light."""
    x, y, z = loc
    lathe(f"{name}_Wax", [(r * 0.97, 0), (r, 0.004), (r, h - 0.004), (r * 0.98, h + 0.003), (r * 0.8, h + 0.001),
                          (r * 0.5, h - 0.006), (0.0, h - 0.008)], (x, y, z), WAX, segs=20, parent=parent)
    for k in range(2):
        a = random.uniform(0, 2 * math.pi)
        ln = random.uniform(0.02, 0.05)
        ball(f"{name}_Drip", 0.0045, (x + math.cos(a) * r, y + math.sin(a) * r, z + h - ln / 2), WAX,
             scale=(1, 1, ln / 0.009), segs=8, parent=parent)
    cyl(f"{name}_Wick", 0.0012, 0.012, (x, y, z + h - 0.003), mat("dark", 0.8), segs=6, bevel=0, parent=parent)
    if CANDLES and (NIGHT or magic):                     # enchanted candles burn by day too
        flame(f"{name}_Flame", (x, y, z + h + 0.002), size=flame_size, parent=parent)
        if halo:                                         # soft glow round the flame (seen from far away)
            no_shadow(ball(f"{name}_Halo", 0.028 * flame_size, (x, y, z + h + 0.02 * flame_size), mat("flame", 0.9,
                           emit=2.5, color=COLORS["flame"], alpha=0.16), scale=(1, 1, 1.3), parent=parent, segs=12))
        if light_w and NIGHT:
            light(f"Light_{name}", "POINT", light_w, kelvin(LAMP_WARMTH), (x, y, z + h + 0.06), size=0.03,
                  parent=parent)


def candlestick(name, loc, parent=None, h=0.2, light_w=None, candle_h=0.17):
    """Turned brass candlestick (about 20 cm) with a church candle."""
    x, y, z = loc
    lathe(f"{name}_Stick", [(0.05, 0), (0.052, 0.006), (0.04, 0.014), (0.016, 0.03), (0.022, 0.05), (0.011, 0.07),
                            (0.011, h - 0.04), (0.02, h - 0.03), (0.012, h - 0.018), (0.028, h - 0.01),
                            (0.03, h - 0.004), (0.018, h)], (x, y, z), BRASS, segs=24, parent=parent)
    candle(f"{name}_Candle", (x, y, z + h - 0.004), h=candle_h, r=0.013, parent=parent, light_w=light_w)


def book(name, size, loc, material, parent=None, rot=(0, 0, 0), bands=True):
    """Leather-bound book: boards, cream page block, raised gilt bands on the spine (spine faces local -Y)."""
    t, d, h = size
    e = empty(name, loc, rot=rot, parent=parent)
    box(f"{name}_Boards", (t, d, h), (0, 0, h / 2), material, bevel=0.003, parent=e)
    box(f"{name}_Pages", (t - 0.006, d - 0.004, h - 0.012), (0, 0.004, h / 2), PAPER, bevel=0.001, parent=e)
    if bands:
        for k, zz in enumerate((0.18, 0.82) if h < 0.22 else (0.15, 0.38, 0.62, 0.85)):
            box(f"{name}_Band", (t + 0.002, 0.004, 0.006), (0, -d / 2 - 0.0005, h * zz), GILT, bevel=0, parent=e)
    return e


# =====================================================================
#  ROOM SHELL: a round tower room in coursed ashlar, cut away towards the camera
# =====================================================================
# Course heights (bottom of each course), scaled with WALL_HEIGHT. Real tower courses are 22-32 cm.
_BASE = [0, 0.30, 0.56, 0.84, 1.10, 1.36, 1.62, 1.88, 2.14, 2.42, 2.68, 2.94, 3.20]
COURSES = [z * H / 3.2 for z in _BASE]
WALL_A0, WALL_A1 = 45.0, 225.0          # the far half of the tower keeps its full height
CUT = [max(0.0, 26 - 2.4 * k) + (random.uniform(-2.5, 2.5) if k else 0) for k in range(len(COURSES) - 1)]

# Windows: a tall lancet with a splayed reveal (wide inside, narrow at the glass) over the desk, and a round
# "oculus" high above the first bed. Angles are round the room (90 = back, 180 = left).
GW, SW = 0.27, 0.43                     # lancet half widths: at the glass / at the inside face
Z_SILL, Z_SPRING = 1.0, 2.0             # lancet window board, and where its pointed arch starts
RG = RI + 0.2                           # radius of the glass (near the outer face)
WINDOWS = [
    {"a": 91.0, "shape": "lancet"},
    {"a": 166.0, "shape": "round", "zc": 2.48, "glass": 0.22, "inner": 0.3},
]


def circle_pts(r, zc, n=48):
    return [(r * math.cos(2 * math.pi * k / n), zc + r * math.sin(2 * math.pi * k / n)) for k in range(n)]


for _w in WINDOWS:                      # outlines, the stone surround's size and the courses it replaces
    if _w["shape"] == "lancet":
        _w["wide"], _w["narrow"] = lancet(SW, Z_SILL, Z_SPRING), lancet(GW, Z_SILL, Z_SPRING)
        _w["p0"], _w["hwr"] = (0.0, (Z_SILL + Z_SPRING) / 2), SW + 0.13
        lo, hi = Z_SILL - 0.08, Z_SPRING + 1.732 * SW + 0.12
    else:
        _w["wide"], _w["narrow"] = circle_pts(_w["inner"], _w["zc"]), circle_pts(_w["glass"], _w["zc"])
        _w["p0"], _w["hwr"] = (0.0, _w["zc"]), _w["inner"] + 0.12
        lo, hi = _w["zc"] - _w["inner"] - 0.1, _w["zc"] + _w["inner"] + 0.1
    _w["gz0"] = max(c for c in COURSES if c <= lo)
    _w["gz1"] = min([c for c in COURSES if c >= hi] or [COURSES[-1]])

BREAST_A, BREAST_W, BREAST_D = 135.0, 1.6, 0.45     # chimney breast: angle, width, how far it stands out
FIRE_OPEN = 0.47                                    # half width of the fire opening in the breast


BASE_Z = -0.52                                      # the tower carries on below the floor (two courses)


def course_spans(k, z0, z1):
    """Angle ranges (degrees) of stone in course k, minus the window openings."""
    spans = [(WALL_A1 - 360.0, WALL_A1)] if k == 0 else [(WALL_A0 - CUT[k], WALL_A1 + CUT[k])]
    for wd in WINDOWS:
        wa = wd["a"]
        if z0 < wd["gz1"] - 1e-6 and z1 > wd["gz0"] + 1e-6:
            half = math.degrees(wd["hwr"] / RI)
            out = []
            for a0, a1 in spans:
                if wa + half <= a0 or wa - half >= a1:
                    out.append((a0, a1))
                    continue
                if wa - half > a0:
                    out.append((a0, wa - half))
                if wa + half < a1:
                    out.append((wa + half, a1))
            spans = out
    return spans


def build_tower():
    g = 0.012                                                    # lime mortar joint
    bm_s, bm_m = bmesh.new(), bmesh.new()
    for k, (z0, z1) in enumerate(zip(COURSES, COURSES[1:])):
        for a0, a1 in course_spans(k, z0, z1):
            arc_block(bm_m, RI + 0.006, RO - 0.006, a0 + 0.12, a1 - 0.12, max(0.0, z0 - 0.007), z1 - 0.007)
            length = R(a1 - a0) * RI
            for s0, s1 in split_run(length):
                ga0 = a0 + math.degrees((s0 + g / 2) / RI)
                ga1 = a0 + math.degrees((s1 - g / 2) / RI)
                arc_block(bm_s, RI - random.uniform(0.0, 0.014), RO + random.uniform(0.0, 0.01), ga0, ga1,
                          z0 + g / 2, z1 - g / 2, mi=random.randrange(len(STONE_TINTS)))
    # The base: the tower carries on below the floor (three courses), so the room sits on solid masonry.
    base = [BASE_Z, BASE_Z / 2, 0.0]
    for z0, z1 in zip(base, base[1:]):
        arc_block(bm_m, RI + 0.006, RO - 0.006, 0, 360, z0, z1 - 0.007)
        for s0, s1 in split_run(R(360) * RO, 0.45, 0.8):
            ga0, ga1 = math.degrees((s0 + g / 2) / RO), math.degrees((s1 - g / 2) / RO)
            arc_block(bm_s, RI, RO + random.uniform(0.0, 0.012), ga0, ga1, z0 + g / 2, z1 - g / 2,
                      mi=random.randrange(len(STONE_TINTS)))
    mesh_from("Tower_Stones", bm_s, STONE_TINTS, bevel=0.012)
    mesh_from("Tower_Mortar", bm_m, [MORTAR])

    # Dressed coping on the full-height wall and crenellated battlements (merlons about 0.56 m, gaps 0.4 m).
    bm_c = bmesh.new()
    arc_block(bm_c, RI - 0.035, RO + 0.03, WALL_A0, WALL_A1, H, H + 0.08)
    a, merlon, crenel = WALL_A0 + 1.0, math.degrees(0.56 / RI), math.degrees(0.40 / RI)
    while a + merlon <= WALL_A1 - 0.5:
        if abs(a + merlon / 2 - BREAST_A) > 14:                  # the chimney stack stands where two would be
            arc_block(bm_c, RI, RO, a, a + merlon, H + 0.08, H + 0.58)
            arc_block(bm_c, RI - 0.02, RO + 0.02, a - 0.3, a + merlon + 0.3, H + 0.58, H + 0.64)
        a += merlon + crenel
    mesh_from("Tower_Battlements", bm_c, [DRESSED], bevel=0.01)

    # Dressed kerb stones round the edge of the floor.
    bm_k = bmesh.new()
    for s0, s1 in split_run(R(360) * RI, 0.5, 0.7):
        arc_block(bm_k, RI - 0.2, RI + 0.01, math.degrees((s0 + 0.004) / RI), math.degrees((s1 - 0.004) / RI),
                  0.0, FLOOR_Z + 0.022)
    mesh_from("Floor_Kerb", bm_k, [DRESSED_DK], bevel=0.008)
    cyl("Tower_Plinth", RO + 0.06, 0.08, (CX, CY, BASE_Z - 0.04), mat("dark", 0.9, color=shade(COLORS["wall"], 0.45)),
        segs=96, bevel=0.02)


build_tower()


def window_surround(name, wd):
    """Dressed-stone window surround: a solid ring of stone with the window hole, wide inside and narrow at the
    glass (the splay), filling the gap left in the coursed wall."""
    a, hwr = wd["a"], wd["hwr"]
    rect = [(hwr, wd["gz0"]), (hwr, wd["gz1"]), (-hwr, wd["gz1"]), (-hwr, wd["gz0"])]
    N = 72
    dirs = [(math.cos(R(-90 + 360 * i / N)), math.sin(R(-90 + 360 * i / N))) for i in range(N)]
    loops_2d = [(rect, RI - 0.012), (wd["wide"], RI - 0.012), (wd["narrow"], RG), (wd["narrow"], RO + 0.004),
                (rect, RO + 0.004)]
    bm, loops = bmesh.new(), []
    for poly, r in loops_2d:
        ring_ = []
        for d in dirs:
            u, z = ray_hit(wd["p0"], d, poly)
            ring_.append(bm.verts.new(P(r, a - math.degrees(u / RI), z)))
        loops.append(ring_)
    for A, B in zip(loops, loops[1:] + loops[:1]):
        for i in range(N):
            j = (i + 1) % N
            bm.faces.new((A[i], A[j], B[j], B[i]))
    return mesh_from(name, bm, [DRESSED], bevel=0.0)


def came_bars(lines_, poly, y=-0.006, t=0.006):
    """Lead cames / iron bars: straight lines clipped to the window outline -> box parts for boxes()."""
    parts = []
    for p, q in lines_:
        seg = clip_line(p, q, poly)
        if seg is None:
            continue
        (x0, z0), (x1, z1) = seg
        ln = math.hypot(x1 - x0, z1 - z0)
        if ln > 0.01:
            parts.append(((ln, t, t), ((x0 + x1) / 2, y, (z0 + z1) / 2), (0, -math.atan2(z1 - z0, x1 - x0), 0)))
    return parts


def window(idx, wd):
    a = wd["a"]
    window_surround(f"Window{idx}_Surround", wd)
    fr = at_wall(f"Window{idx}", a, r=RG)                       # flat frame at the glass, local -y = into room
    k_ = RG / RI                                                # the hole is a touch wider out at the glass
    lead = mat("iron", 0.4, metal=0.5, color=shade(COLORS["iron"], 1.3))
    sky_emit = 1.4 if NIGHT else 1.2
    rnd = random.Random(SEED + idx * 7)
    if wd["shape"] == "lancet":
        gw = GW * k_
        no_shadow(prism(f"Window{idx}_Glass", lancet(gw * 1.06, Z_SILL - 0.01, Z_SPRING), 0.004, GLASS, parent=fr))
        inner = lancet(gw, Z_SILL, Z_SPRING)
        slope = math.tan(R(60))                                 # diamond quarries about 15 x 26 cm
        lines_ = [((k * 0.15 - sg * 0.2 / slope, Z_SILL - 0.2), (k * 0.15 + sg * 2.0 / slope, Z_SILL + 2.0))
                  for sg in (-1, 1) for k in range(-10, 11)]
        boxes(f"Window{idx}_Cames", came_bars(lines_, inner, t=0.0045), lead, bevel=0, parent=fr)
        for zb in (Z_SILL + 0.38, Z_SILL + 0.78):               # iron saddle bars
            box(f"Window{idx}_SaddleBar", (2 * gw + 0.04, 0.01, 0.012), (0, -0.012, zb), IRON, bevel=0.002, parent=fr)
        # The view outside (only seen through the glass): sky, distant hills, the loch, snow or autumn trees.
        hz = Z_SILL + 0.46                                       # horizon (the far shore of the loch)
        top = Z_SPRING + 1.732 * gw + 0.1
        box(f"Window{idx}_Sky", (0.7, 0.004, top - hz + 0.05), (0, 0.075, (top + hz) / 2),
            glow(COLORS["sky"], sky_emit), bevel=0, parent=fr)
        box(f"Window{idx}_SkyLow", (0.7, 0.004, 0.36), (0, 0.072, hz + 0.16), glow(COLORS["sky_low"], sky_emit),
            bevel=0, parent=fr)
        # Two ranges of mountains: tall jagged far peaks with snow caps, and lower dark hills in front.
        far, x, peaks = [(-0.36, hz - 0.02)], -0.36, []
        while x < 0.34:
            x += rnd.uniform(0.07, 0.12)
            far.append((min(x, 0.36), hz + rnd.uniform(0.2, 0.42)))
            peaks.append(len(far) - 1)
            x += rnd.uniform(0.04, 0.07)
            far.append((min(x, 0.36), hz + rnd.uniform(0.08, 0.16)))
        far += [(0.36, hz - 0.02)]
        far_key = mix_hex(COLORS["hills"], COLORS["sky"], 0.3) if NIGHT else mix_hex(COLORS["hills"], COLORS["sky_low"], 0.3)
        prism(f"Window{idx}_Mountains", far, 0.004, glow(far_key, 0.7 if NIGHT else 0.95), loc=(0, 0.07, 0),
              parent=fr)
        caps = []
        for i in peaks:                                          # snow on each peak, following its two slopes
            (ax, az), (px_, pz_), (bx, bz) = far[i - 1], far[i], far[i + 1]
            f_ = 0.32 if pz_ - hz > 0.28 else 0.2
            caps.append([(px_ + (ax - px_) * f_, pz_ + (az - pz_) * f_), (px_ + (bx - px_) * f_ * 0.7,
                         pz_ + (bz - pz_) * f_ * 0.7), (px_, pz_)])
        flat_polys(f"Window{idx}_SnowCaps", caps, 0.068, glow(COLORS["snow"], 1.3 if NIGHT else 1.0), parent=fr)
        ridge, x = [(-0.36, hz - 0.02)], -0.36
        while x < 0.36:
            x += rnd.uniform(0.08, 0.15)
            ridge.append((min(x, 0.36), hz + rnd.uniform(0.04, 0.11)))
        ridge += [(0.36, hz - 0.02)]
        prism(f"Window{idx}_Hills", ridge, 0.004, glow(COLORS["hills"], 0.5 if NIGHT else 0.9), loc=(0, 0.066, 0),
              parent=fr)
        # A dark forest of pines along the near shore of the loch (autumn: the larches and birches turn).
        pines, x = [], -0.37
        while x < 0.37:
            th = rnd.uniform(0.05, 0.12)
            for k in range(3):                                   # three stacked tiers make a fir silhouette
                zb = hz - 0.03 + th * 0.28 * k
                ww = th * (0.34 - 0.08 * k)
                pines.append([(x - ww, zb), (x + ww, zb), (x, zb + th * 0.5)])
            x += rnd.uniform(0.022, 0.04)
        flat_polys(f"Window{idx}_Forest", pines, 0.063, glow(shade(COLORS["tree_1"], 0.55) if NIGHT else
                   COLORS["tree_1"], 0.3 if NIGHT else 0.9), parent=fr)
        box(f"Window{idx}_Lake", (0.7, 0.004, hz - Z_SILL + 0.04), (0, 0.064, (hz + Z_SILL) / 2 - 0.02),
            glow(COLORS["lake"], 1.0 if NIGHT else 1.1), bevel=0, parent=fr)
        if NIGHT:
            # A full moon low over the peaks, so the view reads as "moonlit loch" even at thumbnail size.
            cyl(f"Window{idx}_Moon", 0.055, 0.003, (-0.07, 0.073, hz + 0.6), glow(COLORS["moon"], 3.0),
                rot=(R(90), 0, 0), segs=32, bevel=0, parent=fr)
            cyl(f"Window{idx}_MoonHalo", 0.1, 0.002, (-0.07, 0.074, hz + 0.6),
                glow(mix_hex(COLORS["sky"], COLORS["moon"], 0.35), 1.6), rot=(R(90), 0, 0), segs=32, bevel=0,
                parent=fr)
            for s in range(7):                                   # its path glinting on the loch: widening dashes
                zz = hz - 0.025 - s * (hz - Z_SILL - 0.05) / 7
                box(f"Window{idx}_MoonGlint", (0.03 + 0.018 * s, 0.004, 0.011), (-0.07 + rnd.uniform(-0.012, 0.012),
                    0.062, zz), glow(COLORS["moon"], 1.4), bevel=0, parent=fr)
            for s in range(9):
                box(f"Window{idx}_Star", (0.008, 0.004, 0.008),
                    (rnd.uniform(-0.2, 0.2), 0.07, rnd.uniform(hz + 0.4, top - 0.12)), glow(COLORS["moon"], 3.0),
                    bevel=0, rot=(0, R(45), 0), parent=fr)
            for s in range(7):                                   # snow lying on the outer sill
                ball(f"Window{idx}_Snow", 0.05, (-0.27 + s * 0.09, 0.03, Z_SILL + 0.005), mat("snow", 0.9, emit=0.25),
                     scale=(1.1, 0.6, 0.45), parent=fr)
        else:
            for s in range(9):                                   # autumn trees in the valley below
                key = "tree_1" if s % 2 else "tree_2"
                ball(f"Window{idx}_Tree", rnd.uniform(0.05, 0.09), (-0.32 + s * 0.08 + rnd.uniform(-0.02, 0.02), 0.045,
                     Z_SILL + rnd.uniform(0.02, 0.12)), glow(COLORS[key], 0.9), scale=(1, 0.3, 0.85), parent=fr)
        lz = 1.85
    else:                                                        # round window: a leaded wheel, sky only
        zc, gr = wd["zc"], wd["glass"] * k_
        no_shadow(prism(f"Window{idx}_Glass", circle_pts(gr * 1.06, zc), 0.004, GLASS, parent=fr))
        inner = circle_pts(gr, zc)
        hub = 0.42 * gr                                          # a wheel window: eight spokes out from a hub ring
        lines_ = [((hub * math.cos(R(22.5 + 45 * k)), zc + hub * math.sin(R(22.5 + 45 * k))),
                   (0.4 * math.cos(R(22.5 + 45 * k)), zc + 0.4 * math.sin(R(22.5 + 45 * k)))) for k in range(8)]
        ring_ = circle_pts(hub, zc, 20)
        rim_ = circle_pts(gr * 0.97, zc, 28)                    # outer lead ring holding the spokes
        parts = came_bars(lines_, circle_pts(gr, zc)) + came_bars(list(zip(ring_, ring_[1:] + ring_[:1])), inner) + \
            came_bars(list(zip(rim_, rim_[1:] + rim_[:1])), circle_pts(gr * 1.05, zc))
        boxes(f"Window{idx}_Cames", parts, lead, bevel=0, parent=fr)
        box(f"Window{idx}_Sky", (0.7, 0.004, 0.7), (0, 0.075, zc), glow(COLORS["sky"], sky_emit), bevel=0, parent=fr)
        if NIGHT:
            cyl(f"Window{idx}_Moon", 0.075, 0.004, (0.05, 0.07, zc + 0.04), glow(COLORS["moon"], 3.0),
                rot=(R(90), 0, 0), segs=32, bevel=0, parent=fr)
            for s in range(5):
                box(f"Window{idx}_Star", (0.008, 0.004, 0.008), (rnd.uniform(-0.15, 0.15), 0.072,
                    zc + rnd.uniform(-0.15, 0.15)), glow(COLORS["moon"], 3.0), bevel=0, rot=(0, R(45), 0), parent=fr)
        else:
            for s in range(2):                                   # two soft clouds
                ball(f"Window{idx}_Cloud", 0.09, (rnd.uniform(-0.1, 0.1), 0.07, zc + rnd.uniform(-0.12, 0.08)),
                     glow(COLORS["sky_low"], 1.4), scale=(1.4, 0.2, 0.45), parent=fr)
        lz = zc
    # Window light into the room: cold moonlight at night, golden afternoon sun in autumn.
    col = kelvin(SUN_WARMTH) if NIGHT else kelvin(3300)
    power = (14 if NIGHT else 30) * (1.0 if wd["shape"] == "lancet" else 0.5)
    light(f"Light_Window{idx}", "AREA", power, col, P(RI - 0.5, a, lz), aim=P(RI - 2.5, a, 0.3), size=0.6)
    return fr


WIN_FRAMES = [window(i + 1, wd) for i, wd in enumerate(WINDOWS)]


def build_breast():
    """Chimney breast in the same coursed stone, with the fire opening, plus the stack above the battlements."""
    fr = at_wall("Breast", BREAST_A)
    parts = [[] for _ in STONE_TINTS]
    g = 0.012
    stack_top = H + 0.88
    zs = COURSES + [H + 0.22 * i for i in range(1, 5)]
    zs = [z for z in zs if z <= stack_top + 1e-6]
    for k, (z0, z1) in enumerate(zip(zs, zs[1:])):
        above = z0 >= H - 1e-6
        hw = 0.62 if above else BREAST_W / 2
        y0, y1 = (-0.25, 0.42) if above else (-BREAST_D, 0.12)
        spans = [(-hw, hw)]
        if z0 < 1.0:                                             # the fire opening
            spans = [(-hw, -FIRE_OPEN), (FIRE_OPEN, hw)]
        for x0, x1 in spans:
            for s0, s1 in split_run(x1 - x0, 0.3, 0.55):
                sx0, sx1 = x0 + s0 + g / 2, x0 + s1 - g / 2
                dy = random.uniform(0, 0.01)
                parts[random.randrange(len(parts))].append(
                    ((sx1 - sx0, y1 - y0 + dy, z1 - z0 - g), ((sx0 + sx1) / 2, (y0 + y1 - dy) / 2, (z0 + z1) / 2),
                     (0, 0, 0)))
    for i, p in enumerate(parts):
        if p:
            boxes(f"Breast_Stones_{i}", p, STONE_TINTS[i], bevel=0.01, parent=fr)
    # Mortar behind the stones (one block each for breast and stack; the opening keeps its own gap).
    fz = COURSES[next(i for i, c in enumerate(COURSES) if c >= 1.0)]          # top of the fire opening
    box("Breast_Mortar_Body", (BREAST_W - 0.02, BREAST_D + 0.1, H - fz), (0, -BREAST_D / 2 + 0.07, (H + fz) / 2),
        MORTAR, bevel=0, parent=fr)
    for sx in (-1, 1):
        wlow = BREAST_W / 2 - FIRE_OPEN - 0.02
        box("Breast_Mortar_Low", (wlow, BREAST_D + 0.1, fz), (sx * (FIRE_OPEN + 0.01 + wlow / 2),
            -BREAST_D / 2 + 0.07, fz / 2), MORTAR, bevel=0, parent=fr)
    box("Stack_Mortar", (1.22, 0.65, stack_top - H), (0, 0.085, (stack_top + H) / 2), MORTAR, bevel=0, parent=fr)
    box("Breast_Cap", (BREAST_W + 0.04, 0.24, 0.06), (0, -BREAST_D + 0.1, H + 0.03), DRESSED, bevel=0.01, parent=fr)
    # Firebox: soot-black brick sides and back, with a cast-iron fireback.
    box("Firebox_Back", (2 * FIRE_OPEN + 0.04, 0.05, fz), (0, 0.06, fz / 2), SOOT, bevel=0, parent=fr)
    for sx in (-1, 1):
        box("Firebox_Side", (0.04, BREAST_D + 0.12, fz), (sx * (FIRE_OPEN + 0.0), -BREAST_D / 2 + 0.06, fz / 2),
            SOOT, bevel=0, parent=fr)
    box("Firebox_Top", (2 * FIRE_OPEN + 0.04, BREAST_D + 0.12, 0.04), (0, -BREAST_D / 2 + 0.06, fz - 0.02), SOOT,
        bevel=0, parent=fr)
    box("Firebox_Floor", (2 * FIRE_OPEN, BREAST_D + 0.12, 0.02), (0, -BREAST_D / 2 + 0.06, FLOOR_Z - 0.008),
        SOOT, bevel=0, parent=fr)
    fb = [(-0.3, 0.05), (0.3, 0.05), (0.3, 0.5), (0.18, 0.62), (0.0, 0.68), (-0.18, 0.62), (-0.3, 0.5)]
    prism("Fireback", fb, 0.025, IRON, loc=(0, 0.02, 0), parent=fr, bevel=0.004)
    ball("Fireback_Boss", 0.06, (0, 0.006, 0.42), IRON, scale=(1, 0.25, 1), parent=fr)
    # Stack top: dressed cap and two clay chimney pots.
    box("Stack_Cap", (1.34, 0.79, 0.08), (0, 0.085, stack_top + 0.04), DRESSED, bevel=0.01, parent=fr)
    for sx in (-0.26, 0.26):
        lathe("Stack_Pot", [(0.12, 0), (0.12, 0.05), (0.1, 0.07), (0.085, 0.34), (0.105, 0.37), (0.105, 0.42),
                            (0.08, 0.42), (0.07, 0.3), (0.0, 0.3)], (sx, 0.085, stack_top + 0.08), TERRACOTTA, segs=24,
              parent=fr)
    return fr


BREAST = build_breast()
BREAST_FACE = RI - BREAST_D            # radius of the breast's front face

# ---------------------------------------------------------------- the enchanted ceiling: a painted starry vault
# The top of the tower room is plastered and painted as a night sky where the vault would spring: deep blue with gilt
# stars, constellations joined by fine gold lines and two crescents, above a gilt bead. The real sky shows through the
# open top of the cut-away tower, so painted sky and real sky run into each other - an "enchanted" ceiling.
VAULT_Z0 = COURSES[-3]                                    # the painted band starts two courses below the coping
VAULT = M("vault", 0.8, "plaster", scale=2.5, emit=0.22 if NIGHT else 0.14)
STAR_PAINT = glow(COLORS["vault_star"], 2.8 if NIGHT else 1.2)
VAULT_R = RI - 0.016                                      # face of the plaster, just proud of the stones


def star_shape(c, u, v, size, points=4, inner=0.32, turn=0.0):
    """Outline of a pointed star round c in the plane of unit vectors u, v."""
    out = []
    for i in range(points * 2):
        a = turn + math.pi * i / points
        rr = size if i % 2 == 0 else size * inner
        out.append(c + u * (rr * math.cos(a)) + v * (rr * math.sin(a)))
    return out


def vault_floor(a_deg):
    """Lowest painted height at angle a: the band steps up over the window surrounds."""
    z = VAULT_Z0
    for wd in WINDOWS:
        if abs(a_deg - wd["a"]) < math.degrees(wd["hwr"] / RI) + 0.8:
            z = max(z, wd["gz1"])
    return z


def build_vault():
    rnd = random.Random(SEED + 41)
    half = math.degrees(math.asin(0.79 / RI))                    # the chimney breast cuts the band in two
    spans = [(WALL_A0 + 2.0, BREAST_A - half), (BREAST_A + half, WALL_A1 - 2.0)]
    bm = bmesh.new()
    for a0, a1 in spans:                                         # plaster shell, stepped over the windows
        cuts = sorted({a0, a1} | {c for wd in WINDOWS for c in (wd["a"] - math.degrees(wd["hwr"] / RI) - 0.8,
                                                                wd["a"] + math.degrees(wd["hwr"] / RI) + 0.8)
                                  if a0 < c < a1})
        for c0, c1 in zip(cuts, cuts[1:]):
            arc_block(bm, VAULT_R, RI + 0.004, c0, c1, vault_floor((c0 + c1) / 2), H - 0.004, seg=2.0)
    mesh_from("Vault_Paint", bm, [VAULT], smooth=True)
    for a0, a1 in spans:                                         # gilt bead along the bottom edge
        n = max(2, math.ceil((a1 - a0) / 2.0))
        pts = [P(VAULT_R - 0.004, a0 + (a1 - a0) * i / n, vault_floor(a0 + (a1 - a0) * i / n) + 0.008)
               for i in range(n + 1)]
        tube("Vault_Bead", pts, 0.012, GILT, segs=8)

    def frame_at(a_deg, z):
        a = R(a_deg)
        c = Vector((CX + (VAULT_R - 0.002) * math.cos(a), CY + (VAULT_R - 0.002) * math.sin(a), z))
        return c, Vector((-math.sin(a), math.cos(a), 0)), Vector((0, 0, 1))

    bm, lines = bmesh.new(), []
    for a0, a1 in spans:
        length = R(a1 - a0) * RI
        for k in range(int(length * 34)):
            a_ = rnd.uniform(a0 + 0.8, a1 - 0.8)
            z_ = rnd.uniform(vault_floor(a_) + 0.05, H - 0.03)
            c, u, v = frame_at(a_, z_)
            big = rnd.random() < 0.16
            size = rnd.uniform(0.02, 0.034) if big else rnd.uniform(0.006, 0.013)
            bm.faces.new([bm.verts.new(p_) for p_ in star_shape(c, u, v, size, 4 if rnd.random() < 0.7 else 5,
                                                                 0.3 if big else 0.45, rnd.uniform(0, 1))])
        for g in range(int(length / 1.4)):                         # constellations: 4-6 stars joined by gold lines
            a_ = rnd.uniform(a0 + 3, a1 - 12)
            z_ = rnd.uniform(VAULT_Z0 + 0.12, H - 0.12)
            chain = []
            for k in range(rnd.randint(4, 6)):
                if z_ > vault_floor(a_) + 0.05:
                    chain.append(frame_at(a_, z_)[0])
                a_ += rnd.uniform(1.6, 3.0)
                z_ = min(H - 0.06, max(VAULT_Z0 + 0.06, z_ + rnd.uniform(-0.13, 0.13)))
            for pa, pb in zip(chain, chain[1:]):
                d_ = (pb - pa).normalized()
                side = d_.cross(Vector((pa.x - CX, pa.y - CY, 0)).normalized()).normalized() * 0.0022
                lines.append([pa - side, pb - side, pb + side, pa + side])
            for c in chain:
                a_c = math.degrees(math.atan2(c.y - CY, c.x - CX))
                _, u, v = frame_at(a_c, c.z)
                bm.faces.new([bm.verts.new(p_) for p_ in star_shape(c + (Vector((CX, CY, c.z)) - c).normalized()
                                                                     * 0.001, u, v, 0.024, 4, 0.28)])
    for q in lines:
        bm.faces.new([bm.verts.new(p_) for p_ in q])
    o = _obj("Vault_Stars", bm)
    o.data.materials.append(STAR_PAINT)
    COL_ROOM.objects.link(o)
    no_shadow(o)
    for a_, z_ in ((WALL_A0 + 18, H - 0.2), (BREAST_A + 40, H - 0.17)):    # two painted gilt crescents
        c, u, v = frame_at(a_, z_)
        bm = bmesh.new()
        outer = [c + u * (0.1 * math.cos(R(t))) + v * (0.1 * math.sin(R(t))) for t in range(-110, 111, 10)]
        inner_ = [c + u * (0.035 + 0.075 * math.cos(R(t))) + v * (0.083 * math.sin(R(t))) for t in range(110, -111, -10)]
        bm.faces.new([bm.verts.new(p_) for p_ in outer + inner_])
        mo = _obj("Vault_Crescent", bm)
        mo.data.materials.append(STAR_PAINT)
        COL_ROOM.objects.link(mo)


build_vault()


def build_floor():
    """180 mm oak boards in random lengths, clipped to the round room, with a hole for the spiral stair."""
    rnd = random.Random(SEED + 3)
    bw, gap = 0.18, 0.003
    parts = [[] for _ in OAK_FLOOR]
    under = []
    rmax = RI - 0.02
    y = CY - rmax
    while y < CY + rmax:
        yc = y + bw / 2
        dy = max(0.0, abs(yc - CY) - bw / 2)
        if dy < rmax:
            half = math.sqrt(rmax * rmax - dy * dy)
            spans = [(CX - half, CX + half)]
            sdy = max(0.0, abs(yc - STAIR[1]) - bw / 2)
            if sdy < WELL_R:
                sh = math.sqrt(WELL_R ** 2 - sdy ** 2)
                spans = [(CX - half, STAIR[0] - sh), (STAIR[0] + sh, CX + half)]
            for x0, x1 in spans:
                if x1 - x0 < 0.05:
                    continue
                under.append(((x1 - x0, bw, 0.004), ((x0 + x1) / 2, yc, 0.002), (0, 0, 0)))
                pos = x0
                while pos < x1 - 0.01:
                    ln = min(rnd.uniform(0.9, 2.2), x1 - pos)
                    if pos == x0:
                        ln = min(rnd.uniform(0.3, 1.8), x1 - pos)
                    parts[rnd.randrange(len(parts))].append(
                        ((ln - gap, bw - gap, FLOOR_Z - 0.004), (pos + ln / 2, yc, 0.004 + (FLOOR_Z - 0.004) / 2),
                         (0, 0, 0)))
                    pos += ln
        y += bw
    for i, p in enumerate(parts):
        boxes(f"Floor_Boards_{i}", p, OAK_FLOOR[i], bevel=0.0015)
    boxes("Floor_Joints", under, mat("dark", 0.9, color=shade(COLORS["floor"], 0.35)), bevel=0)


STAIR = P(1.55, 262)                   # centre of the spiral stair well (front, by the trunk)
WELL_R = 0.5
SHAFT_Z = -1.2                         # the stair shaft goes on down inside the tower (hidden by the plinth)
build_floor()


def build_stair():
    """Medieval newel stair: wedge treads round a central newel, a stone kerb and an oak handrail."""
    sx, sy = STAIR[0], STAIR[1]
    bm = bmesh.new()
    for s0, s1 in split_run(R(360) * (WELL_R + 0.07), 0.35, 0.5):
        a0, a1 = math.degrees(s0 / (WELL_R + 0.07)), math.degrees(s1 / (WELL_R + 0.07))
        arc_block(bm, WELL_R, WELL_R + 0.15, a0 + 0.4, a1 - 0.4, -0.02, FLOOR_Z + 0.035, cx=sx, cy=sy)
    mesh_from("Stair_Kerb", bm, [DRESSED], bevel=0.008)
    bm, bm_m = bmesh.new(), bmesh.new()                          # the stair shaft: curved stones going down
    for z0, z1 in ((SHAFT_Z, -0.9), (-0.9, -0.6), (-0.6, -0.3), (-0.3, -0.01)):
        arc_block(bm_m, WELL_R + 0.01, WELL_R + 0.05, 0, 360, z0, z1, cx=sx, cy=sy, seg=6)
        off = random.uniform(0, 60)
        for s0, s1 in split_run(R(360) * WELL_R, 0.3, 0.45):
            arc_block(bm, WELL_R - random.uniform(0, 0.01), WELL_R + 0.05, off + math.degrees(s0 / WELL_R) + 0.8,
                      off + math.degrees(s1 / WELL_R) - 0.8, z0 + 0.006, z1 - 0.006, cx=sx, cy=sy, seg=6,
                      mi=random.randrange(len(STONE_TINTS)))
    mesh_from("Stair_Shaft", bm, STONE_TINTS, bevel=0.008)
    mesh_from("Stair_ShaftMortar", bm_m, [MORTAR])
    # Wedge treads (15 cm rise, 30 degrees each). You step down on the far side, facing the room, so the first
    # treads wind down in plain view; the rest carry on round under the near side.
    rise, a = 0.15, 172.0
    top = FLOOR_Z - rise
    cyl("Stair_Newel", 0.075, top - SHAFT_Z, (sx, sy, (SHAFT_Z + top) / 2), DRESSED, segs=24, bevel=0.01)
    lathe("Stair_NewelPost", [(0.05, 0), (0.05, 0.06), (0.036, 0.1), (0.04, 0.3), (0.028, 0.6), (0.03, 0.92),
                               (0.042, 0.96), (0.03, 1.0)], (sx, sy, top), OAK_V, segs=16)   # oak newel post
    ball("Stair_NewelPostCap", 0.045, (sx, sy, top + 1.04), OAK)
    cyl("Stair_Bottom", WELL_R + 0.02, 0.02, (sx, sy, SHAFT_Z), SOOT, segs=40, bevel=0)
    bm = bmesh.new()
    for k in range(7):
        z = FLOOR_Z - rise * (k + 1)
        arc_block(bm, 0.07, WELL_R - 0.004, a - 30 * (k + 1) + 1.2, a - 30 * k, z - 0.06, z, cx=sx, cy=sy, seg=4,
                  mi=k % 2)
    mesh_from("Stair_Treads", bm, [DRESSED, DRESSED_DK], bevel=0.008)
    bm = bmesh.new()                                             # worn oak nosing strips on the treads
    for k in range(7):
        z = FLOOR_Z - rise * (k + 1)
        arc_block(bm, 0.09, WELL_R - 0.02, a - 30 * (k + 1) + 1.4, a - 30 * (k + 1) + 4.5, z - 0.004, z + 0.012, cx=sx, cy=sy,
                  seg=4)
    mesh_from("Stair_Nosing", bm, [OAK], bevel=0.003)
    # Oak handrails on turned balusters either side of the far opening where you step down (newel posts at each
    # end); the near side is left open so you can look down the stair.
    rail_r = WELL_R + 0.075
    for r0, r1 in ((a + 6, a + 78), (a - 135, a - 66)):
        ang = [r0 + i * (r1 - r0) / 4 for i in range(5)]
        for aa in ang[1:-1]:
            bx, by = sx + rail_r * math.cos(R(aa)), sy + rail_r * math.sin(R(aa))
            lathe("Stair_Baluster", [(0.02, 0), (0.02, 0.05), (0.013, 0.08), (0.022, 0.2), (0.012, 0.45),
                                     (0.016, 0.74), (0.016, 0.82)], (bx, by, FLOOR_Z + 0.035), OAK_V, segs=12)
        for aa in (ang[0], ang[-1]):
            bx, by = sx + rail_r * math.cos(R(aa)), sy + rail_r * math.sin(R(aa))
            box("Stair_Post", (0.06, 0.06, 0.9), (bx, by, FLOOR_Z + 0.48), OAK_V, bevel=0.005, rot=(0, 0, R(aa)))
            ball("Stair_PostCap", 0.04, (bx, by, FLOOR_Z + 0.96), OAK)
        pts = [(sx + rail_r * math.cos(R(t)), sy + rail_r * math.sin(R(t)), FLOOR_Z + 0.88)
               for t in [r0 + i * (r1 - r0) / 24 for i in range(25)]]
        tube("Stair_Handrail", pts, 0.025, OAK, segs=12)
    # Warm light rising from the room below.
    light("Light_Stair", "AREA", 70 if NIGHT else 20, kelvin(2600), (sx, sy, SHAFT_Z + 0.1), aim=(sx, sy, 2),
          size=0.7)
    light("Light_StairWell", "POINT", 22 if NIGHT else 8, kelvin(2400), (sx + 0.2, sy - 0.2, -0.45), size=0.15)
    # A candle on the wall of the shaft, a few treads down on the far side, so the winding treads catch the light.
    light("Light_StairTreads", "POINT", 14 if NIGHT else 5, kelvin(2200),
          (sx + (WELL_R - 0.12) * math.cos(R(a - 45)), sy + (WELL_R - 0.12) * math.sin(R(a - 45)), FLOOR_Z - 0.12),
          size=0.08)
    # Iron lantern on the kerb with a candle inside.
    lx, ly = sx + (rail_r + 0.2) * math.cos(R(292)), sy + (rail_r + 0.2) * math.sin(R(292))
    le = empty("Lantern", (lx, ly, FLOOR_Z), rot=(0, 0, R(20)))
    box("Lantern_Base", (0.16, 0.16, 0.03), (0, 0, 0.015), IRON, bevel=0.004, parent=le)
    for cx_ in (-1, 1):
        for cy_ in (-1, 1):
            box("Lantern_Post", (0.012, 0.012, 0.22), (cx_ * 0.072, cy_ * 0.072, 0.14), IRON, bevel=0.002, parent=le)
    for k in range(4):
        rot = (0, 0, R(90 * k))
        off = Vector((0, -0.072, 0.14))
        off.rotate(Euler(rot))
        g_ = box("Lantern_Pane", (0.13, 0.003, 0.2), tuple(off), mat("glass", 0.05, alpha=0.25), bevel=0, rot=rot,
                 parent=le)
        no_shadow(g_)
    lathe("Lantern_Roof", [(0.1, 0), (0.1, 0.01), (0.03, 0.08), (0.015, 0.09), (0.0, 0.09)], (0, 0, 0.25), IRON,
          segs=4, parent=le, rot=(0, 0, R(45)))
    ring("Lantern_Ring", 0.025, 0.004, (0, 0, 0.36), IRON, rot=(R(90), 0, 0), parent=le)
    candle("Lantern_Candle", (0, 0, 0.03), h=0.1, r=0.022, parent=le, light_w=LAMP_STRENGTH * 1.5)


build_stair()


# =====================================================================
#  FURNITURE SLOTS  (shared names; size = (width, depth, height) in metres; front faces local -Y)
# =====================================================================
def polar_slot(name, size, r, a, turn, z=FLOOR_Z, kind="floor", shape="box"):
    p = P(r, a)
    return slot(name, size, (round(p.x, 3), round(p.y, 3)), z=z, turn=turn, kind=kind, shape=shape)


# The round room is fitted like a real one: the big pieces stand square to the room (the shared slot boxes are
# axis-aligned), along the left and back curves of the wall; the fireplace sits on the diagonal between them.
polar_slot("fireplace", (1.3, 0.3, 1.5), BREAST_FACE - 0.15, BREAST_A, BREAST_A - 90, shape="box")
slot("bed",       (1.04, 2.1, 2.3),   (0.9, 2.65),   turn=0, shape="bed")      # head towards the fireplace
slot("trunk",     (0.86, 0.48, 0.56), (1.12, 1.3),   turn=0, shape="box")      # at the foot of the bed
slot("armchair",  (0.78, 0.84, 1.06), (1.93, 3.3),   turn=75, shape="chair")   # fireside wing chair
slot("desk",      (1.0, 0.55, 0.75),  (2.75, 5.15),  turn=0, shape="table")    # under the lancet window
slot("chair",     (0.5, 0.52, 0.92),  (2.75, 4.6),   turn=180, shape="chair")
polar_slot("bookcase", (0.6, 0.32, 1.75), 2.6, 110, 20, shape="shelf")         # beside the chimney breast
slot("pet",       (0.6, 0.55, 1.95),  (3.7, 4.85),   turn=10, shape="pet")      # owl cage on a stand by the window
slot("rug",       (1.8, 1.8, 0.012),  (2.65, 2.85),  kind="rug", shape="rug")


# =====================================================================
#  PLACEHOLDER FURNITURE  (replaced when you add your own with add_furniture.py)
# =====================================================================
def drape(name, path, z_top, z_bot, material, parent, amp=0.025, pitch=0.11, anchor=None, tie=None, rows=12):
    """Pleated curtain hanging from a rail along `path` (local (x, y) points). anchor + tie = a tied-back curtain:
    at the tie height the cloth is gathered toward the anchor (a bed post), flaring again below."""
    P_ = [Vector((x, y, 0)) for x, y in path]
    seglen = [(b - a).length for a, b in zip(P_, P_[1:])]
    total = sum(seglen)
    n = max(8, int(total / pitch * 6))
    bm, grid = bmesh.new(), []
    zt = None if tie is None else (z_top - tie) / (z_top - z_bot)

    def at(s):
        for (a, b), L in zip(zip(P_, P_[1:]), seglen):
            if s <= L or (a, b) == (P_[-2], P_[-1]):
                t = min(1.0, s / L) if L else 0
                return a + (b - a) * t, (b - a).normalized()
            s -= L

    for j in range(rows + 1):
        f = j / rows
        z = z_top + (z_bot - z_top) * f
        g = 1.0
        if zt is not None:                                       # 1 at the rail, pinched at the tie, flared below
            g = 1 - 0.78 * math.exp(-((f - zt) / 0.18) ** 2) if f < zt else 0.22 + 0.4 * (f - zt) / (1 - zt)
            g = min(1.0, g) if f < zt else g
        row = []
        for i in range(n + 1):
            s = total * i / n
            p, tdir = at(s)
            nrm = Vector((-tdir.y, tdir.x, 0))
            fold = amp * (0.6 + 0.4 * f) * math.sin(2 * math.pi * s / pitch) * (1.4 - 0.4 * g)
            q = p + nrm * fold
            if anchor is not None:
                av = Vector((anchor[0], anchor[1], 0))
                q = av + (q - av) * g
            row.append(bm.verts.new((q.x, q.y, z)))
        grid.append(row)
    for A, B in zip(grid, grid[1:]):
        for i in range(n):
            bm.faces.new((A[i], A[i + 1], B[i + 1], B[i]))
    o = _obj(name, bm)
    o.data.materials.append(material)
    sol = o.modifiers.new("Thickness", "SOLIDIFY")
    sol.thickness, sol.offset = 0.012, 0
    o.data.polygons.foreach_set("use_smooth", [True] * len(o.data.polygons))
    COL_ROOM.objects.link(o)
    o.parent = parent
    return o


def four_poster(root, w=1.04, l=2.1, wall_side=-1, prefix="Bed", quilt=None, head_curtain=True, open_head=False,
                tie_all=False, pelmet_sides=(0, 1, 2, 3)):
    """Single four-poster with an open tester: turned posts on square blocks, panelled head, low foot, a pleated
    pelmet with a gold fringe round the tester, velvet curtains drawn along the wall side and tied back on the
    room side. head_curtain=False ties the head-end curtain back too (so you can see past the bed); open_head=True
    leaves the pelmet off the head end and the room side and drops the head curtains, so the bed does not hide
    what stands behind it (the tester rails stay). tie_all=True ties every curtain back to its post (nothing is
    drawn closed), for a bed that stands out in the room; pelmet_sides picks the sides of the tester that carry a
    pelmet (0 foot, 1 +x side, 2 head, 3 -x side)."""
    quilt = quilt or VELVET
    px, py = w / 2 - 0.04, l / 2 - 0.04
    for sx in (-1, 1):
        for sy in (-1, 1):
            x, y = sx * px, sy * py
            box(f"{prefix}_PostBlock", (0.075, 0.075, 0.58), (x, y, 0.29), WOOD_V, bevel=0.004, parent=root)
            lathe(f"{prefix}_Post", [(0.03, 0), (0.034, 0.02), (0.026, 0.04), (0.032, 0.12), (0.036, 0.2),
                                     (0.028, 0.3), (0.022, 0.42), (0.02, 0.9), (0.026, 0.96), (0.02, 1.02),
                                     (0.018, 1.5), (0.024, 1.54), (0.024, 1.58)], (x, y, 0.58), WOOD_V, segs=16,
                  parent=root)
            lathe(f"{prefix}_Finial", [(0.02, 0), (0.03, 0.03), (0.034, 0.05), (0.02, 0.08), (0.008, 0.11),
                                       (0.0, 0.13)], (x, y, 2.16), WOOD_V, segs=16, parent=root)
    for sx in (-1, 1):                                            # side rails and the tester frame
        box(f"{prefix}_SideRail", (0.035, l - 0.12, 0.15), (sx * px, 0, 0.33), WOOD, bevel=0.003, parent=root)
        box(f"{prefix}_TesterSide", (0.045, l - 0.04, 0.05), (sx * px, 0, 2.14), WOOD, bevel=0.003, parent=root)
    for sy in (-1, 1):
        box(f"{prefix}_EndRail", (w - 0.12, 0.035, 0.15), (0, sy * py, 0.33), WOOD, bevel=0.003, parent=root)
        box(f"{prefix}_TesterEnd", (w - 0.04, 0.045, 0.05), (0, sy * py, 2.14), WOOD, bevel=0.003, parent=root)
    # Panelled headboard with an arched top rail; low panelled footboard.
    box(f"{prefix}_Headboard", (w - 0.1, 0.03, 0.62), (0, py, 0.86), WOOD, bevel=0.004, parent=root)
    for k in (-1, 0, 1):
        box(f"{prefix}_HeadPanel", (0.24, 0.012, 0.36), (k * 0.29, py - 0.018, 0.86), WOOD_DK, bevel=0.006,
            parent=root)
    arch = [(x_, py, 1.17 + 0.1 * math.cos(math.pi * x_ / (w - 0.1))) for x_ in
            [-(w - 0.1) / 2 + i * (w - 0.1) / 16 for i in range(17)]]
    tube(f"{prefix}_HeadTopRail", arch, 0.025, WOOD, segs=10, parent=root)
    box(f"{prefix}_HeadTopFill", (w - 0.16, 0.028, 0.08), (0, py, 1.2), WOOD, bevel=0.003, parent=root)
    box(f"{prefix}_Footboard", (w - 0.1, 0.03, 0.24), (0, -py, 0.5), WOOD, bevel=0.004, parent=root)
    cyl(f"{prefix}_FootRail", 0.02, w - 0.1, (0, -py, 0.63), WOOD, rot=(0, R(90), 0), segs=12, parent=root)
    # Mattress (top at 55 cm), quilt with a turned-down linen sheet, pillow and a folded knitted throw.
    box(f"{prefix}_Mattress", (w - 0.12, l - 0.14, 0.18), (0, 0, 0.46), LINEN_DK, bevel=0.04, parent=root)
    ql = l * 0.7
    qy = -l / 2 + 0.07 + ql / 2
    box(f"{prefix}_Quilt", (w - 0.08, ql, 0.05), (0, qy, 0.56), quilt, bevel=0.022, parent=root)
    for sx in (-1, 1):
        box(f"{prefix}_QuiltDrop", (0.03, ql, 0.2), (sx * (w / 2 - 0.045), qy, 0.47), quilt, bevel=0.012,
            parent=root)
    box(f"{prefix}_Sheet", (w - 0.08, 0.16, 0.056), (0, qy + ql / 2 + 0.06, 0.562), LINEN, bevel=0.022, parent=root)
    box(f"{prefix}_QuiltBand", (w - 0.075, 0.05, 0.052), (0, qy + ql / 2 - 0.04, 0.565), GOLD_CLOTH, bevel=0.02,
        parent=root)
    ball(f"{prefix}_Pillow", 0.1, (0, py - 0.24, 0.62), LINEN, scale=(3.6, 1.7, 0.8), parent=root)
    box(f"{prefix}_Throw", (w - 0.02, 0.3, 0.03), (0, -l / 2 + 0.36, 0.6), TEAL_KNIT, bevel=0.012, parent=root)
    for sx in (-1, 1):
        box(f"{prefix}_ThrowDrop", (0.025, 0.3, 0.2), (sx * (w / 2 - 0.0), -l / 2 + 0.36, 0.5), TEAL_KNIT,
            bevel=0.01, parent=root)
    # Pleated pelmet round all four sides of the tester, and a gold fringe under it.
    e = 0.05
    corners = [(-w / 2 - e + 0.02, -l / 2 - e + 0.02), (w / 2 + e - 0.02, -l / 2 - e + 0.02),
               (w / 2 + e - 0.02, l / 2 + e - 0.02), (-w / 2 - e + 0.02, l / 2 + e - 0.02)]
    for k in range(4):
        a_, b_ = corners[k], corners[(k + 1) % 4]
        if (open_head and (k == 2 or (k == 3 if wall_side > 0 else k == 1))) or k not in pelmet_sides:
            continue                                              # k: 0 foot, 1 +x side, 2 head, 3 -x side
        drape(f"{prefix}_Pelmet", [a_, b_], 2.2, 1.98, VELVET, root, amp=0.008, pitch=0.06, rows=3)
        mid = ((a_[0] + b_[0]) / 2, (a_[1] + b_[1]) / 2)
        ln = math.hypot(b_[0] - a_[0], b_[1] - a_[1])
        rz = math.atan2(b_[1] - a_[1], b_[0] - a_[0])
        box(f"{prefix}_Fringe", (ln, 0.02, 0.035), (mid[0], mid[1], 1.965), GOLD_CLOTH, bevel=0.004,
            rot=(0, 0, rz), parent=root)
    # Curtains: drawn closed along the wall side and behind the headboard; tied back on the room side and foot.
    cx_w, cx_r = wall_side * (w / 2 + 0.03), -wall_side * (w / 2 + 0.03)
    if not tie_all:
        drape(f"{prefix}_CurtainWall", [(cx_w, -l / 2 + 0.02), (cx_w, l / 2 - 0.02)], 1.97, 0.06, VELVET, root,
              amp=0.03, pitch=0.13)
    tied = [("Head", [(cx_r, l / 2 - 0.03), (cx_r, l / 2 - 0.42)], (cx_r, py)),
            ("Foot", [(cx_r, -l / 2 + 0.03), (cx_r, -l / 2 + 0.42)], (cx_r, -py)),
            ("FootWall", [(cx_w * 0.98, -l / 2 - 0.03), (-cx_w * 0.2, -l / 2 - 0.03)], (wall_side * px, -py))]
    if tie_all:                                                   # all four corners tied back to their posts
        tied = [t for t in tied if t[0] != "FootWall"] + [
            ("WallHead", [(cx_w, l / 2 - 0.03), (cx_w, l / 2 - 0.42)], (wall_side * px, py)),
            ("WallFoot", [(cx_w, -l / 2 + 0.03), (cx_w, -l / 2 + 0.42)], (wall_side * px, -py))]
    elif open_head:
        tied = [t for t in tied if t[0] != "Head"]
    elif head_curtain:
        drape(f"{prefix}_CurtainHead", [(-w / 2 + 0.03, l / 2 + 0.03), (w / 2 - 0.03, l / 2 + 0.03)], 1.97, 0.06,
              VELVET, root, amp=0.03, pitch=0.13)
    if not head_curtain and not open_head:
        tied.append(("HeadWall", [(cx_w * 0.98, l / 2 + 0.03), (-cx_w * 0.2, l / 2 + 0.03)], (wall_side * px, py)))
    tie_z = 1.0
    for nm, path, post in tied:
        drape(f"{prefix}_Curtain{nm}", path, 1.97, 0.08, VELVET, root, amp=0.028, pitch=0.1, anchor=post,
              tie=tie_z, rows=16)
        tb = (post[0] + (0.035 if post[0] < 0 else -0.035) * 0, post[1], tie_z)
        ring(f"{prefix}_TieBack{nm}", 0.07, 0.008, tb, GOLD_CLOTH, parent=root, segs=24)
        lathe(f"{prefix}_Tassel{nm}", [(0.004, 0), (0.016, 0.02), (0.02, 0.06), (0.012, 0.085), (0.006, 0.09),
                                       (0.0, 0.1)], (tb[0], tb[1], tie_z - 0.015), GOLD_CLOTH, segs=12,
              parent=root, rot=(R(180), 0, 0))


def build_bed():
    """Single four-poster (Pino / Farringdon single type, 210 x 104 cm, 2.22 m tall) against the curved wall."""
    root, w, d, h = furniture_root("bed")
    four_poster(root, w, d, wall_side=-1, prefix="Bed")


def steamer_trunk(root, w=0.86, d=0.48, h=0.56, prefix="Trunk", body=None):
    """Flat-top steamer trunk: leather-covered body and lid, oak slats, brass corners and edge bindings,
    two leather straps with buckles, a lock hasp, leather end handles."""
    body = body or LEATHER
    lid_h = 0.15
    box(f"{prefix}_Body", (w - 0.01, d - 0.01, h - lid_h - 0.006), (0, 0, (h - lid_h - 0.006) / 2), body,
        bevel=0.006, parent=root)
    box(f"{prefix}_Lid", (w, d, lid_h), (0, 0, h - lid_h / 2), body, bevel=0.008, parent=root)
    for z_ in (0.1, 0.27):                                      # horizontal oak slats, front and back
        for sy in (-1, 1):
            box(f"{prefix}_Slat", (w - 0.1, 0.012, 0.045), (0, sy * (d / 2 - 0.0), z_), OAK, bevel=0.003,
                parent=root)
    for sx in (-1, 1):
        box(f"{prefix}_LidSlat", (0.045, d - 0.08, 0.012), (sx * 0.2, 0, h + 0.001), OAK, bevel=0.003, parent=root)
        for sy in (-1, 1):                                      # brass corner caps and vertical bindings
            for zc in (0.02, h - 0.02):
                box(f"{prefix}_Corner", (0.06, 0.06, 0.05), (sx * (w / 2 - 0.025), sy * (d / 2 - 0.025), zc), BRASS,
                    bevel=0.008, parent=root)
            box(f"{prefix}_Binding", (0.02, 0.02, h - 0.1), (sx * (w / 2 - 0.004), sy * (d / 2 - 0.004), h / 2),
                BRASS, bevel=0.003, parent=root)
        # leather straps over the lid and down the front, with brass buckles
        sx_ = sx * 0.26
        box(f"{prefix}_StrapTop", (0.045, d + 0.012, 0.006), (sx_, 0, h + 0.004), LEATHER_DK, bevel=0.002,
            parent=root)
        box(f"{prefix}_StrapFront", (0.045, 0.006, 0.3), (sx_, -d / 2 - 0.004, h - 0.15), LEATHER_DK, bevel=0.002,
            parent=root)
        box(f"{prefix}_Buckle", (0.06, 0.008, 0.05), (sx_, -d / 2 - 0.009, h - 0.18), BRASS, bevel=0.003,
            parent=root)
        # leather carrying handle on each end
        hp = [(sx * (w / 2 + 0.005), -0.08, h - 0.2), (sx * (w / 2 + 0.03), -0.06, h - 0.24),
              (sx * (w / 2 + 0.035), 0, h - 0.25), (sx * (w / 2 + 0.03), 0.06, h - 0.24),
              (sx * (w / 2 + 0.005), 0.08, h - 0.2)]
        tube(f"{prefix}_Handle", spline(hp, 4), 0.01, LEATHER_DK, segs=8, parent=root)
        box(f"{prefix}_HandleCap", (0.012, 0.03, 0.03), (sx * (w / 2 + 0.003), -0.08, h - 0.2), BRASS, bevel=0.003,
            parent=root)
        box(f"{prefix}_HandleCap", (0.012, 0.03, 0.03), (sx * (w / 2 + 0.003), 0.08, h - 0.2), BRASS, bevel=0.003,
            parent=root)
    box(f"{prefix}_Hasp", (0.07, 0.01, 0.09), (0, -d / 2 - 0.004, h - lid_h - 0.01), BRASS, bevel=0.004,
        parent=root)
    cyl(f"{prefix}_Keyhole", 0.006, 0.004, (0, -d / 2 - 0.01, h - lid_h - 0.02), INK, rot=(R(90), 0, 0), segs=10,
        bevel=0, parent=root)


def build_trunk():
    """Victorian flat-top steamer trunk (86 x 48 x 56 cm) at the foot of the bed. It opens your LinkedIn (CV)."""
    root, w, d, h = furniture_root("trunk")
    steamer_trunk(root, w, d, h)
    book("Trunk_Book", (0.04, 0.17, 0.24), (0.24, 0.07, h + 0.027), LEATHER_RED, parent=root,
         rot=(0, R(90), R(80)))
    # Engraved brass name plate on the lid, like a school trunk marked with its owner's name (your name again).
    box("Trunk_NamePlate", (0.23, 0.006, 0.056), (0, -d / 2 - 0.003, h - 0.058), BRASS, bevel=0.002, parent=root)
    for sx in (-1, 1):
        ball("Trunk_PlateRivet", 0.004, (sx * 0.1, -d / 2 - 0.0065, h - 0.058), BRASS, parent=root, segs=8)
    hook_text("name", 2, "YOUR NAME", 0.03, (0, -d / 2 - 0.0068, h - 0.058), material=mat("dark", 0.5,
              color="#2A1E16"), max_width=0.18, parent=root, depth=0.0012)
    # An open wand box: a lidded walnut box lined in velvet, with a carved wooden wand lying in it.
    wb = empty("WandBox", (-0.17, -0.07, h + 0.008), rot=(0, 0, R(6)), parent=root)
    bl, bw_, bh = 0.36, 0.085, 0.045
    box("WandBox_Base", (bl, bw_, bh), (0, 0, bh / 2), WOOD_DK, bevel=0.003, parent=wb)
    satin = M("cream", 0.4, "fabric", color=mix_hex(COLORS["cream"], "#FFFFFF", 0.3))   # pale satin lining
    box("WandBox_Lining", (bl - 0.02, bw_ - 0.02, 0.004), (0, 0, bh + 0.0005), satin, bevel=0.002, parent=wb)
    lid = empty("WandBox_Hinge", (0, bw_ / 2, bh), rot=(R(-105), 0, 0), parent=wb)  # opened back past upright
    box("WandBox_Lid", (bl, bw_, 0.012), (0, -bw_ / 2, 0.006), WOOD_DK, bevel=0.003, parent=lid)
    box("WandBox_LidLining", (bl - 0.02, bw_ - 0.02, 0.003), (0, -bw_ / 2, -0.0005), satin, bevel=0.001,
        parent=lid)
    wand = [(-0.155 + 0.31 * i / 10, 0.004 * math.sin(i * 0.9), bh + 0.012) for i in range(11)]
    tube("Wand_Shaft", wand, 0.0075, wood(0.6, along="X"), r2=0.0032, segs=10, parent=wb)
    for k, (xx, rr) in enumerate(((-0.15, 0.0095), (-0.128, 0.011), (-0.1, 0.0098), (-0.075, 0.0105))):
        ring("Wand_Carving", rr - 0.003, 0.0035, (xx, 0, bh + 0.012), WOOD_DK, rot=(0, R(90), 0), segs=12,
             parent=wb)
    ball("Wand_Pommel", 0.011, (-0.16, 0, bh + 0.012), WOOD_DK, scale=(0.8, 1, 1), parent=wb)
    hook_link(root, "linkedin")


def build_fireplace():
    """Tudor-arch stone surround (W130 cm, opening 86 x 82 cm, shelf 1.45 m), hearth slab, fire basket, logs,
    flames and andirons."""
    root, w, d, h = furniture_root("fireplace")
    yb = d / 2                                                   # the breast face
    sy = yb - 0.11                                               # centre of the surround's depth
    # Jambs on plinth blocks.
    for sx in (-1, 1):
        box("Fire_Plinth", (0.24, 0.24, 0.14), (sx * 0.55, sy, 0.07 + FLOOR_Z * 0), DRESSED, bevel=0.01, parent=root)
        box("Fire_Jamb", (0.2, 0.22, 0.72), (sx * 0.55, sy, 0.14 + 0.36), DRESSED, bevel=0.01, parent=root)
        box("Fire_JambBead", (0.025, 0.015, 0.7), (sx * 0.44, sy - 0.11, 0.5), DRESSED_DK, bevel=0.006,
            parent=root)
    # Four-centred (Tudor) arched lintel with carved roundels in the spandrels.
    arc = spline([(0.45, 0.86), (0.41, 0.94), (0.3, 1.0), (0.0, 1.03)], 5)
    outline = [(0.65, 1.22), (-0.65, 1.22), (-0.65, 0.86)] + [(-x, z) for x, z in arc] + \
              [(x, z) for x, z in reversed(arc[:-1])] + [(0.65, 0.86)]
    prism("Fire_Lintel", outline, 0.22, DRESSED, loc=(0, sy, 0), parent=root, bevel=0.008)
    for sx in (-1, 1):
        cyl("Fire_Roundel", 0.065, 0.02, (sx * 0.46, sy - 0.115, 1.1), DRESSED_DK, rot=(R(90), 0, 0), segs=24,
            bevel=0.006, parent=root)
        for k in range(4):                                       # four petals = a carved quatrefoil
            ang = R(45 + 90 * k)
            ball("Fire_Petal", 0.022, (sx * 0.46 + 0.026 * math.cos(ang), sy - 0.125, 1.1 + 0.026 * math.sin(ang)),
                 DRESSED, scale=(1, 0.4, 1), parent=root)
    # Frieze, moulding, corbels and the mantel shelf.
    box("Fire_Frieze", (1.3, 0.2, 0.14), (0, sy + 0.01, 1.29), DRESSED, bevel=0.006, parent=root)
    box("Fire_Moulding", (1.38, 0.24, 0.035), (0, sy - 0.005, 1.375), DRESSED_DK, bevel=0.01, parent=root)
    for sx in (-1, 1):
        box("Fire_Corbel", (0.1, 0.16, 0.12), (sx * 0.58, sy - 0.12, 1.3), DRESSED, bevel=0.012, parent=root)
    box("Fire_Shelf", (1.5, 0.3, 0.06), (0, sy - 0.03, 1.42), DRESSED, bevel=0.01, parent=root)
    # Hearth slab, cast-iron fire basket on legs, andirons, logs, embers and flames.
    box("Fire_Hearth", (1.5, 0.5, 0.04), (0, yb - 0.25, 0.02), DRESSED_DK, bevel=0.008,
        parent=root)
    bz = 0.14
    fy = yb + 0.18                                               # basket sits inside the opening
    box("Fire_BasketFloor", (0.56, 0.26, 0.012), (0, fy, bz), IRON, bevel=0.002, parent=root)
    boxes("Fire_BasketBars", [((0.012, 0.012, 0.16), (-0.27 + i * 0.054, fy - 0.13, bz + 0.08), (0, 0, 0))
                              for i in range(11)], IRON, bevel=0.002, parent=root)
    box("Fire_BasketRail", (0.58, 0.016, 0.016), (0, fy - 0.13, bz + 0.16), IRON, bevel=0.003, parent=root)
    for sx in (-1, 1):
        box("Fire_BasketLeg", (0.025, 0.025, bz), (sx * 0.26, fy - 0.11, bz / 2 + 0.04), IRON, bevel=0.003,
            parent=root)
        tube("Fire_Andiron", [(sx * 0.34, fy - 0.34, 0.04), (sx * 0.34, fy - 0.3, 0.2), (sx * 0.34, fy - 0.26, 0.34)],
             0.016, IRON, segs=10, parent=root)
        lathe("Fire_AndironKnob", [(0.0, 0), (0.03, 0.01), (0.035, 0.04), (0.02, 0.07), (0.0, 0.08)],
              (sx * 0.34, fy - 0.26, 0.33), BRASS, segs=16, parent=root)
        box("Fire_AndironFoot", (0.04, 0.16, 0.025), (sx * 0.34, fy - 0.34, 0.052), IRON, bevel=0.004, parent=root)
    bark = M("wood", 0.9, "wood", color=shade(COLORS["wood"], 0.55))
    fire_on = 1.0 if NIGHT else 0.45
    for i, (lx, ly, lz, rz, ry) in enumerate(((-0.06, fy, bz + 0.06, 8, 0), (0.07, fy + 0.03, bz + 0.06, -12, 0),
                                              (0.0, fy - 0.02, bz + 0.13, 70, 18))):
        cyl(f"Fire_Log_{i}", 0.045, 0.42, (lx, ly, lz), bark, rot=(R(ry), R(90), R(rz)), segs=14, bevel=0.01,
            parent=root)
    embers = glow("#FF6A1E", 6.0 * fire_on)
    for k in range(9):
        no_shadow(ball("Fire_Ember", random.uniform(0.02, 0.035),
                       (random.uniform(-0.2, 0.2), fy + random.uniform(-0.08, 0.08), bz + 0.025), embers,
                       scale=(1.2, 1, 0.5), parent=root))
    # Flames: orange outer tongues with a smaller yellow core in each, so the fire reads as fire, not white cones.
    for k, (fx, fz, s) in enumerate(((-0.08, 0.2, 1.0), (0.05, 0.22, 1.25), (0.13, 0.19, 0.8), (-0.15, 0.18, 0.7),
                                     (0.0, 0.24, 0.9), (0.19, 0.17, 0.55), (-0.21, 0.16, 0.5))):
        fh, fr = 0.28 * s * fire_on, 0.06 * s
        tilt = (R(random.uniform(-6, 6)), R(random.uniform(-10, 10)), 0)
        for part, (col, st, f_) in (("Outer", ("#FF6A14", 3.0, 1.0)), ("Core", ("#FFC24A", 4.0, 0.55))):
            ph, pr = fh * (f_ if part == "Core" else 1.0), fr * f_
            no_shadow(lathe(f"Fire_Flame{part}_{k}", [(0.0, 0), (pr * 0.8, ph * 0.12), (pr, ph * 0.3),
                                                       (pr * 0.55, ph * 0.65), (pr * 0.12, ph * 0.92), (0.0, ph)],
                            (fx, fy + 0.02 - (0.012 if part == "Core" else 0), bz + fz - 0.06),
                            glow(col, st), segs=12, parent=root, rot=tilt, scale=(1, 0.6, 1)))
    light("Light_Fire", "POINT", FIRE_STRENGTH * fire_on, kelvin(1900), (0, fy - 0.15, 0.4), size=0.25, parent=root)
    light("Light_FireSpill", "AREA", FIRE_STRENGTH * 0.6 * fire_on, kelvin(2000), (0, yb - 0.1, 0.5),
          aim=None, size=0.6, parent=root).rotation_euler = (R(-90), 0, 0)


def build_armchair():
    """Queen Anne-style wing chair (78 x 84 cm, 106 cm high): cabriole legs with pad feet, loose seat cushion,
    tall back, flared wings and rolled arms, in teal velvet."""
    root, w, d, h = furniture_root("armchair")
    fab, fab_lt = TEAL, cloth("accent_1", 1.15)
    leg = WOOD_DK_V
    for sx in (-1, 1):                                          # cabriole front legs, raked back legs
        x = sx * (w / 2 - 0.09)
        cab = spline([(x, -d / 2 + 0.12, 0.2), (x + sx * 0.012, -d / 2 + 0.09, 0.14), (x, -d / 2 + 0.1, 0.06),
                      (x - sx * 0.01, -d / 2 + 0.07, 0.015)], 5)
        tube("Armchair_LegFront", cab, 0.022, leg, segs=10, r2=0.014, parent=root)
        ball("Armchair_PadFoot", 0.024, (x - sx * 0.01, -d / 2 + 0.065, 0.012), leg, scale=(1, 1, 0.5), parent=root)
        tube("Armchair_LegBack", [(x, d / 2 - 0.14, 0.2), (x, d / 2 - 0.1, 0.1), (x, d / 2 - 0.06, 0.0)], 0.02, leg,
             segs=10, r2=0.015, parent=root)
    box("Armchair_Base", (w - 0.06, d - 0.18, 0.2), (0, -0.04, 0.29), fab, bevel=0.022, parent=root)
    box("Armchair_Cushion", (w - 0.28, d - 0.3, 0.1), (0, -0.1, 0.43), fab_lt, bevel=0.03, parent=root)
    box("Armchair_Piping", (w - 0.275, d - 0.295, 0.008), (0, -0.1, 0.43), fab, bevel=0.003, parent=root)
    for sx in (-1, 1):
        ax = sx * (w / 2 - 0.075)
        box("Armchair_ArmPanel", (0.12, d - 0.26, 0.3), (ax, -0.04, 0.46), fab, bevel=0.02, parent=root)
        cyl("Armchair_ArmRoll", 0.06, d - 0.26, (ax + sx * 0.012, -0.05, 0.62), fab, segs=24, bevel=0.012,
            rot=(R(90), 0, 0), parent=root)
        cyl("Armchair_ArmScroll", 0.062, 0.014, (ax + sx * 0.012, -d / 2 + 0.07, 0.62), fab_lt, segs=24,
            bevel=0.004, rot=(R(90), 0, 0), parent=root)
        wing = [(d / 2 - 0.1, 0.6), (d / 2 - 0.1, h - 0.03), (d / 2 - 0.24, h - 0.01), (d / 2 - 0.36, h - 0.06),
                (d / 2 - 0.44, h - 0.16), (d / 2 - 0.5, h - 0.3), (d / 2 - 0.52, 0.6)]
        bm = bmesh.new()
        face = bm.faces.new([bm.verts.new((-0.045, y, z)) for y, z in wing])
        ext = bmesh.ops.extrude_face_region(bm, geom=[face])
        bmesh.ops.translate(bm, vec=(0.09, 0, 0), verts=[v for v in ext["geom"] if isinstance(v, bmesh.types.BMVert)])
        bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
        wo = _finish(_obj("Armchair_Wing", bm), fab, 0.03, None, root)
        wo.location, wo.rotation_euler = (ax + sx * 0.01, 0, 0), (0, 0, R(-sx * 6))
    box("Armchair_Back", (w - 0.16, 0.14, 0.66), (0, d / 2 - 0.13, 0.74), fab, bevel=0.04, rot=(R(-8), 0, 0),
        parent=root)
    box("Armchair_BackCushion", (w - 0.3, 0.09, 0.48), (0, d / 2 - 0.23, 0.72), fab_lt, bevel=0.03,
        rot=(R(-10), 0, 0), parent=root)
    # A plum velvet cushion and an open book left on the seat arm.
    box("Armchair_Pillow", (0.3, 0.12, 0.24), (0.06, d / 2 - 0.33, 0.6), VELVET_LT, bevel=0.05, rot=(R(-20), 0, R(8)),
        parent=root)


def build_desk():
    """Victorian oak two-drawer writing table (100 x 55 cm, 75 cm high) with a leather inset, set out with a brass
    orrery (your website), quill and ink, a wax-seal kit and a letter rack (your email)."""
    root, w, d, h = furniture_root("desk")
    top_t = 0.022
    box("Desk_Top", (w, d, top_t), (0, 0, h - top_t / 2), WOOD, bevel=0.004, parent=root)
    box("Desk_Leather", (w - 0.12, d - 0.12, 0.002), (0, 0, h + 0.001), M("accent_1", 0.5, "leather",
        color=shade(COLORS["accent_1"], 0.7)), bevel=0, parent=root)
    for k in range(2):                                           # gilt tooling round the leather
        for sy in (-1, 1):
            box("Desk_Tooling", (w - 0.14 + 0.0 * k, 0.004, 0.0015), (0, sy * (d / 2 - 0.07), h + 0.0022), GILT,
                bevel=0, parent=root)
        for sx in (-1, 1):
            box("Desk_Tooling", (0.004, d - 0.14, 0.0015), (sx * (w / 2 - 0.07), 0, h + 0.0022), GILT, bevel=0,
                parent=root)
    box("Desk_Apron", (w - 0.1, d - 0.1, 0.12), (0, 0, h - top_t - 0.06), WOOD, bevel=0.003, parent=root)
    for sx in (-1, 1):                                           # two drawers with 3 mm gaps and brass knobs
        box("Desk_Drawer", (0.4, 0.012, 0.09), (sx * 0.215, -d / 2 + 0.046, h - top_t - 0.06), WOOD_DK,
            bevel=0.003, parent=root)
        lathe("Desk_Knob", [(0.008, 0), (0.008, 0.008), (0.014, 0.016), (0.012, 0.024), (0.0, 0.026)],
              (sx * 0.215, -d / 2 + 0.04, h - top_t - 0.06), BRASS, segs=12, parent=root, rot=(R(90), 0, 0))
        for sy in (-1, 1):                                       # turned legs
            lathe("Desk_Leg", [(0.022, 0), (0.026, 0.02), (0.018, 0.04), (0.02, 0.2), (0.026, 0.3), (0.017, 0.4),
                               (0.024, 0.5), (0.028, 0.53), (0.028, h - 0.15)],
                  (sx * (w / 2 - 0.07), sy * (d / 2 - 0.07), 0), WOOD_V, segs=16, parent=root)
    z = h + 0.002
    # Brass orrery on a turned base (your website): sun, planets on arms, a tilted ring, glowing motes.
    ox, oy = -w / 2 + 0.17, d / 2 - 0.17
    orr = empty("Orrery", (ox, oy, z), parent=root)
    lathe("Orrery_Base", [(0.09, 0), (0.095, 0.01), (0.08, 0.025), (0.05, 0.035), (0.0, 0.035)], (0, 0, 0), WOOD_DK,
          segs=28, parent=orr)
    lathe("Orrery_Column", [(0.012, 0), (0.012, 0.12), (0.02, 0.13), (0.008, 0.14)], (0, 0, 0.035), BRASS, segs=12,
          parent=orr)
    sun = ball("Orrery_Sun", 0.035, (0, 0, 0.2), glow(COLORS["accent_2"], 2.5 if NIGHT else 0.6), parent=orr)
    no_shadow(sun)
    for k, (rr, key, pr, ang) in enumerate(((0.07, "cream", 0.01, 30), (0.11, "accent_3", 0.014, 150),
                                            (0.15, "accent_1", 0.018, 260))):
        px_, py_ = rr * math.cos(R(ang)), rr * math.sin(R(ang))
        tube("Orrery_Arm", [(0, 0, 0.16), (px_, py_, 0.16), (px_, py_, 0.2 - 0.01 * k)], 0.002, BRASS, segs=6,
             parent=orr)
        ball("Orrery_Planet", pr, (px_, py_, 0.2 - 0.01 * k + pr), mat(key, 0.4), parent=orr)
    ring("Orrery_Ring", 0.13, 0.003, (0, 0, 0.2), BRASS, rot=(R(23), 0, 0), parent=orr)
    if NIGHT:
        for k in range(10):                                      # the only "magic": a few glowing motes
            a_ = random.uniform(0, 2 * math.pi)
            rr = random.uniform(0.08, 0.2)
            no_shadow(ball("Orrery_Mote", 0.004, (rr * math.cos(a_), rr * math.sin(a_), random.uniform(0.15, 0.32)),
                           glow(COLORS["accent_2"], 6.0), parent=orr, segs=8))
    hook_link(orr, "website")
    # Writing set: glass inkwell, quill, brass seal and two sticks of sealing wax, an open book.
    ix, iy = 0.1, d / 2 - 0.12
    lathe("Desk_Inkwell", [(0.03, 0), (0.032, 0.005), (0.032, 0.035), (0.016, 0.045), (0.012, 0.055),
                           (0.0, 0.055)], (ix, iy, z), mat("glass", 0.05, alpha=0.5), segs=20, parent=root)
    cyl("Desk_Ink", 0.026, 0.03, (ix, iy, z + 0.017), INK, segs=16, bevel=0, parent=root)
    quill = spline([(ix + 0.01, iy, z + 0.05), (ix + 0.05, iy + 0.03, z + 0.15), (ix + 0.07, iy + 0.06, z + 0.26)], 6)
    tube("Desk_QuillShaft", quill, 0.0025, mat("cream", 0.5), segs=6, parent=root)
    q0, q1 = Vector(quill[2]), Vector(quill[-1])              # the feather: a broad, flat vane along the shaft
    qd = q1 - q0
    ball("Desk_QuillVane", 0.017, tuple((q0 + q1) / 2 + qd * 0.08), mat("cream", 0.8, color=mix_hex(COLORS["cream"],
         "#B9AE9E", 0.35)), scale=(1.0, 0.16, (qd.length * 0.62) / 0.017), rot=tuple(qd.to_track_quat("Z", "Y").to_euler()),
         parent=root, segs=16)
    lathe("Desk_Seal", [(0.012, 0), (0.012, 0.01), (0.007, 0.02), (0.01, 0.06), (0.006, 0.075), (0.0, 0.078)],
          (ix + 0.1, iy - 0.02, z), WOOD_DK, segs=14, parent=root)
    for k in range(2):
        box("Desk_WaxStick", (0.1, 0.008, 0.008), (ix + 0.12, iy - 0.1 - k * 0.014, z + 0.004), SEAL_WAX, bevel=0.002,
            rot=(0, 0, R(10)), parent=root)
    bk = empty("Desk_OpenBook", (-0.08, -0.06, z), rot=(0, 0, R(-8)), parent=root)
    for sx in (-1, 1):
        box("Desk_BookCover", (0.16, 0.23, 0.006), (sx * 0.08, 0, 0.003), LEATHER_RED, bevel=0.002,
            rot=(0, R(sx * -4), 0), parent=bk)
        box("Desk_BookPages", (0.15, 0.22, 0.012), (sx * 0.078, 0, 0.011), PARCHMENT, bevel=0.003,
            rot=(0, R(sx * -6), 0), parent=bk)
        for ln in range(7):
            box("Desk_BookLine", (0.1, 0.004, 0.0008), (sx * 0.08, 0.08 - ln * 0.025, 0.0178), INK, bevel=0,
                parent=bk)
    # Letter rack with wax-sealed envelopes (your email).
    rx, ry = w / 2 - 0.15, d / 2 - 0.1
    rack = empty("Desk_LetterRack", (rx, ry, z), rot=(0, 0, R(-6)), parent=root)
    box("Rack_Base", (0.2, 0.09, 0.012), (0, 0, 0.006), OAK, bevel=0.003, parent=rack)
    for k, yy in enumerate((-0.03, 0.0, 0.03)):
        box("Rack_Divider", (0.2, 0.006, 0.05 + 0.03 * k), (0, yy - 0.012, 0.012 + (0.05 + 0.03 * k) / 2), OAK,
            bevel=0.002, parent=rack)
        env = box("Rack_Envelope", (0.16, 0.003, 0.1), (random.uniform(-0.01, 0.01), yy, 0.06 + 0.01 * k), PAPER,
                  bevel=0.001, rot=(R(-4), 0, R(random.uniform(-3, 3))), parent=rack)
        cyl("Rack_Seal", 0.011, 0.004, (0, yy - 0.003, 0.085 + 0.01 * k), SEAL_WAX, rot=(R(90), 0, 0), segs=14,
            bevel=0.001, parent=rack)
        env.name = f"Rack_Envelope_{k}"
    hook_link(rack, "email")
    # Brass chamberstick with a candle (lights the desk), and two books with ribbons.
    cs = empty("Desk_Chamberstick", (-w / 2 + 0.34, -d / 2 + 0.14, z), parent=root)
    lathe("Chamber_Pan", [(0.06, 0), (0.062, 0.008), (0.056, 0.014), (0.012, 0.012), (0.0, 0.012)], (0, 0, 0), BRASS,
          segs=24, parent=cs)
    lathe("Chamber_Socket", [(0.016, 0), (0.016, 0.04), (0.022, 0.046), (0.0, 0.046)], (0, 0, 0.012), BRASS, segs=16,
          parent=cs)
    tube("Chamber_Handle", spline([(0.055, 0, 0.012), (0.08, 0, 0.03), (0.07, 0, 0.055), (0.055, 0, 0.045)], 4),
         0.004, BRASS, segs=6, parent=cs)
    candle("Chamber_Candle", (0, 0, 0.05), h=0.12, r=0.012, parent=cs, light_w=LAMP_STRENGTH * 1.2)
    zb = z                                                       # a stack of three old spell books
    for k, (m_, t_, sz) in enumerate(((VELVET_DK, 0.05, 0.25), (LEATHER, 0.035, 0.23), (LEATHER_RED, 0.045, 0.21))):
        book(f"Desk_StackBook_{k}", (t_, sz * 0.68, sz), (w / 2 - 0.2, -d / 2 + 0.15, zb + t_ / 2),
             m_, parent=root, rot=(0, R(90), R(5 - 12 * k + 9 * (k == 2))))
        zb += t_


def build_chair():
    """English hoop-back Windsor chair (50 x 52 cm, 92 cm high, seat 45 cm): saddle seat, splayed turned legs with
    an H-stretcher, a steam-bent hoop and seven spindles."""
    root, w, d, h = furniture_root("chair")
    ch = WOOD_V
    seat = cyl("Chair_Seat", 0.22, 0.04, (0, 0, 0.43), WOOD, segs=32, bevel=0.012, parent=root)
    seat.scale = (1.0, 0.92, 1)
    legs = []
    for sx in (-1, 1):
        for sy in (-1, 1):
            top = Vector((sx * 0.15, sy * 0.13, 0.41))
            foot = Vector((sx * 0.21, sy * 0.2, 0.0))
            tube("Chair_Leg", [foot, (foot + top) / 2, top], 0.016, ch, segs=10, r2=0.019, parent=root)
            legs.append((foot, top))
    for sx in (-1, 1):                                            # H-stretcher
        a_ = legs[(0 if sx < 0 else 2)]
        b_ = legs[(1 if sx < 0 else 3)]
        pa, pb = a_[0].lerp(a_[1], 0.35), b_[0].lerp(b_[1], 0.35)
        tube("Chair_SideStretcher", [pa, pb], 0.011, ch, segs=8, parent=root)
    tube("Chair_CrossStretcher", [Vector((-0.17, 0, 0.14)), Vector((0.17, 0, 0.14))], 0.011, ch, segs=8, parent=root)
    hoop = [(0.17 * math.cos(R(t)), 0.15 + 0.08 * math.sin(R(t)), 0.45 + 0.47 * math.sin(R(t)))
            for t in [i * 180 / 24 for i in range(25)]]
    tube("Chair_Hoop", hoop, 0.014, ch, segs=10, parent=root)
    for k in range(7):
        x = -0.12 + k * 0.04
        zt = 0.45 + 0.47 * math.sqrt(max(0.0, 1 - (x / 0.17) ** 2)) - 0.01
        tube("Chair_Spindle", [(x, 0.15, 0.45), (x, 0.15 + 0.08 * (zt - 0.45) / 0.47, zt)], 0.0065, ch, segs=6,
             parent=root)


def build_bookcase():
    """Narrow open bookcase in stained walnut (62 x 32 x 175 cm, 18 mm shelves) with a plinth and cornice,
    filled with leather-bound books with raised gilt bands. It opens your GitHub."""
    root, w, d, h = furniture_root("bookcase")
    t = 0.018
    for sx in (-1, 1):
        box("Bookcase_Side", (t, d - 0.02, h - 0.1), (sx * (w / 2 - t / 2 - 0.01), 0.0, (h - 0.1) / 2 + 0.07),
            WOOD_V, bevel=0.003, parent=root)
    box("Bookcase_Plinth", (w - 0.02, d - 0.03, 0.08), (0, -0.005, 0.04), WOOD_DK, bevel=0.004, parent=root)
    box("Bookcase_Back", (w - 0.04, 0.008, h - 0.12), (0, d / 2 - 0.016, h / 2), WOOD_DK, bevel=0, parent=root)
    box("Bookcase_Cornice", (w + 0.04, d + 0.02, 0.05), (0, -0.01, h - 0.025), WOOD, bevel=0.006, parent=root)
    box("Bookcase_CorniceBead", (w + 0.0, d - 0.01, 0.025), (0, -0.01, h - 0.062), WOOD_DK, bevel=0.006,
        parent=root)
    shelves = [0.08, 0.42, 0.76, 1.1, 1.42]
    for z0 in shelves:
        box("Bookcase_Shelf", (w - 0.05, d - 0.04, t), (0, 0.0, z0 + t / 2), WOOD, bevel=0.002, parent=root)
    keys = [VELVET_DK, LEATHER, LEATHER_RED, cloth("accent_1", 0.75, kind="leather"), LEATHER_DK,
            M("plant", 0.55, "leather", color=shade(COLORS["plant"], 0.75)), cloth("cream", 0.85, kind="leather")]
    rnd = random.Random(SEED + 9)
    for si, z0 in enumerate(shelves[:-1]):
        gap = (shelves[si + 1] - z0) - t - 0.02
        x = -w / 2 + 0.04
        while x < w / 2 - 0.09:
            tk = rnd.uniform(0.025, 0.055)
            hh = min(gap, rnd.uniform(0.2, 0.3))
            if rnd.random() < 0.1 and x < w / 2 - 0.2:          # one leaning book
                book("Bookcase_Book", (tk, 0.18, hh), (x + 0.06, -0.02, z0 + t), rnd.choice(keys), parent=root,
                     rot=(0, R(-18), 0))
                x += 0.12
                continue
            book("Bookcase_Book", (tk, rnd.uniform(0.15, 0.2), hh), (x + tk / 2, -0.02, z0 + t), rnd.choice(keys),
                 parent=root)
            if rnd.random() < 0.25:                              # silk ribbon bookmark hanging out
                box("Bookcase_Ribbon", (0.006, 0.002, 0.06), (x + tk / 2, -0.115, z0 + t + 0.02),
                    mat("accent_2", 0.5), bevel=0, parent=root)
            x += tk + 0.002
    # On top: a small stack of books and a glass specimen jar.
    book("Bookcase_TopBook", (0.04, 0.2, 0.26), (-0.1, 0, h + 0.02), LEATHER_RED, parent=root, rot=(0, R(90), R(4)))
    book("Bookcase_TopBook", (0.035, 0.18, 0.22), (-0.1, 0, h + 0.058), VELVET_DK, parent=root, rot=(0, R(90), R(-6)))
    candlestick("Bookcase_Candle", (0.16, -0.02, h), parent=root, h=0.16, light_w=LAMP_STRENGTH)
    hook_link(root, "github")


def build_pet():
    """Barn owl (Tyto alba, 34 cm) in a brass domed bird cage (dia 44 cm) hanging from a wrought-iron cage stand
    (1.9 m, tripod feet, shepherd's-crook top), by the window: heart-shaped white face, dark eyes, buff-gold back
    with grey mottling, white front. The cage door stands open."""
    root, w, d, h = furniture_root("pet")
    # The stand: a turned pole on three scrolled feet, curving over at the top into a crook that holds the cage.
    sx0, sy0 = 0.15, 0.06
    for k in range(3):
        a = R(90 + 120 * k)
        c, s_ = math.cos(a), math.sin(a)
        tube("CageStand_Foot", spline([(sx0, sy0, 0.3), (sx0 + 0.11 * c, sy0 + 0.11 * s_, 0.12),
                                       (sx0 + 0.21 * c, sy0 + 0.21 * s_, 0.02), (sx0 + 0.26 * c, sy0 + 0.26 * s_,
                                       0.035)], 5), 0.012, IRON, segs=8, parent=root)
        ball("CageStand_Toe", 0.016, (sx0 + 0.26 * c, sy0 + 0.26 * s_, 0.035), BRASS, parent=root, segs=10)
    lathe("CageStand_Pole", [(0.022, 0.28), (0.03, 0.32), (0.016, 0.36), (0.014, 1.0), (0.022, 1.03), (0.014, 1.06),
                             (0.013, 1.86)], (sx0, sy0, 0), IRON, segs=12, parent=root)
    cz = 1.08                                                    # bottom of the cage
    hook_x, hook_y = -0.02, -0.01
    tube("CageStand_Crook", spline([(sx0, sy0, 1.84), (sx0 - 0.02, sy0 - 0.01, 1.93), (0.06, 0.02, 1.96),
                                    (hook_x, hook_y, 1.9), (hook_x, hook_y, 1.84)], 6), 0.011, IRON, segs=8,
         parent=root)
    ball("CageStand_Finial", 0.022, (sx0 + 0.005, sy0, 1.95), BRASS, parent=root)
    # The cage: a brass tray with a skirt, upright wires, three hoops, a bell dome of curved wires and a ring.
    ce = empty("Cage", (hook_x, hook_y, cz), parent=root)
    cr, ch, dh = 0.2, 0.4, 0.22                                   # radius, wall height, dome height
    lathe("Cage_Tray", [(0.0, -0.04), (0.2, -0.04), (0.225, -0.03), (0.225, 0.0), (0.21, 0.012), (0.0, 0.012)],
          (0, 0, 0), BRASS, segs=40, parent=ce)
    for zz in (0.012, 0.13, ch):
        ring("Cage_Hoop", cr, 0.004, (0, 0, zz), BRASS, segs=40, parent=ce)
    door_a, door_w = -90.0, 26.0                                 # the door is at the front (local -y)
    door_z0, door_z1 = 0.02, 0.22
    for k in range(28):
        a_deg = 360 * k / 28
        a = R(a_deg)
        c, s_ = math.cos(a), math.sin(a)
        if abs(((a_deg - door_a + 180) % 360) - 180) < door_w / 2:
            tube("Cage_Wire", [(cr * c, cr * s_, door_z1), (cr * c, cr * s_, ch)], 0.0028, BRASS, segs=5, parent=ce)
        else:
            tube("Cage_Wire", [(cr * c, cr * s_, 0.012), (cr * c, cr * s_, ch)], 0.0028, BRASS, segs=5, parent=ce)
        if k % 2 == 0:                                           # every other wire carries on up the dome
            dome = [(cr * math.cos(R(t)) * c, cr * math.cos(R(t)) * s_, ch + dh * math.sin(R(t)) ** 0.8)
                    for t in range(0, 91, 10)]
            tube("Cage_DomeWire", dome, 0.003, BRASS, segs=5, parent=ce)
    ring("Cage_DomeHoop", cr * 0.62, 0.0035, (0, 0, ch + dh * 0.82), BRASS, segs=32, parent=ce)
    lathe("Cage_Cap", [(0.0, 0), (0.035, 0), (0.03, 0.02), (0.012, 0.035), (0.0, 0.04)], (0, 0, ch + dh - 0.005),
          BRASS, segs=20, parent=ce)
    ring("Cage_HangRing", 0.022, 0.004, (0, 0, ch + dh + 0.06), BRASS, rot=(R(90), 0, 0), segs=16, parent=ce)
    tube("Cage_Hanger", [(0, 0, ch + dh + 0.03), (0, 0, ch + dh + 0.045)], 0.004, BRASS, segs=6, parent=ce)
    # The open door: a small hinged frame of wires swung out to the side.
    door = empty("Cage_Door", (cr * math.cos(R(door_a - door_w / 2)), cr * math.sin(R(door_a - door_w / 2)), 0),
                 rot=(0, 0, R(door_a - 90 - 70)), parent=ce)
    dw = 2 * cr * math.sin(R(door_w / 2))
    for zz in (door_z0, door_z1):
        tube("Cage_DoorRail", [(0, 0, zz), (dw, 0, zz)], 0.003, BRASS, segs=5, parent=door)
    for k in range(4):
        tube("Cage_DoorWire", [(dw * k / 3, 0, door_z0), (dw * k / 3, 0, door_z1)], 0.0026, BRASS, segs=5,
             parent=door)
    cyl("Cage_Perch", 0.009, 2 * cr - 0.02, (0, 0.05, 0.13), WOOD, rot=(0, R(90), 0), segs=10, parent=ce)
    lathe("Cage_SeedCup", [(0.0, 0), (0.03, 0), (0.035, 0.03), (0.03, 0.03), (0.026, 0.006), (0.0, 0.006)],
          (0.12, 0.08, 0.012), mat("cream", 0.3, color=mix_hex(COLORS["cream"], "#FFFFFF", 0.4)), segs=16, parent=ce)
    owl = empty("Owl", (0.0, 0.04, 0.138), rot=(0, 0, R(35)), parent=ce)     # turned to look at you
    owl.scale = (0.96, 0.96, 0.96)
    buff = M("owl", 0.8, "knit", scale=0.6)
    white = M("owl_face", 0.85, "knit", scale=0.6)
    grey = mat("owl", 0.8, color=mix_hex(COLORS["owl"], "#7F7F86", 0.6))
    ball("Owl_Body", 0.1, (0, 0.01, 0.13), white, scale=(0.95, 0.85, 1.35), parent=owl)
    for sx in (-1, 1):                                           # folded wings over the sides and back
        ball("Owl_Wing", 0.1, (sx * 0.045, 0.03, 0.14), buff, scale=(0.5, 0.95, 1.3), rot=(R(-8), 0, R(sx * 6)),
             parent=owl)
    ball("Owl_Back", 0.1, (0, 0.045, 0.16), buff, scale=(0.85, 0.6, 1.2), parent=owl)
    ball("Owl_Head", 0.075, (0, 0.0, 0.28), buff, scale=(1.05, 0.95, 0.92), parent=owl)
    for sx in (-1, 1):                                           # heart-shaped facial disc = two lobes
        ball("Owl_Face", 0.045, (sx * 0.026, -0.05, 0.285), white, scale=(0.95, 0.35, 1.15), rot=(0, R(-sx * 12), 0),
             parent=owl)
        ball("Owl_Eye", 0.011, (sx * 0.024, -0.066, 0.292), INK, parent=owl)
        ball("Owl_EyeGlint", 0.0025, (sx * 0.021, -0.076, 0.296), mat("cream", 0.2, emit=1.0), parent=owl)
        ball("Owl_Rim", 0.047, (sx * 0.027, -0.045, 0.287), mat("owl", 0.8, color=shade(COLORS["owl"], 0.85)),
             scale=(1.0, 0.3, 1.2), rot=(0, R(-sx * 12), 0), parent=owl)
    lathe("Owl_Beak", [(0.007, 0), (0.005, 0.012), (0.0, 0.02)], (0, -0.07, 0.265), mat("owl_face", 0.5,
          color=mix_hex(COLORS["owl_face"], "#D9B98A", 0.6)), segs=8, rot=(R(160), 0, 0), parent=owl)
    for k in range(16):                                          # grey and dark mottling on the back
        a_ = random.uniform(-1.2, 1.2)
        ball("Owl_Spot", 0.006, (0.09 * math.sin(a_), 0.04 + 0.06 * math.cos(a_), random.uniform(0.1, 0.3)), grey,
             scale=(1, 0.4, 1), parent=owl)
    for sx in (-1, 1):
        for k in range(3):
            tube("Owl_Toe", [(sx * 0.03, -0.0, 0.0), (sx * 0.03 + (k - 1) * 0.012, -0.03, -0.018)], 0.004,
                 mat("owl_face", 0.6, color="#8A7A70"), segs=5, parent=owl)
    ball("Owl_Tail", 0.04, (0, 0.07, 0.03), buff, scale=(1.0, 0.6, 1.2), rot=(R(30), 0, 0), parent=owl)


def build_rug():
    """Round wool rug (dia 190 cm): teal border with a row of small diamonds, plum field, eight-point star."""
    root, w, d, h = furniture_root("rug")
    r = w / 2
    cyl("Rug_Border", r, h * 0.6, (0, 0, h * 0.3), cloth("accent_1", 0.9), segs=72, bevel=0.002, parent=root)
    cyl("Rug_Field", r - 0.13, h * 0.2, (0, 0, h * 0.7), VELVET, segs=72, bevel=0, parent=root)
    cyl("Rug_Line", r - 0.1, h * 0.15, (0, 0, h * 0.62), GOLD_CLOTH, segs=72, bevel=0, parent=root)
    n = 28
    boxes("Rug_Diamonds", [((0.045, 0.045, h * 0.2), (math.cos(2 * math.pi * k / n) * (r - 0.055),
                            math.sin(2 * math.pi * k / n) * (r - 0.055), h * 0.65), (0, 0, 2 * math.pi * k / n + R(45)))
                           for k in range(n)], cloth("cream", 0.95), bevel=0, parent=root)
    for k, (sz, m_) in enumerate(((0.62, GOLD_CLOTH), (0.42, cloth("accent_1", 0.9)), (0.24, cloth("cream", 0.95)))):
        for rot_ in (0, 45):
            box("Rug_Star", (sz, sz, h * 0.15), (0, 0, h * (0.8 + 0.1 * k)), m_, bevel=0, rot=(0, 0, R(rot_)),
                parent=root)


PLACEHOLDERS = {
    "fireplace": build_fireplace, "bed": build_bed, "trunk": build_trunk, "armchair": build_armchair,
    "desk": build_desk, "chair": build_chair, "bookcase": build_bookcase, "pet": build_pet, "rug": build_rug,
}

if SHOW_PLACEHOLDER_FURNITURE:
    for slot_name, build in PLACEHOLDERS.items():
        build()

# The second bed and trunk across the room (the dorm is shared). It stands out in the room on the open, cut-away side,
# so every curtain is tied back to its post and the tester rails sit low in the picture, clear of the writing desk.
BED2_XY, BED2_TURN, TRUNK_OFF = (4.4, 2.0), -30.0, 0.26
bed2 = empty("Bed2", (BED2_XY[0], BED2_XY[1], FLOOR_Z), rot=(0, 0, R(BED2_TURN)))
four_poster(bed2, wall_side=1, prefix="Bed2", tie_all=True, pelmet_sides=(0, 2))


def loft(name, rings, material, parent=None, caps=(True, True), smooth=True):
    """Skin through rings of points (each ring the same length, closed loops): garments, cowls, sacks."""
    bm = bmesh.new()
    vs = [[bm.verts.new(p) for p in r] for r in rings]
    n = len(vs[0])
    for A, B in zip(vs, vs[1:]):
        for i in range(n):
            bm.faces.new((A[i], A[(i + 1) % n], B[(i + 1) % n], B[i]))
    if caps[0]:
        bm.faces.new(list(reversed(vs[0])))
    if caps[1]:
        bm.faces.new(vs[-1])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    o = _obj(name, bm)
    o.data.materials.append(material)
    o.data.polygons.foreach_set("use_smooth", [smooth] * len(o.data.polygons))
    COL_ROOM.objects.link(o)
    o.parent = parent
    return o


def striped_scarf(name, path, side, width, parent, mats, stripe=0.075, thick=0.012):
    """Hand-knitted scarf: a flat band laid along `path` (its width along the unit vector `side`), in broad
    alternating stripes, with a tassel fringe at both ends."""
    pts = spline(path, 10)
    dense = [Vector(pts[0])]
    for a, b in zip(pts, pts[1:]):                               # resample every ~1 cm so stripes stay crisp
        a, b = Vector(a), Vector(b)
        k = max(1, int((b - a).length / 0.01))
        dense += [a.lerp(b, (i + 1) / k) for i in range(k)]
    side = Vector(side).normalized()
    bm, rows, s_acc = bmesh.new(), [], [0.0]
    for i, p in enumerate(dense):
        t = (dense[min(i + 1, len(dense) - 1)] - dense[max(i - 1, 0)]).normalized()
        nrm = t.cross(side).normalized()
        rows.append([bm.verts.new(p + side * (sx * width / 2) + nrm * (sz * thick / 2))
                     for sx, sz in ((-1, -1), (1, -1), (1, 1), (-1, 1))])
        if i:
            s_acc.append(s_acc[-1] + (p - dense[i - 1]).length)
    for i, (A, B) in enumerate(zip(rows, rows[1:])):
        mi = int(((s_acc[i] + s_acc[i + 1]) / 2) / stripe) % len(mats)
        for k in range(4):
            bm.faces.new((A[k], B[k], B[(k + 1) % 4], A[(k + 1) % 4])).material_index = mi
    bm.faces.new(list(reversed(rows[0])))
    bm.faces.new(rows[-1])
    mesh_from(name, bm, mats, smooth=False, parent=parent)
    for end, sgn in ((0, -1), (len(dense) - 1, 1)):              # fringe: little tassels carrying on past each end
        t = (dense[end] - dense[end - sgn]).normalized() * sgn if end else (dense[0] - dense[1]).normalized()
        for k in range(7):
            p0 = dense[end] + side * ((k - 3) / 3 * width * 0.42)
            tube(f"{name}_Fringe", [p0, p0 + t * 0.05 + Vector((0, 0, -0.012 if t.z > -0.5 else 0))], 0.0035,
                 mats[k % 2], segs=5, parent=parent)


# A knitted scarf flung across the second bed: an oatmeal ground with narrow teal and rust stripes (a three-colour
# pattern on purpose, so it never reads as a two-colour "school" scarf, and it stands out against the plum quilt).
_oat = M("cream", 0.96, "knit", scale=0.8, color=mix_hex(COLORS["cream"], "#C9B79A", 0.35))
SCARF = [_oat, M("accent_1", 0.95, "knit", scale=0.8, color=shade(COLORS["accent_1"], 1.05)), _oat,
         M("accent_3", 0.95, "knit", scale=0.8, color=shade(COLORS["accent_3"], 1.05))]
striped_scarf("Bed2_Scarf", [(-0.3, -0.22, 0.596), (0.05, -0.3, 0.597), (0.36, -0.36, 0.597), (0.5, -0.39, 0.58),
                             (0.54, -0.4, 0.5), (0.548, -0.41, 0.36), (0.55, -0.42, 0.24)], (0, 1, 0), 0.15, bed2,
              SCARF, stripe=0.05)
_f2 = Vector((BED2_XY[0], BED2_XY[1], 0)) + Vector((math.sin(R(BED2_TURN)), -math.cos(R(BED2_TURN)), 0)) * (1.05 + TRUNK_OFF)
_f2 -= Vector((math.cos(R(BED2_TURN)), math.sin(R(BED2_TURN)), 0)) * 0.07   # a little in from the wall kerb
trunk2 = empty("Trunk2", (_f2.x, _f2.y, FLOOR_Z), rot=(0, 0, R(BED2_TURN)))
steamer_trunk(trunk2, prefix="Trunk2", body=M("accent_1", 0.55, "leather", color=shade(COLORS["accent_1"], 0.7)))


def chess_set(name, loc, parent, rot=0.0):
    """Folding wooden chess board (30 cm, 8 x 8 squares) with a game in progress: turned bone and ebony pieces."""
    e = empty(name, loc, rot=(0, 0, R(rot)), parent=parent)
    sq, n = 0.034, 8
    box(f"{name}_Board", (sq * n + 0.03, sq * n + 0.03, 0.018), (0, 0, 0.009), WOOD_DK, bevel=0.003, parent=e)
    light_sq, dark_sq = [], []
    for i in range(n):
        for j in range(n):
            ((light_sq if (i + j) % 2 else dark_sq)).append(((sq, sq, 0.002), ((i - 3.5) * sq, (j - 3.5) * sq, 0.019),
                                                             (0, 0, 0)))
    boxes(f"{name}_LightSq", light_sq, M("cream", 0.5, "wood", color=mix_hex(COLORS["cream"], "#C9A878", 0.4)),
          bevel=0, parent=e)
    boxes(f"{name}_DarkSq", dark_sq, WOOD, bevel=0, parent=e)
    bone, ebony = mat("cream", 0.35, color=mix_hex(COLORS["cream"], "#E8DCC0", 0.5)), mat("dark", 0.3,
                                                                                        color="#1C1618")
    pawn = [(0.011, 0), (0.011, 0.004), (0.006, 0.008), (0.004, 0.018), (0.007, 0.02), (0.006, 0.026),
            (0.0, 0.032)]
    rook = [(0.012, 0), (0.012, 0.005), (0.008, 0.01), (0.007, 0.03), (0.01, 0.033), (0.01, 0.041), (0.0, 0.041)]
    king = [(0.013, 0), (0.013, 0.005), (0.008, 0.012), (0.006, 0.04), (0.01, 0.044), (0.007, 0.05), (0.0, 0.058)]
    queen = [(0.013, 0), (0.013, 0.005), (0.008, 0.012), (0.006, 0.036), (0.011, 0.042), (0.004, 0.05), (0.0, 0.052)]
    bishop = [(0.011, 0), (0.011, 0.004), (0.007, 0.01), (0.005, 0.03), (0.008, 0.034), (0.005, 0.044), (0.0, 0.048)]
    layout = [(pawn, 0, 1), (pawn, 2, 2), (pawn, 3, 3), (pawn, 5, 1), (rook, 0, 0), (king, 4, 0), (bishop, 2, 4),
              (pawn, 4, 4), (pawn, 1, 6), (pawn, 6, 5), (queen, 3, 7), (rook, 7, 7), (king, 6, 7), (bishop, 5, 6)]
    for k, (prof_, i, j) in enumerate(layout):
        lathe(f"{name}_Piece", prof_, ((i - 3.5) * sq, (j - 3.5) * sq, 0.02), bone if j < 4 else ebony, segs=14,
              parent=e)
    lathe(f"{name}_Taken", pawn, (sq * 4.7, -0.05, 0.0), ebony, segs=14, parent=e, rot=(0, R(90), R(30)))
    return e


def scroll(name, loc, parent, length=0.22, r=0.017, rot=(0, 0, 0)):
    """Rolled parchment scroll tied with a ribbon and closed with a red wax seal on a tag."""
    e = empty(name, loc, rot=rot, parent=parent)
    cyl(f"{name}_Roll", r, length, (0, 0, 0), PARCHMENT, rot=(0, R(90), 0), segs=18, bevel=0.003, parent=e)
    for sx in (-1, 1):                                           # the curled outer edge shows at each end
        ring(f"{name}_Curl", r * 0.7, r * 0.32, (sx * length / 2, 0, 0), PARCHMENT, rot=(0, R(90), 0), segs=16,
             parent=e)
    ring(f"{name}_Ribbon", r + 0.0015, 0.0022, (0.02, 0, 0), mat("accent_3", 0.5), rot=(0, R(90), 0), segs=18,
         parent=e)
    cyl(f"{name}_Seal", 0.012, 0.004, (0.02, -r - 0.012, -r * 0.4), SEAL_WAX, rot=(R(80), 0, 0), segs=14,
        bevel=0.0015, parent=e)
    return e


chess_set("Trunk2_Chess", (-0.17, 0.0, 0.562), trunk2, rot=6)
if NIGHT:                                    # sealed scrolls on the lid (autumn: a bowl of apples instead)
    for k, (yy, zz, rz) in enumerate(((-0.06, 0.017, 8), (0.05, 0.017, -4), (-0.005, 0.047, 2))):
        scroll(f"Trunk2_Scroll_{k}", (0.23, yy, 0.562 + zz), trunk2, length=0.24 - 0.02 * k, rot=(0, 0, R(rz)))


def cauldron(name, loc, parent):
    """Pewter-grey cast cauldron (dia 42 cm) on a three-legged iron trivet, with a faint glow over the brew."""
    e = empty(name, loc, parent=parent)
    pewter = M("pewter", 0.42, "brushed", metal=0.75, scale=0.6)
    ring(f"{name}_TrivetRing", 0.16, 0.012, (0, 0, 0.16), IRON, segs=36, parent=e)
    for k in range(3):                                           # trivet legs with little scrolled feet
        a = R(270 + 120 * k)
        c, s_ = math.cos(a), math.sin(a)
        tube(f"{name}_TrivetLeg", spline([(0.16 * c, 0.16 * s_, 0.16), (0.19 * c, 0.19 * s_, 0.07),
                                          (0.215 * c, 0.215 * s_, 0.015), (0.24 * c, 0.24 * s_, 0.012)], 4), 0.011,
             IRON, segs=8, parent=e)
    lathe(f"{name}_Body", [(0.0, 0.0), (0.08, 0.0), (0.14, 0.025), (0.185, 0.07), (0.205, 0.13), (0.198, 0.2),
                           (0.175, 0.245), (0.165, 0.262), (0.18, 0.272), (0.183, 0.29), (0.165, 0.292),
                           (0.155, 0.27), (0.152, 0.25), (0.0, 0.25)], (0, 0, 0.11), pewter, segs=40, parent=e)
    for sx in (-1, 1):                                           # lugs and a bail handle folded back
        ring(f"{name}_Lug", 0.016, 0.006, (sx * 0.19, 0, 0.36), IRON, rot=(R(90), 0, 0), segs=12, parent=e)
    tube(f"{name}_Bail", [(0.19 * math.cos(R(t)), -0.2 * math.sin(R(t)) * 0.45, 0.36 + 0.2 * math.sin(R(t)) * 0.9)
                          for t in range(0, 181, 12)], 0.006, IRON, segs=8, parent=e)
    brew = glow(COLORS["brew"], 1.6 if NIGHT else 0.5)
    no_shadow(cyl(f"{name}_Brew", 0.152, 0.004, (0, 0, 0.364), brew, segs=36, bevel=0, parent=e))
    rnd = random.Random(SEED + 51)
    for k in range(7):                                           # bubbles breaking on the surface
        a, rr = rnd.uniform(0, 2 * math.pi), rnd.uniform(0.0, 0.12)
        no_shadow(ball(f"{name}_Bubble", rnd.uniform(0.008, 0.018), (rr * math.cos(a), rr * math.sin(a), 0.368),
                       glow(mix_hex(COLORS["brew"], "#FFFFFF", 0.4), 2.0 if NIGHT else 0.7), scale=(1, 1, 0.55),
                       parent=e, segs=10))
    steam = mat("cream", 0.9, emit=0.3 if NIGHT else 0.12, color=mix_hex(COLORS["brew"], "#FFFFFF", 0.7), alpha=0.1)
    wisp = spline([(0.0, 0.0, 0.38), (0.04, 0.01, 0.48), (-0.02, 0.0, 0.6), (0.03, -0.01, 0.72)], 6)
    no_shadow(tube(f"{name}_Steam", wisp, 0.05, steam, r2=0.015, segs=12, parent=e))
    paddle = spline([(0.05, 0.03, 0.3), (0.12, 0.06, 0.45), (0.2, 0.09, 0.62)], 4)
    tube(f"{name}_Paddle", paddle, 0.011, wood(1.2, along="Z"), segs=8, parent=e)
    light(f"Light_{name}", "POINT", 6 if NIGHT else 1.5, lin(COLORS["brew"]), (0, 0, 0.5), size=0.15, parent=e)
    return e


fire_root = next(o for o in COL_FURN.objects if o.get("kit_slot") == "fireplace")
cauldron("Cauldron", (0.72, -0.56, 0.0), fire_root)

# A traditional besom resting on two forged-iron wall hooks above the first bed. The hooks stand well off the curved
# wall so the straight broom clears the stones along its whole length.
PEG_A, PEG_Z, PEG_L = (186.0, 196.0), 2.38, 0.2     # just above the tester, the twig head under the round window
pegs = [P(RI - PEG_L, a_, PEG_Z) for a_ in PEG_A]
for i, a_ in enumerate(PEG_A):
    pf = at_wall(f"BroomHook_{i}", a_, r=RI - 0.004, z=PEG_Z)
    box(f"BroomHook_{i}_Plate", (0.05, 0.012, 0.11), (0, -0.006, -0.01), IRON, bevel=0.003, parent=pf)
    tube(f"BroomHook_{i}_Arm", spline([(0, -0.01, 0.0), (0, -0.1, -0.012), (0, -PEG_L, -0.02),
                                       (0, -PEG_L - 0.025, 0.02), (0, -PEG_L - 0.02, 0.045)], 5), 0.008, IRON,
         segs=8, parent=pf)
    ball(f"BroomHook_{i}_Knob", 0.012, (0, -PEG_L - 0.02, 0.048), IRON, parent=pf)
mid = (pegs[0] + pegs[1]) / 2
axis = (pegs[0] - pegs[1]).normalized()                         # twig head towards the round window
broom = empty("Besom", (mid.x, mid.y, PEG_Z + 0.006), rot=tuple(axis.to_track_quat("Z", "Y").to_euler()))
handle_wood = M("wood", 0.6, "wood", along="Z", color=mix_hex(COLORS["wood"], "#A88A62", 0.5))
cyl("Besom_Handle", 0.018, 0.9, (0, 0, -0.145), handle_wood, segs=12, parent=broom)      # -0.595 .. +0.305
lathe("Besom_Head", [(0.0, 0.27), (0.026, 0.27), (0.045, 0.33), (0.085, 0.5), (0.096, 0.62), (0.075, 0.67),
                     (0.0, 0.67)], (0, 0, 0), TWIGS, segs=20, parent=broom)
rnd_b = random.Random(SEED + 61)
for k in range(16):                                              # loose twig ends splaying from the bundle
    a_ = 2 * math.pi * k / 16 + rnd_b.uniform(-0.1, 0.1)
    r0, r1 = 0.075, 0.1 + rnd_b.uniform(0, 0.01)
    tube("Besom_Twig", [(r0 * math.cos(a_), r0 * math.sin(a_), 0.6), (r1 * math.cos(a_), r1 * math.sin(a_),
                        0.68 + rnd_b.uniform(0, 0.02))], 0.0035, TWIGS, segs=4, parent=broom)
for zb, rb in ((0.3, 0.032), (0.37, 0.05)):
    ring("Besom_Binding", rb, 0.006, (0, 0, zb), mat("wood", 0.8, color="#6E5A3C"), parent=broom)


def robe(name, loc, face, parent=None, length=1.25):
    """Plain black hooded school robe hanging from a coat hook by its collar loop: a full gathered body with soft
    folds, wide bell sleeves and the hood bunched over the hook. face = the direction (degrees) its front looks."""
    e = empty(name, loc, rot=(0, 0, R(face + 90)), parent=parent)   # local -y = the front
    rnd = random.Random(sum(map(ord, name)) + SEED)
    fab = cloth("robe", kind="fabric", rough=0.92)
    rings = []
    for z, hw, hd, yo in ((-0.03, 0.07, 0.05, 0.0), (-0.1, 0.16, 0.08, -0.02), (-0.2, 0.19, 0.1, -0.04),
                          (-0.45, 0.2, 0.11, -0.05), (-0.8, 0.24, 0.13, -0.05), (-length, 0.28, 0.15, -0.045)):
        f = min(1.0, -z / length)
        ph = rnd.uniform(0, 1)
        ring_ = []
        for i in range(48):
            a = 2 * math.pi * i / 48
            fold = 1 + (0.03 + 0.09 * f) * math.sin(7 * a + ph * 6) + 0.03 * f * math.sin(13 * a)
            ring_.append(Vector((hw * fold * math.cos(a), yo + hd * fold * math.sin(a), z)))
        rings.append(ring_)
    loft(f"{name}_Body", rings, fab, parent=e)
    box(f"{name}_Facing", (0.022, 0.012, length - 0.12), (0, -0.05 - 0.15 * 0.96, -0.06 - (length - 0.12) / 2), fab,
        bevel=0.004, rot=(R(-3.5), 0, 0), parent=e)
    for sx in (-1, 1):                                           # wide sleeves hanging at the sides
        sl = spline([(sx * 0.17, -0.03, -0.12), (sx * 0.21, -0.05, -0.4), (sx * 0.23, -0.06, -0.72)], 4)
        tube(f"{name}_Sleeve", sl, 0.05, fab, r2=0.085, segs=14, parent=e)
        ball(f"{name}_Cuff", 0.085, (sx * 0.23, -0.06, -0.72), fab, scale=(1, 0.8, 0.25), parent=e)
    # The hood, gathered over the hook: a soft cowl with its point falling down the back.
    ball(f"{name}_Hood", 0.12, (0, 0.03, 0.0), fab, scale=(1.05, 0.95, 0.9), parent=e)
    tube(f"{name}_HoodPoint", spline([(0, 0.08, 0.05), (0, 0.13, -0.03), (0, 0.15, -0.16)], 4), 0.06, fab, r2=0.012,
         segs=12, parent=e)
    ring(f"{name}_Clasp", 0.012, 0.003, (0, -0.075, -0.09), M("pewter", 0.4, "brushed", metal=0.8), rot=(R(90), 0, 0),
         segs=12, parent=e)
    return e


def coat_stand(name, loc):
    """Bentwood hat-and-coat stand (Thonet No. 11 type, 1.9 m): turned pole, four bent feet, an umbrella ring and
    six bent coat hooks under a turned top."""
    e = empty(name, loc)
    bent = WOOD_DK_V
    lathe(f"{name}_Pole", [(0.026, 0), (0.026, 0.3), (0.02, 0.36), (0.022, 1.6), (0.026, 1.7), (0.022, 1.84),
                           (0.03, 1.86), (0.028, 1.9), (0.0, 1.92)], (0, 0, 0), bent, segs=16, parent=e)
    ball(f"{name}_Top", 0.04, (0, 0, 1.93), bent, parent=e)
    for k in range(4):
        a = R(45 + 90 * k)
        c, s_ = math.cos(a), math.sin(a)
        tube(f"{name}_Foot", spline([(0.02 * c, 0.02 * s_, 0.42), (0.12 * c, 0.12 * s_, 0.28),
                                     (0.26 * c, 0.26 * s_, 0.03), (0.32 * c, 0.32 * s_, 0.015)], 6), 0.016, bent,
             segs=10, parent=e)
        tube(f"{name}_UmbrellaArm", [(0.02 * c, 0.02 * s_, 0.5), (0.2 * c, 0.2 * s_, 0.5)], 0.008, bent, segs=6,
             parent=e)
    ring(f"{name}_UmbrellaRing", 0.2, 0.01, (0, 0, 0.5), bent, segs=40, parent=e)
    hooks = []
    for k in range(6):
        a = R(30 + 60 * k)
        c, s_ = math.cos(a), math.sin(a)
        tube(f"{name}_Hook", spline([(0.02 * c, 0.02 * s_, 1.82), (0.11 * c, 0.11 * s_, 1.74),
                                     (0.16 * c, 0.16 * s_, 1.66), (0.18 * c, 0.18 * s_, 1.71)], 5), 0.01, bent,
             segs=8, parent=e)
        ball(f"{name}_HookTip", 0.014, (0.18 * c, 0.18 * s_, 1.71), bent, parent=e)
        hooks.append(Vector((0.17 * c, 0.17 * s_, 1.68)))
    return e, hooks


stand, stand_hooks = coat_stand("CoatStand", (4.85, 3.75, FLOOR_Z))
robe("Robe_1", stand_hooks[5] + Vector((0, 0, 0.02)), face=-30, parent=stand)      # hook at -30 deg: faces the camera
robe("Robe_2", stand_hooks[2] + Vector((0, 0, 0.04)), face=150, parent=stand, length=1.15)

# A pile of spell books on the floor by the wing chair.
pile = Vector((2.68, 3.62, FLOOR_Z))
for k in range(3):
    book(f"FloorBook_{k}", (0.05, 0.2, 0.27), (pile.x, pile.y, FLOOR_Z + k * 0.05 + 0.025), (LEATHER_RED, VELVET_DK,
         LEATHER)[k], rot=(0, R(90), R(30 + k * 14)))

if not NIGHT:                                    # autumn term: squashes on the hearth and a bowl of apples
    def squash(name, loc, r, key, parent=None):
        """Small ribbed squash (Crown Prince / munchkin pumpkin size): eight lobes round a short woody stem."""
        sq = empty(name, loc, parent=parent)
        skin = M(key, 0.5, "ceramic", scale=0.4)
        for k in range(8):
            a_ = R(22.5 + 45 * k)
            ball(f"{name}_Lobe", r * 0.62, (r * 0.38 * math.cos(a_), r * 0.38 * math.sin(a_), r * 0.6), skin,
                 scale=(1.0, 1.0, 0.95), parent=sq, segs=16)
        cyl(f"{name}_Stem", r * 0.12, r * 0.5, (0, 0, r * 1.2), M("wood", 0.8, "wood", color="#6E5A3C"), r2=r * 0.08,
            segs=8, parent=sq)
        return sq

    squash("Hearth_Squash", (0.3, -0.24, 0.04), 0.09, "accent_3", parent=fire_root)
    squash("Hearth_SquashSmall", (0.42, -0.16, 0.04), 0.06, "accent_2", parent=fire_root)
    bowl = empty("Trunk_AppleBowl", (0.22, 0.0, 0.565), parent=trunk2)
    lathe("AppleBowl_Bowl", [(0.0, 0.0), (0.05, 0.0), (0.06, 0.008), (0.1, 0.035), (0.115, 0.065), (0.108, 0.068),
                             (0.09, 0.04), (0.0, 0.03)], (0, 0, 0), WOOD_DK, segs=28, parent=bowl)
    for k, (ax, ay, az) in enumerate(((0.0, 0.0, 0.07), (0.05, 0.02, 0.06), (-0.04, 0.04, 0.06), (-0.02, -0.05, 0.06),
                                      (0.03, -0.035, 0.1))):
        ball("AppleBowl_Apple", 0.034, (ax, ay, az), mat("accent_3" if k % 3 else "plant", 0.4,
             color=shade(COLORS["accent_3"], 0.9) if k % 3 else mix_hex(COLORS["plant"], "#C9B43A", 0.4)),
             scale=(1, 1, 0.9), parent=bowl, segs=14)
    # A few fallen leaves blown in by the window and the stair.
    rnd = random.Random(SEED + 31)
    for k in range(14):
        x, y = (rnd.uniform(2.0, 3.6), rnd.uniform(3.6, 4.7)) if k < 8 else (rnd.uniform(1.8, 3.4), rnd.uniform(1.4, 2.6))
        key = ("tree_1", "tree_2", "accent_3")[k % 3]
        leaf = prism("Leaf", [(0, 0), (0.035, 0.028), (0.042, 0.07), (0.0, 0.105), (-0.042, 0.07), (-0.035, 0.028)], 0.002,
                     mat(key, 0.7), loc=(x, y, FLOOR_Z + 0.014), rot=(R(90), 0, R(rnd.uniform(0, 360))))
        leaf.rotation_euler = (R(90 + rnd.uniform(-8, 8)), R(rnd.uniform(-8, 8)), R(rnd.uniform(0, 360)))

# =====================================================================
#  WALL DECOR + PORTFOLIO PICTURES AND SIGN
# =====================================================================
BF = at_wall("BreastFace", BREAST_A, r=BREAST_FACE)              # flat front of the chimney breast, -y = room


def framed(name, size, loc, parent, frame_mat=None, fw=0.035, depth=0.03):
    """Gilt picture frame (35 mm moulding with an inner bead) hung flat on a wall frame. Returns the picture
    location just in front of the backing."""
    x, z = loc
    w, h = size
    fm = frame_mat or GILT
    ow, oh = w + 2 * fw, h + 2 * fw
    box(f"{name}_Backing", (ow - 0.01, 0.01, oh - 0.01), (x, -0.005, z), WOOD_DK, bevel=0, parent=parent)
    for sz in (-1, 1):
        box(f"{name}_FrameH", (ow, depth, fw), (x, -depth / 2, z + sz * (oh - fw) / 2), fm, bevel=0.006,
            parent=parent)
    for sx in (-1, 1):
        box(f"{name}_FrameV", (fw, depth, oh - 2 * fw), (x + sx * (ow - fw) / 2, -depth / 2, z), fm, bevel=0.006,
            parent=parent)
    for sz in (-1, 1):
        box(f"{name}_BeadH", (w + 0.01, 0.006, 0.008), (x, -depth + 0.003, z + sz * (h / 2 + 0.003)),
            mat("accent_2", 0.5, color=shade(COLORS["accent_2"], 0.7)), bevel=0, parent=parent)
    return (x, -0.0125, z)


# Frame 1: landscape painting over the mantel. Frames 2-3: two portrait-format paintings either side.
FR1 = (0.6, 0.44)
loc = framed("Painting1", FR1, (0, 1.99), BF)
f1 = hook_image("frame", 1, FR1, loc, parent=BF, default_key="sky_low")
P1O = empty("Painting1_Art", (0, 0, 0.11), parent=BF)        # the default picture, drawn for z = 1.88
hook_default(f1,
             box("Painting1_Sky", (FR1[0], 0.002, 0.2), (0, -0.014, 1.88 + 0.12), mat("sky_low", 0.8,
                 color=mix_hex(COLORS["sky_low"], "#F2D9A8", 0.5)), bevel=0, parent=P1O),
             prism("Painting1_Hills", [(-0.3, 1.70), (-0.3, 1.86), (-0.16, 1.95), (-0.04, 1.88), (0.1, 1.99),
                                       (0.3, 1.86), (0.3, 1.70)], 0.002, mat("plant", 0.8), loc=(0, -0.0145, 0),
                   parent=P1O),
             box("Painting1_Lake", (FR1[0], 0.002, 0.08), (0, -0.015, 1.7), mat("lake", 0.6), bevel=0, parent=P1O),
             prism("Painting1_Tower", [(0.12, 1.84), (0.17, 1.84), (0.17, 1.98), (0.18, 1.98), (0.18, 2.0),
                                       (0.11, 2.0), (0.11, 1.98), (0.12, 1.98)], 0.002, mat("wall", 0.8),
                   loc=(0, -0.016, 0), parent=P1O),
             cyl("Painting1_Moon", 0.03, 0.002, (-0.17, -0.016, 2.04), mat("moon", 0.5), rot=(R(90), 0, 0), segs=20,
                 bevel=0, parent=P1O))
FR2 = (0.3, 0.4)
for i, sx in enumerate((-0.6, 0.6)):
    loc = framed(f"Painting{i + 2}", FR2, (sx, 2.04), BF)
    fh = hook_image("frame", i + 2, FR2, loc, parent=BF, default_key="accent_1" if i == 0 else "main")
    P2O = empty(f"Painting{i + 2}_Art", (0, 0, 0.14), parent=BF)
    if i == 0:                                       # still life: a candle in a holder
        hook_default(fh,
                     box("Painting2_Table", (0.3, 0.002, 0.08), (sx, -0.014, 1.74), mat("wood", 0.8), bevel=0,
                         parent=P2O),
                     box("Painting2_Candle", (0.05, 0.002, 0.16), (sx, -0.015, 1.86), mat("cream", 0.7), bevel=0,
                         parent=P2O),
                     ball("Painting2_Flame", 0.018, (sx, -0.016, 1.965), mat("accent_2", 0.5, emit=0.6),
                          scale=(0.8, 0.1, 1.5), parent=P2O))
    else:                                            # a crescent moon over a hill
        hook_default(fh,
                     cyl("Painting3_Moon", 0.07, 0.002, (sx + 0.02, -0.014, 1.98), mat("moon", 0.5),
                         rot=(R(90), 0, 0), segs=24, bevel=0, parent=P2O),
                     cyl("Painting3_MoonCut", 0.065, 0.002, (sx + 0.055, -0.015, 2.0), mat("main", 0.4),
                         rot=(R(90), 0, 0), segs=24, bevel=0, parent=P2O),
                     ball("Painting3_Hill", 0.2, (sx, -0.015, 1.7), mat("plant", 0.8), scale=(0.75, 0.01, 0.35),
                          parent=P2O))

# Two gilt portrait frames on the tower walls (frames 4 and 5): painterly, faceless head-and-shoulders studies of
# nobody in particular, each with a small brass title plaque (your project titles once the frames hold your images).
PORTRAITS = [(4, 70.0, 2.42, (0.3, 0.4), "accent_1", "PROJECT FOUR"), (5, 187.0, 2.66, (0.26, 0.34), "main",
                                                                         "PROJECT FIVE")]
for idx, a_, zc_, fs, coat, ttl in PORTRAITS:
    pf = at_wall(f"Portrait{idx}", a_, r=RI - 0.02)
    loc = framed(f"Portrait{idx}", fs, (0, zc_), pf, fw=0.04, depth=0.035)
    ph = hook_image("frame", idx, fs, loc, parent=pf, default_key="dark")
    pw, ph_ = fs
    ground = mix_hex(COLORS["dark"], COLORS["wood"], 0.55)
    art = [box(f"Portrait{idx}_Ground", (pw, 0.002, ph_), (0, -0.0135, zc_), mat("dark", 0.85, color=ground),
               bevel=0, parent=pf),
           cyl(f"Portrait{idx}_Glow", pw * 0.42, 0.002, (0, -0.014, zc_ + ph_ * 0.08), mat("cream", 0.85,
               color=mix_hex(ground, COLORS["accent_2"], 0.35)), rot=(R(90), 0, 0), segs=32, bevel=0, parent=pf),
           ball(f"Portrait{idx}_Shoulders", pw * 0.42, (0, -0.0145, zc_ - ph_ * 0.42), mat(coat, 0.8,
                color=shade(COLORS[coat], 0.6)), scale=(1.0, 0.01, 0.62), parent=pf),
           ball(f"Portrait{idx}_Collar", pw * 0.12, (0, -0.015, zc_ - ph_ * 0.2), mat("cream", 0.8), scale=(1.4, 0.01,
                0.5), parent=pf),
           ball(f"Portrait{idx}_Head", pw * 0.15, (0, -0.0155, zc_ + ph_ * 0.02), mat("cream", 0.8,
                color=mix_hex(COLORS["cream"], "#C99A78", 0.5)), scale=(0.82, 0.01, 1.05), parent=pf),
           ball(f"Portrait{idx}_Hair", pw * 0.16, (0, -0.0152, zc_ + ph_ * 0.07), mat("dark", 0.8,
                color=mix_hex(COLORS["dark"], COLORS["accent_3"], 0.35)), scale=(0.9, 0.01, 0.8), parent=pf)]
    rs = random.Random(SEED + idx)
    for k in range(9):                                           # a few loose brush strokes in the background
        art.append(box(f"Portrait{idx}_Stroke", (rs.uniform(0.03, 0.08), 0.001, 0.006),
                       (rs.uniform(-pw * 0.4, pw * 0.4), -0.0158, zc_ + rs.uniform(-ph_ * 0.1, ph_ * 0.45)),
                       mat("cream", 0.8, color=mix_hex(ground, COLORS["accent_2"], 0.55)), bevel=0,
                       rot=(0, R(rs.uniform(-25, 25)), 0), parent=pf))
    hook_default(ph, *art)
    pz = zc_ - ph_ / 2 - 0.02                                    # brass title plaque on the bottom rail
    box(f"Portrait{idx}_Plaque", (0.2, 0.006, 0.036), (0, -0.038, pz), BRASS, bevel=0.002, parent=pf)
    hook_text("title", idx, ttl, 0.018, (0, -0.0415, pz), material=mat("dark", 0.5, color="#2A1E16"),
              max_width=0.18, parent=pf, depth=0.0008)

# Cloth banner over the paintings, hanging from an iron rod: your name and role, embroidered in gold.
BAN_W, BAN_Z, BAN_H = 1.5, 2.56, 0.52
box("Banner_Rod", (BAN_W + 0.16, 0.022, 0.022), (0, -0.05, BAN_Z + BAN_H / 2 + 0.03), IRON, bevel=0.006, parent=BF)
for sx in (-1, 1):
    ball("Banner_RodFinial", 0.022, (sx * (BAN_W / 2 + 0.1), -0.05, BAN_Z + BAN_H / 2 + 0.03), IRON, parent=BF)
    box("Banner_RodBracket", (0.02, 0.05, 0.02), (sx * (BAN_W / 2 + 0.04), -0.025, BAN_Z + BAN_H / 2 + 0.03), IRON,
        bevel=0.004, parent=BF)
ban = [(-BAN_W / 2, BAN_Z + BAN_H / 2), (BAN_W / 2, BAN_Z + BAN_H / 2), (BAN_W / 2, BAN_Z - BAN_H / 2 + 0.08),
       (0, BAN_Z - BAN_H / 2), (-BAN_W / 2, BAN_Z - BAN_H / 2 + 0.08)]
ban = [ban[0]] + list(reversed(ban[1:]))                 # anticlockwise as seen from the room
prism("Banner_Cloth", ban, 0.012, VELVET, loc=(0, -0.05, 0), parent=BF)
inner = [(x * 0.94, BAN_Z + (z - BAN_Z) * 0.86) for x, z in ban]
for (xa, za), (xb, zb) in zip(inner, inner[1:] + inner[:1]):           # gold border stitched on
    ln = math.hypot(xb - xa, zb - za)
    box("Banner_Border", (ln, 0.004, 0.012), ((xa + xb) / 2, -0.058, (za + zb) / 2), GOLD_CLOTH, bevel=0,
        rot=(0, -math.atan2(zb - za, xb - xa), 0), parent=BF)
boxes("Banner_Loops", [((0.04, 0.016, 0.05), (-BAN_W / 2 + 0.08 + k * (BAN_W - 0.16) / 5, -0.05, BAN_Z + BAN_H / 2),
                        (0, 0, 0)) for k in range(6)], VELVET_DK, bevel=0.004, parent=BF)
gold_text = mat("accent_2", 0.35, emit=0.5, metal=0.4)
hook_text("name", 1, "YOUR NAME", 0.155, (0, -0.062, BAN_Z + 0.075), material=gold_text, max_width=BAN_W - 0.2,
          parent=BF, depth=0.004)
hook_text("role", 1, "your role", 0.11, (0, -0.062, BAN_Z - 0.1), material=mat("cream", 0.5, emit=0.5),
          max_width=BAN_W - 0.4, parent=BF, depth=0.003)
box("Banner_Rule", (0.5, 0.004, 0.006), (0, -0.06, BAN_Z - 0.015), GOLD_CLOTH, bevel=0, parent=BF)

# The painted night sky carries on across the top of the chimney breast, under a dressed cornice.
BSKY_Z0 = COURSES[-2]                                    # above the banner rod
box("Breast_SkyPanel", (BREAST_W + 0.02, 0.02, H - BSKY_Z0), (0, -0.01, (H + BSKY_Z0) / 2), VAULT, bevel=0.003,
    parent=BF)
box("Breast_SkyBead", (BREAST_W + 0.04, 0.03, 0.026), (0, -0.016, BSKY_Z0 + 0.012), GILT, bevel=0.008, parent=BF)
box("Breast_Cornice", (BREAST_W + 0.06, 0.07, 0.05), (0, -0.03, H - 0.02), DRESSED_DK, bevel=0.008, parent=BF)
_rb = random.Random(SEED + 43)
_bm = bmesh.new()
for k in range(46):
    c_ = Vector((_rb.uniform(-0.76, 0.76), -0.0215, _rb.uniform(BSKY_Z0 + 0.04, H - 0.06)))
    big_ = _rb.random() < 0.2
    _bm.faces.new([_bm.verts.new(p_) for p_ in star_shape(c_, Vector((1, 0, 0)), Vector((0, 0, 1)),
                   _rb.uniform(0.016, 0.026) if big_ else _rb.uniform(0.006, 0.011), 4, 0.3, _rb.uniform(0, 1))])
_st = _obj("Breast_SkyStars", _bm)
_st.data.materials.append(STAR_PAINT)
COL_ROOM.objects.link(_st)
_st.parent = BF

# Mantel candlesticks (the candles light the paintings).
for sx in (-0.66, 0.66):
    candlestick(f"Mantel_Candle_{'L' if sx < 0 else 'R'}", (sx, -0.16, 1.45), parent=BF, h=0.15,
                light_w=LAMP_STRENGTH, candle_h=0.12)
PEWTER = M("pewter", 0.4, "brushed", metal=0.8, scale=0.6)
for k, gx in enumerate((-0.12, -0.03)):                    # two plain pewter goblets
    lathe(f"Mantel_Goblet_{k}", [(0.0, 0), (0.034, 0), (0.036, 0.006), (0.012, 0.014), (0.008, 0.05), (0.014, 0.058),
                                 (0.008, 0.066), (0.012, 0.072), (0.034, 0.1), (0.038, 0.15), (0.034, 0.15),
                                 (0.03, 0.105), (0.0, 0.1)], (gx, -0.15 - 0.03 * k, 1.45), PEWTER, segs=24, parent=BF)
GLAZE = M("accent_1", 0.3, "ceramic", color=shade(COLORS["accent_1"], 1.1))
lathe("Mantel_Jar", [(0.0, 0), (0.04, 0), (0.055, 0.03), (0.055, 0.09), (0.035, 0.12), (0.03, 0.13), (0.0, 0.13)],
      (-0.32, -0.15, 1.45), GLAZE, segs=24, parent=BF)
lathe("Mantel_JarLid", [(0.034, 0), (0.036, 0.008), (0.012, 0.02), (0.014, 0.035), (0.0, 0.038)],
      (-0.32, -0.15, 1.58), GLAZE, segs=20, parent=BF)
for k in range(2):
    book(f"Mantel_Book_{k}", (0.03, 0.15, 0.2), (0.3, -0.16, 1.45 + 0.015 + k * 0.03), (LEATHER_RED, VELVET_DK)[k],
         parent=BF, rot=(0, R(90), R(8 - 14 * k)))
lathe("Mantel_Pot", [(0.0, 0), (0.035, 0), (0.045, 0.07), (0.05, 0.08), (0.0, 0.08)], (0.3, -0.16, 1.51),
      TERRACOTTA, segs=20, parent=BF)
foliage_pts = [(0.3 + 0.07 * math.cos(R(t)), -0.16 + 0.05 * math.sin(R(t)), 1.6 + 0.03 * math.sin(R(3 * t)))
               for t in range(0, 360, 40)]
for k, fp in enumerate(foliage_pts):
    ball("Mantel_Fern", 0.035, fp, mat("plant", 0.7), scale=(1.5, 0.6, 0.35), rot=(0, 0, R(40 * k)), parent=BF)

# Cork timetable board on the wall above the bookcase (picture hook "board"): oak frame, pinned cards.
TB = at_wall("Timetable", 110.0, r=RI - 0.01)
BW_, BH_ = 0.48, 0.36
TBZ = 2.4
box("Timetable_Frame", (BW_ + 0.06, 0.025, BH_ + 0.06), (0, -0.0125, TBZ), OAK, bevel=0.005, parent=TB)
box("Timetable_Cork", (BW_ + 0.01, 0.006, BH_ + 0.01), (0, -0.027, TBZ), CORK, bevel=0, parent=TB)
tb = hook_image("board", 1, (BW_, BH_), (0, -0.031, TBZ), parent=TB, default_key="cork")
cards = []
for row in range(2):
    for col in range(3):
        cx_, cz_ = -0.15 + col * 0.15, TBZ + 0.08 - row * 0.16
        cards.append(box("Timetable_Card", (0.12, 0.002, 0.12), (cx_ + random.uniform(-0.01, 0.01), -0.033, cz_),
                         PARCHMENT if (row + col) % 2 else PAPER, bevel=0, rot=(0, R(random.uniform(-5, 5)), 0),
                         parent=TB))
        cards.append(ball("Timetable_Pin", 0.008, (cx_, -0.037, cz_ + 0.045), mat(("accent_3", "accent_1",
                          "accent_2")[(row + col) % 3], 0.3), parent=TB))
        for ln in range(3):
            cards.append(box("Timetable_Ink", (0.08 - 0.02 * (ln % 2), 0.001, 0.005),
                             (cx_, -0.0345, cz_ + 0.015 - ln * 0.025), INK, bevel=0, parent=TB))
hook_default(tb, *cards)

# A church candle and a book on the lancet's stone window board.
for i, wd in enumerate(WINDOWS):
    if wd["shape"] != "lancet":
        continue
    a = wd["a"]
    p = P(RI + 0.03, a - 5.5, Z_SILL)
    candle(f"Sill_Candle_{i}", (p.x, p.y, Z_SILL), h=0.14, r=0.03, light_w=LAMP_STRENGTH)
    # A small brass table telescope on its tripod, pointed out over the loch at the sky.
    tp = at_wall("Sill_Telescope", a + 0.5, r=RI, z=Z_SILL)
    for k in range(3):
        a_ = R(90 + 120 * k)
        tube("Telescope_Leg", [(0, 0, 0.1), (0.06 * math.cos(a_), 0.06 * math.sin(a_), 0.002)], 0.004, BRASS, segs=6,
             parent=tp)
    lathe("Telescope_Head", [(0.0, 0.09), (0.012, 0.09), (0.012, 0.115), (0.0, 0.115)], (0, 0, 0), BRASS, segs=12,
          parent=tp)
    tel = empty("Telescope_Tube", (0, 0, 0.125), rot=(R(-90 + 22), 0, 0), parent=tp)   # points out and up
    lathe("Telescope_Body", [(0.0, -0.17), (0.012, -0.17), (0.012, -0.12), (0.016, -0.115), (0.016, -0.03),
                             (0.02, -0.025), (0.02, 0.1), (0.026, 0.105), (0.026, 0.16), (0.0, 0.16)], (0, 0, 0),
          BRASS, segs=20, parent=tel)
    ring("Telescope_Band", 0.021, 0.003, (0, 0, 0.0), LEATHER_DK, segs=20, parent=tel)
    cyl("Telescope_Lens", 0.022, 0.002, (0, 0, 0.161), mat("glass", 0.05, color=COLORS["sky_low"], emit=0.6),
        segs=20, bevel=0, parent=tel)
    # A stack of letters closed with wax seals, waiting on the window board.
    lp = at_wall("Sill_Letters", a + 6.0, r=RI + 0.06, z=Z_SILL)
    for k in range(3):
        box(f"Sill_Letter_{k}", (0.12, 0.085, 0.004), (0, 0, 0.002 + 0.0045 * k), PAPER if k % 2 else PARCHMENT,
            bevel=0.001, rot=(0, 0, R(-8 + 9 * k)), parent=lp)
    cyl("Sill_LetterSeal", 0.011, 0.004, (0.01, -0.01, 0.016), SEAL_WAX, segs=14, bevel=0.0015, parent=lp)
    tube("Sill_LetterString", [(-0.062, 0.0, 0.016), (0.062, 0.0, 0.016)], 0.0015, ROPE, segs=4, parent=lp)

# =====================================================================
#  LIGHTS, WORLD, CAMERA, RENDER
# =====================================================================
# Night: cold moonlight from behind the tower (the walls throw long shadows, the windows throw light shafts),
# a dim blue fill from the camera side, the fire and candles warm. Autumn: low golden sun, brighter warm fill.
if NIGHT:
    sun_k, sun_s, fill_k, fill_w, amb = SUN_WARMTH, SUN_STRENGTH, 8000, 260, 0.35
else:
    sun_k, sun_s, fill_k, fill_w, amb = 3200, SUN_STRENGTH * 5.0, 4800, 380, 0.5
target = Vector((CX, CY, 0))
sun_dir = (P(1, 160 if NIGHT else 112) - Vector((CX, CY, 0))).normalized() * -1   # comes from behind the tower
sun_dir.z = -math.tan(R(36 if NIGHT else 24))
sun_dir.normalize()
light("Light_Sun", "SUN", sun_s, kelvin(sun_k), target - sun_dir * 8, aim=target, size=R(1.5))
light("Light_Fill", "AREA", fill_w, kelvin(fill_k), (W + 3.5, -3.5, H + 3), aim=(CX, CY, 0.8), size=7)
light("Light_Bounce", "AREA", 60 if NIGHT else 90, kelvin(2600 if NIGHT else 3600), (CX, CY, H + 0.4),
      aim=(CX, CY, 0), size=4)

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
bg_amb.inputs["Strength"].default_value = amb
path = wn.new("ShaderNodeLightPath")
mix = wn.new("ShaderNodeMixShader")
wl.new(path.outputs["Is Camera Ray"], mix.inputs["Fac"])
wl.new(bg_amb.outputs[0], mix.inputs[1])
wl.new(bg_cam.outputs[0], mix.inputs[2])
wl.new(mix.outputs[0], out.inputs["Surface"])

# Orthographic camera. The tower is round, so instead of a box the framing uses what the camera really sees:
# kit_bounds is the smallest box (in this camera's view) that holds every visible part of the tower.
cam_data = bpy.data.cameras.new("Camera")
cam_data.type = "ORTHO"
cam = bpy.data.objects.new("Camera", cam_data)
scene.collection.objects.link(cam)
scene.camera = cam
cam.rotation_euler = Euler((R(90 - CAMERA_HEIGHT_ANGLE), 0, R(CAMERA_TURN)))
rot = cam.rotation_euler.to_matrix()
right, up, back = rot.col[0], rot.col[1], rot.col[2]
aspect = RESOLUTION[0] / RESOLUTION[1]
bpy.context.view_layer.update()
xs, ys = [], []
for o in scene.objects:
    if o.type != "MESH" or o.hide_render or o.name.startswith("Sky_"):
        continue
    mw_ = o.matrix_world
    for v in o.data.vertices:
        p = mw_ @ v.co
        xs.append(p.dot(right))
        ys.append(p.dot(up))
r0, r1, u0, u1 = min(xs), max(xs), min(ys), max(ys)
ct, st_ = math.cos(R(CAMERA_TURN)), math.sin(R(CAMERA_TURN))
sh, ch = math.sin(R(CAMERA_HEIGHT_ANGLE)), math.cos(R(CAMERA_HEIGHT_ANGLE))
span = abs(ct) + abs(st_)
a_ = (r1 - r0) / 2 / span
rc = (r0 + r1) / 2
bx, by = rc * ct, rc * st_
z_lo, z_hi = (u0 + a_ * sh * span) / ch, (u1 - a_ * sh * span) / ch
if z_hi < z_lo:
    z_lo = z_hi = (u0 + u1) / 2 / ch
BOUNDS = [round(v, 3) for v in (bx - a_, by - a_, z_lo, bx + a_, by + a_, z_hi)]
corners = [Vector((x, y, z)) for x in (BOUNDS[0], BOUNDS[3]) for y in (BOUNDS[1], BOUNDS[4]) for z in (BOUNDS[2], BOUNDS[5])]
cxs = [c.dot(right) for c in corners]
cys = [c.dot(up) for c in corners]
cam_data.ortho_scale = max(max(cxs) - min(cxs), (max(cys) - min(cys)) * aspect) * 1.06
centre_v = right * (max(cxs) + min(cxs)) / 2 + up * (max(cys) + min(cys)) / 2
cam.location = centre_v + back * 30
cam_data.clip_end = 100

# Floating candles drifting under the painted vault. They are placed after the camera, so none of them can hide
# your name, role, pictures or the clickable objects: each candidate is projected into the picture and dropped if it
# lands on one of them. (By day, in the autumn theme, they hang unlit.)
def screen_rect(objs, pad=0.05):
    xs_, ys_ = [], []
    for o in objs:
        for c in o.bound_box:
            p_ = o.matrix_world @ Vector(c)
            xs_.append(p_.dot(right))
            ys_.append(p_.dot(up))
    return (min(xs_) - pad, min(ys_) - pad, max(xs_) + pad, max(ys_) + pad) if xs_ else None


def with_children(o):
    return [c for c in [o] + list(o.children_recursive) if c.type in ("MESH", "FONT")]


bpy.context.view_layer.update()
keep_clear = [o for o in scene.objects if o.get("kit_hook")]
keep_clear += [c for o in scene.objects if o.get("kit_link") for c in with_children(o)]
keep_clear += [o for o in scene.objects if o.name.startswith(("Window1_Glass", "Cage_", "Owl_", "Banner_Cloth",
                                                               "Fire_Flame", "Besom"))]
CLEAR_RECTS = [r for r in (screen_rect([o]) for o in keep_clear) if r]


def screen_seg(o):
    """The centre line of a long rail (its longest local axis), projected into the picture."""
    bb = [Vector(c) for c in o.bound_box]
    lo_ = Vector([min(c[i] for c in bb) for i in range(3)])
    hi_ = Vector([max(c[i] for c in bb) for i in range(3)])
    ax_ = max(range(3), key=lambda i: hi_[i] - lo_[i])
    d_ = Vector((0, 0, 0))
    d_[ax_] = (hi_[ax_] - lo_[ax_]) / 2
    ends = [o.matrix_world @ ((lo_ + hi_) / 2 + sg * d_) for sg in (-1, 1)]
    return [Vector((e.dot(right), e.dot(up))) for e in ends]


# The bed testers: a candle drawn just on top of (or hanging in front of) a tester rail looks as if it stands on the
# bed, so candidates whose candle would touch a rail in the picture are dropped too.
RAILS = [screen_seg(o) for o in scene.objects if o.type == "MESH" and o.name.startswith(("Bed_Tester", "Bed2_Tester"))]


def touches_rail(sx_, sy_):
    for a2, b2 in RAILS:
        ab = b2 - a2
        for k in range(9):
            q = Vector((sx_, sy_ - 0.26 + 0.045 * k))            # from the pelmet's hem up to above the flame
            t = max(0.0, min(1.0, (q - a2).dot(ab) / max(ab.length_squared, 1e-9)))
            if (q - (a2 + ab * t)).length < 0.06:
                return True
    return False


rnd_c = random.Random(SEED + 71)
placed, tries = [], 0
while len(placed) < FLOATING_CANDLES and tries < 6000:
    tries += 1
    rr, aa = 2.05 * math.sqrt(rnd_c.random()), rnd_c.uniform(0, 360)
    p_ = P(rr, aa, rnd_c.uniform(2.3, 2.9))
    if (p_ - P(BREAST_FACE - 0.1, BREAST_A, p_.z)).length < 0.55:
        continue                                                   # not inside the chimney breast
    sx_, sy_ = p_.dot(right), p_.dot(up)
    if any(abs(sx_ - q.dot(right)) < 0.2 and abs(sy_ - q.dot(up)) < 0.3 for q in placed):
        continue                                                   # spread out in the picture, not just in the room
    if sum(1 for q in placed if abs(sx_ - q.dot(right)) < 0.3) >= 3:
        continue                                                   # at most three in any slice of the picture
    if any(r[0] < sx_ + 0.03 and sx_ - 0.03 < r[2] and r[1] < sy_ + 0.26 and sy_ - 0.04 < r[3] for r in CLEAR_RECTS):
        continue
    if touches_rail(sx_, sy_):
        continue
    placed.append(p_)
print(f"[RoomKit] {len(placed)} floating candles")
for k, p_ in enumerate(placed):
    fc = empty(f"FloatCandle_{k}", tuple(p_), rot=(R(rnd_c.uniform(-5, 5)), R(rnd_c.uniform(-5, 5)), 0))
    candle(f"FloatCandle_{k}", (0, 0, 0), h=rnd_c.uniform(0.11, 0.2), r=rnd_c.uniform(0.012, 0.017), parent=fc,
           light_w=LAMP_STRENGTH * 0.8 if k % 3 == 0 else None, flame_size=1.5, halo=True, magic=True)

# Night sky behind the tower: a big soft moon and a scatter of stars (decoration only, outside kit_bounds).
if NIGHT and STARS:
    sky_c = centre_v - back * 12
    half_w, half_h = cam_data.ortho_scale / 2, cam_data.ortho_scale / 2 / aspect
    moon_p = sky_c + right * half_w * 0.7 + up * half_h * 0.62
    m_ = cyl("Sky_Moon", 0.62, 0.02, tuple(moon_p), glow(COLORS["moon"], 1.25), segs=64, bevel=0)
    m_.rotation_euler = back.to_track_quat("Z", "Y").to_euler()
    for k in range(12):                                          # glow: many close rings fade smoothly
        f_ = (k + 1) / 12
        hr, t_ = 0.66 + 0.75 * f_, 0.34 * (1 - f_) ** 1.6
        halo = cyl(f"Sky_MoonHalo_{k}", hr, 0.02, tuple(moon_p - back * (0.1 + 0.02 * k)), mat("sky", 0.9, emit=1.0,
                   color=mix_hex(COLORS["background"], COLORS["sky_low"], t_)), segs=64, bevel=0)
        halo.rotation_euler = m_.rotation_euler
    rnd = random.Random(SEED + 21)
    star_m = glow(COLORS["moon"], 4.0)
    for k in range(70):
        sx_, sy_ = rnd.uniform(-1, 1) * half_w, rnd.uniform(-1, 1) * half_h
        if abs(sx_) < half_w * 0.42 and sy_ < half_h * 0.6:       # keep stars off the tower itself
            continue
        rr = rnd.choice((0.012, 0.016, 0.022, 0.03))
        s_ = cyl("Sky_Star", rr, 0.01, tuple(sky_c + right * sx_ + up * sy_), star_m, segs=16, bevel=0)
        s_.rotation_euler = m_.rotation_euler
        if rr > 0.025:                                   # the brightest stars twinkle (a four-point glint)
            for ang in (0, 90):
                g_ = box("Sky_Glint", (0.16, 0.012, 0.012), tuple(sky_c + right * sx_ + up * sy_), star_m, bevel=0)
                g_.rotation_euler = (m_.rotation_euler.to_matrix() @ Euler((0, 0, R(ang))).to_matrix()).to_euler()
    for o in [o for o in COL_ROOM.objects if o.name.startswith("Sky_")]:
        if hasattr(o, "visible_shadow"):
            o.visible_shadow = False

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
scene.view_settings.exposure = 0.0 if NIGHT else -0.1

# Remember the style so add_furniture.py can match colours later.
scene["kit_style"] = STYLE
scene["kit_version"] = KIT_VERSION
scene["kit_palette"] = json.dumps(COLORS)
scene["kit_material_finish"] = json.dumps({"roughness": 0.6, "bevel": 0.005, "saturation": 0.75})
scene["kit_theme"] = THEME
scene["kit_bounds"] = BOUNDS            # the visible tower (walls, battlements, chimney, base), as this camera sees it
scene["kit_room_size"] = [W, D, H]      # the square the round room (and every slot) sits in, for check_room.py
scene["kit_furniture_colors"] = json.dumps(["main", "accent_1", "accent_2", "accent_3", "cream", "wood", "leather",
                                            "brass", "plant", "dark"])   # colours add_furniture.py may use


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
