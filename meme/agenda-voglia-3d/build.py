# Builds body.html for the 3D «Agenda e Voglia» strip from the rendered panels in 3d/ (see ../agenda-voglia/3d/scene.html)
st=open('../_stile/sticker.html').read()
def bubble(x,y,w,h,lines,fs=24,tail="bl",col="#fff"):
    t=''.join(f'<text x="{x+w/2}" y="{y+(h-len(lines)*fs*1.2)/2+fs+i*fs*1.2:.1f}" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="{fs}" fill="#1E2B5C">{l}</text>' for i,l in enumerate(lines))
    tx={'bl':x+w*0.3,'br':x+w*0.7}[tail]; d=-26 if tail=='bl' else 26
    tl=f'<path d="M{tx-14} {y+h-3} L{tx+d} {y+h+28} L{tx+14} {y+h-3}" fill="{col}" stroke="#1E2B5C" stroke-width="5" stroke-linejoin="round"/><rect x="{tx-16}" y="{y+h-10}" width="32" height="12" fill="{col}"/>'
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="{col}" stroke="#1E2B5C" stroke-width="5"/>{tl}{t}'
def panel(img,ov,label):
    return f'<div class="pnl"><img src="3d/{img}"><span class="time">{label}</span><svg width="470" height="500" viewBox="0 0 470 500">{ov}</svg></div>'
p1=panel('p1.png',bubble(12,48,288,96,["Stasera alle 18: camminata.","L'ho scritto: è ufficiale."],19,"bl")+bubble(306,56,152,84,["Io porto","l'entusiasmo!"],20,"bl",col="#FFE6DC"),"ORE 9:00")
p2=panel('p2.png',bubble(26,44,200,96,["…42 minuti","valgono come","camminata seduta?"],19,"bl")+bubble(250,24,200,64,["Nuovo episodio!"],21,"bl",col="#FFF3C4")+bubble(248,104,212,64,["Dura solo 42 minuti!"],18,"bl",col="#FFE6DC"),"ORE 17:58")
p3=panel('p3.png',bubble(12,46,236,86,["Correggo: era una","maratona. Di episodi."],21,"br")+bubble(236,132,220,70,["Abbiamo allenato","il pollice."],21,"bl",col="#FFE6DC"),"ORE 21:40")
note=('<g transform="translate(240 86) rotate(-3)"><rect x="-205" y="-50" width="410" height="100" rx="10" fill="#fff" stroke="#1E2B5C" stroke-width="4"/>'
      '<text x="0" y="-10" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="22" fill="#1E9E9E">SE esce un episodio,</text>'
      '<text x="0" y="22" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="22" fill="#D9592A">ALLORA lo ascoltiamo camminando.</text></g>')
lab=('<rect x="16" y="430" width="438" height="62" rx="10" fill="#D9592A"/><text x="235" y="456" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="19" fill="#fff">Chi aveva un «se… allora…» ha fatto meglio</text>'
     '<text x="235" y="481" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="19" fill="#fff">del 74% di chi aveva solo l\'intenzione</text>')
p4=panel('p4.png',note+bubble(230,146,228,58,["Episodio 8, 4.000 passi!"],17,"bl",col="#FFE6DC")+lab,"IL GIORNO DOPO")
body=f'''<style>
.slide{{background:#1E9E9E;color:#fff}}
.slide .top .brand,.slide .top .brand .we,.slide .top .brand .self{{color:#fff}}.slide .top .brand img{{background:#fff;border-radius:12px;padding:4px}}
.sticker{{position:absolute;right:44px;top:22px;transform:rotate(5deg) scale(.9);transform-origin:right top;z-index:3}}
.l1{{font-weight:900;font-size:66px;line-height:1.0;letter-spacing:-.035em;text-shadow:5px 5px 0 #1E2B5C}}
.grid4{{display:grid;grid-template-columns:1fr 1fr;gap:12px}}
.pnl{{position:relative;border:6px solid #1E2B5C;border-radius:18px;overflow:hidden;height:500px}}
.pnl img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.pnl svg{{position:absolute;inset:0;display:block;width:100%;height:100%}}
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
open('body.html','w').write(body)
