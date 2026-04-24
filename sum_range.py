# Replace the "ANSWER HERE" for your answer

def sum_to_n(n):
    """
    Retorna la suma de todos los enteros desde 1 hasta n (inclusive).
    Si n <= 0, retorna 0.

    Ejemplo: sum_to_n(5) -> 15  (1+2+3+4+5)
    """
    if n <= 0:
        return 0 
    suma = 0
    for i in range(1, n+1):
        suma = suma + i

    return suma

def sum_evens(n):
    if n <= 0:
        return 0 
    suma = 0
    for i in range(0, n+1, 2):
        suma = suma + i
    return suma


def factorial(n):

    if n <= 0:
        return 1
    
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
    return factorial

print(sum_evens(10))