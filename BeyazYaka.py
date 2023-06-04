from Calisan import Calisan
class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube, maas, tesvik_primi, sektor=""):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def zam_hakki(self):
        try:
            maaş = self.get_maas()
            tecrube = self.get_tecrube()

            if tecrube < 2:
                zam_miktari = self.__tesvik_primi
            elif tecrube >= 2 and tecrube <= 4 and maaş < 15000:
                zam_miktari = (maaş % tecrube) * 5 + self.__tesvik_primi
            elif tecrube > 4 and maaş < 25000:
                zam_miktari = (maaş % tecrube) * 4 + self.__tesvik_primi
            else:
                zam_miktari = 0

            yeni_maas = maaş + zam_miktari

            if yeni_maas == maaş:
                return maaş
            else:
                return yeni_maas

        except Exception as e:
            print("Hata:", str(e))
            return None

    def __str__(self):
        try:
            return f"BEYAZ YAKA-\nAd: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.get_tecrube()}\nYeni Maaş: {self.zam_hakki()}"

        except Exception as e:
            print("Hata:", str(e))
            return None
