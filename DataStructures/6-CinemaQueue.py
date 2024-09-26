lugares_vagos = [10, 2, 1, 3, 0]

def exibir_lugares_vagos():
    for i, lugares in enumerate(lugares_vagos):
        print(f"Salas {i + 1}: {lugares} lugares vagos")

while True:
    exibir_lugares_vagos()
    sala = int(input("Digite o número da sala (0 para sair): "))

    if sala == 0:
        print("Saindo do sistema.")
        break

    if 1 <= sala <= 5:
        quantidade = int(input("Digite a quantidade de lugares solicitados: "))

        if quantidade < 0:
            print("Quantidade de lugares deve ser um número positivo.")
            continue

        if lugares_vagos[sala - 1] >= quantidade:
            lugares_vagos[sala - 1] -= quantidade
            print(f"{quantidade} lugares vendidos na sala {sala}.")
        else:
            print(f"Não há lugares suficientes na sala {sala}. Apenas {lugares_vagos[sala - 1]} lugares disponíveis.")
    else:
        print("Sala inválida. Por favor, escolha uma sala entre 1 e 5.")
