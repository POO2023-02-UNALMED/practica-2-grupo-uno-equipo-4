from .ErrorRegister import ErrorRegister

#@autor: David Restrepo
# Esta clase controla los errores que se presentan cuando se deja algo sin editar dentro de un formulario

class ErrorEmpty(ErrorRegister):
    def __init__(self, cajon):
        super().__init__(f"Ha dejado un elemento sin editar {cajon}")
        self.cajon = cajon
        
    def mostrarMensaje(self):
        return (f"Ha dejado un elemento sin editar: {self.cajon}")