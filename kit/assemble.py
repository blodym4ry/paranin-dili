"""KİNETİK house-style assembler. A video folder provides spec.py with:
  SRT (path), DUR (float), REPL (list of (words, display)), EM (set), RED (set),
  scenes(A) -> list of (id, start, end)  where A(phrase, after=0) finds a word time,
  AV dict id -> [x,y,w,h,r] avatar window, SCENE_HTML (str), SCENE_JS (str, may use st('id')),
  SFX list [t, kind, dB, accent(0/1), note], RISERS list [t, 'sharp'|'metallic', dB]
usage: python3 assemble.py <video_dir>   -> writes index.html + edl_audio.json"""
import json, re, sys, os, importlib.util
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'engine'))
from build_edl import parse_srt, words_from_segs, tl, find
import build_edl
KIT = os.path.dirname(os.path.abspath(__file__))
vd = os.path.abspath(sys.argv[1])
spec_p = os.path.join(vd, 'spec.py')
sp = importlib.util.spec_from_file_location('spec', spec_p); S = importlib.util.module_from_spec(sp); sp.loader.exec_module(S)
build_edl.REPL[:0] = S.REPL
words = build_edl.merge(words_from_segs(parse_srt(S.SRT)))
open(os.path.join(vd, 'words.txt'), 'w').write(' '.join(f"{x['w']}@{x['t0']:.2f}" for x in words))
def A(p, after=0):
    t = find(words, p, after)
    if t is None: raise SystemExit(f'anchor not found: {p!r} after {after}')
    return t
SC = S.scenes(A)
clean = lambda w: tl(re.sub(r'[.,:!?…"\']+$', '', w))
def isem(w): return bool(re.search(r'\d', w)) or clean(w) in S.EM
chunks, cur = [], []
for w in words:
    if isem(w['w']) and cur and any(isem(x['w']) for x in cur): chunks.append(cur); cur = []
    cur.append(w)
    if len(cur) >= 3 or len(' '.join(x['w'] for x in cur)) >= 16 or re.search(r'[.?!,:]"?$', w['w']): chunks.append(cur); cur = []
if cur: chunks.append(cur)
caps = []
for i, ch in enumerate(chunks):
    nxt = chunks[i + 1][0]['t0'] if i + 1 < len(chunks) else S.DUR
    caps.append({'a': round(ch[0]['t0'], 3), 'b': round(min(nxt, ch[-1]['t1'] + .35), 3),
                 'w': [[re.sub(r'[.,:!…"]+$', '', x['w']).replace('"', ''), round(x['t0'], 3), 2 if clean(x['w']) in S.RED else (1 if isem(x['w']) else 0)] for x in ch]})
css = open(os.path.join(KIT, getattr(S, 'CSS_FILE', 'kinetik.css.html'))).read().replace('__FONTS__', open(os.path.join(KIT, 'fonts.css')).read())
core = open(os.path.join(KIT, 'kinetik_core.js')).read().replace('__CAPS__', json.dumps(caps, ensure_ascii=False)) \
    .replace('__SCENES__', json.dumps(SC)).replace('__AV__', json.dumps(S.AV)).replace('__DUR__', str(S.DUR))
exitf = "SC.slice(0,-1).forEach(([id,a,b])=>{tl.to(`#${id} > *`,{opacity:0,duration:.22,ease:'power2.in'},b-.45);});\n"
html = f'''<!doctype html>
<html lang="tr" data-resolution="portrait">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1920" />
<script src="media/gsap.min.js"></script>
{css}
{getattr(S, 'EXTRA_CSS', '')}
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{S.DUR}" data-width="1080" data-height="1920">
  <div class="bg"><div id="glow"></div><div id="grid"></div></div>
{S.SCENE_HTML}
  <div id="avbox"><div id="avw"><div id="avc"><video id="av" class="clip" src="media/av.mp4" muted playsinline data-start="0" data-duration="{S.DUR}" data-media-start="0" data-track-index="1"></video></div></div></div>
  <div id="caps"></div>
</div>
<script>
{core}
{S.SCENE_JS}
{exitf}window.__timelines['main']=tl;
</script>
</body>
</html>'''
# fill data-start/duration for scene sections
for sid, a, b in SC:
    html = html.replace(f'<section id="{sid}" class="scene clip">', f'<section id="{sid}" class="scene clip" data-start="{a:.3f}" data-duration="{b - a:.3f}">')
open(os.path.join(vd, 'index.html'), 'w').write(html)
L = [{'t': 0, 's': 'K'}] + [{'t': a - .3, 's': 'K'} for _, a, _ in SC[1:]]
json.dump({'dur': S.DUR, 'bpm': 96, 'layout': L, 'layouts': {'K': {'av': {'o': 1}}}, 'emph': [], 'sfx': S.SFX(A) if callable(S.SFX) else S.SFX,
           'risers': S.RISERS(A) if callable(S.RISERS) else S.RISERS}, open(os.path.join(vd, 'edl_audio.json'), 'w'))
print(len(caps), 'caps;', ' '.join(f'{s}:{a:.2f}-{b:.2f}' for s, a, b in SC))
