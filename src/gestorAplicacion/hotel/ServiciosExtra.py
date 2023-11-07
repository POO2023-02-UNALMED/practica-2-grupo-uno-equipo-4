class ServiciosExtra:
    def __init__(self,idServicio):
        self.idServicio = 0
        self.listaTipoServicio = []
        self.tipoServicio = ""
        self.consumidores = []
        self.nombre = ""
        self.tarifa = 0
        self.calificaciones = {}

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
