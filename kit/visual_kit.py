"""Gerçek görsel + hareket kiti (Ata 30 Eki 14:35: "hiç gerçek video ve görsel kullanmıyoruz… hiç animated şeyler yok").
Kullanım (spec.py):
    from visual_kit import VIS_CSS, bg_html, bg_js, card, card_js
    EXTRA_CSS = '<style>' + FRAME_CSS + VIS_CSS + ... + '</style>'
    SCENE_HTML = bg_html([('bg1','foto.jpg',0), ...]) + <svg defs> + <section>...   (arka planlar SECTION'LARIN DIŞINDA olmalı:
                 HERO sahnelerinde .stage gizlenir, arka plan yine görünür)
    card('p1','media/x.jpg', top, height, 'ALTYAZI')  → foto kart (perde açılışı + ışık süpürmesi), section içinde kullan
    SCENE_JS += bg_js({'s1':'bg1',...}, scenes(None)) + card_js('p1', t)
Arka planlar 1080x1920 tam ekran (safezone denetimi tam ekran zemini atlar); kartlar x 155–870.
"""

VIS_CSS = r'''
.bgp{position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:hidden;opacity:0;pointer-events:none}
.bgp img{position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover;transform-origin:50% 45%}
.bgp .sh{position:absolute;left:0;top:0;width:1080px;height:1920px;background:linear-gradient(180deg,rgba(8,6,8,.74) 0%,rgba(8,6,8,.46) 35%,rgba(8,6,8,.62) 70%,rgba(8,6,8,.93) 100%)}
.pc{position:absolute;left:155px;width:715px;border-radius:22px;overflow:hidden;box-shadow:0 0 0 2px rgba(255,255,255,.35),0 26px 60px rgba(0,0,0,.75);--sx:-120%}
.pc img{display:block;width:100%;height:100%;object-fit:cover}
.pc::after{content:'';position:absolute;top:0;bottom:0;left:0;width:45%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.38),transparent);transform:translateX(var(--sx)) skewX(-12deg)}
.pc .cap{position:absolute;left:18px;bottom:16px;padding:8px 16px;border-radius:10px;background:rgba(0,0,0,.66);font:700 24px 'IBM Plex Mono';color:#fff;letter-spacing:.06em}
'''


def bg_html(items):
    """items: [(id, dosya, blur(0/1)[, object-position])]"""
    out = ''
    for it in items:
        i, f, blur = it[:3]
        pos = it[3] if len(it) > 3 else '50% 50%'
        st = f"object-position:{pos};" + ('filter:blur(18px) brightness(.8);' if blur else '')
        out += f'  <div class="bgp" id="{i}"><img src="media/{f}" style="{st}"><div class="sh"></div></div>\n'
    return out


def bg_js(bgmap, scenes):
    sc = {k: (a, b) for k, a, b in scenes}
    js = ''
    for k, (sid, bid) in enumerate(bgmap.items()):
        a, b = sc[sid]
        dx = (-40, 40)[k % 2]
        js += (f"tl.fromTo('#{bid}',{{opacity:0}},{{opacity:1,duration:.45,ease:'power2.out'}},{max(0, a - .05):.2f});"
               f"tl.fromTo('#{bid} img',{{scale:1.04,x:0}},{{scale:1.16,x:{dx},duration:{b - a + .4:.2f},ease:'none'}},{max(0, a - .05):.2f});"
               f"tl.to('#{bid}',{{opacity:0,duration:.35}},{b - .1:.2f});\n")
    return js


def card(cid, src, top, h, cap='', pos='50% 50%'):
    c = f'<div class="cap">{cap}</div>' if cap else ''
    return f'<div class="pc" id="{cid}" style="top:{top}px;height:{h}px;clip-path:inset(0% 100% 0% 0%)"><img src="{src}" style="object-position:{pos}">{c}</div>'


def card_js(cid, t):
    return (f"tl.fromTo('#{cid}',{{clipPath:'inset(0% 100% 0% 0% round 22px)',y:30}},{{clipPath:'inset(0% 0% 0% 0% round 22px)',y:0,duration:.7,ease:'power3.out'}},{t:.2f});"
            f"tl.fromTo('#{cid} img',{{scale:1.18}},{{scale:1.02,duration:3.5,ease:'power2.out'}},{t:.2f});"
            f"tl.fromTo('#{cid}',{{'--sx':'-120%'}},{{'--sx':'260%',duration:.9,ease:'power2.inOut'}},{t + .6:.2f});\n")
