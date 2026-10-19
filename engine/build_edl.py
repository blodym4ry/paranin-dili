"""Build the edit decision list (EDL) from HeyGen's SRT + avatar duration.
usage: python3 build_edl.py subs.srt DURATION out.json
"""
import json, re, sys

FPS = 30
BPM = 100
BEAT = 60 / BPM

def tl(s):  # Turkish-aware lowercase
    return s.replace('I', 'ı').replace('İ', 'i').lower()

def parse_srt(path):
    txt = open(path, encoding='utf-8-sig').read().replace('\r', '')
    segs = []
    for block in re.split(r'\n\s*\n', txt.strip()):
        lines = block.strip().split('\n')
        if len(lines) < 2:
            continue
        m = re.search(r'(\d+):(\d+):(\d+)[,.](\d+)\s*-->\s*(\d+):(\d+):(\d+)[,.](\d+)', lines[1] if '-->' in lines[1] else lines[0])
        if not m:
            continue
        g = list(map(int, m.groups()))
        t0 = g[0] * 3600 + g[1] * 60 + g[2] + g[3] / 1000
        t1 = g[4] * 3600 + g[5] * 60 + g[6] + g[7] / 1000
        text = ' '.join(l for l in lines if '-->' not in l and not l.strip().isdigit())
        segs.append((t0, t1, text.strip()))
    return segs

def words_from_segs(segs):
    out = []
    for t0, t1, text in segs:
        ws = text.split()
        if not ws:
            continue
        weights = [len(w) + 2 for w in ws]
        tot = sum(weights)
        t = t0
        for w, wt in zip(ws, weights):
            d = (t1 - t0) * wt / tot
            out.append({'w': w, 't0': t, 't1': t + d})
            t += d
    return out

def norm(w):
    return re.sub(r"[^\wçğıöşüâî'%$]", '', tl(w))

REPL = [
    (['sıfır', 'virgül', 'seksen', 'bir'], '0,81'),
    (['yüzde', '5'], '%5'), (['yüzde', '2'], '%2'),
    (['50', 'bin', 'dolarlık'], "$50.000'lık"), (['50', 'bin', 'dolar'], '$50.000'),
    (['250', 'bin', 'dolar'], '$250.000'),
]

def merge(words):
    out, i = [], 0
    while i < len(words):
        hit = None
        for seq, rep in REPL:
            n = len(seq)
            if [norm(w['w']) for w in words[i:i + n]] == seq:
                hit = (n, rep)
                break
        if hit:
            n, rep = hit
            tail = re.findall(r'[.,?!]+$', words[i + n - 1]['w'])
            out.append({'w': rep + (tail[0] if tail else ''), 't0': words[i]['t0'], 't1': words[i + n - 1]['t1']})
            i += n
        else:
            out.append(dict(words[i]))
            i += 1
    return out

def find(words, phrase, after=0.0):
    seq = [norm(p) for p in phrase.split()]
    for i in range(len(words)):
        if words[i]['t0'] < after:
            continue
        if [norm(w['w']) for w in words[i:i + len(seq)]] == seq or norm(words[i]['w']) == norm(phrase):
            return words[i]['t0']
    raise SystemExit(f'anchor not found: {phrase}')

def snap(t):
    b = round(t / BEAT) * BEAT
    return b if -0.25 <= b - t <= 0.12 else t

HL = {'tesla', 'roadster', '0,81', '%5', '%2', "2017'de", "2020'de", '2028', '$50.000', "$50.000'lık", '$250.000',
      'depozito', 'depozitolar', 'faizsiz', 'kredi', 'satış', 'yorumlara', 'düştü', 'yükseldi', 'düşüş'}

def main(srt, dur, outp):
    dur = float(dur)
    words = merge(words_from_segs(parse_srt(srt)))
    A = lambda p, after=0.0: find(words, p, after)

    a = {k: A(v) for k, v in {
        'ticker': 'Ertesi gün', 'orb': 'Peki neden', 'bakin': 'Bakın,', 'speed': 'Sıfırdan',
        'chart': 'Ertesi sabah', 'rumor': 'Borsada buna', 'cycle': 'Fiyat, haberi', 'story': 'Ama asıl',
        'years': 'Bu araba ilk', 'coins': 'Bu sürede', 'thrust': 'Şimdi bir model', 'nocar': 'Müşteri parayı',
        'credit': 'Şirket için', 'compare': 'Yani gösteriyi', 'cta': 'Sen olsan', 'sig': 'Paranın dilini'}.items()}
    s = {k: snap(v) for k, v in a.items()}

    layout = [
        {'t': 0, 's': 'A'},
        {'t': s['bakin'] - 0.2, 's': 'B'},
        {'t': s['rumor'] - 0.2, 's': 'E'}, {'t': s['cycle'] - 0.25, 's': 'B'},
        {'t': s['story'] - 0.2, 's': 'E'}, {'t': s['years'] - 0.25, 's': 'B'},
        {'t': s['credit'] - 0.2, 's': 'E'}, {'t': s['compare'] - 0.25, 's': 'B'},
        {'t': s['cta'] - 0.3, 's': 'A'},
    ]
    sc = lambda i, a_, b_, title: {'id': i, 'start': round(a_, 3), 'end': round(b_, 3), 'title': title}
    scenes = [
        sc('car', 0, s['ticker'], 'roadster.demo'),
        sc('ticker', s['ticker'], s['orb'], 'tsla.nasdaq'),
        sc('orb', s['orb'], s['bakin'] + 0.3, 'analiz'),
        sc('reveal', s['bakin'], s['speed'], 'roadster.demo'),
        sc('speed', s['speed'], s['chart'], 'roadster.demo'),
        sc('chart', s['chart'], s['rumor'] + 0.3, 'tsla.16ekim'),
        sc('cycle', s['cycle'], s['story'] + 0.3, 'borsa.döngü'),
        sc('years', s['years'], s['coins'], 'takvim'),
        sc('coins', s['coins'], s['thrust'], 'depozito'),
        sc('thrust', s['thrust'], s['nocar'], 'depozito'),
        sc('nocar', s['nocar'], s['credit'] + 0.3, 'teslimat'),
        sc('compare', s['compare'], s['cta'], 'karar'),
        sc('cta', s['cta'], s['sig'], 'yorum'),
        sc('sig', s['sig'], dur + 1, 'paranın dili'),
    ]
    emph = [
        {'t0': s['rumor'], 't1': s['cycle'] - 0.1, 'l1': 'Söylentiyi al', 'l2': 'haberi sat'},
        {'t0': s['story'], 't1': s['years'] - 0.1, 'l1': 'Asıl hikâye', 'l2': 'başka'},
        {'t0': s['credit'], 't1': s['compare'] - 0.1, 'l1': 'Faizsiz', 'l2': 'kredi'},
    ]

    # caption chunks (skip words inside emphasis windows)
    def in_emph(t):
        return any(e['t0'] - 0.05 <= t < e['t1'] for e in emph)
    chunks, cur = [], []
    def flush():
        if cur:
            chunks.append(list(cur)); cur.clear()
    for w in words:
        if in_emph(w['t0']):
            flush(); continue
        cur.append(w)
        txt = ' '.join(x['w'] for x in cur)
        if len(cur) >= 3 or len(txt) >= 15 or re.search(r'[.?!,]$', w['w']):
            flush()
    flush()
    caps = []
    for i, ch in enumerate(chunks):
        t0 = ch[0]['t0']
        nxt = chunks[i + 1][0]['t0'] if i + 1 < len(chunks) else dur
        t1 = min(nxt, ch[-1]['t1'] + 0.45)
        if t1 - t0 < 0.35:
            t1 = min(nxt, t0 + 0.35)
        disp = [re.sub(r'[.,]+$', '', x['w']) for x in ch]
        hl = [j for j, x in enumerate(disp) if tl(x).strip('?!') in HL]
        caps.append({'t0': round(t0, 3), 't1': round(t1, 3), 'words': disp, 'hl': hl})

    edl = {'fps': FPS, 'bpm': BPM, 'dur': dur, 'layout': layout, 'scenes': scenes, 'caps': caps, 'emph': emph,
           'anchors': s, 'avFrames': int(dur * FPS)}
    json.dump(edl, open(outp, 'w'), ensure_ascii=False, indent=1)
    print(f'{len(caps)} captions, {len(scenes)} scenes; anchors:', {k: round(v, 2) for k, v in s.items()})

if __name__ == '__main__':
    main(*sys.argv[1:4])
