class Persona:
    def __init__(self):
        self.nombres = ""
        self.apellidos = ""
        self.apellido_casada = ""
        self.fecha_nacimiento = ""

    def insertar_nombres(self, nombres):
        self.nombres = nombres

    def insertar_apellidos(self, apellidos):
        self.apellidos = apellidos

    def insertar_apellido_casada(self, apellido_casada):
        self.apellido_casada = apellido_casada

    def insertar_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def obtener_nombres(self):
        return self.nombres

    def obtener_apellidos(self):
        if self.apellido_casada:
            return f"{self.apellidos} de casada: {self.apellido_casada}"
        else:
            return self.apellidos

    def obtener_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def obtener_nombre_completo(self):
        nombre_completo = f"{self.nombres} {self.obtener_apellidos()}"
        return nombre_completo

persona = Persona()
persona.insertar_nombres("Artemisa")
persona.insertar_apellidos("Meyer")
persona.insertar_apellido_casada("Koslova")
persona.insertar_fecha_nacimiento("12/12/1997")

print("Nombres:", persona.obtener_nombres())
print("Apellidos:", persona.obtener_apellidos())
print("Fecha de nacimiento:", persona.obtener_fecha_nacimiento())
print("Nombre completo:", persona.obtener_nombre_completo())

