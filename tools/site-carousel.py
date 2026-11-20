# Builds a carousel in the weself.app style from <folder>/testi.json -> <folder>/slides.html
# Usage: python3 tools/site-carousel.py carosselli/cofondatore && node tools/render.cjs carosselli/cofondatore weself-cofondatore
# Text markup in testi.json: *parola* = accent colour (brick), WESELF = coloured wordmark.
import json, re, sys, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
folder = pathlib.Path(sys.argv[1]).resolve()
data = json.loads((folder / "testi.json").read_text())
rel = lambda p: pathlib.Path("../.." if folder.parent.name else "..") / p  # folder is carosselli/<name>

def md(t):
    t = t.replace("WESELF", '<b class="wm"><b class="we">We</b><b class="self">Self</b></b>')
    t = re.sub(r"\*(.+?)\*", r"<em>\1</em>", t)
    return t.replace("\n", "<br>")

def art(name):
    s = (root / "brand/site-art" / f"{name}.svg").read_text()
    return s.replace("<svg ", '<svg class="ill" ', 1)

def visual(v):
    if not v: return ""
    if v == "phone":
        return f'''<div class="card g-sea phonecard"><div class="phone"><img src="{rel('brand/site-art/app-oggi.jpg')}" alt=""></div>
<span class="chip c1"><svg viewBox="0 0 24 24"><path d="M5 12.5 L10 17.5 L19 7"/></svg>Passo fatto</span>
<span class="chip c3"><b class="dot"></b>In prova su Google Play</span></div>'''
    name, _, grad = v.partition(":")
    return f'<div class="card {grad or "g-sea"}">{art(name)}</div>'

N = len(data["slides"])
out = [(root / "tools/site-carousel.css").read_text().replace("FONTS", str(rel("fonts")))]
for i, s in enumerate(data["slides"], 1):
    t = s["type"]
    cls = {"cta": "cta", "honest": "warm"}.get(t, "")
    h = [f'<section class="slide {cls}" id="s{i}">',
         f'<div class="top"><span class="brand"><img src="{rel("templates/carousel/weself-mark.png")}" alt=""><span><b class="we">We</b><b class="self">Self</b></span></span><span class="count">{i}/{N}</span></div>',
         '<div class="main">']
    if s.get("kicker"): h.append(f'<p class="kick">{md(s["kicker"])}</p>')
    tag = "h1" if t in ("cover", "cta") else "h2"
    if s.get("title"): h.append(f'<{tag}>{md(s["title"])}</{tag}>')
    if s.get("text"): h.append(f'<p class="body">{md(s["text"])}</p>')
    if s.get("items"):
        h.append('<ul class="items">' + "".join(f'<li><i><svg viewBox="0 0 24 24"><path d="M5 12.5 L10 17.5 L19 7"/></svg></i><span>{md(x)}</span></li>' for x in s["items"]) + "</ul>")
    if s.get("steps"):
        h.append('<ol class="steps">' + "".join(f'<li><b>{md(a)}</b><span>{md(b)}</span></li>' for a, b in s["steps"]) + "</ol>")
    if s.get("timeline"):
        h.append('<ol class="tl">' + "".join(f'<li class="{st}"><small>{md(w)}</small><b>{md(a)}</b><span>{md(b)}</span></li>' for w, st, a, b in s["timeline"]) + "</ol>")
    if s.get("note"): h.append(f'<div class="note">{md(s["note"])}</div>')
    if s.get("buttons"): h.append('<div class="btns">' + "".join(f'<span class="btn">{md(b)}</span>' for b in s["buttons"]) + "</div>")
    h.append(visual(s.get("visual")))
    h.append("</div>")
    foot = s.get("foot", data.get("foot", ""))
    h.append(f'<div class="foot"><span>weself.app</span><span>{md(foot)}</span></div></section>')
    out.append("\n".join(h))
out.append("</body></html>")
(folder / "slides.html").write_text("\n".join(out))
print("wrote", folder / "slides.html")
