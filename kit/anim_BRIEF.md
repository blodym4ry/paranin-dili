# Animasyon deneme videosu — ortak brief (Paranın Dili, @atamertuysaler)
Bu iş için `animation-studio` skill'ini kullan. Skill klasörü:
/root/.claude/skills/synced/7dc524db-7a70-47e9-b12b-cabb86239b4f_6beda3e3-4f9e-4b1a-b88d-4192e955d5a7/animation-studio
Önce SKILL.md'yi, sonra references/INPUT_CONTRACT.md, PRODUCTION_WORKFLOW.md, RENDERING_AND_QA.md, QUALITY_RUBRIC.md ve SADECE seçili stilin references/styles/<stil>.md dosyasını oku ve uygula.

## Girdiler (her video için görev mesajında verilir)
- Script (kilitli, kelimesi kelimesine seslendirilmiş): /home/claude/paranin-dili/videos/<slug>/script.txt
- Seslendirme: /home/claude/pd_work/<slug>/voice.wav  (HeyGen TTS, Türkçe)
- Kelime zamanları: /home/claude/pd_work/<slug>/words.json  → [{"word","start","end"}], ilk/son öğeler "<start>"/"<end>" işaretçisi
- Kaynak/rakam notları (varsa): /home/claude/paranin-dili/videos/<slug>/kaynaklar.md
- İlk 4 saniye başlığı (2 satır, ≤6 kelime): görev mesajında

## Sabit kararlar (soru sorma)
- 1080x1920 dikey, 24 fps. Süre = kırpılmış seslendirme süresi + 0.4 sn.
- SES: Seslendirmenin başındaki sessizliği kırp: ilk gerçek kelimenin start'ından 0.05 sn önce başlat (ffmpeg -ss … ile voice_trim.wav üret), words.json zamanlarını da aynı miktarda kaydır. Ses hızı DEĞİŞMEZ. Render: --audio voice_trim.wav --audio-kind narration. Müzik/ses efekti ekleme (sonradan biz ekleyeceğiz).
- İLK 4 SANİYE KURALI (en önemli): Kare 1'de ekranda DEV başlık + hareket olmalı (boş kare, logo, yavaş fade-in YOK). Başlık stilin diline uygun çizilsin, ~2.2 sn'de çıkışla sahneye geçsin. 1.5–2 sn civarı görsel bir değişim/vuruş olsun. İlk sahne konunun en ilginç görselini/rakamını göstersin.
- ALTYAZI: AÇIK. words.json zamanlarıyla senkron, 2–4 kelimelik kısa gruplar, stile uygun ama okunaklı (telefon ekranında net). Altyazı y 1250–1420 bandında.
- GÜVENLİ ALAN: Tüm yazı/önemli öğe x 100–880, y 220–1440 içinde. Sağdaki 200 px'e yazı koyma (Instagram butonları). Alt 480 px'e önemli şey koyma.
- DİL: Ekrandaki TÜM yazılar Türkçe; İngilizce kelime yok (marka adları hariç). Türkçe karakterler (ş ğ ı İ ç ö ü) doğru görünmeli — font bunları desteklemeli; kontrol et. Fontlar: /home/claude/paranin-dili/kit/fonts/ttf/ (anton, inter-tight 900, dm-serif italic) ve sistem fontları (Inter, Noto). Ağdan font çekme.
- RAKAMLAR: Sadece script'teki/kaynaklar.md'deki rakamları kullan; uydurma veri, grafik değeri veya iddia ekleme. Her önemli iddia ekranda görsel olarak kanıtlansın (sayaç, karşılaştırma çubuğu, adım listesi vb.).
- MARKALAR: Logo kopyalama yok; ürünleri (Dyson, MacBook, Monster vb.) jenerik çizimle göster, adları düz yazıyla yazılabilir.
- Sondaki CTA cümlesinde ("Bunu, … arkadaşına gönder.") gönder/paylaş görseli olsun.
- three.js gerekirse proje klasöründe `npm install three` ile kur (npm registry açık). Başka ağ çağrısı yapma.

## Süreç
1. Proje klasörü: /home/claude/pd_work/anim/<tarih>/ (görevde verilir). project.json + storyboard + animation.html burada.
2. Önce --preview ile render et, previews/ PNG'lerine (açılış kare 1, ~1.5 sn, ~3 sn, %40, %90, son) Read ile bak, sorunları düzelt.
3. Final: node <skill>/scripts/render_video.mjs --html <abs>/animation.html --seconds <S> --width 1080 --height 1920 --fps 24 --output /home/claude/pd_work/anim/<tarih>/final.mp4 --audio <abs>/voice_trim.wav --audio-kind narration
4. ffprobe ile doğrula (h264, 1080x1920, süre, ses akışı). Dosya 90 MB'ı geçmemeli.
5. Disk dar (~4 GB boş, başka render'lar da çalışıyor): ara kare klasörlerini sakla­ma (--keep-frames kullanma), işin bitince node_modules hariç büyük ara dosyaları sil.

## Yapma
Git commit/push yapma, Metricool/sosyal medyaya dokunma, başka klasörlerdeki dosyaları değiştirme.

## Rapor (kısa)
final.mp4 yolu, ffprobe çıktısı (süre/boyut/codec/ses), 3 önizleme PNG yolu (kare 1, ~3 sn, orta), sahne listesi (1 satır/sahne), bilinen sınırlamalar.

## Ek notlar (6 Kas)
- Sunucunun yüzü (Ata) sonradan biz ekliyoruz (giriş ~0,9–3,8 sn, ortada bir vurgu cümlesi, kapanış CTA). Sana bir şey düşmüyor; animasyonu normal kur.
- Render: Disk dar ve CPU paylaşımlı. Kareleri diske yazmadan ffmpeg'e akıtan hazır örnek: /home/claude/pd_work/anim/2026-11-21/render_pipe.mjs (veya 2026-12-02/render_pipe.mjs — three.js/SwiftShader için). Gerekirse PLAYWRIGHT_MODULE_PATH=/opt/node-tools/node_modules/playwright-core. Uzun render'ı arka planda çalıştır ve bitmesini bekle (1 saati bulabilir).
- 3D stillerde (cgimotion, legostyle, zackdfilms): three.js'i proje klasörüne npm ile kur; 3D katmanı düşük çözünürlükte (ör. 540x960) çizip büyüt, yazı/altyazıyı 1080'de keskin çiz — 2026-12-02 (ps2) projesi örnek.
- Örnek tamamlanmış projeler (stil kalitesi referansı): /home/claude/pd_work/anim/2026-11-13 (comicart), 2026-11-17 (chalkboard), 2026-11-24 (pixelart).
