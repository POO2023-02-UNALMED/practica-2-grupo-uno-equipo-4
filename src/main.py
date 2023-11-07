from tkinter import Tk
from gestorGrafico.Root import Root
from gestorGrafico.Inicio import Inicio

if __name__ == '__main__' :
    #Deserializador.deserializador()

    root = Root()
    Inicio(root)
    root.mainloop()
    
    #Serializador.serializador()