from Insan import Insan

class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, statu, tecrubeler):
        super().__init__(tc_no, ad, soyad, yas,cinsiyet, uyruk)
        self.__tecrubeler = tecrubeler
        self.__statu = self.statu_bul()
        
    def get_tecrubeler(self):
        return self.__tecrubeler
    
    def set_tecrubeler(self, tecrubeler):
        self.__tecrubeler = tecrubeler
        
    def get_statu(self):
        return self.__statu
    
    def statu_bul(self):
        try:
            mavi_yaka = self.__tecrubeler.get("mavi yaka", 0)
            beyaz_yaka = self.__tecrubeler.get("beyaz yaka", 0)
            yonetici = self.__tecrubeler.get("yonetici", 0)
            
            mavi_yaka_etkisi = mavi_yaka * 0.2
            beyaz_yaka_etkisi = beyaz_yaka * 0.35
            yonetici_etkisi = yonetici * 0.45 