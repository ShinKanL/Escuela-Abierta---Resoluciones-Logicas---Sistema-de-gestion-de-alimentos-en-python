import pandas as pd
import time as t


def verDonacionEnCSV():
    ruta = r"C:\Users\aquil\Desktop\mierda\Escuela-Abierta---Resoluciones-Logicas---Sistema-de-gestion-de-alimentos-en-python\python\donaciones.csv"

    df = pd.read_csv(ruta)
    print(df)
    t.sleep(2)
        
def Donar():
    ruta = r"C:\Users\aquil\Desktop\mierda\Escuela-Abierta---Resoluciones-Logicas---Sistema-de-gestion-de-alimentos-en-python\python\donaciones.csv"

    alimento = input("Ingrese el nombre del alimento: ")
    tipo_de_alimento = input("Ingrese el tipo de alimento(Bebida o comida): ")
    while tipo_de_alimento.lower() not in ["bebida", "comida"]:
        print("Tipo de alimento inválido. Por favor, ingrese 'Bebida' o 'Comida'.")
        tipo_de_alimento = input("Ingrese el tipo de alimento(Bebida o comida): ")
    
    cantidad = input("Ingrese la cantidad: ")
    while not cantidad.isdigit():
        print("Cantidad inválida. Por favor, ingrese un número válido.")
        cantidad = input("Ingrese la cantidad: ")
    
    fecha_de_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
    while True:
        try:
            pd.to_datetime(fecha_de_vencimiento, format='%Y-%m-%d')
            break
        except ValueError:
            print("Fecha de vencimiento inválida. Por favor, ingrese una fecha en el formato YYYY-MM-DD.")
            fecha_de_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
    
    donador = input("Ingrese su DNI: ")
    while not donador.isdigit():
        print("DNI inválido. Por favor, ingrese un número válido.")
        donador = input("Ingrese su DNI: ")

    ruta2 = r"C:\Users\aquil\Desktop\mierda\Escuela-Abierta---Resoluciones-Logicas---Sistema-de-gestion-de-alimentos-en-python\python\usuarios.csv"
    df_usuarios = pd.read_csv(ruta2)
    
    if not df_usuarios[df_usuarios['DNI'] == int(donador)].empty:
        print("DNI válido. Procediendo con la donación.")
    else:
        print("DNI no encontrado en el sistema.")
        return
    
    
    nuevo_dato = {
        "Alimento": alimento,
        "TipoDeAlimento": tipo_de_alimento,
        "Cantidad": cantidad,
        "FechaDeVencimiento": fecha_de_vencimiento,
        "Donador": donador
    }

    try:
        df = pd.read_csv(ruta)
        df = pd.concat([df, pd.DataFrame([nuevo_dato])], ignore_index=True)
        df.to_csv(ruta, index=False)
        print("Donación registrada correctamente.")
    except FileNotFoundError:
        pd.DataFrame([nuevo_dato]).to_csv(ruta, index=False)
        print("Archivo creado y donación registrada correctamente.")
        t.sleep(2)
   
    