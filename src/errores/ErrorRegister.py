from errores.ErrorAplicacion import ErrorAplicacion

#@autor: David Restrepo
# Esta clase se encarga de manejar los errores generales que se pueden presentar dentro del registro de datos

class ErrorRegister(ErrorAplicacion):
    def __init__(self, complemento = ""):
        super().__init__("Error en el registro " + "("+ complemento +")")