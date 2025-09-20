num = int(input("Digite um numero:"))
while num % 2 != 0:
    print("numero invalido")
    num = int(input("digite um numero par:"))
print(f"obrigado! {num} é um numero par.") 