import os
# Kinetik stili (son video Gazete idi). Ayrık yöntem: avatar sadece s1 (kanca), s3 (kilit), s7 (ara kanca), s12-s13 (CTA + döngü).
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
# TTS metninde "reyel" yazıldı (telaffuz için); ekranda "reel"
REPL = [
    (N('reyel', 'faiz', 'bir', 'yılda', 'bir', 'puandan'), 'Reel faiz 1 yılda 1 puandan'),
    (N('reyel', 'faiz'), 'reel faiz'), (N('reyel', 'faizi'), 'reel faizi'),
    (N('ağustostan',), "Ağustos'tan"), (N('yüzde', 'on'), '%10'),
    (N('iki', 'bin', 'on', 'üçte'), "2013'te"), (N('yüzde', 'yirmi', 'sekiz'), '%28'),
    (N('on', 'yıllık'), '10 yıllık'), (N('beş', "ekim'de"), "5 Ekim'de"),
    (N('yüzde', 'iki', 'virgül', 'doksan', 'beşe'), "%2,95'e"), (N('iki', 'bin', 'sekizden'), "2008'den"),
    (N('yüzde', 'üç'), '%3'), (N('sekiz', 'günde'), '8 günde'),
]
EM = {'türkiye', 'rakam', 'reel', 'faiz', 'ödemez', 'bedeli', 'alarm', 'yön', 'kaydet', 'sinyallerden'}
RED = {'%10', '%28', 'alarm', 'ödemez', "%2,95'e"}
BIG = [170, 330, 740, 1040, 28]      # 740:1040 portre: saç + çene her zaman görünür
FRONT = [250, 300, 580, 815, 24]
AV = {'s1': FRONT, 's2': None, 's3': BIG, 's4': None, 's5': None, 's6': None, 's7': [170, 360, 740, 1040, 28],
      's8': None, 's9': None, 's10': None, 's11': None, 's12': FRONT, 's13': FRONT}


def scenes(A):
    b = lambda t: round(t - .1, 3)
    t2 = A("2013'te"); t3 = A('Sonunda'); t4 = A('Rakamın'); t5 = A("Amerika'nın"); t6 = A('Peki'); t7 = A('Ama', 33)
    t8 = min(b(A('Eylülde')), 35.45)  # ara kanca avatar parçası 35.41'de bitiyor
    t9 = A('Reel faiz 1 yılda 1 puandan'); t10 = A('Tekrarlanacak'); t11 = A('Ons', 47); t12 = A('Altına', 52); t13 = A('Çünkü', 55)
    return [('s1', 0, b(t2)), ('s2', b(t2), b(t3)), ('s3', b(t3), b(t4)), ('s4', b(t4), b(t5)), ('s5', b(t5), b(t6)),
            ('s6', b(t6), b(t7)), ('s7', b(t7), t8), ('s8', t8, b(t9)), ('s9', b(t9), b(t10)), ('s10', b(t10), b(t11)),
            ('s11', b(t11), b(t12)), ('s12', b(t12), b(t13)), ('s13', b(t13), DUR)]


def SFX(A):
    return [[A('düştü'), 'impact', -8, 1, 'hook'], [A('rakam.'), 'stamp', -10, 0, 'rakam'], [A('%28'), 'impact', -8, 1, '-28'],
            [A('Rakamın'), 'whoosh_hollow', -12, 0, 'def'], [A('enflasyonu'), 'marker', -11, 0, 'minus'],
            [A("%2,95'e"), 'stamp', -8, 1, '2.95'], [A("2008'den"), 'pop', -10, 0, 'badge'], [A('ödemez.'), 'paper_drop', -9, 0, 'gold0'],
            [A('Tahvil'), 'ui_click', -11, 0, 'bond'], [A('Avrupa'), 'stamp', -10, 0, 'ecb'], [A('Amerika', 37), 'stamp', -10, 0, 'fed'],
            [A('Japonya'), 'stamp', -10, 0, 'boj'], [A('Reel faiz 1 yılda 1 puandan'), 'gears', -12, 0, 'count'],
            [A('yön', 46), 'impact', -9, 1, 'yon'], [A('kaydet.') + .05, 'success', -10, 1, 'kaydet'], [A('Türkiye', 57), 'impact', -8, 1, 'loop']]


def RISERS(A): return [[A('Ama', 33) - .5, 'sharp', -9], [A('Tekrarlanacak') - .4, 'metallic', -10]]


SCENE_HTML = r'''
  <section id="s1" class="scene clip">
    <div class="a h" id="s1a" style="left:0;right:0;top:1150px;text-align:center;font-size:92px">ALTIN <span class="red">%10</span> DÜŞTÜ</div>
    <div class="a h gold" id="s1b" style="left:0;right:0;top:1255px;text-align:center;font-size:64px">SEBEP: TEK BİR RAKAM</div>
  </section>
  <section id="s2" class="scene clip">
    <div class="a ghost" id="s2g" data-layout-allow-overflow data-layout-allow-occlusion data-layout-allow-overlap style="left:-20px;top:240px">2013</div>
    <div class="a lab" id="s2l" style="left:60px;top:300px">2013 · DAHA ÖNCE OLDU</div>
    <div class="a card" id="s2c1" style="left:60px;top:400px;width:960px;display:flex;align-items:center;gap:30px">
      <div class="big gold" style="font-size:130px">↑</div><div><div class="h" style="font-size:64px">ABD REEL FAİZ</div><div class="mono" style="margin-top:12px">sertçe yükseldi</div></div></div>
    <div class="a card" id="s2c2" style="left:60px;top:720px;width:960px;display:flex;align-items:center;gap:30px;border-color:#ff4a3d">
      <div class="big red" style="font-size:130px">↓</div><div><div class="h" style="font-size:64px">ONS ALTIN</div><div class="big red" id="s2v" style="font-size:120px;margin-top:8px">%-28</div></div></div>
    <svg class="a" id="s2svg" style="left:640px;top:760px" width="340" height="260" viewBox="0 0 340 260">
      <rect x="20" y="20" width="120" height="220" rx="10" fill="rgba(232,185,49,.35)"/>
      <rect id="s2bar" x="200" y="20" width="120" height="220" rx="10" fill="#e8b931"/>
      <text x="80" y="255" text-anchor="middle" font-family="IBM Plex Mono" font-size="22" fill="rgba(243,239,230,.7)">OCAK</text>
      <text x="260" y="255" text-anchor="middle" font-family="IBM Plex Mono" font-size="22" fill="rgba(243,239,230,.7)">ARALIK</text></svg>
  </section>
  <section id="s3" class="scene clip">
    <div class="a lab" id="s3l" style="left:0;right:0;top:250px;text-align:center;font-size:32px">SONUNDA: İZLEYECEĞİN TEK RAKAM ↓</div>
  </section>
  <section id="s4" class="scene clip">
    <div class="a ghost" id="s4g" data-layout-allow-overflow data-layout-allow-occlusion data-layout-allow-overlap style="left:640px;top:820px">%</div>
    <div class="a lab" id="s4l" style="left:60px;top:300px">RAKAMIN ADI</div>
    <div class="a h gold" id="s4h" style="left:60px;top:360px;font-size:140px">REEL FAİZ</div>
    <div class="a h" id="s4r1" style="left:60px;top:640px;font-size:96px">FAİZ</div>
    <div class="a h red" id="s4r2" style="left:60px;top:760px;font-size:96px">− ENFLASYON</div>
    <div class="a rule" id="s4rule" style="left:60px;top:885px;width:800px"></div>
    <div class="a h gold" id="s4r3" style="left:60px;top:920px;font-size:96px">= KALAN</div>
    <div class="a mono" id="s4m" style="left:60px;top:1050px">paranın enflasyon üstündeki gerçek getirisi</div>
  </section>
  <section id="s5" class="scene clip">
    <div class="a lab" id="s5l" style="left:60px;top:290px">ABD 10 YILLIK REEL FAİZ (TIPS)</div>
    <div class="a big gold" id="s5v" style="left:52px;top:340px;font-size:210px">%1,80</div>
    <svg class="a" id="s5svg" style="left:60px;top:580px" width="960" height="560" viewBox="0 0 960 560"></svg>
    <div class="a h" id="s5b" style="left:60px;top:1180px;font-size:50px;background:#e8b931;color:#0d0c0a;padding:12px 24px;border-radius:40px">2008'DEN BERİ EN YÜKSEK KAPANIŞ</div>
  </section>
  <section id="s6" class="scene clip">
    <div class="a h" id="s6q" style="left:60px;top:290px;font-size:76px">ALTINI NEDEN <span class="red">VURUYOR?</span></div>
    <div class="a card" id="s6a" style="left:60px;top:470px;width:450px;height:560px;text-align:center;border-color:#ff4a3d">
      <div class="lab" style="color:#f3efe6">ALTIN</div><div class="big red" style="font-size:190px;margin-top:70px">%0</div><div class="mono" style="margin-top:40px">faiz ödemez</div></div>
    <div class="a card" id="s6b" style="left:570px;top:470px;width:450px;height:560px;text-align:center;border-color:#e8b931">
      <div class="lab" style="color:#f3efe6">ABD TAHVİLİ</div><div class="big gold" style="font-size:150px;margin-top:80px">≈%3</div><div class="mono" style="margin-top:50px">enflasyonun üstüne</div></div>
    <div class="a h" id="s6c" style="left:60px;top:1110px;font-size:58px">ALTIN TUTMANIN <span class="gold">BEDELİ ↑</span></div>
  </section>
  <section id="s7" class="scene clip">
    <div class="a h red" id="s7h" style="left:0;right:0;top:245px;text-align:center;font-size:84px">⚠ ASIL ALARM</div>
  </section>
  <section id="s8" class="scene clip">
    <div class="a lab" id="s8l" style="left:60px;top:300px">EYLÜL 2026 · 8 GÜN · 3 ARTIŞ</div>
    <div class="a card" id="s8r0" style="left:60px;top:380px;width:960px;display:flex;justify-content:space-between;align-items:center"><span class="mono">10 EYL</span><span class="h" style="font-size:62px">AVRUPA</span><span class="h gold" style="font-size:62px">%2,50 ↑</span></div>
    <div class="a card" id="s8r1" style="left:60px;top:580px;width:960px;display:flex;justify-content:space-between;align-items:center"><span class="mono">16 EYL</span><span class="h" style="font-size:62px">ABD</span><span class="h gold" style="font-size:62px">%3,75-4 ↑</span></div>
    <div class="a card" id="s8r2" style="left:60px;top:780px;width:960px;display:flex;justify-content:space-between;align-items:center"><span class="mono">18 EYL</span><span class="h" style="font-size:62px">JAPONYA</span><span class="h gold" style="font-size:62px">%1,25 ↑</span></div>
    <div class="a mono" id="s8m" style="left:60px;top:1000px">merkez bankası politika faizleri</div>
  </section>
  <section id="s9" class="scene clip">
    <div class="a lab" id="s9l" style="left:60px;top:300px">REEL FAİZ · SON 1 YIL</div>
    <div class="a big gold" id="s9v" style="left:52px;top:350px;font-size:230px">+0</div>
    <div class="a h" id="s9u" style="left:60px;top:590px;font-size:80px">PUANDAN FAZLA</div>
    <div class="a card" id="s9c" style="left:60px;top:780px;width:960px;border-color:#ff4a3d">
      <div class="lab" style="color:#f3efe6">2013'TE DE AYNISI</div>
      <div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:24px"><span class="h" style="font-size:58px">REEL FAİZ +1 puan+</span><span class="h red" style="font-size:58px">ALTIN %-28</span></div></div>
  </section>
  <section id="s10" class="scene clip">
    <div class="a h" id="s10a" style="left:60px;top:470px;font-size:104px">TEKRAR</div>
    <div class="a h" id="s10b" style="left:60px;top:585px;font-size:104px;color:rgba(243,239,230,.55)">≠ GARANTİ</div>
    <div class="a rule" id="s10r" style="left:60px;top:740px;width:520px"></div>
    <div class="a h gold" id="s10c" style="left:60px;top:790px;font-size:150px">YÖN AYNI ↗</div>
  </section>
  <section id="s11" class="scene clip">
    <div class="a lab" id="s11l" style="left:60px;top:300px">ONS ALTININ EN GÜÇLÜ SİNYALLERİNDEN</div>
    <svg class="a" id="s11svg" style="left:60px;top:420px" width="960" height="640" viewBox="0 0 960 640">
      <g id="s11beam" style="transform-origin:480px 420px"><rect x="60" y="406" width="840" height="28" rx="14" fill="#f3efe6"/>
        <rect x="70" y="250" width="300" height="150" rx="22" fill="#e8b931"/><text x="220" y="345" text-anchor="middle" font-family="Inter Tight" font-weight="900" font-size="58" fill="#0d0c0a">REEL FAİZ</text>
        <rect x="590" y="250" width="300" height="150" rx="22" fill="none" stroke="#e8b931" stroke-width="6"/><text x="740" y="345" text-anchor="middle" font-family="Inter Tight" font-weight="900" font-size="64" fill="#e8b931">ALTIN</text></g>
      <path d="M440 600 L480 440 L520 600 Z" fill="rgba(243,239,230,.45)"/></svg>
    <div class="a h gold" id="s11u" style="left:120px;top:1110px;font-size:64px">↑ YÜKSELİRSE</div>
    <div class="a h red" id="s11d" style="left:640px;top:1110px;font-size:64px">↓ BASKI</div>
  </section>
  <section id="s12" class="scene clip">
    <svg class="a" id="s12i" style="left:250px;top:1166px" width="96" height="120" viewBox="0 0 96 120"><path d="M8 6h80v108L48 86 8 114z" fill="#e8b931"/></svg>
    <div class="a h gold" id="s12t" style="left:370px;top:1170px;font-size:118px">KAYDET</div>
  </section>
  <section id="s13" class="scene clip">
    <div class="a h" id="s13a" style="left:0;right:0;top:1150px;text-align:center;font-size:72px">SEBEP HER ZAMAN</div>
    <div class="a h gold" id="s13b" style="left:0;right:0;top:1240px;text-align:center;font-size:84px">TÜRKİYE DEĞİL</div>
  </section>
'''

SCENE_JS = r'''
const W=(p)=>CAPS.flatMap(c=>c.w).find(w=>w[0].toLowerCase().startsWith(p.toLowerCase()));
const at=(p,after=0)=>{for(const c of CAPS)for(const w of c.w)if(w[1]>=after&&w[0].toLowerCase().startsWith(p.toLowerCase()))return w[1];return null;};
// S1 hook
inn('#s1a',.25,{s:1.1}); inn('#s1b',at('Sebebi')+.1);
// S2 2013
const s2=st('s2'); tl.fromTo('#s2g',{x:0},{x:-200,duration:st('s3')-s2,ease:'none'},s2);
inn('#s2l',s2+.4); inn('#s2c1',s2+.5,{y:60}); inn('#s2c2',at('altın',7.5)-.1,{y:60}); slam('#s2v',at('%28')); inn('#s2svg',at('altın',7.5)+.1,{y:0});
tl.fromTo('#s2bar',{attr:{y:20,height:220}},{attr:{y:20+220*.28,height:220*.72},duration:.6,ease:'power3.out'},at('%28'));
// S3 kilit
inn('#s3l',st('s3')+.4,{y:-20});
// S4 tanım
const s4=st('s4'); inn('#s4l',s4+.4); slam('#s4h',s4+.5); inn('#s4r1',at('faizden')); inn('#s4r2',at('enflasyonu'));
tl.fromTo('#s4rule',{scaleX:0},{scaleX:1,duration:.35,ease:'power3.out'},at('çıkarınca')); slam('#s4r3',at('kalan')); inn('#s4m',at('kalan')+.4,{y:16});
// S5 TIPS çubukları (doğrulanmış 3 nokta)
const s5=st('s5'); inn('#s5l',s5+.4); inn('#s5v',s5+.45); inn('#s5svg',s5+.55,{y:30});
(function(){const svg=$('#s5svg');const P=[['1 YIL ÖNCE','%1,8',1.8],['25 AĞU','%2,32',2.32],['5 EKİM','%2,95',2.95]];const H=v=>v/3.2*430;
 let g='<line x1="0" x2="960" y1="470" y2="470" stroke="rgba(243,239,230,.25)" stroke-width="3"/>';
 P.forEach(([l,t,v],i)=>{const x=40+i*320,h=H(v);g+=`<rect id="s5r${i}" x="${x}" y="${470-h}" width="240" height="${h}" rx="14" fill="${i==2?'#e8b931':'rgba(243,239,230,.28)'}"/>`+
 `<text id="s5t${i}" x="${x+120}" y="${470-h-22}" text-anchor="middle" font-family="Inter Tight" font-weight="900" font-size="54" fill="${i==2?'#e8b931':'#f3efe6'}">${t}</text>`+
 `<text x="${x+120}" y="520" text-anchor="middle" font-family="IBM Plex Mono" font-size="26" fill="rgba(243,239,230,.7)">${l}</text>`;});
 svg.innerHTML=g; const T=[s5+.7,s5+1.6,at("%2,95")-.2];
 P.forEach((p,i)=>{tl.fromTo('#s5r'+i,{scaleY:0,transformOrigin:'50% 100%'},{scaleY:1,duration:.5,ease:'power3.out'},T[i]);tl.fromTo('#s5t'+i,{opacity:0},{opacity:1,duration:.25},T[i]+.35);});})();
count('#s5v',1.8,2.95,at("%2,95")-.6,1.0,v=>v.toFixed(2).replace('.',','),'%');
slam('#s5b',at("2008'den"));
// S6 neden
const s6=st('s6'); inn('#s6q',s6+.4); inn('#s6a',at('altın',27.5),{y:60}); inn('#s6b',at('Tahvil'),{y:60}); slam('#s6c',at('bedeli'));
// S7 ara kanca
const s7=st('s7'); tl.fromTo('#s7h',{opacity:0,scale:1.5,transformOrigin:'50% 50%'},{opacity:1,scale:1,duration:.3,ease:'power4.in'},s7+.4);
// S8 üç merkez bankası
const s8=st('s8'); inn('#s8l',s8+.4); slam('#s8r0',at('Avrupa')); slam('#s8r1',at('Amerika',37)); slam('#s8r2',at('Japonya')); inn('#s8m',at('artırdı')+.2,{y:16});
// S9 +1 puan + 2013
const s9=st('s9'); inn('#s9l',s9+.4); inn('#s9v',s9+.45); count('#s9v',0,1,s9+.6,1.0,v=>'+'+Math.round(v)); inn('#s9u',s9+1.2); inn('#s9c',at("2013'te",43),{y:60});
// S10
const s10=st('s10'); slam('#s10a',s10+.4); inn('#s10b',s10+.7); tl.fromTo('#s10r',{scaleX:0},{scaleX:1,duration:.3},at('ama',46)); slam('#s10c',at('yön',46));
// S11 tahterevalli
const s11=st('s11'); inn('#s11l',s11+.4); inn('#s11svg',s11+.45,{y:30});
tl.fromTo('#s11beam',{rotation:0},{rotation:-12,duration:.9,ease:'back.out(1.6)',svgOrigin:'480 420'},at('Amerikan')); inn('#s11u',at('Amerikan')+.3); inn('#s11d',at('Amerikan')+.6);
// S12 CTA
const s12=st('s12'); tl.fromTo('#s12i',{opacity:0,y:-80},{opacity:1,y:0,duration:.4,ease:'bounce.out'},at('kaydet')-.1); slam('#s12t',at('kaydet'));
// S13 döngü
const s13=st('s13'); inn('#s13a',s13+.4); slam('#s13b',at('Türkiye',57));
'''
