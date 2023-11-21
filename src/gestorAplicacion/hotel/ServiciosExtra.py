#from gestorAplicacion.usuarios.Huesped import Huesped
from gestorAplicacion.finanzas.CuentaBancaria import CuentaBancaria

class ServiciosExtra:
    def __init__(self,idServicio = 0, tipoServicio="", tarifa=0):
        self.idServicio = idServicio
        self.listaTipoServicio = []
        self.tipoServicio = tipoServicio
        self.consumidores = []
        self.nombre = ""
        self.tarifa = tarifa
        self.calificaciones = {}

    #Se encarga de calcular el promedio del servicio
    @classmethod
    def promedioCalificaciones(cls,servicio):
        total = 0
        for clave,valor in servicio.getCalificaciones().items():
            total = total + valor
        return total

    #agrega calificaciones
    def addCalificacion(self,usuario,calificacion):
        self.calificaciones[usuario] = calificacion

    def setIdServicio(self,idServicio):
        self.idServicio = idServicio

    def getListaTipoServicio(self):
        return self.listaTipoServicio

    def setListaTipoServicio(self,listaTipoServicio):
        self.listaTipoServicio = listaTipoServicio

    def getTipoServicio(self):
        return self.tipoServicio

    def setTipoServicio(self,tipoServicio):
        self.tipoServicio = tipoServicio

    def getConsumidores(self):
        return self.consumidores

    def setConsumidores(self,consumidores):
        self.consumidores = consumidores

    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre = nombre

    def getTarifa(self):
        return self.tarifa

    def setTarifa(self,tarifa):
        self.tarifa = tarifa

    def getCalificaciones(self):
        return self.calificaciones

    def setCalificaciones(self,calificaciones):
        self.calificaciones = calificaciones

    def transportar(self):
        pass

    def escogerLimpiador(self):
        pass

    @classmethod

    def listServiciosExtra(cls, huesped):

        servicios = huesped.getReservaServis().getServicios()

        if servicios == []:

            return False
        
        else:

            return servicios

    @classmethod

    def agregarServicioTransporte(cls, huesped):
        transporte = ServiciosExtra(0, "Transporte", 2000)
        huesped.getReserva().addServicios(transporte)

        cuentaHotel = huesped.getReserva().getHotel().getCuentaBancaria()
        CuentaBancaria.transfarencia(huesped.getCuentaBancaria(), cuentaHotel, 2000)

    @classmethod

    def agregarServicioAlimentacion(cls, huesped):
        alimentacion = ServiciosExtra(1, "Alimentación", 1000)
        huesped.getReserva().addServicios(alimentacion)

        cuentaHotel = huesped.getReserva().getHotel().getCuentaBancaria()
        CuentaBancaria.transfarencia(huesped.getCuentaBancaria(), cuentaHotel, 1000)

    @classmethod

    def agregarServicioLimpieza(cls, huesped):
        limpieza = ServiciosExtra(2, "Limpieza", 3000)
        huesped.getReserva().addServicios(limpieza)

        cuentaHotel = huesped.getReserva().getHotel().getCuentaBancaria()
        CuentaBancaria.transfarencia(huesped.getCuentaBancaria(), cuentaHotel, 3000)

    @classmethod

    def eliminarServicio(cls, huesped, servicio):

        huesped.getReserva().delServicio(servicio)

        costo = 0

        if servicio.getTipoServicio() == "Transporte":
            costo = 2000

        elif servicio.getTipoServicio() == "Alimentación":
            costo = 1000

        elif servicio.getTipoServicio() == "Limpieza":
            costo = 3000



        cuentaHotel = huesped.getReserva().getHotel().getCuentaBancaria()
        CuentaBancaria.transfarencia(cuentaHotel, huesped.getCuentaBancaria(), costo)


