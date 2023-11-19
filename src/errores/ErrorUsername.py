from .ErrorRegister import ErrorRegister

#@autor: David Restrepo

class ErrorUsername(ErrorRegister):
    def __init__(self, nombre):
        super().__init__(f"El nombre de usuario {nombre} ya está en uso.")
        self.nombre = nombre
        
    def mostrarMensaje(self):
        return (f"El nombre de usuario {self.nombre} ya está en uso.")