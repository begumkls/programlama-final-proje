from Insan import Insan # Insan sınıfı import edildi

class Calisan(Insan): # Insan sınıfından türetilen Calisan sınıfı oluşturuldu
    # değişkenlerin sınıf içerisinde kullanımını sağlayan init fonksiyonu oluşturuldu
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = self.sektor_kontrol(sektor)
        self.__tecrube = tecrube
        self.__maas = maas
        self.__yeni_maas = None

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
    # kullanıcıdan alınan sektör girişinin kontrolünü yapan fonksiyon oluşturuldu    
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

            if tecrube < 24:
                zam_orani = 0
            elif tecrube >= 24 and tecrube <= 48 and maas < 15000:
                zam_orani = maas % tecrube
            elif tecrube > 48 and maas < 25000:
                zam_orani = (maas % tecrube)/ 2
            else:
                zam_orani = 0

            self.__yeni_maas = maas * zam_orani

            if self.__yeni_maas == maas:
                self.__yeni_maas = maas
            else:
                return self.__yeni_maas

        except Exception as e: # oluşacak bir hatanın kontrolü try except blokları ile yapıldı
            print("Hata:", str(e))
            return None

    def __str__(self): # Ekrana bilgilerin yazdırılmasını sağlayan str fonksiyonu oluşturuldu
        self.zam_hakki()
        return f"Ad: {self.get_ad()}, Soyad: {self.get_soyad()}, Sektör: {self.__sektor}, Tecrübe: {self.get_tecrube()} Ay, Yeni Maaş: {self.__yeni_maas:.2f}"
