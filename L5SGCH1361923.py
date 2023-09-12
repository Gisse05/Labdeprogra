
print("Ejercicio 1")

try:
    numero = int(input("Número ENTERO: "))
    if numero > 0:
        resultado = "positivo"
    elif numero < 0:
        resultado = "negativo"
    else:
        resultado = "cero"

    print("RESULTADO:", resultado)

except ValueError:
    print("Error: Debes ingresar un número entero válido.")
