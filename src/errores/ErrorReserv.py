from errores.ErrorAplicacion import ErrorAplicacion

#@autor: David Restrepo

class ErrorReserv(ErrorAplicacion):
    def __init__(self, complemento = ""):
        super().__init__("Error en la reserva " + "("+ complemento +")")