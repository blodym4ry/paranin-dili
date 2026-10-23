"""Eski ses zamanlamasıyla yazılmış spec'i yeni sese taşır (aynı metin, farklı TTS/duraklama).
RT = remap(old_words.json, new_words.json): kelime sırası aynı → eski zamandan yeni zamana parça parça doğrusal eşleme.
retime_js(js, RT): JS içindeki zaman argümanlarını (seçici dizesinden ya da {..} nesnesinden hemen sonraki ilk sayı) çevirir;
süreler (zamandan sonraki sayılar) olduğu gibi kalır."""
import json, re
import numpy as np


def _starts(p):
    W = [x for x in json.load(open(p)) if not x['word'].startswith('<')]
    return [x['start'] for x in W], [x['end'] for x in W]


def remap(old_p, new_p):
    os_, oe = _starts(old_p); ns, ne = _starts(new_p)
    assert len(os_) == len(ns), f'kelime sayısı farklı: {len(os_)} vs {len(ns)}'
    xo = np.array([0.0] + [v for pair in zip(os_, oe) for v in pair]); xn = np.array([0.0] + [v for pair in zip(ns, ne) for v in pair])
    o = np.maximum.accumulate(xo); n = np.maximum.accumulate(xn)
    tail = n[-1] - o[-1]
    def RT(t):
        if t >= o[-1]: return round(float(t + tail), 3)
        return round(float(np.interp(t, o, n)), 3)
    return RT


def retime_js(js, RT):
    js = re.sub(r"""(['"`]\s*,\s*)(\d+(?:\.\d+)?)(?=\s*[,)])""", lambda m: m.group(1) + str(RT(float(m.group(2)))), js)
    js = re.sub(r"""(\}\s*,\s*)(\d+(?:\.\d+)?)(?=\s*[)+])""", lambda m: m.group(1) + str(RT(float(m.group(2)))), js)
    return js


def scene_bounds(SC, segs, DUR):
    """Avatarlı sahneleri (id kümesi) avatar parçalarının sınırlarına oturt; komşu sahneleri buna göre kaydır.
    SC: [(id, a, b, av_bool)], segs: segments.json listesi. Avatarlı sahne, başlangıcına en yakın parçanın [a,b] aralığına çekilir."""
    out = [list(x) for x in SC]
    for k, (sid, a, b, av) in enumerate(out):
        if not av: continue
        s = min(segs, key=lambda g: abs(g['a'] - a))
        na, nb = (0.0 if k == 0 else s['a'] + .06), min(DUR, s['b'] - .06)
        # aynı parçayı paylaşan ardışık avatar sahneleri: yalnız ilkinin başı ve sonuncunun sonu parçaya oturur
        if k > 0 and out[k - 1][3] and min(segs, key=lambda g: abs(g['a'] - out[k - 1][1])) is s: na = out[k - 1][2]
        nxt_same = k + 1 < len(out) and out[k + 1][3] and min(segs, key=lambda g: abs(g['a'] - out[k + 1][1])) is s
        out[k][1] = round(na, 3)
        if not nxt_same: out[k][2] = round(nb, 3)
        if k > 0: out[k - 1][2] = out[k][1]
        if k + 1 < len(out) and not nxt_same: out[k + 1][1] = out[k][2]
    out[-1][2] = DUR
    return [(sid, a, b) for sid, a, b, _ in out]
