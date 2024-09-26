def calcular_digito_verificador(numero_conta):
    soma = sum(int(digito) for digito in str(numero_conta))
    digito_verificador = soma % 10
    return digito_verificador

numero_conta = input("Digite o número da conta (até 6 dígitos): ")

if len(numero_conta) > 6 or not numero_conta.isdigit():
    print("Número da conta inválido. Deve ter até 6 dígitos.")
else:
    digito_verificador = calcular_digito_verificador(numero_conta)
    numero_conta_completo = f"{int(numero_conta):06d}-{digito_verificador}"
    print(f"Número da conta completo: {numero_conta_completo}")
