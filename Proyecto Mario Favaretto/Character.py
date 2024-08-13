class Character:
    
    def __init__(self, name, species, gender, height, weight, hair_color, eye_color, skin_color, year_born, homeworld, year_died, description):
        self.name = name	
        self.species = species	
        self.gender = gender	
        self.height = height	
        self.weight = weight	
        self.hair_color = hair_color	
        self.eye_color = eye_color	
        self.skin_color = skin_color	
        self.year_born = year_born	
        self.homeworld = homeworld	
        self.year_died = year_died	
        self.description = description

    def print(self):
        print(f"Nombre: {self.name}")
        print(f"Especie: {self.species}")
        print(f"Género: {self.gender}")
        print(f"Altura: {self.height}")
        print(f"Peso: {self.weight}")
        print(f"Color de cabello: {self.hair_color}")
        print(f"Color de ojos: {self.eye_color}")
        print(f"Color de piel: {self.skin_color}")
        print(f"Año de nacimiento: {self.year_born}")
        print(f"Planeta de origen: {self.homeworld}")
        print(f"Año de fallecimiento: {self.year_died}")
        print(f"Descripción: {self.description}")
        print("------------------------------")
        
        
    
