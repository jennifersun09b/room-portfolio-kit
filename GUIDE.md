# 3D Room Portfolio Kit: Beginner Guide

Fill in one file with your name, projects and links. The kit then makes:
- a 3D room with your work on its screens, frames and signs
- a clickable one-page portfolio site
- an interactive 3D version of that site: visitors turn the room, zoom in and click things
- images sized for LinkedIn, X and Instagram

You don't need to know Blender.

```
RoomKit/
  profile.json   ← your details (edit this)
  templates/     17 rooms (see below)
  tools/         build_portfolio.py · export_web.py · add_furniture.py · photo_to_3d.py · check_room.py
  research/      the real products and venues each room is modelled on (with sizes and links)
  samples/       practice files: an armchair .glb, a photo, project images
  examples/      a finished portfolio built from the sample profile
  previews/      every room in every theme
```

> **Don't want to type commands?** Double-click **Start.command** (Mac) or **Start.bat** (Windows) to open **RoomKit Studio**, a visual builder in your browser. It does everything in this guide with forms, drag-and-drop and buttons. See [STUDIO.md](STUDIO.md). The rest of this guide is for people who prefer the command line.

## 1. Install (about 5 minutes)
1. Download **Blender 4.2 or newer** (free) from [blender.org/download](https://www.blender.org/download/) and install it.
2. On a Mac, the program is at `/Applications/Blender.app/Contents/MacOS/Blender`. Use that path wherever you see `blender` below. On Windows and Linux, use your Blender install path.

## 2. Pick your room
Every room is furnished with pieces modelled on real products at their real sizes, so visitors recognise them: IKEA-style desks, shelves and armchairs, a bakery-café counter with a pastry cabinet, a Chesterfield, and so on. No brand names or logos appear in the rooms. `research/<room>.md` lists what each piece is based on.

| Room (`--room`) | For | Themes (`--theme`) |
|---|---|---|
| `dev_office` | developers, CS students | daylight · japandi · night |
| `streamer_den` | streamers, VTubers, game devs | neon · clean |
| `living_lounge` | video, photo, podcast creators | smooth · retro70s |
| `cozy_cafe` | cafés, bakeries, small shops | morning · bakery |
| `cozy_bedroom` | students, first portfolios | pastel · coquette · cottagecore |
| `academia_library` | writers, researchers | rainy_evening · sunny_reading |
| `design_studio` | designers, illustrators, 3D artists | airy · studio_night |
| `music_studio` | musicians, producers, podcasters | evening · daylight |
| `potion_shop` | fantasy creators, Etsy makers | moonlit · harvest |
| `plant_shop` | florists, makers | morning · golden_hour |

**Themed rooms** (original designs that capture a feeling, with no characters or brands):

| Room (`--room`) | For | Themes (`--theme`) |
|---|---|---|
| `fairytale_atelier` | fashion and bridal designers, dressmakers, princesscore creators | morning_blush · midnight_ball |
| `wizard_school_dorm` | writers, fandom creators, students, streamers | candlelit_night · autumn_term |
| `tiny_planet_stargazer` | illustrators, poets, brand designers, teachers | sunset_hour · starry_night |
| `animal_city_apartment` | animators, character designers, streamers, students | sunny_downtown · neon_nightlife |
| `hearth_cottage` | artists, writers, crafters, couples | summer_afternoon · rainy_lantern |
| `lantern_ramen_bar` | restaurants, food creators, game devs | lantern_night · neon_rain |
| `glow_beauty_bar` | nail, lash and beauty businesses | milk_blush · jelly_neon |

## 3. Make your portfolio (one command)
1. Open `profile.json` in any text editor and fill in:
   - your name, role and tagline
   - your links: `email`, `github`, `linkedin`, `website`, and also `behance`, `dribbble`, `instagram`, `etsy`, `kofi`, `twitch`, `youtube`. A full link or just your handle (`"instagram": "@myshop"`) both work. Leave out the ones you don't have. If the room has an object for a link you left out (say, the GitHub bookshelf), it opens one of your other links instead.
   - 3–9 projects (title, image, url)
   - your room
   - optional: `brand_color`, a hex code such as `"#FF8A00"`
   Image paths are relative to `profile.json`.
2. Run:
```bash
blender -b -P tools/build_portfolio.py -- --profile profile.json
```
   `--profile` can also be the folder that holds your `profile.json`.
3. Open the new `portfolio_<room>/` folder. It contains:
   - `index.html`: your site. Visitors click the screens, frames and sign to open your projects, and click the mug or mailbox to email you. Upload the folder to GitHub Pages, Netlify or Vercel as it is.
   - `hero.png` (1920×1080), `og.png` (link preview), `instagram.png` and `banner.png` (LinkedIn header).
   - `room.blend`, if you want to keep editing.

Useful options: `--room dev_office`, `--theme night`, `--seed 12` (reshuffles books and props), and `--fast` (a quick preview).

**More image sizes:** add `--exports` with the ones you want, separated by commas:

| Name | Size | For |
|---|---|---|
| `hero` | 1920×1080 | your site (always made) |
| `og` | 1200×630 | link previews |
| `instagram` | 1080×1350 | Instagram post |
| `banner` | 1584×396 | LinkedIn / X header |
| `behance` | 808×632 | Behance project cover |
| `dribbble` | 1600×1200 | Dribbble shot |
| `story` | 1080×1920 | Instagram / TikTok story |
| `obs4k` | 3840×2160 | stream background (OBS) |

```bash
blender -b -P tools/build_portfolio.py -- --profile profile.json --exports hero,behance,dribbble,story
```
Without `--exports` you get the first four.

### Make it 3D (optional, adds a few minutes)
Add `--web`:
```bash
blender -b -P tools/build_portfolio.py -- --profile profile.json --web
```
This adds `room3d.html` and a `3d/` folder. It's a real 3D room in the browser:
- Visitors drag to turn it, scroll or pinch to zoom, and click the dots, screens and objects.
- Projects open in a pop-up with their image, description and link; the mug or mailbox opens an email.
- The lighting is baked once with Blender's Cycles renderer, so it looks like your renders and runs smoothly on phones. The whole room is about 1–3 MB.
- `index.html` gets an "Explore my room in 3D" button.

**To look at it, just double-click `room3d.html`.** It is one self-contained file: the room, its lighting and your project images are all inside it (usually 2–5 MB). It needs an internet connection, because it downloads the 3D engine (Three.js). Upload the folder to GitHub Pages, Netlify or Vercel as it is.

Want a smaller page with the 3D files kept separate (for big rooms on your own host)? Add `--separate-files`. That page must then be opened through a web server: `cd portfolio_dev_office && python3 -m http.server 8000`, then http://localhost:8000/room3d.html.

Already built the portfolio? Make just the 3D part from its `room.blend`:
```bash
blender -b portfolio_dev_office/room.blend -P tools/export_web.py
```
The 3D page loads Three.js from the jsDelivr CDN, so visitors need an internet connection.

## 4. Add your own furniture (optional)
Every room has named **slots**, which are invisible boxes that furniture snaps into: `desk`, `chair`, `sofa`, `counter`, `shelf`, `plant`, `pet`, and more. A new piece replaces the placeholder in that slot. It is resized to fit, set down on the floor (or hung on the wall), and recoloured to match the room.

**Which slots does my room have?** Ask the room:
```bash
blender -b templates/output/dev_office.blend -P tools/add_furniture.py -- --list-slots
```
It lists every slot with its kind (floor, wall, surface...), the shape built from photos, and its size in metres.

**From a photo, with AI (easiest):** add `--ai auto`. The kit sends your photo to an AI service, gets a real textured 3D model back and puts it in the slot:
```bash
blender -b templates/output/dev_office.blend -P tools/add_furniture.py -- --slot chair --photo ~/Downloads/my_chair.jpg --ai auto --save my_room.blend
```
- `auto` uses the first service you have a key for: **Meshy** (best, about $0.30–0.60 a model, needs a paid Meshy plan), then **fal.ai** (pay as you go, about $0.02–0.30), then the **free Hugging Face** demo (no key, but only 1–2 models a day and sometimes busy). You can also name one: `--ai meshy`, `--ai fal`, `--ai hf`. `--ai sample` is a free practice run that uses the sample armchair.
- **Keys** go in environment variables (`MESHY_API_KEY`, `FAL_KEY`, and optionally a free `HF_TOKEN`) or in a file `~/.roomkit/keys.json`: `{"MESHY_API_KEY": "msy_..."}`. Never put keys in `profile.json`, which ends up on the web.
- Before a paid service runs, the kit shows the estimated cost and asks. Add `--yes` to skip the question. `--quality draft` is cheaper and faster (good for small props).
- The same photo is never paid for twice: models are kept in `~/.roomkit/cache/`. If a service takes too long, run the same command again later to pick up the finished model.
- If no AI model can be made (no key, no internet, the free demo is full), the kit tells you and builds the simple blocky version instead, so you always get furniture.
- iPhone `.heic`, `.png`, `.webp` and `.jpg` photos all work. Best results: one object, plain background, the whole object in view, taken from a slight angle.

You can also run the AI step on its own: `python3 tools/photo_to_3d.py --photo my_chair.jpg --out my_chair.glb`.

**From a 3D file you already have:** make one on **Meshy** (meshy.ai), the free **TRELLIS.2** demo on Hugging Face, or **Hunyuan3D**, then download it as **.glb**:
```bash
blender -b templates/output/dev_office.blend -P tools/add_furniture.py -- --slot chair --model ~/Downloads/my_chair.glb --save my_room.blend
```
**No 3D model?** Use the photo itself. The kit builds a simple version from basic shapes, using the photo's proportions and colours. Your cat can go in the `pet` slot.
```bash
blender -b templates/output/dev_office.blend -P tools/add_furniture.py -- --slot pet --photo ~/Downloads/my_cat.jpg --save my_room.blend
```
**Then build the portfolio from that room** (to add more pieces first, run add_furniture again on `my_room.blend`):
```bash
blender -b -P tools/build_portfolio.py -- --profile profile.json --blend my_room.blend
```
Options:
- `--turn 90`: the furniture faces the wrong way.
- `--scale 0.9`: a little smaller (anything from `0.5` to `1.5`; it still stands on the floor or hangs on the wall).
- `--colors palette`: flat room colours. `match` (the default) keeps the model's detail but tints it toward the room's colours; `original` changes nothing.
- `--save my_room.blend`: save to a new file and keep the original room untouched (without it, the room file you opened is changed).

> If you made a model on Meshy's free web plan, credit Meshy (CC BY licence). Paid plans and the API (`--ai meshy`) don't need credit. The free Hugging Face demo and fal.ai use TRELLIS, which is free for commercial use (MIT licence).

## 5. Change the room itself
Open a script in `templates/` and edit only the lines between `SETTINGS` and `END OF SETTINGS`:
- `THEME` and the colours in `THEMES` (hex codes)
- room size
- light warmth: 2500 K is a sunset glow, 6500 K is cool daylight
- `SEED`
- camera angle

Then run the script:
```bash
blender -b -P templates/dev_office.py
```
Or inside Blender: **Scripting** tab → **Open** → **Run Script** → press **F12** to render.

## If something goes wrong
- **"command not found: blender"**: use the full path from step 1.
- **"No slot 'xyz'"**: the message lists the slots this room has.
- **A project image looks cropped**: images fill each screen or frame like a phone wallpaper. Landscape 16:10 images work best.
- **A long name is shrunk**: names are scaled down to fit the sign. Keep `role` short.
- **The 3D page stays on "loading" or shows an error**: check your internet connection (the 3D engine downloads from the web; some school and office networks block it). Pages made with `--separate-files` must be opened through a web server (see "Make it 3D").
- **`--ai` built a blocky piece instead of an AI model**: read the `[photo-to-3d]` lines above it. They say what was missing: a key, credits, internet, or the free demo's daily limit.
- **The 3D bake is slow**: add `--fast` for a quick, softer version. A Mac with Apple silicon or a PC with an NVIDIA/AMD graphics card bakes much faster than a CPU alone.
- **Made your own room?** Run `blender -b templates/output/<room>.blend -P tools/check_room.py`. It explains anything that would stop the tools working with it. The rules are in `SPEC.md`.
