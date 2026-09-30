class GestorAlimentos:
    
    def __init__(self):
        self.alimentos = []
        
    def agregar(self, alimento):
        self.alimentos.append(alimento)
        
    def listar(self):
        for alimento in self.alimentos:
            print(alimento)