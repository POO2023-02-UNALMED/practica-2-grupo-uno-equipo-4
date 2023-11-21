from .ErrorReserv import ErrorReserv

#@autor: David Restrepo
# Esta clase maneja los errores en los que se intersecan la fechas dentro de reserva

class ErrorDateIntersection(ErrorReserv):
    def __init__(self, fReIni, fReFin):
        super().__init__(f"Error. Su fecha se está intersecando con las fechas de la siguiente reserva:\n"+
                        f"Fecha de inicio: {fReIni}\n"+
                        f"Fecha de fin: {fReFin}\n")
        self.fReIni = "/".join(fReIni)
        self.fReFin = "/".join(fReFin)
        
    def mostrarMensaje(self):
        return (f"Error. Su fecha se está intersecando con las fechas de la siguiente reserva:\n"+
                f"Fecha de inicio: {self.fReIni}\n"+
                f"Fecha de fin: {self.fReFin}\n")