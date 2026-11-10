"""
3D ROOM PORTFOLIO KIT  -  Template: DARK ACADEMIA STUDY / LIBRARY
=================================================================
Builds a moody isometric library from scratch and renders a 1920x1080 image: built-in bookcases with a
hook-on library ladder, a deep-buttoned Chesterfield wing chair, a leather-topped partners' desk under a sash
window, a green banker's lamp, a marble chimneypiece with a cast-iron insert, a library globe and a Heriz rug
on oak herringbone parquet - all modelled on real pieces you could find at an antiques dealer.

HOW TO RUN
  Option A (no Blender UI):   blender -b -P academia_library.py
  Option B (inside Blender):  Scripting tab > Open > academia_library.py > Run Script (then F12 to render)

You only need to edit the SETTINGS block below. Everything under it builds the room.
Output: output/academia_library.png and output/academia_library.blend next to this script.
"""
# REFERENCES  (what each piece is modelled on; real sizes in metres; details in research/academia_library.md)
#   shelf      built-in library bookcase, BILLY-width bays + Trinity Long Room joinery: 3 x 0.78 bays, 2.84 H,
#              cupboards 0.42 D x 0.86 H, shelves 0.30 D  https://www.ikea.com/ca/en/p/billy-oxberg-bookcase-with-doors-white-s59581558
#   ladder     hook-on library ladder + 1in rail (Quiet Glide kit): 0.41 tread width, 8 treads, rail at 2.3
#              https://www.lowes.com/pd/Quiet-Glide-8-06-ft-Unfinished-Red-oak-Library-Ladder/1002532456
#   armchair   English leather Chesterfield wingback: 0.85 W x 0.90 D x 1.08 H, seat 0.47; hand-tufted diamonds,
#              brass nailhead trim, piped cushion
#              https://www.1stdibs.com/furniture/seating/wingback-chairs/vintage-brown-leather-chesterfield-wingback-chair-from-england/id-f_29668362/
#   desk       Edwardian mahogany partners' pedestal desk, leather top: 1.52 x 0.92 x 0.76, knee-hole 0.58 H
#              https://www.londonfine.co.uk/collections/sold/products/antique-partners-desk-english-mahogany-leather-writing-table-edwardian
#   chair      oak captain's / smoker's-bow swivel desk chair: 0.57 x 0.55 x 0.85, seat 0.45
#              https://www.chairish.com/product/3776218/english-art-craft-captain-swivel-desk-chair-1920s
#   lamp       green glass banker's lamp: 0.36 H, shade 0.235 x 0.146 x 0.076, base 0.15
#              https://www.lampsplus.com/products/360-lighting-hammond-14-high-green-glass-and-brass-bankers-table-lamp__23r12.html
#   side_table Victorian mahogany tripod wine table: 0.56 dia x 0.69 H
#              https://www.chairish.com/product/24951511/english-victorian-mahogany-round-tripod-winelamptea-table
#   floor_lamp brass standard lamp with faux-silk shade: 1.56 H, shade 0.42
#              https://costco.co.uk/Furniture-Mattresses/Lighting/Lamps/Madrid-Antique-Brass-Floor-Lamp-with-Faux-Silk-Shade/p/475680
#   hero_prop  18in terrestrial library globe on stand: globe 0.46, horizon ring 0.62, 1.05 H
#              https://www.1stdibs.com/furniture/more-furniture-collectibles/home-accents/globes/charles-smith-son-18-inch-terrestrial-globe-on-stand-w-compass-circa-1845-48/id-f_38527992
#   footstool  matching buttoned Chesterfield footstool: 0.56 x 0.40 x 0.36 (decor, pairs with the wing chair)
#   rug        antique Heriz carpet (brick red / navy / ivory): 2.7 x 1.9, design on a 1 cm knot grid
#              https://arsinruggallery.com/rug/75462/
#   wall_art   gilt-framed oils (7 cm swept moulding) with 18in brass picture lights (0.46 W, 0.15 projection)
#              https://www.lampsplus.com/p/22A26
#   fireplace  Victorian chimneypiece + arched cast-iron insert: 1.45 W x 1.27 H, opening 1.01 x 0.92
#              https://www.chairish.com/product/37856305/victorian-cast-iron-fireplace-surround-1896
#   coal bucket Victorian copper coal bucket with brass rim and swing handle: 0.32 dia x 0.34 H (real 32-39 H)
#              https://www.chairish.com/product/20909010/victorian-brass-and-copper-coal-bucket-1860s
#   teapot     6-cup "Brown Betty" red-clay teapot (on the wine table): 15.5 H x 15 dia x 27 L
#              https://www.edwardschina.co.uk/brown-betty-6-cup-teapot.html
#   fender     Victorian brass fender + fire irons (real 1.32 x 0.36)  https://www.chairish.com/product/9522428/victorian-pierced-brass-fender-with-fire-irons
#   panelling  raised-panel dado, 0.9 H, 0.1 stiles/rails, 0.22 skirting  https://finehomebuilding.com/1984/03/01/raised-panel-wainscot
#   window     six-over-six timber sash, 1.0 x 1.55, sill 0.9  (Gwynedd timber-window conservation leaflet)
#   floor      oak herringbone parquet, 70 x 350 mm blocks with a two-strip border

# =====================================================================
#  SETTINGS  -  change these lines, then run the script again
# =====================================================================
ROOM_NAME = "academia_library"      # used for the output file names

ROOM_WIDTH = 4.4                    # metres, left to right
ROOM_DEPTH = 4.0                    # metres, front to back
WALL_HEIGHT = 3.0                   # metres (tall, so the bookcase can reach the ceiling)

THEME = "rainy_evening"             # pick one of the colour themes below
THEMES = {                          # any hex colour works; "main" is the room's hero colour (oxblood leather)
    # Lights change with the theme too (see LIGHTS below): "rainy_evening" = blue rain light, lamps and a
    # lit fire; "sunny_reading" = warm daylight through the window, lamps dimmed and the fire low.
    "rainy_evening": {
        "background": "#1F272B", "wall": "#2F4536", "wall_trim": "#3A251A", "floor": "#7A5333",
        "wood": "#4E2C1C", "main": "#6E1F24", "accent_1": "#2A5A3E", "accent_2": "#B88E4E",
        "accent_3": "#9AB0C4", "cream": "#E6D6B0", "plant": "#5F7550", "dark": "#1A1D1B",
        "stone": "#B3AA9C", "navy": "#24304A", "tan": "#9C7448", "sky": "#4E6A86", "fire": "#FF8A3A",
    },
    "sunny_reading": {
        "background": "#EDE4D3", "wall": "#6F8A66", "wall_trim": "#5A3A28", "floor": "#A87A4E",
        "wood": "#6A3F28", "main": "#8C2E33", "accent_1": "#3E6B50", "accent_2": "#C9A15E",
        "accent_3": "#BFD8EA", "cream": "#F1E6CC", "plant": "#6E9A5E", "dark": "#2A2420",
        "stone": "#DCD5C8", "navy": "#2F4166", "tan": "#B08654", "sky": "#CFE6F7", "fire": "#FF9A4A",
    },
}

SUN_WARMTH = 9000                   # Kelvin of the light from the window (9000 = cool rainy blue)
SUN_STRENGTH = 0.8                  # how bright the window light is
LAMP_WARMTH = 2600                  # Kelvin of the banker's lamp and the reading lamp
LAMP_STRENGTH = 30                  # Watts of the banker's lamp
FIRE_STRENGTH = 90                  # Watts of the fireplace glow (0 = no fire)
RAIN = True                         # rain streaks on the window
SEED = 7                            # change to shuffle books and small props

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

STYLE = "academia_library"
KIT_VERSION = 2
W, D, H = ROOM_WIDTH, ROOM_DEPTH, WALL_HEIGHT
T = 0.15            # wall thickness
FLOOR_Z = 0.02      # top of the parquet; furniture stands here
R = math.radians
NIGHT = THEME != "sunny_reading"
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
    for img in list(bpy.data.images):           # baked pictures from an earlier run (rug, globe, paintings)
        if img.get("kit_baked"):
            bpy.data.images.remove(img)
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
def wood(f=1.0, rough=0.42, along="X", key="wood", kind="wood"):
    """Mahogany / walnut. along = grain direction in the part's own axes (Z for uprights)."""
    tag = {"X": 0.0, "Y": 0.001, "Z": 0.002}[along]          # separate cached material per grain direction
    return surface(mat(key, round(rough + tag, 3), color=shade(COLORS[key], f) if f != 1.0 else None), kind,
                   along=along)


def brass(rough=0.32):
    """Brass: metallic + brushed; a little glow so it still reads in the dark theme."""
    return surface(mat("accent_2", rough, emit=0.1 if NIGHT else 0.0, metal=0.75), "brushed")


def iron():
    return surface(mat("dark", 0.55, metal=0.5, color=shade(COLORS["dark"], 1.25)), "brushed", scale=0.3)


def leather(key="main", f=1.0, rough=0.38):
    return surface(mat(key, rough, color=shade(COLORS[key], f) if f != 1.0 else None), "leather")


def marble():
    return surface(mat("stone", 0.28), "marble")


def glow(hex_color, strength):
    return mat("flame", 0.4, emit=strength, color=hex_color)


# Baked pictures: the rug design, the globe map and the default oil paintings are painted pixel by pixel from
# COLORS when the script runs (so every theme repaints them) and packed into the .blend.
def srgb(hex_color):
    h = hex_color.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def blend(a, b, t):
    return tuple(x + (y - x) * t for x, y in zip(a, b))


def value_noise(seed, nx, ny):
    """Smooth random field on a coarse nx x ny grid: f(u, v) -> 0..1 for u, v in 0..1."""
    rnd = random.Random(seed)
    g = [[rnd.random() for _ in range(nx + 2)] for _ in range(ny + 2)]

    def f(u, v):
        x, y = min(max(u, 0.0), 1.0) * nx, min(max(v, 0.0), 1.0) * ny
        i, j = int(x), int(y)
        fx, fy = x - i, y - j
        fx, fy = fx * fx * (3 - 2 * fx), fy * fy * (3 - 2 * fy)
        a = g[j][i] + (g[j][i + 1] - g[j][i]) * fx
        b = g[j + 1][i] + (g[j + 1][i + 1] - g[j + 1][i]) * fx
        return a + (b - a) * fy
    return f


def baked_image(name, wpx, hpx, paint):
    """paint(u, v) -> sRGB (r, g, b) with u, v in 0..1 (v = up). Returns a packed image."""
    img = bpy.data.images.new(name, wpx, hpx, alpha=False)
    px = []
    for j in range(hpx):
        v = (j + 0.5) / hpx
        for i in range(wpx):
            r, g, b = paint((i + 0.5) / wpx, v)
            px += (min(1.0, max(0.0, r)), min(1.0, max(0.0, g)), min(1.0, max(0.0, b)), 1.0)
    img.pixels.foreach_set(px)
    img.pack()
    img["kit_baked"] = True
    return img


def picture_material(key, img, rough=0.6, kind="paper", coords="UV"):
    """A real surface (weave, paper...) whose colour comes from a baked image instead of one palette colour."""
    m = surface(mat(key, rough, color=COLORS["cream"]), kind)
    nt = m.node_tree
    if nt.nodes.get("KIT_IMAGE"):
        return m
    tex = nt.nodes.new("ShaderNodeTexImage")
    tex.name, tex.image = "KIT_IMAGE", img
    tc = nt.nodes.new("ShaderNodeTexCoord")
    nt.links.new(tc.outputs[coords], tex.inputs["Vector"])
    base = nt.nodes["KIT_BASE"]
    for link in [ln for ln in nt.links if ln.from_node == base]:
        nt.links.new(tex.outputs["Color"], link.to_socket)
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
    return _finish(o, material, min(bevel, min(size) * 0.45), coll, parent)


def boxes(name, parts, material, bevel=0.003, coll=None, parent=None, segs=2):
    """MANY boxes merged into one object (fast for hundreds of books). parts = [(size, loc, rot), ...]."""
    bm = bmesh.new()
    for size, loc, rot in parts:
        verts = bmesh.ops.create_cube(bm, size=1.0)["verts"]
        bmesh.ops.transform(bm, matrix=Matrix.LocRotScale(Vector(loc), Euler(rot), Vector(size)), verts=verts)
    return _finish(_obj(name, bm), material, bevel, coll, parent, segs)


def cyl(name, r, h, loc, material, r2=None, segs=32, bevel=0.003, rot=(0, 0, 0), coll=None, parent=None):
    """Cylinder (or tapered cylinder with r2). loc = centre."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=segs, radius1=r, radius2=r if r2 is None else r2, depth=h)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, bevel, coll, parent)


def ball(name, r, loc, material, scale=(1, 1, 1), coll=None, parent=None, segs=24):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=segs, v_segments=max(8, segs // 2 + 2), radius=r)
    o = _obj(name, bm)
    o.location, o.scale = loc, scale
    return _finish(o, material, 0, coll, parent)


def ring(name, big_r, r, loc, material, rot=(0, 0, 0), arc=1.0, segs=40, coll=None, parent=None):
    """Torus (ring) lying flat in local XY. arc < 1 makes an open arc starting at +X, counter-clockwise."""
    bm = bmesh.new()
    n_main = segs + (0 if arc >= 1 else 1)
    rows = []
    for i in range(n_main):
        a = 2 * math.pi * arc * i / segs
        rows.append([bm.verts.new(((big_r + r * math.cos(b)) * math.cos(a), (big_r + r * math.cos(b)) * math.sin(a),
                                   r * math.sin(b))) for b in (2 * math.pi * j / 10 for j in range(10))])
    for i in range(n_main if arc >= 1 else n_main - 1):
        r1, r2 = rows[i], rows[(i + 1) % n_main]
        for j in range(10):
            bm.faces.new((r1[j], r2[j], r2[(j + 1) % 10], r1[(j + 1) % 10]))
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, 0, coll, parent)


def lathe(name, prof, loc, material, segs=32, rot=(0, 0, 0), wave=None, closed=False, coll=None, parent=None):
    """A TURNED part (table column, candlestick, lamp base...). prof = [(radius, z), ...] from bottom to top,
    spun around local Z. wave=(count, amount) adds pleats/flutes. closed=True joins the last ring to the first."""
    bm = bmesh.new()
    rings = []
    for r, z in prof:
        rings.append([bm.verts.new(((r * (1 + (wave[1] * math.cos(wave[0] * a) if wave else 0))) * math.cos(a),
                                    (r * (1 + (wave[1] * math.cos(wave[0] * a) if wave else 0))) * math.sin(a), z))
                      for a in (2 * math.pi * i / segs for i in range(segs))])
    pairs = list(zip(rings, rings[1:])) + ([(rings[-1], rings[0])] if closed else [])
    for r1, r2 in pairs:
        for i in range(segs):
            bm.faces.new((r1[i], r1[(i + 1) % segs], r2[(i + 1) % segs], r2[i]))
    if not closed:
        if prof[0][0] > 0.0005:
            bm.faces.new(list(reversed(rings[0])))
        if prof[-1][0] > 0.0005:
            bm.faces.new(rings[-1])
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    _finish(o, material, 0, coll, parent)
    flat = [abs(p.normal.z) > 0.97 for p in o.data.polygons]        # crisp steps, smooth curves
    o.data.polygons.foreach_set("use_smooth", [not f for f in flat])
    return o


def tube(name, pts, radii, material, segs=10, coll=None, parent=None, flat=1.0):
    """A round bar swept along a list of points (cabriole legs, chair bows, lamp arms, hooks)."""
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
        rings.append([bm.verts.new(p + radii[i] * (math.cos(a) * n1 + flat * math.sin(a) * n2))
                      for a in (2 * math.pi * k / segs for k in range(segs))])
    for r1, r2 in zip(rings, rings[1:]):
        for k in range(segs):
            bm.faces.new((r1[k], r1[(k + 1) % segs], r2[(k + 1) % segs], r2[k]))
    bm.faces.new(list(reversed(rings[0])))
    bm.faces.new(rings[-1])
    return _finish(_obj(name, bm), material, 0, coll, parent)


def half_cyl(name, r, length, loc, material, rot=(0, 0, 0), parent=None, segs=32, coll=None):
    """Open-bottomed half cylinder lying along local X (a banker's lamp shade, a picture-light hood)."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=segs, radius1=r, radius2=r, depth=length)
    bmesh.ops.rotate(bm, verts=bm.verts, cent=(0, 0, 0), matrix=Matrix.Rotation(R(90), 3, "Y"))
    bmesh.ops.bisect_plane(bm, geom=bm.verts[:] + bm.edges[:] + bm.faces[:], plane_co=(0, 0, 0),
                           plane_no=(0, 0, 1), clear_inner=True)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, 0, coll, parent)


def quad(name, w, h, loc, material, rot=(0, 0, 0), parent=None):
    """Flat picture plane with UVs, facing local -Y (a painted canvas)."""
    bm = bmesh.new()
    face = bm.faces.new([bm.verts.new(v) for v in ((-w / 2, 0, -h / 2), (w / 2, 0, -h / 2), (w / 2, 0, h / 2),
                                                    (-w / 2, 0, h / 2))])
    uv = bm.loops.layers.uv.new("UVMap")
    for loop, co in zip(face.loops, ((0, 0), (1, 0), (1, 1), (0, 1))):
        loop[uv].uv = co
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, 0, None, parent)


def pebbles(name, items, material, parent=None, subdiv=1, smooth=True):
    """MANY small rounded lumps in one object (coal, nailhead studs). items = [(loc, (sx, sy, sz), rot), ...]."""
    bm = bmesh.new()
    for loc, size, rot in items:
        bmesh.ops.create_icosphere(bm, subdivisions=subdiv, radius=1.0,
                                   matrix=Matrix.LocRotScale(Vector(loc), Euler(rot), Vector(size)))
    o = _finish(_obj(name, bm), material, 0, None, parent)
    if not smooth:
        o.data.polygons.foreach_set("use_smooth", [False] * len(o.data.polygons))
    return o


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
            o.visible_shadow = False


def lying_book(name, size, loc, key, turn=0.0, parent=None):
    """A real hardback lying flat: 3 mm leather boards and a spine (local -Y) that overhang a cream page block,
    so the paper shows on the three open sides. size = (w, d, thickness), loc = centre of the bottom face."""
    w, d, t = size
    bk = anchor(name, loc, turn, coll=COL_FURN if parent else None, parent=parent)
    boxes(f"{name}_Boards", [((w, d, 0.003), (0, 0, 0.0015), (0, 0, 0)), ((w, d, 0.003), (0, 0, t - 0.0015), (0, 0, 0)),
                             ((w, 0.005, t), (0, -d / 2 + 0.0025, t / 2), (0, 0, 0))], leather(key, 1.0, 0.6),
          bevel=0.0012, parent=bk)
    box(f"{name}_Pages", (w - 0.008, d - 0.008, t - 0.006), (0, 0.0, t / 2),
        surface(mat("cream", 0.85, color=shade(COLORS["cream"], 0.93)), "paper"), bevel=0.001, parent=bk)
    return bk


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
#   picture hooks: "screen" (glows), "frame", "poster", "board"  -> project images (in order)
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


GOLD_TEXT = mat("accent_2", 0.3, emit=0.7 if NIGHT else 0.2, metal=0.4)   # gilt lettering


# --------------------------------------------------------------------- shared real-world parts
def oil_landscape(u, v, _n=[]):
    """Default canvas 1: an English river landscape in the manner of a 19th-century oil (sky, clouds, trees, water)."""
    if not _n:
        _n += [value_noise(SEED + 21, 7, 5), value_noise(SEED + 22, 30, 24), value_noise(SEED + 23, 12, 10)]
    clouds, brush, leaves = _n
    C = lambda key, f=1.0: srgb(shade(COLORS[key], f))
    hz = 0.42 + 0.05 * math.sin(u * 4.0 + 1.0) * (1 - u) + 0.03 * leaves(u, 0.3)
    if v > hz:                                                          # sky with heaped clouds
        t = (v - hz) / (1 - hz)
        col = blend(blend(C("cream", 1.0), C("accent_3", 1.0), 0.35), blend(C("accent_3", 0.85), C("navy", 1.4), 0.3),
                    t ** 0.7)
        c = min(1.0, max(0.0, (clouds(u, v) - 0.45) * 3.5))
        col = blend(col, blend(C("cream", 1.05), C("accent_3", 0.7), max(0.0, 0.6 - t) * 0.8), c * 0.85)
    elif v > hz - 0.09:                                                 # distant blue hills
        col = blend(C("plant", 0.8), C("accent_3", 0.75), 0.55)
    else:                                                               # meadow, darker towards the front
        col = blend(blend(C("plant", 0.85), C("tan", 0.9), leaves(u, v)), C("wood", 0.7), (hz - 0.09 - v) * 1.2)
        river = 0.2 + 0.1 * u - 0.04 * math.sin(u * 7)
        if abs(v - river) < 0.012 + 0.02 * u:
            col = blend(blend(C("cream", 1.0), C("accent_3", 1.0), 0.4), C("dark", 1.0), 0.25)
    rough = 0.35 * (leaves(u * 5, v * 5) - 0.5) + 0.25 * (brush(u * 0.6, v * 0.6) - 0.5)
    tree = min(((u - cx) / rx) ** 2 + ((v - cy) / ry) ** 2 for cx, cy, rx, ry in
               ((0.74, 0.62, 0.13, 0.2), (0.64, 0.52, 0.09, 0.13), (0.86, 0.54, 0.08, 0.15), (0.2, 0.47, 0.05, 0.07)))
    if tree + rough < 1.0:                                              # clumps of dark oaks, lit on the left
        col = blend(C("plant", 0.4), C("plant", 0.85), max(0.0, (0.68 - u) * 2.5) * 0.6 + 0.35 * leaves(u * 6, v * 6))
    elif abs(u - 0.745) < 0.009 and hz - 0.13 < v < 0.46:
        col = C("dark", 1.6)
    f = (0.9 + 0.18 * brush(u, v)) * (1 - 0.55 * ((u - 0.5) ** 2 + (v - 0.5) ** 2))   # brushwork + vignette
    return tuple(c * f * k for c, k in zip(col, (1.0, 0.96, 0.82)))              # old yellowed varnish


def oil_portrait(u, v, _n=[]):
    """Default canvas 2: a 17th-century-style scholar, head and shoulders in a dark gown with a white falling-band
    collar, brown hair and a black cap, lit from the upper left against a warm dark ground."""
    if not _n:
        _n += [value_noise(SEED + 31, 30, 36), value_noise(SEED + 32, 6, 8)]
    brush, ground = _n
    C = lambda key, f=1.0: srgb(shade(COLORS[key], f))
    halo = max(0.0, 1 - math.hypot(u - 0.36, v - 0.7) / 0.6)
    col = blend(blend(C("wood", 0.6), C("dark", 1.0), 0.35), C("tan", 0.85), halo * 0.75 + 0.15 * ground(u, v))
    skin = blend(blend(C("cream", 0.9), C("tan", 1.0), 0.35), C("main", 2.0), 0.15)
    shadow_skin = blend(skin, C("wood", 0.6), 0.55)
    light = min(1.0, max(0.0, (u - 0.42) / 0.16))                       # 0 = lit side, 1 = shadow side
    if ((u - 0.5) / 0.44) ** 2 + ((v - 0.02) / 0.4) ** 2 < 1:           # gown with broad shoulders
        col = blend(C("dark", 2.4), C("dark", 0.9), min(1.0, max(0.0, (u - 0.2) * 1.6)))
    if abs(u - 0.5) < 0.05 and 0.36 < v < 0.47:                         # neck
        col = blend(skin, shadow_skin, 0.4 + 0.5 * light)
    band = 0.16 - (v - 0.3) * 0.35                                      # white falling-band collar (trapezoid)
    if 0.3 < v < 0.4 and abs(u - 0.5) < band:
        col = blend(C("cream", 1.08), C("cream", 0.7), min(1.0, max(0.0, (u - 0.36) * 1.8)))
    if ((u - 0.5) / 0.135) ** 2 + ((v - 0.63) / 0.155) ** 2 < 1:       # hair framing the face
        col = blend(blend(C("wood", 0.9), C("tan", 0.7), 0.4), C("dark", 1.2), 0.3 + 0.5 * light)
    face = ((u - 0.5) / 0.098) ** 2 + ((v - 0.6) / 0.112) ** 2
    if face < 1:
        f_col = blend(skin, shadow_skin, light)
        for ex in (0.468, 0.532):                                       # eyes under the brow
            if ((u - ex) / 0.014) ** 2 + ((v - 0.618) / 0.007) ** 2 < 1:
                f_col = C("dark", 1.3)
        if 0.503 < u < 0.515 and 0.56 < v < 0.61:                       # shadow beside the nose
            f_col = blend(f_col, shadow_skin, 0.6)
        if abs(u - 0.5) < 0.025 and abs(v - 0.535) < 0.004:             # mouth
            f_col = blend(f_col, C("main", 1.2), 0.6)
        if v < 0.53:                                                    # short grey-brown beard
            f_col = blend(f_col, blend(C("dark", 1.8), C("tan", 0.8), 0.35), min(1.0, (0.53 - v) * 30) * 0.9)
        col = blend(col, f_col, min(1.0, (1 - face) * 8))
    if ((u - 0.5) / 0.13) ** 2 + ((v - 0.735) / 0.06) ** 2 < 1 and v > 0.7:
        col = C("dark", 1.2)                                            # black scholar's cap
    f = (0.88 + 0.2 * brush(u, v)) * (1 - 0.6 * ((u - 0.5) ** 2 + (v - 0.5) ** 2))
    return tuple(c * f * k for c, k in zip(col, (1.0, 0.95, 0.8)))


_canvases = {}


def oil_canvas(style):
    """Material of a default oil painting (canvas weave + baked picture)."""
    if style not in _canvases:
        paint, size = (oil_portrait, (240, 300)) if style == "portrait" else (oil_landscape, (240, 176))
        _canvases[style] = picture_material(f"oil_{style}", baked_image(f"Oil_{style}", *size, paint), 0.45, "fabric")
    return _canvases[style]


def moulded_frame(name, w, h, cx, cz, y_wall, prof, material, parent):
    """Picture frame as ONE mitred moulding. prof = [(inset from the outer edge, height off the wall), ...],
    outer edge first; each step becomes a rectangle loop, so the mitres at the corners come out exactly."""
    bm = bmesh.new()
    loops = [[bm.verts.new((cx + sx * (w / 2 - i), y_wall - z, cz + sz * (h / 2 - i)))
              for sx, sz in ((-1, -1), (1, -1), (1, 1), (-1, 1))] for i, z in prof]
    for l1, l2 in zip(loops, loops[1:]):
        for k in range(4):
            bm.faces.new((l1[k], l1[(k + 1) % 4], l2[(k + 1) % 4], l2[k]))
    o = _finish(_obj(name, bm), material, 0, None, parent)
    o.data.polygons.foreach_set("use_smooth", [False] * len(o.data.polygons))
    return o


# Gilt swept frame moulding (7 cm wide): outer bead, a deep cove, a raised ogee and a sight-edge bead.
GILT_PROFILE = [(0, 0), (0, 0.03), (0.005, 0.041), (0.013, 0.046), (0.021, 0.042), (0.027, 0.034), (0.038, 0.027),
                (0.047, 0.029), (0.054, 0.036), (0.06, 0.034), (0.064, 0.027), (0.067, 0.028), (0.07, 0.021)]


def painting(parent, cx, cz, w, h, y_wall, kind, index, style):
    """Gilt-framed oil painting on a wall (local frame: wall at y_wall, front = -y). The canvas is a picture hook."""
    gilt = surface(mat("accent_2", 0.36, emit=0.05 if NIGHT else 0.0, metal=0.85, color=shade(COLORS["accent_2"], 0.92)),
                   "brushed")
    slip = surface(mat("cream", 0.8, color=shade(COLORS["cream"], 0.85)), "fabric")
    fw = GILT_PROFILE[-1][0]
    moulded_frame("Painting_Frame", w + 2 * fw, h + 2 * fw, cx, cz, y_wall, GILT_PROFILE, gilt, parent)
    box("Painting_Back", (w + 0.02, 0.01, h + 0.02), (cx, y_wall - 0.006, cz), mat("dark", 0.9), bevel=0, parent=parent)
    box("Painting_Slip", (w, 0.01, h), (cx, y_wall - 0.012, cz), slip, bevel=0, parent=parent)   # linen slip
    cw, ch = w - 0.06, h - 0.06
    cy = y_wall - 0.019
    canvas = hook_image(kind, index, (cw, ch), (cx, cy, cz), parent=parent, default_key="accent_1")
    hook_default(canvas, quad("Oil_Painting", cw, ch, (cx, cy - 0.001, cz), oil_canvas(style), parent=parent))
    return canvas


def picture_light(parent, cx, z_top, width, y_wall):
    """18in-style brass picture light: wall plate, curved arm and a hood that throws light down the canvas."""
    b = brass(0.3)
    box("PicLight_Plate", (0.06, 0.012, 0.09), (cx, y_wall - 0.006, z_top + 0.05), b, bevel=0.004, parent=parent)
    tube("PicLight_Arm", [(cx, y_wall - 0.012, z_top + 0.06), (cx, y_wall - 0.06, z_top + 0.11),
                          (cx, y_wall - 0.13, z_top + 0.12), (cx, y_wall - 0.15, z_top + 0.11)], 0.007, b, parent=parent)
    hood = half_cyl("PicLight_Hood", 0.03, width, (cx, y_wall - 0.15, z_top + 0.095), b, parent=parent)
    hood.scale = (1, 1.15, 0.9)
    strip = box("PicLight_Glow", (width - 0.02, 0.03, 0.004), (cx, y_wall - 0.15, z_top + 0.093),
                glow("#FFE3B0", 4.0 if NIGHT else 0.4), bevel=0, parent=parent)
    no_shadow(strip)


# =====================================================================
#  ROOM SHELL
# =====================================================================
# Floor: oak herringbone parquet (70 x 350 mm blocks) inside a two-strip border along the walls.
box("Floor_Base", (W + T, D + T, 0.2), ((W - T) / 2, (D + T) / 2, -0.1), mat("wall_trim", 0.7), bevel=0.02)
BW, BL, NB = 0.07, 0.35, 5                      # block width, length (= 5 x width)
BORDER = 2 * BW
cutter = box("Parquet_Cutter", (W - 2 * BORDER, D - 2 * BORDER, 1.0), (W / 2, D / 2, 0), mat("floor"), bevel=0)
cutter.hide_render = cutter.hide_viewport = True
s2 = math.sqrt(0.5)
groups = {(o, t): [] for o in "AB" for t in range(3)}
for k in range(-int(W / s2 / BW) - NB - 2, int(D / s2 / BW) + 2):
    for m in range(-12, 30):
        u0, v0 = (k + 2 * NB * m) * BW, k * BW              # herringbone lattice: k*(1,1) + m*(2n,0), B = A + (0,1)
        for o, (ua, ub, va, vb) in (("A", (u0, u0 + BL, v0, v0 + BW)), ("B", (u0, u0 + BW, v0 + BW, v0 + BW + BL))):
            xs_ = [(u - v) * s2 for u in (ua, ub) for v in (va, vb)]
            ys_ = [(u + v) * s2 for u in (ua, ub) for v in (va, vb)]
            if max(xs_) < BORDER or min(xs_) > W or max(ys_) < 0 or min(ys_) > D - BORDER:
                continue
            cu, cv = (ua + ub) / 2, (va + vb) / 2
            if o == "A":            # A blocks: long along u; the object is turned 45 deg so grain follows the block
                part = ((BL - 0.003, BW - 0.003, FLOOR_Z), (cu, cv, FLOOR_Z / 2), (0, 0, 0))
            else:                   # B blocks: long along v; object turned 135 deg -> local (v, -u)
                part = ((BL - 0.003, BW - 0.003, FLOOR_Z), (cv, -cu, FLOOR_Z / 2), (0, 0, 0))
            groups[(o, random.choice((0, 0, 1, 2)))].append(part)
for (o, tone), parts in groups.items():
    if not parts:
        continue
    pq = boxes(f"Floor_Parquet_{o}{tone}", parts, wood((1.0, 0.88, 1.12)[tone], 0.5, key="floor"), bevel=0.0015, segs=1)
    pq.rotation_euler = (0, 0, R(45 if o == "A" else 135))
    cut = pq.modifiers.new("Room", "BOOLEAN")
    cut.operation, cut.object = "INTERSECT", cutter
strip_y = wood(0.82, 0.5, along="Y", key="floor")
strip_x = wood(0.82, 0.5, along="X", key="floor")
for i in range(2):                      # two-strip border on all four sides (also hides the cut block ends)
    for nm, xx in (("L", BW * (i + 0.5)), ("R", W - BW * (i + 0.5))):
        box(f"Floor_Border_{nm}{i}", (BW - 0.003, D, FLOOR_Z), (xx, D / 2, FLOOR_Z / 2), strip_y, bevel=0.0015)
    for nm, yy in (("B", D - BW * (i + 0.5)), ("F", BW * (i + 0.5))):
        box(f"Floor_Border_{nm}{i}", (W - 2 * BORDER, BW - 0.003, FLOOR_Z), (W / 2, yy, FLOOR_Z / 2), strip_x,
            bevel=0.0015)

# Walls: deep green painted plaster. Window opening in the left wall above the desk.
WIN_Y = (1.95, 2.95)                # from front to back
WIN_Z = (0.9, 2.45)                 # sill at dado height, like a real Victorian sash
plaster = surface(mat("wall", 0.9), "plaster")
left = box("Wall_Left", (T, D + T, H), (-T / 2, (D + T) / 2, H / 2), plaster, bevel=0.0)
win_cut = box("Window_Cutter", (T * 3, WIN_Y[1] - WIN_Y[0], WIN_Z[1] - WIN_Z[0]),
              (-T / 2, sum(WIN_Y) / 2, sum(WIN_Z) / 2), mat("wall"), bevel=0.0)
win_cut.hide_render = win_cut.hide_viewport = True
boolean = left.modifiers.new("Window", "BOOLEAN")
boolean.operation, boolean.object = "DIFFERENCE", win_cut
box("Wall_Back", (W + T, T, H), ((W - T) / 2, D + T / 2, H / 2),
    surface(mat("wall", 0.9, color=shade(COLORS["wall"], 1.1)), "plaster"), bevel=0.0)
# Diorama caps on the cut walls.
box("Trim_Top_Back", (W + T + 0.04, T + 0.04, 0.08), ((W - T) / 2, D + T / 2, H + 0.04), wood(0.8), bevel=0.01)
box("Trim_Top_Left", (T + 0.04, D + T + 0.04, 0.08), (-T / 2, (D + T) / 2 - 0.02, H + 0.04), wood(0.8, along="Y"),
    bevel=0.01)

# Mouldings: stepped cornice, picture rail, dado rail and a tall skirting (Victorian proportions).
trim_x, trim_y = wood(0.95, 0.4, key="wall_trim"), wood(0.95, 0.4, along="Y", key="wall_trim")
cream_x = surface(mat("cream", 0.6, color=shade(COLORS["cream"], 0.9)), "plaster")
for i, (dz, dd, hh) in enumerate(((0.0, 0.035, 0.06), (0.06, 0.07, 0.05), (0.11, 0.1, 0.03))):   # 3-step cornice
    z = H - 0.14 + dz + hh / 2
    box(f"Cornice_Back_{i}", (W, dd, hh), (W / 2, D - dd / 2, z), cream_x, bevel=0.006)
    box(f"Cornice_Left_{i}", (dd, D, hh), (dd / 2, D / 2, z), cream_x, bevel=0.006)
PICTURE_RAIL = 2.62
box("PictureRail_Back", (W, 0.025, 0.035), (W / 2, D - 0.0125, PICTURE_RAIL), trim_x, bevel=0.006)
box("PictureRail_Left", (0.025, D, 0.035), (0.0125, D / 2, PICTURE_RAIL), trim_y, bevel=0.006)

# Raised-panel dado (0.9 m): back boards, rails & stiles, raised fields, a dado rail cap and 22 cm skirting.
DADO, SKIRT = 0.9, 0.22
FX, FW = 0.95, 1.45                 # fireplace centre x and surround width (built below)
BOOK_X0 = 1.92                      # left edge of the built-in bookcase
panel_wood = wood(1.0, 0.45, key="wall_trim", kind="veneer")
panel_wood_y = wood(1.0, 0.45, along="Y", key="wall_trim", kind="veneer")
field = wood(1.12, 0.4, key="wall_trim", kind="veneer")
field_y = wood(1.12, 0.4, along="Y", key="wall_trim", kind="veneer")


def dado_run(axis, a0, a1):
    """Panelling along the back wall (axis 'x') or the left wall (axis 'y') between a0 and a1."""
    L = a1 - a0
    if L < 0.08:
        return
    mid = (a0 + a1) / 2
    n = max(1, round(L / 0.55))
    pw = L / n
    if axis == "x":
        P = lambda nm, sx, sz, a, z, dy, mt: box(nm, (sx, dy, sz), (a, D - dy / 2, z), mt, bevel=0.003)
    else:
        P = lambda nm, sx, sz, a, z, dy, mt: box(nm, (dy, sx, sz), (dy / 2, a, z), mt, bevel=0.003)
    pm, fm = (panel_wood, field) if axis == "x" else (panel_wood_y, field_y)
    P("Dado_Board", L, DADO, mid, DADO / 2, 0.02, pm)
    P("Dado_TopRail", L, 0.09, mid, DADO - 0.045, 0.032, pm)
    P("Dado_BottomRail", L, 0.06, mid, SKIRT + 0.03, 0.032, pm)
    for i in range(n + 1 if L > 0.3 else 0):             # a short return gets plain boarding, no squeezed panel
        P("Dado_Stile", 0.08, DADO - SKIRT - 0.15, a0 + i * pw + (0.04 if i == 0 else -0.04 if i == n else 0),
          SKIRT + 0.06 + (DADO - SKIRT - 0.15) / 2, 0.032, pm)
    fh = DADO - SKIRT - 0.15 - 0.06
    for i in range(n if L > 0.3 else 0):
        P("Dado_Field", pw - 0.08 - 0.06, fh, a0 + (i + 0.5) * pw, SKIRT + 0.06 + 0.03 + fh / 2, 0.042, fm)
    P("Dado_Cap", L, 0.03, mid, DADO + 0.015, 0.05, pm)                 # moulded dado rail
    P("Dado_CapBead", L, 0.018, mid, DADO - 0.01, 0.04, pm)
    P("Skirting", L, SKIRT, mid, SKIRT / 2, 0.034, pm)
    P("Skirting_Top", L, 0.03, mid, SKIRT - 0.015, 0.045, pm)


dado_run("y", 0.0, WIN_Y[0] - 0.08)
dado_run("y", WIN_Y[1] + 0.08, D)
box("Dado_UnderWindow", (0.02, WIN_Y[1] - WIN_Y[0] + 0.16, DADO), (0.01, sum(WIN_Y) / 2, DADO / 2), panel_wood_y,
    bevel=0.003)
box("Skirting_UnderWindow", (0.034, WIN_Y[1] - WIN_Y[0] + 0.16, SKIRT), (0.017, sum(WIN_Y) / 2, SKIRT / 2),
    panel_wood_y, bevel=0.003)
dado_run("x", 0.0, FX - FW / 2)
dado_run("x", FX + FW / 2, BOOK_X0)
dado_run("x", BOOK_X0 + 2.4, W)

# Six-over-six timber sash window: architrave, reveal linings, box frame, two sashes, glazing bars, window board.
wy, wz = sum(WIN_Y) / 2, sum(WIN_Z) / 2
ww, wh = WIN_Y[1] - WIN_Y[0], WIN_Z[1] - WIN_Z[0]
paint_white = surface(mat("cream", 0.45, color=shade(COLORS["cream"], 0.92)), "plaster", scale=3)
for nm, size, loc in (("Top", (T, ww, 0.02), (-T / 2, wy, WIN_Z[1] - 0.01)),
                      ("Front", (T, 0.02, wh), (-T / 2, WIN_Y[0] + 0.01, wz)),
                      ("Back", (T, 0.02, wh), (-T / 2, WIN_Y[1] - 0.01, wz))):
    box(f"Window_Lining_{nm}", size, loc, paint_white, bevel=0.002)
for nm, size, loc in (("Top", (0.025, ww + 0.2, 0.09), (0.0125, wy, WIN_Z[1] + 0.045)),
                      ("Front", (0.025, 0.09, wh + 0.02), (0.0125, WIN_Y[0] - 0.045, wz)),
                      ("Back", (0.025, 0.09, wh + 0.02), (0.0125, WIN_Y[1] + 0.045, wz))):
    box(f"Window_Architrave_{nm}", size, loc, paint_white, bevel=0.006)
box("Window_Board", (T + 0.05, ww + 0.14, 0.03), (-T / 2 + 0.025, wy, WIN_Z[0] - 0.015), paint_white, bevel=0.006)
box("Window_Apron", (0.03, ww + 0.1, 0.07), (0.015, wy, WIN_Z[0] - 0.065), paint_white, bevel=0.003)  # proud of the dado
fr = []
for xx, z0, z1, bottom in ((-0.105, wz - 0.02, WIN_Z[1] - 0.02, 0.045), (-0.07, WIN_Z[0], wz + 0.02, 0.075)):
    zc, sh = (z0 + z1) / 2, z1 - z0
    fr += [((0.035, 0.045, sh), (xx, WIN_Y[0] + 0.0425, zc), (0, 0, 0)),
           ((0.035, 0.045, sh), (xx, WIN_Y[1] - 0.0425, zc), (0, 0, 0)),
           ((0.035, ww - 0.04, 0.045), (xx, wy, z1 - 0.0225), (0, 0, 0)),
           ((0.035, ww - 0.04, bottom), (xx, wy, z0 + bottom / 2), (0, 0, 0))]
    gy0, gy1, gz0, gz1 = WIN_Y[0] + 0.065, WIN_Y[1] - 0.065, z0 + bottom, z1 - 0.045
    fr += [((0.02, 0.016, gz1 - gz0), (xx - 0.005, gy0 + (gy1 - gy0) * k / 3, (gz0 + gz1) / 2), (0, 0, 0)) for k in (1, 2)]
    fr += [((0.02, gy1 - gy0, 0.016), (xx - 0.005, wy, (gz0 + gz1) / 2), (0, 0, 0))]
boxes("Window_Sashes", fr, paint_white, bevel=0.003)
box("Window_SashLock", (0.02, 0.06, 0.012), (-0.045, wy, wz + 0.03), brass(), bevel=0.003)
glass = box("Window_Glass", (0.005, ww, wh), (-0.125, wy, wz), mat("sky", 0.1, emit=1.0 if NIGHT else 1.3), bevel=0)
no_shadow(glass)
if RAIN and NIGHT:                                  # streaks on the glass
    streaks = []
    for k in range(52):
        ln = random.uniform(0.05, 0.26)
        streaks.append(((0.003, 0.004, ln), (-0.118, random.uniform(WIN_Y[0] + 0.05, WIN_Y[1] - 0.05),
                                             random.uniform(WIN_Z[0] + ln / 2 + 0.05, WIN_Z[1] - ln / 2)),
                        (R(random.uniform(-6, 6)), 0, 0)))
    no_shadow(boxes("Window_Rain", streaks, mat("rain", 0.1, emit=1.1, color=shade(COLORS["sky"], 1.7)), bevel=0))
sil = [((0.004, random.uniform(0.1, 0.24), random.uniform(0.15, 0.5)), (-0.13, y, WIN_Z[0] + 0.12), (0, 0, 0))
       for y in [WIN_Y[0] + 0.07 + i * 0.12 for i in range(8)]]
no_shadow(boxes("Window_Rooftops", sil, mat("skyline", 0.9, color=shade(COLORS["sky"], 0.55 if NIGHT else 0.8)), bevel=0))

# Velvet curtains on a brass pole with rings, gathered by tie-backs (real pinch-pleat drape, not cylinders).
POLE_Z = WIN_Z[1] + 0.17
velvet = surface(mat("main", 0.8, color=shade(COLORS["main"], 0.92)), "fabric")
cyl("Curtain_Pole", 0.016, ww + 1.1, (0.11, wy, POLE_Z), brass(), rot=(R(90), 0, 0), segs=16)
for side in (-1, 1):
    lathe(f"Curtain_Finial_{side}", [(0.012, 0), (0.03, 0.02), (0.035, 0.045), (0.018, 0.07), (0.005, 0.085)],
          (0.11, wy + side * (ww / 2 + 0.55), POLE_Z), brass(), rot=(R(-90 * side), 0, 0), segs=16)
    box(f"Curtain_Bracket_{side}", (0.11, 0.02, 0.02), (0.055, wy + side * (ww / 2 + 0.42), POLE_Z), brass(), bevel=0.004)
    y_out = wy + side * (ww / 2 + 0.5)                      # the outer (wall) edge of the drape
    top_w, tie_z, bottom = 0.5, 1.05, FLOOR_Z + 0.01
    nu, nv, folds = 36, 22, 7
    bm = bmesh.new()
    grid = []
    for j in range(nv + 1):
        z = POLE_Z - 0.04 - (POLE_Z - 0.04 - bottom) * j / nv
        if z > tie_z:
            t = (POLE_Z - z) / (POLE_Z - tie_z)
            width = top_w + (0.2 - top_w) * t ** 1.6
        else:
            t = (tie_z - z) / (tie_z - bottom)
            width = 0.2 + 0.2 * math.sqrt(t)
        amp = 0.03 * (top_w / width) ** 0.5
        row = []
        for i in range(nu + 1):
            u = i / nu
            x = 0.085 + amp * (0.5 + 0.5 * math.sin(2 * math.pi * folds * u))
            row.append(bm.verts.new((x, y_out - side * u * width, z)))
        grid.append(row)
    for j in range(nv):
        for i in range(nu):
            bm.faces.new((grid[j][i], grid[j][i + 1], grid[j + 1][i + 1], grid[j + 1][i]))
    drape = _finish(_obj(f"Curtain_{side}", bm), velvet, 0, None, None)
    sol = drape.modifiers.new("Thickness", "SOLIDIFY")
    sol.thickness = 0.012
    for i in range(9):                                  # rings on the pole
        ring(f"Curtain_Ring_{side}_{i}", 0.024, 0.004, (0.11, y_out - side * i * top_w / 8, POLE_Z),
             brass(), rot=(0, R(90), 0), segs=16)
    lathe(f"Curtain_Holdback_{side}", [(0.01, 0), (0.012, 0.06), (0.04, 0.065), (0.035, 0.08), (0.001, 0.085)],
          (0.0, y_out - side * 0.1, tie_z), brass(), rot=(0, R(90), 0), segs=20)

# ---- Fireplace: Victorian chimneypiece (marble), arched cast-iron insert, tiled slips, coal grate, hearth, fender.
JAMB_W, JD = 0.22, 0.16                     # jamb width / how far the surround stands out from the wall
OPEN_W, OPEN_H, FRIEZE = FW - 2 * JAMB_W, 0.92, 0.3
SHELF_Z = FLOOR_Z + OPEN_H + FRIEZE         # underside of the mantel shelf
stone = marble()
for sx in (-1, 1):
    jx = FX + sx * (OPEN_W / 2 + JAMB_W / 2)
    box(f"Fire_Jamb_{sx}", (JAMB_W, JD, OPEN_H), (jx, D - JD / 2, FLOOR_Z + OPEN_H / 2), stone, bevel=0.006)
    box(f"Fire_JambPanel_{sx}", (JAMB_W - 0.08, 0.012, OPEN_H - 0.32), (jx, D - JD - 0.004, FLOOR_Z + 0.16 + (OPEN_H - 0.32) / 2),
        surface(mat("stone", 0.25, color=shade(COLORS["stone"], 0.86)), "marble"), bevel=0.003)
    box(f"Fire_Plinth_{sx}", (JAMB_W + 0.03, JD + 0.025, 0.13), (jx, D - (JD + 0.025) / 2, FLOOR_Z + 0.065), stone,
        bevel=0.006)
    box(f"Fire_Corbel_{sx}", (JAMB_W + 0.02, JD + 0.03, FRIEZE), (jx, D - (JD + 0.03) / 2, FLOOR_Z + OPEN_H + FRIEZE / 2),
        stone, bevel=0.008)
    lathe(f"Fire_Patera_{sx}", [(0.05, 0), (0.05, 0.006), (0.043, 0.008), (0.043, 0.011), (0.03, 0.013), (0.02, 0.018),
                                (0.001, 0.02)], (jx, D - JD - 0.03, FLOOR_Z + OPEN_H + FRIEZE / 2), stone,
          rot=(R(90), 0, 0), segs=36)
box("Fire_Frieze", (OPEN_W, JD - 0.01, FRIEZE), (FX, D - (JD - 0.01) / 2, FLOOR_Z + OPEN_H + FRIEZE / 2), stone, bevel=0.004)
box("Fire_ShelfMould", (FW + 0.06, JD + 0.06, 0.03), (FX, D - (JD + 0.06) / 2, SHELF_Z + 0.015), stone, bevel=0.008)
box("Fire_Shelf", (FW + 0.14, JD + 0.1, 0.045), (FX, D - (JD + 0.1) / 2, SHELF_Z + 0.0525), stone, bevel=0.008)
MZ = SHELF_Z + 0.075                        # top of the mantel shelf
# Tile slips each side of the insert (15 cm glazed tiles) and the arched cast-iron register grate.
tiles = surface(mat("accent_1", 0.2, color=shade(COLORS["accent_1"], 1.1)), "square_tile", scale=0.66)
SLIP = 0.17
for sx in (-1, 1):
    box(f"Fire_Tiles_{sx}", (SLIP, 0.02, OPEN_H - 0.02), (FX + sx * (OPEN_W / 2 - SLIP / 2), D - 0.07, FLOOR_Z + OPEN_H / 2),
        tiles, bevel=0.002)
IW = OPEN_W - 2 * SLIP                      # cast-iron insert width
AR = 0.23                                   # arch radius
ARCH_Z = FLOOR_Z + 0.42                     # where the arch starts
plate = box("Fire_Insert", (IW, 0.03, OPEN_H), (FX, D - 0.065, FLOOR_Z + OPEN_H / 2), iron(), bevel=0.004)
c1 = box("Fire_ArchCut1", (2 * AR, 0.2, ARCH_Z - FLOOR_Z + 0.01), (FX, D - 0.065, FLOOR_Z + (ARCH_Z - FLOOR_Z) / 2 - 0.005),
         mat("dark"), bevel=0)
c2 = cyl("Fire_ArchCut2", AR, 0.2, (FX, D - 0.065, ARCH_Z), mat("dark"), rot=(R(90), 0, 0), bevel=0, segs=40)
for c in (c1, c2):
    c.hide_render = c.hide_viewport = True
    mod = plate.modifiers.new("Arch", "BOOLEAN")
    mod.operation, mod.object = "DIFFERENCE", c
plate.modifiers.move(0, len(plate.modifiers) - 1)               # bevel after the cut
ring("Fire_ArchBead", AR + 0.012, 0.012, (FX, D - 0.085, ARCH_Z), iron(), rot=(R(90), 0, 0), arc=0.5, segs=30)
for sx in (-1, 1):
    box(f"Fire_ArchBeadSide_{sx}", (0.024, 0.024, ARCH_Z - FLOOR_Z), (FX + sx * (AR + 0.012), D - 0.085,
        FLOOR_Z + (ARCH_Z - FLOOR_Z) / 2), iron(), bevel=0.008)
box("Fire_Back", (2 * AR, 0.03, OPEN_H - 0.15), (FX, D - 0.015, FLOOR_Z + (OPEN_H - 0.15) / 2),
    mat("dark", 0.95, color=shade(COLORS["dark"], 0.7)), bevel=0)
grate = []
for k in range(4):                                              # front bars of the coal basket
    grate.append(((2 * AR - 0.06, 0.012, 0.012), (FX, D - 0.115, FLOOR_Z + 0.1 + k * 0.035), (0, 0, 0)))
for sx in (-1, 0, 1):
    grate.append(((0.014, 0.014, 0.16), (FX + sx * (AR - 0.05), D - 0.115, FLOOR_Z + 0.08), (0, 0, 0)))
boxes("Fire_Grate", grate, iron(), bevel=0.003)
box("Fire_GrateBed", (2 * AR - 0.06, 0.08, 0.012), (FX, D - 0.075, FLOOR_Z + 0.1), iron(), bevel=0.002)
fret = box("Fire_Fret", (2 * AR - 0.01, 0.012, 0.085), (FX, D - 0.128, FLOOR_Z + 0.045), iron(), bevel=0.003)
boxes("Fire_FretSlots", [((0.012, 0.004, 0.05), (FX + k * 0.035, D - 0.135, FLOOR_Z + 0.045), (0, 0, 0))
                         for k in range(-5, 6)], mat("dark", 0.9, color=shade(COLORS["dark"], 0.6)), bevel=0)
# A heap of real coal: faceted lumps piled higher in the middle; the lower, inner ones glow.
coal = mat("dark", 0.9, color=shade(COLORS["dark"], 0.45))
_set(_principled(coal), ["Specular IOR Level", "Specular"], 0.15)


def fire_glow(hex_color, strength):
    """Pure emission (black base) so flames and embers keep their colour instead of washing out to white."""
    m = mat("fire_glow", 1.0, emit=strength, color=hex_color)
    _set(_principled(m), ["Base Color"], (0.0, 0.0, 0.0, 1.0))        # the fire light right in front must not
    _set(_principled(m), ["Specular IOR Level", "Specular"], 0.0)     # wash the glow out to peach
    return m


ember = fire_glow("#D9481A", 1.6 if NIGHT else 0.3)          # deep red-orange glow between black coals
rnd = random.Random(SEED + 3)
lumps = {True: [], False: []}
for k in range(60):
    x = rnd.uniform(-AR + 0.07, AR - 0.07)
    top = FLOOR_Z + 0.2 + 0.07 * (1 - (x / AR) ** 2)
    z = rnd.uniform(FLOOR_Z + 0.12, top)
    lit = rnd.random() < ((0.55 if z < top - 0.035 else 0.08) if NIGHT else 0.06)
    s_ = rnd.uniform(0.016, 0.028)
    lumps[lit].append(((FX + x, rnd.uniform(D - 0.105, D - 0.04), z), (s_ * rnd.uniform(1, 1.5), s_, s_ * rnd.uniform(0.7, 1)),
                       (rnd.uniform(0, 3), rnd.uniform(0, 3), rnd.uniform(0, 3))))
for lit, items in lumps.items():
    if items:
        pebbles("Fire_Coal_Lit" if lit else "Fire_Coal", items, ember if lit else coal, smooth=False)
if NIGHT and FIRE_STRENGTH > 0:
    outer, core = fire_glow(COLORS["fire"], 1.5), fire_glow("#FFB347", 1.7)   # orange tongues, yellow (not white) core
    for k in range(7):                                          # licking flames: orange tongues with a yellow core
        dx = -0.14 + k * 0.047 + rnd.uniform(-0.012, 0.012)
        fh = (0.15 if k in (2, 4) else rnd.uniform(0.05, 0.11)) * (1.15 - abs(dx) / AR)
        y0, z0, lean = D - 0.06 - 0.025 * (k % 2), FLOOR_Z + 0.21 + 0.04 * (1 - (dx / AR) ** 2), R(rnd.uniform(-15, 15))
        ph = rnd.uniform(0, 6.3)
        for m_, f, dy in ((outer, 1.0, 0.0), (core, 0.45, -0.011)):    # a wavy tongue swept up from the coals
            pts = [(0.018 * math.sin(ph + t * 4.5) * t + math.sin(lean) * fh * t, 0, fh * f * t)
                   for t in (0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9, 1.0)]
            fl = tube(f"Fire_Flame_{k}", pts, [0.022 * f, 0.028 * f, 0.026 * f, 0.021 * f, 0.015 * f, 0.009 * f,
                                               0.004 * f, 0.001], m_, segs=12)
            fl.location, fl.scale = (FX + dx, y0 + dy, z0), (1.0, 0.4, 1.0)      # flattened front to back
            no_shadow(fl)
# Hearth: slate kerb with a tiled inner hearth; brass fender with ball feet.
HD = 0.46
box("Hearth_Slate", (FW + 0.12, HD, 0.03), (FX, D - HD / 2, FLOOR_Z + 0.015),
    surface(mat("dark", 0.5, color=shade(COLORS["stone"], 0.42)), "concrete"), bevel=0.004)
box("Hearth_Tiles", (OPEN_W - 0.02, HD - JD - 0.06, 0.004), (FX, D - JD - (HD - JD - 0.06) / 2 - 0.02, FLOOR_Z + 0.032),
    surface(mat("tan", 0.35, color=shade(COLORS["tan"], 0.8)), "square_tile", along="Z", scale=1.3), bevel=0)
FEN_Y, FEN_W = D - HD + 0.04, FW - 0.05
fen = brass(0.28)
box("Fender_Front", (FEN_W, 0.012, 0.09), (FX, FEN_Y, FLOOR_Z + 0.03 + 0.045), fen, bevel=0.003)
cyl("Fender_Rail", 0.011, FEN_W + 0.02, (FX, FEN_Y, FLOOR_Z + 0.03 + 0.095), fen, rot=(0, R(90), 0), segs=14)
for sx in (-1, 1):
    box(f"Fender_Side_{sx}", (0.012, D - JD - FEN_Y - 0.03, 0.09), (FX + sx * FEN_W / 2, (FEN_Y + D - JD - 0.03) / 2,
        FLOOR_Z + 0.075), fen, bevel=0.003)
    ball(f"Fender_Foot_{sx}", 0.016, (FX + sx * FEN_W / 2, FEN_Y, FLOOR_Z + 0.04), fen)
# Fire irons on a companion stand between the fireplace and the bookcase.
CX_, CY_ = FX + FW / 2 + 0.12, D - 0.3
lathe("FireIrons_Base", [(0.075, 0), (0.075, 0.015), (0.05, 0.03), (0.012, 0.045), (0.012, 0.6), (0.02, 0.61),
                         (0.006, 0.66)], (CX_, CY_, FLOOR_Z), fen, segs=24)
box("FireIrons_Bar", (0.02, 0.14, 0.012), (CX_, CY_, FLOOR_Z + 0.58), fen, bevel=0.004, rot=(0, 0, R(30)))
for k, a in enumerate((-60, 60, 180)):
    tx, ty = CX_ + 0.055 * math.cos(R(a)), CY_ + 0.055 * math.sin(R(a))
    cyl(f"FireIrons_Tool_{k}", 0.006, 0.6, (tx, ty, FLOOR_Z + 0.33), iron(), segs=10, rot=(R(2), R(-3), 0))
    ball(f"FireIrons_Handle_{k}", 0.016, (tx, ty, FLOOR_Z + 0.64), fen, scale=(1, 1, 1.4))
box("FireIrons_Shovel", (0.07, 0.01, 0.09), (CX_ + 0.055 * math.cos(R(180)), CY_, FLOOR_Z + 0.07), iron(), bevel=0.003)
box("FireIrons_Brush", (0.05, 0.04, 0.08), (CX_ + 0.03, CY_ - 0.05, FLOOR_Z + 0.06), mat("dark", 0.95), bevel=0.01)

# Inscribed frieze panel: your name + role cut into a slate panel and gilded (a real college-hall detail).
PLZ = FLOOR_Z + OPEN_H + FRIEZE / 2
plaque = box("Name_Panel", (OPEN_W - 0.06, 0.012, FRIEZE - 0.05), (FX, D - JD - 0.002, PLZ),
             surface(mat("dark", 0.45, color=shade(COLORS["dark"], 1.15)), "concrete", scale=2), bevel=0.003)
fil = [((OPEN_W - 0.05, 0.006, 0.008), (FX, D - JD - 0.009, PLZ + sz * (FRIEZE / 2 - 0.036)), (0, 0, 0)) for sz in (-1, 1)]
fil += [((0.008, 0.006, FRIEZE - 0.064), (FX + sx * (OPEN_W / 2 - 0.036), D - JD - 0.009, PLZ), (0, 0, 0)) for sx in (-1, 1)]
boxes("Name_Fillet", fil, GOLD_TEXT, bevel=0.0)
hook_link(plaque, "website")
hook_text("name", 1, "YOUR NAME", 0.12, (FX, D - JD - 0.011, PLZ + 0.04), material=GOLD_TEXT, max_width=OPEN_W - 0.16,
          depth=0.004)
hook_text("role", 1, "your role", 0.065, (FX, D - JD - 0.011, PLZ - 0.07), material=mat("cream", 0.5, emit=0.35 if NIGHT
          else 0.0), max_width=OPEN_W - 0.2, depth=0.003)

# Mantel garniture: a bracket clock, a pair of turned brass candlesticks, a plaster bust and two books.
for sx in (-1, 1):
    cx_ = FX + sx * 0.64
    lathe(f"Mantel_Candlestick_{sx}", [(0.045, 0), (0.045, 0.012), (0.032, 0.02), (0.012, 0.04), (0.017, 0.07),
                                       (0.009, 0.1), (0.011, 0.19), (0.022, 0.2), (0.016, 0.215), (0.013, 0.215)],
          (cx_, D - 0.09, MZ), brass(0.25), segs=24)
    cyl(f"Mantel_Candle_{sx}", 0.012, 0.16, (cx_, D - 0.09, MZ + 0.295), surface(mat("cream", 0.5), "ceramic"), segs=16)
    no_shadow(ball(f"Mantel_Flame_{sx}", 0.011, (cx_, D - 0.09, MZ + 0.39), glow("#FFC25A", 8.0 if NIGHT else 1.0),
                   scale=(1, 1, 1.9)))
CLX = FX - 0.3
clock_case = wood(0.85, 0.3)
box("Clock_Case", (0.2, 0.11, 0.2), (CLX, D - 0.09, MZ + 0.115), clock_case, bevel=0.006)
box("Clock_Plinth", (0.23, 0.13, 0.02), (CLX, D - 0.09, MZ + 0.01), clock_case, bevel=0.004)
half_cyl("Clock_Top", 0.1, 0.11, (CLX, D - 0.09, MZ + 0.215), clock_case, rot=(0, 0, R(90)))
lathe("Clock_Finial", [(0.012, 0), (0.016, 0.01), (0.006, 0.03), (0.001, 0.04)], (CLX, D - 0.09, MZ + 0.31), brass())
cyl("Clock_Dial", 0.062, 0.006, (CLX, D - 0.147, MZ + 0.13), surface(mat("cream", 0.4), "paper"), rot=(R(90), 0, 0))
ring("Clock_Bezel", 0.064, 0.006, (CLX, D - 0.149, MZ + 0.13), brass(0.25), rot=(R(90), 0, 0), segs=32)
for nm, ang, ln_ in (("Clock_HourHand", -60, 0.034), ("Clock_MinHand", 60, 0.05)):   # ten past ten
    box(nm, (0.004, 0.003, ln_), (CLX + math.sin(R(ang)) * ln_ / 2, D - 0.152, MZ + 0.13 + math.cos(R(ang)) * ln_ / 2),
        mat("dark"), bevel=0, rot=(0, R(ang), 0))
for sx in (-1, 1):
    ball(f"Clock_Foot_{sx}", 0.012, (CLX + sx * 0.09, D - 0.09, MZ + 0.004), brass(), scale=(1, 1, 0.6))
BX = FX + 0.32                              # blue-and-white ginger jar with a domed lid
jar = surface(mat("navy", 0.15, color=shade(COLORS["navy"], 1.25)), "ceramic")
lathe("Jar_Body", [(0.045, 0), (0.07, 0.04), (0.078, 0.09), (0.068, 0.15), (0.045, 0.175), (0.04, 0.185)],
      (BX, D - 0.1, MZ), jar, segs=32)
lathe("Jar_Lid", [(0.046, 0), (0.046, 0.012), (0.03, 0.035), (0.012, 0.045), (0.016, 0.055), (0.001, 0.06)],
      (BX, D - 0.1, MZ + 0.183), jar, segs=32)
for zz, rr in ((0.05, 0.073), (0.12, 0.075)):
    ring("Jar_Band", rr, 0.004, (BX, D - 0.1, MZ + zz), surface(mat("cream", 0.15), "ceramic"), segs=32)
for i, (key, bw_) in enumerate((("navy", 0.035), ("main", 0.042))):
    box(f"Mantel_Book_{i}", (bw_, 0.16, 0.23 - i * 0.02), (FX + 0.5 - i * 0.045, D - 0.1, MZ + 0.115 - i * 0.01),
        leather(key, 0.95, 0.6), bevel=0.004)

# Oil painting over the mantel (picture hook) with a brass picture light.
over = anchor("OverMantel", (FX, D, 0))
PZ = 2.02
painting(over, 0, PZ, 0.8, 0.6, 0, "poster", 1, "landscape")
picture_light(over, 0, PZ + 0.3 + 0.075, 0.46, 0)


# =====================================================================
#  FURNITURE SLOTS  (same names in every template)
#  size = (width, depth, height); front of the furniture faces local -Y
# =====================================================================
slot("shelf",      (2.4, 0.42, 2.84), (BOOK_X0 + 1.2, D - 0.21), shape="shelf")
slot("desk",       (1.52, 0.92, 0.76), (0.66, wy), turn=90, shape="table")
slot("chair",      (0.58, 0.56, 0.86), (1.43, wy), turn=-90, shape="chair")
slot("lamp",       (0.26, 0.2, 0.38), (0.42, wy + 0.5), z=FLOOR_Z + 0.76, turn=90, kind="surface", shape="lamp")
slot("armchair",   (0.85, 0.9, 1.08), (3.45, 2.25), turn=32, shape="chair")
slot("side_table", (0.56, 0.56, 0.69), (2.53, 1.72), shape="table")
slot("floor_lamp", (0.44, 0.44, 1.56), (4.12, 3.15), turn=20, shape="lamp")
slot("hero_prop",  (0.62, 0.62, 1.05), (1.15, 0.78), turn=30, shape="box")
slot("rug",        (2.7, 1.9, 0.012), (2.75, 1.78), kind="rug", shape="rug")
slot("wall_art",   (1.3, 0.05, 0.62), (0.025, 0.85), z=1.3, turn=90, kind="wall", shape="frame")


# =====================================================================
#  PLACEHOLDER FURNITURE  (replaced when you add your own with add_furniture.py)
# =====================================================================
BOOK_KEYS = ["main", "accent_1", "navy", "tan", "cream", "dark"]


def build_shelf():
    """Built-in library bookcase: plinth, panelled base cupboards, open shelves with books, cornice,
    a brass rail and a hook-on library ladder."""
    root, w, d, h = furniture_root("shelf")
    hook_link(root, "github")
    case, case_z = wood(1.0, 0.4), wood(1.0, 0.4, along="Z")
    back_m = wood(0.72, 0.6, along="Z", kind="veneer")
    base_h, up_d = 0.86, 0.30                    # cupboard height, depth of the open shelves
    up_y = d / 2 - up_d                          # front face of the upper shelves (local y)
    bays = 3
    stile = 0.05
    bay_w = (w - (bays + 1) * stile) / bays
    bx = [-w / 2 + stile + bay_w / 2 + i * (bay_w + stile) for i in range(bays)]
    # Base cupboards
    box("Shelf_Plinth", (w, d - 0.02, 0.1), (0, 0.01, 0.05), wood(0.75), bevel=0.003, parent=root)
    box("Shelf_BaseCarcass", (w, d, base_h - 0.14), (0, 0, 0.1 + (base_h - 0.14) / 2), wood(1.0, 0.4, along="Y"),
        bevel=0.002, parent=root)                # grain runs front-to-back on the exposed end panel
    box("Shelf_Worktop", (w + 0.02, d + 0.02, 0.035), (0, -0.01, base_h - 0.0225), case, bevel=0.005, parent=root)
    box("Shelf_WorktopMould", (w, 0.02, 0.025), (0, -d / 2 - 0.005, base_h - 0.05), case, bevel=0.004, parent=root)
    doors, fields = [], []
    for x in bx:
        for sx in (-1, 1):
            dx = x + sx * bay_w / 4
            doors.append(((bay_w / 2 - 0.004, 0.02, base_h - 0.22), (dx, -d / 2 - 0.008, 0.11 + (base_h - 0.22) / 2), (0, 0, 0)))
            fields.append(((bay_w / 2 - 0.1, 0.012, base_h - 0.38), (dx, -d / 2 - 0.022, 0.11 + (base_h - 0.22) / 2), (0, 0, 0)))
            ball("Shelf_Knob", 0.011, (x + sx * 0.03, -d / 2 - 0.028, 0.11 + (base_h - 0.22) * 0.62), brass(), parent=root)
    boxes("Shelf_Doors", doors, case_z, bevel=0.004, parent=root)
    boxes("Shelf_DoorFields", fields, wood(1.12, 0.4, along="Z"), bevel=0.01, parent=root, segs=2)
    # Upper carcass: uprights (face-frame stiles), back boards, cornice
    top_z = h - 0.16
    for i in range(bays + 1):
        x = -w / 2 + stile / 2 + i * (bay_w + stile)
        box("Shelf_Upright", (stile, up_d, top_z - base_h), (x, up_y + up_d / 2, base_h + (top_z - base_h) / 2), case_z,
            bevel=0.004, parent=root)
    box("Shelf_Back", (w, 0.02, top_z - base_h), (0, d / 2 - 0.01, base_h + (top_z - base_h) / 2), back_m, bevel=0,
        parent=root)
    box("Shelf_Frieze", (w, up_d, 0.1), (0, up_y + up_d / 2, top_z + 0.05), case, bevel=0.003, parent=root)
    for i, (dz, dd, hh) in enumerate(((0.1, 0.02, 0.025), (0.125, 0.045, 0.02), (0.145, 0.07, 0.015))):
        box("Shelf_Cornice", (w + 2 * dd, up_d + dd, hh), (0, up_y + (up_d - dd) / 2, top_z + dz + hh / 2), case,
            bevel=0.004, parent=root)
    # Shelves: 20 mm boards with a 35 mm front lip, 4 open levels
    levels = 4
    gap = (top_z - base_h) / levels
    for lv in range(1, levels):
        zb = base_h + lv * gap
        box("Shelf_Board", (w - 0.02, up_d - 0.03, 0.02), (0, up_y + up_d / 2, zb - 0.01), case, bevel=0.002, parent=root)
        box("Shelf_Lip", (w - 0.02, 0.02, 0.035), (0, up_y + 0.01, zb - 0.0175), case, bevel=0.003, parent=root)
    by_key = {k: [] for k in BOOK_KEYS}
    bands, labels, decor = [], [], []
    hero_level, hero_bay = 2, 1                  # eye-level shelf, middle bay: your titles go here
    for lv in range(levels):
        zb = base_h + lv * gap
        for bay, x in enumerate(bx):
            x0, x1 = x - bay_w / 2 + 0.01, x + bay_w / 2 - 0.01
            hero = lv == hero_level and bay == hero_bay
            cursor = x0 + (0.5 if hero else 0.0)
            gap_at = random.uniform(x0 + 0.12, x1 - 0.22) if (random.random() < 0.5 and not hero) else None
            if lv == 3 and bay == 0:
                gap_at, decor_kind = x0 + 0.03, "bust"
            else:
                decor_kind = random.choice(("stack", "hourglass", "pot", "stack", "bookend"))
            while cursor < x1 - 0.02:
                if gap_at is not None and cursor > gap_at:          # room for a small object
                    decor.append((cursor + 0.09, zb, decor_kind))
                    cursor += 0.19
                    gap_at = None
                    continue
                bw = random.choice((0.022, 0.028, 0.032, 0.038, 0.045, 0.055))
                bh = min(gap - 0.05, random.choice((0.19, 0.21, 0.23, 0.24, 0.26, 0.29, 0.31)) * random.uniform(0.96, 1.04))
                bd = min(up_d - 0.05, bh * random.uniform(0.66, 0.8))
                if cursor + bw > x1:
                    break
                key = random.choice(BOOK_KEYS[:4] * 3 + BOOK_KEYS[4:])
                lean = R(random.uniform(5, 10)) if (random.random() < 0.05 and cursor > x0 + 0.1) else 0.0
                y = up_y + 0.015 + bd / 2
                by_key[key].append(((bw, bd, bh), (cursor + bw / 2, y, zb + bh / 2 + abs(lean) * bw), (0, lean, 0)))
                if key in ("main", "accent_1", "navy", "tan", "dark") and random.random() < 0.55:
                    for bz in (0.1, 0.16, 0.86):            # gilt bands across old leather spines
                        bands.append(((bw + 0.001, 0.003, 0.004), (cursor + bw / 2, y - bd / 2 - 0.001, zb + bh * bz),
                                      (0, lean, 0)))
                    labels.append(((bw * 0.8, 0.003, bh * 0.12), (cursor + bw / 2, y - bd / 2 - 0.0015, zb + bh * 0.74),
                                   (0, lean, 0)))
                cursor += bw + random.uniform(0.0, 0.004) + abs(lean) * bh * 0.5
    for key, parts in by_key.items():
        if parts:
            m = surface(mat(key, 0.62), "paper" if key == "cream" else "leather")
            boxes(f"Shelf_Books_{key}", parts, m, bevel=0.0025, parent=root)
    if bands:
        boxes("Shelf_Book_Bands", bands, brass(0.4), bevel=0, parent=root)
    if labels:
        boxes("Shelf_Book_Labels", labels, mat("dark", 0.5, color=shade(COLORS["main"], 0.55)), bevel=0, parent=root)
    pm = surface(mat("cream", 0.75, color=shade(COLORS["cream"], 1.05)), "plaster", scale=4)
    for k, (x, z, kind) in enumerate(decor):
        y = up_y + up_d / 2
        if kind == "stack":
            for j in range(3):
                lying_book("Shelf_Stack", (0.19 - j * 0.015, 0.15, 0.032), (x, y, z + j * 0.033),
                           random.choice(BOOK_KEYS[:4]), random.uniform(-6, 6), parent=root)
        elif kind == "hourglass":
            for zz in (0.006, 0.164):
                cyl("Shelf_HourglassCap", 0.04, 0.012, (x, y, z + zz), wood(0.85), parent=root)
            for k2 in range(3):
                a = R(90 + 120 * k2)
                cyl("Shelf_HourglassPost", 0.004, 0.15, (x + 0.032 * math.cos(a), y + 0.032 * math.sin(a), z + 0.085),
                    wood(0.85), segs=8, parent=root)
            lathe("Shelf_HourglassGlass", [(0.025, 0.012), (0.026, 0.04), (0.004, 0.085), (0.026, 0.13), (0.025, 0.158)],
                  (x, y, z), mat("accent_3", 0.05), segs=20, parent=root)
        elif kind == "pot":
            lathe("Shelf_Pot", [(0.03, 0), (0.042, 0.07), (0.047, 0.075), (0.047, 0.085), (0.042, 0.085)],
                  (x, y, z), surface(mat("tan", 0.8, color=shade(COLORS["tan"], 1.05)), "ceramic"), segs=20, parent=root)
            cyl("Shelf_Soil", 0.041, 0.004, (x, y, z + 0.08), mat("dark", 0.95), parent=root)
            for j in range(6):
                ball("Shelf_Leaf", 0.03, (x + math.cos(j * 1.05) * 0.035, y + math.sin(j * 1.05) * 0.03, z + 0.11 + (j % 2) * 0.02),
                     surface(mat("plant", 0.6), "ceramic"), scale=(1.4, 0.7, 0.45), parent=root)
        elif kind == "bookend":
            box("Shelf_Bookend", (0.012, 0.11, 0.15), (x - 0.06, y, z + 0.075), brass(0.35), bevel=0.003, parent=root)
            for j in range(4):
                box("Shelf_Leaning", (0.03, 0.15, 0.22), (x - 0.03 + j * 0.032, y, z + 0.11), leather(BOOK_KEYS[j % 4], 0.9, 0.6),
                    bevel=0.003, rot=(0, R(-12 if j == 3 else 0), 0), parent=root)
        else:                                                   # a plaster bust on its socle
            lathe("Shelf_BustSocle", [(0.05, 0), (0.05, 0.02), (0.022, 0.06), (0.03, 0.075), (0.001, 0.08)],
                  (x, y, z), pm, segs=20, parent=root)
            ball("Shelf_BustBody", 0.08, (x, y, z + 0.11), pm, scale=(1.2, 0.6, 0.55), parent=root)
            cyl("Shelf_BustNeck", 0.022, 0.06, (x, y, z + 0.165), pm, segs=12, parent=root)
            ball("Shelf_BustHead", 0.045, (x, y - 0.004, z + 0.22), pm, scale=(0.82, 0.95, 1.12), parent=root)
            ball("Shelf_BustHair", 0.047, (x, y + 0.006, z + 0.235), pm, scale=(0.86, 0.9, 0.95), parent=root)
            ball("Shelf_BustNose", 0.007, (x, y - 0.043, z + 0.218), pm, scale=(0.8, 1.0, 1.5), parent=root)
    # Hero books: four big folios lying flat at eye level with YOUR project titles in gilt (title hooks).
    hx = bx[hero_bay] - bay_w / 2 + 0.26
    hz = base_h + hero_level * gap
    for i, key in enumerate(("main", "accent_1", "navy", "tan")):
        bt, bl = 0.06, 0.46 - i * 0.03
        bxx, bzz = hx + random.uniform(-0.01, 0.01), hz + bt / 2 + i * bt
        lying_book(f"Shelf_HeroBook_{i}", (bl, 0.25, bt), (bxx, up_y + 0.145, bzz - bt / 2), key, parent=root)
        for sx in (-1, 1):
            box("Shelf_HeroBand", (0.006, 0.003, bt - 0.01), (bxx + sx * (bl / 2 - 0.035), up_y + 0.019, bzz), brass(0.4),
                bevel=0, parent=root)
        hook_text("title", 4 - i, "Project Title", 0.04, (bxx, up_y + 0.017, bzz), material=GOLD_TEXT,
                  max_width=bl - 0.1, parent=root, depth=0.002)
    # Brass rail on brackets + hook-on library ladder (left bay).
    rail_z, rail_y = 2.3, up_y - 0.06
    b = brass(0.28)
    cyl("Shelf_Rail", 0.0127, w - 0.04, (0, rail_y, rail_z), b, rot=(0, R(90), 0), segs=16, parent=root)
    for x in [-w / 2 + stile / 2 + i * (bay_w + stile) for i in range(bays + 1)]:
        box("Shelf_RailBracket", (0.018, 0.06, 0.03), (x, rail_y + 0.03, rail_z), b, bevel=0.004, parent=root)
        lathe("Shelf_RailRose", [(0.022, 0), (0.022, 0.006), (0.012, 0.012)], (x, up_y, rail_z), b, segs=16,
              rot=(R(90), 0, 0), parent=root)
    lx, foot_y = bx[0] + 0.05, -d / 2 - 0.5
    top_y, top_z = rail_y - 0.045, rail_z + 0.1         # the stiles stand just in front of the rail, never through it
    ln = math.hypot(top_y - foot_y, top_z)
    ang = math.atan2(top_y - foot_y, top_z)
    lad = wood(1.1, 0.4, along="Z")
    for sx in (-1, 1):
        x_ = lx + sx * 0.222
        box("Ladder_Stile", (0.032, 0.07, ln), (x_, (foot_y + top_y) / 2, top_z / 2), lad, bevel=0.005,
            rot=(-ang, 0, 0), parent=root)
        cyl("Ladder_Wheel", 0.028, 0.02, (x_, foot_y - 0.01, 0.028), mat("dark", 0.4), rot=(0, R(90), 0),
            segs=16, parent=root)
        # flat brass hook strap: screwed to the back of the stile, over the top of the rail and down behind it
        boxes("Ladder_Hook", [((0.026, 0.006, 0.09), (x_, rail_y - 0.034, rail_z + 0.035), (0, 0, 0)),
                              ((0.026, 0.06, 0.006), (x_, rail_y - 0.007, rail_z + 0.0165), (0, 0, 0)),
                              ((0.026, 0.006, 0.05), (x_, rail_y + 0.02, rail_z - 0.006), (0, 0, 0))], b, bevel=0.0015,
              parent=root)
    for k in range(8):
        t = (k + 0.85) / 8.6
        box("Ladder_Tread", (0.41, 0.1, 0.022), (lx, foot_y + (top_y - foot_y) * t - 0.03, top_z * t), lad, bevel=0.004,
            parent=root)


def build_desk():
    """Partners' pedestal desk: plinths, twin pedestals of graduated drawers with brass bail handles,
    a frieze drawer over the knee-hole and a gilt-tooled leather top."""
    root, w, d, h = furniture_root("desk")
    case, case_z = wood(1.0, 0.36), wood(1.0, 0.36, along="Z")
    front = wood(1.15, 0.33)                                     # flame-mahogany drawer fronts
    ped_w, top_t, plinth = 0.47, 0.03, 0.07
    top_z = h - top_t
    b = brass(0.3)

    def bail(x, z, y):
        """Brass swan-neck bail handle: two round back-plates and a hanging loop."""
        for sx in (-1, 1):
            cyl("Desk_Backplate", 0.012, 0.004, (x + sx * 0.035, y - 0.002, z + 0.006), b, rot=(R(90), 0, 0), segs=14,
                parent=root)
        ring("Desk_Bail", 0.035, 0.0035, (x, y - 0.012, z + 0.006), b, rot=(R(-70), 0, 0), arc=0.5, segs=16, parent=root)

    for sx in (-1, 1):
        px = sx * (w / 2 - ped_w / 2 - 0.01)
        box("Desk_Plinth", (ped_w - 0.02, d - 0.04, plinth), (px, 0, plinth / 2), wood(0.75), bevel=0.004, parent=root)
        box("Desk_Pedestal", (ped_w, d - 0.02, top_z - 0.1 - plinth), (px, 0, plinth + (top_z - 0.1 - plinth) / 2), case_z,
            bevel=0.003, parent=root)
        z = plinth + 0.005
        for k, dh in enumerate((0.21, 0.17, 0.14)):              # graduated drawers, 4 mm gaps
            box("Desk_Drawer", (ped_w - 0.05, 0.02, dh - 0.004), (px, -d / 2 + 0.002, z + dh / 2), front, bevel=0.004,
                parent=root)
            bail(px, z + dh / 2, -d / 2 - 0.008)
            z += dh
        box("Desk_PedBack", (ped_w - 0.05, 0.02, top_z - 0.1 - plinth - 0.02), (px, d / 2 - 0.002, plinth +
            (top_z - 0.1 - plinth) / 2), front, bevel=0.004, parent=root)
    box("Desk_FriezeRail", (w - 0.02, d - 0.02, 0.1), (0, 0, top_z - 0.05), case, bevel=0.003, parent=root)
    for x, dw in ((-(w / 2 - ped_w / 2 - 0.01), ped_w - 0.05), (0, w - 2 * ped_w - 0.07), (w / 2 - ped_w / 2 - 0.01, ped_w - 0.05)):
        box("Desk_FriezeDrawer", (dw, 0.02, 0.085), (x, -d / 2 + 0.002, top_z - 0.05), front, bevel=0.004, parent=root)
        bail(x, top_z - 0.05, -d / 2 - 0.008)
    box("Desk_Modesty", (w - 2 * ped_w - 0.02, 0.02, top_z - 0.1 - 0.15), (0, d / 2 - 0.08, 0.15 + (top_z - 0.25) / 2),
        front, bevel=0.003, parent=root)
    box("Desk_Top", (w + 0.03, d + 0.03, top_t), (0, 0, top_z + top_t / 2), case, bevel=0.006, parent=root)
    box("Desk_Leather", (w - 0.1, d - 0.1, 0.002), (0, 0, h + 0.001), leather("accent_1", 0.85, 0.55), bevel=0.0,
        parent=root)
    tool = [((w - 0.13, 0.004, 0.0006), (0, sy * (d / 2 - 0.065), h + 0.0022), (0, 0, 0)) for sy in (-1, 1)]
    tool += [((0.004, d - 0.13, 0.0006), (sx * (w / 2 - 0.065), 0, h + 0.0022), (0, 0, 0)) for sx in (-1, 1)]
    boxes("Desk_GiltTooling", tool, GOLD_TEXT, bevel=0, parent=root)
    # Book on a reading stand: the open pages are a picture hook.
    sx_, sy_, tilt = -0.12, 0.08, R(-25)
    box("Desk_Stand_Base", (0.42, 0.24, 0.015), (sx_, sy_, h + 0.0095), case, bevel=0.003, parent=root)
    box("Desk_Stand_Ledge", (0.44, 0.03, 0.025), (sx_, sy_ - 0.1, h + 0.025), case, bevel=0.003, parent=root)
    box("Desk_Stand_Back", (0.4, 0.015, 0.3), (sx_, sy_ + 0.03, h + 0.155), case, bevel=0.003, rot=(tilt, 0, 0), parent=root)
    box("Desk_Book_Cover", (0.47, 0.012, 0.32), (sx_, sy_ + 0.012, h + 0.17), leather("main", 0.8, 0.5), bevel=0.004,
        rot=(tilt, 0, 0), parent=root)
    for side in (-1, 1):                                       # page blocks, slightly domed
        box("Desk_Book_Pages", (0.215, 0.014, 0.3), (sx_ + side * 0.112, sy_ + 0.0, h + 0.172),
            surface(mat("cream", 0.7), "paper"), bevel=0.005, rot=(tilt, R(side * -4), 0), parent=root)
    book = hook_image("board", 1, (0.42, 0.28), (sx_, sy_ - 0.0165, h + 0.176), rot=(tilt, 0, 0), parent=root)
    page = anchor("Desk_PageFrame", (sx_, sy_ - 0.0165, h + 0.176), coll=COL_FURN, parent=root)
    page.rotation_euler = (tilt, 0, 0)                          # lines of text lie in the tilted page plane
    lines = [((0.16 if z < 0.09 else 0.09, 0.002, 0.0028), (dx, -0.002, z), (0, 0, 0))
             for dx in (-0.105, 0.105) for z in (-0.11, -0.085, -0.06, -0.035, -0.01, 0.015, 0.04, 0.065, 0.1)]
    hook_default(book, boxes("Desk_Book_Lines", lines, mat("tan", 0.8, color=shade(COLORS["tan"], 0.7)), bevel=0,
                             parent=page),
                 box("Desk_Book_Gutter", (0.006, 0.002, 0.28), (0, -0.002, 0), mat("tan", 0.8), bevel=0, parent=page))
    # Sealed letter (email link), brass inkstand with two cut-glass wells, a pen, a book stack.
    letter = box("Desk_Letter", (0.23, 0.15, 0.004), (-w / 2 + 0.3, -0.24, h + 0.004), surface(mat("cream", 0.7), "paper"),
                 bevel=0.001, rot=(0, 0, R(-10)), parent=root)
    hook_link(letter, "email")
    seal = cyl("Desk_Seal", 0.02, 0.006, (-w / 2 + 0.3, -0.24, h + 0.009), mat("main", 0.4, color=shade(COLORS["main"], 1.5)),
               segs=16, parent=root)
    hook_link(seal, "email")
    box("Desk_Inkstand", (0.26, 0.15, 0.015), (0.3, -0.22, h + 0.0085), b, bevel=0.004, parent=root)
    for sx in (-1, 1):
        cyl("Desk_Inkwell", 0.03, 0.05, (0.3 + sx * 0.07, -0.2, h + 0.04), mat("glass", 0.04, color="#6F8791"),
            segs=8, bevel=0.003, parent=root)                   # faceted cut glass, dark with ink
        lathe("Desk_InkCap", [(0.022, 0), (0.022, 0.012), (0.008, 0.018), (0.004, 0.03)], (0.3 + sx * 0.07, -0.2, h + 0.065),
              b, segs=16, parent=root)
    cyl("Desk_Pen", 0.005, 0.15, (0.3, -0.27, h + 0.023), mat("dark", 0.3), rot=(0, R(90), R(8)), segs=10, parent=root)
    for i, key in enumerate(("navy", "tan", "main")):
        lying_book("Desk_Stack", (0.24 - i * 0.02, 0.17, 0.04), (-w / 2 + 0.2, 0.22, h + 0.002 + i * 0.041), key,
                   i * 7 - 4 + (180 if i == 1 else 0), parent=root)


def build_chair():
    """Captain's / smoker's-bow swivel desk chair: four-leg swivel base on castors, saddle seat with a
    leather pad, a horseshoe arm bow on turned spindles."""
    root, w, d, h = furniture_root("chair")
    oak = wood(1.15, 0.42, along="Z")
    seat_z = 0.45
    for k in range(4):                                           # splayed swivel legs + castors
        a = R(45 + 90 * k)
        tube("Chair_Leg", [(0, 0, 0.3), (0.12 * math.cos(a), 0.12 * math.sin(a), 0.2),
                           (0.24 * math.cos(a), 0.24 * math.sin(a), 0.05)], [0.022, 0.018, 0.014], oak, parent=root)
        ball("Chair_Castor", 0.022, (0.24 * math.cos(a), 0.24 * math.sin(a), 0.022), brass(0.3), parent=root)
    lathe("Chair_Column", [(0.035, 0.28), (0.035, 0.31), (0.02, 0.33), (0.028, 0.37), (0.06, 0.38), (0.06, 0.4)],
          (0, 0, 0), iron(), segs=20, parent=root)
    seat = cyl("Chair_Seat", 0.25, 0.045, (0, 0.01, seat_z - 0.022), wood(1.15, 0.42), segs=40, bevel=0.008, parent=root)
    seat.scale = (1.0, 0.92, 1.0)
    pad = cyl("Chair_Pad", 0.21, 0.03, (0, 0.0, seat_z + 0.012), leather("main", 0.9, 0.4), segs=40, bevel=0.012,
              parent=root)
    pad.scale = (1.0, 0.9, 1.0)
    bow_z, bow_r, arc = 0.66, 0.235, 0.6                          # horseshoe arm bow open to the front
    ring("Chair_Bow", bow_r, 0.02, (0, 0.02, bow_z), oak, rot=(0, 0, R(90 - arc * 180)), arc=arc, segs=36,
         parent=root).scale = (1.0, 1.0, 0.7)
    ring("Chair_Crest", bow_r - 0.005, 0.03, (0, 0.025, bow_z + 0.045), oak, rot=(0, 0, R(90 - 0.28 * 180)), arc=0.28,
         segs=20, parent=root).scale = (1.0, 1.0, 1.1)
    for k in range(9):                                            # turned spindles round the back
        a = R(90 - arc * 180 + 20 + k * (arc * 360 - 40) / 8)
        x, y = bow_r * math.cos(a), bow_r * math.sin(a) + 0.02
        lathe("Chair_Spindle", [(0.009, 0), (0.012, 0.06), (0.008, 0.2), (0.008, bow_z - seat_z)],
              (x * 0.97, y * 0.95, seat_z - 0.005), oak, segs=10, parent=root)
    for sx in (-1, 1):                                            # front arm supports + scrolled hand-holds
        a = R(90 - arc * 180) if sx > 0 else R(90 + arc * 180)
        x, y = bow_r * math.cos(a), bow_r * math.sin(a) + 0.02
        lathe("Chair_ArmPost", [(0.016, 0), (0.02, 0.04), (0.012, 0.1), (0.016, 0.16), (0.012, bow_z - seat_z)],
              (x, y, seat_z - 0.005), oak, segs=12, parent=root)
        box("Chair_HandHold", (0.06, 0.07, 0.028), (x, y - 0.02, bow_z + 0.004), oak, bevel=0.01, parent=root)


def build_lamp():
    """Banker's lamp: round stepped brass base, turned stem, harp arm, half-cylinder green cased-glass shade
    (white inside) and a pull chain."""
    root, w, d, h = furniture_root("lamp")
    b = brass(0.25)
    lathe("Lamp_Base", [(0.075, 0), (0.075, 0.012), (0.06, 0.022), (0.045, 0.03), (0.02, 0.04), (0.001, 0.042)],
          (0, 0, 0), b, segs=32, parent=root)
    lathe("Lamp_Stem", [(0.011, 0.04), (0.016, 0.06), (0.009, 0.08), (0.009, 0.2), (0.014, 0.21), (0.009, 0.22)],
          (0, 0.02, 0), b, segs=16, parent=root)
    tube("Lamp_Harp", [(0, 0.02, 0.215), (0, 0.0, 0.25), (0, -0.03, 0.27)], 0.006, b, parent=root)
    sz, sy = 0.285, -0.035
    shade_out = half_cyl("Lamp_Shade", 0.073, 0.235, (0, sy, sz), mat("accent_1", 0.08, emit=0.6 if NIGHT else 0.05,
                         color=shade(COLORS["accent_1"], 1.05)), rot=(R(-12), 0, 0), parent=root)
    shade_in = half_cyl("Lamp_ShadeInner", 0.069, 0.23, (0, sy, sz - 0.001), glow("#FFF1D0", 3.0 if NIGHT else 0.3),
                        rot=(R(-12), 0, 0), parent=root)
    for sx in (-1, 1):
        half_cyl("Lamp_EndCap", 0.075, 0.006, (sx * 0.12, sy, sz), b, rot=(R(-12), 0, 0), parent=root)
    no_shadow(shade_out, shade_in)
    no_shadow(ball("Lamp_Bulb", 0.022, (0, sy, sz - 0.02), glow("#FFE2A8", 6.0 if NIGHT else 0.6), scale=(2.4, 1, 1),
                   parent=root))
    cyl("Lamp_Chain", 0.0015, 0.09, (0.05, sy - 0.03, sz - 0.04), b, bevel=0, segs=6, parent=root)   # hangs from the socket
    ball("Lamp_ChainBall", 0.006, (0.05, sy - 0.03, sz - 0.088), b, parent=root)


def tufted(name, width, height, pitch, material, button_mat, loc, parent, rot=(0, 0, 0), puff=0.022):
    """Deep-buttoned (Chesterfield) leather: a sheet facing local -Y, centred on loc. Buttons sit on a diamond
    lattice; the leather puffs out between them and creases along the lines joining them, like hand tufting."""
    px, pz = pitch, pitch * 1.25
    nx, nz = max(8, int(width / 0.008)), max(8, int(height / 0.008))
    bm = bmesh.new()
    grid = []
    for j in range(nz + 1):
        z = -height / 2 + height * j / nz
        row = []
        for i in range(nx + 1):
            x = -width / 2 + width * i / nx
            a, b = x / px + z / pz, x / px - z / pz              # diamond-lattice coordinates
            q = (abs(math.sin(math.pi * a)) * abs(math.sin(math.pi * b))) ** 0.45
            edge = max(0.0, min(1.0, (width / 2 - abs(x)) / 0.035, (height / 2 - abs(z)) / 0.035))
            row.append(bm.verts.new((x, -puff * q * edge, z)))
        grid.append(row)
    for j in range(nz):
        for i in range(nx):
            bm.faces.new((grid[j][i], grid[j][i + 1], grid[j + 1][i + 1], grid[j + 1][i]))
    sheet = _finish(_obj(name, bm), material, 0, None, parent)
    sheet.location, sheet.rotation_euler = loc, rot
    pts = [((ia + ib) / 2 * px, (ia - ib) / 2 * pz) for ia in range(-30, 31) for ib in range(-30, 31)]
    buttons = [((x, -0.003, z), (0.011, 0.006, 0.011), (0, 0, 0)) for x, z in pts
               if abs(x) < width / 2 - 0.03 and abs(z) < height / 2 - 0.03]
    if buttons:
        b = pebbles(name + "_Buttons", buttons, button_mat, parent=parent, subdiv=2)
        b.location, b.rotation_euler = loc, rot
    return sheet


def nail_row(p0, p1, spacing=0.022):
    """Points for a row of brass nailhead studs from p0 to p1 (the trim along a Chesterfield's edges)."""
    n = max(1, int((Vector(p1) - Vector(p0)).length / spacing))
    return [tuple(Vector(p0).lerp(Vector(p1), k / n)) for k in range(n + 1)]


def build_armchair():
    """Chesterfield wing chair: deep diamond buttoning on the back and wings, scroll arms with brass nailhead trim,
    a separate piped seat cushion, turned feet on brass castors."""
    root, w, d, h = furniture_root("armchair")
    lth = leather("main", 1.0, 0.42)
    lth_dark = leather("main", 0.62, 0.45)
    lth_light = leather("main", 1.08, 0.4)
    legw = wood(0.8, 0.35)
    nails = []
    for sx in (-1, 1):
        lathe("Arm_FrontLeg", [(0.03, 0.02), (0.038, 0.04), (0.03, 0.07), (0.035, 0.09), (0.035, 0.1)],
              (sx * (w / 2 - 0.09), -d / 2 + 0.1, 0), legw, segs=16, parent=root)
        cyl("Arm_Castor", 0.018, 0.02, (sx * (w / 2 - 0.09), -d / 2 + 0.1, 0.012), brass(0.3), segs=12, parent=root)
        box("Arm_BackLeg", (0.04, 0.04, 0.1), (sx * (w / 2 - 0.08), d / 2 - 0.08, 0.05), legw, bevel=0.004,
            rot=(R(-8), 0, 0), parent=root)
    # Seat platform with nailhead trim along its lower edge, and a separate piped cushion
    bw, bd = w - 0.04, d - 0.08
    box("Arm_Base", (bw, bd, 0.28), (0, 0.0, 0.1 + 0.14), lth, bevel=0.03, parent=root)
    nails += nail_row((-bw / 2 + 0.05, -bd / 2 - 0.002, 0.13), (bw / 2 - 0.05, -bd / 2 - 0.002, 0.13))
    for sx in (-1, 1):
        nails += nail_row((sx * (bw / 2 + 0.002), -bd / 2 + 0.05, 0.13), (sx * (bw / 2 + 0.002), bd / 2 - 0.05, 0.13))
    cw, cd = w - 0.31, d - 0.25
    box("Arm_SeatCushion", (cw, cd, 0.11), (0, -0.07, 0.38 + 0.055), lth_light, bevel=0.03, parent=root)
    py0, py1, px_ = -0.07 - cd / 2 + 0.008, -0.07 + cd / 2 - 0.12, cw / 2 - 0.008   # round the cushion's top edge
    pipe = [(-px_, py1, 0.482), (-px_, py0 + 0.02, 0.482), (-px_ + 0.02, py0, 0.482), (px_ - 0.02, py0, 0.482),
            (px_, py0 + 0.02, 0.482), (px_, py1, 0.482)]
    tube("Arm_CushionPiping", pipe, 0.006, lth_dark, parent=root)
    cyl("Arm_Piping", 0.007, w - 0.08, (0, -bd / 2 + 0.004, 0.37), lth_dark, rot=(0, R(90), 0), segs=8, parent=root)
    # Back: slightly reclined, with a rolled top and deep buttoning
    back_t = 0.16
    back = anchor("Arm_BackFrame", (0, d / 2 - back_t / 2 - 0.02, 0.38), coll=COL_FURN, parent=root)
    back.rotation_euler = (R(-9), 0, 0)
    bh = h - 0.38 - 0.04
    box("Arm_Back", (w - 0.26, back_t, bh), (0, 0, bh / 2), lth, bevel=0.035, parent=back)
    cyl("Arm_BackRoll", 0.07, w - 0.24, (0, 0.0, bh - 0.02), lth, rot=(0, R(90), 0), segs=24, bevel=0.0, parent=back)
    tufted("Arm_BackTufting", w - 0.33, bh - 0.17, 0.11, lth, lth_dark, (0, -back_t / 2 + 0.001, 0.08 + (bh - 0.17) / 2),
           back)
    # Scroll arms and wings
    for sx in (-1, 1):
        ax = sx * (w / 2 - 0.085)
        fy = -d / 2 + 0.027                                         # front face of the scroll panel
        box("Arm_Side", (0.13, d - 0.14, 0.27), (ax, -0.03, 0.38 + 0.12), lth, bevel=0.03, parent=root)
        cyl("Arm_Scroll", 0.075, d - 0.16, (ax + sx * 0.02, -0.04, 0.64), lth, rot=(R(90), 0, 0), segs=28, bevel=0.0,
            parent=root)
        cyl("Arm_ScrollFace", 0.068, 0.012, (ax + sx * 0.02, -d / 2 + 0.035, 0.64), lth_light, rot=(R(90), 0, 0),
            segs=28, bevel=0.004, parent=root)
        box("Arm_ScrollPanel", (0.15, 0.012, 0.22), (ax + sx * 0.005, -d / 2 + 0.035, 0.49), lth_light, bevel=0.01,
            parent=root)
        ball("Arm_ScrollButton", 0.011, (ax + sx * 0.02, fy, 0.64), lth_dark, scale=(1, 0.5, 1), parent=root)
        for k in range(14):                                         # nailheads round the scroll and down the panel
            a = R(-60 + k * 300 / 13)
            nails.append((ax + sx * 0.02 + 0.058 * math.cos(a), fy - 0.002, 0.64 + 0.058 * math.sin(a)))
        for ex in (-1, 1):
            nails += nail_row((ax + sx * 0.005 + ex * 0.064, fy - 0.002, 0.39), (ax + sx * 0.005 + ex * 0.064, fy - 0.002,
                                                                                  0.59))
        wing = anchor("Arm_WingFrame", (ax + sx * 0.01, d / 2 - 0.2, 0.62), coll=COL_FURN, parent=root)
        wing.rotation_euler = (R(-8), R(sx * 6), R(-sx * 8))           # leans back and flares out like the real chair
        wh_ = h - 0.64                              # side silhouette of a Queen Anne wing, extruded 9 cm
        outline = [(0.12, 0.0), (0.12, wh_), (0.0, wh_ + 0.01), (-0.12, wh_ - 0.04), (-0.21, wh_ - 0.14),
                   (-0.25, wh_ - 0.28), (-0.24, 0.06), (-0.2, 0.0)]
        bm = bmesh.new()
        f = bm.faces.new([bm.verts.new((-0.045, y, z)) for y, z in outline])
        ext = bmesh.ops.extrude_face_region(bm, geom=[f])
        bmesh.ops.translate(bm, vec=(0.09, 0, 0), verts=[v for v in ext["geom"] if isinstance(v, bmesh.types.BMVert)])
        bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
        _finish(_obj("Arm_Wing", bm), lth, 0.035, COL_ROOM, wing, segs=4)
        tufted("Arm_WingTufting", 0.25, 0.25, 0.09, lth, lth_dark, (-sx * 0.044, -0.05, 0.18), wing,
               rot=(0, 0, R(-sx * 90)), puff=0.016)
        for k in range(5):                                       # pleats where the leather turns round the scroll
            a = R(-150 + k * 25)
            box("Arm_Pleat", (0.003, 0.003, 0.06), (ax + sx * 0.02 + 0.035 * math.cos(a), -d / 2 + 0.028,
                0.64 + 0.035 * math.sin(a)), lth_dark, bevel=0, rot=(0, -a + R(90), 0), parent=root)
    pebbles("Arm_Nailheads", [(p, (0.0055, 0.0055, 0.0055), (0, 0, 0)) for p in nails], brass(0.3), parent=root, subdiv=2)


def build_side_table():
    """Victorian tripod wine table: moulded round top, turned baluster column, three cabriole snake legs;
    a cup and saucer, teapot and a book."""
    root, w, d, h = furniture_root("side_table")
    mahog = wood(1.05, 0.32)
    r = w / 2
    lathe("Side_Top", [(r - 0.02, h - 0.022), (r, h - 0.018), (r, h - 0.006), (r - 0.006, h), (0.001, h)],
          (0, 0, 0), mahog, segs=48, parent=root)
    lathe("Side_TopUnder", [(0.001, h - 0.04), (0.09, h - 0.04), (0.09, h - 0.022), (0.001, h - 0.022)], (0, 0, 0), mahog,
          segs=24, parent=root)
    lathe("Side_Column", [(0.05, 0.1), (0.056, 0.13), (0.05, 0.17), (0.034, 0.2), (0.03, 0.215), (0.042, 0.24),
                          (0.055, 0.27), (0.061, 0.3), (0.059, 0.33), (0.05, 0.36), (0.038, 0.4), (0.029, 0.45),
                          (0.025, 0.5), (0.025, 0.56), (0.03, 0.575), (0.037, 0.59), (0.03, 0.605), (0.027, 0.62),
                          (0.033, 0.635), (0.035, h - 0.04)], (0, 0, 0),
          wood(1.05, 0.32, along="Z"), segs=32, parent=root)
    for k in range(3):                                          # cabriole "snake" legs ending in pad feet
        a = R(90 + k * 120)
        ca, sa = math.cos(a), math.sin(a)
        prof = [(0.04, 0.2), (0.11, 0.16), (0.17, 0.09), (0.21, 0.04), (0.235, 0.02)]
        tube("Side_Leg", [(ca * rr, sa * rr, z) for rr, z in prof], [0.022, 0.02, 0.016, 0.013, 0.015], mahog,
             parent=root, flat=0.75)
        ball("Side_Pad", 0.022, (ca * 0.24, sa * 0.24, 0.012), mahog, scale=(1.2, 1.2, 0.55), parent=root)
    china = surface(mat("cream", 0.2), "ceramic")
    cx, cy = 0.1, -0.08
    lathe("Side_Saucer", [(0.03, 0), (0.065, 0.008), (0.07, 0.014), (0.001, 0.006)], (cx, cy, h), china, segs=32,
          parent=root)
    lathe("Side_Cup", [(0.025, 0.006), (0.03, 0.01), (0.044, 0.05), (0.046, 0.062), (0.042, 0.062), (0.04, 0.05),
                       (0.024, 0.014), (0.001, 0.014)], (cx, cy, h), china, segs=32, parent=root)
    cyl("Side_Tea", 0.04, 0.003, (cx, cy, h + 0.054), mat("tan", 0.1, color=shade(COLORS["tan"], 0.6)), bevel=0,
        parent=root)
    ring("Side_CupHandle", 0.014, 0.004, (cx + 0.05, cy, h + 0.04), china, rot=(R(90), 0, 0), segs=16, parent=root)
    # A "Brown Betty" teapot (the classic British red-clay pot in a dark treacle glaze): squat round body,
    # a spout rising from low on the belly, a big loop handle and a knobbed lid.
    tx, ty = -0.11, -0.02
    pot = surface(mat("wood", 0.12, color=shade(COLORS["wood"], 0.85)), "ceramic")
    lathe("Side_Teapot", [(0.045, 0), (0.05, 0.004), (0.068, 0.018), (0.08, 0.042), (0.081, 0.06), (0.074, 0.083),
                          (0.058, 0.1), (0.044, 0.106), (0.044, 0.11), (0.001, 0.11)], (tx, ty, h), pot, segs=40, parent=root)
    lathe("Side_TeapotLid", [(0.047, 0), (0.046, 0.006), (0.034, 0.016), (0.01, 0.02), (0.008, 0.026), (0.014, 0.032),
                             (0.011, 0.04), (0.001, 0.042)], (tx, ty, h + 0.108), pot, segs=32, parent=root)
    tube("Side_Spout", [(tx + 0.055, ty, h + 0.03), (tx + 0.085, ty, h + 0.05), (tx + 0.105, ty, h + 0.08),
                        (tx + 0.122, ty, h + 0.105), (tx + 0.132, ty, h + 0.112)],
         [0.02, 0.014, 0.0105, 0.009, 0.0085], pot, segs=14, parent=root)
    tube("Side_PotHandle", [(tx - 0.07, ty, h + 0.09), (tx - 0.105, ty, h + 0.09), (tx - 0.125, ty, h + 0.065),
                            (tx - 0.112, ty, h + 0.035), (tx - 0.075, ty, h + 0.022)], 0.008, pot, segs=12, parent=root,
         flat=0.6)
    lying_book("Side_Book", (0.21, 0.14, 0.03), (0.04, 0.14, h + 0.001), "navy", 18, parent=root)


def build_floor_lamp():
    """Brass standard lamp: stepped round base, turned column with collars, pleated faux-silk shade with trim."""
    root, w, d, h = furniture_root("floor_lamp")
    b = brass(0.25)
    lathe("FloorLamp_Base", [(0.15, 0), (0.15, 0.02), (0.13, 0.03), (0.13, 0.04), (0.08, 0.06), (0.04, 0.1),
                             (0.03, 0.14), (0.001, 0.14)], (0, 0, 0), b, segs=40, parent=root)
    lathe("FloorLamp_Column", [(0.018, 0.14), (0.026, 0.18), (0.016, 0.22), (0.014, 0.6), (0.024, 0.62), (0.014, 0.64),
                               (0.012, 1.15), (0.02, 1.17), (0.012, 1.19), (0.012, h - 0.25), (0.02, h - 0.24)],
          (0, 0, 0), b, segs=20, parent=root)
    silk = mat("cream", 0.7, emit=0.8 if NIGHT else 0.05, color=shade(COLORS["cream"], 0.9))
    shade_ = lathe("FloorLamp_Shade", [(0.21, h - 0.31), (0.13, h - 0.03)], (0, 0, 0), silk, segs=96, wave=(32, 0.06),
                   parent=root)
    no_shadow(shade_)
    for z, r in ((h - 0.31, 0.215), (h - 0.03, 0.134)):
        ring("FloorLamp_Trim", r, 0.006, (0, 0, z), surface(mat("accent_2", 0.8, color=shade(COLORS["accent_2"], 0.9)),
             "fabric"), segs=48, parent=root)
    lathe("FloorLamp_Finial", [(0.01, 0), (0.016, 0.015), (0.004, 0.035)], (0, 0, h - 0.03), b, segs=12, parent=root)
    lamp = light("Light_FloorLamp", "POINT", LAMP_STRENGTH * (1.5 if NIGHT else 0.2), kelvin(LAMP_WARMTH),
                 (0, 0, h - 0.17), size=0.1)
    lamp.parent = root                                 # the light stays when the lamp is replaced


# Simplified coastlines (longitude, latitude in degrees) for the terrestrial globe's map.
CONTINENTS = [
    [(-168, 66), (-162, 70), (-156, 71), (-140, 70), (-128, 70), (-115, 68), (-95, 72), (-82, 70), (-88, 64), (-94, 59),
     (-92, 57), (-82, 55), (-80, 51), (-78, 58), (-73, 62), (-64, 60), (-61, 56), (-56, 52), (-60, 47), (-66, 45),
     (-70, 43), (-75, 39), (-76, 35), (-81, 31), (-80, 26), (-81, 25), (-83, 29), (-89, 30), (-94, 29), (-97, 26),
     (-97, 22), (-94, 18), (-90, 21), (-87, 21), (-88, 16), (-84, 15), (-83, 10), (-79, 9), (-77, 8), (-80, 7),
     (-84, 9), (-86, 12), (-92, 14), (-96, 16), (-105, 20), (-110, 23), (-115, 30), (-117, 33), (-121, 35), (-124, 40),
     (-124, 46), (-125, 49), (-130, 54), (-136, 58), (-142, 60), (-150, 61), (-154, 58), (-164, 55), (-158, 59),
     (-166, 62), (-165, 64)],                                                                    # North America
    [(-80, 9), (-77, 8), (-72, 12), (-64, 10), (-60, 8), (-52, 5), (-50, 0), (-44, -2), (-35, -6), (-35, -9), (-39, -14),
     (-39, -18), (-41, -22), (-48, -26), (-49, -29), (-52, -32), (-58, -35), (-57, -38), (-62, -39), (-65, -41),
     (-64, -45), (-67, -46), (-69, -51), (-68, -54), (-72, -54), (-75, -50), (-74, -44), (-73, -37), (-71, -30),
     (-70, -18), (-76, -14), (-80, -6), (-81, -3), (-80, 0), (-78, 3), (-77, 7)],             # South America
    [(-17, 15), (-17, 21), (-13, 27), (-10, 30), (-6, 35), (0, 35), (10, 37), (11, 33), (20, 32), (25, 32), (32, 31),
     (34, 28), (38, 22), (43, 13), (51, 12), (51, 10), (48, 5), (42, -1), (40, -5), (40, -11), (41, -15), (35, -20),
     (35, -24), (33, -27), (30, -31), (26, -34), (20, -35), (18, -32), (15, -27), (12, -18), (12, -13), (14, -9),
     (12, -5), (9, -1), (9, 4), (5, 6), (0, 6), (-5, 5), (-8, 4), (-12, 7), (-15, 11)],        # Africa
    [(-9, 37), (-9, 43), (-2, 43.5), (-1, 46), (-4.5, 48), (-1, 49.5), (2, 51), (4, 52), (8, 54), (8.5, 57), (10.5, 57.5),
     (12, 56), (11, 59), (6, 58), (5, 62), (10, 64), (14, 68), (19, 70), (26, 71), (31, 70), (41, 67), (34, 66),
     (36, 64), (44, 66), (53, 68), (60, 69), (68, 69), (73, 72), (80, 73), (88, 75), (100, 77), (114, 74), (128, 72),
     (140, 72), (150, 71), (160, 70), (170, 70), (180, 69), (180, 65), (170, 60), (163, 59), (163, 56), (156, 51),
     (156, 57), (160, 61), (150, 59), (143, 59), (137, 54), (141, 52), (140, 47), (135, 43), (130, 42), (129, 36),
     (126, 35), (126, 38), (121, 40), (118, 38), (122, 37), (120, 34), (122, 30), (119, 25), (115, 22), (108, 21),
     (106, 18), (109, 13), (105, 9), (101, 13), (100, 8), (103, 4), (104, 1.5), (100, 6), (98, 9), (98, 16), (94, 19),
     (92, 22), (87, 21), (80, 16), (80, 10), (77, 8), (73, 16), (73, 21), (67, 24), (57, 25), (56, 27), (52, 27),
     (48, 30), (50, 26), (56, 24), (59, 23), (55, 17), (44, 12), (42, 15), (39, 21), (35, 28), (35, 33), (36, 36),
     (30, 36), (27, 37), (26, 40), (23, 40), (21, 38), (20, 40), (19, 42), (14, 45), (12, 44), (16, 41), (18, 40),
     (16, 38), (12, 42), (10, 44), (7, 43.5), (3, 43), (3, 42), (0, 39), (-1, 37), (-5, 36)],  # Europe and Asia
    [(114, -22), (114, -26), (115, -34), (118, -35), (124, -34), (131, -31.5), (135, -35), (138, -35), (140, -38),
     (146, -39), (150, -37), (153, -32), (153, -25), (146, -19), (142, -11), (141, -17), (136, -15), (136, -12),
     (131, -11), (127, -14), (122, -17)],                                                       # Australia
    [(-73, 78), (-60, 82), (-30, 83), (-20, 80), (-18, 76), (-22, 70), (-32, 68), (-40, 65), (-43, 60), (-48, 61),
     (-52, 65), (-54, 68), (-56, 72), (-66, 76)],                                              # Greenland
    [(-180, -90), (180, -90), (180, -72), (150, -68), (100, -66), (60, -67), (20, -69), (-10, -71), (-40, -77),
     (-58, -64), (-65, -68), (-75, -73), (-100, -74), (-140, -76), (-180, -78)],               # Antarctica
    [(-5, 50), (1, 51), (2, 53), (-1, 55), (-2, 57), (-4, 59), (-6, 58), (-5, 56), (-3, 54), (-4, 52)],   # Britain
    [(-10, 52), (-6, 52), (-6, 55), (-8, 55), (-10, 54)],                                       # Ireland
    [(-24, 64), (-14, 65), (-15, 66.5), (-22, 66.5)],                                           # Iceland
    [(-80, 73), (-62, 67), (-66, 62), (-78, 64), (-90, 72)],                                    # Baffin Island
    [(130, 31), (132, 34), (136, 34), (140, 36), (142, 40), (141, 44), (145, 44), (142, 46), (140, 42), (140, 38),
     (136, 37), (132, 35)],                                                                     # Japan
    [(95, 5), (106, -6), (104, -6), (97, 0)], [(109, 1), (117, 7), (119, 1), (116, -4), (110, -3)],
    [(105, -6), (115, -8), (106, -7.5)], [(131, -1), (141, -3), (150, -10), (141, -9), (138, -8)],   # Indonesia, N. Guinea
    [(44, -25), (47, -25), (50, -15), (49, -12), (44, -17)],                                    # Madagascar
    [(172, -35), (178, -38), (175, -41), (171, -45), (167, -46), (172, -41)],                   # New Zealand
    [(-85, 22), (-80, 23), (-74, 20), (-78, 20)],                                               # Cuba
]


def globe_map():
    """Antique terrestrial globe map (equirectangular): aged varnished oceans, outline-coloured countries,
    a brown coastline, coastal shading, 15-degree graticule, equator and ecliptic."""
    wpx, hpx = 512, 256
    land = [[-1] * wpx for _ in range(hpx)]
    for idx, poly in enumerate(CONTINENTS):                     # scan-line fill of every coastline polygon
        for j in range(hpx):
            lat = -90 + (j + 0.5) * 180 / hpx
            xs = sorted(x1 + (lat - y1) * (x2 - x1) / (y2 - y1) for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1])
                        if (y1 <= lat < y2) or (y2 <= lat < y1))
            for a, b in zip(xs[0::2], xs[1::2]):
                for i in range(max(0, int((a + 180) / 360 * wpx)), min(wpx, int((b + 180) / 360 * wpx) + 1)):
                    land[j][i] = idx
    near = [[land[j][i] >= 0 for i in range(wpx)] for j in range(hpx)]
    for _ in range(3):                                          # water within ~2 degrees of a coast
        near = [[near[j][i] or near[j][(i + 1) % wpx] or near[j][i - 1] or near[max(0, j - 1)][i] or
                 near[min(hpx - 1, j + 1)][i] for i in range(wpx)] for j in range(hpx)]
    C = lambda key, f=1.0: srgb(shade(COLORS[key], f))
    ivory = C("cream", 1.0)
    sea = blend(ivory, C("tan", 1.25), 0.5)
    washes = [blend(C("main", 1.9), ivory, 0.55), blend(C("plant", 1.1), ivory, 0.45), blend(C("accent_2", 1.0), ivory, 0.4),
              blend(C("accent_3", 0.9), ivory, 0.35), blend(C("tan", 1.2), ivory, 0.3)]
    coast, line, red = C("wood", 0.9), C("tan", 0.6), C("main", 1.3)
    age = value_noise(SEED + 41, 12, 6)

    def paint(u, v):
        i, j = min(wpx - 1, int(u * wpx)), min(hpx - 1, int(v * hpx))
        lon, lat = u * 360 - 180, v * 180 - 90
        k = land[j][i]
        if k >= 0:
            edge = any(land[jj][ii] != k for ii, jj in ((i - 1, j), ((i + 1) % wpx, j), (i, max(0, j - 1)),
                                                        (i, min(hpx - 1, j + 1))))
            col = coast if edge else washes[k % len(washes)]
        else:
            col = blend(sea, coast, 0.22) if near[j][i] else sea
        if abs(lat) < 0.5 or abs(lat - 23.44 * math.sin(math.radians(lon))) < 0.45:
            col = red                                           # equator and ecliptic
        elif min(abs(lon / 15 - round(lon / 15)) * 15, abs(lat / 15 - round(lat / 15)) * 15) < 0.35:
            col = blend(col, line, 0.5)                         # graticule
        f = 0.84 + 0.2 * age(u, v)                              # patchy amber varnish
        return tuple(c * f * t for c, t in zip(col, (1.0, 0.95, 0.8)))
    return baked_image("Globe_Map", wpx, hpx, paint)


def globe_ball(r, material, parent):
    """UV sphere whose UVs are longitude/latitude, so the equirectangular map wraps correctly."""
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=64, v_segments=32, radius=r)
    uvl = bm.loops.layers.uv.new("UVMap")
    for f in bm.faces:
        uvs = [[0.5 + math.atan2(lp.vert.co.y, lp.vert.co.x) / (2 * math.pi),
                0.5 + math.asin(max(-1.0, min(1.0, lp.vert.co.z / r))) / math.pi] for lp in f.loops]
        if max(c[0] for c in uvs) - min(c[0] for c in uvs) > 0.5:         # face across the date line
            for c in uvs:
                c[0] += 1.0 if c[0] < 0.5 else 0.0
        poles = [abs(lp.vert.co.z) > r * 0.999 for lp in f.loops]
        if any(poles):                                                   # pole vertex: middle of its neighbours
            others = [c[0] for c, p in zip(uvs, poles) if not p]
            for c, p in zip(uvs, poles):
                if p:
                    c[0] = sum(others) / len(others)
        for lp, c in zip(f.loops, uvs):
            lp[uvl].uv = c
    return _finish(_obj("Globe_Ball", bm), material, 0, None, parent)


def build_hero_prop():
    """Your signature object: an 18in library globe on a turned tripod stand (linkedin link)."""
    root, w, d, h = furniture_root("hero_prop")
    hook_link(root, "linkedin")
    mahog_z, mahog = wood(1.0, 0.36, along="Z"), wood(1.0, 0.36)
    ring_z, gr = 0.72, 0.23
    for k in range(3):                                          # turned legs up to the horizon ring
        a = R(90 + k * 120)
        cx, cy = math.cos(a) * 0.27, math.sin(a) * 0.27
        lathe("Globe_Leg", [(0.022, 0.03), (0.03, 0.05), (0.02, 0.12), (0.016, 0.3), (0.028, 0.34), (0.018, 0.4),
                            (0.022, 0.55), (0.03, 0.62), (0.024, ring_z - 0.01)], (cx, cy, 0), mahog_z, segs=16,
              parent=root)
        ball("Globe_BunFoot", 0.03, (cx, cy, 0.024), mahog, scale=(1, 1, 0.8), parent=root)
        box("Globe_Stretcher", (0.25, 0.028, 0.03), (cx / 2, cy / 2, 0.2), mahog, bevel=0.005, rot=(0, 0, a), parent=root)
    lathe("Globe_Hub", [(0.05, 0.18), (0.055, 0.2), (0.05, 0.222), (0.001, 0.222)], (0, 0, 0), mahog, segs=24, parent=root)
    cyl("Globe_Compass", 0.038, 0.004, (0, 0, 0.224), surface(mat("cream", 0.3), "paper"), segs=24, parent=root)
    box("Globe_Needle", (0.06, 0.004, 0.002), (0, 0, 0.227), mat("main", 0.4), bevel=0, rot=(0, 0, R(30)), parent=root)
    lathe("Globe_Horizon", [(gr + 0.02, ring_z - 0.022), (gr + 0.085, ring_z - 0.022), (gr + 0.085, ring_z),
                            (gr + 0.02, ring_z)], (0, 0, 0), mahog, segs=64, closed=True, parent=root)
    lathe("Globe_HorizonPaper", [(gr + 0.025, ring_z + 0.001), (gr + 0.075, ring_z + 0.001), (gr + 0.075, ring_z + 0.003),
                                 (gr + 0.025, ring_z + 0.003)], (0, 0, 0), surface(mat("cream", 0.6), "paper"), segs=64,
          closed=True, parent=root)
    ticks = [((0.002, 0.012, 0.001), ((gr + 0.05) * math.cos(R(t)), (gr + 0.05) * math.sin(R(t)), ring_z + 0.0035),
              (0, 0, R(t))) for t in range(0, 360, 10)]
    boxes("Globe_Ticks", ticks, mat("dark", 0.6), bevel=0, parent=root)
    pivot = anchor("Globe_Pivot", (0, 0, ring_z), coll=COL_FURN, parent=root)
    pivot.rotation_euler = (0, R(23), 0)
    ring("Globe_Meridian", gr + 0.012, 0.008, (0, 0, 0), brass(0.3), rot=(R(90), 0, 0), segs=64, parent=pivot).scale = (1, 1, 2.2)
    globe_ball(gr, picture_material("globe_paper", globe_map(), 0.35, "paper"), pivot).rotation_euler = (0, 0, R(-85))
    for sz in (-1, 1):
        lathe("Globe_Pin", [(0.008, 0), (0.008, 0.02), (0.004, 0.03)], (0, 0, sz * (gr + 0.006)), brass(),
              rot=(0 if sz > 0 else R(180), 0, 0), segs=10, parent=pivot)
    cyl("Globe_MeridianFoot", 0.012, ring_z - 0.24 - 0.222, (0, 0, 0.222 + (ring_z - 0.24 - 0.222) / 2), brass(),
        segs=12, parent=root)


def heriz_design(w, d):
    """The carpet's design, drawn in metres on a 1 cm 'knot block' grid so every outline is stepped like a real
    hand-knotted Heriz: guard stripes, a navy main border of rosettes on an angular vine, a brick-red field with an
    angular trellis, ivory corner spandrels and a big serrated medallion with end pendants. Returns paint(u, v)."""
    C = lambda key, f=1.0: srgb(shade(COLORS[key], f))
    red, navy, ivory = blend(C("main", 1.35), C("tan", 1.0), 0.22), C("navy", 0.95), C("cream", 0.9)   # rust-brick red
    gold, blue, ink = C("accent_2", 0.9), C("accent_3", 0.8), C("dark", 1.1)
    abrash = value_noise(SEED + 5, 16, 2)          # dye-lot bands across the rug, as in real hand-spun wool
    knot = random.Random(SEED + 6)
    q = 0.01                                       # 1 cm knot blocks (a coarse village Heriz)
    fx, fy = w / 2 - 0.26, d / 2 - 0.26           # half size of the field
    step = lambda a: math.floor(a / q) * q

    def design(x, y):
        ax, ay = abs(x), abs(y)
        e, s = (d / 2 - ay, x) if d / 2 - ay < w / 2 - ax else (w / 2 - ax, y)   # distance from edge, run along it
        if e < 0.025:
            return navy
        if e < 0.05:
            return red if (s / 0.04) % 1 < 0.5 else ivory                    # reciprocal guard stripe
        if e < 0.06 or 0.205 < e < 0.215 or 0.245 < e < 0.26:
            return ink
        if e < 0.205:                                                       # main border
            t = e - 0.1325
            m = step(abs(s - round(s / 0.26) * 0.26)) + step(abs(t))
            if m < 0.08:
                return gold if m < 0.025 else ivory if m < 0.05 else red if m < 0.07 else ink
            zig = abs((s / 0.13) % 2 - 1) - 0.5
            return blue if abs(t - zig * 0.09) < 0.01 else navy
        if e < 0.245:
            return red if (s / 0.05) % 1 < 0.3 else gold                     # inner guard
        sx, sy = step(ax), step(ay)
        r = sx / 0.8 + sy / 0.5                                              # big medallion with a hooked edge
        if r < 1.0 + (0.045 if ((sx + sy) / 0.05) % 2 < 1 else 0.0):
            if r > 0.93:
                return ink
            if r > 0.87:
                return ivory
            if r > 0.5:
                return red if (min(sx, sy) < 0.03 and r < 0.8) else gold if abs(r - 0.68) < 0.02 else blend(navy, blue, 0.25)
            if r > 0.45:
                return ink
            r2 = sx / 0.18 + sy / 0.13
            return gold if r2 < 0.5 else navy if r2 < 1 else ivory
        pr = abs(sx - 0.95) / 0.12 + sy / 0.09                               # end pendants on a stem
        if pr < 1:
            return ivory if pr < 0.5 else navy
        if sx < 0.86 and sy < 0.015:
            return navy
        cx, cy = step(fx - ax), step(fy - ay)                                # ivory corner spandrels
        sr = cx / 0.55 + cy / 0.38
        if sr < 1:
            if sr > 0.9:
                return navy
            mot = abs((cx / 0.16) % 1 - 0.5) + abs((cy / 0.16) % 1 - 0.5)
            return red if mot < 0.16 else navy if mot < 0.21 else ivory
        p, m_ = (sx + sy) / 0.42, (sx - sy) / 0.42                           # open brick field: big stepped
        dp, dm = abs(p - round(p)), abs(m_ - round(m_))                      # palmettes, angular leaves and
        dd = dp + dm                                                         # a faint tone-on-tone vine
        if dd < 0.23:
            return gold if dd < 0.07 else navy if dd < 0.15 else ivory if dd < 0.2 else navy
        leaf = min(abs(dp - 0.5) + 2 * dm, abs(dm - 0.5) + 2 * dp)
        if leaf < 0.16:
            return blue if leaf < 0.1 else navy
        if dp < 0.025 or dm < 0.025:
            return blend(red, ink, 0.45)
        return red

    def paint(u, v):
        f = (0.93 + 0.12 * abrash(u, v)) * knot.uniform(0.95, 1.04)
        return tuple(c * f for c in design((u - 0.5) * w, (v - 0.5) * d))
    return paint


def build_rug():
    """Heriz carpet (2.7 x 1.9 m): the knotted design is baked into the wool, fringe on the short ends only."""
    root, w, d, h = furniture_root("rug")
    img = baked_image("Rug_Heriz", int(w / 0.005), int(d / 0.005), heriz_design(w, d))
    box("Rug_Pile", (w, d, h), (0, 0, h / 2), picture_material("rug_wool", img, 1.0, "fabric", coords="Generated"),
        bevel=0, parent=root)
    fringe = [((0.05, 0.008, 0.003), (sx * (w / 2 + 0.025), -d / 2 + 0.03 + k * 0.025, 0.0015), (0, 0, 0))
              for sx in (-1, 1) for k in range(int((d - 0.06) / 0.025) + 1)]
    boxes("Rug_Fringe", fringe, surface(mat("cream", 1.0), "fabric"), bevel=0, parent=root)


def build_wall_art():
    """Two gilt-framed oil paintings (picture hooks), each lit by a brass picture light."""
    root, w, d, h = furniture_root("wall_art")
    for i, (fx, style) in enumerate(((-0.34, "portrait"), (0.32, "landscape"))):
        pw, ph = (0.42, 0.52) if style == "portrait" else (0.5, 0.4)
        painting(root, fx, h / 2 - 0.02, pw, ph, d / 2, "frame", i + 1, style)
        picture_light(root, fx, h / 2 - 0.02 + ph / 2 + 0.075, 0.36, d / 2)


PLACEHOLDERS = {
    "shelf": build_shelf, "desk": build_desk, "chair": build_chair, "lamp": build_lamp, "armchair": build_armchair,
    "side_table": build_side_table, "floor_lamp": build_floor_lamp, "hero_prop": build_hero_prop, "rug": build_rug,
    "wall_art": build_wall_art,
}
if SHOW_PLACEHOLDER_FURNITURE:
    for slot_name, build in PLACEHOLDERS.items():
        build()

# Matching Chesterfield footstool in front of the wing chair (deep-buttoned top, turned bun feet).
stool = anchor("Footstool", (3.95, 1.45, FLOOR_Z), turn=32, coll=COL_FURN)
box("Footstool_Body", (0.56, 0.4, 0.2), (0, 0, 0.17), leather("main", 1.0, 0.42), bevel=0.03, parent=stool)
box("Footstool_Top", (0.54, 0.38, 0.07), (0, 0, 0.29), leather("main", 1.08, 0.4), bevel=0.03, parent=stool)
tufted("Footstool_Tufting", 0.47, 0.31, 0.11, leather("main", 1.08, 0.4), leather("main", 0.62, 0.45), (0, 0, 0.324),
       stool, rot=(R(-90), 0, 0), puff=0.018)
studs = nail_row((-0.24, -0.202, 0.09), (0.24, -0.202, 0.09)) + nail_row((0.282, -0.16, 0.09), (0.282, 0.16, 0.09)) + \
    nail_row((-0.282, -0.16, 0.09), (-0.282, 0.16, 0.09))
pebbles("Footstool_Nailheads", [(p, (0.0055,) * 3, (0, 0, 0)) for p in studs], brass(0.3), parent=stool, subdiv=2)
for sx in (-1, 1):
    for sy in (-1, 1):
        lathe("Footstool_Foot", [(0.025, 0), (0.033, 0.02), (0.026, 0.045), (0.03, 0.07)], (sx * 0.22, sy * 0.14, 0),
              wood(0.8, 0.35), segs=14, parent=stool)

# A stack of folios on the floor by the reading chair (decoration, outside the slots).
zz = FLOOR_Z
for j, (bw_, bt_) in enumerate(((0.3, 0.05), (0.27, 0.04), (0.28, 0.045), (0.24, 0.035))):
    lying_book("Floor_BookStack", (bw_, 0.21 - j * 0.012, bt_), (4.05, 0.5, zz), random.choice(BOOK_KEYS[:4]),
               random.uniform(-14, 14) + (180 if j % 2 else 0))
    zz += bt_

# Victorian copper coal bucket beside the hearth (tapered body, rolled rim, brass ears and a bail handle), full of coal.
SCX, SCY = FX + FW / 2 + 0.17, D - 0.68
copper = surface(mat("copper", 0.3, metal=0.9, color="#A9653F"), "brushed")
lathe("Scuttle_Body", [(0.12, 0), (0.125, 0.014), (0.115, 0.024), (0.135, 0.24), (0.148, 0.325), (0.156, 0.33),
                       (0.15, 0.336), (0.141, 0.315)], (SCX, SCY, FLOOR_Z), copper, segs=40)     # 0.32 dia x 0.34 H
ring("Scuttle_Rim", 0.152, 0.007, (SCX, SCY, FLOOR_Z + 0.331), brass(0.3), segs=40)
heap = []
for _ in range(48):                                        # heaped higher in the middle
    a, rr = random.uniform(0, 6.3), 0.12 * math.sqrt(random.random())
    heap.append(((SCX + rr * math.cos(a), SCY + rr * math.sin(a), FLOOR_Z + 0.315 + 0.04 * (1 - rr / 0.12) +
                  random.uniform(0, 0.012)), (random.uniform(0.018, 0.03),) * 3, (random.uniform(0, 3),) * 3))
pebbles("Scuttle_Coal", heap, coal, smooth=False)
for sx in (-1, 1):
    ball("Scuttle_Ear", 0.015, (SCX + sx * 0.148, SCY, FLOOR_Z + 0.3), brass(0.3), scale=(0.5, 1, 1))
ring("Scuttle_Bail", 0.152, 0.005, (SCX, SCY, FLOOR_Z + 0.3), brass(0.3), rot=(R(55), 0, 0), arc=0.5, segs=24)


# =====================================================================
#  LIGHTS, WORLD, CAMERA, RENDER
# =====================================================================
# Lights depend on the theme: "rainy_evening" uses the SETTINGS values (cool rain light, warm lamps, lit fire);
# "sunny_reading" swaps in a warm daylight sun, a brighter fill and dims the lamps and the fire.
if NIGHT:
    sun_k, sun_e, fill_e, fill_k, lamp_e, fire_e, amb = SUN_WARMTH, SUN_STRENGTH, 145, 7500, LAMP_STRENGTH, FIRE_STRENGTH, 0.22
else:
    sun_k, sun_e, fill_e, fill_k, lamp_e, fire_e, amb = 5000, 4.0, 260, 5600, LAMP_STRENGTH * 0.25, FIRE_STRENGTH * 0.1, 0.4
light("Light_Sun", "SUN", sun_e, kelvin(sun_k), (-3, wy, 4), aim=(1.4, wy - 0.4, 0), size=R(4 if NIGHT else 2))
light("Light_Window", "AREA", 60 if NIGHT else 120, kelvin(sun_k), (-0.2, wy, wz), aim=(2, wy, 0.8), size=1.2)
light("Light_Fill", "AREA", fill_e * (W * D / 16), kelvin(fill_k), (W + 3, -3, H + 2.5), aim=(W / 2, D / 2, 0.6), size=6)
lamp_slot = SLOTS["lamp"]
light("Light_Lamp", "POINT", lamp_e, kelvin(LAMP_WARMTH), lamp_slot.location + Vector((0.1, 0, 0.0)), size=0.06)
light("Light_Fire", "POINT", fire_e, kelvin(1800), (FX, D - 0.35, FLOOR_Z + 0.35), size=0.25)
light("Light_Bounce", "AREA", 50 if NIGHT else 60, kelvin(LAMP_WARMTH if NIGHT else 4500), (W / 2, D / 2, H - 0.1),
      aim=(W / 2, D / 2, 0), size=2.5)
pic_e = 12 if NIGHT else 2                       # brass picture lights washing the oil paintings
light("Light_Picture_Mantel", "AREA", pic_e, kelvin(2700), (FX, D - 0.17, PZ + 0.36), aim=(FX, D, PZ - 0.2), size=0.4)
wa = SLOTS["wall_art"].location
for i, dy in enumerate((-0.325, 0.325)):
    light(f"Light_Picture_{i}", "AREA", pic_e * 0.7, kelvin(2700), (0.17, wa.y + dy, wa.z + 0.36), aim=(0, wa.y + dy, wa.z - 0.2),
          size=0.3)

# World: the camera sees the flat background colour; the room gets a soft ambient light.
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
bg_amb.inputs["Color"].default_value = (*kelvin(8000 if NIGHT else 5500), 1)
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
                    ("shadow_ray_count", 2), ("use_gtao", True), ("use_soft_shadows", True), ("use_bloom", True)):
    if hasattr(ee, attr):
        setattr(ee, attr, value)
if hasattr(ee, "ray_tracing_options"):
    ee.ray_tracing_options.resolution_scale = "2" if "2" in [i.identifier for i in
        type(ee.ray_tracing_options).bl_rna.properties["resolution_scale"].enum_items] else ee.ray_tracing_options.resolution_scale
scene.view_settings.view_transform = "Standard"   # keeps your hex colours exactly as typed
scene.view_settings.exposure = 0.0 if NIGHT else -0.15

# Remember the style so add_furniture.py can match colours later.
scene["kit_style"] = STYLE
scene["kit_version"] = KIT_VERSION
scene["kit_palette"] = json.dumps(COLORS)
scene["kit_material_finish"] = json.dumps({"roughness": 0.45, "bevel": 0.005, "saturation": 0.6})
scene["kit_theme"] = THEME
scene["kit_bounds"] = [-T, 0.0, -0.2, W, D + T, H + 0.12]   # used to re-frame the camera for social sizes
scene["kit_furniture_colors"] = json.dumps(["main", "accent_1", "accent_2", "cream", "wood", "wall_trim", "plant",
                                            "dark", "navy", "tan"])   # colours add_furniture.py may use


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
