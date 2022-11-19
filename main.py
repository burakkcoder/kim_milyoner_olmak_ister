from game_brain import Yarisma
from question_class import Soru
from questions import sorular

print("""
# # # # # # # # # # # # # # # # # # # # # # # # #
#          KİM MİLYONER OLMAK İSTER ?           #
#                                               #
#    1 - 1.000 TL                               #
#    2 - 2.000 TL (1.Baraj)                     #
#    3 - 3.000 TL                               #
#    4 - 5.000 TL                               #
#    5 - 7.500 TL                               #
#    6 - 10.000 TL                              #
#    7 - 30.000 TL (2.Baraj)                    #
#    8 - 50.000 TL                              #
#    9 - 100.000 TL                             #
#    10 - 200.000 TL                            #
#    11 - 400.000 TL                            #
#    12 - 1.000.000 TL (Büyük Ödül)             #
#                                               #
#    JOKERLER :                                 #
#     Seyirciye Sorma Jokeri                    #
#     Telefon Jokeri                            #
#     Yarı Yarıya Jokeri                        #
#     Çift Cevap Jokeri                         #
#                                               #
#    SÜRE KISITLAMASI :                         #
#     1. ve 2. sorularda 15 saniye;             #
#     3, 4, 5, 6, ve 7. sorularda 45 saniye;    #
#     diğer sorularda süre kısıtlaması yok.     #
# # # # # # # # # # # # # # # # # # # # # # # # #
""")

soru_listesi = []
for x in sorular:
    soru = x["soru"]
    siklar = x["siklar"]
    dogru_cevap = x["dogru_cevap"]
    yeni_soru = Soru(soru, siklar, dogru_cevap)
    soru_listesi.append(yeni_soru)

yarisma = Yarisma(soru_listesi)

while yarisma.oyun_devammi():
    yarisma.siradaki_soru()

print("Yarışma Bitti.")
if yarisma.odul_index == 12 and yarisma.yanlis_cevap == False:
    print(f"Ödülün : {yarisma.odul_listesi[yarisma.odul_index]} !!! TEBRİKLER !!!")
elif yarisma.odul_index > 1 and yarisma.odul_index < 11:
    print(f"Ödülün : {yarisma.odul_listesi[yarisma.odul_index - 1]}")  
else:
    print(f"Ödülün : {yarisma.odul_listesi[yarisma.odul_index]}")



    