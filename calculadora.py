# Suma
def sumar(a, b):
    return a + b

# Resta
def restar (a, b):
    return a - b

# Multiplicación
def multiplicar(a, b):
    return a * b

# División
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: la división entre cero no es posible."

if __name__ == "__main__":
    print(sumar(5, 3))
    print(restar(7, 1))
    print(multiplicar(4, 4))
    print(dividir(10, 2))