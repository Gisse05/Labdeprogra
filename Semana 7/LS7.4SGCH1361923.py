import math
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

while True:
    print("\nMenú:")
    print("1. Calcular a * b + c")
    print("2. Calcular a * (b + c)")
    print("3. Calcular a / b * c")
    print("4. Calcular 3a + 2b")
    print("5. Calcular c / 2")
    print("6. Calcular expresión cuadrática")
    print("7. Salir")

    opcion = int(input("Seleccione una opción (1-7): "))

    if opcion == 1:
        resultado = a * b + c
        print(f"Resultado: {resultado}")
    elif opcion == 2:
        resultado = a * (b + c)
        print(f"Resultado: {resultado}")
    elif opcion == 3:
        resultado = a / b * c
        print(f"Resultado: {resultado}")
    elif opcion == 4:
        resultado = 3 * a + 2 * b
        print(f"Resultado: {resultado}")
    elif opcion == 5:
        resultado = c / 2
        print(f"Resultado: {resultado}")
    elif opcion == 6:
        if a == 0:
            print("Error: 'a' no puede ser igual a 0.")
        else:
            discriminante = b**2 - 4 * a * c
            if discriminante < 0:
                print("Error: El discriminante es negativo. No hay soluciones reales.")
            else:
                x1 = (-b + math.sqrt(discriminante)) / (2 * a)
                x2 = (-b - math.sqrt(discriminante)) / (2 * a)
                print(f"Solución 1: x = {x1}")
                print(f"Solución 2: x = {x2}")
    elif opcion == 7:
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

print("¡Gracias por usar el programa!")
