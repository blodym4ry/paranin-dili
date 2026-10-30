import os
from panel_kit import JS, HERO, title, SVG_DEFS
from spec_util import load, FRAME_CSS
# BINANCE HACK (29 Eki 2026) · PANEL + kısa tam ekran açılış (FULLOPEN) + altın çerçeveli avatar. Güvenli alan v2 (x 100–880, y 220–1440).
# Kaynaklar: kaynaklar.md · Telaffuz: Baynens / Eteryum / Teter / Sörkıl / Ripıl (Ata 30 Eki)
U = load(); T = U.T; W = U.W; DUR = U.DUR
SRT = os.path.join(W, 'avatar_cut.srt')
N = lambda *w: list(w)
REPL = [(N("Baynens'ten"), "Binance'ten"), (N("Eteryum'a"), "Ethereum'a"), (N("Baynens'in"), "Binance'in"), (N('Baynens,'), 'Binance,'), (N('Baynens'), 'Binance'),
        (N('Eteryum'), 'Ethereum'), (N('Teter,'), 'Tether,'), (N('Sörkıl'), 'Circle'), (N('Ripıl,'), 'Ripple,'),
        (N('iki', 'milyar', 'dolar'), '2 milyar $'), (N('bir', 'virgül', 'altı', 'milyar', 'dolarlık'), '1,6 milyar $\'lık'),
        (N('yüz', 'altmış', 'yedi', 'bin'), '167 bin'), (N('iki', 'buçuk', 'ile', 'altı', 'milyar', 'dolar'), '2,5–6 milyar $'),
        (N('iki', 'buçuk', 'milyarı'), '2,5 milyarı'), (N('yarım', 'milyar', 'dolardan'), 'yarım milyar $\'dan')]
EM = {'çıktı.', 'altında!', 'imza', 'boşaltıldı.', 'dondurdu!', 'dondurulamıyor.', 'tut.', 'gönder.'}
RED = {'altında!', 'boşaltıldı.', 'dondurulamıyor.', 'kapalı.'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False
FULLOPEN = 1.2   # Ata 29 Eki: tam ekran sadece kanca başında, sonra karta küçül

a1, b1 = U.seg(0); a5, b5 = U.seg(1); a9, _ = U.seg(2)
tP = T('Perşembe', 3); tBu = T('yetki', tP + 1); tU = T('Üç', tBu + 1); tTa = T('Resmi', tU + 3); tKr = T('Kripto', tTa + 1)
tC = T('Çünkü', b5 - .3); tAy = T('Aynı', tC + 1); tE = T('Eteryum', tAy + 1); tB = T('Baynens', tE + 2); tI = T('İki', tB + 2); tUz = T('Uzun', tI + 1)


def scenes(A):
    return [('s1', 0, b1), ('s2', b1, tU - .1), ('s3', tU - .1, tTa - .1), ('s4', tTa - .1, a5), ('s5', a5, b5),
            ('s6', b5, tE - .1), ('s7', tE - .1, tB - .1), ('s8', tB - .1, tI - .1), ('s9', tI - .1, a9), ('s10', a9, DUR)]


AV = {'s1': HERO, 's2': None, 's3': None, 's4': None, 's5': HERO, 's6': None, 's7': None, 's8': None, 's9': None, 's10': HERO}

EXTRA_CSS = '<style>' + FRAME_CSS + r'''
.chip{position:absolute;padding:14px 26px;border-radius:14px;font:800 38px 'Inter Tight';white-space:nowrap}
.chip.g{border:1.5px solid rgba(255,255,255,.45);background:rgba(255,255,255,.04);color:#fff}
.dc{position:absolute;left:150px;width:730px;border-radius:18px;padding:20px 28px;border:1.5px solid rgba(255,255,255,.4);background:rgba(255,255,255,.03)}
.dc .q{font:700 30px 'Inter Tight';color:rgba(255,255,255,.7);letter-spacing:.04em}
.dc .r{font:800 44px 'Inter Tight';margin-top:6px}
.wal{position:absolute;width:300px;height:220px;border-radius:22px;border:2px solid rgba(255,255,255,.45);background:rgba(255,255,255,.035);
  display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:10px}
.wal .lab{font-size:22px}
.wal .nm{font:800 40px 'Inter Tight'}
.arr{position:absolute;height:6px;background:linear-gradient(90deg,rgba(255,255,255,.2),#ff3b30);transform-origin:0 50%;border-radius:3px}
.tx{position:absolute;left:150px;width:730px;border-radius:20px;border:1.5px solid rgba(255,255,255,.4);background:rgba(255,255,255,.03);padding:22px 28px}
.tx .row{display:flex;justify-content:space-between;font:600 30px 'IBM Plex Mono';color:rgba(255,255,255,.75);padding:8px 0;border-bottom:1px solid rgba(255,255,255,.08)}
.tx .row b{color:#fff;font-weight:700}
.bar{position:absolute;border-radius:0 14px 14px 0;transform-origin:0 50%}
.ice{border-color:#7fd3ff!important;color:#bfe9ff!important;box-shadow:0 0 26px rgba(127,211,255,.35)}
.gold{color:#e8b931}
</style>'''

SCENE_HTML = r'''
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">''' + title('t1', 'Tek İşlemde', '<i>2 Milyar $</i> Çıktı') + r'''</section>
  <section id="s2" class="scene clip">
    ''' + title('t2', 'Tek Bir', '<i>İmza</i>') + r'''
    <div class="lab" id="l2" style="position:absolute;left:0;right:0;top:470px;text-align:center;opacity:0">29 EKİM · 23:20:59 (TSİ)</div>
    <div class="wal" id="w21" style="left:130px;top:560px;opacity:0"><div class="lab">BINANCE</div><div class="nm">SICAK<br>CÜZDAN</div></div>
    <div class="arr" id="a2" style="left:440px;top:668px;width:150px"></div>
    <div class="wal" id="w22" style="left:600px;top:560px;width:280px;opacity:0;border-color:#ff3b30"><div class="lab">KONTROL</div><div class="nm" style="color:#ff3b30">SALDIRGANIN<br>KODU</div></div>
    <div class="chip g" id="c2" style="left:190px;top:850px;opacity:0;font-size:32px">TEK İMZA = CÜZDANIN KONTROLÜ</div>
  </section>
  <section id="s3" class="scene clip">
    ''' + title('t3', 'Tek İşlemde', '<i>Boşaltıldı</i>') + r'''
    <div class="gbox" id="b3" style="left:240px;top:460px;width:600px;height:200px"><div class="lab" style="margin-bottom:10px">İMZADAN SONRA</div>
      <div class="num glowt" style="font-size:110px"><span id="n3">00:00</span></div></div>
    <div class="tx" id="x3" style="top:700px;opacity:0">
      <div class="row"><span>DİJİTAL DOLAR</span><b>1,615 MİLYAR $</b></div>
      <div class="row"><span>ETHEREUM</span><b>167.464</b></div>
      <div class="row"><span>+ 63 FARKLI TOKEN</span><b>TEK İŞLEM</b></div>
      <div class="row" style="border:0"><span>İŞLEM ÜCRETİ</span><b class="redt">1 $ BİLE DEĞİL</b></div></div>
  </section>
  <section id="s4" class="scene clip">
    ''' + title('t4', 'Kripto Tarihinin', 'En Büyük <i>Soygunu?</i>') + r'''
    <div class="lab" style="position:absolute;left:150px;top:470px">BINANCE · TAHMİN ARALIĞI</div>
    <div class="bar" id="h41" style="left:150px;top:510px;height:100px;width:420px;background:linear-gradient(90deg,#ff3b30,rgba(255,59,48,.5))"></div>
    <div class="bar" id="h42" style="left:570px;top:510px;height:100px;width:310px;background:repeating-linear-gradient(45deg,rgba(255,59,48,.35) 0 14px,rgba(255,59,48,.12) 14px 28px)"></div>
    <div class="a num" id="v41" style="left:170px;top:625px;font-size:56px;opacity:0">2,5 – 6 MİLYAR $</div>
    <div class="lab" style="position:absolute;left:150px;top:760px">ÖNCEKİ REKOR · BYBIT · ŞUBAT 2025</div>
    <div class="bar" id="h43" style="left:150px;top:800px;height:100px;width:230px;background:linear-gradient(90deg,rgba(255,255,255,.85),rgba(255,255,255,.25))"></div>
    <div class="a num" id="v43" style="left:400px;top:812px;font-size:56px;opacity:0">1,5 MİLYAR $</div>
    <div class="lab" id="l4" style="position:absolute;left:150px;top:950px;opacity:0;font-size:22px">KESİN RAKAM HENÜZ AÇIKLANMADI</div>
  </section>
  <section id="s5" class="scene clip">''' + title('t5', 'Tether · Circle · Ripple', '<i>Dondurdu</i>') + r'''</section>
  <section id="s6" class="scene clip">
    ''' + title('t6', 'Paranın', '<i>Düğmesi</i>') + r'''
    <div class="chip g ice" id="c61" style="left:150px;top:460px;opacity:0">TETHER · 1,57 MİLYAR $</div>
    <div class="chip g ice" id="c62" style="left:150px;top:570px;opacity:0">CIRCLE · 0,8 MİLYAR $</div>
    <div class="chip g ice" id="c63" style="left:150px;top:680px;opacity:0">RIPPLE · ~0,2 MİLYAR $</div>
    <div class="rbox" id="r6" style="left:150px;top:810px;width:730px;height:120px;border-radius:20px;font-size:52px;opacity:0">≈ 2,5 MİLYAR $ DONDU</div>
    <div class="dc" id="d6" style="top:980px;opacity:0"><div class="q">AYNI DÜĞME</div><div class="r">Senin dijital dolarında da <span class="gold">var</span></div></div>
  </section>
  <section id="s7" class="scene clip">
    ''' + title('t7', 'Ethereum', '<i>Dondurulamaz</i>') + r'''
    <div class="gbox" id="b7" style="left:170px;top:470px;width:710px;height:320px"><div class="lab" style="margin-bottom:14px">HÂLÂ SALDIRGANDA</div>
      <div class="num glowt redt" style="font-size:110px">> 0,5 MİLYAR $</div><div class="lab" style="margin-top:14px">PARA HIZLA ETHEREUM'A ÇEVRİLİYOR</div></div>
  </section>
  <section id="s8" class="scene clip">
    ''' + title('t8', 'Binance', 'Ne <i>Dedi?</i>') + r'''
    <div class="dc" id="d81" style="top:460px;opacity:0"><div class="q">BINANCE</div><div class="r">"Kullanıcı fonları <span class="gold">güvende</span>"</div></div>
    <div class="dc" id="d82" style="top:640px;opacity:0"><div class="q">ORTAK CEO YI HE</div><div class="r">Tüm kaybı <span class="gold">Binance karşılayacak</span></div></div>
    <div class="dc" id="d83" style="top:820px;opacity:0;border-color:rgba(255,59,48,.7)"><div class="q">BU ARADA</div><div class="r">Para çekme <span class="redt">şu an kapalı</span></div></div>
  </section>
  <section id="s9" class="scene clip">
    ''' + title('t9', 'Senin İçin', '<i>İki</i> Ders') + r'''
    <div class="dc" id="d91" style="top:460px;opacity:0;border-color:rgba(255,59,48,.7)"><div class="q">1 · SAHTE MESAJ</div><div class="r">"Fonunu geri al" linkine <span class="redt">tıklama</span></div></div>
    <div class="dc" id="d92" style="top:680px;opacity:0"><div class="q">2 · UZUN VADELİ BİRİKİM</div><div class="r">Anahtarı <span class="gold">sende olan</span> cüzdanda</div></div>
  </section>
  <section id="s10" class="scene clip">''' + title('t10', 'Kriptosu Borsadaki', 'Arkadaşına <i>Gönder</i>') + r'''</section>
'''

SCENE_JS = JS + U.frame_js([(FULLOPEN + .35, b1), (a5, b5), (a9, DUR)]) + f'''
tl.set('#t1',{{opacity:1}},0);
ttl('#t2',{b1 + .1}); fin('#l2',{tP + .2}); pop('#w21',{T('sıcak', tP)}); tl.fromTo('#a2',{{scaleX:0}},{{scaleX:1,duration:.5,ease:'power3.out'}},{tBu});
pop('#w22',{T('kontrolünü', tBu)}); pop('#c2',{T('verdi', tBu) + .2});
ttl('#t3',{tU}); {{const o={{v:0}};tl.to(o,{{v:204,duration:1.4,ease:'power2.out',onUpdate:()=>{{const s=Math.round(o.v);$('#n3').textContent=String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0');}}}},{tU + .1});}}
pop('#x3',{T('tek', tU)});
ttl('#t4',{tTa}); tl.fromTo('#h41',{{scaleX:0}},{{scaleX:1,duration:.7,ease:'power3.out'}},{tTa + .3}); tl.fromTo('#h42',{{scaleX:0}},{{scaleX:1,duration:.6,ease:'power3.out'}},{T('altı', tTa)});
pop('#v41',{T('altı', tTa) + .3}); tl.fromTo('#h43',{{scaleX:0}},{{scaleX:1,duration:.6,ease:'power3.out'}},{tKr}); pop('#v43',{tKr + .4}); fin('#l4',{tKr + 1.2});
ttl('#t5',{a5 + .1});
ttl('#t6',{b5 + .1}); pop('#c61',{b5 + .3}); pop('#c62',{b5 + .8}); pop('#c63',{b5 + 1.3}); pop('#r6',{T('şirketlerin', tC)}); pop('#d6',{tAy});
ttl('#t7',{tE}); pop('#b7',{T('yarım', tE)});
ttl('#t8',{tB}); pop('#d81',{T('güvende', tB)}); pop('#d82',{T('kaybı', tB)}); pop('#d83',{T('Ama', tB)});
ttl('#t9',{tI}); pop('#d91',{T('fonunu', tI)}); pop('#d92',{tUz});
ttl('#t10',{a9 + .1});
'''


def SFX(A):
    return [[b1 + .05, 'f:p_whoosh', -13, 0, 'imza'], [tBu, 'f:p_klik', -11, 0, 'ok'], [tU - .1, 'f:p_whoosh_bas', -11, 1, 'bosalt'],
            [tU + 1.5, 'f:p_boom', -10, 1, '0324'], [tTa - .1, 'f:p_whoosh', -13, 0, 'tahmin'], [tKr, 'f:p_klik', -11, 0, 'bybit'],
            [a5, 'f:p_whoosh_bas', -11, 1, 'ilginc'], [b5 + .05, 'f:p_whoosh', -13, 0, 'dugme'], [T('şirketlerin', tC) - .1, 'f:p_boom', -10, 1, 'dondu'],
            [tE - .1, 'f:p_whoosh', -13, 0, 'eth'], [tB - .1, 'f:p_whoosh', -13, 0, 'binance'], [tI - .1, 'f:p_whoosh_bas', -11, 1, 'ders'],
            [a9, 'f:p_whoosh', -13, 0, 'cta']]


def RISERS(A): return []
