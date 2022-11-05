from asyncio.windows_events import NULL
from genericpath import exists
import os
productos_nombres_precios = {}
'''
Hecho por Carlos Eduardo Chavarria Centeno
@EdCenten0
05/11/2022

'''
# Este es un ejercicio de practica de diccionarios basicos hecho por estudiar y por hobbie





def agregar_productos(param_productos_nombres_precios):
    os.system("cls")

    i = 0
    while(i == 0):
        nombre_producto = input("Ingrese el nombre del producto a agregar: ")
        try:
            precio_producto = int(input("Ingrese el precio del producto: "))
        except:
            print("Por favor, agregue un numero")
            break

        print("\nDesea agregar otro producto?")
        param_productos_nombres_precios[nombre_producto] = precio_producto;

        print("1. Si")
        print("2. Salir")

        try:
            i = int(input()) - 1
            print("")
        except:
            print("Ingrese una opcion valida")
            menu(param_productos_nombres_precios)

def leer_productos(param_productos_nombres_precios):
    os.system("cls")
    opcion = int(input("Desea leer todos los productos o uno en especifico?1\n1. Todos\n2. Uno en especifico\n"))
    
    if(opcion == 1):
        os.system("cls")
        print("Todos los productos son: \n")
        print(param_productos_nombres_precios)
        os.system("pause")
    elif(opcion == 2):
        os.system("cls")
        key = input("Ingrese el nombre del producto del cual desea ver el precio: ")
        if(param_productos_nombres_precios is not NULL):
            try:
                os.system("cls")
                print("El producto que busca es: ")
                print(key, ': ', param_productos_nombres_precios[key])
                os.system("pause")
            except:
                print("El elemento llamado \'" + key + "\' no existe")
                os.system("pause")
                menu(param_productos_nombres_precios)
            
    else:
        print("Seleccione una opcion valida")
        os.system("pause")
    

def eliminar_productos(param_productos_nombres_precios):
    os.system("cls")
    key_delete = input("Ingrese el nombre del producto que desea eliminar: ")
    
    try:
        del param_productos_nombres_precios[key_delete]
        print("El producto \'", key_delete, "\' ha sido eliminado con exito")
        os.system("pause")
    except:
        print("El producto \'", key_delete, "\' no existe")
        os.system("pause")
    

def menu(param_productos_nombres_precios):
    
    
    opcion = 1
    while(opcion > 0 and opcion < 4):
        os.system("cls")
        print("Bienvenido al software de colecciones de datos (Diccionarios)".center(90))
        print("Que desea hacer?: ")
        print("1. Agregar datos al diccionario")
        print("2. Leer datos")
        print("3. Eliminar productos")
        print("4. Salir")
        opcion = int(input())

        if(opcion == 1):
            agregar_productos(param_productos_nombres_precios)
        elif(opcion == 2):
            leer_productos(param_productos_nombres_precios)
        elif(opcion == 3):
            eliminar_productos(param_productos_nombres_precios)
        else:  
            ("Ingrese una opcion valida")
            os.system("pause")


def main(param_productos_nombres_precios):
    
    menu(param_productos_nombres_precios)

main(productos_nombres_precios)