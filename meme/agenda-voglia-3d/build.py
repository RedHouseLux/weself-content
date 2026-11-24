# Builds body.html for the 3D «Agenda e Voglia» strip from the rendered panels in 3d/ (see ../agenda-voglia/3d/scene.html)
st=open('../_stile/sticker.html').read()
def bubble(x,y,w,h,lines,fs=24,tail="bl",col="#fff"):
    t=''.join(f'<text x="{x+w/2}" y="{y+(h-len(lines)*fs*1.2)/2+fs+i*fs*1.2:.1f}" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="{fs}" fill="#1E2B5C">{l}</text>' for i,l in enumerate(lines))
    tx={'bl':x+w*0.3,'br':x+w*0.7}[tail]; d=-26 if tail=='bl' else 26
    tl=f'<path d="M{tx-14} {y+h-3} L{tx+d} {y+h+28} L{tx+14} {y+h-3}" fill="{col}" stroke="#1E2B5C" stroke-width="5" stroke-linejoin="round"/><rect x="{tx-16}" y="{y+h-10}" width="32" height="12" fill="{col}"/>'
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="{col}" stroke="#1E2B5C" stroke-width="5"/>{tl}{t}'
def panel(img,ov,label):
    return f'<div class="pnl"><img src="3d/{img}"><span class="time">{label}</span><svg width="470" height="500" viewBox="0 0 470 500">{ov}</svg></div>'
p1=panel('p1.png',bubble(16,50,280,92,["Oggi UNA cosa sola:","alle 18 camminiamo."],24,"bl")+bubble(286,56,170,84,["UNA COSA!","Ricevuto!"],25,"bl",col="#FFE6DC"),"ORE 9:00")
p2=panel('p2.png',bubble(16,48,230,76,["È uscito il","nuovo episodio!"],22,"bl",col="#FFF3C4")+bubble(250,56,170,60,["Solo UNO…"],24,"bl",col="#FFE6DC"),"ORE 17:58")
p3=panel('p3.png',bubble(16,50,220,62,["Avevi UNA cosa."],23,"bl")+bubble(200,140,210,80,["La serie aveva","bisogno di me."],21,"bl",col="#FFE6DC"),"ORE 21:40")
note=('<g transform="translate(240 100) rotate(-3)"><rect x="-205" y="-58" width="410" height="116" rx="10" fill="#fff" stroke="#1E2B5C" stroke-width="4"/>'
      '<text x="0" y="-14" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="23" fill="#1E9E9E">SE sono le 18 ed esce un episodio,</text>'
      '<text x="0" y="20" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="23" fill="#D9592A">ALLORA lo ascolto camminando.</text></g>')
lab=('<rect x="16" y="430" width="438" height="62" rx="10" fill="#D9592A"/><text x="235" y="456" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="19" fill="#fff">Chi aveva un «se… allora…» ha fatto meglio</text>'
     '<text x="235" y="481" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="19" fill="#fff">del 74% di chi aveva solo l\'intenzione</text>')
p4=panel('p4.png',note+lab,"IL GIORNO DOPO")
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
