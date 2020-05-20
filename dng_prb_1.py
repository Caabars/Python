print("----------Mükemmel Sayıyı Bul----------")
sayi = int(input("Bir Sayı Giriniz: "))
i = 1
toplam = 0
while (i < sayi):
    if (sayi % i == 0):
        toplam += i
    i += 1
if (sayi == toplam):
    print("Tebrikler!")
else:
    print("Yanlış Seçim!")


            