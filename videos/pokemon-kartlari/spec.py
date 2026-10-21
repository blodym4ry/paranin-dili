import os
# Şablon: MÜZAYEDE SALONU (Ata seçimi, 21 Eki). Kinetik tabanı + EXTRA_CSS ile bordo kadife / altın / spot ışığı.
# Gerçek görseller (Ata, 21 Eki): media/ altında gerçek kart fotoğrafları + X'ten B-roll (kaynaklar.md). Kart çizimi yok, gerçek foto var.
# Avatar (kahverengi kapüşon+gözlük): s1 kanca+kilit, s4 "Peki yeni kartlar?", s7 CTA+döngü.
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [
    (N('logan', 'pol'), 'Logan Paul'), (N('pikaçu'), 'Pikachu'), (N('çarizard'), 'Charizard'), (N('pi', 'es', 'ey'), 'PSA'),
    (N('dört', 'milyon', 'dolar'), '4 milyon dolar'), (N('dört', 'milyon', 'doları'), '4 milyon doları'),
    (N('dokuz', 'not'), '9 not'), (N('dokuz', 'notluyu'), '9 notluyu'), (N('dokuz', 'notlu'), '9 notlu'), (N('on', 'notlu'), '10 notlu'),
    (N('üç', 'adımda'), '3 adımda'), (N('bin', 'dokuz', 'yüz', 'doksan', 'sekizde'), "1998'de"), (N('otuz', 'dokuz'), '39'),
    (N('on', 'altı', 'buçuk', 'milyon', 'dolara'), '16,5 milyon dolara'), (N('bin', 'dokuz', 'yüz', 'doksan', 'dokuz'), '1999'),
    (N('sekiz', 'bin', 'dolar'), '8.000 dolar'), (N('otuz', 'iki', 'bin'), '32.000'), (N('üç', 'yüz', 'otuz', 'bin'), '330.000'),
    (N('beş', 'bin', 'üç', 'yüz'), '5.300'), (N('yüz', 'yirmi', 'dördü'), "124'ü"), (N('altı', 'milyon'), '6 milyon'),
    (N('yirmi', 'beş', 'dolar'), '25 dolar'), (N('yirmi', 'kartla'), '20 kartla'),
]
EM = {'kıtlığında', 'notunda', 'kusursuz', 'nadir', 'gerçekleşmiş', 'damgasına', 'kaydet', 'takasta'}
RED = {'4 milyon dolar', "124'ü", 'değil'}
FRONT = [250, 330, 580, 815, 18]
AV = {'s1': FRONT, 's2': None, 's3': None, 's4': [290, 380, 500, 703, 18], 's5': None, 's6': None, 's7': FRONT}

EXTRA_CSS = r'''<style>
:root{--gold:#d9b25f;--red:#e0503f;--cap-em-bg:#d9b25f;--cap-em-fg:#1a0b0e}
body,#root{background:#14080b}
.bg{background:radial-gradient(ellipse 120% 70% at 50% 0%,#4a1520 0%,#2a0c12 45%,#14080b 80%)}
.bg::before{content:'';position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(0,0,0,.18) 0 3px,transparent 3px 9px);opacity:.5}
.bg::after{content:'';position:absolute;left:190px;top:-80px;width:700px;height:1300px;background:conic-gradient(from 168deg at 50% 0%,transparent 0deg,rgba(255,236,190,.10) 12deg,transparent 24deg);filter:blur(6px)}
#grid{display:none}
#avbox{filter:drop-shadow(0 0 0 #d9b25f) drop-shadow(5px 0 0 #d9b25f) drop-shadow(-5px 0 0 #d9b25f) drop-shadow(0 5px 0 #d9b25f) drop-shadow(0 -5px 0 #d9b25f) drop-shadow(0 30px 40px rgba(0,0,0,.6))}
.ser{font-family:'DM Serif Display';font-weight:400;letter-spacing:-.01em}
.lot{font:700 26px 'IBM Plex Mono';letter-spacing:.22em;color:#d9b25f}
.slab{position:absolute;width:210px;height:330px;border-radius:14px;background:linear-gradient(160deg,rgba(255,255,255,.22),rgba(255,255,255,.05));border:3px solid rgba(255,255,255,.35);box-shadow:0 20px 40px rgba(0,0,0,.5)}
.slab .lab{position:absolute;left:10px;right:10px;top:10px;height:62px;border-radius:6px;background:#f3efe6;color:#14080b;font:800 20px 'Inter Tight';display:flex;align-items:center;justify-content:space-between;padding:0 12px}
.slab .lab b{font:900 40px 'Inter Tight'}
.slab .crd{position:absolute;left:22px;right:22px;top:86px;bottom:18px;border-radius:10px;background:repeating-linear-gradient(45deg,#7a1f2b 0 10px,#5e1621 10px 20px);border:4px solid #d9b25f}
.slab .crd::after{content:'';position:absolute;left:50%;top:50%;width:62px;height:62px;margin:-31px;border-radius:50%;background:radial-gradient(circle,#f3efe6 0 30%,#14080b 31% 38%,#e0503f 39%)}
.plinth{position:absolute;width:560px;height:60px;border-radius:50%;background:radial-gradient(ellipse,rgba(217,178,95,.45),transparent 70%)}
.tag{position:absolute;background:#f3efe6;color:#14080b;border-radius:10px;padding:14px 26px;font:900 66px 'Inter Tight';letter-spacing:-.03em;box-shadow:0 14px 30px rgba(0,0,0,.45)}
.tag::before{content:'';position:absolute;left:-18px;top:50%;width:22px;height:22px;margin-top:-11px;border-radius:50%;background:#14080b;border:5px solid #f3efe6}
.rimg{position:absolute;left:0;top:0;display:block;border-radius:12px;box-shadow:0 24px 50px rgba(0,0,0,.6)}
.nb{position:absolute;left:50%;bottom:-34px;transform:translateX(-50%);background:#f3efe6;color:#14080b;font:900 46px 'Inter Tight';padding:2px 22px;border-radius:10px;box-shadow:0 8px 20px rgba(0,0,0,.5);white-space:nowrap}
.step{font:800 30px 'IBM Plex Mono';letter-spacing:.14em;color:#14080b;background:#d9b25f;padding:8px 18px;border-radius:8px}
</style>'''


def BROLL(A):
    # gerçek görüntü: Ripit/Goldin satış anı (konfeti) ve teslim (X: @nexta_tv, @GuyImprov — kaynaklar.md)
    return [{'id': 'br_sat', 'src': 'parti.mp4', 'a': A('Bu', 19.5) - .05, 'b': A('Birinci') - .15, 'ms': 3.55, 'dim': .45},
            {'id': 'br_tes', 'src': 'teslim.mp4', 'a': A('İkinci') - .1, 'b': A('İkinci') + 5.8, 'ms': 0, 'dim': .8}]


def scenes(A):
    b = lambda t: round(t - .1, 3)
    t2 = A('O'); t3 = A('Birinci'); t4 = A('Peki'); t5 = A('Geçen'); t6 = A('İkinci'); t7 = A('Çekmeceyi')
    return [('s1', 0, b(t2)), ('s2', b(t2), b(t3)), ('s3', b(t3), b(t4)), ('s4', b(t4), b(t5)), ('s5', b(t5), b(t6)),
            ('s6', b(t6), b(t7)), ('s7', b(t7), DUR)]


def SFX(A):
    return [[A('4 milyon dolar'), 'impact', -8, 1, 'fark'], [A('39'), 'pop', -11, 0, '39'], [A('Logan Paul'), 'ui_click', -12, 0, 'paul'],
            [A('sattı.'), 'stamp', -6, 1, 'gavel'], [A('damgasına'), 'marker', -11, 0, 'stamp'], [A('330.000'), 'impact', -9, 1, '330k'],
            [A("124'ü"), 'stamp', -9, 1, '124'], [A('6 milyon'), 'gears', -12, 0, 'count'], [A('Kusursuz,'), 'impact', -9, 1, 'nadir'],
            [A('ilandaki'), 'paper_drop', -11, 0, 'ilan'], [A('gerçekleşmiş'), 'success', -12, 0, 'sold'], [A('25 dolar'), 'ui_click', -11, 0, 'fee'],
            [A('kaydet.') + .05, 'success', -10, 1, 'kaydet'], [A('kıtlığında.'), 'impact', -9, 1, 'loop']]


def RISERS(A): return [[A('Birinci') - .3, 'sharp', -10], [A('Peki') - .2, 'metallic', -11]]


SCENE_HTML = r'''
  <section id="s1" class="scene clip">
    <div class="a lot" id="s1l" style="left:0;right:0;top:250px;text-align:center">LOT · AYNI KART</div>
    <div class="a" id="s1s9" style="left:12px;top:560px;width:210px;height:330px;transform:scale(.8);transform-origin:0 0"><img class="rimg" src="media/pikachu_slab.jpg" width="210" height="349" style="filter:grayscale(.75) brightness(.8)"><div class="nb">NOT 9</div></div>
    <div class="a" id="s1s10" style="left:900px;top:560px;width:210px;height:330px;transform:scale(.8);transform-origin:0 0"><img class="rimg" src="media/pikachu_slab.jpg" width="210" height="349"><div class="nb">NOT 10</div></div>
    <div class="a ser" id="s1d" style="left:0;right:0;top:1190px;text-align:center;font-size:92px;color:#d9b25f">+4.000.000 $</div>
  </section>
  <section id="s2" class="scene clip">
    <div class="a lot" id="s2l" style="left:60px;top:270px">LOT 1998 · ÇİZİM YARIŞMASI ÖDÜLÜ</div>
    <div class="a ser" id="s2h" style="left:60px;top:320px;font-size:84px;line-height:1">Sadece <span style="color:#d9b25f">39</span> kart</div>
    <div class="a plinth" id="s2p" style="left:260px;top:1040px"></div>
    <div class="a" id="s2c" style="left:390px;top:500px;width:300px;height:499px"><img class="rimg" src="media/pikachu_slab.jpg" width="300" height="499"></div>
    <div class="a" id="s2lp" style="left:40px;top:520px;width:1000px;height:563px"><img class="rimg" src="media/logan_ring.jpg" width="1000" height="563" style="border:4px solid #d9b25f"></div>
    <div class="a mono" id="s2a" style="left:60px;top:1140px;font-size:30px;color:rgba(243,239,230,.8)">2021 · 9 notlu kopya + 4 milyon $ ile alındı</div>
    <div class="a tag" id="s2t" style="left:120px;top:1210px">5.275.000 $</div>
    <svg class="a" id="s2g" style="left:760px;top:1180px" width="230" height="190" viewBox="0 0 230 190"><g fill="#d9b25f"><rect x="60" y="20" width="130" height="56" rx="12" transform="rotate(-28 125 48)"/><rect x="40" y="70" width="20" height="120" rx="8" transform="rotate(-28 50 130)"/></g><rect x="0" y="170" width="200" height="16" rx="6" fill="#7a5a2b"/></svg>
    <div class="a lot" id="s2s" style="left:120px;top:1330px">ŞUBAT 2026 · GOLDIN · REKOR</div>
  </section>
  <section id="s3" class="scene clip">
    <div class="a step" id="s3st" style="left:60px;top:260px">ADIM 1</div>
    <div class="a ser" id="s3h" style="left:60px;top:330px;font-size:70px">İlk baskı damgasına bak</div>
    <div class="a" id="s3card" style="left:70px;top:455px;width:270px;height:452px"><img class="rimg" src="media/charizard_slab.jpg" width="270" height="452"></div>
    <svg class="a" id="s3ring" style="left:48px;top:658px" width="120" height="120" viewBox="0 0 120 120"><circle cx="60" cy="60" r="48" fill="none" stroke="#e0503f" stroke-width="8"/></svg>
    <div class="a lot" id="s3rl" style="left:70px;top:918px;color:#e0503f">↑ DAMGA</div>
    <div class="a mono" id="s3cap" style="left:430px;top:420px;font-size:26px;color:rgba(243,239,230,.8)">1999 · İLK BASKI · CHARIZARD</div>
    <div class="a" id="s3bars" style="left:430px;top:470px;width:600px;height:460px"></div>
    <div class="a mono" id="s3src" style="left:430px;top:945px;font-size:20px;color:rgba(243,239,230,.55)">PriceCharting · Ekim 2026 · yaklaşık</div>
    <div class="a" id="s3f" style="left:60px;top:1030px;width:960px;display:flex;align-items:baseline;gap:22px"><span class="ser" style="font-size:120px;color:#e0503f">124</span><span class="ser" style="font-size:60px;color:rgba(243,239,230,.7)">/ 5.325 kopya</span><span class="lot">→ NOT 10 · %2,3</span></div>
    <div class="a mono" id="s3f2" style="left:60px;top:1170px;font-size:20px;color:rgba(243,239,230,.55)">2025 itibarıyla · PSA nüfus raporu</div>
  </section>
  <section id="s4" class="scene clip">
    <div class="a ser" id="s4h" style="left:0;right:0;top:1130px;text-align:center;font-size:96px">Ya <span style="color:#d9b25f">yeni</span> kartlar?</div>
  </section>
  <section id="s5" class="scene clip">
    <div class="a" id="s5rain" data-layout-allow-overflow data-layout-allow-occlusion data-layout-allow-overlap style="left:0;top:0;width:1080px;height:1920px;overflow:hidden"></div>
    <div class="a lot" id="s5l" style="left:60px;top:300px">2025 · PSA · POKEMON</div>
    <div class="a ser" id="s5v" style="left:52px;top:340px;font-size:200px;color:#d9b25f;text-shadow:0 10px 30px rgba(0,0,0,.6)">0</div>
    <div class="a ser" id="s5u" style="left:60px;top:560px;font-size:64px;text-shadow:0 6px 20px rgba(0,0,0,.7)">kart "10" aldı</div>
    <div class="a" id="s5p" style="left:60px;top:700px;display:flex;align-items:baseline;gap:18px"><span class="ser" style="font-size:150px;color:#e0503f;text-shadow:0 8px 24px rgba(0,0,0,.6)">%50</span><span class="ser" style="font-size:50px;text-shadow:0 6px 20px rgba(0,0,0,.7)">notlananların yarısı</span></div>
    <div class="a ser" id="s5s" style="left:60px;top:960px;font-size:84px;background:#14080b;border:6px solid #d9b25f;padding:10px 30px;border-radius:12px">Kusursuz <span style="color:#e0503f">≠</span> nadir</div>
  </section>
  <section id="s6" class="scene clip">
    <div class="a step" id="s6st" style="left:60px;top:260px">ADIM 2</div>
    <div class="a ser" id="s6h" style="left:60px;top:330px;font-size:64px">İlana değil, satışa bak</div>
    <div class="a" id="s6a" style="left:60px;top:450px;width:440px;height:260px;border-radius:18px;background:rgba(243,239,230,.06);border:3px solid rgba(243,239,230,.25);padding:28px">
      <div class="lot" style="color:rgba(243,239,230,.7)">İLAN FİYATI</div><div class="ser" style="font-size:80px;margin-top:20px;color:rgba(243,239,230,.6)">istenen</div>
      <div id="s6x" style="position:absolute;left:20px;right:20px;top:150px;height:10px;background:#e0503f;transform-origin:0 50%"></div></div>
    <div class="a" id="s6b" style="left:540px;top:450px;width:480px;height:260px;border-radius:18px;background:#d9b25f;color:#14080b;padding:28px">
      <div class="lot" style="color:#14080b">GERÇEKLEŞEN SATIŞ</div><div class="ser" style="font-size:80px;margin-top:20px">ödenen ✓</div></div>
    <div class="a step" id="s6st3" style="left:60px;top:790px">ADIM 3</div>
    <div class="a ser" id="s6h3" style="left:60px;top:860px;font-size:64px">Notlatmanın bedeli</div>
    <div class="a" id="s6m" style="left:60px;top:960px;display:flex;align-items:baseline;gap:16px;flex-wrap:wrap;width:960px">
      <span class="ser" style="font-size:96px">25 $</span><span class="ser" style="font-size:60px;color:rgba(243,239,230,.7)">× en az 20 kart =</span><span class="ser" id="s6tot" style="font-size:96px;color:#d9b25f">~500 $</span></div>
    <div class="a mono" id="s6src" style="left:60px;top:1100px;font-size:20px;color:rgba(243,239,230,.55)">PSA en ucuz tarife · 2026 · üyelik gerekli</div>
  </section>
  <section id="s7" class="scene clip">
    <div class="a tag" id="s7t" style="left:330px;top:1180px;font-size:84px">KAYDET</div>
    <div class="a ser" id="s7a" style="left:0;right:0;top:1170px;text-align:center;font-size:70px">Değer = <span style="color:#d9b25f">not</span> + <span style="color:#d9b25f">kıtlık</span></div>
  </section>
'''

SCENE_JS = r'''
const at=(p,after=0)=>{for(const c of CAPS)for(const w of c.w)if(w[1]>=after&&w[0].toLowerCase().startsWith(p.toLowerCase()))return w[1];return null;};
// S1 kanca: 9 vs 10 → +4M
inn('#s1l',.2,{y:-20}); inn('#s1s9',at('Biri')+.1,{y:30}); inn('#s1s10',at('biri',2.5)+.05,{y:30}); slam('#s1d',at('4 milyon'));
tl.to(['#s1s9','#s1s10'],{opacity:.35,duration:.3},at('4 milyon'));
// S2 müzayede: tek kart vitrinde, fiyat etiketi sayar, çekiç
const s2=st('s2'); inn('#s2l',s2+.4); inn('#s2h',at('39')-.1); inn('#s2p',s2+.5,{y:0}); inn('#s2c',s2+.55,{y:60,s:.9});
tl.fromTo('#s2c',{rotationY:-18},{rotationY:12,duration:st('s3')-s2,ease:'sine.inOut'},s2+.5);
tl.to('#s2c',{opacity:0,y:-30,duration:.3},at('Logan Paul')-.2); inn('#s2lp',at('Logan Paul'),{y:40}); tl.to(['#s2lp','#s2p'],{opacity:0,duration:.3},at('Bu',19.5)-.15); inn('#s2a',at('Logan Paul')); inn('#s2t',at('Logan Paul')+.3,{y:20}); count('#s2t',5275000,16492000,at('16,5')-.4,1.3,v=>fmt(v)+' $');
tl.fromTo('#s2g',{opacity:0,rotation:-25,transformOrigin:'90% 90%'},{opacity:1,rotation:0,duration:.18,ease:'power4.in'},at('sattı')-.12); inn('#s2s',at('sattı')+.1,{y:10});
// S3 adım 1: damga + fiyat merdiveni + 124/5325
const s3=st('s3'); inn('#s3st',s3+.4,{y:-10}); inn('#s3h',s3+.5); inn('#s3card',s3+.6,{y:40});
tl.fromTo('#s3ring',{opacity:0,scale:1.8,transformOrigin:'50% 50%'},{opacity:1,scale:1,duration:.3,ease:'power3.out'},at('damgasına')); inn('#s3rl',at('damgasına')+.2,{y:0});
inn('#s3cap',at('1999')); inn('#s3src',at('1999')+.3,{y:0});
(function(){const box=$('#s3bars');const P=[['NOTSUZ','~8 bin $',8],['NOT 9','~32 bin $',32],['NOT 10','~330 bin $',330]];
 const H=v=>Math.max(14,Math.log10(v)/Math.log10(330)*300);
 box.innerHTML=P.map(([l,t,v],i)=>`<div style="position:absolute;left:${i*200}px;bottom:40px;width:160px;height:${H(v)}px;border-radius:10px 10px 0 0;background:${i==2?'#d9b25f':'rgba(243,239,230,.3)'};transform-origin:50% 100%" id="s3b${i}"></div><div class="ser" id="s3t${i}" style="position:absolute;left:${i*200-20}px;width:200px;text-align:center;bottom:${H(v)+52}px;font-size:40px;color:${i==2?'#d9b25f':'#f3efe6'}">${t}</div><div class="lot" style="position:absolute;left:${i*200}px;width:160px;text-align:center;bottom:0;font-size:20px">${l}</div>`).join('');
 const T=[at('notsuz'),at('9 notlu',30),at('10 notlu',32)];
 [0,1,2].forEach(i=>{tl.fromTo('#s3b'+i,{scaleY:0},{scaleY:1,duration:.45,ease:'power3.out'},T[i]);tl.fromTo('#s3t'+i,{opacity:0},{opacity:1,duration:.2},T[i]+.3);});})();
inn('#s3f',at('Ama',34)); inn('#s3f2',at('Ama',34)+.4,{y:0});
// S4 ara kanca
inn('#s4h',st('s4')+.25,{s:1.1});
// S5 10 yağmuru
const s5=st('s5'), d5=st('s6')-s5;
(function(){const r=$('#s5rain');let h='';for(let i=0;i<26;i++){const x=(i*173)%1000-40,dl=(i*0.37)%2.4,sc=.35+((i*7)%5)/10;h+=`<div id="s5r${i}" style="position:absolute;left:${x}px;top:-420px;width:210px;height:330px;transform:scale(${sc});opacity:.8"><img class="rimg" src="media/${i%2?'charizard_slab.jpg':'pikachu_slab.jpg'}" width="210" height="${i%2?352:349}"></div>`;}
 r.innerHTML=h; for(let i=0;i<26;i++){const dl=(i*0.37)%2.4;tl.fromTo('#s5r'+i,{y:0,rotation:-15+(i%5)*7},{y:2500,rotation:15-(i%4)*8,duration:3.2,ease:'none'},s5+.3+dl);}})();
inn('#s5l',s5+.4); inn('#s5v',s5+.45); count('#s5v',0,6000000,at('6 milyon')-.5,1.2,v=>fmt(v)); inn('#s5u',at('6 milyon')+.5);
inn('#s5p',at('Notlananların')); slam('#s5s',at('Kusursuz'));
// S6 adım 2 + 3
const s6=st('s6'); inn('#s6st',s6+.4,{y:-10}); inn('#s6h',s6+.5); inn('#s6a',at('ilandaki'),{y:30});
tl.fromTo('#s6x',{scaleX:0},{scaleX:1,duration:.3,ease:'power3.out'},at('değil',49)); slam('#s6b',at('gerçekleşmiş'));
inn('#s6st3',at('Üçüncü'),{y:-10}); inn('#s6h3',at('Üçüncü')+.1); inn('#s6m',at('notlatma'),{y:20}); slam('#s6tot',at('20 kartla')); inn('#s6src',at('20 kartla')+.3,{y:0});
// S7 CTA + döngü
slam('#s7t',at('kaydet')); out('#s7t',at('Çünkü',58)-.2); inn('#s7a',at('Çünkü',58)+.1);
'''
