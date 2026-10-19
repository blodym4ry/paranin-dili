"""v2 sound design, following the 'Ultimate Editors' rules:
  WHOOSHES  -> every movement, peak on the fastest frame, -12 dB (max -10)
  TEXTURES  -> every non-slide event (pop, click, marker write-out, reveal, impact), -7 dB
  RISERS+HITS -> anticipation into new segments; ~5 s after hook, + 3 more; riser ends on the cut, hit under it, -5 dB
  MUSIC     -> only under the talking head, -19 dB under the voice; never under graphics
Every sound is synthesized here (no library available). Separate stems are written so each family can be inspected.
usage: python3 audio2.py edl2.json voice.wav out.wav
"""
import json, sys, os
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

SR = 48000
rng = np.random.default_rng(11)
db = lambda x: 10 ** (x / 20)
def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, min(hi, SR / 2 - 100)], 'bandpass', fs=SR, output='sos'), x)
def lp(x, f, o=2): return sosfilt(butter(o, f, 'lowpass', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'highpass', fs=SR, output='sos'), x)
def T(d): return np.arange(int(d * SR)) / SR
def norm(x): return x / (np.max(np.abs(x)) + 1e-9)

# ---------- WHOOSHES ----------
def whoosh(dur=.7, lo=250, hi=3000, kind='hollow'):
    """peak at the middle of the clip (returned with its peak offset)."""
    n = int(dur * SR); t = np.arange(n) / SR; x = rng.standard_normal(n); out = np.zeros(n); steps = 28
    for i in range(steps):
        a, b = i * n // steps, (i + 1) * n // steps
        ph = np.sin(np.pi * (i + .5) / steps)
        f = lo * (hi / lo) ** (ph * .95)
        seg = bp(x[max(0, a - 3000):b], f * .55, f * 1.7)[-(b - a):]
        out[a:b] = seg
    env = np.sin(np.pi * np.clip(t / dur, 0, 1)) ** (2.6 if kind == 'hollow' else 1.8)
    s = out * env
    if kind == 'deep':  # sci-fi "deep voice" texture: add a pitched body
        s += .35 * np.sin(2 * np.pi * (90 + 160 * np.sin(np.pi * t / dur)) * t) * env
    if kind == 'wind':
        s = lp(s, 2200)
    return norm(lp(s, 7000)), dur / 2

# ---------- TEXTURES ----------
def pop(f=700):
    t = T(.14); s = np.sin(2 * np.pi * f * t * (1 + .3 * np.exp(-t * 45))) * np.exp(-t * 30)
    return norm(lp(s, 3000)), .004
def ui_click():
    t = T(.06); s = (np.sin(2 * np.pi * 2900 * t) * np.exp(-t * 120) + .6 * rng.standard_normal(len(t)) * np.exp(-t * 400))
    return norm(hp(s, 900)), .002
def scifi_click():
    t = T(.12); s = np.sin(2 * np.pi * (1800 - 900 * t / .12) * t) * np.exp(-t * 45) + .4 * np.sin(2 * np.pi * 5200 * t) * np.exp(-t * 90)
    return norm(s), .002
def marker(dur=.6):
    """diegetic marker-on-paper scribble for brush write-outs."""
    t = T(dur); x = bp(rng.standard_normal(len(t)), 1800, 7000)
    am = .55 + .45 * np.sin(2 * np.pi * 23 * t + 3 * np.sin(2 * np.pi * 3 * t))
    env = np.clip(t / .03, 0, 1) * np.clip((dur - t) / .08, 0, 1)
    return norm(x * am * env), .03
def impact():
    """sci-fi impact for reveals: low thump + short metallic ring."""
    t = T(.9); body = np.sin(2 * np.pi * (48 + 70 * np.exp(-t * 18)) * t) * np.exp(-t * 6)
    ring = sum(a * np.sin(2 * np.pi * f * t) for f, a in [(1240, .5), (1871, .3), (2633, .2)]) * np.exp(-t * 9)
    nz = hp(rng.standard_normal(len(t)), 3000) * np.exp(-t * 40) * .4
    return norm(body + .35 * ring + nz), .004
def stamp():
    t = T(.35); s = lp(rng.standard_normal(len(t)), 1200) * np.exp(-t * 28) + np.sin(2 * np.pi * 70 * t) * np.exp(-t * 16)
    return norm(s), .003
def gears(n=8, span=1.0):
    """ticks for counters (mechanical gizmo)."""
    out = np.zeros(int((span + .1) * SR))
    for k in range(n):
        p = (k / max(1, n - 1)) ** .6 * span; s = int(p * SR); t = T(.03)
        tick = np.sin(2 * np.pi * (2400 + 120 * k) * t) * np.exp(-t * 180)
        out[s:s + len(t)] += tick
    return norm(hp(out, 1000)), .0
def paper_drop():
    t = T(.22); s = bp(rng.standard_normal(len(t)), 500, 4000) * np.exp(-t * 26) + .4 * np.sin(2 * np.pi * 110 * t) * np.exp(-t * 30)
    return norm(s), .003
def success():
    t = T(.9); s = np.zeros(len(t))
    for i, f in enumerate([880, 1318.5]):
        d = int(i * .09 * SR); tt = t[:len(t) - d]; s[d:] += np.sin(2 * np.pi * f * tt) * np.exp(-tt * 5)
    return norm(s), .003

# ---------- RISERS & HITS ----------
def sharp_bass_riser(dur=1.8):
    t = T(dur); f = 38 * (4.2 ** (t / dur) ** 2)
    ph = 2 * np.pi * np.cumsum(f) / SR
    s = np.sin(ph) + .5 * np.sin(2 * ph) + .25 * np.sign(np.sin(3 * ph)) * .5
    nz = hp(rng.standard_normal(len(t)), 2500) * (t / dur) ** 3 * .5
    env = (t / dur) ** 2.2 * np.clip((dur - t) / .02, 0, 1)
    return norm(lp(s, 900) * env + nz * env), dur
def metallic_riser(dur=1.8):
    t = T(dur); s = np.zeros(len(t))
    for f0, a in [(410, 1), (633, .7), (977, .5), (1514, .35), (2213, .25)]:
        f = f0 * (1 + 1.4 * (t / dur) ** 2); s += a * np.sin(2 * np.pi * np.cumsum(f) / SR)
    rev = hp(rng.standard_normal(len(t)), 5000) * (t / dur) ** 4  # reversed-cymbal swell
    env = (t / dur) ** 2.4 * np.clip((dur - t) / .02, 0, 1)
    return norm(s * env * .7 + rev * env * .6), dur
def hit():
    t = T(1.4); body = np.sin(2 * np.pi * (42 + 60 * np.exp(-t * 14)) * t) * np.exp(-t * 3.2)
    nz = lp(rng.standard_normal(len(t)), 3000) * np.exp(-t * 12) * .5
    return norm(body + nz), .002

# ---------- MUSIC (talking head only) ----------
def music(dur, bpm=92):
    n = int(dur * SR); t = np.arange(n) / SR; beat = 60 / bpm
    prog = [[50, 53, 57, 60], [46, 50, 53, 58], [48, 52, 55, 60], [45, 48, 52, 57]]  # Dm Bb C Am — dark, premium
    pad = np.zeros(n); clen = beat * 8
    for k in range(int(dur / clen) + 2):
        s0 = int(k * clen * SR); s1 = min(n, int((k + 1) * clen * SR) + int(.5 * SR))
        if s0 >= n: break
        L = s1 - s0; tt = np.arange(L) / SR; e = np.clip(tt / 1.0, 0, 1) * np.clip((L / SR - tt) / .8, 0, 1)
        for m in prog[k % 4]:
            f = 440 * 2 ** ((m - 69) / 12)
            for d in (-.08, .08): pad[s0:s1] += e * np.sin(2 * np.pi * f * 2 ** (d / 12) * tt) / 8
    pulse = np.zeros(n)
    for i in range(int(dur / beat) + 1):
        s = int(i * beat * SR)
        if s >= n: break
        L = min(int(.3 * SR), n - s); tt = np.arange(L) / SR
        pulse[s:s + L] += np.sin(2 * np.pi * (46 + 40 * np.exp(-tt * 25)) * tt) * np.exp(-tt * 9) * (1 if i % 2 == 0 else .55)
    return lp(pad, 1800) + .6 * pulse

# ---------- placement ----------
class Track:
    def __init__(s, n): s.buf = np.zeros(n)
    def place(s, snd, t_event, level_db):
        clip, hit_off = snd
        st = int((t_event - hit_off) * SR)
        if st < 0: clip = clip[-st:]; st = 0
        e = min(len(s.buf), st + len(clip))
        if e > st: s.buf[st:e] += clip[:e - st] * db(level_db)
    def place_end(s, snd, t_end, level_db):  # risers: end exactly on the cut
        clip, d = snd; s.place((clip, 0), t_end - d, level_db)

def av_opacity(edl, n):
    L = edl['layout']; o = {'A': 1, 'B': 0, 'E': 1}; o.update({k: v['av'].get('o', 1) for k, v in edl.get('layouts', {}).items()}); tt = np.arange(n) / SR; out = np.zeros(n)
    for i, cur in enumerate(L):
        prev = L[i - 1] if i else cur; t0 = cur['t']; t1 = L[i + 1]['t'] if i + 1 < len(L) else 1e9
        m = (tt >= t0) & (tt < t1); x = np.clip((tt[m] - t0) / .85, 0, 1); x = np.where(x < .5, 4 * x ** 3, 1 - (-2 * x + 2) ** 3 / 2)
        out[m] = o[prev['s']] + (o[cur['s']] - o[prev['s']]) * x
    return out

def main(edl_p, voice_p, out_p):
    edl = json.load(open(edl_p)); a = edl['anchors']; S = {s['id']: s for s in edl['scenes']}
    sr, v = wavfile.read(voice_p); v = v.astype(float) / 32768; v = v.mean(1) if v.ndim == 2 else v
    dur = len(v) / SR + .5; n = int(dur * SR)
    voice = np.zeros(n); voice[:len(v)] = v; voice = voice / np.max(np.abs(voice)) * db(-1)
    W, X, R, H = Track(n), Track(n), Track(n), Track(n)
    cues = []
    def w(t, lvl=-12, kind='hollow', d=.7, why=''): W.place(whoosh(d, kind=kind), t, lvl); cues.append((t, 'WHOOSH', kind, lvl, why))
    XA = Track(n)
    ACCENT = ('big 0 reveal', 'strike on', 'PEŞİN stamp', 'Tesla logo pulse', 'Reddedildi', 'card flips', 'conclusion', 'red X')
    def x(t, snd, lvl=-7, why=''):
        acc = any(why.startswith(k) for k in ACCENT)
        (XA if acc else X).place(snd, t, lvl); cues.append((t, 'ACCENT' if acc else 'TEXTURE', why, lvl, ''))
    # PASS 1 — whooshes (peak = fastest frame)
    for L in edl['layout'][1:]:
        big = True
        w(L['t'] + .425, -10 if big else -12, 'deep', .9, f"layout -> {L['s']}")
    def st(i): return S[i]['start']
    w(st('elon') + .12, -14, 'wind', .6, 'Elon card rises')
    for i in range(6): w(st('elon') + 1.2 + i * .28 + .55, -18, 'wind', .45, 'deposit chip flies in')
    w(st('clip2017') + .3, -12, 'hollow', .8, 'clipping slides in')
    w(st('deposit') + .22, -12, 'hollow', .7, 'deposit card rises')
    w(st('bank') + .2, -12, 'hollow', .7, 'bank card rises')
    w(st('balance') + .2, -12, 'hollow', .7, 'balance sheet rises')
    for k in ['elon', 'zero', 'timeline', 'vault', 'everyday', 'question', 'sig']: pass
    for e in edl['emph']: w(e['t0'] + .3 + .2, -16, 'wind', .6, 'emphasis text rises')
    # PASS 2 — textures (on the event frame)
    x(st('zero') + .2, impact(), -7, 'big 0 reveal')
    x(st('zero') + .55, marker(.8), -8, 'brush circle write-out')
    e0 = edl['emph'][0]; x(e0['t0'] + e0['strikeAt'], marker(.4), -7, 'strike on dolandırıcılık')
    x(st('clip2017') + .9, marker(.7), -8, 'headline underline')
    d = S['deposit']; x(d['start'] + .5, gears(10, 1.0), -9, 'price counter'); x(d['start'] + 1.85, ui_click(), -6, 'Rezerve et click')
    x(d['start'] + d['sub']['founders'] + .1, gears(10, 1.0), -9, 'price counter 250K'); x(d['start'] + d['sub']['founders'] + 1.25, stamp(), -6, 'PEŞİN stamp')
    tl = S['timeline']
    for k in ['y2020', 'y2023', 'y2026', 'y2028']: x(tl['start'] + tl['sub'][k], pop(620), -9, f'timeline row {k}')
    for k in ['y2020', 'y2023']: x(tl['start'] + tl['sub'][k] + .7, marker(.4), -7, 'red X write-out')
    x(tl['start'] + tl['sub']['y2026'] + .35, scifi_click(), -8, 'Roadster photo pops')
    x(tl['start'] + tl['sub']['y2028'] + .6, pop(520), -7, '? pops')
    vt = S['vault']
    for i in range(18):
        land = vt['start'] + .25 + i * .11 + .62 + (i % 3) * .03
        if i < 9 or i % 2 == 0: x(land, paper_drop(), -11 - (i % 3), 'bill lands')
    x(vt['start'] + vt['sub']['tesla'], impact(), -7, 'Tesla logo pulse')
    bk = S['bank']
    for i in range(3): x(bk['start'] + .3 + i * .22, ui_click(), -10, 'row appears')
    x(bk['start'] + bk['sub']['rej'], scifi_click(), -6, 'Reddedildi'); x(bk['start'] + bk['sub']['rej'] + .05, marker(.35), -8, 'X write-out')
    x(bk['start'] + bk['sub']['cust'] + .3, success(), -8, 'card flips to approved')
    bl = S['balance']; x(bl['start'] + 1.0, marker(.5), -7, 'underline müşteri avansları'); x(bl['start'] + 1.2, pop(560), -9, 'term appears')
    ev = S['everyday']; x(ev['start'], ui_click(), -7, 'Tesla tile')
    x(ev['start'] + ev['sub']['phone'], ui_click(), -7, 'phone tile'); x(ev['start'] + ev['sub']['member'], ui_click(), -7, 'membership tile')
    q = S['question']; x(q['start'] + 1.4, marker(.6), -8, 'question underline')
    x(S['sig']['start'] + .05, success(), -9, 'conclusion')
    # PASS 3 — risers & hits (end on the transition frame)
    cut1 = a['y2017'] - .3   # ~5 s after the hook: into the body
    R.place_end(sharp_bass_riser(2.0), cut1, -5); H.place(hit(), cut1, -9); cues.append((cut1, 'RISER', 'sharp bass + hit', -5, 'hook -> body'))
    cut2 = a['size'] - .15
    R.place_end(metallic_riser(1.6), cut2, -6); H.place(hit(), cut2, -11); cues.append((cut2, 'RISER', 'metallic + hit', -6, 'into the question'))
    cut3 = a['hepsinde'] - .15
    R.place_end(sharp_bass_riser(1.5), cut3, -6); H.place(hit(), cut3, -10); cues.append((cut3, 'RISER', 'sharp bass + hit', -6, 'into the payoff'))
    cut4 = a['oyuzden'] - .3
    R.place_end(metallic_riser(1.4), cut4, -7); H.place(hit(), cut4, -12); cues.append((cut4, 'RISER', 'metallic + hit', -7, 'into the outro'))
    # PASS 4 — music only under the talking head, -19 dB under voice
    mus = music(dur, edl['bpm']); gate = av_opacity(edl, n)
    k = int(.25 * SR); gate = np.convolve(gate, np.ones(k) / k, mode='same')
    vr = np.sqrt(np.mean(voice[np.abs(voice) > .01] ** 2)); mr = np.sqrt(np.mean(mus ** 2))
    mus = mus / mr * vr * db(-19) * gate
    fade = np.clip(np.arange(n) / SR / 1.0, 0, 1) * np.clip((dur - np.arange(n) / SR) / 1.2, 0, 1); mus *= fade
    # voice is king: duck SFX under speech so nothing beats the voice
    env = np.convolve(np.abs(voice), np.ones(int(.05 * SR)) / int(.05 * SR), mode='same')
    venv = env / env.max()
    # BUS LEVELS (Ata, v3 feedback): voice always intelligible; simple transition sounds well down,
    # emphasis/accent sounds a bit louder than transitions but still under the voice.
    BUS = {'whoosh': -9, 'simple': -9, 'accent': -2, 'riser': -4, 'hit': -3}
    simple = W.buf * db(BUS['whoosh']) + X.buf * db(BUS['simple'])
    accent = XA.buf * db(BUS['accent']) + R.buf * db(BUS['riser']) + H.buf * db(BUS['hit'])
    duck_s = 1 - .75 * np.clip(venv * 4, 0, 1)   # transitions almost vanish under speech
    duck_a = 1 - .45 * np.clip(venv * 3, 0, 1)
    mix = voice + simple * duck_s + accent * duck_a + mus
    peak = np.max(np.abs(mix))
    if peak > .98: mix *= .98 / peak
    os.makedirs('stems', exist_ok=True)
    for name, b in [('voice', voice), ('whooshes', W.buf), ('textures', X.buf), ('accents', XA.buf), ('risers', R.buf), ('hits', H.buf), ('music', mus)]:
        wavfile.write(f'stems/{name}.wav', SR, (np.clip(b, -1, 1) * 32767).astype(np.int16))
    wavfile.write(out_p, SR, (np.stack([mix, mix], 1) * 32767).astype(np.int16))
    with open('stems/cue_sheet.txt', 'w') as f:
        for c in sorted(cues): f.write(f'{c[0]:7.2f}s  {c[1]:8s} {c[2]:<28s} {c[3]:>4} dB  {c[4]}\n')
    print('cues', len(cues), 'peak', round(20 * np.log10(peak), 1), 'dBFS', 'dur', round(dur, 2))

if __name__ == '__main__': main(*sys.argv[1:4])
