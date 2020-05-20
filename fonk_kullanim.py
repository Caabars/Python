def selamla():
    print("Merhaba")
    print("Nasılsın?")
type(selamla)
selamla()
def selamla(isim):
    print("İsminiz: ",isim)
selamla("Meryem")

def toplama(a,b,c):
    print("Toplamlari:",a+b+c)
toplama(1,1,1)
toplama(3,141592,-653589)

def faktoriyel(sayi):
    faktoriyel = 1
    if (sayi == 0 or sayi == 1):
        print("Faktöriyel: ",faktoriyel)
    else:
        while (sayi >= 1):
            faktoriyel *= sayi
            sayi -= 1
        print("Faktöriyel: ",faktoriyel)
faktoriyel(5)



