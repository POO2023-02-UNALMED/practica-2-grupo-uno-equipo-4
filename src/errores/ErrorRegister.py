from errores.ErrorAplicacion import ErrorAplicacion

#@autor: David Restrepo

class ErrorRegister(ErrorAplicacion):
    def __init__(self, complemento = ""):
        super().__init__("Error en el registro " + "("+ complemento +")")