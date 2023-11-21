#@autor: David Restrepo
# Esta clase es la padre de todos los errores implimentados en la aplicación

class ErrorAplicacion(Exception):
    def __init__(self, complemento = ""):
        super().__init__("Manejo de errores de la Aplicacion: " + complemento)