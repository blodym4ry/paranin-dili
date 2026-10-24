import os
from panel_kit import JS, HERO, title, SVG_DEFS
from spec_util import load, FRAME_CSS
# PARASINA DEĞER Mİ? — "Dyson" · PANEL + altın çerçeveli avatar. Look: zeytin yeşili. Kaynaklar: kaynaklar.md
U = load(); T = U.T; W = U.W; DUR = U.DUR
SRT = os.path.join(W, 'avatar_cut.srt')
N = lambda *w: list(w)
REPL = [(N('Dai', "sın'lar"), "Dyson'lar"), (N('Dai', 'sın'), 'Dyson'), (N('Dai', "sın'ı"), "Dyson'ı"), (N('Dai', "sın'ın"), "Dyson'ın"),
        (N('Ve', 'on', 'beş', 'Ditekt,'), 'V15 Detect,'), (N('Gen', 'beş', 'Ditekt,'), 'Gen5detect,'), (N('Ve', 'on', 'bir,'), 'V11,'),
        (N("Çoys'un"), "CHOICE'un"), (N('on', 'iki,'), '12,'), (N('on', 'iki;'), '12;'), (N('on', 'dört'), '14'),
        (N('otuz', 'altı', 'bin', 'liraya'), '36.000 TL\'ye'), (N('beş', 'bin', 'dört', 'yüz', 'lira.'), '5.400 TL.'), (N('"altmış'), '"60'), (N('altmış'), '60')]
EM = {'bitti.', 'değer', 'dayandı.', 'ikinci', 'musun?', 'gönder.'}
RED = {'bitti.', 'ödüyorsun.'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False

a1, b1 = U.seg(0); a6, b6 = U.seg(1); a9, _ = U.seg(2)
tP = T('Peki', 13); tAv = T('Avustralya', 20); tAma = T('Ama', 28.5); tK = T('Karar', 47.5)


def scenes(A):
    return [('s1', 0, b1), ('s2', b1, tP - .1), ('s3', tP - .1, tAv - .1), ('s4', tAv - .1, tAma - .05), ('s5', tAma - .05, a6),
            ('s6', a6, b6), ('s7', b6, tK - .1), ('s8', tK - .1, a9), ('s9', a9, DUR)]


AV = {'s1': HERO, 's2': None, 's3': None, 's4': None, 's5': None, 's6': HERO, 's7': None, 's8': None, 's9': HERO}

SC = 10  # px / dakika


def hbar(i, y, lab, mins, col, cls=''):
    return (f'<div class="lab" style="position:absolute;left:150px;top:{y - 44}px">{lab}</div>'
            f'<div class="bar" id="hb{i}" style="left:150px;top:{y}px;height:96px;width:{mins * SC}px;background:{col}"></div>'
            f'<div class="a num" id="hv{i}" style="left:{170 + mins * SC}px;top:{y + 10}px;font-size:66px;opacity:0;{cls}">{mins} DK</div>')


EXTRA_CSS = '<style>' + FRAME_CSS + r'''
.bar{position:absolute;border-radius:0 14px 14px 0;transform-origin:0 50%}
.chip{position:absolute;padding:14px 26px;border-radius:14px;font:800 38px 'Inter Tight';white-space:nowrap}
.chip.g{border:1.5px solid rgba(255,255,255,.45);background:rgba(255,255,255,.04);color:#fff}
.rk{position:absolute;left:190px;width:700px;height:110px;border-radius:18px;display:flex;align-items:center;gap:30px;padding:0 34px;box-sizing:border-box;font:800 54px 'Inter Tight'}
.rk.dim{border:1.5px solid rgba(255,255,255,.3);color:rgba(255,255,255,.75)}
.rk.hi{border:3px solid #e8b931;color:#e8b931;box-shadow:0 0 26px rgba(232,185,49,.35)}
.dc{position:absolute;left:90px;width:900px;border-radius:18px;padding:20px 28px;box-sizing:border-box;border:1.5px solid rgba(255,255,255,.4);background:rgba(255,255,255,.03)}
.dc .q{font:700 32px 'Inter Tight';color:rgba(255,255,255,.7);letter-spacing:.04em}
.dc .r{font:800 46px 'Inter Tight';margin-top:6px}
</style>'''

SCENE_HTML = r'''
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">''' + title('t1', 'Kutuda 60 Dakika', 'Testte <i>12–14</i>') + r'''</section>
  <section id="s2" class="scene clip">
    ''' + title('t2', 'V15 Detect', 'Türkiye <i>Fiyatı</i>') + r'''
    <div class="gbox" id="b2" style="left:170px;top:470px;width:740px;height:420px">
      <div class="lab" style="margin-bottom:20px">EKİM SONU · EN UCUZ SATICI</div>
      <div class="num glowt" style="font-size:150px">~<span id="n2">0</span></div><div class="num" style="font-size:64px">TL</div></div>
  </section>
  <section id="s3" class="scene clip">
    ''' + title('t3', '60 Dakika', 'Nereden <i>Geliyor?</i>') + r'''
    <div class="chip g" id="c31" style="left:190px;top:480px;opacity:0">EN DÜŞÜK GÜÇ</div>
    <div class="chip g" id="c32" style="left:190px;top:600px;opacity:0">+ MOTORSUZ BAŞLIK</div>
    <div class="rbox" id="r3" style="left:190px;top:740px;width:700px;height:140px;border-radius:20px;font-size:60px;opacity:0">= KUTUDAKİ SÜRE</div>
  </section>
  <section id="s4" class="scene clip">
    ''' + title('t4', 'Bağımsız', '<i>Test</i>') + r'''
    <div class="chip g" id="c4" style="left:150px;top:440px;opacity:0;font-size:32px">CHOICE · AVUSTRALYA TÜKETİCİ KURULUŞU</div>
    ''' + hbar(0, 640, 'KUTUDAKİ İDDİA (V15)', 60, 'linear-gradient(90deg,rgba(255,255,255,.85),rgba(255,255,255,.25))') + hbar(1, 820, 'GEN5DETECT · TEST', 12, 'linear-gradient(90deg,#ff3b30,rgba(255,59,48,.4))', 'color:#ff3b30') + hbar(2, 1000, 'V11 · TEST', 14, 'linear-gradient(90deg,#ff3b30,rgba(255,59,48,.4))', 'color:#ff3b30') + r'''
  </section>
  <section id="s5" class="scene clip">
    ''' + title('t5', 'Ama Yine de', 'En İyi <i>2. Marka</i>') + r'''
    <div class="lab" style="position:absolute;left:0;right:0;top:450px;text-align:center">CHOICE · 2025 SÜPÜRGE MARKALARI</div>
    <div class="rk dim" id="k1" style="top:520px;opacity:0"><span>1</span><span>LG</span></div>
    <div class="rk hi" id="k2" style="top:660px;opacity:0"><span>2</span><span>DYSON</span></div>
    <div class="chip g" id="c5" style="left:190px;top:830px;opacity:0">MAKİNE KÖTÜ DEĞİL</div>
  </section>
  <section id="s6" class="scene clip">''' + title('t6', 'Farkın', '<i>Karşılığı?</i>') + r'''</section>
  <section id="s7" class="scene clip">
    ''' + title('t7', 'Yedek', '<i>Batarya</i>') + r'''
    <div class="gbox" id="b7" style="left:190px;top:470px;width:700px;height:300px">
      <div class="lab" style="margin-bottom:16px">DYSON TR · V15 / V11 BATARYA</div><div class="num glowt" style="font-size:120px">5.400 TL</div></div>
    <div class="dc" id="d7" style="top:830px;opacity:0"><div class="q">CHOICE UZMANI</div><div class="r">Rakip yedek bataryayı <span class="gold">kutuya koyuyor</span></div></div>
  </section>
  <section id="s8" class="scene clip">
    ''' + title('t8', 'Karar', '<i>Kuralı</i>') + r'''
    <div class="dc" id="d81" style="top:440px;opacity:0"><div class="q">HALI + GÜÇLÜ MOD</div><div class="r">→ 2. bataryayı <span class="gold">bütçeye yaz</span></div></div>
    <div class="dc" id="d82" style="top:640px;opacity:0"><div class="q">PARKE + ÖZELLİKLER ÖNEMLİ</div><div class="r">→ Dyson <span class="gold">iyi makine</span></div></div>
    <div class="dc" id="d83" style="top:840px;opacity:0;border-color:rgba(255,59,48,.7)"><div class="q">SADECE TEMİZ EV</div><div class="r">→ Farkı <span style="color:#ff3b30">özelliklere ödüyorsun</span></div></div>
  </section>
  <section id="s9" class="scene clip">''' + title('t9', 'İndirim Kollayana', '<i>Gönder</i>') + r'''</section>
'''

_bars = ''.join(f"tl.fromTo('#hb{i}',{{scaleX:0}},{{scaleX:1,duration:.7,ease:'power3.out'}},{t}); pop('#hv{i}',{t + .4});"
                for i, t in enumerate([tAv + .2, T('Gen', 24), T('Ve', 26.3)]))
SCENE_JS = JS + U.frame_js([(0, b1), (a6, b6), (a9, DUR)]) + f'''
tl.set('#t1',{{opacity:1}},0);
ttl('#t2',{b1 + .1}); pop('#b2',{b1 + .3}); {{const o={{v:0}};tl.to(o,{{v:36000,duration:1.1,ease:'power2.out',onUpdate:()=>{{$('#n2').textContent=(Math.round(o.v/100)*100).toLocaleString('tr-TR');}}}},{T('otuz', 11)});}}
ttl('#t3',{tP}); pop('#c31',{T('Uzun', 15)}); pop('#c32',{T('düşük', 17)}); pop('#r3',{T('motorsuz', 18)});
ttl('#t4',{tAv}); pop('#c4',{T('Çoys', 22)}); {_bars}
ttl('#t5',{tAma}); pop('#k1',{T('kuruluş', 29.5)}); pop('#k2',{T('Dai', 29.5)}); pop('#c5',{T('markası', 32)});
ttl('#t6',{a6 + .1});
ttl('#t7',{b6 + .1}); pop('#b7',{T('beş', 40)}); pop('#d7',{T('Çoys', 42)});
ttl('#t8',{tK}); pop('#d81',{T('halılıysa', 49)}); pop('#d82',{T('parkeyse', 55)}); pop('#d83',{T('Sadece', 60.5)});
ttl('#t9',{a9 + .1});
'''


def SFX(A):
    return [[b1 + .05, 'f:p_whoosh', -13, 0, 'fiyat'], [T('otuz', 11) - .1, 'f:p_klik', -11, 0, '36bin'], [tP - .1, 'f:p_whoosh', -13, 0, 'nereden'],
            [T('motorsuz', 18) - .1, 'f:p_whoosh_bas', -11, 1, 'kutudaki'], [tAv - .1, 'f:p_whoosh', -13, 0, 'test'], [T('Gen', 24) + .3, 'f:p_boom', -10, 1, '12'],
            [T('Ve', 26.3) + .3, 'f:p_klik', -11, 0, '14'], [tAma - .05, 'f:p_whoosh', -13, 0, 'ikinci'], [T('Dai', 29.5) - .1, 'f:p_klik', -11, 0, 'dyson2'],
            [a6, 'f:p_boom', -10, 1, 'fark'], [b6 + .05, 'f:p_whoosh', -13, 0, 'batarya'], [T('beş', 40) - .1, 'f:p_klik', -11, 0, '5400'],
            [tK - .1, 'f:p_whoosh_bas', -11, 1, 'karar'], [T('Sadece', 60.5) - .1, 'f:p_klik', -11, 0, 'sadece'], [a9, 'f:p_whoosh', -13, 0, 'cta']]


def RISERS(A): return []
