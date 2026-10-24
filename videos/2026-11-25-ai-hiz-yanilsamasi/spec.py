import os, json, re
from panel_kit import JS, HERO, title, glow_path, SVG_DEFS
# AI İLE PARA #1 — "Hız yanılsaması" · PANEL stili + ALTIN ÇERÇEVELİ avatar kartı (Ata 24 Eki 01:55: eski altın videodaki gibi çerçeve).
# Avatar sadece kanca+kilit (s1), vurgu (s5), kapanış+CTA (s9). Look: street hoodie seated. Müzik: onaylı.
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [(N('yüzde', 'on', 'dokuz'), '%19'), (N('yüzde', 'yirmi', 'beş'), '%25'), (N('yüzde', 'yirmi'), '%20'), (N('yüzde', 'kırk'), '%40'),
        (N('on', 'altı'), '16'), (N('iki', 'yüz', 'kırk', 'altı'), '246'), (N('yedi', 'yüz', 'elli', 'sekiz'), '758'),
        (N('iki', 'saat'), '2 saat'), (N('dört', 'saat!'), '4 saat!'), (N('bir', 'dakikada'), '1 dakikada')]
EM = {'tersini', 'yanılsaması', 'test', 'kontrol', 'gönder', 'hızlandıklarını'}
RED = {'yavaşladılar.', 'kötü', 'yavaşladılar'}
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False

# kelime zamanları (words.json) → T('kelime', sonra)
_WS = [x for x in json.load(open(os.path.join(W, 'words.json'))) if not x['word'].startswith('<')]
_cl = lambda s: re.sub(r"[^\wçğıöşüâî']", '', s.replace('I', 'ı').replace('İ', 'i').lower())


def T(w, after=0.0):
    for x in _WS:
        if x['start'] >= after - .01 and _cl(x['word']).startswith(_cl(w)):
            return round(x['start'], 2)
    raise SystemExit(f'kelime yok: {w} @{after}')


SEGS = json.load(open(os.path.join(W, 'segments.json')))['segments']
s1b = SEGS[0]['b']; s5a, s5b = SEGS[1]['a'] + .06, SEGS[1]['b']; s9a = SEGS[2]['a'] + .06
t_tuhaf = T('Ama', 18); t_gecen = T('Geçen', 19)


def scenes(A):
    return [('s1', 0, s1b), ('s2', s1b, t_tuhaf - .05), ('s3', t_tuhaf - .05, t_gecen - .05), ('s4', t_gecen - .05, s5a),
            ('s5', s5a, s5b), ('s6', s5b, T('Kendine', 46) - .1), ('s7', T('Kendine', 46) - .1, s9a), ('s9', s9a, DUR)]


AV = {'s1': HERO, 's2': None, 's3': None, 's4': None, 's5': HERO, 's6': None, 's7': None, 's9': HERO}
GF = ''   # altın çerçeve JS ile #avbox'ın ÜSTÜNE eklenir (avatar katmanı sahnelerin üstünde)

EXTRA_CSS = r'''<style>
.gf{position:absolute;opacity:0;left:132px;top:482px;width:816px;height:956px;border-radius:46px;border:5px solid #e8b931;
  box-shadow:0 0 26px rgba(232,185,49,.45),inset 0 0 18px rgba(232,185,49,.25);pointer-events:none;z-index:6}
.gold{color:#e8b931}
.chip{position:absolute;padding:14px 26px;border-radius:14px;font:800 40px 'Inter Tight';white-space:nowrap}
.chip.g{border:1.5px solid rgba(255,255,255,.45);background:rgba(255,255,255,.04);color:#fff}
.bar{position:absolute;border-radius:14px 14px 0 0;transform-origin:50% 100%}
.chk{display:flex;align-items:center;gap:22px;font:800 50px 'Inter Tight';color:#fff;margin:16px 0}
.chk b{width:50px;height:50px;border:4px solid #e8b931;border-radius:10px;display:inline-flex;align-items:center;justify-content:center;flex:none;font:900 36px 'Inter Tight';color:#e8b931}
.clock{position:absolute;left:390px;top:430px;width:300px;height:300px;border-radius:50%;border:6px solid #fff;box-shadow:0 0 30px rgba(255,255,255,.3)}
.hand{position:absolute;left:147px;top:40px;width:6px;height:110px;background:#e8b931;transform-origin:50% 100%;border-radius:3px;box-shadow:0 0 12px #e8b931}
</style>'''

SCENE_HTML = r'''
  <svg style="position:absolute;width:0;height:0">''' + SVG_DEFS + r'''</svg>
  <section id="s1" class="scene clip">
    ''' + title('t1', 'Yapay Zekâ Zaman', '<i>Kazandırıyor</i> mu?') + GF + r'''
  </section>
  <section id="s2" class="scene clip">
    ''' + title('t2', 'Kullananlar', 'Ne <i>Diyor?</i>') + r'''
    <div class="clock" id="ck"><div class="hand" id="hd"></div></div>
    <div class="a num glowt" id="n2" style="left:0;right:0;top:760px;text-align:center;font-size:130px;opacity:0">2 SAAT</div>
    <div class="lab" id="l2" style="position:absolute;left:0;right:0;top:900px;text-align:center;opacity:0">HAFTADA · ORTALAMA · ABD ANKETİ</div>
    <div class="chip g" id="c2" style="left:190px;top:990px;opacity:0">HER GÜN KULLANAN 1/3 → <span class="gold">4+ SAAT</span></div>
  </section>
  <section id="s3" class="scene clip">
    <div class="a" id="dk" style="left:60px;right:60px;top:620px;text-align:center;opacity:0">
      <div style="font:800 92px/1.02 'Inter Tight';letter-spacing:-.03em">Ama işin</div>
      <div style="font:italic 400 116px 'DM Serif Display';color:#ff3b30;text-shadow:0 0 30px rgba(255,59,48,.5)">tuhaf yanı…</div></div>
  </section>
  <section id="s4" class="scene clip">
    ''' + title('t4', 'Hissettikleri', 'vs <i>Ölçülen</i>') + r'''
    <div class="chip g" id="c4" style="left:200px;top:440px;opacity:0">16 YAZILIMCI · 246 GERÇEK İŞ</div>
    <div class="lab" style="position:absolute;left:0;right:0;top:530px;text-align:center">METR DENEYİ · 2025</div>
    <div style="position:absolute;left:140px;top:900px;width:800px;height:3px;background:rgba(255,255,255,.4)"></div>
    <div class="bar" id="b4a" style="left:250px;top:700px;width:220px;height:200px;background:linear-gradient(0deg,rgba(255,255,255,.25),rgba(255,255,255,.9))"></div>
    <div class="a num" id="v4a" style="left:220px;top:600px;width:280px;text-align:center;font-size:84px;opacity:0">+%20</div>
    <div class="lab" style="position:absolute;left:230px;top:1050px;width:260px;text-align:center">SANDILAR</div>
    <div class="bar" id="b4b" style="left:610px;top:903px;width:220px;height:190px;border-radius:0 0 14px 14px;transform-origin:50% 0;background:linear-gradient(180deg,#ff3b30,rgba(255,59,48,.3));box-shadow:0 0 40px rgba(255,59,48,.35)"></div>
    <div class="a num redt" id="v4b" style="left:580px;top:1100px;width:280px;text-align:center;font-size:84px;opacity:0">−%19</div>
    <div class="lab" style="position:absolute;left:590px;top:600px;width:260px;text-align:center">ÖLÇÜLEN</div>
  </section>
  <section id="s5" class="scene clip">
    ''' + title('t5', 'Hız', '<i>Yanılsaması</i>') + GF + r'''
  </section>
  <section id="s6" class="scene clip">
    ''' + title('t6', 'Harvard · 758', '<i>Danışman</i>') + r'''
    <div class="gbox" id="b61" style="left:110px;top:470px;width:410px;height:520px">
      <div class="lab" style="margin-bottom:26px">UYGUN İŞLER</div>
      <div class="num glowt" style="font-size:96px">+%25</div><div class="lab" style="margin:6px 0 26px">HIZ</div>
      <div class="num glowt" id="q40" style="font-size:96px;opacity:0">+%40</div><div class="lab" id="q40l" style="margin-top:6px;opacity:0">KALİTE</div></div>
    <div class="rbox" id="b62" style="left:560px;top:470px;width:410px;height:520px;border-radius:22px;flex-direction:column;font-size:52px;line-height:1.15;text-align:center;opacity:0">
      <div class="lab" style="color:#ffd0cc;margin-bottom:30px">UYGUN OLMAYAN</div>DAHA<br>KÖTÜ<br>SONUÇ</div>
  </section>
  <section id="s7" class="scene clip">
    ''' + title('t7', '1 Dakikada', '<i>Kontrol</i> Edebilir miyim?') + r'''
    <div class="gbox" id="b7" style="left:130px;top:450px;width:820px;height:440px;align-items:flex-start;padding:0 60px;opacity:0">
      <div class="chk" id="k1" style="opacity:0"><b id="m1"></b>Toplantı notu</div>
      <div class="chk" id="k2" style="opacity:0"><b id="m2"></b>E-posta taslağı</div>
      <div class="chk" id="k3" style="opacity:0"><b id="m3"></b>Tablo formülü</div></div>
    <div class="chip g" id="c71" style="left:130px;top:930px;opacity:0">EVET → <span class="gold">YAPAY ZEKÂYA VER</span></div>
    <div class="rbox" id="c72" style="left:130px;top:1040px;width:820px;height:96px;border-radius:14px;font-size:44px;opacity:0">HAYIR → KENDİN YAP</div>
  </section>
  <section id="s9" class="scene clip">
    ''' + title('t9', 'Kontrol Edebildiğin', '<i>İşte</i>') + GF + r'''
  </section>
'''

_js = JS + f'''
{{const g=document.createElement('div');g.className='gf';g.id='gfr';document.getElementById('avbox').after(g);}}
tl.set('#t1',{{opacity:1}},0); tl.set('#gfr',{{opacity:1}},0); tl.set('#gfr',{{opacity:0}},{s1b - .05});
// S2 — anket: saat + 2 saat + 4+ saat
ttl('#t2',{s1b + .1}); pop('#ck',{s1b + .4}); tl.fromTo('#hd',{{rotation:0}},{{rotation:720,duration:2.4,ease:'power2.inOut'}},{s1b + .6});
pop('#n2',{T('iki', 12) - .1}); fin('#l2',{T('kazandığını', 12)}); pop('#c2',{T('üçte', 15) - .1});
// S3 — desen kırılması
tl.to('.bg',{{opacity:.25,duration:.3}},{t_tuhaf - .05}); fin('#dk',{t_tuhaf + .05},{{y:20,d:.4}}); tl.to('#dk',{{opacity:0,duration:.2}},{t_gecen - .3}); tl.to('.bg',{{opacity:1,duration:.4}},{t_gecen - .1});
// S4 — METR: hissedilen vs ölçülen
ttl('#t4',{t_gecen + .1}); pop('#c4',{T('altı', 20) - .2});
tl.fromTo('#b4a',{{scaleY:0}},{{scaleY:1,duration:.8,ease:'power3.out'}},{T('bitirince', 27)}); pop('#v4a',{T('hızlandıklarını', 28)});
tl.fromTo('#b4b',{{scaleY:0}},{{scaleY:1,duration:.8,ease:'power3.out'}},{T('yüzde', 25)}); pop('#v4b',{T('yavaşladılar', 25)});
// S5 — vurgu (avatar)
ttl('#t5',{s5a + .1}); tl.fromTo('#gfr',{{opacity:0}},{{opacity:1,duration:.35}},{s5a}); tl.set('#gfr',{{opacity:0}},{s5b - .05});
// S6 — Harvard/BCG
ttl('#t6',{s5b + .1}); pop('#b61',{T('uygun', 36) - .1}); pop('#q40',{T('Kalite', 40)}); fin('#q40l',{T('Kalite', 40) + .2}); pop('#b62',{T('olmayan', 42) - .1});
// S7 — test
ttl('#t7',{T('Kendine', 46)}); pop('#b7',{T('sonucu', 47)});
fin('#k1',{T('Toplantı', 50)},{{y:10}}); fin('#k2',{T('e-posta', 50) - .2},{{y:10}}); fin('#k3',{T('tablo', 50)},{{y:10}});
tl.set('#m1, #m2, #m3',{{textContent:'✓'}},{T('evet', 54)}); pop('#c71',{T('zaman', 55) - .1}); pop('#c72',{T('Kontrol', 56)});
// S9 — kapanış + CTA
ttl('#t9',{s9a + .1}); tl.fromTo('#gfr',{{opacity:0}},{{opacity:1,duration:.35}},{s9a});
'''
SCENE_JS = _js


def SFX(A):
    return [[s1b + .05, 'f:p_whoosh', -13, 0, 'anket'], [T('iki', 12) - .12, 'f:p_klik', -12, 0, '2 saat'], [T('üçte', 15) - .12, 'f:p_klik', -12, 0, '4 saat'],
            [t_tuhaf - .05, 'f:p_boom', -9, 1, 'desen'], [t_gecen, 'f:p_whoosh', -13, 0, 'metr'], [T('yavaşladılar', 25) - .1, 'f:p_whoosh_bas', -11, 1, '-19'],
            [T('hızlandıklarını', 28) - .1, 'f:p_klik', -11, 0, '+20'], [s5a, 'f:p_boom', -10, 1, 'yanilsama'], [s5b + .05, 'f:p_whoosh', -13, 0, 'harvard'],
            [T('olmayan', 42) - .12, 'f:p_whoosh_bas', -11, 1, 'kotu'], [T('Kendine', 46), 'f:p_whoosh', -13, 0, 'test'],
            [T('evet', 54) - .05, 'f:p_klik', -11, 0, 'tik'], [T('Kontrol', 56) - .1, 'f:p_klik', -12, 0, 'kendin'], [s9a, 'f:p_whoosh', -13, 0, 'cta']]


def RISERS(A): return []
