class Mision: 
    
    def __init__(self, nombre, planeta, nave, armas, integrantes):
        self.nombre = nombre
        self.planeta = planeta
        self.nave = nave
        self.armas = armas
        self.integrantes = integrantes
        
    def print(self):
        print("--------------------")
        print(f"Nombre: {self.nombre}")
        print(f"Planeta: {self.planeta}")
        print(f"Nave: {self.nave}")

        x=0
        print("Armas")
        for armas in self.armas: 
            x+=1
            print(f"{x}- {armas}")
            
        print(f"Integrantes:")
        x=0
        for integrante in self.integrantes:
            x+=1
            print(f"{x}- {integrante}")
        print("--------------------")
    
    def mision_string(self):
        return f"{self.nombre}|{self.planeta}|{self.nave}|{','.join(self.armas)}| {','.join(self.integrantes)}"
    
    
