# Clase Tablero
class Tablero:
    def __init__(self):
        """
        #Inicializa un tablero con dimensiones predefinidas.
        Cada celda se inicializa con "O" para representar el océano.
        """
        self.dimension = 10 # Tamaño del tablero: 10x10
        self.matriz = [["O" for _ in range(self.dimension)] for _ in range(self.dimension)]

    def mostrar(self):
        
        #Muestra el estado actual del tablero en la consola.
        
        for fila in self.matriz:
            print(" ".join(fila))


# Clase Barco
class Barco:
    def __init__(self, fila, columna, orientacion, tipo):
        
        #Inicializa un barco con su posición, orientación y tipo.
        
        self.fila = fila
        self.columna = columna
        self.orientacion = orientacion
        self.tipo = tipo

    def ocupar_casillas(self, tablero):
        
        #Ocupa las casillas correspondientes en el tablero con "B" para representar el barco.
        
        tamanos_segun_tipos = {
            "grande": 5,
            "pequeño": 3
        }

        if self.orientacion == "horizontal":
            for i in range(tamanos_segun_tipos[self.tipo]):
                tablero.matriz[self.fila][self.columna + i] = "B"
        elif self.orientacion == "vertical":
            for i in range(tamanos_segun_tipos[self.tipo]):
                tablero.matriz[self.fila + i][self.columna] = "B"


# Clase Jugador
class Jugador:
    def __init__(self, nombre):
        
        #Inicializa un jugador con un nombre, un tablero y una lista de barcos.
        
        self.nombre = nombre
        self.tablero = Tablero()
        self.barcos = []

    def colocar_barcos(self):
        
        #Permite al jugador colocar barcos en su tablero.
        
        for _ in range(3):
            fila, columna, orientacion, tipo = self.obtener_datos_barco()
            barco = Barco(fila, columna, orientacion, tipo)
            barco.ocupar_casillas(self.tablero)
            self.barcos.append(barco)

        for _ in range(2):
            fila, columna, orientacion, tipo = self.obtener_datos_barco()
            barco = Barco(fila, columna, orientacion, tipo)
            barco.ocupar_casillas(self.tablero)
            self.barcos.append(barco)

    def obtener_datos_barco(self):
        
        #Solicita al usuario la información del barco con manejo de errores.
        
        while True:
            try:
                fila = input(f"{self.nombre}, ingresa la fila para el barco (A-J): ").upper()
                columna = int(input(f"{self.nombre}, ingresa la columna para el barco (1-10): ")) - 1
                orientacion = input(f"{self.nombre}, ingresa la orientación del barco (horizontal/vertical): ")
                tipo = input(f"{self.nombre}, ingresa el tipo del barco (pequeño/grande): ")
                fila = ord(fila) - ord('A')

                if not (0 <= fila < self.tablero.dimension) or not (0 <= columna < self.tablero.dimension):
                    raise ValueError("La fila y columna ingresadas están fuera de rango.")

                return fila, columna, orientacion, tipo
            except ValueError as e:
                print(f"Error: {e}")
                print("Por favor, ingresa datos válidos.")

    def disparar(self, oponente):
        
        #Permite al jugador disparar al oponente y actualiza el tablero del oponente en consecuencia.
        
        while True:
            try:
                fila = input(f"{self.nombre}, ingresa la fila para disparar al oponente (A-J): ").upper()
                columna = int(input(f"{self.nombre}, ingresa la columna para disparar al oponente (1-10): ")) - 1

                if not (0 <= fila < self.tablero.dimension) or not (0 <= columna < self.tablero.dimension):
                    raise ValueError("La fila y columna ingresadas están fuera de rango.")

                if oponente.tablero.matriz[fila][columna] == "B":
                    print("¡Hundido!")
                    oponente.tablero.matriz[fila][columna] = "X"
                elif oponente.tablero.matriz[fila][columna] == "X":
                    print("¡Repetido!")
                else:
                    print("¡Fallo!")
                    oponente.tablero.matriz[fila][columna] = "X"

                break
            except ValueError as e:
                print(f"Error: {e}")
                print("Por favor, ingresa datos válidos.")

    def ha_ganado(self, oponente):
        
        #Verifica si el jugador ha ganado el juego al hundir todos los barcos del oponente.
        
        return all(barco.tipo == "pequeño" for barco in oponente.barcos)


# Función principal del juego
def jugar_batalla_naval():
    
    #Función principal que inicia y coordina el juego de batalla naval entre dos jugadores.
    
    print("Bienvenido a Batalla Naval")

    jugador1 = Jugador("Jugador 1")
    jugador2 = Jugador("Jugador 2")

    print("Jugador 1, coloca tus barcos:")
    jugador1.colocar_barcos()
    print("\nTablero de Jugador 1:")
    jugador1.tablero.mostrar()

    print("\nJugador 2, coloca tus barcos:")
    jugador2.colocar_barcos()
    print("\nTablero de Jugador 2:")
    jugador2.tablero.mostrar()

    turno = jugador1

    while True:
        print(f"\nTurno de {turno.nombre}")
        turno.disparar(jugador2)
        jugador2.tablero.mostrar()

        if jugador1.ha_ganado(jugador2):
            print(f"{jugador1.nombre} ha ganado.")
            break

        turno = jugador2 if turno == jugador1 else jugador1


if __name__ == "__main__":
    jugar_batalla_naval()
