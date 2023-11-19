import sys
import tkinter as tk
from tkinter import messagebox
from gestorGrafico.Root import Root
#from PIL import Image, ImageTk
from tkinter import Menu
import os
import pathlib
from gestorGrafico.Programador import Programador
from gestorGrafico.Signup import Signup
from gestorGrafico.Login import Login
from gestorGrafico.Calificar import Calificar
from baseDatos.serializador import Serializador

path = os.path.join(pathlib.Path(__file__).parent.absolute())

#@autor: David Restrepo

class Inicio:
    def __init__(self, root:Root):
        def salir():
            Serializador.serializador()
            sys.exit()
        
        def descripcion():
            self.desc.pack(side="top", fill="both")
        
        david = Programador("David Restrepo Aguilar",
                            "Soy de la carrera de Ciencias de la Computación. Nací en medellín Colombia",
                            [path+"\\imagenes\\david1.png", path+"\\imagenes\\david2.png", 
                            path+"\\imagenes\\david3.png", path+"\\imagenes\\david4.png"])
        
        camilo = Programador("Yohan Camilo Sanchez Meza",
                            "Soy de la carrera de Ingeniería de Sistemas.",
                            [path+"\\imagenes\\Camilo1.png", path+"\\imagenes\\Camilo2.png", 
                            path+"\\imagenes\\Camilo3.png", path+"\\imagenes\\Camilo4.png"])
        
        alejandra = Programador("Alejandra Toro Grisales",
                            "Soy de la carrera de Ciencias de la Computación.",
                            [path+"\\imagenes\\Alejandra1.png", path+"\\imagenes\\Alejandra2.png", 
                            path+"\\imagenes\\Alejandra3.png", path+"\\imagenes\\Alejandra4.png"])
        
        pablo = Programador("Juan Pablo Rivera Alvarez",
                            "Soy de la carrera de Ciencias de la Computación.",
                            [path+"\\imagenes\\Pablo1.png", path+"\\imagenes\\Pablo2.png", 
                            path+"\\imagenes\\Pablo3.png", path+"\\imagenes\\Pablo4.png"])
        
        
        jhonDoe = Programador("Samuel Castaño Alfonso",
                            "Soy de la carrera de Ingeniería de Sistemas.",
                            [path+"\\imagenes\\JohnDoe1.png", path+"\\imagenes\\JohnDoe2.png", 
                            path+"\\imagenes\\JohnDoe3.png", path+"\\imagenes\\JohnDoe4.png"])

        self.programadores = [david, camilo, alejandra, pablo, jhonDoe]
        
        imagenp1 = tk.PhotoImage(file = path+"\\imagenes\\logo1.png")
        imagenp1 = imagenp1.subsample(x= 2, y = 1)
        imagenp2 = tk.PhotoImage(file = path+"\\imagenes\\logo2.png")
        imagenp2 = imagenp2.subsample(x= 2, y = 1)
        imagenp3 = tk.PhotoImage(file = path+"\\imagenes\\logo3.png")
        imagenp3 = imagenp3.subsample(x= 2, y = 1)
        imagenp4 = tk.PhotoImage(file = path+"\\imagenes\\logo4.png")
        imagenp4 = imagenp4.subsample(x= 4, y = 1)
        imagenp5 = tk.PhotoImage(file = path+"\\imagenes\\logo5.png")
        imagenp5 = imagenp5.subsample(x= 2, y = 1)
        self.imagenesMGA = [imagenp1, imagenp2, imagenp3, imagenp4, imagenp5]
        
        
        # self.imagenesMGA = [
        #             Image.open(path+"\\imagenes\\logo1.png").resize((600, 600)),
        #             Image.open(path+"\\imagenes\\logo2.png").resize((600, 600)),
        #             Image.open(path+"\\imagenes\\logo3.png").resize((600, 600)),
        #             Image.open(path+"\\imagenes\\logo4.png").resize((600, 600)),
        #             Image.open(path+"\\imagenes\\logo5.png").resize((600, 600))]

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
        archivo.add_command(label="Salir", command=salir)
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
        self.imagenes.bind("<Enter>", self.cambiarImagen)
        #imagen = tk.PhotoImage(self.imagenesMGA[0])
        self.imagenes.config(image=self.imagenesMGA[0])#corregir image
        self.imagenes.image = self.imagenesMGA[0] #corregir image
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

        #imagen1 = ImageTk.PhotoImage(Image.open(self.p.fotos[0]).resize((300, 300)))
        imagen1 = tk.PhotoImage(file = self.p.fotos[0])
        imagen1 = imagen1.subsample(x = 4, y=4)
        self.imagen1 = tk.Label(self.P6, image=imagen1)
        self.imagen1.image = imagen1  # Guardar una referencia para evitar que se elimine la imagen
        self.imagen1.grid(row=0, column=0)

        #imagen2 = ImageTk.PhotoImage(Image.open(self.p.fotos[1]).resize((300, 300)))
        imagen2 = tk.PhotoImage(file = (self.p.fotos[1]))
        imagen2 = imagen2.subsample(x = 2, y=3)
        self.imagen2 = tk.Label(self.P6, image=imagen2)
        self.imagen2.image = imagen2  # Guardar una referencia para evitar que se elimine la imagen
        self.imagen2.grid(row=0, column=1)

        #imagen3 = ImageTk.PhotoImage(Image.open(self.p.fotos[2]).resize((300, 300)))
        imagen3 = tk.PhotoImage(file = (self.p.fotos[2]))
        imagen3 = imagen3.subsample(x = 2, y=3)
        self.imagen3 = tk.Label(self.P6, image=imagen3)
        self.imagen3.image = imagen3  # Guardar una referencia para evitar que se elimine la imagen
        self.imagen3.grid(row=1, column=0)

        #imagen4 = ImageTk.PhotoImage(Image.open(self.p.fotos[3]).resize((300, 300)))
        imagen4 = tk.PhotoImage(file = (self.p.fotos[3]))
        imagen4 = imagen4.subsample(x = 2, y=3)
        self.imagen4 = tk.Label(self.P6, image=imagen4)
        self.imagen4.image = imagen4  # Guardar una referencia para evitar que se elimine la imagen
        self.imagen4.grid(row=1, column=1)

    
        
    def iniciar(self, event):
        self.ventana.cleanRoot()
        Login.login(self.ventana)
        #Calificar.seleccionar(self.ventana)

    def registrar(self, event):
        self.ventana.cleanRoot()
        Signup.iniciar(self.ventana)

    def cambiarImagen(self, event):
        self.contI = (self.contI + 1) % 5
        #newImage = tk.PhotoImage(self.imagenesMGA[self.contI])
        self.imagenes.config(image=self.imagenesMGA[self.contI]) # corregir a new Image
        self.imagenes.image = self.imagenesMGA[self.contI] #corregir a new image
        self.imagenes.pack(side="top")

    def cambioProgramador(self, event):
        self.contP = (self.contP + 1) % 5
        self.p = self.programadores[self.contP]
        self.bio.config(text=f"{self.p.nombre}\nBiografia: {self.p.biografia}")

        self.imagen1.destroy()
        self.imagen2.destroy()
        self.imagen3.destroy()
        self.imagen4.destroy()
        #imagen1 = ImageTk.PhotoImage(Image.open(self.p.fotos[0]).resize((300, 300)))
        imagen1 = tk.PhotoImage(file = self.p.fotos[0])
        imagen1 = imagen1.subsample(x = 2, y=3)
        self.imagen1 = tk.Label(self.P6, image=imagen1)
        self.imagen1.image = imagen1  # Guardar una referencia para evitar que se elimine la imagen
        self.imagen1.grid(row=0, column=0)

        #imagen2 = ImageTk.PhotoImage(Image.open(self.p.fotos[1]).resize((300, 300)))
        imagen2 = tk.PhotoImage(file = (self.p.fotos[1]))
        imagen2 = imagen2.subsample(x = 2, y=3)
        self.imagen2 = tk.Label(self.P6, image=imagen2)
        self.imagen2.image = imagen2  # Guardar una referencia para evitar que se elimine la imagen
        self.imagen2.grid(row=0, column=1)

        #imagen3 = ImageTk.PhotoImage(Image.open(self.p.fotos[2]).resize((300, 300)))
        imagen3 = tk.PhotoImage(file = (self.p.fotos[2]))
        imagen3 = imagen3.subsample(x = 2, y=3)
        self.imagen3 = tk.Label(self.P6, image=imagen3)
        self.imagen3.image = imagen3  # Guardar una referencia para evitar que se elimine la imagen
        self.imagen3.grid(row=1, column=0)

        #imagen4 = ImageTk.PhotoImage(Image.open(self.p.fotos[3]).resize((300, 300)))
        imagen4 = tk.PhotoImage(file = (self.p.fotos[3]))
        imagen4 = imagen4.subsample(x = 2, y=3)
        self.imagen4 = tk.Label(self.P6, image=imagen4)
        self.imagen4.image = imagen4  # Guardar una referencia para evitar que se elimine la imagen
        self.imagen4.grid(row=1, column=1)