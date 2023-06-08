from Calisan import Calisan # Calisan sınıfı import edildi

class MaviYaka(Calisan): # Calisan sınıfından türerilen MaviYaka sınıfı oluşturuldu
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube, maas, yipranma_payi, sektor=""):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tecrube = tecrube
        self.__maas = maas
        self.__yipranma_payi = yipranma_payi

    # değişkenlerin kontrolünü sağlayan get/set fonksiyonları oluşturuldu
    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi
    
    # zam hakkını hesaplayan fonksiyon oluşturuldu    
    def zam_hakki(self):
        try:
            maas = self.get_maas()
            tecrube = self.get_tecrube()

            if tecrube < 24:
                zam_orani = ( self.__yipranma_payi * 10 ) / 100
            elif tecrube >= 24 and tecrube <= 48 and maas < 15000:
                zam_orani = ( ((maas % tecrube) / 2) + (self.__yipranma_payi * 10) ) / 100
            elif tecrube > 48 and maas < 25000:
                zam_orani = (((maas % tecrube) / 3) + (self.__yipranma_payi * 10)) / 100
            else:
                zam_orani = 0
                
            self.__yeni_maas = maas + (maas * zam_orani)
            
            if self.__yeni_maas == maas:
                self.__yeni_maas = maas
            else:
                return self.__yeni_maas

        except Exception as e: # oluşacak bir hatanın kontrolü try except blokları ile yapıldı
            print("Hata:", str(e))
            return None

    def __str__(self): # Ekrana bilgilerin yazdırılmasını sağlayan str fonksiyonu oluşturuldu
        self.zam_hakki()
        return f"\n\n------ Mavi Yaka ------ \nAd: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.get_tecrube()} Ay\nYeni Maaş: {self.__yeni_maas:.2f}"