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
        productos_nombres_precios[nombre_producto] = precio_producto;

        print("1. Si")
        print("2. Salir")

        try:
            i = int(input()) - 1
        except:
            print("Ingrese una opcion valida")
            i = 0



def main():
    agregar_productos(productos_nombres_precios)

main()