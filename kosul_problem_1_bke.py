print("----------------------Beden Kitle Endeksi"
      "----------------------")
ad=str(input("Ad: "))
b=int(input("Boy(cm): "))
b=b/100
k=int(input("Kilo(kg): "))
print("Beden Kitle Endeksin: ",(k/b**2))
btk=k/b**2
if btk < 18.5:
    print("Çok zayıfsın",ad)
elif btk == 18.5 or btk < 25:
    print("\tHarika!\nNormal kilodasın",ad)
elif btk == 25 or btk < 30:
    print("Aşırı Kilolusun",ad)
elif btk >= 30:
    print("Obezsin",ad)
