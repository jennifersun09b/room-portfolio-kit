# RoomKit Studio: make your 3D room portfolio without a terminal

RoomKit Studio is a friendly builder that opens in your web browser. You fill in a few forms, pick a room, and Studio makes your portfolio pictures and a clickable website. It runs on your own computer, works offline, and you never need to open Blender yourself.

## Before you start (one time, about 10 minutes)
1. **Install Blender 4.2 or newer.** It's free, from [blender.org/download](https://www.blender.org/download/). Studio uses it in the background. If Studio can't find it, it shows a download button.
2. **Python 3.9 or newer.**
   - **Mac:** if Python is missing, the launcher offers to install it for you.
   - **Windows:** get Python from [python.org](https://www.python.org/downloads/windows/). Tick **"Add python.exe to PATH"** while installing.
   - **Linux:** Python is usually installed already.

## Start Studio
| Computer | What to do |
|---|---|
| Mac | Double-click **Start.command**. The first time, macOS may block it: right-click it, choose **Open**, then **Open** again. |
| Windows | Double-click **Start.bat**. If Windows SmartScreen appears, click **More info**, then **Run anyway**. |
| Linux | Run `./start.sh`, or double-click it and choose **Run in terminal**. |

Your browser opens RoomKit Studio. Keep the small black window open while you work. Close that window when you're finished.

## Make your portfolio in five steps
1. **You & your room.** Pick who it's for: designer, artist, shop, streamer, student, writer, teacher, or couple/gift. The rooms that suit you appear right below, with the best match marked, and Studio fills in the right links and picture sizes. Click a room, then a colour theme. Prefer to browse? Open **All 17 rooms** or **Themed rooms**. **Shuffle the little things** rearranges books and props, so your room looks like no one else's. Nothing is locked.
2. **Your details.** Add your name, what you do, one line about you, and your links (email, website, Behance, Instagram, Etsy, Ko-fi, Twitch and more). Studio tells you straight away if your name is too long for the room's sign. You can turn on your own brand colour if you like.
3. **Your projects.** Drag pictures of your work onto the page, then give each one a title, a sentence and a link. Drag the handle to change the order. The first project goes on the main screen. Wide pictures (16:10) look best.
4. **Make it yours** (optional). Swap any piece of furniture for your own. Drop in a photo of your chair, plant or pet, or a 3D model (.glb, .obj, .fbx or .stl). For a photo, choose how Studio builds it:
   - **AI 3D model** (best look): needs a key from an AI service. Paste it under **Settings**.
   - **Quick blocky version**: free and instant, made from simple shapes in your photo's colours.

   You can also turn the piece, resize it, and choose whether it matches the room's colours.
5. **Build & publish.**
   1. Start with a **Quick preview**, about a minute, to check everything. Then make **Final quality** for sharing.
   2. Leave **Include the 3D website** on if you want visitors to turn and click your room.
   3. Tick the picture sizes you need: link preview, Instagram, LinkedIn banner, Behance, Dribbble, story, or 4K stream background.

   A progress bar shows each step and the time left. You can cancel at any time. Your previous results stay safe until a new build finishes.

When it's done you'll see your picture and these buttons: **Open 3D website**, **Open 2D site**, **Open folder** and **Download .zip**.

## Put it online for free
**Netlify Drop (easiest)**
1. Click **Open folder**. The `output` folder is your whole website.
2. Go to [app.netlify.com/drop](https://app.netlify.com/drop) and drag the folder onto the page.
3. Create a free account to keep the site. Unclaimed sites are deleted after about an hour.

**GitHub Pages**
1. Create a public repository named `yourname.github.io`.
2. Upload everything inside `output`.
3. Turn on **Settings → Pages**.

Studio shows both checklists step by step, with a **Copy checklist** button.

## Where your things are saved
- **Projects:** `RoomKit Projects` in your home folder. Each project has its own folder:
  - `profile.json`: your details
  - `images/`: your project pictures
  - `furniture/`: your furniture photos and models
  - `output/`: your website and pictures
- **Coming back later:** open Studio again. Your last project opens where you left off, and you can rebuild any time.
- **AI keys:** saved only on your computer in `.roomkit/keys.json` in your home folder, readable only by you. They are never put in a project or on your website.

## AI 3D models: costs and licences
- **Meshy:** about $0.30–0.60 per model. API keys need a Meshy Pro plan.
- **fal.ai:** from about $0.02 per model, pay as you go.
- **Hugging Face:** free, best effort, about 1–2 models a day.
- **Demo model:** lets you try the whole flow without a key.

Each model is made once and reused when you rebuild, so you only pay once. Models made on Meshy's free plan are licensed CC BY, so credit Meshy on your site.

## If something goes wrong
Studio explains problems in plain words, for example "Your computer ran out of memory: close other apps, or choose Quick preview". Click **Details** to see the full technical log if you need to ask for help. Common fixes:
- **"Blender needed":** install Blender 4.2+, then press **Check again**. If Blender is somewhere unusual, paste its location under **Settings → Blender**.
- **The page says Studio has stopped:** start it again with the launcher, then reload the page.
- **iPhone photos won't load (outside a Mac):** on the iPhone, choose **Settings → Camera → Formats → Most Compatible**, or export the photos as JPG.

## For power users
- **Start options:** `python3 tools/studio.py --workspace "/path/to/projects" --port 8800 --no-browser`
- **A specific Blender:** `python3 tools/studio.py --blender "/Applications/Blender 4.2.app"` uses exactly that copy (or set the `BLENDER` environment variable, or choose it under **Settings → Blender**).
- **Command-line builds:** each project's `profile.json` works with `tools/build_portfolio.py`. See GUIDE.md.
- **New rooms:** rooms added to `templates/` appear in Studio automatically. To refresh the room list by hand, run `python3 tools/make_manifest.py`.
- **Security:** Studio listens only on `127.0.0.1` and rejects requests from other websites.
