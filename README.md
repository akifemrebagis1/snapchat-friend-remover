# 👻 Snapchat Friend Remover

> Automate the removal of Snapchat friends using ADB or Appium — supports both real devices and emulators.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![ADB](https://img.shields.io/badge/ADB-34A853?style=for-the-badge&logo=android&logoColor=white)
![Appium](https://img.shields.io/badge/Appium-662D91?style=for-the-badge&logo=appium&logoColor=white)

---

## 🎯 What It Does

Bulk-remove Snapchat friends automatically. Two modes available:

| Mode | File | Device | Method |
|------|------|--------|--------|
| **ADB Mode** | `snapchat_sil.py` | Real phone via USB | Screen coordinate taps via ADB |
| **Appium Mode** | `bot.py` | Android Emulator | UI element automation via Appium |

---

## ✨ Features

- 🔄 **Batch removal** — process entire friend lists automatically
- 📱 **Dual mode** — works with both physical devices and emulators
- 🎯 **Coordinate-based ADB** — ultra-fast, no Appium dependency needed
- 🤖 **Appium integration** — reliable UI element detection for emulators
- ⚙️ **Configurable** — easy coordinate and device ID setup
- 📋 **Bilingual** — Turkish & English documentation

---

## 🚀 Quick Start

### ADB Mode (Real Phone)

```bash
# 1. Connect your phone via USB with USB debugging enabled
# 2. Find your device ID
adb devices

# 3. Update DEVICE and coordinates in snapchat_sil.py
# 4. Run
python snapchat_sil.py
```

### Appium Mode (Emulator)

```bash
# 1. Install requirements
pip install -r requirements.txt

# 2. Start Appium server
appium

# 3. Launch Android emulator with Snapchat installed
# 4. Run
python bot.py
```

---

## ⚙️ Configuration

Edit the coordinate values in `snapchat_sil.py` to match your device's screen:

```python
LONG_PRESS_X, LONG_PRESS_Y = 476, 1721   # Long press on friend
STEP2_X, STEP2_Y = 540, 1146              # Menu option
STEP3_X, STEP3_Y = 264, 1796              # Remove Friend button
STEP4_X, STEP4_Y = 532, 1214              # Confirm button
```

> 💡 **Tip:** Take a screenshot and use Paint/Preview to find the correct coordinates for your device resolution.

---

## 📋 Requirements

- Python 3.8+
- ADB (Android Debug Bridge) installed
- For Appium mode: Appium server + Android emulator

---

## ⚠️ Disclaimer

This tool is for **educational purposes only**. Use responsibly and in accordance with Snapchat's Terms of Service.

## 📄 License

MIT License
