import random

yasakli_esyalar = ["silah", "bıçak", "patlayıcı", "sıvı"]

def esya_tehlikeli_mi(esya):
    """Eşyanın tehlikeli olup olmadığını döndürür"""
    return esya.tehlikeli

def tehlikeli_olasilik(esya_adi):
    """Eşya yasaklıysa kesin tehlikeli, değilse %10 olasılıkla tehlikeli"""
    if esya_adi.lower() in yasakli_esyalar:
        return True
    return random.random() < 0.1
