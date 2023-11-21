from .ErrorReserv import ErrorReserv

#@autor: David Restrepo
# Esta clase se encarga de manejar los errores cuando en vez de ingresar una fecha d/m/a, se ingresa otro dato

class ErrorNoDate(ErrorReserv):
    def __init__(self, cajon, ingreso):
        super().__init__(f"El valor ingresado no es una fecha, está ingresando {ingreso} en {cajon}.")
        self.cajon = cajon
        self.ingreso = ingreso
        
    def mostrarMensaje(self):
        return (f"El valor ingresado no es una fecha, está ingresando {self.ingreso} en {self.cajon}.")