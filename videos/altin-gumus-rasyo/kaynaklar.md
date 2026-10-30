# Altın/gümüş rasyosu backtest — veri ve yöntem (30 Eki 2026 04:50)
- Veri: Yahoo Finance aylık kapanış GC=F (altın vadeli, $/ons) ve SI=F (gümüş vadeli), TRY=X (USD/TRY); Eylül 2000 – Ekim 2026 (268 ay, bazı aylar eksik).
- Kural: ay sonu kapanışında rasyo ≥80 ve altındaysan → tümü gümüşe; rasyo ≤50 ve gümüşteysen → tümü altına. Başlangıç 1 ons altın. Makas/vergi yok (ayrıca %3 makas senaryosu).
- 2000-09 başlangıç: 1 ons altın @273,6$ → 2003-05 r80,5 (g364,5 s4,526) 80,5 ons gümüş → 2006-04 r48,2 (g651,8 s13,51) 1,669 ons altın → 2008-11 r80,1 (g816,2 s10,185) 133,8 ons gümüş → 2010-11 r49,1 (g1385 s28,185) 2,722 ons altın → 2016-02 r82,8 (g1233,9 s14,896) 225,5 ons gümüş → 2026-10: 225,5 × 51,55$ = 11.624$ × 49,92 = 580.331 TL. Sadece altın: 4.018,1$ = 200.600 TL. Oran 2,89x (her geçişte %3 makasla 2,48x). Sadece gümüş: 0,72 ons altın değeri.
- 2016-10 başlangıç: 1 ons altın @1.271,5$ → 2018-02 r80,6 → 80,6 ons gümüş → bugün 4.154$ vs altın 4.018$ (+%3,4; %3 makasla ~%0).
- Eşik hassasiyeti (2000'den): 80/60 → 2,12x · 75/55 → 2,24x · 85/55 → 1,09x · 80/65 → 2,14x. Son 10 yıl 80/65 → 1,30x. → Sonuç eşiğe çok duyarlı (videoda söylenmeli mi?).
- Aylık kapanış rasyo uçları: maks 113 (Nisan 2020), min 32 (Nisan 2011). Bugün ~78.
- Not: vadeli kontrat fiyatı spot'tan az farklıdır; günlük veriyle sonuçlar değişebilir (ör. Ocak 2026 gümüş zirvesi ay içinde).
