class Hotel:
    
    _totalHoteles = []
    
    def __init__(self,__cuenta_bancaria,__nombre=None,__ciudad=None,__servicios=None,__habitaciones=None,__empleados=None):
        
        self.__cuenta_bancaria = __cuenta_bancaria
            
        if __nombre is  not None:
            self.__nombre = __nombre
            
        if __ciudad is not None:
            self.__servicios = __servicios
        
        if __servicios is not None:
            self.__ciudad = __ciudad
            
        if __habitaciones is  not None:
            self.__habitaciones = __habitaciones
            
        if __empleados is not None:
            self.__empleados = __empleados
        
        for i  in  __habitaciones:
            i.__hotel(self)
        
        #for  i  in __empleados:
        #   i.setHotel(self)
    
    def addHabitacion(self, habitacion):
        self.__habitaciones.append(habitacion)
      
    def addHistorialClientes(self, huesped):
        self.__historial_clientes.append(huesped)
        
    def addAdministradores(self, administrador):
        self.__administradores.append(administrador)
    
    @classmethod
    def getTotalHoteles(cls):
        return cls._total_hoteles
    
    @classmethod
    def setTotalHoteles(cls,_total_hoteles):
        cls._total_hoteles = _total_hoteles
    
    @classmethod
    def addTotalHoteles(cls,_hotel):
        cls._total_hoteles.append(_hotel)
    
    @classmethod
    def addTotalHoteles(cls, _total_hoteles):
        cls._total_hoteles = _total_hoteles
    
    @property
    def getCuentaBancaria(self):
        return self.__cuenta_bancaria
    
    def setCuentaBancaria(self, __cuenta_bancaria):
        self.__cuenta_bancaria = __cuenta_bancaria
        
    @property
    def getServicios(self):
        return self.__servicios
    

    def setServicios(self, __servicios):
        self.__servicios = __servicios
        
    @property
    def getNombre(self):
        return self.__nombre
    

    def setNombre(self, __nombre):
        self.__nombre = __nombre
        
    @property
    def getCuidad(self):
       return  self.__ciudad
    

    def setCiudad(self, __ciudad):
        self.__ciudad = __ciudad
        
    @property
    def getHabitaciones(self):
        return self.__habitaciones
    

    def setHabitaciones(self, __habitaciones):
        self.__habitaciones = __habitaciones
        
    @property
    def getEmpleados(self):
       return  self.__empleados
    

    def setEmpleados(self, __empleados):
        self.__empleados = __empleados
        
    @property
    def getHistorialClientes(self):
        return  self.__historial_clientes
    

    def setHistorialCientes(self, __historial_clientes):
        self.__historial_clientes = __historial_clientes
        
    @property
    def getAdministradores(self):
        return  self.__administradores
    

    def setAdministradores(self, __administradores):
        self.__administradores = __administradores 