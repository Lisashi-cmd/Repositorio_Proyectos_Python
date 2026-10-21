
# Primer programa super sencillo, con la función de actuar como una Calculadora Simple.

# Función para realizar las operaciones matemáticas:

def calculadora(a, b, operacion):
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    elif operacion == "multiplicación":
        return a * b
    elif operacion == "división":
        if b != 0:
            return a / b
        else:
            return "Error: No se puede dividir por cero."
    else:
        return "Operación inválida. Por favor, elija suma, resta, multiplicación o división."


while True:
    print("""\n === Calculadora Simple ===
- Ingrese dos números y la operación que desea realizar: 
    
    + Suma
    - Resta
    *  Multiplicación
    /  División
          
 - Ingrese 'salir' para terminar el programa.
    """)

    try:
        # Solicitar al usuario que ingrese dos números y la operación:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        operacion_usuario = input(
            "Ingrese la operación a realizar (suma, resta, multiplicación o división): ").lower()
        resultado = calculadora(numero1, numero2, operacion_usuario)
        print(f"El resultado de la {operacion_usuario} es: {resultado}")
    except ValueError:
        print("Por favor, ingrese un número válido.")
        if input("¿Desea intentar de nuevo? (s/n): ").lower() != 's':
            print("Saliendo del programa...")
            break
    except KeyboardInterrupt:
        print("\nSaliendo del programa...")
        break
