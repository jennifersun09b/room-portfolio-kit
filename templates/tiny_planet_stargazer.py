"""
3D ROOM PORTFOLIO KIT  -  Template: TINY PLANET STARGAZER (themed room, kit v4)
================================================================================
Builds a little round planet floating in a dusk sky: a gently domed lawn on a rocky, cratered ball, with a
limewashed stone cottage-observatory (verdigris dome, arched plank door), a slatted stargazing deck with a
brass refractor on a teak tripod and a canvas deck chair, a brass display orrery on a reeded plaster
pedestal, a knee-high amethyst geode lamp glowing from inside and a rock-crystal cluster, a double-arm garden
lamp post with a lantern and a hanging flower basket, a steamer trunk with a star globe, mini-moons, a paper
plane and shooting stars.
It renders a 1920x1080 image.
Your name and role are on the observatory's sign board, your tagline on a name board on the rock; your projects
hang on its side wall (a star chart and two framed pictures). The paper plane is your email, the three little moons
are your other links.

HOW TO RUN
  Option A (no Blender UI):   blender -b -P tiny_planet_stargazer.py
  Option B (inside Blender):  Scripting tab > Open > tiny_planet_stargazer.py > Run Script (then F12 to render)

You only need to edit the SETTINGS block below. Everything under it builds the room.
Output: output/tiny_planet_stargazer.png and output/tiny_planet_stargazer.blend next to this script.
"""
# REFERENCES  (what each piece is modelled on; brand names appear only here and in research/tiny_planet_stargazer.md)
#   observatory (decor)    garden observatory = small stone cottage + 2.1 m (7 ft) dome (SkyShed POD class), scaled
#                          to a 1.4 x 1.3 m hut, 2.45 m walls, 1.2 m dome; arched ledged plank door 0.74 x 1.92 m
#                          https://astronomyplus.com/products/skyshed-pod-dome-backyard-observatory-pod
#   telescope              brass harbour-master refractor on a teak tripod (Stanley London 50 mm type):
#                          tube 111 cm with draw tubes, height 96-155 cm, 50 mm objective
#                          https://redcarpettelescopes.com/products/stanley-london-50mm-engravable-harbormaster-polished-brass-telescope-w-teak-tripod
#   chair                  traditional folding wooden deck chair, striped canvas sling: W60 D98 H105 cm, seat 43 cm,
#                          with a chunky knitted throw (about 45 cm wide where it lies on the sling)
#                          https://www.thestripescompany.com/shop/Premium-Deck-Chairs
#   side_table             Carl Hansen BM5868 folding teak side table: 45 x 45 x 45 cm, slatted top, X legs
#                          https://www.skandium.com/products/bm5868-outdoor-side-table
#   planisphere            card star wheel in a square jacket with an oval window (about 27 x 27 cm, here 18 cm)
#                          https://en.wikipedia.org/wiki/Planisphere
#   red torch              astronomy red-light torch (about 13 cm long, 3 cm across)
#   hero_prop              brass display orrery (desk models are about 25 cm across; here 35 cm: walnut foot,
#                          horizon ring with month marks, gilt sun, four planets on stepped arms, one ringed, one
#                          with a moon) on a turned walnut plinth (dia 30 cm), on a reeded plaster column
#                          pedestal (H 77 cm, top 25-30 cm)
#                          https://en.wikipedia.org/wiki/Orrery
#                          https://www.londonfine.co.uk/products/vintage-doric-column-architectural-plaster-classical-multiple-available
#   lamp                   Brazilian amethyst "cathedral" geode lamp with LEDs inside, on a blackened steel plinth
#                          (designer pieces 45 x 27 x 17 cm to 72 cm tall): here 30 x 24 cm, 46 cm tall + 5 cm plinth
#                          https://www.1stdibs.com/furniture/lighting/table-lamps/pair-of-amethyst-lamps-demian-quincke/id-f_38827712
#   crystal cluster        clear rock-crystal quartz cluster on its matrix (Brazil, 23-39 cm tall): here 32 cm wide
#                          https://www.1stdibs.com/furniture/decorative-objects/sculptures/natural-specimens/genuine-huge-clear-quartz-crystal-cluster-point-from-brazil-84-lbs/id-f_39235912
#   floor_lamp             2.2 m double-head Victorian cast-iron garden lamp post: arms 82 cm wide, lantern
#                          bracket 1.6 m, post top 1.86 m, 16 cm square base
#                          https://www.englishlampposts.co.uk/small-double-head-victorian-lamp-post.html
#   hanging basket         14 in (35 cm) wire hanging basket with a coco-fibre liner and three chains, planted
#                          with trailing petunias, hung from the lamp post arm (a classic English street-lamp detail)
#   trunk                  flat-top steamer trunk, canvas over wood with oak slats, brass corners, leather
#                          handles: 86 x 51 x 41 cm (34 x 20 x 16 in)
#                          https://www.chairish.com/product/35327189/early-20thc-flat-top-steamer-trunk
#   star globe             12-inch constellation desk globe on a walnut base (scaled to 8 in): H 51 cm at 12 in
#                          https://shop.franklloydwright.org/ja/products/glencoe-constellation-desk-globe-12-85601
#   planter                terracotta trough planter 60 x 22 x 18 cm with lavender
#   rug                    round braided jute / cotton rug, dia 116 cm
#   watering can           Haws 1 litre metal indoor can: L36 H16 cm
#                          https://www.harrodhorticultural.com/haws-copper-indoor-and-seedling-watering-can-pid8329.html
#   deck                   garden decking: 120 x 25 mm boards with 4 mm gaps on joists, curved fascia, skirting
#   tagline board          painted ship's quarterboard (name board) on iron brackets: real boards 1.2-2.5 m long,
#                          15-30 cm tall; here 2.4 x 0.24 m
#   paper plane            classic dart folded from an A4 sheet: about 26 cm long (shown at 50 cm)

# =====================================================================
#  SETTINGS  -  change these lines, then run the script again
# =====================================================================
ROOM_NAME = "tiny_planet_stargazer"   # used for the output file names

ROOM_WIDTH = 5.2                    # metres, left to right (the square the little planet sits in)
ROOM_DEPTH = 5.2                    # metres, front to back
WALL_HEIGHT = 3.5                   # metres: top of the observatory dome (there are no room walls here)

THEME = "sunset_hour"               # pick one of the colour themes below
THEMES = {                          # any hex colour works; "main" is the room's hero colour (door, deck chair)
    # "sunset_hour": apricot-to-rose dusk with an indigo top, a low golden sun setting behind the planet.
    "sunset_hour": {
        "background": "#ECB8A6", "wall": "#F4E8D8", "wall_trim": "#D9C3A5", "floor": "#93B865", "wood": "#C59B6D",
        "main": "#4F72A8", "accent_1": "#D6455B", "accent_2": "#F7C66B", "accent_3": "#A18BD0", "cream": "#FBF3E4",
        "plant": "#5C8F4A", "dark": "#2C2848",
        "sky_top": "#3F3C84", "sky_mid": "#D8839E", "sky_low": "#F8C391", "sun": "#FFE6AE", "fill": "#FFE4DA",
        "rock": "#D49A7E", "rock_2": "#B07364", "soil": "#7A5440", "grass": "#7DAA52", "stone": "#E2D6C6",
        "wood_2": "#B88C60", "teak": "#A9744B", "walnut": "#6A4532", "dome": "#7DB6A4", "brass": "#D4AA5C",
        "iron": "#323748", "geode": "#6B5F70", "leather": "#7B4A34", "trunk": "#3E6E78", "glass": "#EEF6F6",
        "terracotta": "#C9714C", "jute": "#CDA977", "quartz": "#FFF1E2", "star": "#FFF3D2", "moon": "#F1E9DA",
        "moon_2": "#C9B8E8", "moon_3": "#F4C7A8", "chart": "#EFE2C4", "crystal": "#B9A2F0",
    },
    # "starry_night": indigo and violet sky with a milky way, cool moonlight and every lamp switched on.
    # This theme uses different lights (moonlight instead of the sun, brighter lamps): see "LIGHTS" below.
    "starry_night": {
        "background": "#1D1B45", "wall": "#E6DFEE", "wall_trim": "#C2B8D2", "floor": "#6A9A70", "wood": "#BC9168",
        "main": "#5272BF", "accent_1": "#E5536D", "accent_2": "#FFD27A", "accent_3": "#A28CEB", "cream": "#F6F1FB",
        "plant": "#558A60", "dark": "#211F44",
        "sky_top": "#080A22", "sky_mid": "#1E1C55", "sky_low": "#4A3384", "sun": "#E6E4FF", "fill": "#B3C2FF",
        "rock": "#958CC0", "rock_2": "#746CA0", "soil": "#4F4160", "grass": "#67A06E", "stone": "#CFC9DE",
        "wood_2": "#AA825B", "teak": "#A0734F", "walnut": "#634438", "dome": "#7CB0C0", "brass": "#DDB866",
        "iron": "#2C3042", "geode": "#5C5274", "leather": "#744836", "trunk": "#3B6680", "glass": "#E8F0FF",
        "terracotta": "#C06E52", "jute": "#C4A67C", "quartz": "#E9E6FF", "star": "#FFF7E0", "moon": "#F3EFE6",
        "moon_2": "#CBBDF3", "moon_3": "#F4C9B4", "chart": "#ECE2CB", "crystal": "#B9A2FF",
    },
}

SUN_WARMTH = 2700                   # Kelvin: 2500 = sunset orange, 6500 = white daylight (night theme: moonlight)
SUN_STRENGTH = 3.0
LAMP_WARMTH = 2200                  # Kelvin of the lamp-post lantern, window and door lights
LAMP_STRENGTH = 9                   # Watts per lamp (the night theme doubles it)
PLANET_RADIUS = 2.55                # metres: radius of the little planet (fits inside ROOM_WIDTH / 2)
SKY_STARS = True                    # painted starfield in the sky (always on at night, only high up at sunset)
SHOOTING_STARS = 2                  # number of shooting stars streaking across the sky (0-3)
SEED = 7                            # change to shuffle grass, flowers, craters and pebbles

SHOW_PLACEHOLDER_FURNITURE = True   # simple built-in furniture inside each slot
SHOW_SLOT_BOXES = True              # wireframe slot boxes in the viewport (never rendered)

CAMERA_HEIGHT_ANGLE = 30            # degrees above the floor (35 = true isometric)
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
NIGHT = THEME == "starry_night"     # night theme: moonlight, lamps on full, milky way

STYLE = "tiny_planet_stargazer"
KIT_VERSION = 2
W, D, H = ROOM_WIDTH, ROOM_DEPTH, WALL_HEIGHT
FLOOR_Z = 0.0       # top of the lawn at the planet's centre; everything else follows ground(x, y)
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


# The room's real materials (one place, so every piece uses the same stone, teak, brass...).
GLOW = 2.0 if NIGHT else 1.0                       # emissive things glow brighter at night
LAWN = M("floor", 0.95, "knit", scale=0.3)         # mown turf: soft fuzzy weave
GRASS = mat("grass", 0.75)                         # grass blades
CRUST = M("rock", 0.9, "concrete", scale=0.6)      # the planet's rocky ball
CRATER = M("rock_2", 0.92, "concrete", scale=1.2)
SOIL = M("soil", 0.95, "concrete", scale=2.0)
PLASTER = M("wall", 0.85, "plaster")               # limewashed render
ASHLAR = M("wall_trim", 0.8, "brick", scale=0.45)  # sandstone block plinth
STONE = M("wall_trim", 0.78, "concrete", scale=2.0)  # dressed sandstone: quoins, arch, cornice
FLAG = M("stone", 0.85, "concrete", scale=1.5)     # flagstones and pebbles
COLUMN = M("cream", 0.7, "plaster", scale=3.0)     # plaster pedestal
OAK = M("wood", 0.55, "wood")                      # decking, frames, window bars, trunk slats
OAK_V = M("wood", 0.57, "wood", along="Z")
OAK_2 = M("wood_2", 0.58, "wood")                  # every other deck board
TEAK = M("teak", 0.55, "wood")                     # tripod, side table, deck chair frame
TEAK_Y = M("teak", 0.56, "wood", along="Y")
WALNUT = M("walnut", 0.45, "wood")
DOOR = M("main", 0.6, "wood", along="Z")           # painted ledged plank door
SIGN = M("dark", 0.6, "wood")                      # painted sign board
COPPER = M("dome", 0.6, "brushed", metal=0.3)    # verdigris copper dome
RIB = M("dome", 0.5, "brushed", metal=0.6, color="#5E8F82" if not NIGHT else "#5C8796")
BRASS = M("brass", 0.3, "brushed", metal=1.0)
IRON = M("iron", 0.45, "brushed", metal=0.7)       # painted cast iron
GEODE = M("geode", 0.92, "concrete", scale=2.5)    # rough grey-violet outside of the geode
CANVAS_A = M("main", 0.9, "fabric")                # deck-chair stripes
CANVAS_B = M("cream", 0.9, "fabric")
KNIT_A = M("accent_3", 0.95, "knit")               # chunky knitted throw on the deck chair
KNIT_B = M("cream", 0.96, "knit")
LEATHER = M("leather", 0.6, "leather")
TRUNK_CANVAS = M("trunk", 0.85, "fabric")
TERRACOTTA = M("terracotta", 0.8, "concrete", scale=4.0)
PAPER = M("cream", 0.8, "paper")
CHART = M("chart", 0.82, "paper")
RUG_A = M("jute", 0.95, "knit", scale=1.5)
RUG_B = M("cream", 0.97, "knit", scale=1.5)
RUG_C = M("accent_3", 0.95, "knit", scale=1.5)
RUG_D = M("main", 0.97, "knit", scale=1.5)
GLASS = mat("glass", 0.05, alpha=0.16)
LEAF = mat("plant", 0.55)
ORRERY_SUN = mat("accent_2", 0.25, metal=0.6, emit=0.9 * GLOW)   # gilt sun of the orrery
STAR_GOLD = mat("accent_2", 0.3, emit=0.4 * GLOW)
LAVENDER = mat("accent_3", 0.7)
AGATE = M("moon_2", 0.62, "marble", scale=3.0)       # white agate band round the geode's opening
GEODE_GLOW = mat("crystal", 0.15, emit=0.55 * GLOW, color="#9A6BD8" if not NIGHT else "#9C74F0")  # lit amethyst points inside
QUARTZ = mat("quartz", 0.05, emit=0.08 * GLOW, alpha=0.45)  # clear rock crystal (a see-through skin...)
QUARTZ_CORE = mat("crystal", 0.2, emit=0.5 * GLOW, color="#D8CCFF" if not NIGHT else "#C9B8FF")  # ...over a pale core
WINDOW_GLOW = mat("accent_2", 0.3, emit=(1.6 if NIGHT else 0.7))
LANTERN = mat("accent_2", 0.15, emit=(4.0 if NIGHT else 2.2))
STAR = mat("star", 0.3, emit=2.5 * GLOW)
TRAIL = mat("star", 0.4, emit=0.9 * GLOW, alpha=0.75)
CRYSTAL = mat("crystal", 0.2, emit=(1.4 if NIGHT else 0.5))
SLIT = mat("dark", 0.85)
COIR = M("jute", 0.95, "fabric", scale=2.0, color="#8A6440")   # coco-fibre basket liner
LETTERS = mat("cream", 0.5, emit=0.35 * GLOW)


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


def beam(name, p0, p1, size, material, parent=None, bevel=0.003):
    """Rectangular timber or bar from p0 to p1. size = (width, thickness) across the beam."""
    p0, p1 = Vector(p0), Vector(p1)
    d = p1 - p0
    o = box(name, (size[0], size[1], d.length), (p0 + p1) / 2, material, bevel=bevel, parent=parent)
    o.rotation_euler = d.to_track_quat("Z", "Y").to_euler()
    return o


def rod(name, p0, p1, r, material, parent=None, segs=12, r2=None):
    """Round rod (dowel, tube, leg) from p0 to p1."""
    p0, p1 = Vector(p0), Vector(p1)
    d = p1 - p0
    o = cyl(name, r, d.length, (p0 + p1) / 2, material, r2=r2, segs=segs, bevel=min(0.002, r * 0.3), parent=parent)
    o.rotation_euler = d.to_track_quat("Z", "Y").to_euler()
    return o


def prism(name, pts, depth, loc, material, rot=(0, 0, 0), parent=None, bevel=0.003):
    """Flat outline (x, z points, counter-clockwise) extruded `depth` metres along local Y (centred)."""
    bm = bmesh.new()
    front = [bm.verts.new((x, -depth / 2, z)) for x, z in pts]
    back = [bm.verts.new((x, depth / 2, z)) for x, z in pts]
    bm.faces.new(front)
    bm.faces.new(list(reversed(back)))
    n = len(pts)
    for i in range(n):
        bm.faces.new((front[i], back[i], back[(i + 1) % n], front[(i + 1) % n]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, bevel, None, parent)


def star_pts(points, r_out, r_in, turn=0.0):
    """Outline of a star with `points` tips (x, z)."""
    out = []
    for k in range(points * 2):
        a = turn + math.pi / 2 + k * math.pi / points
        rr = r_out if k % 2 == 0 else r_in
        out.append((rr * math.cos(a), rr * math.sin(a)))
    return out


def strip(name, path, x0, x1, materials, stripe=0.0, parent=None, thick=0.004, side=(1, 0, 0)):
    """Cloth strip (canvas sling, knitted throw) along a path, from x0 to x1 across `side`. stripe > 0 changes the
    material every `stripe` metres along the path (knitted bands)."""
    side = Vector(side)
    bm = bmesh.new()
    pts = [Vector(p) for p in path]
    prev, run, idx = None, 0.0, 0
    for i, p in enumerate(pts):
        a, b = bm.verts.new(p + side * x0), bm.verts.new(p + side * x1)
        if prev is not None:
            run += (p - pts[i - 1]).length
            if stripe:
                idx = int(run / stripe) % len(materials)
            f = bm.faces.new((prev[0], prev[1], b, a))
            f.material_index = idx
        prev = (a, b)
    o = _obj(name, bm)
    for m_ in materials:
        o.data.materials.append(m_)
    sol = o.modifiers.new("Thickness", "SOLIDIFY")
    sol.thickness, sol.offset = thick, 0.0
    o.data.polygons.foreach_set("use_smooth", [True] * len(o.data.polygons))
    COL_ROOM.objects.link(o)
    o.parent = parent
    return o


CAM_ROT = Euler((R(90 - CAMERA_HEIGHT_ANGLE), 0, R(CAMERA_TURN)))   # the camera's turn (stars face it)


def facing_star(name, loc, r, material, points=4, parent=None):
    """A flat twinkle star that always faces the camera."""
    o = prism(name, star_pts(points, r, r * (0.28 if points == 4 else 0.45)), r * 0.12, (0, 0, 0), material,
              bevel=0, parent=parent)
    o.location = loc
    o.rotation_euler = (CAM_ROT.to_matrix() @ Matrix.Rotation(R(90), 3, "X")).to_euler()
    return no_shadow(o)


# =====================================================================
#  THE LITTLE PLANET: a domed lawn on a rocky, cratered ball
# =====================================================================
PCX, PCY = W / 2, D / 2             # centre of the planet
PR = min(PLANET_RADIUS, W / 2 - 0.05)
TOP_B, BOT_B, N_TOP = 1.12, 1.6, 2.2  # dome height above the equator, ball depth below it, flatness of the top
T_EDGE = 0.37                       # where the lawn stops and the rock begins (profile angle)


def top_profile(t):
    """Planet top (a flattened 'superellipse' dome) at profile angle t: 0 = equator, pi/2 = centre -> (r, z)."""
    c, s = max(0.0, math.cos(t)), max(0.0, math.sin(t))
    return PR * c ** (2 / N_TOP), -TOP_B + TOP_B * s ** (2 / N_TOP)


def ground(x, y):
    """Height of the lawn at (x, y). Furniture stands on it (or on a level pad or deck)."""
    u = min(math.hypot(x - PCX, y - PCY) / PR, 1.0)
    return -TOP_B + TOP_B * max(0.0, 1 - u ** N_TOP) ** (1 / N_TOP)


def low_ground(x, y, rad):
    """Lowest lawn height under a round footprint (for pads and posts that must reach the ground)."""
    d = math.hypot(x - PCX, y - PCY)
    if d < 1e-6:
        return ground(x + rad, y)
    return ground(x + (x - PCX) / d * rad, y + (y - PCY) / d * rad)


def high_ground(x, y, rad):
    d = math.hypot(x - PCX, y - PCY)
    if d <= rad:
        return FLOOR_Z
    return ground(x - (x - PCX) / d * rad, y - (y - PCY) / d * rad)


# Rock ball: a sphere-ish bottom (deeper than wide) and the flattened dome on top.
prof = [(0.0, -TOP_B - BOT_B)]
for k in range(1, 30):
    th = -math.pi / 2 + k * (math.pi / 2) / 30
    prof.append((PR * math.cos(th), -TOP_B + BOT_B * math.sin(th)))
for k in range(0, 11):
    prof.append(top_profile(k * (T_EDGE + 0.06) / 10))
prof.append((0.0, prof[-1][1]))
lathe("Planet_Crust", prof, (PCX, PCY, 0), CRUST, segs=128)
# Lawn: the dome above the rock line (4 mm proud so the two never flicker).
lawn = [top_profile(T_EDGE + k * (math.pi / 2 - T_EDGE) / 28) for k in range(29)]
lathe("Planet_Lawn", [(r_, z_ + 0.004) for r_, z_ in lawn] + [(0.0, FLOOR_Z + 0.004)], (PCX, PCY, 0), LAWN, segs=128)
# Turf edge: a band of dark soil under a rounded lip of grass, like a cut lawn edge.
er, ez = top_profile(T_EDGE)
soil = [top_profile(T_EDGE - 0.1 + k * 0.012) for k in range(10)]
lathe("Planet_Soil", [(r_ + 0.004 + 0.016 * k / 9, z_) for k, (r_, z_) in enumerate(soil)] + [(0.0, soil[-1][1])],
      (PCX, PCY, 0), SOIL, segs=128)
tube("Planet_Turf_Lip", ring_pts(er + 0.012, ez + 0.012, n=128, cx=PCX, cy=PCY), 0.034, LAWN, segs=10, closed=True)


def crust_point(phi, theta):
    """Point + outward normal on the rocky lower half. phi = compass angle, theta = angle below the equator."""
    ct, st = math.cos(theta), math.sin(theta)
    p = Vector((PCX + PR * ct * math.cos(phi), PCY + PR * ct * math.sin(phi), -TOP_B - BOT_B * st))
    n = Vector((ct * math.cos(phi) / PR, ct * math.sin(phi) / PR, -st / BOT_B)).normalized()
    return p, n


def crater(name, phi, theta, rc):
    """A crater: a raised rim with a darker, sunken bowl (seen on the rocky side facing the camera)."""
    p, n = crust_point(phi, theta)
    rot = n.to_track_quat("Z", "Y").to_euler()
    lathe(f"{name}_Rim", [(rc * 0.78, -0.02), (rc * 0.95, 0.018 * rc / 0.12), (rc * 1.08, 0.022 * rc / 0.12),
                          (rc * 1.3, 0.004), (rc * 1.5, -0.03), (rc * 0.78, -0.03)], p, CRUST, segs=28, rot=rot)
    lathe(f"{name}_Bowl", [(0, -0.012 * rc / 0.12), (rc * 0.5, -0.008 * rc / 0.12), (rc * 0.85, 0.008 * rc / 0.12),
                           (rc * 0.85, -0.04), (0, -0.04)], p, CRATER, segs=28, rot=rot)


rng = random.Random(SEED + 11)
for k, (phi, theta, rc) in enumerate(((-50, 18, 0.2), (-12, 34, 0.13), (-80, 40, 0.16), (-35, 55, 0.11),
                                      (-100, 15, 0.1), (5, 12, 0.09), (-62, 70, 0.08), (20, 42, 0.1))):
    crater(f"Crater_{k}", R(phi + rng.uniform(-6, 6)), R(theta + rng.uniform(-4, 4)), rc)

# Little clusters of glowing crystals poking out of the rock.
for k, (phi, theta) in enumerate(((-28, 26), (-72, 52), (-2, 60))):
    p, n = crust_point(R(phi), R(theta))
    for j in range(4):
        dirv = (n + Vector((rng.uniform(-.5, .5), rng.uniform(-.5, .5), rng.uniform(-.6, 0.1)))).normalized()
        ln = rng.uniform(0.07, 0.16)
        c = cyl(f"Crystal_{k}_{j}", ln * 0.22, ln, p + dirv * ln * 0.35, CRYSTAL, r2=0.0, segs=6, bevel=0)
        c.rotation_euler = dirv.to_track_quat("Z", "Y").to_euler()

# Pebbles half-buried along the rock.
for k in range(14):
    p, n = crust_point(R(rng.uniform(-140, 50)), R(rng.uniform(6, 75)))
    ball(f"Crust_Pebble_{k}", rng.uniform(0.025, 0.06), p, CRATER if k % 2 else FLAG, scale=(1, 0.8, 0.55),
         rot=n.to_track_quat("Z", "Y").to_euler(), segs=10)


# =====================================================================
#  LAYOUT (where everything stands on the lawn)
# =====================================================================
HUT_W, HUT_D, HUT_H = 1.4, 1.45, 2.35              # observatory: width (x), depth (y), wall height
HX, HY = PCX - 0.85, PCY + 0.85                   # straight "behind" the centre as the camera sees it
DECK_X, DECK_Y, DECK_R = PCX - 0.6, PCY - 1.2, 1.0  # round stargazing deck (screen left)
Z0 = max(ground(HX + sx * HUT_W / 2, HY + sy * HUT_D / 2) for sx in (-1, 1) for sy in (-1, 1)) + 0.07
Z0 = max(Z0, FLOOR_Z + 0.06)                      # top of the observatory's stone plinth (its floor)
DECK_TOP = high_ground(DECK_X, DECK_Y, DECK_R) + 0.06
FY = HY - HUT_D / 2                               # observatory front wall (door, sign)
FX = HX + HUT_W / 2                               # observatory side wall (pictures)

TEL_XY = (DECK_X - 0.48, DECK_Y + 0.22)
CHAIR_XY = (DECK_X + 0.42, DECK_Y + 0.05)
TABLE_XY = (DECK_X + 0.3, DECK_Y - 0.58)
RUG_XY = (DECK_X + 0.34, DECK_Y - 0.2)
PED_XY = (PCX + 0.55, PCY - 0.4)
LAMP_XY = (PCX + 1.52, PCY - 0.25)
CONE2_XY = (PCX + 1.35, PCY - 1.0)
POST_XY = (PCX + 1.15, PCY + 1.5)
TRUNK_XY = (PCX + 0.4, PCY + 0.45)
PLANTER_XY = (HX + 0.42, FY - 0.2)


def pad(name, x, y, r, top=None, material=None, sides=0):
    """Level stone (or timber) pad: its top is flat; it reaches down to the lowest lawn under it."""
    top = ground(x, y) + 0.03 if top is None else top
    low = low_ground(x, y, r) - 0.04
    o = cyl(name, r, top - low, (x, y, (top + low) / 2), material or FLAG, segs=sides or 28, bevel=0.008)
    return top


# =====================================================================
#  OBSERVATORY: limewashed stone cottage with a verdigris dome
# =====================================================================
box("Hut_Plinth", (HUT_W + 0.12, HUT_D + 0.12, Z0 + 0.75), (HX, HY, (Z0 - 0.75) / 2), ASHLAR, bevel=0.01)
box("Hut_Plinth_Cap", (HUT_W + 0.17, HUT_D + 0.17, 0.05), (HX, HY, Z0 - 0.02), STONE, bevel=0.008)
walls = box("Hut_Walls", (HUT_W, HUT_D, HUT_H), (HX, HY, Z0 + HUT_H / 2), PLASTER, bevel=0.012)

DX, DOOR_W, SPRING, ARCH_R = HX - 0.24, 0.74, 1.5, 0.37   # door centre, width, where the arch starts, arch radius
WX, WZ, WIN_R = HX + 0.4, Z0 + 1.45, 0.17                  # round window
for nm, o in (("Door_Cut_Box", box("Door_Cut_Box", (DOOR_W, 0.16, SPRING + 0.02), (DX, FY, Z0 + SPRING / 2 - 0.01),
                                   PLASTER, bevel=0)),
              ("Door_Cut_Arch", cyl("Door_Cut_Arch", ARCH_R, 0.16, (DX, FY, Z0 + SPRING), PLASTER, segs=48, bevel=0,
                                    rot=(R(90), 0, 0))),
              ("Window_Cut", cyl("Window_Cut", WIN_R, 0.2, (WX, FY, WZ), PLASTER, segs=40, bevel=0,
                                 rot=(R(90), 0, 0)))):
    o.hide_render = o.hide_viewport = True
    b_ = walls.modifiers.new(nm, "BOOLEAN")
    b_.operation, b_.object = "DIFFERENCE", o

# Quoins: big dressed stones wrapping the corners, alternating long and short.
for cx_, cy_ in ((HX - HUT_W / 2, FY), (FX, FY), (FX, HY + HUT_D / 2), (HX - HUT_W / 2, HY + HUT_D / 2)):
    for k in range(int((HUT_H - 0.05) / 0.27)):
        zz = Z0 + 0.14 + k * 0.27
        lx, ly = (0.2, 0.12) if k % 2 == 0 else (0.12, 0.2)
        sx = 1 if cx_ < HX else -1
        sy = 1 if cy_ < HY else -1
        box("Hut_Quoin", (lx, ly, 0.2), (cx_ + sx * (lx / 2 - 0.012), cy_ + sy * (ly / 2 - 0.012), zz), STONE,
            bevel=0.012)

# Arched, ledged plank door with strap hinges, a ring pull and a little round light.
door = empty("Door", (DX, FY + 0.065, Z0))
n_planks = 8
pw = (DOOR_W - 0.02) / n_planks
for i in range(n_planks):
    x0, x1 = -DOOR_W / 2 + 0.01 + i * pw + 0.0015, -DOOR_W / 2 + 0.01 + (i + 1) * pw - 0.0015

    def top_z(x):
        return SPRING + math.sqrt(max(0.0, (ARCH_R - 0.012) ** 2 - x * x))
    xm = (x0 + x1) / 2
    prism(f"Door_Plank_{i}", [(x0, 0.005), (x1, 0.005), (x1, top_z(x1)), (xm, top_z(xm)), (x0, top_z(x0))], 0.04,
          (0, 0, 0), DOOR, parent=door, bevel=0.003)
for zz in (0.32, 1.22):                                     # black iron strap hinges with round ends
    box("Door_Hinge", (0.5, 0.008, 0.04), (-DOOR_W / 2 + 0.27, -0.024, zz), IRON, bevel=0.002, parent=door)
    cyl("Door_Hinge_End", 0.03, 0.008, (0.02 - DOOR_W / 2 + 0.5, -0.024, zz), IRON, rot=(R(90), 0, 0), parent=door)
    for k in range(3):
        ball("Door_Nail", 0.007, (-DOOR_W / 2 + 0.08 + k * 0.17, -0.03, zz), IRON, parent=door, segs=8)
cyl("Door_Pull_Backplate", 0.035, 0.012, (0.24, -0.026, 0.98), IRON, rot=(R(90), 0, 0), parent=door)
tube("Door_Pull_Ring", ring_pts(0.045, 0, n=24), 0.007, IRON, parent=door, closed=True).location = (0.24, -0.04, 0.94)
bpy.data.objects["Door_Pull_Ring"].rotation_euler = (R(90), 0, 0)
cyl("Door_Keyhole", 0.016, 0.006, (0.24, -0.024, 0.86), BRASS, rot=(R(90), 0, 0), parent=door)
cyl("Door_Light_Glass", 0.075, 0.01, (0, -0.02, 1.62), WINDOW_GLOW, rot=(R(90), 0, 0), parent=door, segs=28)
tube("Door_Light_Ring", ring_pts(0.08, 0, n=32), 0.012, BRASS, parent=door, closed=True).location = (0, -0.028, 1.62)
bpy.data.objects["Door_Light_Ring"].rotation_euler = (R(90), 0, 0)
# Sandstone arch: voussoirs round the top, jamb stones down the sides, a stone threshold step.
for k in range(11):
    a = math.pi * (k + 0.5) / 11
    rr = ARCH_R + 0.07
    box("Door_Voussoir", (0.1 if k != 5 else 0.13, 0.05 if k != 5 else 0.06, 0.12),
        (DX + rr * math.cos(a), FY - 0.012, Z0 + SPRING + rr * math.sin(a)), STONE, bevel=0.008,
        rot=(0, -(a - math.pi / 2), 0))
for sx in (-1, 1):
    for k in range(5):
        ww = 0.15 if k % 2 == 0 else 0.11
        box("Door_Jamb", (ww, 0.05, 0.3), (DX + sx * (DOOR_W / 2 + ww / 2 - 0.01), FY - 0.012, Z0 + 0.15 + k * 0.31),
            STONE, bevel=0.008)
step_low = low_ground(DX, FY - 0.2, 0.25) - 0.04
box("Door_Step", (DOOR_W + 0.26, 0.32, Z0 - step_low), (DX, FY - 0.16, (Z0 + step_low) / 2), STONE, bevel=0.01)

# Round window: deep reveal, glowing panes behind a cross of glazing bars, a stone ring and a sill.
no_shadow(cyl("Window_Glass", WIN_R, 0.01, (WX, FY + 0.09, WZ), WINDOW_GLOW, rot=(R(90), 0, 0), segs=40, bevel=0))
for rx in (0, 90):
    box("Window_Bar", (0.022, 0.02, 2 * WIN_R), (WX, FY + 0.08, WZ), OAK, bevel=0.003, rot=(0, R(rx), 0))
tube("Window_Surround", ring_pts(WIN_R + 0.035, 0, n=40), 0.035, STONE, closed=True).location = (WX, FY - 0.005, WZ)
bpy.data.objects["Window_Surround"].rotation_euler = (R(90), 0, 0)
box("Window_Sill", (2 * WIN_R + 0.16, 0.09, 0.04), (WX, FY - 0.03, WZ - WIN_R - 0.07), STONE, bevel=0.006)

# Sign board over the door: YOUR NAME and your role in cream and gold on a painted board.
SIGN_Z, SIGN_W, SIGN_H = Z0 + 2.165, 1.24, 0.3
box("Sign_Board", (SIGN_W, 0.03, SIGN_H), (HX, FY - 0.015, SIGN_Z), SIGN, bevel=0.006)
for sz in (-1, 1):
    box("Sign_Moulding_H", (SIGN_W + 0.04, 0.04, 0.025), (HX, FY - 0.02, SIGN_Z + sz * (SIGN_H / 2 + 0.0125)), BRASS,
        bevel=0.004)
for sx in (-1, 1):
    box("Sign_Moulding_V", (0.025, 0.04, SIGN_H), (HX + sx * (SIGN_W / 2 + 0.0125), FY - 0.02, SIGN_Z), BRASS,
        bevel=0.004)
    prism("Sign_Star", star_pts(4, 0.045, 0.014), 0.006, (HX + sx * (SIGN_W / 2 - 0.07), FY - 0.034, SIGN_Z + 0.04),
          mat("accent_2", 0.3, emit=0.4 * GLOW), bevel=0)
hook_text("name", 1, "YOUR NAME", 0.125, (HX, FY - 0.036, SIGN_Z + 0.045), material=LETTERS, max_width=SIGN_W - 0.3,
          depth=0.005)
hook_text("role", 1, "your role", 0.09, (HX, FY - 0.036, SIGN_Z - 0.085),
          material=mat("accent_2", 0.45, emit=0.4 * GLOW), max_width=SIGN_W - 0.36, depth=0.004)

# Flat roof with a stone cornice, a drum and the dome with its observing slit open.
box("Hut_Cornice", (HUT_W + 0.16, HUT_D + 0.16, 0.08), (HX, HY, Z0 + HUT_H + 0.04), STONE, bevel=0.012)
ROOF = Z0 + HUT_H + 0.08
box("Hut_Roof", (HUT_W + 0.04, HUT_D + 0.04, 0.05), (HX, HY, ROOF + 0.025), M("wall_trim", 0.9, "concrete"),
    bevel=0.006)
ROOF += 0.05
DOME_R = 0.6
cyl("Dome_Drum", DOME_R + 0.02, 0.24, (HX, HY, ROOF + 0.12), PLASTER, segs=64, bevel=0.01)
cyl("Dome_Drum_Band", DOME_R + 0.045, 0.045, (HX, HY, ROOF + 0.24), STONE, segs=64, bevel=0.01)
DZ = ROOF + 0.26
lathe("Dome", [(DOME_R, -0.005)] + [(DOME_R * math.cos(a), DOME_R * math.sin(a)) for a in
                                    (k * math.pi / 2 / 24 for k in range(1, 24))] + [(0, DOME_R)],
      (HX, HY, DZ), COPPER, segs=64)
SLIT_AZ = R(205)                                       # the slit faces the sunset, a little toward the camera
for k in range(12):                                    # copper ribs between the panels
    az = SLIT_AZ + R(15) + k * (2 * math.pi - R(30)) / 11
    tube("Dome_Rib", [(HX + (DOME_R + 0.006) * math.cos(a) * math.cos(az), HY + (DOME_R + 0.006) * math.cos(a) *
                       math.sin(az), DZ + (DOME_R + 0.006) * math.sin(a)) for a in (R(e) for e in range(0, 82, 6))],
         0.011, RIB, segs=6)
t1 = Vector((-math.sin(SLIT_AZ), math.cos(SLIT_AZ), 0))
for k in range(17):                                    # the open slit: dark gap from the base to past the top
    a = R(2 + k * 5)
    nrm = Vector((math.cos(a) * math.cos(SLIT_AZ), math.cos(a) * math.sin(SLIT_AZ), math.sin(a)))
    tang = nrm.cross(t1)
    rot = Matrix((t1, tang, nrm)).transposed().to_euler()
    box("Dome_Slit", (0.2, 0.06, 0.012), Vector((HX, HY, DZ)) + nrm * (DOME_R + 0.002), SLIT, bevel=0, rot=rot)
for side in (-1, 1):                                   # shutter rails either side of the slit
    tube("Dome_Shutter_Rail", [Vector((HX, HY, DZ)) + t1 * side * 0.115 + Vector((math.cos(a) * math.cos(SLIT_AZ),
          math.cos(a) * math.sin(SLIT_AZ), math.sin(a))) * (DOME_R + 0.01) for a in (R(e) for e in range(0, 96, 6))],
         0.012, BRASS, segs=6)
tel_dir = Vector((math.cos(R(38)) * math.cos(SLIT_AZ), math.cos(R(38)) * math.sin(SLIT_AZ), math.sin(R(38))))
rod("Dome_Telescope", Vector((HX, HY, DZ + 0.1)) + tel_dir * 0.25, Vector((HX, HY, DZ + 0.1)) + tel_dir * 0.78, 0.055,
    BRASS, segs=20)
cyl("Dome_Finial_Base", 0.05, 0.04, (HX, HY, DZ + DOME_R + 0.01), BRASS, segs=20)
rod("Dome_Finial_Rod", (HX, HY, DZ + DOME_R), (HX, HY, DZ + DOME_R + 0.2), 0.008, BRASS)
facing_star("Dome_Finial_Star", (HX, HY, DZ + DOME_R + 0.25), 0.08, mat("brass", 0.3, metal=1.0, emit=0.3 * GLOW))

# Shrubs: clipped box balls and a lavender-blue hydrangea round the cottage (generic garden planting).
for k, (x, y, rr, key) in enumerate(((HX - HUT_W / 2 - 0.12, FY + 0.05, 0.2, "plant"),
                                     (FX + 0.18, HY + HUT_D / 2 - 0.05, 0.24, "plant"),
                                     (HX - HUT_W / 2 + 0.05, HY + HUT_D / 2 + 0.12, 0.22, "plant"))):
    z = ground(x, y)
    foliage(f"Shrub_{k}", [((x, y, z + rr * 0.85), rr)], 260, (0.035, 0.018), mat(key, 0.6), seed=SEED + k, droop=0.0)
    ball(f"Shrub_Core_{k}", rr * 0.82, (x, y, z + rr * 0.85), mat(key, 0.8, color="#3F6A35" if not NIGHT else
                                                                   "#3A6343"))


# Low planting at the front-right edge of the lawn: a clipped ball, a mound of lavender-blue asters.
for k, (dx, dy, rr, col) in enumerate(((1.95, -0.2, 0.17, None), (1.75, -0.65, 0.12, "#8F7CC8" if not NIGHT else "#9C88E0"),
                                       (2.0, 0.25, 0.11, "#E7A0B0" if not NIGHT else "#E59AB2"))):
    x, y = PCX + dx, PCY + dy
    z = ground(x, y)
    if col is None:
        foliage(f"Shrub_Front_{k}", [((x, y, z + rr * 0.8), rr)], 180, (0.032, 0.016), mat("plant", 0.6), seed=SEED + 9,
                droop=0.0)
        ball(f"Shrub_Front_Core_{k}", rr * 0.82, (x, y, z + rr * 0.8), mat("plant", 0.8, color="#3F6A35" if not NIGHT
                                                                                     else "#3A6343"))
    else:
        foliage(f"Flower_Mound_Leaves_{k}", [((x, y, z + rr * 0.4), rr)], 70, (0.03, 0.012), LEAF, seed=SEED + 12 + k,
                droop=0.2)
        frnd = random.Random(SEED + 60 + k)
        for j in range(16):
            a, q = frnd.uniform(0, 2 * math.pi), rr * math.sqrt(frnd.random())
            ball(f"Flower_Mound_Bloom_{k}", 0.017, (x + q * math.cos(a), y + q * math.sin(a),
                                                    z + rr * 0.55 + frnd.uniform(0, 0.06)), mat(f"bloom_{k}", 0.6, color=col),
                 scale=(1, 1, 0.55), segs=10)


# =====================================================================
#  STARGAZING DECK: slatted boards, curved fascia, skirting to the lawn
# =====================================================================
deck = empty("Deck", (DECK_X, DECK_Y, 0))
BW, GAP = 0.12, 0.004
n_b = int(2 * DECK_R / (BW + GAP))
for i in range(n_b):
    yy = -DECK_R + (i + 0.5) * (BW + GAP)
    half = math.sqrt(max(0.0, DECK_R ** 2 - (abs(yy) + BW / 2) ** 2)) - 0.03
    if half <= 0.05:
        continue
    box("Deck_Board", (2 * half, BW, 0.025), (0, yy, DECK_TOP - 0.0125), OAK if i % 2 else OAK_2, bevel=0.003,
        parent=deck)
n_f = 40
for k in range(n_f):                                   # curved fascia board round the edge
    a = 2 * math.pi * (k + 0.5) / n_f
    box("Deck_Fascia", (0.03, 2 * math.pi * DECK_R / n_f + 0.004, 0.14), (math.cos(a) * DECK_R, math.sin(a) * DECK_R,
        DECK_TOP - 0.06), OAK_V, bevel=0.004, rot=(0, 0, a), parent=deck)
for k in range(64):                                    # vertical skirting boards down to the lawn
    a = 2 * math.pi * (k + 0.5) / 64
    x, y = math.cos(a) * (DECK_R - 0.035), math.sin(a) * (DECK_R - 0.035)
    lo = ground(DECK_X + x, DECK_Y + y) - 0.05
    hi = DECK_TOP - 0.12
    if hi - lo > 0.02:
        box("Deck_Skirting", (0.02, 2 * math.pi * DECK_R / 64 - 0.012, hi - lo), (x, y, (hi + lo) / 2), OAK_V,
            bevel=0.003, rot=(0, 0, a), parent=deck)
# =====================================================================
#  PATHS, GRASS AND FLOWERS
# =====================================================================
stones = [(PCX + 0.0, PCY - 0.2), (PCX + 0.28, PCY - 0.13), (PCX + 0.85, PCY + 0.02), (PCX + 1.02, PCY + 0.35),
          (PCX + 1.12, PCY + 0.7), (PCX + 1.18, PCY + 1.05), (PCX + 0.85, PCY - 0.65), (PCX + 1.02, PCY - 0.98)]
for k, (x, y) in enumerate(stones):
    rr = rng.uniform(0.11, 0.15)
    ball(f"Path_Stone_{k}", rr, (x, y, ground(x, y) - 0.004), FLAG, scale=(1, rng.uniform(0.7, 0.9), 0.16),
         rot=(0, 0, rng.uniform(0, math.pi)), segs=16)

BLOCKERS = [(DECK_X, DECK_Y, DECK_R + 0.08), (PED_XY[0], PED_XY[1], 0.3), (LAMP_XY[0], LAMP_XY[1], 0.28),
            (CONE2_XY[0], CONE2_XY[1], 0.22), (POST_XY[0], POST_XY[1], 0.22), (TRUNK_XY[0], TRUNK_XY[1], 0.55),
            (PLANTER_XY[0], PLANTER_XY[1], 0.36), (PCX + 1.95, PCY - 0.2, 0.2), (PCX + 1.75, PCY - 0.65, 0.14),
            (PCX + 2.0, PCY + 0.25, 0.13)] + [(x, y, 0.16) for x, y in stones]


def blocked(x, y):
    if abs(x - HX) < HUT_W / 2 + 0.2 and abs(y - HY) < HUT_D / 2 + 0.2:
        return True
    return any(math.hypot(x - bx, y - by) < br for bx, by, br in BLOCKERS)


def grass_tufts(name, n, seed):
    """Tufts of 4-7 bent blades scattered over the lawn (one mesh)."""
    rnd = random.Random(seed)
    bm = bmesh.new()
    placed = tries = 0
    while placed < n and tries < n * 30:
        tries += 1
        a, rr = rnd.uniform(0, 2 * math.pi), (er - 0.05) * math.sqrt(rnd.random())
        x, y = PCX + rr * math.cos(a), PCY + rr * math.sin(a)
        if blocked(x, y):
            continue
        z = ground(x, y)
        for _ in range(rnd.randint(4, 7)):
            ang, hgt = rnd.uniform(0, 2 * math.pi), rnd.uniform(0.04, 0.1)
            lean = rnd.uniform(0.15, 0.55)
            dirv = Vector((math.cos(ang), math.sin(ang), 0))
            side = Vector((-math.sin(ang), math.cos(ang), 0)) * 0.006
            base = Vector((x, y, z - 0.004)) + dirv * rnd.uniform(0, 0.02)
            tip = base + dirv * lean * hgt + Vector((0, 0, hgt))
            mid = base + dirv * lean * hgt * 0.3 + Vector((0, 0, hgt * 0.55))
            v = [bm.verts.new(p) for p in (base - side, base + side, mid + side * 0.6, mid - side * 0.6, tip)]
            bm.faces.new((v[0], v[1], v[2], v[3]))
            bm.faces.new((v[3], v[2], v[4]))
        placed += 1
    o = _obj(name, bm)
    o.data.materials.append(GRASS)
    COL_ROOM.objects.link(o)
    return o


grass_tufts("Lawn_Grass", 420, SEED + 5)
for k in range(46):                                     # daisies and little violet star-flowers in the grass
    for _ in range(30):
        a, rr = rng.uniform(0, 2 * math.pi), (er - 0.1) * math.sqrt(rng.random())
        x, y = PCX + rr * math.cos(a), PCY + rr * math.sin(a)
        if not blocked(x, y):
            break
    z = ground(x, y)
    rod(f"Flower_Stem_{k}", (x, y, z - 0.005), (x, y, z + 0.05), 0.0025, GRASS, segs=5)
    if k % 3:
        cyl(f"Flower_Petals_{k}", 0.016, 0.004, (x, y, z + 0.052), mat("cream", 0.6), segs=12, bevel=0)
        ball(f"Flower_Eye_{k}", 0.0065, (x, y, z + 0.055), mat("accent_2", 0.5), segs=8)
    else:
        prism(f"Flower_Star_{k}", star_pts(5, 0.017, 0.008), 0.004, (x, y, z + 0.053), mat("accent_3", 0.6),
              rot=(R(90), 0, rng.uniform(0, 3)), bevel=0)


# =====================================================================
#  FURNITURE SLOTS  (same names in every template)
#  size = (width, depth, height); front of the furniture faces local -Y
# =====================================================================
PED_TOP = pad("Pedestal_Flag", PED_XY[0], PED_XY[1], 0.3, sides=6)
LAMP_TOP = pad("Geode_Lamp_Gravel", LAMP_XY[0], LAMP_XY[1], 0.27, sides=9)
CONE2_TOP = pad("Crystal_Cluster_Gravel", CONE2_XY[0], CONE2_XY[1], 0.22, sides=9)
POST_TOP = pad("Lamp_Post_Stone", POST_XY[0], POST_XY[1], 0.2, sides=6)
TRUNK_TOP = ground(*TRUNK_XY) + 0.005
RUG_TOP = DECK_TOP + 0.012                        # top of the braided rug on the deck
slot("telescope",  (0.8, 0.8, 1.62), TEL_XY, z=DECK_TOP, turn=90, shape="lamp")
slot("chair",      (0.62, 1.0, 1.05), CHAIR_XY, z=RUG_TOP, turn=-90, shape="chair")
slot("side_table", (0.45, 0.45, 0.46), TABLE_XY, z=RUG_TOP, shape="table")
slot("rug",        (1.16, 1.16, 0.014), RUG_XY, z=DECK_TOP, kind="rug", shape="rug")
slot("hero_prop",  (0.4, 0.4, 1.26), PED_XY, z=PED_TOP, turn=45, shape="box")
slot("lamp",       (0.44, 0.44, 0.48), LAMP_XY, z=LAMP_TOP, turn=45, shape="lamp")
slot("floor_lamp", (1.3, 0.32, 2.26), POST_XY, z=POST_TOP, turn=45, shape="lamp")
slot("trunk",      (0.86, 0.5, 0.92), TRUNK_XY, z=TRUNK_TOP, turn=90, shape="box")
slot("planter",    (0.6, 0.22, 0.55), PLANTER_XY, z=ground(*PLANTER_XY), shape="plant")


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


LAMPS = LAMP_STRENGTH * (2.0 if NIGHT else 1.0)


# =====================================================================
#  PLACEHOLDER FURNITURE  (replaced when you add your own with add_furniture.py)
# =====================================================================
def build_telescope():
    """Brass refractor (50 mm, 1 m with draw tubes) on a teak tripod, pointing at the sunset (local +Y)."""
    root, w, d, h = furniture_root("telescope")
    head = 1.02
    for k in range(3):                                  # three teak legs with brass feet and clamps
        a = R(-90 + 120 * k)
        foot = Vector((math.cos(a) * 0.36, math.sin(a) * 0.36, 0.0))
        top = Vector((math.cos(a) * 0.045, math.sin(a) * 0.045, head - 0.03))
        beam("Telescope_Leg", foot + Vector((0, 0, 0.03)), top, (0.034, 0.02), TEAK, parent=root)
        rod("Telescope_Foot", foot, foot + (top - foot).normalized() * 0.06, 0.016, BRASS, parent=root)
        clamp = foot + (top - foot) * 0.45
        cyl("Telescope_Clamp", 0.014, 0.05, clamp, BRASS, parent=root, segs=12)
        rod("Telescope_Spreader", foot + (top - foot) * 0.33, Vector((0, 0, foot.z + (top - foot).z * 0.33)), 0.006,
            BRASS, parent=root)
    tray_z = (head - 0.03) * 0.33 + 0.012               # triangular teak accessory tray with two eyepieces
    cyl("Telescope_Tray", 0.105, 0.016, (0, 0, tray_z), TEAK, parent=root, segs=3, bevel=0.004, rot=(0, 0, R(-90)))
    for k, (ex, ey) in enumerate(((0.02, -0.03), (-0.035, 0.012))):
        cyl(f"Telescope_Eyepiece_{k}", 0.011, 0.03, (ex, ey, tray_z + 0.022), BRASS, parent=root, segs=12)
        cyl(f"Telescope_Eyepiece_Lens_{k}", 0.008, 0.002, (ex, ey, tray_z + 0.037), mat("dark", 0.1), parent=root,
            segs=12, bevel=0)
    cyl("Telescope_Head", 0.06, 0.06, (0, 0, head), BRASS, parent=root, segs=24)
    for sx in (-1, 1):                                  # fork that holds the tube
        box("Telescope_Fork", (0.012, 0.05, 0.12), (sx * 0.045, 0, head + 0.08), BRASS, parent=root, bevel=0.003)
    piv = Vector((0, 0, head + 0.12))
    el = R(30)
    dirv = Vector((0, math.cos(el), math.sin(el)))
    upn = Vector((0, -math.sin(el), math.cos(el)))
    rod("Telescope_Tube", piv - dirv * 0.26, piv + dirv * 0.5, 0.032, BRASS, parent=root, segs=24)
    rod("Telescope_Sheath", piv - dirv * 0.12, piv + dirv * 0.22, 0.036, LEATHER, parent=root, segs=24)
    rod("Telescope_Dew_Shield", piv + dirv * 0.47, piv + dirv * 0.64, 0.044, BRASS, parent=root, segs=24)
    rod("Telescope_Objective", piv + dirv * 0.636, piv + dirv * 0.642, 0.038, mat("dark", 0.05, color="#24304A"),
        parent=root, segs=24)
    for k, (a0, a1, r_) in enumerate(((0.26, 0.4, 0.025), (0.4, 0.5, 0.019), (0.5, 0.55, 0.014))):
        rod(f"Telescope_Draw_{k}", piv - dirv * a0, piv - dirv * a1, r_, BRASS, parent=root, segs=20)
    rod("Telescope_Eyecup", piv - dirv * 0.55, piv - dirv * 0.58, 0.017, mat("dark", 0.6), parent=root, segs=16)
    rod("Telescope_Focus", piv - dirv * 0.3 + Vector((-0.05, 0, 0)), piv - dirv * 0.3 + Vector((0.05, 0, 0)), 0.008,
        BRASS, parent=root)
    for sx in (-1, 1):
        cyl("Telescope_Focus_Knob", 0.014, 0.012, piv - dirv * 0.3 + Vector((sx * 0.055, 0, 0)), BRASS, parent=root,
            rot=(0, R(90), 0), segs=14)
    rod("Telescope_Finder", piv + upn * 0.058 - dirv * 0.05, piv + upn * 0.058 + dirv * 0.2, 0.011, BRASS,
        parent=root, segs=14)
    for t in (0.0, 0.15):
        rod("Telescope_Finder_Foot", piv + upn * 0.03 + dirv * t, piv + upn * 0.05 + dirv * t, 0.005, BRASS, parent=root)
    rod("Telescope_Slow_Motion", piv - dirv * 0.18 - upn * 0.03, Vector((0.0, -0.05, head + 0.02)), 0.004, BRASS,
        parent=root)


def build_chair():
    """Traditional folding deck chair: teak frame, striped canvas sling, a knitted throw over the top rail."""
    root, w, d, h = furniture_root("chair")
    rx = 0.285
    f, t = Vector((0, -0.42, 0)), Vector((0, 0.34, 0.98))      # long frame: front feet -> top rail
    for sx in (-1, 1):
        beam("Chair_Rail", f + Vector((sx * rx, 0, 0.015)), t + Vector((sx * rx, 0, 0)), (0.022, 0.045), TEAK,
             parent=root)
        p0 = Vector((sx * 0.245, 0.48, 0.015))                 # rear stand (with the notched ground bar)
        p1 = f + (t - f) * 0.6 + Vector((sx * 0.245, 0, 0))
        beam("Chair_Stand", p0, p1, (0.022, 0.04), TEAK, parent=root)
        cyl("Chair_Pivot", 0.012, 0.012, p1 + Vector((sx * 0.018, 0, 0)), BRASS, rot=(0, R(90), 0), parent=root)
    for nm, p, r_, half in (("Top_Rail", t + Vector((0, -0.005, 0.0)), 0.017, rx + 0.025),
                            ("Front_Rail", f + (t - f) * 0.36, 0.016, rx + 0.02),
                            ("Low_Rail", f + (t - f) * 0.09, 0.013, rx),
                            ("Stand_Bar", Vector((0, 0.48, 0.03)), 0.013, 0.245),
                            ("Stand_Top", f + (t - f) * 0.6 + Vector((0, 0.0, -0.03)), 0.012, 0.245)):
        rod(f"Chair_{nm}", p - Vector((half, 0, 0)), p + Vector((half, 0, 0)), r_, TEAK, parent=root)
    pf = f + (t - f) * 0.36 + Vector((0, 0, 0.02))
    sling = spline([(0, pf.y, pf.z), (0, -0.02, 0.29), (0, 0.13, 0.34), (0, 0.24, 0.6), (0, 0.32, 0.98)], 6)
    n = 7
    for k in range(n):                                          # vertical stripes, alternating colours
        x0 = -0.255 + k * 0.51 / n
        strip(f"Chair_Canvas_{k}", sling, x0, x0 + 0.51 / n, [CANVAS_A if k % 2 == 0 else CANVAS_B], parent=root,
              thick=0.004)
    # Chunky knitted throw lying on the sling, folded over the top rail and hanging down the back.
    sp = spline([(0, 0.125, 0.356), (0, 0.226, 0.607), (0, 0.286, 0.884), (0, 0.322, 1.0), (0, 0.345, 1.012),
                 (0, 0.37, 0.99), (0, 0.385, 0.85), (0, 0.392, 0.64)], 6)
    strip("Chair_Throw", sp, -0.215, 0.215, [KNIT_A, KNIT_B], stripe=0.11, parent=root, thick=0.016)
    for k in range(10):                                         # tassels on the hanging end
        x = -0.2 + k * 0.4 / 9
        rod("Chair_Throw_Tassel", (x, 0.392, 0.645), (x, 0.394, 0.59), 0.004, KNIT_B, parent=root, segs=5)


def build_side_table():
    """Folding teak side table: slatted top on two battens, X legs, with a mug, a star atlas, a planisphere
    (star wheel) and a red-light torch."""
    root, w, d, h = furniture_root("side_table")
    top = 0.45
    for k in range(5):
        box("SideTable_Slat", (0.45, 0.078, 0.02), (0, -0.18 + k * 0.09, top - 0.01), TEAK, bevel=0.003, parent=root)
    for sx in (-1, 1):
        box("SideTable_Batten", (0.03, 0.42, 0.025), (sx * 0.17, 0, top - 0.032), TEAK_Y, bevel=0.003, parent=root)
        for k, sy in enumerate((-1, 1)):
            beam("SideTable_Leg", (sx * (0.2 - k * 0.026), sy * 0.2, 0), (sx * (0.2 - k * 0.026), -sy * 0.17, top - 0.045),
                 (0.022, 0.028), TEAK, parent=root)
        cyl("SideTable_Bolt", 0.012, 0.06, (sx * 0.187, 0.015, (top - 0.045) * 0.53), BRASS, rot=(0, R(90), 0),
            parent=root, segs=12)
    # enamel camping mug
    lathe("SideTable_Mug", [(0, 0), (0.04, 0), (0.041, 0.085), (0.044, 0.088), (0.038, 0.088), (0.037, 0.006), (0, 0.006)],
          (0.11, -0.09, top), M("cream", 0.3, "ceramic"), parent=root, segs=24)
    cyl("SideTable_Tea", 0.037, 0.003, (0.11, -0.09, top + 0.07), mat("tea", 0.2, color="#7A4A2A"), parent=root, bevel=0)
    tube("SideTable_Mug_Handle", spline([(0.15, -0.09, top + 0.07), (0.175, -0.09, top + 0.06), (0.172, -0.09, top + 0.025),
                                         (0.15, -0.09, top + 0.018)], 4), 0.005, M("cream", 0.3, "ceramic"), parent=root)
    tube("SideTable_Mug_Rim", ring_pts(0.042, top + 0.087, n=24, cx=0.11, cy=-0.09), 0.0025, mat("main", 0.4),
         parent=root, closed=True)
    # star atlas
    box("SideTable_Atlas_Cover", (0.24, 0.17, 0.028), (-0.06, -0.06, top + 0.014), M("main", 0.7, "leather"),
        bevel=0.004, parent=root, rot=(0, 0, R(8)))
    box("SideTable_Atlas_Pages", (0.23, 0.162, 0.022), (-0.055, -0.06, top + 0.014), PAPER, bevel=0.001, parent=root,
        rot=(0, 0, R(8)))
    prism("SideTable_Atlas_Star", star_pts(5, 0.03, 0.013), 0.002, (-0.06, -0.06, top + 0.0285), BRASS,
          rot=(R(90), 0, R(8)), parent=root, bevel=0)
    # planisphere (star wheel): a square card jacket with an oval window over the turning star disc
    ps = empty("SideTable_Planisphere", (-0.05, 0.125, top), rot=(0, 0, R(-10)), parent=root)
    jacket = M("planisphere", 0.75, "paper", color="#263A6E" if not NIGHT else "#2A3F7A")
    box("Planisphere_Jacket", (0.18, 0.18, 0.004), (0, 0, 0.002), jacket, bevel=0.0015, parent=ps)
    cyl("Planisphere_Window", 0.068, 0.0015, (0, 0.006, 0.0045), mat("dark", 0.4, color="#141A38"), parent=ps,
        segs=32, bevel=0).scale = (1.0, 0.78, 1.0)
    tube("Planisphere_Window_Rim", [(0.069 * math.cos(a), 0.006 + 0.054 * math.sin(a), 0.0048) for a in
                                    (2 * math.pi * q / 40 for q in range(40))], 0.0013, BRASS, parent=ps, closed=True,
         segs=5)
    prnd = random.Random(SEED + 23)
    for k in range(14):
        a, q = prnd.uniform(0, 2 * math.pi), math.sqrt(prnd.random()) * 0.9
        cyl("Planisphere_Star", 0.0025 if k % 3 else 0.004, 0.001, (0.066 * q * math.cos(a), 0.006 + 0.051 * q *
            math.sin(a), 0.0056), mat("accent_2", 0.3, emit=0.6 * GLOW), parent=ps, segs=6, bevel=0)
    for k in range(24):                                         # month ticks round the window
        a = 2 * math.pi * k / 24
        box("Planisphere_Tick", (0.002, 0.008, 0.0008), (0.079 * math.cos(a), 0.006 + 0.065 * math.sin(a), 0.0044),
            mat("cream", 0.6), bevel=0, rot=(0, 0, a + math.pi / 2), parent=ps)
    # red-light astronomy torch (keeps your night vision)
    rod("SideTable_Torch", (0.07, 0.11, top + 0.016), (0.19, 0.06, top + 0.016), 0.015, mat("dark", 0.45), parent=root,
        segs=16)
    rod("SideTable_Torch_Lens", (0.19, 0.06, top + 0.016), (0.196, 0.0575, top + 0.016), 0.016,
        mat("torch_red", 0.2, emit=1.2 * GLOW, color="#E0303A"), parent=root, segs=16)
    rod("SideTable_Torch_Grip", (0.09, 0.102, top + 0.016), (0.14, 0.081, top + 0.016), 0.0165, mat("iron", 0.8),
        parent=root, segs=16)


def build_rug():
    """Round braided rug (116 cm): coils of jute, cream and two colours, slightly domed braids."""
    root, w, d, h = furniture_root("rug")
    mats = [RUG_A, RUG_B, RUG_A, RUG_C, RUG_B, RUG_A, RUG_D, RUG_B]
    cyl("Rug_Centre", 0.04, 0.01, (0, 0, 0.006), RUG_B, parent=root, bevel=0.004, segs=20)
    rr, k = 0.055, 0
    while rr < w / 2 - 0.012:
        o = tube(f"Rug_Coil_{k}", ring_pts(rr, 0.0, n=max(20, int(rr * 110))), 0.0135, mats[k % len(mats)],
                 parent=root, segs=8, closed=True)
        o.location, o.scale = (0, 0, 0.007), (1, 1, 0.5)
        rr += 0.027
        k += 1


def orrery(root, zb):
    """Brass desk orrery (about 25 cm across): a turned walnut foot, a horizon ring on three legs, a gilt sun on
    the central pillar and four planets on stepped arms (one ringed, one with its moon)."""
    lathe("Orrery_Foot", [(0, zb), (0.09, zb), (0.092, zb + 0.008), (0.075, zb + 0.022), (0.03, zb + 0.03),
                          (0.026, zb + 0.045), (0, zb + 0.045)], (0, 0, 0), WALNUT, parent=root, segs=36)
    ring_z = zb + 0.1
    for k in range(3):                                   # three brass legs carry the horizon ring
        a = R(30 + 120 * k)
        rod("Orrery_Leg", (0.06 * math.cos(a), 0.06 * math.sin(a), zb + 0.012),
            (0.112 * math.cos(a), 0.112 * math.sin(a), ring_z), 0.003, BRASS, parent=root, segs=6)
    tube("Orrery_Horizon_Ring", ring_pts(0.114, ring_z, n=56), 0.0045, BRASS, parent=root, closed=True, segs=6)
    for k in range(12):                                  # engraved month marks on the ring
        a = 2 * math.pi * k / 12
        ball("Orrery_Ring_Mark", 0.0042, (0.114 * math.cos(a), 0.114 * math.sin(a), ring_z + 0.004), STAR_GOLD,
             parent=root, segs=6)
    rod("Orrery_Pillar", (0, 0, zb + 0.045), (0, 0, zb + 0.22), 0.007, BRASS, parent=root, segs=14)
    sun_z = zb + 0.245
    ball("Orrery_Sun", 0.034, (0, 0, sun_z), ORRERY_SUN, parent=root, segs=28)
    for k in range(8):                                   # little sun rays
        a = 2 * math.pi * k / 8
        cyl("Orrery_Sun_Ray", 0.008, 0.016, (0.04 * math.cos(a), 0.04 * math.sin(a), sun_z), ORRERY_SUN, r2=0.0,
            segs=6, bevel=0, rot=(0, R(90), a), parent=root)
    # (arm length, planet radius, colour, angle from the camera side, arm height): spread so none hides the sun
    planets = ((0.052, 0.012, "accent_1", R(75), 0.13), (0.075, 0.016, "main", R(-55), 0.15),
               (0.097, 0.011, "accent_3", R(150), 0.17), (0.1, 0.017, "accent_2", R(-115), 0.19))
    for k, (rad, pr, key, az, arm_z) in enumerate(planets):
        az += R(-90)                                     # local angle that faces the camera (the slot turns 45)
        ex, ey = rad * math.cos(az), rad * math.sin(az)
        rod(f"Orrery_Arm_{k}", (0, 0, zb + arm_z), (ex, ey, zb + arm_z), 0.0028, BRASS, parent=root, segs=6)
        cyl(f"Orrery_Collar_{k}", 0.011, 0.008, (0, 0, zb + arm_z), BRASS, parent=root, segs=14)
        pz = sun_z - 0.01 + 0.012 * k
        rod(f"Orrery_Post_{k}", (ex, ey, zb + arm_z), (ex, ey, pz - pr), 0.0025, BRASS, parent=root, segs=6)
        ball(f"Orrery_Planet_{k}", pr, (ex, ey, pz), mat(key, 0.45, emit=0.15 * GLOW), parent=root, segs=18)
        if k == 3:                                       # ringed giant
            rg = tube("Orrery_Planet_Ring", ring_pts(pr * 1.7, 0, n=32), 0.0025, BRASS, parent=root, closed=True,
                      segs=5)
            rg.location, rg.rotation_euler = (ex, ey, pz), (R(22), R(-10), 0)
        if k == 1:                                       # a moon on a tiny wire arm
            mx, my = ex + 0.026 * math.cos(az + 1.2), ey + 0.026 * math.sin(az + 1.2)
            rod("Orrery_Moon_Arm", (ex, ey, pz - pr - 0.004), (mx, my, pz - pr - 0.004), 0.0015, BRASS, parent=root,
                segs=5)
            ball("Orrery_Moon", 0.0055, (mx, my, pz - pr + 0.002), mat("moon", 0.6), parent=root, segs=10)
    return sun_z


def build_hero_prop():
    """A brass display orrery (35 cm across) on a walnut plinth, on a reeded plaster column pedestal (77 cm)."""
    root, w, d, h = furniture_root("hero_prop")
    box("Pedestal_Plinth", (0.32, 0.32, 0.06), (0, 0, 0.03), COLUMN, bevel=0.006, parent=root)
    box("Pedestal_Plinth_Step", (0.28, 0.28, 0.03), (0, 0, 0.075), COLUMN, bevel=0.006, parent=root)
    lathe("Pedestal_Base_Torus", [(0.13, 0.09), (0.135, 0.105), (0.128, 0.12), (0.115, 0.125), (0.11, 0.125)],
          (0, 0, 0), COLUMN, parent=root, segs=40)
    cyl("Pedestal_Shaft", 0.105, 0.56, (0, 0, 0.405), COLUMN, parent=root, segs=40, bevel=0.003)
    for k in range(18):                                 # reeds round the column
        a = 2 * math.pi * k / 18
        cyl("Pedestal_Reed", 0.011, 0.52, (math.cos(a) * 0.104, math.sin(a) * 0.104, 0.405), COLUMN, parent=root,
            segs=8, bevel=0.003)
    lathe("Pedestal_Capital", [(0.11, 0.685), (0.13, 0.7), (0.135, 0.715), (0.12, 0.725), (0, 0.725)], (0, 0, 0),
          COLUMN, parent=root, segs=40)
    box("Pedestal_Abacus", (0.3, 0.3, 0.05), (0, 0, 0.75), COLUMN, bevel=0.006, parent=root)
    top = 0.775
    lathe("Orrery_Plinth", [(0, top), (0.148, top), (0.15, top + 0.012), (0.142, top + 0.03), (0, top + 0.03)],
          (0, 0, 0), WALNUT, parent=root, segs=40)
    zb = top + 0.03
    orr = empty("Orrery", (0, 0, zb), parent=root)       # a large display orrery: the desk model at 1.4x
    orr.scale = (1.4, 1.4, 1.4)
    sun_z = zb + 1.4 * orrery(orr, 0.0)
    light("Light_Orrery", "POINT", 2.2 * GLOW, lin(COLORS["accent_2"])[:3], (0.0, 0.0, sun_z), size=0.04,
          parent=root)


def crystal_point(name, base, dirv, ln, r, material, parent):
    """One hexagonal crystal: a 6-sided prism with a pointed tip, growing from `base` along `dirv`."""
    dirv = Vector(dirv).normalized()
    rot = dirv.to_track_quat("Z", "Y").to_euler()
    body = ln * 0.72
    cyl(f"{name}_Prism", r, body, Vector(base) + dirv * body / 2, material, segs=6, bevel=0, rot=rot, parent=parent)
    cyl(f"{name}_Tip", r, ln - body, Vector(base) + dirv * (body + (ln - body) / 2), material, r2=0.0, segs=6,
        bevel=0, rot=rot, parent=parent)


def build_lamp():
    """Amethyst cathedral geode lamp: a rough egg of rock split open at the front, lined with glowing violet
    crystal points, a white agate band round the opening, on a blackened steel plinth with LEDs inside."""
    root, w, d, h = furniture_root("lamp")
    rng_g = random.Random(SEED + 31)
    box("Geode_Plinth", (0.3, 0.24, 0.05), (0, 0, 0.025), IRON, bevel=0.006, parent=root)
    box("Geode_Plinth_Foot", (0.26, 0.2, 0.012), (0, 0, 0.056), WALNUT, bevel=0.003, parent=root)
    cx, cz, rx, ry, rz = 0.0, 0.272, 0.15, 0.115, 0.205        # the geode egg (centre z, radii)
    # Shell: a lumpy egg with the front (local -Y) broken away, given real thickness.
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=28, v_segments=18, radius=1.0)
    for v in bm.verts:
        n = v.co.copy()
        lump = 1.0 + 0.06 * math.sin(n.x * 7 + 1.3) * math.cos(n.z * 5) + 0.04 * math.sin(n.y * 9 + n.z * 4)
        v.co = Vector((n.x * rx * lump, n.y * ry * lump, n.z * rz * lump))
    cut = [f for f in bm.faces if f.calc_center_median().y < -ry * 0.42 and f.calc_center_median().z > -rz * 0.72]
    bmesh.ops.delete(bm, geom=cut, context="FACES")
    shell = _obj("Geode_Shell", bm)
    shell.location = (cx, 0, cz)
    _finish(shell, GEODE, 0, None, root)
    sol = shell.modifiers.new("Thickness", "SOLIDIFY")
    sol.thickness, sol.offset = 0.022, -1.0
    # Agate band along the broken edge (rings the opening just inside the shell).
    rim = []
    for k in range(36):
        a = 2 * math.pi * k / 36
        x_, z_ = math.cos(a) * rx * 0.86, math.sin(a) * rz * 0.8
        rim.append((cx + x_, -ry * 0.42 + 0.004, cz + z_ * (0.92 if z_ < 0 else 1.0)))
    tube("Geode_Agate_Band", rim, 0.014, AGATE, parent=root, closed=True, segs=8)
    # Crystal lining: many short violet points growing inward from the inner wall, longest at the back.
    for k in range(70):
        u = rng_g.uniform(R(25), R(155))           # around the back half
        t = rng_g.uniform(R(-70), R(70))
        p = Vector((math.cos(u) * math.cos(t) * rx * 0.82, math.sin(u) * math.cos(t) * ry * 0.82,
                    math.sin(t) * rz * 0.82))
        inward = (-p + Vector((rng_g.uniform(-.02, .02), -0.05, rng_g.uniform(-.02, .02)))).normalized()
        ln = rng_g.uniform(0.028, 0.06)
        crystal_point(f"Geode_Crystal_{k}", (cx + p.x, p.y, cz + p.z), inward, ln, ln * 0.2, GEODE_GLOW, root)
    cyl("Geode_Floor", rx * 0.75, 0.02, (cx, 0.0, cz - rz * 0.74), GEODE_GLOW, segs=18, bevel=0.004, parent=root)
    light("Light_Lamp", "POINT", LAMPS * 0.3, lin(COLORS["crystal"])[:3], (cx, -0.03, cz), size=0.05, parent=root)
    light("Light_Geode_Spill", "POINT", LAMPS * 0.7, lin(COLORS["crystal"])[:3], (cx, -0.2, cz - 0.05), size=0.08,
          parent=root)


def crystal_cluster(name, root, s):
    """Rock-crystal quartz cluster: a rough matrix stone with a few clear hexagonal points fanning upward, one tall
    master point in the middle (points of clearly different sizes, so they read as crystals, not a lump)."""
    rng_c = random.Random(SEED + 37)
    ball(f"{name}_Matrix", 0.16 * s, (0, 0, 0.02 * s), GEODE, scale=(1.0, 0.85, 0.38), parent=root, segs=16)
    ball(f"{name}_Matrix_2", 0.09 * s, (0.08 * s, 0.05 * s, 0.04 * s), GEODE, scale=(1.0, 0.8, 0.5), parent=root,
         segs=12)
    pts = ((0.0, 0.0, 0.0, 0.36, 0.045), (R(20), 0.05, R(24), 0.24, 0.034), (R(140), 0.055, R(30), 0.2, 0.03),
           (R(250), 0.06, R(36), 0.17, 0.026), (R(320), 0.07, R(44), 0.13, 0.022), (R(80), 0.08, R(48), 0.1, 0.018),
           (R(195), 0.09, R(55), 0.08, 0.015))
    for k, (a, off, lean, ln, r) in enumerate(pts):
        a += rng_c.uniform(-0.15, 0.15)
        base = (math.cos(a) * off * s, math.sin(a) * off * s * 0.85, 0.035 * s)
        dirv = Vector((math.sin(lean) * math.cos(a), math.sin(lean) * math.sin(a), math.cos(lean)))
        crystal_point(f"{name}_Point_{k}", base, dirv, ln * s, r * s, QUARTZ, root)
        crystal_point(f"{name}_Core_{k}", Vector(base) + dirv * 0.01, dirv, ln * s * 0.8, r * s * 0.45, QUARTZ_CORE,
                      root)


def build_floor_lamp():
    """Double-arm cast-iron garden lamp post (2.2 m): a lantern on the left arm, a hanging flower basket on the right."""
    root, w, d, h = furniture_root("floor_lamp")
    box("LampPost_Base", (0.16, 0.16, 0.05), (0, 0, 0.025), IRON, bevel=0.006, parent=root)
    lathe("LampPost_Foot", [(0.075, 0.05), (0.075, 0.1), (0.06, 0.13), (0.045, 0.3), (0.05, 0.33), (0.04, 0.36),
                            (0.033, 0.38), (0, 0.38)], (0, 0, 0), IRON, parent=root, segs=24)
    cyl("LampPost_Shaft", 0.03, 1.36, (0, 0, 0.38 + 0.68), IRON, r2=0.024, parent=root, segs=20)
    for zz in (0.9, 1.6):
        lathe("LampPost_Collar", [(0.03, zz - 0.03), (0.04, zz - 0.01), (0.04, zz + 0.01), (0.03, zz + 0.03), (0, zz + 0.03)],
              (0, 0, 0), IRON, parent=root, segs=20)
    arm_z = 1.74
    for sx in (-1, 1):
        tube("LampPost_Arm", [(0, 0, arm_z), (sx * 0.2, 0, arm_z + 0.01), (sx * 0.41, 0, arm_z)], 0.016, IRON,
             parent=root, segs=10)
        curl = [(sx * (0.05 + 0.3 * q), 0, arm_z - 0.03 - 0.12 * math.sin(math.pi * q)) for q in (i / 8 for i in range(9))]
        curl += [(sx * (0.35 + 0.03 * math.cos(a)), 0, arm_z - 0.06 + 0.03 * math.sin(a)) for a in
                 (math.pi + k * 0.7 for k in range(1, 7))]
        tube("LampPost_Scroll", curl, 0.008, IRON, parent=root, segs=8)
    lathe("LampPost_Cap", [(0.035, 1.78), (0.045, 1.8), (0.02, 1.84), (0.012, 1.9), (0, 1.94)], (0, 0, 0), IRON,
          parent=root, segs=16)
    # Victorian lantern standing on the left arm end.
    lx, lz = -0.41, arm_z + 0.015
    lathe("Lantern_Cup", [(0.02, lz), (0.06, lz + 0.03), (0.065, lz + 0.05), (0, lz + 0.05)], (lx, 0, 0), IRON,
          parent=root, segs=4, rot=(0, 0, R(45)))
    for sx in (-1, 1):
        for sy in (-1, 1):
            box("Lantern_Post", (0.012, 0.012, 0.2), (lx + sx * 0.055, sy * 0.055, lz + 0.15), IRON, parent=root,
                bevel=0.002, rot=(0, 0, 0))
    no_shadow(box("Lantern_Glass", (0.1, 0.1, 0.19), (lx, 0, lz + 0.15), LANTERN, parent=root, bevel=0.002))
    lathe("Lantern_Roof", [(0.085, lz + 0.25), (0.085, lz + 0.265), (0.03, lz + 0.33), (0.012, lz + 0.345),
                           (0, lz + 0.35)], (lx, 0, 0), IRON, parent=root, segs=4, rot=(0, 0, R(45)))
    ball("Lantern_Finial", 0.014, (lx, 0, lz + 0.36), IRON, parent=root, segs=10)
    light("Light_Lantern", "POINT", LAMPS * 1.4, kelvin(LAMP_WARMTH), (lx, 0, lz + 0.15), size=0.05, parent=root)
    # Hanging flower basket on the right arm: a 35 cm wire basket with a coco liner, three chains,
    # a dome of foliage and trailing flowers in the theme colours.
    bx_, rim_z = 0.39, 1.45
    cyl("Basket_Hook", 0.012, 0.05, (bx_, 0, arm_z - 0.04), IRON, parent=root, segs=10)
    for k in range(3):
        a = R(90 + 120 * k)
        rod("Basket_Chain", (bx_, 0, arm_z - 0.065), (bx_ + 0.16 * math.cos(a), 0.16 * math.sin(a), rim_z + 0.01),
            0.003, IRON, parent=root, segs=5)
    lathe("Basket_Liner", [(0.0, rim_z - 0.15), (0.06, rim_z - 0.145), (0.12, rim_z - 0.11), (0.155, rim_z - 0.055),
                           (0.17, rim_z), (0.0, rim_z)], (bx_, 0, 0), COIR, parent=root, segs=28)
    for zz, rr in ((rim_z, 0.172), (rim_z - 0.06, 0.153), (rim_z - 0.115, 0.115)):
        tube("Basket_Wire", ring_pts(rr + 0.004, zz, n=36, cx=bx_), 0.003, IRON, parent=root, closed=True, segs=5)
    foliage("Basket_Foliage", [((bx_, 0, rim_z + 0.05), 0.15), ((bx_ - 0.08, -0.06, rim_z - 0.06), 0.09),
                               ((bx_ + 0.1, -0.04, rim_z - 0.1), 0.08)], 120, (0.04, 0.02), mat("plant", 0.6),
            parent=root, seed=SEED + 71, droop=0.35)
    ball("Basket_Foliage_Core", 0.14, (bx_, 0, rim_z + 0.04), mat("plant", 0.8, color="#3F6A35" if not NIGHT else
                                                                    "#3A6343"), scale=(1, 1, 0.7), parent=root)
    brnd = random.Random(SEED + 73)
    for k in range(34):                                 # petunia-style flowers: a five-lobed cup with a pale eye
        a = brnd.uniform(0, 2 * math.pi)
        up = brnd.uniform(-0.9, 1.0)
        rr = 0.17 if up > -0.2 else 0.16
        p = Vector((bx_ + rr * math.cos(a) * math.sqrt(1 - 0.5 * up * up), rr * math.sin(a) *
                    math.sqrt(1 - 0.5 * up * up), rim_z + 0.04 + up * 0.13))
        key = ("accent_1", "cream", "accent_3")[k % 3]
        nrm = (p - Vector((bx_, 0, rim_z))).normalized()
        cyl("Basket_Flower", 0.022, 0.008, p, mat(key, 0.6), segs=5, bevel=0.003, parent=root,
            rot=nrm.to_track_quat("Z", "Y").to_euler())
        ball("Basket_Flower_Eye", 0.006, p + nrm * 0.005, mat("accent_2", 0.5), parent=root, segs=6)
    for k in range(7):                                  # trailing stems spilling over the rim
        a = R(-75 + k * 25)
        top_ = Vector((bx_ + 0.15 * math.cos(a), 0.15 * math.sin(a), rim_z - 0.02))
        hang = [top_, top_ + Vector((0.03 * math.cos(a), 0.03 * math.sin(a), -0.08)),
                top_ + Vector((0.04 * math.cos(a), 0.04 * math.sin(a), -0.2 - 0.03 * (k % 3)))]
        tube("Basket_Trail", spline(hang, 4), 0.003, LEAF, parent=root, segs=5)
        foliage("Basket_Trail_Leaves", [(hang[-1] + Vector((0, 0, 0.04)), 0.04), (hang[1], 0.035)], 14, (0.028, 0.014),
                mat("plant", 0.6), parent=root, seed=SEED + 80 + k, droop=0.5)
        cyl("Basket_Trail_Flower", 0.02, 0.008, hang[-1] + Vector((0, 0, -0.005)), mat(("accent_1", "cream",
            "accent_3")[k % 3], 0.6), segs=5, bevel=0.003, parent=root, rot=(R(-160), 0, a))


def build_trunk():
    """Flat-top steamer trunk (86 x 51 x 41 cm): canvas over wood, oak slats, brass corners, leather handles,
    with a constellation globe and two rolled star charts on the lid."""
    root, w, d, h = furniture_root("trunk")
    L, Dd, Hb, Hl = 0.86, 0.5, 0.33, 0.08
    for sx in (-1, 1):
        box("Trunk_Skid", (0.05, Dd - 0.04, 0.025), (sx * 0.3, 0, 0.0125), OAK, parent=root, bevel=0.003)
    z0 = 0.025
    box("Trunk_Body", (L, Dd, Hb), (0, 0, z0 + Hb / 2), TRUNK_CANVAS, parent=root, bevel=0.006)
    box("Trunk_Lid", (L, Dd, Hl), (0, 0, z0 + Hb + 0.004 + Hl / 2), TRUNK_CANVAS, parent=root, bevel=0.008)
    top = z0 + Hb + 0.004 + Hl
    for yy in (-0.16, 0.0, 0.16):
        box("Trunk_Lid_Slat", (L + 0.01, 0.05, 0.012), (0, yy, top + 0.004), OAK, parent=root, bevel=0.003)
    for zz in (z0 + 0.08, z0 + Hb - 0.05):
        box("Trunk_Band_Front", (L + 0.01, 0.012, 0.045), (0, -Dd / 2 - 0.004, zz), OAK, parent=root, bevel=0.003)
        for sx in (-1, 1):
            box("Trunk_Band_End", (0.012, Dd + 0.01, 0.045), (sx * (L / 2 + 0.004), 0, zz), OAK_V, parent=root,
                bevel=0.003)
    for sx in (-1, 1):
        box("Trunk_Upright", (0.05, 0.014, Hb - 0.01), (sx * 0.24, -Dd / 2 - 0.006, z0 + Hb / 2), OAK_V, parent=root,
            bevel=0.003)
        for sy in (-1, 1):
            for zz in (z0 + 0.03, top - 0.03):
                box("Trunk_Corner", (0.07, 0.07, 0.07), (sx * (L / 2 - 0.03), sy * (Dd / 2 - 0.03), zz), BRASS,
                    parent=root, bevel=0.01)
        tube("Trunk_Handle", spline([(sx * (L / 2 + 0.01), -0.09, z0 + 0.25), (sx * (L / 2 + 0.035), -0.05, z0 + 0.22),
                                     (sx * (L / 2 + 0.035), 0.05, z0 + 0.22), (sx * (L / 2 + 0.01), 0.09, z0 + 0.25)], 4),
             0.009, LEATHER, parent=root, segs=8)
        for sy in (-1, 1):
            box("Trunk_Handle_Plate", (0.006, 0.04, 0.05), (sx * (L / 2 + 0.006), sy * 0.09, z0 + 0.25), BRASS,
                parent=root, bevel=0.002)
        box("Trunk_Latch", (0.05, 0.01, 0.07), (sx * 0.3, -Dd / 2 - 0.006, z0 + Hb), BRASS, parent=root, bevel=0.003)
    box("Trunk_Lock", (0.09, 0.012, 0.09), (0, -Dd / 2 - 0.006, z0 + Hb), BRASS, parent=root, bevel=0.004)
    cyl("Trunk_Keyhole", 0.01, 0.004, (0, -Dd / 2 - 0.013, z0 + Hb - 0.01), mat("dark", 0.5), rot=(R(90), 0, 0),
        parent=root, segs=10)
    # Constellation desk globe (8 in): turned walnut foot, brass half-meridian, dark blue sphere with gold stars.
    gx, gy, gz = 0.18, 0.04, top + 0.01
    lathe("Globe_Foot", [(0, gz), (0.075, gz), (0.075, gz + 0.015), (0.05, gz + 0.03), (0.02, gz + 0.05), (0.018, gz + 0.1),
                         (0.03, gz + 0.115), (0, gz + 0.115)], (gx, gy, 0), WALNUT, parent=root, segs=28)
    gc = Vector((gx, gy, gz + 0.235))
    ball("Globe_Sphere", 0.1, gc, M("dark", 0.45, "paper", color="#26305E" if not NIGHT else "#2C3A72"), parent=root,
         segs=32)
    tilt = Matrix.Rotation(R(23.5), 3, "Y")
    tube("Globe_Meridian", [gc + tilt @ Vector((0.112 * math.sin(a), 0, 0.112 * math.cos(a))) for a in
                            (R(-100 + 10 * k) for k in range(21))], 0.006, BRASS, parent=root, segs=8)
    rod("Globe_Holder", (gx, gy, gz + 0.112), gc + tilt @ Vector((0, 0, -0.112)), 0.006, BRASS, parent=root)
    grnd = random.Random(SEED + 21)
    dots = []
    for k in range(26):
        v = Vector((grnd.gauss(0, 1), grnd.gauss(0, 1), grnd.gauss(0, 1))).normalized()
        if v.dot(Vector((1, -1, 0.3)).normalized()) < 0.1:
            v = -v
        dots.append(gc + v * 0.1005)
        ball("Globe_Star", 0.0045 if k % 4 else 0.0065, gc + v * 0.1, mat("accent_2", 0.3, emit=0.6 * GLOW),
             parent=root, segs=6)
    for a, b in ((0, 1), (1, 2), (2, 3), (4, 5), (5, 6)):
        tube("Globe_Line", [dots[a], (dots[a] + dots[b]) / 2 + ((dots[a] + dots[b]) / 2 - gc).normalized() * 0.002,
                            dots[b]], 0.0015, mat("accent_2", 0.4, emit=0.3 * GLOW), parent=root, segs=4)
    # two rolled charts tied with ribbon
    for k, (yy, rr_) in enumerate(((-0.12, 0.028), (-0.06, 0.024))):
        rod("Trunk_Chart_Roll", (-0.38, yy, top + 0.01 + rr_), (0.02, yy + 0.02, top + 0.01 + rr_), rr_, CHART,
            parent=root, segs=20)
        tube("Trunk_Chart_Ribbon", ring_pts(rr_ + 0.002, 0, n=16), 0.003, mat("accent_1", 0.6), parent=root,
             closed=True).location = (-0.18, yy + 0.01, top + 0.01 + rr_)
    for o in root.children:
        if o.name.startswith("Trunk_Chart_Ribbon"):
            o.rotation_euler = (0, R(90), 0)


def build_planter():
    """Terracotta trough planter (60 x 22 x 18 cm) of lavender with silvery leaves."""
    root, w, d, h = furniture_root("planter")
    for sx in (-1, 1):
        box("Planter_Foot", (0.06, 0.16, 0.025), (sx * 0.22, 0, 0.0125), TERRACOTTA, parent=root, bevel=0.004)
    box("Planter_Trough", (0.56, 0.19, 0.16), (0, 0, 0.025 + 0.08), TERRACOTTA, parent=root, bevel=0.01)
    box("Planter_Rim", (0.6, 0.22, 0.028), (0, 0, 0.025 + 0.16 + 0.006), TERRACOTTA, parent=root, bevel=0.008)
    box("Planter_Soil", (0.54, 0.17, 0.01), (0, 0, 0.025 + 0.17), SOIL, parent=root, bevel=0.003)
    rnd = random.Random(SEED + 31)
    foliage("Planter_Leaves", [((x, 0, 0.25), 0.07) for x in (-0.19, -0.06, 0.07, 0.19)], 45, (0.05, 0.008),
            mat("plant", 0.6, color="#93A88B"), parent=root, seed=SEED + 3, droop=0.1)
    for k in range(22):
        x, y = rnd.uniform(-0.24, 0.24), rnd.uniform(-0.06, 0.06)
        tip = Vector((x + rnd.uniform(-0.05, 0.05), y + rnd.uniform(-0.04, 0.04), rnd.uniform(0.42, 0.53)))
        rod("Lavender_Stem", (x, y, 0.2), tip, 0.0025, mat("plant", 0.6, color="#7E9A73"), parent=root, segs=5)
        for j in range(5):
            ball("Lavender_Bud", 0.009, tip + Vector((0, 0, -j * 0.013)), LAVENDER, scale=(1, 1, 1.3), parent=root,
                 segs=8)


PLACEHOLDERS = {
    "telescope": build_telescope, "chair": build_chair, "side_table": build_side_table, "rug": build_rug,
    "hero_prop": build_hero_prop, "lamp": build_lamp, "floor_lamp": build_floor_lamp, "trunk": build_trunk,
    "planter": build_planter,
}

if SHOW_PLACEHOLDER_FURNITURE:
    for slot_name, build in PLACEHOLDERS.items():
        build()

# A rock-crystal cluster on its gravel pad, and a little watering can by the lavender trough.
cone2 = empty("Crystal_Cluster", (CONE2_XY[0], CONE2_XY[1], CONE2_TOP), rot=(0, 0, R(20)))
crystal_cluster("Crystal_Cluster", cone2, 1.0)
WC_XY = (PLANTER_XY[0] + 0.45, PLANTER_XY[1] - 0.18)
wc = empty("Watering_Can", (WC_XY[0], WC_XY[1], ground(*WC_XY)), rot=(0, 0, R(-30)))
CAN = M("copper", 0.35, "brushed", metal=1.0, color="#C27B4E")
lathe("Watering_Can_Body", [(0, 0), (0.06, 0), (0.065, 0.01), (0.062, 0.12), (0.05, 0.14), (0.03, 0.15), (0, 0.15)],
      (0, 0, 0), CAN, parent=wc, segs=28)
rod("Watering_Can_Spout", (0.05, 0, 0.04), (0.2, 0, 0.15), 0.008, CAN, parent=wc, r2=0.006)
cyl("Watering_Can_Sprinkler", 0.016, 0.018, (0.205, 0, 0.155), BRASS, rot=(0, R(55), 0), parent=wc, segs=14)
tube("Watering_Can_Handle", spline([(-0.045, 0, 0.14), (-0.01, 0, 0.2), (0.04, 0, 0.18), (0.055, 0, 0.13)], 5), 0.007,
     CAN, parent=wc)


# =====================================================================
#  WALL DECOR + PORTFOLIO PICTURES  (on the observatory's side wall)
# =====================================================================
def framed_x(name, y, z, size, frame_mat=None, mount=0.03, depth=0.025):
    """Picture frame on the +x wall (22 mm moulding, a mount round the picture). Returns hook loc + rot."""
    w, h = size
    fw = 0.022
    ow, oh = w + 2 * mount + 2 * fw, h + 2 * mount + 2 * fw
    fm = frame_mat or OAK
    box(f"{name}_Backing", (0.01, ow - 0.01, oh - 0.01), (FX + 0.005, y, z), PAPER, bevel=0)
    for sz in (-1, 1):
        box(f"{name}_Frame_H", (depth, ow, fw), (FX + depth / 2, y, z + sz * (oh - fw) / 2), fm, bevel=0.003)
    for sy in (-1, 1):
        box(f"{name}_Frame_V", (depth, fw, oh - 2 * fw), (FX + depth / 2, y + sy * (ow - fw) / 2, z), fm, bevel=0.003)
    return (FX + 0.0115, y, z), (0, 0, R(90))


# Poster 1: the star chart (your first project shows here).
loc, rot = framed_x("StarChart", HY, Z0 + 1.72, (0.78, 0.5), frame_mat=BRASS, mount=0.025)
p1 = hook_image("poster", 1, (0.78, 0.5), loc, rot=rot, default_key="dark")
px_ = loc[0] + 0.002
crnd = random.Random(SEED + 41)
chart_stars = []
for k in range(22):
    yy, zz = HY + crnd.uniform(-0.36, 0.36), loc[2] + crnd.uniform(-0.22, 0.22)
    chart_stars.append((yy, zz))
deco = [no_shadow(prism(f"StarChart_Star_{k}", star_pts(4, 0.018 if k % 5 == 0 else 0.009, 0.004), 0.002,
                        (px_, yy, zz), mat("accent_2", 0.3, emit=0.6 * GLOW), rot=(0, 0, R(90)), bevel=0))
        for k, (yy, zz) in enumerate(chart_stars)]
for k, (a, b) in enumerate(((0, 5), (5, 10), (10, 15), (3, 8), (8, 13), (13, 18))):
    ya, za = chart_stars[a]
    yb, zb = chart_stars[b]
    deco.append(no_shadow(beam(f"StarChart_Line_{k}", (px_, ya, za), (px_, yb, zb), (0.002, 0.003),
                               mat("cream", 0.6, emit=0.2 * GLOW), bevel=0)))
deco.append(no_shadow(tube("StarChart_Circle", [(px_, HY + 0.2 * math.cos(a), loc[2] + 0.2 * math.sin(a)) for a in
                                                (2 * math.pi * q / 48 for q in range(48))], 0.0015,
                           mat("cream", 0.6, emit=0.2 * GLOW), closed=True, segs=4)))
hook_default(p1, *deco)

# Frames 1 and 2: below the chart, either side.
DEFAULT_ART = (("main", "accent_2"), ("accent_3", "cream"))
for i, sy in enumerate((-1, 1)):
    loc, rot = framed_x(f"Frame{i + 1}", HY + sy * 0.26, Z0 + 0.98, (0.32, 0.42), mount=0.025)
    f = hook_image("frame", i + 1, (0.32, 0.42), loc, rot=rot, default_key=DEFAULT_ART[i][0])
    x_, y_, z_ = loc[0] + 0.002, loc[1], loc[2]
    if i == 0:              # a sunset over hills
        hook_default(f, ball("Frame1_Sun", 0.05, (x_, y_ + 0.04, z_ + 0.05), mat("accent_2", 0.7), scale=(0.05, 1, 1)),
                     box("Frame1_Hill", (0.002, 0.32, 0.12), (x_ + 0.001, y_, z_ - 0.15), mat("plant", 0.8), bevel=0),
                     ball("Frame1_Hill2", 0.1, (x_ + 0.0015, y_ - 0.06, z_ - 0.08), mat("floor", 0.8),
                          scale=(0.02, 1, 0.45)))
    else:                   # moon phases
        hook_default(f, *[ball(f"Frame2_Moon_{k}", 0.03, (x_, y_, z_ + 0.12 - k * 0.08), mat("cream", 0.6,
                          emit=0.2 * GLOW), scale=(0.05, 0.4 + 0.3 * k if k < 2 else 1.0 - 0.3 * (k - 2), 1))
                          for k in range(4)])
# Brass title plates under the pictures (your project titles).
for i, (yy, zz, wdt) in enumerate(((HY, Z0 + 1.35, 0.46), (HY - 0.26, Z0 + 0.665, 0.34), (HY + 0.26, Z0 + 0.665, 0.34))):
    box(f"Title_Plate_{i + 1}", (0.006, wdt, 0.068), (FX + 0.003, yy, zz), BRASS, bevel=0.002)
    hook_text("title", i + 1, f"PROJECT {('ONE', 'TWO', 'THREE')[i]}", 0.042, (FX + 0.009, yy, zz),
              rot=(R(90), 0, R(90)), material=mat("dark", 0.5), max_width=wdt - 0.03, depth=0.002)

# Tagline on a long painted name board (like a ship's quarterboard) fixed to the front of the rock on iron
# brackets, so even a long sentence stays readable. Left blank if you have no tagline.
QB_W, QB_H, QB_Z, QB_D = 2.4, 0.24, -0.98, PR + 0.06
qb_dir = Vector((math.cos(R(CAMERA_TURN - 90)), math.sin(R(CAMERA_TURN - 90)), 0))   # towards the camera
qb = empty("Quarterboard", (PCX + qb_dir.x * QB_D, PCY + qb_dir.y * QB_D, QB_Z), rot=(0, 0, R(CAMERA_TURN)))
box("Quarterboard_Board", (QB_W, 0.04, QB_H), (0, 0.0, 0), SIGN, bevel=0.01, parent=qb)
for sz in (-1, 1):
    box("Quarterboard_Moulding", (QB_W - 0.04, 0.012, 0.016), (0, -0.024, sz * (QB_H / 2 - 0.022)), BRASS, bevel=0.003,
        parent=qb)
for sx in (-1, 1):
    prism("Quarterboard_Star", star_pts(4, 0.06, 0.018), 0.008, (sx * (QB_W / 2 - 0.08), -0.026, 0),
          mat("accent_2", 0.3, emit=0.4 * GLOW), bevel=0, parent=qb)
    bx_ = sx * 0.85                                     # iron bracket back to the rock
    gap = QB_D - math.sqrt(PR ** 2 - bx_ ** 2) + 0.06    # from the board back into the rock
    box("Quarterboard_Bracket", (0.03, gap, 0.03), (bx_, 0.02 + gap / 2, 0), IRON, bevel=0.004, parent=qb)
    cyl("Quarterboard_Bolt", 0.018, 0.01, (bx_, -0.024, 0), IRON, rot=(R(90), 0, 0), parent=qb, segs=12)
hook_text("tagline", 1, "your tagline here", 0.11, (0, -0.031, 0), material=LETTERS, max_width=QB_W - 0.48,
          depth=0.004, parent=qb)


# =====================================================================
#  SKY: mini-moons (your links), a paper plane (email), shooting stars
# =====================================================================
def moon(name, loc, r, key, link, ring=False, seed=0):
    rnd = random.Random(SEED + seed)
    dark_hex = "#" + "".join(f"{int(int(COLORS[key][i:i + 2], 16) * 0.88):02X}" for i in (1, 3, 5))
    crater_mat = mat(f"{key}_crater", 0.9, color=dark_hex, emit=(0.2 if NIGHT else 0.03))
    m_ = M(key, 0.85, "concrete", scale=1.5, emit=(0.25 if NIGHT else 0.05))
    o = ball(name, r, loc, m_, segs=36)
    for k in range(4):
        v = (Vector((1, -1, 0.5)).normalized() * 0.6 + Vector((rnd.uniform(-1, 1), rnd.uniform(-1, 1), rnd.uniform(-.8, .8))))
        if k == 0:                                      # the big crater sits off to one side, not dead centre
            v = Vector((1, -1, 0.5)).normalized() + Vector((0.55, 0.45, 0.35))
        v.normalize()
        rc = r * (0.32 if k == 0 else rnd.uniform(0.1, 0.18))
        lathe(f"{name}_Crater_{k}", [(0, -0.003), (rc * 0.8, -0.001), (rc, 0.0025), (rc * 1.2, 0.0), (rc * 1.25, -0.01),
                                     (0, -0.01)], v * r, crater_mat,
              parent=o, segs=20, rot=v.to_track_quat("Z", "Y").to_euler())
    if ring:
        rg = tube(f"{name}_Ring", ring_pts(r * 1.75, 0, n=48), r * 0.09, mat("accent_2", 0.4, emit=0.2 * GLOW),
                  parent=o, closed=True, segs=8)
        rg.scale, rg.rotation_euler = (1, 1, 0.25), (R(18), R(-12), 0)
    hook_link(o, link)
    return o


moon("Moon_GitHub", (0.25, 0.9, 2.15), 0.24, "moon", "github", seed=1)
moon("Moon_LinkedIn", (5.05, 4.25, 1.35), 0.2, "moon_2", "linkedin", ring=True, seed=2)
moon("Moon_Website", (5.4, 3.35, -0.85), 0.17, "moon_3", "website", seed=3)

# Paper plane looping out from behind the first moon, with a dashed trail (click it to email). The trail is laid
# out in the camera's own screen axes (right, up, towards the camera), so the plane always shows its profile.
_cr = CAM_ROT.to_matrix()
_right, _up, _back = _cr.col[0], _cr.col[1], _cr.col[2]
loop_ru = [(2.265, 2.544), (1.523, 2.447), (0.974, 2.06), (0.748, 1.415), (0.813, 0.963), (1.039, 0.64), (1.297, 0.479)]
trail = spline([_right * r_ + _up * u_ + _back * (-0.87 + 2.17 * k / (len(loop_ru) - 1))
                for k, (r_, u_) in enumerate(loop_ru)], 8)
for k in range(0, len(trail) - 2, 2):
    no_shadow(rod(f"Plane_Trail_{k}", trail[k], trail[k] + (trail[k + 1] - trail[k]) * 0.85, 0.007, TRAIL, segs=6))
plane_dir = (Vector(trail[-1]) - Vector(trail[-3])).normalized()
bm = bmesh.new()
# Classic dart: two wings folded up from a centre keel (slight dihedral), nose forward along +X.
vs = [bm.verts.new(p) for p in ((0.27, 0, 0), (-0.23, 0.17, 0.035), (-0.23, 0, 0.0), (-0.23, -0.17, 0.035),
                                (-0.23, 0, -0.065), (-0.2, 0, -0.065))]
bm.faces.new((vs[0], vs[1], vs[2])).material_index = 0
bm.faces.new((vs[0], vs[2], vs[3])).material_index = 0
bm.faces.new((vs[0], vs[5], vs[4], vs[2])).material_index = 1
plane = _obj("Paper_Plane", bm)
plane.data.materials.append(mat("cream", 0.7, emit=0.15 * GLOW))
plane.data.materials.append(mat("plane_keel", 0.75, emit=0.1 * GLOW, color="#E4D8C8" if not NIGHT else "#D6D2EA"))
COL_ROOM.objects.link(plane)
sol = plane.modifiers.new("Paper", "SOLIDIFY")
sol.thickness = 0.003
plane.location = Vector(trail[-1]) + plane_dir * 0.3
plane.rotation_euler = plane_dir.to_track_quat("X", "Z").to_euler()
plane.rotation_euler.rotate_axis("X", R(-12))
for k in range(2):                                      # fold creases along the top of each wing
    no_shadow(beam(f"Paper_Plane_Crease_{k}", (0.25, 0, 0.002), (-0.22, (0.06 if k else -0.06), 0.014), (0.002, 0.002),
                   mat("plane_keel", 0.75, emit=0.1 * GLOW, color="#E4D8C8" if not NIGHT else "#D6D2EA"),
                   parent=plane, bevel=0))
hook_link(plane, "email")

# Asteroid stepping stones drifting off the front edge of the planet.
arnd = random.Random(SEED + 51)
for k, (rad, z, r_) in enumerate(((2.85, -1.15, 0.12), (3.12, -1.45, 0.095), (3.36, -1.74, 0.07), (3.55, -2.0, 0.05))):
    az = R(-140 + k * 7)
    ball(f"Asteroid_{k}", r_, (PCX + rad * math.cos(az), PCY + rad * math.sin(az), z), CRUST if k % 2 == 0 else CRATER,
         scale=(1.0, arnd.uniform(0.75, 0.95), arnd.uniform(0.55, 0.7)), rot=(arnd.random(), arnd.random(), arnd.random()),
         segs=9)

# Twinkle stars and shooting stars in the sky around the planet (camera-facing, never cast shadows).
SKY_SPOTS = [(-0.4, 4.6, 2.6, 0.07), (1.0, 5.6, 3.1, 0.05), (2.8, 5.9, 3.3, 0.085), (4.9, 5.7, 2.4, 0.06),
             (5.6, 3.2, 2.3, 0.05), (-0.6, 2.6, 2.9, 0.05), (5.6, 2.2, 0.4, 0.045), (-0.7, 0.5, 0.2, 0.06),
             (0.3, 5.2, 0.9, 0.04), (4.3, 5.9, 1.0, 0.05)]
for k, (x, y, z, r_) in enumerate(SKY_SPOTS):
    facing_star(f"Sky_Star_{k}", (x, y, z), r_ * (1.4 if NIGHT else 1.0), STAR)
for k in range(max(0, min(3, SHOOTING_STARS))):
    head = Vector(((-0.2, 4.2, 3.6), (5.6, 4.9, 3.0), (5.2, 0.0, 0.6))[k])
    tail_dir = Vector(((-0.9, 0.5, 0.45), (0.9, -0.4, 0.55), (0.9, 0.3, 0.5))[k]).normalized()
    no_shadow(rod(f"Sky_Shooting_Star_{k}", head, head + tail_dir * 0.9, 0.02, mat("star", 0.3, emit=1.5 * GLOW,
                  alpha=0.7), r2=0.002, segs=10))
    facing_star(f"Sky_Shooting_Head_{k}", head, 0.06, STAR)


# =====================================================================
#  LIGHTS, WORLD, CAMERA, RENDER
# =====================================================================
# Sunset: a low warm sun from behind-left (rim light and long shadows), a rosy fill from the camera side,
# a violet glow from below the planet. Night: a cool moon from the front-left, a blue fill, lamps on full.
centre = Vector((PCX, PCY, -0.3))
if NIGHT:
    key_dir = Vector((0.35, 0.85, -0.75)).normalized()
    light("Light_Sun", "SUN", 1.1, kelvin(9500), centre - key_dir * 8, aim=centre, size=R(3))
    fill_e, fill_c, under_e = 260, lin(COLORS["fill"])[:3], 380
else:
    key_dir = Vector((1.0, 0.25, -0.36)).normalized()
    light("Light_Sun", "SUN", SUN_STRENGTH, kelvin(SUN_WARMTH), centre - key_dir * 8, aim=centre, size=R(2.5))
    fill_e, fill_c, under_e = 520, lin(COLORS["fill"])[:3], 300
cam_back = CAM_ROT.to_matrix().col[2]
light("Light_Fill", "AREA", fill_e, fill_c, centre + cam_back * 9 + Vector((0, 0, 2)), aim=centre, size=7)
light("Light_Under", "AREA", under_e, lin(COLORS["accent_3"])[:3], (PCX + 1.2, PCY - 1.2, -5.0),
      aim=(PCX, PCY, -1.6), size=5)
light("Light_Rim", "AREA", 260 if not NIGHT else 160, lin(COLORS["sun"])[:3], (PCX - 4.5, PCY + 4.5, 2.5),
      aim=(PCX, PCY, 0.5), size=4)
light("Light_Side", "AREA", 90 if not NIGHT else 45, kelvin(4800 if not NIGHT else 7000), (FX + 2.6, HY - 1.6, Z0 + 2.2),
      aim=(FX, HY, Z0 + 1.3), size=1.5)
light("Light_Window", "POINT", 6 * GLOW, kelvin(LAMP_WARMTH), (WX, FY - 0.35, WZ), size=0.2)
light("Light_Door", "POINT", 4 * GLOW, kelvin(LAMP_WARMTH), (DX, FY - 0.4, Z0 + 1.6), size=0.2)

# World: the camera sees a painted dusk sky (gradient, sun or moon glow, stars, milky way); everything else
# is lit by a soft ambient in the sky's middle colour.
world = bpy.data.worlds.get("RoomKit_World") or bpy.data.worlds.new("RoomKit_World")
scene.world = world
if bpy.app.version < (5, 0, 0):
    world.use_nodes = True
wn, wl = world.node_tree.nodes, world.node_tree.links
wn.clear()
out = wn.new("ShaderNodeOutputWorld")
aspect = RESOLUTION[0] / RESOLUTION[1]
tc = wn.new("ShaderNodeTexCoord")
sep = wn.new("ShaderNodeSeparateXYZ")
wl.new(tc.outputs["Window"], sep.inputs[0])


def wmath(op, a, b=None, value=None):
    n = wn.new("ShaderNodeMath")
    n.operation = op
    for i, src in enumerate((a, b)):
        if src is None:
            continue
        if isinstance(src, (int, float)):
            n.inputs[i].default_value = src
        else:
            wl.new(src, n.inputs[i])
    return n.outputs[0]


def wramp(src, stops):
    r = wn.new("ShaderNodeValToRGB")
    els = r.color_ramp.elements
    els[0].position, els[0].color = stops[0]
    els[1].position, els[1].color = stops[-1]
    for pos, col in stops[1:-1]:
        els.new(pos).color = col
    wl.new(src, r.inputs["Fac"])
    return r.outputs["Color"]


def wmix(a, b, fac=1.0, blend="ADD"):
    m_ = wn.new("ShaderNodeMix")
    m_.data_type, m_.blend_type = "RGBA", blend
    if isinstance(fac, (int, float)):
        m_.inputs["Factor"].default_value = fac
    else:
        wl.new(fac, m_.inputs["Factor"])
    wl.new(a, m_.inputs[6])
    wl.new(b, m_.inputs[7])
    return m_.outputs[2]


sx_n, sy_n = sep.outputs["X"], sep.outputs["Y"]
ax = wmath("MULTIPLY", sx_n, aspect)                     # x in the same units as y (round sun, round stars)
sky = wramp(sy_n, [(0.0, lin(COLORS["sky_low"])), (0.42, lin(COLORS["sky_mid"])), (1.0, lin(COLORS["sky_top"]))])
SUN_UV = (0.27, 0.36) if not NIGHT else (0.8, 0.8)
dist = wmath("SQRT", wmath("ADD", wmath("POWER", wmath("SUBTRACT", ax, SUN_UV[0] * aspect), 2),
                           wmath("POWER", wmath("SUBTRACT", sy_n, SUN_UV[1]), 2)))
sun_c = lin(COLORS["sun"])
halo = [(0.0, (sun_c[0] * 1.3, sun_c[1] * 1.25, sun_c[2] * 1.1, 1)), (0.062, (sun_c[0] * 1.15, sun_c[1] * 1.05, sun_c[2] * 0.9, 1)),
        (0.07, (sun_c[0] * 0.4, sun_c[1] * 0.3, sun_c[2] * 0.22, 1)), (0.4, (0, 0, 0, 1))]
if NIGHT:                                                # a soft moon glow high on the right
    halo = [(0.0, (0.95, 0.94, 1.0, 1)), (0.042, (0.88, 0.87, 0.95, 1)), (0.046, (0.09, 0.08, 0.16, 1)),
            (0.07, (0.03, 0.03, 0.06, 1)), (0.13, (0, 0, 0, 1)), (1.0, (0, 0, 0, 1))]
sky = wmix(sky, wramp(dist, halo))
if SKY_STARS or NIGHT:
    for scale_, thr, bright in ((70, 0.06, 1.0), (140, 0.045, 0.6)):
        vec = wn.new("ShaderNodeCombineXYZ")
        wl.new(ax, vec.inputs["X"])
        wl.new(sy_n, vec.inputs["Y"])
        vor = wn.new("ShaderNodeTexVoronoi")
        if hasattr(vor, "voronoi_dimensions"):
            vor.voronoi_dimensions = "2D"
        vor.inputs["Scale"].default_value = scale_
        wl.new(vec.outputs[0], vor.inputs["Vector"])
        dots = wramp(vor.outputs["Distance"], [(0.0, (bright * 2, bright * 2, bright * 1.8, 1)), (thr, (0, 0, 0, 1)),
                                               (1.0, (0, 0, 0, 1))])
        cell = wn.new("ShaderNodeRGBToBW")
        wl.new(vor.outputs["Color"], cell.inputs[0])
        keep = wmath("GREATER_THAN", cell.outputs[0], 0.45)
        mask = keep if NIGHT else wmath("MULTIPLY", keep, wmath("SMOOTH_MIN", 1.0, wmath("MULTIPLY", wmath(
            "SUBTRACT", sy_n, 0.55), 2.5), 0.1))
        sky = wmix(sky, dots, fac=wmath("MAXIMUM", wmath("MINIMUM", mask, 1.0), 0.0))
if NIGHT:                                                # milky way: a soft, mottled band across the sky
    band = wmath("ABSOLUTE", wmath("SUBTRACT", wmath("ADD", wmath("MULTIPLY", ax, 0.42), sy_n), 1.05))
    vec = wn.new("ShaderNodeCombineXYZ")
    wl.new(ax, vec.inputs["X"])
    wl.new(sy_n, vec.inputs["Y"])
    nz = wn.new("ShaderNodeTexNoise")
    nz.inputs["Scale"].default_value = 3.5
    nz.inputs["Detail"].default_value = 8.0
    wl.new(vec.outputs[0], nz.inputs["Vector"])
    glow = wmath("MULTIPLY", wmath("MAXIMUM", wmath("SUBTRACT", 1.0, wmath("MULTIPLY", band, 4.0)), 0.0),
                 nz.outputs["Fac"])
    mw = lin(COLORS["accent_3"])
    sky = wmix(sky, wramp(glow, [(0.0, (0, 0, 0, 1)), (0.35, (0, 0, 0, 1)), (0.75, (mw[0] * 0.5, mw[1] * 0.4,
                                                                                   mw[2] * 0.6, 1)), (1.0, (0.6, 0.5, 0.75, 1))]))
bg_cam = wn.new("ShaderNodeBackground")
wl.new(sky, bg_cam.inputs["Color"])
bg_cam.inputs["Strength"].default_value = 1.0
bg_amb = wn.new("ShaderNodeBackground")
bg_amb.inputs["Color"].default_value = lin(COLORS["sky_mid"])
bg_amb.inputs["Strength"].default_value = 0.4 if not NIGHT else 0.5
path = wn.new("ShaderNodeLightPath")
mix = wn.new("ShaderNodeMixShader")
wl.new(path.outputs["Is Camera Ray"], mix.inputs["Fac"])
wl.new(bg_amb.outputs[0], mix.inputs[1])
wl.new(bg_cam.outputs[0], mix.inputs[2])
wl.new(mix.outputs[0], out.inputs["Surface"])

# Orthographic camera framed on what you actually see (planet, observatory, moons, paper plane).
# kit_bounds is a box chosen so that, seen from this camera, it covers exactly that: a round planet's corner
# box would leave big empty corners. build_portfolio.py and the 3D web page frame the same box.
cam_data = bpy.data.cameras.new("Camera")
cam_data.type = "ORTHO"
cam = bpy.data.objects.new("Camera", cam_data)
scene.collection.objects.link(cam)
scene.camera = cam
cam.rotation_euler = CAM_ROT.copy()
rot = cam.rotation_euler.to_matrix()
right, up, back = rot.col[0], rot.col[1], rot.col[2]
bpy.context.view_layer.update()
xs, ys = [], []
for o in scene.objects:
    if o.type != "MESH" or o.hide_render or o.name.startswith(("Sky_", "Door_Cut", "Window_Cut")):
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
scene["kit_material_finish"] = json.dumps({"roughness": 0.6, "bevel": 0.005, "saturation": 0.75})
scene["kit_theme"] = THEME
scene["kit_bounds"] = BOUNDS            # the visible planet + sky objects, as seen by this camera
scene["kit_room_size"] = [W, D, H]      # the square the planet (and every slot) sits in, for check_room.py
scene["kit_furniture_colors"] = json.dumps(["main", "accent_1", "accent_2", "accent_3", "cream", "wood", "teak",
                                            "walnut", "brass", "plant", "dark"])   # colours add_furniture.py may use


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
