
print("Ejercicio 2")
numero_dia = int(input("Ingrese un número de día"))


if numero_dia >= 1 and numero_dia <= 7:
    if numero_dia == 1:
        dia = "lunes"
    elif numero_dia == 2:
        dia = "martes"
    elif numero_dia == 3:
        dia = "miércoles"
    elif numero_dia == 4:
        dia = "jueves"
    elif numero_dia == 5:
        dia = "viernes"
    elif numero_dia == 6:
        dia = "sábado"
    else:
        dia = "domingo"
    
    print("DIA:", dia)
else:
    print("Error. El número a ingresar debe estar contenido entre 1 y 7")
