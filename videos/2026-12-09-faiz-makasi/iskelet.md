# Faiz makası — iskelet (yayın 9 Ara 2026, Çar 19:45 — REEL)
Kavram adı + metafor: **"makasın iki ağzı da devlette"** — bir ağız mevduattaki stopaj, öbürü karttaki vergi+fon. Kalıcı harita: 100 TL'lik tek çubuk; soldan mevduat (43 → 35,5), sağdan kart (45 → 58,5), aradaki 23'lük boşluk renklenir: 21 devlet (kırmızı), 2 banka.

1. **KANCA** [FULLOPEN→HERO]: Bankaya yüz lira koyarsan, yılda kırk üç lira faiz alırsın. Kart borcunda aynı yüz lira sana elli sekiz buçuk ödetebilir.
2. **KİLİT** [HERO]: Aradaki makasın çoğu bankaya gitmiyor… Kime gittiğini ve kendi faizini nerede göreceğini söyleyeceğim.
3. **BLOK 1 — mevduat** [PIP]: Ekim'de ortalama mevduat faizi ~%43 (TCMB, 16 Eki haftası %42,9). Stopaj %17,5 → net 35,5.
4. **ARA KANCA 1** [HERO, desen kırılması]: Kartta kesinti daha büyük.
5. **BLOK 2 — kart** [PIP]: Dönem borcu 30 bin+ → tavan aylık %3,75'ten başlıyor → yılda 45. Üstüne faizin %30'u kadar vergi ve fon (KKDF %15 + BSMV %15) → +13,5. Ünlem.
   → Teslim (kilidin 1. sözü) [HERO]: Yirmi üç liralık makasın yirmi bir lirası devletin.
6. **ARA KANCA 2 (zorunlu)** [HERO]: Asıl önemlisi şu… Bankanın derdi geri dönmeyen para.
7. **BLOK 3 — risk + adım** [PIP]: Batık bireysel kart borcu yılbaşından beri +%65 (125,2 → 207,2 milyar TL). Bu risk faize yazılıyor. Ekstrende "akdi faiz oranı" satırı = senin oranın (kilidin 2. sözü). Sadece asgari → kalan borca faiz hesap kesim gününden işler.
8. **KAPANIŞ / sınır** [HERO]: Dürüst olayım, bu kaba bir hesap. Banka vadesiz hesaplara neredeyse faiz ödemiyor.
9. **CTA + DÖNGÜ** [HERO]: Bunu, kart borcunu asgariyle çeviren arkadaşına gönder. O elli sekiz buçuk lirayı o ödüyor. (→ 2. cümledeki 58,5'e döner)

## Kancalar (tools/hookscore_tr.py, hooks.txt)
| # | Formül | Kanca (ekran yazımı) | Puan |
|---|---|---|---|
| 1 ✅ | rakam zıtlığı (A vs B) | Bankaya 100 lira koyarsan yılda 43 lira faiz alırsın. Kart borcunda 58,5 ödeyebilirsin. | **81,6** STRONG |
| 2 | "herkes X sanıyor, tersi" (ifşa) | Kart faizin ile mevduat faizi arasındaki 23 liralık makasın 21'i bankaya değil, devlete gidiyor. | 75,1 STRONG (v2/v3 deneme kancası adayı) |
| 3 | "X yapıyorsan sebebi Y" | Kartında sadece asgariyi ödüyorsan, faizin son ödeme gününden değil, hesap kesimden işliyor. | 54,4 OK |
İlk kare başlığı önerisi: "100 TL: +43 / −58,5" (≤6 kelime).

## Süre
- 159 kelime. `beats.py --target 60`: 80,0 sn (araç Türkçe harfleri ayrı kelime sayıyor → 220 "kelime"; şişkin). Kalibrasyon: aynı-maaş 151 kelime → beats 69,1 sn → gerçek 58,0 sn (oran 0,84). Tahmini gerçek süre **~65–67 sn** (55–70 aralığında, üst uçta). Kısaltma gerekirse ilk aday: "Ekim'de" cümlesini "Ortalama mevduat faizi yüzde kırk üç civarı." yapmak (−2) ve "Senin oranın orada." cümlesini atmak (−3). "Bu risk de faize yazılıyor." ve kilitteki ekstre sözü korunmalı.

## Öz-inceleme rubriği (RUNBOOK §2, 1–16) — dürüst işaret
1. Doğruluk: ✅ her rakam kaynaklı (kaynaklar.md). ⚠️ hesap basit yıllık (aylık × 12), kart tavanı 30–180 bin dilimi, mevduat ağırlıklı ortalaması; "kaba hesap" cümlesiyle sınır çizildi. Tarih: "Ekim'de" sözlü; ekranda "Ekim 2026, TCMB" yazılmalı.
2. Abartı/garanti/tavsiye yok: ✅ ("ödetebilir", "kaba bir hesap").
3. Selamsız, kime belli, merak boşluğu: ✅
4. Kilit ne kazanılacağını söylüyor: ✅ (kime gittiği + kendi faizini nerede göreceği)
5. Blok tek fikir + ara kanca: ✅ (2 ara kanca: "Kartta kesinti daha büyük." / "Asıl önemlisi şu…")
6. Tekrar/dolgu: ✅ ("yüz lira" tekrarı bilinçli, karşılaştırma birimi)
7. Kapanış tek cümle, tek CTA, DM vaadi yok: ⚠️ KISMEN — özet/teslim cümlesi ("…yirmi bir lirası devletin") ortada; sonda "dürüst olayım" sınır cümlesi kapanış işlevi görüyor. Tek CTA ✅.
8. Son cümle ilk cümleye bağlanıyor: ✅/⚠️ — "elli sekiz buçuk" kancanın 2. cümlesine bağlanıyor (1. cümleye değil). beats.py "no loop" uyarısı verdi (ASCII eşleştirme; "yüz lira" kelimesi CTA'da yok).
9. Süre 55–70: ✅ (~65–67 tahmini)
10. 70/100 başlangıç, ilk zirve ≤10 sn: ✅ (43 vs 58,5 ilk 5 sn)
11. Yoğunlaştırıcı döngü 5–15 sn: ✅ ("makasın çoğu bankaya gitmiyor…")
12. Mini zirve 10–15 sn, ilk yeniden kanca ≤25 sn: ✅ ("Kartta kesinti daha büyük." ≈22–24 sn)
13. Risk + büyük soru + ters köşe: ✅ (izleyici "banka kazıklıyor" sanıyor → makasın çoğu devlette)
14. Hikâye ipi, sapma yok: ✅ (risk bloğu makasın bileşeni olarak bağlı)
15. Uygulama + arzu çapası: ✅ (ekstre satırı + asgari tuzağı)
16. Kanca dili geniş kitleye açık: ✅ ("bankaya yüz lira", "kart borcu")
Bağımsız inceleme (taze alt-ajan) BU OTURUMDA YAPILMADI — TTS öncesi RUNBOOK gereği yapılmalı.

## Doluluk testi
1. ≥4 kaynaklı bilgi: ✅ mevduat ~%42,9 (TCMB) · stopaj %17,5 · kart tavanı aylık %3,75 (30–180 bin) · KKDF %15 + BSMV %15 · batık kart borcu +%65 · faizin hesap kesimden işlemesi.
2. Şaşırtıcı bilgi: ✅ 23 puanlık makasın ~21'i devlete.
3. Somut adım: ✅ ekstrede "akdi faiz oranı" satırı; asgari ödemenin faizi hesap kesimden başlattığı.
4. Kilit sözü eksiksiz: ✅ kime gittiği (devlet + risk/vadesiz açıklaması) ve kendi faizini nerede göreceği (ekstre).

## Telaffuz listesi (script'te kısaltma/marka YOK — KKDF/BSMV bilinçli olarak "vergi ve fon" dendi)
| Kelime | TTS yazımı | Not |
|---|---|---|
| Ekim'de | Ekim'de | sorun beklenmez |
| stopajla | stopajla | ⚠️ dinle: "sto-paj" (j yumuşak) |
| akdi | akdi | ⚠️ dinle: doğru okunuş "ak-dî"; "ak-di" de kabul; garip çıkarsa "sözleşme faizi oranı" ile değiştir (ama ekstrede "akdi" yazıyor, ekranda "Akdi faiz oranı" göster) |
| ekstrende | ekstrende | ⚠️ dinle (eks-tren-de) |
| asgariyi / asgariyle | asgariyi / asgariyle | sorun beklenmez |
| virgül yetmiş beş | olduğu gibi | ekranda %3,75 (REPL) |
Ekran REPL: "yüzde kırk üç"→%43 · "yüzde on yedi buçuk"→%17,5 · "yüzde üç virgül yetmiş beş"→%3,75 · "elli sekiz buçuk"→58,5 · "on üç buçuk"→13,5 · "yüzde altmış beş"→%65 · "vergi ve fon"→ekranda "KKDF %15 + BSMV %15".
