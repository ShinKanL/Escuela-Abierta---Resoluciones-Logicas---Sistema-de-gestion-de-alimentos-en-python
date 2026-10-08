
def menu():
    print("Bienvenido al menú principal.")
    print("Seleccione una opción:")
    print("1.Ver alimentos")
    print("2. Agregar alimento")
    print("3. Quitar alimento")
    print("")

    while True:
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            print("Has seleccionado la Opción 1.")
            # Aquí puedes agregar la lógica para la Opción 1
        elif opcion == "2":
            print("Has seleccionado la Opción 2.")
            # Aquí puedes agregar la lógica para la Opción 2
        elif opcion == "3":
            print("Saliendo del menú. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido (1, 2 o 3).")