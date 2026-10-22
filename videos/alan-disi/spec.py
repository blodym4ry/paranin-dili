import os
# Şablon: OPTİK FORM / SINAV KÂĞIDI (Ata seçimi, 22 Eki). Krem kâğıt, pembe optik ızgara, kurşun kalemle doldurulan şıklar, kırmızı kalemle öğretmen notu.
# Anlatım: soru → veri → ters köşe. Avatar: gri kapüşon. Müzik: drive.
# v2 (Ata, 22 Eki): CTA "kaydet" → "arkadaşına gönder"; tempo yavaş — seslendirme 0.93 hız, her ekranda tek fikir,
#   öğe grupları birlikte ve yumuşak gelir, ~19 giriş (v1: ~40). v1 kurgusu: spec_v1.py
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
EM = {'tuzak', 'tuzağın', 'diplomanın', 'gönder', 'şaşırtıcı', 'arat'}
RED = {"%43'ü", '%21', '%30', 'düşürmüyor'}
FRONT = [250, 330, 580, 815, 18]
MID = [290, 330, 500, 703, 18]
AV = {'s1': FRONT, 's2': None, 's3': None, 's4': None, 's5': None, 's5b': None, 's6': None, 's7': MID, 's8': None,
      's9': None, 's10': FRONT}

EXTRA_CSS = r'''<style>
:root{--paper:#f7f2e6;--ink:#1f2430;--pink:#e7a3ae;--pen:#d0312d;--lead:#3a3d44;--cap-em-bg:#1f2430;--cap-em-fg:#f7f2e6;--cap-on:#1f2430;--cap-red:#d0312d}
.cw{color:rgba(31,36,48,.32)}
body,#root{background:#f7f2e6}
.bg{background:linear-gradient(#f7f2e6,#efe8d6)}
.bg::before{content:'';position:absolute;inset:0;background:repeating-linear-gradient(0deg,transparent 0 58px,rgba(231,163,174,.45) 58px 60px),repeating-linear-gradient(90deg,transparent 0 58px,rgba(231,163,174,.25) 58px 60px)}
.bg::after{content:'';position:absolute;left:52px;top:0;bottom:0;width:4px;background:rgba(208,49,45,.45)}
#grid{display:none}
#avbox{filter:drop-shadow(0 0 0 #1f2430) drop-shadow(5px 0 0 #1f2430) drop-shadow(-5px 0 0 #1f2430) drop-shadow(0 5px 0 #1f2430) drop-shadow(0 -5px 0 #1f2430) drop-shadow(0 24px 40px rgba(0,0,0,.35))}
.hdr{font:700 26px 'IBM Plex Mono';letter-spacing:.14em;color:#b25866;white-space:nowrap}
.q{font:800 52px/1.15 'Inter Tight';color:var(--ink);letter-spacing:-.02em}
.opts{display:flex;gap:22px}
.b{width:74px;height:74px;border-radius:50%;border:4px solid var(--pink);display:flex;align-items:center;justify-content:center;font:700 34px 'IBM Plex Mono';color:#b25866;background:rgba(255,255,255,.5);position:relative}
.dot{width:58px;height:58px;border-radius:50%;border:3px solid var(--pink);background:rgba(255,255,255,.6)}
.dot.on{background:var(--pen);border-color:var(--pen)}
.big{font:900 170px/1 'Inter Tight';letter-spacing:-.05em;color:var(--ink)}
.pen{color:var(--pen)}
.ring{position:absolute;border:7px solid var(--pen);border-radius:50%;transform:rotate(-3deg)}
.note{font:italic 700 46px 'DM Serif Display';color:var(--pen)}
.row{position:absolute;left:70px;width:940px}
.row .lab{font:800 40px 'Inter Tight';color:var(--ink);margin-bottom:12px}
.row .track{height:66px;border:4px solid var(--pink);border-radius:40px;background:rgba(255,255,255,.6);overflow:hidden}
.row .fill{height:100%;border-radius:40px;transform-origin:0 50%}
.ph{position:absolute;overflow:hidden;border:10px solid #fff;box-shadow:0 20px 44px rgba(0,0,0,.3);transform:rotate(-2deg)}
.ph img{display:block;width:100%;height:100%;object-fit:cover}
.src{font:500 20px 'IBM Plex Mono';color:#7d6f62;white-space:nowrap}
.card{position:absolute;background:#fff;border:3px solid var(--ink);border-radius:12px;padding:20px 26px;font:800 40px 'Inter Tight';color:var(--ink);box-shadow:8px 8px 0 var(--ink)}
.x{position:absolute;font:900 140px/1 'Inter Tight';color:var(--pen)}
.grp{position:absolute;left:0;top:0;width:1080px;height:1400px}
</style>'''


def scenes(A):
    return [('s1', 0, 5.10), ('s2', 5.10, 10.36), ('s3', 10.36, 13.06), ('s4', 13.06, 20.30), ('s5', 20.30, 26.30),
            ('s5b', 26.30, 33.50), ('s6', 33.50, 41.44), ('s7', 41.44, 45.43), ('s8', 45.43, 48.60),
            ('s9', 48.60, 58.73), ('s10', 58.73, DUR)]


DOTS = ''.join(f'<div class="dot" id="s2d{i}" style="position:absolute;left:{80 + (i % 10) * 92}px;top:{360 + (i // 10) * 72}px"></div>' for i in range(100))

SCENE_HTML = r'''
  <section id="s1" class="scene clip">
    <div class="grp" id="s1g">
      <div class="a hdr" style="left:80px;top:230px">SORU 1</div>
      <div class="a opts" style="left:200px;top:1180px"><div class="b">A</div><div class="b">B</div><div class="b">C</div><div class="b">D</div><div class="b">E</div></div>
    </div>
  </section>
  <section id="s2" class="scene clip">
    <div class="grp" id="s2top">
      <div class="a hdr" style="left:80px;top:250px">MAAŞLI ÇALIŞAN 100 LİSANS MEZUNU</div>''' + DOTS + r'''</div>
    <div class="grp" id="s2bot">
      <div class="a big pen" style="left:80px;top:1130px">%43</div>
      <div class="a q" style="left:520px;top:1150px;font-size:44px;width:500px">alanının dışında çalışıyor</div>
      <div class="a src" style="left:80px;top:1320px">TÜİK Yükseköğretim İstihdam Göstergeleri 2025 (23.07.2026)</div>
    </div>
  </section>
  <section id="s3" class="scene clip">
    <div class="grp" id="s3g">
      <div class="a hdr" style="left:80px;top:420px">SORU 2</div>
      <div class="a q" style="left:80px;top:480px;width:920px;font-size:84px">Asıl tuzak bu mu?</div>
      <div class="a note" style="left:80px;top:620px;font-size:60px">→ cevap sonda</div>
    </div>
  </section>
  <section id="s4" class="scene clip">
    <div class="grp" id="s4g1">
      <div class="a hdr" style="left:80px;top:250px">ALANINDA ÇALIŞANLAR · LİSANS</div>
      <div class="a row" style="top:360px"><div class="lab">Sağlık</div><div class="track"><div class="fill" id="s4f1" style="width:80%;background:#2e7d4f"></div></div><div class="big" style="font-size:110px;margin-top:10px">%80</div></div>
    </div>
    <div class="a row" id="s4r2" style="top:760px"><div class="lab">Sosyal bilimler ve gazetecilik</div><div class="track"><div class="fill" id="s4f2" style="width:21%;background:#d0312d"></div></div><div class="big pen" style="font-size:110px;margin-top:10px">%21</div></div>
  </section>
  <section id="s5" class="scene clip">
    <div class="grp" id="s5g">
      <div class="a ph" style="left:70px;top:240px;width:940px;height:600px"><img src="media/kep.jpg"></div>
      <div class="a hdr" style="left:80px;top:900px">ÜNİVERSİTE SAYISI · 2005 → BUGÜN</div>
      <div class="a big" id="s5n" style="left:80px;top:950px">77</div>
      <div class="a src" style="left:80px;top:1140px">TEPAV (2025)</div>
    </div>
  </section>
  <section id="s5b" class="scene clip">
    <div class="a card" id="s5m" style="left:70px;top:330px;font-size:56px">Her yıl ~1 milyon mezun</div>
    <div class="grp" id="s5i">
      <div class="a hdr" style="left:80px;top:580px">24 YAŞ ALTI ÜNİVERSİTE MEZUNU</div>
      <div class="a big pen" style="left:80px;top:630px;font-size:220px">%30</div>
      <div class="a q" style="left:80px;top:870px">işsiz</div>
      <div class="a src" style="left:80px;top:960px">TÜİK 2025 4. çeyrek verisi, A. Aktaş hesabı (Karar)</div>
    </div>
  </section>
  <section id="s6" class="scene clip">
    <div class="grp" id="s6g">
      <div class="a hdr" style="left:80px;top:250px">YAYGIN CEVAP</div>
      <div class="a q" style="left:80px;top:310px;width:760px">"Alan dışında çalışırsan daha az kazanırsın."</div>
    </div>
    <div class="grp" id="s6r">
      <div class="a x" style="left:860px;top:300px">✗</div>
      <div class="a card" style="left:80px;top:620px;font-size:44px">Alan dışı → maaş <span class="pen">tek başına düşmüyor</span></div>
      <div class="a src" style="left:80px;top:780px">ETF (2024, HİA 2016–19) · Orbay, Aydede, Erkol (Applied Economics, 2021)</div>
    </div>
  </section>
  <section id="s7" class="scene clip">
    <div class="a card" id="s7t" style="left:170px;top:1090px;font-size:46px;border-color:#d0312d;box-shadow:8px 8px 0 #d0312d">ASIL TUZAK</div>
  </section>
  <section id="s8" class="scene clip">
    <div class="grp" id="s8g">
      <div class="a hdr" style="left:80px;top:400px">DİPLOMANIN GEREKTİRMEDİĞİ İŞ</div>
      <div class="a big pen" style="left:80px;top:450px;font-size:260px">−¼</div>
      <div class="a q" style="left:80px;top:760px;width:920px;font-size:60px">maaş, yaklaşık dörtte bir düşük</div>
      <div class="a src" style="left:80px;top:860px">ETF 2024: aşırı nitelik ücret cezası ≈ %24</div>
    </div>
  </section>
  <section id="s9" class="scene clip">
    <div class="a hdr" style="left:80px;top:250px">KENDİN KONTROL ET</div>
    <div class="grp" id="s9a">
      <div class="a ph" style="left:620px;top:320px;width:380px;height:300px;transform:rotate(3deg)"><img src="media/optik.jpg"></div>
      <div class="a card" style="left:80px;top:330px;width:500px;font-size:34px">1 · TÜİK<br>Yükseköğretim<br>İstihdam Göstergeleri</div>
    </div>
    <div class="a card" id="s9b" style="left:80px;top:680px;width:920px;font-size:40px">2 · Bölümünü arat</div>
    <div class="grp" id="s9c">
      <div class="a card" style="left:80px;top:830px;width:920px;font-size:40px">3 · İlk işe girme süresi + kayıtlı istihdam</div>
      <div class="a ring" style="left:55px;top:805px;width:970px;height:150px"></div>
    </div>
  </section>
  <section id="s10" class="scene clip">
    <div class="a card" id="s10k" style="left:120px;top:1110px;font-size:46px;border-color:#d0312d;color:#d0312d;box-shadow:8px 8px 0 #d0312d;transform:rotate(-3deg);white-space:nowrap">→ ALAN DIŞI ÇALIŞAN ARKADAŞINA</div>
    <div class="a note" id="s10a" style="left:0;right:0;top:1150px;text-align:center;font-size:52px">bölüm değil, <span style="text-decoration:underline">iş</span></div>
  </section>
'''

SCENE_JS = r'''
// v2: yavaş tempo — her ekranda tek fikir; öğe grupları birlikte, yumuşak (0.6 sn) gelir.
const I=(s,t,o={})=>inn(s,t,Object.assign({d:.6,y:24,e:'power3.out'},o));
const stamp=(s,t)=>tl.fromTo(s,{opacity:0,scale:1.5},{opacity:1,scale:1,duration:.3,ease:'power3.in'},t);
// S1
I('#s1g',.4);
// S2 100 nokta → 43 kırmızı (yavaş dolar)
I('#s2top',5.2); for(let i=0;i<43;i++) tl.set('#s2d'+i,{className:'dot on'},7.9+i*.025); I('#s2bot',8.2);
// S3
I('#s3g',10.5);
// S4
I('#s4g1',13.2); tl.fromTo('#s4f1',{scaleX:0},{scaleX:1,duration:1.0,ease:'power2.out'},14.9);
I('#s4r2',16.45); tl.fromTo('#s4f2',{scaleX:0},{scaleX:1,duration:.8,ease:'power2.out'},19.0);
// S5 üniversite sayısı
I('#s5g',20.45,{y:0,s:1.03}); count('#s5n',77,205,24.9,1.3,v=>Math.round(v));
// S5b mezun + işsizlik
I('#s5m',26.4); I('#s5i',29.4);
// S6 ters köşe
I('#s6g',33.65); stamp('#s6r',39.35);
// S7 ara kanca
I('#s7t',41.65);
// S8 −¼
I('#s8g',45.6);
// S9 kontrol adımları
I('#s9a',48.75); I('#s9b',53.9); I('#s9c',55.35);
// S10 CTA + döngü
stamp('#s10k',59.0); out('#s10k',62.7,.35); I('#s10a',63.1);
'''


def SFX(A):
    return [[5.2, 'paper_drop', -12, 0, 'dots'], [8.2, 'impact', -9, 1, '43'], [10.5, 'paper_drop', -12, 0, 'soru2'],
            [19.0, 'impact', -10, 1, '21'], [24.9, 'gears', -13, 0, '205'], [29.4, 'impact', -9, 1, '30'],
            [39.35, 'stamp', -8, 1, 'x'], [45.6, 'impact', -9, 1, 'ceyrek'], [55.35, 'marker', -11, 0, 'ring'],
            [59.0, 'stamp', -8, 1, 'gonder'], [67.6, 'success', -12, 0, 'loop']]


def RISERS(A): return [[10.1, 'sharp', -12], [33.3, 'metallic', -12], [45.2, 'sharp', -12]]
