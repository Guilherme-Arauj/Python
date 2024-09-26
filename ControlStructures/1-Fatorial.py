def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

numero = int(input("Digite um número inteiro não negativo: "))
if numero < 0:
    print("Por favor, insira um número não negativo.")
else:
    resultado = fatorial(numero)
    print(f"O fatorial de {numero} é: {resultado}")
4