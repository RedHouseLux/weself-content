import math
st=open('/home/user/weself-content/meme/_stile/sticker.html').read()
INK="#1E2B5C"
def legs(x,y,h=34,col=INK):
    return f'<path d="M{x-12} {y} v{h} h-10 M{x+12} {y} v{h} h10" fill="none" stroke="{col}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
def agenda(x,y,s=1.0,face="calm",arm="none",extra=""):
    g=[f'<g transform="translate({x} {y}) scale({s})">',legs(0,60)]
    arms={'none':'<path d="M-46 10 q-20 20 -14 40 M46 10 q20 20 14 40" fill="none" stroke="#1E2B5C" stroke-width="6" stroke-linecap="round"/>',
          'point':'<path d="M-46 10 q-20 20 -14 40 M46 0 q30 -10 44 -30" fill="none" stroke="#1E2B5C" stroke-width="6" stroke-linecap="round"/>',
          'watch':'<path d="M-46 10 q-20 20 -14 40" fill="none" stroke="#1E2B5C" stroke-width="6" stroke-linecap="round"/><path d="M46 6 q26 0 20 -24" fill="none" stroke="#1E2B5C" stroke-width="6" stroke-linecap="round"/><circle cx="66" cy="-22" r="9" fill="#FFD23F" stroke="#1E2B5C" stroke-width="3"/>',
          'pen':'<path d="M-46 10 q-20 20 -14 40 M46 10 q26 -4 30 -26" fill="none" stroke="#1E2B5C" stroke-width="6" stroke-linecap="round"/><path d="M70 -20 l18 -30" stroke="#D9592A" stroke-width="8" stroke-linecap="round"/>'}[arm]
    g.append(arms)
    g.append('<rect x="-50" y="-70" width="100" height="134" rx="14" fill="#7FD3C8" stroke="#1E2B5C" stroke-width="5"/>')
    g.append('<rect x="-50" y="-70" width="16" height="134" rx="6" fill="#1E9E9E" stroke="#1E2B5C" stroke-width="4"/>')
    g.append(''.join(f'<circle cx="{cx}" cy="-72" r="6" fill="#fff" stroke="#1E2B5C" stroke-width="3"/>' for cx in (-24,-4,16,36)))
    g.append('<circle cx="-6" cy="-28" r="15" fill="#fff" stroke="#1E2B5C" stroke-width="4"/><circle cx="28" cy="-28" r="15" fill="#fff" stroke="#1E2B5C" stroke-width="4"/><path d="M9 -28 h4" stroke="#1E2B5C" stroke-width="4"/>')
    if face=='calm': g.append('<circle cx="-4" cy="-27" r="5" fill="#1E2B5C"/><circle cx="30" cy="-27" r="5" fill="#1E2B5C"/><path d="M0 4 q12 8 24 0" fill="none" stroke="#1E2B5C" stroke-width="5" stroke-linecap="round"/>')
    if face=='flat': g.append('<path d="M-14 -27 h16 M20 -27 h16" stroke="#1E2B5C" stroke-width="5" stroke-linecap="round"/><path d="M0 8 h24" stroke="#1E2B5C" stroke-width="5" stroke-linecap="round"/>')
    if face=='smile': g.append('<circle cx="-4" cy="-27" r="5" fill="#1E2B5C"/><circle cx="30" cy="-27" r="5" fill="#1E2B5C"/><path d="M-2 2 q14 14 28 0" fill="#1E2B5C"/>')
    g.append(extra+'</g>'); return ''.join(g)
def voglia(x,y,s=1.0,face="excited",pose="normal",extra=""):
    g=[f'<g transform="translate({x} {y}) scale({s})">']
    if pose!='sit': g.append(legs(0,44,32))
    arms={'normal':'<path d="M-44 0 q-24 -10 -30 -34 M44 0 q24 -10 30 -34" fill="none" stroke="#1E2B5C" stroke-width="6" stroke-linecap="round"/>',
          'salute':'<path d="M-44 0 q-24 10 -24 34 M38 -14 q22 -20 6 -46" fill="none" stroke="#1E2B5C" stroke-width="6" stroke-linecap="round"/>',
          'lazy':'<path d="M-44 10 q-30 10 -40 30 M44 10 q30 10 40 30" fill="none" stroke="#1E2B5C" stroke-width="6" stroke-linecap="round"/>',
          'walk':'<path d="M-44 0 q-24 10 -20 34 M44 0 q30 -6 34 -26" fill="none" stroke="#1E2B5C" stroke-width="6" stroke-linecap="round"/>'}[pose if pose in ('normal','salute','lazy','walk') else 'lazy']
    g.append(arms)
    g.append('<path d="M-8 -66 q-6 -30 14 -40 q-4 18 12 22 q4 -20 18 -22 q-6 24 8 34" fill="#F09B7C" stroke="#1E2B5C" stroke-width="4" stroke-linejoin="round"/>')
    g.append('<circle cx="0" cy="-10" r="56" fill="#F09B7C" stroke="#1E2B5C" stroke-width="5"/>')
    if face=='excited': g.append('<circle cx="-18" cy="-22" r="14" fill="#fff" stroke="#1E2B5C" stroke-width="4"/><circle cx="18" cy="-22" r="14" fill="#fff" stroke="#1E2B5C" stroke-width="4"/><circle cx="-14" cy="-24" r="6" fill="#1E2B5C"/><circle cx="22" cy="-24" r="6" fill="#1E2B5C"/><path d="M-20 4 q20 26 40 0z" fill="#1E2B5C"/>')
    if face=='hypno': g.append('<circle cx="-18" cy="-22" r="14" fill="#fff" stroke="#1E2B5C" stroke-width="4"/><circle cx="18" cy="-22" r="14" fill="#fff" stroke="#1E2B5C" stroke-width="4"/><path d="M-24 -22 a6 6 0 1 1 12 0 a3 3 0 1 1 -6 0 M12 -22 a6 6 0 1 1 12 0 a3 3 0 1 1 -6 0" fill="none" stroke="#1E2B5C" stroke-width="3"/><path d="M-10 10 q10 6 20 0" fill="none" stroke="#1E2B5C" stroke-width="4" stroke-linecap="round"/>')
    if face=='guilty': g.append('<path d="M-30 -24 q10 8 20 0 M10 -24 q10 8 20 0" fill="none" stroke="#1E2B5C" stroke-width="5" stroke-linecap="round"/><path d="M-14 12 q14 -8 28 0" fill="none" stroke="#1E2B5C" stroke-width="5" stroke-linecap="round"/><path d="M40 -40 q8 14 0 20 q-8 -6 0 -20z" fill="#7FD3EE" stroke="#1E2B5C" stroke-width="3"/>')
    if face=='happy': g.append('<path d="M-28 -24 q10 -12 20 0 M8 -24 q10 -12 20 0" fill="none" stroke="#1E2B5C" stroke-width="5" stroke-linecap="round"/><path d="M-18 2 q18 22 36 0z" fill="#1E2B5C"/>')
    g.append(extra+'</g>'); return ''.join(g)
def bell(x,y,s=1.0,txt=None):
    g=f'<g transform="translate({x} {y}) scale({s})"><path d="M-30 20 q0 -50 30 -54 q30 4 30 54 l8 10 h-76z" fill="#FFD23F" stroke="#1E2B5C" stroke-width="4" stroke-linejoin="round"/><circle cx="0" cy="38" r="8" fill="#FFD23F" stroke="#1E2B5C" stroke-width="4"/>'
    g+='<circle cx="-10" cy="-2" r="5" fill="#1E2B5C"/><circle cx="10" cy="-2" r="5" fill="#1E2B5C"/><path d="M-8 10 q8 8 16 0" fill="none" stroke="#1E2B5C" stroke-width="3" stroke-linecap="round"/>'
    g+='<path d="M-44 -20 l-12 -8 M44 -20 l12 -8 M-46 0 h-14 M46 0 h14" stroke="#1E2B5C" stroke-width="3" stroke-linecap="round"/></g>'
    return g
def bubble(x,y,w,h,lines,fs=24,tail="bl",col="#fff"):
    t=''.join(f'<text x="{x+w/2}" y="{y+(h-len(lines)*fs*1.2)/2+fs+i*fs*1.2:.1f}" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="{fs}" fill="#1E2B5C">{l}</text>' for i,l in enumerate(lines))
    tx={'bl':x+w*0.3,'br':x+w*0.7}[tail]; d=-26 if tail=='bl' else 26
    tl=f'<path d="M{tx-14} {y+h-3} L{tx+d} {y+h+28} L{tx+14} {y+h-3}" fill="{col}" stroke="#1E2B5C" stroke-width="5" stroke-linejoin="round"/><rect x="{tx-16}" y="{y+h-10}" width="32" height="12" fill="{col}"/>'
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="{col}" stroke="#1E2B5C" stroke-width="5"/>{tl}{t}'
W,H=470,500
def panel(inner,label,bg="#FFF6EC"): return f'<div class="pnl" style="background:{bg}"><span class="time">{label}</span><svg width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="470" height="500" fill="{bg}"/>{inner}</svg></div>'
FLOOR='<rect x="0" y="448" width="470" height="52" fill="#E8D3B0"/><line x1="0" y1="448" x2="470" y2="448" stroke="#1E2B5C" stroke-width="4"/>'
sofa=('<g transform="translate(250 404)"><rect x="-140" y="-56" width="280" height="64" rx="22" fill="#6B79EE" stroke="#1E2B5C" stroke-width="5"/>'
      '<rect x="-160" y="0" width="320" height="50" rx="20" fill="#4A5BE8" stroke="#1E2B5C" stroke-width="5"/>'
      '<rect x="-178" y="-30" width="46" height="82" rx="18" fill="#4A5BE8" stroke="#1E2B5C" stroke-width="5"/><rect x="132" y="-30" width="46" height="82" rx="18" fill="#4A5BE8" stroke="#1E2B5C" stroke-width="5"/></g>')
tv=('<g transform="translate(360 150)"><rect x="-80" y="-56" width="160" height="104" rx="10" fill="#1E2B5C"/><rect x="-70" y="-46" width="140" height="84" rx="6" fill="#AAB3DD"/>'
    '<text x="0" y="6" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="18" fill="#1E2B5C">EPISODIO 1</text></g>')
p1=panel(FLOOR+agenda(130,330,1.0,"calm","point")+voglia(330,360,1.0,"excited","salute")
         +bubble(20,46,300,110,["Oggi UNA cosa sola:","alle 18 camminiamo."],26,"bl")
         +bubble(250,170,200,96,["UNA COSA!","Ricevuto!"],28,"bl",col="#FFE6DC"),"ORE 9:00")
p2=panel(FLOOR+tv.replace('translate(360 150)','translate(120 190)')+voglia(250,360,1.0,"hypno","normal")+bell(390,250,1.0)
         +bubble(190,46,260,86,["È uscito il","nuovo episodio!"],24,"br",col="#FFF3C4")
         +bubble(20,290,170,64,["Solo UNO…"],26,"br",col="#FFE6DC"),"ORE 17:58")
snacks=''.join(f'<text x="{x}" y="{y}" font-family="Noto Color Emoji" font-size="40">{e}</text>' for x,y,e in [(160,330,"🍿"),(390,334,"🍕"),(140,440,"🥤"),(350,440,"🍫")])
tv2=tv.replace('EPISODIO 1','EPISODIO 7')
p3=panel(FLOOR+tv2+sofa+voglia(230,340,0.95,"guilty","lazy")+snacks+agenda(70,300,0.75,"flat","watch")
         +bubble(20,46,230,70,["Avevi UNA cosa."],24,"bl")
         +bubble(250,200,210,90,["La serie aveva","bisogno di me."],22,"bl",col="#FFE6DC"),"ORE 21:40")
note=('<g transform="translate(250 120) rotate(-3)"><rect x="-200" y="-60" width="400" height="122" rx="10" fill="#fff" stroke="#1E2B5C" stroke-width="4"/>'
      '<text x="0" y="-18" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="23" fill="#1E9E9E">SE sono le 18 ed esce un episodio,</text>'
      '<text x="0" y="16" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="23" fill="#D9592A">ALLORA lo ascolto camminando.</text></g>')
phones='<path d="M-30 -60 q30 -40 60 0" fill="none" stroke="#1E2B5C" stroke-width="7"/><rect x="-40" y="-56" width="16" height="26" rx="6" fill="#1E2B5C"/><rect x="24" y="-56" width="16" height="26" rx="6" fill="#1E2B5C"/>'
p4=panel(FLOOR+note+agenda(110,310,0.8,"smile","pen")+voglia(320,320,0.9,"happy","walk",extra=phones)+bell(430,300,0.55)
         +'<rect x="16" y="424" width="438" height="70" rx="10" fill="#D9592A"/><text x="235" y="453" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="20" fill="#fff">Chi aveva un «se… allora…» ha fatto meglio</text><text x="235" y="480" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="20" fill="#fff">del 74% di chi aveva solo l\'intenzione</text>',"IL GIORNO DOPO")
body=f'''<style>
.slide{{background:#1E9E9E;color:#fff}}
.slide .top .brand,.slide .top .brand .we,.slide .top .brand .self{{color:#fff}}.slide .top .brand img{{background:#fff;border-radius:12px;padding:4px}}
.sticker{{position:absolute;right:44px;top:22px;transform:rotate(5deg) scale(.9);transform-origin:right top;z-index:3}}
.l1{{font-weight:900;font-size:66px;line-height:1.0;letter-spacing:-.035em;text-shadow:5px 5px 0 #1E2B5C}}
.grid4{{display:grid;grid-template-columns:1fr 1fr;gap:12px}}
.pnl{{position:relative;border:6px solid #1E2B5C;border-radius:18px;overflow:hidden;height:500px}}
.pnl svg{{display:block;width:100%;height:100%}}
.pnl .time{{position:absolute;left:10px;top:10px;background:#FFD23F;color:#1E2B5C;font-weight:900;font-size:18px;letter-spacing:.06em;padding:5px 10px;border:3px solid #1E2B5C;border-radius:8px;z-index:2}}
.srcl{{font-family:Literata,serif;font-size:22px;color:rgba(255,255,255,.85)}}
</style>
<section class="slide" id="s1">{st}
  <div class="top"><div class="brand"><img src="weself-mark.png"><span><span class="we">We</span><span class="self">Self</span></span></div></div>
  <div class="stack" style="margin-top:62px;gap:24px">
    <p class="l1">Agenda e Voglia:</p>
    <div class="grid4">{p1}{p2}{p3}{p4}</div>
  </div>
  <p class="srcl" style="margin-top:auto">Fonte: Gollwitzer &amp; Sheeran, 2006</p>
</section></body></html>'''
open('/home/user/weself-content/meme/agenda-voglia/body.html','w').write(body)
