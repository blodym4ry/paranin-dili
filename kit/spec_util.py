"""Spec yardımcıları (24 Eki): kelime zamanı T(), avatar parçaları, ALTIN ÇERÇEVELİ kart (Ata 24 Eki 01:55).
Kullanım (spec.py):  from spec_util import load; U = load(); T = U.T; SEGS = U.SEGS
  U.frame_js(on_ranges)  → altın çerçeveyi #avbox'ın üstüne ekler ve verilen [(a,b),..] aralıklarında gösterir.
  Avatar sahnesi sınırı: parça başlangıcı + .06 (pv.py AVATAR GUARD)."""
import os, json, re

from panel_kit import HERO as _H
FRAME_CSS = f'''.gf{{position:absolute;left:{_H[0]-8}px;top:{_H[1]-8}px;width:{_H[2]+16}px;height:{_H[3]+16}px;border-radius:46px;border:5px solid #e8b931;opacity:0;
  box-shadow:0 0 26px rgba(232,185,49,.45),inset 0 0 18px rgba(232,185,49,.25);pointer-events:none;z-index:6}}
.gold{{color:#e8b931}}'''


class load:
    def __init__(self):
        self.W = os.environ['VIDEO_WORK']
        self.DUR = round(float(open(os.path.join(self.W, 'dur.txt')).read()) - .05, 2)
        self.WS = [x for x in json.load(open(os.path.join(self.W, 'words.json'))) if not x['word'].startswith('<')]
        self.SEGS = json.load(open(os.path.join(self.W, 'segments.json')))['segments']

    @staticmethod
    def _cl(s):
        return re.sub(r"[^\wçğıöşüâî'-]", '', s.replace('I', 'ı').replace('İ', 'i').lower())

    def T(self, w, after=0.0):
        for x in self.WS:
            if x['start'] >= after - .01 and self._cl(x['word']).startswith(self._cl(w)):
                return round(x['start'], 2)
        raise SystemExit(f'kelime yok: {w} @{after}')

    def seg(self, i):
        s = self.SEGS[i]
        return (round(s['a'] + (.06 if s['a'] > 0 else 0), 2), round(s['b'], 2))

    def frame_js(self, ranges):
        js = "{const g=document.createElement('div');g.className='gf';g.id='gfr';document.getElementById('avbox').after(g);}\n"
        for a, b in ranges:
            js += f"tl.fromTo('#gfr',{{opacity:0}},{{opacity:1,duration:{0 if a == 0 else .35}}},{a}); tl.set('#gfr',{{opacity:0}},{max(a + .1, b - .05)});\n"
        return js
