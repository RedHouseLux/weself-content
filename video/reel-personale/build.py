# Builds cards.html from template + the website's illustrations in art/
import pathlib, re
d = pathlib.Path(__file__).parent
def art(n): 
    s = (d/'art'/f'{n}.svg').read_text()
    return re.sub(r'<svg ', '<svg class="ill" ', s, count=1)
def words(t, start=.35, step=.12):
    out, i = [], 0
    for tok in re.split(r'(<[^>]+>)', t):
        if tok.startswith('<'): out.append(tok); continue
        for w in tok.replace('WESELF','\x00').split(' '):
            w=w.replace('\x00','<b class="we">We</b><b class="self">Self.</b>')
            if not w: continue
            out.append(f'<span class="w" style="animation-delay:{start+i*step:.2f}s">{w}</span> '); i += 1
    return ''.join(out)
clips = [
 ('c01','', 'UNA STORIA VERA',        'Ti racconto perché ho <em>iniziato.</em>', 'founder', 'g-sea'),
 ('c02','', '1 · TUTTO È INIZIATO',   'Tutto è iniziato <em>così.</em>', 'sara-0', 'g-warm'),
 ('c03','', '2 · QUELLO CHE HO VISTO','Ho notato <em>una cosa.</em>', 'people', 'g-we'),
 ('c04','', '3 · LA SCELTA',          'Così ho iniziato a costruire WESELF', 'meet', 'g-sea'),
 ('c05','', '4 · DIETRO LE QUINTE',   'La parte che <em>non si vede.</em>', 'sara-1', 'g-we'),
 ('c06','long', '5 · DOVE VOGLIO ARRIVARE','Il cambiamento arriva comunque. <em>Accogliamolo insieme.</em>', 'sara-3', 'g-warm'),
]
html = [(d/'head.html').read_text()]
for cid, cls, kick, h, a, g in clips:
    html.append(f'''<section class="clip {cls}" id="{cid}"><p class="kick">{kick}</p><h1>{words(h)}</h1>
<div class="card {g}">{art(a)}</div></section>''')
html.append(f'''<section class="clip long l2" id="c07"><p class="kick peri">6 · OGGI</p><h1>{words('Siamo in beta. Cerco persone che la <em>provino con me.</em>')}</h1>
<div class="card g-sea phonecard"><div class="phone"><img src="art/app-oggi.jpg" alt=""></div>
<span class="chip c1"><svg viewBox="0 0 24 24"><path d="M5 12.5 L10 17.5 L19 7"/></svg>Passo fatto</span>
<span class="chip c2">Come stai?<i></i><i></i><i class="on"></i><i></i></span>
<span class="chip c3"><b class="dot"></b>In prova su Android</span></div></section>''')
html.append(f'''<section class="clip full" id="c08"><p class="kick">SE TI VA</p><h1 class="xl">{words('Segui il <em>percorso.</em>')}</h1>
<div class="heroart">{art('hero')}</div>
<div class="handle w" style="animation-delay:1.6s">@weselfofficial</div>
<div class="chans w" style="animation-delay:1.8s"><span>Instagram</span><span>Facebook</span></div>
<div class="beta w" style="animation-delay:2.1s"><b>Vuoi provarla in anteprima?</b><span>È in prova su Android. Scrivimi in privato.</span></div>
<div class="mark w" style="animation-delay:2.4s"><img src="weself-mark.png" alt=""><span><b class="we">We</b><b class="self">Self</b></span></div></section>''')
for i, g in enumerate(['', 'g-sea', 'g-we', 'g-warm'], 1):
    html.append(f'<section class="clip bg {g}" id="b0{i}"></section>')
html.append('<script>document.querySelectorAll(".ill").forEach(s=>{[...s.children].forEach((c,i)=>{c.classList.add("pop");c.style.animationDelay=(0.75+i*0.07)+"s"})})</script></body></html>')
(d/'cards.html').write_text('\n'.join(html))
