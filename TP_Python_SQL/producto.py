from TP_Python_SQL.db import DB

class Producto(object):
    id_Producto = None
    nombre_Producto = None
    precio = None
    categoria = None

    def Insertar(self):
        DB.run("insert into Producto(id_Producto,nombre,precio,Categoria_idtable1) Values(" + str(self.id_Producto) + ", '" + self.nombre_Producto + "', " +str(self.precio) + "," + str(self.categoria) + ");")

    def Borrar(self):
        DB.run("Delete from Producto where id_Producto = (" + str(self.id_Producto) + ");")

    def Modificar(self):
        DB.run("UPDATE Producto SET nombre = '%s', precio = %i, Categoria_idtable1 = %i WHERE id_Producto = %i;" % (self.nombre, self.precio, self.categoria,self.id_Producto))