import random
from typing import List
from .bagaj import Bagaj

yolcu_sayac = 1

class Yolcu:
    def __init__(self, isim: str, bagajlar: List[Bagaj], yolcu_id=None):
        global yolcu_sayac
        self.id = yolcu_id if yolcu_id else f"Yolcu#{yolcu_sayac}"
        self.isim = isim
        self.bagajlar = bagajlar
        self.risk = 0
        yolcu_sayac += 1

def yolcu_olustur():
    """Rastgele isim ve bagajlarla yeni yolcu oluşturur"""
    isim = f"Yolcu_{random.randint(100,999)}"
    from .bagaj import rastgele_bagaj_olustur
    bagajlar = [rastgele_bagaj_olustur() for _ in range(random.randint(1,2))]
    return Yolcu(isim, bagajlar)
