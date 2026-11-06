# Taksit psikolojisi — iskelet (öz-inceleme v1, 6 Kas 2026)
Kavram adı + metafor: **taksit merceği** — aylığı büyütüyor, toplamı saklıyor.
Kelime: 154 (wc) · beats.py: ~73,5 sn @165 wpm (araç fazla tahmin ediyor: ayni-maas 151 kelime → gerçek 58 sn) → tahmini gerçek ~60 sn + cümle arası 0,3 sn duraklama ≈ 65–68 sn.

1. KANCA [avatar, FULLOPEN]: Yetmiş iki bin lira pahalı geliyor. Ama ayda altı bin, ucuz! Para aynı… beynin neden ikisine farklı fiyat biçiyor?
2. KİLİT [avatar]: Sonda, taksitten önceki tek kontrolü söyleyeceğim.
3. BLOK 1 (ödeme acısı, mekanizma): Bunun adı ödeme acısı. İki bin yedide, alışveriş yapanların beyni tarandı. Pahalı fiyatta, acıyla ilişkili bir bölge yanıyordu. Yandıkça insanlar vazgeçiyordu. [Knutson vd. 2007; ekranda "Stanford, 2007" + beyin taraması görseli]
4. GEÇİŞ / mini zirve: Kart ve taksit bu acıyı hafifletiyor. Bir deneyde kartla ödeyecekler, aynı maç biletine nakitçilerin iki katından fazlasını teklif etti. [Prelec & Simester 2001; ekranda "MIT, 2001" + bilet görseli]
5. ARA KANCA 1 [HERO]: Peki Türkiye'de?
6. BLOK 2 (Türkiye verisi): Bireysel kart harcamalarının yaklaşık üçte biri taksitli. [BDDK/Ekonomim, Mayıs 2026]
7. ARA KANCA 2 — ZORUNLU [HERO, desen kırılması]: Asıl önemlisi şu… faizli taksitte acı sonradan geliyor.
8. BLOK 3 (toplam maliyet): Kasım başı itibarıyla kart faizinin tavanı ayda yüzde üç virgül yetmiş beş. Bu oranla yetmiş iki bin lira, on iki ayda doksan bini geçiyor. Vergiler hariç! [72.000 → 90.731 TL; ekranda sayaç]
9. KAVRAM [HERO]: Buna taksit merceği diyorum. Aylığı büyütüyor, toplamı saklıyor.
10. SINIR: Dürüst olayım. Peşin fiyatına faizsiz taksit kötü değil.
11. ADIM (izleyicinin kontrolü): Kontrol şu. Ödeme ekranındaki taksit tablosunda toplam tutarı bul. Yanına, kaç maaşın ettiğini yaz.
12. CTA + DÖNGÜ [HERO]: Bunu, her alışverişte "kaç taksit?" diye soran arkadaşına gönder. Çünkü o altı bin, aslında yetmiş iki bindi.

## Kancalar (tools/hookscore_tr.py, ekranda okunacak hâliyle)
| Puan | Kanca |
|---|---|
| **82,3 STRONG** | 72 bin lira pahalı geliyor ama ayda 6 bin ucuz: beynin seni neden kandırıyor? ← SEÇİLDİ (ilk kare başlığı: "72 BİN PAHALI | AYDA 6 BİN UCUZ?") |
| 57,0 OK | Taksitle alıyorsan dur: 72 bin liralık şey sana 90 bini geçebilir. (v2/v3 deneme kancası adayı) |
| 49,0 WEAK | Kartla ödeyenler aynı bilete nakitçilerin 2 katından fazlasını verdi, sebebi taksitte de var. |

## Doluluk testi
1. ≥4 kaynaklı bilgi: ✅ Knutson 2007 (insula) · Prelec & Simester 2001 (kartla 2 katı) · BDDK taksit payı ~üçte bir · TCMB tavan %3,75 (1 Kas 2026) · hesap 72k→90,7k. (+ Prelec & Loewenstein 1998, Gourville 1998 kaynakta/ekranda)
2. Şaşırtıcı bilgi: ✅ kartla ödeyecekleri bilen kişiler aynı bilete iki katından fazlasını teklif ediyor; 72 bin → 90 bin+.
3. Somut adım: ✅ ödeme ekranındaki taksit tablosunda "toplam" satırı + kaç maaş ettiğini yazmak.
4. Kilit sözü teslim: ✅ kilit "tek kontrol" diyor; blok 11'de tek kontrol veriliyor. Hiçbir blok tek cümleyle geçiştirilmiyor (blok 2 tek cümle ama veri bloğu; ara kancayla birlikte iş görüyor — sınırda).

## Rubrik öz-incelemesi (RUNBOOK §2, 1–16) — dürüst
1. Doğruluk ✅ (tüm rakamlar kaynaklarda; "Kasım başı" tarihli). ⚠ taksit payı ikincil haber kaynağı.
2. Abartı/garanti/tavsiye ✅ yok; "tavan oran", "vergiler hariç", "faizsiz taksit kötü değil" sınırı var.
3. İlk cümle selamsız, merak boşluğu ✅ (kime: taksitle alışveriş yapan herkes — "sen" hitabı 3. cümlede).
4. Kilit ne kazanılacağını söylüyor ✅ ("tek kontrol").
5. Blok tek fikir + örnek, ara kancalar ✅ (2 ara kanca).
6. Tekrar/dolgu ✅ yok ("acı" kelimesi 3 kez — bilinçli zincir).
7. Kapanış tek cümle, tek CTA, DM/hediye yok ✅.
8. Son cümle ilk cümleye bağlı ✅ (altı bin ↔ yetmiş iki bin).
9. Süre 55–70 sn ✅ (tahmini 65–68; beats.py 73,5 der — seslendirmeden sonra ölç, 70'i geçerse "Dürüst olayım" cümlesini koru, "Bunun adı ödeme acısı."yı kes).
10. 70/100'den başlıyor ✅; ilk zirve (para aynı, beyin farklı fiyat) ilk 10 sn'de ✅.
11. Yoğunlaştırıcı döngü 5–15 sn ✅ ("beynin neden ikisine farklı fiyat biçiyor?" + "tek kontrol").
12. Mini zirve 10–15 sn'de ✅ (beyin taraması ~15 sn, kart deneyi ~25 sn); ilk yeniden kanca ≤25 sn ⚠ SINIRDA: "Kart ve taksit bu acıyı hafifletiyor" ~23 sn'de yumuşak geçiş; açık soru-kanca "Peki Türkiye'de?" ~30 sn'de.
13. Risk + büyük soru + ters köşe ✅ (inanılan: taksit ucuzlatır → gerçek: acıyı kısıyor, faizliyse 90 bin).
14. Hikâye ipi ✅ — her cümle "fiyat algısı → toplam maliyet" ipine bağlı.
15. Uygulama, arzu çapası ✅ (izleyicinin kendi ödeme ekranı ve maaşı).
16. Kanca dili geniş kitle ✅ (terim yok; "zihinsel muhasebe" bilinçli olarak söylenmedi).
Not: Bu bir ÖZ-incelemedir; RUNBOOK'un istediği bağımsız alt-ajan incelemesi (Agent aracı bu oturumda yok) TTS öncesi ayrıca yapılmalı.

## Telaffuz listesi
Senaryoda marka, kurum adı ya da kısaltma YOK (Stanford, MIT, BDDK, TCMB bilinçli olarak sözden çıkarıldı; ekranda yazılabilir).
- "yüzde üç virgül yetmiş beş" — düz okunur. "nakitçilerin", "taksit merceği" — Türkçe, sorun beklenmez.
- ⚠ "kaç taksit?" tırnak içinde soru: TTS soru tonuyla okuyup CTA'yı bölebilir → `pv.py tel` ve dinleme kontrolü; sorun olursa tırnakları kaldır: 'Bunu, her alışverişte kaç taksit diye soran arkadaşına gönder.'
- ⚠ "Sonda," (kısa) — TTS "sonda" (alet) gibi vurgulayabilir; gerekirse "Sonunda," yap.
