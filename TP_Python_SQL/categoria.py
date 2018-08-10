from db import DB

class Categoria(object):
    id_Categoria = None
    nombre_Categoria = None

    def Insertar(self):
        DB.run("Insert into Categoria(id_Categoria,nombre_Categoria) Values("+ str(self.id_Categoria) +", '"+ self.nombre_Categoria +"');")

    def Borrar(self):
        DB.run("Delete from Producto where Categoria_idtable1 = ("+ str(self.id_Categoria) + ")")
        DB.run("Delete from Categoria where id_Categoria = ("+ str(self.id_Categoria) +")")

    def Modificar(self):
        DB.run("UPDATE Categoria SET nombre_Categoria = '%s' WHERE id_Categoria = %i;" % (self.nombre_Categoria, self.id_Categoria))


