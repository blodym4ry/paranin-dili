"""Telaffuz testi: python3 telaffuz.py voice.wav script.txt
HeyGen sesini Whisper (large-v3-turbo, yerel) ile yaziya doker, gonderilen metinle kelime kelime karsilastirir,
farkli okunan / dusuk guvenli yerleri zamaniyla listeler."""
import sys, re, json, difflib
from faster_whisper import WhisperModel
import os
M = os.environ.get('WHISPER_MODEL', os.path.expanduser('~/models/whisper-turbo'))
def norm(s):
    s = re.sub(r'<[^>]+>', ' ', s).replace('İ', 'i').replace('I', 'ı').lower()
    return [w for w in re.sub(r"[^\wçğıöşüâîû']+", ' ', s).split() if w]
wav, scr = sys.argv[1], open(sys.argv[2]).read()
m = WhisperModel(M, device='cpu', compute_type='int8')
import subprocess, numpy as np
pcm = subprocess.run(['ffmpeg', '-v', 'error', '-i', wav, '-ac', '1', '-ar', '16000', '-f', 's16le', '-'], capture_output=True).stdout
audio = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
segs, _ = m.transcribe(audio, language='tr', word_timestamps=True, beam_size=5, initial_prompt=re.sub(r'<[^>]+>', ' ', scr)[:600] if '--prompt' in sys.argv else None)
W = [(w.word, w.start, w.probability) for s in segs for w in s.words]
heard = []; times = []; probs = []
for w, t, p in W:
    for n in norm(w): heard.append(n); times.append(t); probs.append(p)
want = norm(scr)
from num2words import num2words
def flat(ws):
    ws = list(ws); m2 = []
    for w in ws:
        if m2 and re.fullmatch(r'\d{3}', w) and re.fullmatch(r'\d+', m2[-1]): m2[-1] += w
        else: m2.append(w)
    ws = m2; out = []
    for w in ws:
        w = w.replace('â', 'a').replace('î', 'i').replace('û', 'u')
        if re.fullmatch(r'\d+', w):
            try: w = num2words(int(w), lang='tr')
            except Exception: pass
        out.append(w)
    s = ''.join(out)
    for x in ('yüzde', 'virgül', ' '): s = s.replace(x, '')
    s = s.replace('buçuk', 'beş')
    return s
def numeq(a, b): return flat(a) == flat(b)
sm = difflib.SequenceMatcher(a=want, b=heard, autojunk=False)
issues = []
for op, a0, a1, b0, b1 in sm.get_opcodes():
    if op == 'equal':
        for k in range(b0, b1):
            if probs[k] < .45: issues.append((times[k], 'DÜŞÜK GÜVEN', want[a0 + k - b0], heard[k], probs[k]))
        continue
    t = times[b0] if b0 < len(times) else (times[-1] if times else 0)
    if numeq(want[a0:a1], heard[b0:b1]): continue
    issues.append((t, op.upper(), ' '.join(want[a0:a1]), ' '.join(heard[b0:b1]), None))
print('DUYULAN:', ' '.join(heard)); print()
print(f'Eşleşme oranı: {sm.ratio():.3f}  ({len(issues)} şüpheli yer)')
for t, op, a, b, p in issues:
    print(f'{int(t//60)}:{t%60:05.2f}  {op:12s} metin: "{a}"  →  duyulan: "{b}"' + (f'  (güven {p:.2f})' if p is not None else ''))
json.dump([dict(t=i[0], op=i[1], metin=i[2], duyulan=i[3]) for i in issues], open(wav + '.telaffuz.json', 'w'), ensure_ascii=False, indent=1)
