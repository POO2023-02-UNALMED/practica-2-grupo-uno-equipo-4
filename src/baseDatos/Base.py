from abc import ABC, abstractclassmethod

#@autor: David Restrepo
class Base(ABC):
    _administradores = []
    _hoteles = []
    _huespedes = []
    _empleados = []

    @classmethod
    def setAdministradores(cls, administradores):
        cls._administradores = administradores

    @classmethod
    def getAdministradores(cls):
        return cls._administradores

    @classmethod
    def addAdministradores(cls, administrador):
        cls._administradores.append(administrador)

    @classmethod
    def setHoteles(cls, hoteles):
        cls._hoteles = hoteles

    @classmethod
    def getHoteles(cls):
        return cls._hoteles

    @classmethod
    def addHoteles(cls, hotel):
        cls._hoteles.append(hotel)

    @classmethod
    def getHuespedes(cls):
        return cls._huespedes

    @classmethod
    def setHuespedes(cls, huespedes):
        cls._huespedes = huespedes

    @classmethod
    def addHuespedes(cls, huesped):
        cls._huespedes.append(huesped)

    @classmethod
    def getEmpleados(cls):
        return cls._empleados

    @classmethod
    def setEmpleados(cls, empleados):
        cls._empleados = empleados

    @classmethod
    def addEmpleados(cls, empleado):
        cls._empleados.append(empleado)