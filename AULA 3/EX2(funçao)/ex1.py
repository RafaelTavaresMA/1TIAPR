def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b == 0:
        return "Divisão por zero não é permitida."
    return a / b

resultado_soma = soma(10, 5)
resultado_subtracao = subtracao(10, 5)
resultado_multiplicacao = multiplicacao(10, 5)
resultado_divisao = divisao(10, 5) 

print("Soma:", resultado_soma)
print("Subtração:", resultado_subtracao)
print("Multiplicação:", resultado_multiplicacao)
print("Divisão:", resultado_divisao)
            



    
    
    
