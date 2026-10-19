import os
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [
    (N('bir', "ağustos'ta"), "1 Ağustos'ta"), (N('son', 'otuz', 'günün'), 'son 30 günün'), (N('son', 'on', 'gün'), 'son 10 gün'),
    (N('on', 'bir', 'gün'), '11 gün'), (N('bin', 'liralık'), '1.000 liralık'), (N('bin', 'beş', 'yüz'), '1.500'),
    (N('bin', 'liraya'), '1.000 liraya'), (N('yüzde', 'otuz', 'üç'), '%33'),
    (N('iki', 'yüz', 'kırk', 'dokuz', 'milyon', 'liradan'), '249 milyon liradan'), (N('yüzde', 'yetmiş', 'beşe'), "%75'e"),
    (N('son', 'üç', 'ayın'), 'son 3 ayın'), (N('ilk', 'dokuz', 'ayında'), 'ilk 9 ayında'),
]
EM = {'grafiğine', 'bak', 'değişti', 'eskiden', 'artık', 'aynı', 'takip', 'zıplama', 'kaydet', 'sakın'}
RED = {'sakın', '1.500', '%33', 'aynı', '249 milyon liradan', "%75'e", 'zıplama'}
HOOK = [170, 250, 740, 1040, 370]; R = [600, 270, 420, 700, 210]; TL = [60, 250, 300, 300, 150]; BR = [760, 1150, 260, 260, 130]; TC = [390, 250, 300, 300, 150]
AV = {'s1': HOOK, 's2': R, 's3': TL, 's4': BR, 's5': R, 's6': TC, 's7': R, 's8': HOOK, 's9': HOOK}
def scenes(A):
    t2 = A('Çünkü'); t3 = A('Eskiden'); t4 = A('Yani', t3); t5 = A('Örnek'); t6 = A('Reklam'); t7 = A('Almak'); t8 = A('Kaydet,') if False else A('Kaydet')
    t9 = A('Efsane', t8 + .5)
    return [('s1', 0, t2 - .1), ('s2', t2 - .1, t3 - .1), ('s3', t3 - .1, t4 - .1), ('s4', t4 - .1, t5 - .1), ('s5', t5 - .1, t6 - .1),
            ('s6', t6 - .1, t7 - .1), ('s7', t7 - .1, t8 - .1), ('s8', t8 - .1, t9 - .1), ('s9', t9 - .1, DUR)]
_A = None
def SFX(A):
    t = lambda p, a=0: A(p, a)
    return [[t('grafiğine') , 'impact', -8, 1, 'hook'], [t('Çünkü') + .3, 'stamp', -9, 1, 'date'], [t('Ürünlerde'), 'impact', -8, 1, '10gün'],
            [t('yükseltirse'), 'marker', -11, 0, 'jump'], [t('Örnek') + .3, 'whoosh_hollow', -12, 0, 'card'], [t('1.500') , 'pop', -10, 0, 'up'],
            [t('%33'), 'stamp', -8, 1, 'badge'], [t('aynı'), 'impact', -7, 1, 'same'], [t('249 milyon liradan'), 'gears', -11, 0, 'count'],
            [t("%75'e"), 'stamp', -9, 1, '75'], [t('Almak') + .2, 'ui_click', -11, 0, 'c1'], [t('Sepete') + .2, 'ui_click', -11, 0, 'c2'],
            [t('Kampanyadan') + .2, 'ui_click', -11, 0, 'c3'], [t('Kaydet') + .1, 'success', -10, 1, 'kaydet']]
def RISERS(A): return [[A('Yani', A('Eskiden')), 'sharp', -9], [A('Reklam'), 'metallic', -9]]
SCENE_HTML = r'''
  <section id="s1" class="scene clip">
    <div class="a ghost" id="s1g" data-layout-allow-overflow data-layout-allow-occlusion style="left:-30px;top:-70px">%50</div>
    <div class="a h" id="s1a" style="left:0;right:0;top:1330px;text-align:center;font-size:84px"><span id="s1x" style="position:relative;display:inline-block">İNDİRİME<span id="s1s" style="position:absolute;left:-6px;right:-6px;top:46%;height:9px;background:#ff4a3d;transform-origin:0 50%"></span></span> DEĞİL</div>
    <div class="a h gold" id="s1b" style="left:0;right:0;top:1330px;text-align:center;font-size:84px">GRAFİĞE BAK ↗</div>
  </section>
  <section id="s2" class="scene clip">
    <div class="a card" id="s2c" style="left:60px;top:300px;width:380px;padding:0;overflow:hidden;text-align:center">
      <div style="background:#ff4a3d;padding:14px;font:700 30px 'IBM Plex Mono';color:#0d0c0a;letter-spacing:.18em">2026</div>
      <div class="big" style="font-size:220px;padding-top:20px">1</div>
      <div class="lab" style="padding:10px 0 30px;font-size:34px">AĞUSTOS</div>
    </div>
    <div class="a h" id="s2h" style="left:60px;top:830px;font-size:88px">KURAL</div>
    <div class="a h gold" id="s2h2" style="left:60px;top:925px;font-size:88px">DEĞİŞTİ</div>
    <div class="a mono" id="s2m" style="left:60px;top:1040px">indirimli satış · ürünler</div>
  </section>
  <section id="s3" class="scene clip">
    <div class="a h gold" id="s3h" style="left:400px;top:290px;font-size:60px">REFERANS FİYAT</div>
    <div class="a mono" id="s3m" style="left:400px;top:370px">indirimden önceki</div>
    <div class="a mono" id="s3m2" style="left:400px;top:412px">en düşük fiyat</div>
    <div class="a big" id="s3a" style="left:52px;top:620px;font-size:200px;color:rgba(243,239,230,.9)"><span id="s3w" style="position:relative;display:inline-block">30 GÜN<span id="s3s" style="position:absolute;left:-8px;right:-8px;top:46%;height:14px;background:#ff4a3d;transform-origin:0 50%"></span></span></div>
    <div class="a big gold" id="s3b" style="left:52px;top:840px;font-size:200px">10 GÜN</div>
    <div class="a" id="s3strip" style="left:60px;top:1110px;width:900px;height:70px"></div>
    <div class="a mono" id="s3sl" style="left:60px;top:1200px">← 30 gün önce</div>
    <div class="a mono gold" id="s3sr" style="left:620px;top:1200px">indirim başlar ↓</div>
  </section>
  <section id="s4" class="scene clip">
    <div class="a h" id="s4h" style="left:60px;top:280px">FİYAT OYUNU</div>
    <div class="a mono" id="s4m" style="left:60px;top:365px">kampanyadan 11 gün önce zam</div>
    <svg class="a" id="s4svg" style="left:40px;top:430px" width="820" height="620" viewBox="0 0 820 620"></svg>
  </section>
  <section id="s5" class="scene clip">
    <div class="a card" id="s5c" style="left:60px;top:290px;width:510px;height:1110px"></div>
    <svg class="a" id="s5i" style="left:110px;top:330px" width="150" height="150" viewBox="0 0 100 100"><path d="M18 58 V48 a32 32 0 0 1 64 0 V58" fill="none" stroke="#f3efe6" stroke-width="7" stroke-linecap="round"/><rect x="10" y="54" width="20" height="32" rx="7" fill="#e8b931"/><rect x="70" y="54" width="20" height="32" rx="7" fill="#e8b931"/></svg>
    <div class="a h" id="s5t" style="left:280px;top:370px;font-size:56px">KULAKLIK</div>
    <div class="a mono" id="s5t2" style="left:280px;top:440px">örnek ürün</div>
    <div class="a mono" id="s5r1" style="left:100px;top:560px">EKİM</div><div class="a big" id="s5v1" style="left:96px;top:600px;font-size:96px">1.000 ₺</div>
    <div class="a mono" id="s5r2" style="left:100px;top:740px">KASIM BAŞI</div><div class="a big red" id="s5v2" style="left:96px;top:780px;font-size:96px">1.500 ₺ ↑</div>
    <div class="a mono gold" id="s5r3" style="left:100px;top:920px">EFSANE CUMA</div>
    <div class="a big" id="s5v3o" style="left:96px;top:960px;font-size:60px;color:rgba(243,239,230,.55)"><span style="text-decoration:line-through;text-decoration-color:#ff4a3d;text-decoration-thickness:6px">1.500 ₺</span></div>
    <div class="a big gold" id="s5v3" style="left:96px;top:1030px;font-size:110px">1.000 ₺</div>
    <div class="a h" id="s5b" style="left:360px;top:960px;font-size:44px;background:#ff4a3d;color:#0d0c0a;padding:8px 18px;border-radius:40px">%33 ↓</div>
    <div class="a h red" id="s5s" style="left:96px;top:1190px;font-size:72px;border:6px solid #ff4a3d;padding:8px 20px;border-radius:16px">AYNI FİYAT</div>
  </section>
  <section id="s6" class="scene clip">
    <div class="a lab" id="s6l" style="left:60px;top:600px">REKLAM KURULU · 2026 · İLK 9 AY</div>
    <div class="a big gold" id="s6v" style="left:52px;top:650px;font-size:300px">0</div>
    <div class="a h" id="s6u" style="left:60px;top:930px;font-size:96px">MİLYON ₺+ CEZA</div>
    <div class="a mono" id="s6m" style="left:60px;top:1040px">yanıltıcı reklamlara</div>
    <div class="a card" id="s6c" style="left:60px;top:1130px;width:900px;border-color:#ff4a3d"><span class="h red" style="font-size:72px">%75'e varan</span><span class="mono" style="margin-left:20px">gerçek dışı indirim</span></div>
  </section>
  <section id="s7" class="scene clip">
    <div class="a lab" id="s7l" style="left:60px;top:300px">ALMADAN ÖNCE</div>
    <div class="a" id="s7r0" style="left:60px;top:370px;width:510px;display:flex;gap:22px;align-items:center"><div class="tick" id="s7k0"></div><div class="h" style="font-size:46px;white-space:normal;line-height:1.05">Bugünden takip et</div></div>
    <div class="a" id="s7r1" style="left:60px;top:500px;width:510px;display:flex;gap:22px;align-items:center"><div class="tick" id="s7k1"></div><div class="h" style="font-size:46px;white-space:normal;line-height:1.05">Son 3 ayın grafiği</div></div>
    <div class="a" id="s7r2" style="left:60px;top:630px;width:510px;display:flex;gap:22px;align-items:center"><div class="tick" id="s7k2"></div><div class="h" style="font-size:46px;white-space:normal;line-height:1.05">Zıplama = <span class="red">indirim değil</span></div></div>
    <svg class="a" id="s7svg" style="left:60px;top:820px" width="510" height="420" viewBox="0 0 510 420"></svg>
  </section>
  <section id="s8" class="scene clip">
    <svg class="a" id="s8i" style="left:250px;top:1316px" width="96" height="120" viewBox="0 0 96 120"><path d="M8 6h80v108L48 86 8 114z" fill="#e8b931"/></svg>
    <div class="a h gold" id="s8t" style="left:370px;top:1320px;font-size:118px">KAYDET</div>
  </section>
  <section id="s9" class="scene clip">
    <div class="a h" id="s9a" style="left:0;right:0;top:1330px;text-align:center;font-size:64px">İNDİRİME DEĞİL, <span class="gold">GRAFİĞE BAK</span></div>
  </section>
'''
SCENE_JS = r'''
// S1
tl.fromTo('#s1g',{x:0},{x:-260,duration:st('s2'),ease:'none'},0);
inn('#s1a',.3); tl.fromTo('#s1s',{scaleX:0},{scaleX:1,duration:.35,ease:'power3.out'},1.0); out('#s1a',1.9); inn('#s1b',2.15,{s:1.15});
// S2
const s2=st('s2'); inn('#s2c',s2+.1,{y:80}); inn('#s2h',s2+.7); inn('#s2h2',s2+.9); inn('#s2m',s2+1.3,{y:16});
// S3
const s3=st('s3'); inn('#s3h',s3+.1); inn('#s3m',s3+.3); inn('#s3m2',s3+.4); inn('#s3a',s3+.3); inn('#s3strip',s3+.5,{y:0}); inn('#s3sl',s3+.6,{y:0}); inn('#s3sr',s3+.6,{y:0});
(function(){const b=$('#s3strip');for(let i=0;i<30;i++){const c=document.createElement('div');c.id='s3c'+i;Object.assign(c.style,{position:'absolute',left:(i*30)+'px',top:'0',width:'24px',height:'70px',borderRadius:'6px',background:'rgba(243,239,230,.35)'});b.appendChild(c);}})();
const t10=st('s4')-st('s3'); const tU=Math.max(1.4, t10*0.62);
tl.fromTo('#s3s',{scaleX:0},{scaleX:1,duration:.35,ease:'power3.out'},s3+tU-.2); slam('#s3b',s3+tU);
for(let i=0;i<30;i++){ if(i<20) tl.to('#s3c'+i,{opacity:.12,duration:.25},s3+tU+.05+i*.01); else tl.to('#s3c'+i,{backgroundColor:'#e8b931',duration:.25},s3+tU+.1+(i-20)*.03); }
// S4 price timeline
const s4=st('s4'); inn('#s4h',s4+.1); inn('#s4m',s4+.3); inn('#s4svg',s4+.35,{y:20});
(function(){const svg=$('#s4svg');const D=26;const X=d=>40+d*(740/D);const Y=v=>520-(v-800)/(1700-800)*420;
 let p='';for(let d=0;d<=D;d++){const v=d<15?1000:1500;p+=(d?'L':'M')+X(d)+','+Y(v);}
 let g=`<line x1="40" x2="780" y1="${Y(1000)}" y2="${Y(1000)}" stroke="rgba(243,239,230,.12)" stroke-width="2"/><line x1="40" x2="780" y1="${Y(1500)}" y2="${Y(1500)}" stroke="rgba(243,239,230,.12)" stroke-width="2"/>`;
 g+=`<text x="40" y="${Y(1000)+44}" font-family="IBM Plex Mono" font-size="26" fill="rgba(243,239,230,.75)">1.000 ₺</text><text x="40" y="${Y(1500)-18}" font-family="IBM Plex Mono" font-size="26" fill="#ff4a3d">1.500 ₺</text>`;
 g+=`<rect id="s4win" x="${X(16)}" y="40" width="${X(26)-X(16)}" height="${Y(800)-40}" fill="rgba(232,185,49,.14)" stroke="#e8b931" stroke-width="3" stroke-dasharray="10 8" rx="10"/>`;
 g+=`<text id="s4wt" x="${(X(16)+X(26))/2}" y="30" text-anchor="middle" font-family="IBM Plex Mono" font-weight="700" font-size="24" fill="#e8b931">SON 10 GÜN</text>`;
 g+=`<path id="s4p" d="${p}" fill="none" stroke="#f3efe6" stroke-width="8" stroke-linejoin="round"/>`;
 g+=`<g id="s4z"><circle cx="${X(15)}" cy="${Y(1500)}" r="16" fill="#ff4a3d"/><text x="${X(15)-20}" y="${Y(1500)-34}" text-anchor="end" font-family="Inter Tight" font-weight="800" font-size="34" fill="#ff4a3d">ZAM · 11 GÜN ÖNCE</text></g>`;
 g+=`<g id="s4e"><rect x="${X(16)+20}" y="${Y(1500)+30}" width="300" height="56" rx="12" fill="#e8b931"/><text x="${X(16)+170}" y="${Y(1500)+68}" text-anchor="middle" font-family="Inter Tight" font-weight="800" font-size="30" fill="#0d0c0a">YENİ "ESKİ FİYAT"</text></g>`;
 g+=`<text x="${X(26)}" y="${Y(800)+40}" text-anchor="end" font-family="IBM Plex Mono" font-size="24" fill="rgba(243,239,230,.75)">KAMPANYA</text>`;
 svg.innerHTML=g;const path=$('#s4p');const L=path.getTotalLength();path.style.strokeDasharray=L;
 const d=st('s5')-s4;tl.fromTo(path,{strokeDashoffset:L},{strokeDashoffset:0,duration:Math.min(2.2,d*.4),ease:'power1.inOut'},s4+.5);
 tl.fromTo('#s4z',{opacity:0},{opacity:1,duration:.25},s4+Math.min(1.6,d*.3)); tl.fromTo(['#s4win','#s4wt'],{opacity:0},{opacity:1,duration:.3},s4+Math.min(2.6,d*.5)); tl.fromTo('#s4e',{opacity:0,y:20},{opacity:1,y:0,duration:.3},s4+Math.min(3.4,d*.7));})();
// S5 product card
const s5=st('s5'), d5=st('s6')-s5; inn('#s5c',s5+.05,{y:60}); inn('#s5i',s5+.2,{s:.8}); inn('#s5t',s5+.3); inn('#s5t2',s5+.4);
inn('#s5r1',s5+.5); inn('#s5v1',s5+.55); inn('#s5r2',s5+d5*.22); inn('#s5v2',s5+d5*.24,{s:1.1});
inn('#s5r3',s5+d5*.42); inn('#s5v3o',s5+d5*.44); slam('#s5v3',s5+d5*.47); slam('#s5b',s5+d5*.6); slam('#s5s',s5+d5*.82);
// S6 fines
const s6=st('s6'), d6=st('s7')-s6; inn('#s6l',s6+.45); inn('#s6v',s6+.5); count('#s6v',0,249,s6+.6,1.5); inn('#s6u',s6+1.2); inn('#s6m',s6+1.4,{y:16}); inn('#s6c',s6+d6*.62,{y:50});
// S7 checklist + jump chart
const s7=st('s7'), d7=st('s8')-s7; inn('#s7l',s7+.05);
[[0,.05],[1,.36],[2,.68]].forEach(([i,f])=>{inn('#s7r'+i,s7+d7*f+.05,{y:24}); tl.to('#s7k'+i,{backgroundColor:'#e8b931',duration:.15},s7+d7*f+.45);});
(function(){const svg=$('#s7svg');const V=[1010,990,1020,1000,980,1005,995,1000,1010,1490,1500,1495,1000];const X=i=>30+i*(450/12);const Y=v=>360-(v-900)/(1600-900)*300;
 let p='';V.forEach((v,i)=>{p+=(i?'L':'M')+X(i)+','+Y(v);});
 svg.innerHTML=`<rect x="0" y="0" width="510" height="420" rx="28" fill="rgba(243,239,230,.04)" stroke="rgba(243,239,230,.12)" stroke-width="3"/><text x="30" y="52" font-family="IBM Plex Mono" font-weight="700" font-size="24" fill="#e8b931">FİYAT · SON 3 AY</text><path id="s7p" d="${p}" fill="none" stroke="#f3efe6" stroke-width="7" stroke-linejoin="round"/><ellipse id="s7o" cx="${X(9.5)}" cy="${Y(1495)}" rx="70" ry="44" fill="none" stroke="#ff4a3d" stroke-width="6"/>`;
 const path=$('#s7p');const L=path.getTotalLength();path.style.strokeDasharray=L;
 inn('#s7svg',s7+d7*.36,{y:30}); tl.fromTo(path,{strokeDashoffset:L},{strokeDashoffset:0,duration:1.4,ease:'power1.inOut'},s7+d7*.36+.2);
 tl.fromTo('#s7o',{opacity:0,scale:1.6,transformOrigin:'50% 50%'},{opacity:1,scale:1,duration:.3,ease:'power3.out'},s7+d7*.7);})();
// S8 CTA
const s8=st('s8'); tl.fromTo('#s8i',{opacity:0,y:-80},{opacity:1,y:0,duration:.4,ease:'bounce.out'},s8+.1); slam('#s8t',s8+.2);
// S9 loop
const s9=st('s9'); inn('#s9a',s9+.2);
'''
