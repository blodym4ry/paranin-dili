# Gümüş: fakirin altını, iki kez kaybettirebilir — 31 Ekim 2026 (taslak, TTS YOK)

Açı: Gümüş ocak zirvesinden yarıdan fazla düştü (altın ~dörtte bir). Fiyat oynaklığının üstüne, kuyumcuda külçe gümüşte alış-satış makası ~%10'a varabilir; gram altında ~%1,2. Mekanizma + rakam + "kendin hesapla". Yatırım tavsiyesi yok, "ucuz/pahalı" denmez.

Kanca puanları (tools/hookscore_tr.py): A 83,0 (seçilen — geniş kitle, ters köşe) · B 78,0 · C 93,8 (en yüksek ama "zarar ettiysen" kitleyi daraltıyor → deneme varyasyonu için sakla).

## Senaryo (141 kelime; beats.py tahmini uzun çıkıyor, gerçek süre TTS sonrası ölçülmeli)
| # | Bölüm | Metin | Vurgu / ton | Ekran notu |
|---|---|---|---|---|
| 1 | Kanca | Gümüşe fakirin altını dediler. Ama ocaktan beri altından iki kat sert düştü! | "fakirin" merak · "iki kat" şok | Avatar tam ekran ≤1,5 sn → HERO kart. Başlık: "Fakirin altı­nı / **iki kat** düştü". Gümüş külçe gerçek fotoğraf. |
| 2 | Kilit | Sebebi iki rakamda. İkincisini kuyumcu söylemez. | "ikincisini" merak | Avatar devam. İki boş kutu: "1" ve "2 ?" (kalıcı harita başlar). |
| 3 | Blok 1 | Ocakta bir ons gümüş, yüz yirmi bir doları gördü. Ekimde elli üç doların altına indi! | "yüz yirmi bir" / "elli üç" ciddi | Parlayan kırmızı çizgi grafik: Oca 2026 zirve 121,6 → Eki ~52; kilit noktada halka. |
| 4 | | Altın aynı sürede dörtte bir civarı düştü. | "dörtte bir" | İkinci (soluk altın) çizgi aynı grafiğe; "-%57 / -%28" sabit genişlik sayaç. |
| 5 | | Çünkü gümüş küçük bir piyasa. Üstelik en büyük alıcısı sanayi. | "sanayi" | Pasta/çubuk: sanayi ~650 Moz payı (Silver Institute). |
| 6 | | Güneş paneli üreticileri gümüşü azaltıyor. Bu yıl o talep yüzde on dokuz düşebilir. | "on dokuz" ciddi | Güneş paneli gerçek görsel + "-%19 (tahmin, 2026)" kırmızı kutu. Harita kutusu 1 dolar: "FİYAT". |
| 7 | Ara kanca 1 / desen kırılması | Ama ikinci rakam, fiyat ekranında yok… | merak, yavaş | Zemin kararır, tek cümle (büyük sans + kırmızı italik "yok"). Avatar vurgu klibi (yarım ekran). |
| 8 | Blok 2 | Kuyumcuda gram altının alış satış farkı, yüzde bir civarı. | sakin | İki etiket: ALIŞ 6.396,95 / SATIŞ 6.474,76 TL (26 Eki, Kapalıçarşı) → "%1,2". |
| 9 | | Külçe gümüşte bu fark, yüzde ona kadar çıkabiliyor! | "yüzde ona" heyecan | Gümüş külçe etiketi, "%10'a kadar" büyüyen kırmızı kutu; altının %1,2'si yanında küçük kalır. |
| 10 | | Yüz bin liralık gümüşü aynı gün satsan, doksan bine düşebilirsin. | "doksan" ciddi | 100.000 → 90.000 TL sayaç geri sayar. Dipnot: "örnek hesap, %10 makasla". |
| 11 | Ara kanca 2 (zorunlu) | Çoğu kişi tam burada hata yapıyor. Sadece satış fiyatına bakıyor. | "hata" ciddi | Zoom: yalnız "SATIŞ" etiketi parlıyor, "ALIŞ" gri. |
| 12 | Blok 3 (uygulama) | Almadan önce iki fiyatı da sor. Satıştan alışı çıkar. Sonucu satışa böl. | net, adım adım | Formül kartı: (Satış − Alış) ÷ Satış = makas. Örnekle doldur. |
| 13 | | Ödediğin makas bu. | vurgu | Harita kutusu 2 dolar: "TEZGÂH". |
| 14 | Kapanış | Yani gümüşte iki kez kaybedebilirsin. Fiyatta ve tezgâhta. | "iki kez" | Kalıcı harita tek karede: 1 FİYAT (-%57) · 2 TEZGÂH (%10). Avatar HERO. |
| 15 | CTA + döngü | Bunu, kuyumcuya gümüş almaya giden bir arkadaşına gönder. Fakirin altını, ona pahalıya gelmesin. | sıcak, son cümle hafif gülümseme | Avatar yarım ekran; başlık "fakirin altını" geri gelir (döngü). |

İmla notu: özne-yüklem arası virgül yok; "yüzde ona" TTS'te "o-na" değil "on'a" okunuyor mu `pv.py tel` ile kontrol et (gerekirse "yüzde on seviyesine"). "tezgâhta" şapka TTS'i etkilemez, kontrol et.

## Doluluk testi
1. ≥4 kaynaklı bilgi: gümüş zirve 121,6 $ (29 Oca) · Eki ~52–54 $ · altın zirve ~5.405–5.589 $ → ~4.030 $ · güneş paneli talebi 2026 −%19 tahmini · gram altın makası %1,2 · külçe gümüş makası ~%6,7–10. ✔
2. Şaşırtıcı: aynı gün satışta %10'a varan kayıp; "fakirin altını" altından iki kat sert düştü. ✔
3. Kendi kontrolün: (Satış−Alış)÷Satış formülü. ✔
4. Kilit sözü ("iki rakam") teslim: 1 fiyat, 2 tezgâh. ✔
