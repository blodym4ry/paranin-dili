import os
# Şablon: OPTİK FORM / SINAV KÂĞIDI (Ata seçimi, 22 Eki). Krem kâğıt, pembe optik ızgara, kurşun kalemle doldurulan şıklar, kırmızı kalemle öğretmen notu.
# Anlatım: soru → veri → ters köşe. Avatar: gri kapüşon. Müzik: drive.
# Gerçek görseller: media/ (kep.jpg: Siirt Üniversitesi mezuniyet töreni; optik.jpg: daktilo.com) — kaynaklar.md
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [
    (N('yüzde', 'kırk', 'üçü'), "%43'ü"), (N('yüzde', 'seksen'), '%80'), (N('yüzde', 'yirmi', 'bir'), '%21'),
    (N('iki', 'bin', 'beşte'), "2005'te"), (N('yetmiş', 'yedi'), '77'), (N('iki', 'yüzü'), "200'ü"),
    (N('bir', 'milyon'), '1 milyon'), (N('yirmi', 'dört'), '24'), (N('yüzde', 'otuz'), '%30'),
]
EM = {'tuzak', 'tuzağın', 'diplomanın', 'kaydet', 'şaşırtıcı', 'arat'}
RED = {"%43'ü", '%21', '%30', 'düşürmüyor'}
FRONT = [250, 330, 580, 815, 18]
MID = [290, 330, 500, 703, 18]
AV = {'s1': FRONT, 's2': None, 's3': None, 's4': None, 's5': None, 's6': None, 's7': MID, 's8': None, 's9': FRONT}

EXTRA_CSS = r'''<style>
:root{--paper:#f7f2e6;--ink:#1f2430;--pink:#e7a3ae;--pen:#d0312d;--lead:#3a3d44;--cap-em-bg:#1f2430;--cap-em-fg:#f7f2e6;--cap-on:#1f2430;--cap-red:#d0312d}
.cw{color:rgba(31,36,48,.32)}
body,#root{background:#f7f2e6}
.bg{background:linear-gradient(#f7f2e6,#efe8d6)}
.bg::before{content:'';position:absolute;inset:0;background:repeating-linear-gradient(0deg,transparent 0 58px,rgba(231,163,174,.45) 58px 60px),repeating-linear-gradient(90deg,transparent 0 58px,rgba(231,163,174,.25) 58px 60px)}
.bg::after{content:'';position:absolute;left:52px;top:0;bottom:0;width:4px;background:rgba(208,49,45,.45)}
#grid{display:none}
#avbox{filter:drop-shadow(0 0 0 #1f2430) drop-shadow(5px 0 0 #1f2430) drop-shadow(-5px 0 0 #1f2430) drop-shadow(0 5px 0 #1f2430) drop-shadow(0 -5px 0 #1f2430) drop-shadow(0 24px 40px rgba(0,0,0,.35))}
.hdr{font:700 26px 'IBM Plex Mono';letter-spacing:.14em;color:#b25866}
.q{font:800 52px/1.15 'Inter Tight';color:var(--ink);letter-spacing:-.02em}
.opts{display:flex;gap:22px}
.b{width:74px;height:74px;border-radius:50%;border:4px solid var(--pink);display:flex;align-items:center;justify-content:center;font:700 34px 'IBM Plex Mono';color:#b25866;background:rgba(255,255,255,.5);position:relative}
.b.f::after{content:'';position:absolute;inset:6px;border-radius:50%;background:var(--lead)}
.dot{width:58px;height:58px;border-radius:50%;border:3px solid var(--pink);background:rgba(255,255,255,.6)}
.dot.on{background:var(--pen);border-color:var(--pen)}
.big{font:900 170px/1 'Inter Tight';letter-spacing:-.05em;color:var(--ink)}
.pen{color:var(--pen)}
.ring{position:absolute;border:7px solid var(--pen);border-radius:50%;transform:rotate(-6deg)}
.note{font:italic 700 46px 'DM Serif Display';color:var(--pen)}
.row{position:absolute;left:70px;width:940px}
.row .lab{font:800 40px 'Inter Tight';color:var(--ink);margin-bottom:12px}
.row .track{height:66px;border:4px solid var(--pink);border-radius:40px;background:rgba(255,255,255,.6);overflow:hidden}
.row .fill{height:100%;border-radius:40px;transform-origin:0 50%}
.ph{position:absolute;overflow:hidden;border:10px solid #fff;box-shadow:0 20px 44px rgba(0,0,0,.3);transform:rotate(-2deg)}
.ph img{display:block;width:100%;height:100%;object-fit:cover}
.src{font:500 20px 'IBM Plex Mono';color:#7d6f62}
.card{position:absolute;background:#fff;border:3px solid var(--ink);border-radius:12px;padding:20px 26px;font:800 40px 'Inter Tight';color:var(--ink);box-shadow:8px 8px 0 var(--ink)}
.x{position:absolute;font:900 140px/1 'Inter Tight';color:var(--pen)}
</style>'''


def scenes(A):
    return [('s1', 0, 4.749), ('s2', 4.749, 9.62), ('s3', 9.62, 12.15), ('s4', 12.15, 18.85), ('s5', 18.85, 31.15),
            ('s6', 31.15, 38.53), ('s7', 38.53, 42.26), ('s8', 42.26, 54.74), ('s9', 54.74, DUR)]


DOTS = ''.join(f'<div class="dot" id="s2d{i}" style="position:absolute;left:{80 + (i % 10) * 92}px;top:{360 + (i // 10) * 72}px"></div>' for i in range(100))

SCENE_HTML = r'''
  <section id="s1" class="scene clip">
    <div class="a hdr" id="s1h" style="left:80px;top:230px">SORU 1</div>
    <div class="a opts" id="s1o" style="left:200px;top:1180px"><div class="b">A</div><div class="b">B</div><div class="b">C</div><div class="b">D</div><div class="b">E</div></div>
  </section>
  <section id="s2" class="scene clip">
    <div class="a hdr" id="s2h" style="left:80px;top:250px">MAAŞLI ÇALIŞAN 100 LİSANS MEZUNU</div>
    <div class="a" id="s2dots" style="left:0;top:0;width:1080px;height:1120px">''' + DOTS + r'''</div>
    <div class="a big pen" id="s2v" style="left:80px;top:1130px">%43</div>
    <div class="a q" id="s2t" style="left:520px;top:1150px;font-size:44px;width:500px">alanının dışında çalışıyor</div>
    <div class="a src" id="s2src" style="left:80px;top:1320px">TÜİK Yükseköğretim İstihdam Göstergeleri 2025 (23.07.2026)</div>
  </section>
  <section id="s3" class="scene clip">
    <div class="a hdr" id="s3h" style="left:80px;top:300px">SORU 2</div>
    <div class="a q" id="s3q" style="left:80px;top:350px;width:920px">Asıl tuzak bu mu?</div>
    <div class="a opts" id="s3o" style="left:80px;top:520px"><div class="b">E</div><div class="b">H</div><div class="b" style="border-color:#d0312d;color:#d0312d">?</div></div>
    <div class="a note" id="s3n" style="left:80px;top:680px">→ cevap sonda</div>
  </section>
  <section id="s4" class="scene clip">
    <div class="a hdr" id="s4h" style="left:80px;top:250px">ALANINDA ÇALIŞANLAR · LİSANS</div>
    <div class="a row" id="s4r1" style="top:360px"><div class="lab">Sağlık</div><div class="track"><div class="fill" id="s4f1" style="width:80%;background:#2e7d4f"></div></div><div class="big" style="font-size:110px;margin-top:10px">%80</div></div>
    <div class="a row" id="s4r2" style="top:760px"><div class="lab">Sosyal bilimler ve gazetecilik</div><div class="track"><div class="fill" id="s4f2" style="width:21%;background:#d0312d"></div></div><div class="big pen" style="font-size:110px;margin-top:10px">%21</div></div>
  </section>
  <section id="s5" class="scene clip">
    <div class="a ph" id="s5p" style="left:70px;top:240px;width:940px;height:520px"><img src="media/kep.jpg"></div>
    <div class="a card" id="s5u" style="left:70px;top:820px">Üniversite sayısı: <span id="s5n">77</span></div>
    <div class="a note" id="s5y" style="left:640px;top:830px">2005 → 2024</div>
    <div class="a card" id="s5m" style="left:70px;top:960px">Her yıl ~1 milyon mezun</div>
    <div class="a card" id="s5i" style="left:70px;top:1100px;border-color:#d0312d;box-shadow:8px 8px 0 #d0312d">24 yaş altı mezun işsizliği: <span class="pen">%30</span></div>
    <div class="a src" id="s5src" style="left:70px;top:1260px">TEPAV (2025) · TÜİK 2025 4. çeyrek verisi, A. Aktaş hesabı (Karar)</div>
  </section>
  <section id="s6" class="scene clip">
    <div class="a hdr" id="s6h" style="left:80px;top:250px">YAYGIN CEVAP</div>
    <div class="a q" id="s6q" style="left:80px;top:310px;width:920px">"Alan dışında çalışırsan daha az kazanırsın."</div>
    <div class="a x" id="s6x" style="left:860px;top:450px">✗</div>
    <div class="a card" id="s6a" style="left:80px;top:620px;font-size:44px">Alan dışı → maaş <span class="pen">tek başına düşmüyor</span></div>
    <div class="a src" id="s6src" style="left:80px;top:780px">ETF (2024, HİA 2016–19) · Orbay, Aydede, Erkol (Applied Economics, 2021)</div>
  </section>
  <section id="s7" class="scene clip">
    <div class="a card" id="s7t" style="left:170px;top:1090px;font-size:46px;border-color:#d0312d;box-shadow:8px 8px 0 #d0312d">ASIL TUZAK</div>
  </section>
  <section id="s8" class="scene clip">
    <div class="a hdr" id="s8h" style="left:80px;top:250px">DİPLOMANIN GEREKTİRMEDİĞİ İŞ</div>
    <div class="a big pen" id="s8v" style="left:80px;top:300px">−¼</div>
    <div class="a q" id="s8t" style="left:420px;top:340px;width:580px;font-size:46px">maaş, yaklaşık dörtte bir düşük</div>
    <div class="a src" id="s8src" style="left:80px;top:490px">ETF 2024: aşırı nitelik ücret cezası ≈ %24</div>
    <div class="a ph" id="s8p" style="left:620px;top:560px;width:380px;height:300px;transform:rotate(3deg)"><img src="media/optik.jpg"></div>
    <div class="a card" id="s8a" style="left:80px;top:580px;width:500px;font-size:34px">1 · TÜİK<br>Yükseköğretim<br>İstihdam Göstergeleri</div>
    <div class="a card" id="s8b" style="left:80px;top:850px;width:920px;font-size:38px">2 · Bölümünü arat</div>
    <div class="a card" id="s8c" style="left:80px;top:990px;width:920px;font-size:38px">3 · İlk işe girme süresi + kayıtlı istihdam</div>
    <div class="a ring" id="s8r" style="left:60px;top:960px;width:960px;height:150px"></div>
  </section>
  <section id="s9" class="scene clip">
    <div class="a card" id="s9k" style="left:330px;top:1120px;font-size:64px;border-color:#d0312d;color:#d0312d;box-shadow:8px 8px 0 #d0312d;transform:rotate(-5deg)">KAYDET</div>
    <div class="a note" id="s9a" style="left:0;right:0;top:1150px;text-align:center;font-size:52px">bölüm değil, <span style="text-decoration:underline">iş</span></div>
  </section>
'''

SCENE_JS = r'''
const stamp=(s,t)=>tl.fromTo(s,{opacity:0,scale:1.8},{opacity:1,scale:1,duration:.22,ease:'power4.in'},t);
// S1 soru
inn('#s1h',.2,{y:-10}); inn('#s1o',1.6,{y:30}); tl.to('#s1o .b:nth-child(3)',{backgroundColor:'#3a3d44',duration:.2},3.4);
// S2 100 nokta, 43 kırmızı
inn('#s2h',4.8); tl.fromTo('#s2dots .dot',{opacity:0,scale:.3},{opacity:1,scale:1,duration:.25,stagger:.008},4.85);
for(let i=0;i<43;i++) tl.set('#s2d'+i,{className:'dot on'},7.4+i*.012);
slam('#s2v',7.4); inn('#s2t',7.8,{y:20}); inn('#s2src',8.2,{y:0});
// S3 soru 2
inn('#s3h',9.7); inn('#s3q',9.75); inn('#s3o',10.3,{y:20}); inn('#s3n',11.2,{y:10});
// S4 alanlar
inn('#s4h',12.2); inn('#s4r1',12.25,{y:30}); tl.fromTo('#s4f1',{scaleX:0},{scaleX:1,duration:.7,ease:'power3.out'},13.7);
inn('#s4r2',15.3,{y:30}); tl.fromTo('#s4f2',{scaleX:0},{scaleX:1,duration:.5,ease:'power3.out'},17.9);
// S5 neden
inn('#s5p',18.95,{s:1.05}); inn('#s5u',19.9,{y:30}); count('#s5n',77,205,22.85,1.0,v=>Math.round(v)); inn('#s5y',20.9,{y:10});
inn('#s5m',25.4,{y:30}); slam('#s5i',27.33); inn('#s5src',28.0,{y:0});
// S6 ters köşe
inn('#s6h',31.25); inn('#s6q',31.4,{y:30}); stamp('#s6x',36.6); inn('#s6a',37.1,{y:30}); inn('#s6src',37.4,{y:0});
// S7 ara kanca
inn('#s7t',38.75,{y:20});
// S8 tuzak + kontrol adımı
inn('#s8h',42.35); slam('#s8v',43.75); inn('#s8t',43.9,{y:20}); inn('#s8src',44.4,{y:0});
inn('#s8a',47.59,{y:30}); inn('#s8p',47.7,{y:40}); inn('#s8b',50.28,{y:30}); inn('#s8c',51.45,{y:30});
tl.fromTo('#s8r',{opacity:0,scale:1.15},{opacity:1,scale:1,duration:.3,ease:'power3.out'},52.95);
// S9 CTA + döngü
stamp('#s9k',54.91); out('#s9k',55.9); inn('#s9a',56.1,{y:20});
'''


def SFX(A):
    return [[1.6, 'pop', -12, 0, 'opts'], [3.4, 'marker', -11, 0, 'fill'], [4.85, 'gears', -13, 0, 'dots'], [7.4, 'impact', -8, 1, '43'],
            [9.75, 'paper_drop', -11, 0, 'soru2'], [13.7, 'ui_click', -12, 0, '80'], [17.9, 'impact', -9, 1, '21'],
            [18.95, 'paper_drop', -11, 0, 'kep'], [22.85, 'gears', -12, 0, '205'], [27.33, 'impact', -9, 1, '30'],
            [31.4, 'pop', -11, 0, 'yaygin'], [36.6, 'stamp', -7, 1, 'x'], [43.75, 'impact', -8, 1, 'ceyrek'],
            [47.59, 'ui_click', -12, 0, 'adim1'], [50.28, 'ui_click', -12, 0, 'adim2'], [52.95, 'marker', -10, 0, 'ring'],
            [54.91, 'stamp', -7, 1, 'kaydet'], [58.36, 'success', -11, 0, 'loop']]


def RISERS(A): return [[9.4, 'sharp', -11], [31.0, 'metallic', -11], [42.1, 'sharp', -12]]
