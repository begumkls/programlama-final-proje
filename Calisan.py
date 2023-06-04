from Insan import Insan # Insan sınıfı import edildi

class Calisan(Insan): # Insna sınıfından türetilen Calisan sınıfı oluşturuldu
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = self.sektor_kontrol(sektor)
        self.__tecrube = tecrube
        self.__maas = maas

    # değişkenlerin kontrolünü sağlayan get/set fonksiyonları oluşturuldu
    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas
        
    def sektor_kontrol(self, sektor):
        sektorler = ["teknoloji", "muhasebe", "inşaat", "diğer"]

        if sektor.lower() in sektorler:
            return sektor.lower()
        else:
            return "diğer"  # Geçersiz sektor değeri girilirse varsayılan olarak "diğer" seçiliyor
        
    # zam hakkını hesaplayan fonksiyon oluşturuldu
    def zam_hakki(self):
        try:
            tecrube = self.get_tecrube()
            maas = self.get_maas()

            if tecrube < 2:
                zam_orani = 0
            elif tecrube >= 2 and tecrube <= 4 and maas < 15000:
                zam_orani = maas * tecrube / 100
            elif tecrube > 4 and maas < 25000:
                zam_orani = (maas * tecrube) / 200
            else:
                zam_orani = 0

            yeni_maas = maas + zam_orani

            if yeni_maas == maas:
                return maas
            else:
                return yeni_maas

        except Exception as e: # oluşacak bir hatanın kontrolü try except blokları ile yapıldı
            print("Hata:", str(e))
            return None

    def __str__(self): # Ekrana bilgilerin yazdıırlmasını sağlayan str fonksiyonu oluşturuldu
        return f"Ad: {self.get_ad()}, Soyad: {self.get_soyad()}, Sektör: {self.__sektor}, Tecrübe: {self.get_tecrube()}, Yeni Maaş: {self.zam_hakki()}"
