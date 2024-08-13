import csv
import matplotlib.pyplot as plt

def people_by_planet(characters):
    
    planetas_nombres = []
    cantidad = []
    for c in characters:
        if c.homeworld not in planetas_nombres:
            planetas_nombres.append(c.homeworld)
            cantidad.append(1)
        else: 
            index = planetas_nombres.index(c.homeworld)
            cantidad[index] += 1
    

    x = planetas_nombres
    y = cantidad
    
    plt.figure(figsize=(18,8))
    plt.bar(x, y, color = 'lightblue', width = 0.5) 
    plt.xticks(rotation = 50) 
    plt.xlabel('Planetas') 
    plt.ylabel('Personajes') 
    plt.title('Planetas segun cantidad de personajes', fontsize = 15) 
    for i in range(len(x)):
        plt.text(i, y[i]//2,y[i], ha = 'center') 
    plt.tight_layout()
    plt.show() 
        
        
def starships_graphs(bd_starships_csv):
    x = []
    y = []
    plt.figure(figsize=(12,8))
    while True: 
        print("""
                Posibles graficas de naves:
                    A. Longitud de la nave
                    B. Capacidad de la carga
                    C. Clasificacion de hiperimpulsor
                    D. MGLT (Modern Galactic Light Time)
                    E. Salir
                    """)
        choice = input("\nIngrese la opcion de la grafica que desea ver:  ")
        
        if choice.upper() == "A":

            for s in bd_starships_csv:
                x.append(s.nombre)
                y.append(float(s.longitud.replace(",","")))
            
            plt.xlabel('Naves', fontsize = 8) 
            plt.ylabel('Longitud') 
            plt.title('Naves segun longitudes', fontsize = 14) 
            break
               
        elif choice.upper() == "B":
            
            for s in bd_starships_csv:
                if s.capacidad != "":
                    x.append(s.nombre)
                    y.append(float(s.capacidad))
            
            plt.xlabel('Naves', fontsize = 8) 
            plt.ylabel('Capacidad') 
            plt.title('Naves segun capacidades', fontsize = 14) 
            break
            
        elif choice.upper() == "C":

            for s in bd_starships_csv:
                if s.hyperdrive != "":
                    x.append(s.nombre)
                    y.append(float(s.hyperdrive))
                
            
            plt.xlabel('Naves', fontsize = 8) 
            plt.ylabel('Hyperdrive') 
            plt.title('Naves segun hyperdrive', fontsize = 14) 
            break
                 
        elif choice.upper() == "D":

            for s in bd_starships_csv:
                if s.MGLT != "":
                    x.append(s.nombre)
                    y.append(float(s.MGLT))
            
            plt.xlabel('Naves', fontsize = 8) 
            plt.ylabel('MGLT') 
            plt.title('Naves segun MGLT', fontsize = 14) 
            break
            
        elif choice.upper() == "E":
            pass
            break    
        
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
    
    plt.bar(x, y, color = 'lightblue', width=0.4)
    plt.xticks(rotation = 90) 
    plt.tight_layout()
    plt.show() 