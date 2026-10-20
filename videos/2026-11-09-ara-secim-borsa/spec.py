import os
# Kinetik stili (verilen). Ayrık yöntem: avatar s1 (kanca), s5 (ara kanca), s12-s14 (kapanış + CTA + döngü).
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
# TTS metninde "es end pi" yazıldı (telaffuz), ekranda S&P 500
REPL = [
    (N('yirmi', 'birde', 'yirmi', 'bir'), "21'de 21"), (N('yirmide', 'yirmi'), "20'de 20"),
    (N('bin', 'dokuz', 'yüz', 'kırk', 'altıdan'), "1946'dan"), (N('yirmi', 'ara'), '20 ara'), (N('yirmi', 'seçim'), '20 seçim'),
    (N('es', 'end', 'pi', 'beş', 'yüz'), 'S&P 500'), (N('yüzde', 'on', 'beş'), '%15'), (N('iki', 'katı'), '2 katı'),
    (N('yüzde', 'dört', 'virgül', 'yedi'), '%4,7'), (N('yüzde', 'dokuz', 'buçuk'), '%9,5'), (N('bir', 'yıl'), '1 yıl'),
]
EM = {'parti', 'belirsizlik', 'tuzak', 'tuzağını', 'garanti', 'yön', 'kaydet', 'yukarıdaydı', 'kongre\'nin', 'dalgalanır'}
RED = {'tuzak', 'tuzağını', 'garanti', 'değil', 'düşüşler'}
BIG = [170, 300, 740, 1040, 28]       # 740:1040 portre: saç + çene görünür
MID = [250, 330, 580, 815, 24]
AV = {'s1': MID, 's2': None, 's3': None, 's4': None, 's5': MID, 's6': None, 's7': None, 's8': None, 's9': None,
      's10': None, 's11': None, 's12': MID, 's13': MID, 's14': MID}
EXTRA_CSS = '<style>.dot{width:150px;height:150px;border-radius:22px;border:4px solid rgba(243,239,230,.18);display:flex;align-items:center;justify-content:center;font:700 30px "IBM Plex Mono";color:rgba(243,239,230,.55)} #s2,#s10,#s11{transform:translateY(170px)}</style>'


def scenes(A):
    b = lambda t: round(t - .1, 3)
    t2 = A('Sonunda'); t3 = A("1946'dan"); t4 = A('Ortalama'); t5 = A('Peki'); t6 = A('Belirsizlik.')
    t7 = A('Ara', 29); t8 = A('Sonuç'); t9 = A('Ama'); t10 = A('20 seçim'); t11 = A('Geçmiş'); t12 = A('Seçim', 45)
    t13 = A('1 yıl', 48); t14 = A('Bakalım')
    return [('s1', 0, b(t2)), ('s2', b(t2), b(t3)), ('s3', b(t3), b(t4)), ('s4', b(t4), b(t5)), ('s5', b(t5), b(t6)),
            ('s6', b(t6), b(t7)), ('s7', b(t7), b(t8)), ('s8', b(t8), b(t9)), ('s9', b(t9), b(t10)), ('s10', b(t10), b(t11)),
            ('s11', b(t11), b(t12)), ('s12', b(t12), b(t13)), ('s13', b(t13), b(t14)), ('s14', b(t14), DUR)]


def SFX(A):
    return [[A("20'de 20"), 'impact', -8, 1, 'hook'], [A('değil.'), 'stamp', -10, 0, 'parti'], [A('Sonunda') + .4, 'whoosh_hollow', -12, 0, 'kilit'],
            [A("1946'dan"), 'stamp', -10, 0, '1946'], [A('Her') + .3, 'gears', -12, 0, 'grid'], [A('%15'), 'impact', -8, 1, '15'],
            [A('2 katı'), 'pop', -10, 0, '2x'], [A('Belirsizlik.'), 'impact', -8, 1, 'bel'], [A('dalgalanır.'), 'marker', -11, 0, 'wave'],
            [A('%4,7'), 'stamp', -10, 0, '47'], [A('%9,5'), 'stamp', -10, 0, '95'], [A('kalkar.'), 'whoosh_hollow', -12, 0, 'calm'],
            [A('tuzak'), 'impact', -8, 1, 'tuzak'], [A('düşüşler'), 'paper_drop', -9, 0, 'dusus'], [A('garanti'), 'stamp', -9, 1, 'garanti'],
            [A('yön'), 'pop', -11, 0, 'yon'], [A('kaydet.') + .05, 'success', -10, 1, 'kaydet'], [A("21'de 21"), 'impact', -8, 1, 'loop']]


def RISERS(A): return [[A('Peki') - .5, 'sharp', -9], [A('Ama') - .4, 'metallic', -10]]


SCENE_HTML = r'''
  <section id="s1" class="scene clip">
    <div class="a lab" id="s1l" style="left:0;right:0;top:250px;text-align:center">ABD ARA SEÇİMİ · 1 YIL SONRA BORSA</div>
    <div class="a big gold" id="s1v" style="left:0;right:0;top:1180px;text-align:center;font-size:190px">20/20</div>
  </section>
  <section id="s2" class="scene clip">
    <div class="a lab" id="s2l" style="left:60px;top:330px">SONUNDA ELİNDE OLACAK</div>
    <div class="a card" id="s2c1" style="left:60px;top:420px;width:960px;display:flex;align-items:center;gap:30px">
      <div class="big gold" style="font-size:120px">1</div><div class="h" style="font-size:66px">Nasıl okunur?</div></div>
    <div class="a card" id="s2c2" style="left:60px;top:680px;width:960px;display:flex;align-items:center;gap:30px;border-color:#ff4a3d">
      <div class="big red" style="font-size:120px">2</div><div class="h" style="font-size:66px">Gizli <span class="red">tuzak</span></div></div>
    <div class="a mono" id="s2m" style="left:60px;top:960px">ama önce rakamlar ↓</div>
  </section>
  <section id="s3" class="scene clip">
    <div class="a lab" id="s3l" style="left:60px;top:270px">1946–2022 · 20 ARA SEÇİM</div>
    <div class="a" id="s3g" style="left:60px;top:340px;width:960px;display:grid;grid-template-columns:repeat(5,150px);gap:52px 52px">__DOTS__</div>
    <div class="a h" id="s3h" style="left:60px;top:1240px;font-size:62px">1 YIL SONRA: <span class="green">HEPSİ YUKARIDA</span></div>
  </section>
  <section id="s4" class="scene clip">
    <div class="a lab" id="s4l" style="left:60px;top:290px">S&amp;P 500 · SEÇİMDEN 1 YIL SONRA</div>
    <div class="a mono" id="s4m0" style="left:60px;top:345px">ortalama getiri</div>
    <svg class="a" id="s4svg" style="left:60px;top:420px" width="960" height="760" viewBox="0 0 960 760">
      <line x1="0" x2="960" y1="660" y2="660" stroke="rgba(243,239,230,.25)" stroke-width="3"/>
      <rect id="s4b1" x="80" y="140" width="320" height="520" rx="16" fill="#e8b931"/>
      <rect id="s4b2" x="560" y="380" width="320" height="280" rx="16" fill="rgba(243,239,230,.28)"/>
      <text id="s4t1" x="240" y="115" text-anchor="middle" font-family="Inter Tight" font-weight="900" font-size="96" fill="#e8b931">≈%15</text>
      <text id="s4t2" x="720" y="350" text-anchor="middle" font-family="Inter Tight" font-weight="900" font-size="70" fill="#f3efe6">≈ YARISI</text>
      <text x="240" y="715" text-anchor="middle" font-family="IBM Plex Mono" font-size="28" fill="rgba(243,239,230,.75)">ARA SEÇİM SONRASI</text>
      <text x="720" y="715" text-anchor="middle" font-family="IBM Plex Mono" font-size="28" fill="rgba(243,239,230,.75)">DİĞER YILLAR</text></svg>
    <div class="a h gold" id="s4x" style="left:60px;top:1240px;font-size:84px">NEREDEYSE 2 KAT</div>
  </section>
  <section id="s5" class="scene clip">
    <div class="a h" id="s5h" style="left:0;right:0;top:1180px;text-align:center;font-size:96px">SEBEP <span class="gold">NE?</span></div>
  </section>
  <section id="s6" class="scene clip">
    <div class="a ghost" id="s6g" data-layout-allow-overflow data-layout-allow-occlusion data-layout-allow-overlap style="left:-30px;top:300px">?</div>
    <div class="a big gold" id="s6h" style="left:60px;top:300px;font-size:150px">BELİRSİZLİK</div>
    <div class="a mono" id="s6m" style="left:60px;top:470px">Kongre kime kalacak? · seçim yılı</div>
    <svg class="a" id="s6svg" style="left:60px;top:560px" width="960" height="560" viewBox="0 0 960 560">
      <path id="s6p" d="M0 280 L60 150 L110 400 L170 120 L230 430 L290 170 L350 390 L410 130 L470 420 L530 200 L590 360 L650 230 L700 300" fill="none" stroke="#ff4a3d" stroke-width="10" stroke-linejoin="round"/>
      <line x1="700" x2="700" y1="40" y2="520" stroke="#e8b931" stroke-width="5" stroke-dasharray="14 12"/>
      <text x="720" y="80" font-family="IBM Plex Mono" font-weight="700" font-size="30" fill="#e8b931">SEÇİM GÜNÜ</text></svg>
    <div class="a h red" id="s6w" style="left:60px;top:1180px;font-size:76px">DALGALANMA ↑</div>
  </section>
  <section id="s7" class="scene clip">
    <div class="a lab" id="s7l" style="left:60px;top:290px">S&amp;P 500 · YILLIK ORT. GETİRİ · 1930–2022</div>
    <div class="a card" id="s7a" style="left:60px;top:380px;width:450px;height:640px;text-align:center;border-color:#ff4a3d">
      <div class="lab" style="color:#f3efe6">ARA SEÇİM YILI</div><div class="big red" id="s7v1" style="font-size:150px;margin-top:150px">%4,7</div></div>
    <div class="a card" id="s7b" style="left:570px;top:380px;width:450px;height:640px;text-align:center;border-color:#3ddc84">
      <div class="lab" style="color:#f3efe6">DİĞER YILLAR</div><div class="big green" id="s7v2" style="font-size:150px;margin-top:150px">%9,5</div></div>
    <div class="a mono" id="s7m" style="left:60px;top:1070px">kaynak: Capital Group (toplam getiri)</div>
  </section>
  <section id="s8" class="scene clip">
    <div class="a lab" id="s8l" style="left:60px;top:300px">SONUÇ BELLİ OLUNCA</div>
    <svg class="a" id="s8svg" style="left:60px;top:380px" width="960" height="560" viewBox="0 0 960 560">
      <path d="M0 280 L60 170 L110 380 L170 150 L230 400 L290 200 L330 300" fill="none" stroke="rgba(255,74,61,.45)" stroke-width="8" stroke-linejoin="round"/>
      <line x1="330" x2="330" y1="40" y2="520" stroke="#e8b931" stroke-width="5" stroke-dasharray="14 12"/>
      <path id="s8p" d="M330 300 C 450 290, 560 250, 660 220 S 860 150, 950 120" fill="none" stroke="#3ddc84" stroke-width="12" stroke-linecap="round"/></svg>
    <div class="a h" id="s8h" style="left:60px;top:1000px;font-size:84px">BELİRSİZLİK <span class="green">KALKAR</span></div>
  </section>
  <section id="s9" class="scene clip">
    <div class="a h red" id="s9h" style="left:0;right:0;top:640px;text-align:center;font-size:150px">⚠ TUZAK</div>
  </section>
  <section id="s10" class="scene clip">
    <div class="a lab" id="s10l" style="left:60px;top:300px">ÖRNEKLEM</div>
    <div class="a big gold" id="s10v" style="left:52px;top:350px;font-size:230px">20</div>
    <div class="a h" id="s10u" style="left:60px;top:590px;font-size:80px">SEÇİM = KÜÇÜK</div>
    <div class="a card" id="s10c" style="left:60px;top:760px;width:960px;border-color:#ff4a3d">
      <div class="lab" style="color:#f3efe6">DAHA ESKİ SERİ (1946 ÖNCESİ)</div>
      <div class="h red" style="font-size:64px;margin-top:22px">↓ DÜŞÜŞ YILLARI DA VAR</div></div>
  </section>
  <section id="s11" class="scene clip">
    <div class="a h" id="s11a" style="left:60px;top:460px;font-size:100px">GEÇMİŞ</div>
    <div class="a h" id="s11b" style="left:60px;top:575px;font-size:100px">PERFORMANS</div>
    <div class="a h red" id="s11c" style="left:60px;top:760px;font-size:76px;border:7px solid #ff4a3d;padding:8px 26px;border-radius:12px;transform:rotate(-4deg)">≠ GARANTİ</div>
  </section>
  <section id="s12" class="scene clip">
    <div class="a h" id="s12a" style="left:120px;top:1180px;font-size:84px">YÖN <span class="green">✓</span></div>
    <div class="a h" id="s12b" style="left:600px;top:1180px;font-size:84px">SÖZ <span class="red">✗</span></div>
  </section>
  <section id="s13" class="scene clip">
    <svg class="a" id="s13i" style="left:250px;top:1166px" width="96" height="120" viewBox="0 0 96 120"><path d="M8 6h80v108L48 86 8 114z" fill="#e8b931"/></svg>
    <div class="a h gold" id="s13t" style="left:370px;top:1170px;font-size:118px">KAYDET</div>
  </section>
  <section id="s14" class="scene clip">
    <div class="a big" id="s14a" style="left:0;right:0;top:1170px;text-align:center;font-size:90px">20/20 → <span class="gold">21/21?</span></div>
  </section>
'''
_YEARS = list(range(1946, 2023, 4))
SCENE_HTML = SCENE_HTML.replace('__DOTS__', ''.join(f'<div class="dot" id="d{i}">{y}</div>' for i, y in enumerate(_YEARS)))

SCENE_JS = r'''
const at=(p,after=0)=>{for(const c of CAPS)for(const w of c.w)if(w[1]>=after&&w[0].toLowerCase().startsWith(p.toLowerCase()))return w[1];return null;};
// S1 kanca
inn('#s1l',.3,{y:-20}); slam('#s1v',at("20'de"));
// S2 kilit
const s2=st('s2'); inn('#s2l',s2+.4); inn('#s2c1',at('okuyacağını')-.2,{y:60}); inn('#s2c2',at('tuzağını')-.1,{y:60}); inn('#s2m',at('bileceksin')+.2,{y:16});
// S3 20 kare
const s3=st('s3'); inn('#s3l',s3+.4); inn('#s3g',s3+.5,{y:30});
for(let i=0;i<20;i++){tl.to('#d'+i,{backgroundColor:'rgba(61,220,132,.22)',borderColor:'#3ddc84',color:'#f3efe6',duration:.12},at('Her')+.2+i*.13);}
slam('#s3h',at('yukarıdaydı'));
// S4 çubuklar
const s4=st('s4'); inn('#s4l',s4+.4); inn('#s4m0',s4+.45); inn('#s4svg',s4+.5,{y:0});
tl.fromTo('#s4b1',{scaleY:0,transformOrigin:'50% 100%'},{scaleY:1,duration:.6,ease:'power3.out'},at('%15')-.3);
tl.fromTo('#s4t1',{opacity:0},{opacity:1,duration:.25},at('%15'));
tl.fromTo('#s4b2',{scaleY:0,transformOrigin:'50% 100%'},{scaleY:1,duration:.5,ease:'power3.out'},at('diğer'));
tl.fromTo('#s4t2',{opacity:0},{opacity:1,duration:.25},at('diğer')+.4); slam('#s4x',at('2 katı'));
// S5 ara kanca
inn('#s5h',st('s5')+.4,{s:1.15});
// S6 belirsizlik
const s6=st('s6'); tl.fromTo('#s6g',{x:0},{x:120,duration:st('s7')-s6,ease:'none'},s6); slam('#s6h',s6+.4); inn('#s6m',at('Seçim',25));
inn('#s6svg',at('Seçim',25)+.1,{y:0}); tl.fromTo('#s6p',{strokeDasharray:2600,strokeDashoffset:2600},{strokeDashoffset:0,duration:2.4,ease:'none'},at('Seçim',25)+.2);
slam('#s6w',at('dalgalanır'));
// S7 4,7 vs 9,5
const s7=st('s7'); inn('#s7l',s7+.4); inn('#s7a',s7+.5,{y:60}); slam('#s7v1',at('%4,7')); inn('#s7b',at('diğer',33)-.2,{y:60}); slam('#s7v2',at('%9,5')); inn('#s7m',at('%9,5')+.4,{y:10});
// S8 sakinleşme
const s8=st('s8'); inn('#s8l',s8+.4); inn('#s8svg',s8+.45,{y:0});
tl.fromTo('#s8p',{strokeDasharray:800,strokeDashoffset:800},{strokeDashoffset:0,duration:1.2,ease:'power2.out'},s8+.7); slam('#s8h',at('kalkar'));
// S9 tuzak
const s9=st('s9'); tl.fromTo('#s9h',{opacity:0,scale:1.6,transformOrigin:'50% 50%'},{opacity:1,scale:1,duration:.3,ease:'power4.in'},s9+.4);
// S10 örneklem
const s10=st('s10'); inn('#s10l',s10+.4); slam('#s10v',s10+.45); inn('#s10u',at('küçük')); inn('#s10c',at('eski')-.1,{y:60});
// S11 garanti değil
const s11=st('s11'); slam('#s11a',s11+.4); inn('#s11b',at('performans')); tl.fromTo('#s11c',{opacity:0,scale:1.6},{opacity:1,scale:1,duration:.25,ease:'power4.in'},at('garanti'));
// S12 yön / söz
const s12=st('s12'); slam('#s12a',at('yön')); slam('#s12b',at('söz'));
// S13 CTA
const s13=st('s13'); tl.fromTo('#s13i',{opacity:0,y:-80},{opacity:1,y:0,duration:.4,ease:'bounce.out'},at('kaydet')-.1); slam('#s13t',at('kaydet'));
// S14 döngü
const s14=st('s14'); inn('#s14a',s14+.4,{s:1.1});
'''
