CSS_FILE = 'gazete.css.html'
import os
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [
    (N('bir', 'milyon', 'beş', 'yüz', 'elli', 'bin', 'lira'), '1.550.000 lira'), (N('bir', 'milyon', 'altı', 'yüz', 'bin'), '1,6 milyon'),
    (N('yüz', 'yirmi', 'beş', 'liradan'), '125 liradan'), (N('altı', 'bin', 'altı', 'yüze'), "6.600'e"),
    (N('kırk', 'dokuz', 'buçuğa'), "49,5'a"), (N('on', 'beş', 'buçuk', 'kat'), '15,5 kat'), (N('bist', 'yüz', 'endeksi'), 'BIST 100 endeksi'),
    (N('bir', 'buçuk', 'milyon'), '1,5 milyon'), (N('yüz', 'bin', 'lirası'), '100 bin lirası'), (N('yüz', 'bin', 'lira'), '100 bin lira'),
    (N('beş', 'milyonu'), '5 milyonu'), (N('üç', 'liradan'), '3 liradan'), (N('üç', 'kattan'), '3 kattan'),
    (N('on', 'yıl'), '10 yıl'), (N('on', 'yılda'), '10 yılda'),
]
EM = {'zenginleşmedi', 'temettü', 'gerçekten', 'enflasyondan', 'kaydet', 'tüik', 'altın', 'borsa', 'dolar', 'zengin', 'garantisi'}
RED = {'zenginleşmedi', 'saydı', 'değil', 'yerinde'}
FRONT = [250, 375, 580, 815, 6]
MID = [300, 420, 480, 675, 6]
AV = {'s1': FRONT, 's2': None, 's3': None, 's4': None, 's5': MID, 's6': None, 's7': None, 's8': None, 's9': None, 's10': FRONT, 's11': FRONT}
EXTRA_CSS = '''<style>
.row{position:absolute;left:60px;width:960px;height:150px}
.rl{position:absolute;left:0;top:0;font:700 30px 'IBM Plex Mono';letter-spacing:.12em;color:#161412}
.rb{position:absolute;left:0;top:44px;height:78px;background:#161412;transform-origin:0 50%}
.rv{position:absolute;top:50px;font:400 60px/1 'DM Serif Display';color:#161412;white-space:nowrap}
.gold-b{background:repeating-linear-gradient(-45deg,#b07a12 0 7px,#d9a520 7px 14px)}
.infl{position:absolute;top:-30px;width:0;height:540px;border-left:6px dashed #c8261b}
.stampbox{border:8px solid #c8261b;color:#c8261b;padding:6px 30px;border-radius:10px;font:400 96px/1 'DM Serif Display';white-space:nowrap}
.q{font:400 150px/1 'DM Serif Display';color:#c8261b}
</style>'''


def scenes(A):
    b = lambda t: round(t - .1, 3)
    t2 = A('Aynı'); t3 = A('Birinci'); t4 = A('İkinci'); t5 = A('Kulağa'); t6 = A('TÜİK'); t7 = A('Üçüncü'); t8 = A('Enflasyondan')
    t9 = A('Gerçekten', t8); t10 = A('Geçmiş'); t11 = A('Kaydet')
    # s1 / s5 end a little earlier than word-0.1 so the avatar window is gone before its clip ends (AVATAR GUARD)
    return [('s1', 0, round(t2 - .16, 3)), ('s2', round(t2 - .16, 3), b(t3)), ('s3', b(t3), b(t4)), ('s4', b(t4), b(t5)),
            ('s5', b(t5), round(t6 - .14, 3)), ('s6', round(t6 - .14, 3), b(t7)), ('s7', b(t7), b(t8)), ('s8', b(t8), b(t9)),
            ('s9', b(t9), b(t10)), ('s10', b(t10), b(t11)), ('s11', b(t11), DUR)]


def SFX(A):
    return [[A('zenginleşmedi'), 'stamp', -9, 1, 'hook'], [A('Sonunda'), 'whoosh_hollow', -13, 0, 'race'],
            [A('BIST 100 endeksi'), 'marker', -11, 0, 'bist'], [A('1.550.000 lira'), 'impact', -9, 1, 'bist-val'],
            [A('3 liradan'), 'marker', -11, 0, 'usd'], [A('1,6 milyon'), 'impact', -9, 1, 'usd-val'],
            [A('Kulağa'), 'whoosh_deep', -11, 0, 'turn'], [A('15,5 kat', A('TÜİK')), 'paper_drop', -9, 0, 'tufe'],
            [A('saydı'), 'stamp', -8, 1, 'flat'], [A('gram', A('Üçüncü')), 'whoosh_hollow', -12, 0, 'gold'],
            [A('5 milyonu'), 'impact', -8, 1, 'gold-val'], [A('3 kattan'), 'marker', -11, 0, 'real'],
            [A('Gerçekten', A('Enflasyondan')), 'success', -11, 1, 'winner'], [A('Kaydet') + .1, 'stamp', -10, 1, 'kaydet']]


def RISERS(A): return [[A('Kulağa'), 'sharp', -10], [A('Üçüncü'), 'metallic', -11]]


SCENE_HTML = r'''
  <div id="mast" style="position:absolute;left:60px;right:60px;top:236px">
    <div style="height:5px;background:#161412"></div>
    <div style="display:flex;justify-content:space-between;align-items:baseline;padding:10px 0 6px">
      <span style="font:400 66px/1 'DM Serif Display';color:#161412">Paranın Dili</span>
      <span class="mono" style="font-size:22px">EKİM 2016 → 15 EKİM 2026</span></div>
    <div style="height:2px;background:#161412"></div>
  </div>
  <section id="s1" class="scene clip">
    <div class="a h" id="s1h" style="left:60px;top:1240px;font-size:84px">100.000 ₺ → <span class="red">1,5 milyon</span></div>
    <div class="a h" id="s1h2" style="left:60px;top:1335px;font-size:84px">ama zengin <span id="s1w" style="position:relative;display:inline-block">değil?<svg id="s1c" style="position:absolute;left:-30px;top:-20px;overflow:visible" width="330" height="130" viewBox="0 0 330 130"><path d="M30,70 C20,15 160,5 270,14 C330,20 325,110 230,118 C130,126 30,118 26,64" fill="none" stroke="#c8261b" stroke-width="7" stroke-linecap="round"/></svg></span></div>
    <div class="a mono" id="s1n" style="left:60px;top:1440px;font-size:22px">BIST 100 · temettü hariç</div>
  </section>
  <section id="s2" class="scene clip">
    <div class="a lab" id="s2l" style="left:60px;top:400px">EKİM 2016 · HER BİRİ 100.000 ₺</div>
    <div class="a card" id="s2c0" style="left:60px;top:480px;width:300px;height:360px;text-align:center"><div class="mono" style="font-size:30px">BORSA</div><div class="q" style="margin-top:40px">?</div></div>
    <div class="a card" id="s2c1" style="left:390px;top:480px;width:300px;height:360px;text-align:center"><div class="mono" style="font-size:30px">DOLAR</div><div class="q" style="margin-top:40px">?</div></div>
    <div class="a card" id="s2c2" style="left:720px;top:480px;width:300px;height:360px;text-align:center"><div class="mono" style="font-size:30px">ALTIN</div><div class="q" style="margin-top:40px">?</div></div>
    <div class="a h" id="s2h" style="left:60px;top:900px;font-size:88px">Kim <span class="red">gerçekten</span> kazandı?</div>
    <div class="a mono" id="s2n" style="left:60px;top:1010px;font-size:24px">cevap videonun sonunda</div>
  </section>
  <section id="s3" class="scene clip">
    <div class="a lab" id="s3l" style="left:60px;top:400px">1. KİŞİ · BORSA (BIST 100)</div>
    <div class="a" id="s3g" style="left:60px;top:470px;width:960px;height:380px"></div>
    <div class="a mono" id="s3a" style="left:60px;top:870px">14.10.2016: 775,54*</div>
    <div class="a mono" id="s3b" style="left:600px;top:870px">15.10.2026: 12.057</div>
    <div class="a big" id="s3v" style="left:52px;top:950px;font-size:150px">100.000 ₺</div>
    <div class="a mono" id="s3n" style="left:60px;top:1120px;font-size:22px">*77.554 (2020'de iki sıfır atıldı) · temettü hariç</div>
  </section>
  <section id="s4" class="scene clip">
    <div class="a lab" id="s4l" style="left:60px;top:400px">2. KİŞİ · DOLAR</div>
    <div class="a h" id="s4a" style="left:60px;top:480px;font-size:150px">3,09</div>
    <div class="a h" id="s4ar" style="left:390px;top:500px;font-size:110px">→</div>
    <div class="a h red" id="s4b" style="left:560px;top:480px;font-size:150px">49,42</div>
    <div class="a mono" id="s4m" style="left:60px;top:650px">USD/TRY · 14.10.2016 → 15.10.2026</div>
    <div class="a" id="s4bag" style="left:60px;top:740px;width:960px;height:120px;border:5px solid #161412"><div id="s4fill" style="position:absolute;left:0;top:0;bottom:0;width:100%;background:repeating-linear-gradient(90deg,#1f7a4d 0 40px,#2a8f5d 40px 80px);transform-origin:0 50%"></div></div>
    <div class="a big" id="s4v" style="left:52px;top:900px;font-size:150px">32.362 $</div>
  </section>
  <section id="s5" class="scene clip">
    <div class="a stampbox" id="s5t" style="left:60px;top:1220px">AMA…</div>
    <div class="a h" id="s5h" style="left:60px;top:1345px;font-size:70px">bir rakam daha var</div>
  </section>
  <section id="s6" class="scene clip">
    <div class="a lab" id="s6l" style="left:60px;top:400px">100.000 ₺ BUGÜN NE OLDU · MİLYON ₺</div>
    <div class="row" id="s6r0" style="top:480px"><div class="rl">BORSA</div><div class="rb" id="s6b0" style="width:266px"></div><div class="rv" style="left:290px">1,55</div></div>
    <div class="row" id="s6r1" style="top:640px"><div class="rl">DOLAR</div><div class="rb" id="s6b1" style="width:274px"></div><div class="rv" style="left:298px">1,60</div></div>
    <div class="row" id="s6r2" style="top:800px"><div class="rl">ALTIN</div><div class="rv" style="left:0;top:40px;color:#c8261b">?</div></div>
    <div class="a" id="s6inf" style="left:325px;top:480px"><div class="infl"></div><div class="mono" style="position:absolute;left:14px;top:470px;color:#c8261b;font-size:24px;white-space:nowrap">ENFLASYON x15,5 → 1,55</div></div>
    <div class="a stampbox" id="s6s" style="left:280px;top:1080px;transform:rotate(-4deg)">YERİNDE SAYDI</div>
    <div class="a mono" id="s6n" style="left:60px;top:1210px;font-size:22px">TÜİK TÜFE · Eylül 2016 → Eylül 2026</div>
  </section>
  <section id="s7" class="scene clip">
    <div class="a lab" id="s7l" style="left:60px;top:400px">3. KİŞİ · GRAM ALTIN · MİLYON ₺</div>
    <div class="row" id="s7r0" style="top:480px"><div class="rl">BORSA</div><div class="rb" style="width:266px"></div><div class="rv" style="left:290px">1,55</div></div>
    <div class="row" id="s7r1" style="top:640px"><div class="rl">DOLAR</div><div class="rb" style="width:274px"></div><div class="rv" style="left:298px">1,60</div></div>
    <div class="row" id="s7r2" style="top:800px"><div class="rl">ALTIN</div><div class="rb gold-b" id="s7b2" style="width:760px"></div><div class="rv" id="s7v2" style="left:780px">5,25</div></div>
    <div class="a h" id="s7p" style="left:60px;top:1000px;font-size:96px">125 ₺ → <span class="red">6.600 ₺</span></div>
    <div class="a mono" id="s7n" style="left:60px;top:1110px;font-size:22px">gram · Ekim 2016 (AA Finans) → 15.10.2026 Kapalıçarşı</div>
  </section>
  <section id="s8" class="scene clip">
    <div class="a lab" id="s8l" style="left:60px;top:400px">ENFLASYONDAN ARINDIRILMIŞ · ALIM GÜCÜ</div>
    <div class="row" id="s8r0" style="top:480px"><div class="rl">BORSA</div><div class="rb" style="width:226px;background:#8a8580"></div><div class="rv" style="left:250px">x1,00</div></div>
    <div class="row" id="s8r1" style="top:640px"><div class="rl">DOLAR</div><div class="rb" style="width:233px;background:#8a8580"></div><div class="rv" style="left:257px">x1,03</div></div>
    <div class="row" id="s8r2" style="top:800px"><div class="rl">ALTIN</div><div class="rb gold-b" id="s8b2" style="width:766px"></div><div class="rv" style="left:786px">x3,4</div></div>
    <div class="a mono" id="s8n" style="left:60px;top:990px;font-size:24px">çizgi = 100.000 ₺'nin 2016'daki alım gücü</div>
    <div class="a" id="s8base" style="left:286px;top:450px;width:0;height:500px;border-left:6px dashed #c8261b"></div>
  </section>
  <section id="s9" class="scene clip">
    <div class="a lab" id="s9l" style="left:60px;top:400px">10 YILIN SONUCU</div>
    <div class="a big" id="s9a" style="left:52px;top:470px;font-size:220px">ALTIN</div>
    <div class="a h" id="s9b" style="left:60px;top:700px;font-size:96px">x52,5 <span class="mono" style="font-size:30px">nominal</span></div>
    <div class="a h red" id="s9c" style="left:60px;top:820px;font-size:96px">x3,4 <span class="mono" style="font-size:30px;color:#c8261b">reel</span></div>
    <div class="a card" id="s9d" style="left:60px;top:960px;width:960px"><span class="mono" style="font-size:26px;color:#161412;white-space:normal">borsa x15,5 · dolar x16,0 · enflasyon x15,5 — işlem maliyeti, vergi, makas yok</span></div>
  </section>
  <section id="s10" class="scene clip">
    <div class="a h" id="s10a" style="left:60px;top:1240px;font-size:76px">Geçmiş getiri</div>
    <div class="a h red" id="s10b" style="left:60px;top:1330px;font-size:76px">garanti değildir.</div>
  </section>
  <section id="s11" class="scene clip">
    <div class="a h red" id="s11t" style="left:0;right:0;top:1262px;text-align:center;font-size:110px"><span style="border:8px solid #c8261b;padding:0 30px;border-radius:12px">KAYDET</span></div>
    <div class="a h" id="s11b" style="left:0;right:0;top:1405px;text-align:center;font-size:62px">1,5 milyon ≠ zengin</div>
  </section>
'''
SCENE_JS = r'''
const CAPY={s1:60,s2:0,s3:0,s4:0,s5:60,s6:0,s7:0,s8:0,s9:0,s10:60,s11:80};
tl.set('#caps',{y:CAPY.s1},0); SC.slice(1).forEach(([id,a])=>tl.to('#caps',{y:CAPY[id],duration:.01},a));
inn('#mast',.05,{y:-20});
// S1 hook
inn('#s1h',.4); inn('#s1h2',4.3); inn('#s1n',1.0,{y:10});
(function(){const p=document.querySelector('#s1c path');const L=p.getTotalLength();p.style.strokeDasharray=L;tl.fromTo(p,{strokeDashoffset:L},{strokeDashoffset:0,duration:.5,ease:'power2.inOut'},5.2);})();
// S2 three cards
const s2=st('s2'), d2=st('s3')-s2; inn('#s2l',s2+.4); [0,1,2].forEach(i=>inn('#s2c'+i,s2+.5+i*.25,{y:60})); inn('#s2h',s2+d2*.5); inn('#s2n',s2+d2*.62,{y:10});
// S3 BIST line chart
const s3=st('s3'), d3=st('s4')-s3; inn('#s3l',s3+.4);
(function(){const g=document.querySelector('#s3g');
 g.innerHTML=`<div style="position:absolute;left:0;right:0;bottom:0;height:3px;background:#161412"></div>`+
 `<div id="s3c0" style="position:absolute;left:60px;bottom:3px;width:220px;height:${(775/12057*360).toFixed(0)}px;background:#161412;transform-origin:50% 100%"></div>`+
 `<div id="s3c1" style="position:absolute;left:600px;bottom:3px;width:220px;height:360px;background:#c8261b;transform-origin:50% 100%"></div>`+
 `<div class="h" style="position:absolute;left:300px;top:150px;font-size:80px;color:#c8261b">x15,5</div>`;})();
inn('#s3g',s3+.45,{y:0}); tl.fromTo('#s3c0',{scaleY:0},{scaleY:1,duration:.4,ease:'power3.out'},s3+.5); tl.fromTo('#s3c1',{scaleY:0},{scaleY:1,duration:1.0,ease:'power3.out'},s3+1.6);
inn('#s3a',s3+.6,{y:10}); inn('#s3b',s3+2.0,{y:10}); inn('#s3v',s3+d3*.55); count('#s3v',100000,1554700,s3+d3*.6,1.2,v=>fmt(v)+' ₺'); inn('#s3n',s3+d3*.62,{y:10});
// S4 dollar
const s4=st('s4'), d4=st('s5')-s4; inn('#s4l',s4+.4); inn('#s4a',s4+.5); inn('#s4ar',s4+.9,{y:0}); slam('#s4b',s4+d4*.35); inn('#s4m',s4+d4*.38,{y:10});
inn('#s4bag',s4+.6,{y:0}); tl.fromTo('#s4fill',{scaleX:0},{scaleX:1,duration:.7,ease:'power3.out'},s4+.8); inn('#s4v',s4+.7);
count('#s4v',32362,1599350,s4+d4*.62,1.0,v=>fmt(v)+' ₺');
// S5 turn (avatar)
const s5=st('s5'); slam('#s5t',s5+.4); inn('#s5h',s5+.9);
// S6 race 1 + inflation line
const s6=st('s6'), d6=st('s7')-s6; inn('#s6l',s6+.4); inn('#s6r0',s6+.5,{y:20}); inn('#s6r1',s6+.6,{y:20}); inn('#s6r2',s6+.7,{y:20});
tl.fromTo('#s6b0',{scaleX:0},{scaleX:1,duration:.6,ease:'power3.out'},s6+.6); tl.fromTo('#s6b1',{scaleX:0},{scaleX:1,duration:.6,ease:'power3.out'},s6+.7);
tl.fromTo('#s6inf',{opacity:0,scaleY:0,transformOrigin:'50% 0%'},{opacity:1,scaleY:1,duration:.6,ease:'power2.out'},s6+d6*.42); inn('#s6n',s6+d6*.45,{y:10});
slam('#s6s',s6+d6*.8);
// S7 gold shoots
const s7=st('s7'), d7=st('s8')-s7; inn('#s7l',s7+.4); inn('#s7r0',s7+.4,{y:0}); inn('#s7r1',s7+.4,{y:0}); inn('#s7r2',s7+.45,{y:0});
tl.fromTo('#s7b2',{scaleX:0},{scaleX:1,duration:2.2,ease:'power2.in'},s7+d7*.3); count('#s7v2',0,5.25,s7+d7*.3,2.2,v=>v.toFixed(2).replace('.',','));
inn('#s7p',s7+d7*.3); inn('#s7n',s7+d7*.35,{y:10});
// S8 real
const s8=st('s8'); inn('#s8l',s8+.4); inn('#s8base',s8+.45,{y:0}); [0,1,2].forEach(i=>inn('#s8r'+i,s8+.55+i*.25,{y:20}));
tl.fromTo('#s8b2',{scaleX:0},{scaleX:1,duration:.9,ease:'power3.out'},s8+1.2); inn('#s8n',s8+1.4,{y:10});
// S9 winner
const s9=st('s9'), d9=st('s10')-s9; inn('#s9l',s9+.4); slam('#s9a',s9+.5); inn('#s9b',s9+1.1); inn('#s9c',s9+1.5); inn('#s9d',s9+2.0,{y:30});
// S10 disclaimer
const s10=st('s10'); inn('#s10a',s10+.4); inn('#s10b',s10+.7);
// S11 CTA + loop
const s11=st('s11'); slam('#s11t',s11+.3); inn('#s11b',s11+1.4);
'''
