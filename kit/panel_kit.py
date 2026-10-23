"""PANEL stili kiti (Ata 23 Eki 02:39 — gönderdiği Kallaway-tarzı ekran görüntüleri; "artık videoları buna döndürelim").
Spec'te: CSS_FILE='panel.css.html', SOUND_KIT='panel', EXIT_FADE=False, AV her sahnede CARD (avatar video boyunca kartta).
Dil: siyah noktalı zemin · üstte 2 satır başlık (2. satır kırmızı kutu, bir kelime italik serif) · ortada TEK parlayan grafik
· tek kelime altyazı (--cap-mode:word) · altta yuvarlak köşeli avatar kartı. Grafik alanı y=380–1150. İngilizce yazı yok.
Hareket: yumuşak (power3/expo), bulanıktan netleşme, parlayan çizgi çizimi; her giriş ≥1,5 sn ekranda (TEMPO kuralı)."""
# Güvenli alan (Ata 23 Eki 03:17: "çok aşağıda kalmışım… safe zone'da değilim"): Instagram alt arayüzü y>1450, sağ aksiyon
# butonları x>950 / y>1100. Kart artık y=1065–1460, x=90–990; grafikler 'stage' ile y=410–965'e ölçeklenir (STAGE_S).
CARD = [90, 1065, 900, 395, 36, .28]
STAGE_S = .72

JS = r'''
// ---- güvenli alan: başlık dışındaki her sahne öğesi .stage içine alınır, y=380'den başlayıp STAGE_S oranında küçülür
document.querySelectorAll('section.scene').forEach(sc=>{const st=document.createElement('div');st.className='stage';
 [...sc.children].filter(e=>!e.classList.contains('ttl')).forEach(e=>st.appendChild(e));sc.appendChild(st);});
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
