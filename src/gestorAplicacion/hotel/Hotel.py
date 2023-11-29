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
            self.__servicios = __servicios
        else:
            self.__servicios = []  # Inicializar __servicios si no se proporciona
            
        if _habitaciones is  not None:
            self._habitaciones = _habitaciones
            
        if __empleados is not None:
            self.__empleados = __empleados
           # for  i  in __empleados:
            #   i.setHotel(self)
        else:
            self.__empleados = []  # Inicializar __servicios si no se proporciona

            
        if _habitaciones is not None:
            for i  in  _habitaciones:
                i.setHotel(self)
            
    def calcularPromedioHotel(self):
        totalHabitaciones = 0
        totalEmpleados = 0
        totalServicios = 0
        for  i in self.getHabitaciones():
            totalHabitaciones = totalHabitaciones+i.calcularPromedio()
        for i in self.getEmpleados():
            totalEmpleados = totalEmpleados + i.promedioCalificaciones(i)
        for i in self.getServicios():
            totalServicios = totalServicios + i.promedioCalificaciones(i)
        totalHabitaciones = totalHabitaciones/len(self._habitaciones)
        totalServicios = totalServicios/len(self.__servicios)
        totalEmpleados = totalEmpleados/len(self.__empleados)
        return (totalEmpleados+totalServicios+totalHabitaciones)/3

    def addServicioExtra(self, servicio):
        self.__servicios.append(servicio)
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
        return self.__servicios
    
    def setServicios(self, __servicios):
        self.__servicios = __servicios
        
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

    def addHabitaciones(self, habitacion):

        self._habitaciones.append(habitacion)
        
    def getEmpleados(self):
       return  self.__empleados
    
    def getEmpleado(self):
       return  self.__empleados
    
    def setEmpleados(self, __empleados):
        self.__empleados = __empleados
        
    def addEmpleados(self, empleado):
        self.__empleados.append(empleado)
        
    def getHistorialClientes(self):
        return  self.__historial_clientes
    

    def setHistorialCientes(self, __historial_clientes):
        self.__historial_clientes = __historial_clientes
        
    @property
    def getAdministradores(self):
        return  self.__administradores
    

    def setAdministradores(self, __administradores):
        self.__administradores = __administradores 