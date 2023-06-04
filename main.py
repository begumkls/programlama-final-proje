import pandas as pd
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka


# Insan sınıfı için 2 nesne oluşturulması
insan1 = Insan("00459245873", "Tuana", "Kabataş", 34, "Kadın", "Türk")
insan2 = Insan("55554875120", "Burak", "Solmaz", 36, "Erkek", "Türk")
# Insan sınıfı nesnelerinin bilgilerinin yazdırılması
print("1. Kişi Bilgileri:")
print(insan1)
print("----------------------")
print("2. Kişi Bilgileri:")
print(insan2)
print("----------------------")
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