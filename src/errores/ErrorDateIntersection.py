from .ErrorReserv import ErrorReserv

#@autor: David Restrepo

class ErrorDateIntersection(ErrorReserv):
    def __init__(self, fReIni, fReFin):
        super().__init__(f"Error. Su fecha se está intersecando con las fechas de la siguiente reserva:\n"+
                        f"Fecha de inicio: {fReIni}\n"+
                        f"Fecha de fin: {fReFin}\n")
        self.fReIni = fReIni
        self.fReFin = fReFin
        
    def mostrarMensaje(self):
        return (f"Error. Su fecha se está intersecando con las fechas de la siguiente reserva:\n"+
                f"Fecha de inicio: {self.fReIni}\n"+
                f"Fecha de fin: {self.fReFin}\n")