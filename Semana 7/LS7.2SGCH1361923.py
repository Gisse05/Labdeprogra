while True:
    print("Ejercicio 1: Operaciones Aritméticas")
    
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    print("\nOperaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo")
    print("6. Exponenciación")
    print("7. Cociente")
    print("8. Salir")
    
    opcion = int(input("Elija una operación (1-8): "))
    
    if opcion == 1:
        resultado = num1 + num2
        operacion = "+"
    elif opcion == 2:
        resultado = num1 - num2
        operacion = "-"
    elif opcion == 3:
        resultado = num1 * num2
        operacion = "*"
    elif opcion == 4:
        if num2 != 0:
            resultado = num1 / num2
            operacion = "/"
        else:
            print("No se puede dividir por cero.")
            continue
    elif opcion == 5:
        resultado = num1 % num2
        operacion = "%"
    elif opcion == 6:
        resultado = num1 ** num2
        operacion = "**"
    elif opcion == 7:
        resultado = num1 // num2
        operacion = "//"
    elif opcion == 8:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
        continue

    # Mostrar el resultado
    print(f"{num1} {operacion} {num2} = {resultado}\n")
