vize1=int(input("Vize 1: "))
vize2=int(input("Vize 2: "))
final=int(input("Final: "))
print("Vize 1 %30: {}\nVize 2 %30: {}\nFinal %40: {}".format(vize1*0.3,vize2*0.3,final*0.4))
gno=vize1*0.3+vize2*0.3+final*0.4
print("Genel Ortalama: ",vize1*0.3+vize2*0.3+final*0.4)
hn=str("Harf Notu: ")
if gno >= 90:
    print(hn,"AA")
elif gno >= 85:
    print(hn,"BA")
elif gno >= 80:
    print(hn,"BB")
elif gno >= 75:
    print(hn,"CB")
elif gno >= 70:
    print(hn,"CC")
elif gno >= 65:
    print(hn,"DC")
elif gno >= 60:
    print(hn,"DD")
elif gno >= 55:
    print(hn,"FD")
else:
    print(hn,"FF")