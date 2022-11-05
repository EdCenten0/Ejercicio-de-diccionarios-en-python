
productos_nombres_precios = {}




def agregar_productos(param_productos_nombres_precios):
    i = 0
    while(i == 0):
        nombre_producto = input("Ingrese el nombre del producto a agregar: ")
        precio_producto = int(input("Ingrese el precio del producto: "))
        print("Desea agregar otro producto?")
        productos_nombres_precios[nombre_producto] = precio_producto;

        print("1. Si")
        print("2. Salir")
        i = int(input()) - 1



def main():
    agregar_productos(productos_nombres_precios)

main()