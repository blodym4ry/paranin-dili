# VARYASYON v3 (manset) — kaynak: videos/asgari-ucret-2027/spec.py; kanca: Asgari ücretli misin? Zammı duyunca hemen sevinme.
import os
from panel_kit import JS, HERO, PIP, title, SVG_DEFS
from spec_util import load, FRAME_CSS
from visual_kit import VIS_CSS, bg_html, bg_js, card, card_js
# ASGARİ ÜCRET 2027 — ters köşe: zam senaryoları → maaşın kaç ekmek ettiği → işveren maliyeti fiyata döner (Ata 30 Eki 13:41).
# HEP VARIM (HERO vurgu + PIP) + GERÇEK GÖRSEL (Pexels: fırın, otobüs, fabrika, çarşı).
U = load(); T = U.T; W = U.W; DUR = U.DUR
SRT = os.path.join(W, 'avatar_cut.srt')
N = lambda s: s.split()
REPL = [(N('Yüzde yirmi gelirse,'), '%20 gelirse,'), (N('otuz üç bin yedi yüz lira.'), '33.700 lira.'), (N('Yüzde yirmi beş gelirse,'), '%25 gelirse,'),
        (N('otuz beş bin yüz lira.'), '35.100 lira.'), (N('Yüzde otuz gelirse,'), '%30 gelirse,'), (N('otuz altı bin beş yüz lira.'), '36.500 lira.'),
        (N('iki bin yirmi altı.'), '2026.'), (N('yirmi sekiz bin yetmiş beş lira.'), '28.075 lira.'), (N('on lira.'), '10 lira.'),
        (N('iki bin sekiz yüz ekmek'), '2.800 ekmek'), (N('on iki buçuk lira'), '12,5 lira'), (N('iki bin iki yüz elli ekmek.'), '2.250 ekmek.'),
        (N('beş yüzden'), '500\'den'), (N('otuz beş liradan,'), '35 liradan,'), (N('kırk iki liraya'), '42 liraya'), (N('kırk bin lirayı'), '40 bin lirayı'),
        (N('Yüzde yirmi beş zamla,'), '%25 zamla,'), (N('elli bin lirayı'), '50 bin lirayı'), (N('On çalışanı'), '10 çalışanı'),
        (N('yüz bin lira'), '100 bin lira'), (N('İki bin yirmi altı zammı'), '2026 zammı'), (N('yüzde yirmi yedi'), '%27'),
        (N('İki bin yirmi beş enflasyonu'), '2025 enflasyonu'), (N('yüzde otuz virgül dokuz.'), '%30,9.'), (N('yüzde yirmi ile otuz'), '%20 ile 30'),
        (N('yüzde otuz.'), '%30.')]
EM = {'bak.', 'gitti.', 'ödüyor.', 'döner.', 'karşılamadı.', 'sayarsın.', 'say.'}
RED = {'gitti.', 'karşılamadı.'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False
FULLOPEN = 0

t2 = T('Masada') - .1; t3 = T('Hangisi', t2) - .1; t4 = T('Ocak', t3) - .1; t5 = T('Mayısta', t4) - .1; t5b = T('Maaş', T('ekmek', t5 + 3)) - .1
t6 = T('Otobüs', t5b) - .1; t7 = T('Asıl', t6) - .1; t8 = T('Bugün', t7) - .1; t9 = T('On', T('geçer', t8)) - .1; t10 = T('Yani', t9) - .1
t11 = T('Bunu', t10) - .1; t12 = T('Masada', t11) - .1; t12b = T('Yani', t12) - .1; t13 = T('O', t12b) - .1; t14 = T('Bunu,', t13) - .1
TS = [0, t2, t3, t4, t5, t5b, t6, t7, t8, t9, t10, t11, t12, t12b, t13, t14, DUR]
IDS = ['s1', 's2', 's3', 's4', 's5', 's5b', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's12b', 's13', 's14']
HEROS = ['s14']


def scenes(A):
    return [(IDS[k], TS[k], TS[k + 1]) for k in range(len(IDS))]


AV = {k: (HERO if k in HEROS else PIP) for k in IDS}
AV['s1'] = None   # VARYASYON: kanca avatarsız (Ata 30 Eki)

EXTRA_CSS = '<style>' + '\n.ttl .l2{background:#f4f1ea!important;color:#0d0c0a!important;border-left:14px solid #d81e1e}\n.ttl .l2 i{color:#b01212}\n#t1{top:520px!important;left:120px!important;right:220px!important;padding:30px 24px 36px;background:rgba(244,241,234,.97);color:#0d0c0a!important;\n  border-top:16px solid #d81e1e;border-radius:6px;box-shadow:0 30px 70px rgba(0,0,0,.7);text-shadow:none!important;font-size:60px!important}\n#t1 i{font-size:66px!important;color:#fff!important}\n#t1 .l2{background:#d81e1e!important;color:#fff!important;border-left:0}\n' + FRAME_CSS + VIS_CSS + r'''
.chip{position:absolute;padding:14px 24px;border-radius:14px;font:800 34px 'Inter Tight';white-space:nowrap}
.chip.g{border:1.5px solid rgba(255,255,255,.45);background:rgba(0,0,0,.5);color:#fff}
.row{position:absolute;left:155px;width:715px;height:92px;box-sizing:border-box;display:flex;align-items:center;justify-content:space-between;padding:0 26px;
  border-radius:16px;border:1.5px solid rgba(255,255,255,.35);background:rgba(0,0,0,.55);font:800 40px 'Inter Tight';color:#fff}
.row span.k{font:600 28px 'IBM Plex Mono';color:rgba(255,255,255,.75);letter-spacing:.06em}
.big{position:absolute;left:155px;width:715px;text-align:center;font:800 104px/1 'Inter Tight';color:#fff;text-shadow:0 0 30px rgba(0,0,0,.8)}
.big small{display:block;font:700 30px 'IBM Plex Mono';letter-spacing:.08em;color:rgba(255,255,255,.75);margin-top:10px}
.loaf{position:absolute;width:56px;height:34px;border-radius:28px 28px 10px 10px;background:linear-gradient(180deg,#e4a556,#a8622a);box-shadow:inset 0 -4px 0 rgba(0,0,0,.25)}
.per{position:absolute;width:56px;height:84px;color:rgba(255,255,255,.7)}
.per .h{position:absolute;left:16px;top:0;width:24px;height:24px;border-radius:50%;background:currentColor}
.per .b{position:absolute;left:6px;top:28px;width:44px;height:54px;border-radius:22px 22px 6px 6px;background:currentColor}
.bar{position:absolute;left:155px;height:64px;border-radius:14px;transform-origin:0 50%;display:flex;align-items:center;padding-left:22px;box-sizing:border-box;font:800 36px 'Inter Tight';color:#111}
.lab{font:600 28px 'IBM Plex Mono';color:rgba(255,255,255,.8);letter-spacing:.06em}
.gold{color:#e8b931} .redt{color:#ff3b30} .grn{color:#3ddc84}
</style>'''

BGS = [('bg1', 'istanbul.jpg', 0), ('bg2', 'piggy.jpg', 1), ('bg3', 'bazaar1.jpg', 0), ('bg4', 'bread2.jpg', 1), ('bg5', 'bread2.jpg', 1),
       ('bg5b', 'bread1.jpg', 0), ('bg6', 'istanbul.jpg', 1), ('bg7', 'factory1.jpg', 0), ('bg8', 'factory2.jpg', 1), ('bg9', 'bread1.jpg', 1),
       ('bg10', 'card2.jpg', 0), ('bg11', 'chart1.jpg', 1), ('bg12', 'bazaar2.jpg', 1), ('bg12b', 'bazaar2.jpg', 0), ('bg13', 'bread2.jpg', 0),
       ('bg14', 'bazaar1.jpg', 0)]
BGMAP = {s: b for s, b in zip(IDS, [x[0] for x in BGS])}

loaves = ''.join(f'<div class="loaf" id="lf{k}" style="left:{175 + (k % 10) * 68}px;top:{720 + (k // 10) * 52}px;opacity:0"></div>' for k in range(30))
staff = ''.join(f'<div class="per" id="q{k}" style="left:{180 + k * 68}px;top:800px;opacity:0"><div class="h"></div><div class="b"></div></div>' for k in range(10))

SCENE_HTML = bg_html(BGS) + r'''
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">''' + title('t1', 'Asgari Ücretli misin?', 'Hemen <i>Sevinme</i>') + r'''</section>
  <section id="s2" class="scene clip">
    ''' + title('t2', 'Masada', '<i>3 Senaryo</i>') + r'''
    <div class="lab" style="position:absolute;left:155px;top:450px">2026 NET · 28.075 TL</div>
    <div class="row" id="r21" style="top:500px;opacity:0"><span class="k">%20 ZAM</span>33.700 TL</div>
    <div class="row" id="r22" style="top:610px;opacity:0"><span class="k">%25 ZAM</span>35.100 TL</div>
    <div class="row" id="r23" style="top:720px;opacity:0;border-color:rgba(232,185,49,.8)"><span class="k">%30 ZAM</span><span class="gold">36.500 TL</span></div>
    <div class="chip g" id="c2" style="left:155px;top:850px;opacity:0;font-size:28px">NET AYLIK · YUVARLANMIŞ</div>
  </section>
  <section id="s3" class="scene clip">''' + title('t3', 'Sevinmeden Önce', 'Şu <i>Hesaba</i> Bak') + r'''</section>
  <section id="s4" class="scene clip">
    ''' + title('t4', 'Ocak 2026', 'Maaş = <i>Kaç Ekmek?</i>') + r'''
    ''' + card('p4', 'media/bread1.jpg', 450, 250, 'HALK EKMEK · 10 TL') + r'''
    ''' + loaves + r'''
    <div class="big" id="k4" style="top:900px;opacity:0"><span id="n4">0</span><small>EKMEK · 28.075 TL / 10 TL</small></div>
  </section>
  <section id="s5" class="scene clip">
    ''' + title('t5', 'Mayıs 2026', 'Ekmek <i>12,5 TL</i>') + r'''
    <div class="row" id="r51" style="top:450px;opacity:0"><span class="k">HALK EKMEK</span><span>10 → <span class="redt">12,5 TL</span></span></div>
    <div class="big" id="k5" style="top:600px;opacity:0"><span id="n5">2.808</span><small>EKMEK · AYNI MAAŞ</small></div>
    <div class="chip g" id="c5" style="left:155px;top:800px;opacity:0;font-size:40px;border-color:#ff3b30;color:#ff3b30">−550 EKMEK</div>
  </section>
  <section id="s5b" class="scene clip">''' + title('t5b', '500+ Ekmek', 'Cebinden <i>Gitti</i>') + r'''</section>
  <section id="s6" class="scene clip">
    ''' + title('t6', 'Otobüs', 'De <i>Öyle</i>') + r'''
    ''' + card('p6', 'media/bus.jpg', 450, 380, 'İSTANBULKART · TAM BİLET') + r'''
    <div class="row" id="r61" style="top:860px;opacity:0"><span class="k">ŞUBAT 2026</span><span>35 → <span class="redt">42 TL</span></span></div>
    <div class="chip g" id="c6" style="left:155px;top:975px;opacity:0;font-size:36px;border-color:#ff3b30;color:#ff3b30">+%20</div>
  </section>
  <section id="s7" class="scene clip">''' + title('t7', 'Asıl Ters Köşe', 'İşveren de <i>Öder</i>') + r'''</section>
  <section id="s8" class="scene clip">
    ''' + title('t8', 'İşverene', '<i>Maliyet</i>') + r'''
    ''' + card('p8', 'media/factory2.jpg', 450, 260, 'BİR ASGARİ ÜCRETLİ') + r'''
    <div class="lab" style="position:absolute;left:155px;top:740px">BUGÜN</div>
    <div class="bar" id="b81" style="top:780px;width:572px;background:rgba(255,255,255,.85);opacity:0">40.200 TL</div>
    <div class="lab" style="position:absolute;left:155px;top:870px">%25 ZAMLA · AYNI KESİNTİ</div>
    <div class="bar" id="b82" style="top:910px;width:715px;background:#e8b931;opacity:0">50.300 TL</div>
  </section>
  <section id="s9" class="scene clip">
    ''' + title('t9', '10 Çalışanlı', 'Bir <i>Fırın</i>') + r'''
    ''' + card('p9', 'media/bread2.jpg', 450, 300, 'FIRIN') + r'''
    ''' + staff + r'''
    <div class="big" id="k9" style="top:920px;opacity:0;font-size:84px"><span class="redt">+<span id="n9">0</span> TL</span><small>AYLIK EK MALİYET</small></div>
  </section>
  <section id="s10" class="scene clip">''' + title('t10', 'Zam Önce Maaşa', 'Sonra <i>Fiyata</i>') + r'''</section>
  <section id="s11" class="scene clip">
    ''' + title('t11', 'Geçen Yıl', '<i>Yaşadık</i>') + r'''
    <div class="lab" style="position:absolute;left:155px;top:470px">2026 ASGARİ ÜCRET ZAMMI</div>
    <div class="bar" id="b111" style="top:510px;width:622px;background:rgba(255,255,255,.85);opacity:0">%27</div>
    <div class="lab" style="position:absolute;left:155px;top:610px">2025 ENFLASYONU · TÜİK</div>
    <div class="bar" id="b112" style="top:650px;width:715px;background:#ff3b30;opacity:0;color:#fff">%30,9</div>
    <div class="chip g" id="c11" style="left:155px;top:770px;opacity:0;font-size:30px;border-color:#ff3b30;color:#ff3b30">ZAM ENFLASYONU KARŞILAMADI</div>
  </section>
  <section id="s12" class="scene clip">
    ''' + title('t12', '2027', '<i>Hesabı</i>') + r'''
    <div class="row" id="r121" style="top:470px;opacity:0"><span class="k">MASADAKİ ZAM</span>%20 – %30</div>
    <div class="row" id="r122" style="top:580px;opacity:0;border-color:rgba(255,59,48,.8)"><span class="k">YIL SONU ENF. BEKLENTİSİ</span><span class="redt">~%30</span></div>
    <div class="chip g" id="c12" style="left:155px;top:700px;opacity:0;font-size:28px">PİYASA KATILIMCILARI ANKETİ · EKİM</div>
  </section>
  <section id="s12b" class="scene clip">''' + title('t12b', 'En İyi İhtimalle', 'Yerinde <i>Sayarsın</i>') + r'''</section>
  <section id="s13" class="scene clip">''' + title('t13', 'Tutara Değil', '<i>Ekmeğe</i> Bak') + r'''</section>
  <section id="s14" class="scene clip">''' + title('t14', 'Zam Bekleyen', 'Arkadaşına <i>Gönder</i>') + r'''</section>
'''

hr = []
for sid, a, b in scenes(None):
    if sid in HEROS:
        a2 = FULLOPEN + .35 if sid == 's1' else a + .35
        if hr and a2 - hr[-1][1] < .6: hr[-1] = (hr[-1][0], b)
        else: hr.append((a2, b))


def cnt(sel, a, b, t, d=1.0):
    return (f"{{const o={{v:{a}}};tl.fromTo(o,{{v:{a}}},{{v:{b},duration:{d},ease:'power2.out',"
            f"onUpdate:()=>{{$('{sel}').textContent=Math.round(o.v).toLocaleString('tr-TR');}}}},{t:.2f});}}\n")


ty1 = T('Yüzde', t2); ty2 = T('Yüzde', ty1 + .5); ty3 = T('Yüzde', ty2 + .5)
tm = T('maaşın', t4)
SCENE_JS = JS + U.frame_js(hr) + bg_js(BGMAP, scenes(None)) + f'''
tl.set('#t1',{{opacity:1}},0);
ttl('#t2',{t2 + .1}); pop('#r21',{ty1}); pop('#r22',{ty2}); pop('#r23',{ty3}); pop('#c2',{ty3 + .8});
ttl('#t3',{t3 + .1});
ttl('#t4',{t4 + .1}); {''.join(f"pop('#lf{k}',{tm - .3 + k * .04:.2f},{{y:-30}});" for k in range(30))}
pop('#k4',{tm}); ''' + cnt('#n4', 0, 2808, tm, 1.1) + f'''
ttl('#t5',{t5 + .1}); pop('#r51',{T('on', t5)}); pop('#k5',{T('Aynı', t5)}); ''' + cnt('#n5', 2808, 2246, T('iki', T('artık', t5)), 1.0) + f'''
{''.join(f"tl.to('#lf{k}',{{opacity:0,duration:.2}},{T('Aynı', t5) - .1 + k * .02:.2f});" for k in range(24, 30))}
pop('#c5',{T('ekmek', T('elli', t5)) + .1});
ttl('#t5b',{t5b + .1});
ttl('#t6',{t6 + .1}); pop('#r61',{T('Şubatta', t6)}); pop('#c6',{T('kırk', t6)});
ttl('#t7',{t7 + .1});
ttl('#t8',{t8 + .1}); tl.set('#b81',{{opacity:1}},{T('kırk', t8) - .1}); tl.fromTo('#b81',{{scaleX:0}},{{scaleX:1,duration:.7,ease:'power2.out'}},{T('kırk', t8) - .1});
tl.set('#b82',{{opacity:1}},{T('elli', t8) - .1}); tl.fromTo('#b82',{{scaleX:0}},{{scaleX:1,duration:.8,ease:'power2.out'}},{T('elli', t8) - .1});
ttl('#t9',{t9 + .1}); {''.join(f"pop('#q{k}',{t9 + .3 + k * .07:.2f},{{y:24}});" for k in range(10))}
pop('#k9',{T('Ayda', t9) - .1}); ''' + cnt('#n9', 0, 100000, T('Ayda', t9), 1.1) + f'''
{''.join(f"tl.to('#q{k}',{{color:'#e8b931',duration:.2}},{T('Ayda', t9) + k * .05:.2f});" for k in range(10))}
ttl('#t10',{t10 + .1});
ttl('#t11',{t11 + .1}); tl.set('#b111',{{opacity:1}},{T('yüzde', t11) - .1}); tl.fromTo('#b111',{{scaleX:0}},{{scaleX:1,duration:.7,ease:'power2.out'}},{T('yüzde', t11) - .1});
tl.set('#b112',{{opacity:1}},{T('yüzde', T('enflasyonu', t11)) - .1}); tl.fromTo('#b112',{{scaleX:0}},{{scaleX:1,duration:.8,ease:'power2.out'}},{T('yüzde', T('enflasyonu', t11)) - .1});
pop('#c11',{T('karşılamadı', t11) - .5});
ttl('#t12',{t12 + .1}); pop('#r121',{T('yüzde', t12)}); pop('#r122',{T('Piyasanın', t12)}); pop('#c12',{T('beklentisi', t12)});
ttl('#t12b',{t12b + .1}); ttl('#t13',{t13 + .1}); ttl('#t14',{t14 + .1});
''' + card_js('p4', t4 + .15) + card_js('p6', t6 + .15) + card_js('p8', t8 + .15) + card_js('p9', t9 + .15)


def SFX(A):
    return [[t2, 'f:p_whoosh', -13, 0, 'senaryo'], [ty1, 'f:p_klik', -12, 0, '20'], [ty2, 'f:p_klik', -12, 0, '25'], [ty3, 'f:p_klik', -12, 0, '30'],
            [t3, 'f:p_whoosh_bas', -11, 1, 'hesap'], [t4, 'f:p_whoosh', -13, 0, 'ekmek'], [tm, 'f:p_klik', -11, 0, '2800'],
            [t5, 'f:p_whoosh', -13, 0, 'mayis'], [t5b, 'f:p_boom', -10, 1, 'gitti'], [t6, 'f:p_whoosh', -13, 0, 'otobus'],
            [t7, 'f:p_boom', -10, 1, 'terskose'], [t8, 'f:p_whoosh', -13, 0, 'maliyet'], [t9, 'f:p_whoosh', -13, 0, 'firin'],
            [T('Ayda', t9), 'f:p_klik', -11, 0, '100bin'], [t10, 'f:p_whoosh_bas', -11, 1, 'doner'], [t11, 'f:p_whoosh', -13, 0, 'gecenyil'],
            [T('karşılamadı', t11) - .5, 'f:p_boom', -11, 1, 'karsilamadi'], [t12, 'f:p_whoosh', -13, 0, '2027'], [t12b, 'f:p_whoosh_bas', -11, 1, 'yerinde'],
            [t13, 'f:p_whoosh_bas', -11, 1, 'ekmeksay'], [t14, 'f:p_whoosh', -13, 0, 'cta']]


def RISERS(A): return []
