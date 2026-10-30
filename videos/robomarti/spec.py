import os
from panel_kit import JS, HERO, PIP, title, SVG_DEFS
from spec_util import load, FRAME_CSS
# ROBOMARTI — robotaksi taksiyi ucuzlatır mı, plakayı çökertir mi? (Ata 30 Eki, IG reel DfCucqWNbl9). HEP VARIM: HERO vurgu + PIP.
U = load(); T = U.T; W = U.W; DUR = U.DUR
SRT = os.path.join(W, 'avatar_cut.srt')
N = lambda s: s.split()
REPL = [(N('San Fransisko\'da'), "San Francisco'da"), (N('Veymo'), 'Waymo'), (N('Robo Martı\'nın'), "RoboMartı'nın"),
        (N('on milyon liranın'), '10 milyon liranın'), (N('on kilometre'), '10 km'), (N('beş yüz elli lira.'), '550 lira.'),
        (N('yüzde kırkını'), "%40'ını"), (N('on dokuz buçuk dolar.'), '19,5 $.'), (N('on yedi buçuk dolar.'), '17,5 $.'),
        (N('yüzde on üç'), '%13'), (N('on bir yılda'), '11 yılda'), (N('yetmiş beş bin dolardan'), "75.000 $'dan"),
        (N('iki yüz dolar'), '200 $'), (N('sekiz dolar'), '8 $'), (N('on bir milyon liraydı.'), '11 milyon liraydı.'),
        (N('on milyonun'), '10 milyonun'), (N('altı milyon liraya'), '6 milyon liraya')]
EM = {'düştü.', 'ucuzlar', 'tersi', 'pahalı!', 'ucuzlamadı.', 'rekabet', 'plaka.', 'belirliyor.', 'belirler.', 'gönder.'}
RED = {'pahalı!', 'ucuzlamadı.'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False
FULLOPEN = 1.2

t2 = T('Önce') - .1; t3 = T('Ama', t2) - .1; t4 = T('Bir', t3 + 1) - .1; t5 = T('Sürücüsüz', T('Uber', t4)) - .1
t6 = T('Sürücünün', t5) - .1; t6h = T('Yine', t6) - .1; t7 = T('Aynı', t6h) - .1; t8 = T('Şimdi', t7) - .1
t9 = T('Mali', t8) - .1; t10 = T('Şubattaki', t9) - .1; t11 = T('Bu', t10 + 3) - .1; t12 = T('Robo', T('belirler', t11)) - .1; t13 = T('Bunu,', t12) - .1
t1b = T('Şimdi') - .1
TS = [0, t1b, t2, t3, t4, t5, t6, t6h, t7, t8, t9, t10, t11, t12, t13, DUR]
IDS = ['s1', 's1b', 's2', 's3', 's4', 's5', 's6', 's6h', 's7', 's8', 's9', 's10', 's11', 's12', 's13']


def scenes(A):
    return [(IDS[k], TS[k], TS[k + 1]) for k in range(len(IDS))]


HEROS = ['s1', 's3', 's5', 's6h', 's8', 's11', 's13']
AV = {k: (HERO if k in HEROS else PIP) for k in IDS}

EXTRA_CSS = '<style>' + FRAME_CSS + r'''
.chip{position:absolute;padding:14px 24px;border-radius:14px;font:800 34px 'Inter Tight';white-space:nowrap}
.chip.g{border:1.5px solid rgba(255,255,255,.45);background:rgba(255,255,255,.04);color:#fff}
.dc{position:absolute;left:155px;width:715px;box-sizing:border-box;border-radius:18px;padding:18px 26px;border:1.5px solid rgba(255,255,255,.4);background:rgba(255,255,255,.03)}
.dc .q{font:700 28px 'Inter Tight';color:rgba(255,255,255,.7);letter-spacing:.04em}
.dc .r{font:800 42px 'Inter Tight';margin-top:6px;color:#fff}
.row{position:absolute;left:155px;width:715px;height:96px;box-sizing:border-box;display:flex;align-items:center;justify-content:space-between;padding:0 26px;
  border-radius:16px;border:1.5px solid rgba(255,255,255,.35);background:rgba(255,255,255,.03);font:800 38px 'Inter Tight';color:#fff}
.row span.k{font:600 28px 'IBM Plex Mono';color:rgba(255,255,255,.7);letter-spacing:.06em}
.hb{position:absolute;left:150px;height:84px;border-radius:0 14px 14px 0;transform-origin:0 50%;display:flex;align-items:center;padding-left:22px;
  font:800 34px 'Inter Tight';color:#0b0b0d;box-sizing:border-box;white-space:nowrap}
.hv{position:absolute;font:800 44px 'Inter Tight';color:#fff;white-space:nowrap}
.cnt{position:absolute;left:150px;width:730px;text-align:center}
.vb{position:absolute;bottom:0;border-radius:14px 14px 0 0;transform-origin:50% 100%}
.gold{color:#e8b931}
/* Ata 30 Eki 14:35: gerçek görsel + B-roll + animasyon */
.bgp{position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:hidden;opacity:0;pointer-events:none}
.bgp img{position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover;transform-origin:50% 45%}
.bgp .sh{position:absolute;left:0;top:0;width:1080px;height:1920px;background:linear-gradient(180deg,rgba(8,6,8,.72) 0%,rgba(8,6,8,.45) 35%,rgba(8,6,8,.62) 70%,rgba(8,6,8,.92) 100%)}
.pc{position:absolute;left:155px;width:715px;border-radius:22px;overflow:hidden;box-shadow:0 0 0 2px rgba(255,255,255,.35),0 26px 60px rgba(0,0,0,.75);--sx:-120%}
.pc img{display:block;width:100%;height:100%;object-fit:cover}
.pc::after{content:'';position:absolute;top:0;bottom:0;left:0;width:45%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.38),transparent);transform:translateX(var(--sx)) skewX(-12deg)}
.pc .cap{position:absolute;left:18px;bottom:16px;padding:8px 16px;border-radius:10px;background:rgba(0,0,0,.66);font:700 24px 'IBM Plex Mono';color:#fff;letter-spacing:.06em}
</style>'''

SCENE_HTML = r'''
  <div class="bgp" id="bg1"><img src="media/taxi_1.jpg" style=""><div class="sh"></div></div>
  <div class="bgp" id="bg1b"><img src="media/robomarti.png" style="filter:blur(18px) brightness(.8)"><div class="sh"></div></div>
  <div class="bgp" id="bg2"><img src="media/taxi_3.jpg" style=""><div class="sh"></div></div>
  <div class="bgp" id="bg3"><img src="media/sf_city.jpg" style=""><div class="sh"></div></div>
  <div class="bgp" id="bg4"><img src="media/waymo_sf.jpg" style="filter:blur(18px) brightness(.8)"><div class="sh"></div></div>
  <div class="bgp" id="bg5"><img src="media/waymo_res.jpg" style=""><div class="sh"></div></div>
  <div class="bgp" id="bg6"><img src="media/waymo_sensor.jpg" style="filter:blur(18px) brightness(.8)"><div class="sh"></div></div>
  <div class="bgp" id="bg8"><img src="media/taxi_2.jpg" style=""><div class="sh"></div></div>
  <div class="bgp" id="bg9"><img src="media/taxi_1.jpg" style="filter:blur(18px) brightness(.8)"><div class="sh"></div></div>
  <div class="bgp" id="bg10"><img src="media/waymo_res.jpg" style="filter:blur(18px) brightness(.8)"><div class="sh"></div></div>
  <div class="bgp" id="bg11"><img src="media/taxi_3.jpg" style=""><div class="sh"></div></div>
  <div class="bgp" id="bg12"><img src="media/robomarti.png" style="filter:blur(18px) brightness(.8)"><div class="sh"></div></div>
  <div class="bgp" id="bg13"><img src="media/taxi_2.jpg" style=""><div class="sh"></div></div>
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">''' + title('t1', 'Taksi Plakası', '<i>10 Milyonun</i> Altında') + r'''</section>
  <section id="s1b" class="scene clip">
    ''' + title('t1b', 'Martı', '<i>Sürücüsüz</i> Araç') + r'''
    <div class="pc" id="p1b" style="top:450px;height:402px"><img src="media/robomarti.png"><div class="cap">ROBOMARTI · 28 EKİM 2026</div></div>
    <div class="chip g" id="c1b1" style="left:155px;top:890px;opacity:0;font-size:30px">KAMERA + LİDAR + RADAR</div>
    <div class="chip g" id="c1b2" style="left:155px;top:985px;opacity:0;font-size:30px;border-color:#e8b931;color:#e8b931">PLAKA ÇÖKER Mİ? BİLET UCUZLAR MI?</div>
  </section>
  <section id="s2" class="scene clip">
    ''' + title('t2', 'Önce', '<i>Bilet</i>') + r'''
    <div class="row" id="r21" style="top:460px;opacity:0"><span class="k">AÇILIŞ</span>71,94 TL</div>
    <div class="row" id="r22" style="top:572px;opacity:0"><span class="k">KİLOMETRE</span>47,92 TL</div>
    <div class="cnt" id="k2" style="top:720px;opacity:0"><div class="lab">İSTANBUL · 10 KM TAKSİ</div><div class="num glowt gold" style="font-size:120px">~<span id="n2">0</span> TL</div></div>
    <div class="chip g" id="c2" style="left:150px;top:1000px;opacity:0;font-size:30px">SÜRÜCÜ ÇIKARSA → UCUZLAR MI?</div>
  </section>
  <section id="s3" class="scene clip">''' + title('t3', 'San Francisco', '<i>Tersi Oldu</i>') + r'''</section>
  <section id="s4" class="scene clip">
    ''' + title('t4', 'Uygulama', '<i>%40</i> Alıyor') + r'''
    <div class="hb" id="h41" style="top:470px;width:400px;background:#c9ccd3">SÜRÜCÜYE %60</div>
    <div class="hb" id="h42" style="top:470px;left:556px;width:324px;background:#e8b931;border-radius:0 14px 14px 0">UYGULAMA %40</div>
    <div class="pc" id="p4" style="top:580px;height:300px"><img src="media/waymo_sf.jpg" style="object-position:50% 60%"><div class="cap">WAYMO · SAN FRANCISCO</div></div>
    <div class="lab" id="l4" style="position:absolute;left:150px;top:905px;opacity:0">ORTALAMA YOLCULUK</div>
    <div class="hb" id="h43" style="top:950px;width:480px;background:#c9ccd3">UBER</div><div class="hv" id="v43" style="left:650px;top:962px;opacity:0">17,5 $</div>
    <div class="hb" id="h44" style="top:1050px;width:541px;background:#ff3b30;color:#fff">SÜRÜCÜSÜZ</div><div class="hv" id="v44" style="left:711px;top:1062px;opacity:0">19,7 $</div>
  </section>
  <section id="s5" class="scene clip">''' + title('t5', 'Sürücüsüz', '<i>%13</i> Daha Pahalı') + r'''</section>
  <section id="s6" class="scene clip">
    ''' + title('t6', 'Şoför Gitti', 'Yerine <i>Ne Geldi?</i>') + r'''
    <div class="chip g" id="c61" style="left:150px;top:460px;opacity:0">ARAÇ</div>
    <div class="chip g" id="c62" style="left:330px;top:460px;opacity:0">SENSÖR</div>
    <div class="chip g" id="c63" style="left:150px;top:560px;opacity:0">SİGORTA</div>
    <div class="chip g" id="c64" style="left:390px;top:560px;opacity:0">UZAKTAN İZLEME</div>
    <div class="pc" id="p6" style="top:650px;height:300px"><img src="media/waymo_sensor.jpg"><div class="cap">ARAÇ ÜSTÜ SENSÖRLER</div></div>
    <div class="cnt" id="k6" style="top:975px;opacity:0"><div class="lab">LİDAR SENSÖR FİYATI</div><div class="num glowt" style="font-size:96px"><span id="n6">75.000</span> $</div>
      <div class="lab" id="l6" style="margin-top:8px">2015 → <span class="gold">2025</span></div></div>
  </section>
  <section id="s6h" class="scene clip">''' + title('t6h', 'Yine de Bilet', '<i>Ucuzlamadı</i>') + r'''</section>
  <section id="s7" class="scene clip">
    ''' + title('t7', 'Fiyatı', '<i>Rekabet</i> Belirler') + r'''
    <div style="position:absolute;left:150px;top:470px;width:730px;height:470px">
      <div class="vb" id="b71" style="left:40px;width:180px;height:196px;background:linear-gradient(#e8b931,#8a6612)"></div>
      <div class="vb" id="b72" style="left:275px;width:180px;height:419px;background:linear-gradient(#c9ccd3,#5d5f66)"></div>
      <div class="vb" id="b73" style="left:510px;width:180px;height:470px;background:linear-gradient(#ff3b30,#7a0a0a)"></div>
    </div>
    <div class="hv" id="v71" style="left:190px;top:700px;width:180px;text-align:center;opacity:0">8,2 $</div>
    <div class="hv" id="v72" style="left:425px;top:476px;width:180px;text-align:center;opacity:0">17,5 $</div>
    <div class="hv" id="v73" style="left:660px;top:490px;width:180px;text-align:center;opacity:0">19,7 $</div>
    <div class="lab" style="position:absolute;left:190px;top:960px;width:180px;text-align:center">TESLA</div>
    <div class="lab" style="position:absolute;left:425px;top:960px;width:180px;text-align:center">UBER</div>
    <div class="lab" style="position:absolute;left:660px;top:960px;width:180px;text-align:center">WAYMO</div>
    <div class="chip g" id="c71" style="left:150px;top:1020px;opacity:0;font-size:28px">TESLA'DA HÂLÂ GÜVENLİK GÖREVLİSİ VAR</div>
  </section>
  <section id="s8" class="scene clip">''' + title('t8', 'Şimdi Plaka', 'Şubat: <i>11 Milyon</i>') + r'''</section>
  <section id="s9" class="scene clip">
    ''' + title('t9', 'Plaka', '<i>Neden Düştü?</i>') + r'''
    <div class="row" id="r91" style="top:460px;opacity:0"><span class="k">ŞUBAT 2026</span>~11 milyon TL</div>
    <div class="dc" id="d91" style="top:575px;opacity:0"><div class="q">SEBEP</div><div class="r" style="font-size:38px">Mali cihaz + <span class="redt">vergi yükü</span></div></div>
    <div class="row" id="r92" style="top:740px;opacity:0;border-color:rgba(255,59,48,.7)"><span class="k">MART 2026</span><span class="redt">&lt; 10 milyon TL</span></div>
    <div class="row" id="r93" style="top:850px;opacity:0;border-color:rgba(232,185,49,.7)"><span class="k">İBB YENİ PLAKA</span><span class="gold">6 milyon TL</span></div>
    <div class="chip g" id="c91" style="left:150px;top:965px;opacity:0;font-size:28px">DEĞERİ: KAÇ PLAKA VERİLDİĞİ</div>
  </section>
  <section id="s10" class="scene clip">
    ''' + title('t10', 'Kanun', '<i>Taslağı</i>') + r'''
    <div class="dc" id="d101" style="top:470px;opacity:0;border-color:rgba(232,185,49,.7)"><div class="q">HER SÜRÜCÜSÜZ ARAÇ</div><div class="r">İçişleri'nden <span class="gold">izin</span> alacak</div></div>
    <div class="chip g" id="c101" style="left:150px;top:650px;opacity:0;font-size:28px">ŞUBAT 2026 · HENÜZ YÜRÜRLÜKTE DEĞİL</div>
  </section>
  <section id="s11" class="scene clip">''' + title('t11', 'Plakayı', '<i>İzin</i> Belirler') + r'''</section>
  <section id="s12" class="scene clip">
    ''' + title('t12', 'RoboMartı', '<i>Ne Zaman?</i>') + r'''
    <div class="row" id="r121" style="top:460px;opacity:0"><span class="k">TARİH</span><span class="redt">açıklanmadı</span></div>
    <div class="row" id="r122" style="top:572px;opacity:0"><span class="k">ŞEHİR</span><span class="redt">açıklanmadı</span></div>
    <div class="pc" id="p12" style="top:690px;height:300px"><img src="media/robomarti.png"></div>
    <div class="dc" id="d121" style="top:1015px;opacity:0;border-color:rgba(232,185,49,.7)"><div class="q">GELİNCE KARŞILAŞTIR</div><div class="r">Açılış + km ücreti <span class="gold">vs taksi</span></div></div>
  </section>
  <section id="s13" class="scene clip">''' + title('t13', 'Taksiye Para Veren', 'Arkadaşına <i>Gönder</i>') + r'''</section>
'''

hr = []
for sid, a, b in scenes(None):
    if sid in HEROS:
        a2 = FULLOPEN + .35 if sid == 's1' else a + .35
        if hr and a2 - hr[-1][1] < .6: hr[-1] = (hr[-1][0], b)
        else: hr.append((a2, b))

SCENE_JS = JS + U.frame_js(hr) + f'''
tl.set('#t1',{{opacity:1}},0);
ttl('#t2',{t2 + .1}); pop('#r21',{T('İstanbul', t2)}); pop('#r22',{T('kilometre', t2)});
pop('#k2',{T('yaklaşık', t2) - .3}); {{const o={{v:0}};tl.to(o,{{v:551,duration:1.0,ease:'power2.out',onUpdate:()=>{{$('#n2').textContent=Math.round(o.v);}}}},{T('beş', t2)});}}
pop('#c2',{T('Sürücü', t2)});
ttl('#t3',{t3 + .1});
ttl('#t4',{t4 + .1}); tl.fromTo('#h41',{{scaleX:0}},{{scaleX:1,duration:.6,ease:'power3.out'}},{t4 + .3}); tl.fromTo('#h42',{{scaleX:0}},{{scaleX:1,duration:.6,ease:'power3.out'}},{T('yüzde', t4)});
pop('#l4',{T('Buna', t4)}); tl.fromTo('#h43',{{scaleX:0}},{{scaleX:1,duration:.7,ease:'power3.out'}},{T('Uber', t4)}); pop('#v43',{T('Uber', t4) + .6});
tl.fromTo('#h44',{{scaleX:0}},{{scaleX:1,duration:.7,ease:'power3.out'}},{T('sürücüsüz', t4)}); pop('#v44',{T('on', T('ortalama', T('sürücüsüz', t4)))});
ttl('#t5',{t5 + .1});
ttl('#t6',{t6 + .1}); pop('#c61',{T('araç', t6)}); pop('#c62',{T('sensör', t6)}); pop('#c63',{T('sigorta', t6)}); pop('#c64',{T('uzaktan', t6)});
pop('#k6',{T('Lidar', t6)}); {{const o={{v:75000}};tl.to(o,{{v:200,duration:1.4,ease:'power3.inOut',onUpdate:()=>{{$('#n6').textContent=Math.round(o.v).toLocaleString('tr-TR');}}}},{T('iki', T('Lidar', t6)) - .4});}}
ttl('#t6h',{t6h + .1});
ttl('#t7',{t7 + .1}); tl.fromTo('#b71',{{scaleY:0}},{{scaleY:1,duration:.7,ease:'power3.out'}},{T('Tesla', t7)}); pop('#c71',{T('güvenlik', t7)});
pop('#v71',{T('sekiz', t7)}); tl.fromTo('#b72, #b73',{{scaleY:0}},{{scaleY:1,duration:.7,ease:'power3.out',stagger:.15}},{t7 + .3}); pop('#v72',{t7 + .8}); pop('#v73',{t7 + .95});
ttl('#t8',{t8 + .1});
ttl('#t9',{t9 + .1}); pop('#r91',{t9 + .2}); pop('#d91',{t9 + .5}); pop('#r92',{T('martta', t9)}); pop('#r93',{T('İstanbul', t9)}); pop('#c91',{T('Plakanın', t9)});
ttl('#t10',{t10 + .1}); pop('#d101',{T('İçişleri', t10) - .3}); pop('#c101',{t10 + .4});
ttl('#t11',{t11 + .1});
ttl('#t12',{t12 + .1}); pop('#r121',{T('zaman', t12)}); pop('#r122',{T('şehirde', t12)}); pop('#d121',{T('Geldiğinde', t12)});
ttl('#t13',{t13 + .1});
'''


# ---- gerçek görsel katmanı (Ata 30 Eki 14:35): sahne arka plan fotoğrafları Ken Burns ile, foto kartlar perde+ışık süpürmesiyle
BGMAP = {'s1': 'bg1', 's1b': 'bg1b', 's2': 'bg2', 's3': 'bg3', 's4': 'bg4', 's5': 'bg5', 's6': 'bg6', 's8': 'bg8', 's9': 'bg9',
         's10': 'bg10', 's11': 'bg11', 's12': 'bg12', 's13': 'bg13'}
_SC = {k: (a, b) for k, a, b in scenes(None)}
VIS_JS = ''
for k, (sid, bid) in enumerate(BGMAP.items()):
    a, b = _SC[sid]
    dx = (-40, 40)[k % 2]
    VIS_JS += (f"tl.fromTo('#{bid}',{{opacity:0}},{{opacity:1,duration:.45,ease:'power2.out'}},{max(0, a - .05):.2f});"
               f"tl.fromTo('#{bid} img',{{scale:1.04,x:0}},{{scale:1.16,x:{dx},duration:{b - a + .4:.2f},ease:'none'}},{max(0, a - .05):.2f});"
               f"tl.to('#{bid}',{{opacity:0,duration:.35}},{b - .1:.2f});\n")
def card(cid, t):
    return (f"tl.fromTo('#{cid}',{{clipPath:'inset(0% 100% 0% 0% round 22px)',y:30,opacity:1}},{{clipPath:'inset(0% 0% 0% 0% round 22px)',y:0,duration:.7,ease:'power3.out'}},{t:.2f});"
            f"tl.fromTo('#{cid} img',{{scale:1.18}},{{scale:1.02,duration:3.5,ease:'power2.out'}},{t:.2f});"
            f"tl.fromTo('#{cid}',{{'--sx':'-120%'}},{{'--sx':'260%',duration:.9,ease:'power2.inOut'}},{t + .6:.2f});\n")
VIS_JS += card('p1b', t1b + .15) + card('p4', T('Buna', t4) - .5) + card('p6', T('Lidar', t6) - .3) + card('p12', t12 + .3)
VIS_JS += f"ttl('#t1b',{t1b + .05}); pop('#c1b1',{T('gösterdi', t1b)}); pop('#c1b2',{T('Peki', t1b)});\n"
SCENE_JS += VIS_JS


def BROLL(A):
    # gerçek sürücüsüz araç görüntüsü (Pexels 32000333, Las Vegas) — "yine de ucuzlamadı" + Tesla/Uber/Waymo karşılaştırması altında
    return [{'id': 'br_lv', 'src': 'robotaksi_lv.mp4', 'a': t6h - .05, 'b': min(t8 - .05, t6h + 11.8), 'ms': 0, 'dim': .55}]


def SFX(A):
    S = [[t2, 'f:p_whoosh', -13, 0, 'bilet'], [T('beş', t2), 'f:p_klik', -11, 0, '550'], [t3, 'f:p_whoosh_bas', -11, 1, 'sf'],
         [t4, 'f:p_whoosh', -13, 0, 'oran'], [t5, 'f:p_boom', -10, 1, '13'], [t6, 'f:p_whoosh', -13, 0, 'maliyet'],
         [t6h, 'f:p_whoosh_bas', -11, 1, 'ucuzlamadi'], [t7, 'f:p_whoosh', -13, 0, 'tesla'], [t8, 'f:p_whoosh_bas', -11, 1, 'plaka'],
         [t9, 'f:p_whoosh', -13, 0, 'dustu'], [t10, 'f:p_whoosh', -13, 0, 'kanun'], [t11, 'f:p_whoosh_bas', -11, 1, 'izin'],
         [t12, 'f:p_whoosh', -13, 0, 'robo'], [t13, 'f:p_whoosh', -13, 0, 'cta']]
    return S


def RISERS(A): return []
