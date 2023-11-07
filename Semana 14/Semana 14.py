class Automovil:
    def __init__(self):
        self.modelo = 0
        self.precio = 0.0
        self.marca = ""
        self.disponible = True
        self.tipoCambioDolar = 0.0
        self.descuentoAplicado = 0.0

    def DefinirModelo(self, unModelo):
        self.modelo = unModelo

    def DefinirPrecio(self, unPrecio):
        self.precio = unPrecio

    def DefinirMarca(self, unaMarca):
        self.marca = unaMarca

    def DefinirTipoCambio(self, unTipoCambio):
        self.tipoCambioDolar = unTipoCambio

    def CambiarDisponibilidad(self):
        self.disponible = not self.disponible

    def MostrarDisponibilidad(self):
        if self.disponible:
            return "Disponible"
        else:
            return "No se encuentra disponible actualmente"

    def MostrarInformacion(self):
        precio_dolares = self.precio / self.tipoCambioDolar
        return "Marca: " + self.marca + ". Modelo: " + str(self.modelo) + ". Precio de venta: Q" + str(self.precio) + ". Precio en dólares $" + str(precio_dolares) + ". " + self.MostrarDisponibilidad()

    def AplicarDescuento(self, miDescuento):
        self.descuentoAplicado = miDescuento
        self.precio -= self.descuentoAplicado

auto = Automovil()
auto.DefinirModelo(2013)
auto.DefinirPrecio(35000.00)
auto.DefinirMarca("Chevrolet")
auto.DefinirTipoCambio(7.82)
auto.CambiarDisponibilidad()
auto.AplicarDescuento(2500.0)
print(auto.MostrarInformacion())
