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
BUS = {'whoosh': -9, 'simple': -9, 'accent': -2, 'riser': -4, 'hit': -3}
def main(edl_p, voice_p, out_p):
    edl = json.load(open(edl_p))
    sr, v = wavfile.read(voice_p); v = v.astype(float) / 32768; v = v.mean(1) if v.ndim == 2 else v
    dur = len(v) / SR + .5; n = int(dur * SR)
    voice = np.zeros(n); voice[:len(v)] = v; voice = voice / np.max(np.abs(voice)) * db(-1)
    W, X, XA, R, H = Track(n), Track(n), Track(n), Track(n), Track(n)
    cues = []
    for L in edl['layout'][1:]: W.place(whoosh(.9, kind='deep'), L['t'] + .425, -10); cues.append((L['t'] + .425, 'WHOOSH', 'layout', -10))
    for e in edl['emph']: W.place(whoosh(.6, kind='wind'), e['t0'] + .5, -16)
    for t, s, lvl, acc, why in edl['sfx']:
        (XA if acc else X).place(SND[s](), t, lvl); cues.append((t, 'ACCENT' if acc else 'SFX', why, lvl))
    for t, kind, lvl in edl['risers']:
        R.place_end(sharp_bass_riser(1.8) if kind == 'sharp' else metallic_riser(1.5), t, lvl); H.place(hit(), t, lvl - 4); cues.append((t, 'RISER', kind, lvl))
    # energetic beat (Ata 20 Eki: eski pad uyutuyordu). Style rotates per video; MUSIC_STYLE env overrides.
    slug = os.environ.get('PD_SLUG', os.path.basename(os.path.dirname(os.path.abspath(out_p))))
    style = os.environ.get('MUSIC_STYLE') or M.style_for(slug)
    mus = M.drive(dur, style)[:n]
    env = np.convolve(np.abs(voice), np.ones(int(.05 * SR)) / int(.05 * SR), mode='same'); venv = env / env.max()
    vr = np.sqrt(np.mean(voice[np.abs(voice) > .01] ** 2)); mr = np.sqrt(np.mean(mus ** 2))
    duck = np.convolve(np.clip(venv * 3, 0, 1), np.ones(int(.15 * SR)) / int(.15 * SR), mode='same')
    mus = mus / mr * vr * db(float(os.environ.get('MUSIC_DB', -15))) * (1 - .4 * duck)
    mus *= np.clip(np.arange(n) / SR / .3, 0, 1) * np.clip((dur - np.arange(n) / SR) / 1.0, 0, 1)
    print('music', style)
    simple = W.buf * db(BUS['whoosh']) + X.buf * db(BUS['simple'])
    accent = XA.buf * db(BUS['accent']) + R.buf * db(BUS['riser']) + H.buf * db(BUS['hit'])
    mix = voice + simple * (1 - .75 * np.clip(venv * 4, 0, 1)) + accent * (1 - .45 * np.clip(venv * 3, 0, 1)) + mus
    peak = np.max(np.abs(mix)); mix *= min(1, .98 / peak)
    os.makedirs('stems', exist_ok=True)
    with open('stems/cue_sheet.txt', 'w') as f:
        for c in sorted(cues): f.write(f'{c[0]:7.2f}s  {c[1]:7s} {c[2]:<26s} {c[3]:>4} dB\n')
    wavfile.write(out_p, SR, (np.stack([mix, mix], 1) * 32767).astype(np.int16))
    print('cues', len(cues), 'dur', round(dur, 2))
if __name__ == '__main__': main(*sys.argv[1:4])
