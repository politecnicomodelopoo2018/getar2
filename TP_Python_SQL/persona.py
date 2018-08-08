from db import DB

class Persona(object):
    dni = None
    nombre = None
    apellido = None


    def Insertar(self):
        DB.run("insert into Persona(dni,nombre,apellido) Values(" + str(self.dni) + ", '" + self.nombre + "', '" + self.apellido + "');")

    def Borrar(self):
        DB.run("Delete from Persona where dni = (" + str(self.dni) + ");")

    def Modificar(self):
        DB.run("UPDATE Persona SET nombre = '%s', apellido = '%s' WHERE dni = %i;" % (self.nombre, self.apellido, self.dni))

