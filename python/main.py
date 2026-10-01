import time
import pandas as pd
import sys as sys
from defs import ver_productos
from defs import eliminar_producto
from defs import agregar_producto

def main():

        print("---------------SISTEMA DE GESTIÓN DE INVENTARIO---------------")
        print("1. Ver Alimentos disponibles")
        print("2. Agregar un alimento")
        print("3. Eliminar un alimento")
        print("0. Salir")

        BotonSeleccionado = input("Seleccione una opción: ")
        
        if BotonSeleccionado == "1":
            print("Productos disponibles:")
            ver_productos()
        elif BotonSeleccionado == "2":
            print("Agregar un alimento:")
            agregar_producto(input("Ingrese el nombre del producto: "), 
                             input("Ingrese la cantidad: "), 
                             input("Ingrese la fecha de vencimiento (YYYY-MM-DD): "))
            
        elif BotonSeleccionado == "3":
            print("Eliminar un producto:")
            eliminar_producto(input("Ingrese el nombre del producto a eliminar: "))
        elif BotonSeleccionado == "0":
            print("Saliendo del sistema...")
            sys.exit()
        else:
            print("Opción no válida. Vuelve a intentarlo.")
            time.sleep(2)
            main()
            
        
        
if __name__ == "__main__":
    main()