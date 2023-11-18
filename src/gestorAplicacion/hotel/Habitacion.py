from .Hotel import Hotel
from ..usuarios.Huesped import Huesped
from typing import List

class Habitacion:
    
    def __init__(self,__id,__tipo=None,__numero_camas=None,__precio=None,__hotel=None):
        
        self.__id = __id
        self.__calificaciones = {}
        self.__calificaciones[Huesped()] = 5.0
        
        if __tipo is not None:
            self.__tipo = __tipo
            
        if __numero_camas is not None:
            self.__numero_camas =__numero_camas
        
        if __precio is not  None:
            self.__precio = __precio
            
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
        self.__calificaciones[__huesped] = __calificacion
        
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
            
    @property
    def getId(self):
        return self.__id
    
    def setId(self, __id):
        self.__id = __id
        
    @property
    def getHotel(self):
        return self.__hotel
    
    def setHotel(self, __hotel):
        self.__hotel = __hotel
        
    def getTipo(self):
        return self.__tipo
    
    def setTipo(self, __tipo):
        self.__tipo = __tipo
        
    @property
    def getNumeroCamas(self):
        return self.__numero_camas
    
    def setNumeroCamas(self, __numero_camas):
        self.__numero_camas = __numero_camas
        
    @property
    def getPrecio(self):
        return self.__precio
    
    def setPrecio(self, __precio):
        self.__precio = __precio
        
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
        return self.__calificaciones

    def setCalificaciones(self, __calificaciones):
        self.__calificaciones = __calificaciones
        
    @property
    def getReservada(self):
        return self.__reservada
    
    def setReservada(self, __reservada):
        self.__reservada = __reservada
    
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