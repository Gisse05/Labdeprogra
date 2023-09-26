def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
 
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        sequence.append(a) #agrega el elemento al final de la lista.
    return sequence

while True:
    print("Menú:")
    print("1. Factorial")
    print("2. Secuencia de Fibonacci")
    print("3. Salir")
    
    opcion = input("Ingrese el número de opción que desea ejecutar: ")
    if opcion == '1':
        numero = int(input("Ingrese un número para calcular su factorial: "))
        resultado = factorial(numero)
        print(f"{numero} = {numero}! = {resultado}")

    