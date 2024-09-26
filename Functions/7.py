def calcular_estatisticas(*numeros):
    if not numeros:
        return None, None, None
    
    media = sum(numeros) / len(numeros)
    valor_maximo = max(numeros)
    valor_minimo = min(numeros)
    
    return media, valor_maximo, valor_minimo


resultados1 = calcular_estatisticas(10, 20, 30, 40, 50)
print("Resultados para (10, 20, 30, 40, 50):", resultados1)

resultados2 = calcular_estatisticas(5, 3, 8, 1, 4)
print("Resultados para (5, 3, 8, 1, 4):", resultados2)

resultados3 = calcular_estatisticas(15.5, 2.3, 42.0, 7.8)
print("Resultados para (15.5, 2.3, 42.0, 7.8):", resultados3)

resultados4 = calcular_estatisticas()
print("Resultados para nenhum número:", resultados4)
