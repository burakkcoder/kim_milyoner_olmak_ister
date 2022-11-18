class Yarisma:
    def __init__(self, soru_listesi):
        self.odul_listesi = ["1.000 TL", "2.000 TL", "3.000 TL", "5.000 TL", "7.500 TL", "10.000 TL", "30.000 TL", "50.000 TL", "100.000 TL", "200.000 TL", "400.000 TL", "1.000.000 TL"]
        self.odul_index = 0
        self.soru_listesi = soru_listesi
        self.soru_numarasi = 0
        self.jokerler = ["Seyirciye Sorma Jokeri", "Telefon Jokeri", "Yarı Yarıya Jokeri", "Çift Cevap Jokeri"]
        self.cekilme = False
        self.yanlis_cevap = False

    def oyun_devammi(self):
        if self.cekilme == True or self.yanlis_cevap == True:
            return False
        cevap = input(f"{self.odul_listesi[self.odul_index]} TL alıp ayrılmak istiyor musun? (E/H)")
        if cevap == "E":
            return False
        return True
    
    def siradaki_soru(self):
        soru = self.soru_listesi[self.soru_numarasi]
        self.soru_numarasi += 1
        cevap = input(f"{self.odul_listesi[self.odul_index]}'lik Soru : {soru.soru} (A/B/C/D)\n{soru.siklar}")
        self.cevap_kontrolu(cevap, soru.dogru_cevap)

    def cevap_kontrolu(self, cevap, dogru_cevap):
        if cevap.upper() == dogru_cevap:
            print("Doğru Cevap!")
            if self.siradaki_soru():
                self.odul_index += 1
        else:
            self.yanlis_cevap == True
