print("--------Asal Sayıları Listele---------")
for i in range(1,101):
    bolum = False
    for j in range(2,i):
        if  i % j == 0:
            print(i)

