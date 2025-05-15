import random
from utils.olasilik import tehlikeli_olasilik

class Esya:
    def __init__(self, isim, tehlikeli=False):
        self.isim = isim
        self.tehlikeli = tehlikeli

class Bagaj:
    def __init__(self, esyalar):
        self.esyalar = esyalar
        self.suspicious = any(e.tehlikeli for e in esyalar)

def rastgele_bagaj_olustur():
    """Rastgele 5-10 eşya, yasaklıysa kesin, değilse %10 olasılıkla tehlikeli olacak şekilde oluşturur"""
    esya_listesi = ["kitap", "telefon", "giysi", "parfüm", "şarj aleti", "bıçak", "sıvı", "ilaç", "bilgisayar", "silah", "patlayıcı"]
    esya_sayisi = random.randint(5, 10)
    esyalar = []
    for _ in range(esya_sayisi):
        isim = random.choice(esya_listesi)
        tehlikeli = tehlikeli_olasilik(isim)
        esyalar.append(Esya(isim, tehlikeli))
    return Bagaj(esyalar)
