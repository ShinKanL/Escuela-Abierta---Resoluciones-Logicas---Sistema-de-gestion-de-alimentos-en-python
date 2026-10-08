from donador import verDonacionEnCSV
from donador import Donar


def menuDonador():

    while True:

        print("\n--- MENÚ DONADOR ---")
        print("1. Ver donaciones realizadas")
        print("2. Donar alimentos")
        print("0. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            print("\nHas seleccionado la Opción 1.")
            verDonacionEnCSV()

        elif opcion == "2":
            print("\nHas seleccionado la Opción 2.")
            Donar()

        elif opcion == "0":
            print("Saliendo del menú. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, ingrese un número válido.")