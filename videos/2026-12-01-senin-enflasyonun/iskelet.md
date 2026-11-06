# Senin enflasyonun — iskelet (öz-inceleme, 6 Kas 2026)
Kavram adı: **sepet farkı** · metafor: "yüz liralık sepet" (TÜİK'in yüz lirası vs senin yüz liran) · kalıcı harita: yüz liralık sepet çubuğu (kira dilimi 6,76 → 40'a büyür).

1. KANCA [avatar, FULLOPEN]: Kiracıysan, açıklanan yüzde yirmi dokuz senin enflasyonun değil.
2. KİLİT [avatar]: Tüik'in yüz liralık sepetinde kira sadece altı lira yetmiş altı kuruş. Sonunda kendi enflasyonunu hesaplamayı göstereceğim.
3. BLOK 1 (mekanizma): Ekim verisinde yıllık %29,77. Ama bu ortalama hanenin sepeti. Her dört kişiden yaklaşık üçü kira ödemiyor!
4. ARA KANCA 1 [vurgu]: Peki bu neden önemli?
5. BLOK 2 (rakam): Bir yılda kira %39,71, gıda %27,73.
6. ARA KANCA 2 [vurgu, desen kırılması, ZORUNLU]: Asıl önemlisi şu…
7. BLOK 3 (ters köşe + uygulama): Temsili kiracı kira %40, gıda %30 → ~%33. "Sepet farkı". Kendi hesabın: geçen ayın banka hareketleri → paylar → × artış → topla; geri kalana genel rakam.
8. KAPANIŞ [avatar]: Dürüst olayım. Bu kaba bir hesap ama farkı gösterir.
9. CTA + DÖNGÜ [avatar]: Bunu, kira zammı yaklaşan bir arkadaşına gönder. Çünkü yüzde yirmi dokuz onun enflasyonu değil. (→ ilk cümleye döner)

## Kancalar (tools/hookscore_tr.py)
| Puan | Kanca |
|---|---|
| **83,0 STRONG (seçilen)** | Kiracıysan, açıklanan yüzde yirmi dokuz senin enflasyonun değil. |
| 57,0 OK | Tüik'in yüz liralık sepetinde kira altı lira, peki senin bütçende kaç lira? |
| 48,0 WEAK | Enflasyona kimse inanmıyorsa sebebi rakam değil, sepet. |
(Ara denemede "Enflasyona kimse inanmıyorsa sebebi rakam değil, sepet: kiracının enflasyonu yüzde otuz üçe çıkıyor." 84,2 aldı ama cevabı kancada veriyor ve uzun → seçilmedi; v2/v3 deneme kancası adayı.)

## Süre (tools/beats.py --target 60)
143 kelime (wc) · beats 190 token · ~69,1 sn @165 kelime/dk. Hedef bandın (55–70) üst ucunda; onaylı "aynı maaş" senaryosu aynı araçla 69,1 sn. TTS 1.0 + 0,3 sn cümle arası ile ~70 sn'yi biraz geçebilir → gerekirse "Geri kalan için genel rakamı kullan." ekranda yazıya alınıp sesten çıkarılabilir.

## Rubrik (RUNBOOK §2, 1–16) — dürüst öz-işaret
1. Doğruluk ✔ (her rakam kaynaklar.md'de; tarih: "Ekim verisinde"). Uyarı: kancadaki "yüzde yirmi dokuz" = 29,77'nin yuvarlanmamış kısaltması (etiket olarak; tam rakam blok 1'de).
2. Abartı/tavsiye/hukuki risk ✔ — TÜİK'in "yanlış" ya da "doğru" olduğu iddiası yok; sadece sepet ağırlığı mekanizması. Yatırım tavsiyesi yok.
3. Selamsız, kime (kiracı) belli, merak boşluğu ✔
4. Kilit sonda ne kazanılacağını söylüyor ✔ (kendi enflasyonunu hesaplama)
5. Blok tek fikir + ara kanca ✔ (iki ara kanca var)
6. Tekrar/dolgu ✔ (hook-CTA tekrarı bilinçli döngü)
7. Tek kapanış, tek CTA, DM vaadi yok ✔
8. Son cümle ilk cümleye bağlı ✔
9. Süre 55–70 ✔ (sınırda, ~69 sn)
10. 70/100'den başlıyor, ilk zirve (6,76 lira) ilk 10 sn'de ✔
11. Yoğunlaştırıcı döngü 5–15 sn ✔ (6,76 lira + "sonunda göstereceğim")
12. İlk yeniden kanca ≤25 sn ✔ ("Peki bu neden önemli?" ~22 sn); mini zirveler 39,71 (~24 sn), 33 (~40 sn) ✔
13. Risk + büyük soru + ters köşe ✔ (ters köşe: sorun rakam değil sepet; aynı fiyatlarla kiracıda %33)
14. Hikâye ipi ✔ — sapma yok
15. Uygulama + izleyicinin parası ✔ (banka hareketleriyle hesap)
16. Kanca dili geniş/sade ✔ — "kiracı" geniş kitle (nüfusun ~%27'si) ama kancanın dar yanı bu; ev sahibi izleyici de "kimin enflasyonu" merakıyla kalabilir. Kısmen ✔.
Bağımsız alt-ajan incelemesi YAPILMADI (brief: sadece dosya) → TTS öncesi RUNBOOK gereği yapılmalı.

## Doluluk testi
1. ≥4 kaynaklı bilgi ✔ — %29,77 · kira ağırlığı %6,76 · kiracı fert %27 · kira yıllık %39,71 · gıda %27,73 (+ hesap %33)
2. Şaşırtıcı bilgi ✔ — sepette kira yüz liranın 6,76 lirası
3. Somut adım ✔ — geçen ayın banka hareketleri → paylar × artış
4. Kilit sözü teslim ✔ — hesaplama yöntemi blok 3'te tam verildi

## Telaffuz listesi (TTS'e böyle yaz → ekranda REPL)
| Ekranda | TTS metninde | Durum |
|---|---|---|
| TÜİK | Tüik | sözlükte (Ata 30 Eki) ✔ |
| %29,77 / %39,71 / %27,73 / %33 | yazıyla ("yüzde yirmi dokuz virgül yetmiş yedi" …) | ✔ |
| 6,76 lira | altı lira yetmiş altı kuruş | ✔ |
| Başka marka/kurum/kısaltma yok | — | — |
Not: "Ekim" (ay) büyük harfle; "Kiracıysan," virgülü bilinçli duraksama.
