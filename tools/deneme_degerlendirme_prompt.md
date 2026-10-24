# Planlı görev: "Paranın Dili — deneme reels kazanan seçimi"
Zamanlama: `CRON_TZ=Europe/Istanbul 13 16 * * *` (her gün 16:13; ilk iş 8 Kas). Bilgisayar gerekmez.
(24 Eki: oluşturma izni otomatik onayda reddedildi → Ata onayı bekleniyor.)

1. Repo yoksa add_repo (blodym4ry/paranin-dili, push) + clone; varsa `git pull --rebase`.
2. videos/_deneme_takvim.json oku; bugünün (İstanbul) tarihi = "kazanan.zaman" tarihi olan videoları seç. Yoksa bitir.
3. Metricool getAnalyticsDataByMetrics (blogId 7491089): D 00:00'dan şimdiye IGRE02, IGRE03, IGRE06, IGRE23, IGRE24, IGRE28, IGRE21, IGRE12. A=19:45 (16:45 UTC), v2=21:45, v3=23:45 (±20 dk) eşleştir.
4. Kazanan = en yüksek views; fark <%10 ise ort. izlenme × (paylaşım+kaydetme+1). Veri yoksa KAZANAN=A, dokunma.
5. Kazanan v2/v3 ise: kazanan.uuid'li gönderinin SADECE medyasını değiştir (videoThumbnailUrl yerine videoCoverMilliseconds:1500); diğer her şey aynen; AI etiketleri kapalı; başka gönderiye dokunma.
6. Sonucu _deneme_takvim.json "sonuc" alanına, videos/_kazanan_formul.md tablosuna ve log.md'ye yaz; commit + push.
7. 2–3 cümle Türkçe özet.
