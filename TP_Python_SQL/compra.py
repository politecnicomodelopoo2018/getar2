from db import DB

class Compra(object):
    dni = None
    id = None
    def Insertar(self):
        DB.run("insert into Compra(Persona_dni,Producto_id_Producto) Values(" + str(self.dni) + ", " + str(self.id_Producto) + ");")

    def Borrar(self,dni):
        DB.run("Delete from Compra where Persona_dni = (" + str(self.dni) + ");")



