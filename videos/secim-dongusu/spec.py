import os
from panel_kit import CARD, JS, title, line_path, glow_path, SVG_DEFS
# SEÇİM DÖNGÜSÜ v2 — PANEL stili (Ata 23 Eki 02:39). Masa üstü v1 YASAKLANDI (spec_masa_v1.py arşiv).
# Avatar: lacivert balıkçı yaka, video boyunca altta kartta (3 parça: seg_00 + seg_mid + seg_01). Müzik: onaylı kütüphane (aday 1).
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [(N('yedi', 'mayıs', 'iki', 'bin', 'yirmi', 'sekiz'), '7 Mayıs 2028'), (N('iki', 'bin', 'yirmi', 'üç'), '2023'),
        (N('yüzde', 'elli', 'dört'), '%54'), (N('yüzde', 'sekiz', 'buçuktu'), "%8,5'ti"), (N('yüzde', 'yirmi', 'beş'), '%25'),
        (N('mart', 'iki', 'bin', 'yirmi', 'dörtte'), "Mart 2024'te"), (N('yüzde', 'elli'), '%50'), (N('yirmi', 'liradan'), '20 liradan'),
        (N('otuz', 'iki', 'liraya'), '32 liraya'), (N('iki', 'bin', 'on', 'beşte'), "2015'te"), (N('on', 'altı', 'nisan'), '16 Nisan')]
EM = {'fatura', 'faturaya', 'soru', 'gönder'}
RED = {'düştü', 'değil'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False


def scenes(A):
    return [('s1', 0, 6.46), ('s2', 6.46, 12.25), ('s3', 12.25, 20.62), ('s4', 20.62, 27.5), ('s4b', 27.5, 36.75), ('s5', 36.75, 39.2),
            ('s6', 39.2, 47.56), ('s7', 47.56, 51.45), ('s8', 51.45, 54.78), ('s9', 54.78, DUR)]


AV = {k: CARD for k in ['s1', 's2', 's3', 's4', 's4b', 's5', 's6', 's7', 's8', 's9']}

# politika faizi (TCMB PPK): ay 0 = Şub 2023
RATE = [(0, 8.5), (3, 8.5), (4, 15), (5, 17.5), (6, 25), (7, 30), (8, 35), (9, 40), (10, 42.5), (11, 45), (13, 50)]
X0, Y0, CW, CH = 150, 470, 790, 480
P1 = line_path(RATE[:5], X0, Y0, CW, CH, 13, 52)
P2 = line_path(RATE[4:], X0, Y0, CW, CH, 13, 52)
yv = lambda v: Y0 + CH - v / 52 * CH
xm = lambda m: X0 + m / 13 * CW
WAVE = 'M110,760 C230,760 260,560 380,560 C500,560 530,960 650,960 C770,960 800,600 970,600'

EXTRA_CSS = r'''<style>
.ico{position:absolute;stroke:#fff;fill:none;stroke-width:5;stroke-linecap:round;stroke-linejoin:round;filter:drop-shadow(0 0 8px rgba(255,255,255,.5))}
.ring{position:absolute;width:44px;height:44px;margin:-22px 0 0 -22px;border-radius:50%;border:3px solid #ff3b30;opacity:0}
.strk{position:absolute;height:6px;background:#ff3b30;box-shadow:0 0 14px #ff3b30;transform:scaleX(0);transform-origin:0 50%}
.kup{position:absolute;left:110px;width:860px;padding:30px 36px;border-radius:22px;background:rgba(255,255,255,.06);border:1.5px solid rgba(255,255,255,.35);box-shadow:0 0 40px rgba(255,255,255,.06)}
.kup .s{font:500 24px 'IBM Plex Mono';letter-spacing:.14em;color:#ff5a4f;margin-bottom:12px}
.kup .h{font:400 50px/1.12 'DM Serif Display';color:#f2f2f2}
.bar{position:absolute;bottom:0;border-radius:8px 8px 0 0}
</style>'''

SCENE_HTML = r'''
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">
    ''' + title('t1', 'Bir Sonraki <i>Zengin Olma</i>', 'Tarihi Ne Zaman?') + r'''
    <div class="gbox" id="d1" style="left:250px;top:560px;width:580px;height:330px">
      <div class="lab" style="color:#ff5a4f;letter-spacing:.3em">TAKVİMDEKİ ADAY</div>
      <div class="num glowt" style="font-size:124px">7 MAYIS</div>
      <div class="serif" style="font-size:66px;color:#d6d6d6">2028</div></div>
    <svg class="gl" style="left:150px;top:600px" width="100" height="250"><path id="arc1" d="M95,40 C10,70 10,200 70,240" pathLength="1" fill="none" stroke="#fff" stroke-width="4" style="stroke-dasharray:1;stroke-dashoffset:1;filter:drop-shadow(0 0 6px #fff)"/></svg>
  </section>
  <section id="s2" class="scene clip">
    ''' + title('t2', 'O Tarihe Kredi Çeken', '<i>Kazanmayabilir</i>') + r'''
    <div class="rbox" id="b21" style="left:140px;top:500px;width:360px;height:130px;border-radius:14px">KREDİ</div>
    <svg class="gl" style="left:520px;top:540px" width="60" height="60"><path id="ar2" d="M0,30 L50,30 M32,12 L50,30 L32,48" pathLength="1" fill="none" stroke="#fff" stroke-width="5" style="stroke-dasharray:1;stroke-dashoffset:1"/></svg>
    <div class="gbox" id="b22" style="left:600px;top:500px;width:340px;height:130px"><div class="num" style="font-size:96px">?</div></div>
    <div class="gbox" id="b23" style="left:240px;top:760px;width:600px;height:300px">
      <svg width="90" height="100" viewBox="0 0 90 100" style="stroke:#fff;fill:none;stroke-width:6;filter:drop-shadow(0 0 8px rgba(255,255,255,.6))"><rect x="10" y="44" width="70" height="50" rx="10"/><path d="M24,44 V30 a21,21 0 0 1 42,0 V44"/></svg>
      <div class="num" style="font-size:72px;margin-top:10px">TEK SORU</div>
      <div class="lab" style="margin-top:8px">VİDEONUN SONUNDA</div></div>
  </section>
  <section id="s3" class="scene clip">
    ''' + title('t3a', 'Seçim Yıllarında', 'Ekonomi <i>Hızlanır</i>') + title('t3b', 'Asıl Fatura', 'Seçimden <i>Sonra</i> Gelir') + r'''
    <svg class="gl" style="left:0;top:0" width="1080" height="1200">
      <line x1="100" y1="760" x2="980" y2="760" stroke="rgba(255,255,255,.18)" stroke-width="2" stroke-dasharray="6 10"/>
      ''' + glow_path('wv', WAVE) + r'''
      <circle id="pk" cx="380" cy="560" r="14" fill="#fff" opacity="0"/><circle id="tr" cx="650" cy="960" r="14" fill="#fff" opacity="0"/></svg>
    <div class="lab" id="pkl" style="position:absolute;left:300px;top:490px;color:#fff;opacity:0">SEÇİM ▲</div>
    <div class="rbox" id="trl" style="left:560px;top:1010px;width:230px;height:76px;border-radius:12px;font-size:40px;opacity:0">FATURA</div>
    <div class="ph" id="nh" style="left:130px;top:830px;width:200px;height:200px;opacity:0;border-radius:50%"><img src="media/nordhaus.jpg" style="object-position:50% 22%"></div>
    <div class="lab" id="nhl" style="position:absolute;left:110px;top:1045px;opacity:0;font-size:20px;line-height:1.5">NORDHAUS · 1975<br>POLİTİK KONJONKTÜR DÖNGÜSÜ</div>
    <div class="gbox" id="pkd" style="left:110px;top:840px;width:400px;height:110px;opacity:0"><div class="serif" style="font-size:40px">politik konjonktür döngüsü</div></div>
  </section>
  <section id="s4" class="scene clip">
    ''' + title('t4', '2023 Seçiminden', '<i>Önce</i> Ne Oldu?') + r'''
    <div class="gbox" id="b41" style="left:110px;top:520px;width:860px;height:230px">
      <div class="lab">ASGARİ ÜCRET · OCAK 2023</div><div class="num glowt" style="color:#fff">+%54,66</div></div>
    <div class="gbox" id="b42" style="left:110px;top:800px;width:860px;height:230px">
      <div class="lab">POLİTİKA FAİZİ · ŞUBAT 2023</div><div class="num glowt">%8,5</div></div>
  </section>
  <section id="s4b" class="scene clip">
    ''' + title('t4b', 'Seçimden Sonra', 'Gelen <i>Fatura</i>') + r'''
    <svg class="gl" style="left:0;top:0" width="1080" height="1200">
      <line id="ax1" x1="''' + str(X0) + '" y1="' + str(Y0 + CH) + '" x2="960" y2="' + str(Y0 + CH) + r'''" stroke="#fff" stroke-width="3"/>
      <line id="ax2" x1="''' + str(X0) + '" y1="430" x2="' + str(X0) + '" y2="' + str(Y0 + CH) + r'''" stroke="#fff" stroke-width="3"/>
      <line x1="''' + f'{xm(3):.0f}' + '" y1="430" x2="' + f'{xm(3):.0f}' + '" y2="' + str(Y0 + CH) + r'''" stroke="rgba(255,255,255,.3)" stroke-width="2" stroke-dasharray="6 8"/>
      ''' + glow_path('c1', P1) + glow_path('c2', P2) + r'''
      <circle id="cd0" cx="''' + f'{xm(0):.0f}" cy="{yv(8.5):.0f}' + r'''" r="12" fill="#fff"/>
      <circle id="cd1" cx="''' + f'{xm(6):.0f}" cy="{yv(25):.0f}' + r'''" r="13" fill="#fff" opacity="0"/>
      <circle id="cd2" cx="''' + f'{xm(13):.0f}" cy="{yv(50):.0f}' + r'''" r="15" fill="#fff" opacity="0" style="filter:drop-shadow(0 0 10px #fff)"/></svg>
    <div class="ring" id="rg2" style="left:''' + f'{xm(13):.0f}px;top:{yv(50):.0f}' + r'''px"></div>
    <div class="a" style="left:''' + f'{xm(0) + 24:.0f}px;top:{yv(8.5) - 70:.0f}' + r'''px;font:800 44px 'Inter Tight'">%8,5</div>
    <div class="lab" style="position:absolute;left:''' + f'{xm(3) - 70:.0f}' + r'''px;top:395px;font-size:22px;color:#fff">SEÇİM ▼ 28 MAYIS</div>
    <div class="a" id="l25" style="left:''' + f'{xm(6) - 160:.0f}px;top:{yv(25) - 40:.0f}' + r'''px;font:800 50px 'Inter Tight';opacity:0">%25 <span class="lab" style="font-size:20px">AĞU 23</span></div>
    <div class="a" id="l50" style="left:''' + f'{xm(13) - 260:.0f}px;top:{yv(50) + 26:.0f}' + r'''px;font:800 74px 'Inter Tight';opacity:0">%50 <span class="lab" style="font-size:20px">MAR 24</span></div>
    <div class="lab" style="position:absolute;left:''' + str(X0) + 'px;top:' + str(Y0 + CH + 16) + r'''px;font-size:20px">POLİTİKA FAİZİ · TCMB</div>
    <div class="rbox" id="usd" style="left:150px;top:1030px;width:780px;height:120px;border-radius:16px;opacity:0;font-size:58px">DOLAR/TL &nbsp;20&nbsp;→&nbsp;<span id="usdn">20</span></div>
  </section>
  <section id="s5" class="scene clip">
    <div class="a" id="dk" style="left:60px;right:60px;top:560px;text-align:center;opacity:0">
      <div class="lab" style="color:#ff5a4f;letter-spacing:.3em;margin-bottom:26px">AMA</div>
      <div style="font:800 92px/1.02 'Inter Tight';letter-spacing:-.03em">Döngü her seferinde</div>
      <div style="font:italic 400 110px 'DM Serif Display';color:#ff3b30;text-shadow:0 0 30px rgba(255,59,48,.5)">işlemiyor.</div></div>
  </section>
  <section id="s6" class="scene clip">
    ''' + title('t6a', 'Döngü Her Zaman', '<i>Çalışmıyor</i>') + title('t6b', 'Tarih Bile', '<i>Kesin</i> Değil') + r'''
    <div id="g6a">
      <div class="lab" style="position:absolute;left:150px;top:470px">BIST 100 · 2015 (SEÇİM YILI)</div>
      <div class="a" style="left:150px;top:520px;width:780px;height:420px;border-bottom:3px solid #fff">
        <div class="bar" id="bb" style="left:120px;width:220px;height:300px;background:linear-gradient(#fff,rgba(255,255,255,.25))"></div>
        <div class="bar" id="br" style="left:440px;width:220px;height:251px;background:linear-gradient(#ff3b30,rgba(255,59,48,.2));box-shadow:0 0 40px rgba(255,59,48,.4)"></div></div>
      <div class="lab" style="position:absolute;left:290px;top:956px">OCAK</div><div class="lab" style="position:absolute;left:610px;top:956px">ARALIK</div>
      <div class="a redt" id="bsn" style="left:605px;top:580px;font:800 90px 'Inter Tight';opacity:0">−%16</div></div>
    <div id="g6b" style="opacity:0">
      <div class="kup" id="k1" style="top:430px"><div class="s">HABERTÜRK · 25.06.2026</div><div class="h">Mehmet Uçum: 16 Nisan 2028 tarihi erken seçim tarihi değil</div></div>
      <div class="gbox" id="c7" style="left:140px;top:760px;width:360px;height:150px"><div class="lab">OLAĞAN</div><div class="num" style="font-size:66px">7 MAYIS</div></div>
      <div class="gbox" id="c16" style="left:580px;top:760px;width:360px;height:150px"><div class="lab">KONUŞULAN</div><div class="num" style="font-size:66px">16 NİSAN</div></div>
      <div class="rbox" id="als" style="left:190px;top:960px;width:700px;height:120px;border-radius:16px;opacity:0">AL SİNYALİ DEĞİL</div></div>
  </section>
  <section id="s7" class="scene clip">
    ''' + title('t7', 'İşte O', 'Tek <i>Soru</i>') + r'''
    <div class="gbox" id="q7" style="left:110px;top:560px;width:860px;height:420px;border-color:rgba(255,59,48,.7);box-shadow:0 0 60px rgba(255,59,48,.25)">
      <div class="lab" style="color:#ff5a4f;letter-spacing:.3em;margin-bottom:22px">KENDİNE SOR</div>
      <div class="serif" style="font-size:76px;line-height:1.08">Param seçimden sonraki<br><span style="color:#ff3b30">faturaya</span> hazır mı?</div></div>
  </section>
  <section id="s8" class="scene clip">
    ''' + title('t8', 'Bunu Gönder', '<i>Kredi</i> Düşünen Arkadaşına') + r'''
    <svg class="ico" id="pl" style="left:420px;top:560px" width="240" height="240" viewBox="0 0 120 120"><path d="M10,58 L110,12 L78,108 L56,68 Z M56,68 L110,12"/></svg>
  </section>
  <section id="s9" class="scene clip">
    ''' + title('t9', 'Önemli Olan', '<i>Fatura</i> Tarihi') + r'''
    <div class="gbox" id="d9" style="left:250px;top:470px;width:580px;height:300px">
      <div class="lab">ZENGİN OLMA TARİHİ</div><div class="num" style="font-size:110px;color:rgba(255,255,255,.55)">7 MAYIS 2028</div></div>
    <div class="strk" id="x9" style="left:280px;top:640px;width:520px"></div>
    <div class="rbox" id="f9" style="left:250px;top:830px;width:580px;height:150px;border-radius:18px;opacity:0;font-size:66px">FATURA TARİHİ</div>
  </section>
'''

SCENE_JS = JS + r'''
// S1 — kanca: başlık ilk karede hazır (üçlü kanca: söz + başlık + takvim kartı)
tl.set('#t1',{opacity:1},0); pop('#d1',3.2); dr('#arc1',3.5,.7);
// S2 — kredi riski + kilitli tek soru (açık döngü)
ttl('#t2',6.55); pop('#b21',7.35); dr('#ar2',7.75,.35); pop('#b22',8.0); pop('#b23',9.6,{y:30});
// S3 — döngü dalgası, Nordhaus, fatura
ttl('#t3a',12.3); dr('#wv, #wv_g',12.9,1.6); tl.to('#pk',{opacity:1,duration:.2},14.2); fin('#pkl',14.25);
fin('#nh',15.15); fin('#nhl',15.35); 
fout('#t3a',18.2,.25); ttl('#t3b',18.45); tl.to('#tr',{opacity:1,duration:.2},18.8); pop('#trl',18.8);
// S4 — seçimden önce
ttl('#t4',20.7); pop('#b41',23.45); pop('#b42',26.0);
// S4b — fatura grafiği + dolar
ttl('#t4b',27.6); dr('#c1, #c1_g',28.7,1.1,'power2.in'); tl.to('#cd1',{opacity:1,duration:.15},29.8); fin('#l25',29.86,{y:12});
dr('#c2, #c2_g',30.4,2.4,'power2.inOut'); tl.to('#cd2',{opacity:1,duration:.15},32.8); fin('#l50',32.85,{y:12});
tl.fromTo('#rg2',{opacity:.9,scale:.5},{opacity:0,scale:2.4,duration:.7,ease:'power2.out'},32.9);
pop('#usd',34.1); {const o={v:20};tl.fromTo(o,{v:20},{v:32,duration:1.6,ease:'power2.inOut',onUpdate:()=>{$('#usdn').textContent=Math.round(o.v);}},34.6);}
// S5 — desen kırılması: her şey kararır, tek cümle
tl.to('.bg',{opacity:.25,duration:.3},36.75); fin('#dk',36.9,{y:20,d:.45}); tl.to('#dk',{opacity:0,duration:.25},38.95); tl.to('.bg',{opacity:1,duration:.4},39.0);
// S6 — 2015 borsa, tarih tartışması, al sinyali değil
ttl('#t6a',39.3); tl.fromTo('#bb',{scaleY:0,transformOrigin:'50% 100%'},{scaleY:1,duration:.6,ease:'power3.out'},39.5);
tl.fromTo('#br',{scaleY:0,transformOrigin:'50% 100%'},{scaleY:1,duration:.6,ease:'power3.out'},40.3); pop('#bsn',41.4);
fout('#g6a',42.0,.25); fout('#t6a',42.0,.25); ttl('#t6b',42.3); tl.to('#g6b',{opacity:1,duration:.01},42.25); fin('#k1',42.3);
pop('#c7',43.0); pop('#c16',43.7); pop('#als',46.2,{s:1.25});
// S7 — tek soru
ttl('#t7',47.65); pop('#q7',48.4);
// S8 — CTA
ttl('#t8',51.55); tl.fromTo('#pl',{opacity:0,x:-120,y:60,rotation:-10},{opacity:1,x:0,y:0,rotation:0,duration:.7,ease:'expo.out'},51.9);
tl.to('#pl',{x:500,y:-300,opacity:0,duration:.6,ease:'power3.in'},54.2);
// S9 — döngü: zengin olma tarihi çizilir, fatura tarihi
ttl('#t9',54.9); pop('#d9',55.2); strike('#x9',57.35); pop('#f9',58.05,{s:1.2});
'''


def SFX(A):
    return [[3.1, 'f:p_whoosh', -12, 0, 'takvim'], [7.3, 'f:p_klik', -12, 0, 'kredi'], [9.5, 'f:p_whoosh', -13, 0, 'kilit'],
            [12.75, 'f:p_whoosh', -13, 0, 'dalga'], [18.7, 'f:p_klik', -11, 0, 'fatura'],
            [23.4, 'f:p_klik', -12, 0, '%54'], [25.95, 'f:p_klik', -12, 0, '%8,5'], [27.3, 'f:p_whoosh_bas', -11, 1, 'sonra'],
            [29.8, 'f:p_klik', -12, 0, '%25'], [32.75, 'f:p_boom', -9, 1, '%50'], [34.0, 'f:p_whoosh', -13, 0, 'dolar'],
            [36.8, 'f:p_boom', -8, 1, 'desen kirilmasi'], [39.3, 'f:p_whoosh', -13, 0, 'bist'], [41.35, 'f:p_klik', -11, 0, '-16'],
            [42.15, 'f:p_whoosh', -13, 0, 'kupur'], [46.15, 'f:p_boom', -10, 1, 'al sinyali degil'], [48.3, 'f:p_whoosh', -13, 0, 'soru'],
            [51.8, 'f:p_whoosh', -13, 0, 'cta'], [55.1, 'f:p_klik', -12, 0, 'takvim'], [57.95, 'f:p_whoosh_bas', -11, 1, 'fatura tarihi']]


def RISERS(A): return []


# ---- v3 (Ata 23 Eki 16:17): ses 1.0 hız + cümle arası duraklama; avatar SADECE giriş/vurgu/çıkışta BÜYÜK kartta (HERO).
# Eski (0.93) zamanlamayla yazılmış her şey kelime eşlemesiyle yeni sese taşınır (kit/retime.py).
import json as _json
from retime import remap as _remap, retime_js as _retime_js, scene_bounds as _scene_bounds
from panel_kit import HERO as _HERO
_RT = _remap(os.path.join(W, 'v093', 'words.json'), os.path.join(W, 'words.json'))
_SEGS = _json.load(open(os.path.join(W, 'segments.json')))['segments']
_AVS = {'s1', 's5', 's7', 's8', 's9'}
_scenes_old = scenes


def scenes(A):
    old = _scenes_old(A)
    return _scene_bounds([(k, _RT(a), (DUR if i == len(old) - 1 else _RT(b)), k in _AVS) for i, (k, a, b) in enumerate(old)], _SEGS, DUR)


AV = {k: (_HERO if k in _AVS else None) for k in AV}
SCENE_JS = _retime_js(SCENE_JS, _RT)
_sfx_old = SFX


def SFX(A):
    return [[_RT(x[0])] + list(x[1:]) for x in _sfx_old(A)]
