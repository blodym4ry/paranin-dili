# Taksit sınırı (4 Aralık 2026) — iskelet
Kavram adı: **"taksit çarpımı"**. Metafor: kasadaki etiket taksit sayısını gösterir, bedeli ise çarpım söyler.

1. KANCA [avatar, FULLOPEN]: Sıfır telefonu kredi kartına tek taksit bile yapamazsın. Ama aynı kartla buzdolabına dokuz taksit var!
2. KİLİT: Sonunda, taksitin gerçek bedelini tek çarpımla bulacaksın.
3. BLOK 1 (kural + amaç): 2014 yasağı; gerekçe cari açık ve kart borçları; telefon dahil telekomünikasyona taksit yok; BDDK Ekim'de güncelledi, yasak sürüyor.
4. ARA KANCA 1 [vurgu]: Peki telefonu taksitle alanlar nasıl alıyor?
5. BLOK 2 (iki kapı + diğer ürünler): yenilenmiş telefona kartla 12 taksit, tutar sınırı yok; sıfır telefona kredi: 40 bine kadar 12 ay, üstü 3 ay. Buzdolabı ve mobilya 9; TV eşiği hâlâ 5 bin, üstü 4 taksit (ters köşe).
6. ARA KANCA 2 [ZORUNLU, desen kırılması]: Asıl önemlisi şu… sınırı bilmek yetmez.
7. BLOK 3 (uygulama): ödeme ekranında taksit tablosu → aylık × sayı − peşin = vade farkı; kredide "toplam geri ödeme tutarı". Sınır cümlesi: "Dürüst olayım. Peşin fiyatına taksitte bu fark sıfır çıkar."
8. KAPANIŞ [avatar]: Yani sayıyı kural koyar, bedeli çarpım söyler.
9. CTA + DÖNGÜ [avatar]: Bunu, yeni telefonu taksitle almak isteyen arkadaşına gönder. (Döngü: telefon ↔ ilk cümle.)

## Kancalar (tools/hookscore_tr.py)
| Puan | Kanca |
|---|---|
| **81,6 STRONG** (seçilen) | Sıfır telefonu kredi kartına tek taksit bile yapamazsın. Ama buzdolabına 9 taksit var! |
| 54,6 OK | Telefonu kartla taksitle alamıyorsan sebebi bankan değil, 2014'teki bir kural. |
| 49,0 WEAK | Taksitle alışveriş yapıyorsan dur: 9 taksitin sana kaça mal olduğunu tek çarpım söyler. |

## Süre
- 159 kelime (wc). `beats.py --target 60` 77,1 sn diyor, ama araç Türkçe harfleri kelime ayırıcı saydığı için 212 "kelime" sayıyor. Kalibrasyon: ayni-maas'ta beats 69,1 sn dedi, gerçek süre 58,0 sn çıktı (×0,84). Bu senaryoda tahmini gerçek süre **≈ 63–67 sn** (0,3 sn duraklamalar dahil). 70 sn'yi aşarsa ilk kesilecek cümle "Tutar sınırı yok." olur.

## Doluluk testi
1. ✅ 4+ kaynaklı bilgi: 2014 yasağı ve gerekçesi; 1 Ekim 2026 BDDK kararı; yenilenmiş telefona 12 taksit ve tutar sınırı yok; kredide 40 bin / 12 ay / 3 ay; elektrikli eşya ve mobilya 9; TV eşiği 5 bin, üstü 4.
2. ✅ Şaşırtıcı bilgi: sıfır telefona kartla taksit hiç yok ama yenilenmişe sınırsız tutarda 12 taksit var; TV eşiği hâlâ 5 bin TL.
3. ✅ Somut adım: ödeme ekranındaki taksit tablosu (aylık × sayı − peşin); kredi teklifinde "toplam geri ödeme tutarı" satırı.
4. ✅ Kilitteki söz ("tek çarpımla gerçek bedel") Blok 3'te eksiksiz teslim ediliyor.

## Öz-inceleme (RUNBOOK §2 rubriği; bağımsız alt-ajan incelemesi YAPILMADI, sadece öz-inceleme)
1. Doğruluk ✅ (her rakam kaynaklar.md'de; tarih "Ekim" söyleniyor). ⚠ 4 Aralık'a kadar değişirse güncellenmeli.
2. Abartı / tavsiye ✅ (yatırım tavsiyesi yok; "Dürüst olayım" sınır cümlesi var).
3. Selamsız, ikinci tekil şahıs, merak açık ✅
4. Kilit ne kazanılacağını söylüyor ✅
5. Bloklar tek fikirli, aralarında ara kanca var ✅ (Blok 2'de telefon kapıları + diğer ürünler var; ikisi de "sınır" fikri altında, ekranda iki ayrı sahne olmalı)
6. Tekrar / dolgu ✅ ("sadece" iki kez geçiyor, kabul edilebilir)
7. Tek kapanış, tek CTA, DM vaadi yok ✅
8. Döngü ✅ (CTA'daki "telefon" ilk cümleye bağlanıyor)
9. Süre 55–70 ✅ (tahmini 63–67 sn; kayıtta doğrulanmalı)
10. İlk zirve 0–4 sn'de ✅ (telefon 0 / buzdolabı 9 zıtlığı)
11. Yoğunlaştırıcı döngü 5–15 sn ⚠ Kısmen: kilit + "2014" ile mekanizmaya geçiliyor; risk büyüten ayrı bir cümle yok.
12. İlk yeniden kanca ≤25 sn ✅ ("Peki telefonu taksitle alanlar…", ~22–24. sn)
13. Risk + büyük soru + ters köşe ✅ (ters köşe: kural cari açık için konmuş ama yenilenmişe tutar sınırı yok; TV eşiği 5 bin)
14. Hikâye ipi ✅ (her cümle taksit sınırına bağlı)
15. İzleyicinin parasına bağlanıyor ✅ (vade farkı hesabı)
16. Kanca dili geniş kitleye açık ✅

## Telaffuz
- BDDK → "Be De De Ka" (⚠ EMİN DEĞİLİM: sözlükte BTK → "Beteka", SSK → "Se Se Ke" var. Alternatifler: "Bedeteka", "Be De De Ke". Ata seçmeli. Ekranda "BDDK")
- "iki bin on dört" → ekranda 2014 · "Ekim'de" düz okunur · "telekomünikasyon" düz okunur
