
#Ödev 1
print("---------\nÖdev 1\n---------")
def kelimeleri_ayir():
    ifade = input("Bir şeyler yazın: ")
    kelimeler = ifade.split()
    return kelimeler

kelime_listesi = kelimeleri_ayir()
print("Ayrılmış Kelimeler:", kelime_listesi)



#Ödev 2
print("\n\n---------\nÖdev 2\n---------")

def ortak_harf():
    kelime1 = list(input("İlk kelimeyi girin: "))
    kelime2 = list(input("İkinci kelimeyi girin: "))
    ortaklar = {}
    for i in range(len(kelime1)):
        for j in range(len(kelime1)):
            if kelime1[i] == kelime2[j]:
                if (kelime1[i] in ortaklar):
                    continue
                else:
                    ortaklar[i] = kelime1[i]

    print(ortaklar)    

ortak_harf()            



def ortak_harfleri_bul_ve_say(string1, string2):
    # İki string ifadeyi küçük harfe çevirerek büyük/küçük harf farklılığını önleriz.
    string1 = string1.lower()
    string2 = string2.lower()

    # Ortak harfleri ve kullanım sayılarını tutmak için bir sözlük oluşturuyoruz.
    ortak_harfler = {}

    # İlk string ifadedeki harf sayılarını hesaplayarak sözlüğü güncelliyoruz.
    for harf in string1:
        if 'a' <= harf <= 'z':
            if harf in ortak_harfler:
                ortak_harfler[harf][0] += 1
            else:
                ortak_harfler[harf] = [1, 0]

    # İkinci string ifadedeki harf sayılarını hesaplayarak sözlüğü güncelliyoruz.
    for harf in string2:
        if 'a' <= harf <= 'z':
            if harf in ortak_harfler:
                ortak_harfler[harf][1] += 1
            else:
                ortak_harfler[harf] = [0, 1]

    # Ortak harfleri ve kullanım sayılarını ekrana yazdırıyoruz.
    for harf, (sayi1, sayi2) in ortak_harfler.items():
        if sayi1 > 0 and sayi2 > 0:
            print(f"{harf} {sayi1} {sayi2}")

# Örnek kullanım:
string1 = "Anahtar"
string2 = "araba"
ortak_harfleri_bul_ve_say(string1, string2)
