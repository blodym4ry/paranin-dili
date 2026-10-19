"""Trim long pauses (no speed change), write cut video, remapped SRT, frames and voice.
usage: python3 prep_avatar.py SRC_DIR [speed]"""
import json, subprocess, sys, os, shutil
from build_edl import parse_srt
D = sys.argv[1]; SP = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
DUR = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f'{D}/avatar.mp4']))
segs = parse_srt(f'{D}/avatar.srt')
keep, cur, saved = [], 0.0, 0
for i in range(len(segs) - 1):
    t1 = segs[i][1]; nxt = segs[i + 1][0]
    if nxt - t1 > .28:
        a = t1 + .13; b = nxt - .06; keep.append((round(cur, 3), round(a, 3))); saved += b - a; cur = b
keep.append((round(cur, 3), DUR))
# segment-wise cut (low memory): each keep-range encoded separately, then concat demuxer
os.makedirs(f'{D}/_seg', exist_ok=True)
lst = []
for i, (a, b) in enumerate(keep):
    o = f'{D}/_seg/s{i:03d}.mov'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{a:.3f}', '-to', f'{b:.3f}', '-i', f'{D}/avatar.mp4', '-af', f'afade=t=in:d=0.01,afade=t=out:st={max(0, b - a - 0.012):.3f}:d=0.012',
                    '-r', '30', '-c:v', 'libx264', '-crf', '14', '-preset', 'fast', '-c:a', 'pcm_s16le', '-ar', '48000', o], check=True)
    lst.append(f"file '{os.path.abspath(o)}'")
open(f'{D}/_seg/list.txt', 'w').write('\n'.join(lst) + '\n')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{D}/_seg/list.txt', '-c', 'copy', f'{D}/avatar_cut.mov'], check=True)
def remap(t):
    acc = 0
    for a, b in keep:
        if t <= b: return (acc + max(0, t - a)) / SP
        acc += b - a
    return acc / SP
f = lambda x: f"{int(x // 3600):02d}:{int(x % 3600 // 60):02d}:{int(x % 60):02d},{int(round((x % 1) * 1000)) % 1000:03d}"
open(f'{D}/avatar_cut.srt', 'w').write('\n'.join(f"{i + 1}\n{f(remap(a))} --> {f(remap(b))}\n{t}\n" for i, (a, b, t) in enumerate(segs)))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{D}/avatar_cut.mov', '-vn', '-ac', '2', '-ar', '48000', f'{D}/voice.wav'], check=True)
nd = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f'{D}/avatar_cut.mov']))
print('orig', round(DUR, 2), 'saved', round(saved, 2), 'final', round(nd, 2), )
