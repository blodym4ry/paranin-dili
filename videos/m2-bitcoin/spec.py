import os
from panel_kit import JS, HERO, PIP, title, SVG_DEFS
from spec_util import load, FRAME_CSS
# M2 ve BITCOIN — basit anlatım (Ata 30 Eki; @piovincenzo_ BTC–küresel M2 grafiği). PANEL + FULLOPEN + gerçek ekran görüntüleri.
U = load(); T = U.T; W = U.W; DUR = U.DUR
SRT = os.path.join(W, 'avatar_cut.srt')
N = lambda *w: list(w)
REPL = [(N('Bitkoin'), 'Bitcoin'), (N('em', 'iki.'), 'M2.'), (N('em', 'iki'), 'M2'), (N('Treyding', "Viuv'da"), "TradingView'da"),
        (N('yüzde', 'kırk'), '%40'), (N('yüz', 'üç', 'trilyon', 'dolarlık'), '103 trilyon $\'lık'), (N('on', 'iki'), '12'),
        (N('yüzde', 'seksen', 'üçünde,'), '%83\'ünde,'), (N('doksan', 'gün'), '90 gün'), (N('yüz', 'yedi', 'gün'), '107 gün'),
        (N('seksen', 'dört', 'gün'), '84 gün'), (N('altmış'), '60'), (N('yüz', 'yirmi', 'gün'), '120 gün')]
EM = {'kırdı.', 'altında!', 'havuzu!', 'değil.', 'düştü.', 'değil!', 'süs.', 'gönder.'}
RED = {'altında!', 'düştü.', 'değil!'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False
FULLOPEN = 1.2

a1, b1 = U.seg(0); a4, b4 = U.seg(2); a8, _ = U.seg(4)   # 5 parça: 0,[ara],1,[ara],2
tTe = T('Teori', 19); tAr = T('Bir', tTe) - .1; tBY = T('Ama', tTe); tKD = T('Kendin', b4); tTV = T('Treyding', tKD) - .3; tYa = T('Yani', tKD + 5)


def scenes(A):
    return [('s1', 0, b1), ('s2', b1, tTe - .1), ('s3h', tTe - .1, tAr), ('s3', tAr, tBY - .1), ('s4', tBY - .1, a4), ('s5', a4, b4),
            ('s6', b4, tKD - .1), ('s7h', tKD - .1, tTV), ('s7', tTV, tYa - .1), ('s8', tYa - .1, a8), ('s9', a8, DUR)]


# Ata 30 Eki 12:23 "ara ara olmalıyım": HERO vurgu kartları (≤~13 sn arayla) + grafik sahnelerinde yuvarlak PIP; avatar tüm videoda
AV = {k: PIP for k in ('s2', 's3', 's4', 's6', 's7', 's8')}
AV.update({k: HERO for k in ('s1', 's3h', 's5', 's7h', 's9')})

BTC_PATH = ('M165,948 L181,948 L196,926 L212,923 L227,931 L243,918 L258,923 L274,936 L289,932 L305,901 L321,889 L336,871 L352,870 L367,795 '
            'L383,755 L398,798 L414,770 L429,789 L445,782 L461,804 L476,787 L492,759 L507,654 L523,666 L538,630 L554,702 L569,710 L585,663 '
            'L601,622 L616,612 L632,577 L647,607 L663,584 L678,602 L694,678 L709,690 L725,726 L741,772 L756,767 L772,735 L787,746 L803,806 '
            'L818,789 L834,726 L849,706 L865,734')

EXTRA_CSS = '<style>' + FRAME_CSS + r'''
.chip{position:absolute;padding:14px 24px;border-radius:14px;font:800 34px 'Inter Tight';white-space:nowrap}
.chip.g{border:1.5px solid rgba(255,255,255,.45);background:rgba(255,255,255,.04);color:#fff}
.dc{position:absolute;left:150px;width:730px;border-radius:18px;padding:18px 26px;border:1.5px solid rgba(255,255,255,.4);background:rgba(255,255,255,.03)}
.dc .q{font:700 28px 'Inter Tight';color:rgba(255,255,255,.7);letter-spacing:.04em}
.dc .r{font:800 40px 'Inter Tight';margin-top:6px}
.lay{position:absolute;left:150px;width:730px;height:84px;border-radius:14px;display:flex;align-items:center;justify-content:space-between;padding:0 26px;font:800 36px 'Inter Tight';transform-origin:50% 100%}
.shot{position:absolute;border-radius:20px;overflow:hidden;background:#000;box-shadow:0 0 0 2px rgba(255,255,255,.35),0 24px 60px rgba(0,0,0,.7)}
.shot img{display:block;width:100%;height:auto}
.cnt{position:absolute;left:150px;width:730px;text-align:center}
.qs{position:absolute;left:150px;width:730px;min-height:110px;border-radius:18px;border:1.5px solid rgba(232,185,49,.6);background:rgba(232,185,49,.05);
  display:flex;align-items:center;gap:22px;padding:14px 26px;font:800 36px 'Inter Tight';color:#fff}
.qs b{font:800 56px 'DM Serif Display';color:#e8b931}
.gold{color:#e8b931}
</style>'''

SCENE_HTML = r'''
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">''' + title('t1', 'Para Rekorda', 'Bitcoin <i>%40 Aşağıda</i>') + r'''</section>
  <section id="s2" class="scene clip">
    ''' + title('t2', 'M2 Nedir?', '<i>Para Havuzu</i>') + r'''
    <div class="lay" id="y1" style="top:740px;opacity:0;background:rgba(255,255,255,.08);border:1.5px solid rgba(255,255,255,.4)"><span>NAKİT</span><span class="lab">CEBİNDEKİ</span></div>
    <div class="lay" id="y2" style="top:644px;opacity:0;background:rgba(232,185,49,.10);border:1.5px solid rgba(232,185,49,.6)"><span>VADESİZ</span><span class="lab">BANKADA</span></div>
    <div class="lay" id="y3" style="top:548px;opacity:0;background:rgba(255,59,48,.12);border:1.5px solid rgba(255,59,48,.6)"><span>VADELİ</span><span class="lab">BANKADA</span></div>
    <div class="chip g" id="c21" style="left:150px;top:450px;opacity:0;font-size:28px">ABD · AVRUPA · ÇİN · JAPONYA</div>
    <div class="cnt" id="k2" style="top:860px;opacity:0"><div class="lab">KÜRESEL M2 · BİR HESABA GÖRE</div><div class="num glowt gold" style="font-size:100px"><span id="n2">0</span> TRİLYON $</div></div>
    <div class="shot" id="i2" style="left:190px;top:1040px;width:650px;opacity:0"><img src="media/kobeissi.png"></div>
  </section>
  <section id="s3h" class="scene clip">''' + title('t3h', 'Teori', '<i>Basit</i>') + r'''</section>
  <section id="s3" class="scene clip">
    ''' + title('t3', 'Havuzla', '<i>Aynı Yön?</i>') + r'''
    <div class="dc" id="d31" style="top:450px;opacity:0"><div class="q">HAVUZ BÜYÜYÜNCE</div><div class="r">Para → <span class="gold">riskli varlıklara</span></div></div>
    <div class="cnt" id="k3" style="top:640px;opacity:0"><div class="lab">12 AYLIK DÖNEMLERİN</div><div class="num glowt gold" style="font-size:150px">%83</div><div class="lab" style="margin-top:8px">BITCOIN HAVUZLA AYNI YÖNDE</div></div>
  </section>
  <section id="s4" class="scene clip">
    ''' + title('t4', 'Bu Yıl', 'Havuz ↑ <i>Bitcoin ↓</i>') + r'''
    <div class="lab" style="position:absolute;left:165px;top:470px">BITCOIN · 2023–2026 · BİN $</div>
    <svg class="gl" style="left:0;top:0;width:1080px;height:1920px" viewBox="0 0 1080 1920"><path id="p4" d="''' + BTC_PATH + r'''" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" fill="none" stroke="#ff8a3d" stroke-width="7" stroke-linejoin="round" filter="url(#glf)"/></svg>
    <div class="chip g" id="c41" style="left:380px;top:520px;opacity:0;font-size:26px">ZİRVE · EKİM 2025 · 126 BİN $</div>
    <div class="chip g" id="c3" style="left:165px;top:1010px;opacity:0;border-color:#ff3b30;color:#ff3b30;font-size:30px">AYNI YÖN ≠ SEBEP</div>
    <div class="chip g" id="c42" style="left:600px;top:780px;opacity:0;font-size:26px;border-color:#ff3b30;color:#ff3b30">BUGÜN ~77 BİN $</div>
  </section>
  <section id="s5" class="scene clip">''' + title('t5', '90 Gün', '<i>Sabit Değil</i>') + r'''</section>
  <section id="s6" class="scene clip">
    ''' + title('t6', 'Hangi', '<i>Gecikme?</i>') + r'''
    <div class="shot" id="i6" style="left:150px;top:440px;width:730px;opacity:0"><img src="media/pio.png"></div>
    <div class="chip g" id="c61" style="left:150px;top:1010px;opacity:0;border-color:#e8b931;color:#e8b931">90 GÜN</div>
    <div class="chip g" id="c62" style="left:350px;top:1010px;opacity:0">107 GÜN</div>
    <div class="chip g" id="c63" style="left:580px;top:1010px;opacity:0">84 GÜN</div>
  </section>
  <section id="s7h" class="scene clip">''' + title('t7h', 'Kendin', '<i>Dene</i>') + r'''</section>
  <section id="s7" class="scene clip">
    ''' + title('t7', 'Kendin', '<i>Dene</i>') + r'''
    <div class="qs" id="q1" style="top:450px;opacity:0"><b>1</b>TradingView'da küresel M2 göstergesi</div>
    <div class="qs" id="q2" style="top:590px;opacity:0"><b>2</b>Gecikmeyi 60–120 gün arası oynat</div>
    <div class="dc" id="d71" style="top:760px;opacity:0;border-color:rgba(232,185,49,.7)"><div class="q">ÇOĞU AYARDA BİRLİKTE</div><div class="r">→ ilişki <span class="gold">sağlam</span></div></div>
    <div class="dc" id="d72" style="top:920px;opacity:0;border-color:rgba(255,59,48,.7)"><div class="q">SADECE TEK AYARDA</div><div class="r">→ <span class="redt">süs</span></div></div>
  </section>
  <section id="s8" class="scene clip">
    ''' + title('t8', 'Bu Grafik', 'Bir <i>Pusula</i>') + r'''
    <div class="gbox" id="b8" style="left:240px;top:500px;width:600px;height:360px"><div class="lab" style="margin-bottom:10px">YÖNÜ GÖSTERİR</div><div class="num gold" style="font-size:96px">PUSULA</div><div class="num redt" style="font-size:64px;margin-top:10px">SAAT DEĞİL</div></div>
  </section>
  <section id="s9" class="scene clip">''' + title('t9', 'Grafiğe Güvenen', 'Arkadaşına <i>Gönder</i>') + r'''</section>
'''

SCENE_JS = JS + U.frame_js([(FULLOPEN + .35, b1), (tTe + .25, tAr), (a4 + .35, b4), (tKD + .25, tTV), (a8 + .35, DUR)]) + f'''
tl.set('#t1',{{opacity:1}},0);
ttl('#t2',{b1 + .1}); pop('#y1',{T('nakit', b1)}); pop('#y2',{T('vadesiz', b1)}); pop('#y3',{T('vadeli', b1)}); pop('#c21',{T('Amerika', b1)});
pop('#k2',{T('hesaba', b1)}); {{const o={{v:0}};tl.to(o,{{v:103,duration:1.2,ease:'power2.out',onUpdate:()=>{{$('#n2').textContent=Math.round(o.v);}}}},{T('yüz', b1)});}}
pop('#i2',{T('havuzu', b1)});
ttl('#t3h',{tTe}); ttl('#t3',{tAr + .05}); pop('#d31',{tAr + .2}); pop('#k3',{T('yüzde', tTe)}); 
ttl('#t4',{tBY}); pop('#c3',{tBY + .2}); dr('#p4',{tBY + .4},3.2,'power1.inOut'); pop('#c41',{tBY + 2.6}); pop('#c42',{T('düştü', tBY)});
ttl('#t5',{a4 + .1});
ttl('#t6',{b4 + .1}); pop('#i6',{b4 + .2}); pop('#c61',{b4 + .5}); pop('#c62',{T('yüz', b4)}); pop('#c63',{T('seksen', b4)});
ttl('#t7h',{tKD}); ttl('#t7',{tTV + .05}); pop('#q1',{T('göstergesini', tKD) - .4}); pop('#q2',{T('gecikmeyi', tKD)}); pop('#d71',{T('Çizgiler', tKD)}); pop('#d72',{T('Sadece', tKD)});
ttl('#t8',{tYa}); pop('#b8',{T('pusula', tYa)});
ttl('#t9',{a8 + .1});
'''


def SFX(A):
    return [[b1 + .05, 'f:p_whoosh', -13, 0, 'm2'], [T('yüz', b1) - .1, 'f:p_boom', -10, 1, '103'], [tTe - .1, 'f:p_whoosh', -13, 0, 'teori'],
            [T('yüzde', tTe), 'f:p_klik', -11, 0, '83'], [tBY - .1, 'f:p_whoosh_bas', -11, 1, 'buyil'], [a4, 'f:p_whoosh', -13, 0, 'asil'],
            [b4 + .05, 'f:p_whoosh', -13, 0, 'gun'], [tKD - .1, 'f:p_whoosh_bas', -11, 1, 'dene'], [tYa - .1, 'f:p_klik', -11, 0, 'pusula'],
            [a8, 'f:p_whoosh', -13, 0, 'cta']]


def RISERS(A): return []
