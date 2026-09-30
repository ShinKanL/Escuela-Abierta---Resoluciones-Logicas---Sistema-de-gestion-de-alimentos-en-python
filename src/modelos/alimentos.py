
class alimentos: 
    def __init__(self,nombre,cantidad,unidad,fecha_vencimiento):
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidad = unidad
        self.fecha_vencimiento = fecha_vencimiento
        
    def __str__(self):
        return f"{self.nombre} - {self.cantidad} - {self.unidad} - Vence: {self.fecha_vencimiento}"