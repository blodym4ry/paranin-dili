import os
from panel_kit import JS, HERO, title, SVG_DEFS
from spec_util import load, FRAME_CSS
# PARASINA DEĞER Mİ? — "Monster vs MacBook: girişimciye hangisi?" · PANEL + altın çerçeveli avatar. Look: podcast/mikrofon. Kaynaklar: kaynaklar.md
U = load(); T = U.T; W = U.W; DUR = U.DUR
SRT = os.path.join(W, 'avatar_cut.srt')
N = lambda *w: list(w)
REPL = [(N("Monstır'ın"), "Monster'ın"), (N('Monstır'), 'Monster'), (N('Mekbuk', "Eyır'dan"), "MacBook Air'den"), (N('Mekbuk', 'Eyır', 'Em', 'beş'), 'MacBook Air M5'),
        (N("Eyır'ın"), "Air'in"), (N('Eyır'), 'Air'), (N('Mekbuk', 'Neo'), 'MacBook Neo'), (N("Epıl'ın"), "Apple'ın"), (N("Epıl'a"), "Apple'a"),
        (N('Vindovs'), 'Windows'), (N("Vindovs'ta"), "Windows'ta"), (N('Kor', 'Ultra', 'yedi'), 'Core Ultra 7'), (N('Huma', 'He', "dört'ü"), "Huma H4'ü"), (N('Huma', 'He', 'dört'), 'Huma H4'),
        (N('on', 'dört', 'inçlik'), '14 inçlik'), (N('on', 'dört', 'inç'), '14 inç'), (N('beş', 'bin', 'lira'), '5.000 TL'),
        (N('seksen', 'dört', 'bin', 'dokuz', 'yüz', 'doksan', 'dokuz', 'lira'), '84.999 TL'), (N('seksen', 'dokuz', 'bin', 'dokuz', 'yüz', 'doksan', 'dokuz', 'lira'), '89.999 TL'),
        (N('dört', 'yıl'), '4 yıl'), (N('on', 'sekiz', 'saate'), '18 saate'), (N('yüz', 'yetmiş', 'gram'), '170 gram'), (N('yüzde', 'yirmi', 'beş'), '%25'),
        (N('kırk', 'altı', 'bin', 'liralık'), '46.000 TL\'lik')]
EM = {'pahalı.', 'hangisi?', 'ne?', 'değil.', 'arttı.', 'gönder.'}
RED = {'pahalı.', 'değil.'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False

a1, b1 = U.seg(0); a4, b4 = U.seg(1); a9, _ = U.seg(2)
tM = T('Monstır', 17.4); tE = T('Eyır', 37); tB = T('Bir', 42); tK = T('Karar', 47.8)


def scenes(A):
    return [('s1', 0, b1), ('s2', b1, tM - .1), ('s3', tM - .1, a4), ('s4', a4, b4), ('s5', b4, tE - .1), ('s6', tE - .1, tB - .1),
            ('s7', tB - .1, tK - .1), ('s8', tK - .1, a9), ('s9', a9, DUR)]


AV = {'s1': HERO, 's2': None, 's3': None, 's4': HERO, 's5': None, 's6': None, 's7': None, 's8': None, 's9': HERO}

EXTRA_CSS = '<style>' + FRAME_CSS + r'''
.bar{position:absolute;border-radius:0 14px 14px 0;transform-origin:0 50%}
.chip{position:absolute;padding:14px 26px;border-radius:14px;font:800 38px 'Inter Tight';white-space:nowrap}
.chip.g{border:1.5px solid rgba(255,255,255,.45);background:rgba(255,255,255,.04);color:#fff}
.dc{position:absolute;left:90px;width:900px;border-radius:18px;padding:20px 28px;box-sizing:border-box;border:1.5px solid rgba(255,255,255,.4);background:rgba(255,255,255,.03)}
.dc .q{font:700 32px 'Inter Tight';color:rgba(255,255,255,.7);letter-spacing:.04em}
.dc .r{font:800 46px 'Inter Tight';margin-top:6px}
.pc{position:absolute;left:150px;width:780px;height:300px;border-radius:24px;border:2px solid rgba(255,255,255,.45);background:rgba(255,255,255,.03);text-align:center;padding-top:34px;box-sizing:border-box}
.pc .lab{margin-bottom:14px}
.pc .num{font-size:120px}
</style>'''

SCENE_HTML = r'''
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">''' + title('t1', 'Monster vs MacBook', '<i>Girişimciye</i> Hangisi?') + r'''</section>
  <section id="s2" class="scene clip">
    ''' + title('t2', 'Resmi Site', '<i>Fiyatları</i>') + r'''
    <div class="pc" id="p2" style="top:470px;opacity:0"><div class="lab">APPLE · AIR M5 · 16 GB / 512 GB</div><div class="num glowt">84.999 TL</div></div>
    <div class="lab" id="l2" style="position:absolute;left:0;right:0;top:800px;text-align:center;opacity:0">EKİM SONU</div>
  </section>
  <section id="s3" class="scene clip">
    ''' + title('t3', 'Resmi Site', '<i>Fiyatları</i>') + r'''
    <div class="pc" style="top:470px;height:220px;padding-top:24px;opacity:.55"><div class="lab">MACBOOK AIR M5 · 16 / 512</div><div class="num" style="font-size:90px">84.999 TL</div></div>
    <div class="pc" id="p3" style="top:730px;height:260px;padding-top:24px;opacity:0;border-color:#e8b931"><div class="lab">HUMA H4 · 16 / 500 · WINDOWS</div><div class="num gold" style="font-size:110px">89.999 TL</div></div>
    <div class="rbox" id="r3" style="left:330px;top:1030px;width:420px;height:110px;border-radius:18px;font-size:58px;opacity:0">+5.000 TL</div>
  </section>
  <section id="s4" class="scene clip">''' + title('t4', 'Monster\'ın', '<i>Artısı?</i>') + r'''</section>
  <section id="s5" class="scene clip">
    ''' + title('t5', 'Monster', '<i>Artıları</i>') + r'''
    <div class="dc" id="d51" style="top:450px;opacity:0"><div class="q">EKRAN</div><div class="r">14" <span class="gold">QHD</span></div></div>
    <div class="dc" id="d52" style="top:630px;opacity:0"><div class="q">GARANTİ (90 GÜNDE KAYIT ŞARTI)</div><div class="r"><span class="gold">4 yıl</span> + ömür boyu bakım</div></div>
    <div class="dc" id="d53" style="top:810px;opacity:0;border-color:rgba(255,59,48,.7)"><div class="q">AMA</div><div class="r">Batarya <span style="color:#ff3b30">uzatılmış garantide yok</span></div></div>
  </section>
  <section id="s6" class="scene clip">
    ''' + title('t6', 'Air', '<i>Artıları</i>') + r'''
    <div class="dc" id="d61" style="top:450px;opacity:0"><div class="q">PİL (APPLE'A GÖRE)</div><div class="r"><span class="gold">18 saate kadar</span> video</div></div>
    <div class="dc" id="d62" style="top:630px;opacity:0"><div class="q">AĞIRLIK</div><div class="r">1,23 kg vs 1,40 kg → <span class="gold">170 g hafif</span></div></div>
  </section>
  <section id="s7" class="scene clip">
    ''' + title('t7', 'Bu Air\'in', 'Fiyatı <i>%25</i> Arttı') + r'''
    <div class="lab" style="position:absolute;left:150px;top:500px">MART 2026</div>
    <div class="bar" id="h1" style="left:150px;top:540px;height:110px;width:540px;background:linear-gradient(90deg,rgba(255,255,255,.85),rgba(255,255,255,.25))"></div>
    <div class="a num" id="hv1" style="left:170px;top:552px;font-size:64px;color:#111;opacity:0">67.999 TL</div>
    <div class="lab" style="position:absolute;left:150px;top:710px">EKİM 2026</div>
    <div class="bar" id="h2" style="left:150px;top:750px;height:110px;width:675px;background:linear-gradient(90deg,#ff3b30,rgba(255,59,48,.4))"></div>
    <div class="a num" id="hv2" style="left:170px;top:762px;font-size:64px;opacity:0">84.999 TL</div>
  </section>
  <section id="s8" class="scene clip">
    ''' + title('t8', 'Karar', '<i>Kuralı</i>') + r'''
    <div class="dc" id="d81" style="top:440px;opacity:0"><div class="q">PROGRAMIN SADECE WINDOWS'TA MI?</div><div class="r">→ <span class="gold">Monster</span></div></div>
    <div class="dc" id="d82" style="top:640px;opacity:0"><div class="q">GÜN BOYU PRİZDEN UZAK MISIN?</div><div class="r">→ <span class="gold">Air</span></div></div>
    <div class="dc" id="d83" style="top:840px;opacity:0"><div class="q">TARAYICI + OFİS</div><div class="r">→ İkisi de fazla: <span class="gold">MacBook Neo 45.999 TL</span></div></div>
  </section>
  <section id="s9" class="scene clip">''' + title('t9', 'Bilgisayar Alacak', 'Arkadaşına <i>Gönder</i>') + r'''</section>
'''

SCENE_JS = JS + U.frame_js([(0, b1), (a4, b4), (a9, DUR)]) + f'''
tl.set('#t1',{{opacity:1}},0);
ttl('#t2',{b1 + .1}); pop('#p2',{b1 + .3}); fin('#l2',{T('Ekim', 11)});
ttl('#t3',{tM}); pop('#p3',{tM + .2}); pop('#r3',{T('seksen', 22.3)});
ttl('#t4',{a4 + .1});
ttl('#t5',{b4 + .1}); pop('#d51',{T('Daha', 27.4)}); pop('#d52',{T('kayıt', 29.2)}); pop('#d53',{T('Ama', 33.2)});
ttl('#t6',{tE}); pop('#d61',{T('Epıl', 37.9)}); pop('#d62',{T('yüz', 40.4)});
ttl('#t7',{tB}); tl.fromTo('#h1',{{scaleX:0}},{{scaleX:1,duration:.6,ease:'power3.out'}},{tB + .3}); pop('#hv1',{tB + .7});
tl.fromTo('#h2',{{scaleX:0}},{{scaleX:1,duration:.7,ease:'power3.out'}},{T('Mart', 45)}); pop('#hv2',{T('Mart', 45) + .5});
ttl('#t8',{tK}); pop('#d81',{T('İşini', 48.8)}); pop('#d82',{T('Gün', 53)}); pop('#d83',{T('İşin', 55.2)});
ttl('#t9',{a9 + .1});
'''


def SFX(A):
    return [[b1 + .05, 'f:p_whoosh', -13, 0, 'air'], [tM - .1, 'f:p_whoosh', -13, 0, 'monster'], [T('seksen', 22.3) - .1, 'f:p_boom', -10, 1, '5000'],
            [a4, 'f:p_whoosh_bas', -11, 1, 'arti'], [b4 + .05, 'f:p_whoosh', -13, 0, 'm-arti'], [T('Ama', 33.2) - .1, 'f:p_klik', -11, 0, 'batarya'],
            [tE - .1, 'f:p_whoosh', -13, 0, 'air-arti'], [tB - .1, 'f:p_whoosh', -13, 0, 'fiyat'], [T('Mart', 45), 'f:p_boom', -10, 1, '25'],
            [tK - .1, 'f:p_whoosh_bas', -11, 1, 'karar'], [T('Gün', 53) - .1, 'f:p_klik', -11, 0, 'air'], [T('İşin', 55.2) - .1, 'f:p_klik', -11, 0, 'neo'],
            [a9, 'f:p_whoosh', -13, 0, 'cta']]


def RISERS(A): return []
