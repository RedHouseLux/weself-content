# Cover illustration for «liking gap» (v2): two people leave a café after a first chat.
# Each thought bubble carries a heart meter: the gap between what one thinks and what the other feels.
INK="#1E2B5C"

def heart(cx, cy, s, fill, stroke):
    return (f'<path transform="translate({cx} {cy}) scale({s})" d="M0 6 C-2 -2 -14 -2 -14 7 C-14 15 0 22 0 24 C0 22 14 15 14 7 C14 -2 2 -2 0 6Z" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{2.2/s:.2f}" stroke-linejoin="round"/>')

def meter(x, y, n, on, off, stroke):
    return "".join(heart(x+i*36, y, 1.05, on if i < n else off, stroke) for i in range(5))

def walker(x, skin, hair, top, top_dk, pants, shoe, facing, mood, hairstyle, bag=None):
    # facing: -1 walks left (looks back right), 1 walks right (looks back left)
    f = facing
    s = f'<ellipse cx="{x}" cy="528" rx="78" ry="12" fill="{INK}" opacity=".13"/>'
    # legs mid-stride
    s += f'<g transform="rotate({-14*f} {x} 432)"><rect x="{x-14}" y="430" width="28" height="94" rx="13" fill="{pants}"/><rect x="{x-16+8*f}" y="508" width="40" height="18" rx="9" fill="{shoe}"/></g>'
    s += f'<g transform="rotate({16*f} {x} 432)"><rect x="{x-14}" y="430" width="28" height="94" rx="13" fill="{pants}"/><rect x="{x-16+8*f}" y="508" width="40" height="18" rx="9" fill="{shoe}"/></g>'
    # back arm
    s += f'<path d="M{x-30*f} 350 C{x-52*f} 384 {x-56*f} 410 {x-48*f} 432" fill="none" stroke="{top_dk}" stroke-width="22" stroke-linecap="round"/><circle cx="{x-48*f}" cy="436" r="11" fill="{skin}"/>'
    # torso with shading
    s += f'<path d="M{x-50} 440 C{x-54} 366 {x-44} 334 {x} 332 C{x+44} 334 {x+54} 366 {x+50} 440 Z" fill="{top}"/>'
    s += f'<path d="M{x+18*f} 336 C{x+46*f} 344 {x+54*f} 380 {x+50*f} 440 L{x+26*f} 440 C{x+30*f} 396 {x+28*f} 360 {x+18*f} 336Z" fill="{top_dk}" opacity=".55"/>'
    if bag:
        s += f'<path d="M{x-26*f} 338 L{x+30*f} 420" stroke="{bag}" stroke-width="7" stroke-linecap="round"/><rect x="{x+16*f-(0 if f>0 else 44)}" y="408" width="44" height="40" rx="10" fill="{bag}"/>'
    # front arm swinging
    s += f'<path d="M{x+30*f} 350 C{x+48*f} 380 {x+56*f} 404 {x+62*f} 424" fill="none" stroke="{top}" stroke-width="22" stroke-linecap="round"/><circle cx="{x+63*f}" cy="428" r="11" fill="{skin}"/>'
    # neck + head turned back over the shoulder
    hx = x - 10*f
    s += f'<rect x="{x-11}" y="306" width="22" height="30" rx="8" fill="{skin}"/>'
    if hairstyle == "long":
        s += f'<path d="M{hx-38} 288 C{hx-46} 226 {hx+46} 226 {hx+38} 288 L{hx+40} 330 C{hx+24} 324 {hx+20} 300 {hx+18} 280 L{hx-18} 280 C{hx-20} 300 {hx-24} 324 {hx-40} 330 Z" fill="{hair}"/>'
    s += f'<circle cx="{hx}" cy="284" r="34" fill="{skin}"/>'
    s += f'<ellipse cx="{hx+30*f}" cy="288" rx="6" ry="9" fill="{skin}"/>'
    if hairstyle == "long":
        s += f'<path d="M{hx-36} 282 C{hx-36} 240 {hx+36} 238 {hx+36} 276 C{hx+14} 270 {hx-6} 258 {hx-12} 248 C{hx-18} 262 {hx-28} 272 {hx-36} 282Z" fill="{hair}"/>'
    else:
        s += f'<path d="M{hx-35} 282 C{hx-40} 236 {hx+40} 232 {hx+35} 278 C{hx+26} 262 {hx+6} 256 {hx-6} 250 C{hx-14} 262 {hx-24} 270 {hx-35} 282Z" fill="{hair}"/>'
    ex = -7*f
    s += f'<circle cx="{hx-9+ex}" cy="292" r="3.6" fill="{INK}"/><circle cx="{hx+9+ex}" cy="292" r="3.6" fill="{INK}"/>'
    if mood == "worried":
        s += f'<path d="M{hx-17+ex} 279 l8 -4 M{hx+17+ex} 279 l-8 -4" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'
        s += f'<path d="M{hx-7+ex} 309 q7 -5 14 0" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>'
        s += f'<path d="M{hx+24*f} 256 q7 11 0 16 q-7 -5 0 -16z" fill="#8B93E8"/>'
    else:
        s += f'<path d="M{hx-10+ex} 304 q10 11 20 0" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>'
        s += f'<circle cx="{hx-20+ex}" cy="302" r="6.5" fill="#F09B7C" opacity=".5"/><circle cx="{hx+20+ex}" cy="302" r="6.5" fill="#F09B7C" opacity=".5"/>'
    return s

def bubble(x, y, w, h, txt, n, stroke, txtc, on, tail):
    s = f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="34" fill="#FFFFFF" stroke="{stroke}" stroke-width="4"/>'
    s += f'<text x="{x+w/2}" y="{y+44}" text-anchor="middle" font-family="Literata" font-style="italic" font-size="24" fill="{txtc}">{txt}</text>'
    s += meter(x+w/2-72, y+62, n, on, "#FFFFFF", stroke)
    tx, ty = tail
    s += f'<circle cx="{tx}" cy="{ty}" r="9" fill="#FFFFFF" stroke="{stroke}" stroke-width="3"/><circle cx="{tx+(10 if tx>x+w/2 else -10)}" cy="{ty+20}" r="5" fill="#FFFFFF" stroke="{stroke}" stroke-width="3"/></g>'
    return s

def svg():
    s = '<svg width="952" height="600" viewBox="0 0 952 600" style="display:block;margin-top:10px;align-self:center">'
    s += '''<defs>
<linearGradient id="lk-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE9C7"/><stop offset=".6" stop-color="#FBE3D8"/><stop offset="1" stop-color="#F3EEE8"/></linearGradient>
<linearGradient id="lk-win" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFD98A"/><stop offset="1" stop-color="#F5B49C"/></linearGradient>
<radialGradient id="lk-glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFE7A8" stop-opacity=".85"/><stop offset="1" stop-color="#FFE7A8" stop-opacity="0"/></radialGradient>
<clipPath id="lk-card"><rect x="0" y="40" width="952" height="500" rx="40"/></clipPath>
</defs><g clip-path="url(#lk-card)">'''
    s += '<rect x="0" y="40" width="952" height="500" fill="url(#lk-sky)"/>'
    # distant buildings
    s += '<path d="M0 250 H70 V170 H150 V210 H200 V140 H260 V250 H952 V540 H0Z" fill="#EAD9CC" opacity=".7"/>'
    s += '<path d="M700 250 V160 H770 V120 H840 V190 H900 V250Z" fill="#EAD9CC" opacity=".7"/>'
    # café facade
    s += '<rect x="282" y="96" width="388" height="380" rx="10" fill="#FBF8F5"/>'
    s += '<rect x="282" y="96" width="388" height="30" fill="#1E2B5C"/><text x="476" y="118" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="20" fill="#FFD23F" letter-spacing="6">CAFFÈ</text>'
    stripes = "".join(f'<path d="M{282+i*48.5} 126 h48.5 v40 q-24.25 18 -48.5 0z" fill="{"#4A5BE8" if i%2==0 else "#FFFFFF"}"/>' for i in range(8))
    s += stripes
    s += '<ellipse cx="476" cy="270" rx="240" ry="120" fill="url(#lk-glow)"/>'
    s += '<rect x="312" y="196" width="150" height="150" rx="12" fill="url(#lk-win)"/><rect x="490" y="196" width="150" height="150" rx="12" fill="url(#lk-win)"/>'
    # silhouettes inside
    s += '<g fill="#E09A6E" opacity=".55"><circle cx="360" cy="276" r="16"/><rect x="342" y="292" width="36" height="54" rx="16"/><circle cx="590" cy="270" r="16"/><rect x="572" y="286" width="36" height="60" rx="16"/></g>'
    s += '<path d="M312 252 H462 M490 252 H640" stroke="#FBF8F5" stroke-width="5"/>'
    # plant
    s += '<rect x="292" y="420" width="44" height="52" rx="8" fill="#C98E64"/><g fill="#1E9E9E"><ellipse cx="302" cy="402" rx="14" ry="28" transform="rotate(-25 302 402)"/><ellipse cx="326" cy="398" rx="14" ry="30" transform="rotate(20 326 398)"/><ellipse cx="314" cy="390" rx="12" ry="30"/></g>'
    # street
    s += '<rect x="0" y="472" width="952" height="70" fill="#E6DCD1"/><path d="M0 472 H952" stroke="#D8CCBF" stroke-width="4"/>'
    # bistro table, two chairs, two cups (the conversation that just ended)
    s += '<g stroke="#1E2B5C" stroke-width="6" fill="none" stroke-linecap="round"><path d="M398 420 v100 M398 446 h34 M432 446 v74 M398 420 q-6 -40 6 -54"/><path d="M554 420 v100 M554 446 h-34 M520 446 v74 M554 420 q6 -40 -6 -54"/></g>'
    s += '<ellipse cx="476" cy="424" rx="62" ry="12" fill="#1E2B5C"/><rect x="472" y="424" width="8" height="96" fill="#1E2B5C"/><ellipse cx="476" cy="522" rx="34" ry="6" fill="#1E2B5C"/>'
    s += '<rect x="446" y="400" width="24" height="20" rx="5" fill="#FFFFFF"/><rect x="484" y="400" width="24" height="20" rx="5" fill="#FFFFFF"/>'
    s += '<path d="M454 392 q-5 -9 0 -16 M494 392 q-5 -9 0 -16" fill="none" stroke="#AAB3DD" stroke-width="3" stroke-linecap="round"/>'
    # motion lines
    s += '<path d="M232 496 h40 M222 512 h26" stroke="#C9BFB3" stroke-width="5" stroke-linecap="round"/><path d="M720 496 h-40 M730 512 h-26" stroke="#C9BFB3" stroke-width="5" stroke-linecap="round"/>'
    # the two people walking away, looking back
    s += walker(150, "#8D5A3B", "#1E2B5C", "#1E9E9E", "#0F6F6F", "#1E2B5C", "#F09B7C", -1, "worried", "short", bag="#4A5BE8")
    s += walker(800, "#F2C9A8", "#6B3E26", "#F09B7C", "#D9785A", "#4A5BE8", "#1E2B5C", 1, "happy", "long")
    s += '</g>'
    # bubbles with heart meters (outside the clip, can overlap the card edge)
    s += bubble(16, 70, 300, 100, "«Avrò parlato troppo…»", 2, "#AAB3DD", "#5A6488", "#AAB3DD", (176, 186))
    s += bubble(636, 70, 300, 100, "«Che bella chiacchierata!»", 5, "#F09B7C", "#A64A30", "#F09B7C", (776, 186))
    s += '</svg>'
    return s

if __name__ == "__main__":
    print(svg())
