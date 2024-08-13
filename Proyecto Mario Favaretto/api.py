import requests 
from Pelicula import Pelicula
from Especie import Especie
from Planeta import Planeta
from Persona import Persona 
from Nave import Nave

def get_peliculas(url):

    peliculas_bd = []

    peliculasAPI = requests.get(url)
    peliculas = peliculasAPI.json()["result"]

    people_urls = []

    for pelicula in peliculas: 
        planetas = []
        p = pelicula["properties"]
        for url in p["planets"]:
            planetas.append(requests.get(url).json()["result"]["properties"]["name"])
        
        new = Pelicula(p["title"],
                p["episode_id"],
                p["release_date"],
                p["opening_crawl"],
                p["director"],
                planetas,
                p["characters"]
            )
        peliculas_bd.append(new)

    return peliculas_bd
          
def get_especies(url, peliculas_bd):

    especies_bd = []

    especiesAPI = requests.get(url)
    
    especies = especiesAPI.json()["results"]

    for especie in especies: 
        
        e = requests.get(especie["url"]).json()["result"]["properties"]
        
        origen_url = e["homeworld"]
        origenAPI = requests.get(origen_url)
        origen_json = origenAPI.json()["result"]
        origen = origen_json["properties"]["name"]
        
        people = []
        for person_url in e["people"]:
            personAPI = requests.get(person_url)
            person = personAPI.json()["result"]
            people.append(person["properties"]["name"])
        
        peliculas = []
        for p_url in e["people"]:
            for peli in peliculas_bd:    
                if p_url in peli.people_urls:
                    peliculas.append(peli.titulo)
        
        new = Especie(
                e["name"],
                e["average_height"],
                e["classification"],
                origen,
                e["language"],
                people, 
                peliculas
                )
        especies_bd.append(new)

    return especies_bd     
    
def get_planetas(url, personas_bd, peliculas_bd):
    
    planetasAPI = requests.get(url)
    planetas = planetasAPI.json()["results"]
    

    planetas_db = []
    
    for planet in planetas:
        planetAPI = requests.get(planet["url"]).json()["result"]["properties"]
        personajes = []
        episodios = []
        for p in personas_bd:
            if p.origen == planetAPI["name"]:
                personajes.append(p.name)
        for p in peliculas_bd:
            if planetAPI["name"] in p.planetas:
                episodios.append(p.titulo)
            
        
        new = Planeta(
            planetAPI["name"],
            planetAPI["orbital_period"],
            planetAPI["rotation_period"],
            planetAPI["population"],
            planetAPI["climate"],
            episodios,
            personajes
        )
        
        planetas_db.append(new)
    return planetas_db

def search_especie(especies_bd, nombre, origen):
    
    for e in especies_bd:
        if nombre in  e.personajes:
            return e
    
    for e in especies_bd:
        if origen == e.origen:
            return e
        
    for e in especies_bd:
        if e.nombre == "Human": 
            return e

def get_personas(url, especies_bd, starships_bd):
    
    peopleAPI = requests.get(url)
    
    personas = peopleAPI.json()["results"] 
    
    personas_bd = []
    
    for p in personas:
        persona = requests.get(p["url"]).json()["result"]["properties"]
        
        nombre = persona["name"]
        genero = persona["gender"]
        episodios = []
        naves = []
        for n in starships_bd:    
            if nombre in n.pilots:
                naves.append(n.nombre)
        origenAPI = requests.get(persona["homeworld"])
        origen_json = origenAPI.json()["result"]
        origen = origen_json["properties"]["name"]
        especie_obj = search_especie(especies_bd, nombre, origen)
        new = Persona(especie_obj,nombre, episodios, genero, naves)
        personas_bd.append(new)
    
    return personas_bd


def get_starships(url):
    starships_bd = []
    starshipsAPI = requests.get(url)
    starships = starshipsAPI.json()["results"]
    
        
    for s in starships:
        starship = requests.get(s["url"]).json()["result"]["properties"]
        pilots = []
        for url in starship["pilots"]:
            pilots.append(requests.get(url).json()["result"]["properties"]["name"])
        new = Nave(
            starship["name"],
            starship["starship_class"],
            starship["length"],
            starship["cargo_capacity"],
            starship["cost_in_credits"],
            starship["hyperdrive_rating"],
            starship["MGLT"],
            starship["max_atmosphering_speed"],
            pilots
        )
        starships_bd.append(new) 
    
    return starships_bd


