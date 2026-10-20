# 10 yıl: Ekim 2016 -> 15 Ekim 2026, 100.000 TL (kaynaklar.md)
P = 100_000
base = {'altin': 125.7, 'dolar': 3.09, 'bist': 77554.21 / 100}   # BIST 2020'de 100'e bölündü
son = {'altin': 6600.58, 'dolar': 49.42, 'bist': 12057.35}
tufe = 1.0
for r in [11.20, 24.52, 9.26, 11.75, 19.58, 83.45, 61.53, 49.38, 33.29, 29.73]:  # Eylül yıllık TÜFE 2017..2026
    tufe *= 1 + r / 100
print(f'TÜFE Eyl2016->Eyl2026 x{tufe:.2f}; alım gücünü korumak için {P*tufe:,.0f} TL')
for k in base:
    m = son[k] / base[k]
    print(f'{k:6s} x{m:5.2f}  {P*m:12,.0f} TL  reel x{m/tufe:.2f} ({(m/tufe-1)*100:+.1f}%)')
