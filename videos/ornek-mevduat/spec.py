CSS_FILE = 'gazete.css.html'
import os
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [
    (N('yüz', 'bin', 'lira,'), '100 bin lira,'), (N('yüz', 'bin', 'lira'), '100 bin lira'), (N('yirmi', 'üç', 'bin', 'lira'), '23 bin lira'),
    (N('yüzde', 'yirmi', 'dokuz', 'virgül', 'yetmiş', 'üç'), '%29,73'), (N('yüzde', 'kırk', 'dört', 'buçuğa'), "%44,5'e"), (N('yüzde', 'kırk', 'dört'), '%44'),
    (N('yüzde', 'on', 'yedi', 'buçuk'), '%17,5'), (N('yüzde', 'otuz', 'altı'), '%36'), (N('altı', 'buçuk', 'puan'), '6,5 puan'),
    (N('otuz', 'iki', 'günlük'), '32 günlük'), (N('yüzde', 'ikiden'), "%2'den"), (N('bir', 'milyon', 'liranın'), '1 milyon liranın'),
    (N('üç', 'yüz', 'yirmi', 'beş', 'bini'), '325 bini'), (N('üç', 'aya'), '3 aya'),
]
EM = {'duruyor', 'vadesiz', 'stopaj', 'tuzak', 'vitrindeki', 'net', 'kaydet', 'durur', 'faiz', 'işletilmeyen'}
RED = {'23 bin lira', '%17,5', 'duruyor', 'durur', '325 bini', 'tuzak'}
# windows keep the source's 740:1040 portrait ratio -> full head (hair + chin) always visible
FRONT = [250, 375, 580, 815, 6]; INSET = [700, 400, 320, 450, 6]
AV = {'s1': FRONT, 's2': None, 's3': None, 's4': None, 's5': INSET, 's6': None, 's7': None, 's8': [720, 600, 300, 422, 6], 's9': FRONT, 's10': FRONT}
EXTRA_CSS = '<style>#s2,#s3,#s4,#s6,#s7,#s8{transform:translateY(170px)}</style>'
def scenes(A):
    t2 = A('Çünkü'); t3 = A('Eylülde'); t4 = A('Ama', t3); t5 = A('Yani'); t6 = A('Fakat'); t7 = A('İkincisi'); t8 = A('O', t7)
    t9 = A('Kaydet'); t10 = A('Yoksa', t9)
    b = lambda t: round(t - .1, 3)
    return [('s1', 0, b(t2)), ('s2', b(t2), b(t3)), ('s3', b(t3), b(t4)), ('s4', b(t4), b(t5)), ('s5', b(t5), b(t6)), ('s6', b(t6), b(t7)),
            ('s7', b(t7), b(t8)), ('s8', b(t8), b(t9)), ('s9', b(t9), b(t10)), ('s10', b(t10), DUR)]
def SFX(A):
    return [[A('duruyor'), 'stamp', -9, 1, 'hook'], [A('23 bin lira'), 'impact', -8, 1, '-23'], [A('%29,73'), 'marker', -11, 0, 'bar1'],
            [A('%44'), 'marker', -11, 0, 'bar2'], [A('%17,5'), 'paper_drop', -9, 0, 'cut'], [A('6,5 puan'), 'impact', -8, 1, '+6.5'],
            [A('Birincisi'), 'whoosh_hollow', -12, 0, 't1'], [A('İkincisi'), 'whoosh_hollow', -12, 0, 't2'], [A('325 bini'), 'stamp', -8, 1, '325'],
            [A('Kaydet') + .1, 'success', -10, 1, 'kaydet'], [A('durur.', A('Kaydet')), 'impact', -8, 1, 'loop']]
def RISERS(A): return [[A('Fakat'), 'sharp', -9]]
SCENE_HTML = r'''
  <div id="mast" style="position:absolute;left:60px;right:60px;top:236px">
    <div style="height:5px;background:#161412"></div>
    <div style="display:flex;justify-content:space-between;align-items:baseline;padding:10px 0 6px">
      <span style="font:400 66px/1 'DM Serif Display';color:#161412">Paranın Dili</span>
      <span class="mono" style="font-size:22px">EKİM 2026 · MEVDUAT</span></div>
    <div style="height:2px;background:#161412"></div>
  </div>
  <section id="s1" class="scene clip">
    <div class="a h" id="s1h" style="left:60px;top:1300px;font-size:92px">Paran faiz mi alıyor,</div>
    <div class="a h" id="s1h2" style="left:60px;top:1395px;font-size:92px"><span id="s1w" style="position:relative;display:inline-block">duruyor mu?<svg id="s1c" style="position:absolute;left:-26px;top:-18px;overflow:visible" width="480" height="130" viewBox="0 0 480 130"><path d="M30,70 C20,15 230,5 400,14 C475,20 470,110 330,118 C180,126 30,118 26,64" fill="none" stroke="#c8261b" stroke-width="7" stroke-linecap="round"/></svg></span></div>
  </section>
  <section id="s2" class="scene clip">
    <div class="a lab" id="s2l" style="left:60px;top:400px">VADESİZ HESAP · 1 YIL · %29,73 ENFLASYON</div>
    <div class="a mono" id="s2m" style="left:60px;top:470px">alım gücü</div>
    <div class="a big" id="s2v" style="left:52px;top:510px;font-size:190px">100.000 ₺</div>
    <div class="a h red" id="s2d" style="left:60px;top:740px;font-size:110px;border:7px solid #c8261b;padding:4px 26px;border-radius:10px">−23 BİN ₺</div>
  </section>
  <section id="s3" class="scene clip">
    <div class="a lab" id="s3l" style="left:60px;top:400px">YILLIK · EYLÜL 2026</div>
    <div class="a" id="s3b1" style="left:120px;top:470px;width:330px;height:480px"><div id="s3f1" style="position:absolute;left:0;right:0;bottom:0;height:59%;background:repeating-linear-gradient(-45deg,#161412 0 5px,transparent 5px 12px);border:5px solid #161412;transform-origin:50% 100%"></div><div class="h" style="position:absolute;left:0;right:0;bottom:62%;text-align:center;font-size:84px">%29,73</div></div>
    <div class="a" id="s3b2" style="left:600px;top:470px;width:330px;height:480px"><div id="s3f2" style="position:absolute;left:0;right:0;bottom:0;height:88%;background:#161412;transform-origin:50% 100%"></div><div class="h" id="s3t2" style="position:absolute;left:0;right:0;bottom:90%;text-align:center;font-size:84px">%44</div></div>
    <div class="a mono" id="s3c1" style="left:120px;top:955px;width:330px;text-align:center">ENFLASYON</div>
    <div class="a mono" id="s3c2" style="left:600px;top:955px;width:330px;text-align:center">MEVDUAT (3 AY)</div>
  </section>
  <section id="s4" class="scene clip">
    <div class="a lab" id="s4l" style="left:60px;top:400px">MEVDUAT FAİZİ · STOPAJ SONRASI</div>
    <div class="a" id="s4bar" style="left:60px;top:500px;width:960px;height:110px;border:5px solid #161412">
      <div id="s4net" style="position:absolute;left:0;top:0;bottom:0;width:82.5%;background:#161412"></div>
      <div id="s4tax" style="position:absolute;right:0;top:0;bottom:0;width:17.5%;background:repeating-linear-gradient(-45deg,#c8261b 0 5px,transparent 5px 12px)"></div>
    </div>
    <div class="a h" id="s4a" style="left:60px;top:640px;font-size:84px">%44</div>
    <div class="a h red" id="s4b" style="left:520px;top:650px;font-size:72px">−%17,5 stopaj</div>
    <div class="a big" id="s4c" style="left:52px;top:760px;font-size:170px">≈ %36</div>
  </section>
  <section id="s5" class="scene clip">
    <div class="a lab" id="s5l" style="left:60px;top:400px">NET GETİRİ − ENFLASYON</div>
    <div class="a big" id="s5v" style="left:52px;top:440px;font-size:230px">+6,5</div>
    <div class="a h" id="s5u" style="left:60px;top:720px;font-size:84px">puan</div>
    <div class="a" id="s5ruler" style="left:60px;top:880px;width:960px;height:120px"></div>
    <div class="a mono" id="s5n" style="left:60px;top:1040px">%36,3 net · %29,73 enflasyon</div>
  </section>
  <section id="s6" class="scene clip">
    <div class="a lab" id="s6l" style="left:60px;top:400px">TUZAK 1</div>
    <div class="a h" id="s6h" style="left:60px;top:440px;font-size:100px">Vitrindeki oran</div>
    <div class="a" id="s6track" style="left:60px;top:640px;width:960px;height:26px;background:rgba(22,20,18,.15)"><div id="s6fill" style="position:absolute;left:0;top:0;bottom:0;width:100%;background:linear-gradient(90deg,#161412,#c8261b);transform-origin:0 50%"></div></div>
    <div class="a h" id="s6a" style="left:60px;top:690px;font-size:76px">%2</div>
    <div class="a h red" id="s6b" style="left:780px;top:690px;font-size:76px">%44,5</div>
    <div class="a card" id="s6c" style="left:60px;top:820px;width:960px"><span class="mono" style="font-size:30px;color:#161412;white-space:normal">32 gün vadede aralık · en yüksek oran her tutara uygulanmıyor</span></div>
  </section>
  <section id="s7" class="scene clip">
    <div class="a lab" id="s7l" style="left:60px;top:400px">TUZAK 2</div>
    <div class="a h" id="s7h" style="left:60px;top:440px;font-size:100px">Faizsiz bakiye</div>
    <div class="a" id="s7bar" style="left:60px;top:640px;width:960px;height:140px;border:5px solid #161412">
      <div id="s7no" style="position:absolute;left:0;top:0;bottom:0;width:32.5%;background:repeating-linear-gradient(-45deg,#c8261b 0 6px,transparent 6px 14px);display:grid;place-items:center"><span class="h red" style="font-size:44px;background:#f2ede2;padding:2px 10px">FAİZ YOK</span></div>
      <div id="s7yes" style="position:absolute;right:0;top:0;bottom:0;width:67.5%;background:#161412;display:grid;place-items:center"><span class="h" style="font-size:44px;color:#f2ede2">faiz işler</span></div>
    </div>
    <div class="a h red" id="s7a" style="left:60px;top:800px;font-size:84px">325.000 ₺</div>
    <div class="a mono" id="s7b" style="left:500px;top:830px">/ 1.000.000 ₺ bakiye</div>
  </section>
  <section id="s8" class="scene clip">
    <div class="a lab" id="s8l" style="left:60px;top:400px">BANKAYA SORMADAN ÖNCE</div>
    <div class="a" id="s8r0" style="left:60px;top:470px;width:620px;display:flex;gap:22px;align-items:center"><div class="tick" id="s8k0"></div><div class="h" style="font-size:58px;white-space:normal;line-height:1.02">Oran değil, net getiri</div></div>
    <div class="a" id="s8r1" style="left:60px;top:640px;width:620px;display:flex;gap:22px;align-items:center"><div class="tick" id="s8k1"></div><div class="h" style="font-size:58px;white-space:normal;line-height:1.02">Faizsiz tutarı sor</div></div>
    <div class="a" id="s8r2" style="left:60px;top:810px;width:620px;display:flex;gap:22px;align-items:center"><div class="tick" id="s8k2"></div><div class="h" style="font-size:58px;white-space:normal;line-height:1.02">Yenilenen oranı kontrol et</div></div>
  </section>
  <section id="s9" class="scene clip">
    <div class="a h red" id="s9t" style="left:0;right:0;top:1330px;text-align:center;font-size:130px"><span style="border:8px solid #c8261b;padding:0 30px;border-radius:12px">KAYDET</span></div>
  </section>
  <section id="s10" class="scene clip">
    <div class="a h" id="s10a" style="left:60px;top:1300px;font-size:92px">Yoksa paran</div>
    <div class="a h red" id="s10b" style="left:60px;top:1395px;font-size:92px">sadece durur.</div>
  </section>
'''
SCENE_JS = r'''
// captions position per layout: front page -> 1520, bottom layout -> between stage and avatar
const CAPY={s1:20,s2:20,s3:20,s4:20,s5:20,s6:20,s7:20,s8:20,s9:20,s10:20};
tl.set('#caps',{y:CAPY.s1},0); SC.slice(1).forEach(([id,a])=>tl.to('#caps',{y:CAPY[id],duration:.01},a));
inn('#mast',.05,{y:-20});
// S1 front page
inn('#s1h',.3); inn('#s1h2',.5); (function(){const p=document.querySelector('#s1c path');const L=p.getTotalLength();p.style.strokeDasharray=L;tl.fromTo(p,{strokeDashoffset:L},{strokeDashoffset:0,duration:.5,ease:'power2.inOut'},1.6);})();
// S2
const s2=st('s2'), d2=st('s3')-s2; inn('#s2l',s2+.45); inn('#s2m',s2+.55); inn('#s2v',s2+.6); count('#s2v',100000,77083,s2+d2*.55,1.2,v=>fmt(v)+' ₺'); slam('#s2d',s2+d2*.72);
// S3 bars
const s3=st('s3'), d3=st('s4')-s3; inn('#s3l',s3+.4); inn('#s3b1',s3+.45,{y:0}); inn('#s3c1',s3+.5);
tl.fromTo('#s3f1',{scaleY:0},{scaleY:1,duration:.6,ease:'power3.out'},s3+.5); inn('#s3b2',s3+d3*.5,{y:0}); inn('#s3c2',s3+d3*.5);
tl.fromTo('#s3f2',{scaleY:0},{scaleY:1,duration:.6,ease:'power3.out'},s3+d3*.52);
// S4 stopaj cut
const s4=st('s4'), d4=st('s5')-s4; inn('#s4l',s4+.4); inn('#s4bar',s4+.45,{y:0}); inn('#s4a',s4+.5);
tl.fromTo('#s4tax',{opacity:0},{opacity:1,duration:.3},s4+.9); inn('#s4b',s4+.95); tl.to('#s4tax',{x:40,opacity:.25,duration:.5,ease:'power2.in'},s4+d4*.55); slam('#s4c',s4+d4*.62);
// S5 +6.5
const s5=st('s5'), d5=st('s6')-s5; inn('#s5l',s5+.45); slam('#s5v',s5+.6); inn('#s5u',s5+.8); inn('#s5n',s5+1.0,{y:10});
(function(){const r=document.querySelector('#s5ruler');const X=v=>(v-20)/(40-20)*960;
 r.innerHTML=`<div style="position:absolute;left:0;right:0;top:56px;height:4px;background:#161412"></div>`+[20,25,30,35,40].map(v=>`<div style="position:absolute;left:${X(v)-1}px;top:44px;width:3px;height:28px;background:#161412"></div><div class="mono" style="position:absolute;left:${X(v)-30}px;top:80px;width:60px;text-align:center;font-size:22px">%${v}</div>`).join('')+
 `<div id="s5gap" style="position:absolute;left:${X(29.73)}px;width:${X(36.3)-X(29.73)}px;top:36px;height:44px;background:#c8261b;transform-origin:0 50%"></div>`;
 tl.fromTo('#s5ruler',{opacity:0},{opacity:1,duration:.3},s5+1.0); tl.fromTo('#s5gap',{scaleX:0},{scaleX:1,duration:.6,ease:'power3.out'},s5+1.3);})();
// S6 tuzak 1
const s6=st('s6'), d6=st('s7')-s6; inn('#s6l',s6+.45); inn('#s6h',s6+.55); inn('#s6track',s6+d6*.3,{y:0});
tl.fromTo('#s6fill',{scaleX:0},{scaleX:1,duration:1.0,ease:'power2.inOut'},s6+d6*.32); inn('#s6a',s6+d6*.32); inn('#s6b',s6+d6*.45); inn('#s6c',s6+d6*.7,{y:30});
// S7 tuzak 2
const s7=st('s7'), d7=st('s8')-s7; inn('#s7l',s7+.45); inn('#s7h',s7+.55); inn('#s7bar',s7+d7*.35,{y:0}); tl.fromTo('#s7no',{scaleX:0,transformOrigin:'0 50%'},{scaleX:1,duration:.5,ease:'power3.out'},s7+d7*.6); slam('#s7a',s7+d7*.62); inn('#s7b',s7+d7*.66,{y:10});
// S8 checklist
const s8=st('s8'), d8=st('s9')-s8; inn('#s8l',s8+.45);
[[0,.05],[1,.42],[2,.7]].forEach(([i,f])=>{inn('#s8r'+i,s8+.45+d8*f,{y:24}); tl.to('#s8k'+i,{backgroundColor:'#161412',duration:.15},s8+.85+d8*f);});
// S9 CTA
const s9=st('s9'); slam('#s9t',s9+.3);
// S10 loop
const s10=st('s10'); inn('#s10a',s10+.3); inn('#s10b',s10+.6,{s:1.05});
'''
