#numero = int(input("digite um numero"))

def nprimo(numero):
    if numero <= 1: 
        return False 
    for i in range(2, int(numero * 0.5) + 1):
        if numero % i == 0:
            return False 
    return True
   
numero = int(input("digite um numero"))

if nprimo(numero):
    print(str(f"{numero} é primo"))
else:
    print(str(f"{numero} nao é primo"))
