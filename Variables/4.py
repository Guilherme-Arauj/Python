numero = input("Digite um número de cinco dígitos: ")

if len(numero) == 5 and numero.isdigit():
    digitos_separados = '   '.join(numero)
    print(digitos_separados)
else:
    print("Por favor, insira um número válido de cinco dígitos.")
