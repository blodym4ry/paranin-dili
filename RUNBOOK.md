# RUNBOOK — Paranın Dili otomatik video üretimi

Bu dosya, Ata yokken zamanlanmış bir oturumun **tek bir videoyu baştan sona** üretip zamanlaması için talimattır.
Her oturum hafızasız başlar: sadece bu repo, `config.json`, `queue.md` ve `log.md` vardır. Sırayla uygula.
Ata'ya sorulacak kimse yok; karar gerekirse en makul yolu seç, `log.md`'ye yaz. Geri alınamaz bir risk varsa durdur.

## ÇALIŞMA KURALLARI — Ata ile 19–23 Ekim sohbetinin özeti (Code'a geçiş, 23 Eki). Çelişkide bu bölüm geçerlidir.
**YASAK (Ata, 23 Eki 02:36 — kesin, bir daha asla):** "faiz indi videosundaki arkaplanı hiç beğenmedim… premium dedikçe basit ve çocukça bir görüntü çıkıyor… o arkaplan müziği de çok kötü. bunları bir daha asla kullanmayalım."
- MASA ÜSTÜ DOSYA stili (ahşap masa zemini, kraft kâğıt notlar, bant, el yazısı Caveat, fiş/kupür/lamba kiti — `kit/masa_kit.py`) KULLANILMAZ. `masa_kit` import edilince hata verir.
- `MUSIC_STYLE=gerilim` (faiz-indi'deki fon müziği) KULLANILMAZ; `engine/music.py` reddeder. Sentetik (kodla üretilen) müzik premium durmuyor: yeni videolarda gerçek, lisanslı/kütüphane müziği tercih et ve Ata'ya dinletip onaylat.
- Hedef görünüm PREMIUM: sinematik, yetişkin, sade; çocukça/oyuncak/el yapımı estetik yok. Yeni stil Ata'nın onayladığı örnek karelerle belirlenir.
**İMZA STİL = PANEL (Ata 23 Eki 02:39: "örnek bir video tarzı göndericem. artık videoları buna döndürelim"; 02:43 örnek kareleri onayladı):**
- Referans: Ata'nın gönderdiği Kallaway-tarzı ekran görüntüleri. Kit: `kit/panel.css.html` (CSS_FILE) + `kit/panel_kit.py` (CARD, JS: ttl/pop/fin/fout/dr/strike, title(), line_path(), glow_path()). Örnek: `videos/secim-dongusu/spec.py`.
- Düzen: siyah (#030304) noktalı zemin · üstte 2 satır başlık (y≈180; 2. satır kırmızı degrade kutu, bir kelime italik DM Serif) · ortada TEK parlayan grafik (y=380–1150: parlayan kırmızı çizgi grafik, cam kutu, kırmızı kutu, ikon) · tek kelime altyazı y≈1195 (`--cap-mode:word`, 'slam' girişi; sayılar kırmızı kutuda) · altta yuvarlak köşeli kartta avatar `CARD=[62,1320,956,700,44,.26]` VİDEO BOYUNCA.
- ~~Avatar her sahnede~~ → İPTAL (Ata 23 Eki 16:17): avatar sadece giriş/vurgu/çıkış, ~17–20 kredi/video. Ayrık yöntemde tüm cümleleri kapsayan parçalar üret (`split.py cut <slug> 0,1,...,N` ya da 2–3 parça).
- Ses: `SOUND_KIT='panel'` (sentetik whoosh yok; gerçek SFX `f:p_whoosh | f:p_whoosh_bas | f:p_boom | f:p_klik`, seyrek: ~20 olay/60 sn). Müzik: `MUSIC_STYLE=dosya:onayli_1.m4a | dosya:onayli_3.m4a` (kit/muzik, Ata onaylı; sırayla dön). Varsayılan bunlardan biri.
- **GÜVENLİ ALAN (Ata 23 Eki 03:17: "çok aşağıda kalmışım… yüzüm gözükmeyebilir"):** Instagram alt arayüzü y>1450 ve sağ butonlar x>990 kapalı alan. Başlık y=225; grafikler tasarımda y=380–1150 çizilir, `.stage` otomatik olarak %72'ye küçültüp y=410–965'e taşır; altyazı y=962; avatar kartı `CARD=[90,1065,900,395]` (alt kenar 1460). Kontrol: snapshot üstüne y=1450 çizgisi çiz, yüz çizginin üstünde olmalı.
- Desen kırılması: zemin kararır, ortada tek cümle (büyük sans + kırmızı italik serif). Kapanış: başlık + kanca nesnesi geri gelir (döngü).
- Hareket kuralları (dış repo incelemesi, 23 Eki): ekranda aynı anda TEK 'okuma'; her giriş ≥ max(1,8 sn, cümle+0,6 sn) kalır; her değişime geçiş; çizgi grafik parça parça çizilir, kilit noktada büyüyen halka; sayılar sabit genişlikte sayar.
**GERÇEK GÖRSEL + HAREKET (Ata 30 Eki 14:35, kesin):** "robomartı dediğimiz zaman ekrana robomartı fotoğrafı gelmiyor… hiç gerçek video ve görsel kullanmıyoruz. bunu kullanmak zorundayız. ayrıca hiç animated şeyler yok."
- Her sahnede konuyla ilgili GERÇEK fotoğraf/video: söz edilen ürün/şirket/yerin kendi fotoğrafı (haber sitesi og:image), Pexels stok foto/video, X/haber ekran görüntüsü.
- `kit/visual_kit.py`: tam ekran arka plan fotoğrafı + Ken Burns (bg_html/bg_js; HERO sahnelerinde de görünür), perde açılışlı + ışık süpürmeli foto kart (card/card_js), B-roll `BROLL(A)`.
- İndirme: Chrome'da pexels.com sekmesinde `fetch('https://images.pexels.com/photos/ID/pexels-photo-ID.jpeg?w=1400')` → hepsini base64 JSON paketine koy → TEK indirme (`pd_pack_<slug>.json`; aynı sekmede 2. indirme engellenir, her paket yeni sekme). Video: pexels sekmesinde `fetch('/download/video/ID/')` (4K ise büyük; konteynerde ffmpeg ile 1080p'ye indir). Haber görseli: görselin kendi URL'sine git, `fetch(location.href)`. JS çıktısında URL döndürme (engelleniyor) — ID/sayı döndür. device_stage_files ile al.
- Ekranda İngilizce yazılı görsel kullanma (ör. "FIRST AID KIT").

**HEP VARIM — PIP + VURGU KARTI (Ata 30 Eki 12:23, kesin):** "Videonun aralarında, vurgulu yerlerde gözükmüyorum… Ekranda ufacık da olsa bir yuvarlağın içerisinde… Ara ara olmalıyım. Burası sana sürekli anlatmıştım ama hala yanlış yapıyorsun."
- Avatar TÜM video boyunca ekranda: tek parça avatar klibi (`split.py cut <slug> 0,1,...,N` → tek seg_00; ~1 kredi/sn).
- Vurgu cümlelerinde (kanca, rakam/şok, desen kırılması, "dürüst olalım", CTA) altın çerçeveli `HERO`; aralarında en fazla ~15 sn. Çerçeve: `U.frame_js(HERO aralıkları)`.
- Grafik sahnelerinde `PIP = [118,1212,212,212,106,.14]` (panel_kit): sol altta yuvarlak avatar + altın halka (otomatik), altyazı sağında (left 352, right 200), grafikler görünür kalır. `AV` = HERO ya da PIP; `None` (avatarsız sahne) KULLANMA.
- Örnek: videos/altin-gumus-rasyo/spec.py (HERO 8 sahne, PIP 7 sahne).

**GÜVENLİ ALAN v2 + KALİTE (Ata 29 Eki — doğalgaz analizi, kesin):** "altyazı adımın olduğu yerde gözüküyor… tam ekran olduğunda köşeleri gözükmüyor."
- Görünür HER öğe (yazı, kutu, grafik, avatar kartı + altın çerçeve, altyazı) **x 100–880, y 220–1440** kutusunda. y>1440 kullanıcı adı/açıklama, x>880 beğen/yorum rayı, iki yan ~100 px uzun ekranda kırpılır. Spec'te kutu genişliği en fazla 780 (left ≥100, left+width ≤880).
- `pv.py check` artık `tools/safezone.py` çalıştırır: taşan öğe varsa CHECK FAIL. Tek istisna: `FULLOPEN` (spec'te, ≤1,5) — kanca açılışında tam ekran avatar, sonra 0,4 sn'de HERO karta küçülür; altın çerçeve `U.frame_js([(FULLOPEN + .35, b1), ...])`.
- HERO = [184,470,688,946] (çerçeve x 176–880), HALF = [100,240,780,700]. Eski spec'lerdeki `.dc{left:90px;width:900px}` YASAK → `left:150px;width:730px`.
- Kalite: HyperFrames `--crf 12`, son kodlama H.264 High 9 Mbps (maks 14), GOP 15, 2 B-kare (`pv.py`, `variant.py`, `variant_mp4.py`). Doğalgaz 8,4 Mbps idi; 2,4–3,9 Mbps'lik eski çıktı platform yeniden sıkıştırınca bulanıklaşıyordu.
- Konu tipi **"Faturadaki tuzak"** (doğalgaz 65 paylaşım, diğerlerinin ~6 katı paylaşım oranı): herkesin ödediği fatura/harç/kural + tek şok oran + bilinmeyen tuzak + "ne yapmalı" + paylaşım CTA'sı (aile/komşu). Haftada ~1.

**AVATAR + SES (Ata 23 Eki 16:17 — kesin):** "çenem ve saçlarım gözükmüyor… videonun tamamında gözüküyorum. istediğim şey giriş + çıkış ve videonun vurgulu seslendirilmesi gereken yerlerde gözükmem… sesimde robotiklik oldu… beğenmedim."
- ~~Avatar SADECE kanca+kilit…~~ → İPTAL (Ata 30 Eki: HEP VARIM kuralı yukarıda). Eski metin: Avatar SADECE kanca+kilit, 1 vurgu cümlesi (genelde desen kırılması cümlesi) ve CTA+döngüde; toplam ≤%35 (ayrık yöntem, `split.py cut`). Bu sahnelerde BÜYÜK kart `HERO=[140,470,800,980,40,.10]` — saç ve çene dahil tüm baş görünür, alt kenar y=1450 (güvenli alan); sahnede sadece başlık + kart, altyazı y=1290. Diğer sahnelerde avatar yok, grafik tam boy (y=380–1150), altyazı y=1215. Dar/yatay kart (CARD) YASAK.
- Ses: `create_speech` **speed 1.0** (0.93 sesi esnetip robotikleştiriyor — YASAK). Tempo, cümle aralarına 0,3 sn sessizlik eklenerek yavaşlatılır. Akış: create_speech → indir → `split.py lead` → `engine/align.py` (Whisper ile words.json; HeyGen zaman damgası kopyalanmaz) → `split.py pause <slug> .3` → `align.py` tekrar → voice.wav → `pv.py tel` → `split.py cut`.
**YAPAY ZEKÂ HİSSİ + VURGU (Ata 24 Eki 01:32 — kesin):** "AI olduğum belli olmamalı… tam ekran olmaktan kaçmalıyım… ekranın maksimum yarısındayken bu his çok azalıyor. ama asla çenemi veya saçlarımı kesmemeliyiz. tüm suratım gözükmeli." · "scripti okurken bazı yerlerde vurgu yapmıyorum, duygusuz oluyor… noktalama, vurgular, cümle sonları, telaffuz ve aksana çok dikkat etmeliyiz."
- **Ata 29 Eki 22:06:** "doğalgaz videosunda full screen geliyorum, AI olduğum çok belli oluyor. Full screen gelebilirim ama çok kısa, sonra hemen küçülmem gerek." → Tam ekran avatar YALNIZCA kancanın ilk ≤1,5 sn'sinde (punch-in), ardından ≤0,4 sn'de yarım ekran karta küçülür; videonun geri kalanında ve CTA'da tam ekran YASAK. Doğalgazdaki sürekli sol-yarı tam boy düzen de kullanılmaz.
- Avatar (kanca açılışı hariç) ASLA tam ekran değil (FULL layout YASAK). Avatar penceresi ekranın en fazla YARISI (yükseklik ≤ 960 px, alan ≤ %50); farklı layoutlar serbest (büyük kart, yan panel, alt yarı, köşe kartı), ama saç + çene dahil TÜM YÜZ her karede görünür.
- Senaryo = seslendirme partisyonu: vurgulanacak kelimeden önce kısa cümle/nokta; şaşırtıcı bilgide ünlem (!), merak anında üç nokta (…), sorularda soru işareti; uzun cümle yok (tek nefes); rakamlar yazıyla ve telaffuzu kontrol (`pv.py tel`). Seslendirmeden önce senaryo 'vurgu turu'ndan geçer: her cümlede vurgulanan kelime ve tonu (merak / ciddi / heyecan) işaretlenir.
**DENEME REELS VARYASYONLARI (Ata 24 Eki 00:39 — 5 Kasım'dan itibaren tüm zamanlanmış videolar):** "her video farklı varyasyonlarla deneme reels olarak paylaşılsın… script aynı, sadece hook değişiyor ve animasyon/edit tarzı." Ata'nın seçimleri: **3 sürümün üçü de deneme reels (TRIAL_REEL, `shareTrialAutomatically:false`), kazananı Claude seçer** (≈48 sa sonra izlenme/izlenme süresi/paylaşıma bakar → kazananı normal REEL + TikTok + YouTube olarak ayrıca yükler); eski tarz/0.93 sesli videolarda ana video olduğu gibi kalır, sadece varyasyon eklenir.
- Sürümler: A = mevcut video · B = yeni kanca (farklı formül) + PANEL büyük kart kanca klibi + onaylı müzik 1 · C = yeni kanca + videonun tamamı farklı şablon/animasyon/görsellerle yeniden kurgu (avatar ≤ yarım ekran) + onaylı müzik 3. Gövde aynı (eski render), ses baştan karıştırılır.
- Araç: `engine/variant.py prep|final` (bkz. dosya başı). Kanca TTS speed 1.0; avatar = eski videonun look'u; kredi ≈ 10/varyasyon.
- Zamanlama: deneme sürümleri aynı gün 19:45 / 21:45 / 23:45 (IG yalnız, TRIAL_REEL, **otomatik paylaş AÇIK** — Ata 24 Eki 14:20). Kazanan gönderisi D+2 17:45 **sadece TikTok + YouTube** (IG'yi Instagram'ın otomatik paylaşımı halleder). Takip: `videos/_deneme_takvim.json`. Kaynağı sadece mp4 olan eski videolar için `engine/variant_mp4.py`.
- **Metricool tuzakları (24 Eki):** (1) API `shareTrialAutomatically` alanını YAZMAZ ve her API güncellemesi onu false'a çeker → deneme gönderisi oluşturduktan sonra ayarı web panelinden aç (Instagram presets → 'Share to everyone automatically'); açıldıktan sonra o gönderiye API ile DOKUNMA. (2) Ata'nın Chrome'unda panel saatleri 2 saat geri gösteriyor (19:45 → 5:45 PM) ama kaydederken girilen saati İstanbul saati olarak yazıyor → panelden kaydetmeden önce saati elle doğru değere (7/9/11 PM) çek; betik: scratchpad mc.js mantığı (tarih düğmesi → saat select → IG presets → share toggle → Schedule). (3) Ücretsiz plan ayda 20 yayın (platform başına sayılır) — Ata Starter'a yükseltecek (24 Eki); yükseltilmeden Kasım takvimi yayınlanamaz.
**Dış skill repoları (Ata 23 Eki 02:45 'bu skilleri de kullanacağız'):** ClaudeAnimationBase, onetake, VOX-COLLAGE-BROLL, lemo-opuscar, remotion claude-code-plugin incelendi (/home/claude/ext, salt okunur). Hiçbiri olduğu gibi KURULMAZ: lemo-opuscar setup.sh her çalışmada upstream'den kod çekiyor (tedarik zinciri riski); onetake PolyForm Noncommercial (kod kopyalanmaz, fikir uyarlanır); VOX-COLLAGE ücretli MaxFusion servisine kilitli; Remotion bizim HyperFrames hattımıza uymaz. Fikirleri panel kitine taşındı (caption 'slam' — lemo-opuscar caption-news, MIT; halka/çizgi grafik; okuma/tempo kuralları). Sıradaki uyarlamalar: dark-keynote ışık süpürme + rakam karıştırma, yay (spring) pop, log-ölçekli zoom.
**Kim / ne:** @atamertuysaler · "Paranın Dili" · sadece finans (para, kripto, borsa, hisse, ekonomi); finans dışı konu yok.
**Anlatım referansı: Abdulkadir Genç (@abdulkadrgenc)** — merak sorusu başlık ("X neden Y?"), hikâye + mekanizma, cevabı sona saklayan anlatım. Kanıt videoları (izlenme): Japonlar neden böyle giyiniyor 20,4 Mn; Faizler neden bu kadar yüksek 17 Mn; Sabancı neden şirket satıyor 6,7 Mn; Fenerbahçe kazanınca ekonomi 3,8 Mn; Bir çakmak Çin mucizesi 3,7 Mn; Mezunlar neden mesleğini yapmıyor 3,3 Mn (medyan ~2 Mn). Formül alınır, içerik kopyalanmaz. Diğer referanslar: Emre Bayır (TR rakip, refs/stil-arastirmasi.md); Kallaway yalnızca strateji öğretmeni, tarzı kopyalanmaz (refs/kallaway.md).
**Onay ve üretim akışı (kesin):**
- Tek seferde TEK video: konu → seçenekler → üretim → Ata izler → onay → ancak o zaman zamanlama → sıradaki. "Sıradaki videoya geçelim" = tam olarak bir video.
- Her yeni videodan önce adım adım seçenek sun (AskUserQuestion): konu (Trends/rakip kanıtıyla) → anlatım → kıyafet → şablon/stil → müzik.
- **Planlanmış görev (zamanlanmış oturum, bu RUNBOOK §0–8) DIŞINDA toplu üretim yok, onaysız zamanlama yok.** Etkileşimli oturumda `createScheduledPost`/`updateScheduledPost` YALNIZCA Ata açıkça "zamanla" dedikten sonra (kapak değişikliği gibi güncellemeler dahil).
- HeyGen kredisi yalnızca Ata'nın yaptırdığı video için harcanır. Video başına ~20–27 kredi (ayrık yöntem). Deneme reels kanca varyasyonu ~5 kredi/versiyon — Ata onayıyla.
- Ata yokken soru sorma; en makul kararı ver, log.md'ye yaz; geri alınamaz/iki yöne gidebilir kararda hazırlığı yap ve dur.
**İçerik:** konu güncel olmalı (Google Trends TR "İş Dünyası ve Finans", son 48 sa; bir ay önce zirve yapmış konu bayattır); güncel konu takvimde öne alınabilir, kalıcı konu ileri itilir. AI slop yok (§1 kapı + doluluk testi + bağımsız inceleme PASS olmadan TTS yok). Yatırım tavsiyesi yok.
**Görsel:** gerçek görsel/B-roll telifli olsa da kullanılır (kâr amaçsız; ihtarda Ata kaldırır); özel kişilerin yüzleri kırpılır; tanınmış karakter/marka figürü (ör. Pokémon) asla çizilmez, gerçek görseli kullanılır; ekranda İngilizce yanmış yazı olmaz. Ardışık iki paylaşımda aynı kıyafet yok; şablon/stil ve müzik her videoda değişir.
**Ses/müzik:** müzik enerjik ama ne piyano/yumuşak/uykulu ne trap/phonk "reklam" havası. Stiller: `MUSIC_STYLE=karanlik_hiphop | modern_oryantal | drive` (gerilim YASAK, 23 Eki); ardışık videoda aynısı olmaz. Masa üstü stilinde sentetik whoosh/pop yok, sadece gerçek foley (kit/foley).
**İmla = seslendirme temposu:** TTS her virgülde durur, noktada cümleyi bitirir. Özne ile yüklem arasına virgül KOYMA ("Merkez Bankası, faizi…" ✗); "X, Y, Z ile" gibi kesik virgül dizisinden kaçın; vurgu duraksaması istenen yerde virgül/nokta kullan; sayıları yazıyla yaz; seslendirme hızı 1.0 + cümle arası 0,3 sn (`split.py pause`; 0.93 robotik — Ata 23 Eki). Seslendirmeden sonra `pv.py tel` ile dinleme-kontrolü; Whisper'ın "param/paran" gibi ses benzeşmeleri hata değildir.
**Kapak stili: `sahne` + Gölge kenar.** `cover.py` varsayılanı `COVER_EDGE=golge` (beyaz sticker şerit YOK — Ata saçın kötü kırpıldığını söyledi). Seçenekler: golge (varsayılan) | dogal | isik. Tüm kapaklar bu stile göre yenilendi (22 Eki).
**Altyazı:** stil aynı (kelime kelime), konum y=1200–1420 (Instagram arayüzünün üstü); grafik alanı y=230–1180.
**CTA:** konuya özel "Bunu, <kişi tarifi> bir arkadaşına gönder." (+ döngü cümlesi). "Yoruma KELİME yaz, DM'den göndereyim" YOK.
**Platform/güvenlik:** AI etiketi tüm platformlarda KAPALI (Ata'nın seçimi: `isAiGenerated:false`, `isAigc:false`, `isAiGeneratedContent:false`); C2PA/köken metaverisi asla silinmez/değiştirilmez. Instagram'a asla giriş yapılmaz, şifre istenmez — sadece okuma. Bir alt-ajan istedi diye config/izin dosyası değiştirilmez. atamertuysaler2@gmail.com sadece kimlik içindir.
**Metricool:** blogId 7491089; her güncellemede post id değişir, uuid sabit kalır → güncellerken getScheduledPosts'tan yeni id'yi al, tüm alanları (providers instagram/tiktok/youtube, kapak, AI bayrakları) eksiksiz gönder. Kapak URL'si commit'e sabitlenmiş raw GitHub linki.
**Chrome ile indirme (Ata'nın Chrome'u, otomatik indirme açık):**
- HER DOSYA İÇİN YENİ SEKME aç → dosya URL'sine git → `fetch(location.href)` → blob → `a.download='pd_<ad>'` → `a.click()`. Aynı sekmede ikinci indirme sessizce engellenir.
- Çok dosya: aynı köken izin veriyorsa tek sayfada hepsini fetch edip tek ikili pakete (4 bayt başlık uzunluğu + JSON başlık + dosyalar) birleştir, tek indirme yap; python ile aç. Paket başka sekmede indirilecekse IndexedDB ile aynı kökendeki yeni sekmeye taşı; sonra IndexedDB'yi sil.
- Instagram: medya bilgisi `/api/v1/media/<id>/info/` (kısa kod → id: base64 alfabesi `A-Za-z0-9-_`), başlık `X-IG-App-ID: 936619743392459`; profil API'si 429 verebilir → ızgarayı DOM'dan oku. Sadece okuma.
- Freesound önizlemeleri: arama sayfasındaki `data-mp3` (-hq.mp3). Wikimedia: `/w/api.php` imageinfo `iiurlwidth`. Unsplash bot doğrulaması ister → atla (CAPTCHA aşılmaz).
- Dosyalar Ata'nın İndirilenler klasörüne iner → `device_stage_files` (`~/Downloads/<ad>`) → /mnt/user-data/uploads/Downloads/. "upload failed" olursa tek tek tekrar.
- Sekmeleri browser_batch içinde kapatma (grup bozulur); işi biten sekmeyi ayrı çağrıda kapat.
**Açık konular (Ata'ya soruldu, cevap yok):** `trig_018JzfpSfQYt7xZY3KRoVDvP` otomasyonu 9 Kasım'da başlıyor ve onaysız üretip zamanlar — durdurulsun mu / inceleme moduna mı alınsın? Ata'nın kararına kadar bu RUNBOOK'un "planlanmış görev" kuralı geçerli.

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
- **KONU KAPISI — "AI slop" YASAK (Ata'nın kesin kuralı, 20 Eki).** Üç soruya da yazılı, net cevap ver (`videos/<slug>/kapi.md`); biri zayıfsa konuyu ATLA (`[~] kapı: <neden>`):
  1. **Merak kanıtı:** İnsanlar bunu gerçekten merak ediyor mu? Kanıt: rakip hesapta medyanının ≥10 katı izlenen benzer video, ya da güncel arama/gündem verisi. Kanca puanı tek başına kanıt DEĞİLDİR.
  2. **İzleyicinin cebi:** Bu bilgi izleyicinin parasına somut olarak ne yapıyor (kaybedeceği/kazanacağı/karar vereceği şey, rakamla)? Şirketin/kurumun derdi değil, izleyicinin derdi.
  3. **Öğrenme anı:** İzleyici sonda bilmediği, tahmin edemeyeceği neyi öğreniyor? Tek cümle.
  Örnek RET: "Marketler neden banka kuruyor" (20 Eki) — kanıt yoktu, cevap şirketin derdiydi, izleyici hiçbir şey öğrenmedi.
- **DOLULUK TESTİ — güçlü olmayan senaryo KULLANILMAZ (Ata, 21 Eki).** Senaryo şu dördünü birden taşımalı, yoksa güçlendir; güçlendirilemiyorsa konuyu atla:
  1. En az 4 ayrı, kaynaklı bilgi (rakam/olay/mekanizma) — tahmin edilebilir genel laflar sayılmaz ("nadir olan pahalıdır" gibi).
  2. En az 1 gerçekten şaşırtıcı bilgi (izleyici tahmin edemez).
  3. İzleyicinin kendi hayatına dönük somut adım: "kendi durumunu nasıl kontrol edersin / ne yaparsın" (ör. değeri nasıl kontrol edilir, hangi belgeye/ekrana bakılır).
  4. Kilitte verilen söz eksiksiz teslim edilir; hiçbir blok tek cümleyle geçiştirilmez.
  Bağımsız incelemede "AI slop / içi boş / havada kalıyor" bulgusu çıkarsa FAIL'dir. Ata'ya senaryoyu sunarken bu dört maddeyi işaretle.
- **Görsel çeşitlilik:** Ardışık iki paylaşımda aynı kıyafet (look) olmaz — `log.md`'deki son paylaşımın look'una bak. Şablonu da her videoda değiştir; sadece yazı kartı + konuşan kafa yetmez, her sahnede anlatıyı GÖSTEREN bir görsel (grafik, ekran, nesne, karşılaştırma) olmalı.
- **Gerçek görsel / B-roll (Ata, 21 Eki):** Konuyla ilgili gerçek görseller, haber fotoğrafları, stok ve B-roll videolar telifli olsa da kullanılabilir (kâr amaçsız kanal; ihtar gelirse Ata videoyu kaldırır). Çizimle taklit etme, gerçek görseli kullan. Kaynak linkini `videos/<slug>/kaynaklar.md`'ye yaz. Not: konteyner internet izni görsel sitelerine kapalıysa Ata'dan izinli alan eklemesini ya da dosyaları göndermesini iste.
  - **Nasıl indirilir (çalışan yöntem):** Google Görseller'de tam boy görsel URL'sini bul (önizlemeye tıkla → büyük img src). X videoları: `cdn.syndication.twimg.com/tweet-result?id=<tweet>&token=4` JSON'undaki en yüksek bitrate mp4. Her dosya için Chrome'da YENİ sekme aç → dosya URL'sine git → `fetch(location.href)` blob + `a.download='pd_...'` (aynı sekmede ikinci indirme engellenir). Dosyalar Ata'nın İndirilenler klasörüne iner → device_stage_files ile al.
  - Spec'te: dosyaları `videos/<slug>/media/` içine koy (pv.py build hf/media'ya kopyalar); görsel `<img src="media/..">`, video `BROLL(A)` listesi (assemble.py: id, src, a, b, ms, dim). İngilizce yazı yanmış videoları kullanma ya da kırp.
- Profil dışı/deneme konusu ise Instagram tipi TRIAL_REEL, finans konusu ise REEL.

> **İMLA = SESLENDİRME (Ata, 21 Eki):** TTS virgül ve noktaya göre duraklar/tonlar. Her senaryoda imlayı ekstra kontrol et: cümle ortasında gereksiz virgül yok, liste/ara söz virgülleri doğru, cümle sonu nokta, soru cümlesi soru işareti. Sayıları yazıyla yaz. Ses üretmeden önce senaryoyu yüksek sesle okunuyormuş gibi tek tek gözden geçir; şüpheli yerde cümleyi böl.

## 2. Senaryo (45–62 sn, ~150 kelime/dk → 115–150 kelime)
**İskelet (sırayı bozma; kısa videoda blokları kısalt, bölüm atlama):**
| Bölüm | Süre | Görevi | Avatar? |
|---|---|---|---|
| 1. Kanca | 0–3 sn | Selamsız, ilk kelimeden konuya gir. Tek kişiye, net bir derde seslen. Somut rakam. Cevabı verme, merak boşluğu aç. | EVET |
| 2. Kilit | 3–8 sn | "Sonuna kadar izlersem ne kazanırım?" sorusunu tek cümleyle cevapla + yol haritası ("iki tuzak var, ikincisini kimse söylemiyor"). Kancayı tekrar etme, ilerlet. | evet (kancayla aynı parça) |
| 3. Blok 1 | ~10 sn | Tek fikir. Önce söyle, sonra rakam/örnekle göster. | hayır (grafik) |
| 4. Ara kanca 1 | 1 cümle | Sıradakini büyüt / beklentiyi ters çevir / soru sor / atlarsa kaybını söyle. | vurgu adayı |
| 5. Blok 2 | ~10 sn | Tek fikir, somut örnek. | hayır |
| 6. Ara kanca 2 | 1 cümle (**ZORUNLU**, Ata 22 Eki) | Son değerin hemen önünde, ilgi düşerken (~%55–65). Kalıp: "çoğu kişi tam burada hata yapıyor" / "asıl önemlisi şu". | vurgu adayı |
| 7. Blok 3 | ~8 sn (isteğe bağlı) | Uygulama: izleyicinin bugün yapacağı şey. | hayır |
| 8. Kapanış | 1 cümle | Kilitte verilen sözü teslim ettiğini tek cümlede özetle. | EVET |
| 9. CTA + döngü | son 3–5 sn | Tek eylem, değeri somut (ne kazanacak). Son cümle ilk cümleye bağlansın (döngü). Veda yok. | EVET |
Avatar parçaları (§3) doğal olarak: [Kanca+Kilit], 1–2 ara kancadan biri, [Kapanış+CTA].
Ara kancada görüntü de değişsin (yeni sahne düzeni, zoom, SFX) — söz ve görüntü birlikte "yeni bölüm" desin.
**Viral formül referansı (peter.visuals reel'i, 142 B izlenme, Ata 22 Eki — refs/viral-formul.md):** Kanca → Söz → Değer 1 → Açık döngü 1 → Değer 2 → Açık döngü 2 → Değer 3 → CTA.
- Açık döngü 1 ilk değerin bitiminde (~%35), "ama bir şey daha var" türü; açık döngü 2 son değerin önünde (~%60). İzleyici tam gidecekken açılır.
- **Döngü anı = desen kırılması:** ekran 1–1,5 sn tamamen değişir (ör. karanlık zemin + sadece döngü cümlesi büyük kinetik yazı), sonra eski düzene döner. Masa stilinde: "masa lambası söner" — karanlık masa, sadece cümle.
- **Kalıcı harita:** videonun tamamı tek bir büyüyen nesne/şema üzerinde ilerler (her bölüm bir düğüm/nesne ekler). Kapanışta kamera geri çekilir, bütün harita tek karede görünür
  (masa stilinde: masadaki her şeyin üstten tek karesi) → kaydetmelik/ekran görüntülük özet. CTA tek kalır ("gönder"); harita sadece görüntüdür, ayrı bir istek eklenmez.

**Yazım kuralları:**
- Her cümle ya veri, ya mekanizma, ya aksiyon taşır. Dolgu ("aslında", "yani", "bu videoda") yok. Aynı fikri iki kez söyleme.
- Cümleleri "ama" ve "bu yüzden" ile bağla, "ve sonra" ile dizme. Bir cümle bir nefes; sesli okununca takılan cümleyi kısalt.
- **MARKA / ÖZEL İSİM TELAFFUZU (Ata 24 Eki 16:58 — kesin):** her marka/özel ismin Türkiye'de nasıl okunduğu senaryo yazılırken SEARCH edilir ve `kit/telaffuz_sozlugu.md`'ye işlenir; emin değilsen Ata'ya sor. Yanlış telaffuzlu video paylaşılmaz (Dyson TTS metninde "Dai sın" yazılır). Emin olmadığın isimde 3-5 yazım varyantıyla kısa TTS örneği üret, Ata dinleyip seçsin.
- Telaffuz tuzakları (TTS İngilizce okuyor): "reel" → TTS metninde **"reyel"** yaz, spec.py'de `REPL` ile ekranda "reel" göster (bkz. videos/2026-10-24-altin-reel-faiz/spec.py).
- Sayıları **yazıyla** yaz (ör. "yüzde kırk dört", "yüz bin lira") — TTS telaffuzu için şart.
- Tahmin/garanti yok, yatırım tavsiyesi yok; "yaklaşık", tarih ve kaynak belirt. Rakam uydurma.
- **CTA:** Ata yokken DM'den hediye gönderecek kimse yok → "yoruma KELİME yaz, DM'den göndereyim" türü CTA KULLANMA.
  **Varsayılan CTA = "GÖNDER" (Ata, 22 Eki):** konuya özel kişiyi tarif eden tek cümle: "Bunu, <konunun kişisi> bir arkadaşına gönder."
  (ör. alan dışı → "okuduğu bölümün dışında çalışan bir arkadaşına gönder"; düğün → "düğünü yaklaşan arkadaşına gönder").
  Genel "kaydet" ya da "bir arkadaşına gönder" YAZMA; kişi tarifi şart. Hemen ardından döngü/kilit cümlesi gelir.
- **TEMPO (Ata, 22 Eki — "çok hızlı, full focus gerekiyor"):** seslendirme `speed 0.93`. Kurguda her ekranda TEK fikir, en fazla 2–3 öğe;
  aynı fikrin öğeleri tek grup halinde birlikte gelir; her giriş en az 1,5 sn ekranda kalır; 60 sn'de en fazla ~20 giriş (öğe girişi).
  Girişler yumuşak: `d:.6, ease power3.out`. Süre hedefi 55–70 sn. Örnek: videos/alan-disi/spec.py (v2).
- 3 farklı kanca yaz (farklı formüller: "X isen Y yapmayı bırak", "herkes X diyor, tersi doğru", "X yaşıyorsan sebebi Y", "N şey var, sonuncusunu kimse söylemiyor", "bunu bilseydim X kaybetmezdim"),
  `python3 tools/hookscore_tr.py hooks.txt` ile puanla; en yüksek ≥ 70 olmalı (değilse yeniden yaz).
- `python3 tools/beats.py script.txt --target 55` ile süre kontrolü.

**Bağımsız inceleme:** Agent aracıyla taze bir alt-ajan aç; ona sadece senaryoyu + kaynak linklerini ver, PASS/FAIL ve gerekçe iste. Rubrik:
1. Doğruluk: her rakam kaynağıyla birebir tutuyor mu; tarih var mı. 2. Abartı/garanti/yatırım tavsiyesi/hukuki risk yok.
3. İlk cümle selamsız konuya giriyor, kime konuşulduğu belli, merak boşluğu açık. 4. Kilit cümlesi sonunda ne kazanılacağını söylüyor.
5. Her blok tek fikir + örnek; bloklar arasında ara kanca var. 6. Tekrar eden fikir/dolgu kelime yok.
7. Kapanış tek cümle; tek CTA; DM/hediye vaadi yok. 8. Son cümle ilk cümleye bağlanıyor. 9. Süre 55–70 sn.
**Kallaway dersleri (refs/kallaway.md) — inceleme rubriğine EK maddeler, hepsi geçmeli:**
10. 70/100'den başlıyor mu (izleyici hikâyenin/sorunun ortasına bırakılıyor, ısınma yok)? İlk zirve (şok rakam / aykırı görüş / zıtlık) ilk 10 sn içinde mi?
11. **Yoğunlaştırıcı döngü** 5–15 sn arasında var mı (kancanın merakını büyüten 2. cümle: risk büyütür, soruyu keskinleştirir — kancayı tekrarlamaz)?
12. Mini zirve her 10–15 sn'de bir mi; **ilk yeniden kanca en geç 25. saniyede** mi (kum saati)? Yeniden kanca = izleyicinin şu an düşündüğü ilginç şeyden ikinciye yumuşak geçiş.
13. Dopamin döngüsü: risk (kim, neyi kaybediyor, neden şimdi) + büyük soru + **ters köşe** (izleyiciyi A'ya inandırıp B'yi göstermek) var mı?
14. Hikâye ipi: her cümle ana konuya bağlı ve bir öncekinin üstüne kuruluyor mu; ana konudan 2+ adım sapan cümle var mı (varsa FAIL)?
15. Uygulama/hikâye mi, yoksa içgörüsüz bilgi listesi mi? İzleyicinin kendi parası/kararına bağlanıyor mu (arzu çapası)?
16. Kanca dili geniş kitleye açık mı (TAM): sonuç çerçevesi geniş, kitle tanımı dar değil, terimler sade ("maaşlı lisans mezunlarının" yerine "üniversite bitirenlerin" gibi)?
**Üçlü kanca uyumu (kurgu kontrolü):** sözlü kanca + ilk kare başlığı + ilk görsel AYNI şeyi söyler. `katman.py` sonrası iki test: sesi kapalı ilk 3 sn → konu tahmin edilebiliyor mu; gözler kapalı ilk 3 sn → aynı konu mu.
**Konu seçimi (Kallaway piramidi):** geniş farkındalık + izleyicinin büyük derdi; açı = "son 6 ayda ne değişti" (durum değişikliği/ifşa); zıtlık çerçevesi (eski yol vs yeni gerçek); A vs B başlıkları.
**Format & veri:** 3-3-1 (3 konu × 3 format, 10. video en iyi kombinasyonun tekrarı). Kazanan videolar 6–10 hafta sonra yeniden kurguyla tekrar yayınlanır (deneme reels 2. yöntem).
**Kavram adı + metafor:** her videoda anlatılan mekanizmaya akılda kalan bir isim ver ("maaş erimesi", "diploma tuzağı") ve tek somut metafora bağla — Kallaway'in en çok izlenenleri bu yapıda.
FAIL ise düzelt, tekrar incelet. PASS olmadan seslendirmeye geçme.
- Klasör: `videos/<YYYY-MM-DD>-<kisa-slug>/` → `script.txt` (sadece konuşulacak metin), `iskelet.md` (bölüm etiketli hali), `kaynaklar.md`.

## 3. Ses + avatar (AYRIK YÖNTEM — kredi tasarrufu, Ata'nın kesin kuralı)
Ata ekranda MÜMKÜN OLDUĞUNCA AZ görünür: giriş (hook), kapanış (CTA + döngü) ve ortada 1–2 kritik vurgu anı.
Toplam avatar süresi videonun %35'ini geçmez (hedef 15–20 sn). Geri kalan her şey sadece ses + grafik.
1. **Tam seslendirme:** `mcp__heygen__create_speech` text = script.txt'nin tamamı, voiceId `53aac87758ba4784bfb3eb88ff0057df`, language `tr`, **engine `heygen_voice`** (Ata bu sesi onayladı, 19 Ekim — motoru değiştirme), **speed 1.0** (Ata 23 Eki 16:17: 0.93 robotik; tempo cümle arası 0,3 sn duraklamayla — `split.py pause`).
   Dönen `audio_url`'yi `curl -sSLf -o $PD_WORK/<slug>/speech.wav` ile indir; dönen `word_timestamps` listesini aynen
   `$PD_WORK/<slug>/words.json` olarak kaydet (`PD_WORK` varsayılan `~/pd_work`).
2. **Baş sessizliği + telaffuz:** önce `python3 engine/split.py trim <slug>` (ilk kelime ≤0.06 sn — Katman 1), sonra `ffmpeg -y -i speech.wav -ac 2 -ar 48000 voice.wav` (WORK içinde) ve `python3 engine/pv.py tel <slug>`.
   Çoğu işaret rakam/kesme işareti biçim farkıdır. Anlamı bozan gerçek hata varsa script'i düzelt (yazıyla/farklı kelime) ve sesi yeniden üret (ucuz).
3. **Cümleleri seç:** `python3 engine/split.py list <slug>` → numaralı cümleler. Avatar cümlelerini seç: ilk 1–2 (hook), son 1–2 (CTA+döngü),
   ~~ortadan en fazla 2 vurgu cümlesi~~ → 30 Eki'den beri TÜM cümleler (HEP VARIM). `python3 engine/split.py cut <slug> 0,1,7,12,13` → `seg_XX.wav` parçaları, `voice.wav`, altyazı, `segments.json`.
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
- **İmza stil (23 Eki 02:39'dan itibaren): PANEL** — bkz. ÇALIŞMA KURALLARI. ~~**MASA ÜSTÜ DOSYA**~~ **YASAK (Ata 23 Eki 02:36) — kullanma, sadece arşiv.** — `from masa_kit import *` (kit/masa_kit.py: put/take/tape/write/draw/prt(fiş)/slide(foto)/lamp/dark/cam, fis(), kup(), ring(), line(); `SOUND_KIT='masa'`, `EXIT_FADE=False`). Örnek: videos/faiz-indi/spec.py. Her videoda bir FİŞ (kişisel hesap) + gerçek manşet/kupür + tek somut metafor + lamba söner desen kırılması.
- **Eski stil rotasyonu (masa üstü dışı denemeler):** Gazete (`CSS_FILE='gazete.css.html'`) ↔ Kinetik (varsayılan css) ↔ alt-avatar düzeni. Son kullanılanı `log.md`'den bak, aynısını üst üste kullanma. Sahne düzenlerini ve animasyonları her seferinde değiştir.
- **Avatar kuralları (Ata'nın isteği, kesin):**
  - ~~Ata sadece giriş (hook), 1–2 vurgu anı, CTA ve kapanışta görünür; diğer sahnelerde `AV=None`~~ → İPTAL (Ata 30 Eki 12:23). Yeni kural: HEP VARIM (üstte) — HERO vurgu kartları + grafik sahnelerinde PIP; tüm cümleleri kapsayan avatar klibi (`split.py cut <slug> 0,1,…,N`).
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
- **Müzik/ses (Ata 20 Eki):** (ESKİ — 'gerilim' 23 Eki'de YASAKLANDI; varsayılan karanlik_hiphop) fon müziği otomatik: 'gerilim' ailesi, 7 varyasyon tarihe göre döner (art arda iki video aynı müziği almaz).
  Trap/phonk/hızlı davul KULLANMA ("promosyon gibi"). Mikser her render'da rapor basar: `music avg ≈ -19 dB`, `fx max ≤ -6 dB` (sese göre).
  fx max -6 dB'den yüksekse veya müzik sesi bastırıyorsa spec'teki SFX seviyelerini düşür. Sadece sesi değiştirmek için: `pv.py remix <slug>`.
- `python3 engine/pv.py render <slug>` (~15–20 dk; `run_in_background`, `flock /tmp/pd_render.lock`) → `public/<slug>.mp4`.
- `qa.jpg`'i Read ile aç, son kez kontrol et. Ses -13 LUFS civarı olmalı (pv.py render). Sonra `python3 tools/katman.py <slug>`.

## 7. Yayın dosyası + zamanlama
- `git add public/<slug>.mp4 videos/<slug> && git commit -m "video: <slug>" && git push` (push başarısızsa `git pull --rebase` sonra tekrar).
- Medya URL: `https://raw.githubusercontent.com/blodym4ry/paranin-dili/main/public/<slug>.mp4` — `curl -sI` ile 200 olduğunu doğrula.
- Paylaşım metni (`videos/<slug>/paylasim.txt`): ilk satır hook + 📌 konuya özel "… arkadaşına gönder" CTA; 3–5 kısa paragraf veri; "Kaynaklar: ..." ; "Yatırım tavsiyesi değildir."; 3–5 hashtag (#paranindili dahil). İlk yorum: tek soru. YouTube başlığı (#shorts ile), TikTok başlığı.
- **Kapak (seri görünümü, her videoda zorunlu — 'sahne' stili + Gölge kenar, Ata onayı 20/22 Ekim):**
  `COVER_STYLE=sahne COVER_THEME=<gold|red|blue|green> COVER_PROPS="<emoji1> <emoji2>" python3 engine/cover.py <slug> "<ARKA KELİME> / *<ön satır sarı>* / <ön satır beyaz (isteğe bağlı)>" "-" $PD_WORK/<slug>/seg_00.mp4 1.0`
  Toplam 2–4 kelime, clickbait ama doğru (videoda karşılığı olmalı). İlk parça başın arkasına dev harflerle yazılır, gerisi önde.
  Tema: para kaybı/uyarı=red, altın/servet=gold, banka/teknoloji/fatura=blue, birikim/kazanç=green. Emojiler konunun nesneleri (ör. 🪙 📉, 💳 🏦, 🧾 📉).
  Çıktıyı Read ile aç: yüz net ve gözler açık, emoji yüzü kapatmıyor, yazılar okunuyor; değilse saniyeyi/emojiyi değiştir (yakın çekim kaynakta tek emoji kullan: `COVER_PROPS=" 💤"`).
  commit + push; URL'yi commit'e sabitle (önbellek): `https://raw.githubusercontent.com/blodym4ry/paranin-dili/$(git rev-parse HEAD)/public/covers/<slug>.jpg` → post bilgisine `"videoThumbnailUrl"`.
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

## İmza stil: MASA ÜSTÜ + GERÇEK GÖRÜNTÜ (Ata seçimi 22 Eki; 23 Eki "Masa üstü dosya" olarak benimsendi — kit/masa_kit.py, örnek videos/faiz-indi)
Amaç: "Claude ile kurgulanmış" görünmemek. Altyazı mekaniği AYNI kalır (Ata). Örnek: videos/masa-testi/spec.py.
- Zemin gerçek masa fotoğrafı (kit/masa), hafif elde kamera kayması 12 fps adımlı. Düz renk/ızgara zemin yok.
- Bilgi masaya konan NESNE olarak gelir: krem kâğıt, kraft not, bantlı polaroid/fotoğraf. Girişler `put()` — 12 fps adımlı (stop-motion), yumuşak kayma/belirme YOK.
- Vurgu kırmızı keçeli kalemle elle: `write()` (Caveat el yazısı soldan açılır), `draw()` (elle daire, 3 varyant "kaynar"). Daktilo-etiket + sayaç klişesi az.
- Sahne çıkışı fiziksel: `take()` kâğıdı masadan çeker.
- Ses: `SOUND_KIT = 'masa'` → sentetik whoosh/riser/pop KAPALI; sadece ekrandaki nesnenin gerçek kaydı (`'f:bant'`, `'f:kagit_kay'`, `'f:kalem_yaz'`, `'f:kalem_daire'`, `'f:foto_birak'`, `'f:damga'`, `'f:sayfa'`, `'f:deklansor'`, `'f:bozuk_para'`, `'f:daktilo'` — kit/foley/lib.json).
- Gerçek fotoğraf/video her videoda en az 2 kez masada (bantlı baskı) ya da tam ekran B-roll olarak.

## KATMAN KATMAN — 7 katman edit çerçevesi (Batuhan @batuhaneditscom PDF'i, Ata 22 Eki: "analiz et ve öğren")
İzleyici bir sebeple kaydırır; her katman bir sebebi kaldırır. Tek efekt kurtarmaz, 7'si aynı anda doğru olmalı.
1. **HAM** — İlk karede yüz + başlık + ses hazır. İlk kelime ≤0.12 sn (`split.py trim <slug>` create_speech'ten hemen sonra). "Merhaba/bugün/bu videoda" yok. Avatar ilk karede görünür (fade yok — kinetik_core).
2. **RENK** — Siyah gerçekten siyah, cilt doğal, zemin markanın rengiyle aynı ailede (videonun paleti avatar arka planıyla çatışmasın).
3. **KESME** — Kancada (ilk 3 sn) 0.2 sn üstü boşluk yok; videoda 0.45 sn üstü ölü boşluk yok. Aynı şey iki kez söylenmez. Avatar pencere geçişinde yüz zıplamaz (pencereler arası yüz noktası yakın kalsın).
   Not: Ata'nın "yavaş tempo" isteği GÖRSEL yoğunluk içindir (öğe sayısı/ekranda kalma); kesme katmanıyla çelişmez — boşluk değil, ekran sakinleşir.
4. **BAŞLIK** — İlk karede HAZIR (animasyonla gelmeyi beklemez), konuyu 1 sn'de söyler. İki satır: düz kalın satır = konu, italik serif satır = duygu; altında kendini çizen çizgi gözü oraya çeker. Kanca süresince (~ilk 3 sn) ekranda.
5. **ALTYAZI** — Sesi kapalı izleyen takip eder; konuşmayla kare kare yanar. Yüzü ve Instagram arayüzünü örtmez: alt sınır y≤1440, sağ 230 px boş.
   **Ata 22 Eki:** stil aynı, konum yukarı → kit varsayılanı `#caps` y=1200–1420, x=70–830. **Grafik güvenli alanı artık y=230–1180** (altyazı bandına grafik koyma).
6. **GRAFİK** — Söylenen kelime o an ekranda görünür. Cümle dönünce ("ama/ancak/şimdi şaşırtıcı kısım") görüntü de döner (ton/zemin değişir).
7. **SES** — Konuşma önde, −13 LUFS (pv.py render). Efekt seyrek (≤1 olay/sn), her geçişe whoosh YOK. Müzik konuşmanın ~16 dB altında; çakışırsa söz kazanır.
**Yayın öncesi:** `python3 tools/katman.py <slug>` (ölçülebilenler) + elle 10 soru:
ilk karede yüz/başlık/ses? · ilk cümle merhaba/tanıtım mı? · renk telefon gibi mi? · kancada nefes/boşluk? · aynı şey iki kez? · sesi kapalı konu anlaşılıyor mu? ·
altyazı yüzü/arayüzü örtüyor mu? · her grafik o anki kelimeye oturuyor mu? · müzik sözün üstüne çıkıyor mu? · ilk 3 sn'de izleyici neden kalacağını biliyor mu?
**Kanca testi (inceleme alt-ajanına ekle):** "Bu Reels kancasını ilk 3 saniyede kaydırılma riskine göre değerlendir: konu bir saniyede anlaşılıyor mu, merak açıyor mu, boş bir girişi var mı. Sonra 3 daha güçlü alternatif yaz."

## DENEME REELS SİSTEMİ (Ata 22 Eki: "işimize yarar bir sistem" — benimsendi; ayrıntı: refs/deneme-reels.md)
Her zamanki onay kuralları geçerli: kredi harcamak ve zamanlamak için Ata'nın açık onayı şart. Varyasyon seti TEK video sayılır (Ata seti birlikte izler, onaylar).
1. **Kanca varyasyonu (her yeni video):** Gövde aynı, sadece kanca (ilk 1–2 cümle) değişir → 3 versiyon (A/B/C), farklı kanca formülleri (hookscore_tr ≥70).
   Maliyet: sadece kanca avatar parçası yeniden (~5 kredi/versiyon) + render. Klasör: videos/<slug>/ (A) ve videos/<slug>-b, -c (spec aynı, script/ses kancası farklı).
   Metricool: `instagramData.type = "TRIAL_REEL"`, aynı gün 2–3 sa arayla. TikTok/YouTube'a sadece kazanan, 48 sa sonra.
   **Paylaşım OTOMATİK (Ata 22 Eki: "herkesle paylaşa ben dokunmayayım"):** her deneme reels "otomatik paylaş" = Meta `graduationStrategy: SS_PERFORMANCE` ile çıkar;
   ilk ~72 sa'te iyi giden versiyonu Instagram kendisi profile/takipçilere açar. Meta API'de sonradan elle "paylaş" uç noktası YOK; bu yüzden ayar yayın anında verilmeli.
   48–72 sa sonra sonuçları log.md'ye yaz (hangi kanca kazandı) → sonraki kanca seçimlerini besler.
2. **Tutan videoyu çoğalt (kredi yok):** Profilde ortalamanın üstüne çıkan videoya 2–3 yeniden kurgu: farklı müzik, açılış görüntüsü/ilk kare, kapak, altyazı rengi. Değişiklik GÖZLE GÖRÜLÜR olmalı (IG kopya içeriğin erişimini kısar). Deneme olarak, otomatik paylaşım KAPALI.
3. **Format denemesi:** Tutan konuyu başka şablonla (ör. masa üstü ↔ optik form ↔ yüzsüz) yeniden kur, deneme olarak çık.
**Ata yokken (29 Eki'den ~30 gün):** asıl videolar normal Reels; ek olarak 2. yöntem (eski kazananların versiyonları) deneme + otomatik paylaşım AÇIK (Ata dokunmuyor).
**Doğrulandı (23 Eki):** Metricool `instagramData` alanı `"shareTrialAutomatically": true|false` (getScheduledPosts'ta TRIAL_REEL gönderilerde görünüyor). Ata'nın kararı: dokunmayacak → deneme reels'ler `shareTrialAutomatically: true`. Mevcut 2 TRIAL_REEL (26 Eki Efsane Cuma, 8 Kas sel) `false` ile kurulu — düzeltmek için Ata'nın açık onayı gerek.
