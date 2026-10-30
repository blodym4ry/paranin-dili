import os
from panel_kit import JS, HERO, title, SVG_DEFS
from spec_util import load, FRAME_CSS
# BINANCE HACK (29 Eki 2026) v2 — uzun anlatım (Ata 30 Eki 04:33: dakika dakika, varlıklar, açıklama, saldırganın hamleleri, sonrası)
# PANEL + FULLOPEN + altın çerçeveli avatar · gerçek ekran görüntüleri (X, Türkçe çeviri görünümü) · güvenli alan v2.
U = load(); T = U.T; W = U.W; DUR = U.DUR
SRT = os.path.join(W, 'avatar_cut.srt')
N = lambda *w: list(w)
REPL = [(N("Baynens'ten"), "Binance'ten"), (N("Baynens'in"), "Binance'in"), (N('Baynens'), 'Binance'), (N("Eteryum'a"), "Ethereum'a"),
        (N("Eteryum'u"), "Ethereum'u"), (N('Eteryum,'), 'Ethereum,'), (N('Eteryum'), 'Ethereum'), (N('Teter,'), 'Tether,'), (N('Sörkıl'), 'Circle'),
        (N('Ripıl,'), 'Ripple,'), (N('Bitkoin'), 'Bitcoin'), (N("Baybit'in"), "Bybit'in"),
        (N('iki', 'milyar', 'dolar'), '2 milyar $'), (N('on', 'biri', 'yirmi', 'geçe,'), '23.20\'de,'), (N('elli'), '50'),
        (N('Yirmi', 'üç', 'yirmi', 'dört.'), '23.24'), (N('Yirmi', 'üç', 'otuz', 'dokuz.'), '23.39'), (N('Yirmi', 'üç', 'kırk', 'bir.'), '23.41'),
        (N('bir', 'virgül', 'altı', 'milyar', 'dolarlık'), '1,6 milyar $\'lık'), (N('yüz', 'altmış', 'yedi', 'bin'), '167 bin'),
        (N('yirmi', 'sekiz', 'bin'), '28 bin'), (N('Yüz', 'doksan', 'beş', 'bin'), '195 bin'), (N('Yedi', 'yüz', 'seksen', 'milyon', 'dolarlık'), '780 milyon $\'lık'),
        (N('beş', 'virgül', 'altı', 'milyar', 'dolar'), '5,6 milyar $'), (N('iki', 'buçuk', 'ile', 'altı', 'milyar', 'dolar'), '2,5–6 milyar $'),
        (N('iki', 'buçuk', 'milyarı'), '2,5 milyarı'), (N('bir', 'buçuk', 'milyarıydı.'), '1,5 milyarıydı.'), (N('yirmi', 'bin'), '20 bin'),
        (N('seksen', 'bin'), '80 bin'), (N('yüzde', 'yedi'), '%7')]
EM = {'çıktı.', 'altında!', 'tuttu', 'gitti.', 'soygunu.', 'dondurdu!', 'dondurulamıyor.', 'yok.', 'karşılayacak.', 'kapalı.', 'tut.', 'gönder.'}
RED = {'altında!', 'gitti.', 'dondurulamıyor.', 'kapalı.', 'düştü.'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False
FULLOPEN = 1.2

a1, b1 = U.seg(0); a7, b7 = U.seg(1); a15, _ = U.seg(2)
tBG = T('Bir', 19); tSD = T('Şimdi', tBG + 2); tZA = T('zincir', tSD + 15) - .45; tRR = T('Resmi', tZA + 8)
tE = T('Eteryum', b7 + 3); tL = T('İlk', tE + 10); tB = T('Baynens\'in', tL + 2); tP = T('Piyasa', tB + 6); tBS = T('Bundan', tP + 4)
tID = T('İki', tBS + 4)
t24 = T('Yirmi', tSD); t26 = T('İki', t24 + 2); t39 = T('Yirmi', T('daha', t26) + .1); t41 = T('Yirmi', t39 + 2)


def scenes(A):
    return [('s1', 0, b1), ('s2', b1, tBG - .1), ('s3', tBG - .1, tSD - .1), ('s4', tSD - .1, tZA), ('s5', tZA, tRR - .1),
            ('s6', tRR - .1, a7), ('s7', a7, b7), ('s8', b7, tE - .1), ('s9', tE - .1, tL - .1), ('s10', tL - .1, tB - .1),
            ('s11', tB - .1, tP - .1), ('s12', tP - .1, tBS - .1), ('s13', tBS - .1, tID - .1), ('s14', tID - .1, a15), ('s15', a15, DUR)]


AV = {f's{k}': None for k in range(1, 16)}
AV.update({'s1': HERO, 's7': HERO, 's15': HERO})

EXTRA_CSS = '<style>' + FRAME_CSS + r'''
.chip{position:absolute;padding:14px 24px;border-radius:14px;font:800 34px 'Inter Tight';white-space:nowrap}
.chip.g{border:1.5px solid rgba(255,255,255,.45);background:rgba(255,255,255,.04);color:#fff}
.ice{border-color:#7fd3ff!important;color:#bfe9ff!important;box-shadow:0 0 26px rgba(127,211,255,.35)}
.dc{position:absolute;left:150px;width:730px;border-radius:18px;padding:18px 26px;border:1.5px solid rgba(255,255,255,.4);background:rgba(255,255,255,.03)}
.dc .q{font:700 28px 'Inter Tight';color:rgba(255,255,255,.7);letter-spacing:.04em}
.dc .r{font:800 42px 'Inter Tight';margin-top:6px}
.wal{position:absolute;width:300px;height:220px;border-radius:22px;border:2px solid rgba(255,255,255,.45);background:rgba(255,255,255,.035);
  display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:10px}
.wal .lab{font-size:22px}.wal .nm{font:800 40px 'Inter Tight'}
.arr{position:absolute;height:6px;background:linear-gradient(90deg,rgba(255,255,255,.2),#ff3b30);transform-origin:0 50%;border-radius:3px}
.bar{position:absolute;border-radius:0 14px 14px 0;transform-origin:0 50%}
.shot{position:absolute;border-radius:20px;overflow:hidden;background:#000;box-shadow:0 0 0 2px rgba(255,255,255,.35),0 24px 60px rgba(0,0,0,.7)}
.shot img{display:block;width:100%;height:auto}
.tl{position:absolute;left:150px;width:730px;height:96px;border-radius:16px;border:1.5px solid rgba(255,255,255,.35);background:rgba(255,255,255,.035);
  display:flex;align-items:center;gap:26px;padding:0 24px}
.tl .h{font:800 40px 'IBM Plex Mono';color:#ff3b30;min-width:130px}
.tl .x{font:800 34px 'Inter Tight';color:#fff;white-space:nowrap}
.cnt{position:absolute;left:150px;width:730px;text-align:center}
.qs{position:absolute;left:150px;width:730px;height:120px;border-radius:18px;border:1.5px solid rgba(232,185,49,.6);background:rgba(232,185,49,.05);
  display:flex;align-items:center;gap:22px;padding:0 26px;font:800 40px 'Inter Tight';color:#fff}
.qs b{font:800 60px 'DM Serif Display';color:#e8b931}
.gold{color:#e8b931}
</style>'''

SCENE_HTML = r'''
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">''' + title('t1', 'Tek İşlemde', '<i>2 Milyar $</i> Çıktı') + r'''</section>
  <section id="s2" class="scene clip">
    ''' + title('t2', 'Tek Bir', '<i>İmza</i>') + r'''
    <div class="lab" id="l2" style="position:absolute;left:0;right:0;top:450px;text-align:center;opacity:0">29 EKİM · 23.20 (TSİ)</div>
    <div class="wal" id="w21" style="left:130px;top:520px;opacity:0"><div class="lab">BINANCE</div><div class="nm">SICAK<br>CÜZDAN</div></div>
    <div class="arr" id="a2" style="left:440px;top:628px;width:150px"></div>
    <div class="wal" id="w22" style="left:600px;top:520px;width:280px;opacity:0;border-color:#ff3b30"><div class="lab">KONTROL</div><div class="nm" style="color:#ff3b30">SALDIRGANIN<br>KODU</div></div>
    <div class="dc" id="d2" style="top:800px;opacity:0"><div class="q">ÖNCEDEN HAZIRLANAN YETKİ</div><div class="r"><span class="gold">50</span> denendi → <span class="redt">1'i tuttu</span></div></div>
  </section>
  <section id="s3" class="scene clip">
    ''' + title('t3', '1 Gün Önce', '<i>İz</i> Bırakmadan') + r'''
    <div class="wal" id="w31" style="left:130px;top:500px;width:300px;opacity:0"><div class="lab">28 EKİM</div><div class="nm" style="font-size:34px">KARIŞTIRMA<br>SERVİSİ</div></div>
    <div class="arr" id="a3" style="left:440px;top:608px;width:150px"></div>
    <div class="wal" id="w32" style="left:600px;top:500px;width:280px;opacity:0;border-color:#ff3b30"><div class="lab">SALDIRGAN ADRESİ</div><div class="nm" style="color:#ff3b30">0,1 ETH</div></div>
    <div class="chip g" id="c3" style="left:150px;top:780px;opacity:0;font-size:30px">KAYNAĞI GİZLENMİŞ KÜÇÜK BİR TRANSFER</div>
  </section>
  <section id="s4" class="scene clip">
    ''' + title('t4', 'Dakika', '<i>Dakika</i>') + r'''
    <div class="tl" id="r41" style="top:440px;opacity:0"><div class="h">23.24</div><div class="x">1,6 MLR $ + 167 BİN ETH</div></div>
    <div class="tl" id="r42" style="top:556px;opacity:0"><div class="h">23.26</div><div class="x">+28 BİN ETH · 2. CÜZDAN</div></div>
    <div class="tl" id="r43" style="top:672px;opacity:0"><div class="h">23.39</div><div class="x">195 BİN ETH TAŞINDI</div></div>
    <div class="tl" id="r44" style="top:788px;opacity:0"><div class="h">23.41</div><div class="x">+780 MİLYON $ DİJİTAL DOLAR</div></div>
    <div class="cnt" id="k4" style="top:920px;opacity:0"><div class="lab">ETHEREUM AĞINDAN ÇIKAN (TAHMİNİ)</div><div class="num glowt redt" style="font-size:96px">~<span id="n4">0</span> MLR $</div></div>
  </section>
  <section id="s5" class="scene clip">
    ''' + title('t5', 'Saldırganın', '<i>Cüzdanı</i>') + r'''
    <div class="shot" id="i51" style="left:150px;top:440px;width:730px;opacity:0"><img src="media/arkham.png"></div>
    <div class="shot" id="i52" style="left:180px;top:680px;width:670px;opacity:0"><img src="media/watcher.png"></div>
    <div class="chip g" id="c5" style="left:150px;top:1080px;opacity:0;font-size:26px;border-color:#e8b931;color:#e8b931">TRON ÇIKIŞLARI: BINANCE'İN KENDİSİ (ANALİST)</div>
  </section>
  <section id="s6" class="scene clip">
    ''' + title('t6', 'Kripto Tarihinin', 'En Büyük <i>Soygunu</i>') + r'''
    <div class="lab" style="position:absolute;left:150px;top:450px">BINANCE · TAHMİN ARALIĞI</div>
    <div class="bar" id="h61" style="left:150px;top:490px;height:100px;width:310px;background:linear-gradient(90deg,#ff3b30,rgba(255,59,48,.5))"></div>
    <div class="bar" id="h62" style="left:460px;top:490px;height:100px;width:420px;background:repeating-linear-gradient(45deg,rgba(255,59,48,.35) 0 14px,rgba(255,59,48,.12) 14px 28px)"></div>
    <div class="a num" id="v61" style="left:170px;top:605px;font-size:56px;opacity:0">2,5 – 6 MİLYAR $</div>
    <div class="lab" style="position:absolute;left:150px;top:730px">ÖNCEKİ REKOR · BYBIT · ŞUBAT 2025</div>
    <div class="bar" id="h63" style="left:150px;top:770px;height:100px;width:190px;background:linear-gradient(90deg,rgba(255,255,255,.85),rgba(255,255,255,.25))"></div>
    <div class="a num" id="v63" style="left:360px;top:782px;font-size:56px;opacity:0">1,5 MİLYAR $</div>
    <div class="chip g" id="c6" style="left:150px;top:920px;opacity:0;font-size:28px">RESMİ KAYIP RAKAMI HENÜZ YOK</div>
  </section>
  <section id="s7" class="scene clip">''' + title('t7', 'Tether · Circle · Ripple', '<i>Dondurdu</i>') + r'''</section>
  <section id="s8" class="scene clip">
    ''' + title('t8', 'Paranın', '<i>Düğmesi</i>') + r'''
    <div class="chip g ice" id="c81" style="left:150px;top:440px;opacity:0">TETHER · 1,57 MLR $</div>
    <div class="chip g ice" id="c82" style="left:150px;top:540px;opacity:0">CIRCLE · 0,8 MLR $</div>
    <div class="chip g ice" id="c83" style="left:150px;top:640px;opacity:0">RIPPLE · ~0,2 MLR $</div>
    <div class="shot" id="i8" style="left:150px;top:770px;width:730px;opacity:0"><img src="media/paolo.png"></div>
    <div class="rbox" id="r8" style="left:150px;top:1040px;width:730px;height:100px;border-radius:18px;font-size:44px;opacity:0">SENİN DİJİTAL DOLARINDA DA VAR</div>
  </section>
  <section id="s9" class="scene clip">
    ''' + title('t9', 'Ethereum', '<i>Dondurulamaz</i>') + r'''
    <div class="dc" id="d91" style="top:440px;opacity:0"><div class="q">1 · TAKAS</div><div class="r">Dijital dolar → <span class="gold">Ethereum</span></div></div>
    <div class="dc" id="d92" style="top:600px;opacity:0"><div class="q">2 · KREDİ PLATFORMU</div><div class="r">~20 bin ETH <span class="redt">borç aldı</span></div></div>
    <div class="dc" id="d93" style="top:760px;opacity:0;border-color:rgba(127,211,255,.7)"><div class="q">3 · PLATFORM</div><div class="r">Bazı piyasalarını <span style="color:#bfe9ff">dondurdu</span></div></div>
    <div class="cnt" id="k9" style="top:930px;opacity:0"><div class="lab">HÂLÂ SALDIRGANDA</div><div class="num glowt redt" style="font-size:96px">> 0,5 MLR $</div></div>
  </section>
  <section id="s10" class="scene clip">
    ''' + title('t10', 'Kim', '<i>Yaptı?</i>') + r'''
    <div class="gbox" id="b10" style="left:150px;top:470px;width:730px;height:280px"><div class="lab" style="margin-bottom:14px">İLK İZLER</div>
      <div class="num" style="font-size:84px">KUZEY KORE</div><div class="num redt" style="font-size:64px;margin-top:8px">LAZARUS?</div></div>
    <div class="chip g" id="c10" style="left:240px;top:800px;opacity:0;font-size:32px">RESMİ DOĞRULAMA YOK</div>
  </section>
  <section id="s11" class="scene clip">
    ''' + title('t11', 'Binance', 'Ne <i>Dedi?</i>') + r'''
    <div class="shot" id="i11" style="left:150px;top:440px;width:730px;opacity:0"><img src="media/yihe.png"></div>
    <div class="dc" id="d11" style="top:960px;opacity:0;border-color:rgba(255,59,48,.7)"><div class="q">ŞU AN</div><div class="r">Yatırma ve çekme <span class="redt">kapalı</span></div></div>
  </section>
  <section id="s12" class="scene clip">
    ''' + title('t12', 'Piyasa', '<i>Sarsıldı</i>') + r'''
    <div class="shot" id="i12" style="left:200px;top:430px;width:630px;opacity:0"><img src="media/bpt.png"></div>
    <div class="chip g" id="c121" style="left:150px;top:1030px;opacity:0;border-color:#ff3b30;color:#ff3b30">BTC < 80 BİN $</div>
    <div class="chip g" id="c122" style="left:560px;top:1030px;opacity:0;border-color:#ff3b30;color:#ff3b30">BNB −%7</div>
  </section>
  <section id="s13" class="scene clip">
    ''' + title('t13', 'Bundan Sonra', '<i>Neye</i> Bak?') + r'''
    <div class="qs" id="q1" style="top:450px;opacity:0"><b>1</b>Çekimler ne zaman açılacak?</div>
    <div class="qs" id="q2" style="top:600px;opacity:0"><b>2</b>Donan para geri dönecek mi?</div>
    <div class="qs" id="q3" style="top:750px;opacity:0"><b>3</b>Kalan ETH nereye gidecek?</div>
  </section>
  <section id="s14" class="scene clip">
    ''' + title('t14', 'Senin İçin', '<i>İki</i> Ders') + r'''
    <div class="dc" id="d141" style="top:460px;opacity:0;border-color:rgba(255,59,48,.7)"><div class="q">1 · SAHTE MESAJ</div><div class="r">"Fonunu geri al" linkine <span class="redt">tıklama</span></div></div>
    <div class="dc" id="d142" style="top:660px;opacity:0"><div class="q">2 · UZUN VADELİ BİRİKİM</div><div class="r">Anahtarı <span class="gold">sende olan</span> cüzdanda</div></div>
  </section>
  <section id="s15" class="scene clip">''' + title('t15', 'Kriptosu Borsadaki', 'Arkadaşına <i>Gönder</i>') + r'''</section>
'''


def _cnt(a, b, t):
    return f"{{const o={{v:{a}}};tl.to(o,{{v:{b},duration:.9,ease:'power2.out',onUpdate:()=>{{$('#n4').textContent=o.v.toFixed(1).replace('.',',');}}}},{t});}}"


SCENE_JS = JS + U.frame_js([(FULLOPEN + .35, b1), (a7, b7), (a15, DUR)]) + f'''
tl.set('#t1',{{opacity:1}},0);
ttl('#t2',{b1 + .1}); fin('#l2',{b1 + .4}); pop('#w21',{T('sıcak', b1)}); tl.fromTo('#a2',{{scaleX:0}},{{scaleX:1,duration:.5,ease:'power3.out'}},{T('imzası', b1)});
pop('#w22',{T('imzası', b1) + .4}); pop('#d2',{T('Saldırgan', b1)});
ttl('#t3',{tBG}); pop('#w31',{T('karıştırma', tBG)}); tl.fromTo('#a3',{{scaleX:0}},{{scaleX:1,duration:.5,ease:'power3.out'}},{T('küçük', tBG)}); pop('#w32',{T('miktar', tBG)}); pop('#c3',{T('gelmişti', tBG)});
ttl('#t4',{tSD}); pop('#r41',{t24}); pop('#k4',{t24 + .2}); {_cnt(0, 2.0, T('gitti', t24) - .3)}
pop('#r42',{t26}); {_cnt(2.0, 2.07, T('daha', t26))} pop('#r43',{t39}); pop('#r44',{t41}); {_cnt(2.07, 2.85, T('çıktı', t41) - .3)}
ttl('#t5',{tZA + .1}); pop('#i51',{T('şirketi', tZA)}); pop('#i52',{T('İçinde', tZA)}); pop('#c5',{T('Tron', tZA)});
ttl('#t6',{tRR}); tl.fromTo('#h61',{{scaleX:0}},{{scaleX:1,duration:.7,ease:'power3.out'}},{T('Tahminler', tRR)}); tl.fromTo('#h62',{{scaleX:0}},{{scaleX:1,duration:.6,ease:'power3.out'}},{T('altı', tRR)});
pop('#v61',{T('altı', tRR) + .3}); tl.fromTo('#h63',{{scaleX:0}},{{scaleX:1,duration:.6,ease:'power3.out'}},{T('Önceki', tRR)}); pop('#v63',{T('Önceki', tRR) + .4}); pop('#c6',{tRR + .2});
ttl('#t7',{a7 + .1});
ttl('#t8',{b7 + .1}); pop('#c81',{b7 + .3}); pop('#c82',{b7 + .6}); pop('#c83',{b7 + .9}); pop('#i8',{T('şirketlerin', b7)}); pop('#r8',{T('Aynı', b7)});
ttl('#t9',{tE}); pop('#d91',{T('çevirdi', tE) - .4}); pop('#d92',{T('kredi', tE)}); pop('#d93',{T('Platform', T('aldı', tE))}); pop('#k9',{T('Yarım', tE)});
ttl('#t10',{tL}); pop('#b10',{T('Kuzey', tL)}); pop('#c10',{T('Ama', tL)});
ttl('#t11',{tB}); pop('#i11',{T('ortak', tB)}); pop('#d11',{T('Para', tB)});
ttl('#t12',{tP}); pop('#i12',{tP + .2}); pop('#c121',{T('Bitkoin', tP)}); pop('#c122',{T('coini', tP)});
ttl('#t13',{tBS}); pop('#q1',{T('Çekimler', tBS)}); pop('#q2',{T('Dondurulan', tBS)}); pop('#q3',{T('saldırgan', tBS)});
ttl('#t14',{tID}); pop('#d141',{T('Fonunu', tID)}); pop('#d142',{T('Uzun', tID)});
ttl('#t15',{a15 + .1});
'''


def SFX(A):
    return [[b1 + .05, 'f:p_whoosh', -13, 0, 'imza'], [T('Saldırgan', b1) - .1, 'f:p_klik', -11, 0, '50'], [tBG - .1, 'f:p_whoosh', -13, 0, 'mixer'],
            [tSD - .1, 'f:p_whoosh_bas', -11, 1, 'dakika'], [t24, 'f:p_boom', -10, 1, '2324'], [t26, 'f:p_klik', -11, 0, '2326'], [t39, 'f:p_klik', -11, 0, '2339'],
            [t41, 'f:p_klik', -11, 0, '2341'], [tZA, 'f:p_whoosh', -13, 0, 'arkham'], [tRR - .1, 'f:p_whoosh', -13, 0, 'rekor'],
            [a7, 'f:p_whoosh_bas', -11, 1, 'dondur'], [b7 + .05, 'f:p_whoosh', -13, 0, 'dugme'], [tE - .1, 'f:p_whoosh', -13, 0, 'eth'],
            [tL - .1, 'f:p_boom', -10, 1, 'kim'], [tB - .1, 'f:p_whoosh', -13, 0, 'binance'], [tP - .1, 'f:p_whoosh', -13, 0, 'piyasa'],
            [tBS - .1, 'f:p_whoosh_bas', -11, 1, 'sonra'], [tID - .1, 'f:p_whoosh', -13, 0, 'ders'], [a15, 'f:p_whoosh', -13, 0, 'cta']]


def RISERS(A): return []
