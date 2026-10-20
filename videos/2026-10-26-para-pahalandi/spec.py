import os
# Gazete stili (video 1 Kinetik idi). Ayrık yöntem: avatar s1 (kanca+kilit), s4 (ara kanca), s9 (CTA+döngü).
CSS_FILE = 'gazete.css.html'
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [
    (N('üç', 'halkalı'), '3 halkalı'), (N('on', 'yıllık'), '10 yıllık'), (N('beş', "ekim'de"), "5 Ekim'de"),
    (N('yüzde', 'iki', 'virgül', 'doksan', 'beşe'), "%2,95'e"), (N('iki', 'bin', 'sekizden'), "2008'den"),
    (N('sekiz', 'günde'), '8 günde'), (N('iki', 'bin', 'on', 'üçte'), "2013'te"),
    (N('ocak', 'iki', 'bin', 'on', 'dörtte'), "Ocak 2014'te"), (N('yüzde', 'dört', 'buçuktan'), "%4,5'tan"), (N('yüzde', 'ona'), "%10'a"),
]
EM = {'kredi', 'faizin', "washington'da", 'ankara', 'zincir', 'cebin', 'kaydet', 'zayıflatır', 'kırılgan', 'baskı', 'yukarı'}
RED = {'düşmüyor', 'zayıflatır', "%10'a", 'yukarı', 'indiremez'}
FRONT = [250, 375, 580, 815, 6]
AV = {'s1': FRONT, 's2': None, 's3': None, 's4': [290, 400, 500, 703, 6], 's5': None, 's6': None, 's7': None, 's8': None, 's9': FRONT}


def scenes(A):
    b = lambda t: round(t - .1, 3)
    t2 = A('Birinci'); t3 = A('Eylülde'); t4 = A('Peki'); t5 = A('İkinci'); t6 = A('Bunu'); t7 = A("Ocak 2014'te"); t8 = A('Üçüncü'); t9 = A('Kaydet')
    return [('s1', 0, b(t2)), ('s2', b(t2), b(t3)), ('s3', b(t3), b(t4)), ('s4', b(t4), b(t5)), ('s5', b(t5), b(t6)),
            ('s6', b(t6), b(t7)), ('s7', b(t7), b(t8)), ('s8', b(t8), b(t9)), ('s9', b(t9), DUR)]


def SFX(A):
    return [[A('düşmüyor?'), 'stamp', -9, 1, 'hook'], [A("Washington'da."), 'impact', -8, 1, 'wash'], [A('zincir'), 'gears', -12, 0, 'chain'],
            [A("%2,95'e"), 'stamp', -8, 1, '2.95'], [A("2008'den"), 'paper_drop', -9, 0, 'stamp'], [A('Avrupa'), 'stamp', -10, 0, 'ecb'],
            [A('Amerika', 21), 'stamp', -10, 0, 'fed'], [A('Japonya'), 'stamp', -10, 0, 'boj'], [A('piyasalardan'), 'whoosh_hollow', -12, 0, 'flow'],
            [A('zayıflatır,'), 'impact', -8, 1, 'tl'], [A('kırılgan'), 'stamp', -9, 1, 'fragile'], [A("%10'a"), 'impact', -8, 1, '10'],
            [A('indiremez,'), 'marker', -11, 0, 'slow'], [A('Kaydet') + .1, 'success', -10, 1, 'kaydet'], [A('Ankara', 60), 'impact', -8, 1, 'loop']]


def RISERS(A): return [[A('Peki') - .5, 'sharp', -9], [A('Bunu') - .4, 'metallic', -10]]


SCENE_HTML = r'''
  <div id="mast" style="position:absolute;left:60px;right:60px;top:236px">
    <div style="height:5px;background:#161412"></div>
    <div style="display:flex;justify-content:space-between;align-items:baseline;padding:10px 0 6px">
      <span style="font:400 66px/1 'DM Serif Display';color:#161412">Paranın Dili</span>
      <span class="mono" style="font-size:22px">EKİM 2026 · FAİZ</span></div>
    <div style="height:2px;background:#161412"></div>
  </div>
  <section id="s1" class="scene clip">
    <div class="a h" id="s1h" style="left:60px;top:1215px;font-size:84px">Kredi faizin neden</div>
    <div class="a h red" id="s1h2" style="left:60px;top:1305px;font-size:84px">düşmüyor?</div>
    <div class="a h" id="s1c" style="left:60px;top:1215px;font-size:84px">Sebebin bir kısmı:</div>
    <div class="a h red" id="s1c2" style="left:60px;top:1305px;font-size:84px">Washington</div>
    <div class="a" id="s1d" style="left:60px;top:1230px;display:flex;align-items:center;gap:26px">
      <svg width="250" height="110" viewBox="0 0 250 110"><g fill="none" stroke-width="12"><ellipse id="r1" cx="55" cy="55" rx="45" ry="32" stroke="#161412"/><ellipse id="r2" cx="125" cy="55" rx="45" ry="32" stroke="#161412"/><ellipse id="r3" cx="195" cy="55" rx="45" ry="32" stroke="#c8261b"/></g></svg>
      <div><div class="h" style="font-size:72px">3 halka</div><div class="mono">sonuncusu: senin cebin</div></div></div>
  </section>
  <section id="s2" class="scene clip">
    <div class="a lab" id="s2l" style="left:60px;top:400px">HALKA 1 · AMERİKA</div>
    <div class="a h" id="s2h" style="left:60px;top:450px;font-size:76px;white-space:normal;width:960px;line-height:1.02">Enflasyondan arındırılmış 10 yıllık faiz</div>
    <div class="a big" id="s2v" style="left:52px;top:640px;font-size:250px">%1,80</div>
    <div class="a mono" id="s2m" style="left:60px;top:880px">ABD 10Y TIPS · 5 EKİM 2026 KAPANIŞ</div>
    <div class="a h red" id="s2s" style="left:470px;top:960px;font-size:62px;border:6px solid #c8261b;padding:8px 22px;border-radius:8px;transform:rotate(-5deg)">2008'DEN BERİ EN YÜKSEK</div>
  </section>
  <section id="s3" class="scene clip">
    <div class="a lab" id="s3l" style="left:60px;top:400px">EYLÜL 2026 · 8 GÜNDE 3 ARTIŞ</div>
    <div class="a card" id="s3r0" style="left:60px;top:470px;width:960px;display:flex;justify-content:space-between;align-items:baseline"><span class="mono">10 EYLÜL</span><span class="h" style="font-size:66px">Avrupa</span><span class="h red" style="font-size:66px">%2,50 ↑</span></div>
    <div class="a card" id="s3r1" style="left:60px;top:650px;width:960px;display:flex;justify-content:space-between;align-items:baseline"><span class="mono">16 EYLÜL</span><span class="h" style="font-size:66px">Amerika</span><span class="h red" style="font-size:66px">%3,75–4 ↑</span></div>
    <div class="a card" id="s3r2" style="left:60px;top:830px;width:960px;display:flex;justify-content:space-between;align-items:baseline"><span class="mono">18 EYLÜL</span><span class="h" style="font-size:66px">Japonya</span><span class="h red" style="font-size:66px">%1,25 ↑</span></div>
    <div class="a mono" id="s3m" style="left:60px;top:1010px">merkez bankası politika faizleri</div>
  </section>
  <section id="s4" class="scene clip">
    <div class="a h" id="s4h" style="left:0;right:0;top:1150px;text-align:center;font-size:96px">Bize <span class="red">ne?</span></div>
  </section>
  <section id="s5" class="scene clip">
    <div class="a lab" id="s5l" style="left:60px;top:400px">HALKA 2 · PARA YER DEĞİŞTİRİR</div>
    <div class="a card" id="s5a" style="left:60px;top:480px;width:380px;height:220px;text-align:center"><div class="mono">RİSKLİ</div><div class="h" style="font-size:72px;margin-top:30px">Türkiye</div></div>
    <div class="a card" id="s5b" style="left:640px;top:480px;width:380px;height:220px;text-align:center;background:#161412"><div class="mono" style="color:rgba(242,237,226,.7)">GÜVENLİ</div><div class="h" style="font-size:66px;margin-top:30px;color:#f2ede2">ABD tahvili</div></div>
    <svg class="a" id="s5svg" style="left:440px;top:540px" width="200" height="100" viewBox="0 0 200 100"><path d="M10 50 H170" stroke="#161412" stroke-width="8"/><path d="M150 25 L185 50 L150 75" fill="none" stroke="#161412" stroke-width="8"/>
      <circle id="d0" cx="20" cy="50" r="12" fill="#c8261b"/><circle id="d1" cx="20" cy="50" r="12" fill="#c8261b"/><circle id="d2" cx="20" cy="50" r="12" fill="#c8261b"/></svg>
    <div class="a" id="s5x" style="left:60px;top:800px;width:960px;display:flex;gap:40px">
      <div id="s5t" class="card" style="flex:1;text-align:center"><div class="mono">LİRA</div><div class="big red" style="font-size:150px">↓</div></div>
      <div id="s5f" class="card" style="flex:1;text-align:center"><div class="mono">FAİZLER</div><div class="big red" style="font-size:150px">↑</div></div></div>
  </section>
  <section id="s6" class="scene clip">
    <div class="a ghost" id="s6g" data-layout-allow-overflow data-layout-allow-occlusion data-layout-allow-overlap style="left:420px;top:1000px">2013</div>
    <div class="a lab" id="s6l" style="left:60px;top:400px">BUNU YAŞADIK · 2013</div>
    <div class="a h" id="s6h" style="left:60px;top:450px;font-size:70px;white-space:normal;width:960px;line-height:1.05">ABD: "tahvil alımını azaltacağız"</div>
    <div class="a h red" id="s6s" style="left:60px;top:650px;font-size:84px;border:7px solid #c8261b;padding:6px 26px;border-radius:8px">KIRILGAN BEŞLİ</div>
    <div class="a" id="s6list" style="left:60px;top:800px;width:960px;display:flex;flex-wrap:wrap;gap:16px 34px">
      <span class="h red" style="font-size:64px">Türkiye</span><span class="h" style="font-size:64px;opacity:.45">Brezilya</span><span class="h" style="font-size:64px;opacity:.45">Hindistan</span>
      <span class="h" style="font-size:64px;opacity:.45">Endonezya</span><span class="h" style="font-size:64px;opacity:.45">G. Afrika</span></div>
    <div class="a mono" id="s6m" style="left:60px;top:1010px">Morgan Stanley, Ağustos 2013</div>
  </section>
  <section id="s7" class="scene clip">
    <div class="a lab" id="s7l" style="left:60px;top:400px">TCMB · 28 OCAK 2014 · HAFTALIK REPO</div>
    <div class="a" id="s7b1" style="left:120px;top:470px;width:330px;height:500px"><div id="s7f1" style="position:absolute;left:0;right:0;bottom:0;height:40%;background:repeating-linear-gradient(-45deg,#161412 0 5px,transparent 5px 12px);border:5px solid #161412;transform-origin:50% 100%"></div><div class="h" style="position:absolute;left:0;right:0;bottom:43%;text-align:center;font-size:90px">%4,5</div></div>
    <div class="a" id="s7b2" style="left:600px;top:470px;width:330px;height:500px"><div id="s7f2" style="position:absolute;left:0;right:0;bottom:0;height:89%;background:#c8261b;transform-origin:50% 100%"></div><div class="h red" style="position:absolute;left:0;right:0;bottom:91%;text-align:center;font-size:90px">%10</div></div>
    <div class="a mono" id="s7c1" style="left:120px;top:985px;width:330px;text-align:center">ÖNCE</div>
    <div class="a mono" id="s7c2" style="left:600px;top:985px;width:330px;text-align:center">TEK GECEDE</div>
  </section>
  <section id="s8" class="scene clip">
    <div class="a lab" id="s8l" style="left:60px;top:400px">HALKA 3 · SEN</div>
    <div class="a" id="s8r0" style="left:60px;top:470px;width:960px;display:flex;gap:22px;align-items:center"><div class="tick" id="s8k0"></div><div class="h" style="font-size:62px">Dışarıda baskı sürer</div></div>
    <div class="a" id="s8r1" style="left:60px;top:640px;width:960px;display:flex;gap:22px;align-items:center"><div class="tick" id="s8k1"></div><div class="h" style="font-size:62px">TCMB hızlı indiremez</div></div>
    <div class="a" id="s8r2" style="left:60px;top:810px;width:960px;display:flex;gap:22px;align-items:center"><div class="tick" id="s8k2"></div><div class="h red" style="font-size:62px">Kredi + kart faizi yavaş iner</div></div>
  </section>
  <section id="s9" class="scene clip">
    <div class="a h red" id="s9t" style="left:0;right:0;top:1230px;text-align:center;font-size:120px"><span style="border:8px solid #c8261b;padding:0 30px;border-radius:12px">KAYDET</span></div>
    <div class="a h" id="s9a" style="left:0;right:0;top:1215px;text-align:center;font-size:76px">Sebep her zaman</div>
    <div class="a h red" id="s9b" style="left:0;right:0;top:1305px;text-align:center;font-size:84px">Ankara değil.</div>
  </section>
'''

SCENE_JS = r'''
const at=(p,after=0)=>{for(const c of CAPS)for(const w of c.w)if(w[1]>=after&&w[0].toLowerCase().startsWith(p.toLowerCase()))return w[1];return null;};
inn('#mast',.05,{y:-20});
// S1 kanca + kilit
inn('#s1h',.3); slam('#s1h2',at('düşmüyor')); out(['#s1h','#s1h2'],at('Sebebin')-.2);
inn('#s1c',at('Sebebin')); slam('#s1c2',at("Washington")); out(['#s1c','#s1c2'],at('Arada')-.2);
inn('#s1d',at('Arada')); ['#r1','#r2','#r3'].forEach((r,i)=>tl.fromTo(r,{opacity:0},{opacity:1,duration:.2},at('Arada')+.3+i*.25));
// S2 halka 1
const s2=st('s2'); inn('#s2l',s2+.4); inn('#s2h',at('Amerika')); inn('#s2v',at('Amerika')+.3); count('#s2v',1.8,2.95,at('Amerika')+.45,at('%2,95')-at('Amerika')-.3,v=>v.toFixed(2).replace('.',','),'%');
inn('#s2m',at('%2,95')+.5,{y:10}); tl.fromTo('#s2s',{opacity:0,scale:1.6},{opacity:1,scale:1,duration:.25,ease:'power4.in'},at("2008'den"));
// S3 üç banka
const s3=st('s3'); inn('#s3l',s3+.4); slam('#s3r0',at('Avrupa')); slam('#s3r1',at('Amerika',21)); slam('#s3r2',at('Japonya')); inn('#s3m',at('artırdı')+.1,{y:10});
// S4 ara kanca
inn('#s4h',st('s4')+.35,{s:1.1});
// S5 halka 2
const s5=st('s5'); inn('#s5l',s5+.4); inn('#s5a',at('Para')); inn('#s5b',at('güvenli')); inn('#s5svg',at('güvenli')+.2,{y:0});
[0,1,2].forEach(i=>tl.fromTo('#d'+i,{attr:{cx:20},opacity:1},{attr:{cx:160},opacity:0,duration:.9,ease:'power1.in',repeat:2},at('piyasalardan')+i*.3));
tl.to('#s5a',{opacity:.45,duration:.4},at('çıkma')); inn('#s5t',at('lirayı'),{y:40}); inn('#s5f',at('faizleri'),{y:40});
// S6 2013
const s6=st('s6'); tl.fromTo('#s6g',{x:0,opacity:0},{x:-160,opacity:.07,duration:st('s7')-s6,ease:'none'},s6); inn('#s6l',s6+.4);
inn('#s6h',at('Amerika',37)); slam('#s6s',at('kırılgan')); inn('#s6list',at('kırılgan')+.3,{y:20}); inn('#s6m',at('listesine')+.2,{y:10});
// S7 2014 repo
const s7=st('s7'); inn('#s7l',s7+.4); inn('#s7b1',s7+.5,{y:0}); inn('#s7c1',s7+.5); tl.fromTo('#s7f1',{scaleY:0},{scaleY:1,duration:.5,ease:'power3.out'},s7+.55);
inn('#s7b2',at("%10'a")-.3,{y:0}); inn('#s7c2',at("%10'a")-.3); tl.fromTo('#s7f2',{scaleY:0},{scaleY:1,duration:.5,ease:'power4.out'},at("%10'a")-.25);
// S8 halka 3
const s8=st('s8'); inn('#s8l',s8+.4);
[['baskı',0],['Merkez',1],['bankalar',2]].forEach(([p,i])=>{const t=at(p,51)-.1; inn('#s8r'+i,t,{y:24}); tl.to('#s8k'+i,{backgroundColor:'#161412',duration:.15},t+.35);});
// S9 CTA + döngü
slam('#s9t',at('Kaydet')); out('#s9t',at('sebep',59)-.25); inn('#s9a',at('sebep',59)); slam('#s9b',at('Ankara',60));
'''
