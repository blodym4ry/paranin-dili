import os
# Kinetik stili (önceki video Gazete). Ayrık yöntem: avatar s1 (kanca), s9 (ara kanca 2), s11-s12 (kapanış + CTA/döngü).
# Düzen 22 Kas Kinetik videosundan farklı: üstte geniş portre + altta karşılaştırma şeridi, yığın bar grafikleri, merdiven grafiği.
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [
    (N('yüzde', 'on', 'iki', 'virgül', 'on', 'dokuz'), '%12,19'), (N('yüzde', 'yirmi', 'yedi'), '%27'),
    (N('altı', 'ayın'), '6 ayın'), (N('iki', 'bin', 'yirmi', 'beşte'), "2025'te"), (N('yüzde', 'otuz', 'beş'), '%35'),
    (N('yüzde', 'otuz', 'iki'), '%32'), (N('yüzde', 'otuz'), '%30'), (N('yüzde', 'on', 'yedi', 'virgül', 'yetmiş', 'altı'), '%17,76'),
    (N('altı', 'ay'), '6 ay'),
]
EM = {'formül', 'formülden', 'temmuz', "temmuz'da", "temmuz'u", 'faturası', 'tek', 'toplam', 'zamanlamada', 'erir', 'telafi', 'kaydet', 'kanunda'}
RED = {'%27', 'erir', 'kayıp', 'geçmez'}
TOP = [215, 250, 650, 914, 26]         # 740:1040 portre — saç ve çene görünür
BIG = [170, 300, 740, 1040, 28]
AV = {'s1': TOP, 's2': None, 's3': None, 's4': None, 's5': None, 's6': None, 's7': None, 's8': None, 's9': BIG, 's10': None,
      's11': [60, 330, 440, 618, 22], 's12': TOP}
EXTRA_CSS = r'''<style>
.chip{display:inline-block;padding:10px 22px;border-radius:40px;font:800 40px 'Inter Tight';background:rgba(243,239,230,.08);border:3px solid rgba(243,239,230,.18)}
.seg{position:absolute;left:0;right:0;transform-origin:50% 100%}
</style>'''


def scenes(A):
    b = lambda t: round(t - .1, 3)
    t2 = A('Sonunda'); t3 = A('Formül'); t4 = A('Yani'); t5 = A('Peki'); t6 = A('Çünkü'); t7 = A("2025'te"); t8 = A('Bu', 38)
    t9 = A('Asıl'); t10 = A('Fiyatlar'); t11 = A('Formül', 52); t12 = A('Kaydet')
    return [('s1', 0, b(t2)), ('s2', b(t2), b(t3)), ('s3', b(t3), b(t4)), ('s4', b(t4), b(t5)), ('s5', b(t5), b(t6)),
            ('s6', b(t6), b(t7)), ('s7', b(t7), b(t8)), ('s8', b(t8), b(t9)), ('s9', b(t9), b(t10)), ('s10', b(t10), b(t11)),
            ('s11', b(t11), b(t12)), ('s12', b(t12), DUR)]


def SFX(A):
    return [[A('%12,19'), 'stamp', -9, 1, 'emekli'], [A('%27'), 'impact', -8, 1, 'asgari'], [A("Temmuz'da."), 'whoosh_hollow', -12, 0, 'tem'],
            [A('Formül'), 'paper_drop', -10, 0, 'kanun'], [A('6 ayın'), 'marker', -11, 0, '6ay'], [A('faturası.'), 'stamp', -9, 1, 'fatura'],
            [A('tek', 30), 'pop', -10, 0, 'tek'], [A('%35'), 'impact', -8, 1, '35'], [A('%30'), 'marker', -11, 0, '30'],
            [A('%17,76'), 'pop', -10, 0, '1776'], [A('%32'), 'impact', -8, 1, '32'], [A('erir.'), 'paper_drop', -10, 0, 'erir'],
            [A('Kaydet') + .1, 'success', -10, 1, 'kaydet'], [A("Temmuz'u"), 'impact', -9, 1, 'loop']]


def RISERS(A): return [[A('Peki') - .5, 'sharp', -9], [A('Asıl') - .4, 'metallic', -10]]


SCENE_HTML = r'''
  <section id="s1" class="scene clip">
    <div class="a" id="s1row" style="left:60px;right:60px;top:1200px;display:flex;gap:24px">
      <div class="card" id="s1e" style="flex:1;padding:22px 26px"><div class="lab">EMEKLİ · OCAK</div><div class="big" style="font-size:118px;margin-top:10px">%12,19</div></div>
      <div class="card" id="s1a" style="flex:1;padding:22px 26px;border-color:#e8b931"><div class="lab">ASGARİ ÜCRET</div><div class="big gold" style="font-size:118px;margin-top:10px">%27</div></div></div>
    <div class="a h" id="s1t" data-layout-allow-overflow style="left:0;right:0;top:1200px;text-align:center;font-size:84px">+ TEMMUZ <span class="gold">?</span></div>
  </section>
  <section id="s2" class="scene clip">
    <div class="a ghost" id="s2g" data-layout-allow-overflow data-layout-allow-occlusion data-layout-allow-overlap style="left:-40px;top:380px">f(x)</div>
    <div class="a big" id="s2n" style="left:60px;top:560px;font-size:300px">1</div>
    <div class="a h" id="s2h" style="left:280px;top:620px;font-size:130px">FORMÜL</div>
    <svg class="a" id="s2svg" style="left:60px;top:900px" width="960" height="240" viewBox="0 0 960 240">
      <rect x="0" y="40" width="430" height="160" rx="24" fill="rgba(243,239,230,.04)" stroke="rgba(243,239,230,.18)" stroke-width="3"/>
      <text x="215" y="140" text-anchor="middle" font-family="Inter Tight" font-weight="900" font-size="56" fill="#f3efe6">OCAK</text>
      <path id="s2p" d="M450 120 H500" stroke="#e8b931" stroke-width="8"/><path d="M490 95 L520 120 L490 145" fill="none" stroke="#e8b931" stroke-width="8"/>
      <rect x="530" y="40" width="430" height="160" rx="24" fill="rgba(232,185,49,.12)" stroke="#e8b931" stroke-width="3"/>
      <text x="745" y="140" text-anchor="middle" font-family="Inter Tight" font-weight="900" font-size="56" fill="#e8b931">YIL SONU</text></svg>
  </section>
  <section id="s3" class="scene clip">
    <div class="a lab" id="s3l" style="left:60px;top:380px">5510 SAYILI KANUN · MADDE 55</div>
    <div class="a card" id="s3c" style="left:60px;top:440px;width:960px;padding:36px 40px">
      <div class="h" style="font-size:66px;line-height:1.1;white-space:normal">Emekli aylığı artışı =</div>
      <div class="h gold" style="font-size:80px;line-height:1.1;margin-top:14px;white-space:normal">önceki 6 ayın enflasyonu</div></div>
    <div class="a" id="s3tl" style="left:60px;top:840px;width:960px;height:220px"></div>
  </section>
  <section id="s4" class="scene clip">
    <div class="a lab" id="s4l" style="left:60px;top:380px">OCAK ZAMMI NEYİ ÖDER?</div>
    <div class="a" id="s4cal" style="left:60px;top:450px;width:960px;display:grid;grid-template-columns:repeat(6,1fr);gap:14px"></div>
    <div class="a h" id="s4a" style="left:60px;top:800px;font-size:72px">Yeni yılın değil,</div>
    <div class="a h gold" id="s4b" style="left:60px;top:890px;font-size:72px">geçen yılın 2. yarısı</div>
    <div class="a card" id="s4f" style="left:60px;top:1020px;padding:18px 30px;border-color:#ff4a3d"><span class="h red" style="font-size:60px">= FATURA</span></div>
  </section>
  <section id="s5" class="scene clip">
    <div class="a h" id="s5a" style="left:0;right:0;top:560px;text-align:center;font-size:96px">Asgari ücret</div>
    <div class="a h" id="s5b" style="left:0;right:0;top:680px;text-align:center;font-size:96px">neden <span class="gold">BÜYÜK</span></div>
    <div class="a h" id="s5c" style="left:0;right:0;top:800px;text-align:center;font-size:96px">görünüyor?</div>
  </section>
  <section id="s6" class="scene clip">
    <div class="a card" id="s6a" style="left:60px;top:420px;width:960px;padding:30px 36px;border-color:#e8b931">
      <div class="lab">ASGARİ ÜCRET</div><div style="display:flex;align-items:baseline;gap:24px;margin-top:14px"><span class="big gold" style="font-size:120px">1</span><span class="h" style="font-size:62px">karar · 12 ay</span></div>
      <div id="s6bar1" style="margin-top:20px;height:40px;border-radius:10px;background:#e8b931;transform-origin:0 50%"></div></div>
    <div class="a card" id="s6b" style="left:60px;top:800px;width:960px;padding:30px 36px">
      <div class="lab" style="color:#f3efe6">EMEKLİ</div><div style="display:flex;align-items:baseline;gap:24px;margin-top:14px"><span class="big" style="font-size:120px">2</span><span class="h" style="font-size:62px">parça · Ocak + Temmuz</span></div>
      <div style="margin-top:20px;display:flex;gap:14px"><div id="s6p1" style="flex:1;height:40px;border-radius:10px;background:#f3efe6;transform-origin:0 50%"></div><div id="s6p2" style="flex:1;height:40px;border-radius:10px;background:#f3efe6;transform-origin:0 50%"></div></div></div>
  </section>
  <section id="s7" class="scene clip">
    <div class="a lab" id="s7l" style="left:60px;top:300px">2025 · YIL TOPLAMI</div>
    <div class="a" id="s7e" style="left:170px;top:470px;width:300px;height:620px">
      <div class="seg" id="s7e1" style="bottom:0;height:42.7%;background:rgba(243,239,230,.55);border-radius:0 0 14px 14px"><div class="mono" style="position:absolute;left:0;right:0;top:40%;text-align:center;color:#0d0c0a;font-weight:700">OCAK 15,75</div></div>
      <div class="seg" id="s7e2" style="bottom:42.7%;height:52.3%;background:#f3efe6;border-radius:14px 14px 0 0"><div class="mono" style="position:absolute;left:0;right:0;top:40%;text-align:center;color:#0d0c0a;font-weight:700">TEMMUZ 16,67</div></div></div>
    <div class="a" id="s7a" style="left:610px;top:470px;width:300px;height:620px"><div class="seg" id="s7a1" style="bottom:0;height:81.4%;background:#e8b931;border-radius:14px"></div></div>
    <div class="a big" id="s7ev" style="left:170px;top:400px;width:300px;text-align:center;font-size:96px">~%35</div>
    <div class="a big gold" id="s7av" style="left:610px;top:480px;width:300px;text-align:center;font-size:96px">%30</div>
    <div class="a h" id="s7c1" style="left:170px;top:1110px;width:300px;text-align:center;font-size:56px">Emekli</div>
    <div class="a h" id="s7c2" style="left:610px;top:1110px;width:300px;text-align:center;font-size:56px">Asgari ücret</div>
  </section>
  <section id="s8" class="scene clip">
    <div class="a lab" id="s8l" style="left:60px;top:300px">2026 · YIL TOPLAMI</div>
    <div class="a" id="s8e" style="left:170px;top:470px;width:300px;height:620px">
      <div class="seg" id="s8e1" style="bottom:0;height:33.1%;background:rgba(243,239,230,.55);border-radius:0 0 14px 14px"><div class="mono" style="position:absolute;left:0;right:0;top:35%;text-align:center;color:#0d0c0a;font-weight:700">OCAK 12,19</div></div>
      <div class="seg" id="s8e2" style="bottom:33.1%;height:53.8%;background:#f3efe6;border-radius:14px 14px 0 0"><div class="mono" style="position:absolute;left:0;right:0;top:40%;text-align:center;color:#0d0c0a;font-weight:700">TEMMUZ 17,76</div></div></div>
    <div class="a" id="s8a" style="left:610px;top:470px;width:300px;height:620px"><div class="seg" id="s8a1" style="bottom:0;height:73.3%;background:#e8b931;border-radius:14px"></div></div>
    <div class="a big" id="s8ev" style="left:170px;top:450px;width:300px;text-align:center;font-size:96px">~%32</div>
    <div class="a big gold" id="s8av" style="left:610px;top:530px;width:300px;text-align:center;font-size:96px">%27</div>
    <div class="a h" id="s8c1" style="left:170px;top:1110px;width:300px;text-align:center;font-size:56px">Emekli</div>
    <div class="a h" id="s8c2" style="left:610px;top:1110px;width:300px;text-align:center;font-size:56px">Asgari ücret</div>
  </section>
  <section id="s9" class="scene clip">
    <div class="a h gold" id="s9h" style="left:0;right:0;top:1380px;text-align:center;font-size:84px">ZAMANLAMA</div>
  </section>
  <section id="s10" class="scene clip">
    <div class="a lab" id="s10l" style="left:60px;top:380px">FİYATLAR ÖNCE · AYLIK SONRA</div>
    <svg class="a" id="s10svg" style="left:40px;top:440px" width="1000" height="700" viewBox="0 0 1000 700"></svg>
  </section>
  <section id="s11" class="scene clip">
    <div class="a" id="s11r0" style="left:540px;top:400px;display:flex;gap:20px;align-items:center"><div class="tick" id="s11k0"></div><div class="h" style="font-size:64px">Telafi</div></div>
    <div class="a" id="s11r1" style="left:540px;top:540px;display:flex;gap:20px;align-items:center"><div class="tick" id="s11k1" style="border-color:#ff4a3d"></div><div class="h red" style="font-size:64px">Öne geçmek</div></div>
    <div class="a mono" id="s11m" style="left:540px;top:680px">formül = enflasyon kadar</div>
  </section>
  <section id="s12" class="scene clip">
    <svg class="a" id="s12i" style="left:250px;top:1200px" width="96" height="120" viewBox="0 0 96 120"><path d="M8 6h80v108L48 86 8 114z" fill="#e8b931"/></svg>
    <div class="a h gold" id="s12t" style="left:370px;top:1210px;font-size:118px">KAYDET</div>
    <div class="a h" id="s12a" style="left:0;right:0;top:1210px;text-align:center;font-size:84px">OCAK <span class="gold">+ TEMMUZ</span></div>
  </section>
'''

SCENE_JS = r'''
const at=(p,after=0)=>{for(const c of CAPS)for(const w of c.w)if(w[1]>=after&&w[0].toLowerCase().startsWith(p.toLowerCase()))return w[1];return null;};
// S1 kanca
inn('#s1e',at('%12,19'),{y:40}); inn('#s1a',at('%27'),{y:40}); out(['#s1e','#s1a'],at('Ama')-.2); slam('#s1t',at('Temmuz'));
// S2 tek formül
const s2=st('s2'); tl.fromTo('#s2g',{x:0},{x:-180,duration:st('s3')-s2,ease:'none'},s2); slam('#s2n',at('tek')); inn('#s2h',at('formülden'));
inn('#s2svg',at('yıl',10),{y:30});
// S3 kanun + Ocak/Temmuz zaman çizgisi
const s3=st('s3'); inn('#s3l',s3+.4); inn('#s3c',at('kanunda'),{y:40});
(function(){const b=$('#s3tl');const M=['O','Ş','M','N','M','H','T','A','E','E','K','A'];
 M.forEach((m,i)=>{const d=document.createElement('div');d.id='s3m'+i;const k=(i===0||i===6);
  Object.assign(d.style,{position:'absolute',left:(i*80)+'px',top:'60px',width:'68px',height:'100px',borderRadius:'12px',display:'flex',alignItems:'center',justifyContent:'center',
   font:"800 34px 'Inter Tight'",background:k?'#e8b931':'rgba(243,239,230,.08)',color:k?'#0d0c0a':'rgba(243,239,230,.6)'});d.textContent=m;b.appendChild(d);});
 for(let i=0;i<12;i++) tl.fromTo('#s3m'+i,{opacity:0,y:20},{opacity:1,y:0,duration:.25},at('Ocak',16)-.3+i*.03);
 tl.to(['#s3m0','#s3m6'],{scale:1.15,duration:.2,yoyo:true,repeat:1},at('Temmuz',16));})();
// S4 takvim: Tem–Ara 2025 → Ocak 2026
const s4=st('s4'); inn('#s4l',s4+.4);
(function(){const g=$('#s4cal');const M=['TEM','AĞU','EYL','EKİ','KAS','ARA'];M.forEach((m,i)=>{const d=document.createElement('div');d.id='s4c'+i;
 Object.assign(d.style,{height:'150px',borderRadius:'16px',background:'rgba(243,239,230,.06)',border:'3px solid rgba(243,239,230,.15)',display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center',font:"800 34px 'Inter Tight'",color:'#f3efe6'});
 d.innerHTML=m+'<span style="font:500 22px IBM Plex Mono;opacity:.6;margin-top:6px">2025</span>';g.appendChild(d);});
 for(let i=0;i<6;i++){tl.fromTo('#s4c'+i,{opacity:0,y:30},{opacity:1,y:0,duration:.3},s4+.45+i*.05); tl.to('#s4c'+i,{backgroundColor:'rgba(232,185,49,.35)',borderColor:'#e8b931',duration:.2},at('geçen')+i*.08);}})();
inn('#s4a',at('yeni')); inn('#s4b',at('geçen')); slam('#s4f',at('faturası'));
// S5 ara kanca
const s5=st('s5'); inn('#s5a',s5+.4); inn('#s5b',at('neden',26)); inn('#s5c',at('görünüyor'));
// S6 1 karar vs 2 parça
const s6=st('s6'); inn('#s6a',s6+.4,{y:40}); tl.fromTo('#s6bar1',{scaleX:0},{scaleX:1,duration:.8,ease:'power2.out'},at('tüm'));
inn('#s6b',at('tek',30),{y:40}); tl.fromTo('#s6p1',{scaleX:0},{scaleX:1,duration:.4},at('seferde')); tl.fromTo('#s6p2',{scaleX:0},{scaleX:1,duration:.4},at('belirlenir'));
// S7 2025
const s7=st('s7'); inn('#s7l',s7+.4); inn(['#s7c1','#s7c2'],s7+.45,{y:16});
tl.fromTo('#s7e1',{scaleY:0},{scaleY:1,duration:.45,ease:'power3.out'},at('iki',33)); tl.fromTo('#s7e2',{scaleY:0},{scaleY:1,duration:.45,ease:'power3.out'},at('zamla'));
slam('#s7ev',at('%35')); tl.fromTo('#s7a1',{scaleY:0},{scaleY:1,duration:.5,ease:'power3.out'},at('asgari',36)); slam('#s7av',at('%30'));
// S8 2026
const s8=st('s8'); inn('#s8l',s8+.4); inn(['#s8c1','#s8c2'],s8+.45,{y:16}); tl.fromTo('#s8e1',{scaleY:0},{scaleY:1,duration:.45,ease:'power3.out'},s8+.5);
tl.fromTo('#s8e2',{scaleY:0},{scaleY:1,duration:.45,ease:'power3.out'},at('%17,76')); slam('#s8ev',at('%32'));
tl.fromTo('#s8a1',{scaleY:0},{scaleY:1,duration:.5,ease:'power3.out'},at('asgari',43)); slam('#s8av',at('%27',43));
// S9 ara kanca 2
inn('#s9h',st('s9')+.35,{y:20});
// S10 merdiven grafiği: fiyat sürekli, aylık 6 ayda bir basamak
const s10=st('s10'); inn('#s10l',s10+.4);
(function(){const svg=$('#s10svg');const X=m=>60+m*(880/12),Y=v=>620-(v-100)/(132-100)*520;
 let pp='',pa='',area='';const P=m=>100*Math.pow(1.0235,m);
 for(let m=0;m<=12;m+=.25){pp+=(m?'L':'M')+X(m).toFixed(1)+','+Y(P(m)).toFixed(1);}
 const A=m=>m<6?100:(m<12?P(6):P(12)); const steps=[[0,100],[6,100],[6,P(6)],[12,P(6)],[12,P(12)]];
 steps.forEach(([m,v],i)=>{pa+=(i?'L':'M')+X(m).toFixed(1)+','+Y(v).toFixed(1);});
 area='M'+X(0)+','+Y(100);for(let m=0;m<=6;m+=.25)area+='L'+X(m).toFixed(1)+','+Y(P(m)).toFixed(1);area+='L'+X(6)+','+Y(100)+'Z';
 let area2='M'+X(6)+','+Y(P(6));for(let m=6;m<=12;m+=.25)area2+='L'+X(m).toFixed(1)+','+Y(P(m)).toFixed(1);area2+='L'+X(12)+','+Y(P(6))+'Z';
 svg.innerHTML=`<line x1="60" x2="940" y1="620" y2="620" stroke="rgba(243,239,230,.2)" stroke-width="3"/>
  <text x="${X(0)}" y="670" font-family="IBM Plex Mono" font-size="28" fill="rgba(243,239,230,.7)">OCAK</text><text x="${X(6)}" y="670" text-anchor="middle" font-family="IBM Plex Mono" font-size="28" fill="rgba(243,239,230,.7)">TEMMUZ</text><text x="${X(12)}" y="670" text-anchor="end" font-family="IBM Plex Mono" font-size="28" fill="rgba(243,239,230,.7)">OCAK</text>
  <path id="s10g1" d="${area}" fill="rgba(255,74,61,.22)"/><path id="s10g2" d="${area2}" fill="rgba(255,74,61,.22)"/>
  <path id="s10pp" d="${pp}" fill="none" stroke="#ff4a3d" stroke-width="9" stroke-linejoin="round"/>
  <path id="s10pa" d="${pa}" fill="none" stroke="#e8b931" stroke-width="10" stroke-linejoin="round"/>
  <g id="s10k1"><rect x="80" y="40" width="300" height="60" rx="14" fill="#ff4a3d"/><text x="230" y="81" text-anchor="middle" font-family="Inter Tight" font-weight="800" font-size="34" fill="#0d0c0a">FİYATLAR</text></g>
  <g id="s10k2"><rect x="420" y="40" width="300" height="60" rx="14" fill="#e8b931"/><text x="570" y="81" text-anchor="middle" font-family="Inter Tight" font-weight="800" font-size="34" fill="#0d0c0a">EMEKLİ AYLIĞI</text></g>
  <text id="s10t" x="${X(3)}" y="${Y(102)}" text-anchor="middle" font-family="Inter Tight" font-weight="900" font-size="44" fill="#ff4a3d">ALIM GÜCÜ ERİR</text>`;
 const a=$('#s10pp'),b=$('#s10pa');const La=a.getTotalLength(),Lb=b.getTotalLength();a.style.strokeDasharray=La;b.style.strokeDasharray=Lb;
 tl.fromTo('#s10k1',{opacity:0},{opacity:1,duration:.25},at('Fiyatlar')); tl.fromTo(a,{strokeDashoffset:La},{strokeDashoffset:0,duration:1.6,ease:'none'},at('Fiyatlar')+.1);
 tl.fromTo('#s10k2',{opacity:0},{opacity:1,duration:.25},at('aylık',48)); tl.fromTo(b,{strokeDashoffset:Lb},{strokeDashoffset:0,duration:1.5,ease:'power1.inOut'},at('aylık',48)+.1);
 tl.fromTo(['#s10g1','#s10g2'],{opacity:0},{opacity:1,duration:.4},at('arada')); tl.fromTo('#s10t',{opacity:0,y:20},{opacity:1,y:0,duration:.3},at('alım'));})();
// S11 kapanış
const s11=st('s11'); inn('#s11r0',at('telafi')-.1,{y:24}); tl.to('#s11k0',{backgroundColor:'#e8b931',duration:.15},at('telafi')+.25);
inn('#s11r1',at('öne'),{y:24}); tl.to('#s11k1',{backgroundColor:'#ff4a3d',duration:.15},at('geçmez')); inn('#s11m',at('öne')+.1,{y:10});
// S12 CTA + döngü
const s12=st('s12'); tl.fromTo('#s12i',{opacity:0,y:-80},{opacity:1,y:0,duration:.4,ease:'bounce.out'},s12+.1); slam('#s12t',s12+.2);
out(['#s12i','#s12t'],at("Temmuz'u")-.3); slam('#s12a',at("Temmuz'u"));
'''
