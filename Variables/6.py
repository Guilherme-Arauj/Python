total_segundos = int(input("Digite a quantidade de segundos: "))

dias = total_segundos // 86400
horas = (total_segundos % 86400) // 3600
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60

print(f"{total_segundos} segundos equivalem a {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")
