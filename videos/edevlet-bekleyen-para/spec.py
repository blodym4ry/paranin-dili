import os
from panel_kit import JS, HERO, PIP, title, SVG_DEFS
from spec_util import load, FRAME_CSS
from visual_kit import VIS_CSS, bg_html, bg_js, card, card_js
# E-DEVLET BEKLEYEN PARA — unutulan hesap/hisse/dijital cüzdan için 3 e-Devlet sorgusu (TMSF devri, YTM, TCMB ödeme kuruluşu sorgusu).
# HEP VARIM (HERO vurgu + PIP) + GERÇEK GÖRSEL (Pexels: kumbara, banka gişesi, mobil bankacılık, borsa ekranı).
U = load(); T = U.T; W = U.W; DUR = U.DUR
SRT = os.path.join(W, 'avatar_cut.srt')
N = lambda s: s.split()
REPL = [(N('on yıl'), '10 yıl'), (N('İki bin yirmi beşte'), "2025'te"), (N('yedi yüz otuz iki milyon lira'), '732 milyon lira'),
        (N("Temesefe'ye"), "TMSF'ye"), (N('İki milyondan'), '2 milyondan'), (N('Üç sorgu'), '3 sorgu'), (N("On beş Haziran'a"), "15 Haziran'a"),
        (N('Son iki sorgu'), 'Son 2 sorgu')]
EM = {'çıkabilir.', 'hesap!', "e-Devlet'te.", 'yok.', 'var!', 'dönüyor.', 'istiyorsun.', 'gönder.'}
RED = {'yok.'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False
FULLOPEN = 1.2

t2 = T('İki', 7) - .1; t3 = T('Üç', t2) - .1; t4 = T('Bir', 17) - .1; t4b = T('Sonra', T('kurtuluyor', t4)) - .1; t5 = T('İki', t4b) - .1
t5b = T('Burada', t5) - .1; t5c = T('Hissen', t5b) - .1; t6 = T('Üç', t5c) - .1; t7 = T('Son', t6) - .1; t8 = T('Dürüst', t7) - .1
t9 = T('Bir', t8) - .1; t10 = T('Bunu,', t9) - .1
TS = [0, t2, t3, t4, t4b, t5, t5b, t5c, t6, t7, t8, t9, t10, DUR]
IDS = ['s1', 's2', 's3', 's4', 's4b', 's5', 's5b', 's5c', 's6', 's7', 's8', 's9', 's10']
HEROS = ['s1', 's3', 's4b', 's5b', 's8', 's10']


def scenes(A):
    return [(IDS[k], TS[k], TS[k + 1]) for k in range(len(IDS))]


AV = {k: (HERO if k in HEROS else PIP) for k in IDS}

EXTRA_CSS = '<style>' + FRAME_CSS + VIS_CSS + r'''
.chip{position:absolute;padding:14px 24px;border-radius:14px;font:800 34px 'Inter Tight';white-space:nowrap}
.chip.g{border:1.5px solid rgba(255,255,255,.45);background:rgba(0,0,0,.5);color:#fff}
.row{position:absolute;left:155px;width:715px;height:92px;box-sizing:border-box;display:flex;align-items:center;justify-content:space-between;padding:0 26px;
  border-radius:16px;border:1.5px solid rgba(255,255,255,.35);background:rgba(0,0,0,.55);font:800 38px 'Inter Tight';color:#fff}
.row span.k{font:600 28px 'IBM Plex Mono';color:rgba(255,255,255,.75);letter-spacing:.06em}
.big{position:absolute;left:155px;width:715px;text-align:center;font:800 110px/1 'Inter Tight';color:#fff;text-shadow:0 0 30px rgba(0,0,0,.8)}
.big small{display:block;font:700 30px 'IBM Plex Mono';letter-spacing:.08em;color:rgba(255,255,255,.75);margin-top:10px}
.step{position:absolute;left:155px;width:715px;height:104px;box-sizing:border-box;border-radius:18px;display:flex;align-items:center;gap:22px;padding:0 26px;
  background:rgba(0,0,0,.55);border:1.5px solid rgba(255,255,255,.4);font:800 36px 'Inter Tight';color:#fff}
.step b{font:800 26px 'IBM Plex Mono';letter-spacing:.08em;color:#e8b931;min-width:150px}
.arr{position:absolute;left:497px;width:30px;height:30px;background:#e8b931;clip-path:polygon(0 0,100% 0,50% 100%)}
.gold{color:#e8b931} .redt{color:#ff3b30} .grn{color:#3ddc84}
</style>'''

BGS = [('bg1', 'piggy.jpg', 0), ('bg2', 'counter.jpg', 1), ('bg3', 'phone.jpg', 0), ('bg4', 'mob2.jpg', 1), ('bg4b', 'atm.jpg', 0),
       ('bg5', 'chart2.jpg', 1), ('bg5b', 'chart1.jpg', 0), ('bg5c', 'chart2.jpg', 1), ('bg6', 'mob3.jpg', 1), ('bg7', 'istanbul.jpg', 1),
       ('bg8', 'piggy.jpg', 0), ('bg9', 'counter.jpg', 1), ('bg10', 'chart1.jpg', 0)]
BGMAP = {s: b for s, b in zip(IDS, [x[0] for x in BGS])}

SCENE_HTML = bg_html(BGS) + r'''
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">''' + title('t1', 'Adına', 'Unutulan <i>Para</i>') + r'''</section>
  <section id="s2" class="scene clip">
    ''' + title('t2', '2025\'te', '<i>TMSF\'ye</i> Geçti') + r'''
    <div class="big" id="k2" style="top:480px;opacity:0"><span id="n2">0</span><small>MİLYON TL · 10 YIL DOKUNULMAYAN</small></div>
    <div class="chip g" id="c2" style="left:155px;top:690px;opacity:0;font-size:40px;border-color:#e8b931;color:#e8b931">2 MİLYONDAN FAZLA HESAP</div>
    ''' + card('p2', 'media/counter.jpg', 800, 260, 'BANKA HESAPLARI') + r'''
  </section>
  <section id="s3" class="scene clip">''' + title('t3', '3 Sorgu', 'Üçü de <i>e-Devlet\'te</i>') + r'''</section>
  <section id="s4" class="scene clip">
    ''' + title('t4', 'Sorgu 1', '<i>Banka</i> Hesabın') + r'''
    ''' + card('p4', 'media/mob1.jpg', 450, 230, 'TMSF\'YE DEVREDİLECEK HESAPLAR') + r'''
    <div class="step" id="st1" style="top:700px;opacity:0"><b>ŞUBAT</b>Yeni liste çıkar</div>
    <div class="arr" id="ar1" style="top:812px;opacity:0"></div>
    <div class="step" id="st2" style="top:850px;opacity:0;border-color:rgba(61,220,132,.8)"><b>15 HAZİRAN</b><span class="grn">Bankana git, kurtar</span></div>
    <div class="arr" id="ar2" style="top:962px;opacity:0"></div>
    <div class="step" id="st3" style="top:1000px;opacity:0;border-color:rgba(255,59,48,.85)"><b style="color:#ff3b30">SONRA</b><span class="redt">Fona gelir yazılır</span></div>
  </section>
  <section id="s4b" class="scene clip">''' + title('t4b', 'Geri Alma', '<i>Garantisi Yok</i>') + r'''</section>
  <section id="s5" class="scene clip">
    ''' + title('t5', 'Sorgu 2', 'Hisse ve <i>Fon</i>') + r'''
    ''' + card('p5', 'media/chart2.jpg', 450, 300, 'ARACI KURUMDA UNUTULAN YATIRIM') + r'''
    <div class="row" id="r51" style="top:790px;opacity:0"><span class="k">10 YIL SONRA</span><span class="gold">Yatırımcı Tazmin Merkezi</span></div>
  </section>
  <section id="s5b" class="scene clip">''' + title('t5b', 'Burada', 'İyi <i>Haber</i> Var') + r'''</section>
  <section id="s5c" class="scene clip">
    ''' + title('t5c', 'Geri', '<i>Alınabiliyor</i>') + r'''
    <div class="row" id="r52" style="top:470px;opacity:0"><span class="k">HİSSE</span><span class="grn">geri döner</span></div>
    <div class="row" id="r53" style="top:575px;opacity:0"><span class="k">NAKİT</span><span class="grn">nemasıyla döner</span></div>
  </section>
  <section id="s6" class="scene clip">
    ''' + title('t6', 'Sorgu 3', 'Dijital <i>Cüzdanlar</i>') + r'''
    ''' + card('p6', 'media/mob3.jpg', 450, 300, 'MERKEZ BANKASI · YENİ SORGU') + r'''
    <div class="row" id="r61" style="top:790px;opacity:0"><span class="k">ÖDEME KURULUŞLARI</span><span class="grn">listelenir</span></div>
    <div class="row" id="r62" style="top:895px;opacity:0;border-color:rgba(255,59,48,.8)"><span class="k">BAKİYE</span><span class="redt">gösterilmez</span></div>
  </section>
  <section id="s7" class="scene clip">
    ''' + title('t7', 'Vefat Eden', '<i>Yakının</i> Adına') + r'''
    <div class="row" id="r71" style="top:470px;opacity:0"><span class="k">SORGU 2 · HİSSE / FON</span><span class="grn">✓</span></div>
    <div class="row" id="r72" style="top:575px;opacity:0"><span class="k">SORGU 3 · DİJİTAL CÜZDAN</span><span class="grn">✓</span></div>
  </section>
  <section id="s8" class="scene clip">''' + title('t8', 'Dürüst', '<i>Olayım</i>') + r'''</section>
  <section id="s9" class="scene clip">
    ''' + title('t9', 'Hisse İadesi', 'Başvurusu') + r'''
    <div class="row" id="r91" style="top:470px;opacity:0;border-color:rgba(255,59,48,.8)"><span class="k">E-DEVLET</span><span class="redt">şimdilik yok</span></div>
    <div class="row" id="r92" style="top:575px;opacity:0;border-color:rgba(232,185,49,.8)"><span class="k">YTM'YE POSTA İLE</span><span class="gold">✓</span></div>
    <div class="chip g" id="c9" style="left:155px;top:700px;opacity:0;font-size:28px">ÇOĞU KİŞİNİN LİSTESİ BOŞ ÇIKAR</div>
  </section>
  <section id="s10" class="scene clip">''' + title('t10', 'Hisse Alıp Unutan', 'Arkadaşına <i>Gönder</i>') + r'''</section>
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


ty = T('yedi', t2)
SCENE_JS = JS + U.frame_js(hr) + bg_js(BGMAP, scenes(None)) + f'''
tl.set('#t1',{{opacity:1}},0);
ttl('#t2',{t2 + .1}); pop('#k2',{ty - .2}); ''' + cnt('#n2', 0, 732, ty, 1.1) + f'''
pop('#c2',{T('milyondan', t2) - .2});
ttl('#t3',{t3 + .1});
ttl('#t4',{t4 + .1}); pop('#st1',{T('Yeni', t4)}); pop('#ar1',{T('On', t4) - .2}); pop('#st2',{T('On', t4)}); pop('#ar2',{T('Sonra', t4) - .5}); pop('#st3',{T('Sonra', t4) - .3});
ttl('#t4b',{t4b + .1});
ttl('#t5',{t5 + .1}); pop('#r51',{T('Yatırımcı', t5)});
ttl('#t5b',{t5b + .1});
ttl('#t5c',{t5c + .1}); pop('#r52',{t5c + .2}); pop('#r53',{T('Nakit', t5c)});
ttl('#t6',{t6 + .1}); pop('#r61',{T('ödeme', t6)}); pop('#r62',{T('Bakiyeyi', t6)});
ttl('#t7',{t7 + .1}); pop('#r71',{t7 + .3}); pop('#r72',{t7 + .6});
ttl('#t8',{t8 + .1});
ttl('#t9',{t9 + .1}); pop('#r91',{T('şimdilik', t9)}); pop('#r92',{T('Yatırımcı', t9)}); pop('#c9',{T('posta', t9)});
ttl('#t10',{t10 + .1});
''' + card_js('p2', T('İki', t2 + 3) - .2) + card_js('p4', t4 + .15) + card_js('p5', t5 + .15) + card_js('p6', t6 + .15)


def SFX(A):
    return [[t2, 'f:p_whoosh', -13, 0, 'tmsf'], [ty, 'f:p_klik', -11, 0, '732'], [t3, 'f:p_whoosh_bas', -11, 1, '3sorgu'],
            [t4, 'f:p_whoosh', -13, 0, 'sorgu1'], [t4b, 'f:p_boom', -10, 1, 'garantiyok'], [t5, 'f:p_whoosh', -13, 0, 'sorgu2'],
            [t5b, 'f:p_whoosh_bas', -11, 1, 'iyihaber'], [t6, 'f:p_whoosh', -13, 0, 'sorgu3'], [t7, 'f:p_klik', -12, 0, 'vefat'],
            [t8, 'f:p_whoosh_bas', -11, 1, 'durust'], [t9, 'f:p_whoosh', -13, 0, 'posta'], [t10, 'f:p_whoosh', -13, 0, 'cta']]


def RISERS(A): return []
