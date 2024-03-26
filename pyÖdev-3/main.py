from personel import Personel
from firma import Firma

# Personel nesnelerini oluşturma
personel1 = Personel("Barkın Bayoğlu", "İnsan Kaynakları", 5, 15000)
personel2 = Personel("Serhat Ayaşlı", "IT", 3, 17000)

# Firma nesnesi oluşturma
firma = Firma()

# Personel ekleme
firma.personel_ekle(personel1)
firma.personel_ekle(personel2)

# Personel listeleme
print("Firmadaki Personeller:")
firma.personel_listele()

# Maaş zammi
firma.maas_zammi(personel1, 10)

# personel listeleme
print("\nMaaş Zammı Sonrası Personeller:")
firma.personel_listele()

# Personel çıkartma
firma.personel_cikart(personel1)

# Son durumu listeleme
print("\nPersonel Çıkartma Sonrası Personeller:")
firma.personel_listele()
