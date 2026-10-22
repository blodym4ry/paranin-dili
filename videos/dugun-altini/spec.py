import os
# Şablon: KUYUMCU VİTRİNİ (Ata seçimi, 22 Eki). Siyah kadife, cam vitrin yansıması, beyaz ipli fiyat etiketleri, gerçek çeyrek/takı fotoğrafları.
# 2. perde (Yargıtay): krem dosya + kırmızı damga. Anlatım: soru + iki perde. Avatar: lacivert balıkçı yaka. Müzik: modern_oryantal.
# Gerçek görseller: media/ (çeyrek: cimri/ceyrekci; takı: haber7 — YÜZLER KIRPILDI; Yargıtay binası: yapivebahce) — kaynaklar.md
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [
    (N('iki', 'bin', 'on', 'altıda'), "2016'da"), (N('iki', 'bin', 'yirmi', 'dörtte'), "2024'te"),
    (N('iki', 'yüz', 'on', 'iki', 'liraydı'), '212 liraydı'), (N('on', 'bin', 'sekiz', 'yüzü'), "10.800'ü"),
    (N('elli', 'bir', 'kat'), '51 kat'), (N('on', 'beş', 'buçuk', 'kat'), '15,5 kat'), (N('on', 'çeyrek'), '10 çeyrek'),
    (N('bir', 'buçuktan'), "1,5'tan"), (N('dört', 'bin', 'tondan'), '4.000 tondan'), (N('üç', 'kattan'), '3 kattan'),
    (N('on', 'yılda'), '10 yılda'), (N('neredeyse', 'dört'), 'neredeyse 4'),
]
EM = {'altın', 'kimin', 'kadına', 'anlaşmasına', 'örfe', 'alış', 'işçilik', 'kaydet', 'birikim'}
RED = {'51 kat', 'neredeyse 4', 'geri'}
FRONT = [250, 330, 580, 815, 18]
MID = [290, 330, 500, 703, 18]
AV = {'s1': FRONT, 's2': None, 's3': None, 's4': None, 's5': None, 's6': None, 's7': MID, 's8': None, 's9': None, 's10': FRONT}

EXTRA_CSS = r'''<style>
:root{--gold:#e6b84a;--gold2:#ffd77a;--cream:#f6f0e2;--ink:#14100a;--red:#c8322b;--cap-em-bg:#e6b84a;--cap-em-fg:#14100a}
body,#root{background:#07060a}
.bg{background:radial-gradient(ellipse 70% 45% at 50% 30%,rgba(230,184,74,.20) 0%,rgba(0,0,0,0) 70%),radial-gradient(ellipse 120% 80% at 50% 100%,#1a1022 0%,#07060a 70%)}
.bg::before{content:'';position:absolute;inset:0;background:repeating-linear-gradient(115deg,rgba(255,255,255,.035) 0 2px,transparent 2px 9px);opacity:.6}
.bg::after{content:'';position:absolute;left:-200px;top:0;width:520px;height:1920px;background:linear-gradient(100deg,transparent,rgba(255,255,255,.07),transparent);transform:skewX(-12deg)}
#grid{display:none}
#avbox{filter:drop-shadow(0 0 0 #e6b84a) drop-shadow(5px 0 0 #e6b84a) drop-shadow(-5px 0 0 #e6b84a) drop-shadow(0 5px 0 #e6b84a) drop-shadow(0 -5px 0 #e6b84a) drop-shadow(0 30px 50px rgba(0,0,0,.7))}
.tag{position:absolute;background:var(--cream);color:var(--ink);border-radius:8px 14px 14px 8px;padding:14px 30px 14px 46px;font:900 64px/1 'Inter Tight';letter-spacing:-.03em;box-shadow:0 16px 34px rgba(0,0,0,.55)}
.tag::before{content:'';position:absolute;left:14px;top:50%;width:18px;height:18px;margin-top:-9px;border-radius:50%;background:#07060a;box-shadow:0 0 0 3px #b9ae96}
.tag small{display:block;font:700 22px 'IBM Plex Mono';letter-spacing:.1em;color:#7a6c50;margin-bottom:6px}
.str{position:absolute;width:3px;background:linear-gradient(#e6e0d0,#b9ae96);transform-origin:50% 0}
.coin{position:absolute;border-radius:50%;box-shadow:0 20px 40px rgba(0,0,0,.7),0 0 60px rgba(230,184,74,.35)}
.lbl{font:700 26px 'IBM Plex Mono';letter-spacing:.16em;color:var(--gold)}
.gold{color:var(--gold2)}
.big{font:900 150px/1 'Inter Tight';letter-spacing:-.05em}
.bar{position:absolute;bottom:0;border-radius:12px 12px 0 0;transform-origin:50% 100%}
.file{position:absolute;background:var(--cream);color:var(--ink);border-radius:8px;box-shadow:0 26px 50px rgba(0,0,0,.6);padding:28px 34px;font:600 34px/1.35 'Inter Tight'}
.file .hd{font:700 22px 'IBM Plex Mono';letter-spacing:.12em;color:#7a6c50;border-bottom:3px solid #14100a;padding-bottom:10px;margin-bottom:12px}
.stamp{position:absolute;border:7px solid var(--red);color:var(--red);font:800 42px 'IBM Plex Mono';letter-spacing:.06em;padding:8px 22px;border-radius:10px;transform:rotate(-8deg);text-align:center;line-height:1.1;background:rgba(246,240,226,.9)}
.ph{position:absolute;overflow:hidden;border-radius:14px;box-shadow:0 26px 60px rgba(0,0,0,.7);border:4px solid var(--gold)}
.ph img{display:block;width:100%;height:100%;object-fit:cover}
.step{display:flex;align-items:center;gap:22px;background:var(--cream);color:var(--ink);border-radius:12px;padding:16px 26px;margin-bottom:16px;font:800 40px 'Inter Tight';box-shadow:0 14px 30px rgba(0,0,0,.5)}
.step b{font:900 44px 'IBM Plex Mono';color:var(--red)}
.src{font:500 20px 'IBM Plex Mono';color:rgba(246,240,226,.55)}
</style>'''


def scenes(A):
    return [('s1', 0, 5.75), ('s2', 5.75, 8.6), ('s3', 8.6, 15.0), ('s4', 15.0, 17.72), ('s5', 17.72, 23.9), ('s6', 23.9, 28.88),
            ('s7', 28.88, 30.68), ('s8', 30.68, 48.33), ('s9', 48.33, 55.86), ('s10', 55.86, DUR)]


COINS10 = ''.join(f'<img class="coin" id="s5c{i}" src="media/ceyrek.jpg" style="left:{120 + (i % 5) * 170}px;top:{430 + (i // 5) * 190}px;width:160px;height:160px">' for i in range(10))

SCENE_HTML = r'''
  <section id="s1" class="scene clip">
    <div class="a lbl" id="s1l" style="left:0;right:0;top:240px;text-align:center">VİTRİN · DÜĞÜN ALTINI</div>
    <img class="a coin" id="s1c" src="media/ceyrek.jpg" style="left:40px;top:1080px;width:230px;height:230px">
    <div class="a tag" id="s1t" style="left:640px;top:1150px">×3<small style="display:inline;margin-left:10px">ENFLASYONU YENDİ</small></div>
  </section>
  <section id="s2" class="scene clip">
    <div class="a ph" id="s2p" style="left:90px;top:300px;width:900px;height:810px"><img src="media/taki_kirp.jpg"></div>
    <div class="a tag" id="s2t" style="left:300px;top:1160px;font-size:90px">KİMİN?</div>
  </section>
  <section id="s3" class="scene clip">
    <div class="a lbl" id="s3l" style="left:60px;top:250px">ÇEYREK ALTIN · SATIŞ</div>
    <img class="a coin" id="s3c" src="media/ceyrek.jpg" style="left:290px;top:330px;width:500px;height:500px">
    <div class="a str" id="s3s1" style="left:300px;top:760px;height:120px;transform:rotate(18deg)"></div>
    <div class="a tag" id="s3t1" style="left:70px;top:880px"><small>EKİM 2016</small>212 TL</div>
    <div class="a str" id="s3s2" style="left:770px;top:760px;height:120px;transform:rotate(-18deg)"></div>
    <div class="a tag" id="s3t2" style="left:560px;top:880px"><small>EKİM 2026</small>10.845 TL</div>
    <div class="a big gold" id="s3x" style="left:0;right:0;top:1090px;text-align:center;text-shadow:0 10px 40px rgba(230,184,74,.4)">×51</div>
    <div class="a src" id="s3src" style="left:60px;top:1270px">Kapalıçarşı: Bloomberg HT 03.11.2016 · Dünya 18.10.2026</div>
  </section>
  <section id="s4" class="scene clip">
    <div class="a lbl" id="s4l" style="left:60px;top:250px">2016 → 2026 · KAÇ KATINA ÇIKTI?</div>
    <div class="a" id="s4box" style="left:140px;top:330px;width:800px;height:900px">
      <div class="bar" id="s4b1" style="left:60px;width:260px;height:274px;background:rgba(246,240,226,.35)"></div>
      <div class="bar" id="s4b2" style="left:480px;width:260px;height:900px;background:linear-gradient(#ffd77a,#b9852a)"></div></div>
    <div class="a" id="s4v1" style="left:200px;top:1250px;width:260px;text-align:center;font:900 70px 'Inter Tight'">×15,5<div class="lbl" style="font-size:22px;color:#cfc6b0">FİYATLAR (TÜFE)</div></div>
    <div class="a" id="s4v2" style="left:620px;top:1250px;width:260px;text-align:center;font:900 70px 'Inter Tight';color:#ffd77a">×51<div class="lbl" style="font-size:22px">ÇEYREK</div></div>
  </section>
  <section id="s5" class="scene clip">
    <div class="a lbl" id="s5l" style="left:60px;top:250px">DÜĞÜNDE TAKILAN 10 ÇEYREK</div>
    <div class="a" id="s5coins" style="left:0;top:0;width:1080px;height:900px">''' + COINS10 + r'''</div>
    <div class="a tag" id="s5a" style="left:70px;top:900px"><small>2016</small>1,6 asgari ücret</div>
    <div class="a tag" id="s5b" style="left:70px;top:1080px;background:#ffd77a"><small style="color:#5a4210">2026</small>3,9 asgari ücret</div>
    <div class="a src" id="s5src" style="left:70px;top:1250px">net asgari ücret 1.300,99 TL (2016) · 28.075,50 TL (2026)</div>
  </section>
  <section id="s6" class="scene clip">
    <div class="a ph" id="s6p" style="left:60px;top:260px;width:960px;height:600px"><img src="media/taki_kirp.jpg" style="object-position:50% 40%"></div>
    <div class="a big gold" id="s6v" style="left:0;right:0;top:900px;text-align:center">4.000+ TON</div>
    <div class="a lbl" id="s6u" style="left:0;right:0;top:1065px;text-align:center;color:#f6f0e2">TÜRK HALKININ ELİNDEKİ ALTIN · TAHMİN</div>
    <div class="a src" id="s6src" style="left:0;right:0;top:1120px;text-align:center">QNB tahmini (CNBC-e, Eylül 2025) · resmi veri yok</div>
  </section>
  <section id="s7" class="scene clip">
    <div class="a tag" id="s7t" style="left:330px;top:1100px;font-size:80px">KİMİN?</div>
  </section>
  <section id="s8" class="scene clip">
    <div class="a ph" id="s8p" style="left:60px;top:250px;width:960px;height:330px"><img src="media/yargitay.jpg" style="object-position:50% 30%"></div>
    <div class="a file" id="s8f1" style="left:60px;top:610px;width:960px"><div class="hd">ESKİ İÇTİHAT · YARGITAY</div>Düğünde takılanlar <b>kadına aittir.</b></div>
    <div class="a stamp" id="s8st" style="left:600px;top:640px">2024<br>DEĞİŞTİ</div>
    <div class="a file" id="s8f2" style="left:60px;top:810px;width:960px;padding:22px 30px"><div class="hd">YARGITAY 2. HD · 04.04.2024 · YENİ SIRA</div>
      <div class="step" id="s8a" style="box-shadow:none;background:#efe6d0"><b>1</b>Eşlerin anlaşması</div>
      <div class="step" id="s8b" style="box-shadow:none;background:#efe6d0"><b>2</b>Yöresel örf</div>
      <div class="step" id="s8c" style="box-shadow:none;background:#efe6d0;margin-bottom:0"><b>3</b>Kime takıldıysa onun</div></div>
    <div class="a" id="s8g" style="left:60px;top:1290px;width:960px;display:flex;gap:20px">
      <div class="tag" style="position:relative;flex:1;font-size:40px;padding-left:40px"><small>KADINA ÖZGÜ</small>→ kadının</div>
      <div class="tag" style="position:relative;flex:1;font-size:40px;padding-left:40px"><small>ERKEĞE ÖZGÜ</small>→ erkeğin</div></div>
  </section>
  <section id="s9" class="scene clip">
    <div class="a lbl" id="s9l" style="left:60px;top:250px">SATMADAN ÖNCE</div>
    <div class="a tag" id="s9al" style="left:60px;top:320px;font-size:80px;background:#ffd77a"><small style="color:#5a4210">BAK</small>ALIŞ fiyatı</div>
    <div class="a tag" id="s9sa" style="left:560px;top:340px;font-size:60px;opacity:.7"><small>DEĞİL</small><span style="position:relative">SATIŞ<span id="s9x" style="position:absolute;left:-6px;right:-6px;top:50%;height:7px;background:#c8322b;transform-origin:0 50%"></span></span></div>
    <div class="a ph" id="s9p" style="left:240px;top:560px;width:600px;height:600px;background:#fff"><img src="media/bilezik.jpg" style="object-fit:contain"></div>
    <div class="a stamp" id="s9st" style="left:430px;top:1060px;font-size:38px">İŞÇİLİK<br>GERİ GELMEZ</div>
  </section>
  <section id="s10" class="scene clip">
    <div class="a stamp" id="s10k" style="left:330px;top:1170px;font-size:72px;transform:rotate(-6deg)">KAYDET</div>
    <div class="a" id="s10a" style="left:0;right:0;top:1180px;text-align:center;font:800 54px 'Inter Tight'">süs değil, <span class="gold">birikim</span></div>
  </section>
'''

SCENE_JS = r'''
const stamp=(s,t)=>tl.fromTo(s,{opacity:0,scale:1.8},{opacity:1,scale:1,duration:.22,ease:'power4.in'},t);
const swing=(s,t)=>tl.fromTo(s,{opacity:0,rotation:-14,y:-60,transformOrigin:'0% 0%'},{opacity:1,rotation:0,y:0,duration:.8,ease:'elastic.out(1,.5)'},t);
// S1 kanca
inn('#s1l',.2,{y:-20}); tl.fromTo('#s1c',{opacity:0,rotationY:-90},{opacity:1,rotationY:0,duration:.6,ease:'back.out(1.6)'},2.45); swing('#s1t',4.22);
// S2 kimin?
inn('#s2p',5.8,{s:1.08}); swing('#s2t',7.3);
// S3 fiyat etiketleri
inn('#s3l',8.65,{y:-10}); tl.fromTo('#s3c',{opacity:0,rotationY:-180,scale:.7},{opacity:1,rotationY:0,scale:1,duration:.9,ease:'expo.out'},8.7);
tl.fromTo('#s3s1',{opacity:0},{opacity:1,duration:.2},10.45); swing('#s3t1',10.5);
tl.fromTo('#s3s2',{opacity:0},{opacity:1,duration:.2},12.25); swing('#s3t2',12.3); slam('#s3x',13.86); inn('#s3src',12.4,{y:0});
// S4 çubuklar
inn('#s4l',15.1); tl.fromTo('#s4b1',{scaleY:0},{scaleY:1,duration:.6,ease:'power3.out'},15.2); inn('#s4v1',15.4,{y:20});
tl.fromTo('#s4b2',{scaleY:0},{scaleY:1,duration:.9,ease:'power3.out'},16.3); inn('#s4v2',16.6,{y:20});
// S5 10 çeyrek
inn('#s5l',17.8); [0,1,2,3,4,5,6,7,8,9].forEach(i=>tl.fromTo('#s5c'+i,{opacity:0,y:-300,rotation:-40},{opacity:1,y:0,rotation:0,duration:.45,ease:'bounce.out'},18.6+i*.07));
swing('#s5a',19.9); swing('#s5b',22.33); inn('#s5src',20.5,{y:0});
// S6 yastık altı
inn('#s6p',24.0,{s:1.06}); slam('#s6v',25.66); inn('#s6u',26.4,{y:10}); inn('#s6src',27.9,{y:0});
// S7 ara kanca
swing('#s7t',29.3);
// S8 Yargıtay
inn('#s8p',30.75,{y:40}); inn('#s8f1',31.4,{y:40}); stamp('#s8st',34.45); inn('#s8f2',36.1,{y:60});
tl.fromTo(['#s8a','#s8b','#s8c'],{opacity:.15},{opacity:1,duration:.2,stagger:0},36.1); tl.set(['#s8a','#s8b','#s8c'],{opacity:.25},36.5);
tl.to('#s8a',{opacity:1,duration:.25},38.5); tl.to('#s8b',{opacity:1,duration:.25},40.34); tl.to('#s8c',{opacity:1,duration:.25},42.94);
tl.to(['#s8p','#s8f1','#s8st'],{opacity:.25,duration:.3},38.2); inn('#s8g',44.86,{y:30});
// S9 kuyumcu
inn('#s9l',48.4,{y:-10}); swing('#s9al',51.67); inn('#s9sa',50.9,{y:0}); tl.fromTo('#s9x',{scaleX:0},{scaleX:1,duration:.3},52.0);
inn('#s9p',52.99,{s:1.08}); stamp('#s9st',54.78);
// S10 CTA + döngü
stamp('#s10k',56.02); out('#s10k',56.8); inn('#s10a',57.0,{y:20});
'''


def SFX(A):
    return [[2.45, 'pop', -11, 0, 'coin'], [4.22, 'impact', -9, 1, 'x3'], [7.3, 'pop', -11, 0, 'kimin'],
            [8.7, 'ui_click', -12, 0, 'coin2'], [10.5, 'paper_drop', -11, 0, 'tag1'], [12.3, 'paper_drop', -11, 0, 'tag2'], [13.86, 'impact', -8, 1, 'x51'],
            [16.3, 'gears', -12, 0, 'bar'], [18.6, 'pop', -12, 0, 'coins'], [22.33, 'impact', -9, 1, '4asg'], [25.66, 'impact', -9, 1, 'ton'],
            [29.3, 'pop', -10, 0, 'kimin2'], [34.45, 'stamp', -7, 1, '2024'], [38.5, 'ui_click', -12, 0, '1'], [40.34, 'ui_click', -12, 0, '2'],
            [42.94, 'ui_click', -12, 0, '3'], [51.67, 'paper_drop', -11, 0, 'alis'], [52.0, 'marker', -11, 0, 'satis_x'], [54.78, 'stamp', -8, 1, 'iscilik'],
            [56.02, 'stamp', -7, 1, 'kaydet'], [58.84, 'success', -11, 0, 'loop']]


def RISERS(A): return [[8.4, 'sharp', -11], [28.6, 'metallic', -11], [48.1, 'sharp', -12]]
