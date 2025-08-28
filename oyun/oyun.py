# oyun/oyun.py
import random, time
from .karakter import Karakter
from .ai import ai_secim
from .dukkan import dukkan
from .ui import vs_anim, karakter_goster, yazdir_mesajlar

def karakter_secimi(karakterler, oyuncu_num):
    print(f"\nOyuncu {oyuncu_num} karakter seçimi:")
    for i, k in enumerate(karakterler):
        print(f"{i+1} - {k.isim} ({k.sinif})")
    while True:
        sec = input(f"Karakter seç (1-{len(karakterler)}): ")
        if sec.isdigit() and 1 <= int(sec) <= len(karakterler):
            return karakterler.pop(int(sec)-1)
        print("Geçersiz seçim.")

def oyun():
    karakterler = [
        Karakter("Maximus","Gladyatör",100,50,12,8,3,0.2,"Ağır Darbe"),
        Karakter("Spartacus","Gladyatör",90,55,11,9,3,0.25,"Çift Darbe"),
        Karakter("Leonidas","Gladyatör",95,60,13,7,4,0.18,"Çift Darbe"),
        Karakter("Merlin","Büyücü",70,80,8,4,4,0.15,"Büyü Saldırısı"),
        Karakter("Morgana","Büyücü",65,90,9,3,4,0.2,"Zehir Büyüsü"),
        Karakter("Artemis","Okçu",80,60,10,5,5,0.25,"Uzak Saldırı"),
        Karakter("Orion","Okçu",75,65,11,4,5,0.2,"Hızlı Ok"),
        Karakter("Hector","Gladyatör",110,45,14,6,3,0.15,"Ağır Darbe"),
        Karakter("Selene","Büyücü",60,100,7,3,4,0.2,"Zehir Büyüsü"),
        Karakter("Apollo","Okçu",85,55,12,4,6,0.22,"Hızlı Ok")
    ]

    while True:
        mod = input("Kaç oyuncu? (1=AI vs Sen, 2=İki oyuncu): ")
        if mod in ["1", "2"]:
            mod = int(mod); break
        print("Geçersiz seçim.")

    oyuncu_sira = [1,2] if random.random() < 0.5 else [2,1]

    if mod == 1:
        oyuncu1 = karakter_secimi(karakterler, 1)
        oyuncu2 = random.choice(karakterler)
        print(f"AI karakteri: {oyuncu2.isim}")
    else:
        oyuncu1 = karakter_secimi(karakterler, 1)
        oyuncu2 = karakter_secimi(karakterler, 2)

    mac = 0
    while True:
        while mac < 3:
            oyuncu1.can, oyuncu1.enerji = oyuncu1.max_can, oyuncu1.max_enerji
            oyuncu2.can, oyuncu2.enerji = oyuncu2.max_can, oyuncu2.max_enerji
            vs_anim()
            tur = 1
            while oyuncu1.can > 0 and oyuncu2.can > 0:
                print(f"\n--- Tur {tur} ---")
                karakter_goster(oyuncu1)
                karakter_goster(oyuncu2)

                for siradaki in oyuncu_sira:
                    if siradaki == 1:
                        print("\nOyuncu 1 sırası: 1-Hafif 2-Orta 3-Ağır 4-Dinlen 5-Savun")
                        sec = input("Seçim: ") if (mod==2 or siradaki==1) else random.choice(["1","2","3"])
                        if sec in ["1","2","3"]:
                            yazdir_mesajlar(oyuncu1.saldir(oyuncu2, int(sec)))
                        elif sec == "4":
                            yazdir_mesajlar(oyuncu1.dinlen())
                        elif sec == "5":
                            yazdir_mesajlar(oyuncu1.savun())
                        if oyuncu2.can <= 0:
                            print("Oyuncu 1 kazandı!")
                            oyuncu1.kazanc += 1; oyuncu1.para += 50
                            dukkan(oyuncu1, print)
                            break
                    else:
                        print("\nOyuncu 2 sırası:")
                        sec = input("Seçim: ") if mod==2 else ai_secim(oyuncu2, oyuncu1)
                        if sec in [1,2,3]:
                            yazdir_mesajlar(oyuncu2.saldir(oyuncu1, sec))
                        elif sec == 4:
                            yazdir_mesajlar(oyuncu2.dinlen())
                        elif sec == 5:
                            yazdir_mesajlar(oyuncu2.savun())
                        if oyuncu1.can <= 0:
                            print("Oyuncu 2 kazandı!")
                            oyuncu2.kazanc += 1; oyuncu2.para += 50
                            dukkan(oyuncu2, print)
                            break
                tur += 1
                time.sleep(1)
            mac += 1

        tekrar = input("\nMaçlar bitti! Tekrar? (E/H): ").strip().upper()
        if tekrar != "E":
            print("Oyun bitti! Teşekkürler!")
            break
        mac = 0
