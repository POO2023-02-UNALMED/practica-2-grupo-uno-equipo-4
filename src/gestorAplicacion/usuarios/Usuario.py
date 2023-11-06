from abc import ABC, abstractmethod

class Usuario(ABC):
    _numUser= 0
    def __init__(self,nombre=None,telefono=None,username=None,password=None,cuentaBancaria=None):
        Usuario._numUsuario+=1
        self._id = Usuario._numUsuario
        if nombre is not None:
            self._nombre = nombre

        if telefono is not None:
            self._telefono = telefono
        
        if username is not None:
            self._username = username
        
        if password is not None:
            self._password = password

        if cuentaBancaria is not None:
            self._cuentaBancaria = cuentaBancaria
    
    def getId(self):
        return self._id
    

    def getNombre(self):
        return self._nombre

    def setNombre(self,nombre):
        self._nombre = nombre
    
    def getTelefono(self):
        return self._telefono

    def setTelefono(self,telefono):
        self._telefono = telefono

    def getUsername(self):
        return self._username

    def setUsername(self,username):
        self._username = username

    def getPassword(self):
        return self._password

    def setPassword(self,password):
        self._password = password

    def getCuentaBancaria(self):
        return self._cuentaBancaria

    def setCuentaBancaria(self,cuentaBancaria):
        self._cuentaBancaria = cuentaBancaria

    @classmethod
    def getNumUser():
        return Usuario._numUser

    @abstractmethod
    def entrando():
        pass
    
    @abstractmethod
    def presentacion():
        pass
    