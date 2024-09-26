def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def cos_taylor(x, termos=10):
    soma = 0
    for n in range(termos):
        termo = ((-1) ** n) * (x ** (2 * n)) / fatorial(2 * n)
        soma += termo
    return soma


x = float(input("Digite o valor de x (em radianos) para calcular cos(x): "))


resultado = cos_taylor(x)

print(f"O valor aproximado de cos({x}) pela série de Taylor é: {resultado:.6f}")
