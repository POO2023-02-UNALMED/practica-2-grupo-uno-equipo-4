from tkinter import Tk, Menu, messagebox
from baseDatos.serializador import Serializador

#@autor: David Restrepo

class Root(Tk) :
    def __init__(self) -> None:
        super().__init__()
        self.state("zoomed")

    def mainloop(self, n: int = 0) -> None:
        return super().mainloop(n)
    
    def cleanRoot(self) :
        for w in self.winfo_children() :
            w.destroy()

    def salir(self) :
        from gestorGrafico.Inicio import Inicio
        Serializador.serializador()
        self.cleanRoot()
        Inicio(self)

    def inicio(self, user) :
        #from gestorGrafico.UserWindow import UserWindow
        self.cleanRoot()
       # UserWindow(self, user)
       
    def aplicacion(self):
        messagebox.showinfo("Aplicación", "CosmoReserve es un programa desarrollado para gestionar una cadena de hoteles.")
        
    def ayuda(self):
        messagebox.showinfo("Ayuda","¿Qué haces por aquí 👀?\t\t\n\nSomos:\nAlejandra Toro Grisales\nJuan Pablo Rivera Alvarez\nDavid Restrepo Aguilar\nYohan Camilo Sanchez Meza\nSamuel Castaño Alfonso")