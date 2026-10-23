#!/usr/bin/env python3
"""DENEME REELS — KAYNAĞI SADECE FİNAL MP4 OLAN VİDEOLAR İÇİN (repo'da çalışma klasörü olmayan eski videolar: 6 Kas faiz, 8 Kas sel).
variant.py'den farkı: gövde sesi yeniden karıştırılamaz (elimizde sadece karışık final ses var). Bu yüzden:
  kanca klibi = yeni kanca sesi + yeni avatar (HERO/HALF) + onaylı müzik (pv.py render ile tam miks)
  gövde      = kaynak mp4'ün kesme noktasından sonrası (görüntü + ses aynen)
  birleşim   = video düz ekleme, ses 0,12 sn çapraz geçiş, loudnorm -13.

  python3 engine/variant_mp4.py prep  <slug> <v> <hook.wav> "<kanca metni>" "<başlık 1>" "<başlık 2>" <hero|full>
  (seg_00.wav → public/audio push → create_video_from_avatar → PD_WORK/<slug>__<v>/seg_00.mp4 → split.py join → pv.py build → render)
  python3 engine/variant_mp4.py final <slug> <v> <kaynak.mp4> <kesme_sn>   → public/<slug>__<v>.mp4
"""
import os, re, shutil, subprocess, sys
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PDW = os.environ.get('PD_WORK', os.path.expanduser('~/pd_work'))
ENG = os.path.join(REPO, 'engine')
sys.path.insert(0, ENG)
import split as SP
from variant import SPEC, dur


def prep(slug, v, hookwav, hook, l1, l2, mode):
    w = os.path.join(PDW, f'{slug}__{v}'); vd = os.path.join(REPO, 'videos', f'{slug}__{v}')
    os.makedirs(w, exist_ok=True); os.makedirs(vd, exist_ok=True)
    o = subprocess.run(['ffmpeg', '-i', hookwav, '-af', 'silencedetect=n=-40dB:d=0.05', '-f', 'null', '-'], capture_output=True, text=True).stderr
    m = re.search(r'silence_start: (-?[\d.]+)\s.*?silence_end: ([\d.]+)', o, re.S)
    lead = max(0.0, float(m.group(2)) - .06) if m and float(m.group(1)) <= .01 else 0.0
    t = os.path.join(w, 'hook_t.wav'); s = os.path.join(w, 'sil.wav')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{lead:.3f}', '-i', hookwav, '-ac', '1', '-ar', '44100', t], check=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=mono', '-t', '0.25', s], check=True)
    lst = os.path.join(w, 'parts.txt'); open(lst, 'w').write(f"file '{t}'\nfile '{s}'\n")
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, os.path.join(w, 'speech.wav')], check=True)
    open(os.path.join(vd, 'script.txt'), 'w').write(hook.strip() + '\n')
    open(os.path.join(vd, 'spec.py'), 'w').write(SPEC.replace('__MODE__', mode).replace('__L1__', l1).replace('__L2__', l2))
    subprocess.run([sys.executable, os.path.join(ENG, 'align.py'), f'{slug}__{v}'], check=True)
    n = len(SP.sentences(SP.words(w)))
    subprocess.run([sys.executable, os.path.join(ENG, 'split.py'), 'cut', f'{slug}__{v}', ','.join(map(str, range(n)))], check=True)
    print(f'prep OK: kanca klibi {dur(os.path.join(w, "speech.wav")):.2f} sn')


def final(slug, v, src, cut):
    w = os.path.join(PDW, f'{slug}__{v}'); out = os.path.join(w, 'final'); os.makedirs(out, exist_ok=True)
    hook = os.path.join(REPO, 'public', f'{slug}__{v}.mp4')          # pv.py render çıktısı (kanca klibi, tam miks)
    a = os.path.join(out, 'hook.mp4')
    if not os.path.exists(a): shutil.copy(hook, a)                  # ikinci çalıştırmada final'i kanca sanmasın
    H = dur(a); X = .12
    fin = os.path.join(w, f'{slug}__{v}.mp4')
    fc = (f'[0:v]fps=30,format=yuv420p,setsar=1[v0];[1:v]trim=start={float(cut):.3f},setpts=PTS-STARTPTS,fps=30,scale=1080:1920,format=yuv420p,setsar=1[v1];'
          f'[v0][v1]concat=n=2:v=1:a=0[v];'
          f'[0:a]aresample=48000,aformat=channel_layouts=stereo,apad=pad_dur={X}[a0];'
          f'[1:a]atrim=start={float(cut) - X:.3f},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo[a1];'
          f'[a0][a1]acrossfade=d={X}:c1=tri:c2=tri,loudnorm=I=-13:TP=-1.5[a]')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', a, '-i', src, '-filter_complex', fc, '-map', '[v]', '-map', '[a]',
                    '-c:v', 'libx264', '-b:v', '4M', '-maxrate', '5M', '-bufsize', '8M', '-preset', 'medium', '-c:a', 'aac', '-b:a', '192k',
                    '-ar', '48000', '-movflags', '+faststart', fin], check=True)
    shutil.copy(fin, hook)
    print(f'FINAL {fin} {dur(fin):.1f}s (kanca {H:.2f}s, kaynak kesme {float(cut):.2f}s)')


if __name__ == '__main__':
    c = sys.argv[1]
    if c == 'prep': prep(*sys.argv[2:9])
    elif c == 'final': final(*sys.argv[2:6])
    else: sys.exit(__doc__)
