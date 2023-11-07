import sys
import tkinter as tk
from tkinter import messagebox
from gestorGrafico.Root import Root
from PIL import Image, ImageTk
from tkinter import Menu
import os
import pathlib
from gestorGrafico.Programador import Programador
from gestorGrafico.Signup import Signup

path = os.path.join(pathlib.Path(__file__).parent.absolute())

class Inicio:
    def __init__(self, root:Root):
        def descripcion():
            self.desc.pack(side="top", fill="both")
        
        david = Programador("David Restrepo Aguilar",
                            "Soy de la carrera de Ciencias de la Computación. Nací en medellín Colombia",
                            [path+"\\imagenes\\david1.png", path+"\\imagenes\\david2.png", 
                            path+"\\imagenes\\david3.png", path+"\\imagenes\\david4.png"])

        self.programadores = [david]
        self.imagenesMGA = [
                    Image.open(path+"\\imagenes\\logo1.png").resize((600, 600)),
                    Image.open(path+"\\imagenes\\logo2.png").resize((600, 600)),
                    Image.open(path+"\\imagenes\\logo3.png").resize((600, 600)),
                    Image.open(path+"\\imagenes\\logo4.png").resize((600, 600)),
                    Image.open(path+"\\imagenes\\logo5.png").resize((600, 600))]

        self.contP = 0
        self.contI = 0
        self.p = self.programadores[self.contP]

        self.ventana = root
        
        self.ventana.title("Ventana de inicio")
        self.P1 = tk.Frame(self.ventana, bg= "lightgray")
        self.P1.pack(side="left", padx=10, pady=5, fill="both", expand=True)
        
        
        #Bienvenida
        self.P3 = tk.Frame(self.P1)
        self.P3.pack(side="top", fill="both")
        self.desc = tk.Label(self.P3, text="Este programa se encarga de administrar una cadena de hoteles")
        self.saludo = tk.Label(self.P3, text="Bienvenido a\nCosmoReserve", font=("arial", 30))
        self.saludo.pack(padx=5, pady=5, anchor="center")
        
        #Menú
        barra_menu = Menu()
        archivo = Menu(barra_menu, tearoff=False)
        archivo.add_command(label="Descripción de la aplicación", command=descripcion)
        archivo.add_command(label="Salir", command=sys.exit)
        root.config(menu=barra_menu)
        barra_menu.add_cascade(menu=archivo, label="Archivo")
        
        
        self.P4 = tk.Frame(self.P1)
        self.P4.pack(side="bottom", fill="both")

        self.botones = tk.Frame(self.P4)
        self.botones.pack(side="bottom")


        self.boton1 = tk.Button(self.botones, text="Iniciar Sesión")
        self.boton1.pack(side="left", padx=7, pady=2)
        self.boton1.bind("<Button-1>", self.iniciar)

        self.boton2 = tk.Button(self.botones, text="Registrarse")
        self.boton2.pack(side="right", padx=7, pady=2)
        self.boton2.bind("<Button-1>", self.registrar)

        self.imagenes = tk.Label(self.P4)
        self.imagenes.bind("<Button-1>", self.cambiarImagen)
        imagen = ImageTk.PhotoImage(self.imagenesMGA[0])
        self.imagenes.config(image=imagen)
        self.imagenes.image = imagen 
        self.imagenes.pack(side="top")

        self.P2 = tk.Frame(self.ventana, bg= "lightgray")
        self.P2.pack(side="right", padx=10, pady=5, fill="both", expand=True)

        self.P5 = tk.Frame(self.P2)
        self.P5.pack(side="top", fill="x")

        self.bio = tk.Button(self.P5, text=f"{self.p.nombre}\nBiografia: {self.p.biografia}",
                             font=("arial", 9))
        self.bio.bind("<Button-1>", self.cambioProgramador)
        self.bio.pack(fill="both", anchor="center")
        self.bio.config(relief="flat")

        self.P6 = tk.Frame(self.P2)
        self.P6.pack(side="bottom", fill="both")

        imagen1 = ImageTk.PhotoImage(Image.open(self.p.fotos[0]).resize((300, 300)))
        self.imagen1 = tk.Label(self.P6, image=imagen1)
        self.imagen1.image = imagen1  # Guardar una referencia para evitar que se elimine la imagen
        self.imagen1.grid(row=0, column=0)

        imagen2 = ImageTk.PhotoImage(Image.open(self.p.fotos[1]).resize((300, 300)))
        self.imagen2 = tk.Label(self.P6, image=imagen2)
        self.imagen2.image = imagen2  # Guardar una referencia para evitar que se elimine la imagen
        self.imagen2.grid(row=0, column=1)

        imagen3 = ImageTk.PhotoImage(Image.open(self.p.fotos[2]).resize((300, 300)))
        self.imagen3 = tk.Label(self.P6, image=imagen3)
        self.imagen3.image = imagen3  # Guardar una referencia para evitar que se elimine la imagen
        self.imagen3.grid(row=1, column=0)

        imagen4 = ImageTk.PhotoImage(Image.open(self.p.fotos[3]).resize((300, 300)))
        self.imagen4 = tk.Label(self.P6, image=imagen4)
        self.imagen4.image = imagen4  # Guardar una referencia para evitar que se elimine la imagen
        self.imagen4.grid(row=1, column=1)

    
        
    def iniciar(self, event):
        self.ventana.cleanRoot()
        #Login.iniciar(self.ventana)

    def registrar(self, event):
        self.ventana.cleanRoot()
        Signup.iniciar(self.ventana)

    def cambiarImagen(self, event):
        self.contI = (self.contI + 1) % 5
        newImage = ImageTk.PhotoImage(self.imagenesMGA[self.contI])
        self.imagenes.config(image=newImage)
        self.imagenes.image = newImage 
        self.imagenes.pack(side="top")

    def cambioProgramador(self, event):
        self.contP = (self.contP + 1) % 4
        self.p = self.programadores[self.contP]
        self.bio.config(text=f"{self.p.nombre}\nBiografia: {self.p.biografia}")

        self.imagen1.destroy()
        self.imagen2.destroy()
        self.imagen3.destroy()
        self.imagen4.destroy()
        imagen1 = ImageTk.PhotoImage(Image.open(self.p.fotos[0]).resize((300, 300)))
        self.imagen1 = tk.Label(self.P6, image=imagen1)
        self.imagen1.image = imagen1  # Guardar una referencia para evitar que se elimine la imagen
        self.imagen1.grid(row=0, column=0)

        imagen2 = ImageTk.PhotoImage(Image.open(self.p.fotos[1]).resize((300, 300)))
        self.imagen2 = tk.Label(self.P6, image=imagen2)
        self.imagen2.image = imagen2  # Guardar una referencia para evitar que se elimine la imagen
        self.imagen2.grid(row=0, column=1)

        imagen3 = ImageTk.PhotoImage(Image.open(self.p.fotos[2]).resize((300, 300)))
        self.imagen3 = tk.Label(self.P6, image=imagen3)
        self.imagen3.image = imagen3  # Guardar una referencia para evitar que se elimine la imagen
        self.imagen3.grid(row=1, column=0)

        imagen4 = ImageTk.PhotoImage(Image.open(self.p.fotos[3]).resize((300, 300)))
        self.imagen4 = tk.Label(self.P6, image=imagen4)
        self.imagen4.image = imagen4  # Guardar una referencia para evitar que se elimine la imagen
        self.imagen4.grid(row=1, column=1)