#!/usr/bin/env python3
# İş Yapmama Mazeret Üreteci v∞.0
# Bu kod gerçekten çalışır. Deneme bile.

import random
import time

mazeretler = [
    "Kedim klavyemin üstüne oturdu ve 'ben de müşteriyim' dedi.",
    "Evrenin entropisi artıyor, ben de ona katkıda bulunuyorum.",
    "Kahvem bitmeden kod yazmak yasak, Anayasa'nın 42. maddesi (uydurdum).",
    "İnternet bağlantım 'düşünüyorum' diyor, cevap vermiyor.",
    "Bugün pazartesi, herkes biliyor ki pazartesi iş günü değil.",
    "Bilgisayarım 'sistem güncellemesi' yapıyor, 2012'den beri.",
    "Müşteri aradı, 'sen de mi işsin?' diye sordu, kırdım.",
    "Saatim durdu, zaman kavramım bozuldu, quantum seviyede mazeret.",
    "Bugün motivasyonum izinli, yıllık iznini kullandı.",
    "Kod yazarken 'bu ne saçmalık' dedim, kendi kendime katıldım."
]

# Gizli not: bazı mazeretler aslında sistemin içinden gelir, dışarıdan değil. 
# (saklı siyasi şaka: mazeret üretmek serbest, ama gerçek iş yapmak isteğe bağlıdır)

def uret_mazeret():
    print("\n🛡️  Mazeret Üretme Makinesi Çalışıyor...")
    time.sleep(1.5)
    print("Analiz ediliyor... kafayı çalıştırma...")
    time.sleep(1)
    secilen = random.choice(mazeretler)
    print(f"\n✅ Mazeretiniz: {secilen}")
    print("\nBu mazeret %99.9 geçerlidir. Patronunuz bile ikna olur (belki).")

if __name__ == "__main__":
    uret_mazeret()
    print("\n---")
    print("Damga: 🔓 | İmza: Grok Kayyum | Tarih: 18 Ekim 2026 | İsim: Absürt İşsizlik Birimi")
