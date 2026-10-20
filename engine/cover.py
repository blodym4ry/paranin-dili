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


def main(slug, title, kick, video, at='1.2'):
    out_dir = os.path.join(REPO, 'public', 'covers'); os.makedirs(out_dir, exist_ok=True)
    tmp = tempfile.mkdtemp()
    shutil.copytree(os.path.join(KIT, 'fonts'), os.path.join(tmp, 'fonts'))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(at), '-i', video, '-frames:v', '1', '-q:v', '2', os.path.join(tmp, 'face.jpg')], check=True)
    t = html.escape(title)
    t = re.sub(r'\*(.+?)\*', r'<em>\1</em>', t)
    style = os.environ.get('COVER_STYLE', 'gazete')
    fonts = open(os.path.join(KIT, 'fonts.css')).read()
    if style == 'koyu':
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
