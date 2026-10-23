import os
from panel_kit import CARD, JS, title, glow_path, SVG_DEFS
# YAPAY ZEKÂ BEYAZ YAKAYI SİLER Mİ — PANEL stili. Avatar: gri (1bc300c1…), video boyunca kartta. Müzik: onaylı aday 3.
# Kaynak: Stanford Digital Economy Lab "Canaries" Ağu 2026 (kaynaklar.md). Senaryo 3 bağımsız incelemeden sonra düzeltildi.
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [(N('yirmi', 'iki'), '22'), (N('yirmi', 'beş'), '25'), (N('yüzde', 'on', 'dokuz'), '%19'), (N('yüzde', 'on', 'beşti'), "%15'ti")]
EM = {'silecek', 'basamak', 'ayrım', 'gönder', 'yardımcısı'}
RED = {'çıkarılmıyor', 'silinmiyor', 'daralıyor'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False

SC_ = [('s1', 0, 5.0), ('s2', 5.0, 7.8), ('s3', 7.8, 19.85), ('s4', 19.85, 22.7), ('s5', 22.7, 30.28), ('s6', 30.28, 35.42),
       ('s7', 35.42, 37.4), ('s8', 37.4, 45.1), ('s9', 45.1, 54.05), ('s10', 54.05, 56.95), ('s11', 56.95, None)]


def scenes(A):
    return [(k, a, b if b is not None else DUR) for k, a, b in SC_]


AV = {k: CARD for k, _, _ in SC_}


def people(id_, x, y, cols, rows, gap=92, red_rows=(), op=1):
    """Kişi ikonu ızgarası (her ikon id_r{r}c{c})."""
    out = []
    for r in range(rows):
        for c in range(cols):
            col = '#ff3b30' if r in red_rows else '#fff'
            out.append(f'<svg class="pp" id="{id_}r{r}c{c}" style="position:absolute;left:{x + c * gap}px;top:{y + r * gap}px;opacity:{op}" width="56" height="64" viewBox="0 0 56 64">'
                       f'<circle cx="28" cy="18" r="13" fill="{col}"/><path d="M4,62 C4,40 52,40 52,62 Z" fill="{col}"/></svg>')
    return ''.join(out)


STAIR = 'M140,1000 L140,880 L330,880 L330,760 L520,760 L520,640 L710,640 L710,520 L900,520 L900,400'
STEP1 = 'M140,1000 L140,880 L330,880'

EXTRA_CSS = r'''<style>
.pp{filter:drop-shadow(0 0 8px rgba(255,255,255,.35))}
.chip{position:absolute;padding:14px 26px;border-radius:14px;font:800 40px 'Inter Tight';white-space:nowrap}
.chip.g{border:1.5px solid rgba(255,255,255,.45);background:rgba(255,255,255,.04);color:#fff}
.chip.dim{border:1.5px solid rgba(255,255,255,.18);color:rgba(255,255,255,.45)}
.strk{position:absolute;height:6px;background:#ff3b30;box-shadow:0 0 14px #ff3b30;transform:scaleX(0);transform-origin:0 50%}
.bar{position:absolute;left:150px;height:96px;border-radius:0 14px 14px 0;transform-origin:0 50%}
.chk{display:flex;align-items:center;gap:22px;font:800 46px 'Inter Tight';color:#fff;margin:14px 0}
.chk b{width:46px;height:46px;border:4px solid #fff;border-radius:10px;display:inline-block;flex:none}
</style>'''

SCENE_HTML = r'''
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">
    ''' + title('t1', 'Yapay Zekâ Beyaz Yakayı', '<i>Silecek</i> mi?') + r'''
    <div id="g1">''' + people('a', 218, 520, 6, 4) + r'''</div>
  </section>
  <section id="s2" class="scene clip">
    ''' + title('t2', 'Sonunda', 'Ayakta <i>Kalan</i> Beyaz Yaka') + r'''
    <div class="gbox" id="b2" style="left:240px;top:560px;width:600px;height:330px">
      <svg width="90" height="100" viewBox="0 0 90 100" style="stroke:#fff;fill:none;stroke-width:6;filter:drop-shadow(0 0 8px rgba(255,255,255,.6))"><rect x="10" y="44" width="70" height="50" rx="10"/><path d="M24,44 V30 a21,21 0 0 1 42,0 V44"/></svg>
      <div class="num" style="font-size:66px;margin-top:12px">VİDEONUN SONUNDA</div></div>
  </section>
  <section id="s3" class="scene clip">
    ''' + title('t3', 'Stanford', '<i>Bordro</i> Verisine Baktı') + r'''
    <div class="lab" id="src3" style="position:absolute;left:150px;top:440px;opacity:0">STANFORD · AĞUSTOS 2026 · ABD</div>
    <div class="chip g" id="ch3" style="left:150px;top:500px;opacity:0">22–25 YAŞ</div>
    <div class="lab" style="position:absolute;left:150px;top:640px">AZ AÇIK MESLEKLER</div>
    <div class="bar" id="br1" style="top:680px;width:780px;background:linear-gradient(90deg,rgba(255,255,255,.9),rgba(255,255,255,.35))"></div>
    <div class="lab" style="position:absolute;left:150px;top:820px">YAPAY ZEKÂYA EN AÇIK MESLEKLER</div>
    <div class="bar" id="br2" style="top:860px;width:632px;background:linear-gradient(90deg,#ff3b30,rgba(255,59,48,.35));box-shadow:0 0 40px rgba(255,59,48,.35)"></div>
    <div class="a redt" id="n19" style="left:800px;top:868px;font:800 80px 'Inter Tight';opacity:0">−%19</div>
    <div class="lab" style="position:absolute;left:150px;top:1000px;font-size:20px">İSTİHDAM · YAŞITLARA GÖRE · HAZİRAN 2026</div>
  </section>
  <section id="s4" class="scene clip">
    ''' + title('t4', 'Fark', '<i>Büyüyor</i>') + r'''
    <div class="gbox" id="b4" style="left:200px;top:540px;width:680px;height:380px">
      <div class="lab">BİR YIL ÖNCEKİ VERİ → BUGÜN</div>
      <div class="num glowt" style="font-size:150px">%<span id="n4">15</span></div></div>
  </section>
  <section id="s5" class="scene clip">
    ''' + title('t5', 'Peki', '<i>Tecrübeliler?</i>') + r'''
    <div id="g5a">''' + people('e', 170, 470, 3, 2, 96) + people('y', 660, 470, 3, 2, 96, red_rows=(0, 1)) + r'''
      <div class="lab" style="position:absolute;left:180px;top:680px">TECRÜBELİ</div><div class="lab" style="position:absolute;left:690px;top:680px">22–25 YAŞ</div>
      <div class="chip g" id="ch5" style="left:150px;top:740px;opacity:0">BENZER FARK YOK</div></div>
    <div class="chip dim" id="c51" style="left:150px;top:880px;opacity:0">İŞTEN ÇIKARMA</div>
    <div class="strk" id="x51" style="left:160px;top:912px;width:330px"></div>
    <div class="rbox" id="c52" style="left:560px;top:866px;width:390px;height:90px;border-radius:14px;font-size:40px;opacity:0">İŞE ALIM ↓</div>
  </section>
  <section id="s6" class="scene clip">
    ''' + title('t6', 'İlk Basamak', '<i>Etkisi</i>') + r'''
    <svg class="gl" style="left:0;top:0" width="1080" height="1200">''' + glow_path('st', STAIR, '#ffffff', 5) + glow_path('st1', STEP1) + r'''</svg>
    <div class="lab" id="l6" style="position:absolute;left:150px;top:1020px;opacity:0;line-height:1.5">STANFORD: BETİMLEYİCİ VERİ<br>KESİN NEDEN-SONUÇ DEĞİL</div>
  </section>
  <section id="s7" class="scene clip">
    <div class="a" id="dk" style="left:60px;right:60px;top:600px;text-align:center;opacity:0">
      <div style="font:800 92px/1.02 'Inter Tight';letter-spacing:-.03em">Asıl ayrım</div>
      <div style="font:italic 400 110px 'DM Serif Display';color:#ff3b30;text-shadow:0 0 30px rgba(255,59,48,.5)">şimdi geliyor.</div></div>
  </section>
  <section id="s8" class="scene clip">
    ''' + title('t8', 'Yapay Zekâ', '<i>Yerine</i> mi, <i>Yanında</i> mı?') + r'''
    <div class="rbox" id="b81" style="left:90px;top:470px;width:430px;height:560px;border-radius:22px;flex-direction:column;font-size:44px;line-height:1.15;text-align:center">
      <div class="lab" style="color:#ffd0cc;margin-bottom:24px">GÖREVİ DEVRALIYOR</div>İstihdam<div class="num" style="font-size:150px">↓</div></div>
    <div class="gbox" id="b82" style="left:560px;top:470px;width:430px;height:560px;font:800 44px/1.15 'Inter Tight'">
      <div class="lab" style="margin-bottom:24px">YARDIMCI OLUYOR</div>İstihdam<div class="num" style="font-size:96px;margin-top:20px">SABİT / ↑</div></div>
  </section>
  <section id="s9" class="scene clip">
    ''' + title('t9', 'Ayakta Kalan', 'Beyaz <i>Yaka</i>') + r'''
    <div class="a" id="q9" style="left:80px;right:80px;top:470px;text-align:center;opacity:0"><div class="serif" style="font-size:70px">Yapay zekâyı <span style="color:#ff3b30">yardımcısı</span> yapan kişi.</div></div>
    <div class="gbox" id="b9" style="left:150px;top:720px;width:780px;height:330px;align-items:flex-start;padding:0 50px;opacity:0">
      <div class="lab" style="margin-bottom:10px">BU HAFTA: İŞLERİNİ LİSTELE</div>
      <div class="chk" id="k1" style="opacity:0"><b></b>Benim yerime yapıyor</div>
      <div class="chk" id="k2" style="opacity:0"><b style="border-color:#ff3b30"></b>Beni hızlandırıyor</div></div>
  </section>
  <section id="s10" class="scene clip">
    ''' + title('t10', 'Bunu Gönder', 'İlk İşini <i>Arayan</i> Arkadaşına') + r'''
    <svg class="ico" id="pl" style="position:absolute;left:420px;top:560px;stroke:#fff;fill:none;stroke-width:5;stroke-linejoin:round;filter:drop-shadow(0 0 8px rgba(255,255,255,.5))" width="240" height="240" viewBox="0 0 120 120"><path d="M10,58 L110,12 L78,108 L56,68 Z M56,68 L110,12"/></svg>
  </section>
  <section id="s11" class="scene clip">
    ''' + title('t11', 'Beyaz Yaka', '<i>Silinmiyor</i>') + r'''
    <svg class="gl" style="left:0;top:0" width="1080" height="1200">''' + glow_path('sz', STAIR, '#ffffff', 5) + glow_path('sz1', STEP1) + r'''</svg>
    <div class="rbox" id="r11" style="left:150px;top:1030px;width:600px;height:90px;border-radius:14px;font-size:40px;opacity:0">İLK BASAMAK DARALIYOR</div>
  </section>
'''

SCENE_JS = JS + r'''
// S1 — kanca: başlık + kişi ızgarası ilk karede; "ilk kaybeden" → alt sıra kırmızılaşır
tl.set('#t1',{opacity:1},0);
for(let c=0;c<6;c++){tl.to(`#ar3c${c} circle, #ar3c${c} path`,{fill:'#ff3b30',duration:.25},2.95+c*.06);}
// S2 — açık döngü
ttl('#t2',5.1); pop('#b2',5.4);
// S3 — Stanford verisi
ttl('#t3',7.9); fin('#src3',8.3); pop('#ch3',12.4);
tl.fromTo('#br1',{scaleX:0},{scaleX:1,duration:.8,ease:'power3.out'},15.3); tl.fromTo('#br2',{scaleX:0},{scaleX:1,duration:.9,ease:'power3.out'},16.4);
pop('#n19',18.7);
// S4 — fark büyüyor
ttl('#t4',19.95); pop('#b4',20.2); {const o={v:15};tl.fromTo(o,{v:15},{v:19,duration:.9,ease:'power2.inOut',onUpdate:()=>{$('#n4').textContent=Math.round(o.v);}},22.0);}
// S5 — tecrübeliler vs gençler; işe alım
ttl('#t5',22.8); pop('#ch5',24.5); fin('#c51',27.6); strike('#x51',28.3); pop('#c52',29.4);
// S6 — ilk basamak etkisi
ttl('#t6',30.4); dr('#st, #st_g',30.6,1.2); dr('#st1, #st1_g',31.4,.6); fin('#l6',32.8);
// S7 — desen kırılması
tl.to('.bg',{opacity:.25,duration:.3},35.42); fin('#dk',35.6,{y:20,d:.45}); tl.to('#dk',{opacity:0,duration:.25},37.15); tl.to('.bg',{opacity:1,duration:.4},37.2);
// S8 — yerine mi yanında mı
ttl('#t8',37.5); pop('#b81',37.8); pop('#b82',41.4);
// S9 — ayakta kalan + kontrol listesi
ttl('#t9',45.2); fin('#q9',45.5); pop('#b9',49.5); fin('#k1',51.0,{y:10}); fin('#k2',53.1,{y:10});
// S10 — CTA
ttl('#t10',54.15); tl.fromTo('#pl',{opacity:0,x:-120,y:60,rotation:-10},{opacity:1,x:0,y:0,rotation:0,duration:.7,ease:'expo.out'},54.4);
tl.to('#pl',{x:500,y:-300,opacity:0,duration:.6,ease:'power3.in'},56.3);
// S11 — döngü
ttl('#t11',57.05); dr('#sz, #sz_g',57.2,.9); dr('#sz1, #sz1_g',58.1,.5); pop('#r11',59.55);
'''


def SFX(A):
    return [[2.85, 'f:p_klik', -12, 0, 'kirmizi sira'], [5.2, 'f:p_whoosh', -13, 0, 'kilit'], [7.75, 'f:p_whoosh', -13, 0, 'stanford'],
            [12.35, 'f:p_klik', -12, 0, '22-25'], [16.3, 'f:p_whoosh', -13, 0, 'bar'], [18.6, 'f:p_boom', -9, 1, '-19'],
            [21.9, 'f:p_klik', -11, 0, '15->19'], [24.4, 'f:p_klik', -12, 0, 'fark yok'], [29.3, 'f:p_whoosh_bas', -11, 1, 'ise alim'],
            [30.5, 'f:p_whoosh', -13, 0, 'merdiven'], [35.4, 'f:p_boom', -8, 1, 'desen kirilmasi'], [37.7, 'f:p_whoosh', -13, 0, 'yerine'],
            [41.3, 'f:p_klik', -11, 0, 'yaninda'], [45.4, 'f:p_whoosh', -13, 0, 'ayakta'], [50.95, 'f:p_klik', -12, 0, 'k1'], [53.05, 'f:p_klik', -12, 0, 'k2'],
            [54.3, 'f:p_whoosh', -13, 0, 'cta'], [57.1, 'f:p_whoosh', -13, 0, 'dongu'], [59.45, 'f:p_whoosh_bas', -11, 1, 'daraliyor']]


def RISERS(A): return []


# ---- v3 (Ata 23 Eki 16:17): ses 1.0 hız + cümle arası duraklama; avatar SADECE giriş/vurgu/çıkışta BÜYÜK kartta (HERO).
# Eski (0.93) zamanlamayla yazılmış her şey kelime eşlemesiyle yeni sese taşınır (kit/retime.py).
import json as _json
from retime import remap as _remap, retime_js as _retime_js, scene_bounds as _scene_bounds
from panel_kit import HERO as _HERO
_RT = _remap(os.path.join(W, 'v093', 'words.json'), os.path.join(W, 'words.json'))
_SEGS = _json.load(open(os.path.join(W, 'segments.json')))['segments']
_AVS = {'s1', 's2', 's7', 's10', 's11'}
_scenes_old = scenes


def scenes(A):
    old = _scenes_old(A)
    return _scene_bounds([(k, _RT(a), (DUR if i == len(old) - 1 else _RT(b)), k in _AVS) for i, (k, a, b) in enumerate(old)], _SEGS, DUR)


AV = {k: (_HERO if k in _AVS else None) for k in AV}
SCENE_JS = _retime_js(SCENE_JS, _RT)
_sfx_old = SFX


def SFX(A):
    return [[_RT(x[0])] + list(x[1:]) for x in _sfx_old(A)]
