from abc import ABC, abstractmethod

class PresentacionBono(ABC):
    BONOHUESPED = 50000
    BONOEMPLEADO = 10000 

    @staticmethod
    def recogerDatos(usuario):
        nombre = usuario.getNombre()
        id = usuario.getId()
        tel = usuario.getTelefono()
        intro = f"Mi nombre es {nombre}, mi id es {id}, y mi teléfono es {tel}"
        return intro

    @abstractmethod
    def ofrecerBono(self):
        pass