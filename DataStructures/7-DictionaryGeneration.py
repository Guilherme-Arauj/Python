frase = input("Digite uma frase: ")
dicionario = {}

for caractere in frase:
    if caractere in dicionario:
        dicionario[caractere] += 1
    else:
        dicionario[caractere] = 1

print(dicionario)
