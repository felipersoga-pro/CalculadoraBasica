def sumar(a, b):
    """Realiza la suma de dos números."""
    return a + b

def restar(a, b):
    """Realiza la resta de dos números."""
    return a - b

def calculadora():
    """Función principal que ejecuta la calculadora."""
    print("--- CALCULADORA INICIAL ---")
    # En este primer paso, solo probamos la estructura base
    n1, n2 = 10, 5
    print(f"Suma base: {sumar(n1, n2)}")

if __name__ == "__main__":
    calculadora()