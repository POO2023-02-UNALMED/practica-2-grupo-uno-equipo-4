from .Usuario import Usuario
class Empleado:
    def __init__(self,estadoEmpleado):
        self.estadoEmpleado = estadoEmpleado
        self.motivosCalificacion = {}
        self.sugerencias = {}
        self.calificaciones = {}
        self.ultimoPago = None

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

    def getUltimoPago(self):
        return self.ultimoPago

    def setUltimoPago(self,ultimoPago):
        self.ultimoPago = ultimoPago

    def buenasCalificaciones(self):
        pass
