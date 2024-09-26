def exibir_caixa(largura, altura):
    for i in range(altura):
        print('*' * largura)

def exibir_oval(altura):
    for i in range(altura):
        espacos = ' ' * (altura - i)
        asteriscos = '*' * (2 * i + 1)
        print(espacos + asteriscos)

def exibir_seta(tamanho):
    for i in range(tamanho):
        print(' ' * (tamanho - i - 1) + '*' * (2 * i + 1))
    print(' ' * (tamanho - 1) + '*')
    for i in range(tamanho - 1):
        print(' ' * (tamanho - 1) + '*')

def exibir_losango(tamanho):
    for i in range(tamanho):
        espacos = ' ' * (tamanho - i - 1)
        asteriscos = '*' * (2 * i + 1)
        print(espacos + asteriscos)
    for i in range(tamanho - 2, -1, -1):
        espacos = ' ' * (tamanho - i - 1)
        asteriscos = '*' * (2 * i + 1)
        print(espacos + asteriscos)

print("Caixa:")
exibir_caixa(10, 5)
print("\nOval:")
exibir_oval(5)
print("\nSeta:")
exibir_seta(5)
print("\nLosango:")
exibir_losango(5)
