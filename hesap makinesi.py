i = 0
while i < 1:
    
    print("\nHesap makinesi\n----------------------------------------------------------------------------------\n1. ve 2. sayiyi giriniz. Daha sonra yapmak istediginiz islemi(+,-,*,/) belirtiniz.\n")
    hesapmak = range(3)
    sayi1 = hesapmak[0]
    sayi2 = hesapmak[1]
    islem = hesapmak[2]
    hesapmak = [sayi1, sayi2, islem]
    
    
    
    hesapmak[0]= int(input("İlk sayiyi giriniz: "))
    hesapmak[1]= int(input("İkinci sayiyi giriniz: "))
    hesapmak[2]= input("Yapmak istediginiz islemi giriniz: ")

    a = 0
    while a < 1:
        if hesapmak[2] == "+" :
            sonuc = (hesapmak[0] + hesapmak[1])
            a = a + 1
        elif hesapmak[2] == "-" :
            sonuc = (hesapmak[0] - hesapmak[1])
            a = a + 1
        elif hesapmak[2] == "*" :
            sonuc = (hesapmak[0] * hesapmak[1])
            a = a + 1
        elif hesapmak[2] == "/" :
            sonuc = (hesapmak[0] / hesapmak[1])
            a = a + 1
        else:
            print("Yanlış işlem tipi girdiniz!")
            

    print("\n\n---> Sonuc: " + str(sonuc))
    j = 0
    while j < 1: 
        x = input("\n\n\nDevam etmek istiyor musunuz?\nEvet/Hayır: ")
        x = x.lower()
        if x == "evet":
            j = j + 1
        elif x == "hayır":
            j = j + 1
            i = i + 1
        else:
            print("Yanlis yazdiniz! Tekrar deneyiniz.")
