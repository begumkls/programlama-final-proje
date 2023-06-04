from Insan import Insan # Insna sınıfı import edildi

class Issiz(Insan): # Insna sınıfından türerilen Issiz sınıfı oluşturuldu
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, statu, tecrubeler):
        super().__init__(tc_no, ad, soyad, yas,cinsiyet, uyruk)
        self.__tecrubeler = tecrubeler
        self.__statu = self.statu_bul()
    
    # değişkenlerin kontrolünü sağlayan get/set fonksiyonları oluşturuldu
    def get_tecrubeler(self):
        return self.__tecrubeler
    
    def set_tecrubeler(self, tecrubeler):
        self.__tecrubeler = tecrubeler
        
    def get_statu(self):
        return self.__statu
    
    # Issiz sınıfındaki verilerden uygun statü ataması yapan fonksiyon oluşturuldu
    def statu_bul(self):
        try:
            mavi_yaka = self.__tecrubeler.get("mavi yaka", 0)
            beyaz_yaka = self.__tecrubeler.get("beyaz yaka", 0)
            yonetici = self.__tecrubeler.get("yonetici", 0)
            
            mavi_yaka_etkisi = mavi_yaka * 0.2
            beyaz_yaka_etkisi = beyaz_yaka * 0.35
            yonetici_etkisi = yonetici * 0.45 
            
            max_etki = max(mavi_yaka_etkisi, beyaz_yaka_etkisi, yonetici_etkisi)
            
            if max_etki == mavi_yaka_etkisi:
                return "mavi yaka"
            elif max_etki == beyaz_yaka_etkisi:
                return "beyaz yaka"
            else:
                return "yonetici"
            
        except Exception as e: # oluşacak bir hatanın kontrolü try except blokları ile yapıldı
            print("Hata:", str(e))
            return None

    def __str__(self): # Ekrana bilgilerin yazdıırlmasını sağlayan str fonksiyonu oluşturuldu
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nUygun Statü: {self.get_statu()}"
