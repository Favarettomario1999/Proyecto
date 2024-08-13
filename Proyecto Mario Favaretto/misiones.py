from Mision import Mision
from csv_reader import read_naves, read_characters, read_weapons, read_planets

def menu_misiones(misiones_bd, bd_planets_csv, bd_starships_csv, bd_weapons_csv, bd_characters_csv):
    """
    Menú principal para gestionar misiones.
    """
    while True:
        print("\nMenú de Misiones")
        print("1. Crear misión")
        print("2. Modificar misión")
        print("3. Ver misión")
        print("4. Guardar misiones (en TXT)")
        print("5. Cargar misiones")
        print("6. Salir")

        opcion = input("\nIngrese una opción: ")

        if opcion == "1":
            crear_mision(misiones_bd, bd_planets_csv, bd_starships_csv, bd_weapons_csv, bd_characters_csv)
            
        elif opcion == "2":
            modificar_mision(misiones_bd, bd_planets_csv, bd_starships_csv, bd_characters_csv)
            
        elif opcion == "3":
            ver_mision(misiones_bd)
            
        elif opcion == "4":
            guardar_mision(misiones_bd)
            
        elif opcion == "5":
            misiones_bd = cargar_mision()
            
        elif opcion == "6":
            print("Saliendo del menú...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
            
    return misiones_bd


def crear_mision(misiones_bd, bd_planets_csv, bd_starships_csv, bd_weapons_csv, bd_characters_csv):

    """
    Crea una nueva misión.
    """
    print("\nCrear Misión")

    nombre = input("\nIngrese el nombre de la misión: ")

    print("\nSeleccione un planeta:")
           
    for i, planeta in enumerate(bd_planets_csv):
        print(f"{i+1}. {planeta.nombre}")
    planeta_id = int(input("\nIngrese el número del planeta: ")) - 1
    planeta_seleccionado = bd_planets_csv[planeta_id].nombre

    print("\nSeleccione una nave:")
    for i, nave in enumerate(bd_starships_csv):
        print(f"{i+1}. {nave.nombre}")
    nave_id = int(input("\nIngrese el número de la nave: ")) - 1
    nave_seleccionada = bd_starships_csv[nave_id].nombre

    integrantes = []
    print("\nIntegrantes: ")
    for j, ch in enumerate(bd_characters_csv):
        print(f"{j+1}. {ch.name}")
    while len(integrantes)<7:
        integrante_id = input("\nIngrese el número del integrante (o pulse Enter para finalizar): ")
        if integrante_id == "":
            break
        integrante_id = int(integrante_id) - 1
        integrante = bd_characters_csv[integrante_id].name
        
        if integrante not in integrantes:
            integrantes.append(integrante)
            print(f"{integrante} agregado")
        else: 
            print("\nYa estaba incluido")
    if len(integrantes)==7:print("\nMaximo de integrantes")
        

    armas = []
    print("\nArmas: ")
    for j, arma in enumerate(bd_weapons_csv):
            print(f"{j+1}. {arma.name}")
    while len(armas)<7:
        arma_id = input("\nIngrese el número del arma a agregar (o pulse Enter para finalizar): ")
        if arma_id == "":
            break
        arma_id = int(arma_id) - 1
        arma = bd_weapons_csv[arma_id].name
        
        if arma not in armas:
            armas.append(arma)
            print(f"{arma} agregada")
        else: 
            print("\nYa estaba incluido")
    if len(armas)==7:print("\nMaximo de armas")
        
    new = Mision(
        nombre,
        planeta_seleccionado,
        nave_seleccionada,
        armas,
        integrantes)

   
    misiones_bd.append(new)

    print("Misión creada con éxito!")
    pass


def guardar_mision(misiones_bd):
    with open("misiones.txt", "w") as f:
        for mision in misiones_bd:
            f.write(Mision.mision_string(mision))
            f.write("\n")
            
    print("Base de datos guardada con exito.")

def ver_mision(misiones_bd):
    if len(misiones_bd) == 0: 
        print("\tAun no hay misiones guardadas. ")
        return
    mision_seleccionada = search_mision(misiones_bd)
    Mision.print(mision_seleccionada)

def search_mision(misiones_bd):
    print("\nSeleccione una misión:")
    for i, mision in enumerate(misiones_bd):
        print(f"{i+1}. {mision.nombre}")

    mision_id = int(input("\nIngrese el número de la misión: ")) - 1
    mision_seleccionada = misiones_bd[mision_id]
    return mision_seleccionada
       
def modificar_mision(misiones_bd, bd_planets_csv, bd_starships_csv, bd_characters_csv):
    """
    Modifica una misión existente.
    """
    if len(misiones_bd) == 0: 
        print("\tAun no hay misiones guardadas. ")
        return
    print("\nMision a modificar: ")
    mision_seleccionada = search_mision(misiones_bd)
    Mision.print(mision_seleccionada)
    print("\nModificar atributos de la misión:")
    print("1. Nombre de la misión")
    print("2. Planeta")
    print("3. Nave")
    print("4. Integrantes")
    print("5. Armas")

    opcion = input("\nIngrese una opción: ")

    if opcion == "1":
        nuevo_nombre = input("\nIngrese el nuevo nombre de la misión: ")
        mision_seleccionada.nombre = nuevo_nombre

    elif opcion == "2":
        print("\nSeleccione un planeta:")
        for i, planeta in enumerate(bd_planets_csv):
            print(f"{i+1}. {planeta['nombre']}")
        planeta_id = int(input("\nIngrese el número del planeta: ")) - 1
        mision_seleccionada.planeta = bd_planets_csv[planeta_id].nombre

    elif opcion == "3":
        print("\nSeleccione una nave:")
        for i, nave in enumerate(bd_starships_csv):
            print(f"{i+1}. {nave['nombre']}")
        nave_id = int(input("\nIngrese el número de la nave: ")) - 1
        mision_seleccionada.nave = bd_starships_csv[nave_id].nombre
        
    elif opcion == "4":
        while True:
            print("\nModificar integrantes")
            print("1. Eliminar integrante")
            print("2. Agregar integrante")

            opcion = int(input("\nIngrese una opción: "))
            
            if opcion == 1:
                integrante_id = input("\nIngrese el número del integrante a eliminar: ")
                integrante_id = int(integrante_id) - 1
                print(f"\nSe elimino exitosamente a {mision_seleccionada.integrantes[integrante_id]}")
                mision_seleccionada.integrantes.pop(integrante_id)
                break
                
            elif opcion == 2: 
                if len(mision_seleccionada.integrantes) == 7:
                    print("\nNo se pueden agregar más integrantes. Se han llegado al máximo de 7.")
                    break
                print("\nIntegrantes para agregar:")
                for i, c in enumerate(bd_characters_csv):
                    print(f"{i+1}. {c.name}")
                integrante_id = input("\nIngrese el número del integrante: ")
                integrante_id = int(integrante_id) - 1
                integrante = bd_characters_csv[integrante_id].name
                if integrante not in mision_seleccionada.integrantes:
                    mision_seleccionada.integrantes.append(integrante)
                    print("\nAgregado con exito.")
                else: 
                    print("\nYa estaba incluido")
                break

    elif opcion == "5":
        
        while True:
            print("\nModificar armas")
            print("1. Eliminar arma")
            print("2. Agregar arma")

            opcion = int(input("\nIngrese una opción: "))
            
            if opcion == 1:
                arma_id = input("\nIngrese el número del arma a eliminar: ")
                arma_id = int(arma_id) - 1
                print(f"\nSe elimino exitosamente {mision_seleccionada.armas[arma_id]}")
                mision_seleccionada.armas.pop(arma_id)
                break
                
            elif opcion == 2: 
                if len(mision_seleccionada.armas) == 7:
                    print("\nNo se pueden agregar más armas. Se han llegado al máximo de 7.")
                    break
                print("\nArmas para agregar:")
                for i, c in enumerate(bd_characters_csv):
                    print(f"{i+1}. {c.name}")
                arma_id = input("\nIngrese el número del arma: ")
                arma_id = int(arma_id) - 1
                arma = bd_characters_csv[arma_id].name
                if arma not in mision_seleccionada.armas:
                    mision_seleccionada.armas.append(arma)
                    print("\nAgregada con exito.")
                else: 
                    print("\nYa estaba incluida")
                break

    else:
        print("Opción inválida. No se realizaron cambios.")

    print("Misión modificada con éxito!")
   
def cargar_mision():

    misiones_bd = []
    with open("misiones.txt", "r") as f:
        for line in f:
            mision = line.split("|")
            nombre = mision[0]
            planeta = mision[1]
            nave = mision[2]
            armas = mision[3].split(",")
            integrantes = mision[0].split(",")
            new = Mision(
                nombre,
                planeta,
                nave,
                armas,
                integrantes
            )
            misiones_bd.append(new)
    
    print("\nMisiones cargadas exitosamente")
    return misiones_bd
  