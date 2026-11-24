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
WALL="#FFF6EC"; FLOOR='<rect x="0" y="440" width="470" height="60" fill="#E8D3B0"/><line x1="0" y1="440" x2="470" y2="440" stroke="#1E2B5C" stroke-width="4"/>'
def window(x,y,kind):
    inner={'moon':'<rect x="0" y="0" width="110" height="110" fill="#1E2B5C"/><circle cx="72" cy="36" r="16" fill="#FFF3C4"/><circle cx="64" cy="30" r="15" fill="#1E2B5C"/><circle cx="24" cy="24" r="3" fill="#FFF3C4"/><circle cx="40" cy="70" r="2.5" fill="#FFF3C4"/>',
           'rain':'<rect x="0" y="0" width="110" height="110" fill="#AAB3DD"/>'+''.join(f'<path d="M{a} {b} l-8 16" stroke="#fff" stroke-width="4" stroke-linecap="round"/>' for a,b in [(20,10),(52,30),(86,8),(34,60),(70,66),(96,48),(18,86),(60,92)]),
           'sun':'<rect x="0" y="0" width="110" height="110" fill="#A8E6DD"/><circle cx="56" cy="50" r="22" fill="#FFD23F"/>'}[kind]
    return (f'<g transform="translate({x} {y})">{inner}<rect x="0" y="0" width="110" height="110" fill="none" stroke="#1E2B5C" stroke-width="6"/>'
            f'<line x1="55" y1="0" x2="55" y2="110" stroke="#1E2B5C" stroke-width="4"/><line x1="0" y1="55" x2="110" y2="55" stroke="#1E2B5C" stroke-width="4"/></g>')
def sofa(x,y,mood,s=1.0):
    eyes={'neutral':'<circle cx="-30" cy="18" r="8" fill="#fff"/><circle cx="30" cy="18" r="8" fill="#fff"/><circle cx="-28" cy="20" r="4" fill="#1E2B5C"/><circle cx="32" cy="20" r="4" fill="#1E2B5C"/><path d="M-14 42 h28" stroke="#fff" stroke-width="5" stroke-linecap="round"/>',
          'happy':'<path d="M-40 20 q10 -12 20 0 M20 20 q10 -12 20 0" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/><path d="M-16 36 q16 16 32 0" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>',
          'sad':'<circle cx="-30" cy="18" r="8" fill="#fff"/><circle cx="30" cy="18" r="8" fill="#fff"/><circle cx="-30" cy="22" r="4" fill="#1E2B5C"/><circle cx="30" cy="22" r="4" fill="#1E2B5C"/><path d="M-40 4 l16 6 M40 4 l-16 6" stroke="#fff" stroke-width="4" stroke-linecap="round"/><path d="M-14 46 q14 -12 28 0" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/><path d="M-36 30 q-6 12 0 18 q6 -6 0 -18z" fill="#7FD3EE" stroke="#1E2B5C" stroke-width="2"/>'}[mood]
    return (f'<g transform="translate({x} {y}) scale({s})">'
      '<rect x="-130" y="-60" width="260" height="70" rx="22" fill="#6B79EE" stroke="#1E2B5C" stroke-width="5"/>'
      '<rect x="-150" y="0" width="300" height="76" rx="24" fill="#4A5BE8" stroke="#1E2B5C" stroke-width="5"/>'
      '<rect x="-170" y="-30" width="48" height="106" rx="20" fill="#4A5BE8" stroke="#1E2B5C" stroke-width="5"/><rect x="122" y="-30" width="48" height="106" rx="20" fill="#4A5BE8" stroke="#1E2B5C" stroke-width="5"/>'
      f'{eyes}</g>')
def shoe(x,y): return f'<g transform="translate({x} {y})"><path d="M0 0 q20 -18 40 -4 l22 6 q10 4 6 14 h-68z" fill="#D9592A" stroke="#1E2B5C" stroke-width="4"/><path d="M0 16 h68" stroke="#fff" stroke-width="5"/></g>'
# 1 · bedroom at 5:00
bed=('<rect x="20" y="360" width="250" height="80" rx="14" fill="#7FD3C8" stroke="#1E2B5C" stroke-width="5"/>'
     '<rect x="20" y="320" width="40" height="120" rx="10" fill="#1E9E9E" stroke="#1E2B5C" stroke-width="5"/>'
     '<path d="M70 360 q90 -40 200 0" fill="#A8E6DD" stroke="#1E2B5C" stroke-width="5"/>')
night=('<g transform="translate(390 400)"><rect x="-36" y="0" width="72" height="40" rx="6" fill="#E8D3B0" stroke="#1E2B5C" stroke-width="4"/></g>'
       '<g transform="translate(390 366)"><circle r="30" fill="#fff" stroke="#1E2B5C" stroke-width="4"/><circle cx="-22" cy="-26" r="9" fill="#D9592A" stroke="#1E2B5C" stroke-width="3"/><circle cx="22" cy="-26" r="9" fill="#D9592A" stroke="#1E2B5C" stroke-width="3"/>'
       '<text y="8" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="20" fill="#1E2B5C">5:00</text>'
       '<path d="M-42 -6 l-12 -4 M-42 8 l-12 4 M42 -6 l12 -4 M42 8 l12 4" stroke="#1E2B5C" stroke-width="4" stroke-linecap="round"/></g>')
p1=panel(f'<rect width="470" height="500" fill="{WALL}"/>'+window(330,150,'moon')+FLOOR+bed+night
         +cat(190,300,0.85,band=True,stars=True)+shoe(140,410)+shoe(230,418)
         +bubble(20,52,300,110,["Sveglia alle 5.","Corsa e insalata!"],27,tail_left=True),"GIORNO 1 · 5:00","#FFF6EC")
# 2 · living room, selfie post
phone=('<g transform="translate(340 250) rotate(6)"><rect x="-60" y="-100" width="120" height="200" rx="18" fill="#1E2B5C"/><rect x="-50" y="-82" width="100" height="160" rx="8" fill="#fff"/>'
       '<text x="0" y="-48" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="15" fill="#1E2B5C">21 GIORNI</text>'
       '<text x="0" y="-28" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="15" fill="#1E2B5C">DI CORSA!</text>'
       '<text x="0" y="14" text-anchor="middle" font-family="Noto Color Emoji" font-size="34">🏆</text>'
       '<text x="0" y="58" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="15" fill="#D9592A">#nuovome</text></g>')
p2=panel(f'<rect width="470" height="500" fill="{WALL}"/>'+window(30,150,'sun')+FLOOR+sofa(235,400,'neutral',0.72)
         +cat(170,330,0.85,face="smug",band=True)+phone
         +bubble(20,52,300,90,["Ormai è un'abitudine."],26,tail_left=True),"GIORNO 21","#FFF6EC")
# 3 · rain, cat melts on the happy sofa
p3=panel(f'<rect width="470" height="500" fill="#EEF0FD"/>'+window(330,140,'rain')+FLOOR+sofa(235,400,'happy',1.0)
         +melted(230,330)+shoe(40,424)
         +bubble(20,52,240,90,["Piove.","Riposo attivo."],26,tail_left=False)
         +bubble(300,280,150,60,["Bentornato!"],21,tail_left=False),"GIORNO 22","#EEF0FD")
# 4 · rain again, the cat goes out anyway, the sofa is sad
door=('<rect x="330" y="200" width="120" height="240" rx="6" fill="#AAB3DD" stroke="#1E2B5C" stroke-width="6"/>'
      +''.join(f'<path d="M{a} {b} l-8 16" stroke="#fff" stroke-width="4" stroke-linecap="round"/>' for a,b in [(350,220),(390,250),(430,230),(360,300),(410,320),(440,280),(370,370),(420,390)]))
umb=('<g transform="translate(400 250)"><path d="M-60 0 a60 50 0 0 1 120 0z" fill="#D9592A" stroke="#1E2B5C" stroke-width="5"/><path d="M0 0 v70 q0 12 -12 12" fill="none" stroke="#1E2B5C" stroke-width="5"/></g>')
p4=panel(f'<rect width="470" height="500" fill="{WALL}"/>'+door+FLOOR+sofa(150,376,'sad',0.72)
         +cat(395,345,0.7,face="run",band=True)+umb
         +bubble(20,48,250,84,["Piove? Vado","lo stesso."],24,tail_left=False)
         +bubble(30,220,170,60,["E noi…?"],24,tail_left=True)
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
