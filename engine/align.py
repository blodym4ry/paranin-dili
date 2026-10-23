#!/usr/bin/env python3
"""words.json üret: speech.wav'ı Whisper ile kelime zamanlı çöz, script.txt kelimelerine hizala (HeyGen word_timestamps'ı elle kopyalamaya gerek kalmaz).
  python3 engine/align.py <slug>      (PD_WORK/<slug>/speech.wav + videos/<slug>/script.txt → PD_WORK/<slug>/words.json)
Eşleşmeyen script kelimelerine komşu eşleşmelerden doğrusal zaman verilir. Sayılar Whisper'da rakam çıkabilir → rakam token'ı ilgili yazı kelimelerine yayılır."""
import difflib, json, os, re, subprocess, sys
import numpy as np
from faster_whisper import WhisperModel

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
slug = sys.argv[1]
W = os.path.join(os.environ.get('PD_WORK', os.path.expanduser('~/pd_work')), slug)
script = open(os.path.join(REPO, 'videos', slug, 'script.txt')).read().split()
tl = lambda s: s.replace('I', 'ı').replace('İ', 'i').lower()
norm = lambda s: re.sub(r"[^\wçğıöşüâî]", '', tl(s))
pcm = subprocess.run(['ffmpeg', '-v', 'error', '-i', os.path.join(W, 'speech.wav'), '-ac', '1', '-ar', '16000', '-f', 's16le', '-'], capture_output=True, check=True).stdout
audio = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
m = WhisperModel(os.environ.get('WHISPER_MODEL', 'large-v3-turbo'), device='cpu', compute_type='int8')
segs, _ = m.transcribe(audio, language='tr', word_timestamps=True, beam_size=5, initial_prompt=' '.join(script)[:600])
hw = [(w.word.strip(), w.start, w.end) for s in segs for w in s.words]
a = [norm(x) for x in script]; b = [norm(x[0]) for x in hw]
T = [None] * len(script)
for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
    if tag == 'equal':
        for k in range(i2 - i1): T[i1 + k] = (hw[j1 + k][1], hw[j1 + k][2])
    elif tag == 'replace' and j2 > j1:   # ör. "yüzde elli dört" ↔ "%54": zaman aralığını kelimelere böl
        s0, e0 = hw[j1][1], hw[j2 - 1][2]; n = i2 - i1
        for k in range(n): T[i1 + k] = (s0 + (e0 - s0) * k / n, s0 + (e0 - s0) * (k + 1) / n)
# boşlukları komşulardan doldur
known = [i for i, t in enumerate(T) if t]
for i, t in enumerate(T):
    if t: continue
    p = max([k for k in known if k < i], default=None); q = min([k for k in known if k > i], default=None)
    s0 = T[p][1] if p is not None else 0.0; e0 = T[q][0] if q is not None else s0 + .4
    T[i] = (s0, max(s0 + .05, e0))
out = [{'word': '<start>', 'start': 0.0, 'end': 0.0}] + [{'word': w, 'start': round(t[0], 4), 'end': round(t[1], 4)} for w, t in zip(script, T)]
dur = len(audio) / 16000
out.append({'word': '<end>', 'start': round(dur, 4), 'end': round(dur, 4)})
json.dump(out, open(os.path.join(W, 'words.json'), 'w'), ensure_ascii=False)
print(f'align: {sum(1 for t in known)}/{len(script)} kelime doğrudan eşleşti → {W}/words.json')
