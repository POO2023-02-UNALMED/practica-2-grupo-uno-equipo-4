from .ErrorRegister import ErrorRegister

#@autor: David Restrepo

class ErrorValores(ErrorRegister):
    def __init__(self, cajon, typeError):
        super().__init__(f"El valor ingresado es erróneo, pues se debe ingresar un {typeError} y está ingresando otro dato.")
        self.cajon = cajon
        self.typeError = typeError
        
    def mostrarMensaje(self):
        return (f"El valor ingresado es erróneo, pues se debe ingresar un {self.typeError} y está ingresando otro dato en: {self.cajon}.")
    
    