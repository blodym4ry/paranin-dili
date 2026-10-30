# VARYASYON v3 (manset) — kaynak: videos/internet-faturasi-btk/spec.py; kanca: İzmir'de bir abone, ödediği cayma bedelini geri aldı.
import os
from panel_kit import JS, HERO, PIP, title, SVG_DEFS
from spec_util import load, FRAME_CSS
from visual_kit import VIS_CSS, bg_html, bg_js, card, card_js
# İNTERNET TAAHHÜDÜ — hız gelmiyorsa cezasız fesih (BTK Hız Testi + adrese dayalı kriter), cayma bedeli tavanı, şikâyet yolu, İzmir hakem heyeti örneği.
# HEP VARIM (HERO vurgu + PIP) + GERÇEK GÖRSEL (Pexels: modem, telefon).
U = load(); T = U.T; W = U.W; DUR = U.DUR
SRT = os.path.join(W, 'avatar_cut.srt')
N = lambda s: s.split()
REPL = [(N("Beteka'nın"), "BTK'nın"), (N('Beteka Hız Testi.'), 'BTK Hız Testi.'), (N('on iş günü'), '10 iş günü'),
        (N('yüz seksen altı bin lira.'), '186 bin lira.'), (N('dört bin iki yüz on bir lira!'), '4.211 lira!')]
EM = {'yok.', 'yok!', 'o!', 'zorunda.', 'lira!', 'belirler.', 'gönder.'}
RED = {'yok!'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False
FULLOPEN = 0

t2 = T('Bir', 4.88) - .1; t3 = T('İki', t2) - .1; t3b = T('Cayma', t3) - .1; t4 = T('Üç', t3b) - .1; t4b = T('Hangisi', t4) - .1
t5 = T('Peki', t4b) - .1; t6 = T('Önce', t5) - .1; t6b = T('Bu', T('başvur', t6)) - .1; t7 = T('Bu', t6b + 1) - .1; t7b = T('Tam', t7) - .1
t8 = T('Dürüst', t7b) - .1; t9 = T('Sadece', t8) - .1; t10 = T('Bunu,', t9) - .1
TS = [0, t2, t3, t3b, t4, t4b, t5, t6, t6b, t7, t7b, t8, t9, t10, DUR]
IDS = ['s1', 's2', 's3', 's3b', 's4', 's4b', 's5', 's6', 's6b', 's7', 's7b', 's8', 's9', 's10']
HEROS = ['s10']


def scenes(A):
    return [(IDS[k], TS[k], TS[k + 1]) for k in range(len(IDS))]


AV = {k: (HERO if k in HEROS else PIP) for k in IDS}
AV['s1'] = None   # VARYASYON: kanca avatarsız (Ata 30 Eki)

EXTRA_CSS = '<style>' + '\n.ttl .l2{background:#f4f1ea!important;color:#0d0c0a!important;border-left:14px solid #d81e1e}\n.ttl .l2 i{color:#b01212}\n#t1{top:520px!important;left:120px!important;right:220px!important;padding:30px 24px 36px;background:rgba(244,241,234,.97);color:#0d0c0a!important;\n  border-top:16px solid #d81e1e;border-radius:6px;box-shadow:0 30px 70px rgba(0,0,0,.7);text-shadow:none!important;font-size:60px!important}\n#t1 i{font-size:66px!important;color:#fff!important}\n#t1 .l2{background:#d81e1e!important;color:#fff!important;border-left:0}\n' + FRAME_CSS + VIS_CSS + r'''
.chip{position:absolute;padding:14px 24px;border-radius:14px;font:800 34px 'Inter Tight';white-space:nowrap}
.chip.g{border:1.5px solid rgba(255,255,255,.45);background:rgba(0,0,0,.5);color:#fff}
.row{position:absolute;left:155px;width:715px;height:92px;box-sizing:border-box;display:flex;align-items:center;justify-content:space-between;padding:0 26px;
  border-radius:16px;border:1.5px solid rgba(255,255,255,.35);background:rgba(0,0,0,.55);font:800 38px 'Inter Tight';color:#fff}
.row span.k{font:600 28px 'IBM Plex Mono';color:rgba(255,255,255,.75);letter-spacing:.06em}
.big{position:absolute;left:155px;width:715px;text-align:center;font:800 110px/1 'Inter Tight';color:#fff;text-shadow:0 0 30px rgba(0,0,0,.8)}
.big small{display:block;font:700 30px 'IBM Plex Mono';letter-spacing:.08em;color:rgba(255,255,255,.75);margin-top:10px}
.step{position:absolute;left:155px;width:715px;height:104px;box-sizing:border-box;border-radius:18px;display:flex;align-items:center;gap:22px;padding:0 26px;
  background:rgba(0,0,0,.55);border:1.5px solid rgba(255,255,255,.4);font:800 36px 'Inter Tight';color:#fff}
.step b{font:800 26px 'IBM Plex Mono';letter-spacing:.08em;color:#e8b931;min-width:70px}
.arr{position:absolute;left:497px;width:30px;height:30px;background:#e8b931;clip-path:polygon(0 0,100% 0,50% 100%)}
.bar{position:absolute;left:155px;height:70px;border-radius:14px;transform-origin:0 50%;display:flex;align-items:center;padding-left:22px;box-sizing:border-box;font:800 32px 'Inter Tight';color:#111}
.lab{font:600 28px 'IBM Plex Mono';color:rgba(255,255,255,.8);letter-spacing:.06em}
.gold{color:#e8b931} .redt{color:#ff3b30} .grn{color:#3ddc84}
</style>'''

BGS = [('bg1', 'router2.jpg', 0), ('bg2', 'router3.jpg', 1), ('bg3', 'phone.jpg', 1), ('bg3b', 'router1.jpg', 0), ('bg4', 'mob1.jpg', 1),
       ('bg4b', 'router3.jpg', 0), ('bg5', 'waiting.jpg', 0), ('bg6', 'counter.jpg', 1), ('bg6b', 'counter.jpg', 0), ('bg7', 'router2.jpg', 1),
       ('bg7b', 'router1.jpg', 0), ('bg8', 'waiting.jpg', 0), ('bg9', 'phone.jpg', 1), ('bg10', 'router2.jpg', 0)]
BGMAP = {s: b for s, b in zip(IDS, [x[0] for x in BGS])}

SCENE_HTML = bg_html(BGS) + r'''
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">''' + title('t1', "İzmir'de Bir Abone", 'Parasını <i>Geri Aldı</i>') + r'''</section>
  <section id="s2" class="scene clip">
    ''' + title('t2', 'Adım 1', 'Resmi Araçla <i>Ölç</i>') + r'''
    ''' + card('p2', 'media/router2.jpg', 450, 280, 'BTK HIZ TESTİ') + r'''
    <div class="row" id="r21" style="top:760px;opacity:0"><span class="k">BAĞLANTI</span>Kabloyla</div>
    <div class="row" id="r22" style="top:865px;opacity:0"><span class="k">ZAMAN</span>Farklı gün + saat</div>
    <div class="row" id="r23" style="top:970px;opacity:0;border-color:rgba(232,185,49,.8)"><span class="k">KANIT</span><span class="gold">Ekran görüntüsü</span></div>
  </section>
  <section id="s3" class="scene clip">
    ''' + title('t3', 'Adım 2', '<i>Kriterin</i> Altında mı?') + r'''
    ''' + card('p3', 'media/phone.jpg', 450, 300, 'ADRESE DAYALI KRİTER') + r'''
    <div class="row" id="r31" style="top:790px;opacity:0;border-color:rgba(61,220,132,.8)"><span class="k">ALTINDAYSA</span><span class="grn">taahhüdü bozabilirsin</span></div>
  </section>
  <section id="s3b" class="scene clip">''' + title('t3b', 'Cayma Bedeli', '<i>Yok!</i>') + r'''</section>
  <section id="s4" class="scene clip">
    ''' + title('t4', 'Cayma Bedelinin', '<i>Tavanı</i> Var') + r'''
    <div class="lab" style="position:absolute;left:155px;top:450px">O GÜNE KADARKİ İNDİRİM</div>
    <div class="bar" id="b41" style="top:490px;width:715px;background:rgba(255,255,255,.85);opacity:0"></div>
    <div class="lab" style="position:absolute;left:155px;top:590px">KALAN AYLARIN TOPLAMI</div>
    <div class="bar" id="b42" style="top:630px;width:460px;background:rgba(255,255,255,.85);opacity:0"></div>
    <div class="chip g" id="c4" style="left:155px;top:740px;opacity:0;font-size:34px;border-color:#e8b931;color:#e8b931">EN FAZLA: HANGİSİ DÜŞÜKSE</div>
  </section>
  <section id="s4b" class="scene clip">''' + title('t4b', 'Hangisi Düşükse', '<i>O!</i>') + r'''</section>
  <section id="s5" class="scene clip">''' + title('t5', 'Operatör', '<i>Yanaşmazsa?</i>') + r'''</section>
  <section id="s6" class="scene clip">
    ''' + title('t6', 'Şikâyet', '<i>Yolu</i>') + r'''
    <div class="step" id="st1" style="top:450px;opacity:0"><b>1</b>Yazılı şikâyet et</div>
    <div class="arr" id="ar1" style="top:565px;opacity:0"></div>
    <div class="step" id="st2" style="top:605px;opacity:0"><b>10</b>İş günü içinde çözmeli</div>
    <div class="arr" id="ar2" style="top:720px;opacity:0"></div>
    <div class="step" id="st3" style="top:760px;opacity:0;border-color:rgba(232,185,49,.8)"><b>2</b>e-Devlet · Hakem Heyeti</div>
  </section>
  <section id="s6b" class="scene clip">''' + title('t6b', '186 Bin TL\'ye Kadar', 'Ücret <i>Yok</i>') + r'''</section>
  <section id="s7" class="scene clip">
    ''' + title('t7', 'Bu Yaz', '<i>İzmir</i>') + r'''
    ''' + card('p7', 'media/router1.jpg', 450, 300, 'İNTERNET SÜREKLİ KOPTU') + r'''
    <div class="row" id="r71" style="top:790px;opacity:0"><span class="k">ÖDEDİĞİ CAYMA BEDELİ</span><span class="grn">geri</span></div>
    <div class="big" id="k7" style="top:910px;opacity:0;font-size:90px"><span id="n7">0</span> TL</div>
  </section>
  <section id="s7b" class="scene clip">''' + title('t7b', 'Hakem Heyetinden', '<i>4.211 TL</i> Geri') + r'''</section>
  <section id="s8" class="scene clip">''' + title('t8', 'Dürüst', '<i>Olayım</i>') + r'''</section>
  <section id="s9" class="scene clip">
    ''' + title('t9', 'Tek Başına', '<i>Yetmeyebilir</i>') + r'''
    <div class="row" id="r91" style="top:470px;opacity:0;border-color:rgba(255,59,48,.8)"><span class="k">TARİFE HIZININ ALTI</span><span class="redt">yetmeyebilir</span></div>
    <div class="row" id="r92" style="top:575px;opacity:0"><span class="k">BEDELDEN İNDİRİM</span>istenebilir</div>
    <div class="row" id="r93" style="top:680px;opacity:0;border-color:rgba(232,185,49,.8)"><span class="k">ORANI</span><span class="gold">hakem heyeti</span></div>
  </section>
  <section id="s10" class="scene clip">''' + title('t10', 'Modemi Kapatıp Açan', 'Arkadaşına <i>Gönder</i>') + r'''</section>
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


tk = T('Kalan', t4)
SCENE_JS = JS + U.frame_js(hr) + bg_js(BGMAP, scenes(None)) + f'''
tl.set('#t1',{{opacity:1}},0);
ttl('#t2',{t2 + .1}); pop('#r21',{T('Kabloyla', t2)}); pop('#r22',{T('farklı', t2)}); pop('#r23',{T('ekran', t2)});
ttl('#t3',{t3 + .1}); pop('#r31',{T('taahhüdü', t3)});
ttl('#t3b',{t3b + .1});
ttl('#t4',{t4 + .1}); tl.set('#b41',{{opacity:1}},{T('O', t4) - .1}); tl.fromTo('#b41',{{scaleX:0}},{{scaleX:1,duration:.7,ease:'power2.out'}},{T('O', t4) - .1});
tl.set('#b42',{{opacity:1}},{tk - .1}); tl.fromTo('#b42',{{scaleX:0}},{{scaleX:1,duration:.7,ease:'power2.out'}},{tk - .1});
tl.to('#b42',{{background:'#e8b931',duration:.3}},{T('Hangisi', t4) - .4}); pop('#c4',{T('Hangisi', t4) - .4});
ttl('#t4b',{t4b + .1}); ttl('#t5',{t5 + .1});
ttl('#t6',{t6 + .1}); pop('#st1',{t6 + .2}); pop('#ar1',{T('Operatör', t6) - .2}); pop('#st2',{T('Operatör', t6)}); pop('#ar2',{T('Çözmezse', t6) - .2}); pop('#st3',{T('Çözmezse', t6)});
ttl('#t6b',{t6b + .1});
ttl('#t7',{t7 + .1}); pop('#r71',{T('Ödediği', t7)}); pop('#k7',{T('geri', t7)}); ''' + cnt('#n7', 0, 4211, T('geri', t7), 1.0) + f'''
ttl('#t7b',{t7b + .1}); ttl('#t8',{t8 + .1});
ttl('#t9',{t9 + .1}); pop('#r91',{t9 + .3}); pop('#r92',{T('Bedelden', t9)}); pop('#r93',{T('oranı', t9)});
ttl('#t10',{t10 + .1});
''' + card_js('p2', t2 + .15) + card_js('p3', t3 + .15) + card_js('p7', t7 + .15)


def SFX(A):
    return [[t2, 'f:p_whoosh', -13, 0, 'olc'], [t3, 'f:p_whoosh', -13, 0, 'kriter'], [t3b, 'f:p_boom', -10, 1, 'caymayok'],
            [t4, 'f:p_whoosh', -13, 0, 'tavan'], [t4b, 'f:p_whoosh_bas', -11, 1, 'dusuk'], [t5, 'f:p_whoosh', -13, 0, 'operator'],
            [t6, 'f:p_whoosh', -13, 0, 'sikayet'], [t6b, 'f:p_whoosh_bas', -11, 1, '186'], [t7, 'f:p_whoosh', -13, 0, 'izmir'],
            [T('geri', t7), 'f:p_klik', -11, 0, '4211'], [t7b, 'f:p_boom', -10, 1, 'geri'], [t8, 'f:p_whoosh_bas', -11, 1, 'durust'],
            [t10, 'f:p_whoosh', -13, 0, 'cta']]


def RISERS(A): return []
