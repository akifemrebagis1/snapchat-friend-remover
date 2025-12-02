# 📖 Detailed Setup Guide

This guide explains the installation of Snapchat Friend Remover Bot step by step.

---

## 📱 ADB Mode Setup (Recommended)

### 1. Android SDK Installation

#### Windows
1. Download and install [Android Studio](https://developer.android.com/studio)
2. Install "Android SDK Platform-Tools" from SDK Manager
3. ADB path is usually: `C:\Users\USERNAME\AppData\Local\Android\Sdk\platform-tools\`

#### Linux
```bash
sudo apt install android-tools-adb
```

#### macOS
```bash
brew install android-platform-tools
```

### 2. Phone Settings

1. **Enable Developer Options:**
   - Settings > About Phone > Tap Build Number 7 times

2. **Enable USB Debugging:**
   - Settings > Developer Options > USB Debugging ✓

3. **Security Setting (Important!):**
   - Settings > Developer Options > USB debugging (Security settings) ✓
   - Without this setting, the bot cannot perform taps!

### 3. Connection Test

```bash
# Check if device is connected
adb devices

# Output should be like:
# List of devices attached
# ABC123XYZ    device
```

### 4. Finding Coordinates

```bash
# Take screenshot
adb shell screencap -p /sdcard/screen.png
adb pull /sdcard/screen.png

# Open image and find coordinates
```

### 5. Configuration

Edit `snapchat_sil.py`:

```python
# Enter your device ID
DEVICE = "ABC123XYZ"

# Enter ADB path
ADB_PATH = r"C:\Users\USERNAME\AppData\Local\Android\Sdk\platform-tools\adb.exe"

# Adjust coordinates for your device
LONG_PRESS_X, LONG_PRESS_Y = 476, 1721
STEP2_X, STEP2_Y = 540, 1146
STEP3_X, STEP3_Y = 264, 1796
STEP4_X, STEP4_Y = 532, 1214
```

### 6. Running

```bash
python snapchat_sil.py
```

---

## 🖥️ Appium Mode Setup (Emulator)

### 1. Node.js Installation

Download and install [Node.js](https://nodejs.org/) (LTS version recommended).

### 2. Appium Installation

```bash
npm install -g appium
appium driver install uiautomator2
```

### 3. Android Emulator Setup

1. Open Android Studio
2. Create a new emulator from AVD Manager
3. API Level 30+ recommended

### 4. Install Snapchat APK

Install Snapchat on emulator:
```bash
adb install snapchat.apk
```

### 5. Start Appium Server

```bash
appium
```

### 6. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 7. Run the Bot

```bash
python bot.py
```

---

## ⚠️ Important Notes

### Snapchat Bot Detection

Snapchat can detect bot activity and may lock your account:

- ❌ Using emulator is risky
- ✅ Use real phone
- ✅ Increase delay times
- ✅ Don't remove too many friends (daily limit)

### Coordinate Changes

As Snapchat updates, UI may change. You may need to find coordinates again.

### Speed Settings

For safer usage, increase delay times in `snapchat_sil.py`:

```python
FAST_DELAY = 0.5      # Between each step (default: 0.1)
STEP3_DELAY = 2       # Wait for popup (default: 1)
FINAL_DELAY = 5       # After final step (default: 4)
```

---

## 🔧 Troubleshooting

### "Permission denied" error
- Check if USB debugging (Security settings) is enabled
- Grant "Trust this computer" permission on phone

### Taps going to wrong location
- Find coordinates again
- Check your screen resolution

### Appium can't connect
- Is Appium server running? (`appium`)
- Is emulator open?
- Is port 4723 available?

### Snapchat won't open
- Is Google Play Services installed on emulator?
- Is Snapchat version up to date?

---

## 📞 Support

For issues, use GitHub Issues.
