from db import DB

class Compra(object):
    dni = None
    id = None

    def Insertar(self):
        DB.run("insert into Compra(Persona_dni,Producto_id_Producto) Values(" + str(self.dni) + ", " + str(self.id) + ");")

    def Borrar(self):
        DB.run("Delete from Compra where Persona_dni = (" + str(self.dni) + ") and Producto_id_Producto = (" + str(self.id) + ") ;")



