from ÖRNEK1 import *

print(""""***********************************************

PLAYLİSTE HOŞ GELDİNİZ

İŞLEMLER:


1.ŞARKILARI GÖSTER

2.ŞARKI SORGULA

3.ŞARKI EKLE

4.ŞARKI SİL

5.ŞARKI SÜRESİNİ ARTTIR

ÇIKIŞ İÇİN 'e' YE BASIN
****************************************************************""")

ERD = ERD()


while True:
    işlem = input("YAPICAĞINIZ İŞLEMİ GİRİNİZ:")

    if(işlem == "e"):
        print("PROGRAM SONLANDIRILIYOR.......")
        print("TEKRAR BEKLERİZ.....")
        break

    elif(işlem == 1):
        stüdyo.şarkıları_göster()



    elif(işlem == 2):
        isim = input("HANGİ ŞARKIYI İSTİYORSUNUZ ?:")
        print("ŞARKI SORGULANIYOR")
        time.sleep(2)
        stüdyo.şarkı_sorgula(isim)


    elif(işlem == 3):
        isim = input("İSİM:")

        sanatçı = input("SANATÇI:")

        albüm = input("ALBÜM:")

        prodüksiyon_şirketi = input("PRODÜKSİYON ŞİRKETİ:")

        şarkı_süresi = int(input("ŞARKI SÜRESİ:"))

        yeni_albüm =Şarkı(isim,sanatçı,albüm,prodüksiyon_şirketi,şarkı_süresi)

        print("ŞARKI EKLENİYOR....")
        time.sleep(2)

        stüdyo.şarkı_ekle(yeni_albüm)
        print("ŞARKI EKLENDİ....")



    elif(işlem == 4):
        isim = input("HANGİ ŞARKIYI SİLMEK İSTİYORSUNUZ ?:")

        cevap = input("EMİN MİSİNİZ ? (E/H)")

        if(cevap == "E"):
            print("ŞARKI SİLİNİYOR....")
            time.sleep(2)
            stüdyo.şarkı_sil(isim)
            print("ŞARKI PLAYLİST TEN SİLİNDİ.")

    elif(işlem == 5):
        isim = input("HANGİ ŞARKININ SÜRESİ ARTACAK?")
        time.sleep(2)
        stüdyo.şarkı_süresi_yükselt(isim)


    else:
        print("GEÇERSİZ İŞLEM...")

