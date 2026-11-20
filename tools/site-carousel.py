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
    if v == "days":
        cols = ["#4A5BE8", "#F09B7C", "#1E9E9E"]
        person = lambda c: f'<svg viewBox="0 0 40 56"><circle cx="20" cy="12" r="10" fill="{c}"/><path d="M3 56 C3 36 11 27 20 27 C29 27 37 36 37 56 Z" fill="{c}"/></svg>'
        ppl = "".join(person(cols[i % 3]) for i in range(12))
        days = "".join(f'<i>{d}</i>' for d in range(1, 15))
        return f'''<div class="card g-sea daycard"><div class="ppl">{ppl}</div><small>almeno 12 persone</small><div class="days">{days}</div><small>14 giorni di fila</small></div>'''
    if v == "cofounder":
        P = "M3 56 C3 36 11 27 20 27 C29 27 37 36 37 56 Z"
        svg = f'''<svg class="ill cof" viewBox="0 0 560 420">
<circle cx="280" cy="230" r="182" fill="#DDE0FB"/>
<circle cx="440" cy="330" r="70" fill="#FBE3D8"/>
<circle cx="180" cy="245" r="92" fill="#A8E6DD"/>
<circle cx="380" cy="245" r="92" fill="#fff" stroke="#4A5BE8" stroke-width="4" stroke-dasharray="10 12"/>
<path d="M228 205 Q280 150 332 205" fill="none" stroke="#4A5BE8" stroke-width="4" stroke-dasharray="2 12" stroke-linecap="round"/>
<path d="M280 128 C268 118 256 110 256 98 C256 89 263 82 271 82 C275 82 278 84 280 88 C282 84 285 82 289 82 C297 82 304 89 304 98 C304 110 292 118 280 128 Z" fill="#A64A30"/>
<g transform="translate(140 186) scale(2)"><circle cx="20" cy="12" r="10" fill="#1E9E9E"/><path d="{P}" fill="#1E9E9E"/></g>
<g transform="translate(340 186) scale(2)"><path d="{P}" fill="none" stroke="#4A5BE8" stroke-width="2" stroke-dasharray="4 4"/></g>
<text x="380" y="228" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="58" fill="#4A5BE8">?</text>
<circle cx="96" cy="120" r="9" fill="#F09B7C"/><circle cx="478" cy="132" r="7" fill="#1E9E9E"/><circle cx="120" cy="360" r="6" fill="#4A5BE8"/>
</svg>'''
        return f'''<div class="card g-sea cofcard">{svg}
<span class="chip k1"><svg viewBox="0 0 24 24"><path d="M5 12.5 L10 17.5 L19 7"/></svg>L'app c'è</span>
<span class="chip k2"><b class="dot pe"></b>Chi studia la mente</span></div>'''
    if v == "seat":
        P = "M3 56 C3 36 11 27 20 27 C29 27 37 36 37 56 Z"
        svg = f'''<svg class="seat" viewBox="0 0 900 560">
<defs><radialGradient id="glow"><stop offset="0" stop-color="#F09B7C" stop-opacity=".55"/><stop offset="1" stop-color="#F09B7C" stop-opacity="0"/></radialGradient></defs>
<circle cx="610" cy="300" r="300" fill="url(#glow)"/>
<circle cx="260" cy="330" r="150" fill="#1E9E9E" opacity=".28"/>
<circle cx="610" cy="320" r="190" fill="none" stroke="#F09B7C" stroke-width="7" stroke-dasharray="18 18" stroke-linecap="round"/>
<path d="M350 250 Q440 150 520 230" fill="none" stroke="#fff" stroke-width="6" stroke-dasharray="2 18" stroke-linecap="round" opacity=".8"/>
<path d="M440 150 C424 137 408 127 408 111 C408 99 417 90 428 90 C433 90 437 93 440 98 C443 93 447 90 452 90 C463 90 472 99 472 111 C472 127 456 137 440 150 Z" fill="#F09B7C"/>
<g transform="translate(190 250) scale(3.5)"><circle cx="20" cy="12" r="10" fill="#1E9E9E"/><path d="{P}" fill="#1E9E9E"/></g>
<g transform="translate(520 210) scale(4.5)"><path d="{P}" fill="#F09B7C" fill-opacity=".12" stroke="#F09B7C" stroke-width="1.6" stroke-dasharray="3 3"/></g>
<text x="610" y="300" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="130" fill="#F09B7C">?</text>
<circle cx="120" cy="120" r="10" fill="#A8E6DD"/><circle cx="840" cy="110" r="8" fill="#DDE0FB"/><circle cx="90" cy="480" r="7" fill="#F09B7C"/>
</svg>'''
        return f'''<div class="seatwrap">{svg}<span class="tag">POSTO LIBERO</span>
<span class="chip k3"><svg viewBox="0 0 24 24"><path d="M5 12.5 L10 17.5 L19 7"/></svg>L'app c'è</span></div>'''
    if v == "logo":
        return f'''<div class="logocard"><img src="{rel('brand/logo/weself-heart-original.png')}" alt=""><span class="wm"><b class="we">We</b><b class="self">Self</b></span></div>'''
    if v == "phone":
        return f'''<div class="card g-sea phonecard"><div class="phone"><img src="{rel('brand/site-art/app-oggi.jpg')}" alt=""></div>
<span class="chip c1"><svg viewBox="0 0 24 24"><path d="M5 12.5 L10 17.5 L19 7"/></svg>Passo fatto</span>
<span class="chip c3"><b class="dot"></b>In test su Google Play</span></div>'''
    name, _, grad = v.partition(":")
    return f'<div class="card {grad or "g-sea"}">{art(name)}</div>'

N = len(data["slides"])
out = [(root / "tools/site-carousel.css").read_text().replace("FONTS", str(rel("fonts")))]
for i, s in enumerate(data["slides"], 1):
    t = s["type"]
    cls = {"cta": "cta", "honest": "warm"}.get(t, "") + (" " + s["theme"] if s.get("theme") else "")
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
    if s.get("buttons"): h.append('<div class="btns">' + "".join(f'<span class="btn">{md(b)}</span>' for b in s["buttons"]) + "</div>")
    if s.get("small"): h.append(f'<p class="small">{md(s["small"])}</p>')
    if s.get("note"): h.append(f'<div class="note">{md(s["note"])}</div>')
    h.append(visual(s.get("visual")))
    h.append("</div>")
    foot = s.get("foot", data.get("foot", ""))
    h.append(f'<div class="foot"><span>weself.app</span><span>{md(foot)}</span></div></section>')
    out.append("\n".join(h))
out.append("</body></html>")
(folder / "slides.html").write_text("\n".join(out))
print("wrote", folder / "slides.html")
