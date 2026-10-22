"""KATMAN KATMAN kontrolü (Batuhan'ın 7 katman çerçevesi, Ata 22 Eki) — ölçülebilen maddeler.
usage: python3 tools/katman.py <slug>      (render sonrası; public/<slug>.mp4 + PD_WORK/<slug>)
Ölçülemeyenler (renk, yüz yerinde mi, grafik kelimeye oturuyor mu) için son satırdaki elle kontrol listesine bak."""
import json, os, re, subprocess, sys
slug = sys.argv[1]; REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = os.path.join(os.environ.get('PD_WORK', os.path.expanduser('~/pd_work')), slug)
words = [x for x in json.load(open(os.path.join(W, 'words.json'))) if not x['word'].startswith('<')]
ok = lambda b: '✅' if b else '❌'
R = []
f0 = words[0]['start']; R.append((ok(f0 <= .12), f'1 HAM   ilk kelime {f0:.2f} sn (≤0.12)  → değilse: split.py trim'))
first = words[0]['word'].lower().strip('.,!?')
R.append((ok(first not in {'merhaba', 'selam', 'bugün', 'bu', 'şey'}), f'1 HAM   ilk kelime "{words[0]["word"]}" (selam/tanıtım değil)'))
hook = [x for x in words if x['start'] < 3.0]
gaps = [(round(b['start'] - a['end'], 2), a['word'], b['word']) for a, b in zip(hook, hook[1:]) if b['start'] - a['end'] > .2]
R.append((ok(not gaps), f'3 KESME kancada (ilk 3 sn) 0.2 sn üstü boşluk: {gaps or "yok"}'))
allg = [(round(b['start'] - a['end'], 2), round(a['end'], 1)) for a, b in zip(words, words[1:]) if b['start'] - a['end'] > .45]
R.append((ok(not allg), f'3 KESME videoda 0.45 sn üstü ölü boşluk: {allg or "yok"}'))
ws = [re.sub(r'\W', '', x['word'].lower()) for x in words]; tri = {}
for i in range(len(ws) - 3): tri.setdefault(tuple(ws[i:i + 4]), []).append(i)
rep = [' '.join(k) for k, v in tri.items() if len(v) > 1]
R.append(('ℹ️', f'3 KESME tekrar eden 4\'lü kelime dizisi (döngü cümlesi hariç bilinçli olmalı): {rep or "yok"}'))
spec = open(os.path.join(REPO, 'videos', slug, 'spec.py')).read()
css = open(os.path.join(REPO, 'kit', 'kinetik.css.html')).read()
top = int((re.findall(r'#caps\{[^}]*top:(\d+)px', spec) or re.findall(r'#caps\{[^}]*top:(\d+)px', css))[-1])
hgt = int((re.findall(r'#caps\{[^}]*height:(\d+)px', spec) or re.findall(r'#caps\{[^}]*height:(\d+)px', css))[-1])
R.append((ok(top + hgt <= 1440), f'5 ALTYAZI altyazı alanı y={top}–{top + hgt} (Instagram alt arayüzü 1440 altında başlar)'))
mp4 = os.path.join(REPO, 'public', f'{slug}.mp4')
if os.path.exists(mp4):
    o = subprocess.run(['ffmpeg', '-nostats', '-i', mp4, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    I = float(re.findall(r'I:\s+(-?[\d.]+) LUFS', o)[-1]); R.append((ok(-14.5 <= I <= -12.5), f'7 SES   entegre ses {I} LUFS (hedef −13)'))
cue = os.path.join(W, 'hf', 'stems', 'cue_sheet.txt')
if os.path.exists(cue):
    n = sum(1 for _ in open(cue)); d = words[-1]['end']
    wh = sum('WHOOSH' in l for l in open(cue))
    R.append((ok(n / d <= 1.0 and wh == 0), f'7 SES   efekt yoğunluğu {n / d:.2f}/sn (≤1), geçiş whoosh sayısı {wh} (0 olmalı)'))
for r in R: print(r[0], r[1])
print('\nELLE: ilk karede yüz+başlık+ses hazır mı · renk telefon gibi mi · avatar geçişinde yüz zıplıyor mu · sesi kapalı ilk 3 sn konu anlaşılıyor mu ·'
      ' altyazı yüzü örtüyor mu · her grafik söylenen kelimeye oturuyor mu · "ama/ancak" dönüşünde görüntü de dönüyor mu · müzik sözün üstüne çıkıyor mu')
