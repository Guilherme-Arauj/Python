def calcular_raiz_quadrada(N):
    k = 1.0  
    for i in range(12):
        k = (k + N / k) / 2
        print(f"Valor {i + 1}: {k:.3f}")


N = float(input("Digite o valor de N para calcular a raiz quadrada: "))


print(f"\nCálculo da raiz quadrada de {N} usando o método de Heron:")
calcular_raiz_quadrada(N)
