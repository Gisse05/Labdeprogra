# se usara despues para saber cual de las dos lineas tiene un indice de eficiencia mas alto (o incluso si son iguales)
indices_de_eficiencia_de_las_lineas = []

# repite el bloque de codigo para las dos lineas
for indice_de_linea in range(2):
    numero_de_linea = indice_de_linea + 1

    # consigue una cadena que representa la cantidad de metros cuadrados vendidos del usuario y la convierte en entero
    metros_cuadrados_vendidos = int(input("Ingrese la cantidad de metros cuadrados vendidos en linea no. " + str(numero_de_linea) + ": "))
    
    # consigue una cadena que representa el precio por cada metro cuadrado de los que vendieron del usuario y la convierte en entero
    precio_por_metro_cuadrado = int(input("Ingrese el precio por metro cuadrado: "))

    # estaba en ejemplo y aqui tambien
    print("Costo por metro cuadrado: ")

    # consigue una cadena que representa la cantidad de empleados del usuario y la convierte en entero
    cantidad_de_empleados = int(input("    Ingrese la cantidad de empleados en linea no. " + str(numero_de_linea) + ": "))
    
    # se usaran para hacer calculas despues
    precio_por_hora_de_empleados = []
    cantidad_de_horas_que_trabajaron_los_empleados = []

    # el "for" repite el bloque de codigo por cada empleado que hay en linea
    for indice in range(cantidad_de_empleados):

        # "indice + 1" porque el indice inicia en 0
        numero_de_empleado = indice + 1

        # consigue una cadena que representa las horas que trabajo el empleado del usuario y la convierte en entero
        cantidad_de_horas_que_trabajo_el_empleado = int(input("   Ingrese la cantidad de horas que trabajo el empleado no. " + str(numero_de_empleado) + ": "))
        
        # consigue una cadena que representa el precio por hora del empleado del usuario y la convierte en entero
        precio_por_hora_de_empleado = int(input("   Ingrese el precio por hora del empleado no. " + str(numero_de_empleado) + ": "))

        # agrega los valores a los "arrays" para usarlas despues
        precio_por_hora_de_empleados.append(precio_por_hora_de_empleado)
        cantidad_de_horas_que_trabajaron_los_empleados.append(cantidad_de_horas_que_trabajo_el_empleado)

    # valor de la ganancia total
    ganancia_total = metros_cuadrados_vendidos * precio_por_metro_cuadrado

    # variable que representa el calcula de la ganancia total, ejemplo: "900 * 5"
    cadena_representante_del_calculo_de_la_ganancia_total = str(metros_cuadrados_vendidos) + " * " + str(precio_por_metro_cuadrado)

    # muestra el calculo de la ganancia total y su resultado
    print("Ganancia total = " + cadena_representante_del_calculo_de_la_ganancia_total + " = " + str(ganancia_total))

    # variable que representa el calculo del costo total, ejemplo: "(10 * 50) + (8 * 40)"...
    cadena_representante_del_calculo_del_costo_total = ""
    costo_total = 0

    # el "for" repite el bloque de codigo por cada empleado que hay en linea
    for indice in range(cantidad_de_empleados):
        # añade un "+" a la cadena *unicamente si* no es el primer empleado que se procesa
        # si esto no fuera "(10 * 50) + (8 * 40)" se convirtiera en "+ (10 * 50) + (8 * 40)"
        if indice > 0:
            cadena_representante_del_calculo_del_costo_total += " + "

        # consigue las horas y precio por las horas del empleado siendo procesado desde los "arrays"
        cantidad_de_horas_que_trabajo_el_empleado = cantidad_de_horas_que_trabajaron_los_empleados[indice]
        precio_por_hora_de_empleado = precio_por_hora_de_empleados[indice]

        # agrega al valor numerico del costo total
        costo_total += cantidad_de_horas_que_trabajo_el_empleado * precio_por_hora_de_empleado

        # agrega el calculo del costo del empleado a la cadena
        cadena_representante_del_calculo_del_costo_total += "(" + str(cantidad_de_horas_que_trabajo_el_empleado) + " * " + str(precio_por_hora_de_empleado) + ")"

    # muestra el calculo y el valor del costo total
    print("Costo total = " + cadena_representante_del_calculo_del_costo_total + " = " + str(costo_total))

    # valor de la ganancia neta
    ganancia_neta = ganancia_total - costo_total
    print("Ganancia neta = " + str(ganancia_total) + " - " + str(costo_total) + " = " + str(ganancia_neta))

    # valor del indice de eficiencia convertido a un entero como en el ejemplo
    indice_de_eficiencia = int(ganancia_neta / cantidad_de_empleados)

    # cadena que representa el calculo del indice de eficiencia
    cadena_representante_del_calculo_del_indice_de_eficiencia = str(ganancia_neta) + " / " + str(cantidad_de_empleados)

    # muestra el calculo y valor del indice de eficiencia
    print("Indice de eficiencia = " + cadena_representante_del_calculo_del_indice_de_eficiencia + " = " + str(indice_de_eficiencia))

    indices_de_eficiencia_de_las_lineas.append(indice_de_eficiencia)

    # sirve para hacer dos nuevas linea como espacio
    print("")
    print("")
    

# muestra si la linea no. 1 o linea no. 2 tiene un indice de eficiencia mayor que la otra linea,
# tambien si son iguales muestra la cadena "Ninguna de las 2 lineas tuvo un indice de eficiencia mas alto que la otra"
if indices_de_eficiencia_de_las_lineas[0] > indices_de_eficiencia_de_las_lineas[1]:
    print("La linea no. 1 tuvo un indice de eficiencia mas alto que la linea no. 2")

if indices_de_eficiencia_de_las_lineas[0] < indices_de_eficiencia_de_las_lineas[1]:
    print("La linea no. 2 tuvo un indice de eficiencia mas alto que la linea no. 1")

if indices_de_eficiencia_de_las_lineas[0] == indices_de_eficiencia_de_las_lineas[1]:
    print("Ninguna de las 2 lineas tuvo un indice de eficiencia mas alto que la otra")

# fin