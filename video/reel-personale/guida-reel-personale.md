# Reel personale · Perché sto costruendo WeSelf

Split-screen Reel for the founder's personal Instagram + Facebook. **Top half:** these visuals. **Bottom half:** you talking. You write the story; the visuals only frame it.

## Speaking outline (you write the words)

1. **Hook** – one line that makes people curious about *you*, not the app. → `clip-01`
2. **The moment** – when you realised this mattered to you. → `clip-02`
3. **What you noticed** – in yourself or in the people close to you. → `clip-03`
4. **The decision** – «così ho iniziato a costruire WeSelf». → `clip-04`
5. **The honest part** – what's been hard, what keeps you going. → `clip-05`
6. **What you want it to be** – one sentence, no feature list. → `clip-06`
7. **Now** – «siamo in beta, cerco persone che la provino con me». → `clip-07`
8. **The ask** – «se ti va, segui il percorso». → `clip-08` (full screen)

Aim for 45–75 seconds. Don't read: keep the bullets next to the phone and talk.

## Files (`export/`)

| File | Size | Use |
|---|---|---|
| `clip-01…07.mp4` | 1080×960, 6 s | Top half. Headline + an illustration from weself.app; everything animates in within ~2 s, then holds still |
| `clip-08.mp4` | 1080×1920, 6 s | Ending, full screen |
| `clip-XX.png` | same | Still version of each clip (backup, or to extend) |
| `sfondo-01…04.png` | 1080×960 | Blank backgrounds (cream + the website's three soft gradients) for your own photos or notes |

**Visual story (from the website's «Sara» scene):** alone under a cloud (`clip-02`) → small steps, the checklist (`clip-05`) → together in the sun (`clip-06`). `clip-06` uses the website's own line: «Il cambiamento arriva comunque. Accogliamolo insieme.» `clip-07` shows the real «Oggi» screen of the app from the website.

## Filming (bottom half)

- Phone **vertical**, 1080×1920, 30 fps, at eye level; light from a window in front of you.
- Frame yourself in the **upper part** of the frame (eyes about ⅓ from the top): only the middle band of your video will be visible in the bottom half.
- Leave a 1-second pause between sections: it makes cutting easy.

## Assembling in CapCut

1. New project, ratio **9:16**. Put your video on the main track.
2. **Transform** your video: scale ~100–110% and move it down so it fills the bottom half (y 960–1920). Your face should sit around y 1150–1400.
3. **Overlay** → add `clip-0X.mp4`, place it in the top half (y 0–960), and line it up with the section you're talking about.
4. If you talk longer than 6 s on a section: split the clip at the end and **freeze frame** the last frame (or add the matching `clip-0X.png` after it).
5. Photos from your journey: put a `sfondo-0X.png` in the top half and your photo on top of it, slightly smaller, maybe tilted 2–3° like a polaroid.
6. Last 4–5 seconds: `clip-08.mp4` **over the whole screen**. You can keep your voice underneath.
7. **Captions:** Text → Auto captions (Italian). Style: font Nunito (or similar rounded sans), weight Black, white text with a navy outline `#1E2B5C`, placed **right on the split line** (y ≈ 960). Check every word.
8. Add music (low, under your voice), export 1080p 30 fps.

## Before posting

- The ending says «È in prova su Android. Scrivimi in privato.» (Android as stated on weself.app). If people should join some other way (link, form, TestFlight), tell me and I'll change it.
- Illustrations, app screenshot, colours and type are taken from www.weself.app (files in `art/`).
- Caption idea: write it like a short diary entry, first person, and end with «@weselfofficial se vuoi seguire il percorso». Tag @weselfofficial in the post.

To change any text: edit `build.py`, then `python3 build.py && node render.cjs` (from this folder) re-renders everything.
