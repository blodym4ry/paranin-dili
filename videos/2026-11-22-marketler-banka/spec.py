import os
# Kinetik stili (son üretim Gazete idi). Ayrık yöntem: avatar s1 (kanca), s7 (ara kanca), s10-s11 (kapanış + CTA/döngü).
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [
    (N('on', 'milyar', 'lira'), '10 milyar lira'), (N('üç', 'kalemde'), '3 kalemde'), (N('a', 'yüz', 'birin'), "A101'in"),
    (N('a', 'yüz', 'bir'), 'A101'), (N('dokuz', 'ayda'), '9 ayda'), (N('dokuz', 'yüz', 'yetmiş', 'beş', 'bin'), '975 bin'),
    (N('beş', 'buçuk', 'milyon'), '5,5 milyon'), (N('yüzde', 'altmış', 'beşi', 'ile', 'yetmişi'), "%65-70'i"),
    (N('iki', 'bin', 'yirmi', 'dört'), '2024'), (N('dört', 'buçuk', 'milyar', 'lira'), '4,5 milyar lira'),
    (N('eylülde',), "Eylül'de"),
]
EM = {'reklam', 'sermaye', 'kuruluş', 'tescil', 'kalem', 'müşteri', 'nakit', 'ödeme', 'komisyon', 'kasada', 'kaydet', 'kasanın', 'tom', 'fon'}
RED = {'reklam', 'komisyon', 'değil'}
FRONT = [250, 300, 580, 815, 24]          # 740:1040 portre — saç ve çene görünür
BIG = [170, 330, 740, 1040, 28]
AV = {'s1': FRONT, 's2': None, 's3': None, 's4': None, 's5': None, 's6': None, 's7': BIG, 's8': None, 's9': None,
      's10': [600, 300, 420, 590, 22], 's11': FRONT}


def scenes(A):
    b = lambda t: round(t - .1, 3)
    t2 = A('Haziranda'); t3 = A('Sonunda'); t4 = A('Bu', 15); t5 = A('Birinci'); t6 = A('Genel'); t7 = A('Ama', 32)
    t8 = min(b(A('İkinci', 34)), 34.35)   # ara kanca avatar parçası 34.36'da bitiyor
    t9 = A('Üçüncü', 42); t10 = A('Market', 51); t11 = A('Kaydet')
    return [('s1', 0, b(t2)), ('s2', b(t2), b(t3)), ('s3', b(t3), b(t4)), ('s4', b(t4), b(t5)), ('s5', b(t5), b(t6)),
            ('s6', b(t6), b(t7)), ('s7', b(t7), t8), ('s8', t8, b(t9)), ('s9', b(t9), b(t10)), ('s10', b(t10), b(t11)),
            ('s11', b(t11), DUR)]


def SFX(A):
    return [[A('reklam'), 'stamp', -10, 1, 'hook'], [A('10 milyar lira'), 'impact', -8, 1, '10mlr'],
            [A('Haziranda') + .4, 'paper_drop', -10, 0, 'haz'], [A("Eylül'de") + .1, 'stamp', -10, 0, 'eyl'],
            [A('3 kalemde'), 'pop', -10, 0, '3'], [A('975 bin'), 'gears', -12, 0, 'count'], [A('Birinci'), 'whoosh_hollow', -12, 0, 'k1'],
            [A('5,5 milyon'), 'impact', -8, 1, 'fis'], [A("%65-70'i"), 'stamp', -9, 1, 'pct'], [A('İkinci', 34), 'whoosh_hollow', -12, 0, 'k2'],
            [A('4,5 milyar lira'), 'impact', -8, 1, 'fon'], [A('Üçüncü', 42), 'whoosh_hollow', -12, 0, 'k3'],
            [A('komisyon'), 'ui_click', -11, 0, 'kom'], [A('grupta'), 'success', -11, 0, 'kalir'], [A('Kaydet') + .1, 'success', -10, 1, 'kaydet'],
            [A('kasanın'), 'impact', -9, 1, 'loop']]


def RISERS(A): return [[A('Ama', 32) - .5, 'sharp', -9], [A('Üçüncü', 42) - .4, 'metallic', -10]]


SCENE_HTML = r'''
  <section id="s1" class="scene clip">
    <div class="a h" id="s1a" style="left:0;right:0;top:1150px;text-align:center;font-size:96px"><span id="s1x" style="position:relative;display:inline-block">REKLAM?<span id="s1s" style="position:absolute;left:-8px;right:-8px;top:46%;height:12px;background:#ff4a3d;transform-origin:0 50%"></span></span></div>
    <div class="a" id="s1b" style="left:0;right:0;top:1150px;text-align:center"><span class="big gold" style="font-size:150px">10 MİLYAR ₺</span></div>
    <div class="a mono" id="s1m" style="left:0;right:0;top:1300px;text-align:center">BİM · banka sermayesi</div>
  </section>
  <section id="s2" class="scene clip">
    <div class="a lab" id="s2l" style="left:60px;top:330px">DOST KATILIM BANKASI · 2026</div>
    <div class="a" id="s2line" style="left:118px;top:430px;width:6px;height:780px;background:rgba(243,239,230,.18);transform-origin:50% 0"></div>
    <div class="a" id="s2r0" style="left:90px;top:440px;display:flex;gap:40px;align-items:flex-start"><div class="dot" id="s2d0"></div><div><div class="mono">11 HAZİRAN</div><div class="h" style="font-size:78px;margin-top:10px">BDDK kuruluş izni</div></div></div>
    <div class="a" id="s2r1" style="left:90px;top:720px;display:flex;gap:40px;align-items:flex-start"><div class="dot" id="s2d1"></div><div><div class="mono">16 EYLÜL</div><div class="h" style="font-size:78px;margin-top:10px">Tescil edildi</div></div></div>
    <div class="a" id="s2r2" style="left:90px;top:1000px;display:flex;gap:40px;align-items:flex-start"><div class="dot" id="s2d2" style="background:transparent"></div><div><div class="mono">SIRADA</div><div class="h gold" style="font-size:78px;margin-top:10px">Faaliyet izni</div></div></div>
  </section>
  <section id="s3" class="scene clip">
    <div class="a lab" id="s3l" style="left:60px;top:420px">MARKET BANKADAN NE KAZANIR?</div>
    <div class="a big" id="s3n" style="left:52px;top:480px;font-size:300px">3</div>
    <div class="a h" id="s3k" style="left:290px;top:560px;font-size:110px">KALEM</div>
    <div class="a" id="s3row" style="left:60px;top:860px;width:960px;display:flex;gap:30px">
      <div class="card q" id="s3q0">?</div><div class="card q" id="s3q1">?</div><div class="card q" id="s3q2" style="border-color:#e8b931">💳</div></div>
    <div class="a mono gold" id="s3m" style="left:700px;top:1150px">her kart uzattığında</div>
  </section>
  <section id="s4" class="scene clip">
    <div class="a lab" id="s4l" style="left:60px;top:400px">ÖNCE BU YOLU YÜRÜDÜLER</div>
    <div class="a h" id="s4h" style="left:60px;top:460px;font-size:96px">TOM Bank</div>
    <div class="a mono" id="s4m" style="left:60px;top:565px">A101'in patronlarının bankası</div>
    <div class="a big gold" id="s4v" style="left:52px;top:710px;font-size:210px">0</div>
    <div class="a h" id="s4u" style="left:60px;top:950px;font-size:84px">MÜŞTERİ</div>
    <div class="a card" id="s4c" style="left:600px;top:945px;padding:18px 30px"><span class="h" style="font-size:64px">9 AYDA</span></div>
    <div class="a mono" id="s4s" style="left:60px;top:1080px">Forbes Türkiye · Ocak 2025</div>
  </section>
  <section id="s5" class="scene clip">
    <div class="a ghost" id="s5g" data-layout-allow-overflow data-layout-allow-occlusion data-layout-allow-overlap style="left:40px;top:1020px">FİŞ</div>
    <div class="a lab" id="s5l" style="left:60px;top:380px">KALEM 1</div>
    <div class="a h" id="s5h" style="left:60px;top:430px;font-size:120px">MÜŞTERİ</div>
    <div class="a" id="s5rc" style="left:640px;top:580px;width:340px;height:520px;background:#f3efe6;border-radius:10px;padding:30px 30px;transform-origin:50% 0">
      <div style="font:700 26px 'IBM Plex Mono';color:#0d0c0a;text-align:center">— FİŞ —</div>
      <div style="margin-top:24px;height:14px;background:rgba(13,12,10,.18);border-radius:4px"></div><div style="margin-top:20px;height:14px;width:70%;background:rgba(13,12,10,.18);border-radius:4px"></div>
      <div style="margin-top:20px;height:14px;width:85%;background:rgba(13,12,10,.18);border-radius:4px"></div><div style="margin-top:20px;height:14px;width:60%;background:rgba(13,12,10,.18);border-radius:4px"></div>
      <div style="margin-top:40px;height:4px;background:#0d0c0a"></div><div style="margin-top:20px;font:800 40px 'Inter Tight';color:#0d0c0a;text-align:right">TOPLAM</div></div>
    <div class="a big gold" id="s5v" style="left:52px;top:640px;font-size:190px">5,5</div>
    <div class="a h" id="s5u" style="left:60px;top:830px;font-size:72px">milyon fiş</div>
    <div class="a h gold" id="s5d" style="left:60px;top:915px;font-size:72px">her gün</div>
    <div class="a mono" id="s5m" style="left:60px;top:1030px">grubun şirketleri toplamı</div>
  </section>
  <section id="s6" class="scene clip">
    <div class="a lab" id="s6l" style="left:60px;top:380px">KASA = ŞUBE</div>
    <svg class="a" id="s6svg" style="left:290px;top:440px" width="500" height="500" viewBox="0 0 500 500"></svg>
    <div class="a big" id="s6v" style="left:0;right:0;top:635px;text-align:center;font-size:104px">%65-70</div>
    <div class="a h" id="s6h" style="left:0;right:0;top:990px;text-align:center;font-size:66px">A101 kasasından <span class="gold">para çekiyor</span></div>
    <div class="a mono" id="s6m" style="left:0;right:0;top:1080px;text-align:center">TOM müşterileri · genel müdür beyanı, Şubat 2025</div>
  </section>
  <section id="s7" class="scene clip">
    <div class="a h gold" id="s7h" style="left:0;right:0;top:1395px;text-align:center;font-size:80px">ASIL HESAP →</div>
  </section>
  <section id="s8" class="scene clip">
    <div class="a lab" id="s8l" style="left:60px;top:380px">KALEM 2</div>
    <div class="a h" id="s8h" style="left:60px;top:430px;font-size:120px">NAKİT</div>
    <div class="a card" id="s8a" style="left:60px;top:620px;width:330px;text-align:center;padding:30px 10px"><div class="mono">SEN</div><div style="font-size:90px;margin-top:10px">👤</div></div>
    <div class="a card" id="s8b" style="left:690px;top:620px;width:330px;text-align:center;padding:30px 10px;border-color:#e8b931"><div class="mono gold">BANKA</div><div style="font-size:90px;margin-top:10px">🏦</div></div>
    <svg class="a" id="s8svg" style="left:400px;top:690px" width="280" height="90" viewBox="0 0 280 90"><path d="M10 45 H250" stroke="#e8b931" stroke-width="8"/><path d="M228 20 L262 45 L228 70" fill="none" stroke="#e8b931" stroke-width="8"/>
      <circle id="m0" cx="20" cy="45" r="13" fill="#f3efe6"/><circle id="m1" cx="20" cy="45" r="13" fill="#f3efe6"/><circle id="m2" cx="20" cy="45" r="13" fill="#f3efe6"/></svg>
    <div class="a mono" id="s8m" style="left:60px;top:880px">yatırdığın para = bankanın fonu</div>
    <div class="a big gold" id="s8v" style="left:52px;top:970px;font-size:130px">4,5 MİLYAR ₺</div>
    <div class="a mono" id="s8s" style="left:60px;top:1130px">TOM · 2024 sonu toplanan fon</div>
  </section>
  <section id="s9" class="scene clip">
    <div class="a lab" id="s9l" style="left:60px;top:380px">KALEM 3</div>
    <div class="a h" id="s9h" style="left:60px;top:430px;font-size:120px">ÖDEME</div>
    <div class="a" id="s9card" style="left:60px;top:640px;width:400px;height:250px;border-radius:26px;background:linear-gradient(135deg,#e8b931,#b8860b);padding:30px">
      <div style="width:70px;height:52px;border-radius:10px;background:rgba(13,12,10,.35)"></div><div style="margin-top:70px;font:700 30px 'IBM Plex Mono';color:#0d0c0a;letter-spacing:.12em">•••• 2026</div></div>
    <div class="a card" id="s9o" style="left:560px;top:600px;width:460px;padding:24px 28px"><div class="mono">DIŞ BANKA</div><div class="h red" style="font-size:58px;margin-top:8px">komisyon gider</div></div>
    <div class="a card" id="s9i" style="left:560px;top:790px;width:460px;padding:24px 28px;border-color:#3ddc84"><div class="mono">GRUBUN BANKASI</div><div class="h green" style="font-size:58px;margin-top:8px">pay içeride kalır</div></div>
    <div class="a mono" id="s9m" style="left:60px;top:960px">kartlı ödemede işyeri bankaya komisyon öder</div>
  </section>
  <section id="s10" class="scene clip">
    <div class="a" id="s10r0" style="left:60px;top:380px;display:flex;gap:22px;align-items:center"><div class="tick" id="s10k0"></div><div class="h" style="font-size:66px">Müşteri</div></div>
    <div class="a" id="s10r1" style="left:60px;top:520px;display:flex;gap:22px;align-items:center"><div class="tick" id="s10k1"></div><div class="h" style="font-size:66px">Nakit</div></div>
    <div class="a" id="s10r2" style="left:60px;top:660px;display:flex;gap:22px;align-items:center"><div class="tick" id="s10k2"></div><div class="h" style="font-size:66px">Komisyon</div></div>
    <div class="a h gold" id="s10t" style="left:60px;top:830px;font-size:96px">= KASA</div>
  </section>
  <section id="s11" class="scene clip">
    <svg class="a" id="s11i" style="left:250px;top:1150px" width="96" height="120" viewBox="0 0 96 120"><path d="M8 6h80v108L48 86 8 114z" fill="#e8b931"/></svg>
    <div class="a h gold" id="s11t" style="left:370px;top:1160px;font-size:118px">KAYDET</div>
    <div class="a h" id="s11a" style="left:0;right:0;top:1150px;text-align:center;font-size:70px"><span class="red">REKLAM DEĞİL,</span> KASA</div>
  </section>
'''

EXTRA_CSS = r'''<style>
.dot{width:62px;height:62px;border-radius:50%;background:#e8b931;border:6px solid #e8b931;flex:none;margin-top:10px}
.q{flex:1;height:240px;display:flex;align-items:center;justify-content:center;font:900 130px 'Inter Tight';color:rgba(243,239,230,.55)}
</style>'''

SCENE_JS = r'''
const at=(p,after=0)=>{for(const c of CAPS)for(const w of c.w)if(w[1]>=after&&w[0].toLowerCase().startsWith(p.toLowerCase()))return w[1];return null;};
// S1 kanca
inn('#s1a',.3,{s:1.1}); tl.fromTo('#s1s',{scaleX:0},{scaleX:1,duration:.3,ease:'power3.out'},at('ama')-.1); out('#s1a',at('ama')+.25);
slam('#s1b',at('10')); inn('#s1m',at('sermaye'),{y:14});
// S2 zaman çizelgesi
const s2=st('s2'); inn('#s2l',s2+.4); tl.fromTo('#s2line',{scaleY:0},{scaleY:1,duration:2.6,ease:'none'},s2+.4);
inn('#s2r0',s2+.45,{y:20}); inn('#s2r1',at("Eylül")-.05,{y:20}); inn('#s2r2',at('edildi')+.15,{y:20});
// S3 üç kalem
const s3=st('s3'); inn('#s3l',s3+.4); slam('#s3n',at('3')); inn('#s3k',at('3')+.15);
[0,1,2].forEach(i=>inn('#s3q'+i,at('3')+.4+i*.18,{y:50})); tl.to('#s3q2',{scale:1.08,duration:.3,yoyo:true,repeat:1},at('üçüncüsü')); inn('#s3m',at('kart'),{y:10});
// S4 TOM
const s4=st('s4'); inn('#s4l',s4+.4); inn('#s4h',s4+.5); inn('#s4m',s4+.75,{y:10}); tl.to('#s4h',{color:'#e8b931',duration:.2},at('TOM')); inn('#s4v',at('9 ayda')-.1);
count('#s4v',0,975000,at('9 ayda'),at('müşteriye')-at('9 ayda'),fmt); inn('#s4u',at('müşteriye')); slam('#s4c',at('9 ayda')); inn('#s4s',at('ulaştı'),{y:10});
// S5 fiş
const s5=st('s5'); tl.fromTo('#s5g',{x:0},{x:-200,duration:st('s6')-s5,ease:'none'},s5); inn('#s5l',s5+.4); inn('#s5h',s5+.45);
tl.fromTo('#s5rc',{opacity:0,scaleY:0},{opacity:1,scaleY:1,duration:.6,ease:'power2.out'},at('Grubun')); slam('#s5v',at('5,5'));
inn('#s5u',at('fiş')); inn('#s5d',at('kesiyor')); inn('#s5m',at('kesiyor')+.3,{y:10});
// S6 halka %65-70
const s6=st('s6'); inn('#s6l',s6+.4);
(function(){const svg=$('#s6svg');const R=210,C=2*Math.PI*R;svg.innerHTML=`<circle cx="250" cy="250" r="${R}" fill="none" stroke="rgba(243,239,230,.12)" stroke-width="40"/><circle id="s6arc" cx="250" cy="250" r="${R}" fill="none" stroke="#e8b931" stroke-width="40" stroke-linecap="round" transform="rotate(-90 250 250)" stroke-dasharray="${C}" stroke-dashoffset="${C}"/>`;
 inn('#s6svg',s6+.45,{y:0,s:.9}); tl.to('#s6arc',{attr:{'stroke-dashoffset':C*(1-.675)},duration:1.2,ease:'power2.out'},at('%65')-.1);})();
slam('#s6v',at('%65')); inn('#s6h',at('A101',29)); inn('#s6m',at('çekiyor'),{y:10});
// S7 ara kanca
inn('#s7h',st('s7')+.4,{y:20});
// S8 nakit
const s8=st('s8'); inn('#s8l',s8+.4); inn('#s8h',s8+.45); inn('#s8a',at('banka',35)); inn('#s8b',at('banka',35)+.2); inn('#s8svg',at('müşterisinin'),{y:0});
[0,1,2].forEach(i=>tl.fromTo('#m'+i,{attr:{cx:20},opacity:1},{attr:{cx:230},opacity:0,duration:.8,ease:'power1.in',repeat:2},at('yatırdığı')+i*.27));
inn('#s8m',at('fonlanır'),{y:10}); slam('#s8v',at('4,5')); inn('#s8s',at('topladı'),{y:10});
// S9 ödeme
const s9=st('s9'); inn('#s9l',s9+.4); inn('#s9h',s9+.45); tl.fromTo('#s9card',{opacity:0,x:-120,rotation:-8},{opacity:1,x:0,rotation:0,duration:.5,ease:'expo.out'},at('Kartla'));
inn('#s9o',at('bankaya'),{y:30}); inn('#s9m',at('komisyon')+.3,{y:10}); inn('#s9i',at('kendisininse'),{y:30}); tl.to('#s9o',{opacity:.35,duration:.4},at('grupta'));
// S10 kapanış
const s10=st('s10'); [['müşteriyi',0],['nakdi',1],['komisyonu',2]].forEach(([p,i])=>{const t=at(p,51); inn('#s10r'+i,t-.1,{y:24}); tl.to('#s10k'+i,{backgroundColor:'#e8b931',duration:.15},t+.25);});
slam('#s10t',at('kasada'));
// S11 CTA + döngü
const s11=st('s11'); tl.fromTo('#s11i',{opacity:0,y:-80},{opacity:1,y:0,duration:.4,ease:'bounce.out'},s11+.1); slam('#s11t',s11+.2);
out(['#s11i','#s11t'],at('reklam',57)-.25); slam('#s11a',at('reklam',57));
'''
