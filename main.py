# gerekli kütüphaneler import edildi
import pandas as pd # Data frame işlemleri için gerekli olan kütüphaneler import edildi
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

# try except blokları ile kontrol sağlandı
try:
    # Insan sınıfı için 2 nesne oluşturuldu
    insan1 = Insan("00459245873", "Tuana", "Kabataş", 34, "Kadın", "Türk")
    insan2 = Insan("55554875120", "Burak", "Solmaz", 36, "Erkek", "Türk")
    
    # Insan sınıfı nesnelerinin bilgileri yazdırıldı
    print("1. Kişi Bilgileri:")
    print(insan1)
    print("----------------------")
    print("2. Kişi Bilgileri:")
    print(insan2)
    print("----------------------")
    
    # Issiz sınıfı için nesne atamaları yapıldı
    issiz1_tecrubeler = {
    "mavi yaka": 3,
    "beyaz yaka": 2,
    "yönetici": 2
    }
    issiz1 = Issiz("00001125861", "Rick", "Grimes", 27, "Erkek", "Amerikan", "mavi yaka", issiz1_tecrubeler)
    print("1. İşsiz Bilgileri:")
    print(issiz1)
    print()
    
    issiz2_tecrubeler = {
        "mavi yaka": 2,
        "beyaz yaka": 3,
        "yönetici": 6
    }
    issiz2 = Issiz("54896214541", "Zehra", "Türkoğlu", 34, "Kadın", "Türk", "beyaz yaka", issiz2_tecrubeler)
    print("2. İşsiz Bilgileri:")
    print(issiz2)
    print()
    
    issiz3_tecrubeler = {
        "mavi yaka": 3,
        "beyaz yaka": 5,
        "yönetici": 2
    }
    issiz3 = Issiz("55654565456", "Ahmet", "Tostçu", 37, "Erkek", "Türk", "yonetici", issiz3_tecrubeler)
    print("3. İşsiz Bilgileri:")
    print(issiz3)
    print()
    print("----------------------")
    
    # Kullanıcıdan çalışanların statü bilgileri alındı
    statu1 = input("Lütfen 1. Çalışanın Statüsünü giriniz (teknoloji, muhasebe, inşaat, diğer):")
    statu2 = input("Lütfen 2. Çalışanın Statüsünü giriniz (teknoloji, muhasebe, inşaat, diğer):")
    statu3 = input("Lütfen 3. Çalışanın Statüsünü giriniz (teknoloji, muhasebe, inşaat, diğer):")
        
    calisan1 = Calisan("00486547895", "Mustafa", "Kanmaz", 27, "Erkek", "Türk", statu1, 2, 12500)
    calisan2 = Calisan("0000000005", "Semiha", "Gül", 34, "Kadın", "Türk", statu2, 7, 17200)
    calisan3 = Calisan("0085410320", "Cenk", "Demir", 42, "Erkek", "Türk", statu3, 8, 21000)
    print()
    print("Çalışan Bilgileri:")
    print(calisan1)
    print(calisan2)
    print(calisan3)
    print()
    print()

    # MaviYaka sınıfı için nesneler atandı
    maviyaka1 = MaviYaka("55555555555", "Gürkan", "Sedef", 32, "Erkek", "Türk", 2, 14500, 5)
    maviyaka2 = MaviYaka("98546715840", "Zeynep", "Demir", 35, "Kadın", "Türk", 7, 15000, 8)
    maviyaka3 = MaviYaka("00005485694", "Murat", "Kara", 42, "Erkek", "Türk", 10, 21000, 6)
    print("Mavi Yaka Bilgileri:")
    print(maviyaka1)
    print(maviyaka2)
    print(maviyaka3)
    print()
    # BeyazYaka sınıfı için nesneler atandı
    beyazyaka1 = BeyazYaka("11111111111", "Burak", "Yılmaz", 31, "Erkek", "Türk", 3, 16000, 2000)
    beyazyaka2 = BeyazYaka("22222222222", "Sıla", "Demir", 36, "Kadın", "Türk", 6, 18000, 1600)
    beyazyaka3 = BeyazYaka("33333333333", "Barış", "Kaya", 29, "Erkek", "Türk", 1, 11000, 1000)
    print("Beyaz Yaka Bilgileri:")
    print(beyazyaka1)
    print(beyazyaka2)
    print(beyazyaka3)
    print()
    print("---------------------")
    print()
    
except Exception as e:
    print("Bir hata oluştu:", e)