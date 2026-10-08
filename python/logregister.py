import pandas as pd
import time as t
import requests

from menuDonador import menuDonador
from menuEncargado import menuEncargado

def obtener_ubicacion(direccion):
    """
    Convierte una dirección en latitud y longitud
    utilizando Nominatim (OpenStreetMap).
    """

    url = "https://nominatim.openstreetmap.org/search"

    parametros = {
        "q": direccion,
        "format": "json",
        "limit": 1,
        "countrycodes": "ar"
    }

    encabezados = {
        "User-Agent": "SistemaGestionAlimentos/1.0"
    }

    try:
        respuesta = requests.get(
            url,
            params=parametros,
            headers=encabezados,
            timeout=10
        )

        respuesta.raise_for_status()

        resultados = respuesta.json()

        if resultados:
            latitud = float(resultados[0]["lat"])
            longitud = float(resultados[0]["lon"])

            return latitud, longitud

        return None, None

    except requests.RequestException:
        print("No se pudo verificar la dirección.")
        return None, None


def registrarse():

    ruta = r"C:\Users\aquil\Desktop\mierda\Escuela-Abierta---Resoluciones-Logicas---Sistema-de-gestion-de-alimentos-en-python\python\usuarios.csv"

    print("---REGISTRO DE USUARIO---")

    print("Ingrese su nombre de usuario:")
    nombre_usuario = input()

    print("Ingrese su correo electrónico (example@gmail.com):")
    correo = input()

    while True:

        if not correo.endswith("@gmail.com") or correo.startswith("@gmail.com"):

            print(
                "El correo electrónico debe ser de Gmail. "
                "Por favor, ingrese un correo válido:"
            )

            correo = input()

        else:
            break

    print("Ingrese su contraseña (mínimo 8 caracteres):")
    contraseña = input()

    while True:

        if len(contraseña) < 8:

            print(
                "La contraseña debe tener al menos 8 caracteres. "
                "Por favor, ingrese una contraseña válida:"
            )

            contraseña = input()

        else:
            break

    print("Ingrese su DNI:")
    dni = input()

    while True:

        if not dni.isdigit() or len(dni) != 8:

            print(
                "El DNI debe contener exactamente 8 números. "
                "Por favor, ingrese un DNI válido:"
            )

            dni = input()

        else:
            break

    print("Usted es donador o encargado de alimentos?")
    print("Ingrese 'donador' o 'encargado':")

    tipo_usuario = input()

    while True:

        if tipo_usuario.lower() not in ["donador", "encargado"]:

            print(
                "Opción inválida. "
                "Por favor, ingrese 'donador' o 'encargado':"
            )

            tipo_usuario = input()

        else:
            break

    # Valores por defecto
    direccion = ""
    latitud = ""
    longitud = ""

    # -----------------------------------------
    # UBICACIÓN DEL DONADOR
    # -----------------------------------------

    if tipo_usuario.lower() == "donador":

        while True:

            print()
            print("Coloque la dirección de donde trabaja o dona alimentos:")
            direccion = input()

            print()
            print("Verificando dirección...")

            latitud, longitud = obtener_ubicacion(direccion)

            if latitud is not None:

                print()
                print("✓ Dirección encontrada correctamente.")
                print(f"Latitud: {latitud}")
                print(f"Longitud: {longitud}")
                print()

                break

            else:

                print()
                print("✗ No se encontró esa dirección.")
                print("Intente escribirla nuevamente.")
                print()
                
    else:
        if tipo_usuario.lower() == "encargado":
            print("---BIENVENIDO AL REGISTRO DE ENCARGADO---")
            ruta3 = r"C:\Users\aquil\Desktop\mierda\Escuela-Abierta---Resoluciones-Logicas---Sistema-de-gestion-de-alimentos-en-python\python\comedores_mendoza.csv"
            try:
                df_comedores = pd.read_csv(ruta3)
                while True:
                    print("Ingrese el ID o nombre del comedor/merendero que administra:")
                    busqueda = input().strip()

                    if busqueda.isdigit():
                        comedor_encontrado = df_comedores[df_comedores['Identificador'] == int(busqueda)]
                    else:
                        comedor_encontrado = df_comedores[df_comedores['Nombre'].astype(str).str.contains(busqueda, case=False, na=False)]

                    if not comedor_encontrado.empty:
                        comedor = comedor_encontrado.iloc[0]
                        id_comedor = str(comedor['Identificador'])
                        nombre_comedor = comedor['Nombre']
                        
                        calle = str(comedor['Calle']) if pd.notna(comedor['Calle']) else ''
                        altura = str(comedor['Altura']) if pd.notna(comedor['Altura']) else ''
                        localidad = str(comedor['Localidad']) if pd.notna(comedor['Localidad']) else ''
                        
                        direccion = f"{calle} {altura}, {localidad}".strip()
                        latitud = comedor['Latitud']
                        longitud = comedor['Longitud']

                        print()
                        print(f"✓ Comedor verificado: {nombre_comedor} (ID: {id_comedor})")
                        print(f"  Dirección: {direccion}")
                        print(f"  Latitud: {latitud}, Longitud: {longitud}")
                        print()
                        break
                    else:
                        print()
                        print("✗ No se encontró ningún comedor con ese ID o nombre en Mendoza.")
                        print("Por favor, verifique los datos e intente nuevamente.")
                        print()

            except FileNotFoundError:
                print("Advertencia: No se encontró 'comedores_mendoza.csv'.")
                print("Ingrese la dirección del comedor/merendero:")
                direccion = input()
                latitud, longitud = obtener_ubicacion(direccion)

    print("Usuario registrado con éxito.")

    # -----------------------------------------
    # CREAR DATOS DEL USUARIO
    # -----------------------------------------

    nuevo_df = pd.DataFrame([{

        "NombreDeUsuario": nombre_usuario,
        "Correo": correo,
        "Contraseña": contraseña,
        "DNI": dni,
        "TipoUsuario": tipo_usuario.lower(),
        "Direccion": direccion,
        "Latitud": latitud,
        "Longitud": longitud

    }])

    # -----------------------------------------
    # GUARDAR EN CSV
    # -----------------------------------------

    try:

        df = pd.read_csv(ruta, dtype={"DNI": str})

        df = pd.concat(
            [df, nuevo_df],
            ignore_index=True
        )

        df.to_csv(
            ruta,
            index=False
        )

        print()
        print("GUARDANDO EN:")
        print(ruta)
        print()
        print("ARCHIVO GUARDADO")
        print("Usuario agregado correctamente.")

    except FileNotFoundError:

        nuevo_df.to_csv(
            ruta,
            index=False
        )

        print()
        print("Archivo creado y usuario agregado correctamente.")

    t.sleep(2)




def iniciar_sesion():

    ruta = r"C:\Users\aquil\Desktop\mierda\Escuela-Abierta---Resoluciones-Logicas---Sistema-de-gestion-de-alimentos-en-python\python\usuarios.csv"

    try:

        df_usuarios = pd.read_csv(
            ruta,
            dtype={"DNI": str}
        )

    except FileNotFoundError:

        print("No existe el archivo de usuarios.")
        return False

    usuario_ingresado = input("Ingresa tu usuario: ")
    correo_ingresado = input("Ingresa tu correo electrónico: ")
    password_ingresada = input("Ingresa tu contraseña: ")
    dni_ingresado = input("Ingresa tu DNI: ")

    coincidencia = df_usuarios[
        (df_usuarios["NombreDeUsuario"].astype(str) == usuario_ingresado) &
        (df_usuarios["Correo"].astype(str) == correo_ingresado) &
        (df_usuarios["Contraseña"].astype(str) == password_ingresada) &
        (df_usuarios["DNI"].astype(str) == dni_ingresado)
    ]

    if not coincidencia.empty:

        print("¡Inicio de sesión exitoso!")
        menuDonador()
        return True


    else:

        print(
            "Error: El usuario no existe "
            "o los datos ingresados no coinciden."
        )
        return False