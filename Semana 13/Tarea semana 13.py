import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def ObtenerPerimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro

    def ObtenerArea(self):
        area = math.pi * (self.radio ** 2)
        return area

    def ObtenerVolumen(self):
        volumen = (4/3) * math.pi * (self.radio ** 3)
        return volumen


num_circulos = int(input("Ingrese la cantidad de círculos que desea crear: "))


circulos = []
for i in range(num_circulos):
    radio_circulo = float(input(f"Ingrese el radio del círculo {i + 1}: "))
    circulo = Circulo(radio_circulo)
    circulos.append(circulo)


for i, circulo in enumerate(circulos):
    print(f"Resultados para el círculo {i + 1}:")
    print(f"Radio: {circulo.radio}")
    print(f"Perímetro: {circulo.ObtenerPerimetro()}")
    print(f"Área: {circulo.ObtenerArea()}")
    print(f"Volumen de la esfera: {circulo.ObtenerVolumen()}")
    print()
