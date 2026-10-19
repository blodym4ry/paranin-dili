# RUNBOOK — Paranın Dili otomatik video üretimi

Bu dosya, Ata yokken zamanlanmış bir oturumun **tek bir videoyu baştan sona** üretip zamanlaması için talimattır.
Her oturum hafızasız başlar: sadece bu repo, `config.json`, `queue.md` ve `log.md` vardır. Sırayla uygula.
Ata'ya sorulacak kimse yok; karar gerekirse en makul yolu seç, `log.md`'ye yaz. Geri alınamaz bir risk varsa durdur.

## 0. Hazırlık
1. `bash setup.sh` → `SETUP_OK` görmelisin.
2. `git pull --rebase` (repo güncel olsun).
3. **Hangi slot?** Bugünden itibaren 2 gün sonraki ilk paylaşım günü (Pzt/Çar/Cum/Paz, 19:45 İstanbul).
   Metricool `getScheduledPosts` (blogId 7491089, timezone Europe/Istanbul) ile o güne bak.
   O gün zaten bir post varsa sonraki boş paylaşım gününü al. 7 gün içinde boş slot yoksa: log yaz, bitir.
4. **Kredi kontrolü:** `mcp__heygen__get_current_user`. Gerekli ≈ hedef süre(sn) × 1.05 + 10.
   Yetmiyorsa: videoyu üretme; `log.md`'ye "KREDİ YETERSİZ" yaz, push et, oturum sonunda bunu net söyle (bildirim gider). Bitir.

## 1. Konu
- `queue.md`'deki ilk `[ ]` konu. Konunun güncel verilerini web'den (WebSearch/WebFetch) doğrula: TÜİK, TCMB, resmi kurumlar, ana akım haber.
  Verisi doğrulanamayan konuyu atla (`[~] veri yok` işaretle), sıradakine geç.
- Profil dışı/deneme konusu ise Instagram tipi TRIAL_REEL, finans konusu ise REEL.

## 2. Senaryo (45–62 sn, ~150 kelime/dk → 115–150 kelime)
Yapı: **Hook (ilk 2 cümle) + kaliteli bilgi + tek CTA + hook'u yankılayan döngü cümlesi.**
- Her cümle ya veri, ya mekanizma, ya aksiyon taşır. Dolgu yok. Selam/giriş yok.
- 3 farklı hook yaz, `python3 tools/hookscore_tr.py hooks.txt` ile puanla; en yüksek ≥ 70 olmalı (değilse yeniden yaz).
- Sayıları **yazıyla** yaz (ör. "yüzde kırk dört", "yüz bin lira") — TTS telaffuzu için şart.
- Tahmin/garanti yok, yatırım tavsiyesi yok; "yaklaşık", tarih ve kaynak belirt.
- `python3 tools/beats.py script.txt --target 55` ile süre kontrolü.
- **Bağımsız inceleme:** Agent aracıyla taze bir alt-ajan aç; ona sadece senaryoyu + kaynak linklerini ver ve şu rubrikle PASS/FAIL iste:
  doğruluk (her rakam kaynağıyla tutuyor mu), abartı/garanti iddiası, hukuki risk, hook gücü, dolgu cümle, tek CTA, döngü cümlesi.
  FAIL ise düzelt, tekrar incelet. PASS olmadan HeyGen'e geçme.
- Klasör: `videos/<YYYY-MM-DD>-<kisa-slug>/` → `script.txt` (sadece konuşulacak metin), `kaynaklar.md`.

## 3. HeyGen
- Look: `config.json` → `look_rotation` sırasından, `log.md`'deki son kullanılan look'tan sonraki. Yasaklı look'ları asla kullanma.
- `mcp__heygen__create_video_from_avatar`: avatarId, script (tam metin), voiceId `53aac87758ba4784bfb3eb88ff0057df`,
  engine `{"type":"avatar_v","reference_look_id":"f0df07495ccc48c5a90c06390f547b4b"}`, aspectRatio `9:16`, resolution `1080p`,
  caption `{"file_format":"srt"}`, title = slug.
- `get_video` ile 30 sn arayla bekle (asla yeniden oluşturma). Tamamlanınca:
  `curl -sSLf -o $PD_WORK/<slug>/avatar.mp4 "<video_url>"` ve `curl -sSLf -o $PD_WORK/<slug>/avatar.srt "<subtitle_url>"`
  (`PD_WORK` varsayılan `~/pd_work`).

## 4. Hazırla + telaffuz
- `python3 engine/pv.py prep <slug>`
- `python3 engine/pv.py tel <slug>` → işaretli yerler. Çoğu rakam/kesme işareti biçim farkıdır, gerçek hata değildir.
  Gerçek hata şüphesinde o bölümü `--prompt` ile tekrar dinle. Anlamı bozan gerçek bir telaffuz hatası varsa ve kredi yetiyorsa
  sadece o cümleyi yeniden üretip ffmpeg ile ekle; yetmiyorsa log'a not düş ve devam et.

## 5. Kurgu (spec.py)
- Örnekler: `videos/ornek-mevduat/spec.py` (Gazete stili), `videos/ornek-indirim/spec.py` (Kinetik stili). Birini kopyala, yeni senaryoya göre yeniden yaz.
- **Stil rotasyonu:** her videoda farklı: Gazete (`CSS_FILE='gazete.css.html'`) ↔ Kinetik (varsayılan css) ↔ alt-avatar düzeni. Son kullanılanı `log.md`'den bak, aynısını üst üste kullanma. Sahne düzenlerini ve animasyonları her seferinde değiştir.
- **Avatar kuralları (Ata'nın isteği, kesin):**
  - Ata sadece giriş (hook), 1–2 vurgu anı, CTA ve kapanışta görünür. Diğer sahnelerde `AV['sX'] = None` → sadece grafik.
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
