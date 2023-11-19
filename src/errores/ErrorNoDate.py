from .ErrorReserv import ErrorReserv

#@autor: David Restrepo

class ErrorNoDate(ErrorReserv):
    def __init__(self, cajon, ingreso):
        super().__init__(f"El valor ingresado no es una fecha, está ingresando {ingreso} en {cajon}.")
        self.cajon = cajon
        self.ingreso = ingreso
        
    def mostrarMensaje(self):
        return (f"El valor ingresado no es una fecha, está ingresando {self.ingreso} en {self.cajon}.")