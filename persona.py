from db import DB

class Persona(object):
    dni = None
    nombre = None
    apellido = None

    def __init__(self):
        Lista_Compras = []

    def insertar(self):
        DB.run("insert into Persona(dni,nombre,apellido) Values(" + self.dni + ", " + self.nombre + ", " + self.apellido + ");")

    def Borrar(self):
        DB.run("Delete from Persona set dni = self.dni ")

    def Modificar(self,nuevo_dni,nuevo_nombre,nuevo_apellido):
        DB.run("Update Persona set dni = nuevo_dni and  nombre = nuevo_nombre and apellido = nuevo_apellido where dni = self.dni")