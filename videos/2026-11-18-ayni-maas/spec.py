import os
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [
    (N('yüzde', 'yirmi', 'dokuz', 'virgül', 'yetmiş', 'üçtü'), "%29,73'tü"), (N('yetmiş', 'iki', 'bin', 'liralık'), '72 bin liralık'),
    (N('yetmiş', 'iki', 'bin', 'lira'), '72 bin lira'), (N('yetmiş', 'sekiz', 'bin', 'lira'), '78 bin lira'), (N('altmış', 'bin', 'lira'), '60 bin lira'),
    (N('seksen', 'dört', 'bin'), '84 bin'), (N('yüzde', 'kırk', 'beşi'), "%45'i"), (N('yüzde', 'kırk'), '%40'),
    (N('yüz', 'bin', 'dolardan'), '100 bin dolardan'), (N('altı', 'bin'), '6 bin'), (N('altı', 'binde'), '6 binde'), (N('altı', 'bini'), '6 bini'),
    (N('on', 'iki', 'ayda'), '12 ayda'), (N('iki', 'abonelik'), '2 abonelik'),
]
EM = {'zam', 'temsili', 'gerçek', 'yaşam', 'standardı', 'enflasyonu', 'ayrı', 'kural', 'kaydet', 'önce', 'ilk'}
RED = {'sıfır', 'eriyor', "%29,73'tü", "%45'i"}
HOOK = [170, 250, 740, 1040, 34]
SIDE = [60, 330, 500, 703, 28]
MIDW = [230, 300, 620, 871, 30]
AV = {'s1': HOOK, 's2': SIDE, 's3': None, 's4': None, 's5': None, 's6': MIDW, 's7': None, 's8': None, 's9': None, 's10': None, 's11': HOOK}
EXTRA_CSS = '''<style>
.pc{position:absolute;width:450px;height:620px;border-radius:28px;background:rgba(243,239,230,.05);border:3px solid rgba(243,239,230,.14);overflow:hidden}
.pc .t{position:absolute;left:0;right:0;top:0;padding:16px;text-align:center;font:700 30px 'IBM Plex Mono';letter-spacing:.16em;color:#0d0c0a}
.chip{display:inline-block;padding:10px 22px;border-radius:40px;font:800 40px 'Inter Tight';white-space:nowrap}
#s10{transform:translateY(220px)}
.cell{position:absolute;width:62px;height:62px;border-radius:12px;background:rgba(243,239,230,.10)}
</style>'''


def scenes(A):
    b = lambda t: round(t - .1, 3)
    t2 = A('Aynı'); t3 = A('Farkı'); t4 = A('Ama', A('Temsili')); t5 = A('Gerçek'); t6 = A('Asıl'); t7 = A('Birinci'); t8 = A('Bunun')
    t9 = A('İkinci'); t10 = A('Kural', A('İkinci')); t11 = A('Kaydet')
    return [('s1', 0, b(t2)), ('s2', b(t2), b(t3)), ('s3', b(t3), b(t4)), ('s4', b(t4), b(t5)), ('s5', b(t5), b(t6)),
            ('s6', b(t6), round(t7 - .13, 3)), ('s7', round(t7 - .13, 3), b(t8)), ('s8', b(t8), b(t9)), ('s9', b(t9), b(t10)),
            ('s10', b(t10), b(t11)), ('s11', b(t11), DUR)]


def SFX(A):
    return [[A('değil,'), 'impact', -9, 1, 'hook'], [A('sıfır'), 'stamp', -9, 1, 'zero'], [A('Temsili'), 'whoosh_hollow', -13, 0, 'cards'],
            [A('%40'), 'pop', -11, 0, 'zam'], [A('84 bin'), 'marker', -11, 0, '84'], [A("%29,73'tü"), 'stamp', -9, 1, 'tufe'],
            [A('78 bin lira'), 'marker', -11, 0, '78'], [A('6 bin', A('Gerçek')), 'impact', -8, 1, '6bin'], [A('Asıl'), 'whoosh_deep', -11, 0, 'turn'],
            [A('telefon'), 'ui_click', -12, 0, 'tel'], [A('2 abonelik'), 'ui_click', -12, 0, 'sub'], [A('eriyor'), 'paper_drop', -9, 0, 'melt'],
            [A("%45'i"), 'stamp', -9, 1, '45'], [A('ayrı'), 'ui_click', -11, 0, 'save'], [A('72 bin lira', A('İkinci')), 'success', -11, 1, '72'],
            [A('Kaydet') + .1, 'stamp', -10, 1, 'kaydet']]


def RISERS(A): return [[A('Asıl'), 'sharp', -10], [A('İkinci'), 'metallic', -11]]


SCENE_HTML = r'''
  <section id="s1" class="scene clip">
    <div class="a h" id="s1a" style="left:0;right:0;top:1330px;text-align:center;font-size:80px">ZAM GELDİ, <span class="red">AY SONU YOK</span></div>
  </section>
  <section id="s2" class="scene clip">
    <div class="a lab" id="s2l" style="left:600px;top:330px">AYNI MAAŞ · 1 YIL</div>
    <div class="a mono" id="s2a0" style="left:600px;top:420px">1. kişi</div>
    <div class="a big red" id="s2a" style="left:596px;top:460px;font-size:150px">0 ₺</div>
    <div class="a mono" id="s2b0" style="left:600px;top:680px">2. kişi</div>
    <div class="a big gold" id="s2b" style="left:596px;top:720px;font-size:110px">72.000 ₺</div>
    <div class="a mono" id="s2n" style="left:600px;top:880px;font-size:22px">temsili örnek</div>
  </section>
  <section id="s3" class="scene clip">
    <div class="a lab" id="s3l" style="left:60px;top:280px">TEMSİLİ ÖRNEK · FARKI YARATAN KURAL SONDA</div>
    <div class="pc" id="s3c0" style="left:60px;top:350px"><div class="t" style="background:#ff4a3d">1. KİŞİ</div>
      <div class="mono" style="position:absolute;left:36px;top:110px">maaş</div><div class="big" style="position:absolute;left:30px;top:150px;font-size:96px">60.000</div>
      <div class="chip" id="s3z0" style="position:absolute;left:36px;top:300px;background:#e8b931;color:#0d0c0a">+%40 ZAM</div>
      <div class="big" id="s3n0" style="position:absolute;left:30px;top:410px;font-size:110px">84.000</div></div>
    <div class="pc" id="s3c1" style="left:570px;top:350px"><div class="t" style="background:#3ddc84">2. KİŞİ</div>
      <div class="mono" style="position:absolute;left:36px;top:110px">maaş</div><div class="big" style="position:absolute;left:30px;top:150px;font-size:96px">60.000</div>
      <div class="chip" id="s3z1" style="position:absolute;left:36px;top:300px;background:#e8b931;color:#0d0c0a">+%40 ZAM</div>
      <div class="big" id="s3n1" style="position:absolute;left:30px;top:410px;font-size:110px">84.000</div></div>
    <div class="a h" id="s3e" style="left:0;right:0;top:1060px;text-align:center;font-size:84px">AYNI MAAŞ = <span class="gold">AYNI ZAM</span></div>
  </section>
  <section id="s4" class="scene clip">
    <div class="a lab" id="s4l" style="left:60px;top:280px">YILLIK TÜFE · EYLÜL 2026 · TÜİK</div>
    <div class="a big red" id="s4v" style="left:52px;top:330px;font-size:230px">%29,73</div>
    <div class="a mono" id="s4m0" style="left:60px;top:640px">yeni maaş</div>
    <div class="a" id="s4b0" style="left:60px;top:690px;width:960px;height:110px;border-radius:16px;background:#f3efe6;transform-origin:0 50%"><span class="h" style="position:absolute;left:30px;top:14px;font-size:76px;color:#0d0c0a">84.000 ₺</span></div>
    <div class="a mono" id="s4m1" style="left:60px;top:840px">aynı hayat (60.000 × 1,2973)</div>
    <div class="a" id="s4b1" style="left:60px;top:890px;width:890px;height:110px;border-radius:16px;background:#ff4a3d;transform-origin:0 50%"><span class="h" style="position:absolute;left:30px;top:14px;font-size:76px;color:#0d0c0a">≈ 77.840 ₺</span></div>
  </section>
  <section id="s5" class="scene clip">
    <div class="a lab" id="s5l" style="left:60px;top:560px">GERÇEK ARTIŞ · AYLIK</div>
    <div class="a big gold" id="s5v" style="left:52px;top:620px;font-size:300px">+6.000</div>
    <div class="a h" id="s5u" style="left:60px;top:920px;font-size:90px">₺ civarı</div>
  </section>
  <section id="s6" class="scene clip">
    <div class="a h gold" id="s6t" style="left:0;right:0;top:1230px;text-align:center;font-size:96px">ASIL FARK BURADA</div>
  </section>
  <section id="s7" class="scene clip">
    <div class="a lab" id="s7l" style="left:60px;top:280px">1. KİŞİ · ZAMDAN SONRAKİ İLK AY</div>
    <div class="a card" id="s7r0" style="left:60px;top:360px;width:960px;display:flex;justify-content:space-between;align-items:center"><span class="h" style="font-size:60px">📱 Telefon taksiti</span><span class="h red" style="font-size:60px">−</span></div>
    <div class="a card" id="s7r1" style="left:60px;top:520px;width:960px;display:flex;justify-content:space-between;align-items:center"><span class="h" style="font-size:60px">🎬 Abonelik</span><span class="h red" style="font-size:60px">−</span></div>
    <div class="a card" id="s7r2" style="left:60px;top:680px;width:960px;display:flex;justify-content:space-between;align-items:center"><span class="h" style="font-size:60px">🎧 Abonelik</span><span class="h red" style="font-size:60px">−</span></div>
    <div class="a mono" id="s7m" style="left:60px;top:870px">kalan gerçek artış</div>
    <div class="a big" id="s7v" style="left:52px;top:910px;font-size:190px">6.000 ₺</div>
  </section>
  <section id="s8" class="scene clip">
    <div class="a ghost" id="s8g" data-layout-allow-overflow data-layout-allow-occlusion style="left:-20px;top:240px;font-size:260px">CREEP</div>
    <div class="a h" id="s8h" style="left:60px;top:300px;font-size:84px">YAŞAM STANDARDI</div>
    <div class="a h gold" id="s8h2" style="left:60px;top:390px;font-size:84px">ENFLASYONU</div>
    <div class="a mono" id="s8m" style="left:60px;top:500px">gelir artınca harcama da sessizce artar</div>
    <div class="a lab" id="s8l" style="left:60px;top:640px">ABD · YILDA 100.000 $+ KAZANANLAR</div>
    <div class="a big red" id="s8v" style="left:52px;top:690px;font-size:260px">%45</div>
    <div class="a h" id="s8u" style="left:60px;top:960px;font-size:70px">maaştan maaşa yaşıyor</div>
    <div class="a mono" id="s8s" style="left:60px;top:1060px;font-size:22px">LendingClub · Kasım 2023 verisi</div>
  </section>
  <section id="s9" class="scene clip">
    <div class="a lab" id="s9l" style="left:60px;top:280px">2. KİŞİ · MAAŞ YATTIĞI GÜN → AYRI HESAP</div>
    <div class="a" id="s9grid" style="left:60px;top:360px;width:960px;height:180px"></div>
    <div class="a mono" id="s9m" style="left:60px;top:560px">12 ay × 6.000 ₺ · faiz/getiri hariç</div>
    <div class="a big gold" id="s9v" style="left:52px;top:620px;font-size:240px">0 ₺</div>
  </section>
  <section id="s10" class="scene clip">
    <div class="a lab" id="s10l" style="left:60px;top:420px">KURAL</div>
    <div class="a card" id="s10c" style="left:60px;top:480px;width:960px;border-color:#e8b931">
      <div class="h" style="font-size:66px;white-space:normal;line-height:1.08">Zammın <span class="gold">enflasyonu aşan</span> kısmını,</div>
      <div class="h" style="font-size:66px;white-space:normal;line-height:1.08;margin-top:14px"><span class="red">harcamadan önce</span> ayır.</div>
    </div>
    <div class="a mono" id="s10m" style="left:60px;top:860px">maaş günü · otomatik talimat</div>
  </section>
  <section id="s11" class="scene clip">
    <div class="a h gold" id="s11t" style="left:0;right:0;top:1325px;text-align:center;font-size:110px">KAYDET</div>
  </section>
'''
SCENE_JS = r'''
// S1 hook
inn('#s1a',.35,{s:1.08});
// S2 0 vs 72k next to avatar
const s2=st('s2'), d2=st('s3')-s2; inn('#s2l',s2+.45); inn('#s2b0',s2+.5); inn('#s2b',s2+.55); count('#s2b',0,72000,s2+.6,1.6,v=>fmt(v)+' ₺');
inn('#s2a0',s2+d2*.75); slam('#s2a',s2+d2*.78); inn('#s2n',s2+.9,{y:10});
// S3 two cards
const s3=st('s3'), d3=st('s4')-s3; inn('#s3l',s3+.4); inn('#s3c0',s3+.5,{y:80}); inn('#s3c1',s3+.65,{y:80});
slam('#s3z0',s3+d3*.55); slam('#s3z1',s3+d3*.57); inn('#s3n0',s3+d3*.75); inn('#s3n1',s3+d3*.77); inn('#s3e',s3+d3*.82);
// S4 inflation bars
const s4=st('s4'), d4=st('s5')-s4; inn('#s4l',s4+.4); slam('#s4v',s4+.55); inn('#s4m0',s4+d4*.45,{y:10});
tl.fromTo('#s4b0',{scaleX:0},{scaleX:1,duration:.5,ease:'power3.out'},s4+d4*.45); inn('#s4m1',s4+d4*.6,{y:10});
tl.fromTo('#s4b1',{scaleX:0},{scaleX:1,duration:.7,ease:'power3.out'},s4+d4*.62);
// S5 +6000
const s5=st('s5'); inn('#s5l',s5+.4); slam('#s5v',s5+.5); count('#s5v',0,6000,s5+.5,.9,v=>'+'+fmt(v)); inn('#s5u',s5+.9);
// S6 avatar turn
const s6=st('s6'); slam('#s6t',s6+.4);
// S7 money melts
const s7=st('s7'), d7=st('s8')-s7; inn('#s7l',s7+.4); inn('#s7v',s7+.5); inn('#s7m',s7+.45,{y:10});
[0,1,2].forEach((i,k)=>{const t=s7+[.12,.4,.5][k]*d7+.3; inn('#s7r'+i,t,{y:30});});
count('#s7v',6000,0,s7+d7*.62,1.2,v=>fmt(v)+' ₺'); tl.to('#s7v',{color:'#ff4a3d',duration:.3},s7+d7*.62+1.0);
// S8 concept + 45%
const s8=st('s8'), d8=st('s9')-s8; tl.fromTo('#s8g',{x:0},{x:-200,duration:d8,ease:'none'},s8); inn('#s8h',s8+.4); inn('#s8h2',s8+.55); inn('#s8m',s8+.9,{y:10});
inn('#s8l',s8+d8*.33); slam('#s8v',s8+d8*.62); count('#s8v',0,45,s8+d8*.62,.8,v=>'%'+Math.round(v)); inn('#s8u',s8+d8*.7); inn('#s8s',s8+d8*.72,{y:10});
// S9 12 months fill
const s9=st('s9'), d9=st('s10')-s9; inn('#s9l',s9+.4);
(function(){const g=$('#s9grid');for(let i=0;i<12;i++){const c=document.createElement('div');c.className='cell';c.id='s9c'+i;c.style.left=(i*80)+'px';c.style.top='40px';g.appendChild(c);
 const lb=document.createElement('div');lb.className='mono';lb.style.cssText=`position:absolute;left:${i*80+14}px;top:120px;font-size:22px`;lb.textContent=(i+1);g.appendChild(lb);}})();
inn('#s9grid',s9+.45,{y:0}); inn('#s9m',s9+.6,{y:10}); inn('#s9v',s9+.6);
const t9=s9+d9*.45; for(let i=0;i<12;i++) tl.to('#s9c'+i,{backgroundColor:'#e8b931',duration:.12},t9+i*.12);
count('#s9v',0,72000,t9,1.45,v=>fmt(v)+' ₺');
// S10 rule
const s10=st('s10'); inn('#s10l',s10+.4); inn('#s10c',s10+.5,{y:50}); inn('#s10m',s10+1.6,{y:10});
// S11 CTA
const s11=st('s11'); slam('#s11t',s11+.3);
'''
