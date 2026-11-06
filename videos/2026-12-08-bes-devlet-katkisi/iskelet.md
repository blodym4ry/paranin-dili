# Bes devlet katkısı — iskelet (öz-inceleme v1, 6 Kas 2026)
Kavram adı: **"eşik takvimi"** · metafor: katkı = vadesi dolmamış hediye; takvim eşiği geçince senin olur.

1. KANCA [avatar, FULLOPEN]: Bes'te devlet katkın yüzde otuzdan yüzde yirmiye indi. Ama asıl kaybın orada değil, çıkış gününde.
2. KİLİT [avatar]: Bir dakikada kalmanın matematiğini göstereyim.
3. BLOK 1 (oran): Ayda 1.000 TL → eskiden 300, bu yıl 200; yılda 1.200 TL eksik. Eski %30'luk katkılar duruyor.
4. ARA KANCA 1 [HERO, ters köşe]: Ama o para henüz tam senin değil.
5. BLOK 2 (hak ediş): 3 yıl dolmadan %0 · 3 yıl %15 · 6 yıl %35 · 10 yıl %60 · tamamı 10 yıl + 56 yaş. Şok: katkının yarısından fazlası erken çıkışla Hazine'ye döndü!
6. ARA KANCA 2 [HERO, desen kırılması, ZORUNLU]: Asıl önemlisi şu… bir sonraki eşiğe kaç ay kaldı?
7. BLOK 3 (uygulama): 5 yıl 10 ayda çıkan %15, 2 ay bekleyen %35. e-Devlet → EGM devlet katkısı sorgusu; giriş tarihi sözleşme sorgusunda. Sınır: "Dürüst olayım. Kal ya da çık demiyorum; fon getirisi de hesapta."
8. KAPANIŞ [HERO]: Kararı yüzde değil, takvim veriyor.
9. CTA + DÖNGÜ [HERO]: Bunu, Bes'ten çıkmayı düşünen arkadaşına gönder; asıl kaybı çıkış gününde. (→ kancadaki "asıl kaybın … çıkış gününde")

## Kancalar (tools/hookscore_tr.py hooks.txt — ekranda okunacak biçim)
| Puan | Kanca |
|---|---|
| **88.0 STRONG** ← seçildi | Bes'te devlet katkın %30'dan %20'ye indi ama asıl kaybın orada değil, çıkış gününde. |
| 61.6 OK | Bes'teysen, 1 Ocak'tan beri devletin sana eklediği para üçte bir azaldı. Ama asıl kaybı çıkış gününde yaşıyorsun. |
| 49.0 WEAK | Bes'ten çıkmayı düşünüyorsan dur: 3 yıl dolmadan çıkarsan devlet katkısının hepsi geri gidiyor. (v2/v3 deneme kancası olarak değerlendirilebilir) |

## Süre (tools/beats.py --target 60)
- wc: **156 kelime** (brief sınırı 115–160 içinde). beats.py: 222 token, ~80,7 sn @165 wpm, "20,7 sn fazla" uyarısı.
- Kalibrasyon: onaylı örnekler de beats.py'de taşıyor (ayni-maas 151 kelime → 69,1 sn; edevlet-bekleyen-para 163 kelime → 78,2 sn). Gerçek TTS (speed 1.0 + 0,3 sn duraklar) için tahmin ~62–70 sn. 70'i aşarsa ilk kesilecek: "Yılda bin iki yüz lira eksik." ve "Bir dakikada" kelimeleri.
- beats.py döngü: "last beat repeats … from the hook" (döngü var).

## Rubrik (RUNBOOK §2, öz-inceleme — bağımsız alt-ajan incelemesi YAPILMADI)
1. Doğruluk ✔ (her rakam kaynaklarda; %58 → "yarısından fazlası" sektör kaynaklı, işaretli)
2. Abartı/tavsiye yok ✔ ("Kal ya da çık demiyorum")
3. Selamsız, kime belli (Bes'te olan), merak boşluğu ✔
4. Kilit kazancı söylüyor ✔ (kısa; yol haritası zayıf — "matematik" sözü yeterli kabul edildi)
5. Her blok tek fikir + örnek, ara kancalar ✔
6. Tekrar/dolgu yok ✔ (CTA'daki "asıl kaybı çıkış gününde" bilinçli döngü tekrarı)
7. Tek kapanış, tek CTA, DM yok ✔
8. Son cümle ilk cümleye bağlı ✔
9. Süre 55–70 sn ~ (tahmin sınırda; TTS sonrası ölç)
10. 70/100'den başlıyor, ilk zirve <10 sn ✔ (%30→%20 ilk saniye)
11. Yoğunlaştırıcı döngü 5–15 sn ✔ ("asıl kaybın orada değil, çıkış gününde")
12. Yeniden kanca ≤25 sn ✔ ("Ama o para henüz tam senin değil" ~20–23 sn)
13. Risk + büyük soru + ters köşe ✔ (oran kaybı sanılıyor → asıl kayıp hak ediş)
14. Hikâye ipi ✔ (sapma yok)
15. Uygulama, izleyicinin kararına bağlı ✔ (e-Devlet sorgusu + eşik hesabı)
16. Kanca dili geniş kitleye açık ✔ (BES herkesin bildiği kelime)

## Doluluk testi
1. ≥4 kaynaklı bilgi ✔ — oran %30→%20 (RG 7 Oca 2026); eski katkılar korunur; hak ediş 0/15/35/60/100 (EGM); %58 Hazine'ye dönüş; e-Devlet EGM sorgusu.
2. Şaşırtıcı bilgi ✔ — katkının yarısından fazlası erken çıkışla Hazine'ye döndü; 2 ay farkla %15 → %35.
3. Somut adım ✔ — e-Devlet "Bireysel Emeklilik ve Otomatik Katılım Sistemlerinde Devlet Katkısı Sorgulama" + "Bireysel Emeklilik Sözleşmeleri Sorgulama" (giriş tarihi → eşik).
4. Kilit sözü teslim ✔ — "kalmanın matematiği" blok 1–3'te rakamla verildi.

## Telaffuz (TTS metni → ekran)
| Ekranda | script.txt (TTS) | Durum |
|---|---|---|
| BES'te / BES'ten | Bes'te / Bes'ten | ⚠ emin değil — TR'de "bes" diye tek hece okunuyor (yaygın kullanım); sözlükte yok, Ata dinleyip onaylasın. Alternatif: "Be E Se" |
| e-Devlet | e devlet | ✔ sözlük (Ata 30 Eki) |
| EGM | Emeklilik Gözetim Merkezi (açık hali) | ✔ kısaltma kullanılmadı |
| Hazine | Hazine | ✔ düz |
| OKS / TES | — | senaryoda yok |
