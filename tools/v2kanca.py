#!/usr/bin/env python3
"""21:45 v2 deneme: ana videonun ilk cümlesini yeni kancayla değiştirir (Ata onaylı kanca, 6 Kas).
  python3 tools/v2kanca.py <anim_final.mp4> <ana_out.mp4> <kanca.mp3> <words_trim.json> <cikti.mp4> [kanca_words.json]
A: animasyonun ilk H sn'si (avatarsız) + yeni kanca sesi (+boom); B: ana videonun 2. cümleden itibaren kalanı.
"""
import json, os, re, subprocess, sys, tempfile, shutil

SFX = '/home/claude/pd_work/sfx/boom.mp3'


def dur(p): return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]))


def main(anim, ana, hook, wtrim, out, hookwords=None):
    W = [w for w in json.load(open(wtrim)) if not w.get('word', w.get('w', '')).startswith('<')]
    W = [{'word': w.get('word', w.get('w')), 'start': w.get('start', w.get('s')), 'end': w.get('end', w.get('e'))} for w in W]
    i = next(k for k, w in enumerate(W) if re.search(r'[.!?…]["”»]?$', w['word']))
    cut = round((W[i]['end'] + W[i + 1]['start']) / 2, 3)          # 1. ve 2. cümle arası
    tmp = tempfile.mkdtemp(prefix='v2_', dir='/home/claude/pd_work')
    h = os.path.join(tmp, 'hook.wav')
    # baştaki sessizliği 0,06 sn'ye indir, sona 0,25 sn nefes
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', hook, '-af', 'silenceremove=start_periods=1:start_threshold=-45dB,adelay=60|60,apad=pad_dur=0.25',
                    '-ac', '2', '-ar', '48000', h], check=True)
    H = dur(h)
    a = os.path.join(tmp, 'a.mp4'); b = os.path.join(tmp, 'b.mp4')
    # eski altyazıyı (y 1240–1460) bulanıklaştır, yeni kanca altyazısını yaz
    caps = ''
    if hookwords:
        HW = [w for w in json.load(open(hookwords)) if not w['word'].startswith('<')]
        sh = HW[0]['start'] - 0.06
        G, cur = [], []
        for w in HW:
            cur.append(w)
            if len(cur) == 3 or re.search(r'[.,!?]$', w['word']): G.append(cur); cur = []
        if cur: G.append(cur)
        F = '/home/claude/paranin-dili/kit/fonts/ttf/inter-bold-tr.ttf'
        for k, g in enumerate(G):
            t0 = g[0]['start'] - sh; t1 = (G[k + 1][0]['start'] - sh) if k + 1 < len(G) else H
            txt = ' '.join(x['word'] for x in g).replace("'", "\u2019").replace(':', '\\:').replace(',', '\\,')
            caps += f",drawtext=fontfile={F}:text='{txt}':fontsize=62:fontcolor=white:borderw=6:bordercolor=black@0.85:x=(w-text_w)/2:y=1300:enable='between(t\\,{t0:.2f}\\,{t1:.2f})'"
    vf = f"[0:v]fps=24,format=yuv420p,setsar=1,split[o][c];[c]crop=1080:220:0:1240,boxblur=30:4,eq=brightness=-0.25[bl];[o][bl]overlay=0:1240{caps}[v];"
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-t', f'{H:.3f}', '-i', anim, '-i', h, '-i', SFX, '-filter_complex',
                    vf + '[2:a]volume=-7dB[bm];[1:a][bm]amix=inputs=2:normalize=0:duration=first[a]',
                    '-map', '[v]', '-map', '[a]', '-t', f'{H:.3f}', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-c:a', 'aac', '-ar', '48000', '-ac', '2', a], check=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{cut:.3f}', '-i', ana, '-vf', 'fps=24,format=yuv420p,setsar=1',
                    '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-c:a', 'aac', '-ar', '48000', '-ac', '2', b], check=True)
    lst = os.path.join(tmp, 'l.txt'); open(lst, 'w').write(f"file '{a}'\nfile '{b}'\n")
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', '-movflags', '+faststart', out], check=True)
    shutil.rmtree(tmp, ignore_errors=True)
    print('V2', out, 'kanca', round(H, 2), 'kesim', cut, 'süre', round(dur(out), 2))


if __name__ == '__main__':
    main(*sys.argv[1:7])
