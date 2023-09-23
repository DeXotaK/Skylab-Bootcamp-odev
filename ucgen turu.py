print("Siz ucgenin kenar uzunluklarini girin. Ben size ucgenin turunu soyleyeyim.\n---------------------------------------------------\n")

kenar1 = input("İlk kenarin uzunlugunu giriniz: ")
kenar2 = input("İkinci kenarin uzunlugunu giriniz: ")
kenar3 = input("Ucuncu kenarin uzunlugunu giriniz: ")
ucgen = [kenar1, kenar2, kenar3]

5
if ucgen[0] == ucgen[1] == ucgen[2]:
    print("Bu ucgen bir eskenar ucgendir.")
elif ucgen[0] == ucgen[1] or ucgen[0] == ucgen[2] or ucgen[2] == ucgen[1]:
    print("Bu ucgen bir ikizkenar ucgendir.")
else:
    print("Bu ucken bir cesitkenar ucgendir.")
