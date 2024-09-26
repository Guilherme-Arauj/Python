def criptografar(numero):
    # Adiciona 7 a cada dígito e pega o resto da divisão por 10
    digitos = [int(d) for d in str(numero)]
    digitos_criptografados = [(d + 7) % 10 for d in digitos]
    
    # Troca o primeiro dígito pelo terceiro e o segundo pelo quarto
    digitos_criptografados[0], digitos_criptografados[2] = digitos_criptografados[2], digitos_criptografados[0]
    digitos_criptografados[1], digitos_criptografados[3] = digitos_criptografados[3], digitos_criptografados[1]
    
    # Converte a lista de dígitos de volta para um número
    return int(''.join(map(str, digitos_criptografados)))

def descriptografar(numero_criptografado):
    # Extrai os dígitos
    digitos = [int(d) for d in str(numero_criptografado)]
    
    # Inverte a troca de posições
    digitos[0], digitos[2] = digitos[2], digitos[0]
    digitos[1], digitos[3] = digitos[3], digitos[1]
    
    # Subtrai 7 e ajusta para o intervalo 0-9
    digitos_desscriptografados = [(d - 7) % 10 for d in digitos]
    
    # Converte a lista de dígitos de volta para um número
    return int(''.join(map(str, digitos_desscriptografados)))

# Exemplo de uso
numero_original = int(input("Digite um número inteiro de quatro dígitos: "))
numero_criptografado = criptografar(numero_original)
print(f"Número criptografado: {numero_criptografado}")

numero_desscriptografado = descriptografar(numero_criptografado)
print(f"Número original após descriptografia: {numero_desscriptografado}")
