class Hotel:
    
    _totalHoteles = []
    
    def __init__(self,__cuenta_bancaria,__nombre=None,__ciudad=None,__servicios=None,_habitaciones=None,__empleados=None):
        
        self.__cuenta_bancaria = __cuenta_bancaria
        self.__historial_clientes = []
            
        if __nombre is  not None:
            self.__nombre = __nombre
            
        if __ciudad is not None:
            self.__ciudad = __ciudad
        
        if __servicios is not None:
            self._servicios = __servicios
            
        if _habitaciones is  not None:
            self._habitaciones = _habitaciones
            
        if __empleados is not None:
            self.__empleados = __empleados
        if _habitaciones is not None:
            for i  in  _habitaciones:
                i.setHotel(self)
        if __empleados is not None:
            for  i  in __empleados:
               i.setHotel(self)
    
    def addHabitacion(self, habitacion):
        self._habitaciones.append(habitacion)
      
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
    
    
    def getCuentaBancaria(self):
        return self.__cuenta_bancaria
    
    def setCuentaBancaria(self, __cuenta_bancaria):
        self.__cuenta_bancaria = __cuenta_bancaria
        
    
    def getServicios(self):
        return self._servicios
    

    def setServicios(self, _servicios):
        self._servicios = _servicios
        
    def getNombre(self):
        return self.__nombre
    

    def setNombre(self, __nombre):
        self.__nombre = __nombre
        
    def getCiudad(self):
       return  self.__ciudad
    

    def setCiudad(self, __ciudad):
        self.__ciudad = __ciudad
        
    def getHabitaciones(self):
        return self._habitaciones
    

    def setHabitaciones(self, _habitaciones):
        self._habitaciones = _habitaciones
        
    @property
    def getEmpleados(self):
       return  self.__empleados
    

    def setEmpleados(self, __empleados):
        self.__empleados = __empleados
        
    def getHistorialClientes(self):
        return  self.__historial_clientes
    

    def setHistorialCientes(self, __historial_clientes):
        self.__historial_clientes = __historial_clientes
        
    @property
    def getAdministradores(self):
        return  self.__administradores
    

    def setAdministradores(self, __administradores):
        self.__administradores = __administradores 