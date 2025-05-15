from models.yolcu import yolcu_olustur, Yolcu
from models.queue import YolcuKuyrugu
from models.stack import BagajStack
from models.linkedlist import KaraListe
from utils.olasilik import esya_tehlikeli_mi
import json
import random

# Global yapılar
kuyruk = YolcuKuyrugu()
stack = BagajStack()
kara_liste = KaraListe()
kontrolden_gecen_yolcular = []  # Kontrolden geçen yolcular (işlenenler)
alarm_sayisi = 0
loglar = []
toplam_yolcu_sayisi = 0  # Sisteme eklenen toplam yolcu
kontrolden_gecen_yolcu = 0  # Kontrolden geçen yolcu sayısı
TEMIZ_RISK_ESIK = 2  # Temiz sayılacak risk puanı eşiği

RISK_ESIK = 2  # Kara liste için risk puanı eşiği
KARA_LISTE_OLASILIK = 0.5  # %50 olasılık

# Kara listeyi json'dan yükle
with open('baggage_simulator/data/kara_liste.json', 'r') as f:
    kara_liste_json = json.load(f)
    for kayit in kara_liste_json:
        kara_liste.ekle(kayit['yolcu_id'], kayit['sebep'])

def yolcu_ekle():
    """A. Yeni yolcu oluştur ve kuyruğa ekle"""
    global toplam_yolcu_sayisi
    yolcu = yolcu_olustur()
    kuyruk.enqueue(yolcu)
    toplam_yolcu_sayisi += 1
    loglar.append(f"[EKLE] {yolcu.id} kuyruğa eklendi.")
    print(f"[EKLE] {yolcu.id} kuyruğa eklendi.")
    return yolcu

def simulasyonu_baslat():
    """B. Kuyruktan yolcu al, kara liste kontrolü ve bagaj tarama"""
    global alarm_sayisi, kontrolden_gecen_yolcu
    if kuyruk.is_empty():
        print("Kuyruk boş!")
        return
    yolcu = kuyruk.dequeue()
    kontrolden_gecen_yolcu += 1
    kontrolden_gecen_yolcular.append(yolcu)
    print(f"[KONTROL] {yolcu.id} kuyruğa alındı.")
    loglar.append(f"[KONTROL] {yolcu.id} kuyruğa alındı.")
    kara_listede = kara_listede_mi(yolcu.id)
    if kara_listede:
        yolcu.risk += 1
        loglar.append(f"[KARA LİSTE] {yolcu.id} riskli yolcu! Risk puanı: {yolcu.risk}")
        print(f"[KARA LİSTE] {yolcu.id} riskli yolcu! Risk puanı: {yolcu.risk}")
        bagaj_tarama(yolcu, kara_liste_etiketi=True)
    else:
        bagaj_tarama(yolcu)
    # Risk puanı eşik ve olasılık kontrolü
    if yolcu.risk >= RISK_ESIK and not kara_listede:
        if random.random() < KARA_LISTE_OLASILIK:
            kara_liste.ekle(yolcu.id, "Otomatik: Yüksek risk puanı")
            loglar.append(f"[OTOMATİK KARA LİSTE] {yolcu.id} risk puanı {yolcu.risk} ile kara listeye eklendi!")
            print(f"[OTOMATİK KARA LİSTE] {yolcu.id} risk puanı {yolcu.risk} ile kara listeye eklendi!")

def tum_bagajlar_temiz(yolcu):
    for bagaj in yolcu.bagajlar:
        for esya in bagaj.esyalar:
            if esya_tehlikeli_mi(esya):
                return False
    return True

def kara_listede_mi(yolcu_id):
    """C. Kara liste kontrolü"""
    return kara_liste.kara_listede_mi(yolcu_id)

def bagaj_tarama(yolcu, kara_liste_etiketi=False):
    """D. Bagajı stack'e aktar ve tehlikeli mi kontrol et"""
    global alarm_sayisi
    for bagaj in yolcu.bagajlar:
        stack.push(bagaj, yolcu.id)
        for esya in bagaj.esyalar:
            if esya_tehlikeli_mi(esya):
                alarm_sayisi += 1
                yolcu.risk += 1  # Her alarmda risk puanı artır
                if kara_liste_etiketi:
                    loglar.append(f"[ALARM] {yolcu.id} (Kara Liste) bagajında TEHLİKELİ eşya: {esya.isim}")
                    print(f"[ALARM] {yolcu.id} (Kara Liste) bagajında TEHLİKELİ eşya: {esya.isim}")
                else:
                    loglar.append(f"[ALARM] {yolcu.id} bagajında TEHLİKELİ eşya: {esya.isim}")
                    print(f"[ALARM] {yolcu.id} bagajında TEHLİKELİ eşya: {esya.isim}")

def stack_taramasi():
    """E. Stack incelemesi"""
    while not stack.is_empty():
        bagaj_tuple = stack.pop()
        bagaj, yolcu_id = bagaj_tuple
        tehlikeli_var = any(esya_tehlikeli_mi(e) for e in bagaj.esyalar)
        if tehlikeli_var:
            print(f"[ALARM] Stack'ten çıkan bagajda tehlikeli eşya var!")
        else:
            print(f"[TEMİZ] Stack'ten çıkan bagaj temiz.")

def temiz_gecen_yolculari_getir():
    """Kara listeye girmemiş ve risk puanı eşikten düşük olan yolcuları döndürür."""
    return [y for y in kontrolden_gecen_yolcular if (not kara_listede_mi(y.id) and y.risk < TEMIZ_RISK_ESIK)]

def rapor_goster():
    """F. Gün sonu raporu"""
    print("\n--- RAPOR ---")
    print(f"Kontrolden geçen yolcu: {kontrolden_gecen_yolcu}")
    print(f"Alarm sayısı: {alarm_sayisi}")
    print(f"Kara listede yakalananlar: {[k[0] for k in kara_liste.tum_yolcular()]}")
    print(f"Temiz geçen yolcular: {len(temiz_gecen_yolculari_getir())}")
    print(f"Stack'e alınan bagaj sayısı: {stack.size()}")
    print("--- Risk Puanları ---")
    for y in kontrolden_gecen_yolcular:
        print(f"{y.id}: Risk puanı = {y.risk}")

if __name__ == "__main__":
    # Örnek akış
    for _ in range(5):
        yolcu_ekle()
    for _ in range(5):
        simulasyonu_baslat()
    stack_taramasi()
    rapor_goster()
