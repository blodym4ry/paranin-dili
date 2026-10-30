# Konu kapısı — "Siparişteki tuzak" (Faturadaki tuzak tipi) · 30 Ekim 2026

**Formül:** herkesin yaptığı harcama (akşam siparişi) + tek şok oran (1.000 TL'nin 469'unu restoran görmüyor) + bilinmeyen tuzak (kesinti menü fiyatına biniyor; evdekinin ~2,5 katı) + somut adım (söylemeden önce restoranın kendi hattı / gel-al fiyatı) + "gönder" CTA.

1. **Merak kanıtı — ORTA (tamamlanmalı).** @milyoner.dersleri reeli tetikleyici ama izlenme/medyan oranı ölçülmedi. Gündem kanıtı var: KDK üst sınır tavsiyesi (20 Ara 2025), TÜRES boykot/%20 indirim (Kas 2025), Ticaret Bakanlığı şeffaflık düzenlemesi (1 Nis 2026) ana akımda geniş yer aldı. Ama son 48 sa Google Trends verisi yok. → TTS öncesi: reelin izlenmesi/hesap medyanı + Trends "yemek siparişi/Yemeksepeti" kontrolü.
2. **İzleyicinin cebi — GÜÇLÜ.** Haftada iki akşam sipariş = evde pişirmeye göre yılda ~33.800 TL fark (kişi başı; 525 TL tabak vs ~200 TL ev porsiyonu). Doğrudan siparişte %20 indirim varsa 525 TL'lik tabakta ~105 TL.
3. **Öğrenme anı — GÜÇLÜ.** "Ödediğim paranın neredeyse yarısı restorana gitmiyor; üstelik bu kesinti bana menü fiyatı olarak geri dönüyor — aynı restoranı doğrudan arayınca daha ucuz olabilir."

**Doluluk testi**
1. ≥4 kaynaklı bilgi: %32 komisyon + KDV → 616 TL; 531 TL kalan; 525 TL tabak; BBC ev maliyeti 166 TL (Ocak 2026); TÜRES %20 doğrudan indirim. ✓
2. Şaşırtıcı bilgi: komisyonun üstüne KDV + 1.000 TL'nin 469'unu restoranın görmemesi. ✓
3. Somut adım: söylemeden önce restoranın kendi telefonuna / gel-al fiyatına bak. ✓ (daha güçlü yapılabilir: "uygulamadaki fiyatın ekran görüntüsünü al, restoranı ara, aynı ürünü sor")
4. Kilit sözü ("aynı yemeği daha ucuza almanın yolu") teslim ediliyor. ✓

**Riskler (bağımsız incelemede bakılmalı)**
- 469/531/%32 restoran derneğinin (taraf) rakamı — senaryoda atfedildi; platformların itirazı/yanıtı aranmadı.
- "Restoran bu kesintiyi menüye ekliyor" + 525 TL örneği nedensellik gibi okunabilir; 525 TL restoran menü fiyatı, platform fiyatı değil.
- Ev maliyeti 200 TL tahmin (BBC 166 TL × ~%20 gıda artışı).
- Ahlak dersi yok, "ev yemeği sağlıklı" yargısı yok; sipariş yasaklanmıyor, kanal değiştiriliyor. Yatırım tavsiyesi yok.
- Süre: 144 kelime, beats.py ~74 sn tahmini (hedef 55–70) → gerekirse "Peki o para nereye gidiyor?" ya da "Restoran bu kesintiyi menüye ekliyor." çıkar.

**Kanca adayları** (ekran sürümü hookscore_tr ile)
| # | Formül | Seslendirme | Ekran | Puan |
|---|---|---|---|---|
| A (seçilen) | şok oran | Siparişe ödediğin her bin liranın dört yüz altmış dokuz lirasını restoran hiç görmüyor. | Siparişe ödediğin her 1.000 liranın 469 lirasını restoran hiç görmüyor. | 83,0 STRONG |
| B | "X yapıyorsan Y kaybediyorsun" | Haftada iki akşam sipariş veriyorsan yılda otuz dört bin lirayı fazladan ödüyorsun. | Haftada 2 akşam sipariş veriyorsan yılda 34 bin lirayı fazladan ödüyorsun. | 83,0 STRONG |
| (yedek) | herkes X diyor | Ev yemeği ekonomik diyorlar. Asıl tuzak siparişin bin lirasının dört yüz altmış dokuzunda. | … 1.000 lirasının 469 lirasında. | 79,4 |
| (KULLANMA) | — | …469 lirasını yemeğe değil uygulamaya ödüyorsun. | | 93,8 ama yanlış: 64 TL'si KDV (devlete), bir kısmı restoranın kendi indirimi |
B kancası kullanılırsa "evde pişirmeye göre" bağlamı 2. cümlede verilmeli (yoksa "fazladan" belirsiz).
