"""
3D ROOM PORTFOLIO KIT  -  Template: FAIRYTALE ATELIER (a gown designer's dressing salon)
=========================================================================================
Builds a little isometric couture atelier with a storybook, princesscore feeling, modelled on real bridal and
evening-wear boutiques: a curved brass gown rail with six ORIGINAL ball gowns on padded hangers (each named after
a gemstone or flower and cut in a different silhouette), a dress form on a round fitting podium, a dressing table
with a bulb-lit vanity mirror and a tufted stool, a glass vitrine with a tiara, a full-length gilded mirror, an
arched window with swag curtains, a crystal candle chandelier, a sewing table, a sketch easel and a swatch board.
It renders a 1920x1080 image.
Your name and role are on the boutique sign over the gown rail; your projects are the croquis on the easel and
the cards on the swatch board.

HOW TO RUN
  Option A (no Blender UI):   blender -b -P fairytale_atelier.py
  Option B (inside Blender):  Scripting tab > Open > fairytale_atelier.py > Run Script (then F12 to render)

You only need to edit the SETTINGS block below. Everything under it builds the room.
Output: output/fairytale_atelier.png and output/fairytale_atelier.blend next to this script.
"""
# REFERENCES  (what each piece is modelled on; product names appear only here and in research/fairytale_atelier.md)
#   clothes_rack   curved freestanding bridal gown rail in polished brass (Mandai "Jade" curved bridal rail type,
#                  YDF brass rail 130 x 40 x 200 cm), here a 2.8 m bow on two uprights + 2 wall stays, bar 2.0 m
#                  https://www.mandai-design.com/products/clothing-rail-jade-white-w-120-d-50-h-132-192
#                  https://architonic.com/en/product/ydf-clothes-rail-in-brass/1566005
#   gown hangers   satin padded bridal hangers, 43 cm wide (Morplan type)
#                  https://www-morplan-com-25814.01.mdoq.io/gb_en/82371
#   gowns          six original evening/bridal silhouettes, shoulder-to-hem about 1.55 m (A-line, layered tulle,
#                  cap-sleeve, mermaid, slip column, empire halter); colours by gemstone / season
#   hero_prop      professional dress form on a cast-iron caster base (Wolf / TSC type): torso 36 cm wide,
#                  base 43 cm across, shoulder height 1.33 m  https://theshopcompany.com/dress-forms/professionals.html
#   fitting podium round bridal fitting riser: dia 90 cm, H 15 cm (boutique plinth type)
#                  https://www.mandai-design.com/collections/shopfittings-for-bridal
#   vanity         Louis-style dressing table with cabriole legs and 3 drawers (Marseille type): 105 x 46 x 76 cm
#                  https://www.anindo.com/?p=28258
#   vanity mirror  Hollywood bulb mirror 80 x 60 cm with 12 globe bulbs (Hepburn 80x60 type)
#                  https://hollywoodmirrors.co.uk/collections/tabletop/products/hepburn-hollywood-mirror-80x60cm
#   stool          round button-tufted velvet vanity stool on gold legs: dia 42 cm, H 46 cm
#                  https://www.archiexpo.com/prod/insplosion/product-156759-2288857.html
#   display_case   glass-top jewellery pedestal vitrine: 45 x 45 cm, H 100 cm pedestal + 40 cm glass hood
#                  https://www.juliettesinteriors.co.uk/product/graduated-ornamental-pedestal
#   mirror         full-length gold leaner mirror with an arched top: 170 x 62 cm (Sutton 170 x 60 type)
#                  https://www.kmart.co.nz/product/sutton-gold-look-floor-mirror-170cm-x-60cm-43695164/
#   pendant_lamp   Swedish-style 6-arm brass candle chandelier with crystal drops: dia 60 cm, H 50 cm
#                  (Gustavian 6-arm: 59 x 59 x 46 cm)  https://chairish.com/product/5540274/swedish-style-crystal-chandelier-with-6-arms-medium
#   workbench      vintage sewing-machine table: 90 x 46 x 76 cm, with a retro domestic sewing machine
#                  https://vinterior.co/furniture/tables/side-tables/oak-cased-singer-sewing-machine-side-table-circa-1920-sku95805405
#   easel          French beech A-frame studio easel: footprint 55 x 55 cm, H 1.78 m
#                  https://www.1stdibs.com/furniture/more-furniture-collectibles/racks-stands/easels/french-artist-easel/id-f_30189972
#   hat boxes      round lidded storage hat boxes, nesting set of 3 (largest about 15 in): dia 38 / 32 / 26 cm
#                  https://www.staples.com/Household-Essentials-Hat-Box-Set-with-Faux-Leather-Lids-Floral/product_1529810
#   shoe ledges    floating painted wall shelves on brass scroll brackets, 108 x 22 cm (floating shelf 23 cm deep)
#                  https://shop.app/products/11663246786828/halifax-floating-wall-shelf
#   court shoes    pointed-toe satin pumps, 8.5 cm stiletto, 25 cm long (size 38)
#                  https://en.zalando.de/kazar-new-paris-na-smuklym-obcasie-high-heels-black-k0q11b04w-q11.html
#   pouf           round velvet pouffe with piping: dia 52 cm, H 40 cm (Art Deco pouf type)
#                  https://www.1stdibs.com/furniture/seating/ottomans-poufs/elegant-round-art-deco-poef-velvet-upholstery-france-ca-1925/id-f_43821202
#   window         arched casement (90-110 cm wide) with a fanlight, swag valance + tied-back curtains
#   floor          pale oak herringbone parquet with a border: 70 x 350 mm blocks; rug: round wool rug dia 2.4 m

# =====================================================================
#  SETTINGS  -  change these lines, then run the script again
# =====================================================================
ROOM_NAME = "fairytale_atelier"     # used for the output file names

ROOM_WIDTH = 5.0                    # metres, left to right
ROOM_DEPTH = 4.4                    # metres, front to back
WALL_HEIGHT = 3.1                   # metres

THEME = "morning_blush"             # pick one of the colour themes below
THEMES = {                          # any hex colour works; "main" is the room's hero colour (velvet)
    # "morning_blush": blush plaster, ivory panelling, champagne gold and sage, soft pink-white daylight.
    "morning_blush": {
        "background": "#F3E4E1", "wall": "#F4D8D4", "wall_trim": "#FDF6F0", "floor": "#E6D1BA", "floor_2": "#DBC3A8",
        "wood": "#D9B996", "main": "#E2A2AC", "accent_1": "#C77F8B", "accent_2": "#F2DDB4", "accent_3": "#A9B99A",
        "cream": "#FBF5EC", "plant": "#7F9A6E", "dark": "#4A363C", "gold": "#D8B36A", "glass": "#F1F6F7",
        "mirror": "#F2F3F6", "sky": "#F3E2E6", "paper": "#FFFCF6", "rug": "#F1DCD6", "curtain": "#B5C3A4",
        "sign": "#FBF2EA", "sign_ink": "#7A4652", "podium": "#E9C2C4",
        "gown_opal": "#F8F1E6", "gown_peony": "#F3B6C1", "gown_sage": "#BCC9AB", "gown_moon": "#CBC2DA",
        "gown_champ": "#EAD2A8", "gown_midnight": "#465486", "gown_form": "#F6D9DC",
    },
    # "midnight_ball": deep navy walls, silver instead of gold, lilac velvet; moonlight through the window and
    # the bulbs, candles and fairy lights glowing.  Lights are different: see NIGHT in the LIGHTS section.
    "midnight_ball": {
        "background": "#191B30", "wall": "#36406E", "wall_trim": "#4A558E", "floor": "#6E5C66", "floor_2": "#63525C",
        "wood": "#8A7A92", "main": "#8C79B8", "accent_1": "#B595D9", "accent_2": "#DCDFEA", "accent_3": "#7F96C9",
        "cream": "#ECE9F4", "plant": "#6F8E80", "dark": "#15162A", "gold": "#CDD1DC", "glass": "#E6ECF6",
        "mirror": "#C9D0E4", "sky": "#24325E", "paper": "#F4F2FA", "rug": "#4A4677", "curtain": "#5E5A93",
        "sign": "#222848", "sign_ink": "#E9EBF5", "podium": "#5D5390",
        "gown_opal": "#EEEAF6", "gown_peony": "#C9A6DD", "gown_sage": "#93AAA4", "gown_moon": "#AEB6D9",
        "gown_champ": "#D9CFC2", "gown_midnight": "#2E3A70", "gown_form": "#D7C7EA",
    },
}

SUN_WARMTH = 5600                   # Kelvin: 2500 = sunset orange, 6500 = white daylight (night: moonlight)
SUN_STRENGTH = 3.2
LAMP_WARMTH = 2700                  # Kelvin of the chandelier candles and the vanity bulbs
LAMP_STRENGTH = 45                  # Watts of the chandelier light
FAIRY_LIGHTS = True                 # tiny warm lights along the curtain swag
SEED = 5                            # change to shuffle perfume bottles, swatches, pins and props

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
NIGHT = THEME == "midnight_ball"    # moonlight, brighter bulbs and candles

STYLE = "fairytale_atelier"
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

# The room's real materials (one place, so every piece uses the same gilt, velvet, satin, paint...).
PLASTER = M("wall", 0.85, "plaster")               # blush (or navy) plaster walls
TRIM = M("wall_trim", 0.5, "plaster", scale=3)     # painted panelling, skirting, cornice
PAINT = M("cream", 0.45, "plaster", scale=3)       # painted furniture: dressing table, sewing table, pedestal
OAK = M("wood", 0.5, "wood")                       # beech / oak: easel, hangers' hooks block, sewing machine base
OAK_V = M("wood", 0.52, "wood", along="Z")
GOLD = M("gold", 0.28, "brushed", metal=1.0)       # polished brass / gilt (silver in the midnight theme)
GOLD_V = M("gold", 0.3, "brushed", metal=1.0, along="Z")
GILT = mat("gold", 0.25, metal=1.0, emit=0.1)      # gilded mouldings that catch the light
VELVET = M("main", 0.92, "fabric")                 # hero velvet: stool, pouf, podium
VELVET_2 = M("accent_1", 0.9, "fabric")
SATIN = M("accent_2", 0.86, "fabric", scale=0.5)   # champagne satin: hangers, ribbons, shoes
LINEN = M("cream", 0.9, "fabric")
CURTAIN = M("curtain", 0.9, "fabric")
RUG = M("rug", 0.95, "knit", scale=0.6)
PAPER = M("paper", 0.8, "paper")
KRAFT = M("accent_2", 0.85, "paper")
CERAMIC = M("cream", 0.3, "ceramic")
IRON = M("dark", 0.5, "brushed", metal=0.7)        # cast-iron dress-form base, sewing machine
GLASS = mat("glass", 0.05, alpha=0.16)
CRYSTAL = mat("glass", 0.03, emit=0.6 if NIGHT else 0.35, alpha=0.6)    # chandelier drops and tiara stones
MIRROR = mat("mirror", 0.12, metal=0.35, emit=0.18)  # silvered glass: pale and soft, so it reads as a mirror in a render
BULB = mat("bulb", 0.2, emit=9.0 if NIGHT else 5.0, color="#FFE6C2")    # vanity globe bulbs
FLAME = mat("flame", 0.3, emit=16.0 if NIGHT else 6.0, color="#FFC982")  # candle-bulb flames
FAIRY = mat("fairy", 0.3, emit=10.0 if NIGHT else 4.0, color="#FFD9A0")
SKY = mat("sky", 0.05, emit=0.45 if not NIGHT else 0.5, alpha=0.5)      # window: soft sky seen through glass
GLINT = mat("paper", 0.1, emit=0.9, alpha=0.3)     # reflection streaks on glass
INK = mat("dark", 0.6)                             # pencil lines on the croquis
SOIL = mat("soil", 0.95, color="#3A2A20")
LEAF = mat("plant", 0.55)


def GOWN(key, rough=0.78):
    """Gown fabric: satin / crepe with a fine weave and sheen, in a palette colour."""
    return M(key, rough, "fabric", scale=0.6)



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



def rod(name, a, b, r, material, r2=None, segs=12, parent=None):
    """Straight round bar from point a to point b (legs, braces, rails)."""
    a, b = Vector(a), Vector(b)
    o = cyl(name, r, (b - a).length, (a + b) / 2, material, r2=r2, segs=segs, bevel=0, parent=parent)
    o.rotation_euler = (b - a).to_track_quat("Z", "Y").to_euler()
    return o


def solidify(o, thick, offset=0.0):
    m = o.modifiers.new("Solidify", "SOLIDIFY")
    m.thickness, m.offset = thick, offset
    m.use_even_offset = True
    return o


def subsurf(o, levels=1):
    m = o.modifiers.new("Subsurf", "SUBSURF")
    m.levels = m.render_levels = levels
    return o


def mesh_obj(name, verts, faces, material, loc=(0, 0, 0), rot=(0, 0, 0), parent=None):
    me = bpy.data.meshes.new(name)
    me.from_pydata([tuple(v) for v in verts], [], faces)
    me.update()
    o = bpy.data.objects.new(name, me)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, 0, None, parent)


def arch_outline(w, h_rect, rise, n=18, inset=0.0):
    """(u, v) points round an arched-top opening: flat bottom at v = 0, straight sides up to h_rect, then an
    elliptical arch that rises `rise` more. inset shrinks it evenly (for frames and glass)."""
    hw, top = w / 2 - inset, h_rect
    pts = [(-hw, inset), (hw, inset)]
    for k in range(n + 1):
        a = math.pi * k / n
        pts.append((hw * math.cos(a), top + (rise - inset) * math.sin(a)))
    return pts


def wall_poly(name, pts, material, wall, at, parent=None, thick=0.0):
    """Flat shape from (u, v) points on a wall: wall='back' -> plane y = at (u = x), 'left' -> plane x = at (u = y).
    It faces into the room. thick > 0 adds a solidify towards the wall."""
    if wall == "back":
        vs = [(u, at, v) for u, v in pts]
    else:
        vs = [(at, u, v) for u, v in reversed(pts)]
    o = mesh_obj(name, vs, [list(range(len(vs)))], material, parent=parent)
    if thick:
        solidify(o, thick, 0.0)
    return o


def ring_band(name, outer, inner, material, wall, at, thick, parent=None):
    """Flat frame between two outlines with the same number of points (a gilt mirror or sign frame)."""
    n = len(outer)
    if wall == "back":
        vs = [(u, at, v) for u, v in outer] + [(u, at, v) for u, v in inner]
    else:
        vs = [(at, u, v) for u, v in outer] + [(at, u, v) for u, v in inner]
    faces = [(i, (i + 1) % n, n + (i + 1) % n, n + i) for i in range(n)]
    return solidify(mesh_obj(name, vs, faces, material, parent=parent), thick, 0.0)


def prof_r(prof, t):
    """Radius at height t (0 = waist, 1 = hem) from a few (t, r) control points, smoothly interpolated."""
    dense = spline([(pt, pr, 0) for pt, pr in prof], 10)
    for a, b in zip(dense, dense[1:]):
        if a.x <= t <= b.x:
            u = (t - a.x) / max(1e-6, b.x - a.x)
            return a.y + (b.y - a.y) * u
    return dense[-1].y if t > 0.5 else dense[0].y


def skirt(name, prof, z_top, z_hem, material, parent=None, loc=(0, 0, 0), t0=0.0, t1=1.0, grow=1.0, folds=10,
          amp=0.06, ys=0.72, ruffle=0.0, seed=1, n=24, segs=72, arc=None):
    """Gown skirt: a turned bell (radius profile `prof`) with soft folds that deepen towards the hem.
    t0..t1 builds only part of it (tulle tiers), arc=(a0, a1) leaves it open (a half-pinned drape).
    ys < 1 flattens it front-to-back, the way a gown hangs on a hanger."""
    rnd = random.Random(seed)
    ph = [rnd.uniform(0, 6.283) for _ in range(3)]
    full = arc is None
    a0, a1 = arc or (0.0, 2 * math.pi)
    cols = segs if full else segs + 1
    bm, rings = bmesh.new(), []
    for k in range(n + 1):
        t = t0 + (t1 - t0) * k / n
        r = prof_r(prof, t) * grow
        z = z_top + (z_hem - z_top) * t
        wv = t ** 1.4
        ring = []
        for i in range(cols):
            th = a0 + (a1 - a0) * i / segs
            f = 1 + amp * wv * math.sin(folds * th + ph[0] + 0.8 * math.sin(2 * th + ph[1]))
            if ruffle and k >= n - 3:
                f += ruffle * ((k - (n - 3)) / 3) * math.sin(26 * th + ph[2])
            zz = z + (0.012 * wv * math.sin(folds * th + ph[0]) if k == n else 0.0)
            ring.append(bm.verts.new((r * f * math.cos(th), r * f * math.sin(th) * ys, zz)))
        rings.append(ring)
    for a, b in zip(rings, rings[1:]):
        for i in range(cols if full else cols - 1):
            j = (i + 1) % cols
            bm.faces.new((a[i], a[j], b[j], b[i]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    o = _obj(name, bm)
    o.location = loc
    _finish(o, material, 0, None, parent)
    return solidify(o, 0.006)


# =====================================================================
#  ROOM SHELL: oak herringbone floor, plaster walls with panelling, arched window, swag curtains
# =====================================================================
box("Floor_Base", (W + T, D + T, 0.2), ((W - T) / 2, (D + T) / 2, -0.1), TRIM, bevel=0.02)
box("Floor_Joints", (W, D, 0.004), (W / 2, D / 2, 0.002), mat("dark", 0.9), bevel=0)   # dark gaps between blocks


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

# Left wall: one tall arched casement window in the middle (a turret-salon window).
WIN_C, WIN_W = 2.4, 1.1                     # window centre (y) and width
WIN_Y = (WIN_C - WIN_W / 2, WIN_C + WIN_W / 2)
SILL, SPRING = 0.92, 2.05                    # sill height and where the round arch starts
ARCH_R = WIN_W / 2                           # semicircular head: top of the opening at SPRING + 0.55
FX = -T / 2                                  # the window joinery sits in the middle of the wall
left = box("Wall_Left", (T, D + T, H), (-T / 2, (D + T) / 2, H / 2), PLASTER, bevel=0.0)
cut_box = box("Window_Cutter", (T * 3, WIN_W, SPRING - SILL), (-T / 2, WIN_C, (SILL + SPRING) / 2), mat("wall"),
              bevel=0.0)
cut_arch = cyl("Window_Cutter_Arch", ARCH_R, T * 3, (-T / 2, WIN_C, SPRING), mat("wall"), segs=48, bevel=0,
               rot=(0, R(90), 0))
for nm, cutter in (("Window", cut_box), ("Arch", cut_arch)):
    cutter.hide_render = cutter.hide_viewport = True
    boolean = left.modifiers.new(nm, "BOOLEAN")
    boolean.operation, boolean.object = "DIFFERENCE", cutter
box("Wall_Back", (W + T, T, H), ((W - T) / 2, D + T / 2, H / 2), PLASTER, bevel=0.0)

# Cornice on top of the walls (a stepped painted moulding) and a cove just under it.
box("Trim_Top_Back", (W + T + 0.04, T + 0.06, 0.08), ((W - T) / 2, D + T / 2, H + 0.04), TRIM, bevel=0.01)
box("Trim_Top_Left", (T + 0.06, D + T + 0.04, 0.08), (-T / 2, (D + T) / 2 - 0.02, H + 0.04), TRIM, bevel=0.01)
box("Cornice_Back", (W, 0.05, 0.07), (W / 2, D - 0.025, H - 0.035), TRIM, bevel=0.012)
box("Cornice_Left", (0.05, D, 0.07), (0.025, D / 2, H - 0.035), TRIM, bevel=0.012)

# Panelled walls (boiserie): skirting 120 mm, a dado rail at 86 cm, picture-frame mouldings below and above.
SK, DADO = 0.12, 0.86
box("Skirting_Back", (W, 0.018, SK), (W / 2, D - 0.009, FLOOR_Z + SK / 2), TRIM, bevel=0.004)
box("Skirting_Left", (0.018, D - 0.018, SK), (0.009, (D - 0.018) / 2, FLOOR_Z + SK / 2), TRIM, bevel=0.004)
box("Dado_Back", (W, 0.028, 0.045), (W / 2, D - 0.014, DADO), TRIM, bevel=0.006)
box("Dado_Left", (0.028, D - 0.028, 0.045), (0.014, (D - 0.028) / 2, DADO), TRIM, bevel=0.006)


def moulding(name, wall, cu, cz, w, h, fw=0.022, depth=0.012, material=None):
    """Rectangular picture-frame moulding planted on a wall (cu = x on the back wall, y on the left wall)."""
    m_ = material or TRIM
    for sz in (-1, 1):
        size = (w, depth, fw) if wall == "back" else (depth, w, fw)
        loc = (cu, D - depth / 2, cz + sz * (h - fw) / 2) if wall == "back" else (depth / 2, cu, cz + sz * (h - fw) / 2)
        box(f"{name}_H", size, loc, m_, bevel=0.004)
    for su in (-1, 1):
        size = (fw, depth, h - 2 * fw) if wall == "back" else (depth, fw, h - 2 * fw)
        loc = (cu + su * (w - fw) / 2, D - depth / 2, cz) if wall == "back" else (depth / 2, cu + su * (w - fw) / 2, cz)
        box(f"{name}_V", size, loc, m_, bevel=0.004)


LOW_Z, LOW_H = (FLOOR_Z + SK + DADO - 0.03) / 2 + 0.01, DADO - SK - 0.13      # lower panels between skirting + dado
n_back = 6
for k in range(n_back):
    pw = (W - 0.1) / n_back
    moulding("Panel_Low_Back", "back", 0.05 + pw * (k + 0.5), LOW_Z, pw - 0.12, LOW_H)
for k, (y0, y1) in enumerate(((0.05, 1.2), (1.2, 1.8), (1.8, 3.0), (3.0, 3.6), (3.6, D - 0.05))):
    moulding("Panel_Low_Left", "left", (y0 + y1) / 2, LOW_Z, y1 - y0 - 0.12, LOW_H)
UP_Z0, UP_Z1 = DADO + 0.16, H - 0.2                                           # tall upper panels
for nm, wall, c, w_ in (("Back_Corner", "back", 0.45, 0.62), ("Back_Vanity", "back", 4.38, 1.04),
                        ("Left_Front", "left", 0.92, 1.5), ("Left_Back", "left", 3.78, 0.95)):
    moulding(f"Panel_Up_{nm}", wall, c, (UP_Z0 + UP_Z1) / 2, w_, UP_Z1 - UP_Z0)
    moulding(f"Panel_Up_{nm}_Gilt", wall, c, (UP_Z0 + UP_Z1) / 2, w_ - 0.09, UP_Z1 - UP_Z0 - 0.09, fw=0.006,
             depth=0.008, material=GILT)

# Window: a painted frame with a fanlight (radial glazing bars) in the arch, a deep plaster reveal, an oak board.
WIN_PAINT = TRIM
for nm, size, loc in [
    ("Sill", (T + 0.06, WIN_W, 0.06), (FX - 0.02, WIN_C, SILL + 0.03)),
    ("Jamb_Front", (T + 0.02, 0.06, SPRING - SILL), (FX, WIN_Y[0] + 0.03, (SILL + SPRING) / 2)),
    ("Jamb_Back", (T + 0.02, 0.06, SPRING - SILL), (FX, WIN_Y[1] - 0.03, (SILL + SPRING) / 2)),
    ("Transom", (0.07, WIN_W, 0.05), (FX, WIN_C, SPRING)),
    ("Mullion", (0.06, 0.045, SPRING - SILL), (FX, WIN_C, (SILL + SPRING) / 2)),
    ("Bar_Low", (0.05, WIN_W, 0.03), (FX, WIN_C, SILL + (SPRING - SILL) * 0.5)),
]:
    box(f"Window_Frame_{nm}", size, loc, WIN_PAINT, bevel=0.006)


def arch_band(name, cy, cz, r_in, r_out, x0, x1, material, n=32):
    """Curved head of the window frame: a half-ring band extruded through the wall."""
    bm = bmesh.new()
    rows = []
    for k in range(n + 1):
        a = math.pi * k / n
        c, s = math.cos(a), math.sin(a)
        rows.append([bm.verts.new((x, cy + r * c, cz + r * s)) for x, r in ((x0, r_in), (x0, r_out), (x1, r_out),
                                                                             (x1, r_in))])
    for a, b in zip(rows, rows[1:]):
        for i in range(4):
            bm.faces.new((a[i], a[(i + 1) % 4], b[(i + 1) % 4], b[i]))
    for row in (rows[0], rows[-1]):
        bm.faces.new(row)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return _finish(_obj(name, bm), material, 0, None, None)


arch_band("Window_Frame_Arch", WIN_C, SPRING, ARCH_R - 0.06, ARCH_R + 0.002, FX - T / 2 - 0.01, FX + T / 2 + 0.01,
          WIN_PAINT)
for k, a in enumerate((R(45), R(90), R(135))):                     # fanlight: three radial glazing bars
    L = ARCH_R - 0.07
    box(f"Window_Fan_Bar_{k}", (0.04, L, 0.025), (FX, WIN_C + math.cos(a) * L / 2, SPRING + math.sin(a) * L / 2),
        WIN_PAINT, bevel=0.004, rot=(a, 0, 0))
tube("Window_Fan_Hub", [(FX, WIN_C + 0.12 * math.cos(math.pi * k / 16), SPRING + 0.12 * math.sin(math.pi * k / 16))
                        for k in range(17)], 0.016, WIN_PAINT, segs=8)
glass_pts = arch_outline(WIN_W, SPRING - SILL, ARCH_R, n=24)
no_shadow(wall_poly("Window_Glass", [(WIN_C + u, SILL + v) for u, v in glass_pts], SKY, "left", FX - 0.012))
for k, (dy, wdt, ln) in enumerate(((-0.28, 0.06, 0.5), (-0.18, 0.025, 0.4), (0.24, 0.05, 0.45))):
    no_shadow(box(f"Window_Glint_{k}", (0.002, wdt, ln), (FX - 0.006, WIN_C + dy, 1.35), GLINT, bevel=0,
                  rot=(R(-35), 0, 0)))
box("Window_Board", (0.17, WIN_W + 0.12, 0.03), (0.07, WIN_C, SILL + 0.015), OAK, bevel=0.005)

# What you see through the glass: a soft sky plane just outside (clouds by day, a moon and stars at night).
no_shadow(box("Sky_Backdrop", (0.01, 1.7, 2.2), (-0.36, WIN_C + 0.15, 1.7),
              mat("sky", 0.9, emit=0.75 if not NIGHT else 0.8), bevel=0))
if NIGHT:
    no_shadow(ball("Moon", 0.1, (-0.34, WIN_C + 0.32, 2.2), mat("moon", 0.5, emit=3.0, color="#F4F1E4"),
                   scale=(0.2, 1, 1)))
    for k in range(14):
        no_shadow(ball("Star", 0.006, (-0.345, WIN_C - 0.4 + random.random() * 1.0, 1.25 + random.random() * 1.3),
                       mat("star", 0.5, emit=6.0, color="#FFF6DE"), scale=(0.3, 1, 1), segs=8))
else:
    for k, (cy_, cz_, s_) in enumerate(((WIN_C - 0.1, 2.0, 0.12), (WIN_C + 0.15, 2.05, 0.09), (WIN_C + 0.45, 1.6, 0.1),
                                        (WIN_C + 0.3, 1.62, 0.07))):
        no_shadow(ball("Cloud", s_, (-0.345, cy_, cz_), mat("cloud", 0.9, emit=1.4, color="#FFFFFF"),
                       scale=(0.15, 1.8, 0.55), segs=14))


def tied_curtain(name, x0, y_out, y_in_top, y_tie, y_in_bot, top, z_tie, bot, material, folds=5, depth=0.07):
    """Floor-length curtain panel pulled back by a tie-back: full at the top, gathered at z_tie, flaring out to
    the floor. It hangs in the YZ plane of the left wall; pleats stand out along +X."""
    nu, nv = folds * 8, 28
    full = abs(y_in_top - y_out)
    verts = []
    for j in range(nv + 1):
        z = top - (top - bot) * j / nv
        if z >= z_tie:
            f = (top - z) / (top - z_tie)
            y_in = y_in_top + (y_tie - y_in_top) * (f * f * (3 - 2 * f))
        else:
            f = (z_tie - z) / (z_tie - bot)
            y_in = y_tie + (y_in_bot - y_tie) * f ** 0.7
        pd = depth * min(2.0, (full / max(abs(y_in - y_out), 0.05)) ** 0.5)
        for i in range(nu + 1):
            u = i / nu
            verts.append((x0 + pd * 0.5 * (1 - math.cos(2 * math.pi * folds * u)), y_out + (y_in - y_out) * u, z))
    faces = [(j * (nu + 1) + i, j * (nu + 1) + i + 1, (j + 1) * (nu + 1) + i + 1, (j + 1) * (nu + 1) + i)
             for j in range(nv) for i in range(nu)]
    return subsurf(solidify(mesh_obj(name, verts, faces, material), 0.006), 1)


# Curtain pole with finials and rings, a gathered swag valance across the top, two tied-back panels.
ROD_Z, ROD_X = SPRING + ARCH_R + 0.32, 0.1
rod_y = (WIN_Y[0] - 0.38, WIN_Y[1] + 0.38)
rod("Curtain_Pole", (ROD_X, rod_y[0], ROD_Z), (ROD_X, rod_y[1], ROD_Z), 0.016, GOLD, segs=16)
for sy, yy in ((-1, rod_y[0]), (1, rod_y[1])):
    ball("Curtain_Finial", 0.032, (ROD_X, yy + sy * 0.03, ROD_Z), GOLD)
    cyl("Curtain_Finial_Neck", 0.012, 0.03, (ROD_X, yy + sy * 0.005, ROD_Z), GOLD, rot=(R(90), 0, 0), segs=12)
    rod("Curtain_Bracket", (0.0, yy + sy * -0.06, ROD_Z), (ROD_X, yy + sy * -0.06, ROD_Z), 0.008, GOLD)
    cyl("Curtain_Bracket_Rose", 0.03, 0.01, (0.005, yy + sy * -0.06, ROD_Z), GOLD, rot=(0, R(90), 0), segs=16)
for k, (sag, dz, rr) in enumerate(((0.06, 0.0, 0.045), (0.1, -0.025, 0.045), (0.14, -0.05, 0.042), (0.17, -0.075, 0.04))):
    pts = [(ROD_X + 0.03 + 0.012 * k, rod_y[0] + 0.1 + (rod_y[1] - rod_y[0] - 0.2) * u,
            ROD_Z - 0.03 + dz - sag * math.sin(math.pi * u)) for u in (q / 16 for q in range(17))]
    subsurf(tube(f"Curtain_Swag_{k}", pts, rr, CURTAIN, segs=12), 1)
for sy in (-1, 1):                                                   # the swag's cascading tails at both ends
    yy = rod_y[0] + 0.12 if sy < 0 else rod_y[1] - 0.12
    ball("Curtain_Swag_Knot", 0.07, (ROD_X + 0.05, yy, ROD_Z - 0.05), CURTAIN, scale=(0.7, 1, 1.1))
if FAIRY_LIGHTS:                                                     # a strand of tiny warm lights along the swag
    pts = [(ROD_X + 0.11, rod_y[0] + 0.14 + (rod_y[1] - rod_y[0] - 0.28) * u,
            ROD_Z - 0.13 - 0.17 * math.sin(math.pi * u)) for u in (q / 24 for q in range(25))]
    tube("Fairy_Wire", pts, 0.0015, mat("dark", 0.5), segs=5)
    for k, p in enumerate(pts[1:-1]):
        no_shadow(ball("Fairy_Bulb", 0.009, p, FAIRY, segs=8))
TIE_Z = 1.15
for side, (y_out, y_in_top, y_tie, y_in_bot) in (("Front", (rod_y[0] + 0.05, WIN_Y[0] + 0.2, rod_y[0] + 0.22,
                                                            WIN_Y[0] + 0.0)),
                                                  ("Back", (rod_y[1] - 0.05, WIN_Y[1] - 0.2, rod_y[1] - 0.22,
                                                            WIN_Y[1] - 0.0))):
    tied_curtain(f"Curtain_{side}", 0.04, y_out, y_in_top, y_tie, y_in_bot, ROD_Z - 0.03, TIE_Z, FLOOR_Z + 0.01,
                 CURTAIN, folds=4, depth=0.06)
    yc = (y_out + y_tie) / 2
    tube(f"Curtain_Tieback_{side}", [(0.03, y_out, TIE_Z + 0.02), (0.13, yc, TIE_Z - 0.01), (0.07, y_tie + 0.03 *
         (1 if side == "Front" else -1), TIE_Z + 0.01)], 0.008, GOLD, segs=8)
    ball(f"Curtain_Tassel_{side}", 0.022, (0.12, yc, TIE_Z - 0.06), GOLD, scale=(1, 1, 1.8))
    cyl(f"Curtain_Holdback_{side}", 0.03, 0.03, (0.015, y_out, TIE_Z + 0.02), GOLD, rot=(0, R(90), 0), segs=16)


# =====================================================================
#  FURNITURE SLOTS  (same names in every template)
#  size = (width, depth, height); front of the furniture faces local -Y
# =====================================================================
PODIUM_XY, PODIUM_R, PODIUM_H = (2.35, 2.15), 0.45, 0.15       # round fitting podium in the middle of the salon
slot("clothes_rack", (2.9, 0.9, 2.12), (2.31, D - 0.45), shape="shelf")                       # curved gown rail
slot("vanity",       (1.05, 0.46, 1.5), (4.36, D - 0.24), shape="table")                       # table + bulb mirror
slot("stool",        (0.46, 0.46, 0.47), (4.36, D - 0.85), shape="stool")                      # tufted vanity stool
slot("mirror",       (0.72, 0.34, 1.82), (0.18, 3.76), turn=90, shape="frame")                 # gilt floor mirror
slot("hero_prop",    (0.84, 0.84, 1.48), PODIUM_XY, z=FLOOR_Z + PODIUM_H + 0.02, turn=45, kind="surface",
     shape="box")                                                                              # dress form on the podium
slot("pendant_lamp", (0.75, 0.75, 0.95), PODIUM_XY, z=H - 0.95, kind="hanging", shape="lamp")  # candle chandelier
slot("easel",        (0.62, 0.62, 1.78), (1.18, 0.95), turn=45, shape="frame")                 # sketch easel
slot("display_case", (0.5, 0.5, 1.45), (4.4, 1.5), turn=0, shape="cabinet")                    # tiara vitrine
slot("workbench",    (0.9, 0.5, 0.78), (0.3, WIN_C), turn=90, shape="table")                   # sewing table
slot("rug",          (2.4, 2.4, 0.012), (2.4, 2.0), kind="rug", shape="rug")                   # round wool rug


# =====================================================================
#  LIGHTS helper (the chandelier, the bulb mirror and the sign lamp carry their own lights)
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
    if parent is not None:                                   # keep the world position, follow the furniture
        bpy.context.view_layer.update()
        mw = o.matrix_world.copy()
        o.parent = parent
        o.matrix_parent_inverse = parent.matrix_world.inverted()
        o.matrix_world = mw
    return o


# =====================================================================
#  PLACEHOLDER FURNITURE  (replaced when you add your own with add_furniture.py)
# =====================================================================
# Six original gowns. Each is named after a gemstone or flower and has its own silhouette, so none of them
# reads as any film costume. style = skirt shape, neck = neckline / sleeves.
GOWNS = [
    {"name": "Moonstone", "key": "gown_moon", "style": "mermaid", "neck": "straps", "r_hem": 0.25, "waist": -0.56},
    {"name": "Sage", "key": "gown_sage", "style": "aline", "neck": "cap", "r_hem": 0.25, "waist": -0.55,
     "sash": True},
    {"name": "Peony", "key": "gown_peony", "style": "ball", "neck": "sweetheart", "r_hem": 0.31, "waist": -0.56,
     "tiers": True},
    {"name": "Opal", "key": "gown_opal", "style": "aline", "neck": "off", "r_hem": 0.27, "waist": -0.56},
    {"name": "Midnight", "key": "gown_midnight", "style": "aline", "neck": "halter", "r_hem": 0.27, "waist": -0.43},
    {"name": "Champagne", "key": "gown_champ", "style": "column", "neck": "straps", "r_hem": 0.19, "waist": -0.57},
]
HEM_Z = -1.72                                   # gown hem below the rail (rail at 2.0 m -> hem 28 cm off the floor)


def skirt_profile(style, rt, rh):
    """(t, radius) control points from the waist (t = 0) to the hem (t = 1)."""
    if style == "ball":
        return [(0, rt), (0.12, rt + 0.42 * (rh - rt)), (0.45, rt + 0.82 * (rh - rt)), (1, rh)]
    if style == "mermaid":
        return [(0, rt), (0.22, rt * 1.22), (0.58, rt * 0.98), (0.8, rt * 1.3), (1, rh)]
    if style == "column":
        return [(0, rt), (0.25, rt * 1.18), (0.7, rt * 1.2), (1, rh)]
    return [(0, rt), (0.5, rt + 0.52 * (rh - rt)), (1, rh)]               # A-line


def gown(spec, root, loc, turn, idx):
    """One gown on a satin padded hanger with a swivel hook. Built in the gown's own space: the rail is at
    z = 0, local x runs along the rail, the gown's front faces local -Y."""
    g = empty(f"Gown_{spec['name']}", loc, rot=(0, 0, turn), parent=root)
    fab = GOWN(spec["key"])
    zw, rt = spec["waist"], 0.125 if spec["waist"] < -0.5 else 0.14
    # brass swivel hook over the rail, then a 43 cm satin padded hanger
    tube("Hanger_Hook", spline([(0, 0, -0.115), (0, 0, -0.065), (0, -0.022, -0.03), (0, -0.021, 0.006), (0, 0, 0.027),
                                (0, 0.021, 0.01), (0, 0.022, -0.006)], 4), 0.0028, GOLD, parent=g, segs=8)
    tube("Hanger_Padded", spline([(-0.215, 0, -0.178), (-0.12, 0, -0.135), (0, 0, -0.118), (0.12, 0, -0.135),
                                  (0.215, 0, -0.178)], 5), 0.017, SATIN, parent=g, segs=12)
    ball("Hanger_Bow", 0.016, (0, -0.012, -0.112), SATIN, scale=(1.6, 0.6, 0.8), parent=g, segs=12)
    # card swing tag hung off the hanger arm, at the side so it does not sit on the bodice like a white blob
    box("Hanger_Tag", (0.002, 0.032, 0.045), (0.205, -0.004, -0.232), PAPER, bevel=0, rot=(R(6), 0, 0), parent=g)
    tube("Hanger_Tag_Thread", [(0.2, 0.0, -0.175), (0.204, -0.003, -0.192), (0.205, -0.004, -0.209)], 0.001,
         mat("dark", 0.6), parent=g, segs=4)
    # bodice: a shaped, boned bodice (flattened front-to-back like a gown on a hanger)
    top = -0.215 if spec["neck"] in ("sweetheart", "off") else -0.2
    rb = 0.152
    lathe("Gown_Bodice", [(0, zw - 0.005), (rt, zw), (rt * 1.04, zw + 0.08), (rb, zw + 0.25), (rb * 1.02, top - 0.045),
                          (rb * 0.93, top), (rb * 0.8, top - 0.008), (0, top - 0.014)], (0, 0, 0), fab, segs=40,
          parent=g, scale=(1, 0.64, 1))                  # neckline closed by the lining, so no dark "tube" opening
    # neckline binding: a fine piped edge round the top, so the bodice reads as a finished garment
    tube("Gown_Neckline", [(rb * 0.94 * math.cos(a), rb * 0.94 * 0.64 * math.sin(a), top - 0.003)
                           for a in (2 * math.pi * k / 48 for k in range(48))], 0.0055, fab, parent=g, closed=True,
         segs=6)
    tube("Gown_Waist_Seam", [(rt * 1.03 * math.cos(a), rt * 1.03 * 0.66 * math.sin(a), zw) for a in
                             (2 * math.pi * k / 28 for k in range(28))], 0.006, fab, parent=g, closed=True, segs=6)
    if spec["neck"] == "off":                       # off-the-shoulder band with soft draped sleeves
        tube("Gown_Offshoulder", [(0.172 * math.cos(a), 0.172 * 0.66 * math.sin(a), top - 0.035 + 0.012 * math.cos(2 * a))
                                  for a in (2 * math.pi * k / 32 for k in range(32))], 0.022, fab, parent=g,
             closed=True, segs=10)
        for sx in (-1, 1):                          # soft draped sleeves falling off the band, not puffs
            tube("Gown_Sleeve", spline([(sx * 0.16, -0.005, top - 0.03), (sx * 0.2, 0.0, top - 0.065),
                                        (sx * 0.215, 0.0, top - 0.12), (sx * 0.21, 0.0, top - 0.16)], 4), 0.028, fab,
                 parent=g, segs=12, r2=0.016)
    elif spec["neck"] == "cap":                     # little cap sleeves at the shoulders
        for sx in (-1, 1):
            ball("Gown_CapSleeve", 0.055, (sx * 0.152, 0, top - 0.02), fab, scale=(1, 0.72, 0.7), parent=g)
    elif spec["neck"] == "straps":                  # thin shoulder straps up to the hanger
        for sx in (-1, 1):
            tube("Gown_Strap", [(sx * 0.085, -0.07, top + 0.004), (sx * 0.11, -0.02, -0.15), (sx * 0.11, 0.0, -0.138),
                                (sx * 0.11, 0.02, -0.15), (sx * 0.085, 0.07, top + 0.004)], 0.004, fab, parent=g,
                 segs=6)
    elif spec["neck"] == "halter":                  # halter neck tied behind the hook
        for sx in (-1, 1):
            tube("Gown_Halter", [(sx * 0.07, -0.08, top + 0.004), (sx * 0.035, -0.04, -0.15), (0, -0.01, -0.12)],
                 0.01, fab, parent=g, segs=8)
    else:                                           # strapless sweetheart: ribbon loops on the hanger
        for sx in (-1, 1):
            tube("Gown_Loop", [(sx * 0.13, 0, top), (sx * 0.16, -0.01, -0.17), (sx * 0.17, 0, -0.16)], 0.003, SATIN,
                 parent=g, segs=5)
    # skirt (and layered tulle tiers for the ball gown)
    prof = skirt_profile(spec["style"], rt * 1.02, spec["r_hem"])
    folds = {"ball": 11, "aline": 9, "mermaid": 12, "column": 7}[spec["style"]]
    amp = {"ball": 0.07, "aline": 0.06, "mermaid": 0.05, "column": 0.035}[spec["style"]]
    skirt("Gown_Skirt", prof, zw, HEM_Z + random.uniform(-0.015, 0.015), fab, parent=g, folds=folds, amp=amp,
          seed=SEED + idx)
    if spec.get("tiers"):
        tulle = M(spec["key"], 0.84, "knit", scale=0.4)
        for k, (t0, t1) in enumerate(((0.0, 0.42), (0.36, 0.72))):      # upper tier overlaps the lower one
            skirt(f"Gown_Tier_{k}", prof, zw, HEM_Z, tulle, parent=g, t0=t0, t1=t1, grow=1.14 - 0.05 * k, folds=17,
                  amp=0.06, ruffle=0.0, seed=SEED + 10 + k, n=12)
    if spec.get("sash"):                            # satin sash with a bow at the front
        sash = M("accent_2", 0.87, "fabric", scale=0.5)
        tube("Gown_Sash", [(rt * 1.06 * math.cos(a), rt * 1.06 * 0.64 * math.sin(a), zw + 0.01) for a in
                           (2 * math.pi * k / 28 for k in range(28))], 0.018, sash, parent=g, closed=True, segs=8)
        for sx in (-1, 1):
            ball("Gown_Bow_Loop", 0.035, (sx * 0.035, -rt * 0.66 - 0.012, zw + 0.012), sash, scale=(1.1, 0.4, 0.7),
                 rot=(0, sx * R(20), 0), parent=g)
            tube("Gown_Bow_Tail", [(sx * 0.01, -rt * 0.66 - 0.015, zw), (sx * 0.03, -rt * 0.75 - 0.01, zw - 0.12),
                                   (sx * 0.045, -rt * 0.85 - 0.01, zw - 0.24)], 0.008, sash, parent=g, segs=6)
        ball("Gown_Bow_Knot", 0.014, (0, -rt * 0.66 - 0.018, zw + 0.012), sash, parent=g)
    return g


RAIL_Z = 2.0                                   # bar height of the gown rail


def build_clothes_rack():
    """Curved brass bridal rail: a 2.8 m bow on two uprights with domed weighted feet, two wall stays,
    ball finials, and six original gowns hung face-out on padded hangers."""
    root, w, d, h = furniture_root("clothes_rack")
    x0, x1, y_end, bow = -1.41, 1.41, d / 2 - 0.34, 0.3

    def rail_pt(s):
        return Vector((x0 + (x1 - x0) * s, y_end - bow * math.sin(math.pi * s), RAIL_Z))

    tube("Rail_Bar", [rail_pt(k / 40) for k in range(41)], 0.016, GOLD, parent=root, segs=14)
    for s in (0.0, 1.0):
        p = rail_pt(s)
        rod("Rail_Upright", (p.x, p.y, 0.03), (p.x, p.y, RAIL_Z), 0.018, GOLD_V, parent=root, segs=14)
        ball("Rail_Knuckle", 0.026, p, GOLD, parent=root)
        ball("Rail_Finial", 0.03, (p.x, p.y, RAIL_Z + 0.06), GOLD, parent=root)
        cyl("Rail_Finial_Neck", 0.011, 0.04, (p.x, p.y, RAIL_Z + 0.028), GOLD, segs=12, parent=root)
        lathe("Rail_Foot", [(0, 0), (0.15, 0), (0.15, 0.012), (0.12, 0.03), (0.05, 0.05), (0.03, 0.09), (0, 0.09)],
              (p.x, p.y, 0), GOLD, segs=40, parent=root)
        cyl("Rail_Collar", 0.026, 0.05, (p.x, p.y, 0.9), GOLD, segs=14, parent=root)
    for s in (0.34, 0.66):                         # wall stays hold the bow steady
        p = rail_pt(s)
        rod("Rail_Stay", (p.x, p.y, RAIL_Z), (p.x, d / 2 - 0.01, RAIL_Z), 0.011, GOLD, parent=root)
        cyl("Rail_Stay_Rose", 0.035, 0.012, (p.x, d / 2 - 0.006, RAIL_Z), GOLD, rot=(R(90), 0, 0), segs=20, parent=root)
        ball("Rail_Stay_Clip", 0.02, p, GOLD, parent=root)
    for k, spec in enumerate(GOWNS):
        s = 0.1 + 0.16 * k
        p = rail_pt(s)
        ang = math.atan2(-bow * math.pi * math.cos(math.pi * s), x1 - x0)
        gown(spec, root, p, ang, k)


def build_vanity():
    """Louis-style dressing table (cabriole legs, three drawers, gilt knobs) with a Hollywood bulb mirror,
    perfume bottles, a jewellery dish, a vase of peonies and a letter rack of invitations (your email)."""
    root, w, d, h = furniture_root("vanity")
    th = 0.76
    box("Vanity_Top", (w, d, 0.025), (0, 0, th - 0.0125), PAINT, bevel=0.006, parent=root)
    box("Vanity_Top_Edge", (w + 0.008, d + 0.008, 0.008), (0, 0, th - 0.03), GILT, bevel=0.002, parent=root)
    box("Vanity_Apron", (w - 0.07, d - 0.07, 0.12), (0, 0.005, th - 0.095), PAINT, bevel=0.004, parent=root)
    fy = -(d - 0.07) / 2 - 0.006
    for k, (cx, dw) in enumerate(((-0.33, 0.24), (0.0, 0.4), (0.33, 0.24))):
        box("Vanity_Drawer", (dw - 0.004, 0.014, 0.092), (cx, fy, th - 0.095), PAINT, bevel=0.004, parent=root)
        box("Vanity_Drawer_Bead", (dw - 0.04, 0.003, 0.06), (cx, fy - 0.008, th - 0.095), GILT, bevel=0.001, parent=root)
        box("Vanity_Drawer_Field", (dw - 0.05, 0.004, 0.05), (cx, fy - 0.009, th - 0.095), PAINT, bevel=0.001,
            parent=root)
        ball("Vanity_Knob", 0.011, (cx, fy - 0.017, th - 0.095), GOLD, parent=root, segs=12)
    for sx in (-1, 1):
        for sy in (-1, 1):
            lx, ly = sx * (w / 2 - 0.06), sy * (d / 2 - 0.06)
            tube("Vanity_Leg", spline([(lx, ly, th - 0.14), (lx + sx * 0.018, ly + sy * 0.018, th - 0.3),
                                       (lx - sx * 0.005, ly - sy * 0.005, 0.12), (lx + sx * 0.012, ly + sy * 0.012, 0.03)], 4),
                 0.018, PAINT, parent=root, segs=12, r2=0.01)
            ball("Vanity_Sabot", 0.016, (lx + sx * 0.014, ly + sy * 0.014, 0.022), GOLD, scale=(1, 1, 0.8), parent=root)
    # Hollywood mirror: 80 x 60 cm frame with 12 globe bulbs, leaning back a little on its stand
    mir = empty("Vanity_Mirror", (0, 0.07, th), rot=(R(-6), 0, 0), parent=root)
    box("Vanity_Mirror_Frame", (0.8, 0.035, 0.6), (0, 0, 0.32), PAINT, bevel=0.01, parent=mir)
    no_shadow(box("Vanity_Mirror_Glass", (0.64, 0.004, 0.44), (0, -0.0185, 0.32), MIRROR, bevel=0, parent=mir))
    for k, (dy, wdt) in enumerate(((-0.12, 0.05), (0.02, 0.02))):
        no_shadow(box("Vanity_Mirror_Glint", (wdt, 0.002, 0.34), (dy, -0.021, 0.32), GLINT, bevel=0,
                      rot=(0, R(-30), 0), parent=mir))
    for sx in (-1, 1):
        box("Vanity_Mirror_Foot", (0.06, 0.12, 0.02), (sx * 0.32, 0.0, 0.01), GOLD, bevel=0.004, parent=mir)
    bulbs = [(x, 0.57) for x in (-0.29, -0.1, 0.1, 0.29)] + [(sx * 0.355, z) for sx in (-1, 1) for z in (0.44, 0.32, 0.2)] + \
            [(x, 0.07) for x in (-0.1, 0.1)]
    for k, (bx, bz) in enumerate(bulbs):
        cyl("Vanity_Bulb_Socket", 0.012, 0.012, (bx, -0.022, bz), GOLD, rot=(R(90), 0, 0), segs=12, parent=mir)
        no_shadow(ball("Vanity_Bulb", 0.022, (bx, -0.045, bz), BULB, parent=mir, segs=14))
    light("Light_Vanity", "AREA", 34 if NIGHT else 16, kelvin(LAMP_WARMTH + 300),
          (root.location.x, root.location.y - 0.4, FLOOR_Z + th + 0.35), aim=(root.location.x, root.location.y - 1.2, 0.5),
          size=0.6, parent=root)
    # on the table: perfume bottles, a jewellery dish with pearls, peonies, a letter rack with invitations
    for k, (px, key, hh) in enumerate(((-0.42, "gown_peony", 0.1), (-0.35, "accent_3", 0.075), (-0.28, "gown_champ", 0.09))):
        lathe("Perfume_Bottle", [(0, 0), (0.026, 0), (0.03, 0.01), (0.03, hh * 0.7), (0.012, hh * 0.85), (0.008, hh),
                                 (0, hh)], (px, -0.1 + 0.03 * (k % 2), th), mat("glass", 0.05, alpha=0.4), segs=20, parent=root)
        cyl("Perfume_Fill", 0.025, hh * 0.55, (px, -0.1 + 0.03 * (k % 2), th + hh * 0.3), mat(key, 0.2), bevel=0.004,
            segs=16, parent=root)
        cyl("Perfume_Cap", 0.011, 0.025, (px, -0.1 + 0.03 * (k % 2), th + hh + 0.012), GOLD, segs=12, parent=root)
    ball("Perfume_Atomiser", 0.016, (-0.45, -0.02, th + 0.016), SATIN, scale=(1, 1, 0.8), parent=root, segs=12)
    lathe("Jewel_Dish", [(0, 0), (0.05, 0), (0.07, 0.012), (0.072, 0.016), (0.066, 0.014), (0.045, 0.006), (0, 0.006)],
          (-0.12, -0.08, th), GOLD, segs=28, parent=root)
    for k in range(9):
        a = k * 0.6
        ball("Pearl", 0.007, (-0.12 + 0.03 * math.cos(a) * (1 - k / 20), -0.08 + 0.03 * math.sin(a), th + 0.012),
             mat("pearl", 0.25, color="#FBF6EC"), parent=root, segs=8)
    vx, vy = 0.4, -0.06                                          # peonies in a fluted glass vase
    lathe("Vase", [(0, 0), (0.035, 0), (0.05, 0.05), (0.04, 0.12), (0.045, 0.15), (0.04, 0.15), (0.035, 0.12),
                   (0.044, 0.05), (0, 0.006)], (vx, vy, th), mat("glass", 0.05, alpha=0.35), segs=24, parent=root)
    for k, (dx, dy, dz, key) in enumerate(((0, 0, 0.24, "gown_peony"), (-0.06, 0.02, 0.21, "cream"),
                                           (0.055, 0.01, 0.2, "gown_peony"), (0.02, -0.05, 0.19, "accent_1"),
                                           (-0.03, 0.05, 0.25, "cream"))):
        tube("Peony_Stem", [(vx, vy, th + 0.05), (vx + dx * 0.6, vy + dy * 0.6, th + dz - 0.06), (vx + dx, vy + dy, th + dz)],
             0.003, LEAF, parent=root, segs=5)
        for j in range(3):                                        # three cupped layers of petals
            ball("Peony_Bloom", 0.042 - j * 0.01, (vx + dx, vy + dy, th + dz + j * 0.012), M(key, 0.8, "fabric"),
                 scale=(1, 1, 0.62), parent=root, segs=14)
    foliage("Peony_Leaves", [((vx, vy, th + 0.17), 0.08)], 26, (0.06, 0.022), LEAF, parent=root, seed=SEED + 4, droop=0.5)
    # letter rack: three sealed invitations standing up (click to email)
    lx = 0.18
    for sx in (-1, 1):
        tube("LetterRack_Hoop", [(lx + sx * 0.06, -0.05 + 0.03 * math.cos(a), th + 0.075 * math.sin(a)) for a in
                                 (math.pi * k / 10 for k in range(11))], 0.003, GOLD, parent=root, segs=6)
    box("LetterRack_Base", (0.14, 0.07, 0.008), (lx, -0.05, th + 0.004), GOLD, bevel=0.002, parent=root)
    env = None
    for k in range(3):
        e = box("Invitation", (0.16, 0.004, 0.11), (lx, -0.07 + k * 0.018, th + 0.064), PAPER if k != 1 else KRAFT,
                bevel=0.001, rot=(R(-8 + k * 6), 0, 0), parent=root)
        env = env or e
    ball("Invitation_Seal", 0.011, (lx, -0.074, th + 0.07), mat("accent_1", 0.35), scale=(1, 0.3, 1), parent=root, segs=12)
    hook_link(env, "email")


def build_stool():
    """Round button-tufted velvet vanity stool on four splayed gilt legs."""
    root, w, d, h = furniture_root("stool")
    r = w / 2 - 0.02
    cyl("Stool_Seat", r, 0.1, (0, 0, h - 0.05), VELVET, bevel=0.035, segs=40, parent=root)
    tube("Stool_Piping", ring_pts(r - 0.002, h - 0.1, 48), 0.006, VELVET, parent=root, closed=True, segs=6)
    tube("Stool_Apron", ring_pts(r - 0.03, h - 0.11, 48), 0.012, GOLD, parent=root, closed=True, segs=8)
    for k, (bx, by) in enumerate([(0, 0)] + [(0.1 * math.cos(a), 0.1 * math.sin(a)) for a in
                                             (2 * math.pi * q / 6 for q in range(6))]):
        ball("Stool_Button", 0.009, (bx, by, h - 0.004), VELVET_2, scale=(1, 1, 0.6), parent=root, segs=10)
    for k in range(4):
        a = R(45 + 90 * k)
        rod("Stool_Leg", (0.12 * math.cos(a), 0.12 * math.sin(a), h - 0.11), (0.18 * math.cos(a), 0.18 * math.sin(a), 0.02),
            0.014, GOLD, r2=0.009, parent=root)
        ball("Stool_Toe", 0.011, (0.18 * math.cos(a), 0.18 * math.sin(a), 0.012), GOLD, parent=root, segs=10)
    tube("Stool_Stretcher", ring_pts(0.155, 0.16, 40), 0.006, GOLD, parent=root, closed=True, segs=6)


def build_mirror():
    """Full-length leaner mirror with an arched top and a gilt frame, resting on the floor against the wall."""
    root, w, d, h = furniture_root("mirror")
    lean = math.atan2(d - 0.1, h)
    m_ = empty("Mirror_Leaner", (0, -d / 2 + 0.06, 0.0), rot=(-lean, 0, 0), parent=root)
    fw, rect, rise = 0.62, 1.42, 0.28
    outer = arch_outline(fw, rect, rise, n=22)
    inner = arch_outline(fw, rect, rise, n=22, inset=0.06)
    ring_band("Mirror_Frame", outer, inner, GILT, "back", 0.0, 0.04, parent=m_)
    ring_band("Mirror_Frame_Bead", arch_outline(fw, rect, rise, n=22, inset=0.052), inner, GOLD, "back", -0.026, 0.008,
              parent=m_)
    no_shadow(wall_poly("Mirror_Glass", arch_outline(fw, rect, rise, n=22, inset=0.055), MIRROR, "back", -0.004,
                        parent=m_))
    for k, (dx, wdt) in enumerate(((-0.1, 0.06), (0.06, 0.025))):
        no_shadow(box("Mirror_Glint", (wdt, 0.002, 0.9), (dx, -0.008, 0.85), GLINT, bevel=0, rot=(0, R(-28), 0),
                      parent=m_))
    for sx in (-1, 0, 1):                           # a gilded ribbon-bow ornament on top of the arch
        ball("Mirror_Bow", 0.04 if sx else 0.022, (sx * 0.05, -0.03, rect + rise + 0.005 - abs(sx) * 0.012), GILT,
             scale=(1.2 if sx else 1, 0.4, 0.75), rot=(0, sx * R(25), 0), parent=m_)


def build_hero_prop():
    """Professional dress form on a cast-iron caster base, wearing a half-pinned gown: bodice wrapped,
    the skirt draped round three quarters of the form, pins along the seam and a tape measure round the neck."""
    root, w, d, h = furniture_root("hero_prop")
    for k in range(4):                              # cross base with four casters
        a = R(45 + 90 * k)
        box("Form_Base_Leg", (0.2, 0.035, 0.025), (0.1 * math.cos(a), 0.1 * math.sin(a), 0.045), IRON, bevel=0.006,
            rot=(0, 0, a), parent=root)
        cyl("Form_Caster", 0.018, 0.02, (0.19 * math.cos(a), 0.19 * math.sin(a), 0.02), mat("dark", 0.4),
            rot=(R(90), 0, a), segs=14, parent=root)
    cyl("Form_Hub", 0.04, 0.05, (0, 0, 0.05), IRON, segs=20, parent=root)
    cyl("Form_Pole", 0.014, 0.8, (0, 0, 0.45), GOLD_V, segs=14, parent=root)
    cyl("Form_Collar", 0.022, 0.05, (0, 0, 0.62), GOLD, segs=14, parent=root)
    lathe("Form_Torso", [(0, 0.78), (0.15, 0.78), (0.172, 0.86), (0.163, 0.95), (0.125, 1.05), (0.13, 1.12), (0.163, 1.2),
                         (0.158, 1.27), (0.133, 1.33), (0.06, 1.36), (0.045, 1.37), (0.044, 1.42), (0.05, 1.43), (0, 1.44)],
          (0, 0, 0), LINEN, segs=40, parent=root, scale=(1, 0.72, 1))
    ball("Form_Neck_Cap", 0.04, (0, 0, 1.445), OAK, scale=(1, 1, 0.55), parent=root)
    fab = GOWN("gown_form")
    lathe("Form_Gown_Bodice", [(0, 1.03), (0.13, 1.03), (0.136, 1.12), (0.169, 1.2), (0.163, 1.26), (0.0, 1.265)],
          (0, 0, 0), fab, segs=40, parent=root, scale=(1, 0.73, 1))
    prof = [(0, 0.135), (0.1, 0.2), (0.45, 0.33), (1, 0.4)]
    skirt("Form_Petticoat", [(t, r * 0.93) for t, r in prof], 1.05, 0.015, M("cream", 0.85, "knit", scale=0.4),
          parent=root, folds=14, amp=0.04, ruffle=0.03, seed=SEED + 30)
    skirt("Form_Gown_Skirt", prof, 1.05, 0.01, fab, parent=root, folds=10, amp=0.07, seed=SEED + 31, ys=0.95,
          arc=(R(10), R(300)))                     # left open on the camera side: the petticoat shows through
    for k in range(9):                              # dressmaker's pins along the open seam and the waist
        t = k / 8
        a = R(6)
        r_ = prof_r(prof, t * 0.7)
        z = 1.05 + (0.01 - 1.05) * t * 0.7
        ball("Form_Pin", 0.006, (r_ * 1.04 * math.cos(a), r_ * 0.99 * math.sin(a), z), mat(("accent_1", "accent_3",
             "gold")[k % 3], 0.3), parent=root, segs=8)
    for k in range(8):
        a = R(-160 + k * 28)
        ball("Form_Waist_Pin", 0.006, (0.142 * math.cos(a), 0.142 * 0.75 * math.sin(a), 1.05), mat("gold", 0.3),
             parent=root, segs=8)
    for k in range(5):                              # a second row of pins along the other edge of the drape
        t = 0.1 + k * 0.15
        r_ = prof_r(prof, t)
        a = R(-56)
        ball("Form_Pin", 0.006, (r_ * 1.04 * math.cos(a), r_ * 0.99 * math.sin(a), 1.05 + (0.01 - 1.05) * t),
             mat(("gold", "accent_1")[k % 2], 0.3), parent=root, segs=8)
    # champagne satin sash tied in a bow at the front waist
    sash = M("accent_2", 0.86, "fabric", scale=0.5)
    tube("Form_Sash", [(0.142 * math.cos(a), 0.142 * 0.76 * math.sin(a), 1.045) for a in
                       (2 * math.pi * k / 32 for k in range(32))], 0.02, sash, parent=root, closed=True, segs=8)
    for sx in (-1, 1):
        ball("Form_Bow_Loop", 0.055, (sx * 0.055, -0.118, 1.05), sash, scale=(1.1, 0.35, 0.65), rot=(0, sx * R(18), 0),
             parent=root)
    ball("Form_Bow_Knot", 0.022, (0, -0.124, 1.05), sash, scale=(1, 0.7, 1), parent=root)
    tape = mat("tape", 0.6, color="#F0CF73")
    for sx in (-1, 1):                              # tape measure round the neck, both ends hanging down the front
        tube("Form_Tape", spline([(sx * 0.052, 0.01, 1.4), (sx * 0.06, -0.06, 1.37), (sx * 0.07, -0.103, 1.31),
                                  (sx * 0.075, -0.128, 1.24), (sx * 0.072, -0.12, 1.16), (sx * 0.07 + 0.01, -0.112, 1.08)], 4),
             0.006, tape, parent=root, segs=6).scale = (1, 1, 1)
    tube("Form_Tape_Neck", [(0.052 * math.cos(a), 0.04 * math.sin(a) + 0.0, 1.4) for a in
                            (R(-60) + R(300) * k / 20 for k in range(21))], 0.006, tape, parent=root, segs=6)


def build_pendant_lamp():
    """Six-arm brass candle chandelier with crystal drops and bead swags, on a chain."""
    root, w, d, h = furniture_root("pendant_lamp")
    lathe("Chandelier_Column", [(0, 0.075), (0.05, 0.085), (0.062, 0.12), (0.036, 0.17), (0.046, 0.23), (0.03, 0.29),
                                (0.042, 0.36), (0.02, 0.42), (0.026, 0.5), (0, 0.52)], (0, 0, 0), GOLD, segs=28, parent=root)
    ball("Chandelier_Finial", 0.028, (0, 0, 0.065), GOLD, parent=root, segs=16)
    no_shadow(ball("Chandelier_Drop", 0.022, (0, 0, 0.02), CRYSTAL, scale=(1, 1, 1.7), parent=root, segs=14))
    tips = []
    for k in range(6):
        a = 2 * math.pi * k / 6 + R(30)
        ca, sa = math.cos(a), math.sin(a)
        tube("Chandelier_Arm", spline([(0.04 * ca, 0.04 * sa, 0.2), (0.13 * ca, 0.13 * sa, 0.13), (0.23 * ca, 0.23 * sa, 0.15),
                                       (0.29 * ca, 0.29 * sa, 0.22), (0.29 * ca, 0.29 * sa, 0.26)], 4), 0.009, GOLD,
             parent=root, segs=10)
        tx, ty = 0.29 * ca, 0.29 * sa
        lathe("Chandelier_Bobeche", [(0, 0), (0.014, 0), (0.044, 0.012), (0.046, 0.016), (0.04, 0.015), (0.014, 0.01),
                                     (0, 0.01)], (tx, ty, 0.26), GOLD, segs=20, parent=root)
        cyl("Chandelier_Candle", 0.012, 0.075, (tx, ty, 0.3075), mat("cream", 0.5), segs=14, parent=root)
        no_shadow(ball("Chandelier_Flame", 0.012, (tx, ty, 0.36), FLAME, scale=(1, 1, 1.7), parent=root, segs=12))
        for j in (-1, 1):
            no_shadow(ball("Chandelier_Prism", 0.01, (tx + 0.04 * math.cos(a + j * 0.5), ty + 0.04 * math.sin(a + j * 0.5),
                                                      0.235), CRYSTAL, scale=(1, 1, 1.9), parent=root, segs=10))
        no_shadow(ball("Chandelier_Arm_Drop", 0.016, (0.13 * ca, 0.13 * sa, 0.095), CRYSTAL, scale=(1, 1, 1.8),
                       parent=root, segs=12))
        tips.append((a, tx, ty))
    for k in range(6):                              # bead swags between the arms
        a0, a1 = tips[k][0], tips[(k + 1) % 6][0]
        pts = []
        for q in range(9):
            u = q / 8
            a = a0 + (a1 - a0 if k < 5 else a1 + 2 * math.pi - a0) * u
            pts.append((0.27 * math.cos(a), 0.27 * math.sin(a), 0.245 - 0.07 * math.sin(math.pi * u)))
        no_shadow(tube("Chandelier_Swag", pts, 0.004, CRYSTAL, parent=root, segs=5))
    tube("Chandelier_Crown", ring_pts(0.09, 0.46, 24), 0.006, GOLD, parent=root, closed=True, segs=6)
    for k in range(8):
        a = 2 * math.pi * k / 8
        no_shadow(ball("Chandelier_Crown_Drop", 0.008, (0.09 * math.cos(a), 0.09 * math.sin(a), 0.435), CRYSTAL,
                       scale=(1, 1, 1.8), parent=root, segs=8))
        rod("Chandelier_Crown_Spoke", (0.02 * math.cos(a), 0.02 * math.sin(a), 0.49), (0.09 * math.cos(a), 0.09 * math.sin(a),
            0.46), 0.003, GOLD, parent=root)
    for k in range(11):                             # chain links up to the ceiling
        z = 0.54 + k * 0.038
        cyl("Chandelier_Link", 0.009, 0.03, (0, 0, z), GOLD, segs=10, bevel=0.004,
            rot=(0, 0, R(90 * (k % 2))), parent=root).scale = (1, 0.35, 1)
    light("Light_Chandelier", "POINT", LAMP_STRENGTH * (4.6 if NIGHT else 1.0), kelvin(LAMP_WARMTH),
          (root.location.x, root.location.y, root.location.z + 0.3), size=0.25, parent=root)


def build_easel():
    """French beech A-frame studio easel holding a croquis board (your first project)."""
    root, w, d, h = furniture_root("easel")
    for sx in (-1, 1):
        rod("Easel_Leg", (sx * 0.25, -0.17, 0.0), (sx * 0.05, 0.02, 1.72), 0.017, OAK_V, segs=10, parent=root)
    rod("Easel_Back_Leg", (0, 0.29, 0.0), (0, 0.03, 1.56), 0.016, OAK_V, segs=10, parent=root)
    rod("Easel_Mast", (0, -0.1, 0.6), (0, 0.025, 1.78), 0.015, OAK_V, segs=10, parent=root)
    box("Easel_Brace", (0.42, 0.02, 0.03), (0, -0.125, 0.42), OAK, bevel=0.004, parent=root)
    box("Easel_Tray", (0.56, 0.075, 0.022), (0, -0.115, 0.615), OAK, bevel=0.004, parent=root)
    box("Easel_Tray_Lip", (0.56, 0.008, 0.03), (0, -0.152, 0.635), OAK, bevel=0.002, parent=root)
    cv = empty("Easel_Canvas", (0, -0.112, 0.626), rot=(R(-6), 0, 0), parent=root)
    box("Croquis_Board", (0.5, 0.02, 0.66), (0, 0, 0.33), PAPER, bevel=0.003, parent=cv)
    box("Easel_Clamp", (0.08, 0.04, 0.035), (0, 0.0, 0.67), OAK, bevel=0.004, parent=cv)
    canvas = hook_image("canvas", 1, (0.46, 0.62), (0, -0.0105, 0.33), parent=cv, default_key="paper")
    # default croquis: a quick fashion sketch with a watercolour wash (hidden when a project image is applied)
    y_ = -0.012
    sk = [ball("Croquis_Head", 0.022, (0, y_, 0.57), INK, scale=(0.8, 0.05, 1), parent=cv, segs=12)]
    for pts in ([(0, 0.545), (0, 0.52)], [(-0.035, 0.515), (-0.03, 0.44), (-0.022, 0.4)],
                [(0.035, 0.515), (0.03, 0.44), (0.022, 0.4)], [(-0.022, 0.4), (-0.1, 0.25), (-0.17, 0.09)],
                [(0.022, 0.4), (0.1, 0.25), (0.17, 0.09)], [(-0.17, 0.09), (-0.06, 0.075), (0.06, 0.08), (0.17, 0.09)]):
        sk.append(tube("Croquis_Line", spline([(x, y_, z) for x, z in pts], 4), 0.0018, INK, parent=cv, segs=5))
    wash = mesh_obj("Croquis_Wash", [(-0.02, y_ + 0.001, 0.4), (0.02, y_ + 0.001, 0.4), (0.16, y_ + 0.001, 0.095),
                                     (-0.16, y_ + 0.001, 0.095)], [(0, 1, 2, 3)], GOWN("gown_peony"), parent=cv)
    sk.append(wash)
    for k, key in enumerate(("gown_peony", "gown_sage", "gown_champ")):
        sk.append(box("Croquis_Swatch", (0.04, 0.002, 0.03), (0.16, y_, 0.55 - k * 0.045), mat(key, 0.8), bevel=0,
                      parent=cv))
    hook_default(canvas, *sk)
    cyl("Easel_Pencil", 0.004, 0.17, (0.1, -0.13, 0.632), mat("accent_2", 0.6), rot=(0, R(90), 0), segs=8, parent=root)


def build_display_case():
    """Pedestal vitrine: a painted column with gilt mouldings and a glass hood over a velvet cushion and tiara."""
    root, w, d, h = furniture_root("display_case")
    box("Case_Plinth", (0.48, 0.48, 0.08), (0, 0, 0.04), PAINT, bevel=0.006, parent=root)
    box("Case_Shaft", (0.4, 0.4, 0.86), (0, 0, 0.51), PAINT, bevel=0.004, parent=root)
    for k in range(4):                              # gilt panel mouldings on the four faces
        a = R(90 * k)
        for dz, hh in ((0.0, 0.62),):
            frame = empty("Case_Panel", (0.201 * math.sin(a), -0.201 * math.cos(a), 0.51), rot=(0, 0, a), parent=root)
            for sz in (-1, 1):
                box("Case_Panel_H", (0.28, 0.006, 0.012), (0, 0, sz * hh / 2), GILT, bevel=0.001, parent=frame)
                box("Case_Panel_V", (0.012, 0.006, hh), (sz * 0.14, 0, 0), GILT, bevel=0.001, parent=frame)
    box("Case_Capital", (0.48, 0.48, 0.05), (0, 0, 0.965), PAINT, bevel=0.008, parent=root)
    box("Case_Capital_Gilt", (0.485, 0.485, 0.012), (0, 0, 0.94), GILT, bevel=0.002, parent=root)
    gz0, gs, gh = 0.99, 0.42, 0.4                   # glass hood
    for nm, size, loc in (("Front", (gs, 0.006, gh), (0, -gs / 2, gz0 + gh / 2)), ("Back", (gs, 0.006, gh), (0, gs / 2, gz0 + gh / 2)),
                          ("Left", (0.006, gs, gh), (-gs / 2, 0, gz0 + gh / 2)), ("Right", (0.006, gs, gh), (gs / 2, 0, gz0 + gh / 2)),
                          ("Top", (gs, gs, 0.006), (0, 0, gz0 + gh))):
        no_shadow(box(f"Case_Glass_{nm}", size, loc, GLASS, bevel=0, parent=root))
    for sx in (-1, 1):
        for sy in (-1, 1):
            box("Case_Glass_Post", (0.014, 0.014, gh), (sx * gs / 2, sy * gs / 2, gz0 + gh / 2), GOLD, bevel=0.002, parent=root)
    for nm, size, loc in (("F", (gs + 0.014, 0.014, 0.014), (0, -gs / 2, gz0 + gh)), ("B", (gs + 0.014, 0.014, 0.014), (0, gs / 2, gz0 + gh)),
                          ("L", (0.014, gs, 0.014), (-gs / 2, 0, gz0 + gh)), ("Rt", (0.014, gs, 0.014), (gs / 2, 0, gz0 + gh))):
        box(f"Case_Glass_Rail_{nm}", size, loc, GOLD, bevel=0.002, parent=root)
    ball("Case_Finial", 0.02, (0, 0, gz0 + gh + 0.025), GOLD, parent=root)
    no_shadow(box("Case_Glint", (0.05, 0.002, 0.3), (-0.08, -gs / 2 - 0.004, gz0 + gh / 2), GLINT, bevel=0,
                  rot=(0, R(-30), 0), parent=root))
    box("Case_Cushion", (0.26, 0.2, 0.06), (0, 0.02, gz0 + 0.03), VELVET_2, bevel=0.025, parent=root)
    for sx in (-1, 1):
        for sy in (-1, 1):
            ball("Case_Cushion_Tassel", 0.01, (sx * 0.13, 0.02 + sy * 0.1, gz0 + 0.03), GOLD, scale=(1, 1, 1.6), parent=root,
                 segs=8)
    # tiara: an original floral band with seven rising sprays, each tipped with a crystal
    tz, tr = gz0 + 0.064, 0.088                     # 17.6 cm across, 8 cm tall at the centre
    band = [(tr * math.cos(a), 0.03 + tr * 0.6 * math.sin(a), tz) for a in (math.pi + math.pi * k / 16 for k in range(17))]
    tube("Tiara_Band", band, 0.005, GOLD, parent=root, segs=6)
    for k in range(7):
        a = math.pi + math.pi * (k + 0.5) / 7
        bx, by = tr * math.cos(a), 0.03 + tr * 0.6 * math.sin(a)
        hh = 0.034 + 0.046 * math.sin(math.pi * (k + 0.5) / 7) ** 2
        tube("Tiara_Spray", spline([(bx - 0.008, by, tz), (bx - 0.006, by - 0.004, tz + hh * 0.6), (bx, by - 0.006, tz + hh),
                                    (bx + 0.006, by - 0.004, tz + hh * 0.6), (bx + 0.008, by, tz)], 3), 0.0028, GOLD,
             parent=root, segs=5)
        no_shadow(ball("Tiara_Stone", 0.0075 + 0.004 * (k == 3), (bx, by - 0.007, tz + hh + 0.006), CRYSTAL, parent=root,
                       segs=10))
        ball("Tiara_Pearl", 0.004, (bx, by - 0.004, tz + 0.012), mat("pearl", 0.25, color="#FBF6EC"), parent=root, segs=8)


def build_workbench():
    """Painted sewing table with turned legs and a drawer, a retro sewing machine, thread, scissors, pincushion."""
    root, w, d, h = furniture_root("workbench")
    box("Sew_Top", (w, d, 0.025), (0, 0, h - 0.0125), PAINT, bevel=0.005, parent=root)
    box("Sew_Apron", (w - 0.08, d - 0.08, 0.1), (0, 0, h - 0.075), PAINT, bevel=0.003, parent=root)
    box("Sew_Drawer", (0.36, 0.012, 0.075), (0.18, -(d - 0.08) / 2 - 0.006, h - 0.075), PAINT, bevel=0.003, parent=root)
    ball("Sew_Drawer_Knob", 0.011, (0.18, -(d - 0.08) / 2 - 0.016, h - 0.075), GOLD, parent=root, segs=12)
    for sx in (-1, 1):
        for sy in (-1, 1):
            lathe("Sew_Leg", [(0, 0), (0.016, 0), (0.014, 0.05), (0.02, 0.08), (0.015, 0.12), (0.017, 0.5), (0.024, 0.55),
                              (0.022, h - 0.12), (0.024, h - 0.12), (0, h - 0.12)], (sx * (w / 2 - 0.05), sy * (d / 2 - 0.05), 0),
                  PAINT, segs=16, parent=root)
    top = h
    body = M("accent_3", 0.3, "ceramic")             # enamelled machine body
    mx, my = -0.05, 0.03
    box("Machine_Bed", (0.42, 0.19, 0.05), (mx, my, top + 0.025), body, bevel=0.012, parent=root)
    box("Machine_Pillar", (0.08, 0.1, 0.2), (mx + 0.15, my + 0.02, top + 0.15), body, bevel=0.02, parent=root)
    box("Machine_Arm", (0.36, 0.085, 0.075), (mx + 0.01, my + 0.02, top + 0.21), body, bevel=0.025, parent=root)
    box("Machine_Head", (0.075, 0.095, 0.16), (mx - 0.15, my + 0.015, top + 0.17), body, bevel=0.018, parent=root)
    box("Machine_Stripe", (0.3, 0.002, 0.012), (mx + 0.0, my - 0.023, top + 0.215), mat("cream", 0.4), bevel=0, parent=root)
    cyl("Machine_Needle_Bar", 0.004, 0.07, (mx - 0.16, my - 0.02, top + 0.08), mat("metal", 0.2, metal=1.0, color="#D8D8DC"),
        segs=8, parent=root)
    box("Machine_Foot", (0.02, 0.03, 0.006), (mx - 0.16, my - 0.02, top + 0.053), mat("metal", 0.2, metal=1.0, color="#D8D8DC"),
        bevel=0.002, parent=root)
    cyl("Machine_Handwheel", 0.045, 0.025, (mx + 0.205, my + 0.02, top + 0.2), mat("cream", 0.35), rot=(0, R(90), 0), segs=24,
        parent=root)
    cyl("Machine_Spool_Pin", 0.003, 0.05, (mx + 0.08, my + 0.02, top + 0.27), GOLD, segs=6, parent=root)
    cyl("Machine_Spool", 0.013, 0.035, (mx + 0.08, my + 0.02, top + 0.265), mat("accent_1", 0.6), segs=14, parent=root)
    box("Sew_Fabric", (0.34, 0.24, 0.004), (mx - 0.12, my - 0.08, top + 0.002), GOWN("gown_opal"), bevel=0.001,
        rot=(0, 0, R(12)), parent=root)
    for k, key in enumerate(("gown_peony", "gown_sage", "gown_moon", "gold")):
        cyl("Thread_Spool", 0.014, 0.04, (0.3 + 0.035 * (k % 2), 0.12 - 0.035 * (k // 2), top + 0.02), mat(key, 0.6),
            segs=14, parent=root)
    ball("Pincushion", 0.035, (0.28, -0.12, top + 0.025), VELVET_2, scale=(1, 1, 0.7), parent=root)
    for k in range(6):
        a = k * 1.05
        ball("Pincushion_Pin", 0.005, (0.28 + 0.025 * math.cos(a), -0.12 + 0.025 * math.sin(a), top + 0.05),
             mat(("gold", "accent_3", "cream")[k % 3], 0.3), parent=root, segs=6)
    for sx in (-1, 1):                              # dressmaker's shears
        tube("Shears_Blade", [(0.12, -0.15 + sx * 0.004, top + 0.004), (0.24, -0.17 + sx * 0.01, top + 0.004)], 0.004,
             mat("metal", 0.2, metal=1.0, color="#D8D8DC"), parent=root, segs=6)
        tube("Shears_Ring", ring_pts(0.016, top + 0.004, 14, 0.095, -0.145 + sx * 0.02), 0.004, mat("dark", 0.4),
             parent=root, closed=True, segs=6)


def build_rug():
    """Round wool rug with a darker border ring."""
    root, w, d, h = furniture_root("rug")
    cyl("Rug", w / 2, h, (0, 0, h / 2), RUG, segs=72, bevel=0.004, parent=root)
    for nm, rr, tr in (("Rug_Border", w / 2 - 0.09, 0.022), ("Rug_Border_2", w / 2 - 0.16, 0.008)):
        o = tube(nm, ring_pts(rr, 0.0, 96), tr, M("podium", 0.95, "knit", scale=0.6), parent=root, closed=True, segs=6)
        o.location, o.scale = (0, 0, h), (1, 1, 0.12)        # a flat woven band just proud of the pile


PLACEHOLDERS = {
    "clothes_rack": build_clothes_rack, "vanity": build_vanity, "stool": build_stool, "mirror": build_mirror,
    "hero_prop": build_hero_prop, "pendant_lamp": build_pendant_lamp, "easel": build_easel,
    "display_case": build_display_case, "workbench": build_workbench, "rug": build_rug,
}

if SHOW_PLACEHOLDER_FURNITURE:
    for slot_name, build in PLACEHOLDERS.items():
        build()

# =====================================================================
#  DECORATION: fitting podium, pouf + shopping bag, heels, hat boxes, candles
# =====================================================================
px_, py_ = PODIUM_XY
cyl("Podium_Plinth", PODIUM_R - 0.02, 0.1, (px_, py_, FLOOR_Z + 0.06), PAINT, segs=72, bevel=0.006)
cyl("Podium_Toe", PODIUM_R - 0.035, 0.012, (px_, py_, FLOOR_Z + 0.006), mat("dark", 0.6), segs=72, bevel=0.002)
tube("Podium_Gilt_Band", ring_pts(PODIUM_R - 0.018, FLOOR_Z + 0.105, 96, px_, py_), 0.008, GILT, closed=True, segs=6)
cyl("Podium_Top", PODIUM_R, 0.045, (px_, py_, FLOOR_Z + PODIUM_H - 0.0225 + 0.02), M("podium", 0.92, "fabric"), segs=72,
    bevel=0.016)
ball("Podium_Pincushion", 0.04, (px_ + 0.3, py_ - 0.26, FLOOR_Z + PODIUM_H + 0.045), VELVET_2, scale=(1, 1, 0.7))
for k in range(6):
    a = k * 1.05
    ball("Podium_Pin", 0.005, (px_ + 0.3 + 0.028 * math.cos(a), py_ - 0.26 + 0.028 * math.sin(a), FLOOR_Z + PODIUM_H + 0.07),
         mat(("gold", "accent_3", "cream")[k % 3], 0.3), segs=6)

# Round velvet pouf with piping and a centre button; a boutique shopping bag with tissue sits on it (your website).
POUF_XY = (3.22, 1.22)
POUF = M("accent_3", 0.93, "fabric")
cyl("Pouf", 0.26, 0.4, (POUF_XY[0], POUF_XY[1], FLOOR_Z + 0.2), POUF, segs=56, bevel=0.07)
for z in (FLOOR_Z + 0.07, FLOOR_Z + 0.33):
    tube("Pouf_Piping", ring_pts(0.258, z, 56, *POUF_XY), 0.007, POUF, closed=True, segs=6)
ball("Pouf_Button", 0.016, (POUF_XY[0], POUF_XY[1], FLOOR_Z + 0.4), GOLD, scale=(1, 1, 0.5))
bag = empty("Shopping_Bag", (POUF_XY[0] + 0.03, POUF_XY[1] - 0.02, FLOOR_Z + 0.395), rot=(0, 0, R(30)))
BAG = M("accent_1", 0.6, "paper")
body = box("Bag_Body", (0.26, 0.11, 0.28), (0, 0, 0.14), BAG, bevel=0.004, parent=bag)
hook_link(body, "website")
box("Bag_Fold", (0.262, 0.112, 0.03), (0, 0, 0.265), M("cream", 0.7, "paper"), bevel=0.003, parent=bag)
for sy in (-1, 1):
    tube("Bag_Handle", spline([(-0.06, sy * 0.05, 0.27), (-0.04, sy * 0.05, 0.36), (0.04, sy * 0.05, 0.36),
                               (0.06, sy * 0.05, 0.27)], 4), 0.004, SATIN, parent=bag, segs=6)
for k, (dx, dz, s) in enumerate(((-0.05, 0.3, 0.06), (0.04, 0.31, 0.055), (0.0, 0.33, 0.05))):
    ball("Bag_Tissue", s, (dx, 0, dz), PAPER, scale=(1, 0.6, 0.8), rot=(0, R(20 * k), 0), parent=bag, segs=12)


def heel(name, loc, turn, material):
    """Satin court shoe (pump), 25 cm long with an 8.5 cm stiletto: a lofted upper with a pointed toe box,
    an open topline that shows the insole, a sloping sole and a slim heel. Toe points to local -X."""
    e = empty(name, loc, rot=(0, 0, turn))
    L, HH, n = 0.25, 0.085, 28

    def sole_z(s):                                   # s = 0 at the toe tip, 1 at the back of the heel
        u = min(1.0, max(0.0, (s - 0.38) / 0.5))
        return 0.004 + HH * u * u * (3 - 2 * u)

    def half_w(s):
        return 0.034 * min(1.0, (s / 0.3) ** 0.55) * (1 - 0.3 * max(0.0, s - 0.45))

    def wall_h(s):                                   # toe box -> low sides at the throat -> heel counter
        return 0.036 if s < 0.3 else 0.036 - 0.016 * min(1.0, (s - 0.3) / 0.2) + 0.03 * max(0.0, s - 0.7) / 0.3

    outline = []
    for i in range(n):
        a = 2 * math.pi * i / n
        s = 0.5 - 0.5 * math.cos(a)
        outline.append((s, -L / 2 + L * s, half_w(s) * math.sin(a) * (1.0 if s > 0.02 else 0.0)))
    bm = bmesh.new()
    bot = [bm.verts.new((x, y, sole_z(s))) for s, x, y in outline]
    top = [bm.verts.new((x, y, sole_z(s) + wall_h(s))) for s, x, y in outline]
    for i in range(n):
        j = (i + 1) % n
        bm.faces.new((bot[i], bot[j], top[j], top[i]))
    bm.faces.new(list(reversed(bot)))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    upper = _obj(f"{name}_Upper", bm)
    _finish(upper, material, 0, None, e)
    solidify(upper, 0.003)
    # vamp: the covered toe box, a soft dome over the front 30 %
    ball(f"{name}_Vamp", 0.034, (-L / 2 + 0.055, 0, 0.026), material, scale=(1.75, 0.98, 0.62), parent=e, segs=18)
    # insole (champagne leather), seen through the open topline
    ins = [(x * 0.96, y * 0.86, sole_z(s) + 0.006) for s, x, y in outline]
    mesh_obj(f"{name}_Insole", ins, [tuple(range(n))], SATIN, parent=e)
    # stiletto heel with a dark top-lift
    hx = L / 2 - 0.028
    cyl(f"{name}_Stiletto", 0.012, HH - 0.004, (hx, 0, (HH - 0.004) / 2 + 0.004), material, r2=0.0045, segs=12,
        parent=e)
    cyl(f"{name}_TopLift", 0.005, 0.006, (hx, 0, 0.003), mat("dark", 0.6), segs=10, parent=e)
    ball(f"{name}_Bow", 0.011, (-L / 2 + 0.085, 0, 0.044), GOLD, scale=(0.7, 1.7, 0.6), parent=e, segs=10)
    return e


# Boutique wall shoe ledges under the swatch board (floating painted shelves on gilt scroll brackets, like a
# bridal-shoe display wall): two shelves, pastel satin court shoes shown side-on in pairs, toes to the front.
LEDGE_Y0, LEDGE_Y1, LEDGE_D = 0.36, 1.44, 0.22
SHOE_KEYS = (("gown_peony", "accent_2", "gown_moon"), ("gown_sage", "gown_champ"))
for row, lz in enumerate((0.5, 0.98)):
    box("ShoeLedge", (LEDGE_D, LEDGE_Y1 - LEDGE_Y0, 0.022), (LEDGE_D / 2, (LEDGE_Y0 + LEDGE_Y1) / 2, lz - 0.011), PAINT,
        bevel=0.004)
    rod("ShoeLedge_Lip", (LEDGE_D - 0.006, LEDGE_Y0, lz + 0.012), (LEDGE_D - 0.006, LEDGE_Y1, lz + 0.012), 0.005, GOLD)
    for by in (LEDGE_Y0 + 0.1, LEDGE_Y1 - 0.1):          # gilt scroll brackets fixed to the wall
        tube("ShoeLedge_Bracket", spline([(0.012, by, lz - 0.2), (0.05, by, lz - 0.17), (0.04, by, lz - 0.1),
                                          (0.12, by, lz - 0.05), (LEDGE_D - 0.03, by, lz - 0.025)], 5), 0.007, GOLD,
             segs=8)
        box("ShoeLedge_Plate", (0.006, 0.03, 0.06), (0.003, by, lz - 0.19), GOLD, bevel=0.002)
    for k, key in enumerate(SHOE_KEYS[row]):
        sy = LEDGE_Y0 + 0.2 + 0.34 * k
        shoe = M(key, 0.84, "fabric", scale=0.5)
        for j, sx in enumerate((0.075, 0.165)):       # a pair: one shoe slightly behind and offset
            heel(f"Heel_{row}{k}{j}", (sx, sy + 0.03 * j, lz), R(90), shoe)
    if row == 1:                                      # a beaded clutch on the top shelf
        box("Clutch", (0.07, 0.2, 0.11), (0.09, 1.25, lz + 0.055), VELVET_2, bevel=0.02)
        rod("Clutch_Frame", (0.128, 1.155, lz + 0.1), (0.128, 1.345, lz + 0.1), 0.005, GOLD, segs=6)
        ball("Clutch_Clasp", 0.012, (0.13, 1.25, lz + 0.112), GOLD, segs=8)

# Stack of round couture hat boxes with satin ribbons (your LinkedIn).
HB_XY = (4.58, 2.66)
z = FLOOR_Z
first = None
for k, (r_, hh, m_) in enumerate(((0.19, 0.24, M("gown_peony", 0.7, "paper")), (0.16, 0.2, PAPER),
                                  (0.13, 0.16, M("accent_3", 0.7, "paper")))):
    cx_, cy_ = HB_XY[0] - 0.02 * k, HB_XY[1] + 0.015 * k
    b = cyl("HatBox", r_, hh - 0.04, (cx_, cy_, z + (hh - 0.04) / 2), m_, segs=56, bevel=0.004)
    first = first or b
    cyl("HatBox_Lid", r_ + 0.006, 0.045, (cx_, cy_, z + hh - 0.0225), m_, segs=56, bevel=0.005)
    tube("HatBox_Ribbon", ring_pts(r_ + 0.0035, z + (hh - 0.04) * 0.5, 56, cx_, cy_), 0.006,
         SATIN if k != 1 else VELVET_2, closed=True, segs=6)
    z += hh
for sx in (-1, 1):
    ball("HatBox_Bow", 0.035, (HB_XY[0] - 0.04 + sx * 0.035, HB_XY[1] + 0.03, z + 0.012), SATIN, scale=(1.1, 0.5, 0.45),
         rot=(0, 0, R(30)))
ball("HatBox_Bow_Knot", 0.014, (HB_XY[0] - 0.04, HB_XY[1] + 0.03, z + 0.014), SATIN)
hook_link(first, "linkedin")

# Two church candles on the window board (lit in the midnight theme).
for k, (cy_, hh) in enumerate(((WIN_C - 0.38, 0.14), (WIN_C - 0.28, 0.1))):
    cyl("Candle", 0.03, hh, (0.08, cy_, SILL + 0.03 + hh / 2), mat("cream", 0.6), segs=20, bevel=0.004)
    lathe("Candle_Dish", [(0, 0), (0.045, 0), (0.05, 0.008), (0.046, 0.008), (0, 0.004)], (0.08, cy_, SILL + 0.03), GOLD,
          segs=20)
    if NIGHT:
        no_shadow(ball("Candle_Flame", 0.009, (0.08, cy_, SILL + 0.03 + hh + 0.018), FLAME, scale=(1, 1, 1.8), segs=10))


# =====================================================================
#  BOUTIQUE SIGN (your name + role) + SWATCH BOARD (your projects)
# =====================================================================
# Arched boutique sign over the gown rail: painted panel, gilt bead, a brass picture light above it.
SIGN_X, SIGN_Z, SIGN_W, SIGN_H, SIGN_RISE = 2.31, 2.2, 1.5, 0.4, 0.13
SIGN_PAINT = M("sign", 0.5, "plaster", scale=3)
outline = [(SIGN_X + u, SIGN_Z + v) for u, v in arch_outline(SIGN_W, SIGN_H, SIGN_RISE, n=24)]
wall_poly("Sign_Panel", outline, SIGN_PAINT, "back", D - 0.016, thick=0.024)
tube("Sign_Bead", [(u, D - 0.03, v) for u, v in
                   [(SIGN_X + u, SIGN_Z + v) for u, v in arch_outline(SIGN_W, SIGN_H, SIGN_RISE, n=24, inset=0.035)]],
     0.007, GILT, closed=True, segs=6)
tube("Sign_Edge", [(u, D - 0.026, v) for u, v in outline], 0.012, GILT, closed=True, segs=8)
ink = mat("sign_ink", 0.45, emit=0.5 if NIGHT else 0.05)
TY = D - 0.032
hook_text("name", 1, "YOUR NAME", 0.17, (SIGN_X, TY, SIGN_Z + 0.25), material=ink, max_width=SIGN_W - 0.2, depth=0.006)
hook_text("role", 1, "your role", 0.095, (SIGN_X, TY, SIGN_Z + 0.095), material=ink, max_width=SIGN_W - 0.4, depth=0.004)
label("Sign_Atelier", "~ ATELIER ~", 0.042, (SIGN_X, TY, SIGN_Z + SIGN_H + 0.04), GILT, depth=0.002)
for sx in (-1, 1):
    box("Sign_Rule", (0.22, 0.004, 0.006), (SIGN_X + sx * 0.42, TY, SIGN_Z + 0.1), GILT, bevel=0)
# brass picture light
rod("SignLamp_Arm", (SIGN_X, D, 2.99), (SIGN_X, D - 0.11, 2.98), 0.007, GOLD)
cyl("SignLamp_Rose", 0.026, 0.012, (SIGN_X, D - 0.006, 2.99), GOLD, rot=(R(90), 0, 0), segs=16)
cyl("SignLamp_Shade", 0.024, 0.44, (SIGN_X, D - 0.12, 2.965), GOLD, rot=(0, R(90), 0), segs=24, bevel=0.004)
no_shadow(box("SignLamp_Glow", (0.4, 0.016, 0.005), (SIGN_X, D - 0.12, 2.942), mat("bulb", 0.3, emit=1.5, color="#FFE6C2"),
              bevel=0))
light("Light_Sign", "AREA", 30 if NIGHT else 16, kelvin(LAMP_WARMTH + 300), (SIGN_X, D - 0.16, 2.92),
      aim=(SIGN_X, D, 2.3), size=0.45)

# Swatch board on the left wall: three project cards, fabric swatches and ribbons pinned to linen.
SB_Y, SB_Z, SB_W, SB_H = 0.95, 1.62, 1.3, 0.85
box("Swatch_Board", (0.022, SB_W, SB_H), (0.011, SB_Y, SB_Z), M("cream", 0.92, "fabric", scale=1.4), bevel=0.004)
for sz in (-1, 1):
    box("Swatch_Board_Frame_H", (0.03, SB_W + 0.04, 0.02), (0.015, SB_Y, SB_Z + sz * (SB_H / 2 + 0.01)), GILT, bevel=0.003)
for sy in (-1, 1):
    box("Swatch_Board_Frame_V", (0.03, 0.02, SB_H), (0.015, SB_Y + sy * (SB_W / 2 + 0.01), SB_Z), GILT, bevel=0.003)
CARD_W, CARD_H = 0.3, 0.38
BX = 0.026
for k, key in enumerate(("gown_peony", "gown_sage", "gown_moon")):
    cy_ = SB_Y - 0.4 + 0.4 * k
    cz_ = SB_Z + 0.11
    box("Swatch_Card_Back", (0.003, CARD_W + 0.03, CARD_H + 0.03), (BX - 0.003, cy_, cz_), PAPER, bevel=0,
        rot=(R(2 - 2 * k), 0, 0))
    card = hook_image("board", k + 1, (CARD_W, CARD_H), (BX, cy_, cz_), rot=(0, R(2 * k - 2), R(90)), default_key=key)
    ball("Swatch_Card_Pin", 0.009, (BX + 0.006, cy_, cz_ + CARD_H / 2 + 0.004), mat(("accent_1", "gold", "accent_3")[k], 0.3),
         segs=10)
    # default: a lookbook gown silhouette on each card
    sil = [mesh_obj("Swatch_Card_Gown", [(BX + 0.002, cy_ - 0.02, cz_ + 0.08), (BX + 0.002, cy_ + 0.02, cz_ + 0.08),
                                          (BX + 0.002, cy_ + 0.1, cz_ - 0.14), (BX + 0.002, cy_ - 0.1, cz_ - 0.14)],
                    [(0, 1, 2, 3)], mat("paper", 0.8)),
           ball("Swatch_Card_Bodice", 0.03, (BX + 0.002, cy_, cz_ + 0.1), mat("paper", 0.8), scale=(0.05, 0.8, 1.2), segs=12)]
    hook_default(card, *sil)
    lab = box("Swatch_Label", (0.003, 0.24, 0.045), (BX - 0.002, cy_, SB_Z - 0.17), PAPER, bevel=0)
    hook_text("title", k + 1, f"PROJECT {('ONE', 'TWO', 'THREE')[k]}", 0.026, (BX + 0.0, cy_, SB_Z - 0.17),
              rot=(R(90), 0, R(90)), material=mat("dark", 0.6), max_width=0.22, depth=0.002)
for k, key in enumerate(("gown_opal", "gown_peony", "gown_sage", "gown_moon", "gown_champ", "gown_midnight", "accent_1")):
    sy_ = SB_Y - 0.52 + k * 0.17
    box("Swatch", (0.004, 0.09, 0.075), (BX - 0.004, sy_, SB_Z - 0.3), GOWN(key), bevel=0.001,
        rot=(R(random.uniform(-6, 6)), 0, 0))
    ball("Swatch_Pin", 0.006, (BX + 0.001, sy_, SB_Z - 0.27), mat("gold", 0.3), segs=8)
tube("Swatch_Ribbon", [(BX, SB_Y - 0.6, SB_Z + 0.37), (BX + 0.004, SB_Y - 0.2, SB_Z + 0.33), (BX, SB_Y + 0.3, SB_Z + 0.36),
                       (BX + 0.002, SB_Y + 0.6, SB_Z + 0.33)], 0.006, SATIN, segs=6)

# =====================================================================
#  LIGHTS, WORLD, CAMERA, RENDER
# =====================================================================
# Day ("morning_blush"): soft pink-white sun through the arched window, a rosy fill from the camera side and
# the warm chandelier, bulb mirror and sign lamp. Night ("midnight_ball"): cool moonlight through the same window,
# a dim lilac fill, and the candles, bulbs and fairy lights doing most of the work.
def tint(rgb, f):
    return tuple(c * k for c, k in zip(rgb, f))


PINK = (1.0, 0.93, 0.93)
sun_dir = Vector((1.0, -0.12, -0.56)).normalized()
target = Vector((2.3, WIN_C - 0.4, 0.0))
if NIGHT:
    light("Light_Sun", "SUN", 2.4, tint(kelvin(9500), (0.92, 0.95, 1.0)), target - sun_dir * 6, aim=target, size=R(1.5))
    light("Light_Fill", "AREA", 140 * (W * D / 16), tint(kelvin(8500), (0.95, 0.9, 1.0)), (W + 3, -3, H + 2.5),
          aim=(W / 2, D / 2, 0.6), size=6)
    light("Light_Window", "AREA", 26, kelvin(9000), (0.3, WIN_C, 1.8), aim=(2.5, WIN_C, 1.1), size=1.2)
    light("Light_Bounce", "AREA", 26, tint(kelvin(4000), (1.0, 0.9, 1.0)), (W / 2, D / 2, H - 0.1), aim=(W / 2, D / 2, 0),
          size=3.0)
else:
    light("Light_Sun", "SUN", SUN_STRENGTH, tint(kelvin(SUN_WARMTH), PINK), target - sun_dir * 6, aim=target, size=R(2.5))
    light("Light_Fill", "AREA", 290 * (W * D / 16), tint(kelvin(6200), PINK), (W + 3, -3, H + 2.5), aim=(W / 2, D / 2, 0.6),
          size=6)
    light("Light_Window", "AREA", 70, tint(kelvin(6000), PINK), (0.3, WIN_C, 1.8), aim=(2.5, WIN_C, 1.1), size=1.2)
    light("Light_Bounce", "AREA", 45, kelvin(LAMP_WARMTH + 700), (W / 2, D / 2, H - 0.1), aim=(W / 2, D / 2, 0), size=3.0)
light("Light_Rail", "AREA", 40 if NIGHT else 30, kelvin(LAMP_WARMTH + 500), (2.31, D - 1.6, 2.7), aim=(2.31, D - 0.4, 1.1),
      size=1.6)                                     # soft boutique spot on the gowns
light("Light_Case", "AREA", 8 if NIGHT else 5, kelvin(4200), (4.4, 1.5, 1.36), aim=(4.4, 1.5, 1.0), size=0.3)

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
bg_amb.inputs["Color"].default_value = (*kelvin(8000 if NIGHT else 6000), 1)
bg_amb.inputs["Strength"].default_value = 0.16 if NIGHT else 0.35
path = wn.new("ShaderNodeLightPath")
mix = wn.new("ShaderNodeMixShader")
wl.new(path.outputs["Is Camera Ray"], mix.inputs["Fac"])
wl.new(bg_amb.outputs[0], mix.inputs[1])
wl.new(bg_cam.outputs[0], mix.inputs[2])
wl.new(mix.outputs[0], out.inputs["Surface"])

# Orthographic camera that frames the whole room automatically (from kit_bounds).
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
scene.view_settings.exposure = -0.1 if NIGHT else -0.15

# Remember the style so add_furniture.py can match colours later.
scene["kit_style"] = STYLE
scene["kit_version"] = KIT_VERSION
scene["kit_palette"] = json.dumps(COLORS)
scene["kit_material_finish"] = json.dumps({"roughness": 0.6, "bevel": 0.005, "saturation": 0.7})
scene["kit_theme"] = THEME
scene["kit_bounds"] = BOUNDS
scene["kit_furniture_colors"] = json.dumps(["main", "accent_1", "accent_2", "accent_3", "cream", "wood", "gold",
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
