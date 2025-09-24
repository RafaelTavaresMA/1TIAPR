matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#adicionando uma nova linha a matriz

nova_linha = {10, 11, 12}
matriz.append(nova_linha)

#Imprimindo a matriz atualizada
for linha in matriz:
    print(linha)

#adicionando um elemento (100) a segunda linha na primeira posição
matriz[1].insert(0, 100)
for linha in matriz:
    print(linha)

#usando 'del' para remover a segunda linha
del matriz[1]

#imprimindo a matriz apos a remoção da segunda linha 
print("Matriz apos a remoção da segunda linha:")
for linha in matriz:
    print(linha)

#Usando 'pop' para remover e obter o elemento na terceira coluna da primeria linha 
elemento = matriz[0].pop(2)
print("\nElemento removido:", elemento)

#imprimindo a matriz apos a remoçao do elemento
print("\nMatriz apos a remoçao do elemento:")
for linha in matriz:
    print(linha)

#matriz de exemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#iterar sobre cada linha da matriz
for linha in matriz:
    #iterar sobre cada elemento da linha
    for elemento in linha:
        print(elemento, end=' ')
    #imprimir uma nova linha apos cada linha da matriz
    print()
