class Especie:
    
    def __init__(self, nombre, altura, clasificacion, origen, lengua, personajes, episodios):
        """
        Args:
            nombre (String) 
            altura (String) 
            clasificacion (String) 
            origen (String) 
            lengua (String) 
            personajes(List)
            episodios(List)
        """    
        self.nombre = nombre
        self.altura = altura
        self.clasificacion = clasificacion
        self.origen = origen
        self.lengua = lengua
        self.personajes = personajes
        self.episodios = episodios
        
    def print(self):
        print(f"Nombre: {self.nombre}")
        print(f"Altura: {self.altura}")
        print(f"Clasificacion: {self.clasificacion}")
        print(f"Origen: {self.origen}")
        print(f"Lengua: {self.lengua}")
        print("Personajes:")
        for personaje in self.personajes:
            print(f"- {personaje}")
        print("Episodios:")
        for episodio in self.episodios:
            print(f"- {episodio}")
        print("--------------------")