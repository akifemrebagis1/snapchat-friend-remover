# 🤖 Snapchat Friend Remover Bot

[🇹🇷 Türkçe](#-türkçe) | [🇬🇧 English](#-english)

---

# 🇹🇷 Türkçe

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
└── README.md          # Bu dosya
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

# 🇬🇧 English

A bot for bulk removing friends from Snapchat friend list. Supports two modes:

1. **ADB Mode** - Works on real phone using ADB (recommended)
2. **Appium Mode** - Works on Android Emulator with Appium

## ⚠️ Warning

This bot is for educational purposes only. Users are responsible for any consequences. It may violate Snapchat's terms of service and could result in account suspension.

## 📋 Features

- ✅ Bulk friend removal
- ✅ Real phone support (ADB)
- ✅ Emulator support (Appium)
- ✅ Adjustable speed
- ✅ Customizable coordinates

> **Note:** The bot does not auto-scroll. You must manually scroll the chat list to the bottom before starting. The bot removes friends from bottom to top.

---

## 🚀 Quick Start (ADB Mode)

### Requirements
- Python 3.8+
- Android SDK (ADB)
- Android phone with USB Debugging enabled

### Installation

```bash
# Clone the repo
git clone https://github.com/akifemrebagis1/snapchat-friend-remover.git
cd snapchat-friend-remover

# Install dependencies
pip install -r requirements.txt
```

### Usage

1. Enable USB Debugging on your phone
2. Connect phone to computer via USB
3. Edit settings in `snapchat_sil.py`:
   - `DEVICE` - Enter your device ID (find with `adb devices`)
   - `ADB_PATH` - Enter ADB path
   - Adjust coordinates for your device

4. Open Snapchat and go to chat list

5. **IMPORTANT:** Scroll chat list to the bottom (bot starts from the last person)

6. Run the bot:
```bash
python snapchat_sil.py
```

---

## 📱 Finding Coordinates

Since every device has different screen size, you need to find coordinates yourself:

1. Take a screenshot:
```bash
adb shell screencap -p /sdcard/screen.png
adb pull /sdcard/screen.png
```

2. Open the image in Paint or similar program
3. Note the cursor coordinates
4. Update coordinates in `snapchat_sil.py`

### Removal Flow
1. **LONG_PRESS** - Long press on a friend in chat list
2. **STEP2** - Select "Manage Friendship" from menu
3. **STEP3** - Click "Remove Friend" button
4. **STEP4** - Click "Remove" on confirmation popup

---

## 🖥️ Appium Mode (Emulator)

If you want to use emulator, use `bot.py`. See [SETUP.md](SETUP.md) for detailed setup.

```bash
python bot.py
```

---

## 🔧 Troubleshooting

### ADB can't find device
```bash
adb devices
```
If device not listed:
- Check if USB Debugging is enabled
- Try different USB cable
- Install ADB drivers on computer

### Taps not working
- Check coordinates
- Enable "USB debugging (Security settings)"
- Increase delay times

### Snapchat account locked
- Bot was detected, your account may be temporarily locked
- Increase delay times
- Use real phone instead of emulator

---

## 📄 License

MIT License - For educational purposes only.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.
