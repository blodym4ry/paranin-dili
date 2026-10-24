import os
from panel_kit import JS, HERO, title, glow_path, SVG_DEFS
from spec_util import load, FRAME_CSS
# PARANIN DİLİ — "Altı ay gecikmesi" (emekli zammı formülü) · PANEL + altın çerçeveli avatar. Look: kahverengi kapüşon + gözlük.
U = load(); T = U.T; W = U.W; DUR = U.DUR
SRT = os.path.join(W, 'avatar_cut.srt')
N = lambda *w: list(w)
REPL = [(N('yüzde', 'on', 'iki', 'virgül', 'on', 'dokuz'), '%12,19'), (N('yüzde', 'yirmi', 'yedi.'), '%27.'), (N('yüzde', 'yirmi', 'yedide'), "%27'de"),
        (N('Se', 'Se', 'Ke'), 'SSK'), (N('İki', 'bin', 'yirmi', 'beşte'), "2025'te"), (N('yüzde', 'otuz', 'beş'), '%35'), (N('yüzde', 'otuz.'), '%30.'),
        (N('yüzde', 'on', 'yedi', 'virgül', 'yetmiş', 'altı'), '%17,76'), (N('yüzde', 'otuz', 'iki.'), '%32.'), (N('yirmi', 'bin', 'lira'), '20.000 TL'),
        (N('on', 'yedi', 'bin', 'lira'), '17.000 TL'), (N('altı', 'ayın'), '6 ayın'), (N('altı', 'ay'), '6 ay')]
EM = {'dönüyor!', 'faturası.', 'gecikmesi', 'gönder;', 'önde?'}
RED = {'kayıp', 'kaldı!'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False

a1, b1 = U.seg(0); a6, b6 = U.seg(1); a8, _ = U.seg(2)
tPeki = T('Peki', 20); tAma = T('Ama', 38); tFiy = T('Fiyatlar', 40)


def scenes(A):
    return [('s1', 0, b1), ('s2', b1, tPeki - .1), ('s3', tPeki - .1, tAma - .05), ('s4', tAma - .05, tFiy - .1), ('s5', tFiy - .1, a6),
            ('s6', a6, b6), ('s7', b6, a8), ('s8', a8, DUR)]


AV = {'s1': HERO, 's2': None, 's3': None, 's4': None, 's5': None, 's6': HERO, 's7': None, 's8': HERO}


def pair(i, x, yr, e, m):
    sc = 13
    return (f'<div class="lab" style="position:absolute;left:{x}px;top:1040px;width:330px;text-align:center">{yr}</div>'
            f'<div class="bar" id="e{i}" style="left:{x}px;top:{1020 - e * sc}px;width:150px;height:{e * sc}px;background:linear-gradient(0deg,rgba(232,185,49,.25),#e8b931)"></div>'
            f'<div class="a num" id="ev{i}" style="left:{x - 20}px;top:{950 - e * sc}px;width:190px;text-align:center;font-size:56px;color:#e8b931;opacity:0">%{e}</div>'
            f'<div class="bar" id="m{i}" style="left:{x + 180}px;top:{1020 - m * sc}px;width:150px;height:{m * sc}px;background:linear-gradient(0deg,rgba(255,255,255,.2),rgba(255,255,255,.85))"></div>'
            f'<div class="a num" id="mv{i}" style="left:{x + 160}px;top:{950 - m * sc}px;width:190px;text-align:center;font-size:56px;opacity:0">%{m}</div>')


PRICE = 'M140,950 L273,900 L406,860 L539,800 L672,760 L805,700 L938,650'
PENS = 'M140,950 L938,950 L938,650'

EXTRA_CSS = '<style>' + FRAME_CSS + r'''
.bar{position:absolute;border-radius:12px 12px 0 0;transform-origin:50% 100%}
.chip{position:absolute;padding:14px 26px;border-radius:14px;font:800 40px 'Inter Tight';white-space:nowrap}
.chip.g{border:1.5px solid rgba(255,255,255,.45);background:rgba(255,255,255,.04);color:#fff}
.mo{position:absolute;top:620px;width:150px;height:150px;border-radius:50%;border:4px solid #e8b931;display:flex;align-items:center;justify-content:center;font:800 40px 'Inter Tight';box-shadow:0 0 24px rgba(232,185,49,.4)}
.leg{position:absolute;font:800 34px 'Inter Tight'}
</style>'''

SCENE_HTML = r'''
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">''' + title('t1', 'Emekli %12,19', 'Asgari Ücret <i>%27</i>') + r'''</section>
  <section id="s2" class="scene clip">
    ''' + title('t2', 'Kural', 'Kanunda <i>Yazıyor</i>') + r'''
    <div class="chip g" id="c2" style="left:300px;top:440px;opacity:0">SSK · BAĞ-KUR</div>
    <div class="mo" id="mo1" style="left:220px;opacity:0">OCAK</div><div class="mo" id="mo2" style="left:710px;opacity:0">TEMMUZ</div>
    <div class="lab" id="l2" style="position:absolute;left:0;right:0;top:820px;text-align:center;opacity:0">ZAM = ÖNCEKİ 6 AYIN ENFLASYONU</div>
    <div class="rbox" id="r2" style="left:190px;top:900px;width:700px;height:110px;border-radius:16px;font-size:50px;opacity:0">OCAK ZAMMI = GEÇEN YILIN FATURASI</div>
  </section>
  <section id="s3" class="scene clip">
    ''' + title('t3', 'Yıl Sonunda', 'Kim <i>Önde?</i>') + r'''
    <div class="leg" style="left:200px;top:440px"><span class="gold">■</span> EMEKLİ (2 ZAM)</div><div class="leg" style="left:620px;top:440px">■ ASGARİ ÜCRET</div>
    ''' + pair(0, 160, '2025', 35, 30) + pair(1, 590, '2026', 32, 27) + r'''
    <div style="position:absolute;left:130px;top:1020px;width:820px;height:3px;background:rgba(255,255,255,.4)"></div>
  </section>
  <section id="s4" class="scene clip">
    <div class="a" id="dk" style="left:60px;right:60px;top:620px;text-align:center;opacity:0">
      <div style="font:800 92px/1.02 'Inter Tight';letter-spacing:-.03em">Ama asıl kayıp</div>
      <div style="font:italic 400 116px 'DM Serif Display';color:#ff3b30;text-shadow:0 0 30px rgba(255,59,48,.5)">başka yerde…</div></div>
  </section>
  <section id="s5" class="scene clip">
    ''' + title('t5', 'Fiyat Her Ay', 'Maaş <i>6 Ay</i> Sonra') + r'''
    <svg class="gl" style="left:0;top:0" width="1080" height="1200">''' + glow_path('pr', PRICE, '#ff3b30', 7) + glow_path('pn', PENS, '#e8b931', 6) + r'''</svg>
    <div class="leg" style="left:150px;top:470px;color:#ff3b30">— FİYATLAR</div><div class="leg gold" style="left:150px;top:520px">— EMEKLİ AYLIĞI</div>
    <div class="lab" style="position:absolute;left:130px;top:980px">OCAK</div><div class="lab" style="position:absolute;left:880px;top:980px">HAZİRAN</div>
    <div class="chip g" id="c5" style="left:150px;top:1050px;opacity:0">20.000 TL → HAZİRAN'DA <span style="color:#ff3b30">~17.000 TL</span> ALIM GÜCÜ</div>
  </section>
  <section id="s6" class="scene clip">''' + title('t6', '6 Ay', '<i>Gecikmesi</i>') + r'''</section>
  <section id="s7" class="scene clip">
    ''' + title('t7', 'Telafi Eder', 'Öne <i>Geçmez</i>') + r'''
    <div class="gbox" id="b7" style="left:170px;top:480px;width:740px;height:360px">
      <div class="lab" style="margin-bottom:24px">OCAK BÜTÇENİ</div><div class="num" style="font-size:72px">HAZİRAN</div><div class="num gold" style="font-size:72px">FİYATLARINA GÖRE</div><div class="lab" style="margin-top:20px">YAP</div></div>
  </section>
  <section id="s8" class="scene clip">''' + title('t8', 'Ocak\'taki Rakam', 'Hikâyenin <i>Yarısı</i>') + r'''</section>
'''

SCENE_JS = JS + U.frame_js([(0, b1), (a6, b6), (a8, DUR)]) + f'''
tl.set('#t1',{{opacity:1}},0);
ttl('#t2',{b1 + .1}); pop('#c2',{T('Çünkü', 9)}); pop('#mo1',{T('Ocak', 13)}); pop('#mo2',{T('Temmuz', 13)}); fin('#l2',{T('önceki', 13)}); pop('#r2',{T('Yani', 17)});
ttl('#t3',{tPeki});
tl.fromTo('#e0',{{scaleY:0}},{{scaleY:1,duration:.6,ease:'power3.out'}},{T('emekli', 22)}); pop('#ev0',{T('yüzde', 23)});
tl.fromTo('#m0',{{scaleY:0}},{{scaleY:1,duration:.6,ease:'power3.out'}},{T('Asgari', 26)}); pop('#mv0',{T('otuz', 27)});
tl.fromTo('#e1',{{scaleY:0}},{{scaleY:1,duration:.6,ease:'power3.out'}},{T('Toplam', 30)}); pop('#ev1',{T('Toplam', 30) + .5});
tl.fromTo('#m1',{{scaleY:0}},{{scaleY:1,duration:.6,ease:'power3.out'}},{T('Asgari', 33)}); pop('#mv1',{T('yedide', 33)});
tl.to('.bg',{{opacity:.25,duration:.3}},{tAma - .05}); fin('#dk',{tAma + .05},{{y:20,d:.4}}); tl.to('#dk',{{opacity:0,duration:.2}},{tFiy - .3}); tl.to('.bg',{{opacity:1,duration:.4}},{tFiy - .1});
ttl('#t5',{tFiy}); dr('#pr, #pr_g',{tFiy + .3},1.8); dr('#pn, #pn_g',{T('aylık', 40)},1.4); pop('#c5',{T('Ocak', 43)});
ttl('#t6',{a6 + .1});
ttl('#t7',{b6 + .1}); pop('#b7',{T('Ocak', 54)});
ttl('#t8',{a8 + .1});
'''


def SFX(A):
    return [[b1 + .05, 'f:p_whoosh', -13, 0, 'kural'], [T('Ocak', 13) - .1, 'f:p_klik', -12, 0, 'ocak'], [T('Temmuz', 13) - .1, 'f:p_klik', -12, 0, 'temmuz'],
            [T('Yani', 17) - .1, 'f:p_whoosh_bas', -11, 1, 'fatura'], [tPeki - .1, 'f:p_whoosh', -13, 0, 'kim'], [T('emekli', 22), 'f:p_klik', -12, 0, '35'],
            [T('Toplam', 30), 'f:p_klik', -12, 0, '32'], [T('yedide', 33) - .1, 'f:p_boom', -10, 1, 'kaldi'], [tAma - .05, 'f:p_boom', -9, 1, 'desen'],
            [tFiy, 'f:p_whoosh', -13, 0, 'grafik'], [T('Ocak', 43) - .1, 'f:p_whoosh_bas', -11, 1, '17bin'], [a6, 'f:p_boom', -10, 1, 'gecikme'],
            [b6 + .05, 'f:p_whoosh', -13, 0, 'telafi'], [a8, 'f:p_whoosh', -13, 0, 'cta']]


def RISERS(A): return []
