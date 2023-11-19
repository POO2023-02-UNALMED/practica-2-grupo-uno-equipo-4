from .ErrorReserv import ErrorReserv

#@autor: David Restrepo

class ErrorEnterDate(ErrorReserv):
    def __init__(self, cajon, ingreso):
        super().__init__(f"La fecha ingresada en: {cajon} es incorrecta, pues no está cumpliendo con el formato dd/mm/aa o no cumple con el orden de las fechas\n\n" +
                f"fecha ingresada: {ingreso}.")
        self.cajon = cajon
        self.ingreso = ingreso
        
    def mostrarMensaje(self):
        return (f"La fecha ingresada en: {self.cajon} es incorrecta, pues no está cumpliendo con el formato dd/mm/aa o no cumple con el orden de las fechas\n\n" +
                f"fecha ingresada: {self.ingreso}.")