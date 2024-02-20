krediler = [
    "Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel",
    "Mutlu Emekli İhtiyaç Kredisi "
]

#alias
for kredi in krediler:
  print("<option>"+kredi+"<option>")

#0'dan itibaren 9'a kadar yazdırır.
for i in range(10):
  print(i)

for i in range(len(krediler)):
  print(krediler[i])

#3'ten 9'a kadar yazdırır.
for i in range(3,10):
  print(i)

#0'dan itibaren 10 dahil değil 2 şerli yazdırır.
for i in range(0,10,2):
  print(i)


