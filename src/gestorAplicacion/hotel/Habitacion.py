from .Hotel import Hotel
from ..usuarios.Huesped import Huesped
from ..usuarios.Huesped import Huesped
from typing import List

class Habitacion:
    
    def __init__(self,_id,_tipo=None,_numero_camas=None,_precio=None,__hotel=None):
        
        self._reservada = False
        self._id = _id
        self._calificaciones = {}
        self._calificaciones[Huesped()] = 5.0
        
        if _tipo is not None:
            self._tipo = _tipo
            
        if _numero_camas is not None:
            self._numero_camas =_numero_camas
        
        if _precio is not  None:
            self._precio = _precio
            
        if __hotel is not None:
            self.__hotel  = __hotel
            

    def calcularPromedio(self) -> float:
        prom = 0
        cont  = 0
        for clave,valor in self.__calificaciones.items():
            prom = prom + valor
            cont = cont + 1
        return prom/cont

    def rangoPrecio(self,totalHabitaciones) -> List:
        rango = []
        for i  in totalHabitaciones:
            if abs(i.getPrecio())-self.__precio:
                rango.append(i)
        return rango

    def mejorCalificadas(self,habitaciones) -> List:
        rango =  []
        for i in habitaciones:
            if i.calcularPromedio() >= 3:
                rango.append(i)

    def  addCalificacion(self, __huesped,__calificacion):
        self._calificaciones[__huesped] = __calificacion
        
    def addMotivos(self, motivo):
        if self.__motivos_calificaciones[motivo] is  not  None:
            self.__motivos_calificaciones[motivo] = self.__motivos_calificaciones[motivo]+1    
        else:
            self.__motivos_calificaciones[motivo] = 1
            
    def  addSugerencias(self,sugerencia):
        if self.__sugerencias[sugerencia] is  not  None:
            self.__sugerencias[sugerencia] = self.__sugerencias[sugerencia]+1    
        else:
            self.__sugerencias[sugerencia] = 1
            
    def addReservas(self,reserva):
        self.__reservas.append(reserva)
            
    
    def getId(self):
        return self._id
    
    def setId(self, _id):
        self._id = _id
        
    @property
    def getHotel(self):
        return self.__hotel
    
    def setHotel(self, __hotel):
        self.__hotel = __hotel
        
    def getTipo(self):
        return self._tipo
    
    def setTipo(self, _tipo):
        self._tipo = _tipo
        
    
    def getNumeroCamas(self):
        return self._numero_camas
    
    def setNumeroCamas(self, _numero_camas):
        self._numero_camas = _numero_camas
        
    
    def getPrecio(self):
        return self._precio
    
    def setPrecio(self, _precio):
        self._precio = _precio
        
    @property
    def getReserva(self):
        return self.__reserva
    
    def setReserva(self, __reserva):
        self.__reserva = __reserva
        
    @property
    def getReservas(self):
        return self.__reservas

    def setReservas(self, __reservas):
        self.__reservas = __reservas
        

    def getCalificaciones(self):
        return self._calificaciones

    def setCalificaciones(self, _calificaciones):
        self._calificaciones = _calificaciones
        
    
    def getReservada(self):
        return self._reservada
    
    def setReservada(self, _reservada):
        self._reservada = _reservada
    
    @property
    def getMotivosCalificaciones(self):
        return  self.__motivos_calificaciones
    
    def setMotivosCalificaciones(self, __motivos_calificaciones):
        if self.__motivos_calificaciones is None:
            self.__motivos_calificaciones[__motivos_calificaciones] = 1
        else:
            self.__motivos_calificaciones[__motivos_calificaciones] =  self.__motivos_calificaciones[__motivos_calificaciones] + 1
        
    @property
    def getSugerencias(self):
        return self.__sugerencias
    
    def setSugerencias(self, __sugerencias):
        self.__sugerencias = __sugerencias