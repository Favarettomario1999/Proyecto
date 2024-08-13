class Planeta:
    
    def __init__(self, nombre, orbita, rotacion, habitantes, clima, episodios, personajes):
    
        self.nombre = nombre
        self.orbita = orbita
        self.rotacion = rotacion
        self.habitantes = habitantes
        self.clima = clima  
        self.episodios = episodios  
        self.personajes = personajes    
        
    def print(self):
        print("Nombre: ", self.nombre)
        print("Periodo de Orbita: ", self.orbita)
        print("Periodo de Rotación: ", self.rotacion)
        print("Habitantes: ", self.habitantes)
        print("Clima: ", self.clima)
        print("Episodios: ", len(self.episodios))
        for e in self.episodios: 
            print(f"- {e}")
        print(f"Personajes: {len(self.personajes)}")
        for personaje in self.personajes:
            print(f"- {personaje}")
        print("------------------------")


