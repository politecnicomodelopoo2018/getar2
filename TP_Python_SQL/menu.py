import os
from categoria import Categoria
from db import DB
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
        while(True):
            print("Opciones de Persona")
            print("1)Crear Persona")
            print("2)Borrar Persona")
            print("3)Actualizar Persona")
            print("4)Volver a Inicion:")
            opcion_persona = int(input("Elija una opcion: "))
            if int(opcion_persona) == 1:
                os.system('clear')
                while(True):
                    print("Crear Persona")
                    nombre_persona = input("Ingrese nombre: ")
                    apellido_persona = input("INgrese apellido: ")
                    dni_persona = input("Ingrese dni")
                    p = Persona()
                    p.dni = dni_persona
                    p.nombre = nombre_persona
                    p.apellido = apellido_persona
                    p.Insertar()
