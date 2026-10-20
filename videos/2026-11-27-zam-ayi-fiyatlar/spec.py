import os
# Gazete stili (önceki video Kinetik). Ayrık yöntem: avatar s1 (kanca), s8 (ara kanca 2), s10-s11 (kapanış + CTA/döngü).
CSS_FILE = 'gazete.css.html'
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [
    (N('dört', 'yılın'), '4 yılın'), (N('yüzde', 'dört', 'virgül', 'sekizin'), "%4,8'in"), (N('üç', 'kalemde'), '3 kalemde'),
    (N('iki', 'bin', 'yirmi', 'beşte'), "2025'te"), (N('yüzde', 'beş', 'virgül', 'sıfır', 'üç'), '%5,03'), (N('yüzde', 'iki'), '%2'),
    (N('bir', "ocak'ta"), "1 Ocak'ta"), (N('yüzde', 'on', 'sekiz', 'virgül', 'doksan', 'beş'), '%18,95'),
    (N('yüzde', 'beşi'), "%5'i"), (N('yüzde', 'yediyi'), "%7'yi"), (N('yüzde', 'yirmi', 'yedi'), '%27'),
    (N('yüzde', 'beş', 'virgül', 'sekiz', 'altı'), '%5,86'),
]
EM = {'zam', 'ocak', "ocak'ında", 'kalem', 'tarifesi', 'endeksli', 'takvimle', 'takvimi', 'kaydet', 'zammınla', 'işgücü', 'konuşulanı'}
RED = {'artıyor', '%5,03', '%18,95', '%27', '%5,86', 'pahalı'}
FRONT = [250, 375, 580, 815, 6]     # 740:1040 portre — saç ve çene görünür
AV = {'s1': FRONT, 's2': None, 's3': None, 's4': None, 's5': None, 's6': None, 's7': None, 's8': FRONT, 's9': None,
      's10': [640, 380, 380, 534, 6], 's11': FRONT}
EXTRA_CSS = '<style>#s2,#s3,#s4,#s5,#s6,#s7,#s9{transform:translateY(120px)}</style>'


def scenes(A):
    b = lambda t: round(t - .1, 3)
    t2 = A('Sonunda'); t3 = A("2025'te"); t4 = A('Peki'); t5 = A('Birinci'); t6 = A('İkinci'); t7 = A("Ocak'ta", 36)
    t8 = A('Üçüncüsü', 39); t9 = min(b(A('Asgari')), 42.28)   # ara kanca avatar parçası 42.24'te bitiyor
    t10 = A('Zam', 52); t11 = A('Kaydet')
    return [('s1', 0, b(t2)), ('s2', b(t2), b(t3)), ('s3', b(t3), b(t4)), ('s4', b(t4), b(t5)), ('s5', b(t5), b(t6)),
            ('s6', b(t6), b(t7)), ('s7', b(t7), b(t8)), ('s8', b(t8), t9), ('s9', t9, b(t10)), ('s10', b(t10), b(t11)),
            ('s11', b(t11), DUR)]


def SFX(A):
    return [[A('artıyor?'), 'stamp', -9, 1, 'hook'], [A("%4,8'in"), 'impact', -8, 1, '4.8'], [A('3 kalemde'), 'pop', -10, 0, '3'],
            [A('%5,03'), 'impact', -8, 1, 'jan'], [A('%2'), 'marker', -11, 0, 'avg'], [A('Birinci'), 'paper_drop', -10, 0, 'k1'],
            [A('%18,95'), 'stamp', -8, 1, 'harc'], [A('İkinci'), 'paper_drop', -10, 0, 'k2'], [A("%5'i"), 'marker', -11, 0, 'kira'],
            [A("%7'yi"), 'marker', -11, 0, 'hizmet'], [A('%27'), 'impact', -8, 1, 'asgari'], [A('%5,86'), 'stamp', -9, 1, 'lokanta'],
            [A('Kaydet') + .1, 'success', -10, 1, 'kaydet'], [A('takvimi'), 'impact', -9, 1, 'loop']]


def RISERS(A): return [[A('Peki') - .5, 'sharp', -9], [A('Üçüncüsü', 39) - .4, 'metallic', -10]]


SCENE_HTML = r'''
  <div id="mast" style="position:absolute;left:60px;right:60px;top:236px">
    <div style="height:5px;background:#161412"></div>
    <div style="display:flex;justify-content:space-between;align-items:baseline;padding:10px 0 6px">
      <span style="font:400 66px/1 'DM Serif Display';color:#161412">Paranın Dili</span>
      <span class="mono" style="font-size:22px">KASIM 2026 · ENFLASYON</span></div>
    <div style="height:2px;background:#161412"></div>
  </div>
  <section id="s1" class="scene clip">
    <div class="a h" id="s1h" style="left:60px;top:1215px;font-size:84px">Maaş zamlandı,</div>
    <div class="a h red" id="s1h2" style="left:60px;top:1305px;font-size:84px">fiyatlar da?</div>
    <div class="a" id="s1d" style="left:60px;top:1225px;display:flex;align-items:center;gap:30px">
      <div class="h red" style="font-size:150px;line-height:1">%4,8+</div>
      <div><div class="h" style="font-size:60px">her Ocak</div><div class="mono">son 4 yıl · aylık TÜFE</div></div></div>
  </section>
  <section id="s2" class="scene clip">
    <div class="a lab" id="s2l" style="left:60px;top:420px">OCAK NEDEN PAHALI?</div>
    <div class="a big" id="s2n" style="left:52px;top:470px;font-size:280px">3</div>
    <div class="a h" id="s2k" style="left:260px;top:560px;font-size:110px">kalem</div>
    <div class="a card" id="s2r0" style="left:60px;top:820px;width:960px;display:flex;justify-content:space-between;align-items:baseline"><span class="mono">KALEM 1</span><span class="h" style="font-size:62px">? ? ?</span></div>
    <div class="a card" id="s2r1" style="left:60px;top:980px;width:960px;display:flex;justify-content:space-between;align-items:baseline"><span class="mono">KALEM 2</span><span class="h" style="font-size:62px">? ? ?</span></div>
    <div class="a card" id="s2r2" style="left:60px;top:1140px;width:960px;display:flex;justify-content:space-between;align-items:baseline;background:#161412"><span class="mono" style="color:rgba(242,237,226,.7)">KALEM 3</span><span class="h" style="font-size:62px;color:#f2ede2">senin <span class="red">zammın</span></span></div>
  </section>
  <section id="s3" class="scene clip">
    <div class="a lab" id="s3l" style="left:60px;top:400px">2025 · AYLIK TÜFE (%) · TÜİK</div>
    <svg class="a" id="s3svg" style="left:40px;top:460px" width="1000" height="760" viewBox="0 0 1000 760"></svg>
  </section>
  <section id="s4" class="scene clip">
    <div class="a ghost" id="s4g" data-layout-allow-overflow data-layout-allow-occlusion data-layout-allow-overlap style="left:-20px;top:560px">OCAK</div>
    <div class="a h" id="s4h" style="left:0;right:0;top:620px;text-align:center;font-size:110px">Neden hep</div>
    <div class="a h red" id="s4h2" style="left:0;right:0;top:740px;text-align:center;font-size:170px">OCAK?</div>
  </section>
  <section id="s5" class="scene clip">
    <div class="a lab" id="s5l" style="left:60px;top:400px">KALEM 1 · DEVLETİN TARİFESİ</div>
    <div class="a" id="s5r0" style="left:60px;top:470px;width:960px;border-bottom:3px solid #161412;padding:16px 0"><span class="h" style="font-size:80px">MTV</span></div>
    <div class="a" id="s5r1" style="left:60px;top:600px;width:960px;border-bottom:3px solid #161412;padding:16px 0"><span class="h" style="font-size:80px">Harçlar</span></div>
    <div class="a" id="s5r2" style="left:60px;top:730px;width:960px;border-bottom:3px solid #161412;padding:16px 0"><span class="h" style="font-size:80px">Damga vergisi</span></div>
    <div class="a h red" id="s5s" style="left:470px;top:900px;font-size:110px;border:8px solid #c8261b;padding:4px 30px;border-radius:8px;transform:rotate(-5deg)">%18,95 ↑</div>
    <div class="a mono" id="s5m" style="left:60px;top:1100px">1 OCAK 2026 · tek seferde</div>
  </section>
  <section id="s6" class="scene clip">
    <div class="a lab" id="s6l" style="left:60px;top:400px">KALEM 2 · ENDEKSLİ FİYATLAR</div>
    <div class="a" id="s6row" style="left:60px;top:470px;width:960px;display:flex;gap:30px">
      <div class="card" id="s6c0" style="flex:1;text-align:center"><div style="font-size:90px">🩺</div><div class="h" style="font-size:52px;margin-top:10px">Sağlık</div></div>
      <div class="card" id="s6c1" style="flex:1;text-align:center"><div style="font-size:90px">🎓</div><div class="h" style="font-size:52px;margin-top:10px">Eğitim</div></div>
      <div class="card" id="s6c2" style="flex:1;text-align:center"><div style="font-size:90px">🏠</div><div class="h" style="font-size:52px;margin-top:10px">Kira</div></div></div>
    <div class="a" id="s6f" style="left:60px;top:820px;width:960px;display:flex;align-items:center;gap:26px">
      <div class="card" style="padding:20px 26px"><div class="mono">GEÇMİŞ</div><div class="h" style="font-size:56px">enflasyon</div></div>
      <div class="h red" style="font-size:90px">→</div>
      <div class="card" style="padding:20px 26px;background:#161412"><div class="mono" style="color:rgba(242,237,226,.7)">YILBAŞI</div><div class="h" style="font-size:56px;color:#f2ede2">yeni fiyat</div></div></div>
    <div class="a mono" id="s6m" style="left:60px;top:1060px">TCMB: dönemsel fiyatlama + endeksleme yaygın</div>
  </section>
  <section id="s7" class="scene clip">
    <div class="a lab" id="s7l" style="left:60px;top:400px">OCAK 2026 · AYLIK ARTIŞ · TCMB</div>
    <div class="a" id="s7b1" style="left:150px;top:470px;width:300px;height:560px"><div id="s7f1" style="position:absolute;left:0;right:0;bottom:0;height:62%;background:repeating-linear-gradient(-45deg,#161412 0 5px,transparent 5px 12px);border:5px solid #161412;transform-origin:50% 100%"></div><div class="h" style="position:absolute;left:0;right:0;bottom:65%;text-align:center;font-size:96px">%5,26</div></div>
    <div class="a" id="s7b2" style="left:610px;top:470px;width:300px;height:560px"><div id="s7f2" style="position:absolute;left:0;right:0;bottom:0;height:87%;background:#c8261b;transform-origin:50% 100%"></div><div class="h red" style="position:absolute;left:0;right:0;bottom:89%;text-align:center;font-size:96px">%7,39</div></div>
    <div class="a h" id="s7c1" style="left:150px;top:1050px;width:300px;text-align:center;font-size:62px">Kira</div>
    <div class="a h" id="s7c2" style="left:610px;top:1050px;width:300px;text-align:center;font-size:62px">Hizmetler</div>
  </section>
  <section id="s8" class="scene clip">
    <div class="a h" id="s8h" style="left:0;right:0;top:1230px;text-align:center;font-size:84px">En az <span class="red">konuşulan</span></div>
  </section>
  <section id="s9" class="scene clip">
    <div class="a lab" id="s9l" style="left:60px;top:400px">KALEM 3 · SENİN ZAMMIN</div>
    <div class="a card" id="s9a" style="left:60px;top:470px;width:960px;display:flex;justify-content:space-between;align-items:center"><div><div class="mono">ASGARİ ÜCRET · OCAK 2026</div><div class="h" style="font-size:66px;margin-top:8px">işgücü maliyeti</div></div><div class="big red" style="font-size:150px">%27</div></div>
    <svg class="a" id="s9arr" style="left:470px;top:700px" width="140" height="150" viewBox="0 0 140 150"><path d="M70 10 V120" stroke="#161412" stroke-width="10"/><path d="M35 95 L70 135 L105 95" fill="none" stroke="#161412" stroke-width="10"/></svg>
    <div class="a card" id="s9b" style="left:60px;top:870px;width:960px;display:flex;justify-content:space-between;align-items:center;background:#161412"><div><div class="mono" style="color:rgba(242,237,226,.7)">LOKANTA-OTEL · OCAK 2026</div><div class="h" style="font-size:66px;margin-top:8px;color:#f2ede2">aylık fiyat</div></div><div class="big" style="font-size:150px;color:#f2ede2">%5,86</div></div>
    <div class="a mono" id="s9m" style="left:60px;top:1100px">TCMB: işgücü maliyetleri ve gıda etkisi</div>
  </section>
  <section id="s10" class="scene clip">
    <div class="a card" id="s10cal" style="left:60px;top:420px;width:520px;padding:0;overflow:hidden;text-align:center">
      <div style="background:#c8261b;padding:16px;font:700 32px 'IBM Plex Mono';color:#f2ede2;letter-spacing:.18em">OCAK</div>
      <div class="big" style="font-size:240px;padding-top:16px">1</div>
      <div style="display:flex;justify-content:center;gap:20px;padding:6px 0 30px"><span class="h" style="font-size:52px">zam</span><span class="h red" style="font-size:52px">+ fiyat</span></div></div>
    <div class="a h" id="s10t" style="left:60px;top:1000px;font-size:70px">Aynı <span class="red">takvim</span></div>
  </section>
  <section id="s11" class="scene clip">
    <div class="a h red" id="s11t" style="left:0;right:0;top:1230px;text-align:center;font-size:120px"><span style="border:8px solid #c8261b;padding:0 30px;border-radius:12px">KAYDET</span></div>
    <div class="a h" id="s11a" style="left:0;right:0;top:1215px;text-align:center;font-size:72px">Zammı değil,</div>
    <div class="a h red" id="s11b" style="left:0;right:0;top:1305px;text-align:center;font-size:84px">takvimi hesapla.</div>
  </section>
'''

SCENE_JS = r'''
const at=(p,after=0)=>{for(const c of CAPS)for(const w of c.w)if(w[1]>=after&&w[0].toLowerCase().startsWith(p.toLowerCase()))return w[1];return null;};
inn('#mast',.05,{y:-20});
// S1 kanca
inn('#s1h',.3); slam('#s1h2',at('fiyatlar')); out(['#s1h','#s1h2'],at('Son')-.2); slam('#s1d',at('%4,8'));
// S2 üç kalem
const s2=st('s2'); inn('#s2l',s2+.4); slam('#s2n',at('3 kalemde')); inn('#s2k',at('3 kalemde')+.15);
inn('#s2r0',at('göreceksin')-.2,{y:30}); inn('#s2r1',at('göreceksin'),{y:30}); slam('#s2r2',at('senin'));
// S3 2025 bar grafiği
const s3=st('s3'); inn('#s3l',s3+.4);
(function(){const V=[5.03,2.27,2.46,3.00,1.53,1.37,2.06,2.04,3.23,2.55,0.87,0.89],M=['O','Ş','M','N','M','H','T','A','E','E','K','A'];
 const svg=$('#s3svg'),H=560,base=640,bw=60,gap=20,x0=40,Y=v=>base-v/5.6*H;let g='';
 V.forEach((v,i)=>{const x=x0+i*(bw+gap);g+=`<rect id="s3b${i}" x="${x}" y="${Y(v)}" width="${bw}" height="${base-Y(v)}" fill="${i?'#161412':'#c8261b'}" opacity="${i?.85:1}"/>`;
  g+=`<text x="${x+bw/2}" y="${base+44}" text-anchor="middle" font-family="IBM Plex Mono" font-size="28" fill="#161412">${M[i]}</text>`;});
 g+=`<line id="s3avg" x1="${x0+bw+gap-10}" x2="${x0+12*(bw+gap)}" y1="${Y(2.02)}" y2="${Y(2.02)}" stroke="#c8261b" stroke-width="6" stroke-dasharray="16 10"/>`;
 g+=`<text id="s3at" x="${x0+12*(bw+gap)-10}" y="${Y(2.02)-60}" text-anchor="end" font-family="DM Serif Display" font-size="56" fill="#c8261b">diğer aylar ort. ~%2</text>`;
 g+=`<text id="s3jt" x="${x0+bw+20}" y="${Y(5.03)+50}" font-family="DM Serif Display" font-size="80" fill="#c8261b">Ocak %5,03</text>`;
 svg.innerHTML=g; V.forEach((v,i)=>tl.fromTo('#s3b'+i,{scaleY:0,transformOrigin:'50% 100%'},{scaleY:1,duration:.35,ease:'power3.out'},(i?at('diğer')-.5:at('%5,03')-.2)+i*.04));
 tl.fromTo('#s3jt',{opacity:0},{opacity:1,duration:.25},at('%5,03')); tl.fromTo(['#s3avg','#s3at'],{opacity:0},{opacity:1,duration:.3},at('%2'));})();
// S4 ara kanca
const s4=st('s4'); tl.fromTo('#s4g',{x:0,opacity:0},{x:-120,opacity:.06,duration:st('s5')-s4,ease:'none'},s4); inn('#s4h',s4+.4); slam('#s4h2',at('Ocak?',20));
// S5 tarife
const s5=st('s5'); inn('#s5l',s5+.4); inn('#s5r0',at('MTV'),{y:20}); inn('#s5r1',at('harçlar'),{y:20}); inn('#s5r2',at('damga'),{y:20});
tl.fromTo('#s5s',{opacity:0,scale:1.6},{opacity:1,scale:1,duration:.25,ease:'power4.in'},at('%18,95')); inn('#s5m',at('arttı',27),{y:10});
// S6 endeksli
const s6=st('s6'); inn('#s6l',s6+.4); inn('#s6c0',at('sağlık'),{y:30}); inn('#s6c1',at('eğitim'),{y:30}); inn('#s6c2',at('kiraların'),{y:30});
inn('#s6f',at('geçmiş'),{y:30}); inn('#s6m',at('güncellenir')+.1,{y:10});
// S7 kira / hizmet
const s7=st('s7'); inn('#s7l',s7+.4); inn('#s7b1',at('kira',36)-.2,{y:0}); inn('#s7c1',at('kira',36)-.2);
tl.fromTo('#s7f1',{scaleY:0},{scaleY:1,duration:.5,ease:'power3.out'},at('kira',36)); inn('#s7b2',at('hizmetler',37)-.2,{y:0}); inn('#s7c2',at('hizmetler',37)-.2);
tl.fromTo('#s7f2',{scaleY:0},{scaleY:1,duration:.5,ease:'power4.out'},at('hizmetler',37));
// S8 ara kanca 2
inn('#s8h',st('s8')+.4,{y:20});
// S9 asgari ücret → lokanta
const s9=st('s9'); inn('#s9l',s9+.4); inn('#s9a',at('Asgari'),{y:30}); inn('#s9arr',at('Merkez'),{y:-20}); inn('#s9b',at('lokanta'),{y:30});
inn('#s9m',at('işgücü'),{y:10});
// S10 kapanış
const s10=st('s10'); inn('#s10cal',s10+.4,{y:60}); slam('#s10t',at('takvimle'));
// S11 CTA + döngü
slam('#s11t',at('Kaydet')); out('#s11t',at('zammı',56)-.25); inn('#s11a',at('zammı',56)); slam('#s11b',at('takvimi'));
'''
