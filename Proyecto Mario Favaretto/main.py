from api import get_peliculas, get_especies, get_planetas, get_personas, get_starships
from Pelicula import Pelicula
from Especie import Especie
from Planeta import Planeta
from Persona import Persona
from graphs import people_by_planet, starships_graphs
from estadisticas import stats
from csv_reader import read_naves, read_characters, read_weapons, read_planets
from misiones import menu_misiones


def search_personaje(personas_db):
    personaje_string = input("\nIngrese el nombre del personaje que desea buscar: ")
    for p in personas_db:
        if p.name == personaje_string or personaje_string in p.name:
            print("\nLista de personajes que coinciden:")
            Persona.print_persona(p)
            return p
    print("\nNo hubo coincidencias.")
    return None

def main(): 
    print("Empezando...")
    starships_bd = get_starships("https://www.swapi.tech/api/starships/")
    print("Naves listas")
    peliculas_bd = get_peliculas("https://www.swapi.tech/api/films/") #List[Pelicula]
    print("Peliculas listas")
    especies_bd = get_especies("https://www.swapi.tech/api/species/", peliculas_bd) 
    print("Especies listas")
    personas_bd = get_personas("https://www.swapi.tech/api/people/", especies_bd, starships_bd)
    print("Personas listas")
    planetas_bd = get_planetas("https://www.swapi.tech/api/planets/", personas_bd, peliculas_bd)
    print("Planetas listos")
    
    print("Disculpa la tardanza...")
    print("Ya casi...")
    bd_planets_csv = read_planets("planets.csv")
    bd_starships_csv = read_naves("starships.csv")
    bd_weapons_csv = read_weapons("weapons.csv")
    bd_characters_csv = read_characters("characters.csv")
    
    misiones_bd = []
    
    while True: 
        
        print("""
            Menú de opciones:
                A. Lista de películas de la saga
                B. Lista de las especies de la saga
                C. Lista de planetas
                D. Buscar personaje
                E. Gráfico de cantidad de personajes nacidos en cada planeta
                F. Gráficos sobre características de naves
                G. Estadísticas sobre naves
                H. Misiones
              """)
   
        option = input("Ingrese su opción (A-H): ")
        
        if option.upper() == "A":
            print("\nLista de películas de la saga")
            x = 0
            for p in peliculas_bd:
                x+=1
                print(x)
                Pelicula.print(p)
            
        elif option.upper() == "B":
            print("\nLista de las especies de la saga")
            x = 0
            for e in especies_bd:
                x+=1
                print(x)
                Especie.print(e)
                
        elif option.upper() == "C":
            print("\nLista de planetas")
            for p in planetas_bd:
                Planeta.print(p)
            
        elif option.upper() == "D":
            print("\nBuscar personaje")
            search_personaje(personas_bd)
            
        elif option.upper() == "E":
            print("\nGráfico de cantidad de personajes nacidos en cada planeta")
            people_by_planet(bd_characters_csv)
            
        elif option.upper() == "F":
           starships_graphs(bd_starships_csv)
            
        elif option.upper() == "G":
            print("\nEstadísticas sobre naves")
            stats(bd_starships_csv)
            
            
        elif option.upper() == "H":
            
            print("Misiones")
            misiones_bd = menu_misiones(misiones_bd, bd_planets_csv, bd_starships_csv, bd_weapons_csv, bd_characters_csv)
            
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

        
        
main()