def convertir(numero):
    string = ""

    # si el numero es zero retorna zero
    if numero == 0:
        return "0"

    # lista de digitos
    digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

    # algoritmo
    while (numero != 0):
        residuo = numero % 16
        numero = numero // 16

        # saca el digito hexadecimal
        string = string + digitos[residuo]

    string_al_revez = ""

    # consigue el string al revez
    for indice in range(len(string)):
        string_al_revez = string_al_revez + string[-(indice + 1)]
        # saca a la letra de un indice inverso (del final al incio)

    return string_al_revez

print(convertir(int(input())))