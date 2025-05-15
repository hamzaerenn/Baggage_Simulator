import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QListWidget, QTextEdit, QListWidgetItem, QFrame
)
from PyQt5.QtCore import Qt
import main as sim

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bagaj Güvenlik Simülatörü")
        self.setGeometry(300, 150, 700, 500)
        self.init_ui()

    def init_ui(self):
        ana_widget = QWidget()
        ana_layout = QVBoxLayout()
        ana_widget.setLayout(ana_layout)
        self.setCentralWidget(ana_widget)

        # Başlık
        baslik = QLabel("Bagaj Güvenlik Simülatörü")
        baslik.setAlignment(Qt.AlignCenter)
        baslik.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 10px;")
        ana_layout.addWidget(baslik)

        # Üstte üç panel (Kuyruk, Stack, Kara Liste)
        ust_panel = QHBoxLayout()
        ana_layout.addLayout(ust_panel)

        # Yolcu Kuyruğu
        queue_frame = QFrame()
        queue_frame.setFrameShape(QFrame.StyledPanel)
        queue_layout = QVBoxLayout()
        queue_label = QLabel("Yolcu Kuyruğu")
        queue_label.setAlignment(Qt.AlignCenter)
        queue_label.setStyleSheet("font-weight: bold;")
        self.queue_list = QListWidget()
        queue_layout.addWidget(queue_label)
        queue_layout.addWidget(self.queue_list)
        queue_frame.setLayout(queue_layout)
        ust_panel.addWidget(queue_frame)

        # Bagaj Yığını
        stack_frame = QFrame()
        stack_frame.setFrameShape(QFrame.StyledPanel)
        stack_layout = QVBoxLayout()
        stack_label = QLabel("Bagaj Yığını")
        stack_label.setAlignment(Qt.AlignCenter)
        stack_label.setStyleSheet("font-weight: bold;")
        self.stack_list = QListWidget()
        stack_layout.addWidget(stack_label)
        stack_layout.addWidget(self.stack_list)
        stack_frame.setLayout(stack_layout)
        ust_panel.addWidget(stack_frame)

        # Kara Liste
        blacklist_frame = QFrame()
        blacklist_frame.setFrameShape(QFrame.StyledPanel)
        blacklist_layout = QVBoxLayout()
        blacklist_label = QLabel("Kara Liste")
        blacklist_label.setAlignment(Qt.AlignCenter)
        blacklist_label.setStyleSheet("font-weight: bold;")
        self.blacklist_list = QListWidget()
        blacklist_layout.addWidget(blacklist_label)
        blacklist_layout.addWidget(self.blacklist_list)
        blacklist_frame.setLayout(blacklist_layout)
        ust_panel.addWidget(blacklist_frame)

        # Log Paneli
        log_label = QLabel("Log")
        log_label.setStyleSheet("font-weight: bold; margin-top: 10px;")
        ana_layout.addWidget(log_label)
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setFixedHeight(80)
        ana_layout.addWidget(self.log_text)

        # Alt butonlar
        buton_panel = QHBoxLayout()
        self.btn_new_passenger = QPushButton("Yeni Yolcu")
        self.btn_new_passenger.clicked.connect(self.yolcu_ekle)
        buton_panel.addWidget(self.btn_new_passenger)
        self.btn_load_data = QPushButton("Veri Yükle")
        self.btn_load_data.clicked.connect(self.load_data)
        buton_panel.addWidget(self.btn_load_data)
        self.btn_start_sim = QPushButton("Simülasyonu Başlat")
        self.btn_start_sim.clicked.connect(self.simulasyonu_baslat)
        buton_panel.addWidget(self.btn_start_sim)
        self.btn_report = QPushButton("Gün Sonu Raporu")
        self.btn_report.clicked.connect(self.rapor_goster)
        buton_panel.addWidget(self.btn_report)
        ana_layout.addLayout(buton_panel)

        self.guncelle_paneller()

    def log_yaz(self, mesaj):
        self.log_text.append(mesaj)

    def guncelle_paneller(self):
        # Kuyruk
        self.queue_list.clear()
        for yolcu in sim.kuyruk.tum_yolcular():
            self.queue_list.addItem(f"{yolcu.id}")
        # Stack (her bagaj için başlık ve altına eşyalar)
        self.stack_list.clear()
        for bagaj, yolcu_id in sim.stack.tum_bagajlar():
            baslik_item = QListWidgetItem(f"{yolcu_id} Bagajı")
            baslik_item.setFlags(baslik_item.flags() & ~Qt.ItemIsSelectable)
            baslik_item.setBackground(Qt.darkGray)
            baslik_item.setForeground(Qt.white)
            font = baslik_item.font()
            font.setBold(True)
            baslik_item.setFont(font)
            self.stack_list.addItem(baslik_item)
            for esya in bagaj.esyalar:
                item = QListWidgetItem(f"   {esya.isim.capitalize()}")
                if esya.tehlikeli:
                    item.setBackground(Qt.red)
                    item.setForeground(Qt.white)
                self.stack_list.addItem(item)
        # Kara Liste
        self.blacklist_list.clear()
        for yolcu_id, _ in sim.kara_liste.tum_yolcular():
            self.blacklist_list.addItem(f"ID: {yolcu_id.split('#')[-1]}")

    def yolcu_ekle(self):
        yolcu = sim.yolcu_ekle()
        self.log_yaz(f"{yolcu.id} kuyruğa eklendi.")
        self.guncelle_paneller()

    def load_data(self):
        for _ in range(30):
            sim.yolcu_ekle()
        self.log_yaz("30 yolcu yüklendi.")
        self.guncelle_paneller()

    def simulasyonu_baslat(self):
        yolcu = sim.kuyruk.kuyruk[0] if not sim.kuyruk.is_empty() else None
        sim.simulasyonu_baslat()
        if yolcu:
            if any(esya.tehlikeli for bagaj in yolcu.bagajlar for esya in bagaj.esyalar):
                self.log_yaz(f"{yolcu.id} → Şüpheli eşya tespit edildi! Alarm verildi.")
            else:
                self.log_yaz(f"{yolcu.id} → Geçiş yaptı.")
        self.guncelle_paneller()

    def rapor_goster(self):
        self.log_yaz("<b>--- GÜN SONU RAPORU ---</b>")
        self.log_yaz(f"<b>Kontrolden geçen yolcu: {sim.kontrolden_gecen_yolcu}</b>")
        self.log_yaz(f"Alarm sayısı: {sim.alarm_sayisi}")
        self.log_yaz(f"Kara listede yakalananlar: {[k[0] for k in sim.kara_liste.tum_yolcular()]}")
        temizler = sim.temiz_gecen_yolculari_getir()
        self.log_yaz(f"Temiz geçen yolcular: {len(temizler)}")
        self.log_yaz(f"Stack'e alınan bagaj sayısı: {sim.stack.size()}")
        self.log_yaz("--- Risk Puanları ---")
        for y in sim.kontrolden_gecen_yolcular:
            self.log_yaz(f"{y.id}: Risk puanı = {y.risk}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = MainWindow()
    pencere.show()
    sys.exit(app.exec_())
