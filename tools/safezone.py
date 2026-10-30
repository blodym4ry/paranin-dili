"""Güvenli alan denetimi (Ata 29 Eki: "altyazı adımın üstünde… tam ekranda köşeler gözükmüyor").
Kural: görünür her öğe (yazı, kutu, grafik, avatar kartı, altyazı) x 100–880, y 220–1440 kutusunda kalır.
- y<220: IG üst çubuğu · y>1440: kullanıcı adı/açıklama/ses şeridi · x>880: beğen/yorum/paylaş rayı
- x<100 / x>980: uzun ekranlı telefonlar tam ekranda iki yandan ~100 px kırpar
İstisna: tam ekran zemin (#grid/#glow/.bg) ve kancanın ilk ≤1,5 sn'lik tam ekran avatar açılışı (FULLOPEN).
Kullanım: python3 tools/safezone.py <hf_dir>   (pv.py check bunu otomatik çağırır)"""
import sys, os, json
from playwright.sync_api import sync_playwright

BOX = dict(l=100, r=880, t=220, b=1440)
TOL = 3

JS = r'''([t, box, tol]) => {
  const tl = window.__timelines['main']; tl.seek(t, false);
  const out = [];
  const skip = el => el.closest('#grid,#glow,.bg,#dark,svg defs') || el.id === 'root';
  const eff = el => { let o = 1; for (let e = el; e && e !== document.body; e = e.parentElement) {
      const cs = getComputedStyle(e); if (cs.display === 'none' || cs.visibility === 'hidden') return 0; o *= parseFloat(cs.opacity); } return o; };
  for (const el of document.querySelectorAll('#root *')) {
    if (skip(el)) continue;
    const cs = getComputedStyle(el);
    const boxy = (cs.borderTopWidth !== '0px' && cs.borderTopStyle !== 'none') || cs.backgroundImage !== 'none' ||
      (cs.backgroundColor !== 'rgba(0, 0, 0, 0)' && cs.backgroundColor !== 'transparent') ||
      ['VIDEO', 'IMG', 'path', 'rect', 'circle', 'line', 'polyline', 'text'].includes(el.tagName);
    const rects = [];
    if (boxy) rects.push(el.getBoundingClientRect());
    for (const n of el.childNodes) if (n.nodeType === 3 && n.textContent.trim()) {
      const rg = document.createRange(); rg.selectNodeContents(n); for (const q of rg.getClientRects()) rects.push(q); }
    if (!rects.length) continue;
    // clip-path: inset(...) olan atada (avatar penceresi) görünür alan kırpılmış kutudur
    for (let e = el; e && e !== document.body; e = e.parentElement) {
      const cp = getComputedStyle(e).clipPath; const m = cp && cp.match(/^inset\(([^)]*?)(?: round[^)]*)?\)$/);
      if (!m) continue; const v = m[1].trim().split(/\s+/).map(parseFloat); const [t, r, b, l] = [v[0], v[1] ?? v[0], v[2] ?? v[0], v[3] ?? v[1] ?? v[0]];
      const bb = e.getBoundingClientRect(), k = bb.width / (e.offsetWidth || bb.width);
      const c = {left: bb.left + l * k, right: bb.right - r * k, top: bb.top + t * k, bottom: bb.bottom - b * k};
      for (const q of rects.splice(0)) rects.push({left: Math.max(q.left, c.left), right: Math.min(q.right, c.right), top: Math.max(q.top, c.top), bottom: Math.min(q.bottom, c.bottom)});
      break; }
    if (eff(el) < .05) continue;
    const r = {left: Math.min(...rects.map(q => q.left)), right: Math.max(...rects.map(q => q.right)),
               top: Math.min(...rects.map(q => q.top)), bottom: Math.max(...rects.map(q => q.bottom))};
    r.width = r.right - r.left; r.height = r.bottom - r.top;
    if (r.width < 2 || r.height < 2) continue;
    if (r.width >= 1070 && r.height >= 1900) continue;   // tam ekran zemin
    const bad = [];
    if (r.left < box.l - tol) bad.push(`sol ${Math.round(r.left)}`);
    if (r.right > box.r + tol) bad.push(`sağ ${Math.round(r.right)}`);
    if (r.top < box.t - tol) bad.push(`üst ${Math.round(r.top)}`);
    if (r.bottom > box.b + tol) bad.push(`alt ${Math.round(r.bottom)}`);
    if (bad.length) out.push(`${el.tagName.toLowerCase()}${el.id ? '#' + el.id : ''}${el.className && typeof el.className === 'string' ? '.' + el.className.split(' ')[0] : ''} "${(el.textContent || '').trim().slice(0, 24)}" → ${bad.join(', ')}`);
  }
  return out;
}'''


def run(hf):
    html = open(os.path.join(hf, 'index.html'), encoding='utf-8').read()
    import re
    fo = re.search(r'const FULLOPEN=([0-9.]+)', html)
    fullopen = float(fo.group(1)) + .45 if fo and float(fo.group(1)) > 0 else 0
    if fullopen > 1.95: print(f'SAFEZONE FAIL: tam ekran açılış {fullopen - .45:.2f} sn (en fazla 1,5)'); return False
    m = re.search(r'SC=(\[\[.*?\]\])', html)
    sc = json.loads(m.group(1)) if m else []
    times = sorted({round(t, 2) for _, a, b in sc for t in (a + .8, (a + b) / 2, b - .12) if t > fullopen})   # a+.8: avatar geçişi 0,7 sn; tween sırasında video kutusu clip-path dışına taşar (görünmez)
    bad = {}
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        pg.add_init_script('window.__timelines = {};')
        pg.goto('file://' + os.path.abspath(os.path.join(hf, 'index.html')))
        for _ in range(60):
            pg.wait_for_timeout(500)
            if pg.evaluate("!!(window.__timelines && window.__timelines['main'])"): break
        else: sys.exit('SAFEZONE: zaman çizelgesi yüklenmedi')
        pg.wait_for_timeout(800)
        for t in times:
            for line in pg.evaluate(JS, [t, BOX, TOL]):
                bad.setdefault(line, []).append(t)
        b.close()
    for line, ts in sorted(bad.items(), key=lambda kv: kv[1][0]):
        print(f'SAFEZONE  t={ts[0]:.1f}s  {line}')
    print('SAFEZONE', 'PASS' if not bad else f'FAIL ({len(bad)} öğe)')
    return not bad


if __name__ == '__main__':
    sys.exit(0 if run(sys.argv[1]) else 1)
