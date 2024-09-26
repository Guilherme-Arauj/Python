from operacoes import *

def aplicar_operacao(num1=None, num2=None, operacao=None):
    if operacao is None:
        return "Operação não especificada"
    
    if operacao in [soma, subtracao, multiplicacao, divisao, resto, potencia]:
        return operacao(num1, num2)
    elif operacao in [raiz, fatorial]:
        return operacao(num1)
    elif operacao in [seno, cosseno, tangente]:
        return operacao(num1)
    else:
        return "Operação inválida"

resultado1 = aplicar_operacao(5, 3, soma)
resultado2 = aplicar_operacao(5, 3, subtracao)
resultado3 = aplicar_operacao(5, 3, multiplicacao)
resultado4 = aplicar_operacao(5, 3, divisao)
resultado5 = aplicar_operacao(5, 3, resto)
resultado6 = aplicar_operacao(2, 3, potencia)
resultado7 = aplicar_operacao(9, operacao=raiz)
resultado8 = aplicar_operacao(5, operacao=fatorial)
resultado9 = aplicar_operacao(0, operacao=cosseno)
resultado10 = aplicar_operacao(0, operacao=seno)
resultado11 = aplicar_operacao(0, operacao=tangente)

print(resultado1)  
print(resultado2)  
print(resultado3)  
print(resultado4)  
print(resultado5)  
print(resultado6)  
print(resultado7)  
print(resultado8)  
print(resultado9)  
print(resultado10)  
print(resultado11)  
