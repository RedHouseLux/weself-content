# WeSelf · Meme e fumetti («Scienza da ridere»)

This folder holds WeSelf's **meme and comic** content (Umorismo pillar), made by a dedicated session. The root `CLAUDE.md` still applies in full (the 4 WeSelf features, every editorial rule, brand colours and type). This file adds only what is specific to memes and comics. Content is in **Italian**; talk to the founder in the language they write in.

## How this session works with the others

- **Branch:** work and push only on the meme branch you were given (`claude/meme`). Never commit to the carousel branch or the LinkedIn branch.
- **Folder:** write only inside `meme/`. Shared files (`templates/`, `brand/`, `fonts/`, `tools/`, the root `CLAUDE.md`) are **read-only** here: if one needs a change, propose it to the founder instead of making it.
- **Status:** keep the meme status table below up to date (not the root one). Before choosing a topic, read the root status table and the Notion page «Brief · Content» (Temi della settimana) to stay coherent with the week, and avoid joking on the same day about a topic that a serious post treats.
- **Reuse:** studies already verified for carousels (`carosselli/<name>/`, their kits and numbers) can be reused. Re-check the numbers against the kit; never add a figure that is not verified at the source.

## The column

- **Name:** «Scienza da ridere». **Sticker:** white pill with a laughing flask, `meme/_stile/sticker.html`, top right. **Background:** WeSelf teal (#1E9E9E). **Title:** Nunito 900, white, dark offset shadow (`text-shadow:5px 5px 0 #1E2B5C`).
- **Shape:** one image 1080×1350 for Instagram/Facebook (often a 4-panel strip), plus an optional animated version 1080×1920, 8–15 s, no voice-over, for Reels/TikTok (`window.render(t)` + `node tools/render-video.cjs`). Keep text between 220 and 1480 px from the top in the Reel.
- **Frequency:** about one a week. Never on loneliness, anxiety, grief, addiction or other sensitive topics; never on awareness days (e.g. 25 November); no political or local-news jokes.

## What makes it work (founder's feedback, Nov 2026)

1. **Shareable first:** an everyday situation anyone recognises in themselves or a friend, so they tag/send/repost it. No inside jokes about WeSelf (followers, our posts, our app): WeSelf is only the signature.
2. **Funny, never blaming:** we laugh *with* people at the situation. Characters fail together and find absurd excuses; nobody scolds anybody. Self-irony in first person («io») is allowed.
3. **The drawing tells the joke:** illustrations take most of the space and must be funny on their own. Never explain the joke on the image: only the setup line, short labels/bubbles inside the drawing and a short source line.
4. **A gag in every panel:** exaggeration, visual joke, absurd detail, deadpan line; the last panel is the punchline (ideally calling back an earlier line).
5. **Coherent story and setting:** one recognisable place (same living room, same sofa, same clock), objects that are used and make sense where they are, time shown consistently (clock, window light).
6. **Highlights and colours:** highlighted text is orange (#D9592A; light orange #FFB48C on teal/blue). Speech bubbles white or light tints, Nunito 900, navy text.

## Science in a meme

- One verified study per post, like every other post. The fact lives **inside the drawing** (a label, a count, e.g. 3 faces out of 13 = 23%) plus «Fonte: Autore, anno» at the bottom.
- The explanation of the study, «Mito o realtà?», «I limiti» and «Un'onestà necessaria» go in the **caption**; the full citation + DOI and how numbers were read go in the **first comment**.
- Kit per meme: `meme/<name>/kit-pubblicazione-meme-<name>.md` with date/time, caption IG/FB, short caption Reel/TikTok, first comment, alt text (image + Reel), reliability notes.

## Characters and visuals

- **Our own characters, never someone else's.** Take inspiration from how famous strips work (two inner voices with opposite characters, a recurring distractor, a callback punchline), never copy their characters or style (e.g. «Heart and Brain» by The Awkward Yeti is protected). No screenshots from films, TV, music videos or other creators. Classic meme images only if they are licensed stock photos (e.g. from Canva) chosen by the founder.
- **Recurring WeSelf cast (3D, clay look, no AI):**
  - **Agenda:** teal notebook with glasses and rings, organised, kind.
  - **Voglia:** coral ball with a flame tuft, impulsive, enthusiastic.
  - **Notifica:** small yellow bell, the distractor.
  - Both main characters have soft limbs in their own colour, mitten hands, white sneakers, eyebrows and shiny eyes (founder: «less creepy, more human»). They are accomplices, not teacher and pupil.
- **3D pipeline:** `meme/agenda-voglia/3d/scene.html` (character kit, living room with window by time of day, wall clock, sofa, TV on cabinet, rug, plant, lamp; one panel per `?p=N`). Setup once: `cd meme/agenda-voglia/3d && npm init -y && npm install three@0.160.0`. Render: `node meme/agenda-voglia/3d/render.cjs` (writes `p1.png`…`p4.png`). Layout and bubbles: `meme/agenda-voglia-3d/build.py`, then `cat head.html body.html > slides.html` and `node tools/render.cjs meme/<name> weself-meme-<name>`.
- Other styles used so far (2D, SVG): chat screenshots drawn by us, stage/spotlight scenes with emoji audiences, 4-panel cartoons with animals (cat). Comics may use stylised humans and animals (founder's choice).

## Status (Meme)

| Content | Folder | State |
|---|---|---|
| «Dobbiamo vederci!» — Hall 2019 (chat; image + 16 s Reel, kit ready) | `meme/dobbiamo-vederci/` | Ready, not published (Thu 26 Nov) |
| «Agenda e Voglia» — Gollwitzer & Sheeran 2006 (3D strip, accomplices version) | `meme/agenda-voglia-3d/` | Draft: kit and Reel to do |
| «Io dopo un errore di battitura» — Gilovich et al. 2000 (spotlight, emoji audience) | `meme/errore-battitura/` | Draft: kit and Reel to do |
| «Io e le nuove abitudini» (cat) — Singh et al. 2024 | `meme/gatto-abitudine/` | Draft (2D) |
| «Io dopo una bella chiacchierata» (cups) — Boothby et al. 2018 | `meme/chiacchierata/` | Draft (2D, needs more gags) |
| «Lo prendo solo un attimo» — Castelo et al. 2025 | `meme/attimo/` | Draft (2D) |
| «Da lunedì inizio» — Gollwitzer & Sheeran 2006 | `meme/da-lunedi/` | Draft (2D) |
| «Pochi follower» | `meme/pochi-follower/` | Discarded (inside joke) |
