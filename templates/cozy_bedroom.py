"""
3D ROOM PORTFOLIO KIT  -  Template: COZY PASTEL BEDROOM
=======================================================
Builds a cosy isometric teen / student bedroom from scratch and renders a 1920x1080 image.
Every piece is modelled on a real product you can buy (see REFERENCES below), in a clean miniature style.

HOW TO RUN
  Option A (no Blender UI):   blender -b -P cozy_bedroom.py
  Option B (inside Blender):  Scripting tab > Open > cozy_bedroom.py > Run Script (then F12 to render)

You only need to edit the SETTINGS block below. Everything under it builds the room.
Output: output/cozy_bedroom.png and output/cozy_bedroom.blend next to this script.
"""

# REFERENCES  (what each piece is modelled on; names live only in comments, never in the scene)
#   bed         IKEA MALM bed frame high 140x200: 156x209 cm, headboard 100 cm, footboard 38 cm
#               https://www.ikea.com/ee/en/p/malm-bed-frame-high-black-brown-s49929229/
#   bedding     double duvet (folded-back cuff), 2x EU 50x60 pillows, chunky knit throw
#   side_table  IKEA HEMNES nightstand 46x35x70 cm, white-stained pine, drawer + knob + open shelf
#               https://www.dimensions.com/element/ikea-hemnes-nightstand
#   lamp        opal mushroom table lamp (Panthella Mini type) 25 cm dia. x 33.5 cm
#               https://www.skandium.com/en-kr/products/panthella-mini-table-lamp
#   desk        IKEA MICKE desk 105x50x75 cm, white paper foil, drawer column + cable outlet
#               https://www.ikea.com/gb/en/p/micke-desk-white-80213074/
#   chair       IKEA ODGER chair 45x51x81 cm, seat 43 cm, moulded shell, splayed legs
#               https://www.ikea.com/ie/en/p/odger-chair-white-beige-60359996
#   shelf       IKEA KALLAX 2x4 upright 77x39x147 cm + DRÖNA boxes 33x38x33 cm
#               https://www.ikea.com/lt/en/p/kallax-shelving-unit-black-brown-20275885/
#               https://www.ikea.com/au/en/p/droena-box-white-70262828/
#   desk lamp   IKEA TERTIAL work lamp, shade 17 cm dia., clamp, twin-rod spring arm
#               https://www.ikea.gr/en/products/tertial-work-lamp/20504288
#   laptop      13" thin laptop (MacBook Air class) 30.4x21.5x1.13 cm   https://support.apple.com/en-gb/126320
#   rug         IKEA LOHALS flatwoven jute rug 160x230 cm
#               https://www.ikea.com/nl/en/p/lohals-rug-flatwoven-natural-50277393/
#   curtains    IKEA RÄCKA rod + rings + floor-length pleated curtains   https://www.ikea.com/us/en/p/-s29929249
#   wall_art    2x IKEA RIBBA frame 50x70 hung landscape, white mount   https://www.ikea.com/my/en/p/ribba-frame-black-50301618
#   poster      wooden magnetic poster hanger, 60x40 cm print
#   name sign   felt letter board 60x45 cm in an oak frame (white push-in letters)
#   fairy       cotton-ball string lights, 6 cm balls   https://goodio.be/en/product/93300-ball-string-lights-10-m-100-leds-warm-white
#   pet         calming donut cat bed 50 cm dia.
#               https://www.petsmart.com/dog/beds-and-furniture/cuddler-beds/the-original-calming-donut-dog-and-cat-bed-84514.html
#   plant       Monstera deliciosa (~1.1 m) in a glazed pot with saucer, glossy leaves with pale midribs
#   pouf        chunky hand-knit cotton pouf 50 cm dia. x 36 cm (common high-street / Etsy item)
#   slippers    open-back plush mule slippers, 27 cm long
#   radiator    double steel panel radiator type 22, 600 x 500 mm (Stelrad / Purmo type), slotted top grille, TRV
#   shell       oak strip floor, plaster walls, skirting, 762x1981 mm door + architrave, casement window
#               (sill 0.90 m), panel radiator, light switch.   Full notes: research/cozy_bedroom.md

# =====================================================================
#  SETTINGS  -  change these lines, then run the script again
# =====================================================================
ROOM_NAME = "cozy_bedroom"          # used for the output file names

ROOM_WIDTH = 4.0                    # metres, left to right
ROOM_DEPTH = 4.0                    # metres, front to back
WALL_HEIGHT = 2.8                   # metres

THEME = "pastel"                    # pick one of the colour themes below
THEMES = {                          # any hex colour works; "main" is the room's hero colour (duvet)
    # extra keys: "pet" = the cat's fur, "jute" = the woven rug
    "pastel": {
        "background": "#F6E7E1", "wall": "#F6DDD5", "wall_trim": "#F3E6DD", "floor": "#DDBB92",
        "wood": "#CFA47A", "main": "#CDB8E8", "accent_1": "#F2B8C0", "accent_2": "#BFE3D0",
        "accent_3": "#F8E3A3", "cream": "#FBF7F1", "plant": "#5E9E6E", "dark": "#4E4049", "pet": "#E3A774",
        "jute": "#D8C6A2",
    },
    "coquette": {
        "background": "#F7E6E6", "wall": "#FAEAE8", "wall_trim": "#F7EDEA", "floor": "#E2C3A6",
        "wood": "#D3AA86", "main": "#EBB2BB", "accent_1": "#C8475A", "accent_2": "#F6D6DA",
        "accent_3": "#FFF1D6", "cream": "#FFF9F5", "plant": "#6F9E6C", "dark": "#5A3A40", "pet": "#EFE2D4",
        "jute": "#E0CFB2",
    },
    "cottagecore": {
        "background": "#EEF0E2", "wall": "#F1E9D6", "wall_trim": "#F4EEE0", "floor": "#C49E72",
        "wood": "#B4865A", "main": "#A8BF94", "accent_1": "#D99A9A", "accent_2": "#E9D9A6",
        "accent_3": "#C9B6D9", "cream": "#FBF6EA", "plant": "#5B8A4C", "dark": "#4F3F33", "pet": "#C9A27E",
        "jute": "#D3C19C",
    },
}

SUN_WARMTH = 4200                   # Kelvin: 2500 = sunset orange, 6500 = white daylight
SUN_STRENGTH = 3.0
LAMP_WARMTH = 2700                  # Kelvin of the bedside lamp and fairy lights
LAMP_STRENGTH = 20                  # Watts
FAIRY_LIGHTS = True                 # cotton-ball string lights over the bed
SEED = 4                            # change to shuffle books and small props

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

STYLE = "cozy_bedroom"
KIT_VERSION = 2
W, D, H = ROOM_WIDTH, ROOM_DEPTH, WALL_HEIGHT
T = 0.15            # wall thickness
FLOOR_Z = 0.03      # top of the floor planks; furniture stands here
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


def shade(hex_color, f):
    """Lighter (f > 1) or darker (f < 1) version of a hex colour, e.g. for plank-to-plank variation."""
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


def mat(key, rough=0.6, emit=0.0, metal=0.0, color=None, tag=""):
    """Material from a COLORS key (or a hex via color=). tag keeps textured variants apart."""
    hex_color = color or COLORS[key]
    name = f"M_{key}_{rough}_{emit}_{metal}_{hex_color}_{tag}"
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


SOFT = {"fabric": 0.45, "knit": 0.55, "plaster": 0.35}   # real paint and linen are calm, not cloudy/blotchy


def smat(key, kind, rough=0.6, metal=0.0, color=None, scale=1.0, along="X", strength=None):
    """Palette material with real surface detail (wood grain, weave, plaster...). See surface().
    strength < 1 softens the pattern (e.g. the faint grain of white-stained pine)."""
    strength = SOFT.get(kind, 1.0) if strength is None else strength
    m = surface(mat(key, rough, metal=metal, color=color, tag=f"{kind}_{scale}_{along}_{strength}"), kind, scale, along)
    for n in m.node_tree.nodes:
        if n.type == "MIX" and getattr(n, "blend_type", "") == "MULTIPLY":
            n.inputs["Factor"].default_value = strength
    return m


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
    """Box with small real-world bevels. size = (x, y, z) in metres, loc = centre."""
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=Vector(size), verts=bm.verts)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, min(bevel, min(size) * 0.45), coll, parent)


def multi_box(name, parts, material, bevel=0.002, coll=None, parent=None):
    """Many boxes in ONE object: parts = [(size, centre), ...]. Used for floor planks, keys, ribs."""
    bm = bmesh.new()
    for size, loc in parts:
        vs = bmesh.ops.create_cube(bm, size=1.0)["verts"]
        bmesh.ops.scale(bm, vec=Vector(size), verts=vs)
        bmesh.ops.translate(bm, vec=Vector(loc), verts=vs)
    return _finish(_obj(name, bm), material, bevel, coll, parent, segments=2)


def cyl(name, r, h, loc, material, r2=None, segs=32, bevel=0.002, rot=(0, 0, 0), coll=None, parent=None):
    """Cylinder (or cone with r2 at the top). loc = centre."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=segs, radius1=r, radius2=r if r2 is None else r2, depth=h)
    o = _obj(name, bm)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, bevel, coll, parent, segments=2)


def ball(name, r, loc, material, scale=(1, 1, 1), coll=None, parent=None, rot=(0, 0, 0)):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=24, v_segments=14, radius=r)
    o = _obj(name, bm)
    o.location, o.scale, o.rotation_euler = loc, scale, rot
    return _finish(o, material, 0, coll, parent)


def rod(name, a, b, r, material, r2=None, segs=12, parent=None):
    """Cylinder from point a to point b (radius r at a, r2 at b)."""
    a, b = Vector(a), Vector(b)
    o = cyl(name, r, (b - a).length, (a + b) / 2, material, r2=r2, segs=segs, bevel=0, parent=parent)
    o.rotation_euler = (b - a).to_track_quat("Z", "Y").to_euler()
    return o


def mesh_obj(name, verts, faces, material, loc=(0, 0, 0), rot=(0, 0, 0), parent=None, coll=None, weld=False):
    me = bpy.data.meshes.new(name)
    me.from_pydata(verts, [], faces)
    if weld:                                    # merge the duplicate points of lathe / pillow meshes
        bm = bmesh.new()
        bm.from_mesh(me)
        bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-6)
        bm.to_mesh(me)
        bm.free()
    me.update()
    o = bpy.data.objects.new(name, me)
    o.location, o.rotation_euler = loc, rot
    return _finish(o, material, 0, coll, parent)


def solidify(o, thick, offset=-1.0):
    m = o.modifiers.new("Solidify", "SOLIDIFY")
    m.thickness, m.offset = thick, offset
    m.use_even_offset = True
    return o


def subsurf(o, levels=1):
    m = o.modifiers.new("Subsurf", "SUBSURF")
    m.levels = m.render_levels = levels
    return o


def lathe(name, profile, loc, material, parent=None, segs=40, rot=(0, 0, 0)):
    """Surface of revolution (pots, mugs, lamp parts). profile = [(radius, z), ...] from bottom to top."""
    n = len(profile)
    verts = [(r_ * math.cos(2 * math.pi * i / segs), r_ * math.sin(2 * math.pi * i / segs), z)
             for i in range(segs) for r_, z in profile]
    faces = [(i * n + k, i * n + k + 1, ((i + 1) % segs) * n + k + 1, ((i + 1) % segs) * n + k)
             for i in range(segs) for k in range(n - 1)]
    return mesh_obj(name, verts, faces, material, loc, rot, parent, weld=True)


def torus(name, ring_r, tube_r, loc, material, parent=None, seg=40, tseg=14, zscale=1.0, rot=(0, 0, 0)):
    verts = []
    for i in range(seg):
        a = 2 * math.pi * i / seg
        for j in range(tseg):
            b = 2 * math.pi * j / tseg
            rr = ring_r + tube_r * math.cos(b)
            verts.append((rr * math.cos(a), rr * math.sin(a), tube_r * math.sin(b) * zscale))
    faces = [(i * tseg + j, ((i + 1) % seg) * tseg + j, ((i + 1) % seg) * tseg + (j + 1) % tseg, i * tseg + (j + 1) % tseg)
             for i in range(seg) for j in range(tseg)]
    return mesh_obj(name, verts, faces, material, loc, rot, parent)


def tube(name, pts, r, material, parent=None):
    """Smooth round cable / stem / tail through the given points (a bevelled Bezier curve)."""
    cu = bpy.data.curves.new(name, "CURVE")
    cu.dimensions = "3D"
    cu.bevel_depth, cu.bevel_resolution = r, 3
    cu.use_fill_caps = True
    sp = cu.splines.new("BEZIER")
    sp.bezier_points.add(len(pts) - 1)
    for bp, p in zip(sp.bezier_points, pts):
        bp.co = p
        bp.handle_left_type = bp.handle_right_type = "AUTO"
    o = bpy.data.objects.new(name, cu)
    o.data.materials.append(material)
    COL_ROOM.objects.link(o)
    o.parent = parent
    return o


def flat(name, pts, loc, material, parent=None, rot=(0, 0, 0)):
    """Flat shape in the XZ plane facing -Y (prints, posters). pts = [(x, z), ...]."""
    return mesh_obj(name, [(x, 0, z) for x, z in pts], [list(range(len(pts)))], material, loc, rot, parent)


def arch(name, r_in, r_out, loc, material, parent=None, segs=24):
    """Half-ring (rainbow arch) in the XZ plane facing -Y."""
    verts, faces = [], []
    for i in range(segs + 1):
        a = math.pi * i / segs
        verts += [(r_out * math.cos(a), 0, r_out * math.sin(a)), (r_in * math.cos(a), 0, r_in * math.sin(a))]
        if i:
            faces.append((2 * i - 2, 2 * i - 1, 2 * i + 1, 2 * i))
    return mesh_obj(name, verts, faces, material, loc, (0, 0, 0), parent)


def puffy(name, sx, sy, thick, loc, material, rot=(0, 0, 0), parent=None, n=14, waist=0.06):
    """Pillow / cushion: two bulging faces sewn together at a pinched seam (sx, sy = flat size)."""
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


def drape(name, half_w, y0, y1, top, hang, material, parent, r=0.06, foot_hang=0.0, rf=None, thick=0.035,
          nx=48, ny=40, wrinkle=0.008, seed=1, puff=0.016, ribs=0.0, rib_w=0.036):
    """Duvet / throw lying on a mattress: flat on top, rolling over the side edges (radius r) and hanging
    down `hang` metres with soft folds. foot_hang > 0 also drapes it over the foot end at y0.
    puff = how much the filling domes up on top; ribs > 0 adds chunky knitted rib columns (rib_w apart)."""
    rnd = random.Random(seed)
    ph = [rnd.uniform(0, 6.283) for _ in range(6)]
    rf = rf or r

    def wrap(s, a, rr):
        sa, sg = abs(s), (1 if s >= 0 else -1)
        if sa <= a:
            return s, 0.0
        arc = math.pi * rr / 2
        if sa <= a + arc:
            phi = (sa - a) / rr
            return sg * (a + rr * math.sin(phi)), rr * (1 - math.cos(phi))
        return sg * (a + rr), rr + (sa - a - arc)

    S = half_w + math.pi * r / 2 + hang
    F = (math.pi * rf / 2 + foot_hang) if foot_hang > 0 else 0.0
    verts = []
    for j in range(ny + 1):
        t = -F + (y1 - y0 + F) * j / ny                # t < 0: the part rolling over the foot edge
        if t >= 0:
            y, dzy, foot = y0 + t, 0.0, 0.0
        else:
            off, dzy = wrap(t, 0.0, rf)
            y, foot = y0 + off, -t / F
        for i in range(nx + 1):
            s = -S + 2 * S * i / nx
            x, dzx = wrap(s, half_w, r)
            yc, drop = y, dzx + dzy
            hx, hy = abs(s) - half_w, -t
            if hx > 0 and hy > 0:                       # corner: the cloth fans round into a soft diagonal droop
                th = math.atan2(hy, hx)
                horiz, drop = wrap(max(hx, hy), 0.0, r * math.cos(th) ** 2 + rf * math.sin(th) ** 2)
                x = math.copysign(half_w + horiz * math.cos(th), s)
                yc = y0 - horiz * math.sin(th)
            side = max(0.0, (abs(s) - half_w) / (S - half_w))
            if side:                                    # vertical folds on the hanging sides
                out = side * max(0.0, 0.024 + 0.018 * math.sin(y * 11 + ph[0]) + 0.012 * math.sin(y * 27 + ph[1]))
                x += math.copysign(out, s)
            yy = yc - foot * max(0.0, 0.012 + 0.012 * math.sin(x * 13 + ph[4]))
            on_top = max(0.0, 1 - 3 * max(side, foot))
            dome = max(0.0, 1 - min(1.0, abs(x) / half_w) ** 6) ** 0.5       # flat-topped, rounded at the edge
            pf = puff * dome * on_top
            wr = wrinkle * on_top * math.sin(x * 6 + y * 2.5 + ph[2]) * math.sin(y * 4.3 - x * 1.7 + ph[3])
            p = Vector((x, yy, max(0.012, top - drop + pf + wr)))
            if ribs:                            # knitted rib columns, pushed out along the cloth's (analytic) normal
                px = min(math.pi / 2, max(0.0, abs(s) - half_w) / r)
                py = min(math.pi / 2, max(0.0, -t) / rf) if t < 0 else 0.0
                n_ = Vector((math.copysign(math.sin(px), s), -math.sin(py), math.cos(px) * math.cos(py))).normalized()
                p += n_ * ribs * abs(math.sin(math.pi * s / rib_w))
            verts.append(tuple(p))
    faces = [(j * (nx + 1) + i, j * (nx + 1) + i + 1, (j + 1) * (nx + 1) + i + 1, (j + 1) * (nx + 1) + i)
             for j in range(ny) for i in range(nx)]
    return subsurf(solidify(mesh_obj(name, verts, faces, material, parent=parent), thick), 1)


def curtain(name, width, height, folds, depth, loc, material, parent=None):
    """Floor-length pleated curtain hanging in the YZ plane (left wall); pleats stick out along +X."""
    ny, nz = folds * 8, 10
    verts = []
    for k in range(nz + 1):
        z = -height * k / nz
        for j in range(ny + 1):
            y = (j / ny - 0.5) * width * (1 + 0.12 * k / nz)
            x = depth * 0.5 * (1 - math.cos(2 * math.pi * folds * j / ny)) * (0.85 + 0.15 * k / nz)
            verts.append((x, y, z))
    faces = [(k * (ny + 1) + j, k * (ny + 1) + j + 1, (k + 1) * (ny + 1) + j + 1, (k + 1) * (ny + 1) + j)
             for k in range(nz) for j in range(ny)]
    return subsurf(solidify(mesh_obj(name, verts, faces, material, loc, parent=parent), 0.005, 0.0), 1)


def monstera_leaf(name, length, width, loc, rot, material, parent=None, slits=4, droop=0.2, rib_material=None):
    """Split heart-shaped leaf. Built in the XY plane (base at the origin, tip along +Y), then droops."""
    cx, cy = 0.0, 0.45 * length
    cuts = [side * (0.75 + k * 1.9 / slits) for side in (-1, 1) for k in range(slits)]
    outline = []
    for k in range(320):
        th = -math.pi + 2 * math.pi * (k + 0.5) / 320
        x = 0.5 * width * math.sin(th)
        y = 0.5 * length * (1 - math.cos(th)) + 0.13 * length * math.exp(-(th / 0.32) ** 2)   # heart notch
        if any(abs(th - c) < 0.022 for c in cuts):                                           # slit toward the rib
            x, y = cx + (x - cx) * 0.42, cy + (y - cy) * 0.42
        outline.append((x, y))
    verts = [(cx, cy, 0.0)] + [(x, y, 0.0) for x, y in outline]
    for i, (x, y, _) in enumerate(verts):
        verts[i] = (x, y, -droop * length * (y / length) ** 2 + 0.25 * width * (x / width) ** 2)
    faces = [(0, i, i % 320 + 1) for i in range(1, 321)]
    leaf = mesh_obj(name, verts, faces, material, loc, rot, parent)
    if rib_material is not None:                    # pale midrib running from the stem to the tip
        rib = []
        for k in range(9):
            y = 0.08 * length + 0.82 * length * k / 8
            half = 0.006 * (1 - 0.6 * k / 8)
            z = -droop * length * (y / length) ** 2 + 0.0015
            rib += [(-half, y, z), (half, y, z)]
        mesh_obj(name + "_Midrib", rib, [(2 * k, 2 * k + 1, 2 * k + 3, 2 * k + 2) for k in range(8)], rib_material,
                 loc, rot, parent)
    return leaf


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
    e["kit_kind"] = kind            # floor / wall / surface / rug
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


# --------------------------------------------------------------------- shared real-world materials
PAINT = smat("wall_trim", "plaster", 0.45, scale=3)                      # painted woodwork: skirting, door, architrave
WHITE_FOIL = smat("cream", "paper", 0.45, scale=4, strength=0.5)                       # white flat-pack (paper foil) furniture
WHITE_PINE = smat("cream", "wood", 0.55, scale=6, along="Z", strength=0.35)                        # white-stained solid pine
PINE_FLAT = smat("cream", "wood", 0.55, scale=6, along="X", strength=0.35)       # same pine, grain along tops/fronts
OAK = smat("wood", "wood", 0.5, scale=3, strength=0.7)                                 # solid oak / oak frames
OAK_VENEER = smat("wood", "veneer", 0.45, scale=8, strength=0.45)       # oak veneer panels: fine, straight grain
OAK_VENEER_Y = smat("wood", "veneer", 0.45, scale=8, along="Y", strength=0.45)   # same veneer on parts running along Y
STEEL = smat("steel", "brushed", 0.3, metal=1.0, color="#B9BCC0")
ALU = smat("alu", "brushed", 0.35, metal=1.0, color="#CDCFD3")
GLASS_SKY = mat("sky", 0.1, emit=0.6, color="#DDEFFF")
DARK = mat("dark", 0.5)
BLACK = mat("black", 0.35, color="#1E1D21")

# =====================================================================
#  ROOM SHELL
# =====================================================================
WIN_Y = (1.25, 2.43)                # window opening in the left wall, front to back
WIN_Z = (0.90, 2.12)                # sill at 0.90 m (real sill height 0.8-0.9 m)
wy, wz = sum(WIN_Y) / 2, sum(WIN_Z) / 2
ww, wh = WIN_Y[1] - WIN_Y[0], WIN_Z[1] - WIN_Z[0]
DOOR_X = 1.30                       # centre of the 762 x 1981 mm internal door in the back wall
DOOR_W, DOOR_H = 0.762, 1.981

# Floor: base slab + oak strip planks (19 cm wide, staggered joints, three slightly different tones).
box("Floor_Base", (W + T, D + T, 0.2), ((W - T) / 2, (D + T) / 2, -0.1),
    mat("wood", 0.7, color=shade(COLORS["floor"], 0.78)), bevel=0.01)
rows = round(W / 0.19)
pw = W / rows
fr = random.Random(7)                           # fixed: the floor does not change with SEED
tones = {k: [] for k in range(3)}
for i in range(rows):
    y = -fr.uniform(0.2, 1.4)
    while y < D:
        length = fr.uniform(0.9, 1.9)
        y0, y1 = max(0.0, y), min(D, y + length)
        if y1 - y0 > 0.05:
            tones[fr.randrange(3)].append(((pw - 0.003, y1 - y0 - 0.003, FLOOR_Z), (pw * (i + 0.5), (y0 + y1) / 2, FLOOR_Z / 2)))
        y += length
for k, parts in tones.items():
    multi_box(f"Floor_Planks_{k}", parts, smat("floor", "wood", 0.5 + 0.04 * k,
              color=shade(COLORS["floor"], (1.0, 0.93, 1.05)[k]), scale=5, along="Y", strength=0.6), bevel=0.0015)

# Walls (painted plaster) with a window opening (left) and a door opening (back).
WALL = smat("wall", "plaster", 0.9, scale=2.5)
left = box("Wall_Left", (T, D + T, H), (-T / 2, (D + T) / 2, H / 2), WALL, bevel=0.0)
back = box("Wall_Back", (W + T, T, H), ((W - T) / 2, D + T / 2, H / 2), WALL, bevel=0.0)
for wall, nm, size, loc in ((left, "Window", (T * 3, ww, wh), (-T / 2, wy, wz)),
                            (back, "Door", (0.80, T * 3, DOOR_H + 0.02), (DOOR_X, D + T / 2, FLOOR_Z + (DOOR_H + 0.02) / 2))):
    cutter = box(f"{nm}_Cutter", size, loc, WALL, bevel=0.0)
    cutter.hide_render = cutter.hide_viewport = True
    boolean = wall.modifiers.new(nm, "BOOLEAN")
    boolean.operation, boolean.object = "DIFFERENCE", cutter
    bev = wall.modifiers.new("Bevel", "BEVEL")
    bev.width, bev.segments, bev.limit_method = 0.006, 2, "ANGLE"

# Diorama cap on top of the walls (the kit's miniature look).
box("Trim_Top_Back", (W + T + 0.04, T + 0.05, 0.08), ((W - T) / 2, D + T / 2, H + 0.04), OAK_VENEER, bevel=0.01)
box("Trim_Top_Left", (T + 0.05, D + T + 0.04, 0.08), (-T / 2, (D + T) / 2 - 0.02, H + 0.04), OAK_VENEER_Y, bevel=0.01)

# Skirting boards (100 mm, painted), split around the door.
for nm, x0, x1 in (("A", 0.0, DOOR_X - 0.47), ("B", DOOR_X + 0.47, W)):
    box(f"Skirting_Back_{nm}", (x1 - x0, 0.018, 0.10), ((x0 + x1) / 2, D - 0.009, FLOOR_Z + 0.05), PAINT, bevel=0.004)
box("Skirting_Left", (0.018, D, 0.10), (0.009, D / 2, FLOOR_Z + 0.05), PAINT, bevel=0.004)

# Internal door: linings, a two-panel painted leaf, lever handle on a round rose, architrave.
for sx in (-1, 1):
    box("Door_Lining", (0.019, T, DOOR_H + 0.02), (DOOR_X + sx * 0.3905, D + T / 2, FLOOR_Z + (DOOR_H + 0.02) / 2), PAINT, bevel=0.002)
    box("Door_Architrave", (0.07, 0.018, DOOR_H + 0.09), (DOOR_X + sx * 0.435, D - 0.009, FLOOR_Z + (DOOR_H + 0.09) / 2), PAINT)
box("Door_Lining_Head", (0.80, T, 0.019), (DOOR_X, D + T / 2, FLOOR_Z + DOOR_H + 0.0105), PAINT, bevel=0.002)
box("Door_Architrave_Head", (0.94, 0.018, 0.07), (DOOR_X, D - 0.009, FLOOR_Z + DOOR_H + 0.055), PAINT)
box("Door_Leaf", (DOOR_W, 0.035, DOOR_H), (DOOR_X, D + 0.0475, FLOOR_Z + 0.003 + DOOR_H / 2), PAINT, bevel=0.003)
mould = []
for pz, ph_ in ((FLOOR_Z + 1.42, 0.86), (FLOOR_Z + 0.52, 0.62)):        # two moulded panels
    for dx, dz, sx_, sz_ in ((0, ph_ / 2, 0.52, 0.022), (0, -ph_ / 2, 0.52, 0.022),
                             (0.26, 0, 0.022, ph_), (-0.26, 0, 0.022, ph_)):
        mould.append(((sx_, 0.008, sz_), (DOOR_X + dx, D + 0.027, pz + dz)))
multi_box("Door_Mouldings", mould, PAINT, bevel=0.003)
hx = DOOR_X + DOOR_W / 2 - 0.065
cyl("Door_Rose", 0.026, 0.01, (hx, D + 0.025, FLOOR_Z + 1.0), STEEL, rot=(R(90), 0, 0))
cyl("Door_Handle_Neck", 0.008, 0.05, (hx, D + 0.005, FLOOR_Z + 1.0), STEEL, rot=(R(90), 0, 0))
box("Door_Handle_Lever", (0.12, 0.018, 0.018), (hx - 0.055, D - 0.02, FLOOR_Z + 1.0), STEEL, bevel=0.007)
box("Light_Switch", (0.086, 0.008, 0.086), (DOOR_X + 0.53, D - 0.004, 1.2), mat("cream", 0.35))
box("Light_Switch_Rocker", (0.028, 0.006, 0.045), (DOOR_X + 0.53, D - 0.01, 1.2), mat("cream", 0.35), bevel=0.003)

# Casement window (white frame, two sashes with handles), window board and sky glass.
WFRAME = smat("cream", "plaster", 0.35, scale=0.5)
for nm, size, loc in [
    ("Top", (0.07, ww, 0.06), (-0.06, wy, WIN_Z[1] - 0.03)),
    ("Bottom", (0.07, ww, 0.06), (-0.06, wy, WIN_Z[0] + 0.03)),
    ("Front", (0.07, 0.06, wh), (-0.06, WIN_Y[0] + 0.03, wz)),
    ("Back", (0.07, 0.06, wh), (-0.06, WIN_Y[1] - 0.03, wz)),
    ("Mullion", (0.07, 0.07, wh), (-0.06, wy, wz)),
]:
    box(f"Window_Frame_{nm}", size, loc, WFRAME, bevel=0.004)
for k, (ya, yb) in enumerate(((WIN_Y[0] + 0.06, wy - 0.035), (wy + 0.035, WIN_Y[1] - 0.06))):
    za, zb = WIN_Z[0] + 0.06, WIN_Z[1] - 0.06
    sy_, sz_ = (ya + yb) / 2, (za + zb) / 2
    for nm, size, loc in (("T", (0.05, yb - ya, 0.05), (-0.03, sy_, zb - 0.025)),
                          ("B", (0.05, yb - ya, 0.06), (-0.03, sy_, za + 0.03)),
                          ("F", (0.05, 0.05, zb - za), (-0.03, ya + 0.025, sz_)),
                          ("K", (0.05, 0.05, zb - za), (-0.03, yb - 0.025, sz_))):
        box(f"Window_Sash_{k}{nm}", size, loc, WFRAME, bevel=0.004)
    hy = yb - 0.025 if k == 0 else ya + 0.025
    box(f"Window_Handle_Base_{k}", (0.012, 0.028, 0.065), (-0.0, hy, sz_), WFRAME, bevel=0.003)
    box(f"Window_Handle_{k}", (0.016, 0.016, 0.10), (0.01, hy, sz_ - 0.04), WFRAME, bevel=0.006)
    glass = box(f"Window_Glass_{k}", (0.006, yb - ya - 0.08, zb - za - 0.09), (-0.035, sy_, sz_ + 0.005), GLASS_SKY, bevel=0)
    if hasattr(glass, "visible_shadow"):
        glass.visible_shadow = False
box("Window_Board", (0.17, ww + 0.10, 0.025), (-0.045, wy, WIN_Z[0] - 0.0125), PAINT, bevel=0.004)

# Curtain rod on brackets with ball finials, rings and two floor-length pleated curtains.
rod_z, rod_x, rod_len = WIN_Z[1] + 0.18, 0.10, ww + 0.62
cyl("Curtain_Rod", 0.013, rod_len, (rod_x, wy, rod_z), STEEL, rot=(R(90), 0, 0), segs=20)
for sy in (-1, 1):
    ball("Curtain_Finial", 0.024, (rod_x, wy + sy * (rod_len / 2 + 0.02), rod_z), STEEL)
for by in (wy - rod_len / 2 + 0.08, wy + rod_len / 2 - 0.08):
    box("Curtain_Bracket", (rod_x, 0.018, 0.03), (rod_x / 2, by, rod_z + 0.005), STEEL, bevel=0.004)
CURTAIN = smat("accent_2", "fabric", 0.9)
for side, yc in (("Front", wy - rod_len / 2 + 0.19), ("Back", wy + rod_len / 2 - 0.19)):
    curtain(f"Curtain_{side}", 0.32, rod_z - 0.03 - FLOOR_Z - 0.015, 4, 0.075, (0.055, yc, rod_z - 0.03), CURTAIN)
    for k in range(9):
        torus("Curtain_Ring", 0.019, 0.0035, (rod_x, yc - 0.16 + k * 0.04, rod_z), STEEL, seg=16, tseg=6,
              rot=(R(90), 0, 0))

# Double steel panel radiator (type 22, 600 x 500 mm), smooth white stove enamel: fluted front panel, slotted top
# grille, side caps, wall brackets, a thermostatic valve and pipe. (Painted steel is calm, so the glaze is faint.)
RAD = smat("cream", "ceramic", 0.28, strength=0.2)
ry, rz = 3.15, FLOOR_Z + 0.13
box("Radiator_Body", (0.07, 0.6, 0.5), (0.085, ry, rz + 0.25), RAD, bevel=0.004)
multi_box("Radiator_Flutes", [((0.006, 0.026, 0.47), (0.121, ry - 0.2775 + k * 0.037, rz + 0.25)) for k in range(16)],
          RAD, bevel=0.003)
multi_box("Radiator_Side_Caps", [((0.10, 0.008, 0.5), (0.085, ry + sy * 0.304, rz + 0.25)) for sy in (-1, 1)], RAD)
box("Radiator_Grille_Gap", (0.09, 0.59, 0.004), (0.085, ry, rz + 0.499), mat("cream", 0.6, color=shade(COLORS["cream"], 0.5)),
    bevel=0)                                                                 # the convector fins seen through the grille
multi_box("Radiator_Grille", [((0.088, 0.006, 0.006), (0.085, ry - 0.28 + k * 0.02, rz + 0.502)) for k in range(29)], RAD,
          bevel=0.001)
for by in (ry - 0.2, ry + 0.2):
    box("Radiator_Bracket", (0.04, 0.03, 0.05), (0.035, by, rz + 0.42), DARK, bevel=0.003)
cyl("Radiator_Valve", 0.02, 0.05, (0.085, ry + 0.33, rz - 0.005), mat("cream", 0.3), bevel=0.003)
cyl("Radiator_Valve_Head", 0.026, 0.07, (0.085, ry + 0.33, rz + 0.06), mat("cream", 0.3), bevel=0.006)
cyl("Radiator_Pipe", 0.008, rz - 0.03 - FLOOR_Z, (0.085, ry + 0.33, (rz - 0.03 + FLOOR_Z) / 2), STEEL)

# Cotton-ball fairy lights draped in two swags over the bed, cable running down to the socket.
if FAIRY_LIGHTS:
    anchors = [(1.95, 2.30), (2.93, 2.32), (3.90, 2.30)]
    fy = D - 0.03
    wire_pts, k = [], 0
    for (xa, za), (xb, zb) in zip(anchors, anchors[1:]):
        n = 8
        for i in range(n + (1 if xb == anchors[-1][0] else 0)):
            u = i / n
            x, z = xa + (xb - xa) * u, za + (zb - za) * u - 0.24 * math.sin(math.pi * u)
            wire_pts.append(Vector((x, fy, z)))
            if 0 < i:
                key = ("cream", "accent_1", "accent_2", "accent_3")[k % 4]
                ball("Fairy_Cotton_Ball", 0.03, (x, fy - 0.012, z - 0.028), mat(key, 0.9, emit=0.9, tag="cotton"))
                k += 1
    for xa, za in anchors:
        cyl("Fairy_Nail", 0.004, 0.02, (xa, D - 0.01, za + 0.005), STEEL, rot=(R(90), 0, 0))
    wire_pts += [Vector((3.95, fy, 2.0)), Vector((3.955, fy, 1.2)), Vector((3.955, fy, 0.42)), Vector((3.955, fy + 0.012, 0.36))]
    tube("Fairy_Cable", wire_pts, 0.0025, mat("cream", 0.5))
    box("Wall_Socket", (0.086, 0.01, 0.086), (3.955, D - 0.005, 0.32), mat("cream", 0.35))      # UK/EU single socket
    box("Wall_Socket_Plug", (0.04, 0.025, 0.045), (3.955, D - 0.018, 0.325), mat("cream", 0.4), bevel=0.006)

# =====================================================================
#  FURNITURE SLOTS  (same names in every template)
#  size = (width, depth, height) in real metres; front of the furniture faces local -Y
# =====================================================================
BED_X = 2.64
slot("bed",        (1.56, 2.09, 1.0),  (BED_X, D - 0.02 - 1.045), shape="bed")                 # MALM 140x200
slot("side_table", (0.46, 0.35, 0.70), (BED_X + 0.78 + 0.04 + 0.23, D - 0.02 - 0.175), shape="cabinet")   # HEMNES
slot("lamp",       (0.26, 0.26, 0.34), (BED_X + 0.78 + 0.04 + 0.23, D - 0.02 - 0.175), z=FLOOR_Z + 0.70,
     kind="surface", shape="lamp")                                                                 # mushroom lamp
slot("desk",       (1.05, 0.50, 0.75), (0.27, wy), turn=90, shape="table")                          # MICKE
slot("chair",      (0.45, 0.51, 0.81), (0.80, wy - 0.04), turn=-90, shape="chair")                  # ODGER
slot("shelf",      (0.77, 0.39, 1.47), (0.025 + 0.385, D - 0.02 - 0.195), shape="shelf")           # KALLAX 2x4
slot("plant",      (0.50, 0.50, 1.15), (0.32, 0.42), shape="plant")                                 # monstera
slot("rug",        (2.30, 1.60, 0.012), (2.45, 1.40), kind="rug", shape="rug")                      # LOHALS
slot("wall_art",   (1.52, 0.05, 0.52), (BED_X, D - 0.025), z=1.27, kind="wall", shape="frame")     # 2x RIBBA
slot("pet",        (0.50, 0.50, 0.30), (0.98, 0.78), turn=20, shape="pet")                          # donut cat bed


# =====================================================================
#  PLACEHOLDER FURNITURE  (replaced when you add your own with add_furniture.py)
# =====================================================================
def build_bed():
    """MALM high bed frame 140x200: slab headboard/footboard as legs, side rails with a gap below."""
    root, w, d, h = furniture_root("bed")
    box("Bed_Headboard", (w, 0.05, h), (0, d / 2 - 0.025, h / 2), OAK_VENEER, parent=root)
    box("Bed_Footboard", (w, 0.04, 0.38), (0, -d / 2 + 0.02, 0.19), OAK_VENEER, parent=root)
    for sx in (-1, 1):
        box("Bed_Side_Rail", (0.03, d - 0.09, 0.21), (sx * (w / 2 - 0.03), -0.005, 0.275), OAK_VENEER_Y, parent=root)
    box("Bed_Slat_Shadow", (w - 0.12, d - 0.1, 0.02), (0, -0.005, 0.20), DARK, bevel=0, parent=root)
    mattress_top = 0.48
    box("Bed_Mattress", (1.42, 1.99, 0.18), (0, -0.005, mattress_top - 0.09), smat("cream", "fabric", 0.9),
        bevel=0.03, parent=root)
    foot = -0.995
    duvet_top = mattress_top + 0.037
    puff = 0.045                                        # a 10.5 tog duvet domes up ~4-5 cm over the mattress
    drape("Bed_Duvet", 0.71, foot, 0.40, duvet_top, 0.20, smat("main", "fabric", 0.9), root,
          r=0.075, foot_hang=0.05, thick=0.04, seed=SEED, puff=puff)
    drape("Bed_Duvet_Cuff", 0.71, 0.16, 0.43, duvet_top + 0.03, 0.15, smat("cream", "fabric", 0.85), root,
          r=0.075 + 0.035, foot_hang=0.012, rf=0.022, thick=0.03, ny=16, wrinkle=0.004, seed=SEED + 1,
          puff=puff + 0.006)
    drape("Bed_Throw", 0.71, foot, foot + 0.50, duvet_top + 0.03, 0.30, smat("accent_1", "knit", 0.95, scale=0.6),
          root, r=0.075 + 0.05, foot_hang=0.10, rf=0.09, thick=0.024, nx=260, ny=28, wrinkle=0.006, seed=SEED + 2,
          puff=puff + 0.004, ribs=0.006)
    for sx in (-1, 1):                                  # two 50x60 pillows leaning on the headboard
        puffy("Bed_Pillow", 0.62, 0.48, 0.16, (sx * 0.36, 0.71, mattress_top + 0.12), smat("cream", "fabric", 0.85),
              rot=(R(24), 0, R(sx * 3)), parent=root)
    puffy("Bed_Cushion", 0.42, 0.42, 0.13, (0.18, 0.50, mattress_top + 0.21), smat("accent_2", "knit", 0.9),
          rot=(R(68), 0, R(-10)), parent=root)


def build_side_table():
    """HEMNES nightstand: white-stained pine, square legs, drawer with a wooden knob, open shelf."""
    root, w, d, h = furniture_root("side_table")
    box("SideTable_Top", (w, d, 0.022), (0, 0, h - 0.011), PINE_FLAT, parent=root)
    lx, ly = w / 2 - 0.03, d / 2 - 0.03
    for sx in (-1, 1):
        for sy in (-1, 1):
            box("SideTable_Leg", (0.04, 0.04, h - 0.022), (sx * lx, sy * ly, (h - 0.022) / 2), WHITE_PINE, parent=root)
        box("SideTable_Side", (0.014, d - 0.1, h - 0.15), (sx * lx, 0, 0.12 + (h - 0.15) / 2 - 0.0), WHITE_PINE,
            bevel=0.002, parent=root)
    box("SideTable_Back", (2 * lx, 0.01, h - 0.15), (0, ly + 0.01, 0.12 + (h - 0.15) / 2), WHITE_PINE, parent=root)
    fy = -ly - 0.016
    box("SideTable_Drawer", (2 * lx - 0.046, 0.018, 0.125), (0, fy, h - 0.022 - 0.004 - 0.0625), PINE_FLAT,
        bevel=0.003, parent=root)
    box("SideTable_Drawer_Shadow", (2 * lx - 0.04, 0.012, 0.131), (0, fy + 0.006, h - 0.022 - 0.004 - 0.0625), DARK,
        bevel=0, parent=root)
    kz = h - 0.022 - 0.004 - 0.0625
    cyl("SideTable_Knob_Stem", 0.007, 0.016, (0, fy - 0.017, kz), WHITE_PINE, rot=(R(90), 0, 0), parent=root)
    ball("SideTable_Knob", 0.017, (0, fy - 0.03, kz), WHITE_PINE, scale=(1, 0.75, 1), parent=root)
    box("SideTable_Rail", (2 * lx - 0.04, 0.02, 0.022), (0, fy + 0.002, kz - 0.075), PINE_FLAT, parent=root)
    box("SideTable_Shelf", (2 * lx - 0.04, d - 0.08, 0.016), (0, 0, 0.33), PINE_FLAT, parent=root)
    box("SideTable_Bottom", (2 * lx - 0.04, d - 0.08, 0.018), (0, 0, 0.12), PINE_FLAT, parent=root)
    box("SideTable_Apron", (2 * lx - 0.04, 0.018, 0.05), (0, fy + 0.002, 0.085), PINE_FLAT, parent=root)
    for i, (key, th, bh) in enumerate((("accent_3", 0.03, 0.22), ("main", 0.025, 0.2), ("dark", 0.035, 0.23))):
        box("SideTable_Book", (bh, 0.15, th), (-0.02 + i * 0.01, 0.0, 0.338 + 0.03 * i + th / 2), mat(key, 0.7),
            bevel=0.003, rot=(0, 0, R(i * 6 - 4)), parent=root)


def build_lamp():
    """Opal mushroom table lamp: round base, flared trumpet stem, glowing dome shade."""
    root, w, d, h = furniture_root("lamp")
    body = smat("accent_1", "ceramic", 0.3)
    lathe("Lamp_Base_Stem", [(0, 0), (0.085, 0), (0.088, 0.006), (0.085, 0.012), (0.05, 0.03), (0.028, 0.06),
                             (0.018, 0.11), (0.014, 0.205), (0, 0.205)], (0, 0, 0), body, parent=root)
    prof = [(0.125 * math.cos(a), 0.2 + 0.135 * math.sin(a)) for a in [R(v) for v in range(0, 91, 10)]]
    shade_ = lathe("Lamp_Shade", [(0.127, 0.198)] + prof, (0, 0, 0), mat("bulb", 0.5, emit=3.5, color="#FFE9C9"),
                   parent=root)
    solidify(shade_, 0.004, 0.0)
    if hasattr(shade_, "visible_shadow"):
        shade_.visible_shadow = False            # let the lamp's light shine through the shade
    tube("Lamp_Cord", [(0.06, 0.03, 0.004), (0.09, 0.12, 0.003), (0.10, 0.172, 0.0), (0.10, 0.182, -0.06),
                       (0.105, 0.186, -0.40), (0.11, 0.188, -0.66)], 0.003, BLACK, parent=root)   # over the back, down to the socket


def build_laptop(root, x, y, z0):
    """13-inch aluminium laptop, lid open ~105 deg. Screen = picture hook #1."""
    box("Laptop_Base", (0.304, 0.215, 0.009), (x, y, z0 + 0.0045), ALU, bevel=0.003, parent=root)
    keys = []
    for row in range(6):
        ky = y + 0.088 - row * 0.0185
        kh = 0.0085 if row == 0 else 0.0155
        if row == 5:
            xs = [(-0.105, 0.016), (-0.087, 0.016), (-0.069, 0.016), (-0.047, 0.024), (0.0, 0.066), (0.047, 0.024),
                  (0.069, 0.016), (0.09, 0.016), (0.11, 0.016)]
        else:
            xs = [(-0.1215 + c * 0.0187, 0.0165) for c in range(14)]
        keys += [((kw, kh, 0.0016), (x + kx, ky, z0 + 0.0094)) for kx, kw in xs]
    multi_box("Laptop_Keys", keys, mat("keys", 0.5, color="#2C2C30"), bevel=0.0006, parent=root)
    box("Laptop_Trackpad", (0.135, 0.083, 0.0006), (x, y - 0.058, z0 + 0.0092), mat("alu", 0.25, color="#BFC1C5"),
        bevel=0.0003, parent=root)
    hinge = Vector((x, y + 0.104, z0 + 0.008))
    tilt = Matrix.Rotation(R(-15), 3, "X")
    rot = (R(-15), 0, 0)
    box("Laptop_Lid", (0.304, 0.005, 0.212), hinge + tilt @ Vector((0, 0.0025, 0.106)), ALU, bevel=0.002, rot=rot,
        parent=root)
    box("Laptop_Bezel", (0.300, 0.001, 0.208), hinge + tilt @ Vector((0, -0.0005, 0.106)), BLACK, bevel=0, rot=rot,
        parent=root)
    scr = hook_image("screen", 1, (0.286, 0.179), hinge + tilt @ Vector((0, -0.0012, 0.116)), rot=rot, parent=root,
                     glow=True, default_key="dark")
    deco = [box("Laptop_UI_Bar", (0.286, 0.0004, 0.014), hinge + tilt @ Vector((0, -0.0016, 0.1985)),
                mat("cream", 0.5, emit=0.6), bevel=0, rot=rot, parent=root),
            box("Laptop_UI_Side", (0.06, 0.0004, 0.165), hinge + tilt @ Vector((-0.113, -0.0016, 0.109)),
                mat("main", 0.5, emit=0.6), bevel=0, rot=rot, parent=root)]
    for i in range(9):                                  # lines of "code"
        key = ("accent_1", "accent_2", "accent_3")[i % 3]
        lw = 0.04 + 0.11 * random.random()
        deco.append(box("Laptop_UI_Line", (lw, 0.0004, 0.007), hinge + tilt @ Vector((-0.07 + lw / 2 + (i % 3) * 0.01,
                    -0.0016, 0.177 - i * 0.016)), mat(key, 0.5, emit=0.9), bevel=0, rot=rot, parent=root))
    hook_default(scr, *deco)


def build_desk():
    """MICKE desk 105x50x75: 25 mm top, panel leg, drawer column, back panel with cable outlet + desk props."""
    root, w, d, h = furniture_root("desk")
    top_t = 0.025
    box("Desk_Top", (w, d, top_t), (0, 0, h - top_t / 2), WHITE_FOIL, bevel=0.003, parent=root)
    box("Desk_Cable_Outlet", (0.2, 0.03, 0.002), (-0.22, d / 2 - 0.04, h + 0.0004), DARK, bevel=0.001, parent=root)
    leg_h = h - top_t
    box("Desk_Leg_Panel", (0.025, d - 0.02, leg_h), (-w / 2 + 0.0125, 0, leg_h / 2), WHITE_FOIL, parent=root)
    ux0, ux1 = w / 2 - 0.36, w / 2                     # drawer column on the right
    box("Desk_Unit_Side_Outer", (0.025, d - 0.02, leg_h), (ux1 - 0.0125, 0, leg_h / 2), WHITE_FOIL, parent=root)
    box("Desk_Unit_Side_Inner", (0.018, d - 0.02, leg_h), (ux0 + 0.009, 0, leg_h / 2), WHITE_FOIL, parent=root)
    iw, icx = (ux1 - 0.025) - (ux0 + 0.018), ((ux1 - 0.025) + (ux0 + 0.018)) / 2
    box("Desk_Unit_Back", (iw, 0.01, leg_h - 0.05), (icx, d / 2 - 0.015, 0.05 + (leg_h - 0.05) / 2), WHITE_FOIL, parent=root)
    for nm, z in (("Divider", 0.555), ("Shelf", 0.30), ("Bottom", 0.06)):
        box(f"Desk_Unit_{nm}", (iw, d - 0.05, 0.018), (icx, 0.0, z), WHITE_FOIL, parent=root)
    box("Desk_Unit_Plinth", (iw, 0.018, 0.05), (icx, -d / 2 + 0.045, 0.025), WHITE_FOIL, parent=root)
    dz = (leg_h + 0.565) / 2
    box("Desk_Drawer_Shadow", (iw, 0.01, leg_h - 0.565), (icx, -d / 2 + 0.016, dz), DARK, bevel=0, parent=root)
    box("Desk_Drawer", (iw - 0.006, 0.018, leg_h - 0.571), (icx, -d / 2 + 0.008, dz), WHITE_FOIL, bevel=0.002, parent=root)
    box("Desk_Drawer_Grip", (0.12, 0.006, 0.02), (icx, -d / 2 - 0.0005, dz + 0.035), DARK, bevel=0.004, parent=root)
    box("Desk_Back_Panel", (ux0 - (-w / 2 + 0.025), 0.016, 0.32), ((ux0 + (-w / 2 + 0.025)) / 2, d / 2 - 0.03,
        leg_h - 0.16), WHITE_FOIL, parent=root)
    for i, key in enumerate(("main", "accent_2", "dark")):           # binders and a box in the column
        box("Desk_Binder", (0.055, 0.28, 0.235), (icx - 0.1 + i * 0.062, 0.02, 0.309 + 0.1175), mat(key, 0.6),
            bevel=0.003, parent=root)
    box("Desk_Storage_Box", (iw - 0.04, 0.32, 0.17), (icx, 0.02, 0.069 + 0.085), smat("accent_3", "fabric", 0.9),
        bevel=0.006, parent=root)

    build_laptop(root, -0.1, -0.03, h)
    # mug (email link), pen pot, notebook, a short book stack
    mug = lathe("Desk_Mug", [(0, 0), (0.038, 0), (0.041, 0.005), (0.041, 0.095), (0.037, 0.095), (0.037, 0.01),
                             (0, 0.01)], (0.27, -0.13, h), smat("accent_3", "ceramic", 0.3), parent=root)
    hook_link(mug, "email")
    tube("Desk_Mug_Handle", [(0.27, -0.168, h + 0.075), (0.27, -0.197, h + 0.065), (0.27, -0.197, h + 0.03),
                             (0.27, -0.168, h + 0.022)], 0.006, smat("accent_3", "ceramic", 0.3), parent=root)
    cyl("Desk_Mug_Tea", 0.036, 0.004, (0.27, -0.13, h + 0.078), mat("tea", 0.2, color="#6B4532"), bevel=0, parent=root)
    lathe("Desk_Pen_Pot", [(0, 0), (0.035, 0), (0.035, 0.1), (0.031, 0.1), (0.031, 0.006), (0, 0.006)], (0.2, 0.17, h),
          smat("dark", "ceramic", 0.3), parent=root)
    for i, key in enumerate(("accent_1", "dark", "accent_2", "accent_3")):
        a = i * 1.6
        rod("Desk_Pen", (0.2 + 0.012 * math.cos(a), 0.17 + 0.012 * math.sin(a), h + 0.01),
            (0.2 + 0.03 * math.cos(a), 0.17 + 0.03 * math.sin(a), h + 0.155), 0.004, mat(key, 0.5), parent=root)
    box("Desk_Notebook", (0.15, 0.21, 0.012), (-0.39, -0.07, h + 0.006), mat("dark", 0.7), bevel=0.003,
        rot=(0, 0, R(-8)), parent=root)
    box("Desk_Notebook_Band", (0.008, 0.212, 0.0135), (-0.34, -0.063, h + 0.006), mat("accent_1", 0.6), bevel=0.001,
        rot=(0, 0, R(-8)), parent=root)
    for i, (key, th) in enumerate((("main", 0.03), ("accent_2", 0.024))):
        bz = h + 0.03 * i + th / 2
        box("Desk_Book", (0.24, 0.17, th), (0.37, 0.07, bz), mat(key, 0.7), bevel=0.003, rot=(0, 0, R(i * 9)), parent=root)
        box("Desk_Book_Pages", (0.232, 0.16, th - 0.006), (0.373, 0.068, bz), mat("cream", 0.8), bevel=0.001,
            rot=(0, 0, R(i * 9)), parent=root)

    # TERTIAL-style work lamp clamped to the back-left edge
    lamp_m = smat("dark", "brushed", 0.45, metal=0.4)
    cxp, cyp = -w / 2 + 0.07, d / 2 - 0.035
    box("Desk_Lamp_Clamp", (0.05, 0.06, 0.035), (cxp, cyp, h + 0.0175), lamp_m, bevel=0.005, parent=root)
    box("Desk_Lamp_Jaw", (0.05, 0.06, 0.015), (cxp, cyp, h - top_t - 0.02), lamp_m, bevel=0.004, parent=root)
    box("Desk_Lamp_Clamp_Back", (0.05, 0.012, 0.085), (cxp, d / 2 + 0.003, h - 0.02), lamp_m, bevel=0.003, parent=root)
    p0 = Vector((cxp, cyp, h + 0.1))
    rod("Desk_Lamp_Post", (cxp, cyp, h + 0.03), p0, 0.008, lamp_m, parent=root)
    p1 = Vector((cxp + 0.08, cyp - 0.06, h + 0.47))
    p2 = Vector((cxp + 0.30, cyp - 0.20, h + 0.40))
    for dx in (-0.012, 0.012):
        rod("Desk_Lamp_Arm_Low", p0 + Vector((dx, 0, 0)), p1 + Vector((dx, 0, 0)), 0.0045, lamp_m, parent=root)
        rod("Desk_Lamp_Arm_High", p1 + Vector((dx, 0, 0)), p2 + Vector((dx, 0, 0)), 0.004, lamp_m, parent=root)
    rod("Desk_Lamp_Spring", p0 + (p1 - p0) * 0.15 + Vector((0, 0.015, 0)), p0 + (p1 - p0) * 0.6 + Vector((0, 0.015, 0)),
        0.007, STEEL, parent=root)
    cyl("Desk_Lamp_Elbow", 0.013, 0.04, p1, lamp_m, rot=(0, R(90), 0), parent=root)
    aim = (Vector((cxp + 0.34, -0.12, h)) - p2).normalized()
    shade_ = cyl("Desk_Lamp_Shade", 0.03, 0.13, p2 + aim * 0.07, lamp_m, r2=0.085, segs=32, bevel=0.002, parent=root)
    shade_.rotation_euler = aim.to_track_quat("Z", "Y").to_euler()
    ball("Desk_Lamp_Cap", 0.032, p2, lamp_m, parent=root)


def build_chair():
    """ODGER chair: one-piece moulded shell with a curved backrest + handle slot, four splayed legs."""
    root, w, d, h = furniture_root("chair")
    shell = mat("accent_1", 0.5, tag="shell") if THEME == "pastel" else mat("cream", 0.5, tag="shell")
    seat_z = 0.43
    # curved backrest: an arc in plan (radius 0.33) leaning back 7 degrees
    rad, cyb, n, rows_ = 0.33, 0.165 - 0.33, 16, 6
    # moulded seat: straight front with rounded corners, the back edge follows the backrest arc (no square corners
    # sticking out behind the back, like the real one-piece shell)
    outline = [(-0.185 + 0.37 * i / 6, -0.235) for i in range(7)]
    outline += [(0.185 + 0.04 * math.sin(R(a)), -0.195 - 0.04 * math.cos(R(a))) for a in (30, 60, 90)]
    outline += [(rad * math.cos(R(a)), cyb + rad * math.sin(R(a))) for a in range(52, 129, 6)]
    outline += [(-0.185 - 0.04 * math.sin(R(a)), -0.195 - 0.04 * math.cos(R(a))) for a in (90, 60, 30)]
    bm = bmesh.new()
    face = bm.faces.new([bm.verts.new((x, y, seat_z - 0.024)) for x, y in outline])
    ext = bmesh.ops.extrude_face_region(bm, geom=[face])
    bmesh.ops.translate(bm, vec=Vector((0, 0, 0.024)), verts=[v for v in ext["geom"] if isinstance(v, bmesh.types.BMVert)])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    seat = _obj("Chair_Seat", bm)
    _finish(seat, shell, 0.008, None, root)
    box("Chair_Seat_Frame", (0.34, 0.26, 0.03), (0, -0.05, seat_z - 0.035), shell, bevel=0.006, parent=root)
    verts, faces = [], []
    for k in range(rows_ + 1):
        z = seat_z - 0.015 + (h - seat_z + 0.015) * k / rows_
        lean = (z - seat_z) * math.tan(R(7))
        for i in range(n + 1):
            a = R(90 - 38 + 76 * i / n)
            verts.append((rad * math.cos(a), cyb + rad * math.sin(a) + lean, z))
    faces = [(k * (n + 1) + i, k * (n + 1) + i + 1, (k + 1) * (n + 1) + i + 1, (k + 1) * (n + 1) + i)
             for k in range(rows_) for i in range(n)]
    back = mesh_obj("Chair_Back", verts, faces, shell, parent=root)
    solidify(back, 0.018, 1.0)
    bev = back.modifiers.new("Bevel", "BEVEL")
    bev.width, bev.segments = 0.006, 2
    box("Chair_Handle_Slot", (0.10, 0.03, 0.024), (0, 0.165 + 0.009 + (0.74 - seat_z) * math.tan(R(7)), 0.74),
        mat("black", 0.6, color="#2A2428"), bevel=0.011, parent=root)
    for sx in (-1, 1):
        for sy, by in ((-1, -0.235), (1, 0.19)):
            rod("Chair_Leg", (sx * 0.16, -0.03 + sy * 0.13, seat_z - 0.04), (sx * 0.205, by, 0.004), 0.016, shell,
                r2=0.012, parent=root)
    # tie-on seat pad, kept inside the backrest curve, with its two ties hanging behind the back legs
    pad = smat("accent_3", "fabric", 0.9)
    puffy("Chair_Pad", 0.36, 0.30, 0.04, (0, -0.08, seat_z + 0.018), pad, parent=root)
    for sx in (-1, 1):
        tube("Chair_Pad_Tie", [(sx * 0.15, 0.06, seat_z + 0.012), (sx * 0.165, 0.115, seat_z - 0.01),
                               (sx * 0.168, 0.12, seat_z - 0.09)], 0.004, pad, parent=root)


def build_shelf():
    """KALLAX 2x4 upright: thick 41 mm outer frame, 16 mm inner dividers, open back, boxes, books, records."""
    root, w, d, h = furniture_root("shelf")
    hook_link(root, "github")
    t, it, cube = 0.041, 0.016, 0.335
    for nm, size, loc in (("Top", (w, d, t), (0, 0, h - t / 2)), ("Bottom", (w, d, t), (0, 0, t / 2)),
                          ("Side_L", (t, d, h - 2 * t), (-w / 2 + t / 2, 0, h / 2)),
                          ("Side_R", (t, d, h - 2 * t), (w / 2 - t / 2, 0, h / 2)),
                          ("Divider_V", (it, d, h - 2 * t), (0, 0, h / 2))):
        box(f"Shelf_{nm}", size, loc, WHITE_FOIL, bevel=0.003, parent=root)
    for k in range(1, 4):
        box("Shelf_Divider_H", (w - 2 * t, d, it), (0, 0, t + k * (cube + it) - it / 2), WHITE_FOIL, bevel=0.002,
            parent=root)
    cols = (-(it / 2 + cube / 2), it / 2 + cube / 2)
    fabric = {k: smat(k, "fabric", 0.9) for k in ("accent_1", "accent_2", "accent_3", "main")}
    rnd = random.Random(SEED)

    def drona(cx, zb, key):                             # DRÖNA fabric box with a pull loop
        box("Shelf_Box", (cube - 0.012, 0.37, cube - 0.01), (cx, -0.005, zb + (cube - 0.01) / 2), fabric[key],
            bevel=0.008, parent=root)
        torus("Shelf_Box_Loop", 0.022, 0.006, (cx, -0.192, zb + cube - 0.07), fabric[key], seg=16, tseg=6,
              zscale=1.0, rot=(R(90), 0, 0), parent=root)

    def books(cx, zb, width):
        """Real spines: paperbacks and hardbacks of varied size, muted shades, title bands near the top."""
        x = cx - width / 2 + 0.01
        while x < cx + width / 2 - 0.05:
            bw, bh, bd = rnd.uniform(0.018, 0.045), rnd.uniform(0.17, 0.29), rnd.uniform(0.13, 0.22)
            key = rnd.choice(["main", "accent_1", "accent_2", "accent_3", "cream", "cream", "dark"])
            col = shade(COLORS[key], rnd.choice((0.78, 0.9, 1.0)))
            by = -d / 2 + 0.03
            box("Shelf_Book", (bw, bd, bh), (x + bw / 2, by + bd / 2, zb + bh / 2), mat(key, 0.7, color=col),
                bevel=0.002, parent=root)
            if rnd.random() < 0.7:                      # printed title band(s) on the spine
                band = mat("dark", 0.6) if key in ("cream", "accent_3") else mat("cream", 0.6, tag="band")
                for bz in ((bh - 0.035,) if rnd.random() < 0.6 else (bh - 0.03, 0.03)):
                    box("Shelf_Book_Band", (bw * 0.8, 0.002, 0.014 if bz > 0.05 else 0.008),
                        (x + bw / 2, by - 0.0008, zb + bz), band, bevel=0, parent=root)
            x += bw + rnd.uniform(0.0, 0.004)
        lean = R(12)                                    # last book leans on the others
        box("Shelf_Book", (0.03, 0.18, 0.24), (x + 0.04, -d / 2 + 0.12, zb + 0.118), mat("accent_2", 0.7), bevel=0.002,
            rot=(0, -lean, 0), parent=root)

    def records(cx, zb):                                # LP sleeves (31 cm square) leaning in a row
        for i in range(9):
            key = ("dark", "accent_1", "cream", "main", "accent_3", "dark", "accent_2", "cream", "accent_1")[i]
            box("Shelf_Record", (0.006, 0.31, 0.31), (cx - 0.13 + i * 0.012, 0.0, zb + 0.157), mat(key, 0.6),
                bevel=0.001, rot=(0, R(10), 0), parent=root)

    zb = [t + k * (cube + it) for k in range(4)]
    drona(cols[0], zb[0], "accent_1")
    drona(cols[1], zb[0], "main")
    books(cols[0], zb[1], cube)
    records(cols[1], zb[1])
    drona(cols[0], zb[2], "accent_2")
    books(cols[1], zb[2], cube * 0.55)
    lathe("Shelf_Candle", [(0, 0), (0.04, 0), (0.04, 0.09), (0, 0.09)], (cols[1] + 0.11, -0.05, zb[2]),
          smat("cream", "ceramic", 0.3), parent=root)
    books(cols[0], zb[3], cube * 0.6)
    box("Shelf_Photo", (0.13, 0.015, 0.18), (cols[0] + 0.11, -0.06, zb[3] + 0.09), OAK, bevel=0.003,
        rot=(R(-8), 0, 0), parent=root)
    box("Shelf_Photo_Print", (0.10, 0.002, 0.15), (cols[0] + 0.11, -0.069, zb[3] + 0.09), mat("accent_3", 0.6),
        bevel=0, rot=(R(-8), 0, 0), parent=root)
    drona(cols[1], zb[3], "accent_3")
    # trailing pothos on top
    lathe("Shelf_Pot", [(0, 0), (0.06, 0), (0.07, 0.11), (0.074, 0.115), (0.07, 0.12), (0.064, 0.112), (0, 0.112)],
          (0.24, -0.04, h), smat("cream", "ceramic", 0.3), parent=root)
    leaf = mat("plant", 0.5)
    cyl("Shelf_Pot_Soil", 0.064, 0.006, (0.24, -0.04, h + 0.105), smat("dark", "concrete", 0.95, scale=4), bevel=0,
        parent=root)
    for k in range(7):                                  # leafy tuft on top of the pot
        a = k * 0.9
        ball("Shelf_Pothos_Leaf", 0.022, (0.24 + 0.035 * math.cos(a), -0.04 + 0.035 * math.sin(a), h + 0.125 + 0.01 * (k % 2)),
             leaf, scale=(1, 0.4, 1.25), rot=(R(60), 0, a + math.pi / 2), parent=root)
    for vine, (dx, length) in enumerate(((-0.03, 0.32), (0.05, 0.45), (0.0, 0.18))):
        pts = [Vector((0.24 + dx, -0.06, h + 0.11)), Vector((0.24 + dx * 2, -0.17, h + 0.06)),
               Vector((0.25 + dx * 2, -0.205, h - length * 0.5)), Vector((0.26 + dx * 3, -0.21, h - length))]
        tube("Shelf_Vine", pts, 0.0025, leaf, parent=root)
        for k in range(int(length / 0.06) + 3):
            u = k / (int(length / 0.06) + 2)
            p = pts[1].lerp(pts[3], u) if u > 0.05 else pts[0]
            ball("Shelf_Pothos_Leaf", 0.02, p + Vector(((-1) ** k * 0.018, -0.01, 0)), leaf, scale=(1, 0.35, 1.25),
                 rot=(0, R((-1) ** k * 30), 0), parent=root)


def build_plant():
    """Monstera deliciosa in a glazed pot with a rolled rim and a saucer."""
    root, w, d, h = furniture_root("plant")
    lathe("Plant_Saucer", [(0, 0), (0.15, 0), (0.17, 0.025), (0.163, 0.027), (0.145, 0.007), (0, 0.007)], (0, 0, 0),
          smat("accent_3", "ceramic", 0.3), parent=root)
    lathe("Plant_Pot", [(0, 0), (0.118, 0), (0.125, 0.01), (0.145, 0.24), (0.156, 0.245), (0.16, 0.268),
                        (0.152, 0.275), (0.141, 0.262), (0, 0.262)], (0, 0, 0.007), smat("accent_3", "ceramic", 0.3),
          parent=root)
    cyl("Plant_Soil", 0.142, 0.012, (0, 0, 0.262), smat("dark", "concrete", 0.95, scale=4), bevel=0, parent=root)
    greens = [mat("plant", 0.35, color=shade(COLORS["plant"], f)) for f in (0.82, 1.0, 1.12)]   # glossy old / new leaves
    rib = mat("plant", 0.5, color=shade(COLORS["plant"], 1.35), tag="midrib")
    stem = mat("plant", 0.6, color=shade(COLORS["plant"], 1.15))
    rnd = random.Random(SEED + 3)
    for k, (ang, reach, top, size) in enumerate(((-60, 0.20, 0.62, 0.30), (-20, 0.22, 0.95, 0.36), (15, 0.16, 0.78, 0.34),
                                                 (50, 0.20, 1.05, 0.38), (85, 0.12, 0.70, 0.30), (110, 0.10, 0.92, 0.33),
                                                 (-95, 0.08, 0.85, 0.30), (30, 0.06, 0.55, 0.26), (70, 0.24, 0.50, 0.28))):
        a = R(ang + rnd.uniform(-8, 8))
        base = Vector((0.03 * math.cos(a), 0.03 * math.sin(a), 0.27))
        tip = Vector((reach * math.cos(a), reach * math.sin(a), top))
        mid = base.lerp(tip, 0.5) + Vector((0, 0, 0.06))
        tube("Plant_Petiole", [base, mid, tip], 0.0055, stem, parent=root)
        monstera_leaf("Plant_Leaf", size, size * 0.92, tip, (R(-rnd.uniform(18, 42)), 0, a - math.pi / 2), greens[k % 3],
                      parent=root, slits=3 + k % 2, droop=0.25, rib_material=rib)


def build_rug():
    """LOHALS flatwoven jute rug 160x230 with bound edges."""
    root, w, d, h = furniture_root("rug")
    jute = smat("jute", "fabric", 0.95, scale=0.5)
    box("Rug_Body", (w, d, 0.006), (0, 0, 0.003), jute, bevel=0.002, parent=root)
    # flat weave: chunky 1.4 cm jute ribs across the rug, two close natural tones with an occasional darker yarn
    pitch, rows_ = 0.014, int((w - 0.06) / 0.014)
    rnd = random.Random(11)
    tones_ = {0: [], 1: [], 2: []}
    for k in range(rows_):
        x = -w / 2 + 0.03 + pitch * (k + 0.5)
        r_ = rnd.random()
        t = 2 if r_ < 0.05 else (1 if r_ < 0.45 else 0)
        tones_[t].append(((pitch * 0.97, d - 0.06, 0.004), (x, 0, 0.007)))
    for t, f in ((0, 1.0), (1, 0.965), (2, 0.9)):           # twisted-yarn look; natural jute varies only a little
        multi_box(f"Rug_Weave_{t}", tones_[t], smat("jute", "knit", 0.95, color=shade(COLORS["jute"], f), scale=0.6),
                  bevel=0.0016, parent=root)
    edge = smat("jute", "fabric", 0.95, color=shade(COLORS["jute"], 0.88), scale=0.5)   # bound in the same jute
    multi_box("Rug_Binding", [((w, 0.03, 0.012), (0, sy * (d / 2 - 0.015), 0.006)) for sy in (-1, 1)] +
              [((0.03, d, 0.012), (sx * (w / 2 - 0.015), 0, 0.006)) for sx in (-1, 1)], edge, bevel=0.003, parent=root)


def build_wall_art():
    """Two RIBBA-style deep box frames hung landscape, white mounts; prints show your projects."""
    root, w, d, h = furniture_root("wall_art")
    fw, fh, fd, bar = 0.72, 0.52, 0.045, 0.02
    frame_m = smat("dark", "veneer", 0.45)
    mount = smat("cream", "paper", 0.8)
    for i, fx in enumerate((-(w - fw) / 2, (w - fw) / 2)):
        fy = d / 2 - fd / 2
        multi_box("Art_Frame", [((fw, fd, bar), (fx, fy, h - bar / 2)), ((fw, fd, bar), (fx, fy, bar / 2)),
                                ((bar, fd, fh - 2 * bar), (fx - fw / 2 + bar / 2, fy, fh / 2)),
                                ((bar, fd, fh - 2 * bar), (fx + fw / 2 - bar / 2, fy, fh / 2))], frame_m,
                  bevel=0.003, parent=root)
        box("Art_Mount", (fw - 2 * bar, 0.004, fh - 2 * bar), (fx, d / 2 - 0.035, fh / 2), mount, bevel=0, parent=root)
        canvas = hook_image("frame", i + 1, (0.56, 0.36), (fx, d / 2 - 0.0375, fh / 2), parent=root,
                            default_key=("accent_3", "cream")[i])
        fy0 = d / 2 - 0.039
        if i == 0:      # print 1: sun over layered hills
            deco = [ball("Art_Sun", 0.06, (fx + 0.12, fy0, fh / 2 + 0.06), mat("accent_1", 0.8), scale=(1, 0.05, 1),
                         parent=root),
                    flat("Art_Hill", [(-0.28, -0.18), (-0.1, 0.03), (0.08, -0.18)], (fx, fy0 - 0.001, fh / 2), mat("main", 0.8),
                         parent=root),
                    flat("Art_Hill", [(-0.08, -0.18), (0.12, -0.02), (0.28, -0.18)], (fx, fy0 - 0.002, fh / 2),
                         mat("plant", 0.8), parent=root)]
        else:           # print 2: rainbow arches
            deco = [arch("Art_Arch", 0.13 - 0.04 * k, 0.17 - 0.04 * k, (fx, fy0 - 0.001 * k, fh / 2 - 0.13),
                         mat(("accent_1", "accent_3", "accent_2", "main")[k], 0.8), parent=root) for k in range(4)]
        hook_default(canvas, *deco)


def tabby(m, stripe_hex):
    """Soft tabby stripes on a fur material: blends a darker colour into KIT_BASE in wavy bands."""
    nt = m.node_tree
    base = nt.nodes.get("KIT_BASE")
    users = [l.to_socket for l in nt.links if l.from_node == base]
    coords = nt.nodes.new("ShaderNodeTexCoord")
    wave = nt.nodes.new("ShaderNodeTexWave")
    wave.wave_type, wave.bands_direction = "BANDS", "X"
    wave.inputs["Scale"].default_value, wave.inputs["Distortion"].default_value = 7.0, 5.0
    if "Detail" in wave.inputs:
        wave.inputs["Detail"].default_value = 3.0
    nt.links.new(coords.outputs["Object"], wave.inputs["Vector"])
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    els = ramp.color_ramp.elements
    els[0].position, els[1].position, els[1].color = 0.55, 0.9, (0.65, 0.65, 0.65, 1)   # soft, broken stripes
    nt.links.new(wave.outputs["Fac"], ramp.inputs["Fac"])
    mix = nt.nodes.new("ShaderNodeMix")
    mix.data_type = "RGBA"
    nt.links.new(ramp.outputs["Color"], mix.inputs["Factor"])
    nt.links.new(base.outputs[0], mix.inputs[6])
    mix.inputs[7].default_value = lin(stripe_hex)
    for sock in users:
        nt.links.new(mix.outputs[2], sock)
    return m


def build_pet():
    """Calming donut cat bed (50 cm) with a curled-up sleeping cat."""
    root, w, d, h = furniture_root("pet")
    plush = smat("accent_2", "knit", 0.95, scale=1.6)
    shag = bpy.data.textures.get("Shag") or bpy.data.textures.new("Shag", "CLOUDS")   # faux-fur pile
    shag.noise_scale = 0.012
    for o in (torus("Pet_Bed_Bolster", 0.178, 0.072, (0, 0, 0.085), plush, zscale=1.2, parent=root),
              ball("Pet_Bed_Cushion", 0.16, (0, 0, 0.05), plush, scale=(1, 1, 0.3), parent=root)):
        subsurf(o, 2)
        disp = o.modifiers.new("Shag", "DISPLACE")
        disp.texture, disp.strength, disp.mid_level, disp.texture_coords = shag, 0.012, 0.5, "GLOBAL"
    cyl("Pet_Bed_Base", 0.2, 0.03, (0, 0, 0.015), plush, bevel=0.012, parent=root)
    fur = tabby(smat("pet", "fabric", 0.95, color=COLORS["pet"]), shade(COLORS["pet"], 0.78))
    belly = mat("cream", 0.9, tag="fur")
    # curled-up cat: round back, head resting on the front paws, tail wrapped around the front
    ball("Pet_Body", 0.12, (0.03, 0.03, 0.12), fur, scale=(1.18, 1.0, 0.68), rot=(0, 0, R(25)), parent=root)
    ball("Pet_Haunch", 0.075, (0.09, 0.06, 0.13), fur, scale=(1.0, 1.0, 0.85), parent=root)
    head = Vector((-0.085, -0.085, 0.165))
    for sx in (-1, 1):
        ball("Pet_Paw", 0.024, Vector((-0.07 + sx * 0.035, -0.13, 0.085)), belly, scale=(0.9, 1.5, 0.7), parent=root)
    ball("Pet_Head", 0.064, head, fur, scale=(1.08, 0.95, 0.85), parent=root)
    for sx in (-1, 1):
        ear = cyl("Pet_Ear", 0.024, 0.045, head + Vector((sx * 0.036, 0.008, 0.052)), fur, r2=0.003, segs=10, bevel=0,
                  parent=root)
        ear.rotation_euler = (R(-12), R(sx * 22), 0)
        box("Pet_Eye", (0.02, 0.004, 0.0035), head + Vector((sx * 0.025, -0.059, 0.012)), DARK, bevel=0,
            rot=(0, R(-sx * 12), 0), parent=root)
    ball("Pet_Muzzle", 0.026, head + Vector((0.0, -0.05, -0.016)), belly, scale=(1.2, 0.75, 0.72), parent=root)
    ball("Pet_Nose", 0.007, head + Vector((0.0, -0.07, -0.004)), mat("accent_1", 0.5), parent=root)
    tube("Pet_Tail", [(0.17, 0.0, 0.1), (0.14, -0.11, 0.095), (0.04, -0.165, 0.092), (-0.03, -0.165, 0.095)], 0.022,
         fur, parent=root)


PLACEHOLDERS = {
    "pet": build_pet, "bed": build_bed, "side_table": build_side_table, "lamp": build_lamp, "desk": build_desk,
    "chair": build_chair, "shelf": build_shelf, "plant": build_plant, "rug": build_rug, "wall_art": build_wall_art,
}
if SHOW_PLACEHOLDER_FURNITURE:
    for slot_name, build in PLACEHOLDERS.items():
        build()


def knit_pouf(name, loc, material, r=0.25, h=0.36, segs=96, rings=25):
    """Chunky hand-knit pouf (50 cm dia. x 36 cm): a rounded drum with raised knit columns and stitch rows."""
    verts = []
    for i in range(segs):
        th = 2 * math.pi * i / segs
        for k in range(rings):
            phi = -math.pi / 2 + math.pi * k / (rings - 1)          # bottom centre -> side -> top centre
            c, s_ = math.cos(phi), math.sin(phi)
            rr = r * abs(c) ** 0.35
            z = h / 2 + h / 2 * math.copysign(abs(s_) ** 0.6, s_)
            side = abs(c) ** 2                                       # stitches show on the sides and top edge
            stitch = (0.5 + 0.5 * math.cos(2 * 14 * th)) * (0.6 + 0.4 * abs(math.sin(math.pi * z / 0.045)))
            rr += 0.012 * side * stitch
            verts.append((rr * math.cos(th), rr * math.sin(th), z))
    faces = [(i * rings + k, i * rings + k + 1, ((i + 1) % segs) * rings + k + 1, ((i + 1) % segs) * rings + k)
             for i in range(segs) for k in range(rings - 1)]
    return subsurf(mesh_obj(name, verts, faces, material, loc, weld=True), 1)


# Real-life clutter that fills the open floor: a chunky knit pouf on the rug and felt slippers kicked off by the bed.
POUF = smat("cream", "knit", 0.95, color=shade(COLORS["cream"], 0.94), scale=0.7)
knit_pouf("Pouf_Knit", (3.22, 1.0, FLOOR_Z + 0.008), POUF)
ball("Pouf_Knot", 0.035, (3.22, 1.0, FLOOR_Z + 0.008 + 0.355), POUF, scale=(1, 1, 0.45))   # the gathered yarn at the top
PLUSH = smat("accent_1", "knit", 0.95, scale=1.4)                     # open-back plush mules, 27 cm long
SOLE = mat("cream", 0.7, color=shade(COLORS["cream"], 0.9), tag="sole")
for k, (sx_, sy_, turn_) in enumerate(((1.62, 1.97, 100), (1.47, 1.80, 75))):
    a = R(turn_)
    fwd = Vector((-math.sin(a), math.cos(a), 0))                        # the slipper's toe direction
    ball("Slipper_Sole", 0.135, (sx_, sy_, FLOOR_Z + 0.009), SOLE, scale=(0.38, 1, 0.07), rot=(0, 0, a))
    ball("Slipper_Footbed", 0.12, Vector((sx_, sy_, FLOOR_Z + 0.017)) - fwd * 0.01, PLUSH, scale=(0.36, 1, 0.03),
         rot=(0, 0, a))
    ball("Slipper_Upper", 0.1, Vector((sx_, sy_, FLOOR_Z + 0.014)) + fwd * 0.055, PLUSH, scale=(0.54, 0.72, 0.5),
         rot=(0, 0, a))

# Felt letter board (your name + role from profile.json) leaning on top of the KALLAX.
board = bpy.data.objects.new("Letter_Board", None)
board.location = (SLOTS["shelf"].location.x, D - 0.062, FLOOR_Z + 1.47 + 0.222)
board.rotation_euler = (R(-10), 0, 0)
COL_ROOM.objects.link(board)
sign = box("Name_Sign", (0.60, 0.022, 0.45), (0, 0, 0), OAK, bevel=0.004, parent=board)
hook_link(sign, "website")
felt = smat("dark", "fabric", 0.95)
box("Name_Sign_Felt", (0.55, 0.004, 0.40), (0, -0.011, 0), felt, bevel=0, parent=board)
multi_box("Name_Sign_Grooves", [((0.55, 0.002, 0.0025), (0, -0.0135, -0.19 + k * 0.0167)) for k in range(23)],
          mat("dark", 0.95, color=shade(COLORS["dark"], 0.7)), bevel=0, parent=board)
letters = mat("cream", 0.4, tag="letters")
hook_text("name", 1, "YOUR NAME", 0.09, (0, -0.016, 0.065), material=letters, max_width=0.5, parent=board, depth=0.004)
hook_text("role", 1, "your role", 0.05, (0, -0.016, -0.065), material=letters, max_width=0.5, parent=board, depth=0.004)

# Poster on a wooden magnetic hanger (left wall, above the plant): picture hook "poster".
px, py, pz = 0.006, 0.52, 1.56
POSTER_ROT = (0, 0, R(90))                      # faces +X, into the room
poster = hook_image("poster", 1, (0.60, 0.40), (px, py, pz), rot=POSTER_ROT, default_key="cream")
for dz in (0.205, -0.205):
    box("Poster_Hanger_Bar", (0.022, 0.64, 0.022), (px + 0.008, py, pz + dz), OAK, bevel=0.003)
tube("Poster_Cord", [(0.012, py - 0.3, pz + 0.215), (0.004, py, pz + 0.33), (0.012, py + 0.3, pz + 0.215)], 0.0018,
     mat("cream", 0.6, tag="cord"))
cyl("Poster_Nail", 0.004, 0.02, (0.01, py, pz + 0.33), STEEL, rot=(0, R(90), 0))
hook_default(poster,
             ball("Poster_Circle", 0.11, (px + 0.003, py - 0.1, pz + 0.04), mat("accent_1", 0.8), scale=(0.05, 1, 1)),
             box("Poster_Block", (0.002, 0.2, 0.26), (px + 0.004, py + 0.13, pz - 0.0), mat("main", 0.8), bevel=0),
             box("Poster_Stripe", (0.002, 0.5, 0.025), (px + 0.005, py, pz - 0.15), mat("dark", 0.8), bevel=0),
             box("Poster_Stripe", (0.002, 0.3, 0.012), (px + 0.005, py - 0.1, pz - 0.175), mat("dark", 0.8), bevel=0))


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


# Sun shining in through the window, a big soft fill from the camera side, the bedside lamp.
light("Light_Sun", "SUN", SUN_STRENGTH, kelvin(SUN_WARMTH), (-3, wy, 4), aim=(1.2, wy - 0.6, 0), size=R(3))
light("Light_Fill", "AREA", 250 * (W * D / 16), kelvin(5600), (W + 3, -3, H + 2.5), aim=(W / 2, D / 2, 0.6), size=6)
lamp_slot = SLOTS["lamp"]
light("Light_Lamp", "POINT", LAMP_STRENGTH, kelvin(LAMP_WARMTH),
      lamp_slot.location + Vector((0, 0, lamp_slot["kit_size"][2] * 0.3)), size=0.08)
light("Light_Bounce", "AREA", 40, kelvin(LAMP_WARMTH), (W / 2, D / 2, H - 0.1), aim=(W / 2, D / 2, 0), size=2.5)
if FAIRY_LIGHTS:
    light("Light_Fairy", "AREA", 12, kelvin(LAMP_WARMTH), (2.9, D - 0.25, 2.15), aim=(2.9, D - 0.6, 1.0), size=1.6)

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
scene["kit_material_finish"] = json.dumps({"roughness": 0.65, "bevel": 0.02, "saturation": 0.75})
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
