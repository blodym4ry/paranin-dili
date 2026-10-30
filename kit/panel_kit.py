"""PANEL stili kiti (Ata 23 Eki 02:39 — gönderdiği Kallaway-tarzı ekran görüntüleri; "artık videoları buna döndürelim").
Spec'te: CSS_FILE='panel.css.html', SOUND_KIT='panel', EXIT_FADE=False, AV her sahnede CARD (avatar video boyunca kartta).
Dil: siyah noktalı zemin · üstte 2 satır başlık (2. satır kırmızı kutu, bir kelime italik serif) · ortada TEK parlayan grafik
· tek kelime altyazı (--cap-mode:word) · altta yuvarlak köşeli avatar kartı. Grafik alanı y=380–1150. İngilizce yazı yok.
Hareket: yumuşak (power3/expo), bulanıktan netleşme, parlayan çizgi çizimi; her giriş ≥1,5 sn ekranda (TEMPO kuralı)."""
# Güvenli alan (Ata 23 Eki 03:17: "çok aşağıda kalmışım… safe zone'da değilim"): Instagram alt arayüzü y>1450, sağ aksiyon
# butonları x>950 / y>1100. Kart artık y=1065–1460, x=90–990; grafikler 'stage' ile y=410–965'e ölçeklenir (STAGE_S).
CARD = [90, 1065, 900, 395, 36, .28]   # ESKİ (kullanma): Ata 16:17 "çenem ve saçlarım gözükmüyor"
# Ata 23 Eki 16:17: avatar SADECE giriş + vurgu + çıkışta, o sahnelerde BÜYÜK kartta (saç ve çene dahil tüm baş görünür).
# Diğer sahnelerde avatar yok, grafikler tam boy (y=380–1150), altyazı y=1215.
HERO = [184, 470, 688, 946, 40, .10]   # Ata 29 Eki güvenli alan: kart+altın çerçeve x 176–880 (sağ ray x>880), y 462–1424
# ESKİ HERO [140,490,800,940] sağ kenarı 948'e taşıyordu (beğen/yorum rayı altı)   # Ata 24 Eki 01:32: avatar ≤ ekranın yarısı (yükseklik ≤960), tam ekran YASAK, tüm yüz görünür
HALF = [100, 240, 780, 700, 30, .10]    # Ata 29 Eki: kenardan kenara değil; x 100–880, y 240–940 (üst çubuk altı)      # üst yarı layout (tam genişlik, y=110–990); başlık altına (y≈1010) alınır. Alt yarı OLMAZ: IG arayüzü y>1450 çeneyi keser
PIP = [118, 1212, 212, 212, 106, .14]   # Ata 30 Eki 12:23: "ara ara olmalıyım… ufacık da olsa bir yuvarlağın içinde" → grafik sahnelerinde sol altta, altyazının solunda yuvarlak avatar (altın halka). x 118–330, y 1212–1424 (güvenli alan içi)
STAGE_S = 1

JS = r'''
// ---- güvenli alan: başlık dışındaki her sahne öğesi .stage içine alınır, y=380'den başlayıp STAGE_S oranında küçülür
document.querySelectorAll('section.scene').forEach(sc=>{const st=document.createElement('div');st.className='stage';
 [...sc.children].filter(e=>!e.classList.contains('ttl')).forEach(e=>st.appendChild(e));sc.appendChild(st);
 if(AV[sc.id]&&!(AV[sc.id][1]>1100)) st.style.display='none';});   // HERO sahnesinde sadece başlık + büyük kart; PIP (yuvarlak) sahnede grafikler görünür
// altyazı konumu: avatarlı sahnede kartın göğüs hizası, grafik sahnesinde grafiklerin altı
const isPip=v=>!!v&&v[1]>1100;
SC.forEach(([id,a])=>tl.set('#caps',{top:isPip(AV[id])?1262:(AV[id]?1290:1215),left:isPip(AV[id])?352:60,right:isPip(AV[id])?200:60,scale:isPip(AV[id])?.8:1,transformOrigin:'50% 50%'},Math.max(0,a-.01)));
// yuvarlak avatar (PIP) için altın halka
{const P=Object.values(AV).find(isPip);if(P){const r=document.createElement('div');r.id='pipr';
 Object.assign(r.style,{position:'absolute',left:(P[0]-5)+'px',top:(P[1]-5)+'px',width:(P[2]+10)+'px',height:(P[3]+10)+'px',borderRadius:'50%',
  border:'5px solid #e8b931',boxShadow:'0 0 22px rgba(232,185,49,.5)',boxSizing:'border-box',opacity:0,zIndex:6,pointerEvents:'none'});
 document.getElementById('avbox').after(r);
 SC.forEach(([id,a,b])=>{if(isPip(AV[id])){tl.fromTo('#pipr',{opacity:0},{opacity:1,duration:.35},a);tl.set('#pipr',{opacity:0},Math.max(a+.1,b-.05));}});}}
// ---- PANEL hareket dili
const ttl=(s,t)=>tl.fromTo(s,{opacity:0,y:-18,filter:'blur(14px)'},{opacity:1,y:0,filter:'blur(0px)',duration:.55,ease:'power3.out'},t);
const pop=(s,t,o={})=>tl.fromTo(s,{opacity:0,scale:o.s??.86,y:o.y??0},{opacity:1,scale:1,y:0,duration:o.d??.5,ease:'back.out(1.6)'},t);
const fin=(s,t,o={})=>tl.fromTo(s,{opacity:0,y:o.y??30,filter:'blur(10px)'},{opacity:1,y:0,filter:'blur(0px)',duration:o.d??.5,ease:'power3.out'},t);
const fout=(s,t,d=.3)=>tl.to(s,{opacity:0,filter:'blur(8px)',duration:d,ease:'power2.in'},t);
const dr=(s,t,d=.8,e='power2.inOut')=>tl.fromTo(s,{strokeDashoffset:1},{strokeDashoffset:0,duration:d,ease:e},t);
const strike=(s,t)=>tl.fromTo(s,{scaleX:0},{scaleX:1,duration:.35,ease:'power3.out',transformOrigin:'0% 50%'},t);
'''


def title(id_, l1, l2):
    """İki satır başlık; l2 kırmızı kutuda. İtalik kelime için <i>..</i> kullan."""
    return f'<div class="ttl" id="{id_}" style="opacity:0">{l1}<br><span class="l2">{l2}</span></div>'


def line_path(pts, x0, y0, w, h, xmax, vmax):
    return ' '.join(('M' if i == 0 else 'L') + f'{x0 + x / xmax * w:.0f},{y0 + h - v / vmax * h:.0f}' for i, (x, v) in enumerate(pts))


def glow_path(id_, d, color='#ff3b30', width=7):
    """Parlayan çizgi: blur'lu kopya + net çizgi; ikisi de pathLength=1 (dr('#id, #id_g', t) ile çizilir)."""
    return (f'<path id="{id_}_g" d="{d}" pathLength="1" fill="none" stroke="{color}" stroke-width="{width * 2.4:.0f}" filter="url(#glf)" opacity=".75" style="stroke-dasharray:1;stroke-dashoffset:1"/>'
            f'<path id="{id_}" d="{d}" pathLength="1" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round" style="stroke-dasharray:1;stroke-dashoffset:1"/>')


SVG_DEFS = '<defs><filter id="glf" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="9"/></filter></defs>'
