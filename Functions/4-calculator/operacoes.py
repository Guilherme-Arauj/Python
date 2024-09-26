def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b if b != 0 else "Divisão por zero"

def resto(a, b):
    return a % b

def potencia(base, exp):
    return base ** exp

def raiz(numero):
    return numero ** 0.5

def fatorial(n):
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def logaritmo(a, base):
    return logaritmo(a / base, base) + 1 if a >= base else 0

def cosseno(x):
    resultado = 1
    termo = 1
    for i in range(1, 10):
        termo *= -x * x / (2 * i * (2 * i - 1))
        resultado += termo
    return resultado

def seno(x):
    resultado = 0
    termo = x
    for i in range(1, 10):
        resultado += termo
        termo *= -x * x / (2 * i * (2 * i + 1))
    return resultado

def tangente(x):
    return seno(x) / cosseno(x)
