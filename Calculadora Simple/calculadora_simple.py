# Primer programa super sencillo, con la función de actuar como una Calculadora Simple.

# Función para realizar las operaciones matemáticas:

def calculadora(a: float, b: float, operacion: str):
    if operacion == "suma" or operacion == '+':
        return a + b
    elif operacion == "resta" or operacion == '-':
        return a - b
    elif operacion == "multiplicación" or operacion == '*':
        return a * b
    elif operacion == "división" or operacion == '/':
        if b != 0:
            return a / b
        else:
            return "Error: No se puede dividir por cero."
    else:
        return "Operación inválida. Por favor, elija suma, resta, multiplicación o división."


while True:
    print("""\n === Calculadora ===
- Ingrese los números y la operación a realizar... 
    
    [+] - Suma
    [-] - Resta
    [*] - Multiplicación
    [/] - División
          
 - Ingrese 'salir' para terminar el programa.
    """)

    try:
        # Solicitar al usuario que ingrese dos números y la operación:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        operacion_usuario = input(
            "Ingrese una operación (segun nombre o signo de la misma):"
            " | 1- suma '+'\n | 2- resta '-'\n | 3- multiplicación '*'\n | 4- división '/'\n").lower()
        
        resultado = calculadora(numero1, numero2, operacion_usuario)
        print(f"El resultado de la {operacion_usuario} es: {resultado}")
    except ValueError:
        print("Por favor, ingrese un número válido.")
        if input("¿Desea realizar otra operación? (s/n): ").lower() != 's':
            print("Saliendo del programa...")
            break
    except KeyboardInterrupt:
        print("\nSaliendo del programa...")
        break
