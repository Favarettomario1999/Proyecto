class Pelicula:
    
    def __init__(self, titulo, num_episodio, fecha, opening, director, planetas, charaters_url_list):
    
        self.titulo = titulo  #String
        self.num_episodio = num_episodio #int
        self.fecha = fecha #String
        self.opening = opening #String
        self.director = director #String
        self.planetas = planetas #List[String]
        self.people_urls = charaters_url_list #List[String]
        
        
    def print(self):
        print(f"-  Título: {self.titulo}")
        print(f"-  Número de episodio: {self.num_episodio}")
        print(f"-  Fecha de estreno: {self.fecha}")
        print(f"-  Opening Crawl:")
        print(f"\t\t{self.opening}")
        print(f"-  Director: {self.director}")
        print("--------------------")
        

        