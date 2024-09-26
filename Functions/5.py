def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def potencia(base, exp):
    if exp == 0:
        return 1
    else:
        return base * potencia(base, exp - 1)

def resto_divisao(a, b):
    if a < b:
        return a
    else:
        return resto_divisao(a - b, b)

def quociente_divisao(a, b):
    if a < b:
        return 0
    else:
        return 1 + quociente_divisao(a - b, b)

def produto(a, b):
    if b == 0:
        return 0
    else:
        return a + produto(a, b - 1)

def suc(n):
    return n + 1

def pred(n):
    return n - 1

def soma(a, b):
    if b == 0:
        return a
    else:
        return soma(suc(a), pred(b))



print("Fatorial de 4:", fatorial(4))              
print("2 elevado a 3:", potencia(2, 3))            
print("Resto da divisão 10 por 3:", resto_divisao(10, 3))  
print("Quociente da divisão 10 por 3:", quociente_divisao(10, 3))  
print("Produto de 3 e 4:", produto(3, 4))          
print("Soma de 3 e 4:", soma(3, 4))               
