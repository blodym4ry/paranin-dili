# VARYASYON v2 (kinetik) — kaynak: videos/banka-ucret-iadesi/spec.py; kanca: Hiç kullanmadığın karttan aidat kesildiyse, o para senin olabilir.
import os
from panel_kit import JS, HERO, PIP, title, SVG_DEFS
from spec_util import load, FRAME_CSS
from visual_kit import VIS_CSS, bg_html, bg_js, card, card_js
# BANKA ÜCRET İADESİ — kart aidatı için bankanın söylemediği 3 kural (BDDK ücret yönetmeliği) + kredi tahsis ücreti binde 5 + başvuru yolu.
# HEP VARIM (HERO vurgu + PIP) + GERÇEK GÖRSEL (Pexels: kart, mobil bankacılık, banka gişesi).
U = load(); T = U.T; W = U.W; DUR = U.DUR
SRT = os.path.join(W, 'avatar_cut.srt')
N = lambda s: s.split()
REPL = [(N('üç kuralı'), '3 kuralı'), (N('Yüz seksen gün'), '180 gün'), (N('binde beşini'), "binde 5'ini"), (N('İki yüz bin liralık'), '200 bin liralık'),
        (N('en fazla bin lira,'), 'en fazla 1.000 lira,'), (N('yüz seksen altı bin lira.'), '186 bin lira.'), (N('üç kurala'), '3 kurala'),
        (N('sözleşmendeyse,'), 'sözleşmende ise,')]
EM = {'söylemez.', 'zorunda.', 'alınamaz.', 'kesilemez.', 'geçemez.', 'yok.', 'bak.', 'gönder.'}
RED = {'kesilemez.'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False
FULLOPEN = 0

t2 = T('Bir', 6.11) - .1; t2b = T('Tek', t2) - .1; t3 = T('İki', t2b) - .1; t3b = T('Sözleşmende', t3) - .1; t4 = T('Aidata', t3b) - .1
t5 = T('Kredi', t4) - .1; t6 = T('Peki', t5) - .1; t7 = T('Önce', t6) - .1; t8 = T('Bu', T('Avukata', t7)) - .1; t9 = T('Kart', T('kontrol', t8)) - .1
t10 = T('Bunu,', t9) - .1
TS = [0, t2, t2b, t3, t3b, t4, t5, t6, t7, t8, t9, t10, DUR]
IDS = ['s1', 's2', 's2b', 's3', 's3b', 's4', 's5', 's6', 's7', 's8', 's9', 's10']
HEROS = ['s2b', 's3b', 's6', 's8', 's10']


def scenes(A):
    return [(IDS[k], TS[k], TS[k + 1]) for k in range(len(IDS))]


AV = {k: (HERO if k in HEROS else PIP) for k in IDS}
AV['s1'] = None   # VARYASYON: kanca avatarsız (Ata 30 Eki)

EXTRA_CSS = '<style>' + "\n.ttl .l2{background:linear-gradient(90deg,#0b3a8f,#1d5fe0)!important}\n.cl{font:italic 400 84px/1.1 'DM Serif Display'!important;letter-spacing:0!important}\n.cw{color:#ffe14d!important}\n.cw.k1{background:linear-gradient(90deg,#0b3a8f,#1d5fe0)!important;color:#fff!important}\n#t1{top:560px!important;left:110px!important;right:210px!important;font-size:66px!important;line-height:1.06}\n#t1 i{font-size:72px!important}\n#t1 .l2{margin-top:14px}\n" + FRAME_CSS + VIS_CSS + r'''
.chip{position:absolute;padding:14px 24px;border-radius:14px;font:800 34px 'Inter Tight';white-space:nowrap}
.chip.g{border:1.5px solid rgba(255,255,255,.45);background:rgba(0,0,0,.5);color:#fff}
.row{position:absolute;left:155px;width:715px;height:92px;box-sizing:border-box;display:flex;align-items:center;justify-content:space-between;padding:0 26px;
  border-radius:16px;border:1.5px solid rgba(255,255,255,.35);background:rgba(0,0,0,.55);font:800 38px 'Inter Tight';color:#fff}
.row span.k{font:600 28px 'IBM Plex Mono';color:rgba(255,255,255,.75);letter-spacing:.06em}
.big{position:absolute;left:155px;width:715px;text-align:center;font:800 104px/1 'Inter Tight';color:#fff;text-shadow:0 0 30px rgba(0,0,0,.8)}
.big small{display:block;font:700 30px 'IBM Plex Mono';letter-spacing:.08em;color:rgba(255,255,255,.75);margin-top:10px}
.step{position:absolute;left:155px;width:715px;height:110px;box-sizing:border-box;border-radius:18px;display:flex;align-items:center;gap:22px;padding:0 26px;
  background:rgba(0,0,0,.55);border:1.5px solid rgba(255,255,255,.4);font:800 36px 'Inter Tight';color:#fff}
.step b{font:800 26px 'IBM Plex Mono';letter-spacing:.08em;color:#e8b931;min-width:70px}
.arr{position:absolute;left:497px;width:30px;height:34px;background:#e8b931;clip-path:polygon(0 0,100% 0,50% 100%)}
.num{position:absolute;left:155px;top:450px;width:110px;height:110px;border-radius:50%;background:#e8b931;color:#111;font:800 64px/110px 'Inter Tight';text-align:center}
.gold{color:#e8b931} .redt{color:#ff3b30} .grn{color:#3ddc84}
</style>'''

BGS = [('bg1', 'stress.jpg', 0), ('bg2', 'card2.jpg', 1), ('bg2b', 'card2.jpg', 0), ('bg3', 'atm.jpg', 1), ('bg3b', 'counter3.jpg', 0),
       ('bg4', 'counter3.jpg', 1), ('bg5', 'piggy.jpg', 1), ('bg6', 'stress.jpg', 0), ('bg7', 'counter2.jpg', 1), ('bg8', 'mob1.jpg', 0),
       ('bg9', 'card1.jpg', 1), ('bg10', 'card1.jpg', 0)]
BGMAP = {s: b for s, b in zip(IDS, [x[0] for x in BGS])}

SCENE_HTML = bg_html(BGS) + r'''
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">''' + title('t1', 'Kullanmadığın Karttan', '<i>Aidat</i> mı Kesildi?') + r'''</section>
  <section id="s2" class="scene clip">
    ''' + title('t2', 'Kural 1', '<i>Ücretsiz</i> Kart') + r'''
    ''' + card('p2', 'media/card1.jpg', 450, 330, 'ÜCRETSİZ KREDİ KARTI') + r'''
    <div class="row" id="r21" style="top:810px;opacity:0"><span class="k">BANKA SUNMAK</span><span class="gold">zorunda</span></div>
    <div class="row" id="r22" style="top:915px;opacity:0"><span class="k">GEÇİŞTE LİMİT</span><span class="grn">aynı kalır</span></div>
  </section>
  <section id="s2b" class="scene clip">''' + title('t2b', 'Tek Fark', 'Taksit ya da <i>Puan</i>') + r'''</section>
  <section id="s3" class="scene clip">
    ''' + title('t3', 'Kullanmadığın Karta', '<i>Aidat Yok</i>') + r'''
    <div class="row" id="r31" style="top:470px;opacity:0"><span class="k">HİÇ KULLANILMADI</span><span class="grn">aidat yok</span></div>
    <div class="big" id="k3" style="top:620px;opacity:0"><span id="n3">0</span> GÜN<small>HAREKETSİZ KART</small></div>
    <div class="row" id="r32" style="top:830px;opacity:0"><span class="k">180 GÜN HAREKETSİZ</span><span class="grn">aidat yok</span></div>
  </section>
  <section id="s3b" class="scene clip">''' + title('t3b', 'Sözleşmede Yoksa', '<i>Kesilemez</i>') + r'''</section>
  <section id="s4" class="scene clip">
    ''' + title('t4', 'Kural 3', 'Aidat <i>Zammı</i>') + r'''
    ''' + card('p4', 'media/mob2.jpg', 450, 330, 'YILLIK KART ÜCRETİ') + r'''
    <div class="row" id="r41" style="top:810px;opacity:0;border-color:rgba(232,185,49,.8)"><span class="k">ZAM TAVANI</span><span class="gold">yıllık enflasyon</span></div>
    <div class="chip g" id="c4" style="left:155px;top:925px;opacity:0;font-size:28px">GEÇEN YIL SONU AÇIKLANAN</div>
  </section>
  <section id="s5" class="scene clip">
    ''' + title('t5', 'Kredi', '<i>Tahsis</i> Ücreti') + r'''
    <div class="row" id="r51" style="top:460px;opacity:0;border-color:rgba(232,185,49,.8)"><span class="k">TAVAN</span><span class="gold">anaparanın binde 5'i</span></div>
    ''' + card('p5', 'media/mob3.jpg', 575, 260, 'KREDİ ÇEKERKEN') + r'''
    <div class="row" id="r52" style="top:860px;opacity:0"><span class="k">200.000 TL KREDİ</span><span>en fazla <span class="gold" id="n5">0</span> TL</span></div>
    <div class="chip g" id="c5" style="left:155px;top:970px;opacity:0;font-size:28px">+ VERGİ</div>
  </section>
  <section id="s6" class="scene clip">''' + title('t6', 'Fazla Kesildiyse', '<i>Ne Yapacaksın?</i>') + r'''</section>
  <section id="s7" class="scene clip">
    ''' + title('t7', 'Başvuru', '<i>Yolu</i>') + r'''
    <div class="step" id="st1" style="top:450px;opacity:0"><b>1</b>Bankaya yazılı başvur</div>
    <div class="arr" id="ar1" style="top:575px;opacity:0"></div>
    <div class="step" id="st2" style="top:625px;opacity:0"><b>2</b>Merkez Bankası</div>
    <div class="step" id="st3" style="top:750px;opacity:0"><b>2</b>e-Devlet · Hakem Heyeti</div>
    <div class="chip g" id="c71" style="left:155px;top:895px;opacity:0;font-size:32px;border-color:#e8b931;color:#e8b931">2026 SINIRI · 186.000 TL</div>
    <div class="chip g" id="c72" style="left:155px;top:990px;opacity:0;font-size:32px">AVUKAT GEREKMEZ</div>
  </section>
  <section id="s8" class="scene clip">''' + title('t8', 'Bu Akşam', '<i>Ekstrene</i> Bak') + r'''</section>
  <section id="s9" class="scene clip">
    ''' + title('t9', 'Dürüst', '<i>Uyarı</i>') + r'''
    <div class="row" id="r91" style="top:470px;opacity:0"><span class="k">KART KULLANILDI</span>✓</div>
    <div class="row" id="r92" style="top:575px;opacity:0"><span class="k">ÜCRET SÖZLEŞMEDE</span>✓</div>
    <div class="row" id="r93" style="top:680px;opacity:0;border-color:rgba(255,59,48,.8)"><span class="k">İADE HAKKI</span><span class="redt">olmayabilir</span></div>
  </section>
  <section id="s10" class="scene clip">''' + title('t10', 'Aidata Söylenen', 'Arkadaşına <i>Gönder</i>') + r'''</section>
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


ty = T('Yüz', t3)
SCENE_JS = JS + U.frame_js(hr) + bg_js(BGMAP, scenes(None)) + f'''
tl.set('#t1',{{opacity:1}},0);
ttl('#t2',{t2 + .1}); pop('#r21',{T('sunmak', t2)}); pop('#r22',{T('limitin', t2)});
ttl('#t2b',{t2b + .1});
ttl('#t3',{t3 + .1}); pop('#r31',{T('alınamaz', t3) - .3}); pop('#k3',{ty - .1}); ''' + cnt('#n3', 0, 180, ty, 1.0) + f'''
pop('#r32',{T('alınamaz', ty) - .3});
ttl('#t3b',{t3b + .1});
ttl('#t4',{t4 + .1}); pop('#r41',{T('enflasyonu', t4) - .3}); pop('#c4',{T('geçemez', t4)});
ttl('#t5',{t5 + .1}); pop('#r51',{T('anaparanın', t5)}); pop('#r52',{T('İki', t5) - .1}); ''' + cnt('#n5', 0, 1000, T('fazla', t5), .8) + f'''
pop('#c5',{T('artı', t5)});
ttl('#t6',{t6 + .1});
ttl('#t7',{t7 + .1}); pop('#st1',{t7 + .2}); pop('#ar1',{T('Sonuç', t7) - .2}); pop('#st2',{T('Merkez', t7)}); pop('#st3',{T('tüketici', t7) - .3});
pop('#c71',{T('sınır', t7)}); pop('#c72',{T('Avukata', t7)});
ttl('#t8',{t8 + .1});
ttl('#t9',{t9 + .1}); pop('#r91',{t9 + .2}); pop('#r92',{T('ücret', t9)}); pop('#r93',{T('iade', t9)});
ttl('#t10',{t10 + .1});
''' + card_js('p2', t2 + .15) + card_js('p4', t4 + .15) + card_js('p5', T('Kredi', t5 + 1) - .2)


def SFX(A):
    return [[t2, 'f:p_whoosh', -13, 0, 'kural1'], [t2b, 'f:p_whoosh_bas', -11, 1, 'fark'], [t3, 'f:p_whoosh', -13, 0, 'kural2'],
            [ty, 'f:p_klik', -11, 0, '180'], [t3b, 'f:p_boom', -10, 1, 'kesilemez'], [t4, 'f:p_whoosh', -13, 0, 'kural3'],
            [t5, 'f:p_whoosh', -13, 0, 'tahsis'], [T('fazla', t5), 'f:p_klik', -11, 0, '1000'], [t6, 'f:p_whoosh_bas', -11, 1, 'peki'],
            [t7, 'f:p_whoosh', -13, 0, 'basvuru'], [t8, 'f:p_whoosh_bas', -11, 1, 'ekstre'], [t9, 'f:p_whoosh', -13, 0, 'uyari'],
            [t10, 'f:p_whoosh', -13, 0, 'cta']]


def RISERS(A): return []
