import pandas as pd
import time as t
from menu import menu 
def registrarse():
    ruta = r"C:\Users\aquil\Desktop\mierda\Escuela-Abierta---Resoluciones-Logicas---Sistema-de-gestion-de-alimentos-en-python\python\usuarios.csv"
    print("---REGISTRO DE USUARIO---")
    print("Ingrese su nombre de usuario:")
    nombre_usuario = input()
    print("Ingrese su correo electrónico (example@gmail.com):")
    correo = input()
    while True:
        if not correo.endswith("@gmail.com") or correo.startswith("@gmail.com"):
            print("El correo electrónico debe ser de Gmail. Por favor, ingrese un correo válido:")
            correo = input()
        else:
            break
    print("Ingrese su contraseña(minimo 8 caracteres):")
    contraseña = input()
    while True:
        if len(contraseña) < 8:
            print("La contraseña debe tener al menos 8 caracteres. Por favor, ingrese una contraseña válida:")
            contraseña = input()
        else:
            break
    print("Ingrese su DNI:")
    dni = input()
    while True:
            if not dni.isdigit() or len(dni) != 8:
                print("El DNI debe contener exactamente 8 numeros. Por favor, ingrese un DNI válido:")
                dni = input()
            else:
                break
    print("Usted es donador o encargado de alimentos? (Ingrese 'donador' o 'encargado'):")
    tipo_usuario = input()
    while True:
        if tipo_usuario.lower() not in ['donador', 'encargado']:
            print("Opción inválida. Por favor, ingrese 'donador' o 'encargado':")
            tipo_usuario = input()
        else:
            break
        
    if tipo_usuario.lower() == 'donador':
        print("Coloque la direccion de donde trabaja o dona alimentos():")
        direccion = input()
    print("Usuario registrado con éxito.")




    
    
    nuevo_df = pd.DataFrame([{
        'NombreDeUsuario': nombre_usuario,
        'Correo': correo,
        'Contraseña': contraseña,
        'DNI': dni
    }])

    try:
        df = pd.read_csv(ruta)

        df = pd.concat([df, nuevo_df], ignore_index=True)
        print("GUARDANDO EN:")
        print(ruta)
        nuevo_df.to_csv(ruta, mode='a', header=False, index=False)
        print("ARCHIVO GUARDADO")
        df.to_csv(ruta, index=False)
        print("Usuario agregado correctamente.")

    except FileNotFoundError:
        # Si el archivo no existe, lo crea con los encabezados
        nuevo_df.to_csv(ruta, index=False)
        print("Archivo creado y usuario agregado correctamente.")

    t.sleep(2)
    main()
    

def iniciar_sesion():
    ruta = "C:\\Users\\aquil\\Desktop\\mierda\\Escuela-Abierta---Resoluciones-Logicas---Sistema-de-gestion-de-alimentos-en-python\\python\\usuarios.csv"

    df_usuarios = pd.read_csv(ruta, dtype={'DNI': str})


    usuario_ingresado = input("Ingresa tu usuario: ")
    correo_ingresado = input("Ingresa tu correo electrónico: ")
    password_ingresada = input("Ingresa tu contraseña: ")
    dni_ingresado = input("Ingresa tu DNI: ")

    # 3. Buscar si coinciden TODOS los campos en una sola fila
    coincidencia = df_usuarios[
        (df_usuarios['NombreDeUsuario'].astype(str) == usuario_ingresado) &
        (df_usuarios['Correo'].astype(str) == correo_ingresado) &
        (df_usuarios['Contraseña'].astype(str) == password_ingresada) &
        (df_usuarios['DNI'].astype(str) == dni_ingresado)
    ]

    # 4. Validar el resultado
    if not coincidencia.empty:
        print("¡Inicio de sesión exitoso! Todos los datos son correctos.")
    else:
        print("Error: El usuario no existe o los datos ingresados no coinciden.")
        
    if iniciar_sesion() == True:
        menu()


