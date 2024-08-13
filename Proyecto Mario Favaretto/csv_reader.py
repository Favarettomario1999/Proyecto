import csv
from Nave import Nave 
from Planeta import Planeta
from Arma import Arma
from Character import Character 

def read_naves(file_name):
    naves = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            nave = Nave(
                
                row[1], #nombre
                row[13], #clase
                row[5], #longitud
                row[9], #capacidad
                row[4], #costo
                row[11], #hyperdrive
                row[12], #MGLT
                row[6], #max_speed
                row[14]

            )
            naves.append(nave)
    return naves


def read_planets(file_name):
    planets = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            planeta = Planeta(
                row["name"],
                row["orbital_period"],
                row["rotation_period"],
                row["population"],
                row["climate"],
                row['films'].split(', ') if row['films'] else [],
                row['residents'].split(', ') if row['residents'] else [],
            )
            planets.append(planeta)
    return planets

def read_weapons(file_name):
    armas = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            arma = Arma(
                row["name"],
                row["model"],
                row["cost_in_credits"],
                row["length"],
                row["type"],
                row["description"],
                row['films'].split(', ') if row['films'] else [],
            )
            armas.append(arma)
    return armas

def read_characters(file_name):
    characters = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            character = Character(
                row["name"],
                row["species"],
                row["gender"],
                row["height"],
                row["weight"],
                row["hair_color"],
                row["eye_color"],
                row["skin_color"],
                row["year_born"],
                row["homeworld"],
                row["year_died"],
                row["description"],
            )
            characters.append(character)
    return characters

