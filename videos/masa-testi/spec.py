import os
# STİL TESTİ — "MASA ÜSTÜ + GERÇEK GÖRÜNTÜ" (Ata seçimi, 22 Eki). Alan dışı videosunun ilk 13 saniyesi.
# İmza kuralları:
#  1. Zemin gerçek fotoğraf (meşe masa, Wikimedia) + hafif "elde kamera" kayması (12 fps adımlı, düzgün değil).
#  2. Bilgi ekrana "basılmaz": masaya konan nesnelerle gelir — kâğıt, kraft not, bantlı fotoğraf. Girişler 12 fps adımlı (stop-motion).
#  3. Vurgu kırmızı keçeli kalemle elle: yazılan rakam, çizilen daire; çizgiler durmaz, "kaynar" (3 varyant, 12 fps).
#  4. Ses: sentetik whoosh/pop YOK; sadece ekranda olan nesnenin gerçek kaydı (bant, kâğıt, kalem) — kit/foley.
#  5. Altyazı aynı kalır (Ata). Avatar: bantlı polaroid.
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [(N('yüzde', 'kırk', 'üçü'), "%43'ü")]
EM = {'tuzağın', 'göstereceğim.'}
RED = {"%43'ü"}
SOUND_KIT = 'masa'
POL = [250, 300, 580, 800, 4]
AV = {'s1': POL, 's2': None, 's3': None}

EXTRA_CSS = r'''<style>
@font-face{font-family:'Caveat';font-weight:700;src:url(fonts/caveat-latin-ext-700-normal.woff2) format('woff2');unicode-range:U+0100-02BA,U+02BD-02C5,U+1E00-1E9F}
@font-face{font-family:'Caveat';font-weight:700;src:url(fonts/caveat-latin-700-normal.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+2000-206F,U+2212}
:root{--cap-on:#fffaf0;--cap-red:#ff5a4a;--cap-em-bg:#d8312a;--cap-em-fg:#fff}
body,#root{background:#3a2a1c}
.bg{background:url(media/masa/masa_mese.jpg) center/cover;inset:-60px -65px -170px -65px}
.bg::after{content:'';position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 40%,transparent 40%,rgba(20,10,4,.55))}
#grid,#glow{display:none}
.cw{color:rgba(255,250,240,.42);text-shadow:0 3px 12px rgba(0,0,0,.55)}
#caps .cl{text-shadow:0 3px 14px rgba(0,0,0,.6)}
/* polaroid avatar */
#avbox{filter:drop-shadow(16px 0 0 #f4f1ea) drop-shadow(-16px 0 0 #f4f1ea) drop-shadow(0 16px 0 #f4f1ea) drop-shadow(0 -16px 0 #f4f1ea) drop-shadow(0 26px 30px rgba(0,0,0,.5))}
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
.pdot{position:absolute;width:52px;height:52px;border-radius:50%;border:3px solid #2a2f3a;opacity:.75}
.pdot.on{background:#cf2a24;border-color:#cf2a24;opacity:.92;border-radius:46% 54% 50% 50%}
.photo{position:absolute;background:#f4f1ea;padding:18px 18px 70px;box-shadow:0 22px 36px rgba(0,0,0,.5)}
.photo img{display:block;width:100%;height:100%;object-fit:cover;filter:saturate(.9) contrast(1.05)}
svg.mk{position:absolute;overflow:visible}
svg.mk path{fill:none;stroke:#cf2a24;stroke-width:9;stroke-linecap:round;stroke-linejoin:round}
</style>'''


def scenes(A):
    return [('s1', 0, 5.10), ('s2', 5.10, 10.36), ('s3', 10.36, DUR)]


# yazdırılmış 10x10 nokta tablosu (kâğıdın üstünde)
DOTS = ''.join(f'<div class="pdot" id="d{i}" style="left:{70 + (i % 10) * 76}px;top:{150 + (i // 10) * 64}px"></div>' for i in range(100))


def ring(id_, w, h, seed):
    """Elle çizilmiş daire: 3 hafif farklı varyant (kaynama). Kapanmayan, üst üste binen uç."""
    import math, random
    out = []
    for v in range(3):
        r = random.Random(seed * 10 + v); pts = []
        for k in range(26):
            a = -2.2 + k / 25 * (2 * math.pi + .5); j = 1 + r.uniform(-.035, .035)
            pts.append((w / 2 + math.cos(a) * w / 2 * j, h / 2 + math.sin(a) * h / 2 * j * (1 + .04 * math.sin(a * 2))))
        d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts)
        out.append(f'<path id="{id_}v{v}" d="{d}" pathLength="1" style="stroke-dasharray:1;stroke-dashoffset:1;opacity:{1 if v == 0 else 0}"/>')
    return f'<svg class="mk" id="{id_}" width="{w}" height="{h}" viewBox="0 0 {w} {h}">' + ''.join(out) + '</svg>'


SCENE_HTML = r'''
  <section id="s1" class="scene clip">
    <div class="tape" id="t1" style="left:190px;top:268px;transform:rotate(-32deg)"></div>
    <div class="tape" id="t2" style="left:690px;top:282px;transform:rotate(30deg)"></div>
    <div class="kraft" id="n1" style="left:500px;top:1180px;width:480px;height:270px;transform:rotate(4deg);padding:28px 30px">
      <div class="hand" style="font-size:44px;color:#5a3a1a">SORU 1</div>
      <div class="hand" style="font-size:58px">Neden okuduğu işi yapmıyor?</div>
    </div>
  </section>
  <section id="s2" class="scene clip">
    <div class="sheet" id="sh" style="left:70px;top:200px;width:940px;height:1180px;transform:rotate(-1.5deg)">
      <div class="print" style="position:absolute;left:70px;top:70px">MAAŞLI ÇALIŞAN 100 LİSANS MEZUNU</div>
      ''' + DOTS + r'''
      <div class="hand red" id="h43" style="position:absolute;left:80px;top:830px;font-size:230px;clip-path:inset(0 100% 0 0)">%43</div>
      <div class="hand" id="h43t" style="position:absolute;left:470px;top:900px;font-size:66px;width:420px;clip-path:inset(0 100% 0 0)">alanının dışında</div>
      <div style="position:absolute;left:40px;top:820px">''' + ring('r43', 420, 250, 3) + r'''</div>
      <div class="print" style="position:absolute;left:70px;top:1110px;font-size:18px">Kaynak: TÜİK Yükseköğretim İstihdam Göstergeleri 2025</div>
    </div>
  </section>
  <section id="s3" class="scene clip">
    <div class="photo" id="ph" style="left:90px;top:260px;width:900px;height:640px;transform:rotate(-3deg)"><img src="media/kep.jpg"></div>
    <div class="tape" id="t3" style="left:80px;top:230px;transform:rotate(-28deg)"></div>
    <div class="tape" id="t4" style="left:830px;top:235px;transform:rotate(24deg)"></div>
    <div class="kraft" id="n3" style="left:140px;top:1000px;width:700px;height:250px;transform:rotate(-2.5deg);padding:30px 36px">
      <div class="hand" id="q3" style="font-size:76px;clip-path:inset(0 100% 0 0)">Asıl tuzak bu mu?</div>
      <div class="hand red" id="q3b" style="font-size:56px;clip-path:inset(0 100% 0 0)">→ cevap sonda</div>
    </div>
  </section>
'''

SCENE_JS = r'''
// ---- MASA ÜSTÜ hareket dili: 12 fps adımlı (stop-motion), nesne masaya konur; kalem yazar.
const F=1/12;
const put=(s,t,o={})=>{const n=o.n??5;tl.fromTo(s,{opacity:0},{opacity:1,duration:.001},t);
  tl.fromTo(s,{x:o.x??0,y:o.y??160,rotation:(o.r??0)+(o.dr??-7),scale:o.s??1.06},
  {x:0,y:0,rotation:o.r??0,scale:1,duration:n*F,ease:`steps(${n})`,immediateRender:false},t);};
const take=(s,t,o={})=>{const n=o.n??4;tl.to(s,{x:o.x??-1300,rotation:'+=6',duration:n*F,ease:`steps(${n})`},t);};
const tape=(s,t,r)=>tl.fromTo(s,{opacity:0,scaleX:.2,rotation:r,transformOrigin:'0% 50%'},{opacity:1,scaleX:1,rotation:r,duration:3*F,ease:'steps(3)'},t);
const write=(s,t,d)=>{const n=Math.max(3,Math.round(d/F));tl.fromTo(s,{clipPath:'inset(0 100% 0 0)'},{clipPath:'inset(0 0% 0 0)',duration:n*F,ease:`steps(${n})`},t);};
const draw=(id,t,d,end)=>{const n=Math.round(d/F);for(let v=0;v<3;v++)tl.fromTo(`#${id}v${v}`,{strokeDashoffset:1},{strokeDashoffset:0,duration:n*F,ease:`steps(${n})`},t);
  for(let k=0;t+k*2*F<end;k++){const v=k%3;for(let u=0;u<3;u++)tl.set(`#${id}v${u}`,{opacity:u===v?1:0},t+k*2*F);}};
// elde kamera: deterministik yavaş kayma + mikro sarsıntı, 12 fps adımlı
for(let k=0;k*F<__DUR__;k++){const t=k*F;tl.set('.bg, .scene',{x:Math.sin(t*.41)*14+Math.sin(t*2.3+1)*2.2,y:Math.sin(t*.29+2)*10+Math.cos(t*2.9)*2,rotation:Math.sin(t*.23)*.35},t);}
// S1 — polaroid bantlanır, kraft not konur
tape('#t1',.25,-32); tape('#t2',.5,30); put('#n1',1.2,{r:4,y:120,x:60});
// S2 — kâğıt kayar, 43 nokta kalemle doldurulur, %43 yazılır, daire çizilir
put('#sh',5.15,{r:-1.5,y:900,dr:-4,n:6});
for(let i=0;i<43;i++) tl.set('#d'+i,{className:'pdot on'},7.9+Math.floor(i/3)*F);
write('#h43',8.25,.6); write('#h43t',8.95,.7); draw('r43',9.4,.6,10.36); take('#sh',10.05);
// S3 — fotoğraf masaya düşer, bantlanır, not yazılır
put('#ph',10.45,{r:-3,y:-140,dr:6,s:1.1,n:5}); tape('#t3',10.95,-28); tape('#t4',11.15,24);
put('#n3',11.45,{r:-2.5,y:200}); write('#q3',11.75,.7); write('#q3b',12.5,.5);
'''.replace('__DUR__', str(DUR))


def SFX(A):
    return [[.25, 'f:bant', -6, 0, 'bant1'], [.5, 'f:bant', -8, 0, 'bant2'], [1.2, 'f:kagit_kay', -8, 0, 'not'],
            [5.15, 'f:kagit_kay', -5, 0, 'kagit'], [7.9, 'f:kalem_yaz', -8, 0, 'noktalar'], [8.25, 'f:kalem_yaz', -6, 1, '43'],
            [9.4, 'f:kalem_daire', -6, 1, 'daire'], [10.05, 'f:kagit_kay', -9, 0, 'kagit_cek'], [10.45, 'f:foto_birak', -5, 0, 'foto'], [10.95, 'f:bant', -7, 0, 'bant3'],
            [11.45, 'f:kagit_kay', -9, 0, 'not3'], [11.75, 'f:kalem_yaz', -8, 0, 'yazi']]


def RISERS(A): return []
