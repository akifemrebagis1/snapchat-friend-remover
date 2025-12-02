# 📖 Detaylı Kurulum Rehberi

Bu rehber, Snapchat Friend Remover Bot'un kurulumunu adım adım anlatır.

---

## 📱 ADB Modu Kurulumu (Önerilen)

### 1. Android SDK Kurulumu

#### Windows
1. [Android Studio](https://developer.android.com/studio) indirin ve kurun
2. SDK Manager'dan "Android SDK Platform-Tools" yükleyin
3. ADB yolu genellikle: `C:\Users\KULLANICI_ADI\AppData\Local\Android\Sdk\platform-tools\`

#### Linux
```bash
sudo apt install android-tools-adb
```

#### macOS
```bash
brew install android-platform-tools
```

### 2. Telefon Ayarları

1. **Geliştirici Seçeneklerini Açın:**
   - Ayarlar > Telefon Hakkında > Yapı Numarası'na 7 kez tıklayın

2. **USB Debugging'i Açın:**
   - Ayarlar > Geliştirici Seçenekleri > USB Debugging ✓

3. **Güvenlik Ayarı (Önemli!):**
   - Ayarlar > Geliştirici Seçenekleri > USB debugging (Security settings) ✓
   - Bu ayar olmadan bot tıklama yapamaz!

### 3. Bağlantı Testi

```bash
# Cihaz bağlı mı kontrol et
adb devices

# Çıktı şöyle olmalı:
# List of devices attached
# ABC123XYZ    device
```

### 4. Koordinat Tespiti

```bash
# Ekran görüntüsü al
adb shell screencap -p /sdcard/screen.png
adb pull /sdcard/screen.png

# Görüntüyü aç ve koordinatları tespit et
```

### 5. Konfigürasyon

`snapchat_sil.py` dosyasını düzenleyin:

```python
# Cihaz ID'nizi girin
DEVICE = "ABC123XYZ"

# ADB yolunu girin
ADB_PATH = r"C:\Users\KULLANICI_ADI\AppData\Local\Android\Sdk\platform-tools\adb.exe"

# Koordinatları cihazınıza göre ayarlayın
LONG_PRESS_X, LONG_PRESS_Y = 476, 1721
STEP2_X, STEP2_Y = 540, 1146
STEP3_X, STEP3_Y = 264, 1796
STEP4_X, STEP4_Y = 532, 1214
```

### 6. Çalıştırma

```bash
python snapchat_sil.py
```

---

## 🖥️ Appium Modu Kurulumu (Emulator)

### 1. Node.js Kurulumu

[Node.js](https://nodejs.org/) indirin ve kurun (LTS sürümü önerilir).

### 2. Appium Kurulumu

```bash
npm install -g appium
appium driver install uiautomator2
```

### 3. Android Emulator Kurulumu

1. Android Studio'yu açın
2. AVD Manager'dan yeni bir emulator oluşturun
3. API Level 30+ önerilir

### 4. Snapchat APK Kurulumu

Emulator'e Snapchat yükleyin:
```bash
adb install snapchat.apk
```

### 5. Appium Server'ı Başlatın

```bash
appium
```

### 6. Python Bağımlılıklarını Yükleyin

```bash
pip install -r requirements.txt
```

### 7. Bot'u Çalıştırın

```bash
python bot.py
```

---

## ⚠️ Önemli Notlar

### Snapchat Bot Algılama

Snapchat, bot aktivitelerini algılayabilir ve hesabınızı kilitleyebilir:

- ❌ Emulator kullanmak risklidir
- ✅ Gerçek telefon kullanın
- ✅ Bekleme sürelerini artırın
- ✅ Çok fazla arkadaş silmeyin (günlük limit)

### Koordinat Değişiklikleri

Snapchat güncellendikçe UI değişebilir. Koordinatları tekrar tespit etmeniz gerekebilir.

### Hız Ayarları

Daha güvenli kullanım için `snapchat_sil.py` dosyasındaki bekleme sürelerini artırın:

```python
FAST_DELAY = 0.5      # Her adım arası (varsayılan: 0.1)
STEP3_DELAY = 2       # Popup bekleme (varsayılan: 1)
FINAL_DELAY = 5       # Son işlem sonrası (varsayılan: 4)
```

---

## 🔧 Sorun Giderme

### "Permission denied" hatası
- USB debugging (Security settings) açık mı kontrol edin
- Telefonda "Bu bilgisayara güven" onayı verin

### Tıklamalar yanlış yere gidiyor
- Koordinatları tekrar tespit edin
- Ekran çözünürlüğünüzü kontrol edin

### Appium bağlanamıyor
- Appium server çalışıyor mu? (`appium`)
- Emulator açık mı?
- Port 4723 kullanılabilir mi?

### Snapchat açılmıyor
- Emulator'de Google Play Services kurulu mu?
- Snapchat sürümü güncel mi?

---

## 📞 Destek

Sorunlarınız için GitHub Issues kullanın.
