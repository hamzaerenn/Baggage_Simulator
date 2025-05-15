class KaraListeNode:
    def __init__(self, yolcu_id, sebep):
        self.yolcu_id = yolcu_id
        self.sebep = sebep
        self.next = None

class KaraListe:
    def __init__(self):
        self.head = None
    def ekle(self, yolcu_id, sebep):
        yeni = KaraListeNode(yolcu_id, sebep)
        if not self.head:
            self.head = yeni
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = yeni
    def kara_listede_mi(self, yolcu_id):
        curr = self.head
        while curr:
            if curr.yolcu_id == yolcu_id:
                return True
            curr = curr.next
        return False
    def sebep_getir(self, yolcu_id):
        curr = self.head
        while curr:
            if curr.yolcu_id == yolcu_id:
                return curr.sebep
            curr = curr.next
        return None
    def tum_yolcular(self):
        curr = self.head
        sonuc = []
        while curr:
            sonuc.append((curr.yolcu_id, curr.sebep))
            curr = curr.next
        return sonuc
