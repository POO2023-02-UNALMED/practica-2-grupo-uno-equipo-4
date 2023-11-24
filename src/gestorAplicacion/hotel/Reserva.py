from .Hotel import Hotel
from gestorAplicacion.hotel.ServiciosExtra import ServiciosExtra

class Reserva:
    def __init__(self,_huesped,_habitacion,_fechaEntrada,_fechaSalida,_costo):

        self._calificacionHotel = 0
        self._calificacionHabitacion = 0
        self._huesped = _huesped
        self._habitacion = _habitacion
        self._fechaEntrada = _fechaEntrada
        self._fechaSalida = _fechaSalida
        self._costo  = _costo
        self._hotel = _habitacion.getHotel()
        #_huesped.addReserva(self)
        ciu = self._hotel.getCiudad()
        self._ciudad = ciu
        self._servicios = []

    def getServicios(self):
        return self._servicios
    
    def addServicios(self, servicio):
        self._servicios.append(servicio)

        self._costo += servicio.getTarifa()

    def delServicio(self, servicio):

        self._servicios.remove(servicio)
        self._costo -= servicio.getTarifa()

    def getHuesped(self):
        return self._huesped

    def setHuesped(self,_huesped):
        self._huesped = _huesped

    def getHabitacion(self):
        return self._habitacion

    def setHabitacion(self,_habitacion):
        self._habitacion = _habitacion

    def getFechaEntrada(self):
        return self._fechaEntrada

    def setFechaEntrada(self,_fechaEntrada):
        self._fechaEntrada = _fechaEntrada

    def getFechaSalida(self):
        return self._fechaSalida

    def setFechaSalida(self, _fechaSalida):
        self._fechaSalida = _fechaSalida

    def getCosto(self):
        return self._costo

    def setCosto(self, _costo):
        self._costo = _costo

    def getCiudad(self):
        return self._ciudad
    
    def setHotel(self,hotel) -> Hotel:
        self._hotel = hotel

    def getHotel(self):
        return self._hotel
    
    def setCiudad(self,ciudad):
        self._ciudad = ciudad

    def setCalificacionHotel(self,calificacion):
        self._calificacionHotel = calificacion
    
    def getCalificacionHotel(self):
        return self._calificacionHotel
    
    def setCalificacionHabitacion(self,calificacion):
        self._calificacionHabitacion = calificacion

    def getCalificacionHabitacion(self):
        return self._calificacionHabitacion
            
        