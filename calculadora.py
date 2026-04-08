def sumar(a, b):
    """Realiza la suma de dos números."""
    return a + b

def restar(a, b):
    """Realiza la resta de dos números."""
    return a - b

def mostrar_menu():
    """Muestra el menú de la calculadora."""
    print("\n--- CALCULADORA ---")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Salir")
    print("------------------------------")

def obtener_numeros():
    """Solicita y valida los dos números al usuario."""
    while True:
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            return num1, num2
        except ValueError:
            print("Entrada inválida. Por favor, introduce solo números válidos.")

def calculadora():
    """Función principal que ejecuta la calculadora."""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '5':
            print("¡Gracias por usar la calculadora! ¡Hasta pronto!")
            break

        # Usamos match case para manejar las opciones
        match opcion:
            case '1' | '+':
                print("--- SUMA ---")
                num1, num2 = obtener_numeros()
                resultado = sumar(num1, num2)
                print(f"El resultado de {num1} + {num2} es: {resultado}")

            case '2' | '-':
                print("--- RESTA ---")
                num1, num2 = obtener_numeros()
                resultado = restar(num1, num2)
                print(f"El resultado de {num1} - {num2} es: {resultado}")

            case '3' | '*':
                print("--- MULTIPLICACIÓN ---")
                num1, num2 = obtener_numeros()
                resultado = multiplicar(num1, num2)
                print(f"El resultado de {num1} * {num2} es: {resultado}")

            case '4' | '/':
                print("--- DIVISIÓN ---")
                num1, num2 = obtener_numeros()
                try:
                    resultado = dividir(num1, num2)
                    print(f"El resultado de {num1} / {num2} es: {resultado}")
                except ValueError as e:
                    # Captura el error de división por cero y lo muestra
                    print(e)
                    # El bucle while principal automáticamente vuelve al menú

            case _:
                print("Opción no válida. Por favor, selecciona un número entre 1 y 5.")

# Ejecución de la calculadora
if __name__ == "__main__":
    calculadora()