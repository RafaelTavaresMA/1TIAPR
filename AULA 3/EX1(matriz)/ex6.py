#mesma coisa que a soma so que com subtração


matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matriz2 = [
    [10,11,12],
    [13,14,15],
    [16,17,18]
]

matriz_resultado = []
for i in range(len(matriz)): 
    linha_resultado = []
    for j in range(len(matriz[i])):
        elemento_soma = matriz[i][j] + matriz2[i][j]
        linha_resultado.append(elemento_soma)
    matriz_resultado.append(linha_resultado)


for linha in matriz_resultado:
    for elemento in linha_resultado:
        print(f"{elemento:4}", end="")
    print()

print(matriz_resultado)