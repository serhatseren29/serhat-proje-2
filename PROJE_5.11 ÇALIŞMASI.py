class Kisi:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def bilgileri_goster(self):
        return f"Ad: {self.ad}, Yaş: {self.yas}"

class Ogrenci(Kisi):
    def __init__(self, ad, yas, ogrenci_numarasi):
        super().__init__(ad, yas)
        self.ogrenci_numarasi = ogrenci_numarasi

    def bilgileri_goster(self):
        return f"{super().bilgileri_goster()}, Öğrenci Numarası: {self.ogrenci_numarasi}"

class Ogretmen(Kisi):
    def __init__(self, ad, yas, ders):
        super().__init__(ad, yas)
        self.ders = ders

    def bilgileri_goster(self):
        return f"{super().bilgileri_goster()}, Ders: {self.ders}"

# Örnek Kullanım
ogrenci = Ogrenci("Murat", 22, "S98765")  # Öğrencinin adı ve numarası değiştirildi
ogretmen = Ogretmen("Mehmet", 35, "Fizik")  # Öğretmenin adı ve dersi değiştirildi

print(ogrenci.bilgileri_goster())  # Murat için bilgileri göster
print(ogretmen.bilgileri_goster())  # Mehmet için bilgileri göster
