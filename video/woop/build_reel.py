"""Build reel.html for the WOOP Reel «Dal volere al fare, in quattro passi» (Wang, Wang & Gai, 2021).

Voice text = final script saved by the founder in the Claude editor (copione.html).
Run: python3 video/woop/build_reel.py  ->  video/woop/reel.html
Render: node tools/render-video.cjs video/woop/reel.html video/woop/weself-woop-reel.mp4 <END> 30
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

SCENES = [
    ("hook", "Volere non basta. C'è un metodo in quattro passi che aiuta a passare dal volere al fare: desiderio, risultato, ostacolo, piano."),
    ("problema", "Molte persone partono con un buon proposito, immaginano già il traguardo… e poi si fermano al primo ostacolo."),
    ("desiderio", "Primo, il desiderio: scegli una cosa che desideri e che puoi davvero ottenere, per esempio camminare tre volte questa settimana."),
    ("risultato", "Secondo, il risultato: immagina il momento più bello in cui ci sei riuscito."),
    ("ostacolo", "Terzo, l'ostacolo: chiediti che cosa, dentro di te, potrebbe fermarti. La stanchezza, la pigrizia, il telefono."),
    ("piano", "Quarto, il piano: «se arriva quell'ostacolo, allora faccio questo». Per esempio: «se torno stanco, allora esco comunque per dieci minuti»."),
    ("ricerca", "Una ricerca del 2021 ha messo insieme 24 studi su questo metodo, con studenti, adulti e bambini, per obiettivi di salute, di studio e personali."),
    ("esito", "In media, chi ha usato il metodo ha ottenuto risultati migliori!"),
    ("opinione", "Secondo me, prima ancora del desiderio viene il perché: chiedersi perché lo voglio davvero. Quando un obiettivo è mio, e non un «dovrei», trovo più facilmente la forza di affrontare l'ostacolo. Aggiungere il perché come primo passo, però, la scienza non l'ha ancora messo alla prova."),
    ("fine", "Prova adesso: un desiderio, il risultato, l'ostacolo, il piano. Quattro passi, un esercizio breve. Il link è in bio."),
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
