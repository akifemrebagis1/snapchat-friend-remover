import subprocess
import time

# ==================== AYARLAR ====================
# Cihaz ID'nizi buraya girin (adb devices komutuyla öğrenebilirsiniz)
DEVICE = "YOUR_DEVICE_ID"

# ADB yolu (Windows için varsayılan)
ADB_PATH = r"C:\Users\YOUR_USERNAME\AppData\Local\Android\Sdk\platform-tools\adb.exe"
# Linux/Mac için: ADB_PATH = "adb"

# ==================== KOORDİNATLAR ====================
# Bu koordinatlar cihazınıza göre değişir!
# Kendi cihazınız için koordinatları tespit etmeniz gerekir
# Ekran görüntüsü alıp Paint'te koordinatları bulabilirsiniz

LONG_PRESS_X, LONG_PRESS_Y = 476, 1721   # Sohbet listesinde arkadaşa uzun bas
STEP2_X, STEP2_Y = 540, 1146              # Menüden "Arkadaşlık Ayarları" veya benzeri
STEP3_X, STEP3_Y = 264, 1796              # "Arkadaşı Kaldır" butonu
STEP4_X, STEP4_Y = 532, 1214              # Onay popup'ındaki "Kaldır" butonu

# Hız ayarı (saniye)
FAST_DELAY = 0.1
STEP3_DELAY = 1  # 3. adımdan sonra popup bekle
FINAL_DELAY = 4  # Son işlem sonrası bekleme

def adb(cmd):
    """ADB komutu çalıştır"""
    full_cmd = f'"{ADB_PATH}" -s {DEVICE} {cmd}'
    result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True, encoding='utf-8', errors='ignore')
    return result.stdout.strip()

def tap(x, y):
    """Ekrana tıkla"""
    adb(f"shell input tap {x} {y}")

def long_press(x, y, duration=1000):
    """Uzun bas"""
    adb(f"shell input swipe {x} {y} {x} {y} {duration}")

def remove_friend():
    """Bir arkadaşı sil"""
    # 1. Uzun bas
    long_press(LONG_PRESS_X, LONG_PRESS_Y)
    time.sleep(FAST_DELAY)
    
    # 2. Tıkla
    tap(STEP2_X, STEP2_Y)
    time.sleep(FAST_DELAY)
    
    # 3. Tıkla
    tap(STEP3_X, STEP3_Y)
    time.sleep(STEP3_DELAY)  # Popup açılmasını bekle
    
    # 4. Onay
    tap(STEP4_X, STEP4_Y)
    time.sleep(FINAL_DELAY)

def main():
    print("=" * 40)
    print("SNAPCHAT ARKADAŞ SİLME BOTU")
    print("=" * 40)
    
    print("\n[!] ÖNEMLİ: Sohbet listesini EN ALTA kaydırdığınızdan emin olun!")
    print("[!] Bot en alttaki kişiden başlayarak yukarı doğru siler.\n")
    
    count = int(input("Kaç arkadaş silinsin? "))
    print(f"\n{count} arkadaş silinecek...")
    print("Listeyi en alta kaydırdıysanız 5 saniye içinde başlıyor...\n")
    time.sleep(5)
    
    for i in range(count):
        print(f"[{i+1}/{count}] Siliniyor...")
        remove_friend()
        print(f"[{i+1}/{count}] Silindi!")
    
    print("\n" + "=" * 40)
    print(f"TAMAMLANDI! {count} arkadaş silindi.")
    print("=" * 40)

if __name__ == "__main__":
    main()
