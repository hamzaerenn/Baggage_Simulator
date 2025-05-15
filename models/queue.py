class YolcuKuyrugu:
    def __init__(self):
        self.kuyruk = []
    def enqueue(self, yolcu):
        self.kuyruk.append(yolcu)
    def dequeue(self):
        return self.kuyruk.pop(0) if self.kuyruk else None
    def is_empty(self):
        return len(self.kuyruk) == 0
    def size(self):
        return len(self.kuyruk)
    def tum_yolcular(self):
        return self.kuyruk.copy()
