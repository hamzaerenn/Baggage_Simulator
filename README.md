# 🧳 Havaalanı Bagaj Simülasyonu

Bu proje, bir havaalanı bagaj kontrol sisteminin simülasyonunu gerçekleştiren Python tabanlı bir uygulamadır. Sistem, yolcuların bagajlarını kontrol eder, tehlikeli eşyaları tespit eder ve risk analizi yapar.

## 🌟 Özellikler

- 🚶 Yolcu kuyruğu yönetimi
- 🎒 Bagaj kontrol sistemi
- ⚠️ Tehlikeli eşya tespiti
- 📋 Kara liste yönetimi
- 📊 Risk puanı hesaplama
- 📈 Detaylı raporlama
- 🖥️ Kullanıcı dostu arayüz

## 🛠️ Teknik Detaylar

Proje aşağıdaki veri yapılarını kullanmaktadır:

- **YolcuKuyrugu**: Yolcuların sırasını yönetir
- **BagajStack**: Bagajların kontrol sürecini yönetir
- **KaraListe**: Riskli yolcuları takip eder

## 📦 Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/kullanici/baggage_simulator.git
cd baggage_simulator
```

2. Gerekli bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

## 🚀 Kullanım

Programı çalıştırmak için:

```bash
python main.py
```

GUI arayüzünü kullanmak için:

```bash
python gui.py
```

## 📊 Sistem Parametreleri

- `TEMIZ_RISK_ESIK`: 2 (Temiz sayılacak risk puanı eşiği)
- `RISK_ESIK`: 2 (Kara liste için risk puanı eşiği)
- `KARA_LISTE_OLASILIK`: 0.5 (%50 olasılık)

## 📝 Proje Yapısı

```
baggage_simulator/
├── data/
│   └── kara_liste.json
├── models/
│   ├── yolcu.py
│   ├── queue.py
│   ├── stack.py
│   └── linkedlist.py
├── utils/
│   └── olasilik.py
├── gui.py
├── main.py
└── README.md
```

## 🤝 Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik: X'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun

## 📜 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 👥 İletişim

Sorularınız veya önerileriniz için lütfen bir issue açın veya pull request gönderin. 