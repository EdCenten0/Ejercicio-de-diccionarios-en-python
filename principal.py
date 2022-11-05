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
            i = 0


def menu(param_productos_nombres_precios):
    os.system("cls")
    print("Bienvenido al software de colecciones de datos (Diccionarios)".center(90))
    opcion = 1
    while(opcion > 0 and opcion < 4):
        print("Que desea hacer?: ")
        print("1. Agregar datos al diccionario")
        print("4. Salir")
        opcion = int(input())

        if(opcion == 1):
            agregar_productos(param_productos_nombres_precios)
        else:  
            ("Ingrese una opcion valida")
            os.system("pause")


def main(param_productos_nombres_precios):
    
    menu(param_productos_nombres_precios)

main(productos_nombres_precios)