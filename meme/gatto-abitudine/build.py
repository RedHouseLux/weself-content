import math
st=open('/home/user/weself-content/meme/_stile/sticker.html').read()
OR,DK="#F2A65A","#C9772E"
def cat(x,y,s=1.0,face="happy",band=False,flip=False,stars=False):
    sx=-s if flip else s
    g=[f'<g transform="translate({x} {y}) scale({sx} {s})">']
    g.append(f'<path d="M58 40 q60 -10 50 -70" fill="none" stroke="#1E2B5C" stroke-width="18" stroke-linecap="round"/><path d="M58 40 q60 -10 50 -70" fill="none" stroke="{OR}" stroke-width="10" stroke-linecap="round"/>')
    g.append(f'<ellipse cx="0" cy="40" rx="62" ry="56" fill="{OR}" stroke="#1E2B5C" stroke-width="5"/><ellipse cx="0" cy="52" rx="34" ry="34" fill="#FFE6CC"/>')
    g.append(f'<path d="M-56 -60 L-48 -118 L-16 -88 Z" fill="{OR}" stroke="#1E2B5C" stroke-width="5" stroke-linejoin="round"/><path d="M56 -60 L48 -118 L16 -88 Z" fill="{OR}" stroke="#1E2B5C" stroke-width="5" stroke-linejoin="round"/>')
    g.append(f'<circle cx="0" cy="-50" r="58" fill="{OR}" stroke="#1E2B5C" stroke-width="5"/>')
    g.append(f'<path d="M-18 -104 q18 -6 36 0" fill="none" stroke="{DK}" stroke-width="6" stroke-linecap="round"/>')
    if stars:
        for cx in (-21,21):
            pts=" ".join(f"{cx+ (14 if i%2==0 else 6)*math.cos(math.pi*i/5-math.pi/2):.1f},{-56+(14 if i%2==0 else 6)*math.sin(math.pi*i/5-math.pi/2):.1f}" for i in range(10))
            g.append(f'<polygon points="{pts}" fill="#FFD23F" stroke="#1E2B5C" stroke-width="3"/>')
        g.append('<path d="M-20 -34 q20 26 40 0z" fill="#1E2B5C"/><path d="M-10 -26 q10 8 20 0" fill="#F09B7C"/>')
    elif face=='smug':
        g.append('<path d="M-32 -56 h20 M12 -56 h20" stroke="#1E2B5C" stroke-width="6" stroke-linecap="round"/><path d="M-14 -34 q20 10 30 -6" fill="none" stroke="#1E2B5C" stroke-width="5" stroke-linecap="round"/>')
    elif face=='run':
        g.append('<circle cx="-20" cy="-56" r="7" fill="#1E2B5C"/><circle cx="20" cy="-56" r="7" fill="#1E2B5C"/><path d="M-14 -36 q14 14 28 0" fill="#1E2B5C"/>')
    g.append('<path d="M-4 -44 h8 l-4 6z" fill="#F09B7C" stroke="#1E2B5C" stroke-width="2"/>')
    g.append('<path d="M-60 -44 h-26 M-60 -36 h-24 M60 -44 h26 M60 -36 h24" stroke="#1E2B5C" stroke-width="3" stroke-linecap="round"/>')
    if band: g.append('<path d="M-56 -78 q56 -22 112 0 l-2 14 q-54 -20 -108 0z" fill="#D9592A" stroke="#1E2B5C" stroke-width="4"/>')
    g.append('</g>'); return ''.join(g)
def melted(x,y):
    # cat poured over the sofa like a puddle
    return (f'<g transform="translate({x} {y})">'
      f'<path d="M-150 30 q-20 -40 30 -50 q40 -40 90 -10 q60 -30 110 0 q50 -6 60 30 q20 30 -20 40 h-240 q-40 0 -30 -10z" fill="{OR}" stroke="#1E2B5C" stroke-width="5"/>'
      f'<path d="M-70 -42 L-62 -86 L-40 -60Z" fill="{OR}" stroke="#1E2B5C" stroke-width="5" stroke-linejoin="round"/><path d="M-10 -46 L-6 -88 L14 -58Z" fill="{OR}" stroke="#1E2B5C" stroke-width="5" stroke-linejoin="round"/>'
      f'<path d="M-62 -18 h18 M-22 -20 h18" stroke="#1E2B5C" stroke-width="5" stroke-linecap="round"/><path d="M-44 0 q10 6 20 0" fill="none" stroke="#1E2B5C" stroke-width="4" stroke-linecap="round"/>'
      f'<path d="M-86 -40 q50 -22 100 0 l-2 12 q-48 -18 -96 0z" fill="#D9592A" stroke="#1E2B5C" stroke-width="4" transform="translate(0 14) rotate(8)"/>'
      f'<path d="M120 -6 q30 0 40 20" fill="none" stroke="#1E2B5C" stroke-width="12" stroke-linecap="round"/><path d="M120 -6 q30 0 40 20" fill="none" stroke="{OR}" stroke-width="6" stroke-linecap="round"/>'
      f'</g>')
def bubble(x,y,w,h,lines,fs=24,tail_left=True,think=False):
    t=''.join(f'<text x="{x+w/2}" y="{y+(h-len(lines)*fs*1.2)/2+fs+i*fs*1.2:.1f}" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="{fs}" fill="#1E2B5C">{l}</text>' for i,l in enumerate(lines))
    tx=x+w*(0.3 if tail_left else 0.7)
    if think:
        tl=f'<circle cx="{tx}" cy="{y+h+16}" r="10" fill="#fff" stroke="#1E2B5C" stroke-width="4"/><circle cx="{tx-12}" cy="{y+h+38}" r="6" fill="#fff" stroke="#1E2B5C" stroke-width="4"/>'
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2.2:.0f}" fill="#fff" stroke="#1E2B5C" stroke-width="5"/>{tl}{t}'
    tl=f'<path d="M{tx-14} {y+h-3} L{tx+(-26 if tail_left else 26)} {y+h+30} L{tx+14} {y+h-3}" fill="#fff" stroke="#1E2B5C" stroke-width="5" stroke-linejoin="round"/><rect x="{tx-16}" y="{y+h-10}" width="32" height="12" fill="#fff"/>'
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="#fff" stroke="#1E2B5C" stroke-width="5"/>{tl}{t}'
def emo(x,y,e,fs=50): return f'<text x="{x}" y="{y}" font-family="Noto Color Emoji" font-size="{fs}">{e}</text>'
W,H=470,500
def panel(inner,label,bg): return f'<div class="pnl" style="background:{bg}"><span class="time">{label}</span><svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">{inner}</svg></div>'
ground='<rect x="0" y="440" width="470" height="60" fill="#A8E6DD"/>'
clock=('<g transform="translate(395 120)"><circle r="46" fill="#fff" stroke="#1E2B5C" stroke-width="5"/><circle cx="-34" cy="-40" r="14" fill="#D9592A" stroke="#1E2B5C" stroke-width="4"/><circle cx="34" cy="-40" r="14" fill="#D9592A" stroke="#1E2B5C" stroke-width="4"/>'
       '<text y="12" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="30" fill="#1E2B5C">5:00</text>'
       '<path d="M-64 -10 l-14 -6 M-64 8 l-16 2 M64 -10 l14 -6 M64 8 l16 2" stroke="#1E2B5C" stroke-width="4" stroke-linecap="round"/></g>')
p1=panel(ground+clock+cat(200,350,1.0,band=True,stars=True)+emo(300,330,"🥦",48)+emo(60,330,"👟",48)
         +bubble(24,56,290,110,["Nuovo me.","Sveglia alle 5!!!"],30,tail_left=False),"GIORNO 1","#FFF6EC")
trophy=('<g transform="translate(335 300)"><path d="M-40 -60 h80 v30 a40 40 0 0 1 -80 0z" fill="#FFD23F" stroke="#1E2B5C" stroke-width="5"/>'
        '<rect x="-10" y="10" width="20" height="40" fill="#FFD23F" stroke="#1E2B5C" stroke-width="5"/><rect x="-70" y="50" width="140" height="28" rx="6" fill="#4A5BE8" stroke="#1E2B5C" stroke-width="4"/>'
        '<text y="68" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="15" fill="#fff">GATTO DELL\'ANNO</text>'
        '<text x="0" y="-26" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="24" fill="#1E2B5C">21</text></g>')
p2=panel(ground+cat(170,350,1.0,face="smug",band=True)+trophy+emo(40,250,"🎉",44)
         +bubble(20,56,430,110,["21 giorni: abitudine","SBLOCCATA. 🏆"],30,tail_left=True),"GIORNO 21","#FFF6EC")
sofa=('<rect x="40" y="330" width="390" height="110" rx="30" fill="#4A5BE8" stroke="#1E2B5C" stroke-width="6"/>'
      '<rect x="20" y="290" width="60" height="150" rx="26" fill="#4A5BE8" stroke="#1E2B5C" stroke-width="6"/><rect x="390" y="290" width="60" height="150" rx="26" fill="#4A5BE8" stroke="#1E2B5C" stroke-width="6"/>')
pizza='<g transform="translate(330 300) rotate(-8)"><rect x="-50" y="-14" width="100" height="22" rx="4" fill="#E8D3B0" stroke="#1E2B5C" stroke-width="4"/><text x="0" y="3" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="13" fill="#A64A30">PIZZA</text></g>'
p3=panel(sofa+melted(220,330)+pizza+emo(70,300,"👟",40)
         +bubble(24,60,300,100,["Oggi faccio","riposo attivo."],30,tail_left=True),"GIORNO 22","#DDE0FB")
sadsofa=('<g>'
  '<rect x="34" y="362" width="200" height="76" rx="22" fill="#4A5BE8" stroke="#1E2B5C" stroke-width="5"/>'
  '<rect x="20" y="330" width="44" height="108" rx="18" fill="#4A5BE8" stroke="#1E2B5C" stroke-width="5"/><rect x="204" y="330" width="44" height="108" rx="18" fill="#4A5BE8" stroke="#1E2B5C" stroke-width="5"/>'
  '<rect x="64" y="318" width="140" height="56" rx="18" fill="#6B79EE" stroke="#1E2B5C" stroke-width="5"/>'
  '<circle cx="112" cy="394" r="7" fill="#fff"/><circle cx="156" cy="394" r="7" fill="#fff"/><circle cx="112" cy="396" r="3" fill="#1E2B5C"/><circle cx="156" cy="396" r="3" fill="#1E2B5C"/>'
  '<path d="M118 424 q16 -12 32 0" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
  '<path d="M104 404 q-6 12 0 18 q6 -6 0 -18z" fill="#7FD3EE" stroke="#1E2B5C" stroke-width="2"/>'
  '</g>')
p4=panel(ground+sadsofa+cat(360,350,0.9,face="run",band=True)+emo(250,300,"💨",44)
         +bubble(40,200,170,70,["Torna…"],28,tail_left=True)
         +bubble(220,56,230,100,["Ah, ecco.","ORA lo è."],28,tail_left=False,think=True)
         +'<rect x="20" y="452" width="430" height="40" rx="10" fill="#D9592A"/><text x="235" y="479" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="21" fill="#fff">Di solito ci sono voluti 59–66 giorni</text>',"GIORNO 66","#FFF6EC")
body=f'''<style>
.slide{{background:#1E9E9E;color:#fff}}
.slide .top .brand,.slide .top .brand .we,.slide .top .brand .self{{color:#fff}}.slide .top .brand img{{background:#fff;border-radius:12px;padding:4px}}
.sticker{{position:absolute;right:44px;top:22px;transform:rotate(5deg) scale(.9);transform-origin:right top;z-index:3}}
.l1{{font-weight:900;font-size:72px;line-height:1.0;letter-spacing:-.035em;text-shadow:5px 5px 0 #1E2B5C}}
.grid4{{display:grid;grid-template-columns:1fr 1fr;gap:12px}}
.pnl{{position:relative;border:6px solid #1E2B5C;border-radius:18px;overflow:hidden;height:500px}}
.pnl svg{{display:block;width:100%;height:100%}}
.pnl .time{{position:absolute;left:10px;top:10px;background:#FFD23F;color:#1E2B5C;font-weight:900;font-size:18px;letter-spacing:.06em;padding:5px 10px;border:3px solid #1E2B5C;border-radius:8px;z-index:2}}
.srcl{{font-family:Literata,serif;font-size:22px;color:rgba(255,255,255,.85)}}
</style>
<section class="slide" id="s1">{st}
  <div class="top"><div class="brand"><img src="weself-mark.png"><span><span class="we">We</span><span class="self">Self</span></span></div></div>
  <div class="stack" style="margin-top:62px;gap:24px">
    <p class="l1">Io e le nuove abitudini:</p>
    <div class="grid4">{p1}{p2}{p3}{p4}</div>
  </div>
  <p class="srcl" style="margin-top:auto">Fonte: Singh et al., 2024 · Healthcare</p>
</section></body></html>'''
open('/home/user/weself-content/meme/gatto-abitudine/body.html','w').write(body)
