class Nave: 
    
    def __init__(self, nombre, clase, longitud, capacidad, costo, hyperdrive, MGLT, max_speed, pilots=None  ):
        """
        Args:
            nombre (string)
            clase (string)
            longitud (string)
            capacidad (string)
            costo (string)
            hyperdrive (string)
            MGLT (string)
            max_speed (string)
        """        
        self.nombre = nombre
        self.clase = clase
        self.longitud = longitud
        self.capacidad = capacidad
        self.costo = costo
        self.hyperdrive = hyperdrive
        self.MGLT = MGLT
        self.max_speed = max_speed
        self.pilots = pilots
        
    def print(self):
        print(f"Nombre: {self.nombre}")
        print(f"Clase: {self.clase}")
        print(f"Longitud: {self.longitud}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Costo: {self.costo}")
        print(f"Hyperdrive: {self.hyperdrive}")
        print(f"MGLT: {self.MGLT}")
        print(f"Max Speed: {self.max_speed}")
        print("")
        
        