print("Ejercicio 3: Jerarquía de operaciones")

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

resultado_1 = a * b + c
resultado_2 = a * (b + c)
resultado_3 = a / b * c
resultado_4 = 3 * a + 2 * b
resultado_5 = c / 2

print(f"Resultado 1: a * b + c = {resultado_1}")
print(f"Resultado 2: a * (b + c) = {resultado_2}")
print(f"Resultado 3: a / b * c = {resultado_3}")
print(f"Resultado 4: 3 * a + 2 * b = {resultado_4}")
print(f"Resultado 5: c / 2 = {resultado_5}")
