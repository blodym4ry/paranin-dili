# Kira formülü (yayın 3 Aralık 2026) — rakamlar Ekim TÜFE / Kasım tavanı, tarihli
Not: 2026-11-13-kira-formul (aynı konu, zamanlanmadı) senaryosunun yeniden yazımı. Yeni: güncel Ekim verisi, "dikiz aynası" metaforu, izleyicinin TÜİK adımı, ay kuralı, aşan kısım/arabulucu/5 yıl.
Kavram adı + metafor: **dikiz aynası** (ortalama geriye bakar).

1. KANCA [FULLOPEN→HERO]: Kiran enflasyondan hızlı artıyorsa sebebi ev sahibin değil, formül.
   İlk kare başlığı önerisi: "ENFLASYON %29,77 | KİRA TAVANI %31,23"
2. KİLİT / YOĞUNLAŞTIRICI [HERO]: Ekim'de yıllık enflasyon yüzde yirmi dokuz virgül yetmiş yedi. Ama Kasım'da kira tavanı yüzde otuz bir virgül yirmi üç! Sonunda kendi tavanını nereden bulacağını söyleyeceğim.
3. BLOK 1 (formül) [PIP]: Yasal tavan yıllık enflasyon değil. Borçlar Kanunu on iki aylık ortalama enflasyona bakıyor.
4. ARA KANCA 1 (~24 sn) [HERO, desen kırılması]: Peki ortalama neden daha yüksek?
5. BLOK 2 (mekanizma + cep) [PIP; çizgi grafik: yıllık TÜFE vs 12 ay ort., Ağu–Eki]: Çünkü ortalama dikiz aynası gibidir, geriye bakar. Enflasyon düşerken eski yüksek aylar hâlâ hesapta. Otuz bin liralık kirada fark ayda dört yüz otuz sekiz lira.
6. ARA KANCA 2 (~%55) [HERO]: Asıl önemlisi şu… tavan zorunlu zam değil, üst sınır.
7. BLOK 3 (uygulama) [PIP; TÜİK bülteni ekran görüntüsü, satır vurgusu]: Tüik'in enflasyon bülteninde on iki aylık ortalama satırına bak. Sözleşmen hangi ay yenileniyorsa, bir önceki ayın verisi geçerli. Tavanı aşan kısım kanunen geçersiz. Anlaşamazsan, davadan önce arabulucu zorunlu.
   SINIR [HERO]: Dürüst olayım. Beş yılı dolan sözleşmede hâkim kirayı emsale göre yeniden belirleyebilir.
8. KAPANIŞ: (blok 3 kilitteki sözü teslim ediyor: "nereden bulacağın" = TÜİK satırı + ay kuralı; ayrı kapanış cümlesi süre için birleştirildi)
9. CTA + DÖNGÜ [HERO]: Bunu, kira sözleşmesi yenilenmek üzere olan arkadaşına gönder. Çünkü zammı ev sahibi değil, formül belirliyor.

## Kancalar (tools/hookscore_tr.py)
| Puan | Kanca | Kullanım |
|---|---|---|
| 93,8 | Enflasyon %29,77 ama kiran %31,23 artabilir: sebebi ev sahibin değil. | İlk kare başlığı / v2 deneme kancası |
| 83,0 | Kira zammında 2 rakam var, senin sözleşmene uyanı kimse söylemiyor. | v3 deneme kancası |
| 80,0 | Kiran enflasyondan hızlı artıyorsa sebebi ev sahibin değil, formül. | Sözlü ana kanca (döngüyle bağlı, rakamlar hemen 2. cümlede) |

## Süre (tools/beats.py --target 60)
141 kelime · araç tahmini ~72,7 sn (165 wpm; rakamları genişletip 200 sayıyor). Onaylı örnekler aynı araçta: ayni-maas 69,1 · zam-ayi 76,0 · edevlet 78,2 sn. Hedefin (55–70) üst sınırında/biraz üstünde; kısaltmak gerekirse ilk aday "Anlaşamazsan, davadan önce arabulucu zorunlu." (−4 sn).
Araç uyarıları: kanca 4,7 sn (8 kelimeden uzun); 4 sn'yi aşan satırlarda görsel değişim şart.

## İnceleme rubriği (öz-değerlendirme, dürüst)
1. Doğruluk ✓ (her rakam kaynaklı, "Ekim'de/Kasım'da" tarihli; "bir önceki ayın verisi" sadeleştirme: yenileme ayından önceki ayın TÜFE'si)
2. Abartı/tavsiye/hukuk ✓ genel bilgi; "geçersiz" ve "arabulucu zorunlu" kanun düzeyinde ifadeler, kişiye yönelik tavsiye yok — ~ hukuki dil ikinci gözle bakılmalı
3. Selamsız, kime konuştuğu belli (kiracı), merak boşluğu ✓
4. Kilit ne kazanılacağını söylüyor ✓
5. Bloklar tek fikir + ara kancalar ✓
6. Tekrar/dolgu ✓ ("ortalama" 3 kez geçiyor — kasıtlı terim)
7. Tek CTA, DM/hediye yok ✓ · kapanış ayrı cümle değil (blok 3 + CTA ile birleşik) ~
8. Son cümle ilk cümleye bağlı ✓
9. Süre ~ (araç 72,7 sn; sınırda)
10. 70/100 başlangıç, ilk zirve ~10 sn'de (%31,23) ✓
11. Yoğunlaştırıcı döngü 5–15 sn ("Ama Kasım'da… !") ✓
12. İlk yeniden kanca ~24 sn ✓ (sınıra yakın)
13. Risk + soru + ters köşe (ev sahibi değil formül; tavan zam değil) ✓
14. Hikâye ipi ✓ (5 yıl cümlesi konuya bağlı sınır cümlesi)
15. İzleyicinin parası/kararı ✓ (438 TL, TÜİK satırı)
16. TAM: geniş kitle ("kiran"), sade dil ✓

## Doluluk testi
1. ≥4 kaynaklı bilgi ✓: %29,77 · %31,23 · TBK 12 aylık ortalama · 438 TL hesap · aşan kısım geçersiz · arabulucu · 5 yıl kuralı
2. Şaşırtıcı ✓: enflasyon düşerken tavan üstünde kalıyor; tavanı aşan kısım geçersiz
3. Somut adım ✓: TÜİK bülteni "on iki aylık ortalamalara göre" satırı + yenileme ayından önceki ay kuralı
4. Kilit sözü teslim ✓ ("tavanını nereden bulacağın")

## Telaffuz
| Metin | TTS'te | Durum |
|---|---|---|
| TÜİK | Tüik | sözlükte (Ata 30 Eki) |
| Borçlar Kanunu | Borçlar Kanunu | düz okunur |
| hâkim | hâkim | EMİN DEĞİLİM: şapka TTS'te sorun çıkarabilir; dinle, gerekirse "hakim" yaz |
| Ekim'de / Kasım'da | aynen | kesme işareti — pv.py tel'de biçim farkı çıkabilir |
| dikiz aynası | aynen | - |
| "…" (Asıl önemlisi şu…) | aynen | merak duraksaması |
