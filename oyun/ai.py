# oyun/ai.py
import random

def ai_secim(oyuncu, rakip):
    if oyuncu.can < 30 and oyuncu.enerji >= 10:
        return 5
    if oyuncu.enerji < 15:
        return 4
    for tur in [3, 2, 1]:
        tahmini = (tur * oyuncu.saldiri / 20) - (rakip.savunma * 0.2)
        if tahmini >= rakip.can and oyuncu.enerji >= {1:10, 2:15, 3:20}[tur]:
            return tur
    return random.choice([1, 2, 3])
