"""Build reel.html for the «Dove sentiamo le emozioni» Reel (Volynets et al., 2020).

Voice text = final script saved by the founder in the Claude editor (copione.html).
Run: python3 video/mappe-emozioni/build_reel.py  ->  video/mappe-emozioni/reel.html
Render: node tools/render-video.cjs video/mappe-emozioni/reel.html video/mappe-emozioni/weself-mappe-emozioni-reel.mp4 <END> 30
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

SCENES = [
    ("hook", "Dove sentiamo le emozioni?"),
    ("studio", "Un gruppo di ricercatori finlandesi ha chiesto a quasi 4.000 persone, in 101 paesi, di colorare su una sagoma dove sentono un'emozione: in rosso dove qualcosa si attiva, in blu dove si spegne."),
    ("diverse", "Il risultato: ogni emozione è stata percepita nel corpo in modo diverso, e queste mappe si sono somigliate in tutto il mondo."),
    ("mappe", "La rabbia si è accesa in testa, nel petto e nelle mani. La paura nel petto. Il disgusto in gola e nello stomaco. La tristezza ha svuotato braccia e gambe. L'amore e la felicità, invece, hanno acceso tutto il corpo ma con intensità diverse."),
    ("mondo", "E queste mappe si sono somigliate moltissimo da un paese all'altro. A fare la differenza è stata l'emozione, molto più della cultura, del sesso o del titolo di studio. E non contava dove si vive, né quanto si è alti o pesanti."),
    ("eta", "L'unica differenza importante è stata l'età: con gli anni, le sensazioni sono diventate più tenui."),
    ("perche", "Perché? Secondo gli autori, un'espressione del volto si può imparare guardando gli altri, il battito del cuore no. Per questo ciò che sentiamo nel corpo sarebbe meno legato alla cultura."),
    ("opinione", "Sembra banale: chi di noi non ha percepito sul proprio corpo un'emozione… ma avere maggiore consapevolezza su cosa percepiamo fisiologicamente potrebbe aiutarci anche a migliorare le nostre decisioni senza saltare a conclusioni affrettate. Magari non è fame quella che stai provando..."),
    ("fine", "La prossima volta che provi un'emozione, chiediti dove la senti. È un modo per ascoltarti. Il link è in bio."),
]
WPS = 2.5  # calm conversational pace (words per second)


def dur(text):
    return max(4.0, round(len(text.split()) / WPS + 1.5, 1))


def chunks(text, limit=110):
    """Split the voice text into short subtitle chunks at sentence/clause breaks."""
    parts = re.split(r"(?<=[.?!…:;])\s+", text)
    out, cur = [], ""
    for p in parts:
        if len(p) > limit and "," in p:
            sub = re.split(r"(?<=,)\s+", p)
        else:
            sub = [p]
        for s in sub:
            if cur and len(cur) + 1 + len(s) > limit:
                out.append(cur)
                cur = s
            else:
                cur = (cur + " " + s).strip()
    if cur:
        out.append(cur)
    return out


T, caps, t = {}, [], 0.0
for sid, text in SCENES:
    d = dur(text)
    T[sid] = round(t, 2)
    cs = chunks(text)
    total = sum(len(c) for c in cs)
    a = t + 0.35
    span = d - 0.7
    for c in cs:
        b = a + span * len(c) / total
        caps.append([round(a, 2), round(b, 2), c])
        a = b
    t += d
END = round(t, 1)

html = open(os.path.join(HERE, "reel_template.html")).read()
html = html.replace("/*__T__*/", "const T=" + json.dumps(T) + ", END=" + str(END) + ";")
html = html.replace("/*__CAPS__*/", "const CAPS=" + json.dumps(caps, ensure_ascii=False) + ";")
open(os.path.join(HERE, "reel.html"), "w").write(html)
print("END", END)
for sid, _ in SCENES:
    print(sid, T[sid])
