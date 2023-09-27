def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

def fibonacci(numero):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(numero):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

while True:
    print("Menú:")
    print("1. Factorial")
    print("2. Secuencia de Fibonacci")
    print("3. Salir")
    
    opcion = input("Ingrese el número de opción que quiere ejecutar: ")
    
    if opcion == "1":
        numero = int(input("Ingrese un número para calcular su factorial: "))
        resultado = factorial(numero)
        print(f"{numero} = {numero} * {str(list(range(1, numero+1)))} = {resultado}")
    elif opcion == "2":
        numero = int(input("Ingrese un número para generar la secuencia de Fibonacci: "))
        secuencia = fibonacci(numero)
        print(f"{', '.join(map(str, secuencia))} ... Fibonacci({numero})")
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
