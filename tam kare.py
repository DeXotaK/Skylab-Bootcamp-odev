bas = int(input("Baslangıcı giriniz: "))
son = int(input("Bitişi giriniz: "))
tam_kare = [bas, son]
i = 0
sayi = 1
while i < 1:
    kare = sayi*sayi
    if kare > tam_kare[0] and kare < tam_kare[1]:
        print(kare)
    elif kare > tam_kare[1]:
        i = i + 1
    sayi = sayi + 1
