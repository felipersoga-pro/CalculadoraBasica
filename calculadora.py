def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    """Realiza la multiplicación de dos números."""
    return a * b

def dividir(a, b):
    """Realiza la división manejando el error por cero."""
    if b == 0:
        raise ValueError("Error: No se puede dividir por cero")
    return a / b

def obtener_numeros():
    """Solicita y valida los números."""
    while True:
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            return num1, num2
        except ValueError:
            print("Entrada inválida.")

def calculadora():
    print("--- CALCULADORA EN DESARROLLO ---")
    n1, n2 = obtener_numeros()
    print(f"Suma: {sumar(n1, n2)}")
    print(f"Multiplicación: {multiplicar(n1, n2)}")

if __name__ == "__main__":
    calculadora()