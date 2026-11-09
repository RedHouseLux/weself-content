# Generates the cover illustration for bias #1 (effetto riflettore) as SVG markup.
INK="#1E2B5C"
def seated(x, skin, hair, shirt, look="down", extra=""):
    # head at (x,300), torso behind table (table top y=430)
    hx = x + (-10 if look=="left" else 8 if look=="right" else 0)
    hy = 296 + (8 if look=="down" else 0)
    g = f'<g>'
    g += f'<path d="M{x-58} 432 C{x-58} 372 {x-40} 346 {x} 346 C{x+40} 346 {x+58} 372 {x+58} 432 Z" fill="{shirt}"/>'
    g += f'<rect x="{x-11}" y="{hy+22}" width="22" height="26" rx="8" fill="{skin}"/>'
    g += f'<circle cx="{hx}" cy="{hy}" r="31" fill="{skin}"/>'
    g += f'<path d="M{hx-32} {hy-2} C{hx-34} {hy-40} {hx+34} {hy-44} {hx+32} {hy-6} C{hx+20} {hy-22} {hx-14} {hy-26} {hx-32} {hy-2} Z" fill="{hair}"/>'
    ex = {"down":(0,6),"left":(-9,0),"right":(9,0)}[look]
    g += f'<circle cx="{hx-10+ex[0]}" cy="{hy+4+ex[1]}" r="3.2" fill="{INK}"/><circle cx="{hx+10+ex[0]}" cy="{hy+4+ex[1]}" r="3.2" fill="{INK}"/>'
    g += extra + '</g>'
    return g

def bubble(x, y, r, icon):
    return (f'<g opacity=".95"><circle cx="{x}" cy="{y}" r="{r}" fill="#FFFFFF" stroke="#EAE3DB" stroke-width="3"/>'
            f'<circle cx="{x-r*0.55}" cy="{y+r+10}" r="7" fill="#FFFFFF" stroke="#EAE3DB" stroke-width="3"/>'
            f'<circle cx="{x-r*0.85}" cy="{y+r+26}" r="4" fill="#FFFFFF" stroke="#EAE3DB" stroke-width="2"/>{icon}</g>')

def svg():
    s = '<svg width="952" height="600" viewBox="0 0 952 600" style="display:block;margin-top:10px;align-self:center">'
    s += '''<defs>
<linearGradient id="beam" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF6EE" stop-opacity=".95"/><stop offset=".55" stop-color="#FBE3D8" stop-opacity=".75"/><stop offset="1" stop-color="#F09B7C" stop-opacity=".35"/></linearGradient>
<radialGradient id="pool" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#F5B49C" stop-opacity=".95"/><stop offset=".6" stop-color="#F09B7C" stop-opacity=".45"/><stop offset="1" stop-color="#F09B7C" stop-opacity="0"/></radialGradient>
<radialGradient id="glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#DDE0FB" stop-opacity=".9"/><stop offset="1" stop-color="#DDE0FB" stop-opacity="0"/></radialGradient>
<linearGradient id="wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F3EEE8"/><stop offset="1" stop-color="#EDE5DC"/></linearGradient>
<linearGradient id="dim" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#1E2B5C" stop-opacity=".10"/><stop offset=".55" stop-color="#1E2B5C" stop-opacity=".03"/><stop offset="1" stop-color="#1E2B5C" stop-opacity="0"/></linearGradient>
</defs>'''
    # room
    s += '<rect x="0" y="40" width="952" height="500" rx="40" fill="url(#wall)"/>'
    s += '<rect x="0" y="40" width="952" height="500" rx="40" fill="url(#dim)"/>'
    s += '<rect x="70" y="92" width="190" height="150" rx="18" fill="#FBF8F5" stroke="#EAE3DB" stroke-width="5"/><line x1="165" y1="92" x2="165" y2="242" stroke="#EAE3DB" stroke-width="5"/><line x1="70" y1="167" x2="260" y2="167" stroke="#EAE3DB" stroke-width="5"/>'
    s += '<path d="M0 470 H952 V500 Q952 540 912 540 H40 Q0 540 0 500 Z" fill="#E6DCD1"/>'
    # spotlight lamp + beam
    s += '<path d="M676 40 L724 40 L712 62 L688 62 Z" fill="#1E2B5C"/><rect x="696" y="40" width="8" height="0" fill="#1E2B5C"/>'
    s += '<path d="M688 62 L712 62 L870 520 L530 520 Z" fill="url(#beam)"/>'
    s += '<ellipse cx="700" cy="520" rx="210" ry="40" fill="url(#pool)"/>'
    for (x,y,r) in [(640,150,3),(735,210,2.5),(690,300,2),(770,330,3),(610,260,2),(720,120,2)]:
        s += f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFFFFF" opacity=".9"/>'
    # table + seated people (looking elsewhere)
    phone = '<g transform="rotate(-8 168 392)"><rect x="150" y="360" width="38" height="62" rx="8" fill="#1E2B5C"/><rect x="155" y="366" width="28" height="48" rx="4" fill="#A8E6DD"/></g><circle cx="168" cy="360" r="46" fill="url(#glow)"/>'
    laptop = '<path d="M262 430 L276 372 L352 372 L340 430 Z" fill="#AAB3DD"/><circle cx="312" cy="400" r="6" fill="#FBF8F5"/>'
    s += seated(130, "#E8B48F", "#2B2238", "#4A5BE8", "down", phone)
    s += seated(330, "#8D5A3B", "#1E2B5C", "#F5B49C", "down", laptop)
    s += seated(450, "#F2C9A8", "#6B3E26", "#1E9E9E", "left")
    s += '<rect x="56" y="428" width="460" height="22" rx="11" fill="#C9BFB3"/><rect x="86" y="450" width="14" height="70" rx="6" fill="#C9BFB3"/><rect x="472" y="450" width="14" height="70" rx="6" fill="#C9BFB3"/>'
    s += '<rect x="400" y="410" width="34" height="22" rx="6" fill="#FBF8F5"/><path d="M434 416 q12 4 0 12" fill="none" stroke="#FBF8F5" stroke-width="5"/>'
    # their thought bubbles: their own concerns
    clock = '<circle cx="96" cy="208" r="17" fill="none" stroke="#4A5BE8" stroke-width="4"/><path d="M96 197 V208 L104 213" stroke="#4A5BE8" stroke-width="4" fill="none" stroke-linecap="round"/>'
    mail = '<rect x="296" y="196" width="40" height="28" rx="5" fill="none" stroke="#4A5BE8" stroke-width="4"/><path d="M296 200 L316 214 L336 200" fill="none" stroke="#4A5BE8" stroke-width="4" stroke-linejoin="round"/>'
    food = '<path d="M464 198 L498 204 L476 232 Z" fill="#F5B49C" stroke="#F09B7C" stroke-width="3" stroke-linejoin="round"/><path d="M464 198 L498 204" stroke="#A64A30" stroke-width="6" stroke-linecap="round"/><circle cx="478" cy="210" r="3.5" fill="#A64A30"/><circle cx="485" cy="219" r="3" fill="#A64A30"/>'
    s += bubble(96, 208, 32, clock) + bubble(316, 210, 34, mail) + bubble(480, 212, 32, food)
    # protagonist in the spotlight, stain on shirt, looking down at it
    x=700
    s += f'<ellipse cx="{x}" cy="522" rx="70" ry="12" fill="#A64A30" opacity=".25"/>'
    s += f'<rect x="{x-34}" y="420" width="30" height="100" rx="14" fill="{INK}"/><rect x="{x+4}" y="420" width="30" height="100" rx="14" fill="{INK}"/>'
    s += f'<path d="M{x-62} 438 C{x-64} 360 {x-52} 330 {x} 328 C{x+52} 330 {x+64} 360 {x+62} 438 Z" fill="#1E9E9E"/>'
    s += f'<path d="M{x-58} 350 C{x-80} 380 {x-74} 420 {x-30} 418" fill="none" stroke="#1E9E9E" stroke-width="24" stroke-linecap="round"/>'
    s += f'<circle cx="{x-28}" cy="414" r="14" fill="#F2C9A8"/>'
    s += f'<path d="M{x+58} 350 C{x+76} 386 {x+70} 420 {x+52} 440" fill="none" stroke="#1E9E9E" stroke-width="24" stroke-linecap="round"/><circle cx="{x+52}" cy="442" r="13" fill="#F2C9A8"/>'
    s += f'<path d="M{x+8} 382 c10 -10 26 -6 24 8 c8 6 2 20 -10 16 c-6 10 -22 8 -22 -4 c-10 -4 -6 -18 8 -20z" fill="#A64A30" opacity=".85"/><circle cx="{x+40}" cy="408" r="4" fill="#A64A30" opacity=".85"/>'
    s += f'<rect x="{x-12}" y="300" width="24" height="34" rx="9" fill="#F2C9A8"/>'
    s += f'<circle cx="{x}" cy="282" r="36" fill="#F2C9A8"/>'
    s += f'<path d="M{x-37} 278 C{x-40} 236 {x+40} 232 {x+37} 274 C{x+24} 258 {x-6} 250 {x-37} 278 Z" fill="#2B2238"/>'
    s += f'<circle cx="{x-11}" cy="292" r="3.4" fill="{INK}"/><circle cx="{x+11}" cy="292" r="3.4" fill="{INK}"/>'
    s += f'<path d="M{x-8} 306 q8 -6 16 0" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>'
    s += f'<path d="M{x+30} 262 q6 10 0 14 q-6 -4 0 -14z" fill="#8B93E8"/>'
    # protagonist thought bubble
    s += ('<g><rect x="742" y="146" width="200" height="80" rx="40" fill="#FFFFFF" stroke="#F09B7C" stroke-width="4"/>'
          '<circle cx="772" cy="246" r="9" fill="#FFFFFF" stroke="#F09B7C" stroke-width="3"/><circle cx="752" cy="264" r="5" fill="#FFFFFF" stroke="#F09B7C" stroke-width="3"/>'
          '<text x="842" y="194" text-anchor="middle" font-family="Literata" font-style="italic" font-size="25" fill="#A64A30">«tutti la vedono»</text></g>')
    s += '</svg>'
    return s
if __name__ == "__main__":
    print(svg())
