class Preferencia:
    def __init__(self,ciudad=None,nombreHotel=None,tiposHabitaciones=None):
        if ciudad is not None:
            self._ciudad = ciudad
        if nombreHotel is not None:
            self._nombreHotel = nombreHotel

        if tiposHabitaciones is not None:
            self._tiposHabitaciones = tiposHabitaciones
    
    def getCiudad(self):
        return self._ciudad
    
    def getNombreHotel(self):
        return self._nombreHotel
    
    def getTiposHabitaciones(self):
        return self._tiposHabitaciones