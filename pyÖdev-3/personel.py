class Personel:
    def __init__(self, adi, departmani, calisma_yili, maasi):
        self.adi = adi
        self.departmani = departmani
        self.calisma_yili = calisma_yili
        self.maasi = maasi

    def __str__(self):
        return f"{self.adi}, {self.departmani} Departmanı, Çalışma Yılı: {self.calisma_yili}, Maaş: {self.maasi}"
