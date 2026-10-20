import os
# Gazete stili (verilen; önceki video Kinetik). Ayrık yöntem: avatar s1 (kanca), s8 (ara kanca), s11-s13 (kapanış + CTA + döngü).
CSS_FILE = 'gazete.css.html'
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [
    (N('yüzde', 'otuz', 'bir', 'virgül', 'kırk', 'dokuzdu'), "%31,49'du"), (N('yüzde', 'yirmi', 'dokuz', 'virgül', 'yetmiş', 'üç'), '%29,73'),
    (N('on', 'iki', 'aylık'), '12 aylık'), (N('yüzde', 'otuz', 'sekiz', 'virgül', 'otuz', 'altı'), '%38,36'),
    (N('yüzde', 'otuz', 'üç', 'virgül', 'yirmi', 'dokuz'), '%33,29'), (N('otuz', 'bin', 'liralık'), '30.000 liralık'),
    (N('beş', 'yüz', 'otuz', 'lira'), '530 lira'), (N('iki', 'oran'), '2 oran'),
]
EM = {'formül', 'tavan', 'tavanı', 'ortalama', 'geriden', 'üst', 'sınır', 'pazarlık', 'kaydet', 'geçemez', 'büyüktü'}
RED = {'formül', 'geçemez', 'zorunlu'}
FRONT = [250, 375, 580, 815, 6]
MID = [290, 400, 500, 703, 6]
AV = {'s1': FRONT, 's2': None, 's3': None, 's4': None, 's5': None, 's6': None, 's7': None, 's8': MID, 's9': None, 's10': None,
      's11': FRONT, 's12': FRONT, 's13': FRONT}


def scenes(A):
    b = lambda t: round(t - .1, 3)
    t2 = A("Ekim'de"); t3 = A('Sonunda'); t4 = A('Tavan,'); t5 = A('Peki'); t6 = A('Çünkü'); t7 = A('Geçen'); t8 = A('Ama')
    t9 = A('Kanun'); t10 = A('30.000 liralık'); t11 = A('Ev', 46); t12 = A('Kira', 50); t13 = A('Çünkü', 50)
    return [('s1', 0, b(t2)), ('s2', b(t2), b(t3)), ('s3', b(t3), b(t4)), ('s4', b(t4), b(t5)), ('s5', b(t5), b(t6)),
            ('s6', b(t6), b(t7)), ('s7', b(t7), b(t8)), ('s8', b(t8), b(t9)), ('s9', b(t9), b(t10)), ('s10', b(t10), b(t11)),
            ('s11', b(t11), b(t12)), ('s12', b(t12), b(t13)), ('s13', b(t13), DUR)]


def SFX(A):
    return [[A('formül.'), 'stamp', -9, 1, 'hook'], [A("%31,49'du"), 'impact', -8, 1, '3149'], [A('%29,73'), 'stamp', -10, 0, '2973'],
            [A('Sonunda') + .3, 'whoosh_hollow', -12, 0, 'kilit'], [A('Tavan,'), 'paper_drop', -9, 0, 'tavan'], [A('12 aylık'), 'stamp', -9, 1, '12'],
            [A('geriden'), 'marker', -11, 0, 'lag'], [A('üstünde'), 'pop', -10, 0, 'ust'], [A('%38,36'), 'stamp', -9, 0, '3836'],
            [A('%33,29'), 'stamp', -10, 0, '3329'], [A('geçemez'), 'impact', -8, 1, 'gecemez'], [A('530 lira'), 'impact', -8, 1, '530'],
            [A('pazarlık'), 'ui_click', -11, 0, 'pazarlik'], [A('kaydet.') + .05, 'success', -10, 1, 'kaydet'], [A('formül.', 55), 'impact', -8, 1, 'loop']]


def RISERS(A): return [[A('Peki') - .5, 'sharp', -9], [A('Ama') - .4, 'metallic', -10]]


SCENE_HTML = r'''
  <div id="mast" style="position:absolute;left:60px;right:60px;top:236px">
    <div style="height:5px;background:#161412"></div>
    <div style="display:flex;justify-content:space-between;align-items:baseline;padding:10px 0 6px">
      <span style="font:400 66px/1 'DM Serif Display';color:#161412">Paranın Dili</span>
      <span class="mono" style="font-size:22px">KİRA · TBK 344</span></div>
    <div style="height:2px;background:#161412"></div>
  </div>
  <section id="s1" class="scene clip">
    <div class="a h" id="s1h" style="left:60px;top:1215px;font-size:80px">Sebep ev sahibin değil:</div>
    <div class="a h red" id="s1h2" style="left:60px;top:1305px;font-size:96px">formül.</div>
  </section>
  <section id="s2" class="scene clip">
    <div class="a lab" id="s2l" style="left:60px;top:400px">EKİM 2026 · İKİ RAKAM</div>
    <div class="a card" id="s2a" style="left:60px;top:470px;width:960px">
      <div class="mono">YASAL KİRA TAVANI (EKİM)</div><div class="big red" id="s2v1" style="font-size:190px;margin-top:10px">%31,49</div></div>
    <div class="a card" id="s2b" style="left:60px;top:790px;width:960px">
      <div class="mono">YILLIK TÜFE (EYLÜL, 5 EKİM'DE AÇIKLANDI)</div><div class="big" id="s2v2" style="font-size:190px;margin-top:10px">%29,73</div></div>
    <div class="a h red" id="s2d" style="left:600px;top:1120px;font-size:62px;border:6px solid #c8261b;padding:6px 22px;border-radius:8px;transform:rotate(-4deg)">+1,76 puan</div>
  </section>
  <section id="s3" class="scene clip">
    <div class="a lab" id="s3l" style="left:60px;top:400px">SONUNDA</div>
    <div class="a" id="s3r0" style="left:60px;top:480px;width:960px;display:flex;gap:22px;align-items:center"><div class="tick" id="s3k0"></div><div class="h" style="font-size:66px">Fark nereden çıkıyor?</div></div>
    <div class="a" id="s3r1" style="left:60px;top:650px;width:960px;display:flex;gap:22px;align-items:center"><div class="tick" id="s3k1"></div><div class="h" style="font-size:66px">Zam konuşurken <span class="red">neye bak?</span></div></div>
  </section>
  <section id="s4" class="scene clip">
    <div class="a lab" id="s4l" style="left:60px;top:400px">KANUNDAKİ ÖLÇÜ</div>
    <div class="a h" id="s4a" style="left:60px;top:470px;font-size:84px;text-decoration:line-through;text-decoration-color:#c8261b;text-decoration-thickness:8px">Yıllık enflasyon</div>
    <div class="a h red" id="s4b" style="left:60px;top:620px;font-size:110px">12 aylık</div>
    <div class="a h red" id="s4c" style="left:60px;top:740px;font-size:110px">ortalama</div>
    <div class="a mono" id="s4m" style="left:60px;top:890px">TÜFE · 12 aylık ortalamalara göre değişim</div>
  </section>
  <section id="s5" class="scene clip">
    <div class="a h" id="s5h" style="left:0;right:0;top:700px;text-align:center;font-size:110px">Neden <span class="red">fark?</span></div>
  </section>
  <section id="s6" class="scene clip">
    <div class="a lab" id="s6l" style="left:60px;top:400px">ORTALAMA GERİDEN GELİR</div>
    <svg class="a" id="s6svg" style="left:60px;top:470px" width="960" height="620" viewBox="0 0 960 620">
      <line x1="0" x2="960" y1="560" y2="560" stroke="#161412" stroke-width="3"/>
      <path id="s6p1" d="M20 60 C 200 140, 380 260, 560 340 S 820 430, 940 450" fill="none" stroke="#161412" stroke-width="9"/>
      <path id="s6p2" d="M20 20 C 260 50, 450 140, 620 230 S 840 320, 940 350" fill="none" stroke="#c8261b" stroke-width="9" stroke-dasharray="1 0"/>
      <text x="700" y="490" font-family="IBM Plex Mono" font-size="26" fill="#161412">yıllık enflasyon</text>
      <text x="610" y="300" font-family="IBM Plex Mono" font-weight="700" font-size="26" fill="#c8261b">12 aylık ort. = tavan</text>
      <text x="20" y="600" font-family="IBM Plex Mono" font-size="22" fill="rgba(22,20,18,.6)">temsili şema</text></svg>
    <div class="a h" id="s6h" style="left:60px;top:1110px;font-size:62px">eski yüksek aylar <span class="red">ortalamada kalır</span></div>
  </section>
  <section id="s7" class="scene clip">
    <div class="a lab" id="s7l" style="left:60px;top:400px">EKİM TAVANI vs YILLIK TÜFE (EYLÜL)</div>
    <div class="a card" id="s7r0" style="left:60px;top:470px;width:960px">
      <div style="display:flex;justify-content:space-between;align-items:baseline"><span class="h" style="font-size:72px">2025</span><span class="mono">fark</span></div>
      <div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:16px"><span class="h red" style="font-size:66px">%38,36</span><span class="h" style="font-size:66px">%33,29</span><span class="h red" style="font-size:66px">+5,07</span></div></div>
    <div class="a card" id="s7r1" style="left:60px;top:760px;width:960px">
      <div style="display:flex;justify-content:space-between;align-items:baseline"><span class="h" style="font-size:72px">2026</span><span class="mono">fark</span></div>
      <div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:16px"><span class="h red" style="font-size:66px">%31,49</span><span class="h" style="font-size:66px">%29,73</span><span class="h red" style="font-size:66px">+1,76</span></div></div>
    <div class="a mono" id="s7m" style="left:60px;top:1060px">tavan · yıllık TÜFE · puan</div>
  </section>
  <section id="s8" class="scene clip">
    <div class="a h" id="s8h" style="left:0;right:0;top:1150px;text-align:center;font-size:84px">Tavan ≠ <span class="red">zorunlu zam</span></div>
  </section>
  <section id="s9" class="scene clip">
    <div class="a lab" id="s9l" style="left:60px;top:400px">TÜRK BORÇLAR KANUNU · MADDE 344</div>
    <div class="a h" id="s9q" style="left:60px;top:470px;font-size:68px;white-space:normal;width:960px;line-height:1.08">"…ortalamalara göre değişim oranını <span class="red">geçemez</span>"</div>
    <div class="a h red" id="s9s" style="left:300px;top:800px;font-size:110px;border:9px solid #c8261b;padding:6px 34px;border-radius:10px;transform:rotate(-5deg)">ÜST SINIR</div>
  </section>
  <section id="s10" class="scene clip">
    <div class="a lab" id="s10l" style="left:60px;top:400px">ÖRNEK · 30.000 TL KİRA</div>
    <div class="a card" id="s10a" style="left:60px;top:470px;width:960px;display:flex;justify-content:space-between;align-items:baseline"><span class="mono">TAVANLA (%31,49)</span><span class="h" style="font-size:76px">39.447 TL</span></div>
    <div class="a card" id="s10b" style="left:60px;top:650px;width:960px;display:flex;justify-content:space-between;align-items:baseline"><span class="mono">YILLIK TÜFE İLE (%29,73)</span><span class="h" style="font-size:76px">38.919 TL</span></div>
    <div class="a mono" id="s10m" style="left:60px;top:860px">AYLIK FARK</div>
    <div class="a big red" id="s10v" style="left:52px;top:900px;font-size:200px">528 TL</div>
  </section>
  <section id="s11" class="scene clip">
    <div class="a h" id="s11a" style="left:0;right:0;top:1215px;text-align:center;font-size:76px">Ev sahibi ⇄ kiracı</div>
    <div class="a h red" id="s11b" style="left:0;right:0;top:1305px;text-align:center;font-size:84px">pazarlık bu farkta</div>
  </section>
  <section id="s12" class="scene clip">
    <div class="a h red" id="s12t" style="left:0;right:0;top:1230px;text-align:center;font-size:120px"><span style="border:8px solid #c8261b;padding:0 30px;border-radius:12px">KAYDET</span></div>
  </section>
  <section id="s13" class="scene clip">
    <div class="a h" id="s13a" style="left:0;right:0;top:1215px;text-align:center;font-size:76px">Sebep ev sahibin değil:</div>
    <div class="a h red" id="s13b" style="left:0;right:0;top:1305px;text-align:center;font-size:96px">formül.</div>
  </section>
'''

SCENE_JS = r'''
const at=(p,after=0)=>{for(const c of CAPS)for(const w of c.w)if(w[1]>=after&&w[0].toLowerCase().startsWith(p.toLowerCase()))return w[1];return null;};
inn('#mast',.05,{y:-20});
// S1 kanca
inn('#s1h',at('sebebi')); slam('#s1h2',at('formül'));
// S2 iki rakam
const s2=st('s2'); inn('#s2l',s2+.4); inn('#s2a',s2+.5,{y:40}); count('#s2v1',0,31.49,s2+.6,at('%31')-s2-.5,v=>v.toFixed(2).replace('.',','),'%');
inn('#s2b',at('yıllık')-.1,{y:40}); count('#s2v2',0,29.73,at('yıllık'),at('%29')-at('yıllık')+.3,v=>v.toFixed(2).replace('.',','),'%');
tl.fromTo('#s2d',{opacity:0,scale:1.6},{opacity:1,scale:1,duration:.25,ease:'power4.in'},at('%29')+.6);
// S3 kilit
const s3=st('s3'); inn('#s3l',s3+.4); inn('#s3r0',at('farkın')-.1,{y:24}); tl.to('#s3k0',{backgroundColor:'#161412',duration:.15},at('farkın')+.3);
inn('#s3r1',at('zam')-.1,{y:24}); tl.to('#s3k1',{backgroundColor:'#161412',duration:.15},at('zam')+.3);
// S4 formül
const s4=st('s4'); inn('#s4l',s4+.4); inn('#s4a',s4+.45); slam('#s4b',at('12 aylık')); slam('#s4c',at('ortalama')); inn('#s4m',at('ortalama')+.4,{y:10});
// S5 ara kanca
inn('#s5h',st('s5')+.4,{s:1.1});
// S6 gecikme şeması
const s6=st('s6'); inn('#s6l',s6+.4); inn('#s6svg',s6+.45,{y:0});
tl.fromTo('#s6p1',{strokeDasharray:1200,strokeDashoffset:1200},{strokeDashoffset:0,duration:1.6,ease:'none'},at('Enflasyon',24)-.1);
tl.fromTo('#s6p2',{strokeDasharray:1200,strokeDashoffset:1200},{strokeDashoffset:0,duration:1.6,ease:'none'},at('Enflasyon',24)+.6);
inn('#s6h',at('eski'),{y:20});
// S7 iki yıl
const s7=st('s7'); inn('#s7l',s7+.4); inn('#s7r0',s7+.5,{y:40}); inn('#s7r1',at('%33')+.4,{y:40}); inn('#s7m',at('%33')+.8,{y:10});
// S8 ara kanca
inn('#s8h',st('s8')+.4,{s:1.1});
// S9 kanun
const s9=st('s9'); inn('#s9l',s9+.4); inn('#s9q',s9+.45); tl.fromTo('#s9s',{opacity:0,scale:1.8},{opacity:1,scale:1,duration:.25,ease:'power4.in'},at('üst',41));
// S10 örnek
const s10=st('s10'); inn('#s10l',s10+.4); inn('#s10a',s10+.5,{y:30}); inn('#s10b',s10+.9,{y:30}); inn('#s10m',at('ayda')-.2); slam('#s10v',at('530'));
// S11 kapanış
inn('#s11a',st('s11')+.4); slam('#s11b',at('pazarlık'));
// S12 CTA
slam('#s12t',at('kaydet'));
// S13 döngü
inn('#s13a',st('s13')+.4); slam('#s13b',at('formül',55));
'''
