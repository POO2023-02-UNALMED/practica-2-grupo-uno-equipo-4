from .ErrorRegister import ErrorRegister

#@autor: David Restrepo
# Esta clase se encarga del error que se presenta cuando el username ingresado ya está en uso (este es extra =) )

class ErrorUsername(ErrorRegister):
    def __init__(self, nombre):
        super().__init__(f"El nombre de usuario {nombre} ya está en uso.")
        self.nombre = nombre
        
    def mostrarMensaje(self):
        return (f"El nombre de usuario {self.nombre} ya está en uso.")