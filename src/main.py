from tkinter import Tk
from gestorGrafico.Root import Root
from gestorGrafico.Inicio import Inicio
from gestorGrafico.Recomendaciones import Recomendaciones
from baseDatos.deserealizador import Deserializador
from baseDatos.serializador import Serializador
from baseDatos.Base import Base

#@autor: David Restrepo


if __name__ == '__main__' :
    Deserializador.deserializador()

    root = Root()
    Inicio(root)
    root.mainloop()
    
    Serializador.serializador()
    