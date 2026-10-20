CSS_FILE = 'gazete.css.html'
import os
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [
    (N('beş', 'bin', 'ile', 'yirmi', 'yedi', 'bin', 'lira'), '5 bin ile 27 bin lira'), (N('otuz', 'beş', 'bine'), '35 bine'),
    (N('doksan', 'bin', 'liranın'), '90 bin liranın'), (N('doksan', 'binlik'), '90 binlik'), (N('doksan', 'bin'), '90 bin'),
    (N('üç', 'yıl'), '3 yıl'), (N('iki', 'şey'), '2 şey'), (N('iki', 'şeyi'), '2 şeyi'),
]
EM = {'nakit', 'koşulsuz', 'koşullu', 'taahhüt', 'kredi', 'kaydet', 'iade', 'pazarlık', 'tarihi'}
RED = {'kredi', 'değil', 'iade', 'karşılaştırılamaz'}
# 740:1040 portrait windows; seated look: head sits in the upper half of the frame -> full head + chin visible
FRONT = [250, 375, 580, 815, 6]
MID = [300, 400, 480, 675, 6]
AV = {'s1': FRONT, 's2': None, 's3': None, 's4': MID, 's5': None, 's6': None, 's7': None, 's8': None, 's9': FRONT}
EXTRA_CSS = '''<style>
.seg{position:absolute;top:0;bottom:0;display:grid;place-items:center;font:700 26px 'IBM Plex Mono';color:#f2ede2;transform-origin:0 50%;overflow:hidden;white-space:nowrap}
.cond{display:flex;gap:22px;align-items:center}
.stampbox{border:8px solid #c8261b;color:#c8261b;padding:6px 30px;border-radius:10px;font:400 86px/1 'DM Serif Display';white-space:nowrap}
</style>'''


def scenes(A):
    b = lambda t: round(t - .1, 3)
    t2 = A('Emekli'); t3 = A('Ekim'); t4 = A('Ama'); t5 = A('35 bine'); t6 = A('90 binlik', t5); t7 = A('Bir de', t6)
    t8 = A('Yani', A('dolduysa')); t9 = A('Kaydet')
    return [('s1', 0, b(t2)), ('s2', b(t2), b(t3)), ('s3', b(t3), b(t4)), ('s4', b(t4), b(t5)), ('s5', b(t5), b(t6)),
            ('s6', b(t6), b(t7)), ('s7', b(t7), b(t8)), ('s8', b(t8), b(t9)), ('s9', b(t9), DUR)]


def SFX(A):
    return [[A('kredi'), 'stamp', -9, 1, 'hook'], [A('3 yıl'), 'marker', -11, 0, '3y'], [A('5 bin ile 27 bin lira'), 'impact', -9, 1, 'range'],
            [A('Ama'), 'whoosh_deep', -11, 0, 'turn'], [A('koşullu'), 'stamp', -9, 1, 'kosul'], [A('otomatik'), 'ui_click', -12, 0, 'c1'],
            [A('kart'), 'ui_click', -12, 0, 'c2'], [A('bazen'), 'ui_click', -12, 0, 'c3'], [A('faizsiz'), 'paper_drop', -10, 0, 'pkg'],
            [A('karşılaştırılamaz'), 'stamp', -9, 1, 'nocomp'], [A('taşırsan'), 'whoosh_hollow', -12, 0, 'move'], [A('iade'), 'impact', -9, 1, 'iade'],
            [A('koşulsuz', A('bakacağın')), 'marker', -11, 0, 'k1'], [A('taahhüt', A('bakacağın')), 'marker', -11, 0, 'k2'],
            [A('Kaydet') + .1, 'stamp', -10, 1, 'kaydet']]


def RISERS(A): return [[A('Ama'), 'sharp', -10], [A('Bir de'), 'metallic', -11]]


SCENE_HTML = r'''
  <div id="mast" style="position:absolute;left:60px;right:60px;top:236px">
    <div style="height:5px;background:#161412"></div>
    <div style="display:flex;justify-content:space-between;align-items:baseline;padding:10px 0 6px">
      <span style="font:400 66px/1 'DM Serif Display';color:#161412">Paranın Dili</span>
      <span class="mono" style="font-size:22px">EKİM 2026 İTİBARIYLA · EMEKLİ</span></div>
    <div style="height:2px;background:#161412"></div>
  </div>
  <section id="s1" class="scene clip">
    <div class="a h" id="s1h" style="left:60px;top:1240px;font-size:84px">"90.000 ₺ promosyon"</div>
    <div class="a h" id="s1h2" style="left:60px;top:1335px;font-size:84px">çoğu <span id="s1w" style="position:relative;display:inline-block" class="red">nakit değil<svg id="s1c" style="position:absolute;left:-30px;top:-20px;overflow:visible" width="460" height="130" viewBox="0 0 460 130"><path d="M30,70 C20,15 230,5 390,14 C460,20 455,110 320,118 C170,126 30,118 26,64" fill="none" stroke="#c8261b" stroke-width="7" stroke-linecap="round"/></svg></span></div>
  </section>
  <section id="s2" class="scene clip">
    <div class="a lab" id="s2l" style="left:60px;top:400px">EMEKLİ PROMOSYONU NEDİR?</div>
    <div class="a h" id="s2h" style="left:60px;top:460px;font-size:96px">Maaş 3 yıl aynı bankada</div>
    <div class="a h red" id="s2h2" style="left:60px;top:560px;font-size:96px">= tek seferlik ödeme</div>
    <div class="a" id="s2t" style="left:60px;top:740px;width:960px;height:100px;border:5px solid #161412">
      <div id="s2f" style="position:absolute;left:0;top:0;bottom:0;width:100%;background:repeating-linear-gradient(90deg,#161412 0 318px,#f2ede2 318px 322px);transform-origin:0 50%"></div></div>
    <div class="a mono" id="s2y0" style="left:60px;top:860px">1. YIL</div><div class="a mono" id="s2y1" style="left:380px;top:860px">2. YIL</div><div class="a mono" id="s2y2" style="left:700px;top:860px">3. YIL</div>
  </section>
  <section id="s3" class="scene clip">
    <div class="a lab" id="s3l" style="left:60px;top:400px">KOŞULSUZ NAKİT · MAAŞ DİLİMİNE GÖRE</div>
    <div class="a big" id="s3a" style="left:52px;top:470px;font-size:170px">5.000 ₺</div>
    <div class="a h" id="s3d" style="left:60px;top:660px;font-size:90px">ile</div>
    <div class="a big red" id="s3b" style="left:52px;top:740px;font-size:170px">27.000 ₺</div>
    <div class="a" id="s3r" style="left:60px;top:960px;width:960px;height:40px;background:rgba(22,20,18,.12)"><div id="s3rf" style="position:absolute;left:0;top:0;bottom:0;width:100%;background:linear-gradient(90deg,#161412,#c8261b);transform-origin:0 50%"></div></div>
    <div class="a mono" id="s3n" style="left:60px;top:1030px;font-size:22px">13 banka · Uzmanpara, 10 Ekim 2026 · kampanyalar değişebilir</div>
  </section>
  <section id="s4" class="scene clip">
    <div class="a stampbox" id="s4t" style="left:60px;top:1220px">AMA…</div>
    <div class="a h" id="s4h" style="left:60px;top:1340px;font-size:66px">reklamdaki rakam başka</div>
  </section>
  <section id="s5" class="scene clip">
    <div class="a lab" id="s5l" style="left:60px;top:400px">"35.000 ₺'YE VARAN" = KOŞULLU</div>
    <div class="a cond" id="s5r0" style="left:60px;top:480px"><div class="tick" id="s5k0"></div><div class="h" style="font-size:66px">Otomatik fatura talimatı</div></div>
    <div class="a cond" id="s5r1" style="left:60px;top:600px"><div class="tick" id="s5k1"></div><div class="h" style="font-size:66px">Kart harcaması</div></div>
    <div class="a cond" id="s5r2" style="left:60px;top:720px"><div class="tick" id="s5k2"></div><div class="h" style="font-size:66px">Kredi / ek hesap / sigorta</div></div>
    <div class="a card" id="s5c" style="left:60px;top:880px;width:960px"><span class="mono" style="font-size:28px;color:#161412;white-space:normal">şartı tutmazsan ek tutar gelmez · koşulsuz kısım: 5.000–27.000 ₺</span></div>
  </section>
  <section id="s6" class="scene clip">
    <div class="a lab" id="s6l" style="left:60px;top:400px">"90.000 ₺'YE VARAN" PAKET NEYDEN OLUŞUYOR?</div>
    <div class="a" id="s6bar" style="left:60px;top:470px;width:960px;height:120px;border:5px solid #161412">
      <div class="seg" id="s6a" style="left:0;width:13.3%;background:#1f7a4d">NAKİT</div>
      <div class="seg" id="s6b" style="left:13.3%;width:44.4%;background:#c8261b">FAİZSİZ KREDİ</div>
      <div class="seg" id="s6c" style="left:57.7%;width:27.8%;background:#7a1610">NAKİT AVANS</div>
      <div class="seg" id="s6d" style="left:85.5%;width:14.5%;background:#8a8580">PUAN</div></div>
    <div class="a h" id="s6v0" style="left:60px;top:630px;font-size:70px"><span class="green">≤12.000 ₺</span> nakit</div>
    <div class="a h" id="s6v1" style="left:60px;top:720px;font-size:70px"><span class="red">40.000 ₺</span> 12 ay faizsiz kredi</div>
    <div class="a h" id="s6v2" style="left:60px;top:810px;font-size:70px"><span class="red">25.000 ₺</span> nakit avans</div>
    <div class="a h" id="s6v3" style="left:60px;top:900px;font-size:70px">+ aylık kart puanı</div>
    <div class="a stampbox" id="s6s" style="left:240px;top:1020px;transform:rotate(-3deg);font-size:64px">KARŞILAŞTIRILAMAZ</div>
  </section>
  <section id="s7" class="scene clip">
    <div class="a lab" id="s7l" style="left:60px;top:400px">TAAHHÜT · 3 YIL</div>
    <div class="a" id="s7t" style="left:60px;top:470px;width:960px;height:100px;border:5px solid #161412">
      <div id="s7u" style="position:absolute;left:0;top:0;bottom:0;width:33.3%;background:#161412;transform-origin:0 50%"></div>
      <div id="s7r" style="position:absolute;left:33.3%;top:0;bottom:0;width:66.7%;background:repeating-linear-gradient(-45deg,#c8261b 0 7px,transparent 7px 15px);transform-origin:0 50%"></div></div>
    <div class="a mono" id="s7m0" style="left:60px;top:590px">1 yıl sonra taşıdın →</div>
    <div class="a h red" id="s7m1" style="left:60px;top:640px;font-size:76px">kalan 2 yılın payı iade</div>
    <div class="a mono" id="s7m2" style="left:60px;top:740px;font-size:24px">örnek: 12.000 ₺ aldın → ≈8.000 ₺ iade (kalan süreye oranla)</div>
    <div class="a card" id="s7c" style="left:60px;top:850px;width:960px"><span class="h" style="font-size:62px">3 yıl doldu mu? → <span class="green">yeni pazarlık</span></span></div>
  </section>
  <section id="s8" class="scene clip">
    <div class="a lab" id="s8l" style="left:60px;top:400px">BAKACAĞIN 2 ŞEY</div>
    <div class="a cond" id="s8r0" style="left:60px;top:480px"><div class="tick" id="s8k0"></div><div class="h" style="font-size:80px">Koşulsuz nakit</div></div>
    <div class="a cond" id="s8r1" style="left:60px;top:620px"><div class="tick" id="s8k1"></div><div class="h" style="font-size:80px">Taahhüt bitiş tarihi</div></div>
    <div class="a mono" id="s8m" style="left:60px;top:780px;font-size:24px">reklamdaki "varan" tutar değil · banka önerisi değildir</div>
  </section>
  <section id="s9" class="scene clip">
    <div class="a h red" id="s9t" style="left:0;right:0;top:1262px;text-align:center;font-size:110px"><span style="border:8px solid #c8261b;padding:0 30px;border-radius:12px">KAYDET</span></div>
    <div class="a h" id="s9b" style="left:0;right:0;top:1405px;text-align:center;font-size:58px">reklamdaki 90 bin ≠ cebine giren</div>
  </section>
'''
SCENE_JS = r'''
const CAPY={s1:60,s2:0,s3:0,s4:60,s5:0,s6:0,s7:0,s8:0,s9:80};
tl.set('#caps',{y:CAPY.s1},0); SC.slice(1).forEach(([id,a])=>tl.to('#caps',{y:CAPY[id],duration:.01},a));
inn('#mast',.05,{y:-20});
// S1
inn('#s1h',.4); inn('#s1h2',3.3);
(function(){const p=document.querySelector('#s1c path');const L=p.getTotalLength();p.style.strokeDasharray=L;tl.fromTo(p,{strokeDashoffset:L},{strokeDashoffset:0,duration:.5,ease:'power2.inOut'},4.4);})();
// S2
const s2=st('s2'), d2=st('s3')-s2; inn('#s2l',s2+.4); inn('#s2h',s2+.5); inn('#s2h2',s2+d2*.55); inn('#s2t',s2+.7,{y:0});
tl.fromTo('#s2f',{scaleX:0},{scaleX:1,duration:1.6,ease:'power1.inOut'},s2+.9); [0,1,2].forEach(i=>inn('#s2y'+i,s2+1.0+i*.5,{y:10}));
// S3
const s3=st('s3'), d3=st('s4')-s3; inn('#s3l',s3+.4); inn('#s3n',s3+.6,{y:10}); slam('#s3a',s3+d3*.62); inn('#s3d',s3+d3*.68); slam('#s3b',s3+d3*.74);
inn('#s3r',s3+d3*.62,{y:0}); tl.fromTo('#s3rf',{scaleX:.18},{scaleX:1,duration:.8,ease:'power3.out'},s3+d3*.74);
// S4 avatar
const s4=st('s4'); slam('#s4t',s4+.4); inn('#s4h',s4+.8);
// S5 conditions
const s5=st('s5'), d5=st('s6')-s5; inn('#s5l',s5+.4);
[[0,.3],[1,.6],[2,.78]].forEach(([i,f])=>{inn('#s5r'+i,s5+d5*f,{y:24}); tl.to('#s5k'+i,{backgroundColor:'#161412',duration:.15},s5+d5*f+.3);}); inn('#s5c',s5+.6,{y:30});
// S6 package
const s6=st('s6'), d6=st('s7')-s6; inn('#s6l',s6+.4); inn('#s6bar',s6+.45,{y:0});
['#s6a','#s6b','#s6c','#s6d'].forEach((s,i)=>tl.fromTo(s,{scaleX:0},{scaleX:1,duration:.4,ease:'power3.out'},s6+.55+i*.3));
[0,1,2,3].forEach(i=>inn('#s6v'+i,s6+.8+i*.35,{y:20})); slam('#s6s',s6+d6*.8);
// S7 commitment
const s7=st('s7'), d7=st('s8')-s7; inn('#s7l',s7+.4); inn('#s7t',s7+.45,{y:0}); tl.fromTo('#s7u',{scaleX:0},{scaleX:1,duration:.6,ease:'power2.out'},s7+.6);
tl.fromTo('#s7r',{opacity:0},{opacity:1,duration:.3},s7+d7*.3); inn('#s7m0',s7+d7*.25,{y:10}); slam('#s7m1',s7+d7*.42); inn('#s7m2',s7+d7*.48,{y:10}); inn('#s7c',s7+d7*.7,{y:30});
// S8 checklist
const s8=st('s8'), d8=st('s9')-s8; inn('#s8l',s8+.4); [[0,.3],[1,.55]].forEach(([i,f])=>{inn('#s8r'+i,s8+d8*f,{y:24}); tl.to('#s8k'+i,{backgroundColor:'#161412',duration:.15},s8+d8*f+.3);}); inn('#s8m',s8+d8*.7,{y:10});
// S9 CTA
const s9=st('s9'); slam('#s9t',s9+.3); inn('#s9b',s9+1.2);
'''
