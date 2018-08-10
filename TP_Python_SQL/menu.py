import os
from categoria import Categoria
from persona import Persona
from producto import Producto

while(True):
    print("Bienvenido al Supermercado de la esquina")
    print("1)Operaciones de Persona")
    print("2)Operaciones de Categoria")
    print("3)Operaciones de Producto")
    print("4)Operaciones de Compra")
    opcion = input("Elija una opcion: ")
    if int(opcion) == 1:
        os.system('clear')
        print("Opciones de Persona")
        print("1)Agregar Persona")
        print("2)Borrar Persona")
        print("3)Actualizar Persona")
        opcion_persona = int(input("Elija una opcion: "))
        if int(opcion_persona) == 1:
            os.system('clear')
            nombre_persona = input("Ingrese nombre: ")
            apellido_persona = input("Ingrese apellido: ")
            p = Persona()
            p.dni = "NULL"
            p.nombre = nombre_persona
            p.apellido = apellido_persona
            p.Insertar()
            print ("Persona Agregada")
            os.system('clear')
        if int(opcion_persona) == 2:
            os.system('clear')
            print("Borrar Persona")
            dni_persona = input("Ingrese DNI: ")
            p = Persona()
            p.dni = dni_persona
            p.Borrar()
            os.system('clear')
        if int(opcion_persona) == 3:
            os.system('clear')
            print("Modificar Persona")
            dni_persona = int(input("Ingrese DNI: "))
            nombre_persona = input("Ingrese nombre nuevo: ")
            apellido_persona = input("Ingrese apellido nuevo: ")
            p = Persona()
            p.dni = dni_persona
            p.nombre = nombre_persona
            p.apellido = apellido_persona
            p.Modificar()
            os.system('clear')
    if int(opcion) == 2:
        os.system('clear')
        print("1)Agregar Categoria")
        print("2)Borrar Categoria")
        print("3)Modificar Categoria")
        opcion_categoria = int(input("Elija una opcion: "))
        if opcion_categoria == 1:
            os.system('clear')
            print("Agregar Categoria")
            categoria_nombre = input("Ingrese nombre: ")
            c = Categoria()
            c.id_Categoria = "NULL"
            c.nombre_Categoria = categoria_nombre
            c.Insertar()
            os.system('clear')
        if opcion_categoria == 2:
            os.system('clear')
            print("Borrar Categoria")
            idCategoria = int(input("Ingrese ID: "))
            c = Categoria()
            c.id_Categoria = idCategoria
            c.Borrar()
            os.system('clear')
        if opcion_categoria == 3:
            os.system('clear')
            print("Modificar Categoria")
            idCategoria = int(input("Ingrese ID: "))
            categoria_nombre = input("Ingrese nuevo nombre: ")
            c = Categoria()
            c.id_Categoria = idCategoria
            c.nombre_Categoria = categoria_nombre
            c.Modificar()
            print("Categoria modificada")




