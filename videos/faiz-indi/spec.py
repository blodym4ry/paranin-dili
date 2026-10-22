import os
from masa_kit import CSS, JS, OVERLAYS, ring, line, kup
# FAİZ İNDİ — stil: MASA ÜSTÜ DOSYA (Ata 23 Eki). Avatar: kahverengi kapüşon + gözlük. Müzik: gerilim/belgesel.
# İmza nesnesi: FİŞ (kişisel hesap satır satır basılır). Desen kırılması: lamba söner ("Asıl hesap şimdi başlıyor").
# Kaynaklar: kaynaklar.md · Grafik alanı y=230–1180 (altyazı 1200–1420).
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
N = lambda *w: list(w)
REPL = [(N('yüz', 'bin'), '100 bin'), (N('yetmiş'), '70'), (N('yüzde', 'kırk'), '%40'), (N('otuz', 'iki'), '32'),
        (N('üç', 'bin', 'beş', 'yüz'), '3.500'), (N('yüzde', 'on', 'yedi', 'buçuğu'), "%17,5'i"), (N('yüzde', 'otuz', 'üç'), '%33'),
        (N('yüzde', 'yirmi', 'dokuz', 'virgül', 'yedi'), '%29,7'), (N('üç', 'puan'), '3 puan'), (N('iki', 'buçuk'), '2,5'), (N('bir', 'puan'), '1 puan')]
EM = {'manşeti', 'hesap', 'net', 'fark', 'farka'}
RED = {'%33', '%29,7', '2,5'}
SOUND_KIT = 'masa'
EXIT_FADE = False
POL = [330, 240, 420, 560, 4]
AV = {'s1': POL, 's2': None, 's3': None, 's5': None, 's6': None, 's8': POL, 's9': None, 's10': POL}

EXTRA_CSS = CSS + r'''<style>
.stamp{position:absolute;font:900 64px 'Inter Tight';color:#c8261f;border:7px solid #c8261f;padding:6px 22px;transform:rotate(-8deg);mix-blend-mode:multiply;letter-spacing:.02em}
.ital{font:italic 700 92px/1.05 'Playfair Display';color:#f6efe2;text-align:center}
.tag{position:absolute;width:200px;padding:16px 10px 18px;background:url(media/masa/kraft.jpg) center/400px;box-shadow:0 10px 16px rgba(0,0,0,.4);text-align:center}
.tag b{display:block;font:800 30px 'Inter Tight';color:#1d2433}.tag i{display:block;font:700 46px 'Caveat';color:#cf2a24;font-style:normal}
.pin{position:absolute;left:88px;top:-12px;width:24px;height:24px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#ff8a7a,#b3221a);box-shadow:0 3px 4px rgba(0,0,0,.4)}
</style>'''


def scenes(A):
    return [('s1', 0, 8.85), ('s2', 8.85, 12.2), ('s3', 12.2, 26.6), ('s5', 26.6, 28.9), ('s6', 28.9, 44.80),
            ('s8', 44.80, 48.95), ('s9', 48.95, 52.62), ('s10', 52.62, DUR)]


FIS = r'''<div class="fis" id="fz" style="left:60px;top:250px;transform:rotate(-2deg)">
  <div class="h">VADELİ HESAP · 32 GÜN</div>
  <div class="l" id="fz0"><span>Anapara</span><span>100.000 TL</span></div>
  <div class="l" id="fz1"><span>Faiz (yıllık)</span><span>%40</span></div>
  <div class="l" id="fz2"><span>Süre</span><span>32 gün</span></div>
  <div class="l t" id="fz3"><span>Brüt getiri</span><span>3.507 TL</span><div style="position:absolute;left:-28px;top:-6px">''' + ring('rb', 630, 66, 5) + r'''</div></div>
  <div class="l" id="fz4" style="color:#b3221a"><span>Stopaj %17,5</span><span>−614 TL</span></div>
  <div class="l t" id="fz5" style="font-size:40px"><span>NET</span><span>2.893 TL</span><div style="position:absolute;left:-28px;top:-2px">''' + ring('rn', 630, 76, 7) + r'''</div></div>
  <div class="l" id="fz6" style="font-size:20px;color:#77776f;margin-top:8px"><span>Örnek: Yapı Kredi %40,25 · 1 Eki</span><span></span></div>
</div>'''

FIS2 = r'''<div class="fis" id="fy" style="left:170px;top:280px;width:740px;transform:rotate(1.5deg)">
  <div class="h">UYGULAMADA BAK</div>
  <div class="l" id="fy0"><span>Brüt faiz</span><span>%40</span><div style="position:absolute;left:-10px;top:12px">''' + line('x0', 700, 9) + r'''</div></div>
  <div class="l" id="fy1"><span>Net getiri</span><span>%33</span></div>
  <div class="l" id="fy2"><span>− Enflasyon</span><span>%29,7</span></div>
  <div class="l t" id="fy3" style="font-size:46px"><span>FARK</span><span>+3,3 puan</span><div style="position:absolute;left:-30px;top:0px">''' + ring('rf', 740, 84, 11) + r'''</div></div>
</div>'''

SCENE_HTML = r'''
  <section id="s1" class="scene clip">
    <div class="tape" id="t1" style="left:290px;top:212px;transform:rotate(-30deg)"></div>
    <div class="tape" id="t2" style="left:650px;top:214px;transform:rotate(28deg)"></div>
    <div class="kraft" id="n1" style="left:60px;top:840px;width:540px;height:320px;transform:rotate(-3deg);padding:30px 38px">
      <div class="hand" style="font-size:104px">Faiz indi.</div>
      <div class="hand red" style="font-size:64px">asıl haber bu değil</div>
    </div>
    <div class="kraft" id="n2" style="left:620px;top:870px;width:400px;height:270px;transform:rotate(4deg);padding:26px 30px">
      <div class="print" style="font-size:24px;color:#3b2a18">100.000 TL · ayda</div>
      <div class="hand red" id="n2w" style="font-size:124px;clip-path:inset(0 100% 0 0)">−70 TL</div>
    </div>
  </section>
  <section id="s2" class="scene clip">
    ''' + kup('k1', 'HABERTÜRK · 22.10.2026', 'Merkez Bankası\'ndan faiz indirimi', 130, 330, -2) + r'''
    ''' + kup('k2', 'ENDEKS24 · 22.10.2026', 'TCMB, ocaktan bu yana ilk indirimle politika faizini yüzde 36\'ya çekti', 120, 360, 1.5, 46) + r'''
    ''' + kup('k3', 'GAZETE VATAN · 22.10.2026', 'MERKEZ BANKASI FAİZ KARARINI AÇIKLADI!', 140, 340, -1, 58) + r'''
    ''' + kup('k4', 'NETINTERNET · 22.10.2026', 'Politika Faizi Yüzde 36\'ya İndi', 125, 350, 2) + r'''
    <div class="stamp" id="st1" style="left:300px;top:760px;opacity:0">%37 → %36</div>
  </section>
  <section id="s3" class="scene clip">
    ''' + FIS + r'''
    <div class="photo" id="bn" style="left:610px;top:830px;width:380px;height:170px;transform:rotate(7deg)"><img src="media/tl200.jpg"><div class="cap">× 500 adet</div></div>
    <div class="kraft" id="n3" style="left:60px;top:850px;width:450px;height:300px;transform:rotate(-3deg);padding:24px 34px">
      <div class="hand" id="n3a" style="font-size:110px;clip-path:inset(0 100% 0 0);text-decoration:line-through;text-decoration-color:#cf2a24">%40</div>
      <div class="hand red" id="n3b" style="font-size:110px;clip-path:inset(0 100% 0 0)">→ %33</div>
    </div>
  </section>
  <section id="s5" class="scene clip"></section>
  <section id="s6" class="scene clip">
    ''' + kup('k5', 'TÜİK · 5 EKİM 2026', 'Eylülde yıllık enflasyon %29,73', 120, 250, -1.5, 56) + r'''
    <div class="strip" id="sp1" style="left:80px;top:540px;width:660px;background:#dfe9d6">Net getirin %33</div>
    <div class="strip" id="sp2" style="left:80px;top:650px;width:595px;background:#f0dcd6">Enflasyon %29,7</div>
    <div class="hand red" id="h3" style="position:absolute;left:770px;top:550px;font-size:92px;clip-path:inset(0 100% 0 0)">3 puan</div>
    <div class="hand red" id="h25" style="position:absolute;left:770px;top:650px;font-size:92px;clip-path:inset(0 100% 0 0)">→ 2,5</div>
    <div class="print" id="ass" style="position:absolute;left:84px;top:760px;font-size:20px;color:#f1e6d4;opacity:0">enflasyon sabit varsayımıyla · net %39 × 0,825 = %32,2</div>
    <div class="tag" id="g1" style="left:70px;top:860px;transform:rotate(-4deg)"><div class="pin"></div><b>ING</b><i>%35</i></div>
    <div class="tag" id="g2" style="left:300px;top:880px;transform:rotate(3deg)"><div class="pin"></div><b>HSBC</b><i>%35</i></div>
    <div class="tag" id="g3" style="left:530px;top:858px;transform:rotate(-2deg)"><div class="pin"></div><b>Citi</b><i>%35</i></div>
    <div class="tag" id="g4" style="left:760px;top:884px;transform:rotate(5deg)"><div class="pin"></div><b>Barclays</b><i>%35</i></div>
    <div class="print" id="gsrc" style="position:absolute;left:84px;top:1100px;font-size:20px;color:#f1e6d4;opacity:0">yıl sonu politika faizi tahmini · 22.10.2026</div>
  </section>
  <section id="s8" class="scene clip">
    <div class="tape" id="t5" style="left:290px;top:212px;transform:rotate(-30deg)"></div>
    <div class="kraft" id="n8" style="left:110px;top:870px;width:860px;height:270px;transform:rotate(-2deg);padding:28px 40px">
      <div class="hand" style="font-size:64px">TEK HESAP:</div>
      <div class="hand red" id="n8w" style="font-size:78px;clip-path:inset(0 100% 0 0)">net getiri − enflasyon</div>
    </div>
  </section>
  <section id="s9" class="scene clip">
    ''' + FIS2 + r'''
  </section>
  <section id="s10" class="scene clip">
    <div class="tape" id="t6" style="left:650px;top:214px;transform:rotate(28deg)"></div>
    <div class="kraft" id="n10" style="left:90px;top:850px;width:900px;height:200px;transform:rotate(2deg);padding:30px 36px">
      <div class="hand red" style="font-size:60px">→ parası bankada duran arkadaşına</div>
    </div>
    ''' + kup('k6', 'HABERTÜRK · 22.10.2026', 'Merkez Bankası\'ndan faiz indirimi', 140, 880, -3) + r'''
  </section>
  ''' + OVERLAYS + r'''
  <div class="ital" id="dk" style="position:absolute;left:60px;right:60px;top:640px;opacity:0">Asıl hesap<br>şimdi başlıyor.</div>
'''

SCENE_JS = JS + r'''
cam(__DUR__);
lamp(0,'rgba(255,200,120,A)',.14);
// S1 — kanca: başlık notu ilk karede hazır; bant; "−70 TL"
tape('#t1',.2,-30); tape('#t2',.4,28);
put('#n2',5.9,{r:4,y:140}); write('#n2w',7.45,.6);
// S2 — manşet montajı (aynı yere art arda düşen gerçek manşetler) + damga
['#k1','#k2','#k3','#k4'].forEach((k,i)=>{tl.set(k,{opacity:0},0);tl.set(k,{opacity:1},8.95+i*.62);if(i<3)tl.set(k,{opacity:0},8.95+(i+1)*.62);});
tl.fromTo('#st1',{opacity:0,scale:1.6},{opacity:1,scale:1,duration:3*F,ease:'steps(3)'},11.45);
// S3 — FİŞ basılır (kişisel hesap)
put('#fz',12.25,{r:-2,y:-500,dr:0,n:5}); ['#fz0','#fz1','#fz2','#fz3','#fz4','#fz5','#fz6'].forEach(s=>tl.set(s,{opacity:0},0));
prt('#fz0',12.5); prt('#fz1',12.85); prt('#fz2',14.35); prt('#fz3',15.5); prt('#fz6',15.9);
slide('#bn',13.45,{y:-90});
draw('rb',17.25,.5,26.6);
prt('#fz4',21.3); prt('#fz5',22.75);
put('#n3',23.55,{r:-3,y:120}); write('#n3a',23.9,.4); write('#n3b',25.3,.5); draw('rn',25.9,.5,26.6);
// S5 — LAMBA SÖNER: desen kırılması
dark(26.7,28.62); tl.fromTo('#dk',{opacity:0},{opacity:1,duration:2*F,ease:'steps(2)'},26.85); tl.to('#dk',{opacity:0,duration:2*F,ease:'steps(2)'},28.55);
// S6 — enflasyon kupürü, şeritler, 4 banka, fark daralır
put('#k5',29.05,{r:-1.5,y:-160}); lamp(29.1,'rgba(255,200,120,A)',.14);
put('#sp1',33.35,{x:-300,y:0,dr:0,n:4}); put('#sp2',33.85,{x:-300,y:0,dr:0,n:4}); write('#h3',34.85,.5); lamp(35,'rgba(120,230,120,A)',.26);
put('#g1',36.2,{y:-120}); put('#g2',36.55,{y:-120}); put('#g3',36.9,{y:-120}); put('#g4',37.25,{y:-120}); tl.to('#gsrc',{opacity:1,duration:F},37.3);
lamp(40.1,'rgba(255,70,50,A)',.34);
tl.to('#sp1',{width:644,duration:4*F,ease:'steps(4)'},41.4); tl.set('#sp1',{innerHTML:'Net getirin %32,2'},41.75);
tl.set('#h3',{textDecoration:'line-through'},43.2); write('#h25',43.3,.5); tl.to('#ass',{opacity:1,duration:F},43.5);
// S8 — tek hesap (avatar)
tape('#t5',44.95,-30); put('#n8',45.15,{r:-2,y:140}); write('#n8w',46.5,1.2); lamp(45,'rgba(255,200,120,A)',.14);
// S9 — uygulamada bak (özet fiş)
put('#fy',49.05,{r:1.5,y:-500,dr:0}); ['#fy0','#fy1','#fy2','#fy3'].forEach(s=>tl.set(s,{opacity:0},0));
prt('#fy0',49.35); prt('#fy1',49.6); prt('#fy2',49.85); prt('#fy3',50.1); draw('x0',51.25,.35,52.62); draw('rf',52.05,.45,52.62);
// S10 — CTA + döngü (manşet)
tape('#t6',52.75,28); put('#n10',53.0,{r:2,y:140}); take('#n10',55.9,{x:1300}); put('#k6',56.1,{r:-3,y:-200,dr:-5});
'''.replace('__DUR__', str(DUR))


def SFX(A):
    return [[.2, 'f:bant', -7, 0, 'bant'], [.4, 'f:bant', -9, 0, 'bant'], [5.9, 'f:kagit_kay', -8, 0, 'not'], [7.45, 'f:kalem_yaz', -6, 1, '-70'],
            [8.95, 'f:deklansor', -8, 0, 'mans1'], [9.57, 'f:deklansor', -9, 0, 'mans2'], [10.19, 'f:deklansor', -9, 0, 'mans3'], [10.81, 'f:deklansor', -9, 0, 'mans4'],
            [11.45, 'f:damga', -5, 1, '37->36'],
            [12.25, 'f:kagit_kay', -7, 0, 'fis'], [12.5, 'f:daktilo', -11, 0, 'r0'], [12.85, 'f:daktilo', -11, 0, 'r1'], [14.35, 'f:daktilo', -11, 0, 'r2'], [15.5, 'f:daktilo', -9, 0, 'brut'],
            [13.45, 'f:foto_birak', -8, 0, 'banknot'], [17.25, 'f:kalem_daire', -6, 1, 'brut daire'], [21.3, 'f:daktilo', -9, 0, 'stopaj'], [22.75, 'f:daktilo', -8, 1, 'net'],
            [23.55, 'f:kagit_kay', -9, 0, 'not3'], [23.9, 'f:kalem_yaz', -8, 0, '%40'], [25.3, 'f:kalem_yaz', -6, 1, '%33'],
            [26.7, 'f:tukenmez_tik', -4, 1, 'lamba kapan'], [28.55, 'f:tukenmez_tik', -6, 0, 'lamba ac'],
            [29.05, 'f:kagit_kay', -7, 0, 'tuik'], [33.35, 'f:kagit_kay', -10, 0, 'serit1'], [33.85, 'f:kagit_kay', -10, 0, 'serit2'], [34.85, 'f:kalem_yaz', -6, 1, '3 puan'],
            [36.2, 'f:ataç', -9, 0, 'ing'], [36.9, 'f:ataç', -10, 0, 'citi'], [41.4, 'f:kalem_yaz', -9, 0, 'daralma'], [43.3, 'f:kalem_yaz', -6, 1, '2,5'],
            [44.95, 'f:bant', -8, 0, 'bant'], [45.15, 'f:kagit_kay', -9, 0, 'not8'], [46.5, 'f:kalem_yaz', -7, 1, 'tek hesap'],
            [49.05, 'f:kagit_kay', -8, 0, 'fis2'], [50.1, 'f:daktilo', -9, 0, 'fark'], [52.05, 'f:kalem_daire', -7, 1, 'fark daire'],
            [52.75, 'f:bant', -9, 0, 'bant'], [53.0, 'f:kagit_kay', -9, 0, 'cta'], [56.1, 'f:foto_birak', -7, 0, 'manset']]


def RISERS(A): return []
