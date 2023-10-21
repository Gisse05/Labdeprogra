
cadena = input("Ingrese una cadena de caracteres: ")

contador_0 = 0
contador_1 = 0
otros_caracteres = ""

for caracter in cadena:
    if caracter == '0':
        contador_0 += 1
    elif caracter == '1':
        contador_1 += 1
    else:
        otros_caracteres += caracter

print(f"Cantidad 0: {contador_0}")
print(f"Cantidad 1: {contador_1}")
print("Otros caracteres:", otros_caracteres)