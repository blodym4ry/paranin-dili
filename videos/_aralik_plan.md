# Aralık 1 + 3–10 üretim planı (Ata onaylı 6 Kas 2026; Ata 7 Kas–~7 Ara askerde)

Ata onayları (6 Kas): 9 senaryo "onaylıyorum" (14:42); 21:45 v2 kancaları "hepsi onaylı" (videos/_aralik_v2_kancalar.tsv);
telaffuz: Euro→"Yuro", TÜİK→"Tüik", BES→"Bes", BDDK→"Be De De Ka", e ailem/e devlet/kilovatsaat/metreküp yazıldığı gibi.
Format (Ata: "Karışık"): kredi yettiği kadar panel+HEP VARIM, gerisi animasyon (animation-studio) + Ata HERO kart giriş/orta/kapanış.
Denemeler (Ata): 21:45 farklı kanca (tools/v2kanca.py, kanca sesi pd_work/aralik/v2/<tarih>.mp3 + .json) + 22:45 hızlı kurgu (tools/hizli.py, animasyon kaynağında --baslik VERME: animasyonun kendi başlığı var).

| Tarih | Slug | Stil | Look | Ses | Avatar | Video | Zamanlama |
|---|---|---|---|---|---|---|---|
| 1 Ara | 2026-12-01-senin-enflasyonun | chalkboard | olive | ✓ | ✓ seg 0,9,18-19 | render | — |
| 3 Ara | 2026-12-03-kira-formulu | (17 Kas) | navy | ✓ | ✗ kredi | — | — |
| 4 Ara | 2026-12-04-taksit-siniri | (17 Kas) | hoodie_glasses | ✓ | ✗ kredi | — | — |
| 5 Ara | yatirim-karnesi-2026 | cgimotion | street | ✓ | ✓ seg 0,12-13,24-25 | render | — |
| 6 Ara | 2026-12-06-emekli-promosyon | glowsketch | olive | ✓ | ✓ | ✓ public/aralik/2026-12-06*.mp4 | ✓ main+v2+hz (pd_work/aralik/metricool_ids.txt) |
| 7 Ara | enerji-destegi-kis | pixelart | navy | ✓ | ✓ seg 0,13,21-22 | render | — |
| 8 Ara | 2026-12-08-bes-devlet-katkisi | (17 Kas) | hoodie_glasses | ✓ | ✗ kredi | — | — |
| 9 Ara | 2026-12-09-faiz-makasi | (17 Kas) | street | ✓ | ✗ kredi | — | — |
| 10 Ara | 2026-12-10-taksit-psikolojisi | (17 Kas) | olive | ✓ | ✗ kredi | — | — |

Paylaşım metinleri: videos/<slug>/paylasim.txt (UZUN/ILK_YORUM/YT_BASLIK/TT_BASLIK/KISA). Kapaklar: public/covers/<slug>.jpg (commit f42acd6).
Ana post yapısı: IG REEL ayrı post + FB/TT/YT tek post, 19:45; AI etiketleri false; deneme TRIAL_REEL shareTrialAutomatically=false; v2 metninin ilk paragrafı v2 kancası.

## Açık riskler
- Telaffuz şüphesi (Ata'ya ses gönderildi, cevap bekleniyor): 9 Ara "akdi" (Whisper "aktif" duydu), 4 Ara "Be De De Ka Ekim'de", 8 Ara "üç yıl dolmadan", 3 Ara "hakim".
- Yayından önce doğrula: 1 Ara TCMB kart faizi tavanı (9, 10 Ara), mevduat faizi + stopaj süresi (9 Ara), emekli promosyon tablosu (6 Ara), BES oranı (8 Ara), Kasım TÜFE 3 Ara (1, 3 Ara metinlerinde "Ekim 2026 verisi" notu var).
