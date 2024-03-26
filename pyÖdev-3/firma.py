from personel import Personel

class Firma:
    def __init__(self):
        self.personel_listesi = []

    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)

    def personel_listele(self):
        for personel in self.personel_listesi:
            print(personel)

    def maas_zammi(self, personel, zam_orani):
        personel.maasi += personel.maasi * zam_orani / 100

    def personel_cikart(self, personel):
        if personel in self.personel_listesi:
            self.personel_listesi.remove(personel)
