arquivo = "texto.txt"

linhas_original = []
linhas = []
with open(arquivo, "r") as f:
    linha_original = f.readlines()
    linha = sorted(linha_original)
    print(linha)

print("linhas do aquivo em ordem alfabetica:")




