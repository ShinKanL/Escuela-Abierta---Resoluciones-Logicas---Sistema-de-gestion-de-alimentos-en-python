import pandas as pd

def ver_productos():
    ruta = r'C:\Users\aquil\Desktop\mierda\Escuela-Abierta---Resoluciones-Logicas---Sistema-de-gestion-de-alimentos-en-python\python\datos-alimentos.csv'
    
    try:
        # skipinitialspace elimina los espacios después de las comas de tu CSV
        df = pd.read_csv(ruta, skipinitialspace=True)
        
        # Si el archivo está vacío, evitamos que rompa el programa con un mensaje amigable
        if df.empty:
            print("El inventario está vacío actualmente.")
        else:
            print("\n", df.to_string(index=False)) # Muestra los datos limpios sin el índice numérico de la izquierda
            print("-" * 50)
            
    except pd.errors.EmptyDataError:
        print("Error: El archivo CSV está completamente vacío. Por favor agrega productos.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta especificada.")
 
        
def agregar_producto(nombre_producto, cantidad, fecha_vencimiento):
    ruta = r'C:\Users\aquil\Desktop\mierda\Escuela-Abierta---Resoluciones-Logicas---Sistema-de-gestion-de-alimentos-en-python\python\datos-alimentos.csv'
    
    try:
        # Intentamos leer el archivo CSV existente
        df = pd.read_csv(ruta, skipinitialspace=True)
    except FileNotFoundError:
        # Si no existe, creamos un DataFrame vacío con las columnas necesarias
        df = pd.DataFrame(columns=['Alimento', 'Cantidad', 'Fecha de vencimiento'])
    
    # Agregamos el nuevo producto al DataFrame
    nuevo_producto = pd.DataFrame({
        'Alimento': [nombre_producto],
        'Cantidad': [cantidad],
        'Fecha de vencimiento': [fecha_vencimiento]
    })
    
    df = pd.concat([df, nuevo_producto], ignore_index=True)
    
    # Guardamos los cambios en el archivo CSV
    df.to_csv(ruta, index=False)
    print(f"Producto '{nombre_producto}' agregado exitosamente.")
    
def eliminar_producto(nombre_producto):
    ruta = r'C:\Users\aquil\Desktop\mierda\Escuela-Abierta---Resoluciones-Logicas---Sistema-de-gestion-de-alimentos-en-python\python\datos-alimentos.csv'
    
    try:
        df = pd.read_csv(ruta, skipinitialspace=True)
        
        # Verificar si el producto existe
        if nombre_producto in df['Alimento'].values:
            df = df[df['Alimento'] != nombre_producto]  # Eliminar el producto
            df.to_csv(ruta, index=False)  # Guardar los cambios en el CSV
            print(f"Producto '{nombre_producto}' eliminado exitosamente.")
        else:
            print(f"Producto '{nombre_producto}' no encontrado en el inventario.")
            
    except pd.errors.EmptyDataError:
        print("Error: El archivo CSV está completamente vacío. No hay productos para eliminar.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta especificada.")
