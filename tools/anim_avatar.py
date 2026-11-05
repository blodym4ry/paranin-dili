#!/usr/bin/env python3
"""Animasyon videosuna Ata'yı ekler (Ata 5 Kas: "girişte + çıkışta + bazen ortada vurgulu cümlede olmalıyım").
  python3 tools/anim_avatar.py <anim.mp4> <slug> <words_trim.json> <out.mp4>
Avatar kaynağı PD_WORK/<slug>: segments.json + seg_0i.mp4 (bölümlü) ya da avatar_cut.mov / tek seg_00.mp4 (tam).
HERO kart: 700x880, x140 y330 (güvenli alan), yuvarlak köşe + beyaz çerçeve; altyazı bandı (y1250+) açık kalır.
"""
import json, os, re, subprocess, sys, tempfile

PDW = os.environ.get('PD_WORK', '/home/claude/pd_work')
X, Y, CW, CH, R, BW = 140, 330, 700, 880, 44, 10
INTRO_FROM, INTRO_MAX, MID_MAX = 0.9, 3.8, 5.0


def dur(p): return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]))


def sentences(W):
    S, cur = [], []
    for w in W:
        if w['word'].startswith('<'): continue
        cur.append(w)
        if re.search(r'[.!?…]["”»]?$', w['word']): S.append(cur); cur = []
    if cur: S.append(cur)
    return S


def main(anim, slug, wtrim, out):
    wd = os.path.join(PDW, slug)
    Wo = [w for w in json.load(open(os.path.join(wd, 'words.json'))) if not w['word'].startswith('<')]
    Wt = [w for w in json.load(open(wtrim)) if not w['word'].startswith('<')]
    T = round(Wo[0]['start'] - Wt[0]['start'], 4)          # kırpma kayması (orijinal = anim + T)
    D = dur(anim)
    seg = json.load(open(os.path.join(wd, 'segments.json')))['segments']
    S = sentences(Wt)
    slots = []
    if len(seg) >= 3 and all(os.path.exists(os.path.join(wd, f'seg_{s["i"]:02d}.mp4')) for s in seg):
        src = lambda t: next((os.path.join(wd, f'seg_{s["i"]:02d}.mp4'), t - s['a']) for s in seg if s['a'] - .01 <= t <= s['b'] + .01)
        a0, b0 = seg[0]['a'] - T, seg[0]['b'] - T
        e1 = S[0][-1]['end'] + .15
        slots.append((max(INTRO_FROM, a0), min(b0, INTRO_MAX)))
        for s in seg[1:-1]:
            slots.append((s['a'] - T + .05, min(s['b'] - T, s['a'] - T + MID_MAX)))
        slots.append((seg[-1]['a'] - T + .05, D))
    else:
        full = os.path.join(wd, 'avatar_cut.mov')
        if not os.path.exists(full): full = os.path.join(wd, 'seg_00.mp4')
        src = lambda t: (full, t)
        e1 = next((s[-1]['end'] + .15 for s in S if s[-1]['end'] >= 2.5), INTRO_MAX)
        slots.append((INTRO_FROM, min(e1, INTRO_MAX)))
        for s in S[1:-1]:
            st = s[0]['start']
            if .3 * D < st < .78 * D and re.match(r'(Ama|Peki|Asıl|Dikkat|Yani|Dürüst|Ve asıl)', s[0]['word']):
                slots.append((st - .05, min(s[-1]['end'] + .15, st + MID_MAX))); break
        else:  # vurgu kelimesi yoksa: ortaya en yakın, 1.5–5 sn'lik cümle
            c = [s for s in S[1:-1] if 1.5 <= s[-1]['end'] - s[0]['start'] <= 5 and .3 * D < s[0]['start'] < .78 * D]
            if c:
                s = min(c, key=lambda s: abs(s[0]['start'] - .55 * D))
                slots.append((s[0]['start'] - .05, s[-1]['end'] + .15))
        slots.sort()
        slots.append((S[-1][0]['start'] - .05, D))
    slots = [(round(a, 3), round(min(b, D), 3)) for a, b in slots if b - a > .6]
    tmp = tempfile.mkdtemp(prefix='anav_', dir=PDW)
    from PIL import Image, ImageDraw, ImageFilter
    m = Image.new('L', (CW, CH), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, CW - 1, CH - 1], R, fill=255); m.save(os.path.join(tmp, 'mask.png'))
    b = Image.new('RGBA', (CW + 2 * BW + 60, CH + 2 * BW + 60), (0, 0, 0, 0)); d = ImageDraw.Draw(b)
    d.rounded_rectangle([30 + 8, 30 + 14, 30 + CW + 2 * BW + 8, 30 + CH + 2 * BW + 14], R + BW, fill=(0, 0, 0, 150))
    b = b.filter(ImageFilter.GaussianBlur(12)); d = ImageDraw.Draw(b)
    d.rounded_rectangle([30, 30, 30 + CW + 2 * BW, 30 + CH + 2 * BW], R + BW, fill=(255, 255, 255, 255))
    b.save(os.path.join(tmp, 'frame.png'))
    g = Image.new('L', (1080, 1240), 255); gd = ImageDraw.Draw(g)
    for y in range(1150, 1240): gd.line([(0, y), (1079, y)], fill=int(255 * (1240 - y) / 90))
    g.save(os.path.join(tmp, 'grad.png'))
    inp = ['-i', anim, '-loop', '1', '-i', os.path.join(tmp, 'mask.png'), '-loop', '1', '-i', os.path.join(tmp, 'frame.png')]
    f = [f'[1:v]format=gray,split={len(slots)}' + ''.join(f'[m{k}]' for k in range(len(slots))),
         f'[2:v]format=rgba,split={len(slots)}' + ''.join(f'[fr{k}]' for k in range(len(slots)))]
    # Ata konuşurken animasyon "geri çekilir": üst bölge (altyazı bandı hariç) bulanık + karartılmış zemine geçer (0.25 sn geçiş);
    # böylece kart, hareket eden bir animasyonun üstüne binmez (Ata 5 Kas 21:29).
    # bulanık zemin: her slot için animasyonu ayrı girdi olarak aç (split+trim tüm videoyu RAM'de tutuyor → OOM)
    prev = '0:v'
    for k, (a, bb) in enumerate(slots):
        a0, b0 = max(0, a - .25), min(D, bb + .25); dd0 = b0 - a0
        n = len(inp) // 2 if False else None
        inp += ['-ss', f'{a0:.3f}', '-t', f'{dd0:.3f}', '-i', anim, '-loop', '1', '-t', f'{dd0:.3f}', '-i', os.path.join(tmp, 'grad.png')]
        idx = sum(1 for x in inp if x == '-i') - 2
        f.append(f"[{idx}:v]setpts=PTS-STARTPTS,crop=1080:1240:0:0,boxblur=28:3,eq=brightness=-0.22:saturation=0.75,format=rgba[bz{k}];[{idx + 1}:v]format=gray,setpts=PTS-STARTPTS[gm{k}];[bz{k}][gm{k}]alphamerge,"
                 f"fade=t=in:st=0:d=0.25:alpha=1,fade=t=out:st={dd0 - .25:.3f}:d=0.25:alpha=1,setpts=PTS-STARTPTS+{a0:.3f}/TB[bl{k}];"
                 f"[{prev}][bl{k}]overlay=0:0:eof_action=pass[bg{k}]")
        prev = f'bg{k}'
    cur = prev
    for k, (a, bb) in enumerate(slots):
        fp, lt = src(a + T); dd = bb - a
        inp += ['-ss', f'{max(0, lt):.3f}', '-t', f'{dd:.3f}', '-i', fp]; n = sum(1 for x in inp if x == '-i') - 1
        fade = f'fade=t=in:st=0:d=0.15:alpha=1,fade=t=out:st={max(0, dd - .15):.3f}:d=0.15:alpha=1'
        f.append(f'[{n}:v]fps=24,crop=1080:1358:0:150,scale={CW}:{CH},format=rgba[c{k}];[m{k}]trim=duration={dd:.3f},setpts=PTS-STARTPTS[mk{k}];[c{k}][mk{k}]alphamerge,{fade},setpts=PTS-STARTPTS+{a:.3f}/TB[av{k}]')
        f.append(f'[fr{k}]trim=duration={dd:.3f},{fade},setpts=PTS-STARTPTS+{a:.3f}/TB[fb{k}]')
        f.append(f'[{cur}][fb{k}]overlay=x={X - BW - 30}:y={Y - BW - 30}:eof_action=pass[o{k}a];[o{k}a][av{k}]overlay=x={X}:y={Y}:eof_action=pass[o{k}]')
        cur = f'o{k}'
    fc = os.path.join(tmp, 'fc.txt'); open(fc, 'w').write(';\n'.join(f))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *inp, '-filter_complex_script', fc, '-map', f'[{cur}]', '-map', '0:a',
                    '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-pix_fmt', 'yuv420p', '-c:a', 'copy', '-movflags', '+faststart',
                    '-t', f'{D:.3f}', out], check=True)
    import shutil; shutil.rmtree(tmp, ignore_errors=True)
    print('AVATAR', slug, 'T=', T, 'slots=', slots)


if __name__ == '__main__':
    main(*sys.argv[1:5])
