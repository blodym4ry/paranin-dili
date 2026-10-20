import os
# Kinetik stili (verilen; önceki video Gazete). Ayrık yöntem: avatar s1 (kanca), s5 (ara kanca, köşe pencere), s13-s15 (kapanış + CTA + döngü).
# Dini hüküm yok: sadece mekanizma + tarihli oranlar.
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [
    (N('yüzde', 'otuz', 'bir', 'ile', 'otuz', 'sekiz'), '%31–38'), (N('yüzde', 'otuz', 'altı', 'ile', 'kırk'), '%36–40'),
    (N('bir', 'aylık'), '1 aylık'), (N('iki', 'banka'), '2 banka'),
]
EM = {'tesadüf', 'havuza', 'havuzun', 'gösterge', 'taahhüt', 'benzerlik', 'piyasa', 'yarışır', 'kaydet', 'birlikte', 'bant'}
RED = {'garanti', 'tesadüf'}
MID = [250, 330, 580, 815, 24]          # 740:1040 portre
CORNER = [600, 300, 420, 590, 20]       # köşe, aynı oran
AV = {'s1': MID, 's2': None, 's3': None, 's4': None, 's5': CORNER, 's6': None, 's7': None, 's8': None, 's9': None,
      's10': None, 's11': None, 's12': None, 's13': MID, 's14': MID, 's15': MID}
EXTRA_CSS = '''<style>
.chip{display:inline-block;font:800 54px 'Inter Tight';padding:16px 28px;border-radius:60px;border:4px solid #e8b931;color:#f3efe6}
.node{position:absolute;left:60px;width:960px;height:140px;border-radius:24px;border:3px solid rgba(243,239,230,.18);background:rgba(243,239,230,.04);display:flex;align-items:center;padding:0 36px;font:900 58px 'Inter Tight';letter-spacing:-.03em}
.arr{position:absolute;left:510px;font:900 60px 'Inter Tight';color:#e8b931}
#s2,#s4,#s8,#s9{transform:translateY(120px)}
</style>'''


def scenes(A):
    b = lambda t: round(t - .1, 3)
    t2 = A('Bu'); t3 = A("Ekim'de"); t4 = A('Fark'); t5 = A('Peki'); t6 = A('Faizde'); t7 = A('Katılma'); t8 = A('İlan')
    t9 = A('Ama'); t10 = A('Havuzun', 38); t11 = A('Üstüne'); t12 = A('Merkez'); t13 = A('Mekanizma', 52); t14 = A('Hesap'); t15 = A('Çünkü')
    T = [0, b(t2), b(t3), b(t4), b(t5), b(t6), b(t7), b(t8), b(t9), b(t10), b(t11), b(t12), b(t13), b(t14), b(t15), DUR]
    return [(f's{i + 1}', T[i], T[i + 1]) for i in range(15)]


def SFX(A):
    return [[A('aynı?'), 'impact', -8, 1, 'hook'], [A('tesadüf'), 'stamp', -10, 0, 'tesaduf'], [A('Bu') + .3, 'whoosh_hollow', -12, 0, 'kilit'],
            [A('%31–38'), 'stamp', -9, 1, 'katilim'], [A('%36–40'), 'stamp', -9, 1, 'mevduat'], [A('bant'), 'impact', -9, 1, 'bant'],
            [A('taahhüt'), 'ui_click', -11, 0, 'lock'], [A('havuza'), 'paper_drop', -10, 0, 'pool'], [A('paylaşılır.'), 'pop', -10, 0, 'split'],
            [A('garanti'), 'stamp', -8, 1, 'garanti'], [A('finansmandan'), 'gears', -12, 0, 'chain'], [A('fiyatlanır.'), 'marker', -11, 0, 'price'],
            [A('yarışır.'), 'whoosh_hollow', -12, 0, 'race'], [A('birlikte', 50), 'pop', -10, 0, 'lines'], [A('kaydet.') + .05, 'success', -10, 1, 'kaydet'],
            [A('tesadüf', 60), 'impact', -8, 1, 'loop']]


def RISERS(A): return [[A('Peki') - .5, 'sharp', -9], [A('Ama') - .4, 'metallic', -10]]


SCENE_HTML = r'''
  <section id="s1" class="scene clip">
    <div class="a lab" id="s1l" style="left:0;right:0;top:255px;text-align:center">KATILIM BANKASI · MEVDUAT BANKASI</div>
    <div class="a h" id="s1a" style="left:0;right:0;top:1180px;text-align:center;font-size:96px">KÂR PAYI <span class="gold">≈</span> FAİZ<span class="gold">?</span></div>
  </section>
  <section id="s2" class="scene clip">
    <div class="a mono" id="s2n" style="left:60px;top:330px;font-size:30px">dini değerlendirme değil · sadece mekanizma</div>
    <div class="a lab" id="s2l" style="left:60px;top:420px">SONUNDA</div>
    <div class="a" id="s2c1" style="left:60px;top:480px"><span class="chip">① kâr payı nasıl hesaplanır</span></div>
    <div class="a" id="s2c2" style="left:60px;top:620px"><span class="chip" style="border-color:#3ddc84">② neden faizle birlikte</span></div>
  </section>
  <section id="s3" class="scene clip">
    <div class="a lab" id="s3l" style="left:60px;top:290px">EKİM 2026 · 1 AYLIK ORANLAR</div>
    <svg class="a" id="s3svg" style="left:60px;top:360px" width="960" height="820" viewBox="0 0 960 820">
      <g font-family="IBM Plex Mono" font-size="26" fill="rgba(243,239,230,.6)">
        <line x1="20" x2="940" y1="760" y2="760" stroke="rgba(243,239,230,.3)" stroke-width="3"/>
        <text x="20" y="800">%30</text><text x="320" y="800">%34</text><text x="620" y="800">%38</text><text x="860" y="800">%42</text></g>
      <text x="20" y="90" font-family="Inter Tight" font-weight="900" font-size="54" fill="#e8b931">KATILIM · KÂR PAYI</text>
      <rect id="s3r1" x="117" y="120" width="480" height="150" rx="75" fill="#e8b931"/>
      <text id="s3t1" x="357" y="218" text-anchor="middle" font-family="Inter Tight" font-weight="900" font-size="64" fill="#0d0c0a">%31,3 – 37,7</text>
      <text x="20" y="420" font-family="Inter Tight" font-weight="900" font-size="54" fill="#f3efe6">MEVDUAT · FAİZ</text>
      <rect id="s3r2" x="507" y="450" width="285" height="150" rx="75" fill="#f3efe6"/>
      <text id="s3t2" x="650" y="690" text-anchor="middle" font-family="Inter Tight" font-weight="900" font-size="60" fill="#f3efe6">%36,5 – 40,25</text>
      <rect id="s3band" x="507" y="100" width="90" height="520" fill="rgba(61,220,132,.16)" stroke="#3ddc84" stroke-width="3" stroke-dasharray="10 8"/></svg>
    <div class="a mono" id="s3m" style="left:60px;top:1230px;font-size:24px">katılım: 13 Eki · mevduat: büyük bankalar, 7 Eki · ilan edilen oranlar</div>
  </section>
  <section id="s4" class="scene clip">
    <div class="a lab" id="s4l" style="left:60px;top:430px">FARK</div>
    <div class="a big" id="s4a" style="left:52px;top:480px;font-size:170px">BİRKAÇ PUAN</div>
    <div class="a big gold" id="s4b" style="left:52px;top:660px;font-size:170px">BANT AYNI</div>
  </section>
  <section id="s5" class="scene clip">
    <div class="a h" id="s5a" style="left:60px;top:420px;font-size:84px;white-space:normal;width:500px;line-height:1">MEKANİZMA <span class="red">≠</span></div>
    <div class="a h gold" id="s5b" style="left:60px;top:620px;font-size:84px">RAKAM ≈</div>
    <div class="a h" id="s5c" style="left:60px;top:1000px;font-size:110px">NEDEN<span class="gold">?</span></div>
  </section>
  <section id="s6" class="scene clip">
    <div class="a lab" id="s6l" style="left:60px;top:330px">MEVDUAT · FAİZ</div>
    <svg class="a" id="s6i" style="left:60px;top:400px" width="220" height="260" viewBox="0 0 220 260">
      <path id="s6sh" d="M50 120 V80 a60 60 0 0 1 120 0 V120" fill="none" stroke="#e8b931" stroke-width="18"/>
      <rect x="20" y="120" width="180" height="130" rx="20" fill="#e8b931"/></svg>
    <div class="a h" id="s6a" style="left:320px;top:440px;font-size:80px">ORAN</div>
    <div class="a h gold" id="s6b" style="left:320px;top:540px;font-size:80px">BAŞTAN SABİT</div>
    <div class="a mono" id="s6m" style="left:60px;top:720px">banka getiriyi taahhüt eder</div>
  </section>
  <section id="s7" class="scene clip">
    <div class="a lab" id="s7l" style="left:60px;top:290px">KATILMA HESABI · HAVUZ</div>
    <svg class="a" id="s7svg" style="left:60px;top:350px" width="960" height="860" viewBox="0 0 960 860">
      <g id="s7coins"><circle cx="200" cy="60" r="34" fill="#e8b931"/><circle cx="330" cy="40" r="34" fill="#e8b931"/><circle cx="460" cy="70" r="34" fill="#e8b931"/><circle cx="590" cy="45" r="34" fill="#e8b931"/><circle cx="720" cy="65" r="34" fill="#e8b931"/></g>
      <path id="s7pool" d="M120 180 H840 L780 420 H180 Z" fill="rgba(232,185,49,.12)" stroke="#e8b931" stroke-width="6"/>
      <text x="480" y="320" text-anchor="middle" font-family="Inter Tight" font-weight="900" font-size="72" fill="#f3efe6">HAVUZ</text>
      <text x="480" y="520" text-anchor="middle" font-family="IBM Plex Mono" font-weight="700" font-size="30" fill="#e8b931">HAVUZUN KÂRI ↓</text>
      <rect id="s7a" x="60" y="570" width="560" height="140" rx="20" fill="#e8b931"/>
      <rect id="s7b" x="640" y="570" width="260" height="140" rx="20" fill="rgba(243,239,230,.3)"/>
      <text id="s7ta" x="340" y="660" text-anchor="middle" font-family="Inter Tight" font-weight="900" font-size="52" fill="#0d0c0a">HESAP SAHİBİ</text>
      <text id="s7tb" x="770" y="660" text-anchor="middle" font-family="Inter Tight" font-weight="900" font-size="52" fill="#f3efe6">BANKA</text>
      <text x="480" y="790" text-anchor="middle" font-family="IBM Plex Mono" font-size="28" fill="rgba(243,239,230,.7)">paylaşım oranı akdin başında belli</text></svg>
  </section>
  <section id="s8" class="scene clip">
    <div class="a lab" id="s8l" style="left:60px;top:400px">İLAN EDİLEN ORAN</div>
    <div class="a big gold" id="s8a" style="left:52px;top:450px;font-size:170px">GÖSTERGE</div>
    <div class="a h red" id="s8b" style="left:300px;top:700px;font-size:96px;border:8px solid #ff4a3d;padding:6px 30px;border-radius:14px;transform:rotate(-5deg)">GARANTİ DEĞİL</div>
  </section>
  <section id="s9" class="scene clip">
    <div class="a h" id="s9a" style="left:0;right:0;top:600px;text-align:center;font-size:130px">BENZERLİK <span class="gold">↓</span></div>
  </section>
  <section id="s10" class="scene clip">
    <div class="a lab" id="s10l" style="left:60px;top:290px">ZİNCİR</div>
    <div class="node" id="s10n0" style="top:350px">PİYASA FAİZLERİ</div><div class="arr" id="s10a0" style="top:495px">↓</div>
    <div class="node" id="s10n1" style="top:570px">FİNANSMAN FİYATI</div><div class="arr" id="s10a1" style="top:715px">↓</div>
    <div class="node" id="s10n2" style="top:790px">HAVUZUN KÂRI</div><div class="arr" id="s10a2" style="top:935px">↓</div>
    <div class="node" id="s10n3" style="top:1010px;border-color:#e8b931;color:#e8b931">SENİN KÂR PAYIN</div>
  </section>
  <section id="s11" class="scene clip">
    <div class="a lab" id="s11l" style="left:60px;top:300px">AYNI MÜŞTERİ İÇİN YARIŞ</div>
    <div class="a card" id="s11a" style="left:60px;top:400px;width:420px;height:300px;text-align:center"><div class="mono">KATILIM</div><div class="h gold" style="font-size:80px;margin-top:60px">KÂR PAYI</div></div>
    <div class="a card" id="s11b" style="left:600px;top:400px;width:420px;height:300px;text-align:center"><div class="mono">MEVDUAT</div><div class="h" style="font-size:80px;margin-top:60px">FAİZ</div></div>
    <svg class="a" id="s11p" style="left:420px;top:780px" width="240" height="300" viewBox="0 0 240 300"><circle cx="120" cy="70" r="60" fill="#f3efe6"/><path d="M20 290 a100 120 0 0 1 200 0 Z" fill="#f3efe6"/></svg>
    <div class="a h" id="s11c" style="left:0;right:0;top:1120px;text-align:center;font-size:64px">SEN</div>
  </section>
  <section id="s12" class="scene clip">
    <div class="a lab" id="s12l" style="left:60px;top:290px">TCMB · TÜRK LİRASI</div>
    <div class="a h" id="s12h" style="left:60px;top:340px;font-size:66px">ÇOĞUNLUKLA <span class="gold">BİRLİKTE</span></div>
    <svg class="a" id="s12svg" style="left:60px;top:470px" width="960" height="620" viewBox="0 0 960 620">
      <line x1="0" x2="960" y1="580" y2="580" stroke="rgba(243,239,230,.25)" stroke-width="3"/>
      <path id="s12p1" d="M20 480 C 160 470, 260 300, 400 260 S 640 200, 760 300 S 900 360, 940 340" fill="none" stroke="#f3efe6" stroke-width="9"/>
      <path id="s12p2" d="M20 520 C 180 510, 290 350, 440 300 S 680 240, 790 330 S 910 390, 940 380" fill="none" stroke="#e8b931" stroke-width="9"/>
      <text x="680" y="190" font-family="IBM Plex Mono" font-size="26" fill="#f3efe6">mevduat faizi</text>
      <text x="700" y="450" font-family="IBM Plex Mono" font-weight="700" font-size="26" fill="#e8b931">kâr payı</text>
      <text x="20" y="615" font-family="IBM Plex Mono" font-size="22" fill="rgba(243,239,230,.55)">temsili şema</text></svg>
  </section>
  <section id="s13" class="scene clip">
    <div class="a h" id="s13a" style="left:0;right:0;top:1170px;text-align:center;font-size:72px">MEKANİZMA FARKLI</div>
    <div class="a h gold" id="s13b" style="left:0;right:0;top:1260px;text-align:center;font-size:72px">FİYAT AYNI PİYASADA</div>
  </section>
  <section id="s14" class="scene clip">
    <svg class="a" id="s14i" style="left:250px;top:1166px" width="96" height="120" viewBox="0 0 96 120"><path d="M8 6h80v108L48 86 8 114z" fill="#e8b931"/></svg>
    <div class="a h gold" id="s14t" style="left:370px;top:1170px;font-size:118px">KAYDET</div>
  </section>
  <section id="s15" class="scene clip">
    <div class="a h" id="s15a" style="left:0;right:0;top:1170px;text-align:center;font-size:84px">TESADÜF <span class="red">DEĞİL</span></div>
  </section>
'''

SCENE_JS = r'''
const at=(p,after=0)=>{for(const c of CAPS)for(const w of c.w)if(w[1]>=after&&w[0].toLowerCase().startsWith(p.toLowerCase()))return w[1];return null;};
// S1 kanca
inn('#s1l',.3,{y:-20}); slam('#s1a',at('aynı'));
// S2 kilit
const s2=st('s2'); inn('#s2n',s2+.4,{y:10}); inn('#s2l',at('sonunda')-.1); inn('#s2c1',at('nasıl')-.1,{y:30}); inn('#s2c2',at('neden',9)-.1,{y:30});
// S3 aralıklar
const s3=st('s3'); inn('#s3l',s3+.4); inn('#s3svg',s3+.45,{y:0});
tl.fromTo('#s3r1',{scaleX:0,transformOrigin:'0% 50%'},{scaleX:1,duration:.6,ease:'power3.out'},at('%31')-.3); tl.fromTo('#s3t1',{opacity:0},{opacity:1,duration:.25},at('%31'));
tl.fromTo('#s3r2',{scaleX:0,transformOrigin:'0% 50%'},{scaleX:1,duration:.6,ease:'power3.out'},at('%36')-.3); tl.fromTo('#s3t2',{opacity:0},{opacity:1,duration:.25},at('%36'));
tl.fromTo('#s3band',{opacity:0},{opacity:1,duration:.3},at('%36')+.7); inn('#s3m',at('%36')+.5,{y:10});
// S4
const s4=st('s4'); inn('#s4l',s4+.4); slam('#s4a',at('birkaç')); slam('#s4b',at('bant'));
// S5 ara kanca (köşe avatar)
const s5=st('s5'); slam('#s5a',at('mekanizma')); slam('#s5b',at('rakam')); inn('#s5c',at('yakın')-.1,{s:1.1});
// S6 faiz kilit
const s6=st('s6'); inn('#s6l',s6+.4); inn('#s6i',s6+.45,{y:-30}); tl.fromTo('#s6sh',{y:-30},{y:0,duration:.25,ease:'power4.in'},at('taahhüt')); inn('#s6a',s6+.6); slam('#s6b',at('baştan')); inn('#s6m',at('taahhüt')+.2,{y:10});
// S7 havuz
const s7=st('s7'); inn('#s7l',s7+.4); inn('#s7svg',s7+.45,{y:0}); tl.fromTo('#s7coins',{y:-60,opacity:0},{y:80,opacity:1,duration:.7,ease:'power2.in'},at('havuza')-.3);
tl.fromTo(['#s7a','#s7ta'],{opacity:0},{opacity:1,duration:.3},at('paylaşılır')-.2); tl.fromTo(['#s7b','#s7tb'],{opacity:0},{opacity:1,duration:.3},at('paylaşılır'));
// S8 gösterge
const s8=st('s8'); inn('#s8l',s8+.4); slam('#s8a',at('gösterge')); tl.fromTo('#s8b',{opacity:0,scale:1.7},{opacity:1,scale:1,duration:.25,ease:'power4.in'},at('garanti'));
// S9 ara kanca 2
const s9=st('s9'); tl.fromTo('#s9a',{opacity:0,scale:1.5,transformOrigin:'50% 50%'},{opacity:1,scale:1,duration:.3,ease:'power4.in'},s9+.4);
// S10 zincir
const s10=st('s10'); inn('#s10l',s10+.4);
inn('#s10n2',s10+.45,{y:24}); inn('#s10a1',at('finansmandan')-.1,{y:-10}); inn('#s10n1',at('finansmandan'),{y:24});
inn('#s10a0',at('piyasa',42)-.1,{y:-10}); inn('#s10n0',at('piyasa',42),{y:24}); inn('#s10a2',at('fiyatlanır'),{y:-10}); slam('#s10n3',at('fiyatlanır')+.2);
// S11 yarış
const s11=st('s11'); inn('#s11l',s11+.4); inn('#s11a',s11+.5,{y:40}); inn('#s11b',s11+.7,{y:40}); inn('#s11p',at('müşteri')-.1,{y:30}); slam('#s11c',at('yarışır'));
// S12 iki çizgi
const s12=st('s12'); inn('#s12l',s12+.4); inn('#s12h',at('ikisinin')); inn('#s12svg',s12+.5,{y:0});
tl.fromTo('#s12p1',{strokeDasharray:1300,strokeDashoffset:1300},{strokeDashoffset:0,duration:2,ease:'none'},s12+.6);
tl.fromTo('#s12p2',{strokeDasharray:1300,strokeDashoffset:1300},{strokeDashoffset:0,duration:2,ease:'none'},s12+.9);
// S13 kapanış
const s13=st('s13'); inn('#s13a',s13+.4); slam('#s13b',at('piyasadaki'));
// S14 CTA
tl.fromTo('#s14i',{opacity:0,y:-80},{opacity:1,y:0,duration:.4,ease:'bounce.out'},at('kaydet')-.1); slam('#s14t',at('kaydet'));
// S15 döngü
const s15=st('s15'); inn('#s15a',s15+.4);
'''
