import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def Obtenerperimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro
    
    def ObtenerArea(self):
        area = math.pi * (self.radio ** 2)
        return area
    
    def obtenervolumen(self):
        volumen= (4/3) * math.pi *(self.radio ** 3)
        return volumen
    
radio_circulo = 9.0
circulo= Circulo(radio_circulo)

perimetro= circulo.Obtenerperimetro()
area=circulo.Obtenerperimetro()
volumen= circulo.obtenervolumen()

print(f"Radio del cirulo: {radio_circulo} ")
print(f"perimetro del cirulo: {perimetro} ")
print(f"Area del ciruclo: {area} ")
print(f"Volumen de la esfera: {volumen} ")