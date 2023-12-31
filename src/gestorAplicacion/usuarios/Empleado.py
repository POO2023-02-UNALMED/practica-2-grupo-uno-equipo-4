from .PresentacionBono import PresentacionBono
from .Usuario import Usuario
#from gestorAplicacion.hotel.Hotel import Hotel
class Empleado (Usuario, PresentacionBono):
    def __init__(self, nombre, telefono, username, password, cuentaBancaria, hotel=None, estado_empleado = False, salario=0):
        super().__init__(nombre, telefono, username, password, cuentaBancaria)
        
        self.salario = salario
        self.estadoEmpleado = estado_empleado
        self.motivosCalificacion = {}
        self.sugerencias = {}
        self.calificaciones = {}
        self.ultimoPago = None

        if hotel is not None:
            self.hotel = hotel
            hotel.addEmpleados(self)


    def addCalificacion(self,usuario,calificacion):
        self.calificaciones[usuario] = calificacion

    def addMotivos(self,motivo):
        if self.motivosCalificacion[motivo] is not None:
            self.motivosCalificacion[motivo] = self.motivosCalificacion[motivo] + 1
        else:
            self.motivosCalificacion[motivo] = 1

    @classmethod
    def promedioCalificaciones(cls,empleado):
        total = 0
        for clave, valor in empleado.getCalificaciones().items():
            total = total + valor
        if len(empleado.getCalificaciones().items()) > 0:
            return  total/len(empleado.getCalificaciones().items())
        else:
            return total

    def mejorCalificacion(self, empleados):
        rango = []
        for i in empleados:
            if self.promedioCalificaciones(i)>=3:
                rango.append(i)
        return rango

    def rangoCalificaciones(self,empleados):
        rango = []
        for i in empleados:
            for clave,valor  in i.getSugerencias().items():
                rango.append(clave)
        return rango

    def addSugerencias(self,sugerencia):
        if self.getSugerencias()[sugerencia] is None:
            self.getSugerencias()[sugerencia] = 1
        else:
            self.getSugerencias()[sugerencia] = self.getSugerencias()[sugerencia]+1

    def addSugerenciasPendientes(self, sugerencias):
        self.sugerenciasPendientes[self.getId()] = sugerencias


    def getEstadoEmpleado(self):
        return self.estadoEmpleado

    def setEstadoEmpleado(self,estadoEmpleado):
        self.estadoEmpleado = estadoEmpleado

    def getMotivosCalificacion(self):
        return self.motivosCalificacion

    def setMotivosCalificacion(self,motivosCalificacion):
        self.motivosCalificacion = motivosCalificacion

    def getSugerencias(self):
        return self.sugerencias

    def setSugerencias(self,sugerencias):
        self.sugerencias = sugerencias

    def getCalificaciones(self):
        return self.calificaciones

    def setCalificaciones(self,calificaciones):
        self.calificaciones = calificaciones

    def getSugerenciasPendientes(self):
        return self.sugerenciasPendientes

    def setSugerenciasPendientes(self,sugerencias):
        self.sugerenciasPendientes = sugerencias

    def getUltimoPago(self):
        return self.ultimoPago

    def setUltimoPago(self,ultimoPago):
        self.ultimoPago = ultimoPago

    def getSalario(self):
        return self.salario
    
    def getHotel(self):
        return self.hotel
    
    def setHotel(self,hotel):
        self.hotel = hotel
    
    def setSalario(self, salario):
        self.salario = salario

    def buenasCalificaciones(self):
        pass
    
    def ofrecerBono(self):
        print(f"Se le han añadido {PresentacionBono.BONOEMPLEADO} $ a su cuenta bancaria")
        self.getCuentaBancaria().depositar(PresentacionBono.BONOEMPLEADO)
    
    def presentacion(self):
        intro = PresentacionBono.recogerDatos(self)
        return f"Soy un empleado. {intro}"

    def entrando(self):
        return "Entrando a su cuenta de Empleado, señor(a) "+ self.getNombre()
    
    