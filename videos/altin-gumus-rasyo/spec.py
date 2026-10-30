import os
from panel_kit import JS, HERO, PIP, title, SVG_DEFS
from spec_util import load, FRAME_CSS
# ALTIN/GÜMÜŞ RASYOSU — 2000'den beri 80/50 kuralı (Ata 30 Eki). İLK "HEP VARIM" VİDEOSU (Ata 30 Eki 12:23):
# vurgulu cümlelerde altın çerçeveli HERO kart (~10–15 sn'de bir), grafik sahnelerinde sol altta yuvarlak PIP. Tek parça avatar (seg_00, tüm video).
U = load(); T = U.T; W = U.W; DUR = U.DUR
SRT = os.path.join(W, 'avatar_cut.srt')
N = lambda s: s.split()
REPL = [(N('bir ons bir virgül altmış iki ons'), '1 ons → 1,62 ons'), (N('İki bin sekiz'), '2008'), (N('İki bin on beş.'), '2015.'),
        (N('İki bin üç.'), '2003.'), (N('İki bin altı.'), '2006.'), (N('İki bin on.'), '2010.'), (N('Eylül iki bin.'), 'Eylül 2000.'),
        (N('İki binde,'), "2000'de,"), (N('iki binden'), "2000'den"), (N('yüz seksen lira'), '180 lira'), (N('iki yüz bin lira.'), '200 bin lira.'),
        (N('sekiz yüz seksen bin'), '880 bin'), (N('yedi yüz otuz bin.'), '730 bin.'), (N('sekseni'), "80'i"), (N('Ellinin'), "50'nin"),
        (N('ellinin'), "50'nin"), (N('seksen bir ons'), '81 ons'), (N('bir virgül altmış üç'), '1,63'), (N('Yüz otuz iki'), '132'),
        (N('kırk dokuz.'), '49.'), (N('İki virgül yetmiş bir'), '2,71'), (N('İki yüz on yedi'), '217'), (N('yüz doları'), '100 doları'),
        (N('dört virgül dört'), '4,4'), (N('on yılda'), '10 yılda'), (N('İki işlem.'), '2 işlem.'), (N('Seksen beş ve elli beş'), '85 ve 55'),
        (N('bir buçuk kat'), '1,5 kat'), (N('seksen.'), '80.'), (N('Bir ons, dört ons'), '1 ons, 4 ons')]
EM = {'olabilirdi!', 'rasyosu.', 'aştı.', 'döndü!', 'dürüst', 'geniş.', 'değil;', 'gönder.'}
RED = {'değil;', 'etmez.'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False
FULLOPEN = 1.2

t2 = T('Ama') - .1; t3 = T('Kuralın') - .1; t4 = T('Rasyo', t3 + 3) - .1; t5 = T('Eylül') - .1; t6 = T('İki', t5 + 1) - .1
t7 = T('İki', T('ellinin', t6) + 1) - .1          # İki bin sekiz krizi
t8 = T('İki', T('gümüş', T('otuz', t7))) - .1                   # İki bin on
t9 = T('Ve', t8) - .1; t10 = T('Rasyo', t9) - .1; t11 = T('Bugün', t10) - .1; t12 = T('Son', t11) - .1
t13 = T('Ama', t12) - .1; t14 = T('Seksen', t13) - .1; t15 = T('Bunu,', t14) - .1


def scenes(A):
    ts = [0, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, DUR]
    return [(f's{k + 1}', ts[k], ts[k + 1]) for k in range(15)]


HEROS = ['s1', 's2', 's5', 's7', 's9', 's11', 's13', 's15']
AV = {f's{k}': PIP for k in range(1, 16)}
AV.update({k: HERO for k in HEROS})

# ---- rasyo grafiği (aylık, 2000-08 … 2026-10)
RS = [int(x) for x in open('/home/claude/paranin-dili/videos/altin-gumus-rasyo/rasyo_aylik.txt').read().split('\n')[2].split(',')]
RS[180] = 80          # 26.08.2015 günlük kapanış 80,1 (haftalık örnekte 76 görünüyor)
X0, XW, Y0, YH, VMIN, VMAX = 170, 700, 510, 500, 30, 125
X = lambda i: X0 + i / (len(RS) - 1) * XW
Y = lambda v: Y0 + (VMAX - v) / (VMAX - VMIN) * YH
I = lambda y, m: (y - 2000) * 12 + m - 8
path = lambda a, b: ' '.join(('M' if i == a else 'L') + f'{X(i):.1f},{Y(RS[i]):.1f}' for i in range(a, b + 1))
KS = [0, I(2003, 5), I(2006, 4), I(2008, 10), I(2010, 11), I(2015, 8), I(2026, 1), len(RS) - 1]
PS = [path(KS[k], KS[k + 1]) for k in range(7)]   # geçişlerde bölünmüş: her parça kendi cümlesinde çizilir
SW = [(I(2003, 5), 'g', 'S'), (I(2006, 4), 's', 'A'), (I(2008, 10), 'g', 'S'), (I(2010, 11), 's', 'A'), (I(2015, 8), 'g', 'S'), (I(2026, 1), 's', 'A')]


def chart(sfx, parts):
    """parts: (path, durum) — durum 'on' = çizili, 'dr' = bu sahnede çizilecek"""
    h = (f'<div class="lab" style="position:absolute;left:{X0}px;top:{Y0 - 60}px">RASYO · AYLIK</div>'
         f'<svg class="gl" style="position:absolute;left:0;top:0;width:1080px;height:1920px" viewBox="0 0 1080 1920">')
    for v, c, lb in [(80, '#c9ccd3', '80'), (50, '#e8b931', '50')]:
        h += (f'<line x1="{X0}" x2="{X0 + XW}" y1="{Y(v):.0f}" y2="{Y(v):.0f}" stroke="{c}" stroke-width="3" stroke-dasharray="12 10" opacity=".85"/>'
              f'<text x="{X0 - 12}" y="{Y(v) + 9:.0f}" text-anchor="end" fill="{c}" font-family="IBM Plex Mono" font-weight="700" font-size="28">{lb}</text>')
    for yr in (2000, 2008, 2015, 2026):
        i = min(I(yr, 8 if yr == 2000 else 1), len(RS) - 1)
        h += f'<text x="{X(i):.0f}" y="{Y0 + YH + 42}" text-anchor="{"start" if yr == 2000 else "end" if yr == 2026 else "middle"}" fill="rgba(255,255,255,.65)" font-family="IBM Plex Mono" font-size="24">{yr}</text>'
    for k, (d, s) in enumerate(parts):
        st = '' if s == 'on' else ' stroke-dasharray="1" stroke-dashoffset="1"'
        h += (f'<path id="{sfx}g{k}" d="{d}" pathLength="1"{st} fill="none" stroke="#ffffff" stroke-width="14" filter="url(#glf)" opacity=".35"/>'
              f'<path id="{sfx}p{k}" d="{d}" pathLength="1"{st} fill="none" stroke="#ffffff" stroke-width="5" stroke-linejoin="round"/>')
    h += '</svg>'
    for n, (i, c, _) in enumerate(SW):
        col = '#c9ccd3' if c == 'g' else '#e8b931'
        h += f'<div class="mk" id="{sfx}m{n}" style="left:{X(i) - 17:.0f}px;top:{Y(RS[i]) - 17:.0f}px;background:{col};opacity:0"></div>'
    h += (f'<div class="lab" style="position:absolute;left:{X0 + XW}px;top:{Y0 - 60}px;transform:translateX(-100%)">'
          '<span class="slv">80↑ GÜMÜŞ</span> · <span class="gold">50↓ ALTIN</span></div>')
    return h


HOLD = ['1 ons <span class="gold">altın</span>', '80,9 ons <span class="slv">gümüş</span>', '1,63 ons <span class="gold">altın</span>',
        '132 ons <span class="slv">gümüş</span>', '2,71 ons <span class="gold">altın</span>', '217 ons <span class="slv">gümüş</span>',
        '4,4 ons <span class="gold">altın</span>']


def hold(sfx, idxs):
    return ''.join(f'<div class="hold" id="{sfx}h{k}" style="opacity:0"><span class="lab">ELİNDE</span><b>{HOLD[k]}</b></div>' for k in idxs)


EXTRA_CSS = '<style>' + FRAME_CSS + r'''
.chip{position:absolute;padding:14px 24px;border-radius:14px;font:800 34px 'Inter Tight';white-space:nowrap}
.chip.g{border:1.5px solid rgba(255,255,255,.45);background:rgba(255,255,255,.04);color:#fff}
.dc{position:absolute;left:150px;width:730px;box-sizing:border-box;border-radius:18px;padding:18px 26px;border:1.5px solid rgba(255,255,255,.4);background:rgba(255,255,255,.03)}
.dc .q{font:700 28px 'Inter Tight';color:rgba(255,255,255,.7);letter-spacing:.04em}
.dc .r{font:800 42px 'Inter Tight';margin-top:6px;color:#fff}
.qs{position:absolute;left:150px;width:730px;box-sizing:border-box;min-height:120px;border-radius:18px;border:1.5px solid rgba(232,185,49,.6);background:rgba(232,185,49,.05);
  display:flex;align-items:center;gap:24px;padding:14px 26px;font:800 38px 'Inter Tight';color:#fff}
.qs b{font:800 60px 'DM Serif Display';color:#e8b931;min-width:110px}
.qs.s{border-color:rgba(201,204,211,.7);background:rgba(201,204,211,.06)} .qs.s b{color:#c9ccd3}
.mk{position:absolute;width:34px;height:34px;border-radius:50%;border:4px solid #0b0b0d;box-shadow:0 0 18px rgba(255,255,255,.6)}
.hold{position:absolute;left:150px;width:730px;top:1100px;height:96px;box-sizing:border-box;border-radius:18px;border:1.5px solid rgba(232,185,49,.6);
  background:rgba(232,185,49,.06);display:flex;align-items:center;justify-content:space-between;padding:0 28px}
.hold b{font:800 50px 'Inter Tight';color:#fff}
.gold{color:#e8b931} .slv{color:#c9ccd3}
.coin{position:absolute;border-radius:50%;display:flex;align-items:center;justify-content:center;font:800 30px 'Inter Tight';color:#1a1408}
.coin.au{background:radial-gradient(circle at 35% 30%,#ffe9a3,#e8b931 55%,#9b7414);box-shadow:0 0 40px rgba(232,185,49,.5)}
.coin.ag{background:radial-gradient(circle at 35% 30%,#ffffff,#c9ccd3 55%,#6f737b);box-shadow:0 0 22px rgba(201,204,211,.35)}
.bar{position:absolute;bottom:0;border-radius:14px 14px 0 0;transform-origin:50% 100%}
</style>'''

coins = ''.join(f'<div class="coin ag" id="ag{k}" style="left:{560 + (k % 5) * 62}px;top:{820 - (k // 5) * 62}px;width:56px;height:56px;opacity:0"></div>' for k in range(15))

SCENE_HTML = r'''
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">''' + title('t1', '1 Ons Altın', '180 TL → <i>200 Bin</i>') + r'''</section>
  <section id="s2" class="scene clip">''' + title('t2', 'Tek Kuralla', '<i>880 Bin</i> TL') + r'''</section>
  <section id="s3" class="scene clip">
    ''' + title('t3', 'Altın / Gümüş', '<i>Rasyosu</i>') + r'''
    <div class="coin au" id="au" style="left:190px;top:600px;width:240px;height:240px;opacity:0;font-size:44px">1 ONS</div>
    <div class="num" id="eq" style="position:absolute;left:452px;top:660px;font-size:110px;opacity:0">=</div>
    ''' + coins + r'''
    <div class="dc" id="d31" style="top:920px;opacity:0;text-align:center"><div class="q">BUGÜN 1 ONS ALTIN =</div><div class="r"><span class="slv" style="font-size:72px">~79</span> ons gümüş</div></div>
  </section>
  <section id="s4" class="scene clip">
    ''' + title('t4', 'Tek', '<i>Kural</i>') + r'''
    <div class="qs s" id="q1" style="top:470px;opacity:0"><b>≥ 80</b>Altını sat, gümüş al</div>
    <div class="qs" id="q2" style="top:620px;opacity:0"><b>≤ 50</b>Gümüşü sat, altına dön</div>
    <div class="dc" id="d41" style="top:800px;opacity:0;text-align:center"><div class="q">KONTROL</div><div class="r">Her gün <span class="gold">kapanış</span>. O kadar.</div></div>
  </section>
  <section id="s5" class="scene clip">''' + title('t5', 'Eylül 2000', '<i>1 Ons Altın</i>') + r'''</section>
  <section id="s6" class="scene clip">''' + title('t6', 'Rasyo', '<i>2000 – 2008</i>') + chart('A', [(PS[k], 'dr') for k in range(3)]) + hold('A', [0, 1, 2]) + r'''</section>
  <section id="s7" class="scene clip">''' + title('t7', '2008 Krizi', '<i>132 Ons</i> Gümüş') + r'''</section>
  <section id="s8" class="scene clip">''' + title('t8', 'Rasyo', '<i>2008 – 2015</i>') + chart('B', [(PS[k], 'on') for k in range(3)] + [(PS[k], 'dr') for k in (3, 4)]) + hold('B', [3, 4, 5]) + r'''</section>
  <section id="s9" class="scene clip">''' + title('t9', 'Ocak 2026', 'Gümüş <i>100 $</i> Üstü') + r'''</section>
  <section id="s10" class="scene clip">''' + title('t10', 'Rasyo', '<i>2015 – 2026</i>') + chart('C', [(PS[k], 'on') for k in range(5)] + [(PS[k], 'dr') for k in (5, 6)]) + hold('C', [5, 6]) + r'''</section>
  <section id="s11" class="scene clip">''' + title('t11', 'Bugün', '<i>~880 Bin</i> TL') + title('t11b', 'Makasla Bile', '<i>730 Bin</i> TL') + r'''</section>
  <section id="s12" class="scene clip">
    ''' + title('t12', 'Son 10 Yıl', '<i>2 İşlem</i>') + r'''
    <div style="position:absolute;left:150px;top:470px;width:730px;height:520px">
      <div class="bar" id="b1" style="left:70px;width:250px;height:300px;background:linear-gradient(#5d5f66,#3a3b40);border:1.5px solid rgba(255,255,255,.4)"></div>
      <div class="bar" id="b2" style="left:410px;width:250px;height:486px;background:linear-gradient(#e8b931,#8a6612);box-shadow:0 0 40px rgba(232,185,49,.35)"></div>
    </div>
    <div class="num" id="v1" style="position:absolute;left:220px;width:250px;top:600px;text-align:center;font-size:64px;opacity:0">1 ons</div>
    <div class="num gold glowt" id="v2" style="position:absolute;left:560px;width:250px;top:420px;text-align:center;font-size:64px;opacity:0">1,62</div>
    <div class="lab" id="l1" style="position:absolute;left:220px;width:250px;top:1010px;text-align:center;opacity:0">SADECE ALTIN</div>
    <div class="lab" id="l2" style="position:absolute;left:560px;width:250px;top:1010px;text-align:center;opacity:0">KURAL 80/50</div>
    <div class="chip g" id="c121" style="left:150px;top:1080px;opacity:0;font-size:28px">ŞUB 2018 → GÜMÜŞ</div>
    <div class="chip g" id="c122" style="left:520px;top:1080px;opacity:0;font-size:28px;border-color:#e8b931;color:#e8b931">OCA 2026 → ALTIN</div>
  </section>
  <section id="s13" class="scene clip">''' + title('t13', 'Dürüst', '<i>Olalım</i>') + r'''</section>
  <section id="s14" class="scene clip">
    ''' + title('t14', 'Geçmiş', '<i>Garanti Değil</i>') + r'''
    <div class="dc" id="d141" style="top:460px;opacity:0;border-color:rgba(232,185,49,.7)"><div class="q">EŞİK 80 / 50 · 2000'DEN</div><div class="r"><span class="gold">4,4 kat</span></div></div>
    <div class="dc" id="d142" style="top:620px;opacity:0;border-color:rgba(255,59,48,.7)"><div class="q">EŞİK 85 / 55 · 2000'DEN</div><div class="r"><span class="redt">1,5 kat</span></div></div>
    <div class="dc" id="d143" style="top:800px;opacity:0"><div class="q">FİZİKİ GÜMÜŞ</div><div class="r">Makas <span class="redt">çok daha geniş</span></div></div>
    <div class="chip g" id="c141" style="left:150px;top:980px;opacity:0;border-color:#ff3b30;color:#ff3b30">BU BİR SİNYAL DEĞİL</div>
  </section>
  <section id="s15" class="scene clip">''' + title('t15', 'Yastık Altı', 'Arkadaşına <i>Gönder</i>') + r'''</section>
'''

hero_ranges = []
for sid, a, b in scenes(None):
    if sid in HEROS:
        hero_ranges.append((FULLOPEN + .35 if sid == 's1' else a + .35, b))
# ardışık HERO sahneleri (s1-s2) tek aralık
mr = []
for a, b in hero_ranges:
    if mr and a - mr[-1][1] < .6: mr[-1] = (mr[-1][0], b)
    else: mr.append((a, b))


def marks(sfx, pairs):
    return ''.join(f"pop('#{sfx}m{n}',{t:.2f},{{s:.3}});" for n, t in pairs)


def drs(sfx, seq):
    return ''.join(f"dr('#{sfx}p{k}, #{sfx}g{k}',{a:.2f},{max(.3, b - a):.2f},'none');" for k, a, b in seq)


def holds(sfx, seq):
    """seq: [(holdidx, t_on)], sonraki gelince öncekini söndür"""
    js = ''
    for k, (h, t) in enumerate(seq):
        js += f"pop('#{sfx}h{h}',{t:.2f});"
        if k + 1 < len(seq): js += f"fout('#{sfx}h{h}',{seq[k + 1][1] - .25:.2f},.2);"
    return js


tg = T('gider', t6); tg2 = T('gider', tg + 2)
SCENE_JS = JS + U.frame_js(mr) + f'''
tl.set('#t1',{{opacity:1}},0); ttl('#t2',{t2 + .1});
ttl('#t3',{t3 + .1}); pop('#au',{T('altınla', t3) - .2}); pop('#eq',{T('kaç', t3) - .1});
{''.join(f"pop('#ag{k}',{T('gümüş', T('kaç', t3)) - .3 + k * .04:.2f},{{s:.4}});" for k in range(15))} pop('#d31',{T('alabildiğin', t3)});
ttl('#t4',{t4 + .1}); pop('#q1',{T('sekseni', t4)}); pop('#q2',{T('Ellinin', t4)}); pop('#d41',{T('Her', t4)});
ttl('#t5',{t5 + .1});
ttl('#t6',{t6 + .1}); {drs('A', [(0, t6 + .2, T('seksen', t6)), (1, T('seksen', t6) + .6, T('ellinin', t6)), (2, T('ellinin', t6) + 2.2, t7 - .3)])}
{marks('A', [(0, T('seksen', t6)), (1, T('ellinin', t6))])}
{holds('A', [(0, t6 + .3), (1, T('seksen', T('gider', t6))), (2, T('bir', T('Gümüş', t6)))])}
ttl('#t7',{t7 + .1});
ttl('#t8',{t8 + .1}); {drs('B', [(3, t8 + .2, T('Rasyo', t8)), (4, T('Rasyo', t8) + 1.3, T('Rasyo', T('on', t8 + 3)))])} tl.set('#Bm0, #Bm1, #Bm2',{{opacity:1}},{t8});
{marks('B', [(3, T('Rasyo', t8)), (4, T('Rasyo', T('on', t8 + 3)))])}
{holds('B', [(3, t8 + .3), (4, T('İki', T('dokuz', t8))), (5, T('İki', T('seksen', T('beş', t8))))])}
ttl('#t9',{t9 + .1});
ttl('#t10',{t10 + .05}); {drs('C', [(5, t10 + .05, t10 + 1.05), (6, t10 + 1.1, t10 + 1.6)])} tl.set('#Cm0, #Cm1, #Cm2, #Cm3, #Cm4',{{opacity:1}},{t10});
{marks('C', [(5, t10 + 1.1)])}
{holds('C', [(5, t10 + .2), (6, T('dört', t10))])}
ttl('#t11',{t11 + .1}); fout('#t11',{T('Kuyumcu', t11) - .3},.25); ttl('#t11b',{T('Kuyumcu', t11)});
ttl('#t12',{t12 + .1});
tl.fromTo('#b1',{{scaleY:0}},{{scaleY:1,duration:.7,ease:'power3.out'}},{T('İki', t12)}); pop('#v1',{T('İki', t12) + .4}); pop('#l1',{T('İki', t12) + .4});
tl.fromTo('#b2',{{scaleY:0}},{{scaleY:1,duration:1.0,ease:'power3.out'}},{T('Makassız', t12)}); pop('#v2',{T('virgül', T('Makassız', t12)) - .2}); pop('#l2',{T('Makassız', t12) + .3});
pop('#c121',{T('işlem', t12)}); pop('#c122',{T('işlem', t12) + .5});
ttl('#t13',{t13 + .1});
ttl('#t14',{t14 + .1}); pop('#d141',{t14 + .3}); pop('#d142',{T('Seksen', t14) + .2}); pop('#d143',{T('Üstelik', t14)}); pop('#c141',{T('sinyal', t14) - .2});
ttl('#t15',{t15 + .1});
'''


def SFX(A):
    S = [[t2, 'f:p_boom', -10, 1, '880'], [t3, 'f:p_whoosh', -13, 0, 'rasyo'], [t4, 'f:p_whoosh', -13, 0, 'kural'],
         [t5, 'f:p_whoosh_bas', -11, 1, '2000'], [t6, 'f:p_whoosh', -13, 0, 'grafik1'], [t7, 'f:p_whoosh_bas', -11, 1, '2008'],
         [t8, 'f:p_whoosh', -13, 0, 'grafik2'], [t9, 'f:p_boom', -10, 1, 'ocak'], [t10, 'f:p_whoosh', -13, 0, 'grafik3'],
         [T('dört', t10), 'f:p_boom', -10, 1, '4,4'], [t11, 'f:p_whoosh_bas', -11, 1, 'bugun'], [t12, 'f:p_whoosh', -13, 0, '10yil'],
         [t13, 'f:p_whoosh_bas', -11, 1, 'durust'], [t14, 'f:p_whoosh', -13, 0, 'esik'], [t15, 'f:p_whoosh', -13, 0, 'cta']]
    for sfx, ts in [('A', [T('seksen', t6), T('ellinin', t6)]), ('B', [T('Rasyo', t8), T('Rasyo', T('on', t8 + 3))])]:
        S += [[t, 'f:p_klik', -11, 0, 'switch'] for t in ts]
    return S


def RISERS(A): return []
