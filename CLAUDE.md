# WeSelf · Content generator

This repository holds WeSelf's social content: carousels, articles, video/Reel kits, the brand assets and the templates to make new ones. The person you work with is the WeSelf founder. Talk to them in the language they write in (often Italian); content is in Italian.

Weekly topic signals come from a separate project (repo `RedHouseLux/weself-listening` and the Notion database **Temi**); this repo is only for making content. Brief, brand book and plan also live in Notion: page **WeSelf · Temi della settimana** → «Brief per nuove sessioni (Claude)», «Brand identity», «Piano editoriale».

## What WeSelf is (describe only these 4 features)

1. **Costruire abitudini sane:** a goal becomes a week of small actions already in the agenda.
2. **Trovare chi ha il tuo obiettivo:** nearby or among the friends you already have.
3. **Una comunità dove ci si sostiene:** small groups, anonymous too.
4. **Uno specialista, se serve:** the user asks for the contact and decides what to show.

Website: https://www.weself.app (Italian /it, articles /it/articles, download /it/install).

## Editorial rules (agreed with the founder; all mandatory)

- **One study (or one survey) per post.** Translate the numbers. Explain what was measured. Exception: a long YouTube video is built around one main study and may cite other studies in support (each verified the same way, all listed in the description).
- **Only verified numbers.** Read the source yourself: PubMed via `eutils.ncbi.nlm.nih.gov` (esearch/efetch return abstracts), Europe PMC (`www.ebi.ac.uk/europepmc/webservices/rest/search`). Journal sites are paywalled; if only the abstract is available, use only what the abstract says and say so in the kit. If a source cannot be reached, say so; never fill gaps.
- **Third person for negative information** («molte persone», «chi da bambino era impulsivo», «c'è chi…»). «Tu» only for invitations and positive actions.
- **Percentages** rather than «x su 100» (e.g. «78%»). Effect sizes (d, g) are converted with Cohen's U3 = Φ(d) and the method is explained in the first comment.
- **Words:** «studi» (not «esperimenti») for the studies in a meta-analysis; the meta-analysis itself is «la ricerca»; avoid «negli studi» for academic performance (use «rendimento», «risultati»).
- **Verb tenses:** past for findings («è risultato», «ha mostrato»), conditional for what was planned («chi avrebbe seguito»), future for what is missing («serviranno»), present only for general truths and for the reader.
- **Full, flowing sentences** on slides; more text is fine.
- **Length:** 8 slides is the usual shape, but add slides whenever a concept needs more explanation to be understood (Instagram and Facebook allow up to 20). One idea per slide beats a crowded slide.
- **Every post has:** a «Mito o realtà?» slide, a «limiti» slide, the source on each slide, «Un'onestà necessaria» in the caption (the study is not about WeSelf), and for sensitive topics (anxiety, loneliness, addiction, stress) a support reference to verify before publishing (medico di base, servizi universitari, Telefono Amico Italia, 112; gambling: Telefono Verde ISS 800 558 822).
- **No clinical promises** (WeSelf never «cura», «tratta», «risolve»). **No political stances.** Never comment on local crime news.

## How to make a carousel

1. Pick the topic (Notion Temi / the founder) and **one** source; verify it (see above).
2. Copy `templates/carousel/head.html` into `carosselli/<name>/` (it holds the brand CSS; fonts are in `/fonts`, referenced relatively) and write `body.html` with `<section class="slide" id="s1">…</section>` per slide (1080×1350). Look at `carosselli/ansia/body.html` and `carosselli/stress/body.html` for the slide types: cover, «La ricerca», numbers, «I numeri, tradotti», «Che cosa ha funzionato», «Mito o realtà?» (`.warmbg` + `.badge.mito`), «I limiti», CTA (`.cta`, peri background).
3. `cat head.html body.html > slides.html`, copy `templates/carousel/weself-mark.png` next to it, then `node tools/render.cjs carosselli/<name> weself-<name>`. It writes the PNGs and flags any OVERFLOW.
4. Look at every slide (make a contact sheet with PIL) before sending.
5. Write `kit-pubblicazione-<name>.md`: when to post, caption IG/FB (+ short TikTok), first comment with the full citation + DOI + how numbers were converted, one alt text per slide, reliability notes.
6. Zip PNGs + kit and send them to the founder.

## «Curiosità» format (hypotheses and theory papers)

Agreed with the founder (Nov 2026) for papers with no data of their own to translate (hypotheses, theory, reviews of ideas). It is the exception to «translate the numbers»; every other rule still applies.

- **Look:** brand dark theme. Build with `cat head.html dark.html body.html > slides.html`, copying `templates/curiosita/dark.html` next to `head.html` (night-navy background with a dotted texture, same fonts, colours and node motif; peri CTA with navy text). See `carosselli/coscienza/`.
- **Label it:** cover pill `<span class="tag"><i></i>Curiosità · un'ipotesi, non un risultato</span>`; the caption opens with «Curiosità · un'ipotesi, non un risultato.»; the source line ends with «(ipotesi)».
- **Wording:** the hypothesis in the conditional («nascerebbe», «sceglierebbe»); evidence the authors cite as theirs («gli indizi che gli autori raccolgono»); say plainly when it goes against the mainstream view and what that view is.
- **Slides:** «Ipotesi o certezza?» replaces «Mito o realtà?» (badge `.badge.dip` «DA VERIFICARE»); «Perché è solo un'ipotesi» replaces «I limiti» (no new data, mainstream view, animal studies, what is hard to measure).
- **Numbers:** none unless they are verified like any other number. Our link to WeSelf goes only on the CTA slide and is declared as ours in «Un'onestà necessaria».
- **Frequency:** at most one every 2–3 weeks; never on clinical advice.

Brand: colours and type are in the CSS of `templates/carousel/head.html` (teal = Self, peri = We, coral = one warm accent per asset; Nunito + Literata). Logos in `brand/logo/`. Full design system: https://claude.ai/artifact/214XU3j96pZnVaHHELpgBa

## Status (7 November 2026)

| Content | Folder | State |
|---|---|---|
| Dunedin study (self-control) — article IT/EN on weself.app, carousel 7 slides | `articoli/`, `carosselli/dunedin/` | Published |
| Ansia da esame — Huntley et al. 2019 | `carosselli/ansia/` | Published |
| Solitudine — sondaggio SWG per Acri e Assifero (ott. 2026) | `carosselli/solitudine/` | Published |
| Stress / staccare dal lavoro — Karabinski et al. 2021 | `carosselli/stress/` | Published |
| Abitudini / quanto tempo serve — Singh et al. 2024 | `carosselli/abitudini/` | Published |
| Amicizia / quante ore per diventare amici — Hall 2019 (pillar Relazioni) | `carosselli/amicizia/` | Published |
| Gentilezza (13 Nov) — Kumar & Epley 2023 (pillar Relazioni) | `carosselli/gentilezza/` | Published |
| Curiosità · coscienza nel tronco encefalico — Devor & Baron 2026 (first «Curiosità» post) | `carosselli/coscienza/` | Published |
| Video YouTube + Reel kit on Dunedin | `video/dunedin/` | Ready, not produced yet |

Open items: a real-life photo for the Dunedin article; the Dunedin article title still uses «te» (founder may want third person); the content plan in `piano/` is v1 and is being redefined around weekly trends (Instagram, Facebook, TikTok; Italy + Caserta/Campania); it now has three recurring pillars (Relazioni incl. couples, Leadership, Umorismo with a lighter tone), see section 3bis.
