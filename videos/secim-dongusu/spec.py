import os, math, random
from masa_kit import CSS, JS, OVERLAYS, ring, line, kup
# SEÇİM DÖNGÜSÜ — stil: MASA ÜSTÜ DOSYA. Avatar: lacivert balıkçı yaka. Müzik: karanlık hip-hop.
# İmza nesnesi: SEÇİM FATURASI fişi (2023: önce/sonra). Desen kırılması: lamba söner ("Döngü her seferinde işlemez").
# Açık döngü: mühürlü ZARF ("tek soru") → s7'de açılır. Kaynaklar: kaynaklar.md · Grafik alanı y=230–1180.
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [(N('yedi', 'mayıs', 'iki', 'bin', 'yirmi', 'sekiz'), '7 Mayıs 2028'), (N('iki', 'bin', 'yirmi', 'üç'), '2023'),
        (N('yüzde', 'elli', 'dört'), '%54'), (N('yüzde', 'sekiz', 'buçuktu'), "%8,5'ti"), (N('yüzde', 'yirmi', 'beş'), '%25'),
        (N('mart', 'iki', 'bin', 'yirmi', 'dörtte'), "Mart 2024'te"), (N('yüzde', 'elli'), '%50'), (N('yirmi', 'liradan'), '20 liradan'),
        (N('otuz', 'iki', 'liraya'), '32 liraya'), (N('iki', 'bin', 'on', 'beşte'), "2015'te"), (N('on', 'altı', 'nisan'), '16 Nisan')]
EM = {'fatura', 'faturaya', 'kesin', 'soru'}
RED = {'%25', '%50', '32 liraya', 'düştü'}
SOUND_KIT = 'masa'
EXIT_FADE = False
POL = [330, 240, 420, 560, 4]
AV = {'s1': POL, 's2': None, 's3': None, 's4': None, 's5': None, 's6': None, 's7': POL, 's8': POL, 's9': POL}


def wave(id_, w, h, seed):
    """Elle çizilmiş döngü dalgası (seçimde tepe, sonra dip): 3 varyant."""
    out = []
    for v in range(3):
        r = random.Random(seed * 10 + v); pts = []
        for k in range(0, 61):
            x = k / 60 * w; ph = k / 60 * 2 * math.pi * 1.5
            y = h / 2 - math.sin(ph) * h * .42 + r.uniform(-3, 3)
            pts.append((x, y))
        d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts)
        out.append(f'<path id="{id_}v{v}" d="{d}" pathLength="1" style="stroke-dasharray:1;stroke-dashoffset:1;opacity:{1 if v == 0 else 0}"/>')
    return f'<svg class="mk" id="{id_}" width="{w}" height="{h}" viewBox="0 0 {w} {h}">' + ''.join(out) + '</svg>'


EXTRA_CSS = CSS + r'''<style>
.stamp{position:absolute;font:900 60px 'Inter Tight';color:#c8261f;border:7px solid #c8261f;padding:6px 22px;transform:rotate(-8deg);mix-blend-mode:multiply;letter-spacing:.02em;white-space:nowrap}
.ital{font:italic 700 92px/1.05 'Playfair Display';color:#f6efe2;text-align:center}
.cal{position:absolute;width:330px;background:#fbfaf5;box-shadow:0 20px 32px rgba(0,0,0,.5);text-align:center;padding-bottom:20px}
.cal .m{background:#b3221a;color:#fff;font:800 40px 'Inter Tight';letter-spacing:.14em;padding:12px 0 10px}
.cal .d{font:900 170px/1 'Playfair Display';color:#15140f;margin-top:10px}
.cal .y{font:600 34px 'IBM Plex Mono';color:#4b4237;letter-spacing:.2em}
.cal .rg{position:absolute;left:-18px;top:-26px}
.zarf{position:absolute;width:520px;height:300px;background:url(media/masa/kraft.jpg) center/500px;box-shadow:0 18px 28px rgba(0,0,0,.45)}
.zarf .fl{position:absolute;left:0;right:0;top:0;height:170px;background:url(media/masa/kraft.jpg) 30% 20%/500px;clip-path:polygon(0 0,100% 0,50% 100%);filter:brightness(.88);transform-origin:50% 0}
.zarf .wx{position:absolute;left:220px;top:130px;width:80px;height:80px;border-radius:50%;background:radial-gradient(circle at 38% 35%,#e0473a,#8f1610);box-shadow:0 3px 6px rgba(0,0,0,.45)}
.zarf .lb{position:absolute;left:0;right:0;bottom:22px;text-align:center}
.fis .s{font:600 24px 'IBM Plex Mono';color:#77776f;text-align:center;letter-spacing:.1em;margin:4px 0}
</style>'''


def scenes(A):
    return [('s1', 0, 6.46), ('s2', 6.46, 12.25), ('s3', 12.25, 20.62), ('s4', 20.62, 36.75), ('s5', 36.75, 39.2),
            ('s6', 39.2, 47.56), ('s7', 47.56, 51.45), ('s8', 51.45, 54.78), ('s9', 54.78, DUR)]


FIS = r'''<div class="fis" id="fz" style="left:60px;top:240px;width:700px;transform:rotate(-1.5deg)">
  <div class="h">SEÇİM FATURASI · 2023</div>
  <div class="s" id="fs0">— SEÇİMDEN ÖNCE —</div>
  <div class="l" id="fz0"><span>Asgari ücret</span><span style="color:#2f7a2a">+%54,66</span></div>
  <div class="l" id="fz1"><span>Politika faizi</span><span>%8,5</span></div>
  <div class="s" id="fs1" style="border-top:3px dashed #9a9a92;padding-top:8px;margin-top:8px">— SEÇİMDEN SONRA —</div>
  <div class="l" id="fz2"><span>Faiz · Ağu 2023</span><span style="color:#b3221a">%25</span></div>
  <div class="l t" id="fz3" style="margin-top:0;border-top:0;padding-top:0"><span>Faiz · Mar 2024</span><span style="color:#b3221a">%50</span><div style="position:absolute;left:490px;top:-8px">''' + ring('r50', 170, 66, 5) + r'''</div></div>
  <div class="l t" id="fz4" style="font-size:38px"><span>Dolar/TL</span><span>20 → 32</span><div style="position:absolute;left:365px;top:-6px">''' + ring('rd', 275, 72, 7) + r'''</div></div>
</div>'''

SCENE_HTML = r'''
  <section id="s1" class="scene clip">
    <div class="tape" id="t1" style="left:290px;top:212px;transform:rotate(-30deg)"></div>
    <div class="tape" id="t2" style="left:650px;top:214px;transform:rotate(28deg)"></div>
    <div class="cal" id="cal" style="left:80px;top:830px;transform:rotate(-4deg)">
      <div class="m">MAYIS</div><div class="d">7</div><div class="y">2028</div>
      <div class="rg">''' + ring('rc', 370, 330, 3) + r'''</div>
    </div>
    <div class="kraft" id="n1" style="left:480px;top:880px;width:520px;height:250px;transform:rotate(3deg);padding:26px 34px">
      <div class="hand" style="font-size:66px">Sıradaki zengin</div>
      <div class="hand red" style="font-size:66px">olma tarihi?</div>
    </div>
  </section>
  <section id="s2" class="scene clip">
    <div class="photo" id="ph1" style="left:120px;top:250px;width:620px;height:440px;transform:rotate(-3deg)"><img src="media/sandik.jpg"><div class="cap">sandık · 2023</div></div>
    <div class="kraft" id="n2" style="left:560px;top:560px;width:450px;height:250px;transform:rotate(5deg);padding:24px 30px">
      <div class="hand" style="font-size:60px">krediyle girersen</div>
      <div class="hand red" id="n2w" style="font-size:76px;clip-path:inset(0 100% 0 0)">kaybedebilirsin</div>
    </div>
    <div class="zarf" id="zf" style="left:230px;top:840px;transform:rotate(-2deg)">
      <div class="fl"></div><div class="wx"></div>
      <div class="lb hand" style="font-size:60px">TEK SORU · sonda</div>
    </div>
  </section>
  <section id="s3" class="scene clip">
    <div class="strip" id="tl0" style="left:60px;top:300px;width:960px;background:#efe9da;justify-content:space-between;font-size:36px">
      <span>2015</span><span>2018</span><span>2023</span><span style="color:#b3221a">2028?</span></div>
    <div style="position:absolute;left:70px;top:420px">''' + wave('wv', 940, 300, 4) + r'''</div>
    <div class="hand" id="up" style="position:absolute;left:150px;top:400px;font-size:60px;clip-path:inset(0 100% 0 0)">seçim: hızlan</div>
    <div class="hand red" id="dn" style="position:absolute;left:520px;top:700px;font-size:72px;clip-path:inset(0 100% 0 0)">sonra: FATURA</div>
    <div class="photo" id="ph2" style="left:90px;top:800px;width:300px;height:250px;transform:rotate(-4deg)"><img src="media/nordhaus.jpg" style="object-position:50% 25%"><div class="cap">Nordhaus · 1975</div></div>
    <div class="kraft" id="n3" style="left:440px;top:880px;width:580px;height:200px;transform:rotate(2deg);padding:26px 30px">
      <div class="print" style="font-size:24px;color:#3b2a18">EKONOMİDE ADI:</div>
      <div class="hand" id="n3w" style="font-size:62px;clip-path:inset(0 100% 0 0)">politik konjonktür döngüsü</div>
    </div>
  </section>
  <section id="s4" class="scene clip">
    ''' + FIS + r'''
    <div class="photo" id="ph3" style="left:600px;top:810px;width:380px;height:260px;transform:rotate(5deg)"><img src="media/tcmb.jpg"><div class="cap">TCMB · Ankara</div></div>
    <div class="kraft" id="n4" style="left:70px;top:880px;width:480px;height:250px;transform:rotate(-3deg);padding:24px 34px">
      <div class="hand" id="n4a" style="font-size:96px;clip-path:inset(0 100% 0 0)">%8,5</div>
      <div class="hand red" id="n4b" style="font-size:96px;clip-path:inset(0 100% 0 0)">→ %50</div>
    </div>
  </section>
  <section id="s5" class="scene clip"></section>
  <section id="s6" class="scene clip">
    <div class="strip" id="bs" style="left:70px;top:260px;width:560px;background:#f0dcd6">BIST100 · 2015 &nbsp;<b style="color:#b3221a">−%16</b></div>
    <div class="hand red" id="bsa" style="position:absolute;left:650px;top:250px;font-size:80px;clip-path:inset(0 100% 0 0)">düştü</div>
    <div class="print" id="bss" style="position:absolute;left:76px;top:360px;font-size:20px;color:#f1e6d4;opacity:0">seçim yılı · 2015 yıllık getiri</div>
    ''' + kup('k1', 'HABERTÜRK · 25.06.2026', 'Mehmet Uçum: 16 Nisan 2028 tarihi erken seçim tarihi değil', 110, 450, -1.5, 50) + r'''
    <div class="cal" id="cal2" style="left:690px;top:760px;width:290px;transform:rotate(6deg)">
      <div class="m">NİSAN</div><div class="d" style="font-size:140px">16</div><div class="y">2028?</div>
    </div>
    <div class="stamp" id="st1" style="left:70px;top:900px;font-size:50px;opacity:0">AL SİNYALİ DEĞİL</div>
  </section>
  <section id="s7" class="scene clip">
    <div class="tape" id="t7" style="left:290px;top:212px;transform:rotate(-30deg)"></div>
    <div class="kraft" id="n7" style="left:80px;top:850px;width:920px;height:300px;transform:rotate(-2deg);padding:26px 40px">
      <div class="print" style="font-size:24px;color:#3b2a18">TEK SORU</div>
      <div class="hand" id="n7w" style="font-size:70px;clip-path:inset(0 100% 0 0)">Param seçimden sonraki</div>
      <div class="hand red" id="n7x" style="font-size:80px;clip-path:inset(0 100% 0 0)">faturaya hazır mı?</div>
    </div>
  </section>
  <section id="s8" class="scene clip">
    <div class="tape" id="t8" style="left:650px;top:214px;transform:rotate(28deg)"></div>
    <div class="kraft" id="n8" style="left:90px;top:860px;width:900px;height:200px;transform:rotate(2deg);padding:30px 36px">
      <div class="hand red" style="font-size:60px">→ kredi çekmeyi düşünen arkadaşına</div>
    </div>
  </section>
  <section id="s9" class="scene clip">
    <div class="cal" id="cal3" style="left:90px;top:830px;transform:rotate(-4deg)">
      <div class="m">MAYIS</div><div class="d">7</div><div class="y">2028</div>
      <div style="position:absolute;left:10px;top:150px">''' + line('x9', 310, 9) + r'''</div>
    </div>
    <div class="kraft" id="n9" style="left:470px;top:880px;width:530px;height:240px;transform:rotate(3deg);padding:28px 34px">
      <div class="hand" style="font-size:52px">asıl önemli olan</div>
      <div class="hand red" id="n9w" style="font-size:84px;clip-path:inset(0 100% 0 0)">fatura tarihi</div>
    </div>
  </section>
  ''' + OVERLAYS + r'''
  <div class="ital" id="dk" style="position:absolute;left:60px;right:60px;top:640px;opacity:0">Döngü her seferinde<br>işlemez.</div>
'''

SCENE_JS = JS + r'''
cam(__DUR__);
lamp(0,'rgba(255,200,120,A)',.14);
// S1 — kanca: takvim yaprağı + not ilk karede hazır; 7 Mayıs daire
tape('#t1',.2,-30); tape('#t2',.4,28); draw('rc',4.5,.6,6.46);
// S2 — sandık fotoğrafı, kredi riski, mühürlü zarf (açık döngü)
slide('#ph1',6.55); put('#n2',7.4,{r:5,y:140}); write('#n2w',8.04,.7); lamp(8.0,'rgba(255,70,50,A)',.26);
put('#zf',9.65,{r:-2,y:200}); lamp(9.7,'rgba(255,200,120,A)',.14);
// S3 — zaman şeridi + döngü dalgası + Nordhaus
put('#tl0',12.35,{x:-300,y:0,dr:0,n:4}); draw('wv',13.4,1.4,20.62); write('#up',14.0,.5);
slide('#ph2',15.14); put('#n3',16.25,{r:2,y:140}); write('#n3w',16.89,.9);
write('#dn',18.81,.6); lamp(18.8,'rgba(255,70,50,A)',.3);
// S4 — SEÇİM FATURASI fişi
put('#fz',20.7,{r:-1.5,y:-520,dr:0,n:5}); ['#fs0','#fz0','#fz1','#fs1','#fz2','#fz3','#fz4'].forEach(s=>tl.set(s,{opacity:0},0));
lamp(20.8,'rgba(255,200,120,A)',.14);
prt('#fs0',21.0); prt('#fz0',23.53); lamp(23.6,'rgba(120,230,120,A)',.26); prt('#fz1',26.1); put('#n4',26.3,{r:-3,y:140}); write('#n4a',26.55,.4);
prt('#fs1',27.61); lamp(28.1,'rgba(255,70,50,A)',.32); slide('#ph3',28.25);
prt('#fz2',29.86);
prt('#fz3',32.88); write('#n4b',33.0,.5); draw('r50',33.3,.45,36.75);
prt('#fz4',34.57); draw('rd',35.9,.45,36.75);
// S5 — LAMBA SÖNER: desen kırılması
dark(36.85,38.95); tl.fromTo('#dk',{opacity:0},{opacity:1,duration:2*F,ease:'steps(2)'},37.0); tl.to('#dk',{opacity:0,duration:2*F,ease:'steps(2)'},38.9);
// S6 — 2015 borsa, 16 Nisan kupürü, damga
lamp(39.2,'rgba(255,200,120,A)',.14);
put('#bs',39.4,{x:-300,y:0,dr:0,n:4}); write('#bsa',41.45,.5); tl.to('#bss',{opacity:1,duration:F},41.5); lamp(41.45,'rgba(255,70,50,A)',.28);
put('#k1',42.3,{r:-1.5,y:-180}); put('#cal2',43.73,{r:6,y:160}); lamp(43.0,'rgba(255,200,120,A)',.14);
tl.fromTo('#st1',{opacity:0,scale:1.6},{opacity:1,scale:1,duration:3*F,ease:'steps(3)'},46.25);
// S7 — zarf açıldı: tek soru (avatar)
tape('#t7',47.65,-30); put('#n7',47.8,{r:-2,y:150}); write('#n7w',48.87,1.0); write('#n7x',50.15,.7);
// S8 — CTA
tape('#t8',51.55,28); put('#n8',51.7,{r:2,y:140}); take('#n8',54.55,{x:1300});
// S9 — döngü: takvim geri gelir, tarih çizilir, fatura tarihi
put('#cal3',54.85,{r:-4,y:200}); put('#n9',55.4,{r:3,y:160}); draw('x9',57.35,.4,DURX); write('#n9w',58.09,.6); lamp(57.4,'rgba(255,70,50,A)',.26);
'''.replace('__DUR__', str(DUR)).replace('DURX', str(DUR))


def SFX(A):
    return [[.2, 'f:bant', -7, 0, 'bant'], [.4, 'f:bant', -9, 0, 'bant'], [4.5, 'f:kalem_daire', -6, 1, '7 mayis'],
            [6.55, 'f:deklansor', -7, 0, 'sandik'], [7.4, 'f:kagit_kay', -9, 0, 'not2'], [8.04, 'f:kalem_yaz', -6, 1, 'kaybedebilir'],
            [9.65, 'f:foto_birak', -7, 0, 'zarf'],
            [12.35, 'f:kagit_kay', -8, 0, 'serit'], [13.4, 'f:kalem_yaz', -9, 0, 'dalga'], [15.14, 'f:deklansor', -8, 0, 'nordhaus'],
            [16.25, 'f:kagit_kay', -9, 0, 'not3'], [16.89, 'f:kalem_yaz', -8, 0, 'pkd'], [18.81, 'f:kalem_yaz', -5, 1, 'fatura'],
            [20.7, 'f:kagit_kay', -7, 0, 'fis'], [21.0, 'f:daktilo', -11, 0, 'once'], [23.53, 'f:daktilo', -9, 1, '%54'], [26.1, 'f:daktilo', -10, 0, '%8,5'],
            [27.61, 'f:daktilo', -10, 0, 'sonra'], [28.25, 'f:deklansor', -8, 0, 'tcmb'], [29.86, 'f:daktilo', -8, 1, '%25'], [26.3, 'f:kagit_kay', -10, 0, 'not4'],
            [32.88, 'f:daktilo', -8, 1, '%50'], [33.3, 'f:kalem_daire', -6, 0, 'daire50'], [34.57, 'f:daktilo', -9, 0, 'dolar'], [35.9, 'f:kalem_daire', -6, 1, 'daire dolar'],
            [36.85, 'f:tukenmez_tik', -4, 1, 'lamba kapan'], [38.9, 'f:tukenmez_tik', -6, 0, 'lamba ac'],
            [39.4, 'f:kagit_kay', -9, 0, 'bist'], [41.45, 'f:kalem_yaz', -6, 1, 'dustu'], [42.3, 'f:foto_birak', -7, 0, 'kupur'], [43.73, 'f:sayfa', -8, 0, '16 nisan'],
            [46.25, 'f:damga', -4, 1, 'al sinyali degil'],
            [47.65, 'f:bant', -8, 0, 'bant'], [47.8, 'f:kagit_kay', -9, 0, 'not7'], [48.87, 'f:kalem_yaz', -7, 0, 'soru'], [50.15, 'f:kalem_yaz', -6, 1, 'hazir mi'],
            [51.55, 'f:bant', -9, 0, 'bant'], [51.7, 'f:kagit_kay', -9, 0, 'cta'],
            [54.85, 'f:sayfa', -8, 0, 'takvim'], [55.4, 'f:kagit_kay', -9, 0, 'not9'], [57.35, 'f:kalem_yaz', -6, 0, 'ciz'], [58.09, 'f:kalem_yaz', -5, 1, 'fatura tarihi']]


def RISERS(A): return []
