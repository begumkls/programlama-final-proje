from Calisan import Calisan #v Calisan sınıfı import edildi

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
        
    def zam_hakki(self):
        try:
            maas = self.get_maas()
            tecrube = self.get_tecrube()

            if tecrube < 2:
                zam_orani = self.__yipranma_payi * 10
            elif tecrube >= 2 and tecrube <= 4 and maas < 15000:
                zam_orani = (maas % tecrube) / 2 + self.__yipranma_payi * 10
            elif tecrube > 4 and maas < 25000:
                zam_orani = (maas % tecrube) / 3 + self.__yipranma_payi * 10
            else:
                zam_orani = 0
            yeni_maas = maas + (maas * zam_orani / 100)
            if yeni_maas == maas:
                return maas
            else:
                return yeni_maas

        except Exception as e: # oluşacak bir hatanın kontrolü try except blokları ile yapıldı
            print("Hata:", str(e))
            return None

    def __str__(self): # Ekrana bilgilerin yazdıırlmasını sağlayan str fonksiyonu oluşturuldu
        return f"\n\n------ Mavi Yaka ------ \nAd: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.get_tecrube()} yıl\nYeni Maaş: {self.zam_hakki()}"
