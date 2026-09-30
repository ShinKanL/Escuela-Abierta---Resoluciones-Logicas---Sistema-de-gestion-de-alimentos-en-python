def iniciar_menu():

    while True:
        print("\n===== GESTOR DE ALIMENTOS =====")
        print("1. Agregar alimento")
        print("2. Ver alimentos")
        print("3. Buscar alimento")
        print("4. Eliminar alimento")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Agregar alimento")

        elif opcion == "2":
            print("Ver alimentos")

        elif opcion == "3":
            print("Buscar alimento")

        elif opcion == "4":
            print("Eliminar alimento")

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")