"""Generic sound design from EDL 'sfx' + 'risers' cue lists (synth library from audio2).
usage: python3 audio3.py edl.json voice.wav out.wav"""
import json, sys, os
import music as M
import numpy as np
from scipy.io import wavfile
from audio2 import (SR, db, whoosh, pop, ui_click, scifi_click, marker, impact, stamp, gears, paper_drop, success,
                    sharp_bass_riser, metallic_riser, hit, music, Track, av_opacity)
SND = {'whoosh_deep': lambda: whoosh(.9, kind='deep'), 'whoosh_hollow': lambda: whoosh(.7, kind='hollow'), 'whoosh_wind': lambda: whoosh(.6, kind='wind'),
       'pop': lambda: pop(640), 'ui_click': ui_click, 'scifi_click': scifi_click, 'marker': lambda: marker(.5), 'impact': impact, 'stamp': stamp,
       'gears': lambda: gears(10, 1.0), 'paper_drop': paper_drop, 'success': success}

from scipy.ndimage import minimum_filter1d
from audio2 import lp, hp


def soften(x):
    """Ear-comfort EQ for music/SFX: no sub rumble, ~-4 dB shelf above 6 kHz (no harsh clicks/sizzle on phones/earbuds)."""
    x = hp(x, 35)
    return .62 * x + .38 * lp(x, 6000)


def cap_loudness(x, cap, win=.05):
    """Program-dependent limiter: short-term RMS of x never exceeds cap. Returns (y, max gain reduction dB)."""
    k = max(1, int(win * SR)); rms = np.sqrt(np.convolve(x ** 2, np.ones(k) / k, mode='same')) + 1e-9
    g = np.minimum(1, cap / rms); g = minimum_filter1d(g, k)                     # attack: look-ahead over window
    g = np.convolve(g, np.ones(int(.08 * SR)) / int(.08 * SR), mode='same')     # smooth release
    return x * g, float(-20 * np.log10(max(1e-6, g.min())))


def report(voice, fx, mus, vr):
    k = int(.4 * SR)
    def mom(x): return 20 * np.log10(np.sqrt(np.convolve(x ** 2, np.ones(k) / k, mode='same')).max() + 1e-9)
    ref = 20 * np.log10(vr)
    mm = 20 * np.log10(np.sqrt(np.mean(mus[np.abs(mus) > 1e-5] ** 2)) + 1e-9)
    return f"voice 0 dB | music avg {mm - ref:+.1f} dB | music max {mom(mus) - ref:+.1f} | fx max {mom(fx) - ref:+.1f}"

FOLEY = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'kit', 'foley')
_fl, _fn = None, {}
def foley(name):
    """Masa üstü kiti: gerçek kayıt one-shot (kit/foley/lib.json). Aynı türden çağrılar dosyalar arasında dönüşümlü."""
    global _fl
    if _fl is None: _fl = json.load(open(os.path.join(FOLEY, 'lib.json')))
    files = _fl[name]; i = _fn.get(name, 0); _fn[name] = i + 1
    sr, x = wavfile.read(os.path.join(FOLEY, 'oneshot', files[i % len(files)] + '.wav'))
    x = x.astype(float); x = x.mean(1) if x.ndim == 2 else x
    if sr != SR: x = np.interp(np.arange(int(len(x) * SR / sr)) * sr / SR, np.arange(len(x)), x)
    return x / (np.max(np.abs(x)) + 1e-9), .02
def snd(s): return foley(s[2:]) if s.startswith('f:') else SND[s]()

BUS = {'whoosh': -9, 'simple': -9, 'accent': -2, 'riser': -4, 'hit': -3}
def main(edl_p, voice_p, out_p):
    edl = json.load(open(edl_p))
    sr, v = wavfile.read(voice_p); v = v.astype(float) / 32768; v = v.mean(1) if v.ndim == 2 else v
    dur = len(v) / SR + .5; n = int(dur * SR)
    voice = np.zeros(n); voice[:len(v)] = v; voice = voice / np.max(np.abs(voice)) * db(-1)
    W, X, XA, R, H = Track(n), Track(n), Track(n), Track(n), Track(n)
    cues = []
    masa = edl.get('sound_kit') == 'masa'      # masa üstü: sentetik whoosh yok, sadece sahnede olan nesnenin gerçek sesi
    if not masa:
        for L in edl['layout'][1:]: W.place(whoosh(.9, kind='deep'), L['t'] + .425, -10); cues.append((L['t'] + .425, 'WHOOSH', 'layout', -10))
        for e in edl['emph']: W.place(whoosh(.6, kind='wind'), e['t0'] + .5, -16)
    for t, s, lvl, acc, why in edl['sfx']:
        (XA if acc else X).place(snd(s), t, lvl); cues.append((t, 'ACCENT' if acc else 'SFX', why, lvl))
    for t, kind, lvl in ([] if masa else edl['risers']):
        R.place_end(sharp_bass_riser(1.8) if kind == 'sharp' else metallic_riser(1.5), t, lvl); H.place(hit(), t, lvl - 4); cues.append((t, 'RISER', kind, lvl))
    # ---- music bed: 'gerilim' family, variant rotates by date (Ata 20 Eki: vary it, suit all ages, ear-friendly)
    slug = os.environ.get('PD_SLUG', os.path.basename(os.path.dirname(os.path.abspath(out_p))))
    style = os.environ.get('MUSIC_STYLE') or M.style_for(slug)
    var = int(os.environ.get('MUSIC_VARIANT', M.variant_for(slug)))
    drops = [r[0] for r in edl['risers']]
    mus = (M.tension(dur, drops, var) if style == 'gerilim' else M.dark_hiphop(dur, drops) if style == 'karanlik_hiphop' else M.oriental(dur, drops) if style == 'modern_oryantal' else M.drive(dur, style))[:n]
    env = np.convolve(np.abs(voice), np.ones(int(.05 * SR)) / int(.05 * SR), mode='same'); venv = env / env.max()
    vr = np.sqrt(np.mean(voice[np.abs(voice) > .01] ** 2)); mr = np.sqrt(np.mean(mus[np.abs(mus) > 1e-4] ** 2))
    duck = np.convolve(np.clip(venv * 3, 0, 1), np.ones(int(.15 * SR)) / int(.15 * SR), mode='same')
    mus = soften(mus) / mr * vr * db(float(os.environ.get('MUSIC_DB', -17))) * (1 - .4 * duck)
    mus *= np.clip(np.arange(n) / SR / .3, 0, 1) * np.clip((dur - np.arange(n) / SR) / 1.0, 0, 1)
    # ---- animation SFX: duck under speech, soften highs, then hard-cap loudness so no hit stabs the ear
    simple = W.buf * db(BUS['whoosh']) + X.buf * db(BUS['simple'])
    accent = XA.buf * db(BUS['accent']) + R.buf * db(BUS['riser']) + H.buf * db(BUS['hit'])
    fx = soften(simple * (1 - .75 * np.clip(venv * 4, 0, 1)) + accent * (1 - .45 * np.clip(venv * 3, 0, 1)))
    fx, fx_red = cap_loudness(fx, vr * db(-6), win=.05)     # 50 ms RMS never above speech RMS -6 dB
    fx = fx * np.minimum(1, np.max(np.abs(voice)) * db(-4) / max(1e-9, np.max(np.abs(fx))))  # peaks 4 dB under voice peak
    mix = voice + fx + mus
    mix = np.tanh(mix / .95) * .95 if np.max(np.abs(mix)) > .95 else mix
    rep = report(voice, fx, mus, vr)
    print(f"music {style}:{M.VARIANTS[var]['name'] if style == 'gerilim' else ''} | " + rep + f" | fx limiter max {fx_red:.1f} dB")
    os.makedirs('stems', exist_ok=True)
    with open('stems/cue_sheet.txt', 'w') as f:
        for c in sorted(cues): f.write(f'{c[0]:7.2f}s  {c[1]:7s} {c[2]:<26s} {c[3]:>4} dB\n')
    wavfile.write(out_p, SR, (np.stack([mix, mix], 1) * 32767).astype(np.int16))
    print('cues', len(cues), 'dur', round(dur, 2))
if __name__ == '__main__': main(*sys.argv[1:4])
