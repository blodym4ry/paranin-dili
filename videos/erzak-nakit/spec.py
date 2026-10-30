import os
from panel_kit import JS, HERO, PIP, title, SVG_DEFS
from spec_util import load, FRAME_CSS
from visual_kit import VIS_CSS, bg_html, bg_js, card, card_js
# ERZAK Mİ NAKİT Mİ — İngiltere "Be Ready" 3 günlük stok çağrısı (22 Eki 2026) + raflar boşaldı (Ata'nın Habertürk reel'i, 30 Eki).
# HEP VARIM (HERO vurgu + PIP) + GERÇEK GÖRSEL (Pexels fotoğrafları, Ken Burns, perde açılışlı foto kartlar).
U = load(); T = U.T; W = U.W; DUR = U.DUR
SRT = os.path.join(W, 'avatar_cut.srt')
N = lambda s: s.split()
REPL = [(N('Yirmi iki Ekim\'de'), "22 Ekim'de"), (N('üç günlük'), '3 günlük'), (N('üç litre'), '3 litre'), (N('ateme'), 'ATM'),
        (N('yüzde kırk'), '%40'), (N('dört katına'), '4 katına'), (N('üç günde'), '3 günde'), (N('otuz altı litre.'), '36 litre.'),
        (N('Sekiz tane'), '8 tane'), (N('beş litrelik'), '5 litrelik'), (N('beş yüz lira.'), '500 lira.'), (N('yüzde yirmi sekiz'), '%28'),
        (N('altı ayda'), '6 ayda'), (N('Tüik\'e'), "TÜİK'e"), (N('dört kişiden'), '4 kişiden'), (N('üç ila altı'), '3-6'),
        (N('bir aylıkla'), '1 aylıkla'), (N('üç gün'), '3 gün'), (N('üç ay.'), '3 ay.')]
EM = {'Nakit!', 'boşaldı.', 'yanıyor.', 'kayıp.', 'birikim.', 'korur.', 'gönder.'}
RED = {'kayıp.', 'çalışmayabilir.'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False
FULLOPEN = 1.2

t2 = T('Nakit!') - .3; t3 = T('Yirmi') - .1; t4 = T('Çağrıdan') - .1; t4b = T('Bir', t4 + 1) - .1; t5 = T('Peki') - .1; t6 = T('Dört', t5) - .1
t7 = T('Ama', t6) - .1; t8 = T('Çantayı', t7) - .1; t9 = T('Bu', T('kayıp', t8)) - .1; t10 = T('Asıl', t9) - .1
t11 = T('Tüik\'e', t10) - .1; t12 = T('Erzak', t11) - .1; t13 = T('Bunu,', t12) - .1
TS = [0, t2, t3, t4, t4b, t5, t6, t7, t8, t9, t10, t11, t12, t13, DUR]
IDS = ['s1', 's2', 's3', 's4', 's4b', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13']
HEROS = ['s1', 's4', 's5', 's7', 's9', 's10', 's12', 's13']


def scenes(A):
    return [(IDS[k], TS[k], TS[k + 1]) for k in range(len(IDS))]


AV = {k: (HERO if k in HEROS else PIP) for k in IDS}

EXTRA_CSS = '<style>' + FRAME_CSS + VIS_CSS + r'''
.chip{position:absolute;padding:14px 24px;border-radius:14px;font:800 34px 'Inter Tight';white-space:nowrap}
.chip.g{border:1.5px solid rgba(255,255,255,.45);background:rgba(0,0,0,.45);color:#fff}
.row{position:absolute;left:155px;width:715px;height:92px;box-sizing:border-box;display:flex;align-items:center;justify-content:space-between;padding:0 26px;
  border-radius:16px;border:1.5px solid rgba(255,255,255,.35);background:rgba(0,0,0,.5);font:800 38px 'Inter Tight';color:#fff}
.row span.k{font:600 28px 'IBM Plex Mono';color:rgba(255,255,255,.75);letter-spacing:.06em}
.big{position:absolute;left:155px;width:715px;text-align:center;font:800 120px/1 'Inter Tight';color:#fff;text-shadow:0 0 30px rgba(0,0,0,.8)}
.btl{position:absolute;width:62px;height:120px;border-radius:14px 14px 10px 10px;background:linear-gradient(180deg,rgba(150,210,255,.95),rgba(60,140,220,.9));
  box-shadow:inset 0 0 0 3px rgba(255,255,255,.5),0 10px 24px rgba(0,0,0,.5)}
.btl::before{content:'';position:absolute;left:21px;top:-16px;width:20px;height:18px;border-radius:5px;background:#e8e8ea}
.per{position:absolute;width:120px;height:170px}
.per .h{position:absolute;left:35px;top:0;width:50px;height:50px;border-radius:50%;background:currentColor}
.per .b{position:absolute;left:15px;top:58px;width:90px;height:110px;border-radius:45px 45px 12px 12px;background:currentColor}
.bar{position:absolute;left:155px;width:715px;height:40px;border-radius:20px;background:rgba(255,255,255,.12);overflow:hidden}
.bar i{position:absolute;left:0;top:0;bottom:0;border-radius:20px;transform-origin:0 50%}
.gold{color:#e8b931} .redt{color:#ff3b30}
</style>'''

BGS = [('bg1', 'london1.jpg', 0), ('bg2', 'lira2.jpg', 1), ('bg3', 'london2.jpg', 1), ('bg4', 'shelves1.jpg', 0), ('bg4b', 'shelves2.jpg', 1),
       ('bg5', 'water2.jpg', 0), ('bg6', 'water1.jpg', 1), ('bg7', 'canned1.jpg', 0), ('bg8', 'canned2.jpg', 1), ('bg9', 'kit2.jpg', 0),
       ('bg10', 'lira2.jpg', 0), ('bg11', 'lira1.jpg', 1), ('bg12', 'shelves2.jpg', 0), ('bg13', 'london1.jpg', 0)]
BGMAP = {s: b for s, b in zip(IDS, [x[0] for x in BGS])}

bottles = ''.join(f'<div class="btl" id="w{k}" style="left:{185 + k * 84}px;top:730px;opacity:0"></div>' for k in range(8))
people = ''.join(f'<div class="per" id="q{k}" style="left:{205 + k * 160}px;top:470px;color:{"#ff3b30" if k == 3 else "rgba(255,255,255,.55)"};opacity:0"><div class="h"></div><div class="b"></div></div>' for k in range(4))

SCENE_HTML = bg_html(BGS) + r'''
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">''' + title('t1', 'İngiltere', '<i>3 Günlük</i> Erzak') + r'''</section>
  <section id="s2" class="scene clip">
    ''' + title('t2', 'Atlanan Kalem', '<i>Nakit</i>') + r'''
    ''' + card('p2', 'media/lira2.jpg', 450, 420, 'BOZUK PARA + BANKNOT') + r'''
    <div class="chip g" id="c2" style="left:155px;top:905px;opacity:0;font-size:30px">SONUNDA İKİ STOĞU DA HESAPLIYORUZ</div>
  </section>
  <section id="s3" class="scene clip">
    ''' + title('t3', '22 Ekim', 'Hazır <i>Ol</i> Çağrısı') + r'''
    <div class="row" id="r31" style="top:450px;opacity:0"><span class="k">SU</span>3 L / kişi / gün</div>
    <div class="row" id="r32" style="top:555px;opacity:0"><span class="k">IŞIK</span>El feneri</div>
    <div class="row" id="r33" style="top:660px;opacity:0;border-color:rgba(232,185,49,.8)"><span class="k">PARA</span><span class="gold">Nakit</span></div>
    ''' + card('p3', 'media/atm2.jpg', 780, 300, 'KESİNTİDE KART VE ATM DURABİLİR') + r'''
  </section>
  <section id="s4" class="scene clip">''' + title('t4', 'Çağrıdan Sonra', 'Raflar <i>Boşaldı</i>') + r'''</section>
  <section id="s4b" class="scene clip">
    ''' + title('t4b', 'Satışlar', '<i>Patladı</i>') + r'''
    ''' + card('p4a', 'media/canned1.jpg', 450, 300, 'KONSERVE') + r'''
    <div class="chip g" id="c4a" style="left:600px;top:470px;opacity:0;font-size:44px;border-color:#e8b931;color:#e8b931">+%40</div>
    ''' + card('p4b', 'media/light.jpg', 780, 300, 'EL FENERİ · 3 GÜNDE') + r'''
    <div class="chip g" id="c4b" style="left:640px;top:800px;opacity:0;font-size:44px;border-color:#e8b931;color:#e8b931">×4</div>
  </section>
  <section id="s5" class="scene clip">''' + title('t5', 'Peki Türkiye\'de', '<i>Kaça Patlar?</i>') + r'''</section>
  <section id="s6" class="scene clip">
    ''' + title('t6', '4 Kişi · 3 Gün', '<i>36 Litre</i> Su') + r'''
    <div class="lab" style="position:absolute;left:185px;top:675px">8 × 5 LİTRELİK ŞİŞE</div>
    ''' + bottles + r'''
    <div class="big" id="k6" style="top:930px;opacity:0">~<span id="n6">0</span> TL</div>
  </section>
  <section id="s7" class="scene clip">''' + title('t7', 'Asıl Para', 'Burada <i>Yanıyor</i>') + r'''</section>
  <section id="s8" class="scene clip">
    ''' + title('t8', 'Son Kullanma', '<i>Tarihi</i> Var') + r'''
    ''' + card('p8', 'media/canned2.jpg', 450, 300, 'KONSERVE · PİL') + r'''
    <div class="row" id="r81" style="top:785px;opacity:0"><span class="k">GIDA · 1 YIL</span><span class="redt">+%28</span></div>
    <div class="row" id="r82" style="top:890px;opacity:0;border-color:rgba(232,185,49,.8)"><span class="k">YENİRSE</span><span class="gold">kazandırır</span></div>
    <div class="row" id="r83" style="top:995px;opacity:0;border-color:rgba(255,59,48,.8)"><span class="k">ÇÖPE GİDERSE</span><span class="redt">hepsi kayıp</span></div>
  </section>
  <section id="s9" class="scene clip">''' + title('t9', '6 Ayda Bir', 'Mutfağa Al, <i>Yenile</i>') + r'''</section>
  <section id="s10" class="scene clip">''' + title('t10', 'Asıl Stok', '<i>Birikim</i>') + r'''</section>
  <section id="s11" class="scene clip">
    ''' + title('t11', 'TÜİK', 'Her <i>4 Kişiden 1</i>') + r'''
    ''' + people + r'''
    <div class="lab" id="l11" style="position:absolute;left:155px;top:665px;width:715px;text-align:center;opacity:0">BEKLENMEDİK MASRAFI KARŞILAYAMIYOR</div>
    <div class="lab" style="position:absolute;left:155px;top:760px">KURAL · 3-6 AYLIK GİDER</div>
    <div class="bar" id="br1" style="top:805px;opacity:0"><i id="bf1" style="width:100%;background:rgba(255,255,255,.35)"></i></div>
    <div class="lab" style="position:absolute;left:155px;top:880px">BAŞLANGIÇ · 1 AYLIK</div>
    <div class="bar" id="br2" style="top:925px;opacity:0"><i id="bf2" style="width:17%;background:#e8b931"></i></div>
  </section>
  <section id="s12" class="scene clip">''' + title('t12', 'Erzak 3 Gün', 'Birikim <i>3 Ay</i>') + r'''</section>
  <section id="s13" class="scene clip">''' + title('t13', 'Deprem Çantası Olan', 'Arkadaşına <i>Gönder</i>') + r'''</section>
'''

hr = []
for sid, a, b in scenes(None):
    if sid in HEROS:
        a2 = FULLOPEN + .35 if sid == 's1' else a + .35
        if hr and a2 - hr[-1][1] < .6: hr[-1] = (hr[-1][0], b)
        else: hr.append((a2, b))

SCENE_JS = JS + U.frame_js(hr) + bg_js(BGMAP, scenes(None)) + f'''
tl.set('#t1',{{opacity:1}},0);
ttl('#t2',{t2 + .1}); pop('#c2',{T('Sonunda')});
ttl('#t3',{t3 + .1}); pop('#r31',{T('Kişi', t3)}); pop('#r32',{T('El', t3)}); pop('#r33',{T('nakit', t3 + 1)});
ttl('#t4',{t4 + .1}); ttl('#t4b',{t4b + .1}); pop('#c4a',{T('yüzde', t4b)}); pop('#c4b',{T('dört', t4b)});
ttl('#t5',{t5 + .1});
ttl('#t6',{t6 + .1}); {''.join(f"pop('#w{k}',{T('Sekiz', t6) + k * .09:.2f},{{y:-40}});" for k in range(8))}
pop('#k6',{T('Yaklaşık', t6) - .2}); {{const o={{v:0}};tl.to(o,{{v:500,duration:.9,ease:'power2.out',onUpdate:()=>{{$('#n6').textContent=Math.round(o.v);}}}},{T('Yaklaşık', t6)});}}
ttl('#t7',{t7 + .1});
ttl('#t8',{t8 + .1}); pop('#r81',{T('Gıda', t8)}); pop('#r82',{T('Stok', t8)}); pop('#r83',{T('Çöpe', t8)});
ttl('#t9',{t9 + .1}); ttl('#t10',{t10 + .1});
ttl('#t11',{t11 + .1}); {''.join(f"pop('#q{k}',{t11 + .25 + k * .12:.2f},{{y:30}});" for k in range(4))}
tl.to('#q3',{{scale:1.15,duration:.3,yoyo:true,repeat:1}},{T('biri', t11)}); pop('#l11',{T('beklenmedik', t11)});
tl.set('#br1',{{opacity:1}},{T('Kural', t11)}); tl.fromTo('#bf1',{{scaleX:0}},{{scaleX:1,duration:.8,ease:'power2.out'}},{T('Kural', t11)});
tl.set('#br2',{{opacity:1}},{T('Sen', t11)}); tl.fromTo('#bf2',{{scaleX:0}},{{scaleX:1,duration:.6,ease:'power2.out'}},{T('Sen', t11)});
ttl('#t12',{t12 + .1}); ttl('#t13',{t13 + .1});
''' + card_js('p2', t2 + .15) + card_js('p3', T('Çünkü', t3) - .3) + card_js('p4a', t4b + .15) + card_js('p4b', T('El', t4b) - .3) + card_js('p8', t8 + .15)


def SFX(A):
    return [[t2, 'f:p_boom', -10, 1, 'nakit'], [t3, 'f:p_whoosh', -13, 0, 'kampanya'], [t4, 'f:p_whoosh_bas', -11, 1, 'raflar'],
            [T('yüzde', t4b), 'f:p_klik', -11, 0, '40'], [T('dört', t4b), 'f:p_klik', -11, 0, 'x4'], [t5, 'f:p_whoosh_bas', -11, 1, 'tr'],
            [t6, 'f:p_whoosh', -13, 0, 'su'], [T('Yaklaşık', t6), 'f:p_klik', -11, 0, '500'], [t7, 'f:p_boom', -10, 1, 'yaniyor'],
            [t8, 'f:p_whoosh', -13, 0, 'skt'], [t9, 'f:p_whoosh_bas', -11, 1, 'rotasyon'], [t10, 'f:p_boom', -10, 1, 'birikim'],
            [t11, 'f:p_whoosh', -13, 0, 'tuik'], [t12, 'f:p_whoosh_bas', -11, 1, '3gun3ay'], [t13, 'f:p_whoosh', -13, 0, 'cta']]


def RISERS(A): return []
