#!/usr/bin/env python3
"""DENEME REELS VARYASYONLARI (Ata 24 Eki 00:39: "her video farklı varyasyonlarla deneme reels… script aynı, sadece hook ve edit/animasyon tarzı değişir").
Yöntem (kanca değiştirme): eski videonun ilk avatar parçası (kanca+kilit) yerine YENİ kanca + eski kilit cümle(ler)i,
yeni avatar klibiyle ayrı bir 'kanca klibi' olarak render edilir; gövde eski render'dan (hf/renders/v.mp4) kesme noktasından devam eder.
Ses baştan karıştırılır: yeni kanca sesi + eski konuşma (kesmeden sonra), ONAYLI müzik (kit/muzik), eski efekt listesi kaydırılarak.

  python3 engine/variant.py prep  <slug> <v> "<kanca cümlesi>" "<başlık 1. satır>" "<başlık 2. satır (i ile italik)>" <hero|full>
        (önce PD_WORK/<slug>__<v>/hook.wav konmuş olmalı: create_speech speed 1.0 çıktısı)
        → PD_WORK/<slug>__<v>/{speech.wav, words.json, segments.json, seg_00.wav}, videos/<slug>__<v>/{script.txt, spec.py}
  (avatar: seg_00.wav'ı public/audio/<slug>__<v>/ ile push et → create_video_from_avatar → seg_00.mp4 → split.py join → pv.py build/render)
  python3 engine/variant.py final <slug> <v>   → public/<slug>__<v>.mp4
"""
import json, os, re, shutil, subprocess, sys
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PDW = os.environ.get('PD_WORK', os.path.expanduser('~/pd_work'))
ENG = os.path.join(REPO, 'engine')
sys.path.insert(0, ENG)
import split as SP


def dur(p): return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]))


def old_cut(slug):
    """Eski ilk avatar parçasının (kanca+kilit) sonu = gövdenin başladığı yer; ve kanca dışındaki cümlelerin metni/başlangıcı."""
    w = os.path.join(PDW, slug); seg = json.load(open(os.path.join(w, 'segments.json')))['segments'][0]
    S = SP.sentences(SP.words(w)); idx = seg['sentences']
    rest = [S[i] for i in idx[1:]]
    return seg['b'], rest


SPEC = r'''import os
from panel_kit import JS, HERO
W = os.environ['VIDEO_WORK']
SRT = os.path.join(W, 'avatar_cut.srt')
DUR = round(float(open(os.path.join(W, 'dur.txt')).read()) - .02, 2)
REPL = []
EM = set(); RED = set()
CSS_FILE = 'panel.css.html'
SOUND_KIT = 'panel'
EXIT_FADE = False
MODE = '__MODE__'
FULL = [0, 0, 1080, 1920, 0, .5]
AV = {'s1': HERO if MODE == 'hero' else FULL}
def scenes(A): return [('s1', 0, DUR)]
EXTRA_CSS = """<style>.ttl{z-index:5}""" + ("""#root::after{content:'';position:absolute;left:0;right:0;top:0;height:560px;z-index:4;background:linear-gradient(#000d,#0000)}
.ttl{font-size:76px}.ttl i{font-size:82px}""" if MODE == 'full' else '') + """</style>"""
SCENE_HTML = """<section id="s1" class="scene clip"><div class="ttl" id="t1">__L1__<br><span class="l2">__L2__</span></div></section>"""
SCENE_JS = JS + "tl.set('#t1',{opacity:1},0);"
def SFX(A): return []
def RISERS(A): return []
'''


def prep(slug, v, hook, l1, l2, mode):
    w0 = os.path.join(PDW, slug); w = os.path.join(PDW, f'{slug}__{v}'); vd = os.path.join(REPO, 'videos', f'{slug}__{v}')
    os.makedirs(vd, exist_ok=True)
    cut, rest = old_cut(slug)
    hw = os.path.join(w, 'hook.wav'); assert os.path.exists(hw), 'önce hook.wav'
    # kanca: baş sessizliği → 0.06 sn; ardından 0.3 sn; sonra eski kilit cümle(ler)i (kesmeye kadar)
    tmp = os.path.join(w, 'hook_t.wav')
    o = subprocess.run(['ffmpeg', '-i', hw, '-af', 'silencedetect=n=-40dB:d=0.05', '-f', 'null', '-'], capture_output=True, text=True).stderr
    m = re.search(r'silence_start: (-?[\d.]+)\s.*?silence_end: ([\d.]+)', o, re.S)
    lead = max(0.0, float(m.group(2)) - .06) if m and float(m.group(1)) <= .01 else 0.0
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{lead:.3f}', '-i', hw, '-ac', '1', '-ar', '44100', tmp], check=True)
    parts = [tmp]
    if rest:
        a = max(0.0, rest[0][0]['start'] - .06)
        r = os.path.join(w, 'rest.wav')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{a:.3f}', '-to', f'{cut:.3f}', '-i', os.path.join(w0, 'speech.wav'), '-ac', '1', '-ar', '44100', r], check=True)
        sil = os.path.join(w, 'sil.wav')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=mono', '-t', '0.3', sil], check=True)
        parts += [sil, r]
    else:
        tail = os.path.join(w, 'sil.wav')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=mono', '-t', '0.25', tail], check=True); parts.append(tail)
    lst = os.path.join(w, 'parts.txt'); open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, os.path.join(w, 'speech.wav')], check=True)
    text = hook.strip() + (' ' + ' '.join(' '.join(x['word'] for x in s) for s in rest) if rest else '')
    open(os.path.join(vd, 'script.txt'), 'w').write(text + '\n')
    open(os.path.join(vd, 'spec.py'), 'w').write(SPEC.replace('__MODE__', mode).replace('__L1__', l1).replace('__L2__', l2))
    subprocess.run([sys.executable, os.path.join(ENG, 'align.py'), f'{slug}__{v}'], check=True)
    n = len(SP.sentences(SP.words(w)))
    subprocess.run([sys.executable, os.path.join(ENG, 'split.py'), 'cut', f'{slug}__{v}', ','.join(map(str, range(n)))], check=True)
    print(f'prep OK: kanca klibi {dur(os.path.join(w, "speech.wav")):.2f} sn, eski kesme {cut:.3f} sn')


def final(slug, v):
    w0 = os.path.join(PDW, slug); w = os.path.join(PDW, f'{slug}__{v}'); hf0 = os.path.join(w0, 'hf'); hf = os.path.join(w, 'hf')
    cut, _ = old_cut(slug); H = dur(os.path.join(w, 'speech.wav')); delta = H - cut
    out = os.path.join(w, 'final'); os.makedirs(out, exist_ok=True)
    # video: kanca klibi (sessiz render) + eski gövde (kesmeden sonrası)
    a = os.path.join(out, 'a.mp4'); b = os.path.join(out, 'b.mp4')
    enc = ['-c:v', 'libx264', '-crf', '16', '-preset', 'fast', '-pix_fmt', 'yuv420p', '-r', '30', '-an']
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', os.path.join(hf, 'renders', 'v.mp4'), '-t', f'{H:.3f}'] + enc + [a], check=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{cut:.3f}', '-i', os.path.join(hf0, 'renders', 'v.mp4')] + enc + [b], check=True)
    lst = os.path.join(out, 'v.txt'); open(lst, 'w').write(f"file '{a}'\nfile '{b}'\n")
    vid = os.path.join(out, 'v.mp4')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', vid], check=True)
    # ses: yeni kanca + eski konuşma (kesmeden sonra)
    vo = os.path.join(out, 'voice.wav'); b0 = os.path.join(out, 'body_voice.wav')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{cut:.3f}', '-i', os.path.join(w0, 'voice.wav'), '-ac', '2', '-ar', '48000', b0], check=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', os.path.join(w, 'voice.wav'), '-i', b0, '-filter_complex',
                    f'[0]atrim=0:{H:.3f},asetpts=PTS-STARTPTS[x];[x][1]concat=n=2:v=0:a=1', '-ac', '2', '-ar', '48000', vo], check=True)
    E = json.load(open(os.path.join(hf0, 'edl_audio.json')))
    sh = lambda t: round(t + delta, 3)
    E['dur'] = round(dur(vo), 3)
    E['layout'] = [{'t': 0, 's': E['layout'][0]['s']}] + [dict(L, t=sh(L['t'])) for L in E['layout'][1:] if L['t'] > cut]
    E['emph'] = [dict(e, t0=sh(e['t0'])) for e in E.get('emph', []) if e['t0'] > cut]
    E['sfx'] = [[sh(x[0])] + x[1:] for x in E['sfx'] if x[0] > cut]
    E['risers'] = [[sh(x[0])] + x[1:] for x in E['risers'] if x[0] > cut]
    ej = os.path.join(out, 'edl_audio.json'); json.dump(E, open(ej, 'w'))
    mix = os.path.join(out, 'mix.wav')
    subprocess.run([sys.executable, os.path.join(ENG, 'audio3.py'), ej, vo, mix], check=True, cwd=out, env=dict(os.environ, PYTHONPATH=ENG, PD_SLUG=f'{slug}__{v}'))
    fin = os.path.join(w, f'{slug}__{v}.mp4')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', vid, '-i', mix, '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-b:v', '4M', '-maxrate', '5M',
                    '-bufsize', '8M', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-af', 'loudnorm=I=-13:TP=-1.5', '-c:a', 'aac', '-b:a', '192k',
                    '-shortest', '-movflags', '+faststart', fin], check=True)
    shutil.copy(fin, os.path.join(REPO, 'public', f'{slug}__{v}.mp4'))
    print(f'FINAL {fin} {dur(fin):.1f}s (kanca {H:.2f}s, eski kesme {cut:.2f}s, kayma {delta:+.2f}s)')


if __name__ == '__main__':
    c = sys.argv[1]
    if c == 'prep': prep(*sys.argv[2:8])
    elif c == 'final': final(sys.argv[2], sys.argv[3])
    else: sys.exit(__doc__)
