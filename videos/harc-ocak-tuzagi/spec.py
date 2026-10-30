import os
from panel_kit import JS, HERO, PIP, title, SVG_DEFS
from spec_util import load, FRAME_CSS
from visual_kit import VIS_CSS, bg_html, bg_js, card, card_js
# OCAK HARÇ TUZAĞI — pasaport harcı Ocak'ta zamlanır; Aralık'ta yatırıp Ocak'ta başvurana fark istenebilir (2023 örneği).
# HEP VARIM + GERÇEK GÖRSEL (NTV pasaport görseli, Pexels havalimanı/İstanbul).
U = load(); T = U.T; W = U.W; DUR = U.DUR
SRT = os.path.join(W, 'avatar_cut.srt')
N = lambda s: s.split()
REPL = [(N('on bin liradan'), '10 bin liradan'), (N('On yıllık'), '10 yıllık'), (N('on üç bin dört yüz lira.'), '13.400 lira.'),
        (N('İki bin yirmi üç başında'), '2023 başında'), (N('üç bin üç yüz liraydı.'), '3.300 liraydı.'), (N('Dört kattan'), '4 kattan'),
        (N('yüzde yirmi sekize'), "%28'e"), (N('yüzde on dokuza'), "%19'a"), (N('dört yetişkin,'), '4 yetişkin,'), (N('dört yetişkinde'), '4 yetişkinde'),
        (N('on bin lirayı'), '10 bin lirayı'), (N('on altı bini'), '16 bini'), (N('İki bin yirmi üçte'), "2023'te"), (N('on bin lira'), '10 bin lira')]
EM = {'ödeyebilir!', 'fazla!', 'istenebilir!', 'tamamla.', 'gönder.'}
RED = {'istenebilir!'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False
FULLOPEN = 1.2

t2 = T('On', 7) - .1; t3 = T('Üstelik') - .1; t4 = T('Geçen') - .1; t5 = T('Ama', t4) - .1; t6 = T('Harcı', t5) - .1
t7 = T('Yani', t6) - .1; t8 = T('Bunu', t7) - .1
TS = [0, t2, t3, t4, t5, t6, t7, t8, DUR]
IDS = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8']
HEROS = ['s1', 's4', 's5', 's7', 's8']


def scenes(A):
    return [(IDS[k], TS[k], TS[k + 1]) for k in range(len(IDS))]


AV = {k: (HERO if k in HEROS else PIP) for k in IDS}

EXTRA_CSS = '<style>' + FRAME_CSS + VIS_CSS + r'''
.chip{position:absolute;padding:14px 24px;border-radius:14px;font:800 34px 'Inter Tight';white-space:nowrap}
.chip.g{border:1.5px solid rgba(255,255,255,.45);background:rgba(0,0,0,.5);color:#fff}
.row{position:absolute;left:155px;width:715px;height:92px;box-sizing:border-box;display:flex;align-items:center;justify-content:space-between;padding:0 26px;
  border-radius:16px;border:1.5px solid rgba(255,255,255,.35);background:rgba(0,0,0,.55);font:800 38px 'Inter Tight';color:#fff}
.row span.k{font:600 28px 'IBM Plex Mono';color:rgba(255,255,255,.75);letter-spacing:.06em}
.big{position:absolute;left:155px;width:715px;text-align:center;font:800 110px/1 'Inter Tight';color:#fff;text-shadow:0 0 30px rgba(0,0,0,.8)}
.step{position:absolute;left:155px;width:715px;height:110px;box-sizing:border-box;border-radius:18px;display:flex;align-items:center;gap:22px;padding:0 26px;
  background:rgba(0,0,0,.55);border:1.5px solid rgba(255,255,255,.4);font:800 38px 'Inter Tight';color:#fff}
.step b{font:800 26px 'IBM Plex Mono';letter-spacing:.08em;color:#e8b931;min-width:130px}
.arr{position:absolute;left:497px;width:30px;height:34px;background:#e8b931;clip-path:polygon(0 0,100% 0,50% 100%)}
.gold{color:#e8b931} .redt{color:#ff3b30}
</style>'''

BGS = [('bg1', 'airport1.jpg', 0), ('bg2', 'pasaport_tr.jpg', 1), ('bg3', 'istanbul.jpg', 1), ('bg4', 'airport2.jpg', 0),
       ('bg5', 'waiting.jpg', 0), ('bg6', 'waiting.jpg', 1), ('bg7', 'bazaar1.jpg', 0), ('bg8', 'airport1.jpg', 0)]
BGMAP = {s: b for s, b in zip(IDS, [x[0] for x in BGS])}

SCENE_HTML = bg_html(BGS) + r'''
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">''' + title('t1', 'Pasaportu Ocak\'ta', 'Çıkarırsan <i>+10 Bin</i>') + r'''</section>
  <section id="s2" class="scene clip">
    ''' + title('t2', '10 Yıllık Pasaport', '<i>Harcı</i>') + r'''
    ''' + card('p2', 'media/pasaport_tr.jpg', 450, 376, 'PASAPORT HARCI') + r'''
    <div class="big" id="k2" style="top:870px;opacity:0"><span id="n2">3.300</span> TL</div>
    <div class="chip g" id="c2" style="left:155px;top:1010px;opacity:0;font-size:30px;border-color:#ff3b30;color:#ff3b30">2023 → 2026 · 4 KATTAN FAZLA</div>
  </section>
  <section id="s3" class="scene clip">
    ''' + title('t3', 'Her Ocak', '<i>Otomatik</i> Zam') + r'''
    <div class="row" id="r31" style="top:460px;opacity:0"><span class="k">2026 ARTIŞI</span>%18,95</div>
    <div class="row" id="r32" style="top:570px;opacity:0;border-color:rgba(232,185,49,.8)"><span class="k">2027 · EYLÜL VERİSİ</span><span class="gold">~%28</span></div>
    <div class="chip g" id="c3" style="left:155px;top:690px;opacity:0;font-size:28px">YENİDEN DEĞERLEME ORANI</div>
  </section>
  <section id="s4" class="scene clip">''' + title('t4', '4 Yetişkinde', 'Fark <i>10–16 Bin</i>') + r'''</section>
  <section id="s5" class="scene clip">''' + title('t5', 'Asıl', '<i>Tuzak</i>') + r'''</section>
  <section id="s6" class="scene clip">
    ''' + title('t6', 'Aralık\'ta Öde', 'Ocak\'ta <i>Başvur</i>') + r'''
    <div class="step" id="st1" style="top:450px;opacity:0"><b>ARALIK</b>Harcı yatırdın</div>
    <div class="arr" id="ar1" style="top:575px;opacity:0"></div>
    <div class="step" id="st2" style="top:625px;opacity:0"><b>OCAK</b>Başvuruya gittin</div>
    <div class="arr" id="ar2" style="top:750px;opacity:0"></div>
    <div class="step" id="st3" style="top:800px;opacity:0;border-color:rgba(255,59,48,.85)"><b style="color:#ff3b30">SONUÇ</b><span class="redt">Fark istenebilir</span></div>
    <div class="chip g" id="c6" style="left:155px;top:950px;opacity:0;font-size:28px">2023 · BAZI NÜFUS MÜDÜRLÜKLERİ</div>
    <div class="chip g" id="c6b" style="left:155px;top:1045px;opacity:0;font-size:28px;border-color:#e8b931;color:#e8b931">GERİ ADIM: BAKAN TALİMATI</div>
  </section>
  <section id="s7" class="scene clip">''' + title('t7', 'Aralık Bitmeden', '<i>Başvuruyu</i> Tamamla') + r'''</section>
  <section id="s8" class="scene clip">''' + title('t8', 'Tatil Planlayan', 'Arkadaşına <i>Gönder</i>') + r'''</section>
'''

hr = []
for sid, a, b in scenes(None):
    if sid in HEROS:
        a2 = FULLOPEN + .35 if sid == 's1' else a + .35
        if hr and a2 - hr[-1][1] < .6: hr[-1] = (hr[-1][0], b)
        else: hr.append((a2, b))

SCENE_JS = JS + U.frame_js(hr) + bg_js(BGMAP, scenes(None)) + f'''
tl.set('#t1',{{opacity:1}},0);
ttl('#t2',{t2 + .1}); pop('#k2',{T('İki', t2) - .2});
{{const o={{v:3300}};tl.fromTo(o,{{v:3300}},{{v:13400,duration:1.3,ease:'power2.inOut',onUpdate:()=>{{$('#n2').textContent=Math.round(o.v).toLocaleString('tr-TR');}}}},{T('Dört', T('liraydı', t2)) - .6});}}
pop('#c2',{T('Dört', T('liraydı', t2))});
ttl('#t3',{t3 + .1}); pop('#r31',{t3 + .5}); pop('#r32',{T('Eylül', t3)}); pop('#c3',{T('oran', t3)});
ttl('#t4',{t4 + .1}); ttl('#t5',{t5 + .1});
ttl('#t6',{t6 + .1}); pop('#st1',{t6 + .2}); pop('#ar1',{T('Ocak', t6) - .2}); pop('#st2',{T('Ocak', t6)}); pop('#ar2',{T('fark', t6) - .2}); pop('#st3',{T('fark', t6)});
pop('#c6',{T('İki', t6)}); pop('#c6b',{T('Geri', t6)});
ttl('#t7',{t7 + .1}); ttl('#t8',{t8 + .1});
''' + card_js('p2', t2 + .15)


def SFX(A):
    return [[t2, 'f:p_whoosh', -13, 0, 'harc'], [T('Dört', T('liraydı', t2)), 'f:p_boom', -10, 1, '4kat'], [t3, 'f:p_whoosh', -13, 0, 'zam'],
            [t4, 'f:p_whoosh_bas', -11, 1, 'fark'], [t5, 'f:p_boom', -10, 1, 'tuzak'], [t6, 'f:p_whoosh', -13, 0, 'akis'],
            [T('fark', t6), 'f:p_klik', -11, 0, 'fark'], [t7, 'f:p_whoosh_bas', -11, 1, 'aralik'], [t8, 'f:p_whoosh', -13, 0, 'cta']]


def RISERS(A): return []
