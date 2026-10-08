import pandas as pd
import time as t
from logregister import registrarse
from logregister import iniciar_sesion


def main():
    ruta = "C:\\Users\\aquil\\Desktop\\mierda\\Escuela-Abierta---Resoluciones-Logicas---Sistema-de-gestion-de-alimentos-en-python\\python\\usuarios.csv"
    lecturaCSV = pd.read_csv(ruta)
    print(lecturaCSV)
    
    print("---Bienvenido al sistema de gestión de alimentos---")
    print("Seleccione una opción:")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("0. Salir")
    opcion = input("Ingrese su opción: ")
    if opcion == "1":
        registrarse()
    elif opcion == "2":
        iniciar_sesion()
    elif opcion == "0":
        print("Saliendo del sistema...")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        
    

if __name__ == "__main__":
    main()