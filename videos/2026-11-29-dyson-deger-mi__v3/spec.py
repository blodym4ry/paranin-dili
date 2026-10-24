import os
from panel_kit import JS, HERO
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .02, 2)
REPL = [(['Dai',"sın'lar"], "Dyson'lar"), (['Dai','sın'], 'Dyson'), (['on','dört'], '14'), (['altmış'], '60'), (['beş','bin','dört','yüz'], '5.400 TL')]
EM = set(); RED = set()
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False
MODE = 'full'
FULL = [0, 0, 1080, 1920, 0, .5]   # YASAK (Ata 24 Eki: tam ekran AI hissi verir) — 'full' modu artık alt-yarı layout'a gider
from panel_kit import HALF
AV = {'s1': HERO if MODE == 'hero' else HALF}
def scenes(A): return [('s1', 0, DUR)]
EXTRA_CSS = """<style>.ttl{z-index:5}""" + ("""#avc{-webkit-mask-image:linear-gradient(#000 80%,transparent)}
.ttl{top:1010px;font-size:70px}.ttl i{font-size:76px}""" if MODE == 'full' else '') + """</style>"""
SCENE_HTML = """<section id="s1" class="scene clip"><div class="ttl" id="t1">Dyson Alacaksan<br><span class="l2">Önce Bu <i>3 Rakama</i> Bak</span></div></section>"""
SCENE_JS = JS + "tl.set('#t1',{opacity:1},0);"
def SFX(A): return []
def RISERS(A): return []
