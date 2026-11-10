# Room Template Spec (kit v2)

This spec is for people building new rooms. The reference implementation is `templates/cozy_bedroom.py`. Copy its structure, helpers and section order. Every room must pass `blender -b templates/output/<room>.blend -P tools/check_room.py`.

## 1. One standalone script per room
- Each room is a single file, `templates/<room_id>.py`, using only `bpy`, `bmesh` and `mathutils`.
- It must run on Blender 4.2+ and 5.x:
  - Try both Eevee engine names.
  - Look up shader nodes by type.
  - Set `use_nodes` only when `bpy.app.version < (5, 0, 0)`.
  - Guard optional Eevee settings with `hasattr`.
- Look: an isometric two-wall cutaway (back wall at y = D, left wall at x = 0), chunky rounded primitives (bevel modifiers), an orthographic camera that frames the room automatically, and the `Standard` view transform.
- Output: 1920×1080 Eevee. Running the script in background mode saves `output/<room_id>.blend` and renders `output/<room_id>.png`. When `ROOMKIT_BUILD_ONLY=1`, it saves but skips the render.
- Aim for about 1,000–2,200 lines (kit v3 realism needs more geometry). Readable is more important than clever.

## 2. SETTINGS block
Keep these names in this order. Each line gets a short comment a beginner can understand.
```
ROOM_NAME
ROOM_WIDTH, ROOM_DEPTH, WALL_HEIGHT
THEME                      # name of the default theme
THEMES = {name: {colour role: hex}}   # at least 2 themes; each has all 12 required keys
SUN_WARMTH, SUN_STRENGTH, LAMP_WARMTH, LAMP_STRENGTH
<style extras>             # e.g. NEON_STRENGTH, FAIRY_LIGHTS (optional)
SEED                       # shuffles books, bottles, plants and props
SHOW_PLACEHOLDER_FURNITURE, SHOW_SLOT_BOXES
CAMERA_HEIGHT_ANGLE, CAMERA_TURN, RESOLUTION, RENDER_SAMPLES, OUTPUT_FOLDER
```
- **Required colour keys:** `background, wall, wall_trim, floor, wood, main, accent_1, accent_2, accent_3, cream, plant, dark`. Extra keys are allowed.
- **Light values per theme:** if a theme needs different lights (for example night vs day), branch on `THEME` in code and say so in a comment next to `THEMES`.
- **Overrides:** right after the imports, honour `ROOMKIT_THEME` and `ROOMKIT_SEED`. Copy that block from the reference.

## 3. Slots (where furniture goes)
Use `slot(name, size, center_xy, z=, turn=, kind=, shape=)`. Each room has **6–10 slots** and every slot has a placeholder builder in `PLACEHOLDERS`.

**Names** come only from this shared vocabulary:
`desk, chair, stool, sofa, armchair, bed, table, side_table, counter, display_case, shelf, wall_shelf, cabinet, media_console, workbench, easel, monitor, instrument, speaker, hero_prop, lamp, floor_lamp, pendant_lamp, plant, hanging_plant, rug, wall_art, pet`
plus (kit v4, themed rooms) `clothes_rack, wardrobe, vanity, mirror, telescope, trunk, fireplace, stove, bookcase, salon_chair, bunk_bed, window_seat, planter`. New slot names still use the existing `shape` list for photo builds (e.g. clothes_rack → `shelf`, vanity → `table`, telescope → `lamp`, trunk → `box`).

**`kind`** is one of:
- `floor`
- `surface` (sits on another piece)
- `wall` (hung; its back touches the wall)
- `rug`
- `hanging` (hangs from above, e.g. a pendant lamp or hanging plant)

**`shape`** is what `add_furniture.py` builds from a photo. Use one of:
`chair, sofa, stool, table, counter, bed, shelf, cabinet, monitor, lamp, plant, rug, frame, pet, box`

Placement rules:
- The furniture's **front faces local −Y**. Set `turn` so that front faces into the room or toward the camera.
- Slots must not overlap, except rugs and things standing on a rug. They must stay inside the room.
- Sizes are real-world metres.
- If the room has a `lamp` slot, name its light `Light_Lamp` and place it at that slot.
- Lights that belong to a piece of furniture (monitor glow, LED strips) may be parented to its placeholder. `add_furniture.py` keeps them when the piece is replaced.

## 4. Portfolio hooks (the main reason people buy the kit)
`tools/build_portfolio.py` fills these hooks from the user's `profile.json`. Use the helpers from the reference: `hook_image`, `hook_text`, `hook_link` and `hook_default`.

**Required in every room:**
- 1 `name` text hook and 1 `role` text hook. They go on a sign, nameplate, neon sign, menu board or similar. Readable in the 1920×1080 render: the name at least about 0.08 m tall, with strong contrast.
- **3 or more picture hooks:** `screen` (glows), `frame`, `poster`, `canvas` or `board`. Each is at least about 0.25 m on its longest side, clearly visible from the camera, and not hidden by furniture. These show the user's project images in this order: screens, frames, posters, canvases, boards.
- **2 or more link hooks,** set with `hook_link(obj, ...)`. One must be `email`; the others can be `github`, `linkedin` or `website`. Choose objects that make sense for the room: a mug or mailbox for email, a bookshelf for github, a sign for website.

**Optional:**
- `title` text hooks (project titles on book spines, labels or a menu board)
- `skill` text hooks (sticky notes, jars, tags)
- a `tagline` hook
- a `logo` picture hook

**Default content:** without a profile, every hook must still look good. Give each hook a pleasant default material, and add decoration (fake UI, a doodle) on top as separate objects marked with `hook_default(hook, *objs)`. Those objects are hidden once a real image is applied.

## 5. Scene metadata (set at the end, like the reference)
- `kit_style` (= room id)
- `kit_version = 2`
- `kit_palette` (JSON of the active COLORS)
- `kit_material_finish`
- `kit_furniture_colors`: the colour keys imported furniture may use. Leave out neon or sky colours.
- `kit_theme`
- `kit_bounds = [-T, 0, -0.2, W, D + T, H + 0.12]`, or larger if the room has things outside the walls, such as an awning. In that case also set `kit_room_size = [W, D, H]`.

## 6. Quality bar
- The room is recognisable as its room type at thumbnail size, and clearly different from the other rooms in palette, light and layout.
- Nothing floats, clips into walls or blocks the hooks. The lighting is pleasing and readable, and dark rooms still show furniture silhouettes.
- Every theme renders correctly.

## 7. Realism standard (kit v3): real products in a cosy style
Buyers must recognise the furniture as **things they could buy or have seen**, not as generic "AI" blocks. Keep the clean isometric miniature look, the palette themes and the portfolio hooks.
- **Every furniture piece and major prop is modelled on a named real-world reference** with real dimensions. Examples: IKEA (KALLAX, BILLY, MALM, POÄNG, LACK, ALEX, BEKANT, LINNMON, MARKUS, HEMNES, EKTORP, STOCKHOLM rug), HAY, Muji, Herman Miller, Muuto, Thonet No.14 / bentwood café chairs, Tolix stools, La Marzocco–style espresso machines, Technics-style turntables, Yamaha-style keyboards, Secretlab-style gaming chairs, IKEA SKÅDIS pegboards.
- **Rooms that are venues copy real venue language**, never their brand. A bakery-café uses a dark-wood or marble counter, a glass pastry cabinet with tiered trays, wicker bread baskets, a chalk or letter menu board, subway tiles, pendant lights and bentwood chairs, like Gail's, Ole & Steen, Le Pain Quotidien or an independent café. The plant shop uses galvanised buckets, terracotta pots, a potting bench and grow lights, and so on.
- **No logos, brand names or trademarked graphics** appear in the scene. Product names belong only in code comments and the reference list.
- **Construction detail is what makes things look real:**
  - legs, rails and stretchers
  - drawer fronts with gaps of 3 mm or more and real handles or knobs
  - cabinet doors, shelf pins, back panels, plinths, skirting boards and door frames
  - sofa seat and back cushions as separate pieces, with arms, legs, piping or seams
  - chair seats, backrests and armrests; office chairs with a five-star base, casters and gas lift
  - monitor stands and bezels; a keyboard with key rows; mug handles; book spines of varied height and thickness
  - plant pots with a rim and soil
  - curtains with folds, a rail and rings
  - Thin parts must be thin: a desktop is 18–25 mm, a shelf 15–20 mm, chair legs 25–40 mm.
- **Edges:** real furniture uses small bevels (2–8 mm). Use 15–25 mm only on soft items: cushions, mattresses, pouffes.
- **Materials:** use `surface()` from `tools/snippets/surfaces.py`, pasted verbatim. It adds wood grain, veneer, fabric weave, knit, leather, veined marble, terrazzo, brushed metal, glazed ceramic, paper, plaster, concrete, brick and tiles while keeping the palette colours, so themes and brand_color keep working. Every wooden, fabric, stone, metal and wall or floor surface gets the matching kind. The floor matches its real counterpart: oak planks, herringbone, terrazzo, tiles or concrete.
- **Scale realism:** standard heights.

  | Item | Height |
  |---|---|
  | Desk | 73–75 cm |
  | Counter | 90–92 cm |
  | Bar stool seat | 65–75 cm |
  | Dining or café chair seat | 45 cm |
  | Sofa seat | 42–45 cm |
  | Bed | 45–55 cm |
  | Door | 2.0–2.1 m |
  | Window sill | 0.8–0.9 m |
  | Pendant lamp | about 0.75 m above the table |

- **Reference list:** each template has a `REFERENCES` comment block under its docstring with one line per piece: what it's modelled on (product or venue type), real dimensions used, and a source URL. There is also a matching `research/<room_id>.md`.

## 8. Themed rooms (kit v4)
Themed rooms capture a *feeling* fans search for (fairytale, wizard school, tiny planet, animal city, hand-painted countryside...) with **original** designs.
- **Never use** franchise names, characters (or recognisable lookalikes), logos, crests or house names, signature costume designs, quotes, maps, or iconic props that only exist in one franchise. Use generic genre props instead: a rail of original ball gowns in varied silhouettes, house-neutral banners, a generic owl perch, a rose under a glass dome. When in doubt, leave it out.
- The realism standard (section 7) still applies: whimsical pieces are built like the real objects behind them, such as a real garment rail, a Hollywood vanity mirror, a refractor telescope, a steamer trunk, a ramen counter, a pedicure chair.
- A themed room may replace the two-wall box with another diorama base (for example a small round planet or a street-corner shopfront). It still uses the same camera framing from `kit_bounds`, sets `kit_room_size`, and keeps every slot inside `[0, W] × [0, D]`.
