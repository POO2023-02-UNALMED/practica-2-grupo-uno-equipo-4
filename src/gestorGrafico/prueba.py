

class Habitacion:
    c = 0
    def __init__(self, calificaciones):
        self._cals = calificaciones
        self.id = Habitacion.c
        Habitacion.c += 1
        
            
    def getCalificaciones(self):
        return self._cals
    
    def getId(self):
        return self.id
        

if __name__ == "__main__":
    
        habitaciones = []
        
        
        hab1 = Habitacion({"hola": 5, "gorda": 3})
        hab2 = Habitacion({"tola": 5, "gola":5})
        hab3 = Habitacion({"cola": 3, "fer": 3})
        
        habitaciones.append(hab1)
        habitaciones.append(hab2)
        habitaciones.append(hab3)

        promHab = {}
        
        for j in habitaciones:
            dicCalificaciones = j.getCalificaciones()
            calificaciones = list(dicCalificaciones.values())
            
            s = 0
            for k in calificaciones:
                s += k
            
            prom = s/len(calificaciones)
            promHab[j] = prom
        
        sortedPromHab = dict(sorted(promHab.items(), key=lambda item:item[1], reverse=True))
        sortedRooms = list(sortedPromHab.keys())
        for i in sortedRooms:
            print(i.getId())