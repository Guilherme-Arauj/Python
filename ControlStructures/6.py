def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def calcular_soma_e(n):
    soma = 1.0  
    for i in range(2, n + 1):
        soma += 1 / fatorial(i)  
    return soma


n = int(input("Digite um valor inteiro e positivo N: "))


if n > 0:
    resultado = calcular_soma_e(n)
    print(f"A soma E = 1 + 1/2! + 1/3! + ... + 1/{n}! é: {resultado:.6f}")
else:
    print("Por favor, insira um valor inteiro positivo.")
