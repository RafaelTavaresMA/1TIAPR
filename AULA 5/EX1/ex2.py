arquivo = "texto.txt"
arquvivo = "texto2.txt"

with open(arquvivo, "r") as arq1, open(arquivo, "r") as arq2:
    conteudo1 = arq1.read()
    conteudo2 = arq2.read()
    
with open("texto_combinado.txt", "w") as arq_combinado:
    arq_combinado.write(conteudo1 + "\n" + conteudo2)

print(f"Os arquivos '{arquvivo}' e '{arquivo}' foram combinados em 'texto_combinado.txt'.")


