def media(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)


numero = [1, 2, 3, 4, 5]
resultado = media(numero)
print(resultado)

