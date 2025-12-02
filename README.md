# 🤖 Snapchat Friend Remover Bot

**🇬🇧 [English](README_EN.md)** | **🇹🇷 Türkçe**

---

Snapchat arkadaş listesinden toplu arkadaş silme botu. İki farklı mod destekler:

1. **ADB Modu** - Gerçek telefonda ADB kullanarak çalışır (önerilen)
2. **Appium Modu** - Android Emulator üzerinde Appium ile çalışır

## ⚠️ Uyarı

Bu bot eğitim amaçlıdır. Kullanımından doğacak sonuçlardan kullanıcı sorumludur. Snapchat'in kullanım şartlarını ihlal edebilir ve hesabınızın askıya alınmasına neden olabilir.

## 📋 Özellikler

- ✅ Toplu arkadaş silme
- ✅ Gerçek telefon desteği (ADB)
- ✅ Emulator desteği (Appium)
- ✅ Ayarlanabilir hız
- ✅ Özelleştirilebilir koordinatlar

> **Not:** Bot otomatik kaydırma yapmaz. Silme işlemi başlamadan önce sohbet listesini en alta kendiniz kaydırmalısınız. Bot en alttaki kişiden başlayarak yukarı doğru siler.

---

## 🚀 Hızlı Başlangıç (ADB Modu)

### Gereksinimler
- Python 3.8+
- Android SDK (ADB)
- USB Debugging aktif Android telefon

### Kurulum

```bash
# Repoyu klonla
git clone https://github.com/akifemrebagis1/snapchat-friend-remover.git
cd snapchat-friend-remover

# Bağımlılıkları yükle
pip install -r requirements.txt
```

### Kullanım

1. Telefonunuzda USB Debugging'i açın
2. Telefonu USB ile bilgisayara bağlayın
3. `snapchat_sil.py` dosyasındaki ayarları düzenleyin:
   - `DEVICE` - Cihaz ID'nizi girin (`adb devices` komutuyla öğrenin)
   - `ADB_PATH` - ADB yolunu girin
   - Koordinatları cihazınıza göre ayarlayın

4. Snapchat'i açın ve sohbet listesine gidin

5. **ÖNEMLİ:** Sohbet listesini en alta kaydırın (bot en alttaki kişiden başlar)

6. Botu çalıştırın:
```bash
python snapchat_sil.py
```

---

## 📱 Koordinat Tespiti

Her cihazın ekran boyutu farklı olduğundan koordinatları kendiniz belirlemelisiniz:

1. Ekran görüntüsü alın:
```bash
adb shell screencap -p /sdcard/screen.png
adb pull /sdcard/screen.png
```

2. Görüntüyü Paint veya benzeri bir programda açın
3. İmleç koordinatlarını not alın
4. `snapchat_sil.py` dosyasındaki koordinatları güncelleyin

### Silme Akışı
1. **LONG_PRESS** - Sohbet listesinde bir arkadaşa uzun basın
2. **STEP2** - Açılan menüden "Arkadaşlık Ayarları" seçin
3. **STEP3** - "Arkadaşı Kaldır" butonuna tıklayın
4. **STEP4** - Onay popup'ında "Kaldır" butonuna tıklayın

---

## 🖥️ Appium Modu (Emulator)

Emulator kullanmak istiyorsanız `bot.py` dosyasını kullanın. Detaylı kurulum için [KURULUM.md](KURULUM.md) dosyasına bakın.

```bash
python bot.py
```

---

## 📁 Dosya Yapısı

```
├── snapchat_sil.py    # ADB modu (gerçek telefon)
├── bot.py             # Appium modu (emulator)
├── requirements.txt   # Python bağımlılıkları
├── KURULUM.md         # Detaylı kurulum rehberi (TR)
├── SETUP.md           # Detailed setup guide (EN)
├── README.md          # Türkçe README
└── README_EN.md       # English README
```

---

## 🔧 Sorun Giderme

### ADB cihazı bulamıyor
```bash
adb devices
```
Cihaz listede görünmüyorsa:
- USB Debugging açık mı kontrol edin
- USB kablosunu değiştirin
- Bilgisayarda ADB sürücülerini yükleyin

### Tıklamalar çalışmıyor
- Koordinatları kontrol edin
- "USB debugging (Security settings)" seçeneğini açın
- Bekleme sürelerini artırın

### Snapchat hesap kilitlendi
- Bot algılandı, hesabınız geçici olarak kilitlenmiş olabilir
- Bekleme sürelerini artırın
- Emulator yerine gerçek telefon kullanın

---

## 📄 Lisans

MIT License - Eğitim amaçlıdır.

---

## 🤝 Katkıda Bulunma

Pull request'ler kabul edilir. Büyük değişiklikler için önce bir issue açın.
