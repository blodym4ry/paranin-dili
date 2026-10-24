import os
from panel_kit import JS, HERO, title, SVG_DEFS
from spec_util import load, FRAME_CSS
# PARANIN DİLİ — "Ocak takvimi" (zam ayı fiyatlar) · PANEL + altın çerçeveli avatar. Look: lacivert balıkçı yaka. Kaynaklar: kaynaklar.md
U = load(); T = U.T; W = U.W; DUR = U.DUR
SRT = os.path.join(W, 'avatar_cut.srt')
N = lambda *w: list(w)
REPL = [(N('iki', 'buçuk', 'katı'), '2,5 katı'), (N('yüzde', 'dört', 'virgül', 'sekizi'), "%4,8'i"), (N('yüzde', 'on', 'sekiz', 'virgül', 'doksan', 'beş'), '%18,95'),
        (N('yüzde', 'beşi,'), "%5'i,"), (N('yüzde', 'yediyi'), "%7'yi"), (N('yüzde', 'yirmi', 'yedi'), '%27'), (N('yüzde', 'beş', 'virgül', 'seksen', 'altı!'), '%5,86!'),
        (N('dört', 'yılın'), '4 yılın'), (N('üç', 'kalem…'), '3 kalem…')]
EM = {'zammın.', 'takvimi', 'gönder;', 'aralık\'ta', 'ocak?'}
RED = {'zammın.', 'itti.'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False

a1, b1 = U.seg(0); a5, b5 = U.seg(1); a8, _ = U.seg(2)
tP = T('Peki', 15); tI = T('İkincisi', 23); tU = T('Üçüncüsü', 35)


def scenes(A):
    return [('s1', 0, b1), ('s2', b1, tP - .1), ('s3', tP - .1, tI - .1), ('s4', tI - .1, tU - .1), ('s5', tU - .1, a5),
            ('s6', a5, b5), ('s7', b5, a8), ('s8', a8, DUR)]


AV = {'s1': HERO, 's2': None, 's3': None, 's4': None, 's5': None, 's6': HERO, 's7': None, 's8': HERO}

YRS = [('2023', 6.65), ('2024', 6.70), ('2025', 5.03), ('2026', 4.84)]
BARS = ''.join(f'''<div class="bar" id="y{i}" style="left:{170 + i * 200}px;top:{1000 - v * 70}px;height:{v * 70}px;width:140px;background:linear-gradient(0deg,rgba(255,59,48,.25),#ff3b30)"></div>
<div class="a num" id="yv{i}" style="left:{150 + i * 200}px;top:{930 - v * 70}px;width:180px;text-align:center;font-size:48px;opacity:0">%{str(v).replace('.', ',')}</div>
<div class="lab" style="position:absolute;left:{170 + i * 200}px;top:1020px;width:140px;text-align:center">OCAK {y}</div>''' for i, (y, v) in enumerate(YRS))

EXTRA_CSS = '<style>' + FRAME_CSS + r'''
.bar{position:absolute;border-radius:12px 12px 0 0;transform-origin:50% 100%;box-shadow:0 0 30px rgba(255,59,48,.3)}
.chip{position:absolute;padding:14px 26px;border-radius:14px;font:800 40px 'Inter Tight';white-space:nowrap}
.chip.g{border:1.5px solid rgba(255,255,255,.45);background:rgba(255,255,255,.04);color:#fff}
.cal{position:absolute;left:290px;top:430px;width:500px;height:440px;border-radius:26px;border:2px solid rgba(255,255,255,.5);background:rgba(255,255,255,.03);overflow:hidden}
.cal .hd{height:110px;background:linear-gradient(90deg,#7a0a0a,#b01212);font:800 64px/110px 'Inter Tight';text-align:center;letter-spacing:.06em}
.cal .it{font:800 50px 'Inter Tight';text-align:center;margin-top:26px}
.arr{font:800 60px 'Inter Tight';color:#e8b931;text-align:center}
</style>'''

SCENE_HTML = r'''
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">''' + title('t1', 'Ocak\'ta Fiyatlar', '<i>2,5 Kat</i> Arttı') + r'''</section>
  <section id="s2" class="scene clip">
    ''' + title('t2', 'Son 4 Yılın', 'Her <i>Ocak\'ı</i>') + r'''
    <div style="position:absolute;left:150px;top:664px;width:790px;border-top:3px dashed #e8b931" id="ln"></div>
    <div class="lab gold" id="lnl" style="position:absolute;left:40px;top:644px;opacity:0">%4,8</div>
    ''' + BARS + r'''
    <div class="chip g" id="c2" style="left:200px;top:1090px;opacity:0">3 KALEM · 3. <span style="color:#ff3b30">SENİN ZAMMIN</span></div>
  </section>
  <section id="s3" class="scene clip">
    ''' + title('t3', '1 · Devletin', '<i>Tarifesi</i>') + r'''
    <div class="gbox" id="b3" style="left:190px;top:470px;width:700px;height:460px">
      <div class="lab" style="margin-bottom:20px">HARÇLAR · ARAÇ VERGİSİ · 1 OCAK 2026</div>
      <div class="num glowt" style="font-size:150px">+%<span id="n3">0</span></div></div>
  </section>
  <section id="s4" class="scene clip">
    ''' + title('t4', '2 · Geriye Bakan', '<i>Fiyatlar</i>') + r'''
    <div class="chip g" id="c4" style="left:100px;top:450px;opacity:0;font-size:32px">KİRA · EĞİTİM · SAĞLIK ← GEÇEN YILIN ENFLASYONU</div>
    <div class="lab" style="position:absolute;left:150px;top:620px">KİRA · OCAK 2026</div>
    <div class="bar" id="h1" style="left:150px;top:660px;height:110px;width:526px;border-radius:0 14px 14px 0;transform-origin:0 50%;background:linear-gradient(90deg,#ff3b30,rgba(255,59,48,.3))"></div>
    <div class="a num" id="hv1" style="left:440px;top:668px;font-size:84px;opacity:0">%5,26</div>
    <div class="lab" style="position:absolute;left:150px;top:820px">HİZMETLER · OCAK 2026</div>
    <div class="bar" id="h2" style="left:150px;top:860px;height:110px;width:739px;border-radius:0 14px 14px 0;transform-origin:0 50%;background:linear-gradient(90deg,#ff3b30,rgba(255,59,48,.3))"></div>
    <div class="a num" id="hv2" style="left:650px;top:868px;font-size:84px;opacity:0">%7,39</div>
  </section>
  <section id="s5" class="scene clip">
    ''' + title('t5', '3 · Senin', '<i>Zammın</i>') + r'''
    <div class="gbox" id="b51" style="left:240px;top:440px;width:600px;height:180px"><div class="lab">ASGARİ ÜCRET</div><div class="num" style="font-size:90px">+%27</div></div>
    <div class="arr" id="ar1" style="position:absolute;left:0;right:0;top:640px;opacity:0">↓ İŞÇİLİK MALİYETİ</div>
    <div class="gbox" id="b52" style="left:240px;top:740px;width:600px;height:150px;opacity:0"><div class="num" style="font-size:60px">HİZMET FİYATLARI ↑</div></div>
    <div class="rbox" id="b53" style="left:240px;top:930px;width:600px;height:150px;border-radius:22px;opacity:0;font-size:56px">LOKANTA · OTEL %5,86</div>
  </section>
  <section id="s6" class="scene clip">''' + title('t6', 'Ocak', '<i>Takvimi</i>') + r'''</section>
  <section id="s7" class="scene clip">
    ''' + title('t7', 'Ocak\'ı', '<i>Ucuz</i> Atlat') + r'''
    <div class="cal" id="cal"><div class="hd">OCAK</div><div class="it" id="i1" style="opacity:0">MAAŞ</div><div class="it" id="i2" style="opacity:0">VERGİ</div><div class="it" id="i3" style="opacity:0">FİYAT</div></div>
    <div class="chip g" id="c71" style="left:110px;top:920px;opacity:0">PASAPORT / EHLİYET → <span class="gold">ARALIK'TA BİTİR</span></div>
    <div class="chip g" id="c72" style="left:110px;top:1030px;opacity:0">KİRA OCAK'TA → <span class="gold">BÜTÇEYE ŞİMDİ YAZ</span></div>
  </section>
  <section id="s8" class="scene clip">''' + title('t8', 'Zammı Gelmeden', '<i>Fiyatı</i> Gelecek') + r'''</section>
'''

_bars = ''.join(f"tl.fromTo('#y{i}',{{scaleY:0}},{{scaleY:1,duration:.6,ease:'power3.out'}},{b1 + .4 + i * .35}); pop('#yv{i}',{b1 + .7 + i * .35});" for i in range(4))
SCENE_JS = JS + U.frame_js([(0, b1), (a5, b5), (a8, DUR)]) + f'''
tl.set('#t1',{{opacity:1}},0);
ttl('#t2',{b1 + .1}); {_bars} fin('#lnl',{T('yüzde', 7)}); pop('#c2',{T('Sebebi', 9)});
ttl('#t3',{tP}); pop('#b3',{T('Harçlar', 17)}); {{const o={{v:0}};tl.to(o,{{v:18.95,duration:1.1,ease:'power2.out',onUpdate:()=>{{$('#n3').textContent=o.v.toFixed(2).replace('.',',');}}}},{T('yüzde', 20)});}}
ttl('#t4',{tI}); pop('#c4',{T('Kira', 25)});
tl.fromTo('#h1',{{scaleX:0}},{{scaleX:1,duration:.7,ease:'power3.out'}},{T('kira', 31)}); pop('#hv1',{T('beşi', 31)});
tl.fromTo('#h2',{{scaleX:0}},{{scaleX:1,duration:.7,ease:'power3.out'}},{T('hizmetler', 31)}); pop('#hv2',{T('yediyi', 31)});
ttl('#t5',{tU}); pop('#b51',{T('asgari', 36)}); fin('#ar1',{T('işçilik', 40)}); pop('#b52',{T('hizmet', 40)}); pop('#b53',{T('Lokanta', 42)});
ttl('#t6',{a5 + .1});
ttl('#t7',{b5 + .1}); pop('#cal',{b5 + .3}); fin('#i1',{T('Maaş', 50)}); fin('#i2',{T('vergi', 50)}); fin('#i3',{T('fiyat', 50)});
pop('#c71',{T('Pasaport', 52)}); pop('#c72',{T('Kira', 57)});
ttl('#t8',{a8 + .1});
'''


def SFX(A):
    return [[b1 + .05, 'f:p_whoosh', -13, 0, 'grafik'], [b1 + 1.4, 'f:p_klik', -12, 0, 'bar'], [T('Sebebi', 9) - .1, 'f:p_klik', -12, 0, '3 kalem'],
            [tP - .1, 'f:p_whoosh', -13, 0, 'neden'], [T('yüzde', 20) - .1, 'f:p_boom', -10, 1, '18,95'], [tI - .1, 'f:p_whoosh', -13, 0, 'geriye'],
            [T('yediyi', 31) - .1, 'f:p_klik', -11, 0, '7,39'], [tU - .1, 'f:p_whoosh_bas', -11, 1, 'zammin'], [T('Lokanta', 42) - .1, 'f:p_klik', -11, 0, 'lokanta'],
            [a5, 'f:p_boom', -9, 1, 'takvim'], [b5 + .05, 'f:p_whoosh', -13, 0, 'atlat'], [T('Pasaport', 52) - .1, 'f:p_klik', -12, 0, 'pasaport'],
            [T('Kira', 57) - .1, 'f:p_klik', -12, 0, 'kira'], [a8, 'f:p_whoosh', -13, 0, 'cta']]


def RISERS(A): return []
