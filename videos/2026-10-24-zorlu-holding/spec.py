import os
# Şablon: KAP BELGESİ / DOSYA MASASI (Ata seçimi, 21 Eki). Ceviz masa, krem kâğıt, sarı fosforlu kalem, kırmızı damga, bant ile yapışmış gerçek fotoğraflar.
# Anlatım: dedektif / ipucu zinciri (4 tarih). Avatar (gri kapüşon): s1 kanca, s6 "aynı hafta", s8 CTA.
# Gerçek görseller: media/ (ZES şarj ünitesi ve ZES görseli: zorlu-zes CDN; Vestel City: Wikimedia; Zorlu Center: YouTube küçük resmi) — kaynaklar.md
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [
    (N('yirmi', 'iki', 'ekim'), '22 Ekim:'), (N('yirmi', 'üç', 'ekim'), '23 Ekim:'), (N('on', 'dokuz', 'ekim'), '19 Ekim:'),
    (N('yirmi', 'ekim'), '20 Ekim:'), (N('dört', 'tarih'), '4 tarih'),
    (N('yüz', 'kırk', 'yedi', 'milyon', 'dolara'), '147 milyon dolara'), (N('iki', 'bin', 'yirmi', 'üçte'), "2023'te"),
    (N('beş', 'yüz', 'milyon', 'dolarlık'), '500 milyon dolarlık'), (N('iki', 'seçenek'), '2 seçenek'),
    (N('yüzde', 'kırk', 'beşinden'), "%45'inden"), (N('iki', 'bin', 'otuz', 'beşe'), "2035'e"),
    (N('yüzde', 'dokuz', 'virgül', 'yetmiş', 'beşten'), "%9,75'ten"), (N('yüzde', 'dörde'), "%4'e"),
]
EM = {'satıldı', 'kapanıyor', 'kaydet', 'borç', 'vazgeç', 'bekle', 'manşet', 'satır', 'nereye', 'aynı'}
RED = {'değil', "%45'inden", 'borç'}
FRONT = [250, 330, 580, 815, 18]
MID = [290, 300, 500, 703, 18]
AV = {'s1': FRONT, 's2': None, 's3': None, 's4': None, 's5': None, 's6': MID, 's7': None, 's8': FRONT}

EXTRA_CSS = r'''<style>
:root{--paper:#f4efe3;--ink:#1d1710;--hl:#ffe14d;--red:#c8322b;--cap-em-bg:#ffe14d;--cap-em-fg:#1d1710}
body,#root{background:#1b120c}
.bg{background:radial-gradient(ellipse 90% 60% at 25% 8%,rgba(255,214,150,.28) 0%,rgba(0,0,0,0) 60%),repeating-linear-gradient(92deg,#3a2517 0 22px,#33200f 22px 40px,#3d2818 40px 70px),#2c1c10}
.bg::after{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 120% 90% at 50% 40%,transparent 40%,rgba(0,0,0,.65) 100%)}
#grid{display:none}
#avbox{filter:drop-shadow(0 0 0 #f4efe3) drop-shadow(10px 0 0 #f4efe3) drop-shadow(-10px 0 0 #f4efe3) drop-shadow(0 10px 0 #f4efe3) drop-shadow(0 -10px 0 #f4efe3) drop-shadow(0 30px 40px rgba(0,0,0,.65))}
.doc{position:absolute;background:var(--paper);color:var(--ink);border-radius:6px;box-shadow:0 30px 60px rgba(0,0,0,.55),0 2px 0 rgba(0,0,0,.2);padding:34px 40px;font:500 34px/1.38 'IBM Plex Mono'}
.doc .hd{font:700 22px 'IBM Plex Mono';letter-spacing:.14em;color:#6b5a44;border-bottom:3px solid #1d1710;padding-bottom:12px;margin-bottom:16px}
.doc .ln{position:relative;margin:10px 0}
.doc .k{color:#6b5a44}
.doc b{font-weight:700}
.hlw{position:relative;display:inline;z-index:0}
.hlb{position:absolute;left:-6px;right:-6px;top:6px;bottom:2px;background:var(--hl);opacity:.9;z-index:-1;transform-origin:0 50%;transform:scaleX(0)}
.tab{position:absolute;background:var(--hl);color:var(--ink);font:800 34px 'IBM Plex Mono';letter-spacing:.06em;padding:8px 22px;border-radius:6px 6px 0 0;box-shadow:0 10px 20px rgba(0,0,0,.4)}
.stamp{position:absolute;border:7px solid var(--red);color:var(--red);font:800 40px 'IBM Plex Mono';letter-spacing:.08em;padding:8px 22px;border-radius:10px;transform:rotate(-9deg);background:rgba(244,239,227,.06);text-align:center;line-height:1.1}
.pol{position:absolute;background:#fbf8f1;padding:14px 14px 50px;box-shadow:0 24px 50px rgba(0,0,0,.6)}
.pol img{display:block;width:100%;height:100%;object-fit:cover}
.pol .cap{position:absolute;left:0;right:0;bottom:10px;text-align:center;font:600 24px 'IBM Plex Mono';color:#3b2f22}
.tape{position:absolute;width:150px;height:40px;background:rgba(255,248,220,.55);left:50%;top:-18px;margin-left:-75px;transform:rotate(-4deg)}
.card{position:absolute;background:var(--paper);color:var(--ink);border-radius:10px;box-shadow:0 24px 50px rgba(0,0,0,.55);padding:22px 26px}
.big{font:900 110px/1 'Inter Tight';letter-spacing:-.04em}
.mono{font-family:'IBM Plex Mono'}
.wht{color:#f4efe3}
.src{font:500 20px 'IBM Plex Mono';color:rgba(244,239,227,.6)}
.row{position:absolute;left:60px;width:960px;height:205px;display:flex;align-items:center;gap:28px;background:var(--paper);color:var(--ink);border-radius:10px;box-shadow:0 18px 40px rgba(0,0,0,.5);padding:0 30px}
.row .d{font:900 64px/1 'Inter Tight';letter-spacing:-.03em;min-width:250px}
.row .t{font:600 32px/1.25 'Inter Tight'}
.row.dim{opacity:.45}
</style>'''


def scenes(A):
    return [('s1', 0, 4.557), ('s2', 4.557, 9.30), ('s3', 9.30, 23.45), ('s4', 23.45, 38.2), ('s5', 38.2, 45.64),
            ('s6', 45.64, 48.98), ('s7', 48.98, 55.68), ('s8', 55.68, DUR)]


SCENE_HTML = r'''
  <section id="s1" class="scene clip">
    <div class="a" id="s1bg" style="left:0;top:0;width:1080px;height:1920px;background:url(media/zorlu_center.jpg) center/cover;filter:blur(6px) brightness(.35)"></div>
    <div class="a tab" id="s1q1" style="left:60px;top:220px;transform:rotate(-3deg)">SATILDI MI?</div>
    <div class="a tab" id="s1q2" style="left:640px;top:240px;transform:rotate(3deg)">KAPANIYOR MU?</div>
    <div class="a stamp" id="s1no" style="left:600px;top:1060px;font-size:64px">HAYIR</div>
  </section>
  <section id="s2" class="scene clip">
    <div class="a mono wht" id="s2l" style="left:60px;top:250px;font-size:30px;letter-spacing:.14em">DOSYA · ZORLU GRUBU · EKİM 2026</div>
    <div class="a card" id="s2c0" style="left:70px;top:340px;width:440px;height:300px;transform:rotate(-4deg)"><div class="mono" style="font-size:24px;color:#6b5a44">TARİH 1</div><div class="big" style="font-size:86px;white-space:nowrap;margin-top:22px;line-height:1.1">19 EKİM</div></div>
    <div class="a card" id="s2c1" style="left:570px;top:380px;width:440px;height:300px;transform:rotate(3deg)"><div class="mono" style="font-size:24px;color:#6b5a44">TARİH 2</div><div class="big" style="font-size:86px;white-space:nowrap;margin-top:22px;line-height:1.1">20 EKİM</div></div>
    <div class="a card" id="s2c2" style="left:90px;top:720px;width:440px;height:300px;transform:rotate(2deg)"><div class="mono" style="font-size:24px;color:#6b5a44">TARİH 3</div><div class="big" style="font-size:86px;white-space:nowrap;margin-top:22px;line-height:1.1">22 EKİM</div></div>
    <div class="a card" id="s2c3" style="left:560px;top:760px;width:440px;height:300px;transform:rotate(-3deg)"><div class="mono" style="font-size:24px;color:#6b5a44">TARİH 4</div><div class="big" style="color:#c8322b;font-size:86px;white-space:nowrap;margin-top:22px;line-height:1.1">23 EKİM</div></div>
    <div class="a mono wht" id="s2e" style="left:0;right:0;top:1150px;text-align:center;font-size:40px">sonunda: <span style="background:#ffe14d;color:#1d1710;padding:0 10px">neye bakacağın</span></div>
  </section>
  <section id="s3" class="scene clip">
    <div class="a tab" id="s3t" style="left:60px;top:250px">19 EKİM</div>
    <div class="a doc" id="s3d" style="left:60px;top:312px;width:960px;transform:rotate(-1deg)">
      <div class="hd">ÖZEL DURUM AÇIKLAMASI (ÖZET) · ZORLU ENERJİ</div>
      <div class="ln"><span class="k">Konu:</span> ZES (Electrip Global) pay satışı</div>
      <div class="ln" id="s3p"><span class="k">Satılan pay:</span> %41,28 <span class="k">→ kalan:</span> <b>%0</b></div>
      <div class="ln" id="s3a"><span class="k">Alıcı:</span> Wren House + Kuveyt Yatırım Otoritesi</div>
      <div class="ln"><span class="k">Bedel:</span> <span class="hlw"><span class="hlb" id="s3h1"></span><b>147.619.178,97 $</b></span></div>
      <div class="ln"><span class="k">Gelirin kullanımı:</span> yatırım harcamaları ve <span class="hlw"><span class="hlb" id="s3h2"></span><b>finansal yükümlülüklerin geri ödemesi</b></span></div>
    </div>
    <div class="a pol" id="s3ph" style="left:650px;top:930px;width:330px;height:440px;transform:rotate(4deg)"><div class="tape"></div><img src="media/zes_sarj.jpg"><div class="cap">ZES şarj ünitesi</div></div>
    <div class="a stamp" id="s3st" style="left:80px;top:1010px">2023<br>KONTROL<br>KUVEYT'TE</div>
    <div class="a src" id="s3src" style="left:60px;top:1350px">KAP · CNBC-e · ParaMedya (19-20.10.2026)</div>
  </section>
  <section id="s4" class="scene clip">
    <div class="a tab" id="s4t" style="left:60px;top:250px">20 EKİM</div>
    <div class="a pol" id="s4ph" style="left:60px;top:312px;width:960px;height:330px;transform:rotate(-1deg);padding-bottom:14px"><div class="tape"></div><img src="media/vestel_city.jpg"></div>
    <div class="a doc" id="s4d" style="left:60px;top:680px;width:960px;padding:22px 34px"><div class="hd" style="margin-bottom:6px;border:0;padding:0">VESTEL · 500 MİLYON $ TAHVİL · VADE 2029 · FAİZ %9,75</div><div style="font-size:28px">Tahvil sahiplerine <b>2 seçenek</b>:</div></div>
    <div class="a card" id="s4a" style="left:60px;top:870px;width:460px;height:360px"><div class="mono" style="font-size:24px;color:#6b5a44">SEÇENEK 1</div><div class="big" style="color:#c8322b">−%45</div><div style="font:700 34px 'Inter Tight';margin-top:10px">alacaktan vazgeç</div><div class="mono" style="font-size:22px;color:#6b5a44;margin-top:14px">yeni vade 2032 · faiz %6</div></div>
    <div class="a card" id="s4b" style="left:560px;top:870px;width:460px;height:360px"><div class="mono" style="font-size:24px;color:#6b5a44">SEÇENEK 2</div><div class="big">2035</div><div style="font:700 34px 'Inter Tight';margin-top:10px">kadar bekle</div>
      <div id="s4f" style="margin-top:14px;font:800 44px 'Inter Tight'"><span id="s4fo" style="position:relative">%9,75<span id="s4x" style="position:absolute;left:-4px;right:-4px;top:50%;height:6px;background:#c8322b;transform-origin:0 50%"></span></span> → <span id="s4fn" style="color:#c8322b">%4</span></div></div>
    <div class="a src" id="s4src" style="left:60px;top:1260px">KAP 1684657 · Bloomberg HT · ParaMedya (20.10.2026)</div>
  </section>
  <section id="s5" class="scene clip">
    <div class="a mono wht" id="s5l" style="left:60px;top:250px;font-size:30px;letter-spacing:.14em">AYNI HAFTA · 4 TARİH</div>
    <div class="a row dim" id="s5r0" style="top:300px"><div class="d">19 EKİM</div><div class="t">ZES'teki son pay satışı imzalandı</div></div>
    <div class="a row dim" id="s5r1" style="top:525px"><div class="d">20 EKİM</div><div class="t">Vestel tahvilcilere 2 seçenek sundu</div></div>
    <div class="a row" id="s5r2" style="top:750px"><div class="d">22 EKİM</div><div class="t">Satışın <span class="hlw"><span class="hlb" id="s5h2"></span>planlanan kapanışı</span></div></div>
    <div class="a row" id="s5r3" style="top:975px"><div class="d" style="color:#c8322b">23 EKİM</div><div class="t">Zorlu Enerji dolar tahvilinin <span class="hlw"><span class="hlb" id="s5h3"></span>faiz ödeme günü</span></div></div>
    <div class="a src" id="s5src" style="left:60px;top:1210px">Ekonomi Manşet · Patronlar Dünyası (21.10.2026)</div>
  </section>
  <section id="s6" class="scene clip">
    <div class="a" id="s6w" style="left:60px;top:1060px;width:960px;display:flex;gap:12px">
      <div class="card" style="position:relative;flex:1;padding:14px 0;text-align:center;font:900 46px 'Inter Tight'">19</div>
      <div class="card" style="position:relative;flex:1;padding:14px 0;text-align:center;font:900 46px 'Inter Tight'">20</div>
      <div class="card" style="position:relative;flex:1;padding:14px 0;text-align:center;font:900 46px 'Inter Tight';opacity:.35">21</div>
      <div class="card" style="position:relative;flex:1;padding:14px 0;text-align:center;font:900 46px 'Inter Tight'">22</div>
      <div class="card" style="position:relative;flex:1;padding:14px 0;text-align:center;font:900 46px 'Inter Tight';color:#c8322b">23</div></div>
    <div class="a mono wht" id="s6c" style="left:0;right:0;top:1200px;text-align:center;font-size:34px">satış + borç takvimi = <span style="background:#ffe14d;color:#1d1710;padding:0 10px">aynı hafta</span></div>
  </section>
  <section id="s7" class="scene clip">
    <div class="a tab" id="s7t" style="left:60px;top:250px">KAP'TA 3 ADIM</div>
    <div class="a card" id="s7a" style="left:60px;top:320px;width:960px;font:700 38px 'Inter Tight'"><span class="mono" style="color:#c8322b">1 </span> kap.org.tr → ZOREN / VESTL</div>
    <div class="a card" id="s7b" style="left:60px;top:450px;width:960px;font:700 38px 'Inter Tight'"><span class="mono" style="color:#c8322b">2 </span> Bildirimler → Özel Durum Açıklaması</div>
    <div class="a card" id="s7c" style="left:60px;top:580px;width:960px;font:700 38px 'Inter Tight'"><span class="mono" style="color:#c8322b">3 </span> O satırı bul ↓</div>
    <div class="a doc" id="s7d" style="left:60px;top:760px;width:960px;transform:rotate(1deg)">
      <div class="ln" id="s7bd" style="position:relative"><span class="k">Bedel:</span> 147.619.178,97 $<span id="s7x" style="position:absolute;left:-6px;right:300px;top:50%;height:6px;background:#c8322b;transform-origin:0 50%"></span></div>
      <div class="ln"><span class="k">Gelirin kullanımı:</span> <span class="hlw"><span class="hlb" id="s7h"></span><b>paranın nereye gideceği</b></span></div></div>
  </section>
  <section id="s8" class="scene clip">
    <div class="a stamp" id="s8k" style="left:330px;top:1170px;font-size:70px;transform:rotate(-6deg);background:#1b120c">KAYDET</div>
    <div class="a mono wht" id="s8a" style="left:0;right:0;top:1180px;text-align:center;font-size:44px">manşet değil, <span style="background:#ffe14d;color:#1d1710;padding:0 10px">o satır</span></div>
  </section>
'''

SCENE_JS = r'''
const hl=(s,t)=>tl.fromTo(s,{scaleX:0},{scaleX:1,duration:.45,ease:'power2.out'},t);
const strike=(s,t)=>tl.fromTo(s,{scaleX:0},{scaleX:1,duration:.3,ease:'power3.out'},t);
const stamp=(s,t)=>tl.fromTo(s,{opacity:0,scale:1.8},{opacity:1,scale:1,duration:.22,ease:'power4.in'},t);
// S1 kanca
tl.fromTo('#s1bg',{opacity:0},{opacity:1,duration:.4},0); inn('#s1q1',.3,{y:-30}); inn('#s1q2',1.83,{y:-30}); stamp('#s1no',3.3);
// S2 dört tarih
inn('#s2l',4.7); [0,1,2,3].forEach(i=>inn('#s2c'+i,5.38+i*.22,{y:80,s:.9})); inn('#s2e',7.25,{y:20});
// S3 19 Ekim KAP
inn('#s3t',9.4,{y:-10}); inn('#s3d',9.5,{y:60}); hl('#s3h1',12.9); inn('#s3ph',11.4,{y:80}); stamp('#s3st',16.85); hl('#s3h2',21.9); inn('#s3src',10.5,{y:0});
// S4 Vestel
inn('#s4t',23.55,{y:-10}); inn('#s4ph',23.6,{y:60}); inn('#s4d',25.45,{y:30}); inn('#s4a',30.3,{y:60}); inn('#s4b',32.26,{y:60});
tl.fromTo('#s4f',{opacity:0},{opacity:1,duration:.3},34.0); tl.fromTo('#s4x',{scaleX:0},{scaleX:1,duration:.3},36.6); slam('#s4fn',36.99); inn('#s4src',26.0,{y:0});
// S5 tarih listesi
inn('#s5l',38.25); [0,1].forEach(i=>tl.fromTo('#s5r'+i,{opacity:0,x:-60},{opacity:.45,x:0,duration:.35,ease:'expo.out'},38.3+i*.12));
inn('#s5r2',38.34,{y:40}); hl('#s5h2',39.9); inn('#s5r3',41.75,{y:40}); hl('#s5h3',44.4); inn('#s5src',42.0,{y:0});
// S6 aynı hafta
inn('#s6w',45.85,{y:40}); inn('#s6c',47.4,{y:20});
// S7 KAP adımları
inn('#s7t',49.05,{y:-10}); inn('#s7a',49.15); inn('#s7b',51.16); inn('#s7c',52.0); inn('#s7d',52.5,{y:40}); strike('#s7x',53.3); hl('#s7h',54.14);
// S8 CTA + döngü
stamp('#s8k',55.85); out('#s8k',56.75); inn('#s8a',57.0,{y:20});
'''


def SFX(A):
    return [[1.85, 'pop', -12, 0, 'q2'], [3.3, 'stamp', -7, 1, 'hayir'], [5.38, 'paper_drop', -11, 0, 'kartlar'],
            [9.5, 'paper_drop', -10, 0, 'kap'], [12.9, 'marker', -11, 0, 'bedel'], [16.85, 'stamp', -8, 1, '2023'], [21.9, 'marker', -11, 0, 'gerekce'],
            [23.6, 'paper_drop', -11, 0, 'vestel'], [30.3, 'impact', -9, 1, '45'], [32.26, 'ui_click', -11, 0, '2035'], [36.99, 'impact', -9, 1, 'faiz4'],
            [38.34, 'paper_drop', -11, 0, '22'], [41.75, 'impact', -10, 1, '23'], [49.15, 'ui_click', -12, 0, 'adim1'], [53.3, 'marker', -11, 0, 'bedel_x'],
            [54.14, 'marker', -10, 0, 'nereye'], [55.85, 'stamp', -7, 1, 'kaydet'], [59.3, 'success', -11, 0, 'loop']]


def RISERS(A): return [[9.1, 'sharp', -11], [23.25, 'metallic', -11], [38.0, 'sharp', -12]]
