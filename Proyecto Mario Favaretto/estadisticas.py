import statistics

def stats(bd_starships_csv):

    hyperdrives = [float(ship.hyperdrive) for ship in bd_starships_csv if ship.hyperdrive != ""]
    costs = [float(ship.costo) for ship in bd_starships_csv if ship.costo != ""]
    mglt_values = [float(ship.MGLT) for ship in bd_starships_csv if ship.MGLT != ""]
    max_speeds = [float(ship.max_speed) for ship in bd_starships_csv if ship.max_speed != ""]


    hyperdrive_avg = statistics.mean(hyperdrives)
    hyperdrive_mode = statistics.mode(hyperdrives)
    hyperdrive_max = max(hyperdrives)
    hyperdrive_min = min(hyperdrives)

    cost_avg = statistics.mean(costs)
    cost_mode = statistics.mode(costs)
    cost_max = max(costs)
    cost_min = min(costs)

    mglt_avg = statistics.mean(mglt_values)
    mglt_mode = statistics.mode(mglt_values)
    mglt_max = max(mglt_values)
    mglt_min = min(mglt_values)

    max_speed_avg = statistics.mean(max_speeds)
    max_speed_mode = statistics.mode(max_speeds)
    max_speed_max = max(max_speeds)
    max_speed_min = min(max_speeds)

    print("Estadísticas:")
    print(f"\tHyperdrive: Promedio = {hyperdrive_avg:.2f}, Moda = {hyperdrive_mode}, Maximo = {hyperdrive_max}, Minimo = {hyperdrive_min}")
    print(f"\tCosto: Promedio = {cost_avg:.2f}, Moda = {cost_mode}, Maximo = {cost_max}, Minimo = {cost_min}")
    print(f"\tMGLT: Promedio = {mglt_avg:.2f}, Moda = {mglt_mode}, Maximo = {mglt_max}, Minimo = {mglt_min}")
    print(f"\tMaxima Velocidad Atmosferica: Promedio = {max_speed_avg:.2f}, Moda = {max_speed_mode}, Maximo = {max_speed_max}, Minimo = {max_speed_min}")
    pass