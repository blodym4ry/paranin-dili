import os
from panel_kit import JS, HERO
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .02, 2)
REPL = []
EM = set(); RED = set()
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False
MODE = 'full'
from panel_kit import HALF
AV = {'s1': HERO if MODE == 'hero' else HALF}
def scenes(A): return [('s1', 0, DUR)]
EXTRA_CSS = """<style>.ttl{z-index:5}""" + ("""#avc{-webkit-mask-image:linear-gradient(#000 80%,transparent)}
.ttl{top:1010px;font-size:70px}.ttl i{font-size:76px}""" if MODE == 'full' else '') + """</style>"""
SCENE_HTML = """<section id="s1" class="scene clip"><div class="ttl" id="t1">Herkes Seçimden Korkuyor<br><span class="l2">Ama <i>Tersi</i> Oldu</span></div></section>"""
SCENE_JS = JS + "tl.set('#t1',{opacity:1},0);"
def SFX(A): return []
def RISERS(A): return []
