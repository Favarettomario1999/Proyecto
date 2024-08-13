from Especie import Especie

class Persona(Especie): 
    
    def __init__(self, especie, name, episodios, genero, naves):
        super().__init__(**especie.__dict__)
        self.name = name
        self.episodios = episodios
        self.genero = genero
        self.naves = naves
        
    def print_persona(self):
        print(f"Nombre: {self.name}")
        print(f"Origen: {self.origen}")
        print("Episodios:")
        for episodio in self.episodios:
            print(f"- {episodio}")
        print(f"Genero: {self.genero}")
        print(f"Especie: {self.nombre}")
        print(f"Naves: {len(self.naves)}")
        for nave in self.naves:
            print(f"- {nave}")


