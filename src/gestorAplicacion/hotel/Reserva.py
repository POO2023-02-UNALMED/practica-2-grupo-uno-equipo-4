class Reserva:
    def __init__(self,__huesped,__habitacion,__fechaEntrada,__fechaSalida,__costo):

        self.__calificacionHotel = 0
        self.__calificacionHabitacion = 0

        self.__huesped = __huesped
        self.__habitacion = __habitacion
        self.__fechaEntrada == __fechaEntrada
        self.__fechaSalida == __fechaSalida
        self.__costo  = __costo

    @property
    def getHuesped(self):
        return self.__huesped

    def setHuesped(self,__huesped):
        self.__huesped = __huesped

    @property
    def getHabitacion(self):
        return self.__habitacion

    def setHabitacion(self,__habitacion):
        self.__habitacion = __habitacion

    @property
    def getFechaEntrada(self):
        return self.__fechaEnrada

    def setFechaEntrada(self,__fechaEntrada):
        self.__fechaEntrada = __fechaEntrada

    @property
    def getFechaSalida(self):
        return self.__fechaSalida

    def setFechaSalida(self, __fechaSalida):
        self.__fechaSalida = __fechaSalida

    @property
    def getCosto(self):
        return self.__costo

    def setCosto(self, __costo):
        self.__costo = __costo
            
        