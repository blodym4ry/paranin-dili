# RUNBOOK — Paranın Dili otomatik video üretimi

Bu dosya, Ata yokken zamanlanmış bir oturumun **tek bir videoyu baştan sona** üretip zamanlaması için talimattır.
Her oturum hafızasız başlar: sadece bu repo, `config.json`, `queue.md` ve `log.md` vardır. Sırayla uygula.
Ata'ya sorulacak kimse yok; karar gerekirse en makul yolu seç, `log.md`'ye yaz. Geri alınamaz bir risk varsa durdur.

## 0. Hazırlık
1. `bash setup.sh` → `SETUP_OK` görmelisin.
2. `git pull --rebase` (repo güncel olsun).
3. **Hangi slot?** Bugünden itibaren 2 gün sonraki ilk paylaşım günü (Pzt/Çar/Cum/Paz, 19:45 İstanbul).
   `config.json` → `auto_start_date` öncesindeki slotlar elle yönetilir: hesaplanan slot bu tarihten önceyse hiçbir şey üretme, log yazma, tek cümleyle bitir.
   Metricool `getScheduledPosts` (blogId 7491089, timezone Europe/Istanbul) ile o güne bak.
   O gün zaten bir post varsa sonraki boş paylaşım gününü al. 7 gün içinde boş slot yoksa: log yaz, bitir.
4. **Kredi kontrolü:** `mcp__heygen__get_current_user`. Gerekli ≈ 25 (seslendirme ~2–5 + avatar ~15–20; ayrık yöntem, §3).
   Yetmiyorsa: videoyu üretme; `log.md`'ye "KREDİ YETERSİZ" yaz, push et, oturum sonunda bunu net söyle (bildirim gider). Bitir.

## 1. Konu
- `queue.md`'deki ilk `[ ]` konu. Konunun güncel verilerini web'den (WebSearch/WebFetch) doğrula: TÜİK, TCMB, resmi kurumlar, ana akım haber.
  Verisi doğrulanamayan konuyu atla (`[~] veri yok` işaretle), sıradakine geç.
- Profil dışı/deneme konusu ise Instagram tipi TRIAL_REEL, finans konusu ise REEL.

## 2. Senaryo (45–62 sn, ~150 kelime/dk → 115–150 kelime)
**İskelet (sırayı bozma; kısa videoda blokları kısalt, bölüm atlama):**
| Bölüm | Süre | Görevi | Avatar? |
|---|---|---|---|
| 1. Kanca | 0–3 sn | Selamsız, ilk kelimeden konuya gir. Tek kişiye, net bir derde seslen. Somut rakam. Cevabı verme, merak boşluğu aç. | EVET |
| 2. Kilit | 3–8 sn | "Sonuna kadar izlersem ne kazanırım?" sorusunu tek cümleyle cevapla + yol haritası ("iki tuzak var, ikincisini kimse söylemiyor"). Kancayı tekrar etme, ilerlet. | evet (kancayla aynı parça) |
| 3. Blok 1 | ~10 sn | Tek fikir. Önce söyle, sonra rakam/örnekle göster. | hayır (grafik) |
| 4. Ara kanca 1 | 1 cümle | Sıradakini büyüt / beklentiyi ters çevir / soru sor / atlarsa kaybını söyle. | vurgu adayı |
| 5. Blok 2 | ~10 sn | Tek fikir, somut örnek. | hayır |
| 6. Ara kanca 2 | 1 cümle (isteğe bağlı) | Aynı teknik, farklı cümle. | vurgu adayı |
| 7. Blok 3 | ~8 sn (isteğe bağlı) | Uygulama: izleyicinin bugün yapacağı şey. | hayır |
| 8. Kapanış | 1 cümle | Kilitte verilen sözü teslim ettiğini tek cümlede özetle. | EVET |
| 9. CTA + döngü | son 3–5 sn | Tek eylem, değeri somut (ne kazanacak). Son cümle ilk cümleye bağlansın (döngü). Veda yok. | EVET |
Avatar parçaları (§3) doğal olarak: [Kanca+Kilit], 1–2 ara kancadan biri, [Kapanış+CTA].
Ara kancada görüntü de değişsin (yeni sahne düzeni, zoom, SFX) — söz ve görüntü birlikte "yeni bölüm" desin.

**Yazım kuralları:**
- Her cümle ya veri, ya mekanizma, ya aksiyon taşır. Dolgu ("aslında", "yani", "bu videoda") yok. Aynı fikri iki kez söyleme.
- Cümleleri "ama" ve "bu yüzden" ile bağla, "ve sonra" ile dizme. Bir cümle bir nefes; sesli okununca takılan cümleyi kısalt.
- Sayıları **yazıyla** yaz (ör. "yüzde kırk dört", "yüz bin lira") — TTS telaffuzu için şart.
- Tahmin/garanti yok, yatırım tavsiyesi yok; "yaklaşık", tarih ve kaynak belirt. Rakam uydurma.
- **CTA:** Ata yokken DM'den hediye gönderecek kimse yok → "yoruma KELİME yaz, DM'den göndereyim" türü CTA KULLANMA.
  Tek eylem seç: **kaydet** (varsayılan; "… öncesi kaydet" gibi bağlamlı) ya da tek soruluk yorum ("senin maaşın hangi dilimde? yaz").
- 3 farklı kanca yaz (farklı formüller: "X isen Y yapmayı bırak", "herkes X diyor, tersi doğru", "X yaşıyorsan sebebi Y", "N şey var, sonuncusunu kimse söylemiyor", "bunu bilseydim X kaybetmezdim"),
  `python3 tools/hookscore_tr.py hooks.txt` ile puanla; en yüksek ≥ 70 olmalı (değilse yeniden yaz).
- `python3 tools/beats.py script.txt --target 55` ile süre kontrolü.

**Bağımsız inceleme:** Agent aracıyla taze bir alt-ajan aç; ona sadece senaryoyu + kaynak linklerini ver, PASS/FAIL ve gerekçe iste. Rubrik:
1. Doğruluk: her rakam kaynağıyla birebir tutuyor mu; tarih var mı. 2. Abartı/garanti/yatırım tavsiyesi/hukuki risk yok.
3. İlk cümle selamsız konuya giriyor, kime konuşulduğu belli, merak boşluğu açık. 4. Kilit cümlesi sonunda ne kazanılacağını söylüyor.
5. Her blok tek fikir + örnek; bloklar arasında ara kanca var. 6. Tekrar eden fikir/dolgu kelime yok.
7. Kapanış tek cümle; tek CTA; DM/hediye vaadi yok. 8. Son cümle ilk cümleye bağlanıyor. 9. Süre 45–62 sn.
FAIL ise düzelt, tekrar incelet. PASS olmadan seslendirmeye geçme.
- Klasör: `videos/<YYYY-MM-DD>-<kisa-slug>/` → `script.txt` (sadece konuşulacak metin), `iskelet.md` (bölüm etiketli hali), `kaynaklar.md`.

## 3. Ses + avatar (AYRIK YÖNTEM — kredi tasarrufu, Ata'nın kesin kuralı)
Ata ekranda MÜMKÜN OLDUĞUNCA AZ görünür: giriş (hook), kapanış (CTA + döngü) ve ortada 1–2 kritik vurgu anı.
Toplam avatar süresi videonun %35'ini geçmez (hedef 15–20 sn). Geri kalan her şey sadece ses + grafik.
1. **Tam seslendirme:** `mcp__heygen__create_speech` text = script.txt'nin tamamı, voiceId `53aac87758ba4784bfb3eb88ff0057df`, language `tr`, **engine `heygen_voice`** (Ata bu sesi onayladı, 19 Ekim — motoru değiştirme), speed 1.
   Dönen `audio_url`'yi `curl -sSLf -o $PD_WORK/<slug>/speech.wav` ile indir; dönen `word_timestamps` listesini aynen
   `$PD_WORK/<slug>/words.json` olarak kaydet (`PD_WORK` varsayılan `~/pd_work`).
2. **Telaffuz:** `ffmpeg -y -i speech.wav -ac 2 -ar 48000 voice.wav` (WORK içinde) sonra `python3 engine/pv.py tel <slug>`.
   Çoğu işaret rakam/kesme işareti biçim farkıdır. Anlamı bozan gerçek hata varsa script'i düzelt (yazıyla/farklı kelime) ve sesi yeniden üret (ucuz).
3. **Cümleleri seç:** `python3 engine/split.py list <slug>` → numaralı cümleler. Avatar cümlelerini seç: ilk 1–2 (hook), son 1–2 (CTA+döngü),
   ortadan en fazla 2 vurgu cümlesi. `python3 engine/split.py cut <slug> 0,1,7,12,13` → `seg_XX.wav` parçaları, `voice.wav`, altyazı, `segments.json`.
   %35 uyarısı çıkarsa daha az cümle seç.
4. **Ses parçalarını yayınla:** `mkdir -p public/audio/<slug> && cp $PD_WORK/<slug>/seg_*.wav public/audio/<slug>/` → commit + push.
   URL: `https://raw.githubusercontent.com/blodym4ry/paranin-dili/main/public/audio/<slug>/seg_XX.wav` (`curl -sI` 200 olmalı).
5. **Kredi kontrolü:** gereken ≈ on-camera saniye + 5. `get_current_user` ile kontrol et; yetmiyorsa DUR (bkz. §0).
6. **Avatar klipleri:** her parça için `mcp__heygen__create_video_from_avatar`: avatarId (look rotasyonu, `config.json`), `audioUrl` = parça URL'si,
   engine `{"type":"avatar_v","reference_look_id":"f0df07495ccc48c5a90c06390f547b4b"}`, aspectRatio `9:16`, resolution `1080p`, title `<slug>-seg_XX`.
   Hepsini gönder, sonra `get_video` ile 30 sn arayla bekle (asla yeniden oluşturma). Bitenleri `curl -sSLf -o $PD_WORK/<slug>/seg_XX.mp4 "<video_url>"`.
   Look: `config.json` → `look_rotation` sırasından, `log.md`'deki son kullanılan look'tan sonraki; aynı videodaki tüm parçalar AYNI look. Yasaklı look'ları asla kullanma.
7. `python3 engine/split.py join <slug>` → `avatar_cut.mov` (avatar klipleri doğru saniyelerde). **`pv.py prep` ÇALIŞTIRMA** (ayrık yöntemde gerekmez).

## 4. (eski tam-avatar yöntemi — sadece ayrık yöntem çalışmazsa)
Tam script ile tek `create_video_from_avatar` (script + voiceId + caption srt), `avatar.mp4`/`avatar.srt` indir, `pv.py prep`, `pv.py tel`.
Bu yol 3 kat kredi harcar; kullanırsan log'a nedenini yaz.

## 5. Kurgu (spec.py)
- Örnekler: `videos/ornek-mevduat/spec.py` (Gazete stili), `videos/ornek-indirim/spec.py` (Kinetik stili). Birini kopyala, yeni senaryoya göre yeniden yaz.
- **Stil rotasyonu:** her videoda farklı: Gazete (`CSS_FILE='gazete.css.html'`) ↔ Kinetik (varsayılan css) ↔ alt-avatar düzeni. Son kullanılanı `log.md`'den bak, aynısını üst üste kullanma. Sahne düzenlerini ve animasyonları her seferinde değiştir.
- **Avatar kuralları (Ata'nın isteği, kesin):**
  - Ata sadece giriş (hook), 1–2 vurgu anı, CTA ve kapanışta görünür. Diğer sahnelerde `AV['sX'] = None` → sadece grafik.
  - Avatarlı sahne, bir avatar parçasının (segments.json) zaman aralığı İÇİNDE olmalı; sahne sınırlarını cümle başlarına koy (`A('ilk kelime') - .1`). `pv.py check` bunu denetler (AVATAR GUARD).
  - İlk sahne avatarsız da olabilir ama varsayılan: hook'ta Ata büyük pencerede.
  - Pencere oranı her zaman ~740:1040 (dikey). Saç ve çene ASLA kesilmez. Geniş/kare pencere yasak.
    Örn. büyük: `[250, 375, 580, 815, 6]`, köşe: `[700, 400, 320, 450, 6]`.
  - Avatarsız sahneler boşluk kalmasın diye içerik `translateY(170px)` ile ortalanabilir (EXTRA_CSS).
- Sahne içeriği sahne başlangıcından ≥0.4 sn sonra girsin. Her sahnede en az bir rakam/grafik.
- Altyazı kelimeleri: rakamlar `REPL` ile rakama çevrilir; vurgulu kelimeler `EM`, kırmızılar `RED`.
- `python3 engine/pv.py build <slug>` → `python3 engine/pv.py check <slug>`.
  CHECK PASS olmalı. Sonra snapshot contact-sheet görsellerini **Read ile açıp bak**: üst üste binme, taşma, kesik yüz, boş sahne, okunmayan yazı.
  Sorun varsa spec'i düzelt, build+check tekrar.

## 6. Render + QA
- `python3 engine/pv.py render <slug>` (~7–10 dk) → `public/<slug>.mp4`.
- `qa.jpg`'i Read ile aç, son kez kontrol et. Ses -14 LUFS civarı olmalı.

## 7. Yayın dosyası + zamanlama
- `git add public/<slug>.mp4 videos/<slug> && git commit -m "video: <slug>" && git push` (push başarısızsa `git pull --rebase` sonra tekrar).
- Medya URL: `https://raw.githubusercontent.com/blodym4ry/paranin-dili/main/public/<slug>.mp4` — `curl -sI` ile 200 olduğunu doğrula.
- Paylaşım metni (`videos/<slug>/paylasim.txt`): ilk satır hook + 📌 "kaydet" CTA; 3–5 kısa paragraf veri; "Kaynaklar: ..." ; "Yatırım tavsiyesi değildir."; 3–5 hashtag (#paranindili dahil). İlk yorum: tek soru. YouTube başlığı (#shorts ile), TikTok başlığı.
- **Kapak (seri görünümü, her videoda zorunlu):** `python3 engine/cover.py <slug> "<başlık, *kırmızı kelimeler* yıldızla>" "<KONU · AY YIL>" $PD_WORK/<slug>/seg_00.mp4 1.0`
  Başlık = kancanın en kısa hali (≤38 karakter, 2–3 satır), 1–2 kelimesi kırmızı. Çıktıyı Read ile aç: yüz net, göz açık, ağız kapalıya yakın kare seç (gerekirse saniyeyi değiştir).
  `public/covers/<slug>.jpg` → commit + push; URL `https://raw.githubusercontent.com/blodym4ry/paranin-dili/main/public/covers/<slug>.jpg`, post bilgisine `"videoThumbnailUrl"` olarak ekle.
- `createScheduledPost` (blogId `7491089`, date `<YYYY-MM-DD>T19:45:00+03:00`). Şablon `videos/ornek-mevduat/post_info.json`. Kurallar `config.json` → `rules`.
  "Failed to normalize media" gelirse 2 dk bekle ve bir kez tekrar dene.
- `getScheduledPosts` ile postun oluştuğunu doğrula.

## 8. Kayıt
- `queue.md`'de konuyu `[x] <tarih> <slug>` yap. `log.md`'ye satır ekle: tarih, slug, look, stil, süre, kredi, hook puanı, Metricool post id, notlar.
- commit + push. Oturumun son mesajında 2–3 cümlelik özet yaz (ne üretildi, ne zaman paylaşılacak, sorun varsa ne).

## Asla
- Videonun metadata'sını (C2PA dahil) silme/değiştirme. Ata'nın Instagram'ına giriş yapma, şifre isteme.
- Doğrulanmamış rakam kullanma. Rakip videolarını kopyalama (sadece formül).
- Aynı slota iki post. Kredi yetmiyorsa yarım video.
