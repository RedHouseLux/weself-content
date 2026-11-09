# Cover illustration for «liking gap»: after a chat, each person walks away with a different thought.
INK="#1E2B5C"
def person(x, skin, hair, shirt, pants, face="worried", look=1, hairstyle="short"):
    s=f'<ellipse cx="{x}" cy="522" rx="62" ry="11" fill="{INK}" opacity=".12"/>'
    s+=f'<rect x="{x-30}" y="420" width="27" height="100" rx="13" fill="{pants}"/><rect x="{x+3}" y="420" width="27" height="100" rx="13" fill="{pants}"/>'
    s+=f'<path d="M{x-56} 436 C{x-58} 360 {x-46} 332 {x} 330 C{x+46} 332 {x+58} 360 {x+56} 436 Z" fill="{shirt}"/>'
    s+=f'<path d="M{x-50} 352 C{x-68} 384 {x-64} 420 {x-52} 440" fill="none" stroke="{shirt}" stroke-width="22" stroke-linecap="round"/><circle cx="{x-52}" cy="442" r="12" fill="{skin}"/>'
    s+=f'<path d="M{x+50} 352 C{x+68} 384 {x+64} 420 {x+52} 440" fill="none" stroke="{shirt}" stroke-width="22" stroke-linecap="round"/><circle cx="{x+52}" cy="442" r="12" fill="{skin}"/>'
    s+=f'<rect x="{x-11}" y="304" width="22" height="30" rx="8" fill="{skin}"/>'
    hx=x+6*look
    s+=f'<circle cx="{hx}" cy="284" r="34" fill="{skin}"/>'
    if hairstyle=="long":
        s+=f'<path d="M{hx-36} 290 C{hx-44} 230 {hx+44} 230 {hx+36} 290 L{hx+38} 318 C{hx+30} 300 {hx+28} 270 {hx+20} 262 C{hx} 270 {hx-24} 266 {hx-28} 262 C{hx-30} 280 {hx-30} 300 {hx-38} 318 Z" fill="{hair}"/>'
    else:
        s+=f'<path d="M{hx-35} 280 C{hx-38} 238 {hx+38} 234 {hx+35} 276 C{hx+22} 260 {hx-6} 252 {hx-35} 280 Z" fill="{hair}"/>'
    ex=4*look
    s+=f'<circle cx="{hx-10+ex}" cy="292" r="3.4" fill="{INK}"/><circle cx="{hx+10+ex}" cy="292" r="3.4" fill="{INK}"/>'
    if face=="worried":
        s+=f'<path d="M{hx-8+ex} 308 q8 -6 16 0" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>'
        s+=f'<path d="M{hx-16+ex} 280 l9 -4 M{hx+16+ex} 280 l-9 -4" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'
    else:
        s+=f'<path d="M{hx-10+ex} 304 q10 10 20 0" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>'
        s+=f'<circle cx="{hx-20+ex}" cy="302" r="6" fill="#F09B7C" opacity=".45"/><circle cx="{hx+20+ex}" cy="302" r="6" fill="#F09B7C" opacity=".45"/>'
    return s

def cloud(x,y,w,h,txt,stroke,color,tailx,taily):
    return (f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="#FFFFFF" stroke="{stroke}" stroke-width="4"/>'
            f'<circle cx="{tailx}" cy="{taily}" r="9" fill="#FFFFFF" stroke="{stroke}" stroke-width="3"/><circle cx="{tailx+(8 if tailx>x+w/2 else -8)}" cy="{taily+20}" r="5" fill="#FFFFFF" stroke="{stroke}" stroke-width="3"/>'
            f'<text x="{x+w/2}" y="{y+h/2+9}" text-anchor="middle" font-family="Literata" font-style="italic" font-size="25" fill="{color}">{txt}</text></g>')

def svg():
    s='<svg width="952" height="600" viewBox="0 0 952 600" style="display:block;margin-top:10px;align-self:center">'
    s+='''<defs><linearGradient id="lw" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F3EEE8"/><stop offset="1" stop-color="#EDE5DC"/></linearGradient>
<radialGradient id="lg" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".9"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient></defs>'''
    s+='<rect x="0" y="40" width="952" height="500" rx="40" fill="url(#lw)"/>'
    # café: awning, window, round table with two cups between them
    s+='<path d="M330 70 H622 L652 120 H300 Z" fill="#4A5BE8"/><path d="M300 120 q24 22 48 0 q24 22 48 0 q24 22 48 0 q24 22 48 0 q24 22 48 0 q24 22 48 0 q24 22 48 0" fill="#DDE0FB"/>'
    s+='<rect x="350" y="150" width="252" height="150" rx="16" fill="#FBF8F5" stroke="#EAE3DB" stroke-width="5"/><line x1="476" y1="150" x2="476" y2="300" stroke="#EAE3DB" stroke-width="5"/>'
    s+='<text x="476" y="108" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="26" fill="#FFFFFF" letter-spacing="4">CAFFÈ</text>'
    s+='<path d="M0 470 H952 V500 Q952 540 912 540 H40 Q0 540 0 500 Z" fill="#E6DCD1"/>'
    s+='<ellipse cx="476" cy="400" rx="78" ry="16" fill="#C9BFB3"/><rect x="470" y="400" width="12" height="118" rx="5" fill="#C9BFB3"/><ellipse cx="476" cy="520" rx="44" ry="8" fill="#C9BFB3"/>'
    s+='<rect x="436" y="374" width="28" height="24" rx="6" fill="#FFFFFF"/><path d="M464 380 q10 4 0 12" fill="none" stroke="#FFFFFF" stroke-width="4"/>'
    s+='<rect x="490" y="374" width="28" height="24" rx="6" fill="#FFFFFF"/><path d="M518 380 q10 4 0 12" fill="none" stroke="#FFFFFF" stroke-width="4"/>'
    s+='<path d="M446 366 q-6 -10 0 -18 M504 366 q-6 -10 0 -18" fill="none" stroke="#AAB3DD" stroke-width="3" stroke-linecap="round"/>'
    # walking-away hints
    s+='<path d="M130 470 h-50 M120 486 h-30" stroke="#C9BFB3" stroke-width="5" stroke-linecap="round"/><path d="M822 470 h50 M832 486 h30" stroke="#C9BFB3" stroke-width="5" stroke-linecap="round"/>'
    # left: worried, looking back; right: smiling
    s+=person(220,"#8D5A3B","#1E2B5C","#1E9E9E","#1E2B5C","worried",1,"short")
    s+=person(732,"#F2C9A8","#6B3E26","#F09B7C","#4A5BE8","happy",-1,"long")
    s+=cloud(52,150,300,74,"«Avrò parlato troppo…»","#AAB3DD","#5A6488",250,238)
    s+=cloud(600,150,300,74,"«Che bella chiacchierata!»","#F09B7C","#A64A30",700,238)
    s+='<path d="M880 128 c-6 -10 -20 -6 -18 6 c2 10 18 18 18 18 c0 0 16 -8 18 -18 c2 -12 -12 -16 -18 -6z" fill="#F09B7C"/>'
    s+='</svg>'
    return s
if __name__=="__main__": print(svg())
