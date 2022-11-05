from asyncio.windows_events import NULL
import os
productos_nombres_precios = {}






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

        print("Desea agregar otro producto?")
        param_productos_nombres_precios[nombre_producto] = precio_producto;

        print("1. Si")
        print("2. Salir")

        try:
            i = int(input()) - 1
        except:
            print("Ingrese una opcion valida")
            menu(param_productos_nombres_precios)

def leer_productos(param_productos_nombres_precios):

    opcion = int(input("Desea leer todos los productos o uno en especifico?1\n1. Todos\n2. Uno es especifico\n"))
    
    if(opcion == 1):
        print(param_productos_nombres_precios)
    elif(opcion == 2):
        key = input("Ingrese el nombre del producto del cual desea ver el precio: ")
        if(param_productos_nombres_precios is not NULL):
            try:
                print(key, ': ', param_productos_nombres_precios[key])
            except:
                print("El elemento no existe")
                os.system("pause")
                menu(param_productos_nombres_precios)
            
    else:
        print("Seleccione una opcion valida")
        os.system("pause")
    


def menu(param_productos_nombres_precios):
    os.system("cls")
    print("Bienvenido al software de colecciones de datos (Diccionarios)".center(90))
    opcion = 1
    while(opcion > 0 and opcion < 4):
        print("Que desea hacer?: ")
        print("1. Agregar datos al diccionario")
        print("2. Leer datos")
        print("4. Salir")
        opcion = int(input())

        if(opcion == 1):
            agregar_productos(param_productos_nombres_precios)
        elif(opcion == 2):
            leer_productos(param_productos_nombres_precios)
        else:  
            ("Ingrese una opcion valida")
            os.system("pause")


def main(param_productos_nombres_precios):
    
    menu(param_productos_nombres_precios)

main(productos_nombres_precios)