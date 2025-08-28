# oyun/karakter.py
import random

class Karakter:
    def __init__(self, isim, sinif, can, enerji, saldiri, savunma, hiz, kritik, ozel_saldiri, para=0, kazanc=0):
        self.isim = isim
        self.sinif = sinif
        self.max_can = can
        self.can = can
        self.max_enerji = enerji
        self.enerji = enerji
        self.saldiri = saldiri
        self.savunma = savunma
        self.hiz = hiz
        self.kritik = kritik
        self.ozel_saldiri = ozel_saldiri
        self.para = para
        self.kazanc = kazanc
        self.hazir_savun = False

    def saldir(self, rakip, tur):
        enerji_maliyet = {1:10, 2:15, 3:20}
        katsayi = {1:0.8, 2:1, 3:1.5}
        if tur not in [1,2,3]:
            return ["Geçersiz saldırı seviyesi!"]
        if self.enerji < enerji_maliyet[tur]:
            return [f"{self.isim} enerji yetmiyor! ({self.enerji})"]

        self.enerji -= enerji_maliyet[tur]
        k = katsayi[tur]
        mesajlar = []

        if random.random() < self.kritik:
            k *= 1.2
            mesajlar.append(f"💥 {self.isim} kritik vuruş yaptı!")

        hasar = (self.saldiri * k) * (1 + self.enerji / self.max_enerji)
        hasar *= (1 - (rakip.savunma * 0.2 / rakip.hiz))

        if rakip.hazir_savun:
            hasar *= 0.5
            rakip.hazir_savun = False
            mesajlar.append(f"{rakip.isim} savunmada! Hasar yarıya düştü.")

        # Özel saldırılar
        if self.ozel_saldiri == "Ağır Darbe" and tur == 3:
            hasar *= 1.5
        elif self.ozel_saldiri == "Çift Darbe" and tur >= 2:
            hasar *= 1.3
            mesajlar.append(f"{self.isim} Çift Darbe yaptı!")
        elif self.ozel_saldiri == "Büyü Saldırısı" and tur == 3:
            hasar *= 1.5
        elif self.ozel_saldiri == "Zehir Büyüsü":
            rakip.can -= 5
            mesajlar.append(f"{self.isim} Zehir Büyüsü! Rakip her tur 5 hasar aldı.")
        elif self.ozel_saldiri == "Uzak Saldırı" and tur == 3:
            hasar *= 1.4
        elif self.ozel_saldiri == "Hızlı Ok" and tur <= 2:
            hasar *= 1.2

        rakip.can = max(0, rakip.can - hasar)
        mesajlar.append(f"{self.isim} saldırdı! {rakip.isim} {hasar:.2f} hasar aldı. (Can: {rakip.can:.2f})")
        return mesajlar

    def dinlen(self):
        self.enerji = min(self.max_enerji, self.enerji + 20)
        return [f"{self.isim} dinlendi. Enerji: {self.enerji}"]

    def savun(self):
        self.hazir_savun = True
        return [f"{self.isim} savunmaya geçti! Bir sonraki saldırıda hasar %50 azalacak."]
