#@autor: David Restrepo
# Esta clase se encarga de crear a programadores, con su nombre, biografía y fotos

class Programador:
    def __init__(self, nombre, biografia, fotos):
        self.nombre = nombre
        self.biografia = biografia
        self.fotos = fotos