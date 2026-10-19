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
const top=t.offsetTop+t.offsetHeight+60, h=Math.min(674, 1620-top), w=Math.round(h*480/674);
p.style.top=top+'px'; p.style.height=h+'px'; p.style.width=w+'px'; p.style.left=Math.round((1080-w)/2)+'px';
</script>
</body></html>'''


def main(slug, title, kick, video, at='1.2'):
    out_dir = os.path.join(REPO, 'public', 'covers'); os.makedirs(out_dir, exist_ok=True)
    tmp = tempfile.mkdtemp()
    shutil.copytree(os.path.join(KIT, 'fonts'), os.path.join(tmp, 'fonts'))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(at), '-i', video, '-frames:v', '1', '-q:v', '2', os.path.join(tmp, 'face.jpg')], check=True)
    t = html.escape(title)
    t = re.sub(r'\*(.+?)\*', r'<em>\1</em>', t)
    page = TPL.replace('__FONTS__', open(os.path.join(KIT, 'fonts.css')).read()).replace('__KICK__', html.escape(kick.upper())) \
              .replace('__TITLE__', t)
    hp = os.path.join(tmp, 'cover.html'); open(hp, 'w').write(page)
    png = os.path.join(tmp, 'cover.png')
    subprocess.run([CHROME, '--headless=new', '--no-sandbox', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
                    '--window-size=1080,1920', '--virtual-time-budget=4000', f'--screenshot={png}', 'file://' + hp],
                   check=True, capture_output=True)
    out = os.path.join(out_dir, f'{slug}.jpg')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', png, '-vf', 'scale=1080:1920', '-q:v', '2', out], check=True)
    shutil.rmtree(tmp)
    print('COVER', out)


if __name__ == '__main__':
    if len(sys.argv) < 5: sys.exit(__doc__)
    main(*sys.argv[1:])
