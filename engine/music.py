"""Energetic background beats (procedural, deterministic, no downloads).
Ata (20 Eki): eski pad müziği uyutuyordu -> hareketli, adrenalinli fon.

  drive(dur, bpm, seed)  -> mono float array at SR
  python3 engine/music.py preview out.wav [style] [seconds]   # listen test

Styles (rotated per video by slug hash): 'trap' (124 bpm, 808 + backbeat clap + hat rolls + minor pluck arp),
'phonk' (132 bpm, cowbell-ish lead, distorted 808), 'drive' (122 bpm, four-on-the-floor + pulsing synth bass).
A file kit/music/<name>.wav (if present and MUSIC_FILE env set) overrides synthesis (looped with crossfade)."""
import os, sys, zlib
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

SR = 48000
def _lp(x, f, o=2): return sosfilt(butter(o, f, 'lowpass', fs=SR, output='sos'), x)
def _hp(x, f, o=2): return sosfilt(butter(o, f, 'highpass', fs=SR, output='sos'), x)
def _bp(x, a, b, o=2): return sosfilt(butter(o, [a, b], 'bandpass', fs=SR, output='sos'), x)
def mtof(m): return 440 * 2 ** ((m - 69) / 12)


def kick(rng, hard=1.0):
    L = int(.42 * SR); t = np.arange(L) / SR
    f = 46 + 120 * np.exp(-t * 38)
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) * np.exp(-t * 7.5) + .35 * np.sin(ph) * np.exp(-t * 40)
    click = _hp(rng.standard_normal(L), 3000) * np.exp(-t * 400) * .25
    return np.tanh((x + click) * 1.6 * hard) * .9


def clap(rng):
    L = int(.3 * SR); t = np.arange(L) / SR; n = rng.standard_normal(L)
    env = np.zeros(L)
    for d in (0, .011, .022): env += np.exp(-np.clip(t - d, 0, None) * 60) * (t >= d)
    env += .6 * np.exp(-t * 14)
    return _bp(n, 900, 6000) * env * .55


def hat(rng, open_=False):
    L = int((.22 if open_ else .05) * SR); t = np.arange(L) / SR
    return _hp(rng.standard_normal(L), 7500, 3) * np.exp(-t * (14 if open_ else 90)) * .32


def bass808(f, L, dist=1.8):
    t = np.arange(L) / SR
    ph = 2 * np.pi * np.cumsum(f * (1 + .0 * t)) / SR if np.ndim(f) else 2 * np.pi * f * t
    x = np.sin(ph) * np.minimum(1, t / .005) * np.exp(-t * 1.2)
    x *= np.clip((L / SR - t) / .03, 0, 1)
    return np.tanh(x * dist) * .55


def pluck(f, L, bright=3500):
    t = np.arange(L) / SR
    x = sum(np.sin(2 * np.pi * f * k * t) / k for k in range(1, 9))  # saw-ish
    x = x * np.exp(-t * 11) * np.minimum(1, t / .002)
    return _lp(x, bright) * .16


def bell(f, L):  # phonk cowbell-like lead
    t = np.arange(L) / SR
    x = np.sign(np.sin(2 * np.pi * f * t)) * .5 + np.sign(np.sin(2 * np.pi * f * 1.48 * t)) * .5
    return _bp(x, 500, 4000) * np.exp(-t * 9) * .13


def _put(buf, x, s):
    if s >= len(buf): return
    e = min(len(buf), s + len(x)); buf[s:e] += x[:e - s]


STYLES = {
    'trap':  dict(bpm=124, prog=[[38, 62, 65, 69], [34, 58, 62, 65], [31, 55, 58, 62], [33, 57, 61, 64]]),   # Dm Bb Gm A
    'phonk': dict(bpm=132, prog=[[40, 64, 67, 71], [36, 60, 64, 67], [38, 62, 65, 69], [35, 59, 62, 66]]),   # Em C Dm Bm
    'drive': dict(bpm=122, prog=[[33, 57, 60, 64], [29, 53, 57, 60], [36, 60, 64, 67], [31, 55, 59, 62]]),   # Am F C G
}


def drive(dur, style='trap', seed=7):
    S = STYLES[style]; bpm = S['bpm']; prog = S['prog']
    rng = np.random.default_rng(seed)
    n = int(dur * SR); step = 60 / bpm / 4; bar = step * 16
    D, B, M = np.zeros(n), np.zeros(n), np.zeros(n)
    K, C = kick(rng), clap(rng)
    nbars = int(dur / bar) + 2
    for b in range(nbars):
        ch = prog[b % 4]; t0 = b * bar; root = ch[0]
        fill = b % 4 == 3; intro = b == 0
        # drums
        if style == 'drive':
            kicks = [0, 4, 8, 12]; claps = [4, 12]
        elif style == 'phonk':
            kicks = [0, 3, 8, 11, 14] if not fill else [0, 3, 8, 10, 12, 14]; claps = [4, 12]
        else:
            kicks = [0, 7, 10] if not fill else [0, 7, 10, 13, 15]; claps = [4, 12]
        if not intro:
            for k in kicks: _put(D, K * (1 if k == 0 else .85), int((t0 + k * step) * SR))
        for c in claps: _put(D, C * (.6 if intro else 1), int((t0 + c * step) * SR))
        for h in range(16):
            if style == 'drive' and h % 4 == 2: _put(D, hat(rng, True) * .8, int((t0 + h * step) * SR)); continue
            acc = .9 if h % 2 == 0 else .55
            if fill and h >= 12 and style != 'drive':  # 32nd/triplet roll into next bar
                for r in range(3 if h < 14 else 2): _put(D, hat(rng) * (.45 + .1 * r), int((t0 + h * step + r * step / (3 if h < 14 else 2)) * SR))
            else:
                _put(D, hat(rng) * acc, int((t0 + h * step) * SR))
        # 808 / synth bass
        if style == 'drive':
            for h in range(16):
                if h % 2 == 1: _put(B, bass808(mtof(root + 12), int(step * 1.6 * SR), 2.5) * .7, int((t0 + h * step) * SR))
        else:
            hits = [0, 7, 10] if style == 'trap' else [0, 3, 8, 11, 14]
            for i, k in enumerate(hits):
                L = int(((hits[i + 1] if i + 1 < len(hits) else 16) - k) * step * SR)
                if not intro: _put(B, bass808(mtof(root), L, 2.2 if style == 'phonk' else 1.8), int((t0 + k * step) * SR))
        # melodic motion: 16th arp over chord tones
        notes = ch[1:] + [ch[1] + 12]
        pat = [0, 1, 2, 3, 2, 1, 2, 3] if style != 'phonk' else [0, 2, 1, 3, 0, 2, 3, 1]
        for h in range(16):
            if style == 'phonk' and h % 2: continue
            m = notes[pat[h % 8]] + (12 if style == 'trap' else 0)
            L = int(step * (2 if style == 'phonk' else 1.3) * SR)
            snd = bell(mtof(m), L) if style == 'phonk' else pluck(mtof(m), L, 2600 if intro else 4200)
            _put(M, snd * (.8 if h % 4 else 1), int((t0 + h * step) * SR))
    mix = .95 * D + .8 * B + .9 * M
    # light glue: soft clip + sidechain pump on kicks for movement
    mix = np.tanh(mix * 1.2) / np.tanh(1.2)
    return mix


# ---------- 'gerilim' (documentary tension) — default since Ata found trap/phonk "promotional" (20 Eki) ----------
# Research-led: under narration keep tempo moderate (~85 bpm), no hats/claps/bright arps, dark minor harmony,
# low sub pulse + soft clock tick for urgency, sparse piano motif; energy comes from drops/section changes, not density.
def _saw(f, t, n=10): return sum(np.sin(2 * np.pi * f * k * t) / k for k in range(1, n))


def tension(dur, drops=(), seed=11, bpm=86):
    rng = np.random.default_rng(seed)
    n = int(dur * SR); t = np.arange(n) / SR; beat = 60 / bpm; bar = 4 * beat
    prog = [(38, [50, 53, 57]), (34, [50, 53, 58]), (31, [50, 55, 58]), (33, [49, 52, 57])]  # Dm Bb Gm A
    pad, sub, pno, tick, kik = (np.zeros(n) for _ in range(5))
    nb = int(dur / bar) + 2
    for b in range(nb):
        root, ch = prog[b % 4]; s0 = int(b * bar * SR); L = min(n - s0, int(bar * SR) + int(.4 * SR))
        if L <= 0: break
        tt = np.arange(L) / SR; e = np.clip(tt / .6, 0, 1) * np.clip((L / SR - tt) / .5, 0, 1)
        x = sum(_saw(mtof(m) * (1 + d), tt, 6) for m in ch for d in (-.003, .003)) / 6
        pad[s0:s0 + L] += x * e
        # sub pulse on 8ths (heartbeat feel), accent on beat
        for k in range(8):
            ps = s0 + int(k * beat / 2 * SR); PL = min(n - ps, int(beat / 2 * SR))
            if PL <= 0: continue
            ptt = np.arange(PL) / SR
            sub[ps:ps + PL] += np.sin(2 * np.pi * mtof(root) * ptt) * np.exp(-ptt * 7) * (1 if k % 2 == 0 else .55)
            # clock tick
            TL = min(n - ps, int(.03 * SR)); tick[ps:ps + TL] += _hp(rng.standard_normal(TL), 4000)[:TL] * np.exp(-np.arange(TL) / SR * 220) * (.5 if k % 2 else .8)
        # soft low thump on 1 and 3 from bar 2
        if b >= 2:
            for k in (0, 2):
                ks = s0 + int(k * beat * SR); KL = min(n - ks, int(.35 * SR))
                if KL > 0: kt = np.arange(KL) / SR; kik[ks:ks + KL] += np.sin(2 * np.pi * (42 + 50 * np.exp(-kt * 30)) * kt) * np.exp(-kt * 9)
        # sparse piano motif: 3 notes per bar, every other bar
        if b % 2 == 0:
            for j, (off, m) in enumerate([(0, ch[2] + 12), (1.5, ch[1] + 12), (3, ch[0] + 12)]):
                ns = s0 + int(off * beat * SR); NL = min(n - ns, int(2.5 * SR))
                if NL <= 0: continue
                nt = np.arange(NL) / SR; f = mtof(m)
                pno[ns:ns + NL] += (np.sin(2 * np.pi * f * nt) + .4 * np.sin(4 * np.pi * f * nt) + .15 * np.sin(6 * np.pi * f * nt)) * np.exp(-nt * 2.2) * np.minimum(1, nt / .004)
    # filter slowly opens across the video -> rising urgency
    pad = _lp(pad, 700) * .9 + _lp(pad, 1600) * np.clip(t / max(dur, 1), 0, 1) * .5
    mix = .55 * pad + .9 * _lp(sub, 200) + .25 * tick + .45 * _lp(pno, 3000) + .7 * kik
    # drops: before each section change (riser time) pull music to near-silence, then re-enter
    g = np.ones(n)
    for d in drops:
        a, b2 = int((d - .9) * SR), int((d + .05) * SR)
        if 0 < a < n:
            r = np.arange(max(0, a), min(n, b2)); x = (r - a) / max(1, b2 - a)
            g[r] = np.minimum(g[r], np.clip(1 - x * 4, .12, 1))
    g = np.convolve(g, np.ones(int(.06 * SR)) / int(.06 * SR), mode='same')
    return np.tanh(mix * g * 1.1)


def style_for(slug):
    return 'gerilim'  # Ata 20 Eki: trap/phonk/drive "promotional" -> documentary tension is the default
    names = list(STYLES)
    try: return names[int(slug[8:10]) % len(names)]  # YYYY-MM-DD-...: day of month rotates styles
    except ValueError: return names[zlib.crc32(slug.encode()) % len(names)]


if __name__ == '__main__':
    if len(sys.argv) >= 3 and sys.argv[1] == 'preview':
        st = sys.argv[3] if len(sys.argv) > 3 else 'trap'; sec = float(sys.argv[4]) if len(sys.argv) > 4 else 20
        x = drive(sec, st); x = x / np.max(np.abs(x)) * .9
        wavfile.write(sys.argv[2], SR, (np.stack([x, x], 1) * 32767).astype(np.int16)); print('wrote', sys.argv[2], st)
    else:
        sys.exit(__doc__)
