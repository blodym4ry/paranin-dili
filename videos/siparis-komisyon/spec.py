import os
from panel_kit import JS, HERO, PIP, title, SVG_DEFS
from spec_util import load, FRAME_CSS
from visual_kit import VIS_CSS, bg_html, bg_js, card, card_js
# SİPARİŞ KOMİSYONU — 1.000 TL siparişin restorana kalanı (TÜRES hesabı: %32 komisyon + KDV → 616, kampanyayla 516), ev maliyeti farkı, gel-al çözümü.
# HEP VARIM (HERO vurgu + PIP) + GERÇEK GÖRSEL (Pexels: kurye, paket, restoran mutfağı).
U = load(); T = U.T; W = U.W; DUR = U.DUR
SRT = os.path.join(W, 'avatar_cut.srt')
N = lambda s: s.split()
REPL = [(N('bin liranın'), '1.000 liranın'), (N('bin liralık'), '1.000 liralık'), (N('yüzde otuz iki'), '%32'), (N('altı yüz on altı lira'), '616 lira'),
        (N('beş yüz on altıya'), "516'ya"), (N('beş yüz yirmi beş lira.'), '525 lira.'), (N('iki yüz liraya'), '200 liraya'), (N('Haftada iki'), 'Haftada 2'),
        (N('otuz dört bin liraya'), '34 bin liraya'), (N('yüzde yirmi'), '%20'), (N("Türes'in"), "TÜRES'in"), (N('Türes'), 'TÜRES')]
EM = {'kalmıyor.', 'gidiyor?', 'söylüyor.', 'ödüyor!', 'yetebilir.', 'bedava.', 'ulaşmıyor.'}
RED = {'ödüyor!'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False
FULLOPEN = 1.2

t2 = T('Restoran', 9) - .1; t3 = T('Dernek,', t2) - .1; t4 = T('Uygulamada', t3) - .1; t5 = T('Haftada', t4) - .1; t6 = T('Siparişi', t5) - .1
t7 = T('Söylemeden', t6) - .1; t8 = T('Bunu,', t7) - .1
TS = [0, t2, t3, t4, t5, t6, t7, t8, DUR]
IDS = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8']
HEROS = ['s1', 's3', 's5', 's6', 's8']


def scenes(A):
    return [(IDS[k], TS[k], TS[k + 1]) for k in range(len(IDS))]


AV = {k: (HERO if k in HEROS else PIP) for k in IDS}

EXTRA_CSS = '<style>' + FRAME_CSS + VIS_CSS + r'''
.chip{position:absolute;padding:14px 24px;border-radius:14px;font:800 34px 'Inter Tight';white-space:nowrap}
.chip.g{border:1.5px solid rgba(255,255,255,.45);background:rgba(0,0,0,.5);color:#fff}
.row{position:absolute;left:155px;width:715px;height:88px;box-sizing:border-box;display:flex;align-items:center;justify-content:space-between;padding:0 26px;
  border-radius:16px;border:1.5px solid rgba(255,255,255,.35);background:rgba(0,0,0,.55);font:800 38px 'Inter Tight';color:#fff}
.row span.k{font:600 28px 'IBM Plex Mono';color:rgba(255,255,255,.75);letter-spacing:.06em}
.big{position:absolute;left:155px;width:715px;text-align:center;font:800 110px/1 'Inter Tight';color:#fff;text-shadow:0 0 30px rgba(0,0,0,.8)}
.big small{display:block;font:700 30px 'IBM Plex Mono';letter-spacing:.08em;color:rgba(255,255,255,.75);margin-top:10px}
.step{position:absolute;left:155px;width:715px;height:104px;box-sizing:border-box;border-radius:18px;display:flex;align-items:center;gap:22px;padding:0 26px;
  background:rgba(0,0,0,.55);border:1.5px solid rgba(255,255,255,.4);font:800 34px 'Inter Tight';color:#fff}
.step b{font:800 26px 'IBM Plex Mono';letter-spacing:.08em;color:#e8b931;min-width:40px}
.arr{position:absolute;left:497px;width:30px;height:30px;background:#e8b931;clip-path:polygon(0 0,100% 0,50% 100%)}
.wf{position:absolute;left:155px;width:715px;height:46px;border-radius:12px;background:rgba(255,255,255,.12);overflow:hidden}
.wf i{position:absolute;left:0;top:0;bottom:0;background:#3ddc84;transform-origin:0 50%}
.gold{color:#e8b931} .redt{color:#ff3b30} .grn{color:#3ddc84}
</style>'''

BGS = [('bg1', 'courier1.jpg', 0), ('bg2', 'deliv2.jpg', 1), ('bg3', 'kitchen2.jpg', 0), ('bg4', 'kitchen1.jpg', 1), ('bg5', 'courier2.jpg', 0),
       ('bg6', 'courier3.jpg', 0), ('bg7', 'kitchen3.jpg', 1), ('bg8', 'deliv1.jpg', 0)]
BGMAP = {s: b for s, b in zip(IDS, [x[0] for x in BGS])}

SCENE_HTML = bg_html(BGS) + r'''
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">''' + title('t1', '1.000 TL Siparişin', '<i>Yarısı</i> Nereye?') + r'''</section>
  <section id="s2" class="scene clip">
    ''' + title('t2', 'TÜRES', '<i>Hesabı</i>') + r'''
    ''' + card('p2', 'media/deliv2.jpg', 450, 230, '1.000 TL SİPARİŞ') + r'''
    <div class="row" id="r21" style="top:705px;opacity:0"><span class="k">KOMİSYON %32</span><span class="redt">−320</span></div>
    <div class="row" id="r22" style="top:803px;opacity:0"><span class="k">KOMİSYONUN KDV'Sİ</span><span class="redt">−64</span></div>
    <div class="wf" id="wf" style="top:910px;opacity:0"><i id="wfi" style="width:100%"></i></div>
    <div class="big" id="k2" style="top:975px;opacity:0;font-size:84px"><span id="n2">1.000</span> TL<small>RESTORANA KALAN</small></div>
  </section>
  <section id="s3" class="scene clip">''' + title('t3', 'Kesinti Menüye', '<i>Yansıyor</i>') + r'''</section>
  <section id="s4" class="scene clip">
    ''' + title('t4', 'Aynı Yemek', '<i>İki Fiyat</i>') + r'''
    ''' + card('p4', 'media/kitchen2.jpg', 450, 300, 'TAVUK GÜVEÇ') + r'''
    <div class="row" id="r41" style="top:790px;opacity:0;border-color:rgba(255,59,48,.8)"><span class="k">UYGULAMADA · ZİNCİR</span><span class="redt">525 TL</span></div>
    <div class="row" id="r42" style="top:893px;opacity:0;border-color:rgba(61,220,132,.8)"><span class="k">EVDE · MALZEME</span><span class="grn">~200 TL</span></div>
  </section>
  <section id="s5" class="scene clip">''' + title('t5', 'Yılda ~34 Bin TL', '<i>Fark</i>') + r'''</section>
  <section id="s6" class="scene clip">''' + title('t6', 'Bırakma', 'Kanalı <i>Değiştir</i>') + r'''</section>
  <section id="s7" class="scene clip">
    ''' + title('t7', 'Gel-Al', '<i>Taktiği</i>') + r'''
    <div class="step" id="st1" style="top:450px;opacity:0"><b>1</b>Uygulamadaki fiyatı not al</div>
    <div class="arr" id="ar1" style="top:565px;opacity:0"></div>
    <div class="step" id="st2" style="top:605px;opacity:0"><b>2</b>Restoranı ara, gel-al fiyatı?</div>
    <div class="chip g" id="c7" style="left:155px;top:750px;opacity:0;font-size:30px;border-color:#e8b931;color:#e8b931">TÜRES · DOĞRUDAN SİPARİŞE %20 ÇAĞRISI</div>
    <div class="chip g" id="c7b" style="left:155px;top:845px;opacity:0;font-size:30px">HER YERDE GEÇERLİ DEĞİL · SORMAK BEDAVA</div>
  </section>
  <section id="s8" class="scene clip">''' + title('t8', 'Hep Uygulamacı', 'Arkadaşına <i>Gönder</i>') + r'''</section>
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


tk = T('yüzde', t2); tv = T('katma', t2); tr = T('Restorana', t2); tc = T('beş', t2)
SCENE_JS = JS + U.frame_js(hr) + bg_js(BGMAP, scenes(None)) + f'''
tl.set('#t1',{{opacity:1}},0);
ttl('#t2',{t2 + .1}); pop('#wf',{t2 + .4}); pop('#k2',{t2 + .4});
pop('#r21',{tk}); tl.to('#wfi',{{scaleX:.68,duration:.6,ease:'power2.out'}},{tk + .2}); ''' + cnt('#n2', 1000, 680, tk + .2, .6) + f'''
pop('#r22',{tv}); tl.to('#wfi',{{scaleX:.616,duration:.5,ease:'power2.out'}},{tv + .2}); ''' + cnt('#n2', 680, 616, tv + .2, .5) + f'''
tl.to('#k2',{{scale:1.08,duration:.2,yoyo:true,repeat:1}},{tr});
tl.to('#wfi',{{scaleX:.516,background:'#e8b931',duration:.5,ease:'power2.out'}},{tc}); ''' + cnt('#n2', 616, 516, tc, .6) + f'''
ttl('#t3',{t3 + .1});
ttl('#t4',{t4 + .1}); pop('#r41',{T('beş', t4)}); pop('#r42',{T('Evde', t4)});
ttl('#t5',{t5 + .1}); ttl('#t6',{t6 + .1});
ttl('#t7',{t7 + .1}); pop('#st1',{t7 + .2}); pop('#ar1',{T('Restoranı', t7) - .2}); pop('#st2',{T('Restoranı', t7)}); pop('#c7',{T('Türes', t7)}); pop('#c7b',{T('Her', t7)});
ttl('#t8',{t8 + .1});
''' + card_js('p2', t2 + .15) + card_js('p4', t4 + .15)


def SFX(A):
    return [[t2, 'f:p_whoosh', -13, 0, 'tures'], [tk, 'f:p_klik', -11, 0, '32'], [tv, 'f:p_klik', -11, 0, 'kdv'], [tc, 'f:p_klik', -11, 0, '516'],
            [t3, 'f:p_whoosh_bas', -11, 1, 'yansiyor'], [t4, 'f:p_whoosh', -13, 0, 'tavuk'], [t5, 'f:p_boom', -10, 1, '34bin'],
            [t6, 'f:p_whoosh_bas', -11, 1, 'kanal'], [t7, 'f:p_whoosh', -13, 0, 'gelal'], [t8, 'f:p_whoosh', -13, 0, 'cta']]


def RISERS(A): return []
