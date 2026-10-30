#!/usr/bin/env python3
"""Paranın Dili video pipeline. Every stage is idempotent; run them in order.

  python3 engine/pv.py prep   <slug>   # WORK/avatar.mp4 + avatar.srt -> silence-cut avatar, voice, media
  python3 engine/pv.py tel    <slug>   # pronunciation check (Whisper) against videos/<slug>/script.txt
  python3 engine/pv.py build  <slug>   # spec.py -> HyperFrames project (index.html) + mix.wav
  python3 engine/pv.py check  <slug>   # layout/contrast check at transitions + preview contact sheet
  python3 engine/pv.py render <slug>   # render, mux, loudnorm -13 LUFS, QA sheet -> public/<slug>.mp4
  python3 engine/pv.py remix  <slug>   # audio only: new music/sfx mix + mux onto the existing render (no re-render)

WORK dir = $PD_WORK/<slug> (default ~/pd_work/<slug>). Heavy files live there, never in git.
"""
import json, os, re, shutil, subprocess, sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ENG, KIT = os.path.join(REPO, 'engine'), os.path.join(REPO, 'kit')
HF = 'hyperframes@0.8.174'
BROWSER = os.environ.get('HYPERFRAMES_BROWSER_PATH') or next(
    (p for p in ['/opt/pw-browsers/chromium-1194/chrome-linux/chrome'] if os.path.exists(p)), None)


def sh(cmd, cwd=None, check=True, env=None, capture=False):
    print('$', cmd if isinstance(cmd, str) else ' '.join(cmd), flush=True)
    e = dict(os.environ, **(env or {}))
    if BROWSER: e['HYPERFRAMES_BROWSER_PATH'] = BROWSER
    r = subprocess.run(cmd, cwd=cwd, shell=isinstance(cmd, str), env=e, check=check,
                       capture_output=capture, text=capture)
    return r.stdout if capture else r


def dur(p):
    return float(sh(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture=True))


def paths(slug):
    vd = os.path.join(REPO, 'videos', slug)
    w = os.path.join(os.environ.get('PD_WORK', os.path.expanduser('~/pd_work')), slug)
    os.makedirs(w, exist_ok=True)
    return vd, w, os.path.join(w, 'hf')


def prep(slug):
    vd, w, _ = paths(slug)
    for f in ['avatar.mp4', 'avatar.srt']:
        if not os.path.exists(os.path.join(w, f)): sys.exit(f'missing {w}/{f} (download HeyGen video + srt first)')
    sh([sys.executable, os.path.join(ENG, 'prep_avatar.py'), w], cwd=w)
    d = dur(os.path.join(w, 'avatar_cut.mov'))
    open(os.path.join(w, 'dur.txt'), 'w').write(f'{d:.3f}')
    print('cut duration', round(d, 2))


def tel(slug):
    vd, w, _ = paths(slug)
    sh([sys.executable, os.path.join(ENG, 'telaffuz.py'), os.path.join(w, 'voice.wav'), os.path.join(vd, 'script.txt')])


def build(slug):
    vd, w, hf = paths(slug)
    os.makedirs(os.path.join(hf, 'media'), exist_ok=True)
    for f in ['hyperframes.json', 'package.json']:
        shutil.copy(os.path.join(ENG, f), hf)
    json.dump({'id': slug, 'name': slug}, open(os.path.join(hf, 'meta.json'), 'w'))
    shutil.copytree(os.path.join(KIT, 'fonts'), os.path.join(hf, 'fonts'), dirs_exist_ok=True)
    shutil.copy(os.path.join(KIT, 'gsap.min.js'), os.path.join(hf, 'media'))
    shutil.copytree(os.path.join(KIT, 'masa'), os.path.join(hf, 'media', 'masa'), dirs_exist_ok=True)  # masa üstü kiti dokuları
    # per-video real images / B-roll (videos/<slug>/media) -> hf/media
    if os.path.isdir(os.path.join(vd, 'media')):
        shutil.copytree(os.path.join(vd, 'media'), os.path.join(hf, 'media'), dirs_exist_ok=True)
    av = os.path.join(hf, 'media', 'av.mp4')
    if not os.path.exists(av) or os.path.getmtime(av) < os.path.getmtime(os.path.join(w, 'avatar_cut.mov')):
        sh(['ffmpeg', '-v', 'error', '-y', '-i', os.path.join(w, 'avatar_cut.mov'), '-an', '-c:v', 'libx264', '-crf', '16',
            '-preset', 'fast', '-pix_fmt', 'yuv420p', '-g', '15', '-movflags', '+faststart', av])
    shutil.copy(os.path.join(vd, 'spec.py'), os.path.join(hf, 'spec.py'))
    sh([sys.executable, os.path.join(KIT, 'assemble.py'), hf], env={'VIDEO_WORK': w})
    sh([sys.executable, os.path.join(ENG, 'audio3.py'), 'edl_audio.json', os.path.join(w, 'voice.wav'), 'mix.wav'], cwd=hf,
       env={'PYTHONPATH': ENG, 'PD_SLUG': slug})


def scenes_at(hf):
    html = open(os.path.join(hf, 'index.html')).read()
    st = sorted(float(x) for x in re.findall(r'class="scene clip" data-start="([\d.]+)"', html))
    at = []
    for t in st[1:]: at += [round(t - .3, 2), round(t + .5, 2)]
    return st, at


def avatar_guard(w, hf):
    """split mode: every scene that shows the avatar must sit inside an avatar clip (else black frames show)."""
    sj = os.path.join(w, 'segments.json')
    if not os.path.exists(sj): return True
    segs = json.load(open(sj))['segments']
    html = open(os.path.join(hf, 'index.html')).read()
    SC = json.loads(re.search(r'SC=(\[.*?\]), AV=', html).group(1))
    AV = json.loads(re.search(r'AV=(\{.*?\});', html).group(1))
    ok, total = True, json.load(open(sj))['total']
    shown = 0.0
    for sid, a, b in SC:
        if not AV.get(sid): continue
        shown += b - a
        # window fades in at scene start-0.05s and is gone by scene end-0.05s: the clip must cover that span
        # bitişik parçalar (aralık ≤0,05 sn) tek kapsama sayılır — panel stilinde avatar video boyunca ekranda
        cov = []
        for sg in sorted(segs, key=lambda x: x['a']):
            if cov and sg['a'] - cov[-1][1] <= .05: cov[-1][1] = max(cov[-1][1], sg['b'])
            else: cov.append([sg['a'], sg['b']])
        if not any(c0 <= max(0.0, a - .05) + .005 and b - .05 <= c1 for c0, c1 in cov):
            print(f'AVATAR GUARD FAIL: scene {sid} {a:.2f}-{b:.2f} shows avatar outside every avatar clip'); ok = False
    print(f'avatar on screen {shown:.1f}s of {total:.1f}s ({shown / total * 100:.0f}%)')
    return ok


def check(slug):
    vd, w, hf = paths(slug)
    if not avatar_guard(w, hf): sys.exit(1)
    st, at = scenes_at(hf)
    out = sh(f'npx --yes {HF} check --samples=80 --at {",".join(map(str, at))} 2>&1 | tail -25', cwd=hf, capture=True)
    print(out)
    mids = [round((a + b) / 2, 2) for a, b in zip(st, st[1:] + [dur(os.path.join(w, 'avatar_cut.mov'))])]
    shutil.rmtree(os.path.join(hf, 'snap'), ignore_errors=True)
    sh(f'npx --yes {HF} snapshot -o snap --no-end --at {",".join(map(str, mids))} 2>&1 | tail -3', cwd=hf, check=False)
    ok = 'Check passed' in out
    sz = subprocess.run([sys.executable, os.path.join(REPO, 'tools', 'safezone.py'), hf], capture_output=True, text=True)
    print(sz.stdout[-3000:] + sz.stderr[-800:])
    ok = ok and sz.returncode == 0
    print('CHECK', 'PASS' if ok else 'FAIL', '| preview sheets:', [os.path.join(hf, 'snap', f) for f in sorted(os.listdir(os.path.join(hf, 'snap'))) if f.startswith('contact')] if os.path.isdir(os.path.join(hf, 'snap')) else [])
    if not ok: sys.exit(1)


def render(slug, video=True):
    vd, w, hf = paths(slug)
    os.makedirs(os.path.join(hf, 'renders'), exist_ok=True)
    if video: sh(f'timeout 2400 npx --yes {HF} render -o renders/v.mp4 --crf 12 --quiet > render.log 2>&1', cwd=hf)
    else: sh([sys.executable, os.path.join(ENG, 'audio3.py'), 'edl_audio.json', os.path.join(w, 'voice.wav'), 'mix.wav'], cwd=hf,
             env={'PYTHONPATH': ENG, 'PD_SLUG': slug})
    final = os.path.join(w, f'{slug}.mp4')
    # GitHub 100 MB sınırı: uzun videoda bitrate süreye göre düşer (≤ ~88 MB); kısa videoda 9 Mbps
    br = min(9.0, 620 / max(dur(os.path.join(w, 'voice.wav')), 1)); mx = min(14.0, br * 1.5)
    sh(['ffmpeg', '-v', 'error', '-y', '-i', 'renders/v.mp4', '-i', 'mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'libx264',
        '-b:v', f'{br:.1f}M', '-maxrate', f'{mx:.1f}M', '-bufsize', f'{mx * 1.5:.1f}M', '-profile:v', 'high', '-g', '15', '-bf', '2', '-preset', 'slow',
        '-pix_fmt', 'yuv420p', '-af',
        'loudnorm=I=-13:TP=-1.5', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', final], cwd=hf)
    sh(['ffmpeg', '-v', 'error', '-y', '-i', final, '-vf', 'fps=1/2.6,scale=200:-1,tile=9x3', '-frames:v', '1',
        os.path.join(w, 'qa.jpg')])
    lufs = sh(f'ffmpeg -nostats -i {final} -af ebur128=peak=true -f null - 2>&1 | grep -E "I:|Peak:" | tail -2', capture=True)
    size = os.path.getsize(final) / 1e6
    print('FINAL', final, f'{dur(final):.1f}s', f'{size:.1f}MB', lufs.replace('\n', ' '), '| QA sheet', os.path.join(w, 'qa.jpg'))
    if size > 95: sys.exit('file too large for GitHub (>95MB)')
    pub = os.path.join(REPO, 'public', f'{slug}.mp4')
    shutil.copy(final, pub)
    print('PUBLIC', pub)


if __name__ == '__main__':
    if len(sys.argv) < 3: sys.exit(__doc__)
    {'prep': prep, 'tel': tel, 'build': build, 'check': check, 'render': render, 'remix': lambda s: render(s, False)}[sys.argv[1]](sys.argv[2])
