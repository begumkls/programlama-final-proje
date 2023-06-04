#Issiz.py
from Insan import Insan # Insan sınıfı import edildi

class Issiz(Insan): # Insan sınıfından türetilen Calisan sınıfı oluşturuldu
    # değişkenlerin sınıf içerisinde kullanımını sağlayan init fonksiyonu oluşturuldu
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, statu, tecrubeler):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk) #super() fonksiyonu üst sınıftaki özelliklerin kullanılmasını sağlar.
        self.__tecrubeler = tecrubeler
        self.__statu = self.statu_bul()

    # değişkenlerin kontrolünü sağlayan get/set fonksiyonları oluşturuldu
    def get_tecrubeler(self):
        return self.__tecrubeler

    def set_tecrubeler(self, tecrubeler):
        self.__tecrubeler = tecrubeler
        
    def get_statu(self):
        return self.__statu
    
    # tecrübelere göre uygun statü bulmaya yarayan fonksiyon oluşturuldu
    def statu_bul(self):
        try:
            mavi_yaka = self.__tecrubeler.get("mavi yaka", 0)
            beyaz_yaka = self.__tecrubeler.get("beyaz yaka", 0)
            yonetici = self.__tecrubeler.get("yönetici", 0)
            
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
            
        except Exception as e:
            print("Hata:", str(e))
            return None

    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nUygun Statü: {self.get_statu()}"
