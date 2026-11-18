# WeSelf · LinkedIn

This folder holds WeSelf's **LinkedIn** content. The root `CLAUDE.md` still applies in full (the 4 WeSelf features, every editorial rule, brand colours and type, how carousels are rendered). This file adds only what is specific to LinkedIn. Content is in **Italian**; talk to the founder in the language they write in.

## How this session works with the others

- **Branch:** work and push only on the LinkedIn branch you were given (e.g. `claude/linkedin`). Never commit to the Instagram/Facebook/TikTok branch.
- **Folder:** write only inside `linkedin/`. Shared files (`templates/`, `brand/`, `fonts/`, `tools/`, the root `CLAUDE.md`) are **read-only** here: if one needs a change, propose it to the founder instead of making it.
- **Status:** keep the LinkedIn status table below up to date (not the root one). Before choosing a topic, read the root status table and the Notion pages «Brief · Content» and «Brief · LinkedIn» to avoid posting the same study on the same days as Instagram.
- **Reuse:** a study already verified for Instagram (folder `carosselli/<name>/`, its kit and its numbers) can be adapted for LinkedIn. Re-check the numbers against the kit; do not add new figures without verifying them at the source.

## Audience and tone

- **Who reads:** professionals, managers, HR and people-development teams, teachers and trainers, founders, possible partners.
- **Tone:** competent and warm, never corporate or «guru». Fewer exclamation marks, no growth-hacking formulas («Ecco 5 cose che…»), no emoji walls (at most 1–2 per post).
- **Voice:** company posts speak as WeSelf («noi»). Founder posts may use the **first person** for opinions and experience, always kept separate from what the study found.
- **Third person** for negative information still applies («molti manager», «c'è chi…»); «tu» only for invitations and positive actions.

## Pillars on LinkedIn

1. **Leadership e lavoro in team** (main pillar): e.g. Lacerenza et al. 2017 (`carosselli/leadership/`).
2. **Benessere al lavoro**: stress and switching off (Karabinski et al. 2021, `carosselli/stress/`), phone and attention (Castelo et al. 2025, `carosselli/senza-internet/`).
3. **Abitudini e obiettivi**: if–then plans (Gollwitzer & Sheeran 2006, `carosselli/se-allora/`), WOOP (Wang, Wang & Gai 2021, `video/woop/`).
4. **Relazioni al lavoro**: conversations and feedback (Kardas, Kumar & Epley 2022, `carosselli/come-stai/`).

Avoid on LinkedIn: clinical topics (anxiety as a disorder, addiction), politics, local news, men-vs-women framing.

## Formats

1. **Carousel as PDF document** (the main format)
   - Build it like an Instagram carousel (`templates/carousel/head.html`, `node tools/render.cjs linkedin/<name> weself-li-<name>`), 1080×1350, usually **8–12 slides**.
   - Combine the slides with `python3 tools/pdf.py linkedin/<name> weself-li-<name> linkedin/<name>/weself-li-<name>.pdf`.
   - Give the document a short title (shown above the PDF on LinkedIn).
   - Same mandatory slides as Instagram: «Mito o realtà?», «I limiti», the source on every slide, and a CTA slide.
2. **Text post** (with one image or none)
   - 1,300–2,000 characters. The **first 2 lines (about 210 characters)** must work on their own, because LinkedIn cuts the rest behind «…altro».
   - Short paragraphs; one idea each.
3. **Single image:** 1080×1350 (or 1080×1080), built from the same template.

## Post rules on LinkedIn

- **Link** to weself.app or to the study: put it in the **first comment**, not in the post body (links in the body reduce reach).
- **Source** of the study: name it in the post («Fonte: Autori, anno, rivista») and give the full citation with DOI in the first comment, plus how numbers were converted (U3), as on Instagram.
- **«Un'onestà necessaria»**: one sentence saying the study is not about WeSelf, as always.
- **Hashtags:** 3–5 at the end, in Italian where they exist (#leadership #benesserealavoro #abitudini #WeSelf).
- **Alt text:** add it to every image; for PDFs, describe the document in the post or in the first comment.
- **When to post:** Tuesday–Thursday, 8:00–9:30 or 12:30–13:30. At most 2–3 posts a week.

## Kit for each post

Write `linkedin/<name>/kit-linkedin-<name>.md` with:
- the date and time to post;
- the post text, ready to paste (with the first 2 lines checked);
- the document title (for PDFs);
- the first comment (citation, DOI, number conversion, link);
- alt text;
- reliability notes.

Send the founder the PDF (or image) and the kit. Offer the Claude editor (`tools/editor/`) when the founder wants to rewrite texts themselves.

## Status (LinkedIn)

| Content | Folder | State |
|---|---|---|
| — | — | Not started yet |
