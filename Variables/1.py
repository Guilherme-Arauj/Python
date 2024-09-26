num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

soma = num1 + num2
produto = num1 * num2
diferenca = num1 - num2
divisao = num1 / num2 if num2 != 0 else "Indefinido (divisão por zero)"

print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Diferença: {diferenca}")
print(f"Divisão: {divisao}")
