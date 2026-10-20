#!/usr/bin/env python3
"""Series cover (thumbnail) for Reels / TikTok / Shorts — one consistent Paranın Dili look.

  python3 engine/cover.py <slug> "<title, *red words* in stars>" "<KICKER LABEL>" <avatar video> [frame_sec]
  -> public/covers/<slug>.jpg (1080x1920 JPEG)

Safe zones: everything that matters sits inside y 300..1620 so the Instagram profile grid crop (3:4, centre)
and the feed crop (4:5) never cut the title or the face. Title: max ~38 characters, 2–3 lines."""
import html, os, re, shutil, subprocess, sys, tempfile

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
KIT = os.path.join(REPO, 'kit')
CHROME = os.environ.get('HYPERFRAMES_BROWSER_PATH', '/opt/pw-browsers/chromium-1194/chrome-linux/chrome')

TPL = '''<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>
__FONTS__
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#f2ede2}
body{position:relative;font-family:'Inter Tight';color:#161412}
.grain{position:absolute;inset:0;background:repeating-linear-gradient(0deg,rgba(22,20,18,.025) 0 2px,transparent 2px 5px)}
.mast{position:absolute;left:60px;right:60px;top:300px}
.mast .rule{height:6px;background:#161412}
.mast .row{display:flex;justify-content:space-between;align-items:baseline;padding:12px 0 8px}
.mast .name{font:400 74px/1 'DM Serif Display'}
.mast .ed{font:500 24px 'IBM Plex Mono';letter-spacing:.08em}
.mast .thin{height:2px;background:#161412}
.kick{position:absolute;left:60px;top:470px;font:700 30px 'IBM Plex Mono';letter-spacing:.16em;color:#c8261b}
.title{position:absolute;left:56px;top:530px;width:968px;font:400 128px/1.0 'DM Serif Display';letter-spacing:-.015em}
.title em{font-style:normal;color:#c8261b}
.photo{position:absolute;left:300px;top:900px;width:480px;height:674px;border:6px solid #161412;box-shadow:16px 16px 0 #161412;overflow:hidden;background:#000}
.photo img{width:100%;height:100%;object-fit:cover;object-position:50% 30%}
.stamp{position:absolute;right:60px;bottom:330px;font:500 24px 'IBM Plex Mono';letter-spacing:.1em;color:rgba(22,20,18,.65)}
</style></head><body><div class="grain"></div>
<div class="mast"><div class="rule"></div><div class="row"><span class="name">Paranın Dili</span><span class="ed">@ATAMERTUYSALER</span></div><div class="thin"></div></div>
<div class="kick">__KICK__</div>
<div class="title" id="t">__TITLE__</div>
<div class="photo" id="p"><img src="face.jpg"></div>
<script>
// place the photo under the real title height; keep it inside the grid-safe zone (bottom <= 1620)
const t=document.getElementById('t'), p=document.getElementById('p');
function place(){const top=t.offsetTop+t.offsetHeight+60, h=Math.min(674, 1620-top), w=Math.round(h*480/674);
 p.style.top=top+'px'; p.style.height=h+'px'; p.style.width=w+'px'; p.style.left=Math.round((1080-w)/2)+'px';}
place(); document.fonts.ready.then(place);
</script>
</body></html>'''

TPL_KOYU = """<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>
__FONTS__
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#0d0c0a}
body{position:relative;font-family:'Inter Tight';color:#f3efe6}
.bg{position:absolute;inset:0;background:url(face.jpg) center 30%/cover}
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,12,10,.0) 0%,rgba(13,12,10,.0) 38%,rgba(13,12,10,.82) 60%,rgba(13,12,10,.96) 100%)}
.top{position:absolute;left:60px;right:60px;top:290px;display:flex;justify-content:space-between;align-items:center}
.brand{font:900 34px 'Inter Tight';letter-spacing:-.01em;background:#e8b931;color:#0d0c0a;padding:8px 18px;border-radius:8px}
.kick{font:700 26px 'IBM Plex Mono';letter-spacing:.14em;color:#f3efe6;background:rgba(13,12,10,.6);padding:8px 14px;border-radius:6px}
.title{position:absolute;left:56px;right:56px;bottom:330px;font:900 132px/0.95 'Inter Tight';letter-spacing:-.045em;text-transform:none}
.title em{font-style:normal;color:#e8b931}
</style></head><body><div class="bg"></div><div class="shade"></div>
<div class="top"><span class="brand">PARANIN DİLİ</span><span class="kick">__KICK__</span></div>
<div class="title">__TITLE__</div></body></html>"""

TPL_BANT = """<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>
__FONTS__
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#0d0c0a}
body{position:relative;font-family:'Inter Tight'}
.bg{position:absolute;inset:0;background:url(face.jpg) center 30%/cover;filter:saturate(1.05) contrast(1.05)}
.vig{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 35%,rgba(0,0,0,0) 45%,rgba(0,0,0,.55) 100%)}
.wrap{position:absolute;left:50px;right:50px;bottom:360px;display:flex;flex-direction:column;align-items:flex-start;gap:14px}
.line{font:900 112px/1 'Inter Tight';letter-spacing:-.04em;color:#0d0c0a;background:#f3efe6;padding:10px 26px 16px;transform:rotate(-1.5deg);box-shadow:10px 10px 0 #0d0c0a}
.line.em{background:#ff4a3d;color:#fff}
.tag{position:absolute;left:50px;top:290px;font:800 30px 'Inter Tight';letter-spacing:.02em;color:#fff;background:#0d0c0a;padding:10px 18px;border-left:10px solid #ff4a3d}
</style></head><body><div class="bg"></div><div class="vig"></div>
<div class="tag">PARANIN DİLİ · __KICK__</div>
<div class="wrap">__LINES__</div></body></html>"""

TPL_LUKS = """<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>
__FONTS__
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#07070a}
body{position:relative;font-family:'Inter Tight';color:#f5f1e8}
.bg{position:absolute;inset:0;background:url(face.jpg) center 28%/cover;filter:brightness(.62) contrast(1.12) saturate(.72)}
.tone{position:absolute;inset:0;background:linear-gradient(180deg,rgba(7,7,10,.55) 0%,rgba(7,7,10,0) 22%,rgba(7,7,10,0) 42%,rgba(7,7,10,.86) 66%,rgba(7,7,10,.97) 100%)}
.vig{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 38%,rgba(0,0,0,0) 40%,rgba(0,0,0,.6) 100%)}
.grain{position:absolute;inset:0;opacity:.07;background:repeating-radial-gradient(circle at 30% 40%,#fff 0 1px,transparent 1px 3px)}
.frame{position:absolute;left:44px;right:44px;top:244px;bottom:244px;border:2px solid rgba(212,175,55,.55)}
.brand{position:absolute;left:0;right:0;top:300px;text-align:center;font:700 30px 'Inter Tight';letter-spacing:.55em;padding-left:.55em;color:#d4af37}
.rule{position:absolute;left:50%;top:352px;width:90px;height:2px;margin-left:-45px;background:#d4af37}
.kick{position:absolute;left:0;right:0;top:1160px;text-align:center;font:500 28px 'IBM Plex Mono';letter-spacing:.32em;padding-left:.32em;color:rgba(245,241,232,.75)}
.title{position:absolute;left:70px;right:70px;top:1215px;text-align:center;font-family:'Playfair Display';font-weight:900;line-height:.92;letter-spacing:-.01em;color:#f5f1e8}
.title em{font-style:italic;font-weight:700;background:linear-gradient(180deg,#f6e3a1 0%,#d4af37 45%,#a8841f 100%);-webkit-background-clip:text;background-clip:text;color:transparent;padding:0 .04em}
.handle{position:absolute;left:0;right:0;bottom:285px;text-align:center;font:600 24px 'Inter Tight';letter-spacing:.4em;padding-left:.4em;color:rgba(212,175,55,.85)}
</style></head><body><div class="bg"></div><div class="tone"></div><div class="vig"></div><div class="grain"></div><div class="frame"></div>
<div class="brand">PARANIN DİLİ</div><div class="rule"></div>
<div class="kick">__KICK__</div>
<div class="title" id="t">__TITLE__</div>
<div class="handle">@ATAMERTUYSALER</div>
<script>
// fit 2-3 words: largest size where every line fits 940px and the block ends above y=1590
const t=document.getElementById('t');
function fit(){let s=250;t.style.fontSize=s+'px';
 while(s>90&&(t.scrollWidth>t.clientWidth+2||t.offsetTop+t.offsetHeight>1540)){s-=4;t.style.fontSize=s+'px';}}
fit();document.fonts.ready.then(fit);
</script></body></html>"""

TPL_VURUCU = """<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>
__FONTS__
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#000}
body{position:relative}
.bg{position:absolute;inset:-40px;background:url(face.jpg) center 26%/cover;transform:scale(1.18);transform-origin:50% 30%;filter:saturate(1.35) contrast(1.18) brightness(1.06)}
.warm{position:absolute;inset:0;background:linear-gradient(160deg,rgba(255,170,60,.18),rgba(0,0,0,0) 45%,rgba(40,90,255,.16));mix-blend-mode:overlay}
.vig{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 34%,rgba(0,0,0,0) 38%,rgba(0,0,0,.7) 100%)}
.low{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 52%,rgba(0,0,0,.55) 78%,rgba(0,0,0,.75) 100%)}
.wrap{position:absolute;left:40px;right:40px;top:1060px;text-align:center;transform:rotate(-3deg)}
.l{display:block;font-family:'Anton';text-transform:uppercase;line-height:.92;letter-spacing:.005em;color:#fff;
   -webkit-text-stroke:10px #000;paint-order:stroke fill;text-shadow:0 10px 0 #000,0 18px 30px rgba(0,0,0,.6)}
.l.y{color:#ffd21f}
.l.r{color:#ff3b30}
.tag{position:absolute;left:0;right:0;top:300px;text-align:center}
.tag span{display:inline-block;font:400 40px 'Anton';letter-spacing:.06em;color:#000;background:#ffd21f;padding:6px 22px 8px;transform:rotate(-2deg);box-shadow:6px 6px 0 #000}
</style></head><body><div class="bg"></div><div class="warm"></div><div class="vig"></div><div class="low"></div>
<div class="tag"><span>__KICK__</span></div>
<div class="wrap" id="w">__LINES__</div>
<script>
// each line auto-sized to fill ~1000px width; whole block ends above y=1600
const w=document.getElementById('w');
function fit(){const L=[...w.querySelectorAll('.l')];L.forEach(l=>{let s=330;l.style.fontSize=s+'px';l.style.whiteSpace='nowrap';
  while(s>80&&l.scrollWidth>1000){s-=6;l.style.fontSize=s+'px';}});
 let k=1;while(w.offsetTop+w.offsetHeight>1600&&k>.5){k-=.04;L.forEach(l=>l.style.fontSize=(parseFloat(l.style.fontSize)*0.96)+'px');}}
fit();document.fonts.ready.then(fit);
</script></body></html>"""

THEMES = {'gold': ('#ffb703', '#3a2600'), 'red': ('#ff3b30', '#3a0603'), 'blue': ('#2f7bff', '#04163a'), 'green': ('#22c55e', '#03260f')}
TPL_SAHNE = """<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>
__FONTS__
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:__DARK__}
body{position:relative}
.bg{position:absolute;inset:-60px;background:url(face.jpg) center 30%/cover;filter:blur(26px) brightness(.45) saturate(1.4)}
.glow{position:absolute;left:50%;top:880px;width:1500px;height:1500px;margin:-750px 0 0 -750px;border-radius:50%;
      background:radial-gradient(circle,__ACC__ 0%,rgba(0,0,0,0) 60%);opacity:.55}
.rays{position:absolute;inset:0;background:repeating-conic-gradient(from 0deg at 50% 46%,rgba(255,255,255,.07) 0deg 6deg,rgba(255,255,255,0) 6deg 18deg);
      -webkit-mask:radial-gradient(circle at 50% 46%,#000 0 30%,transparent 70%);mask:radial-gradient(circle at 50% 46%,#000 0 30%,transparent 70%)}
.back{position:absolute;left:0;right:0;top:290px;text-align:center;font-family:'Anton';text-transform:uppercase;line-height:.9;color:#fff;
      -webkit-text-stroke:10px #000;paint-order:stroke fill;text-shadow:0 12px 0 #000}
.prop{position:absolute;font-family:'Noto Color Emoji';filter:drop-shadow(0 18px 18px rgba(0,0,0,.6))}
.p1{left:-10px;top:760px;font-size:240px;transform:rotate(-14deg)}
.p2{right:-10px;top:880px;font-size:210px;transform:rotate(12deg)}
.who{position:absolute;left:50%;bottom:-40px;width:940px;margin-left:-470px;filter:__EDGE__}
.fade{position:absolute;left:0;right:0;bottom:0;height:520px;background:linear-gradient(180deg,rgba(0,0,0,0),__DARK__ 85%)}
.front{position:absolute;left:30px;right:30px;top:1230px;text-align:center;transform:rotate(-3deg)}
.front span{display:inline-block;font-family:'Anton';text-transform:uppercase;line-height:.92;color:#ffd21f;-webkit-text-stroke:12px #000;paint-order:stroke fill;
      text-shadow:0 12px 0 #000,0 22px 40px rgba(0,0,0,.7)}
.front span.w{color:#fff}
.tag{position:absolute;left:0;right:0;top:1190px;text-align:center}
.tag b{display:inline-block;font:400 38px 'Anton';letter-spacing:.06em;color:#000;background:__ACC__;padding:4px 20px 6px;transform:rotate(-3deg);box-shadow:6px 6px 0 #000}
</style></head><body><div class="bg"></div><div class="glow"></div><div class="rays"></div>
<div class="back"><span id="b" style="display:inline-block">__BACK__</span></div>
<img class="who" src="cut.png">
<div class="fade"></div>
<div class="prop p1">__P1__</div><div class="prop p2">__P2__</div>
<div class="front" id="f">__FRONT__</div>
<script>
function fitOne(el,maxW,start){let s=start;el.style.fontSize=s+'px';el.style.whiteSpace='nowrap';while(s>70&&el.scrollWidth>maxW){s-=6;el.style.fontSize=s+'px';}}
function fit(){fitOne(document.getElementById('b'),1000,300);document.querySelectorAll('#f span').forEach(x=>fitOne(x,1000,240));
 const f=document.getElementById('f');let g=0;while(f.offsetTop+f.offsetHeight>1610&&g<20){g++;f.querySelectorAll('span').forEach(x=>x.style.fontSize=(parseFloat(x.style.fontSize)*.95)+'px');}}
fit();document.fonts.ready.then(fit);
</script></body></html>"""


def feather(path, shrink=2, blur=1.6):
    """Pull the matte in a hair and soften it so no background fringe / hard cut-out edge is left."""
    from PIL import Image, ImageFilter
    im = Image.open(path).convert('RGBA'); a = im.getchannel('A')
    a = a.filter(ImageFilter.MinFilter(2 * shrink + 1)).filter(ImageFilter.GaussianBlur(blur))
    im.putalpha(a); im.save(path)


def main(slug, title, kick, video, at='1.2'):
    out_dir = os.path.join(REPO, 'public', 'covers'); os.makedirs(out_dir, exist_ok=True)
    tmp = tempfile.mkdtemp()
    shutil.copytree(os.path.join(KIT, 'fonts'), os.path.join(tmp, 'fonts'))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(at), '-i', video, '-frames:v', '1', '-q:v', '2', os.path.join(tmp, 'face.jpg')], check=True)
    t = html.escape(title)
    t = re.sub(r'\*(.+?)\*', r'<em>\1</em>', t)
    style = os.environ.get('COVER_STYLE', 'gazete')
    fonts = open(os.path.join(KIT, 'fonts.css')).read()
    if style == 'sahne':
        # title 'ARKA / *ÖN SATIR* / ön satır2'  -> first chunk behind the head, the rest in front (*..* yellow, plain white)
        parts = [x.strip() for x in title.split('/')]
        front = '<br>'.join(f'<span class="{"" if x.startswith("*") else "w"}">{html.escape(x.strip("*"))}</span>' for x in parts[1:])
        acc, dark = THEMES.get(os.environ.get('COVER_THEME', 'gold'), THEMES['gold'])
        props = (os.environ.get('COVER_PROPS', '') + '  ').split(' ')
        hf = os.environ.get('HYPERFRAMES_BROWSER_PATH', CHROME)
        subprocess.run(f'npx --yes hyperframes@0.8.174 remove-background {os.path.join(tmp, "face.jpg")} -o {os.path.join(tmp, "cut.png")} >/dev/null 2>&1',
                       shell=True, check=True, env=dict(os.environ, HYPERFRAMES_BROWSER_PATH=hf))
        # no white sticker outline (Ata, 21 Eki: it cut the hair badly). Feather the matte edge instead.
        feather(os.path.join(tmp, 'cut.png'))
        edge = os.environ.get('COVER_EDGE', 'isik')
        edges = {'dogal': 'drop-shadow(0 30px 40px rgba(0,0,0,.65))',
                 'isik': 'drop-shadow(0 0 2px rgba(255,255,255,.35)) drop-shadow(0 0 28px __ACC__) drop-shadow(0 30px 40px rgba(0,0,0,.65))',
                 'golge': 'drop-shadow(0 0 14px rgba(0,0,0,.9)) drop-shadow(0 0 30px rgba(0,0,0,.6)) drop-shadow(0 30px 40px rgba(0,0,0,.6))'}
        page = TPL_SAHNE.replace('__EDGE__', edges.get(edge, edges['isik'])).replace('__FONTS__', fonts).replace('__BACK__', html.escape(parts[0].strip('*'))).replace('__FRONT__', front) \
            .replace('__ACC__', acc).replace('__DARK__', dark).replace('__P1__', props[0]).replace('__P2__', props[1])
    elif style == 'vurucu':
        # 'satır1 / *satır2* / !satır3!'  -> *..* yellow, !..! red, plain white; one line per '/'
        def line(p):
            c = 'y' if p.startswith('*') else ('r' if p.startswith('!') else '')
            return f'<span class="l {c}">{html.escape(p.strip("*!"))}</span>'
        page = TPL_VURUCU.replace('__FONTS__', fonts).replace('__KICK__', html.escape(kick.upper())).replace('__LINES__', ''.join(line(x.strip()) for x in title.split('/')))
    elif style == 'luks':
        page = TPL_LUKS.replace('__FONTS__', fonts).replace('__KICK__', html.escape(kick.upper())).replace('__TITLE__', t.replace(' / ', '<br>'))
    elif style == 'koyu':
        page = TPL_KOYU.replace('__FONTS__', fonts).replace('__KICK__', html.escape(kick.upper())).replace('__TITLE__', t)
    elif style == 'bant':
        # each '/'-separated chunk is one band; a chunk wrapped in *..* becomes the red band
        parts = [x.strip() for x in title.split('/')]
        lines = ''.join(f'<div class="line{" em" if p.startswith("*") else ""}">{html.escape(p.strip("*"))}</div>' for p in parts)
        page = TPL_BANT.replace('__FONTS__', fonts).replace('__KICK__', html.escape(kick.upper())).replace('__LINES__', lines)
    else:
        page = TPL.replace('__FONTS__', fonts).replace('__KICK__', html.escape(kick.upper())).replace('__TITLE__', t)
    hp = os.path.join(tmp, 'cover.html'); open(hp, 'w').write(page)
    png = os.path.join(tmp, 'cover.png')
    subprocess.run([CHROME, '--headless=new', '--no-sandbox', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
                    '--window-size=1080,1920', '--virtual-time-budget=4000', f'--screenshot={png}', 'file://' + hp],
                   check=True, capture_output=True)
    out = os.path.join(out_dir, f'{slug}.jpg' if style == os.environ.get('COVER_DEFAULT', style) else f'{slug}_{style}.jpg')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', png, '-vf', 'scale=1080:1920', '-q:v', '2', out], check=True)
    shutil.rmtree(tmp)
    print('COVER', out)


if __name__ == '__main__':
    if len(sys.argv) < 5: sys.exit(__doc__)
    main(*sys.argv[1:])
