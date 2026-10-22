#!/usr/bin/env python3
"""Split-voice production: one continuous HeyGen speech track + short avatar clips only where Ata is on camera.

  python3 engine/split.py cut  <slug> <sentence indices, e.g. 0,1,6,11,12>
      in : WORK/speech.wav (create_speech audio), WORK/words.json (its word_timestamps list)
      out: WORK/voice.wav (48k stereo), WORK/avatar.srt (word-timed cues), WORK/dur.txt,
           WORK/segments.json, WORK/seg_00.wav ... (one per run of consecutive on-camera sentences)
      also prints sentences with index + time so you can pick the on-camera ones.
  python3 engine/split.py list <slug>          # just print numbered sentences with times
  python3 engine/split.py join <slug>
      in : WORK/seg_XX.mp4 (HeyGen avatar clips lip-synced to seg_XX.wav)
      out: WORK/avatar_cut.mov  full-length video track, avatar clips at their exact times, black elsewhere,
           and WORK/avatar_cut.srt (copy of avatar.srt). Then run pv.py build/check/render as usual (skip pv.py prep).

Rules: avatar total <= 35% of duration; always the first sentence(s) (hook) and the last (CTA/loop); 1-3 short
emphasis moments in between. In spec.py, AV[scene] may be non-None ONLY for scenes inside an avatar segment
(pv.py check enforces this)."""
import json, os, re, subprocess, sys

PAD = 0.12  # seconds of air kept after each on-camera run
PAD_IN = 0.22  # before: covers scene start (word-0.1s) + avatar fade-in (-0.05s)


def work(slug):
    w = os.path.join(os.environ.get('PD_WORK', os.path.expanduser('~/pd_work')), slug)
    os.makedirs(w, exist_ok=True)
    return w


def dur(p):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]))


def words(w):
    W = [x for x in json.load(open(os.path.join(w, 'words.json'))) if not x['word'].startswith('<')]
    return W


def sentences(W):
    out, cur = [], []
    for x in W:
        cur.append(x)
        if re.search(r'[.?!…]["”’]?$', x['word']):
            out.append(cur); cur = []
    if cur: out.append(cur)
    return out


def fmt(t):
    return f"{int(t // 3600):02d}:{int(t % 3600 // 60):02d}:{int(t % 60):02d},{int(round((t % 1) * 1000)) % 1000:03d}"


def show(S):
    for i, s in enumerate(S):
        print(f"{i:2d}  {s[0]['start']:6.2f}-{s[-1]['end']:6.2f}  {' '.join(x['word'] for x in s)}")


def cut(slug, idx):
    w = work(slug); W = words(w); S = sentences(W); total = dur(os.path.join(w, 'speech.wav'))
    show(S)
    idx = sorted(set(int(i) for i in idx.split(',')))
    runs, cur = [], [idx[0]]
    for i in idx[1:]:
        if i == cur[-1] + 1: cur.append(i)
        else: runs.append(cur); cur = [i]
    runs.append(cur)
    segs = []
    for k, r in enumerate(runs):
        a = max(0.0, S[r[0]][0]['start'] - PAD_IN); b = min(total, S[r[-1]][-1]['end'] + PAD)
        if k == 0 and r[0] == 0: a = 0.0
        if r[-1] == len(S) - 1: b = total
        o = os.path.join(w, f'seg_{k:02d}.wav')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{a:.3f}', '-to', f'{b:.3f}', '-i', os.path.join(w, 'speech.wav'),
                        '-ac', '1', '-ar', '44100', o], check=True)
        segs.append({'i': k, 'a': round(a, 3), 'b': round(b, 3), 'sentences': r, 'wav': o,
                     'text': ' '.join(x['word'] for s in r for x in S[s])})
    on = sum(s['b'] - s['a'] for s in segs)
    json.dump({'total': total, 'segments': segs}, open(os.path.join(w, 'segments.json'), 'w'), ensure_ascii=False, indent=1)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', os.path.join(w, 'speech.wav'), '-ac', '2', '-ar', '48000',
                    os.path.join(w, 'voice.wav')], check=True)
    # captions: cues of <=4 words using real word times
    cues, cur = [], []
    for s in S:
        for x in s:
            cur.append(x)
            if len(cur) >= 4 or x is s[-1]: cues.append(cur); cur = []
    srt = '\n'.join(f"{n + 1}\n{fmt(c[0]['start'])} --> {fmt(c[-1]['end'])}\n{' '.join(x['word'] for x in c)}\n" for n, c in enumerate(cues))
    open(os.path.join(w, 'avatar.srt'), 'w').write(srt)
    open(os.path.join(w, 'dur.txt'), 'w').write(f'{total:.3f}')
    print(f'\nSEGMENTS {len(segs)}  on-camera {on:.1f}s of {total:.1f}s ({on / total * 100:.0f}%)  ≈ {on:.0f} avatar credits')
    for s in segs: print(f"  seg_{s['i']:02d}  {s['a']:.2f}-{s['b']:.2f}  ({s['b'] - s['a']:.1f}s)  {s['text']}")
    if on / total > .35: print('WARN: avatar share above 35% — pick fewer sentences')


def trim(slug, lead=.06):
    """Katman 1 (ilk kelime ilk karede): speech.wav başındaki sessizliği `lead` sn'ye indir, words.json'u kaydır."""
    w = work(slug); p = os.path.join(w, 'words.json'); A = json.load(open(p))
    first = next(x['start'] for x in A if not x['word'].startswith('<')); cut = round(max(0.0, first - lead), 3)
    if cut < .02: print('trim: zaten', first); return
    sp = os.path.join(w, 'speech.wav'); tmp = sp + '.tmp.wav'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{cut:.3f}', '-i', sp, tmp], check=True); os.replace(tmp, sp)
    for x in A:
        x['start'] = round(max(0.0, x['start'] - cut), 4); x['end'] = round(max(0.0, x['end'] - cut), 4)
    json.dump(A, open(p, 'w'), ensure_ascii=False)
    print(f'trim: baştan {cut:.3f} sn kesildi, ilk kelime {first - cut:.3f} sn')


def join(slug):
    w = work(slug); J = json.load(open(os.path.join(w, 'segments.json'))); total = J['total']
    parts, t = [], 0.0
    lst = os.path.join(w, '_join'); os.makedirs(lst, exist_ok=True)
    enc = ['-r', '30', '-c:v', 'libx264', '-crf', '14', '-preset', 'fast', '-pix_fmt', 'yuv420p', '-an']
    def black(d, n):
        o = os.path.join(lst, f'b{n:02d}.mov')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', f'color=c=black:s=1080x1920:r=30:d={d:.3f}'] + enc + [o], check=True)
        return o
    for s in J['segments']:
        mp4 = os.path.join(w, f"seg_{s['i']:02d}.mp4")
        if not os.path.exists(mp4): sys.exit(f'missing {mp4}')
        want = s['b'] - s['a']; got = dur(mp4)
        if abs(got - want) > .25: print(f"WARN seg_{s['i']:02d}: clip {got:.2f}s vs audio {want:.2f}s")
        if s['a'] - t > 0.02: parts.append(black(s['a'] - t, len(parts)))
        o = os.path.join(lst, f"s{s['i']:02d}.mov")
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', mp4, '-t', f'{want:.3f}', '-vf',
                        'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,tpad=stop_mode=clone:stop_duration=1'] + enc + ['-t', f'{want:.3f}', o], check=True)
        parts.append(o); t = s['b']
    if total - t > 0.02: parts.append(black(total - t, len(parts)))
    open(os.path.join(lst, 'list.txt'), 'w').write(''.join(f"file '{p}'\n" for p in parts))
    out = os.path.join(w, 'avatar_cut.mov')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', os.path.join(lst, 'list.txt'), '-c', 'copy', out], check=True)
    subprocess.run(['cp', os.path.join(w, 'avatar.srt'), os.path.join(w, 'avatar_cut.srt')], check=True)
    print(f'avatar_cut.mov {dur(out):.2f}s (voice {total:.2f}s)')


if __name__ == '__main__':
    if len(sys.argv) < 3: sys.exit(__doc__)
    c, slug = sys.argv[1], sys.argv[2]
    if c == 'cut': cut(slug, sys.argv[3])
    elif c == 'trim': trim(slug)
    elif c == 'list': show(sentences(words(work(slug))))
    elif c == 'join': join(slug)
    else: sys.exit(__doc__)
