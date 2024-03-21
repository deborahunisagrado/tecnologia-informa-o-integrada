def adicao(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Os argumentos devem ser números")
    return a + b

def subtracao(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Os argumentos devem ser números")
    return a - b

def multiplicacao(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Os argumentos devem ser números")
    return a * b

def divisao(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Os argumentos devem ser números")
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b
