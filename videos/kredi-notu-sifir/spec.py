import os
from panel_kit import JS, HERO, PIP, title, SVG_DEFS
from spec_util import load, FRAME_CSS
from visual_kit import VIS_CSS, bg_html, bg_js, card, card_js
# KREDİ NOTU SIFIR — notu olmayanın 3 yolu (düşük limit/teminatlı kart, küçük KMH, otomatik ödeme) + efsane + dürüst uyarı.
# @uzmanfinance De7B89SINIk (387K) geliştirilmiş hali. HEP VARIM (HERO + PIP) + GERÇEK GÖRSEL (Pexels).
U = load(); T = U.T; W = U.W; DUR = U.DUR
SRT = os.path.join(W, 'avatar_cut.srt')
N = lambda s: s.split()
REPL = [(N('üç yolu'), '3 yolu'), (N('bin dokuz yüze'), "1.900'e"), (N('son bir yıldır'), 'son 1 yıldır'), (N('yüzde kırk beşini'), "%45'ini"),
        (N('üç ila altı'), '3-6')]
EM = {'vermez.', 'tanımaması.', 'atlıyor.', 'istemiyor.', 'kapat.', 'belirliyor.', 'Düşmez!', 'oluşmaz.', 'gönder.'}
RED = {'Düşmez!'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False
FULLOPEN = 1.2

t2 = T('Sıfırdan') - .1; t3 = T('Önce', t2) - .1; t3b = T('Banka', T('kullanmamışsındır', t3)) - .1; t4 = T('Bir', 27) - .1; t5 = T('İki', t4) - .1
t6 = T('Üç', 50) - .1; t7 = T('Ödeme', T('talimatı', t6) + .3) - .1; t8 = T('Bir', t7 + 3) - .1; t9 = T('Findeks', t8) - .1; t10 = T('Dürüst', t9) - .1
t11 = T('İyileşmeyi', t10) - .1; t12 = T('Bunu,', t11) - .1
TS = [0, t2, t3, t3b, t4, t5, t6, t7, t8, t9, t10, t11, t12, DUR]
IDS = ['s1', 's2', 's3', 's3b', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12']
HEROS = ['s1', 's2', 's3b', 's6', 's8', 's10', 's12']


def scenes(A):
    return [(IDS[k], TS[k], TS[k + 1]) for k in range(len(IDS))]


AV = {k: (HERO if k in HEROS else PIP) for k in IDS}

EXTRA_CSS = '<style>' + FRAME_CSS + VIS_CSS + r'''
.chip{position:absolute;padding:14px 24px;border-radius:14px;font:800 34px 'Inter Tight';white-space:nowrap}
.chip.g{border:1.5px solid rgba(255,255,255,.45);background:rgba(0,0,0,.5);color:#fff}
.row{position:absolute;left:155px;width:715px;height:88px;box-sizing:border-box;display:flex;align-items:center;justify-content:space-between;padding:0 26px;
  border-radius:16px;border:1.5px solid rgba(255,255,255,.35);background:rgba(0,0,0,.55);font:800 36px 'Inter Tight';color:#fff}
.row span.k{font:600 27px 'IBM Plex Mono';color:rgba(255,255,255,.75);letter-spacing:.05em}
.big{position:absolute;left:155px;width:715px;text-align:center;font:800 110px/1 'Inter Tight';color:#fff;text-shadow:0 0 30px rgba(0,0,0,.8)}
.big small{display:block;font:700 30px 'IBM Plex Mono';letter-spacing:.08em;color:rgba(255,255,255,.75);margin-top:10px}
.gauge{position:absolute;left:155px;width:715px;height:40px;border-radius:20px;background:linear-gradient(90deg,#ff3b30,#e8b931 50%,#3ddc84);opacity:.9}
.needle{position:absolute;width:8px;height:70px;border-radius:4px;background:#fff;box-shadow:0 0 12px rgba(0,0,0,.6)}
.bar{position:absolute;left:155px;width:715px;height:70px;border-radius:14px;background:rgba(255,255,255,.12);overflow:hidden}
.bar i{position:absolute;left:0;top:0;bottom:0;width:45%;background:#e8b931;transform-origin:0 50%}
.gold{color:#e8b931} .redt{color:#ff3b30} .grn{color:#3ddc84}
</style>'''

BGS = [('bg1', 'stress.jpg', 0), ('bg2', 'counter3.jpg', 0), ('bg3', 'mob1.jpg', 1), ('bg3b', 'counter2.jpg', 0), ('bg4', 'card2.jpg', 1),
       ('bg5', 'atm.jpg', 1), ('bg6', 'mob3.jpg', 0), ('bg7', 'piggy.jpg', 1), ('bg8', 'mob1.jpg', 0), ('bg9', 'mob2.jpg', 1),
       ('bg10', 'card1.jpg', 0), ('bg11', 'counter3.jpg', 1), ('bg12', 'stress.jpg', 0)]
BGMAP = {s: b for s, b in zip(IDS, [x[0] for x in BGS])}

SCENE_HTML = bg_html(BGS) + r'''
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">''' + title('t1', 'Kredi Notun', '<i>Yoksa</i>') + r'''</section>
  <section id="s2" class="scene clip">''' + title('t2', 'Sıfırdan Not', '<i>3 Yol</i>') + r'''</section>
  <section id="s3" class="scene clip">
    ''' + title('t3', 'Findeks', '<i>Notu</i>') + r'''
    <div class="big" id="k3" style="top:450px;opacity:0"><span id="n3">0</span><small>EN YÜKSEK NOT</small></div>
    <div class="gauge" id="g3" style="top:640px;opacity:0"></div>
    <div class="needle" id="nd3" style="left:155px;top:625px;opacity:0"></div>
    <div class="row" id="r31" style="top:740px;opacity:0;border-color:rgba(255,59,48,.8)"><span class="k">NOT YOK =</span><span class="redt">kredi geçmişi yok</span></div>
    <div class="row" id="r32" style="top:840px;opacity:0"><span class="k">YA DA</span>1 yıldır kullanım yok</div>
  </section>
  <section id="s3b" class="scene clip">''' + title('t3b', 'Ölçemediği Riske', 'Limit <i>Açmıyor</i>') + r'''</section>
  <section id="s4" class="scene clip">
    ''' + title('t4', 'Yol 1', 'Düşük <i>Limitli</i> Kart') + r'''
    ''' + card('p4', 'media/card1.jpg', 450, 300, 'DÜŞÜK LİMİT') + r'''
    <div class="row" id="r41" style="top:790px;opacity:0"><span class="k">ÇIKMIYORSA</span><span class="gold">teminatlı kart sor</span></div>
    <div class="row" id="r42" style="top:890px;opacity:0"><span class="k">ÖRNEK</span>Garanti Anahtar Kart</div>
    <div class="chip g" id="c4" style="left:155px;top:1000px;opacity:0;font-size:28px">HESABINDAKİ PARA TEMİNAT</div>
  </section>
  <section id="s5" class="scene clip">
    ''' + title('t5', 'Yol 2', 'Küçük <i>KMH</i>') + r'''
    ''' + card('p5', 'media/mob2.jpg', 450, 300, 'KREDİLİ MEVDUAT HESABI') + r'''
    <div class="row" id="r51" style="top:790px;opacity:0;border-color:rgba(255,59,48,.8)"><span class="k">KULLANILAN TUTAR</span><span class="redt">faiz işler</span></div>
    <div class="row" id="r52" style="top:890px;opacity:0;border-color:rgba(61,220,132,.8)"><span class="k">KULLANIRSAN</span><span class="grn">hemen kapat</span></div>
  </section>
  <section id="s6" class="scene clip">''' + title('t6', 'Yol 3', 'Otomatik <i>Ödeme</i>') + r'''</section>
  <section id="s7" class="scene clip">
    ''' + title('t7', 'Ödeme', '<i>Geçmişi</i>') + r'''
    <div class="bar" id="br7" style="top:480px;opacity:0"><i id="bi7"></i></div>
    <div class="big" id="k7" style="top:590px;opacity:0">~%<span id="n7">0</span><small>NOTUNUN YAKLAŞIK PAYI</small></div>
  </section>
  <section id="s8" class="scene clip">''' + title('t8', 'Kendi Notuna Bakmak', 'Notu <i>Düşürmez</i>') + r'''</section>
  <section id="s9" class="scene clip">
    ''' + title('t9', 'Findeks', '<i>Her Salı</i> Ücretsiz') + r'''
    <div class="row" id="r91" style="top:470px;opacity:0;border-color:rgba(61,220,132,.8)"><span class="k">31 ARALIK'A KADAR</span><span class="grn">her salı</span></div>
    <div class="row" id="r92" style="top:570px;opacity:0;border-color:rgba(255,59,48,.8)"><span class="k">ART ARDA BAŞVURU</span><span class="redt">yapma</span></div>
  </section>
  <section id="s10" class="scene clip">''' + title('t10', 'Not Bir Gecede', '<i>Oluşmaz</i>') + r'''</section>
  <section id="s11" class="scene clip">
    ''' + title('t11', 'İyileşme', '<i>3-6 Ay</i>') + r'''
    <div class="bar" id="br11" style="top:500px;opacity:0"><i id="bi11" style="width:100%;background:linear-gradient(90deg,#ff3b30,#e8b931,#3ddc84)"></i></div>
    <div class="chip g" id="c11" style="left:155px;top:610px;opacity:0;font-size:30px">DÖNEM DÖNEM GÖRÜRSÜN</div>
  </section>
  <section id="s12" class="scene clip">''' + title('t12', 'Başvurusu Reddedilen', 'Arkadaşına <i>Gönder</i>') + r'''</section>
'''

hr = []
for sid, a, b in scenes(None):
    if sid in HEROS:
        a2 = FULLOPEN + .35 if sid == 's1' else a + .35
        if hr and a2 - hr[-1][1] < .6: hr[-1] = (hr[-1][0], b)
        else: hr.append((a2, b))


def cnt(sel, a, b, t, d=1.0):
    return (f"{{const o={{v:{a}}};tl.fromTo(o,{{v:{a}}},{{v:{b},duration:{d},ease:'power2.out',"
            f"onUpdate:()=>{{$('{sel}').textContent=Math.round(o.v).toLocaleString('tr-TR');}}}},{t:.2f});}}\n")


tb = T('bin', t3)
SCENE_JS = JS + U.frame_js(hr) + bg_js(BGMAP, scenes(None)) + f'''
tl.set('#t1',{{opacity:1}},0);
ttl('#t2',{t2 + .1});
ttl('#t3',{t3 + .1}); pop('#k3',{tb - .2}); ''' + cnt('#n3', 0, 1900, tb, 1.1) + f'''
pop('#g3',{tb}); tl.set('#nd3',{{opacity:1}},{tb}); tl.fromTo('#nd3',{{x:0}},{{x:707,duration:1.1,ease:'power2.out'}},{tb});
tl.to('#nd3',{{x:0,duration:.6,ease:'power2.in'}},{T('Notun', t3) - .2}); pop('#r31',{T('Notun', t3)}); pop('#r32',{T('ya', T('yoktur', t3))});
ttl('#t3b',{t3b + .1});
ttl('#t4',{t4 + .1}); pop('#r41',{T('Kart', t4 + 1)}); pop('#r42',{T('Mesela', t4)}); pop('#c4',{T('hesabındaki', t4)});
ttl('#t5',{t5 + .1}); pop('#r51',{T('Kullandığın', t5)}); pop('#r52',{T('kullanırsan', t5)});
ttl('#t6',{t6 + .1});
ttl('#t7',{t7 + .1}); tl.set('#br7',{{opacity:1}},{t7 + .3}); tl.fromTo('#bi7',{{scaleX:0}},{{scaleX:1,duration:1,ease:'power2.out'}},{T('yüzde', t7) - .1});
pop('#k7',{T('yüzde', t7) - .2}); ''' + cnt('#n7', 0, 45, T('yüzde', t7) - .1, 1.0) + f'''
ttl('#t8',{t8 + .1});
ttl('#t9',{t9 + .1}); pop('#r91',{T('her', t9)}); pop('#r92',{T('art', t9)});
ttl('#t10',{t10 + .1});
ttl('#t11',{t11 + .1}); tl.set('#br11',{{opacity:1}},{t11 + .3}); tl.fromTo('#bi11',{{scaleX:0}},{{scaleX:1,duration:2,ease:'power1.inOut'}},{t11 + .3}); pop('#c11',{T('dönemlerde', t11)});
ttl('#t12',{t12 + .1});
''' + card_js('p4', t4 + .15) + card_js('p5', t5 + .15)


def SFX(A):
    return [[t2, 'f:p_whoosh_bas', -11, 1, '3yol'], [t3, 'f:p_whoosh', -13, 0, 'findeks'], [tb, 'f:p_klik', -11, 0, '1900'],
            [t3b, 'f:p_whoosh_bas', -11, 1, 'risk'], [t4, 'f:p_whoosh', -13, 0, 'yol1'], [t5, 'f:p_whoosh', -13, 0, 'yol2'],
            [t6, 'f:p_boom', -10, 1, 'yol3'], [T('yüzde', t7), 'f:p_klik', -11, 0, '45'], [t8, 'f:p_whoosh_bas', -11, 1, 'efsane'],
            [T('Düşmez', t8), 'f:p_boom', -10, 1, 'dusmez'], [t9, 'f:p_whoosh', -13, 0, 'sali'], [t10, 'f:p_whoosh_bas', -11, 1, 'durust'],
            [t11, 'f:p_whoosh', -13, 0, '3-6'], [t12, 'f:p_whoosh', -13, 0, 'cta']]


def RISERS(A): return []
