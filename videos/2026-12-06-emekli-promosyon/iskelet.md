# İskelet — 2026-12-06-emekli-promosyon
Kavram adı: **"masadaki para"** (bankanın teklif ettiği ama başvurulmadığı için alınmayan promosyon). Metafor: masaya konan para; kalkarsan masada kalır.

| Bölüm | Metin | Avatar |
|---|---|---|
| 1. Kanca | Emekli maaşını hiç taşımadıysan, bankanın masaya koyduğu on iki bin lirayı bırakıyor olabilirsin. | FULLOPEN ≤1,5 sn → HERO |
| 2. Kilit (yol haritası) | Üç şey var. Üçüncüsü taşımayı bile gereksiz kılabilir. | HERO |
| 3. Blok 1 (tablo) | Bir. Kasım başı itibarıyla kamu bankaları yirmi bin ve üstü maaşa on iki bin lira veriyor. Özel bankalarda şartsız nakit yirmi bine çıkıyor. Otuz beş bin gibi rakamlar ise kart ve fatura şartlı. | PIP |
| 4. Ara kanca 1 | Ama bu para üç yıllık bir söz. | HERO (vurgu) |
| 5. Blok 2 (taşıma + iade) | İki. Taşımak için e devlette Banka ve Adres Değişikliği ekranı yeterli. Bir yıl sonra ayrılırsan kalan iki yılın payı geri istenir. On iki binin sekiz bini gider! | PIP |
| 6. Ara kanca 2 (zorunlu) | Asıl önemlisi şu… hiç taşımadıysan tam burası seni ilgilendiriyor. | HERO, desen kırılması |
| 7. Blok 3 (ters köşe + adım) | Üç. Promosyon kendiliğinden yatmıyor. Başvuru istiyor. Ziraat örneğin maaşı zaten kendisine yatan emekliye de başvuruyla ödüyor. Bankanı ara, tek soru sor. Taahhüdüm ne zaman bitiyor? | PIP → HERO (soru) |
| 8. Kapanış / sınır | Dürüst olayım. En büyük rakam her zaman en iyisi değil. | HERO |
| 9. CTA + döngü | Bunu, emekli annesine babasına bakan arkadaşına gönder. O on iki bin lira, taşımadan da masada olabilir. | HERO |

Ekran notları: Blok 1'de tablo kartı (Kamu 5.000–12.000 · Özel şartsız ≤20.000 · Şartlı ≤35.000, altta "Kasım 2026 başı, bankalar değiştirebilir"). Blok 2'de e-Devlet ekran görüntüsü + 36 aylık çubuk, 12. ayda kesik, 24/36 kırmızı = 8.000 TL. Blok 3'te soru büyük yazı: "Taahhüdüm ne zaman bitiyor?". Banka logoları sadece tablo bilgisi; "öneri/en iyi banka" ibaresi yok.

## Kancalar (tools/hookscore_tr.py)
| Puan | Kanca |
|---|---|
| **83,0 STRONG** (seçilen) | Emekli maaşını hiç taşımadıysan, bankanın masaya koyduğu 12 bin lirayı bırakıyor olabilirsin. |
| 59,8 OK | Herkes emekli promosyonu için banka değiştir diyor, ama 12 bin lira kendi bankanda da olabilir. (v2 adayı, zıtlık) |
| 47,1 WEAK | Annenin emekli maaşı yıllardır aynı bankaya yatıyorsa, 12 bin liralık bir başvuruyu kaçırıyor olabilir. (v3 adayı, düzeltilmeli) |

## Süre (tools/beats.py --target 60)
146 kelime (wc). beats.py: 194 konuşma kelimesi, 165 kelime/dk ile ~70,5 sn (araç sayıları açık okuyor, örnek "aynı maaş" 151 kelimede 69,1 sn verdi). Uyarılar: kanca 7,3 sn (3 sn'yi aşıyor; ekran başlığı ilk karede ≤6 kelime ile telafi edilir: "MAAŞINI TAŞIMADIN MI? | 12.000 TL MASADA"); 4 sn'yi aşan birkaç beat → ekran değişimiyle bölünmeli. Döngü: son beat kancadaki "on iki bin / masada / taşı" kelimelerini tekrarlıyor (OK).

## İnceleme rubriği (öz değerlendirme; bağımsız alt-ajan incelemesi YAPILMADI)
1. Doğruluk — ✓ (her rakam kaynaklar.md'de; "Kasım başı itibarıyla" tarihli). Risk: özel banka rakamları Aralık'ta değişebilir.
2. Abartı/tavsiye yok — ✓ (banka önerisi yok; Ziraat yalnız mekanizma örneği; "dürüst olayım" sınırı).
3. Selamsız, kime konuşulduğu belli, merak boşluğu — ✓
4. Kilit ne kazanılacağını söylüyor — ✓ (üç şey + üçüncüsü taşımayı gereksiz kılabilir)
5. Her blok tek fikir + örnek, aralarında ara kanca — ✓
6. Tekrar/dolgu yok — ✓
7. Kapanış tek cümle, tek CTA, DM vaadi yok — ✓
8. Son cümle ilk cümleye bağlı — ✓ (masa / on iki bin / taşımak)
9. Süre 55–70 sn — ~ (beats 70,5 sn; gerçek seslendirmede ~60–65 sn bekleniyor, sınırda)
10. 70/100'den başlıyor, ilk zirve 10 sn içinde — ✓ (12 bin lira ilk cümlede)
11. Yoğunlaştırıcı döngü 5–15 sn — ✓ ("üçüncüsü taşımayı bile gereksiz kılabilir")
12. Mini zirve 10–15 sn'de bir, ilk yeniden kanca ≤25 sn — ✓ (ara kanca 1 ~25 sn)
13. Risk + büyük soru + ters köşe — ✓ (A: taşı, promosyon al → B: taşımadan da alabilirsin, erken taşırsan geri ödersin)
14. Hikâye ipi, sapma yok — ✓
15. İzleyicinin parasına bağlı, uygulama var — ✓ (bankayı ara, taahhüt bitiş tarihini sor)
16. Kanca dili geniş kitleye açık — ✓ (emekli + emekliye bakan çocuk)

## Doluluk testi
1. ≥4 kaynaklı bilgi — ✓ (kamu 12.000; özel şartsız 20.000; şartlı 35.000; 3 yıl peşin taahhüt; kıst iade 24/36; e-Devlet Banka ve Adres Değişikliği; mevcut müşteriye başvuruyla ödeme)
2. Şaşırtıcı bilgi — ✓ (taşımadan, kendi bankandan başvuruyla alınabiliyor; 1 yılda ayrılırsan 12 binin 8 binini geri ödersin)
3. Somut adım — ✓ (bankayı ara: "Taahhüdüm ne zaman bitiyor?"; taşıma ekranının adı)
4. Kilit sözü teslim — ✓ (üçüncü madde gerçekten taşımayı gereksiz kılabilecek bilgiyi veriyor)

## Telaffuz listesi (TTS metninde)
| Ekranda | TTS'e | Not |
|---|---|---|
| e-Devlet | e devlet | sözlükte (Ata 30 Eki) |
| Ziraat | Ziraat | Türkçe, sorun beklenmez |
| Banka ve Adres Değişikliği | aynen | Türkçe hizmet adı |
| 12.000 / 20.000 / 35.000 / 8.000 TL | on iki bin / yirmi bin / otuz beş bin / sekiz bin | yazıyla |
| Taahhüdüm | Taahhüdüm | **emin değilim**: çift "h" TTS'te yutulabilir; `pv.py tel` ile dinle, sorun olursa "Taahüdüm" dene |
| SGK, QNB, Şekerbank | — | seslendirmede YOK, yalnız ekran tablosunda |
