seçim= str(input("Şekli Seçiniz\n\tDörtgen\n\tÜçgen\n\t: "))
if seçim == str("Dörtgen"):
    a = int(input("1. Kenar: "))
    b = int(input("2. Kenar: "))
    c = int(input("3. Kenar: "))
    d = int(input("4. Kenar: "))
    if a == b == c == d:
        print("Kare")
    elif a != b != c != d and b != a != c != d and c != a != b != d and d != a != b != c:
        print("Dörtgen")
    else:
        print("Dikdörtgen")
if seçim == str("Üçgen"):
    e = int(input("1. Kenar: "))
    f = int(input("2. Kenar: "))
    g = int(input("3. Kenar: "))
    if e == f == g:
        print("Eşkenar Üçgen")
    elif e != f != g and f != e != g and g != e != f:
        print("Üçgen")
    elif e == 0 or f == 0 or g == 0:
        print("Üçgen Değil")
    else:
        print("İkizkenar Üçgen")

