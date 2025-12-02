#!/usr/bin/env python3
"""
Snapchat Bot - Appium/Emulator Modu
Appium ve Android Emulator kullanarak çalışır
"""

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

# Test verileri
TEST_FRIENDS = [
    "ahmetali", "betul", "caner", "deniz", "emre",
    "fatih", "gokhan", "huseyin", "ilhan", "jale",
    "kaan", "levent", "mehmet", "nuray", "ozer"
]

class SnapchatBot:
    def __init__(self, test_mode=False):
        self.driver = None
        self.wait = None
        self.test_mode = test_mode
        
        if not test_mode:
            self.setup_driver()
    
    def setup_driver(self):
        """Appium driver'ı başlat"""
        try:
            logger.info("Appium'a bağlanılıyor...")
            
            options = UiAutomator2Options()
            options.platform_name = "Android"
            options.automation_name = "UiAutomator2"
            options.app_package = "com.snapchat.android"
            options.app_activity = "com.snap.mushroom.MainActivity"
            options.no_reset = True
            
            self.driver = webdriver.Remote("http://localhost:4723", options=options)
            self.wait = WebDriverWait(self.driver, 10)
            
            logger.info("✓ Appium bağlantı başarılı")
            
        except Exception as e:
            logger.error(f"✗ Appium hatası: {e}")
            logger.error("Kontrol et: Appium server + Emulator + Snapchat app")
            raise
    
    def login(self, username: str, password: str) -> bool:
        """Demo: Giriş simülasyonu"""
        if self.test_mode:
            logger.info(f"[DEMO] '{username}' ile giriş...")
            time.sleep(1)
            logger.info("✓ Giriş başarılı (demo)")
            return True
        
        try:
            logger.info(f"Giriş yapılıyor: {username}")
            
            time.sleep(3)
            
            # Username - ilk EditText
            username_field = self.wait.until(
                EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText"))
            )
            username_field.clear()
            username_field.send_keys(username)
            logger.info("Kullanıcı adı girildi")
            time.sleep(0.5)
            
            # Password - ikinci EditText
            edit_texts = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
            if len(edit_texts) > 1:
                edit_texts[1].clear()
                edit_texts[1].send_keys(password)
                logger.info("Şifre girildi")
            time.sleep(0.5)
            
            # Login button
            buttons = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")
            for btn in buttons:
                btn_text = (btn.text or "").upper()
                if "LOG" in btn_text or "GIR" in btn_text:
                    btn.click()
                    logger.info("Giriş butonuna tıklandı")
                    break
            
            time.sleep(5)
            logger.info("✓ Giriş başarılı")
            return True
            
        except Exception as e:
            logger.error(f"✗ Giriş hatası: {e}")
            return False
    
    def navigate_to_friends(self) -> bool:
        """Demo: Arkadaş listesine gitme"""
        if self.test_mode:
            logger.info("[DEMO] Arkadaş listesine gidiliyor...")
            time.sleep(1)
            logger.info("✓ Arkadaş listesi açıldı (demo)")
            return True
        
        try:
            logger.info("Arkadaş listesine gidiliyor...")
            
            # Tab veya buton ara
            elements = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageButton")
            for elem in elements:
                desc = elem.get_attribute("content-desc") or ""
                if "friend" in desc.lower():
                    elem.click()
                    time.sleep(2)
                    logger.info("✓ Arkadaş listesi açıldı")
                    return True
            
            logger.warning("⚠ Arkadaş listesi tab'ı bulunamadı")
            return False
            
        except Exception as e:
            logger.error(f"✗ Hata: {e}")
            return False
    
    def get_friends(self) -> list:
        """Demo: Arkadaş listesi"""
        if self.test_mode:
            logger.info(f"[DEMO] {len(TEST_FRIENDS)} test arkadaşı yükleniyor...")
            time.sleep(1)
            return TEST_FRIENDS
        
        try:
            logger.info("Arkadaş listesi taranıyor...")
            
            friends = []
            elements = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
            
            for elem in elements:
                text = elem.get_attribute("text") or ""
                if text and len(text) < 30 and text.strip():
                    friends.append(text)
            
            friends = list(dict.fromkeys(friends))  # Duplikasyonları kaldır
            
            if friends:
                logger.info(f"✓ {len(friends)} arkadaş bulundu")
                return friends
            else:
                logger.warning("Arkadaş bulunamadı")
                return []
                
        except Exception as e:
            logger.error(f"✗ Hata: {e}")
            return []
    
    def remove_friend(self, friend_name: str) -> bool:
        """Demo: Arkadaş silme"""
        if self.test_mode:
            logger.info(f"[DEMO] '{friend_name}' siliniyor...")
            time.sleep(0.3)
            return True
        
        try:
            # Long-press
            friend_elem = self.driver.find_element(
                AppiumBy.XPATH, 
                f"//android.widget.TextView[@text='{friend_name}']"
            )
            
            actions = ActionChains(self.driver)
            actions.long_press(friend_elem).perform()
            time.sleep(0.5)
            
            # Sil seçeneği
            delete_option = self.wait.until(
                EC.presence_of_element_located((AppiumBy.XPATH, "//*[contains(@text, 'Remove')]"))
            )
            delete_option.click()
            
            time.sleep(0.5)
            
            # Onay
            buttons = self.driver.find_elements(AppiumBy.TAG_NAME, "android.widget.Button")
            for btn in buttons:
                desc = btn.get_attribute("content-desc") or ""
                btn_text = btn.text.upper()
                if "remove" in desc.lower() or "remove" in btn_text:
                    btn.click()
                    break
            
            logger.info(f"✓ '{friend_name}' silindi")
            return True
            
        except Exception as e:
            logger.warning(f"⚠ '{friend_name}' silinemedi: {e}")
            return False
    
    def run(self, username: str, password: str, count: int):
        """Bot'u çalıştır"""
        try:
            if not self.login(username, password):
                logger.error("Giriş başarısız!")
                return
            
            if not self.navigate_to_friends():
                logger.error("Arkadaş listesine gidilemedi!")
                return
            
            friends = self.get_friends()
            
            if not friends:
                logger.error("Arkadaş bulunamadı!")
                return
            
            if count > len(friends):
                count = len(friends)
            
            logger.info("="*50)
            logger.info(f"BAŞLANACAK: {count} arkadaş silinecek")
            logger.info("="*50)
            
            removed = 0
            for i in range(count):
                friend = friends[-(i+1)]
                if self.remove_friend(friend):
                    removed += 1
            
            print("\n" + "="*50)
            logger.info(f"✓ İşlem tamamlandı!")
            logger.info(f"Silinen: {removed}/{count}")
            logger.info(f"Başarı: %{(removed/count)*100:.1f}")
            print("="*50 + "\n")
            
        except KeyboardInterrupt:
            logger.warning("İşlem durduruldu")
        except Exception as e:
            logger.error(f"Hata: {e}")
            import traceback
            traceback.print_exc()
        finally:
            if self.driver:
                self.driver.quit()


def main():
    print("\n" + "="*60)
    print("        ⚡ SNAPCHAT ARKADAŞ SİLME BOT")
    print("="*60)
    
    print("\n[!] Mod seçin:")
    print("  1. DEMO - Test verisiyle çalış (hızlı test)")
    print("  2. GERÇEK - Gerçek Snapchat uygulamasında çalıştır")
    
    mode = input("\n[?] Seç (1/2): ").strip()
    
    is_demo = mode == "1"
    
    if is_demo:
        print("\n[*] DEMO MODU başlatılıyor...")
        print(f"[*] Test arkadaşları: {', '.join(TEST_FRIENDS[:5])}...\n")
        
        bot = SnapchatBot(test_mode=True)
        bot.run("test_user", "test_pass", 5)
    
    else:
        print("\n" + "-"*60)
        print("[!] Ön Kontroller:")
        print("  ✓ Android Studio/Emulator açık mı?")
        print("  ✓ Appium Server çalışıyor mu? (appium)")
        print("  ✓ Snapchat uygulaması yüklü mü?")
        print("-"*60)
        
        username = input("\n[?] Snapchat Kullanıcı Adı: ").strip()
        password = input("[?] Snapchat Şifresi: ").strip()
        count_str = input("[?] Silinecek Arkadaş Sayısı: ").strip()
        
        if not username or not password or not count_str:
            logger.error("Eksik bilgi!")
            return
        
        try:
            count = int(count_str)
            if count <= 0:
                raise ValueError()
        except:
            logger.error("Geçersiz sayı!")
            return
        
        print("\n" + "-"*60)
        confirm = "EVET"
        
        if confirm != "EVET":
            logger.info("İptal edildi")
            return
        
        print()
        bot = SnapchatBot(test_mode=False)
        bot.run(username, password, count)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] İptal edildi")
