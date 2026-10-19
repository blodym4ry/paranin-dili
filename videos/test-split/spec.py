import os
CSS_FILE = 'gazete.css.html'
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .05, 2)
REPL = []
EM = {'zam', 'tuzak'}
RED = {'tuzak'}
FRONT = [250, 375, 580, 815, 6]
AV = {'s1': None, 's2': FRONT}
EXTRA_CSS = '<style>#s1{transform:translateY(170px)}</style>'
def scenes(A):
    t2 = round(A('Sorun') - .1, 3)
    return [('s1', 0, t2), ('s2', t2, DUR)]
def SFX(A): return [[A('tuzak.'), 'impact', -8, 1, 'tuzak']]
def RISERS(A): return []
SCENE_HTML = r'''
  <section id="s1" class="scene clip">
    <div class="a lab" id="s1l" style="left:60px;top:400px">MAAŞ · ZAM · HARCAMA</div>
    <div class="a big" id="s1v" style="left:52px;top:460px;font-size:170px">+%30 zam</div>
    <div class="a h red" id="s1d" style="left:60px;top:700px;font-size:110px">+%40 harcama</div>
  </section>
  <section id="s2" class="scene clip">
    <div class="a h red" id="s2t" style="left:0;right:0;top:1330px;text-align:center;font-size:120px">TUZAK</div>
  </section>
'''
SCENE_JS = r'''
inn('#s1l',.15); inn('#s1v',.3); slam('#s1d',1.4);
const s2=st('s2'); slam('#s2t',s2+.5);
'''
