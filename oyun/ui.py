# oyun/ui.py
import os, time

def temizle():
    os.system("cls" if os.name == "nt" else "clear")

def vs_anim():
    temizle()
    print("🔥 VS 🔥")
    time.sleep(0.5)
    temizle()

def yazdir_mesajlar(mesajlar):
    for m in mesajlar:
        print(m)

def karakter_goster(karakter):
    can_bar = "█" * int((karakter.can / karakter.max_can) * 20)
    can_bar += "-" * (20 - len(can_bar))
    enerji_bar = "█" * int((karakter.enerji / karakter.max_enerji) * 20)
    enerji_bar += "-" * (20 - len(enerji_bar))
    info = (
        f"{karakter.isim} ({karakter.sinif})\n"
        f"Can:    [{can_bar}] {karakter.can:.0f}/{karakter.max_can}\n"
        f"Enerji: [{enerji_bar}] {karakter.enerji:.0f}/{karakter.max_enerji}\n"
        f"Saldırı: {karakter.saldiri} | Savunma: {karakter.savunma} | Hız: {karakter.hiz} "
        f"| Kritik: {int(karakter.kritik*100)}% | Para: {karakter.para} | Kazanç: {karakter.kazanc}\n"
        f"Özel Saldırı: {karakter.ozel_saldiri}"
    )
    print(info)
