from .Usuario import Usuario
from .Preferencia import Preferencia
from .PresentacionBono import PresentacionBono
from baseDatos.Base import Base
from ..hotel import Reserva

#@autor: Alejandra Toro

class Huesped(Usuario, PresentacionBono):
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

    def getReserva(self) -> Reserva:
        return self._reserva
    
    def getReservaServis(self):
        return self._reserva
   
    def setReserva(self, value):
        self._reserva = value

    
    def getHabitacion(self):
        return self._habitacion

    
    def setHabitacion(self, value):
        self._habitacion = value

    
    def enReserva(self):
        return self._enReserva

    
    def setEnReserva(self, value):
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
        if self._preferencias is None:
            self._preferencias = []
        self._preferencias.append(preferencia)

    def ofrecerBono(self):
        print(f"Se le han añadido {PresentacionBono.BONOHUESPED} $ a su cuenta bancaria")
        self.getCuentaBancaria().depositar(PresentacionBono.BONOHUESPED)

    def presentacion(self):
        intro = PresentacionBono.recogerDatos(self)
        return f"Soy un huésped. {intro}"

    def entrando(self):
        return "Entrando a su cuenta de Huesped, señor(a) "+ self.getNombre()
    
    #Método que se usa en recomendacion hoteles por similar, para elegir habitaciones basadas en las preferencias
    def _recomendacionHabitacionPorSimilar(self,hotel,preferencia):
        habitacionesHotel = hotel.getHabitaciones()
        tiposHabitacionesPreferencias = preferencia.getTiposHabitaciones()
        habitaciones = [habitacion for habitacion in habitacionesHotel if habitacion.getTipo() in tiposHabitacionesPreferencias]
        return habitaciones
        
    #Para recomendar hoteles basado en las preferencias del huesped
    def recomendacionHotelesPorSimilar(self,ciudad):
        recomendaciones = {}
        hotelesBase = Base.getHoteles()
        for hotel in hotelesBase:
            if(hotel.getCiudad() == ciudad):
                for preferencia in self.getPreferencias():
                    if(hotel.getNombre() == preferencia.getNombreHotel()):
                        habitaciones = self._recomendacionHabitacionPorSimilar(hotel,preferencia)
                        if(habitaciones!= None):
                            recomendaciones[hotel] = habitaciones
        return recomendaciones
    #Método que se usa en recomendacion hoteles por historial, para elegir las habitaciones con calificaciones por encima de 4
    def _recomendacionHabitacionPorHistorial(self,hotel):
        habitacionesHotel = hotel.getHabitaciones()
        habitacionesRecomendadas = []
        for i in range(len(habitacionesHotel)):
            calificaciones = {}
            calificaciones = habitacionesHotel[i].getCalificaciones()
            for huesped in list(calificaciones.keys()):
                if(huesped.getId()==self.getId()):
                    if(calificaciones[huesped]>=4):
                        habitacionesRecomendadas.append(habitacionesHotel[i])
                        break
        return habitacionesRecomendadas

    #Para recomendar hoteles y habitaciones basadas en el historial de reservaciones
    def recomendacionHotelesPorHistorial(self,ciudad):
        recomendaciones = {}
        hoteles = []
        historialReservas = self.getHistorialReservas()
        for reserva in historialReservas:
            if(reserva.getCiudad()==ciudad):
                calificacion = reserva.getCalificacionHotel()
                if(calificacion>=4):
                    hoteles.append(reserva.getHotel())
                
        for hotel in hoteles:
            habitaciones = self._recomendacionHabitacionPorHistorial(hotel)
            if(habitaciones!=None):
                recomendaciones[hotel] = habitaciones
        
        return recomendaciones