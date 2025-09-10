produto = 55
quantidade = int(input("Digite a quantidade:"))
total = produto * quantidade

if quantidade > 10:
    total *= 0.9 #aplica o desconto de 10%
    print("desconto de 10% aplicado")

else: 
    print(total)

   