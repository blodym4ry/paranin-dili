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
FULL = [0, 0, 1080, 1920, 0, .5]
AV = {'s1': HERO if MODE == 'hero' else FULL}
def scenes(A): return [('s1', 0, DUR)]
EXTRA_CSS = """<style>.ttl{z-index:5}""" + ("""#root::after{content:'';position:absolute;left:0;right:0;top:0;height:560px;z-index:4;background:linear-gradient(#000d,#0000)}
.ttl{font-size:76px}.ttl i{font-size:82px}""" if MODE == 'full' else '') + """</style>"""
SCENE_HTML = """<section id="s1" class="scene clip"><div class="ttl" id="t1">Herkes Seçimden Korkuyor<br><span class="l2">Ama <i>Tersi</i> Oldu</span></div></section>"""
SCENE_JS = JS + "tl.set('#t1',{opacity:1},0);"
def SFX(A): return []
def RISERS(A): return []
