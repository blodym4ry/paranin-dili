#!/usr/bin/env python3
"""HIZLI KURGU / MEME varyasyonu (Ata 4 Kas 00:51): mevcut final videodan otomatik yeniden kurgu.
  python3 tools/hizli.py <kaynak.mp4> <çıktı.mp4> [--seed N]
- Whisper kelime zamanlarıyla konuşma arasındaki sessizlikler kesilir (jump cut).
- Her kesimde çerçeve 1.00 / 1.07 / 1.04 yakınlaştırma arasında değişir, kesim başında kısa 'punch' (zoom zıplaması).
- Anahtar kelimelerde emoji 'pop' (güvenli alan içinde), kesimlerde whoosh, emojide tık.
- Ses hızı DEĞİŞMEZ (kural: konuşma hızı 1.0). Altyazılar videoya gömülü olduğu için senkron korunur.
"""
import json, os, random, re, subprocess, sys, tempfile
import numpy as np

SFX = os.path.join(os.environ.get('PD_WORK', '/home/claude/pd_work'), 'sfx')
EMOJI_FONT = '/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf'
GAP = .12      # bu kadardan kısa boşluklar kesilmez
PAD = .05      # kelime önü/sonu payı
EMO = [  # (kök listesi, emoji)
    (('para', 'lira', 'maaş', 'tl'), '💸'), (('banka',), '🏦'), (('altın',), '🥇'), (('gümüş',), '🥈'), (('dolar', 'avro'), '💵'),
    (('borsa', 'hisse'), '📊'), (('düş', 'kayb', 'kaybet', 'eri'), '📉'), (('art', 'zam', 'yüksel', 'kazandır', 'katlan'), '📈'),
    (('dikkat', 'tuzak', 'risk'), '⚠️'), (('ev', 'kira', 'konut'), '🏠'), (('taksi', 'araç', 'araba', 'otobüs'), '🚕'),
    (('telefon', 'iphone'), '📱'), (('yapay',), '🤖'), (('vergi', 'harç', 'fatura'), '🧾'), (('kart',), '💳'), (('faiz',), '🔥'),
    (('sel',), '🌊'), (('gönder',), '📲'), (('kaydet',), '📌'), (('sipariş', 'yemek', 'restoran'), '🍔'), (('ekmek',), '🍞'),
    (('emekli',), '👴'), (('internet',), '📶'), (('seçim',), '🗳️'), (('bitcoin', 'kripto'), '🪙'), (('enflasyon',), '🎈'),
    (('saat', 'dakika', 'zaman'), '⏱️'), (('devlet',), '🏛️'), (('market',), '🛒'), (('kredi', 'borç'), '🧨'),
]
POS = [(140, 300), (640, 300), (140, 1180), (640, 1180)]   # sol-üst, sağ-üst (sağ 230px boş), sol-alt, sağ-alt — güvenli alan


def sh(c): subprocess.run(c, check=True)
def dur(p): return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]))


def words(src):
    from faster_whisper import WhisperModel
    pcm = subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-ac', '1', '-ar', '16000', '-f', 's16le', '-'], capture_output=True, check=True).stdout
    a = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
    m = WhisperModel(os.environ.get('WHISPER_MODEL', '/root/models/whisper-turbo'), device='cpu', compute_type='int8')
    segs, _ = m.transcribe(a, language='tr', word_timestamps=True, beam_size=1, vad_filter=False)
    return [(w.word.strip(), w.start, w.end) for s in segs for w in s.words if w.word.strip()]


def emoji_seq(ch, d, size=210, n=27):
    """pop animasyonu: 0.9 sn, 30 fps, 260x260 sabit tuval (boyut değişmez → ffmpeg güvenli)."""
    from PIL import Image, ImageDraw, ImageFont
    os.makedirs(d, exist_ok=True)
    f = ImageFont.truetype(EMOJI_FONT, 109)
    im = Image.new('RGBA', (160, 160), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((80, 80), ch, font=f, embedded_color=True, anchor='mm')
    im = im.crop(im.getbbox())
    for i in range(n):
        t = i / 30
        sc = min(1.15, .35 + t * 7) if t < .12 else (1.15 - (t - .12) * 1.5 if t < .22 else 1.0)
        al = 1.0 if t < .7 else max(0, 1 - (t - .7) / .2)
        sz = max(2, int(size * sc))
        e = im.resize((sz, sz), Image.LANCZOS)
        if al < 1: e.putalpha(e.getchannel('A').point(lambda v: int(v * al)))
        c = Image.new('RGBA', (260, 260), (0, 0, 0, 0)); c.paste(e, ((260 - sz) // 2, (260 - sz) // 2), e)
        c.save(os.path.join(d, f'{i:02d}.png'))


FD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'kit', 'fonts', 'ttf')
FONT = os.path.join(FD, 'anton-latin-400-normal.ttf')
STILLER = {
    # cut: sessizlik kes · zoom: kesim zoomları · emoji · flash: kesimde beyaz flaş · rakam: rakam pop · grade: renk/grain
    'meme':   dict(cut=True,  zoom=True,  emoji=True,  flash=False, rakam=False, grade=None),
    'sinema': dict(cut=False, zoom=False, emoji=False, flash=False, rakam=False, grade='eq=saturation=0.78:contrast=1.07:brightness=-0.02,vignette=PI/4.5,noise=alls=7:allf=t'),
    'haber':  dict(cut=True,  zoom=True,  emoji=False, flash=True,  rakam=False, grade='eq=contrast=1.05:saturation=1.08'),
    'rakam':  dict(cut=True,  zoom=True,  emoji=False, flash=False, rakam=True,  grade=None),
}


def _fit(font, txt, maxw, size):
    from PIL import ImageFont
    while True:
        f = ImageFont.truetype(font, size); bb = f.getbbox(txt)
        if bb[2] - bb[0] <= maxw or size < 60: return f, bb
        size -= 6


def _line(txt, font, size, fg, box=None, stroke=0, pad=None, maxw=720):
    from PIL import Image, ImageDraw
    f, bb = _fit(font, txt, maxw, size)
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    pad = pad if pad is not None else (26 if box else 14)
    im = Image.new('RGBA', (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0)); dr = ImageDraw.Draw(im)
    if box: dr.rounded_rectangle([0, 0, im.width - 1, im.height - 1], 14, fill=box)
    dr.text((pad - bb[0], pad - bb[1]), txt, font=f, fill=fg, stroke_width=stroke, stroke_fill=(0, 0, 0, 255))
    return im


def baslik_seq(l1, l2, d, stil='meme', n=69):
    """İLK 4 SANİYE: kare 0'da dev başlık görünür (logo/selam yok), 2.1 sn'de çıkış. Güvenli alan x100–880."""
    from PIL import Image, ImageDraw
    os.makedirs(d, exist_ok=True)
    A, IT, SER = FONT, os.path.join(FD, 'inter-tight-latin-900-normal.ttf'), os.path.join(FD, 'dm-serif-display-latin-400-italic.ttf')
    Y = (255, 225, 77, 255); WH = (255, 255, 255, 255); BK = (13, 12, 10, 255); RED = (216, 30, 30, 255)
    parts = []
    if stil == 'sinema':
        parts.append(_line(l1, SER, 120, WH, stroke=3))
        if l2: parts.append(_line(l2, SER, 150, Y, stroke=3))
    elif stil == 'haber':
        parts.append(_line('DİKKAT', IT, 46, WH, box=RED, pad=14))
        parts.append(_line(l1.upper(), IT, 120, WH, box=RED))
        if l2: parts.append(_line(l2.upper(), IT, 120, BK, box=(244, 241, 234, 255)))
    elif stil == 'rakam':
        parts.append(_line(l1.upper(), IT, 120, BK, box=Y))
        if l2: parts.append(_line(l2.upper(), IT, 140, WH, stroke=8))
    else:
        parts.append(_line(l1.upper(), A, 170, WH, stroke=9))
        if l2: parts.append(_line(l2.upper(), A, 170, BK, box=Y))
    W = max(x.width for x in parts); H = sum(x.height for x in parts) + 10 * (len(parts) - 1)
    blk = Image.new('RGBA', (W, H), (0, 0, 0, 0)); yy = 0
    for x in parts: blk.paste(x, ((W - x.width) // 2, yy), x); yy += x.height + 10
    rng = random.Random(3)
    for i in range(n):
        if stil == 'sinema':
            sc = 1.06 - .06 * min(1, i / 20); al = .85 + .15 * min(1, i / 4)
            if i > n - 9: al = max(0, 1 - (i - (n - 9)) / 8)
            dx = dy = 0
        else:
            if i < 5: sc = 1.35 - .35 * i / 4
            elif i > n - 7: sc = max(.05, 1 - (i - (n - 7)) / 6)
            else: sc = 1.0
            al = 1.0 if i <= n - 7 else max(0, 1 - (i - (n - 7)) / 6)
            dx, dy = (rng.randint(-9, 9), rng.randint(-9, 9)) if i < 9 and stil != 'haber' else (0, 0)
        e = blk.resize((max(2, int(W * sc)), max(2, int(H * sc))), Image.LANCZOS)
        if al < 1: e.putalpha(e.getchannel('A').point(lambda v: int(v * al)))
        c = Image.new('RGBA', (1080, 1920), (0, 0, 0, 0))
        if stil == 'sinema':  # okunurluk için alttan karartma bandı
            g = Image.new('RGBA', (1080, H + 200), (0, 0, 0, int(120 * al))); c.paste(g, (0, 640 - 100), g)
        c.paste(e, (490 - e.width // 2 + dx, 640 + H // 2 - e.height // 2 + dy), e)
        c.save(os.path.join(d, f'{i:02d}.png'))
    return n / 30


def rakam_seq(txt, d, n=24):
    from PIL import Image
    os.makedirs(d, exist_ok=True)
    blk = _line(txt, FONT, 210, (255, 225, 77, 255), stroke=10, maxw=640)
    for i in range(n):
        t = i / 30
        sc = min(1.2, .4 + t * 8) if t < .1 else (1.2 - (t - .1) * 2 if t < .2 else 1.0)
        al = 1.0 if i < n - 5 else max(0, 1 - (i - (n - 5)) / 5)
        e = blk.resize((max(2, int(blk.width * sc)), max(2, int(blk.height * sc))), Image.LANCZOS)
        if al < 1: e.putalpha(e.getchannel('A').point(lambda v: int(v * al)))
        c = Image.new('RGBA', (760, 360), (0, 0, 0, 0)); c.paste(e, ((760 - e.width) // 2, (360 - e.height) // 2), e)
        c.save(os.path.join(d, f'{i:02d}.png'))


def main(src, out, seed=7, baslik=None, stil='meme'):
    random.seed(seed)
    ST = STILLER[stil]
    D = dur(src)
    wc = src + '.words.json'
    if os.path.exists(wc): W = [tuple(x) for x in json.load(open(wc))]
    else: W = words(src); json.dump(W, open(wc, 'w'), ensure_ascii=False)
    tl = lambda s: re.sub(r"[^\wçğıöşüâî]", '', s.replace('I', 'ı').replace('İ', 'i').lower())
    # 1) tutulacak aralıklar
    iv = []
    for _, s, e in W:
        a, b = max(0, s - PAD), min(D, e + PAD)
        if iv and a - iv[-1][1] < GAP: iv[-1][1] = max(iv[-1][1], b)
        else: iv.append([a, b])
    iv[0][0] = 0.0                       # ilk kare (FULLOPEN / kanca) korunur
    iv[-1][1] = D                        # son (CTA kartı) korunur
    # çok kısa parçaları komşuya kat
    m = []
    for a, b in iv:
        if m and b - a < .35: m[-1][1] = b
        else: m.append([a, b])
    iv = [[round(a * 30) / 30, round(b * 30) / 30] for a, b in m]
    if not ST['cut']: iv = [[0.0, round(D * 30) / 30]]
    # 2) yeni zaman çizelgesi + kelime eşlemesi
    newt = []; t = 0
    for a, b in iv: newt.append(t); t += b - a
    total = t
    def remap(x):
        for (a, b), n in zip(iv, newt):
            if a <= x <= b: return n + (x - a)
        return None
    # 3) emojiler
    tmp = tempfile.mkdtemp(prefix='hizli_')
    pops, last, pi = [], -9, 0
    for w, s, e in W:
        k = tl(w); ns = remap(s)
        if ST['rakam']:
            if ns is None or ns - last < 1.8 or ns < 2.6 or ns > total - 1.5 or not re.search(r'\d', w): continue
            txt = re.sub(r"[^\d%.,$€₺+\-]", '', w).strip('.,') or w
            if len(txt) > 9: continue
            p = os.path.join(tmp, f'r{len(pops)}'); rakam_seq(txt, p)
            pops.append((ns, p, (160, 1080))); last = ns; continue
        if not ST['emoji']: continue
        if ns is None or ns - last < 2.6 or ns < (2.6 if baslik else 1.6) or ns > total - 1.5: continue
        ch = None
        if w.endswith('?'): ch = '🤔'
        elif w.endswith('!'): ch = '😱'
        else:
            for roots, c in EMO:
                if any(k.startswith(r) for r in roots) and len(k) >= 2: ch = c; break
        if not ch: continue
        p = os.path.join(tmp, f'e{len(pops)}'); emoji_seq(ch, p)
        pops.append((ns, p, POS[pi % len(POS)])); pi += 1; last = ns
    # 4) parçaları tek tek kodla (aynı girdiyi 50 kez trim etmek RAM'i patlatıyor) → concat
    Z = [1.0, 1.07, 1.04, 1.10]
    segs = []
    def enc(t0, t1, zz, fin, fout, flash=False):
        w = int(1080 * zz) // 2 * 2; h = int(1920 * zz) // 2 * 2
        vx = f'scale={w}:{h},crop=1080:1920,setsar=1,fps=30' + (f',{ST["grade"]}' if ST['grade'] else '') + (',fade=t=in:st=0:d=0.1:color=white' if flash else '')
        o = os.path.join(tmp, f's{len(segs):03d}.mkv'); nf = round((t1 - t0) * 30)
        af = f'afade=t=in:d=0.008' if fin else 'anull'
        af += f',afade=t=out:st={max(0, nf / 30 - .01):.3f}:d=0.01' if fout else ''
        sh(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t0:.4f}', '-i', src, '-t', f'{nf / 30:.4f}',
            '-vf', vx, '-af', f'{af},apad', '-frames:v', str(nf),
            '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '14', '-c:a', 'pcm_s16le', '-ar', '48000', '-ac', '2', '-shortest', o])
        segs.append(o)
    for i, (a, b) in enumerate(iv):
        z = (Z[i % len(Z)] if i else 1.0) if ST['zoom'] else 1.0
        fl = ST['flash'] and i > 0 and iv[i][0] - iv[i - 1][1] > .2
        if i == 0 and baslik and not ST['cut']:   # sinema: tek parça; ilk 4 kare hafif zoom vuruşu
            enc(a, a + 4 / 30, 1.06, False, False); enc(a + 4 / 30, b, 1.0, False, True)
        elif i == 0 and baslik:   # kare 0'dan hareket: 1.14 → 1.05 zoom vuruşu
            enc(a, a + 4 / 30, 1.14, False, False); enc(a + 4 / 30, b, 1.05, False, True)
        elif i and b - a > .5 and ST['zoom']:
            enc(a, a + 4 / 30, z + .04, True, False, fl); enc(a + 4 / 30, b, z, False, True)
        else:
            enc(a, b, z, i > 0, True, fl)
    n = len(iv)
    lst = os.path.join(tmp, 'list.txt'); open(lst, 'w').write(''.join(f"file '{x}'\n" for x in segs))
    cat = os.path.join(tmp, 'cat.mkv')
    sh(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', cat])
    for x in segs: os.remove(x)
    f = ['[0:v]null[vc]', '[0:a]anull[ac]']
    inputs = ['-i', cat]
    cur = 'vc'
    nin = 1
    if baslik:
        l1, _, l2 = baslik.partition('|')
        bd = os.path.join(tmp, 'baslik'); bdur = baslik_seq(l1.strip(), l2.strip(), bd, stil)
        inputs += ['-framerate', '30', '-i', os.path.join(bd, '%02d.png')]
        f.append(f"[{nin}:v]format=rgba,setpts=PTS-STARTPTS[bh]"); f.append(f"[{cur}][bh]overlay=0:0:eof_action=pass[ob]"); cur = 'ob'; nin += 1
    for j, (ts, p, (x, y)) in enumerate(pops):
        inputs += ['-framerate', '30', '-i', os.path.join(p, '%02d.png')]
        k = nin; nin += 1
        f.append(f"[{k}:v]format=rgba,setpts=PTS-STARTPTS+{ts:.3f}/TB[e{k}]")
        ox, oy = (x, y) if ST['rakam'] else (x - 25, y - 25)
        f.append(f"[{cur}][e{k}]overlay=x={ox}:y={oy}:eof_action=pass[o{k}]")
        cur = f'o{k}'
    # sfx
    sx = []
    base = nin; sfx0 = base
    if baslik:
        intro = {'sinema': (('whoosh_hava.mp3', 0, -9), ('boom.mp3', 0, -15)), 'haber': (('boom.mp3', 0, -8), ('klik.mp3', 0.05, -10), ('whoosh_kisa.mp3', 2.05, -13))}
        for fn, at, vol in intro.get(stil, (('boom.mp3', 0, -7), ('whoosh_bas.mp3', 2.05, -12))):
            inputs += ['-i', os.path.join(SFX, fn)]
            sx.append(f"[{base}:a]volume={vol}dB,adelay={int(at * 1000)}|{int(at * 1000)}[s{base}]"); base += 1
    cuts = [newt[i] for i in range(1, n) if iv[i][0] - iv[i - 1][1] > .2]
    wh = [c for k2, c in enumerate(cuts) if k2 % 3 == 0]
    wh = [c for c in wh if not baslik or c > 2.6]
    if ST['flash']: wh = [c for c in cuts if c > 2.6]
    for j, c in enumerate(wh):
        inputs += ['-i', os.path.join(SFX, 'klik.mp3' if ST['flash'] else 'whoosh_kisa.mp3')]
        sx.append(f"[{base}:a]volume=-15dB,adelay={int(max(0, c - .08) * 1000)}|{int(max(0, c - .08) * 1000)}[s{base}]"); base += 1
    for ts, _, _ in pops:
        inputs += ['-i', os.path.join(SFX, 'tik.mp3')]
        sx.append(f"[{base}:a]volume=-13dB,adelay={int(ts * 1000)}|{int(ts * 1000)}[s{base}]"); base += 1
    f += sx
    labs = ''.join(f'[s{i}]' for i in range(sfx0, base))
    f.append(f"[ac]{labs}amix=inputs={1 + base - sfx0}:normalize=0:duration=first,alimiter=limit=0.95[am]")
    br = min(9.0, 620 / total)
    fc = os.path.join(tmp, 'fc.txt'); open(fc, 'w').write(';\n'.join(f))
    sh(['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex_script', fc, '-map', f'[{cur}]', '-map', '[am]',
        '-c:v', 'libx264', '-preset', 'veryfast', '-b:v', f'{br:.2f}M', '-maxrate', f'{br * 1.5:.2f}M', '-bufsize', f'{br * 2:.2f}M',
        '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', '-ar', '48000', '-movflags', '+faststart', '-t', f'{total:.3f}', out])
    meta = {'stil': stil, 'baslik': baslik, 'kaynak': src, 'sure_once': round(D, 2), 'sure_sonra': round(total, 2), 'kesim': n - 1, 'emoji': len(pops), 'whoosh': len(wh)}
    json.dump(meta, open(out + '.json', 'w'), ensure_ascii=False)
    print('HIZLI', json.dumps(meta, ensure_ascii=False))


if __name__ == '__main__':
    a = sys.argv[1:]
    main(a[0], a[1], int(a[a.index('--seed') + 1]) if '--seed' in a else 7, a[a.index('--baslik') + 1] if '--baslik' in a else None, a[a.index('--stil') + 1] if '--stil' in a else 'meme')
