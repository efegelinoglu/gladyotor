# oyun/dukkan.py
def dukkan(oyuncu, yazdir):
    while True:
        yazdir("\n--- DÜKKAN ---")
        yazdir("1 - Saldırı +5 (30 para)")
        yazdir("2 - Savunma +3 (20 para)")
        yazdir("3 - Hız +1 (25 para)")
        yazdir("4 - Çıkış")
        secim = input("Seçim: ")
        if secim == "1" and oyuncu.para >= 30:
            oyuncu.saldiri += 5; oyuncu.para -= 30
            yazdir(f"Saldırı güçlendi! {oyuncu.saldiri}")
        elif secim == "2" and oyuncu.para >= 20:
            oyuncu.savunma += 3; oyuncu.para -= 20
            yazdir(f"Savunma güçlendi! {oyuncu.savunma}")
        elif secim == "3" and oyuncu.para >= 25:
            oyuncu.hiz += 1; oyuncu.para -= 25
            yazdir(f"Hız arttı! {oyuncu.hiz}")
        elif secim == "4":
            break
        else:
            yazdir("Yetersiz para veya yanlış seçim.")
