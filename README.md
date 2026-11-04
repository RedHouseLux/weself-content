# weself-content

WeSelf's social content and the tools to make it.

| Folder | What |
|---|---|
| `carosselli/` | One folder per carousel: source HTML (`body.html`, `slides.html`), the PNG slides and the publishing kit |
| `templates/carousel/` | Brand stylesheet (`head.html`) and logo mark for new carousels |
| `tools/render.cjs` | Renders a carousel's slides to PNG: `node tools/render.cjs carosselli/<name> weself-<name>` |
| `fonts/` | Nunito and Literata (used by every HTML file through relative paths) |
| `brand/logo/` | WeSelf logos: horizontal, vertical, square, avatar; light, dark, transparent |
| `articoli/` | Articles (Markdown) |
| `video/` | Video and Reel production kits |
| `piano/` | Content plan (v1) |

Rendering needs Node and Playwright with Chromium. The rules and the workflow are in `CLAUDE.md`.
