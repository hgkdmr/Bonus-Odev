baslik = "HABERİNİZ OLSUN"  #string #tr karakter kullanılmaz.
vade = 12  #integer(tam sayı) #sayılar tırnak içinde yazılmaz.
faizOrani1 = 1.47  #virgül değil nokta kullanılır.
faizOrani2 = 1.44  #bir değişken ismi sayı ile başlamaz. Aralarda sayı ve _ kullanılabilir.

print(baslik)  #string
print(type(baslik))
print(type(vade))  #integer
print(type(faizOrani1))  #float

#değişken atamasaydık her defasında değiştirmek zorunda kalırdık.
mesaj = "Hoşgeldin"
musteriAdi = "Hülya"
musteriSoyadi = "Gökdemir"
sonucMesaj = mesaj + " " + musteriAdi + " " + musteriSoyadi + " ! "
print(sonucMesaj)

sayi1 = 50
sayi2 = 20
print(sayi1 + sayi2)
