from db import DB

class Compra(object):
    dni = None
    id = None
    def Insertar(self):
        DB.run("insert into Compra(Persona_dni,Producto_id_Producto) Values(" + str(self.dni) + ", " + str(self.id_Producto) + ");")

    def Borrar(self,dni):
        DB.run("Delete from Compra where Persona_dni = (" + str(self.dni) + ");")

    def Modificar(self):
        DB.run("UPDATE Compra SET Persona_dni = %i, Producto_id_Producto = %i WHERE Persona_dni = %i;" % (self.dni, self.id, self.dni))

