from Calisan import Calisan # Calisan sınıfı import edildi
class BeyazYaka(Calisan): # Calisan sınıfından türetilen BeyazYaka sınıfı oluşturuldu
    # değişkenlerin sınıf içerisinde kullanımını sağlayan init fonksiyonu oluşturuldu
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube, maas, tesvik_primi, sektor=""):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi

    # değişkenlerin kontrolünü sağlayan get/set fonksiyonları oluşturuldu
    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    # zam hakkını hesaplayan fonksiyon if else fonksiyonları yardımıyla oluşturuldu
    def zam_hakki(self):
        try:
            maas = self.get_maas()
            tecrube = self.get_tecrube()

            if tecrube < 24:
                zam = self.__tesvik_primi
            elif tecrube >= 24 and tecrube <= 48 and maas < 15000:
                zam = (maas % tecrube) * 5 + self.__tesvik_primi
            elif tecrube > 48 and maas < 25000:
                zam = (maas % tecrube ) * 4 + self.__tesvik_primi
            else:
                zam = 0
            
            self.__yeni_maas = maas + zam
            
            if self.__yeni_maas == maas:
                self.__yeni_maas = maas
            else:
                return self.__yeni_maas
                
        except Exception as e: # oluşacak bir hatanın kontrolü try except blokları ile yapıldı
            print("Hata:", str(e))
            return None

    def __str__(self): # Ekrana bilgilerin yazdırılmasını sağlayan str fonksiyonu oluşturuldu
        self.zam_hakki()
        return f"\n\n------ Beyaz Yaka ------\nAd: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.get_tecrube()} Ay\nYeni maas: {self.__yeni_maas:.2f}"
