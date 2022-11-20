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
        while self.sure_kontrolu():
            if self.odul_index == 0:
                self.sure_kontrolu()
                cevap = input(f"\n{self.odul_listesi[self.odul_index + 1]}'lik Soru : {soru.soru} (A/B/C/D)\n\nJoker Kullanmak İçin(1/2/3/4)\n\n{soru.siklar}\n").upper()
                if cevap != "A" and cevap != "B" and cevap != "C" and cevap != "D" and cevap != "1" and cevap != "2" and cevap != "3" and cevap != "4":
                    print("Lütfen şıkkı veya jokeri doğru yazın.\n")
                    continue               
                if cevap == "1" and "Seyirciye Sorma Jokeri" in self.jokerler:
                    print("Seyirciye Sorma Jokeri Kullanıldı\n")
                    self.joker_kullanimi(cevap)
                    continue
                elif cevap == "1" and "Seyirciye Sorma Jokeri" not in self.jokerler:
                    print("Seyirciye Sorma Jokerini Daha Önce Kullandınız!\n")
                    continue
                elif cevap == "2" and "Telefon Jokeri" in self.jokerler:
                    print("Telefon Jokeri Kullanıldı\n")
                    self.joker_kullanimi(cevap)
                    continue
                elif cevap == "2" and "Telefon Jokeri" not in self.jokerler:
                    print("Telefon Jokerini Daha Önce Kullandınız!\n")
                    continue
                elif cevap == "3" and "Yarı Yarıya Jokeri" in self.jokerler:
                    print("Yarı Yarıya Jokeri Kullanıldı\n")
                    cevap = self.yari_yariya_kontrolu()
                elif cevap == "3" and "Yarı Yarıya Jokeri" not in self.jokerler:
                    print("Yarı Yarıya Jokerini Daha Önce Kullandınız!\n")
                    continue
                elif cevap == "4" and "Çift Cevap Jokeri" in self.jokerler:
                    print("Çift Cevap Jokeri 2.Barajı Geçince Kullanılabilir.\n")
                    continue

            elif self.odul_index == 2 or self.odul_index == 7:
                self.sure_kontrolu()
                cevap = input(f"\n{self.odul_listesi[self.odul_index]}'lik Baraj Sorusu : {soru.soru} (A/B/C/D)\nJoker Kullanmak İçin(1/2/3/4)\n\n{soru.siklar}\n").upper()
                if cevap != "A" and cevap != "B" and cevap != "C" and cevap != "D" and cevap != "1" and cevap != "2" and cevap != "3" and cevap != "4":
                    print("Lütfen şıkkı veya jokeri doğru yazın.\n")
                    continue               
                if cevap == "1" and "Seyirciye Sorma Jokeri" in self.jokerler:
                    print("Seyirciye Sorma Jokeri Kullanıldı\n")
                    self.joker_kullanimi(cevap)
                    continue
                elif cevap == "1" and "Seyirciye Sorma Jokeri" not in self.jokerler:
                    print("Seyirciye Sorma Jokerini Daha Önce Kullandınız!\n")
                    continue
                elif cevap == "2" and "Telefon Jokeri" in self.jokerler:
                    print("Telefon Jokeri Kullanıldı\n")
                    self.joker_kullanimi(cevap)
                    continue
                elif cevap == "2" and "Telefon Jokeri" not in self.jokerler:
                    print("Telefon Jokerini Daha Önce Kullandınız!\n")
                    continue
                elif cevap == "3" and "Yarı Yarıya Jokeri" in self.jokerler:
                    print("Yarı Yarıya Jokeri Kullanıldı\n")
                    cevap = self.yari_yariya_kontrolu()
                elif cevap == "3" and "Yarı Yarıya Jokeri" not in self.jokerler:
                    print("Yarı Yarıya Jokerini Daha Önce Kullandınız!\n")
                    continue
                elif cevap == "4" and "Çift Cevap Jokeri" in self.jokerler and self.odul_index <= 7:
                    print("Çift Cevap Jokeri 2.Barajı Geçince Kullanılabilir.\n")
                    continue
                elif cevap == "4" and "Çift Cevap Jokeri" in self.jokerler and self.odul_index > 7:
                    print("Çift Cevap Jokeri Kullanıldı.\n")
                    cevap = self.cift_cevap_kontrolu()
                elif cevap == "4" and "Çift Cevap Jokeri" not in self.jokerler and self.odul_index > 7:
                    print("Çift Cevap Jokerini Daha Önce Kullandınız!\n")
                    continue
            else:
                self.sure_kontrolu()
                cevap = input(f"\n{self.odul_listesi[self.odul_index]}'lik Soru : {soru.soru} (A/B/C/D)\nJoker Kullanmak İçin(1/2/3/4)\n\n{soru.siklar}\n").upper()
                if cevap != "A" and cevap != "B" and cevap != "C" and cevap != "D" and cevap != "1" and cevap != "2" and cevap != "3" and cevap != "4":
                    print("Lütfen şıkkı veya jokeri doğru yazın.\n")
                    continue               
                if cevap == "1" and "Seyirciye Sorma Jokeri" in self.jokerler:
                    print("Seyirciye Sorma Jokeri Kullanıldı\n")
                    self.joker_kullanimi(cevap)
                    continue
                elif cevap == "1" and "Seyirciye Sorma Jokeri" not in self.jokerler:
                    print("Seyirciye Sorma Jokerini Daha Önce Kullandınız!\n")
                    continue
                elif cevap == "2" and "Telefon Jokeri" in self.jokerler:
                    print("Telefon Jokeri Kullanıldı\n")
                    self.joker_kullanimi(cevap)
                    continue
                elif cevap == "2" and "Telefon Jokeri" not in self.jokerler:
                    print("Telefon Jokerini Daha Önce Kullandınız!\n")
                    continue
                elif cevap == "3" and "Yarı Yarıya Jokeri" in self.jokerler:
                    print("Yarı Yarıya Jokeri Kullanıldı\n")
                    cevap = self.yari_yariya_kontrolu()
                elif cevap == "3" and "Yarı Yarıya Jokeri" not in self.jokerler:
                    print("Yarı Yarıya Jokerini Daha Önce Kullandınız!\n")
                    continue
                elif cevap == "4" and "Çift Cevap Jokeri" in self.jokerler and self.odul_index <= 7:
                    print("Çift Cevap Jokeri 2.Barajı Geçince Kullanılabilir.\n")
                    continue
                elif cevap == "4" and "Çift Cevap Jokeri" in self.jokerler and self.odul_index > 7:
                    print("Çift Cevap Jokeri Kullanıldı.\n")
                    cevap = self.cift_cevap_kontrolu()
                elif cevap == "4" and "Çift Cevap Jokeri" not in self.jokerler and self.odul_index > 7:
                    print("Çift Cevap Jokerini Daha Önce Kullandınız!\n")
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
                            print("Lütfen doğru cevabı verin\n")
                            continue
                    else:
                        cevap = input(f"{self.odul_listesi[self.odul_index]} TL alıp ayrılmak istiyor musunuz? (E/H)\n").upper()
                        if cevap != "E" and cevap != "H":
                            print("Lütfen doğru cevabı verin\n")
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
    
    def joker_kullanimi(self, joker_adi):
        soru = self.soru_listesi[self.soru_numarasi]
        sik_indeksleri = {"A" : 0, "B" : 1, "C" : 2, "D" : 3}
        siklar_listesi = soru.siklar.split("\n")
        soru_cevabı = siklar_listesi[sik_indeksleri[soru.dogru_cevap]]
        if joker_adi == "1":
            print("Seyirciye Soruluyor...\n")
            time.sleep(2)
            print(f"{soru_cevabı} ---> {random.randint(50, 100)} (En Yüksek)")
            siklar_listesi.remove(soru_cevabı)
            for x in siklar_listesi:
                print(f"{x} ---> {random.randint(0, 50)}")
            self.jokerler.remove("Seyirciye Sorma Jokeri")
        elif joker_adi == "2":
            print("Aranıyor...")
            time.sleep(2)
            print("Soruldu\n")
            print(f"Cevap : {soru_cevabı}\n")

    def yari_yariya_kontrolu(self):
        soru = self.soru_listesi[self.soru_numarasi]
        sik_indeksleri = {"A" : 0, "B" : 1, "C" : 2, "D" : 3}
        siklar_listesi = soru.siklar.split("\n")
        soru_cevabı = siklar_listesi[sik_indeksleri[soru.dogru_cevap]]
        print("2 Şık Eleniyor...")
        time.sleep(2)
        kalan_cevaplar = []
        for x in siklar_listesi:
            if x == soru_cevabı:
                continue
            kalan_cevaplar.append(x)
        kalan = random.choice(kalan_cevaplar)
        kalan_cevaplar = [kalan, soru_cevabı]
        kalan_cevaplar.sort()
        for x in kalan_cevaplar:
            print(x)
        cevap = input(f"Cevabınızı Seçin : (A/B/C/D)\n").upper()
        return cevap

    def cift_cevap_kontrolu(self):
        soru = self.soru_listesi[self.soru_numarasi]
        sik_indeksleri = {"A" : 0, "B" : 1, "C" : 2, "D" : 3}
        siklar_listesi = soru.siklar.split("\n")
        print("Kullanılıyor...\n")
        time.sleep(2)
        for x in siklar_listesi:
            print(x)
        cevap = input(f"Cevabınızı Seçin : (A/B/C/D)\n").upper()
        if cevap != soru.dogru_cevap:
            siklar_listesi.remove(siklar_listesi[sik_indeksleri[cevap]])
            for x in siklar_listesi:
                print(x)
            cevap = input(f"2.Cevabınızı Seçin : (A/B/C/D)\n").upper()
            return cevap
        return cevap

"""    def sure_kontrolu(self):
        if self.odul_index >= 0 and self.odul_index <= 2:
            if sure1 == 0:        
                return False                    
            else:                                   
                t = Timer(2.0, self.sure_kontrolu())  
                t.start()
        elif self.odul_index >= 3 and self.odul_index <= 7:
            if sure2 == 0:        
                return False                    
            else:                                   
                t = Timer(2.0, self.sure_kontrolu())  
                t.start()
        return True
"""