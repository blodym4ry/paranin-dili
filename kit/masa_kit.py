"""MASA ÜSTÜ DOSYA — imza stil kiti (Ata 23 Eki seçimi). Spec'ler `from masa_kit import *` ile kullanır.
İmza öğeleri: gerçek masa zemini + 12 fps elde kamera; nesneler masaya konur (put/take, adımlı); kırmızı keçeli kalem (write/draw, kaynayan çizgi);
FİŞ (makbuz yazıcısı satır satır basar — kişisel hesap); gazete KUPÜRÜ (gerçek manşet, kaynak+tarih); LAMBA (anlama göre renk; 'söner' = desen kırılması);
fotoğraf bulanıktan netleşerek gelir (+ deklanşör sesi). Ses: SOUND_KIT='masa' (kit/foley). Grafik alanı y=230–1180; altyazı 1200–1420."""
import math, random

CSS = r'''<style>
@font-face{font-family:'Caveat';font-weight:700;src:url(fonts/caveat-latin-ext-700-normal.woff2) format('woff2');unicode-range:U+0100-02BA,U+02BD-02C5,U+1E00-1E9F}
@font-face{font-family:'Caveat';font-weight:700;src:url(fonts/caveat-latin-700-normal.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+2000-206F,U+2192,U+2212}
:root{--cap-on:#fffaf0;--cap-red:#ff5a4a;--cap-em-bg:#d8312a;--cap-em-fg:#fff}
body,#root{background:#3a2a1c}
.bg{background:url(media/masa/masa_mese.jpg) center/cover;inset:-60px -65px -170px -65px}
.bg::after{content:'';position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 40%,transparent 40%,rgba(20,10,4,.55))}
#grid,#glow{display:none}
.cw{color:rgba(255,250,240,.42);text-shadow:0 3px 12px rgba(0,0,0,.55)}
#caps .cl{text-shadow:0 3px 14px rgba(0,0,0,.6)}
#avbox{filter:drop-shadow(16px 0 0 #f4f1ea) drop-shadow(-16px 0 0 #f4f1ea) drop-shadow(0 16px 0 #f4f1ea) drop-shadow(0 -16px 0 #f4f1ea) drop-shadow(0 26px 30px rgba(0,0,0,.5))}
/* lamba: masanın ışığı; renk anlam taşır (sıcak=normal, kırmızı=risk, yeşil=kazanç, kapalı=desen kırılması) */
#lamp{position:absolute;inset:0;pointer-events:none;background:radial-gradient(80% 60% at 50% 35%,rgba(255,200,120,.10),transparent 70%);mix-blend-mode:soft-light}
#dark{position:absolute;inset:0;background:#07050a;opacity:0;pointer-events:none}
.tape{position:absolute;width:190px;height:58px;background:linear-gradient(rgba(236,226,196,.82),rgba(222,208,170,.82));
  clip-path:polygon(0 8%,4% 0,9% 10%,14% 2%,20% 9%,80% 6%,86% 0,91% 9%,96% 1%,100% 10%,100% 92%,95% 100%,90% 90%,84% 99%,78% 91%,22% 95%,16% 100%,10% 91%,5% 100%,0 90%);
  box-shadow:0 2px 4px rgba(0,0,0,.18);mix-blend-mode:multiply}
.tape::after{content:'';position:absolute;inset:0;background:url(media/masa/grain.jpg) center/300px;opacity:.25;mix-blend-mode:multiply}
.kraft{position:absolute;background:url(media/masa/kraft.jpg) center/600px;box-shadow:0 18px 28px rgba(0,0,0,.45),0 2px 3px rgba(0,0,0,.3)}
.sheet{position:absolute;background:#f6f1e4;box-shadow:0 24px 40px rgba(0,0,0,.5),0 2px 4px rgba(0,0,0,.3)}
.sheet::before{content:'';position:absolute;inset:0;background:url(media/masa/kraft.jpg) center/700px;opacity:.16;mix-blend-mode:multiply}
.hand{font:700 64px/1.05 'Caveat';color:#1d2433}
.hand.red{color:#cf2a24}
.print{font:500 24px 'IBM Plex Mono';color:#4b4237;letter-spacing:.06em}
.photo{position:absolute;background:#f4f1ea;padding:18px 18px 70px;box-shadow:0 22px 36px rgba(0,0,0,.5)}
.photo img{display:block;width:100%;height:100%;object-fit:cover;filter:saturate(.9) contrast(1.05)}
.photo .cap{position:absolute;left:20px;bottom:16px;font:700 34px 'Caveat';color:#2a2f3a}
svg.mk{position:absolute;overflow:visible}
svg.mk path{fill:none;stroke:#cf2a24;stroke-width:9;stroke-linecap:round;stroke-linejoin:round}
/* FİŞ: termal makbuz */
.fis{position:absolute;width:640px;background:#fbfbf7;padding:34px 34px 46px;box-shadow:0 22px 34px rgba(0,0,0,.45);
  clip-path:polygon(0 0,100% 0,100% calc(100% - 14px),95% 100%,90% calc(100% - 14px),85% 100%,80% calc(100% - 14px),75% 100%,70% calc(100% - 14px),65% 100%,60% calc(100% - 14px),55% 100%,50% calc(100% - 14px),45% 100%,40% calc(100% - 14px),35% 100%,30% calc(100% - 14px),25% 100%,20% calc(100% - 14px),15% 100%,10% calc(100% - 14px),5% 100%,0 calc(100% - 14px))}
.fis .l{position:relative;display:flex;justify-content:space-between;font:500 32px/1.55 'IBM Plex Mono';color:#2b2b2b;white-space:nowrap}
.fis .h{font:700 30px 'IBM Plex Mono';letter-spacing:.14em;color:#2b2b2b;text-align:center;border-bottom:3px dashed #9a9a92;padding-bottom:12px;margin-bottom:12px}
.fis .t{border-top:3px dashed #9a9a92;margin-top:10px;padding-top:10px;font-weight:700}
/* KUPÜR: gerçek manşet (alıntı) */
.kup{position:absolute;width:880px;background:#efe9da;padding:26px 32px 30px;box-shadow:0 16px 26px rgba(0,0,0,.45)}
.kup::before{content:'';position:absolute;inset:0;background:url(media/masa/kraft.jpg) center/500px;opacity:.12;mix-blend-mode:multiply}
.kup .src{font:700 24px 'IBM Plex Mono';letter-spacing:.12em;color:#7a2a22;border-bottom:2px solid #2a2a2a;padding-bottom:8px;margin-bottom:12px}
.kup .hd{font:900 54px/1.06 'Playfair Display';color:#15140f}
.strip{position:absolute;height:86px;display:flex;align-items:center;padding:0 26px;font:700 40px 'Inter Tight';color:#1d2433;box-shadow:0 10px 18px rgba(0,0,0,.35);transform-origin:0 50%}
</style>'''

JS = r'''
// ---- MASA ÜSTÜ DOSYA hareket dili (12 fps adımlı)
const F=1/12;
const put=(s,t,o={})=>{const n=o.n??5;tl.fromTo(s,{opacity:0},{opacity:1,duration:.001},t);
  tl.fromTo(s,{x:o.x??0,y:o.y??160,rotation:(o.r??0)+(o.dr??-7),scale:o.s??1.06},
  {x:0,y:0,rotation:o.r??0,scale:1,duration:n*F,ease:`steps(${n})`,immediateRender:false},t);};
const take=(s,t,o={})=>{const n=o.n??4;tl.to(s,{x:o.x??-1300,rotation:'+=6',duration:n*F,ease:`steps(${n})`},t);};
const tape=(s,t,r)=>tl.fromTo(s,{opacity:0,scaleX:.2,rotation:r,transformOrigin:'0% 50%'},{opacity:1,scaleX:1,rotation:r,duration:3*F,ease:'steps(3)'},t);
const write=(s,t,d)=>{const n=Math.max(3,Math.round(d/F));tl.fromTo(s,{clipPath:'inset(0 100% 0 0)'},{clipPath:'inset(0 0% 0 0)',duration:n*F,ease:`steps(${n})`},t);};
const draw=(id,t,d,end)=>{const n=Math.round(d/F);for(let v=0;v<3;v++)tl.fromTo(`#${id}v${v}`,{strokeDashoffset:1},{strokeDashoffset:0,duration:n*F,ease:`steps(${n})`},t);
  for(let k=0;t+k*2*F<end;k++){const v=k%3;for(let u=0;u<3;u++)tl.set(`#${id}v${u}`,{opacity:u===v?1:0},t+k*2*F);}};
// fiş satırları: her satır yazıcıdan çıkar gibi tek adımda belirir
const prt=(s,t)=>tl.fromTo(s,{opacity:0,y:-6},{opacity:1,y:0,duration:2*F,ease:'steps(2)'},t);
// fotoğraf: bulanıktan netleşerek kayar (projektör hissi)
const slide=(s,t,o={})=>{tl.fromTo(s,{opacity:0},{opacity:1,duration:.001},t);tl.fromTo(s,{y:o.y??-120,filter:'blur(18px)'},{y:0,filter:'blur(0px)',duration:6*F,ease:'steps(6)',immediateRender:false},t);};
// lamba: renk/ışık; dark(t0,t1) = lamba söner (desen kırılması)
const lamp=(t,c,a=.18)=>tl.to('#lamp',{background:`radial-gradient(80% 60% at 50% 35%,${c.replace('A',a)},transparent 70%)`,duration:3*F,ease:'steps(3)'},t);
const dark=(t0,t1)=>{tl.to('#dark',{opacity:.93,duration:2*F,ease:'steps(2)'},t0);tl.to('#dark',{opacity:0,duration:2*F,ease:'steps(2)'},t1);};
// elde kamera
const cam=(D)=>{for(let k=0;k*F<D;k++){const t=k*F;tl.set('.bg, .scene',{x:Math.sin(t*.41)*14+Math.sin(t*2.3+1)*2.2,y:Math.sin(t*.29+2)*10+Math.cos(t*2.9)*2,rotation:Math.sin(t*.23)*.35},t);}};
'''

OVERLAYS = '<div id="lamp"></div><div id="dark"></div>'


def ring(id_, w, h, seed):
    """Elle çizilmiş daire: 3 hafif farklı varyant (kaynama)."""
    out = []
    for v in range(3):
        r = random.Random(seed * 10 + v); pts = []
        for k in range(26):
            a = -2.2 + k / 25 * (2 * math.pi + .5); j = 1 + r.uniform(-.035, .035)
            pts.append((w / 2 + math.cos(a) * w / 2 * j, h / 2 + math.sin(a) * h / 2 * j * (1 + .04 * math.sin(a * 2))))
        d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts)
        out.append(f'<path id="{id_}v{v}" d="{d}" pathLength="1" style="stroke-dasharray:1;stroke-dashoffset:1;opacity:{1 if v == 0 else 0}"/>')
    return f'<svg class="mk" id="{id_}" width="{w}" height="{h}" viewBox="0 0 {w} {h}">' + ''.join(out) + '</svg>'


def line(id_, w, seed, arrow=False):
    """Elle çizilmiş çizgi/ok (altını çizme), 3 varyant."""
    out = []
    for v in range(3):
        r = random.Random(seed * 10 + v)
        pts = [(x, 10 + r.uniform(-4, 4) + 3 * math.sin(x / 60)) for x in range(0, w + 1, max(20, w // 12))]
        d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts)
        if arrow: d += f' M{w - 34},{-12 + r.uniform(-3, 3)} L{w},10 L{w - 34},{32 + r.uniform(-3, 3)}'
        out.append(f'<path id="{id_}v{v}" d="{d}" pathLength="1" style="stroke-dasharray:1;stroke-dashoffset:1;opacity:{1 if v == 0 else 0}"/>')
    return f'<svg class="mk" id="{id_}" width="{w}" height="40" viewBox="0 -15 {w} 50">' + ''.join(out) + '</svg>'


def fis(id_, title, rows, total=None, left=0, top=0, rot=0):
    """FİŞ: rows=[(sol, sağ), ...] her satır id_r{i}; total=(sol, sağ) id_t."""
    h = f'<div class="fis" id="{id_}" style="left:{left}px;top:{top}px;transform:rotate({rot}deg)"><div class="h">{title}</div>'
    for i, (a, b) in enumerate(rows):
        h += f'<div class="l" id="{id_}r{i}"><span>{a}</span><span>{b}</span></div>'
    if total: h += f'<div class="l t" id="{id_}t"><span>{total[0]}</span><span>{total[1]}</span></div>'
    return h + '</div>'


def kup(id_, src, hd, left=130, top=300, rot=0, size=54):
    return f'<div class="kup" id="{id_}" style="left:{left}px;top:{top}px;transform:rotate({rot}deg)"><div class="src">{src}</div><div class="hd" style="font-size:{size}px">{hd}</div></div>'
