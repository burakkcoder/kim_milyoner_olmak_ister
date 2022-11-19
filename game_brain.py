import time
import random

class Yarisma:
    def __init__(self, soru_listesi):
        self.odul_listesi = ["0", "1.000 TL", "2.000 TL", "3.000 TL", "5.000 TL", "7.500 TL", "10.000 TL", "30.000 TL", "50.000 TL", "100.000 TL", "200.000 TL", "400.000 TL", "1.000.000 TL"]
        self.odul_index = 0
        self.soru_listesi = soru_listesi
        self.soru_numarasi = 0
        self.jokerler = ["Seyirciye Sorma Jokeri", "Telefon Jokeri", "Yarı Yarıya Jokeri", "Çift Cevap Jokeri"]
        self.cekilme = False
        self.yanlis_cevap = False

    def oyun_devammi(self):
        if self.odul_index == 13:
            return False
        if self.cekilme == True or self.yanlis_cevap == True:
            return False
        return True
    
    def siradaki_soru(self):
        soru = self.soru_listesi[self.soru_numarasi]
        while True:
            if self.odul_index == 0:
                cevap = input(f"{self.odul_listesi[self.odul_index + 1]}'lik Soru : {soru.soru} (A/B/C/D)\n{soru.siklar}\n").upper()
                if cevap != "A" and cevap != "B" and cevap != "C" and cevap != "D":
                    print("Lütfen şıkkı doğru yazın.")
                    continue
            elif self.odul_index == 2 or self.odul_index == 7:
                cevap = input(f"{self.odul_listesi[self.odul_index]}'lik Baraj Sorusu : {soru.soru} (A/B/C/D)\n{soru.siklar}\n").upper()
                if cevap != "A" and cevap != "B" and cevap != "C" and cevap != "D":
                    print("Lütfen şıkkı doğru yazın.")
                    continue
            else:
                cevap = input(f"{self.odul_listesi[self.odul_index]}'lik Soru : {soru.soru} (A/B/C/D)\n{soru.siklar}\n").upper()
                if cevap != "A" and cevap != "B" and cevap != "C" and cevap != "D":
                    print("Lütfen şıkkı doğru yazın.")
                    continue
            self.cevap_kontrolu(cevap, soru.dogru_cevap)
            break
        self.soru_numarasi += 1

    def cevap_kontrolu(self, cevap, dogru_cevap):
        if cevap.upper() == dogru_cevap:
            print("Doğru Cevap!")
            if self.odul_index == 12:
                self.cekilme = True
            else:
                while True:
                    if self.odul_index == 0:
                        cevap = input(f"{self.odul_listesi[self.odul_index + 1]} TL alıp ayrılmak istiyor musunuz? (E/H)\n").upper()
                        if cevap != "E" and cevap != "H":
                            print("Lütfen doğru cevabı verin")
                            continue
                    else:
                        cevap = input(f"{self.odul_listesi[self.odul_index]} TL alıp ayrılmak istiyor musunuz? (E/H)\n").upper()
                        if cevap != "E" and cevap != "H":
                            print("Lütfen doğru cevabı verin")
                            continue
                    if cevap == "E":
                        if self.odul_index == 0:
                            self.odul_index += 1
                            self.cekilme = True
                            break
                        else:
                            if self.odul_index != 11:
                                self.odul_index += 1
                                break
                            self.cekilme = True
                            break
                    elif cevap == "H" and self.odul_index == 0:
                        self.odul_index += 2
                        break
                    elif cevap == "H":
                        self.odul_index += 1
                        break
        else:
            if self.odul_index >= 3 and self.odul_index <= 7:
                self.odul_index = 3
            elif self.odul_index >= 8 and self.odul_index <= 12:
                self.odul_index = 8
            self.yanlis_cevap = True
    
    """def joker_kullanimi(self, joker_adi):
        soru = self.soru_listesi[self.soru_numarasi]
        sik_indeksleri = {"A" : 0, "B" : 1, "C" : 2, "D" : 3}
        siklar_listesi = soru.siklar.split("\n")
        soru_cevabı = siklar_listesi[sik_indeksleri[soru.dogru_cevap]]
        if joker_adi == 1:
            print("Seyirciye Soruluyor...")
            time.sleep(2)
            yuzde_A = random.randint(10,30)
            yuzde_B = random.randint(20,45)
            yuzde_C = random.randint(30,40)
            yuzde_D = random.randint(50,100)"""