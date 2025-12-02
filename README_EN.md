# 🤖 Snapchat Friend Remover Bot

**🇬🇧 English** | **🇹🇷 [Türkçe](README.md)**

---

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

## 📁 File Structure

```
├── snapchat_sil.py    # ADB mode (real phone)
├── bot.py             # Appium mode (emulator)
├── requirements.txt   # Python dependencies
├── KURULUM.md         # Detailed setup guide (TR)
├── SETUP.md           # Detailed setup guide (EN)
├── README.md          # Turkish README
└── README_EN.md       # English README
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
