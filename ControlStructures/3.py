def converter_temperatura(valor, de_unidade, para_unidade):
    match (de_unidade, para_unidade):
        case ("Celsius", "Fahrenheit"):
            return (valor * 9/5) + 32
        case ("Celsius", "Kelvin"):
            return valor + 273.15
        case ("Fahrenheit", "Celsius"):
            return (valor - 32) * 5/9
        case ("Fahrenheit", "Kelvin"):
            return (valor - 32) * 5/9 + 273.15
        case ("Kelvin", "Celsius"):
            return valor - 273.15
        case ("Kelvin", "Fahrenheit"):
            return (valor - 273.15) * 9/5 + 32
        case _:
            return None

def converter_distancia(valor, de_unidade, para_unidade):
    match (de_unidade, para_unidade):
        case ("metros", "quilômetros"):
            return valor / 1000
        case ("metros", "milhas"):
            return valor / 1609.34
        case ("quilômetros", "metros"):
            return valor * 1000
        case ("quilômetros", "milhas"):
            return valor / 1.60934
        case ("milhas", "metros"):
            return valor * 1609.34
        case ("milhas", "quilômetros"):
            return valor * 1.60934
        case _:
            return None

def converter_tempo(valor, de_unidade, para_unidade):
    match (de_unidade, para_unidade):
        case ("segundos", "minutos"):
            return valor / 60
        case ("segundos", "horas"):
            return valor / 3600
        case ("minutos", "segundos"):
            return valor * 60
        case ("minutos", "horas"):
            return valor / 60
        case ("horas", "segundos"):
            return valor * 3600
        case ("horas", "minutos"):
            return valor * 60
        case _:
            return None

tipo_conversao = input("Escolha o tipo de conversão (temperatura, distancia, tempo): ").strip().lower()

if tipo_conversao == "temperatura":
    valor = float(input("Digite o valor: "))
    de_unidade = input("De (Celsius, Fahrenheit, Kelvin): ").strip()
    para_unidade = input("Para (Celsius, Fahrenheit, Kelvin): ").strip()
    resultado = converter_temperatura(valor, de_unidade, para_unidade)
elif tipo_conversao == "distancia":
    valor = float(input("Digite o valor: "))
    de_unidade = input("De (metros, quilômetros, milhas): ").strip()
    para_unidade = input("Para (metros, quilômetros, milhas): ").strip()
    resultado = converter_distancia(valor, de_unidade, para_unidade)
elif tipo_conversao == "tempo":
    valor = float(input("Digite o valor: "))
    de_unidade = input("De (segundos, minutos, horas): ").strip()
    para_unidade = input("Para (segundos, minutos, horas): ").strip()
    resultado = converter_tempo(valor, de_unidade, para_unidade)
else:
    resultado = None

if resultado is not None:
    print(f"O resultado da conversão é: {resultado}")
else:
    print("Conversão inválida.")
