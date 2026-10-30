#!/usr/bin/env python3
"""DENEME VARYASYONU v2 (Ata 30 Eki 19:50): ana Reel + 2 deneme; script aynı, KANCA + animasyon + video tarzı farklı.
Ata seçimi: kanca AVATARSIZ (yeni TTS sesi + gerçek görsel + dev yazı), avatar 2. cümlede girer → HeyGen kredisi harcanmaz.

  python3 engine/variant2.py make <slug> <v> <k> "<kanca metni (TTS ile aynı)>" "<başlık 1>" "<başlık 2, <i>..</i> olabilir>" <kinetik|manset> ["kelime=>EKRAN;..."]
      önkoşul: PD_WORK/<slug>__<v>/hook.wav (create_speech speed 1.0, baş/son sessizlik kırpılmış)
      k = orijinalden atılan baştaki cümle sayısı (genelde 1)
      → PD_WORK/<slug>__<v>/{speech.wav, voice.wav, words.json, segments.json, avatar_cut.mov, avatar_cut.srt, dur.txt}
      → videos/<slug>__<v>/{script.txt, spec.py, media -> ../<slug>/media}
  sonra: pv.py build/check/render <slug>__<v>

Stiller:
  kinetik : kanca tam ekran gerçek fotoğraf (bulanıksız) + dev yazı; altyazı ÇOK KELİMELİ satır (karaoke); mavi vurgu bandı.
  manset  : kanca beyaz manşet kartı (siyah yazı, kırmızı şerit); altyazı tek kelime; HERO yalnız CTA'da → gövde neredeyse hep yuvarlak (PIP).
"""
import json, os, re, subprocess, sys
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PDW = os.environ.get('PD_WORK', os.path.expanduser('~/pd_work'))
sys.path.insert(0, os.path.join(REPO, 'engine'))
import split as SP

GAP = .35   # kanca ile gövde arası sessizlik
LEAD = .06


def sh(c, **k): subprocess.run(c, check=True, **k)
def dur(p): return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]))


STYLE_CSS = {
    'kinetik': r"""
.ttl .l2{background:linear-gradient(90deg,#0b3a8f,#1d5fe0)!important}
.cl{font:italic 400 84px/1.1 'DM Serif Display'!important;letter-spacing:0!important}
.cw{color:#ffe14d!important}
.cw.k1{background:linear-gradient(90deg,#0b3a8f,#1d5fe0)!important;color:#fff!important}
#t1{top:560px!important;left:100px!important;right:100px!important;font-size:84px!important;line-height:1.04}
#t1 i{font-size:90px!important}
#t1 .l2{margin-top:14px}
""",
    'manset': r"""
.ttl .l2{background:#f4f1ea!important;color:#0d0c0a!important;border-left:14px solid #d81e1e}
.ttl .l2 i{color:#b01212}
#t1{top:520px!important;left:110px!important;right:110px!important;padding:34px 30px 40px;background:rgba(244,241,234,.97);color:#0d0c0a!important;
  border-top:16px solid #d81e1e;border-radius:6px;box-shadow:0 30px 70px rgba(0,0,0,.7);text-shadow:none!important;font-size:74px!important}
#t1 .l2{background:#d81e1e!important;color:#fff!important;border-left:0}
""",
}


def make(slug, v, k, hook, l1, l2, style, repl=''):
    k = int(k)
    w0 = os.path.join(PDW, slug); w = os.path.join(PDW, f'{slug}__{v}')
    vd0 = os.path.join(REPO, 'videos', slug); vd = os.path.join(REPO, 'videos', f'{slug}__{v}')
    os.makedirs(vd, exist_ok=True)
    S = SP.sentences(SP.words(w0))
    c = round(S[k][0]['start'] - .12, 3)          # gövde başlangıcı (cümle arası sessizlikte)
    hk = os.path.join(w, 'hook.wav'); hd = dur(hk)
    off = round(LEAD + hd + GAP, 3)                # yeni dosyada gövdenin başladığı an
    # 1) ses
    sh(['ffmpeg', '-v', 'error', '-y', '-i', hk, '-i', os.path.join(w0, 'voice.wav'), '-filter_complex',
        f'[0:a]aresample=48000,aformat=channel_layouts=stereo,adelay={int(LEAD*1000)}|{int(LEAD*1000)},apad=whole_dur={LEAD+hd+GAP}[h];'
        f'[1:a]atrim=start={c},asetpts=PTS-STARTPTS[b];[h][b]concat=n=2:v=0:a=1[o]', '-map', '[o]', '-ar', '48000', '-ac', '2',
        os.path.join(w, 'speech.wav')])
    sh(['cp', os.path.join(w, 'speech.wav'), os.path.join(w, 'voice.wav')])
    total = dur(os.path.join(w, 'speech.wav'))
    # 2) script + hizalama
    rest = [' '.join(x['word'] for x in s) for s in S[k:]]
    open(os.path.join(vd, 'script.txt'), 'w').write(hook.strip() + '\n' + '\n'.join(rest) + '\n')
    sh([sys.executable, os.path.join(REPO, 'engine', 'align.py'), f'{slug}__{v}'], env={**os.environ, 'PD_WORK': PDW, 'WHISPER_MODEL': os.environ.get('WHISPER_MODEL', '/root/models/whisper-turbo')})
    # 3) avatar: kanca süresince siyah (sahnede gizli), sonra orijinal avatar c'den
    av0 = os.path.join(w0, 'avatar_cut.mov')
    sh(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', f'color=c=black:s=1080x1920:r=30:d={off}', '-i', av0, '-filter_complex',
        f'[1:v]trim=start={c},setpts=PTS-STARTPTS,fps=30,format=yuv420p[b];[0:v]format=yuv420p[a];[a][b]concat=n=2:v=1:a=0[o]',
        '-map', '[o]', '-c:v', 'libx264', '-crf', '14', '-preset', 'fast', '-t', f'{total:.3f}', os.path.join(w, 'avatar_cut.mov')])
    # 4) segments / srt / dur
    json.dump({'total': total, 'segments': [{'i': 0, 'a': round(off - .1, 3), 'b': round(total, 3), 'sentences': list(range(1, 999)), 'text': 'govde'}]},
              open(os.path.join(w, 'segments.json'), 'w'), ensure_ascii=False, indent=1)
    W2 = SP.words(w); S2 = SP.sentences(W2); cues, cur = [], []
    for s in S2:
        for x in s:
            cur.append(x)
            if len(cur) >= 4 or x is s[-1]: cues.append(cur); cur = []
    srt = '\n'.join(f"{n + 1}\n{SP.fmt(q[0]['start'])} --> {SP.fmt(q[-1]['end'])}\n{' '.join(x['word'] for x in q)}\n" for n, q in enumerate(cues))
    open(os.path.join(w, 'avatar_cut.srt'), 'w').write(srt); open(os.path.join(w, 'avatar.srt'), 'w').write(srt)
    open(os.path.join(w, 'dur.txt'), 'w').write(f'{total:.3f}')
    # 5) spec
    src = open(os.path.join(vd0, 'spec.py')).read()
    src = re.sub(r"FULLOPEN = [\d.]+", "FULLOPEN = 0", src)
    src = re.sub(r"title\('t1', '(?:[^'\\]|\\.)*', '(?:[^'\\]|\\.)*'\)", lambda m: f"title('t1', {l1!r}, {l2!r})", src, count=1)
    hm = re.search(r"HEROS = \[([^\]]*)\]", src)
    heros = [h.strip().strip("'") for h in hm.group(1).split(',') if h.strip()]
    heros = [h for h in heros if h != 's1']
    if style == 'manset': heros = heros[-1:]   # sadece CTA kartı; gövde PIP
    src = src.replace(hm.group(0), 'HEROS = ' + repr(heros))
    src = re.sub(r"(AV = \{k: \(HERO if k in HEROS else PIP\) for k in IDS\})", r"\1\nAV['s1'] = None   # VARYASYON: kanca avatarsız (Ata 30 Eki)", src)
    src = src.replace("tl.set('#t1',{opacity:1},0);", "tl.fromTo('#t1',{opacity:0,scale:1.25},{opacity:1,scale:1,duration:.35,ease:'back.out(1.7)'},0);")
    extra = [tuple(p.split('=>')) for p in repl.split(';') if '=>' in p]
    if extra:
        src = re.sub(r"(REPL = \[)", "REPL = [" + ', '.join(f"(N({a!r}), {b!r})" for a, b in extra) + "] + [", src, count=1)
    if style == 'kinetik':   # kanca arka planı net (bulanıksız)
        src = re.sub(r"\('bg1', '([^']+)', 1\)", r"('bg1', '\1', 0)", src)
    src = src.replace("EXTRA_CSS = '<style>' +", "EXTRA_CSS = '<style>' + " + repr(STYLE_CSS[style]) + " +", 1)
    open(os.path.join(vd, 'spec.py'), 'w').write(f"# VARYASYON {v} ({style}) — kaynak: videos/{slug}/spec.py; kanca: {hook}\n" + src)
    ml = os.path.join(vd, 'media')
    if not os.path.exists(ml): os.symlink(os.path.join('..', slug, 'media'), ml)
    print(f'VARIANT {slug}__{v}: kanca {hd:.2f}s, gövde orijinal {c:.2f}s → {off:.2f}s (kayma {off - c:+.2f}s), toplam {total:.1f}s')


if __name__ == '__main__':
    if sys.argv[1] == 'make': make(*sys.argv[2:])
