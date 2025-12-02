#!/usr/bin/env python3
"""
Snapchat Friend Remover Bot - ADB Mode
Snapchat Arkadaş Silme Botu - ADB Modu

TR: Gerçek telefonda ADB kullanarak arkadaş siler
EN: Removes friends using ADB on real phone
"""

import subprocess
import time

# ==================== AYARLAR / SETTINGS ====================
# TR: Cihaz ID'nizi buraya girin (adb devices komutuyla öğrenebilirsiniz)
# EN: Enter your device ID here (find with 'adb devices' command)
DEVICE = "YOUR_DEVICE_ID"

# TR: ADB yolu (Windows için varsayılan)
# EN: ADB path (default for Windows)
ADB_PATH = r"C:\Users\YOUR_USERNAME\AppData\Local\Android\Sdk\platform-tools\adb.exe"
# Linux/Mac: ADB_PATH = "adb"

# ==================== KOORDİNATLAR / COORDINATES ====================
# TR: Bu koordinatlar cihazınıza göre değişir! Ekran görüntüsü alıp Paint'te koordinatları bulabilirsiniz.
# EN: These coordinates vary by device! Take a screenshot and find coordinates in Paint.

LONG_PRESS_X, LONG_PRESS_Y = 476, 1721   # TR: Uzun bas / EN: Long press on friend
STEP2_X, STEP2_Y = 540, 1146              # TR: Menü seçeneği / EN: Menu option
STEP3_X, STEP3_Y = 264, 1796              # TR: Arkadaşı Kaldır / EN: Remove Friend button
STEP4_X, STEP4_Y = 532, 1214              # TR: Onay butonu / EN: Confirm button

# TR: Hız ayarı (saniye) / EN: Speed settings (seconds)
FAST_DELAY = 0.1          # TR: Adımlar arası / EN: Between steps
STEP3_DELAY = 1           # TR: Popup bekleme / EN: Wait for popup
FINAL_DELAY = 4           # TR: Son işlem sonrası / EN: After final step

def adb(cmd):
    """TR: ADB komutu çalıştır / EN: Run ADB command"""
    full_cmd = f'"{ADB_PATH}" -s {DEVICE} {cmd}'
    result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True, encoding='utf-8', errors='ignore')
    return result.stdout.strip()

def tap(x, y):
    """TR: Ekrana tıkla / EN: Tap on screen"""
    adb(f"shell input tap {x} {y}")

def long_press(x, y, duration=1000):
    """TR: Uzun bas / EN: Long press"""
    adb(f"shell input swipe {x} {y} {x} {y} {duration}")

def remove_friend():
    """TR: Bir arkadaşı sil / EN: Remove a friend"""
    # 1. TR: Uzun bas / EN: Long press
    long_press(LONG_PRESS_X, LONG_PRESS_Y)
    time.sleep(FAST_DELAY)
    
    # 2. TR: Menü seçeneği / EN: Menu option
    tap(STEP2_X, STEP2_Y)
    time.sleep(FAST_DELAY)
    
    # 3. TR: Arkadaşı kaldır / EN: Remove friend
    tap(STEP3_X, STEP3_Y)
    time.sleep(STEP3_DELAY)  # TR: Popup bekle / EN: Wait for popup
    
    # 4. TR: Onay / EN: Confirm
    tap(STEP4_X, STEP4_Y)
    time.sleep(FINAL_DELAY)

def main():
    print("=" * 40)
    print("SNAPCHAT FRIEND REMOVER BOT")
    print("SNAPCHAT ARKADAŞ SİLME BOTU")
    print("=" * 40)
    
    print("\n[!] TR: ÖNEMLİ: Sohbet listesini EN ALTA kaydırdığınızdan emin olun!")
    print("[!] EN: IMPORTANT: Make sure you scrolled chat list to the BOTTOM!")
    print("[!] TR: Bot en alttaki kişiden başlayarak yukarı doğru siler.")
    print("[!] EN: Bot removes from bottom to top.\n")
    
    count = int(input("TR: Kaç arkadaş silinsin? / EN: How many friends to remove? "))
    print(f"\nTR: {count} arkadaş silinecek... / EN: {count} friends will be removed...")
    print("TR: 5 saniye içinde başlıyor... / EN: Starting in 5 seconds...\n")
    time.sleep(5)
    
    for i in range(count):
        print(f"[{i+1}/{count}] Siliniyor...")
        remove_friend()
        print(f"[{i+1}/{count}] Silindi!")
    
    print("\n" + "=" * 40)
    print(f"TR: TAMAMLANDI! {count} arkadaş silindi.")
    print(f"EN: COMPLETED! {count} friends removed.")
    print("=" * 40)

if __name__ == "__main__":
    main()
