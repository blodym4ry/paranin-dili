"""Energetic background beats (procedural, deterministic, no downloads).
Ata (20 Eki): eski pad müziği uyutuyordu -> hareketli, adrenalinli fon.

  drive(dur, bpm, seed)  -> mono float array at SR
  python3 engine/music.py preview out.wav [style|gerilim:N] [seconds]   # listen test

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


# ---------- 'gerilim' family (documentary / calm-tension) — default since Ata found trap/phonk "promotional" (20 Eki) ----------
# Research-led: under narration keep tempo moderate (78-92 bpm), no hats/claps/bright arps, soft highs, sparse motif;
# energy comes from drops before section changes + slowly opening filter, not density. 7 variants rotate by date so
# consecutive videos never share a bed; warm voicings so it suits every age group.
def _saw(f, t, n=10): return sum(np.sin(2 * np.pi * f * k * t) / k for k in range(1, n))

MINOR = {'i': (0, 'm'), 'iv': (5, 'm'), 'V': (7, 'M'), 'VI': (8, 'M'), 'III': (3, 'M'), 'VII': (10, 'M')}
MAJOR = {'I': (0, 'M'), 'V': (7, 'M'), 'vi': (9, 'm'), 'IV': (5, 'M')}
VARIANTS = [
    dict(name='gece',     key=50, mode='m', prog=['i', 'VI', 'iv', 'V'],   bpm=86, lead='piano',   tick=True,  pulse='8th'),
    dict(name='ufuk',     key=52, mode='m', prog=['i', 'VI', 'III', 'VII'], bpm=84, lead='mallet',  tick=False, pulse='quarter'),
    dict(name='nabiz',    key=47, mode='m', prog=['i', 'iv', 'VI', 'V'],   bpm=90, lead='pluck',   tick=False, pulse='heart'),
    dict(name='aydinlik', key=53, mode='M', prog=['I', 'V', 'vi', 'IV'],   bpm=88, lead='piano',   tick=True,  pulse='8th'),
    dict(name='derin',    key=55, mode='m', prog=['i', 'VI', 'III', 'VII'], bpm=78, lead='strings', tick=True,  pulse='quarter'),
    dict(name='sehir',    key=48, mode='m', prog=['i', 'VI', 'iv', 'V'],   bpm=92, lead='keys',    tick=False, pulse='8th'),
    dict(name='yukselis', key=57, mode='m', prog=['i', 'VI', 'III', 'VII'], bpm=88, lead='mallet',  tick=True,  pulse='8th'),
]


def _chord(key, mode, deg):
    off, q = (MINOR if mode == 'm' else MAJOR)[deg]
    r = key + off
    while r > 57: r -= 12
    tri = [r, r + (3 if q == 'm' else 4), r + 7]
    return r - 24, tri


def _lead(kind, f, L):
    t = np.arange(L) / SR; a = np.minimum(1, t / .004)
    if kind == 'piano':   x = (np.sin(2*np.pi*f*t) + .4*np.sin(4*np.pi*f*t) + .15*np.sin(6*np.pi*f*t)) * np.exp(-t * 2.2)
    elif kind == 'mallet': x = (np.sin(2*np.pi*f*t) + .25*np.sin(2*np.pi*f*4.0*t) * np.exp(-t * 9)) * np.exp(-t * 3.0)
    elif kind == 'pluck':  x = _lp(_saw(f, t, 6), 1800) * np.exp(-t * 6) * 1.2
    elif kind == 'keys':   x = (np.sin(2*np.pi*f*t) + .3*np.sin(2*np.pi*f*3*t) * np.exp(-t * 4)) * np.exp(-t * 1.6) * (1 + .15*np.sin(2*np.pi*5*t))
    else:                  a = np.minimum(1, t / .35); x = _lp(_saw(f, t, 8), 1500) * np.exp(-t * .9) * .8   # strings swell
    return x * a


def tension(dur, drops=(), variant=0, seed=11):
    V = VARIANTS[variant % len(VARIANTS)]
    rng = np.random.default_rng(seed + variant)
    n = int(dur * SR); t = np.arange(n) / SR; beat = 60 / V['bpm']; bar = 4 * beat
    pad, sub, lead, tick, kik = (np.zeros(n) for _ in range(5))
    for b in range(int(dur / bar) + 2):
        root, ch = _chord(V['key'], V['mode'], V['prog'][b % 4]); s0 = int(b * bar * SR)
        L = min(n - s0, int(bar * SR) + int(.4 * SR))
        if L <= 0: break
        tt = np.arange(L) / SR; e = np.clip(tt / .6, 0, 1) * np.clip((L / SR - tt) / .5, 0, 1)
        pad[s0:s0 + L] += sum(_saw(mtof(m) * (1 + d), tt, 6) for m in ch for d in (-.003, .003)) / 6 * e
        steps = {'8th': [(k * .5, 1 if k % 2 == 0 else .55) for k in range(8)], 'quarter': [(k, 1 if k % 2 == 0 else .7) for k in range(4)],
                 'heart': [(0, 1), (.35, .7), (2, 1), (2.35, .7)]}[V['pulse']]
        for off, acc in steps:
            ps = s0 + int(off * beat * SR); PL = min(n - ps, int(beat / 2 * SR))
            if PL <= 0: continue
            ptt = np.arange(PL) / SR
            sub[ps:ps + PL] += np.sin(2 * np.pi * mtof(root + 12) * ptt) * np.exp(-ptt * 7) * acc
            if V['tick']:
                TL = min(n - ps, int(.03 * SR)); tick[ps:ps + TL] += _bp(rng.standard_normal(TL), 2500, 6000)[:TL] * np.exp(-np.arange(TL) / SR * 220) * acc
        if b >= 2:
            for k in (0, 2):
                ks = s0 + int(k * beat * SR); KL = min(n - ks, int(.35 * SR))
                if KL > 0: kt = np.arange(KL) / SR; kik[ks:ks + KL] += np.sin(2 * np.pi * (42 + 45 * np.exp(-kt * 30)) * kt) * np.exp(-kt * 9)
        if b % 2 == 0 or V['lead'] == 'strings':
            motif = [(0, ch[2] + 12), (1.5, ch[1] + 12), (3, ch[0] + 12)] if V['lead'] != 'strings' else [(0, ch[2] + 12)]
            for off, m in motif:
                ns = s0 + int(off * beat * SR); NL = min(n - ns, int((bar if V['lead'] == 'strings' else 2.5) * SR))
                if NL > 0: lead[ns:ns + NL] += _lead(V['lead'], mtof(m), NL)
    pad = _lp(pad, 700) * .9 + _lp(pad, 1500) * np.clip(t / max(dur, 1), 0, 1) * .45
    mix = .55 * pad + .85 * _lp(sub, 180) + .18 * tick + .42 * _lp(lead, 2800) + .6 * kik
    g = np.ones(n)
    for d in drops:
        a, b2 = int((d - .9) * SR), int((d + .05) * SR)
        if 0 < a < n:
            r = np.arange(a, min(n, b2)); x = (r - a) / max(1, b2 - a)
            g[r] = np.minimum(g[r], np.clip(1 - x * 4, .12, 1))
    g = np.convolve(g, np.ones(int(.06 * SR)) / int(.06 * SR), mode='same')
    return np.tanh(mix * g * 1.1)


# ---------- 'karanlik_hiphop' (Ata 21 Eki seçimi: piyano/yumuşak yok, promosyon yok) ----------
# Dark minimal hip-hop: boom-bap kick + soft snare, sub/808 bass line, quiet shaker, one dark filtered stab per bar.
# No piano, no bright plucks, no hi-hat spam. Energy from groove + bass; drops before section changes.
def _snare_soft(rng):
    L = int(.25 * SR); t = np.arange(L) / SR
    return _bp(rng.standard_normal(L), 1200, 5000) * np.exp(-t * 22) * .45 + np.sin(2 * np.pi * 190 * t) * np.exp(-t * 30) * .35


def _shaker(rng):
    L = int(.06 * SR); t = np.arange(L) / SR
    return _bp(rng.standard_normal(L), 3000, 7000) * np.exp(-t * 60) * .12


def dark_hiphop(dur, drops=(), seed=5, bpm=92, key=36):
    rng = np.random.default_rng(seed)
    n = int(dur * SR); st = 60 / bpm / 4; bar = 16 * st
    prog = [[0, 3, 7], [-4, 0, 3], [-2, 2, 5], [-5, -1, 2]]   # i VI VII v
    D, B, S = np.zeros(n), np.zeros(n), np.zeros(n)
    K, SN = kick(rng, .9), _snare_soft(rng)
    for b in range(int(dur / bar) + 2):
        t0 = b * bar; ch = prog[b % 4]; root = key + ch[0]; intro = b == 0; fill = b % 4 == 3
        for h in [0, 7, 10] + ([14] if fill else []):
            if not intro: _put(D, K, int((t0 + h * st) * SR))
        for h in (4, 12): _put(D, SN * (.5 if intro else 1), int((t0 + h * st) * SR))
        for h in range(0, 16, 2): _put(D, _shaker(rng) * (1 if h % 4 else .6), int((t0 + h * st) * SR))
        hits = [0, 7, 10]
        for i, h in enumerate(hits):
            L = int(((hits[i + 1] if i + 1 < len(hits) else 16) - h) * st * SR)
            if not intro: _put(B, bass808(mtof(root), L, 1.6) * .9, int((t0 + h * st) * SR))
        L = int(bar * SR); tt = np.arange(L) / SR
        _put(S, sum(_lp(_saw(mtof(key + 24 + c), tt, 6), 900) for c in ch) * np.exp(-tt * 4) * .08, int(t0 * SR))
    mix = .9 * D + .85 * B + .8 * S
    g = np.ones(n)
    for d in drops:
        a, b2 = int((d - .7) * SR), int((d + .05) * SR)
        if 0 < a < n:
            r = np.arange(a, min(n, b2)); x = (r - a) / max(1, b2 - a); g[r] = np.minimum(g[r], np.clip(1 - x * 4, .1, 1))
    g = np.convolve(g, np.ones(int(.05 * SR)) / int(.05 * SR), mode='same')
    return np.tanh(mix * g * 1.15) / np.tanh(1.15)


# ---------- 'modern_oryantal' (Ata 22 Eki seçimi: düğün altını) darbuka + derin bas + ud benzeri pluck, hicaz dizisi ----------
HIJAZ = [0, 1, 4, 5, 7, 8, 10]
def _doum(rng):
    L = int(.35 * SR); t = np.arange(L) / SR
    f = 95 * (1 + .6 * np.exp(-t * 30))
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9) * .95
def _tek(rng, acc=1.0):
    L = int(.12 * SR); t = np.arange(L) / SR
    nz = _bp(rng.standard_normal(L), 1800, 6500) * np.exp(-t * 45)
    ring = np.sin(2 * np.pi * 420 * t) * np.exp(-t * 35) * .4
    return (nz * .55 + ring) * acc
def _ks(f, L, rng, damp=.996):   # karplus-strong: ud/saz benzeri telli
    N = max(2, int(SR / f)); buf = rng.uniform(-1, 1, N); out = np.zeros(L)
    for i in range(L):
        out[i] = buf[i % N]; buf[i % N] = damp * .5 * (buf[i % N] + buf[(i + 1) % N])
    return _lp(out, 4200) * .6
def oriental(dur, drops=(), seed=9, bpm=100, key=38):
    rng = np.random.default_rng(seed)
    n = int(dur * SR); st = 60 / bpm / 4; bar = 16 * st
    D, B, L1, P = np.zeros(n), np.zeros(n), np.zeros(n), np.zeros(n)
    DO = _doum(rng)
    maqsum = [(0, 'D'), (2, 'T'), (6, 'T'), (8, 'D'), (12, 'T')]
    phrase = [(0, 7), (2, 8), (3, 7), (4, 5), (6, 4), (8, 5), (10, 4), (11, 1), (12, 0)]
    for b in range(int(dur / bar) + 2):
        t0 = b * bar; intro = b == 0; fill = b % 4 == 3
        for h, k in maqsum:
            x = DO if k == 'D' else _tek(rng)
            _put(D, x * (.6 if intro else 1), int((t0 + h * st) * SR))
        for h in range(1, 16, 2):
            if not intro: _put(D, _tek(rng, .28 + .1 * (h % 4 == 3)), int((t0 + h * st) * SR))
        if fill:
            for h in (13, 14, 15): _put(D, _tek(rng, .7), int((t0 + h * st) * SR))
        root = key + (0 if b % 4 < 2 else (-2 if b % 4 == 2 else -4))
        for h, L in ((0, 6), (6, 2), (8, 6), (14, 2)):
            if not intro: _put(B, bass808(mtof(root), int(L * st * SR), 1.4) * .8, int((t0 + h * st) * SR))
        if b % 2 == 1 and not intro:
            for h, deg in phrase:
                f = mtof(key + 24 + deg)
                _put(L1, _ks(f, int(3 * st * SR), rng) * .35, int((t0 + h * st) * SR))
        Lb = int(bar * SR); tt = np.arange(Lb) / SR
        pad = sum(np.sin(2 * np.pi * mtof(key + 12 + d) * tt + .3 * np.sin(2 * np.pi * 5 * tt)) for d in (0, 7)) * .04
        _put(P, _lp(pad, 1500) * np.minimum(1, tt * 2), int(t0 * SR))
    mix = .95 * D + .8 * B + .9 * L1 + .7 * P
    g = np.ones(n)
    for d in drops:
        a, b2 = int((d - .7) * SR), int((d + .05) * SR)
        if 0 < a < n:
            r = np.arange(a, min(n, b2)); x = (r - a) / max(1, b2 - a); g[r] = np.minimum(g[r], np.clip(1 - x * 4, .1, 1))
    g = np.convolve(g, np.ones(int(.05 * SR)) / int(.05 * SR), mode='same')
    return np.tanh(mix * g * 1.1) / np.tanh(1.1)


def variant_for(slug):
    """Posting-order rotation: count Mon/Wed/Fri/Sun posting days since 2026-10-01 up to the slug's date, mod 7.
    Consecutive posts always get consecutive beds and all 7 cycle (a plain date%7 would pin each weekday to one bed)."""
    import datetime
    try:
        d = datetime.date.fromisoformat(slug[:10]); e = datetime.date(2026, 10, 1)
        k = sum(1 for i in range((d - e).days + 1) if (e + datetime.timedelta(i)).weekday() in (0, 2, 4, 6))
        return k % len(VARIANTS)
    except ValueError: return zlib.crc32(slug.encode()) % len(VARIANTS)


def style_for(slug):
    return 'karanlik_hiphop'  # Ata 23 Eki: 'gerilim' YASAK. (eski: Ata 20 Eki: trap/phonk/drive "promotional" -> documentary tension is the default
    names = list(STYLES)
    try: return names[int(slug[8:10]) % len(names)]  # YYYY-MM-DD-...: day of month rotates styles
    except ValueError: return names[zlib.crc32(slug.encode()) % len(names)]


if __name__ == '__main__':
    if len(sys.argv) >= 3 and sys.argv[1] == 'preview':
        st = sys.argv[3] if len(sys.argv) > 3 else 'trap'; sec = float(sys.argv[4]) if len(sys.argv) > 4 else 20
        x = tension(sec, [], int(st.split(':')[1])) if st.startswith('gerilim') else drive(sec, st); x = x / np.max(np.abs(x)) * .9
        wavfile.write(sys.argv[2], SR, (np.stack([x, x], 1) * 32767).astype(np.int16)); print('wrote', sys.argv[2], st)
    else:
        sys.exit(__doc__)
