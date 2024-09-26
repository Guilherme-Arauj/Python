def calcular_preco_total(codigo_produto, peso):
    precos = {
        1: 10.00,
        2: 20.00,
        3: 30.00,
        4: 40.00,
        5: 50.00,
        6: 60.00,
        7: 70.00,
        8: 80.00,
        9: 90.00,
        10: 100.00
    }
    return precos[codigo_produto] * peso

def calcular_imposto(preco_total, codigo_pais):
    impostos = {
        1: 0.05,  
        2: 0.10, 
        3: 0.15   
    }
    return preco_total * impostos[codigo_pais]

codigo_produto = int(input("Digite o código do produto (1 a 10): "))
peso = float(input("Digite o peso do produto em quilos: "))
codigo_pais = int(input("Digite o código do país de origem (1 a 3): "))

peso_em_gramas = peso * 1000
preco_total = calcular_preco_total(codigo_produto, peso)
imposto = calcular_imposto(preco_total, codigo_pais)
valor_total = preco_total + imposto

print(f"\nPeso do produto em gramas: {peso_em_gramas:.2f} g")
print(f"Preço total do produto: R$ {preco_total:.2f}")
print(f"Valor do imposto: R$ {imposto:.2f}")
print(f"Valor total (preço + imposto): R$ {valor_total:.2f}")
