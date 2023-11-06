from .Usuario import Usuario
from .Preferencia import Preferencia

class Huesped(Usuario):
    def __init__(self,vip=None,preferencias=None, nombre=None, telefono=None, username=None, password=None, cuentaBancaria=None):
        super().__init__(nombre, telefono, username, password, cuentaBancaria)
        
        if vip is not None:
            self._vip = vip

        if preferencias is not None:
            self._preferencias = preferencias

        self._reserva = None
        self._habitacion = None
        self._enReserva = None
        self._historialReservas = None

    def isVip(self):
        return self._vip

    def setVip(self,vip):
        self._vip = vip

    def getReserva(self):
        return self._reserva
   
    def setReserva(self, value):
        self._reserva = value

    
    def getHabitacion(self):
        return self._habitacion

    
    def setHabitacion(self, value):
        self._habitacion = value

    
    def enReserva(self):
        return self._enReserva

    
    def enReserva(self, value):
        self._enReserva = value

    def getPreferencias(self):
        return self._preferencias
    
    def setPreferencias(self,preferencias):
        if self._preferencias is None:
            self._preferencias = []
        self._preferencias = preferencias
    
    def getHistorialReservas(self):
        return self._historialReservas

    
    def setHistorialReservas(self, value):
        if self._historialReservas is None:
            self._historialReservas = []
        self._historialReservas = value
    
    def addReserva(self,reserva):  
        if self._historialReservas is None:
            self._historialReservas = []
        self._historialReservas.append(reserva)

    def generarReserva(huesped,habitacion,fechaEntrada):
        pass

    def consultarVip(self):
        return self._vip is True
    
    def isEnReserva(self):
        return self._enReserva
    
    def setEnReserva(self,enReserva):
        self._enReserva = enReserva

    def agregarPreferencias(self,ciudad,nombreHotel,tipoHabitacion):
        preferencia = Preferencia(ciudad,nombreHotel,tipoHabitacion)
        self._preferencias.append(preferencia)

    def presentacion():
        pass

    def entrando(self):
        return "Entrando a su cuenta de Huesped, señor(a) "+ self.getNombre()
