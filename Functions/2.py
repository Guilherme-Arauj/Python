def formatar_data(dia, mes, ano):
    return f"{dia:02}/{mes:02}/{ano}"


data1 = formatar_data(dia=5, mes=9, ano=2024)
data2 = formatar_data(ano=2023, mes=12, dia=1)
data3 = formatar_data(mes=7, dia=4, ano=2021)

print(data1)  
print(data2)  
print(data3)  
