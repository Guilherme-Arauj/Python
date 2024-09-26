def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = 10  
print(f"O {n}-ésimo termo da série de Fibonacci é: {fibonacci(n)}")
