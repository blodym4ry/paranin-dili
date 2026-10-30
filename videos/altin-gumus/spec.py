import os
from panel_kit import JS, HERO, PIP, title, SVG_DEFS
from spec_util import load, FRAME_CSS
from visual_kit import VIS_CSS, bg_html, bg_js, card, card_js
# GÜMÜŞ MAKASI — gümüş zirveden ~%56 düştü (altın ~%26); 1. neden sanayi/güneş paneli talebi, 2. rakam kuyumcu alış-satış makası (%1 vs %10'a kadar).
# HEP VARIM (HERO + PIP) + GERÇEK GÖRSEL (Pexels: gümüş külçe/sikke, altın, Kapalıçarşı, kuyumcu vitrini).
U = load(); T = U.T; W = U.W; DUR = U.DUR
SRT = os.path.join(W, 'avatar_cut.srt')
N = lambda s: s.split()
REPL = [(N('iki kat'), '2 kat'), (N('iki rakamda.'), '2 rakamda.'), (N('yüz yirmi bir doları'), '121 doları'), (N('elli üç doların'), '53 doların'),
        (N('dörtte bir'), '1/4'), (N('yüzde on dokuz'), '%19'), (N('yüzde bir civarı.'), '%1 civarı.'), (N('yüzde ona'), "%10'a"),
        (N('Yüz bin liralık'), '100 bin liralık'), (N('doksan bin'), '90 bin'), (N('iki fiyatı'), '2 fiyatı'), (N('iki kez'), '2 kez')]
EM = {'düştü!', 'sormaz.', 'indi!', 'yok…', 'çıkabiliyor!', 'kalabilir.', 'bu.', 'tezgâhta.', 'gelmesin.'}
RED = {'çıkabiliyor!', 'kalabilir.'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False
FULLOPEN = 1.2

t2 = T('Ocakta', 9) - .1; t3 = T('Bir', T('düştü', t2 + 6)) - .1; t3b = T('Ama', t3) - .1; t4 = T('Kapalıçarşı', t3b) - .1; t5 = T('Yüz', T('çıkabiliyor', t4)) - .1
t5b = T('Çoğu', t5) - .1; t6 = T('Almadan', t5b) - .1; t7 = T('Yani', t6) - .1; t8 = T('Bunu,', t7) - .1
TS = [0, t2, t3, t3b, t4, t5, t5b, t6, t7, t8, DUR]
IDS = ['s1', 's2', 's3', 's3b', 's4', 's5', 's5b', 's6', 's7', 's8']
HEROS = ['s1', 's3b', 's5b', 's7', 's8']


def scenes(A):
    return [(IDS[k], TS[k], TS[k + 1]) for k in range(len(IDS))]


AV = {k: (HERO if k in HEROS else PIP) for k in IDS}

EXTRA_CSS = '<style>' + FRAME_CSS + VIS_CSS + r'''
.chip{position:absolute;padding:14px 24px;border-radius:14px;font:800 34px 'Inter Tight';white-space:nowrap}
.chip.g{border:1.5px solid rgba(255,255,255,.45);background:rgba(0,0,0,.5);color:#fff}
.row{position:absolute;left:155px;width:715px;height:88px;box-sizing:border-box;display:flex;align-items:center;justify-content:space-between;padding:0 26px;
  border-radius:16px;border:1.5px solid rgba(255,255,255,.35);background:rgba(0,0,0,.55);font:800 38px 'Inter Tight';color:#fff}
.row span.k{font:600 28px 'IBM Plex Mono';color:rgba(255,255,255,.75);letter-spacing:.06em}
.big{position:absolute;left:155px;width:715px;text-align:center;font:800 104px/1 'Inter Tight';color:#fff;text-shadow:0 0 30px rgba(0,0,0,.8)}
.big small{display:block;font:700 30px 'IBM Plex Mono';letter-spacing:.08em;color:rgba(255,255,255,.75);margin-top:10px}
.bar{position:absolute;left:155px;height:66px;border-radius:14px;transform-origin:0 50%;display:flex;align-items:center;padding-left:22px;box-sizing:border-box;font:800 34px 'Inter Tight';color:#111}
.lab{font:600 28px 'IBM Plex Mono';color:rgba(255,255,255,.8);letter-spacing:.06em}
.frm{position:absolute;left:155px;width:715px;box-sizing:border-box;padding:26px;border-radius:18px;background:rgba(0,0,0,.6);border:1.5px solid rgba(232,185,49,.8);
  font:800 44px/1.25 'Inter Tight';color:#fff;text-align:center}
.frm hr{border:0;border-top:3px solid #fff;margin:14px 80px}
.gold{color:#e8b931} .redt{color:#ff3b30} .grn{color:#3ddc84} .slv{color:#d8dde3}
</style>'''

BGS = [('bg1', 'silver1.jpg', 0), ('bg2', 'chart1.jpg', 1), ('bg3', 'factory2.jpg', 1), ('bg3b', 'jewel2.jpg', 0), ('bg4', 'bazaar1.jpg', 1),
       ('bg5', 'silverbar2.jpg', 1), ('bg5b', 'jewel1.jpg', 0), ('bg6', 'bazaar2.jpg', 1), ('bg7', 'silver2.jpg', 0), ('bg8', 'bazaar1.jpg', 0)]
BGMAP = {s: b for s, b in zip(IDS, [x[0] for x in BGS])}

SCENE_HTML = bg_html(BGS) + r'''
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">''' + title('t1', 'Fakirin Altını', '<i>2 Kat</i> Sert Düştü') + r'''</section>
  <section id="s2" class="scene clip">
    ''' + title('t2', 'Ocak → Ekim', '<i>Gümüş</i> vs Altın') + r'''
    ''' + card('p2', 'media/silver2.jpg', 450, 240, 'GÜMÜŞ · ONS') + r'''
    <div class="big" id="k2" style="top:715px;opacity:0;font-size:90px">$<span id="n2">121</span></div>
    <div class="lab" style="position:absolute;left:155px;top:840px">GÜMÜŞ · ZİRVEDEN</div>
    <div class="bar" id="b21" style="top:880px;width:715px;background:#d8dde3;opacity:0">−%56</div>
    <div class="lab" style="position:absolute;left:155px;top:965px">ALTIN · AYNI SÜREDE</div>
    <div class="bar" id="b22" style="top:1005px;width:330px;background:#e8b931;opacity:0">~−%26</div>
  </section>
  <section id="s3" class="scene clip">
    ''' + title('t3', 'Neden 1', '<i>Sanayi</i>') + r'''
    ''' + card('p3', 'media/factory2.jpg', 450, 300, 'EN BÜYÜK ALICI: SANAYİ') + r'''
    <div class="row" id="r31" style="top:790px;opacity:0"><span class="k">GÜNEŞ PANELİ</span>gümüşü azaltıyor</div>
    <div class="row" id="r32" style="top:893px;opacity:0;border-color:rgba(255,59,48,.8)"><span class="k">2026 TALEBİ</span><span class="redt">−%19</span></div>
  </section>
  <section id="s3b" class="scene clip">''' + title('t3b', 'İkinci Rakam', 'Ekranda <i>Yok</i>') + r'''</section>
  <section id="s4" class="scene clip">
    ''' + title('t4', 'Alış-Satış', '<i>Makası</i>') + r'''
    ''' + card('p4', 'media/bazaar1.jpg', 450, 260, 'KAPALIÇARŞI') + r'''
    <div class="lab" style="position:absolute;left:155px;top:745px">GRAM ALTIN</div>
    <div class="bar" id="b41" style="top:785px;width:110px;background:#e8b931;opacity:0">%1</div>
    <div class="lab" style="position:absolute;left:155px;top:870px">KÜLÇE GÜMÜŞ</div>
    <div class="bar" id="b42" style="top:910px;width:715px;background:#ff3b30;opacity:0;color:#fff">%10'a kadar</div>
  </section>
  <section id="s5" class="scene clip">
    ''' + title('t5', 'Aynı Gün', '<i>Geri Satsan</i>') + r'''
    ''' + card('p5', 'media/silverbar2.jpg', 450, 300, 'KÜLÇE GÜMÜŞ') + r'''
    <div class="big" id="k5" style="top:800px;opacity:0;font-size:96px"><span id="n5">100.000</span> TL</div>
    <div class="chip g" id="c5" style="left:155px;top:930px;opacity:0;font-size:36px;border-color:#ff3b30;color:#ff3b30">−10.000 TL · TEZGÂHTA</div>
  </section>
  <section id="s5b" class="scene clip">''' + title('t5b', 'Sadece Satış Fiyatına', '<i>Bakma</i>') + r'''</section>
  <section id="s6" class="scene clip">
    ''' + title('t6', 'Makas', '<i>Formülü</i>') + r'''
    <div class="frm" id="f6" style="top:460px;opacity:0">(Satış − Alış)<hr>Satış</div>
    <div class="row" id="r61" style="top:720px;opacity:0"><span class="k">ÖRNEK</span>(100 − 90) ÷ 100</div>
    <div class="row" id="r62" style="top:823px;opacity:0;border-color:rgba(255,59,48,.8)"><span class="k">ÖDEDİĞİN MAKAS</span><span class="redt">%10</span></div>
  </section>
  <section id="s7" class="scene clip">''' + title('t7', 'Fiyatta ve', '<i>Tezgâhta</i>') + r'''</section>
  <section id="s8" class="scene clip">''' + title('t8', 'Gümüş Almaya Giden', 'Arkadaşına <i>Gönder</i>') + r'''</section>
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


te = T('Ekimde', t2); ta = T('Altın', te)
SCENE_JS = JS + U.frame_js(hr) + bg_js(BGMAP, scenes(None)) + f'''
tl.set('#t1',{{opacity:1}},0);
ttl('#t2',{t2 + .1}); pop('#k2',{T('yüz', t2) - .2}); ''' + cnt('#n2', 121, 53, te + .5, 1.0) + f'''
tl.set('#b21',{{opacity:1}},{te + .5}); tl.fromTo('#b21',{{scaleX:0}},{{scaleX:1,duration:.8,ease:'power2.out'}},{te + .5});
tl.set('#b22',{{opacity:1}},{ta}); tl.fromTo('#b22',{{scaleX:0}},{{scaleX:1,duration:.7,ease:'power2.out'}},{ta});
ttl('#t3',{t3 + .1}); pop('#r31',{T('Güneş', t3)}); pop('#r32',{T('yüzde', t3)});
ttl('#t3b',{t3b + .1});
ttl('#t4',{t4 + .1}); tl.set('#b41',{{opacity:1}},{T('yüzde', t4) - .1}); tl.fromTo('#b41',{{scaleX:0}},{{scaleX:1,duration:.5}},{T('yüzde', t4) - .1});
tl.set('#b42',{{opacity:1}},{T('yüzde', T('Külçe', t4)) - .1}); tl.fromTo('#b42',{{scaleX:0}},{{scaleX:1,duration:.9,ease:'power2.out'}},{T('yüzde', T('Külçe', t4)) - .1});
ttl('#t5',{t5 + .1}); pop('#k5',{t5 + .3}); ''' + cnt('#n5', 100000, 90000, T('doksan', t5) - .2, .8) + f'''
pop('#c5',{T('doksan', t5) + .5});
ttl('#t5b',{t5b + .1});
ttl('#t6',{t6 + .1}); pop('#f6',{T('Satıştan', t6) - .1}); pop('#r61',{T('Sonucu', t6)}); pop('#r62',{T('Ödediğin', t6)});
ttl('#t7',{t7 + .1}); ttl('#t8',{t8 + .1});
''' + card_js('p2', t2 + .15) + card_js('p3', t3 + .15) + card_js('p4', t4 + .15) + card_js('p5', t5 + .15)


def SFX(A):
    return [[t2, 'f:p_whoosh', -13, 0, 'ocak'], [te + .5, 'f:p_klik', -11, 0, '53'], [t3, 'f:p_whoosh', -13, 0, 'sanayi'],
            [t3b, 'f:p_whoosh_bas', -11, 1, 'ikinci'], [t4, 'f:p_whoosh', -13, 0, 'makas'], [T('Külçe', t4), 'f:p_boom', -10, 1, '10'],
            [t5, 'f:p_whoosh', -13, 0, 'geri'], [T('doksan', t5), 'f:p_klik', -11, 0, '90'], [t5b, 'f:p_whoosh_bas', -11, 1, 'hata'],
            [t6, 'f:p_whoosh', -13, 0, 'formul'], [t7, 'f:p_boom', -10, 1, 'ikikez'], [t8, 'f:p_whoosh', -13, 0, 'cta']]


def RISERS(A): return []
