print("***HESAP MAKİNESİ***")
a=int(input("1.Sayıyı Giriniz: "))
print("Toplama(1)\nÇıkarma(2)\nÇarpma(3)\nBölme(4)\nÜs(5)\nKarekök(6)")
işlem =int(input("İşlem Numarasını Seçiniz: "))
b=int(input("2.Sayıyı Giriniz: "))
if işlem == 1:
    print("Sonuç: ",a+b)
elif işlem == 2:
    print("Sonuç: ",a-b)
elif işlem == 3:
    print("Sonuç: ",a*b)
elif işlem == 4:
    print("Sonuç: ",a/b)
elif işlem == 5:
    print("Sonuç: ",a**b)
elif işlem == 6:
    print("Sonuç: ",a**0.5)
else:
    print("Tekrar Deneyin!")


