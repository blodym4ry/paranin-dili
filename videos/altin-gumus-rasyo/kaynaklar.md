# Altın/gümüş rasyosu backtest — veri ve yöntem (30 Eki 2026 04:50)
- Veri: Yahoo Finance aylık kapanış GC=F (altın vadeli, $/ons) ve SI=F (gümüş vadeli), TRY=X (USD/TRY); Eylül 2000 – Ekim 2026 (268 ay, bazı aylar eksik).
- Kural: ay sonu kapanışında rasyo ≥80 ve altındaysan → tümü gümüşe; rasyo ≤50 ve gümüşteysen → tümü altına. Başlangıç 1 ons altın. Makas/vergi yok (ayrıca %3 makas senaryosu).
- 2000-09 başlangıç: 1 ons altın @273,6$ → 2003-05 r80,5 (g364,5 s4,526) 80,5 ons gümüş → 2006-04 r48,2 (g651,8 s13,51) 1,669 ons altın → 2008-11 r80,1 (g816,2 s10,185) 133,8 ons gümüş → 2010-11 r49,1 (g1385 s28,185) 2,722 ons altın → 2016-02 r82,8 (g1233,9 s14,896) 225,5 ons gümüş → 2026-10: 225,5 × 51,55$ = 11.624$ × 49,92 = 580.331 TL. Sadece altın: 4.018,1$ = 200.600 TL. Oran 2,89x (her geçişte %3 makasla 2,48x). Sadece gümüş: 0,72 ons altın değeri.
- 2016-10 başlangıç: 1 ons altın @1.271,5$ → 2018-02 r80,6 → 80,6 ons gümüş → bugün 4.154$ vs altın 4.018$ (+%3,4; %3 makasla ~%0).
- Eşik hassasiyeti (2000'den): 80/60 → 2,12x · 75/55 → 2,24x · 85/55 → 1,09x · 80/65 → 2,14x. Son 10 yıl 80/65 → 1,30x. → Sonuç eşiğe çok duyarlı (videoda söylenmeli mi?).
- Aylık kapanış rasyo uçları: maks 113 (Nisan 2020), min 32 (Nisan 2011). Bugün ~78.
- Not: vadeli kontrat fiyatı spot'tan az farklıdır; günlük veriyle sonuçlar değişebilir (ör. Ocak 2026 gümüş zirvesi ay içinde).

## v2 — GÜNLÜK kapanış (inceleme: Ocak 2026 rasyo gün içi ~45; aylık kapanış bunu kaçırıyordu)
Veri: Yahoo daily GC=F/SI=F/TRY=X, 6.565 işlem günü (30.08.2000–30.10.2026). Kural 80/50, günlük kapanış.
- 2000-09: 1 ons altın → 2003-05-29 r80,9 (g370 s4,57) 80,9 ons gümüş → 2006-04-06 r49,6 (g595 s12,01) 1,632 ons altın → 2008-10-10 r81,1 (g855 s10,55) 132,4 ons gümüş → 2010-11-09 r48,8 (g1410 s28,90) 2,714 ons altın → 2015-08-26 r80,1 (g1125 s14,05) 217,3 ons gümüş → 2026-01-23 r49,3 (g4980 s100,93) 4,405 ons altın.
- Bugün (30.10.2026): altın 4.013,9 $ × 49,893 = 200.266 TL/ons → 4,405 ons ≈ 882 bin TL. %3 makas/geçiş: 3,67 ons ≈ 735 bin TL.
- 2016-10-28 başlangıç: 2018-02-05 r80,1 → 80,1 ons gümüş → 2026-01-23 → 1,624 ons altın (%3 makasla 1,53).
- Eşik duyarlılığı (2000'den, makassız): 85/55 1,56x · 80/60 2,50x · 75/50 3,54x · 85/50 1,72x. Son 10 yıl: 1,35–1,72x (hepsi >1).
- 2000 TL: USD/TRY Eylül 2000 ≈ 0,67 YTL (inceleme) → 273,6 $ ≈ 185 YTL.
