"""raw/*.mp3 -> one-shot wavs: en güçlü tek olayı kes (onset-20ms .. -32dB düşüşüne kadar, en fazla MAXL sn), fade, -1 dBFS."""
import subprocess, numpy as np, glob, os, sys
SR = 48000; MAXL = {'tape': 1.4, 'tear': 1.4, 'marker': 1.3, 'marker2': 1.3, 'scribble': 1.3, 'highlighter': 1.3, 'pencil': 1.3, 'page': 1.2}
def load(p):
    a = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(a, np.float32).copy()
def env(x, w=480):
    n = len(x) // w; return np.sqrt((x[:n * w].reshape(n, w) ** 2).mean(1) + 1e-12)
os.makedirs('oneshot', exist_ok=True); rows = []
for p in sorted(glob.glob('raw/*.mp3')):
    k = os.path.basename(p)[:-4]; cat = k.rsplit('_', 1)[0]; x = load(p)
    if len(x) < SR * .1: continue
    e = env(x); db = 20 * np.log10(e / e.max()); pk = int(db.argmax())
    s = pk
    while s > 0 and db[s - 1] > -30 and pk - s < 40: s -= 1
    lim = int(MAXL.get(cat, .9) * 100); t = pk
    while t < len(db) - 1 and (db[t] > -32 or t - pk < 8) and t - s < lim: t += 1
    y = x[max(0, s * 480 - 960): t * 480]
    f = int(.03 * SR); y[-f:] *= np.linspace(1, 0, f) ** 2
    y = y / (np.abs(y).max() + 1e-9) * 10 ** (-1 / 20)
    sp = np.abs(np.fft.rfft(y * np.hanning(len(y)))); fr = np.fft.rfftfreq(len(y), 1 / SR); cen = (sp * fr).sum() / sp.sum()
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', f'oneshot/{k}.wav'], input=y.astype(np.float32).tobytes())
    rows.append((k, len(y) / SR, cen, int(np.sum(db > -20))))
for r in rows: print(f'{r[0]:18s} {r[1]:.2f}s  centroid {r[2]:6.0f} Hz  dolu {r[3]}')
