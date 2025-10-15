with open('frutas.txt', "r") as file:
    #le todo o conteudo
    conteudo = file.read()
    print(conteudo)

#abre o arquivo no modo leitura('r')
with open("frutas.txt", "r") as file:
    #le a primeira linha do arquivo
    linha1 = file.readline()
    #le a segunda linha do arquivo
    linha2 = file.readline()
    #le a terceira linha do arquivo
    linha3 = file.readline()
    print(linha1)
    print(linha2)
    print(linha3)



