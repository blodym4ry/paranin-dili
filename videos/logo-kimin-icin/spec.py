import os
from panel_kit import CARD, JS, title, glow_path, SVG_DEFS
# LOGO KİMİN İÇİN — PANEL stili (güvenli alan). Avatar: kahverengi kapüşon + gözlük (bca40a0e…), video boyunca kartta. Müzik: onaylı aday 1.
# Kaynak: Han, Nunes & Drèze (2010) Journal of Marketing; Buffett evi (kaynaklar.md). Senaryo 4 bağımsız inceleme turu.
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [(N('iki', 'bin', 'onda'), "2010'da"), (N('bin', 'dokuz', 'yüz', 'elli', 'sekizde'), "1958'de"), (N('otuz', 'bir', 'bin', 'beş', 'yüz'), '31.500')]
EM = {'pahalı', 'sinyal', 'vergisi', 'soru', 'gönder'}
RED = {'sahtesini', 'değil'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False

SC_ = [('s1', 0, 4.25), ('s2', 4.25, 7.45), ('s3', 7.45, 17.35), ('s4', 17.35, 36.45), ('s5', 36.45, 39.0), ('s6', 39.0, 44.38),
       ('s7', 44.38, 56.0), ('s8', 56.0, 59.95), ('s9', 59.95, 63.3), ('s10', 63.3, None)]


def scenes(A):
    return [(k, a, b if b is not None else DUR) for k, a, b in SC_]


AV = {k: CARD for k, _, _ in SC_}


def bag(id_, x, y, loud=False, red=False, s=1.0):
    col = '#ff3b30' if red else '#fff'
    logo = ('<text x="110" y="150" text-anchor="middle" font-family="DM Serif Display" font-size="90" fill="%s">LG</text>' % col) if loud else \
           ('<text x="110" y="128" text-anchor="middle" font-family="DM Serif Display" font-size="20" fill="%s" opacity=".8">lg</text>' % col)
    return (f'<svg id="{id_}" style="position:absolute;left:{x}px;top:{y}px;overflow:visible;filter:drop-shadow(0 0 12px rgba(255,255,255,.25))" width="{220 * s:.0f}" height="{230 * s:.0f}" viewBox="0 0 220 230">'
            f'<path d="M70,70 C70,20 150,20 150,70" fill="none" stroke="{col}" stroke-width="7"/>'
            f'<rect x="20" y="70" width="180" height="150" rx="18" fill="rgba(255,255,255,.04)" stroke="{col}" stroke-width="6"/>{logo}</svg>')


HOUSE = '<svg width="200" height="170" viewBox="0 0 200 170" style="fill:none;stroke:#fff;stroke-width:7;stroke-linejoin:round;filter:drop-shadow(0 0 10px rgba(255,255,255,.5))"><path d="M20,80 L100,15 L180,80 M40,65 V160 H160 V65 M85,160 V110 H115 V160"/></svg>'
UP = 'M150,1120 C330,1110 470,1080 600,1030 C740,975 850,920 960,880'

EXTRA_CSS = r'''<style>
.chip{position:absolute;padding:14px 26px;border-radius:14px;font:800 40px 'Inter Tight';white-space:nowrap}
.chip.g{border:1.5px solid rgba(255,255,255,.45);background:rgba(255,255,255,.04);color:#fff}
.strk{position:absolute;height:6px;background:#ff3b30;box-shadow:0 0 14px #ff3b30;transform:scaleX(0);transform-origin:0 50%}
.bar{position:absolute;left:150px;height:96px;border-radius:0 14px 14px 0;transform-origin:0 50%}
.row{position:absolute;left:90px;right:90px;height:150px;display:flex;align-items:center;gap:30px;border-bottom:1.5px solid rgba(255,255,255,.12)}
.row .who{flex:1;font:800 56px/1.05 'Inter Tight';color:#fff}
.row .who small{display:block;font:500 26px 'IBM Plex Mono';color:var(--mut);letter-spacing:.1em;margin-top:8px}
.row .what{font:800 46px 'Inter Tight';padding:12px 24px;border-radius:12px;white-space:nowrap}
</style>'''

SCENE_HTML = r'''
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">
    ''' + title('t1', 'Logosu Küçük Çanta', 'Neden Daha <i>Pahalı?</i>') + r'''
    <div class="lab" style="position:absolute;left:190px;top:440px">SESSİZ</div><div class="lab" style="position:absolute;left:660px;top:440px">GÖSTERİŞLİ</div>
    ''' + bag('bg1', 140, 500, red=True, s=1.3) + bag('bg2', 600, 500, loud=True, s=1.3) + r'''
    <div class="num redt" id="p1" style="position:absolute;left:210px;top:830px;font-size:90px">$$$</div>
    <div class="num" id="p2" style="position:absolute;left:700px;top:830px;font-size:90px">$$</div>
    <div class="chip g" id="al" style="left:280px;top:990px;opacity:0">ALÇAKGÖNÜLLÜLÜK?</div>
    <div class="strk" id="xal" style="left:290px;top:1022px;width:500px"></div>
  </section>
  <section id="s2" class="scene clip">
    ''' + title('t2', 'Sonunda', 'Tek <i>Soru</i>') + r'''
    <div class="gbox" id="b2" style="left:240px;top:520px;width:600px;height:360px">
      <svg width="90" height="100" viewBox="0 0 90 100" style="stroke:#fff;fill:none;stroke-width:6;filter:drop-shadow(0 0 8px rgba(255,255,255,.6))"><rect x="10" y="44" width="70" height="50" rx="10"/><path d="M24,44 V30 a21,21 0 0 1 42,0 V44"/></svg>
      <div class="num" style="font-size:62px;margin-top:12px">ALMADAN ÖNCE</div><div class="lab" style="margin-top:8px">VİDEONUN SONUNDA</div></div>
  </section>
  <section id="s3" class="scene clip">
    ''' + title('t3', 'Lüks Çanta', '<i>Fiyatları</i> · 2010') + r'''
    <div class="lab" id="src3" style="position:absolute;left:150px;top:440px;opacity:0">JOURNAL OF MARKETING · USC/UCLA</div>
    <div class="chip g" id="ch3" style="left:150px;top:500px;opacity:0">AYNI MARKA</div>
    <div class="lab" style="position:absolute;left:150px;top:650px">BÜYÜK LOGO</div>
    <div class="bar" id="br1" style="top:690px;width:560px;background:linear-gradient(90deg,rgba(255,255,255,.9),rgba(255,255,255,.35))"></div>
    <div class="lab" style="position:absolute;left:150px;top:830px">KÜÇÜK LOGO</div>
    <div class="bar" id="br2" style="top:870px;width:780px;background:linear-gradient(90deg,#ff3b30,rgba(255,59,48,.35));box-shadow:0 0 40px rgba(255,59,48,.35)"></div>
    <div class="a" id="pd" style="left:540px;top:990px;font:800 56px 'Inter Tight';color:#ff3b30;opacity:0">+ birkaç yüz $</div>
  </section>
  <section id="s4" class="scene clip">
    ''' + title('t4', 'Peki Kim', '<i>Hangisini</i> Alıyor?') + r'''
    <div class="row" id="r1" style="top:430px;opacity:0"><div class="who">Parası var, gösteriş yok<small id="r1s" style="opacity:0">SİNYAL: SADECE KENDİ ÇEVRESİNE</small></div><div class="what" style="border:1.5px solid rgba(255,255,255,.5)">SESSİZ</div></div>
    <div class="row" id="r2" style="top:600px;opacity:0"><div class="who">Yeni zenginler</div><div class="what" style="background:linear-gradient(90deg,#7a0a0a,#b01212)">BÜYÜK LOGO</div></div>
    <div class="row" id="r3" style="top:770px;opacity:0"><div class="who">Zengin görünmek isteyenler</div><div class="what" style="border:2px dashed #ff3b30;color:#ff3b30">SAHTESİ</div></div>
    <div class="rbox" id="sk" style="left:90px;top:960px;width:900px;height:110px;border-radius:16px;font-size:35px;opacity:0">SAHTECİ ÇOĞUNLUKLA BÜYÜK LOGOYU KOPYALAR</div>
  </section>
  <section id="s5" class="scene clip">
    <div class="a" id="dk" style="left:60px;right:60px;top:600px;text-align:center;opacity:0">
      <div style="font:800 88px/1.02 'Inter Tight';letter-spacing:-.03em">Satılan şey çanta değil,</div>
      <div style="font:italic 400 120px 'DM Serif Display';color:#ff3b30;text-shadow:0 0 30px rgba(255,59,48,.5)">sinyal.</div></div>
  </section>
  <section id="s6" class="scene clip">
    ''' + title('t6', 'Markaya Ödediğin Fazla', 'Sinyal <i>Vergisi</i>') + r'''
    <div class="lab" style="position:absolute;left:150px;top:520px">ÖDEDİĞİN FİYAT</div>
    <div class="a" id="pb" style="left:150px;top:570px;width:780px;height:140px;display:flex;border-radius:16px;overflow:hidden">
      <div style="width:55%;background:rgba(255,255,255,.85);color:#111;font:800 40px 'Inter Tight';display:flex;align-items:center;justify-content:center">ÜRÜN</div>
      <div id="pv" style="width:45%;background:linear-gradient(90deg,#b01212,#ff3b30);color:#fff;font:800 40px 'Inter Tight';display:flex;align-items:center;justify-content:center;transform-origin:0 50%">SİNYAL VERGİSİ</div></div>
    <div class="chip g" id="c6a" style="left:150px;top:780px;opacity:0">KÜÇÜK LOGO</div><div class="chip g" id="c6b" style="left:560px;top:780px;opacity:0">BÜYÜK LOGO</div>
    <div class="lab" id="c6c" style="position:absolute;left:150px;top:900px;opacity:0">İKİSİNDE DE VAR</div>
  </section>
  <section id="s7" class="scene clip">
    ''' + title('t7', 'En Zenginlerden Biri', 'Nerede <i>Yaşıyor?</i>') + r'''
    <div class="gbox" id="hb" style="left:240px;top:430px;width:600px;height:420px">
      ''' + HOUSE + r'''<div class="lab" style="margin-top:14px">BUFFETT · OMAHA · 1958</div>
      <div class="num glowt" id="hp" style="font-size:110px;opacity:0">31.500 $</div></div>
    <svg class="gl" style="left:0;top:0" width="1080" height="1200">''' + glow_path('up', UP) + r'''</svg>
    <div class="lab" id="upl" style="position:absolute;left:620px;top:1080px;opacity:0;color:#fff">PARA ÇALIŞIYOR</div>
  </section>
  <section id="s8" class="scene clip">
    ''' + title('t8', 'İşte O', 'Tek <i>Soru</i>') + r'''
    <div class="gbox" id="q8" style="left:110px;top:520px;width:860px;height:440px;border-color:rgba(255,59,48,.7);box-shadow:0 0 60px rgba(255,59,48,.25)">
      <div class="lab" style="color:#ff5a4f;letter-spacing:.3em;margin-bottom:22px">ALMADAN ÖNCE SOR</div>
      <div class="serif" style="font-size:84px;line-height:1.08">Markası olmasa<br>bunu yine <span style="color:#ff3b30">alır mıydım?</span></div></div>
  </section>
  <section id="s9" class="scene clip">
    ''' + title('t9', 'Bunu Gönder', '<i>Taksitle</i> Marka Alacak Arkadaşına') + r'''
    <svg id="pl" style="position:absolute;left:420px;top:560px;stroke:#fff;fill:none;stroke-width:5;stroke-linejoin:round;filter:drop-shadow(0 0 8px rgba(255,255,255,.5))" width="240" height="240" viewBox="0 0 120 120"><path d="M10,58 L110,12 L78,108 L56,68 Z M56,68 L110,12"/></svg>
  </section>
  <section id="s10" class="scene clip">
    ''' + title('t10', 'Küçük Logo', 'Kime <i>Satılır?</i>') + r'''
    ''' + bag('bg3', 140, 480, red=True, s=1.3) + bag('bg4', 600, 480, loud=True, s=1.3) + r'''
    <div class="rbox" id="r10" style="left:90px;top:900px;width:900px;height:130px;border-radius:16px;font-size:44px;opacity:0">KENDİNİ KANITLAMASI GEREKMEYENE</div>
  </section>
'''

SCENE_JS = JS + r'''
// S1 — kanca: başlık + iki çanta + fiyat ilk karede (üçlü kanca)
tl.set('#t1',{opacity:1},0); pop('#al',2.6); strike('#xal',3.5);
// S2 — açık döngü
ttl('#t2',4.35); pop('#b2',4.6);
// S3 — araştırma
ttl('#t3',7.55); fin('#src3',8.6); pop('#ch3',12.3);
tl.fromTo('#br1',{scaleX:0},{scaleX:1,duration:.7,ease:'power3.out'},14.3); tl.fromTo('#br2',{scaleX:0},{scaleX:1,duration:.9,ease:'power3.out'},13.6); pop('#pd',15.5);
// S4 — kim hangisini alıyor (harita)
ttl('#t4',17.5); fin('#r1',19.1); fin('#r1s',24.1,{y:8}); fin('#r2',27.6); fin('#r3',30.4); pop('#sk',33.5);
// S5 — desen kırılması
tl.to('.bg',{opacity:.25,duration:.3},36.45); fin('#dk',36.6,{y:20,d:.45}); tl.to('#dk',{opacity:0,duration:.25},38.75); tl.to('.bg',{opacity:1,duration:.4},38.8);
// S6 — sinyal vergisi
ttl('#t6',39.1); fin('#pb',39.4); tl.fromTo('#pv',{scaleX:0},{scaleX:1,duration:.7,ease:'power3.out'},43.2);
pop('#c6a',39.9); pop('#c6b',40.6); fin('#c6c',41.5);
// S7 — Buffett
ttl('#t7',44.5); pop('#hb',47.1); pop('#hp',49.8); dr('#up, #up_g',52.8,1.4); fin('#upl',54.6);
// S8 — tek soru
ttl('#t8',56.1); pop('#q8',57.4);
// S9 — CTA
ttl('#t9',60.1); tl.fromTo('#pl',{opacity:0,x:-120,y:60,rotation:-10},{opacity:1,x:0,y:0,rotation:0,duration:.7,ease:'expo.out'},60.4);
tl.to('#pl',{x:500,y:-300,opacity:0,duration:.6,ease:'power3.in'},62.7);
// S10 — döngü
ttl('#t10',63.4); tl.to('#bg4',{opacity:.3,duration:.3},64.4); pop('#r10',65.6);
'''


def SFX(A):
    return [[2.5, 'f:p_klik', -12, 0, 'alcakgonulluluk'], [4.4, 'f:p_whoosh', -13, 0, 'kilit'], [7.5, 'f:p_whoosh', -13, 0, 'arastirma'],
            [12.2, 'f:p_klik', -12, 0, 'ayni marka'], [13.5, 'f:p_whoosh', -13, 0, 'bar'], [15.4, 'f:p_boom', -10, 1, 'birkac yuz'],
            [19.0, 'f:p_klik', -12, 0, 'r1'], [27.5, 'f:p_klik', -12, 0, 'r2'], [30.3, 'f:p_klik', -12, 0, 'r3'], [33.4, 'f:p_whoosh_bas', -11, 1, 'sahteci'],
            [36.45, 'f:p_boom', -8, 1, 'desen kirilmasi'], [39.3, 'f:p_whoosh', -13, 0, 'fiyat'], [43.1, 'f:p_whoosh_bas', -11, 1, 'vergi'],
            [47.0, 'f:p_whoosh', -13, 0, 'ev'], [49.7, 'f:p_boom', -10, 1, '31500'], [52.7, 'f:p_whoosh', -13, 0, 'calisiyor'],
            [57.3, 'f:p_klik', -11, 0, 'soru'], [60.3, 'f:p_whoosh', -13, 0, 'cta'], [63.4, 'f:p_whoosh', -13, 0, 'dongu'], [65.5, 'f:p_whoosh_bas', -11, 1, 'kanitlamasi']]


def RISERS(A): return []


# ---- v3 (Ata 23 Eki 16:17): ses 1.0 hız + cümle arası duraklama; avatar SADECE giriş/vurgu/çıkışta BÜYÜK kartta (HERO).
# Eski (0.93) zamanlamayla yazılmış her şey kelime eşlemesiyle yeni sese taşınır (kit/retime.py).
import json as _json
from retime import remap as _remap, retime_js as _retime_js, scene_bounds as _scene_bounds
from panel_kit import HERO as _HERO
_RT = _remap(os.path.join(W, 'v093', 'words.json'), os.path.join(W, 'words.json'))
_SEGS = _json.load(open(os.path.join(W, 'segments.json')))['segments']
_AVS = {'s1', 's2', 's5', 's9', 's10'}
_scenes_old = scenes


def scenes(A):
    old = _scenes_old(A)
    return _scene_bounds([(k, _RT(a), (DUR if i == len(old) - 1 else _RT(b)), k in _AVS) for i, (k, a, b) in enumerate(old)], _SEGS, DUR)


AV = {k: (_HERO if k in _AVS else None) for k in AV}
SCENE_JS = _retime_js(SCENE_JS, _RT)
_sfx_old = SFX


def SFX(A):
    return [[_RT(x[0])] + list(x[1:]) for x in _sfx_old(A)]
