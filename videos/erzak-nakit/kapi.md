# Konu kapısı — "3 günlük erzak dedi, asıl kalem nakit" (30 Ekim 2026)

1. **Merak kanıtı:** Güncel gündem: İngiltere "Be Ready" 22 Eki 2026, Pentagon FORTRESS haberi 25 Eki, Japonya çağrısı 2 Kas; TR'de CNBC-e 26 Eki "72 saatlik acil durum malzemeleri listesi" haberi yaptı. Tetikleyici @feedtalkz ve @benswann_ reelleri. EKSİK: tetikleyici reellerin izlenme/medyan oranı ve Google Trends TR verisi bu araştırmada ölçülmedi → üretimden önce Ata/Chrome ile kontrol et (≥10× medyan şartı).
2. **İzleyicinin cebi:** 4 kişilik aileye 3 günlük su ~500 TL (Hayat 5 L 65,95 TL × 8); çanta unutulursa konserve/su/pil son kullanma tarihiyle %100 kayıp; gıda yıllık ~%27,6 pahalanırken dönen stok bu artışı kilitler. Asıl risk: her 4 kişiden 1'i beklenmedik masrafı karşılayamıyor (TÜİK 2025) → 3–6 aylık gider fonu.
3. **Öğrenme anı:** Hükümetlerin listesindeki en kritik kalem konserve değil nakit; erzak 3 gün korur, birikim aylar — ve çantadaki stok ancak 6 ayda bir yenilenip yenirse para kazandırır.

## Doluluk testi
1. ≥4 kaynaklı bilgi: ✓ (İngiltere 22 Eki + 3 L/gün + nakit gerekçesi; 36 L ≈ 500 TL; gıda %27,6; TÜİK %25,1; 3–6 ay kuralı; 6 ayda bir yenileme)
2. Şaşırtıcı bilgi: ✓ listede nakit / kart-ATM çalışmayabilir; her 4 kişiden 1'i
3. Somut adım: ✓ 6 ayda bir konserveyi mutfağa al, yenisini koy; 1 aylık giderle fon başlat
4. Kilit sözü (iki stok) teslim: ✓ "Erzak üç gün korur. Birikim üç ay."
Not: "Faturadaki tuzak" formülüne uyuyor (herkesin evindeki çanta + tek şok oran + bilinmeyen tuzak + ne yapmalı + kişi tarifli GÖNDER CTA). Korku/komplo dili yok; Pentagon senaryoda kullanılmadı.

## Kancalar (ekran versiyonu `hookscore_tr.py` ile)
| # | Seslendirme (yazıyla) | Ekran | Puan |
|---|---|---|---|
| A (seçilen) | İngiltere halkına üç günlük erzak dedi. Ama listede kimsenin konuşmadığı bir kalem var. Nakit! | "İngiltere 3 günlük erzak dedi. Ama listede kimsenin konuşmadığı kalem: nakit." | 83,0 STRONG |
| B (varyasyon) | Deprem çantan varsa dikkat. İçindeki konserve paranı sessizce eritiyor olabilir. | aynı | 80,0 STRONG |
| (yedek) | Herkes üç günlük erzak konuşuyor. Ama sen üç gün nakitsiz kalırsan ne olur? | "Herkes 3 günlük erzak konuşuyor. Ama sen 3 gün nakitsiz kalırsan ne olur?" | 81,6 STRONG |

## Süre
165 kelime (`wc -w`). Görevdeki 130–170 aralığında; RUNBOOK §2 hedefi 115–150 ve `beats.py --target 55` ~23 sn fazla diyor (aracın tempo tahmini yavaş). 55–62 sn şart ise kesilecek ilk adaylar: "El feneri." · "Yerine yenisini koy." · "Çantayı bir kere doldurup unutuyor." (~10 kelime).
