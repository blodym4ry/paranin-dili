#!/usr/bin/env python3
"""Turkish adapter for hookscore.py — same five checks, Turkish tokenizer and word lists.
Usage: python3 hookscore_tr.py hooks.txt   |   python3 hookscore_tr.py --hook "satır"
Score the line the way it will be READ on screen (digits allowed: "1 m³ fazla = 1.780 TL")."""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hookscore as H

H.WORD_RE = re.compile(r"[\w$%₺'’.,-]+", re.UNICODE)
_orig_words = H.words
def words(text):
    return [w for w in re.findall(r"[\w$%₺'’-]+(?:[.,]\d+)*", re.sub(r"(?<=\d)[.,](?=\d{3})", "", text), re.UNICODE)]
H.words = words
H.NUMBER_RE = re.compile(r"(?:₺|\$)?\s?\d[\d.,]*\s?(?:%|tl\b|lira\b|kuruş\b|m³|metreküp\b|yıl\b|ay\b|gün\b|saat\b|dakika\b)?|%\s?\d+", re.IGNORECASE)
H.PROPER_RE = re.compile(r"(?<!^)\b[A-ZÇĞİÖŞÜ][a-zçğıöşü]{2,}\b")
H.SPOKEN_NUMBERS |= {"sıfır", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz", "on", "yirmi", "otuz", "kırk", "elli", "altmış",
                     "yetmiş", "seksen", "doksan", "yüz", "bin", "milyon", "milyar", "yarısı", "yarım", "iki katı", "katı"}
H.MONEY_WORDS |= {"lira", "tl", "kuruş", "dolar", "euro", "maaş", "maaşın", "kira", "kiran", "fatura", "faturan", "faiz", "vergi", "zam",
                  "borç", "borcun", "kredi", "altın", "fiyat", "fiyatı", "para", "paran", "cebin", "cebinden", "ceza", "aidat"}
H.STAKES |= {"değil", "asla", "hiç", "yok", "kaybet", "kaybettin", "kaybedersin", "zarar", "zararda", "ceza", "tuzak", "tuzağı", "yanlış", "hata",
             "sadece", "fazla", "pahalı", "pahalıya", "bedava", "gizli", "kimse", "ama", "yerine", "önce", "rağmen", "sakın", "dikkat", "uyarı",
             "rekor", "çöktü", "battı", "eridi", "eriyor", "düştü", "kesti", "kesiyor", "öde", "ödersin", "ödüyorsun", "ödeyebilirsin", "kazan", "kazanır",
             "ilk", "son", "iki katı", "neden", "mi", "mı", "mu", "mü"}
H.WEAK_OPENERS += ["merhaba", "selam", "arkadaşlar", "bugün", "bu videoda", "evet", "şimdi", "aslında", "biliyor musunuz", "sizce"]
H.IMPERATIVES |= {"dur", "sakın", "bak", "kontrol", "öde", "ödeme", "al", "alma", "sat", "satma", "yap", "yapma", "kaydet", "unutma", "dikkat", "hesapla"}
_addr = re.compile(r"\b(sen|senin|sana|seni|sence|sende|cebin\w*|faturan\w*|maaşın\w*|paran\w*|kiran\w*|evin\w*|kartın\w*|borcun\w*|\w+(?:sın|sin|sun|sün|ın|in|un|ün))\b", re.IGNORECASE)
def check_address(text):
    low = text.lower()
    if _addr.search(low):
        return 100.0, "izleyiciye konuşuyor"
    w = [x.lower() for x in words(text)]
    if w and w[0] in H.IMPERATIVES:
        return 90.0, f"emir kipiyle açılış (\"{w[0]}\")"
    if re.search(r"\b(ben|benim|bana|biz|bizim)\b", low):
        return 70.0, "birinci tekil/çoğul, izleyici yok"
    return 35.0, "üçüncü şahıs, kimseye konuşmuyor"
H.check_address = check_address
_score = H.score if hasattr(H, 'score') else None
if __name__ == '__main__':
    H.main() if hasattr(H, 'main') else None
