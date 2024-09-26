def dv(cpf):

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    primeiro_digito = 0 if soma % 11 < 2 else 11 - (soma % 11)
    

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    segundo_digito = 0 if soma % 11 < 2 else 11 - (soma % 11)
    
    return primeiro_digito, segundo_digito

def cpf(n, d):
    n_str = str(n).zfill(9)  
    digitos = dv(n_str)
    return str(digitos[0]) + str(digitos[1]) == str(d)


cpf_num = 345702159
digito_verificador = 71
resultado = cpf(cpf_num, digito_verificador)
print(f"O CPF {cpf_num} tem o dígito verificador {digito_verificador}? {resultado}")  
