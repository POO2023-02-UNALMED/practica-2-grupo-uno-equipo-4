import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from baseDatos.Base import Base

class Recomendaciones():
    _ventanaElegirTipoRecomendacion = None
    _ventanaElegirCiudad = None
    _ventanaTipoRecomendacion = None
    def __init__(self,huesped):
        self._huesped = huesped
    def inicio(self):
        Recomendaciones._ventanaElegirTipoRecomendacion = tk.Tk()
        ventana = Recomendaciones._ventanaElegirTipoRecomendacion
        anchoPantalla = ventana.winfo_screenwidth()
        altoPantalla = ventana.winfo_screenheight()
        ventana.geometry(f'{anchoPantalla}x{altoPantalla}')
        ventana.geometry("+0+0")
        ventana.title("Tipo de recomendacion")
        ventana.grid_columnconfigure((0,1), minsize=80)
        labelTitulo = tk.Label(ventana,text="Recomendaciones",font=("arial", 30))
        labelSubtitulo = tk.Label(ventana,text="Elige el tipo de recomendación: ",font=("arial", 30))
        labelTitulo.grid(row=0,column=2,columnspan=2,pady=20)
        labelSubtitulo.grid(row=3,column=2,pady=20,padx=20,sticky="E")
        valorDefecto = tk.StringVar(value="Tipo")
        combo = ttk.Combobox(ventana,values=["Por preferencias","Por historial"],textvariable=valorDefecto,font=("arial", 30),state="readonly")
        combo.grid(row=3,column=3,sticky="w",pady=20)
        siguiente = tk.Button(ventana,text="Siguiente",command=lambda:self._verificacionTipoRecomendacion(combo.get()),font=("arial", 30))
        siguiente.grid(row=4,column=2,columnspan=2,pady=50)
        ventana.mainloop()

    def _verificacionTipoRecomendacion(self,valor):
        if(valor!="Por preferencias" and valor!="Por historial"):
            messagebox.showerror("Error","Elige una opción")
        else:
            self._elegirCiudad(valor)
            Recomendaciones._ventanaElegirTipoRecomendacion.destroy()
        
    def _elegirCiudad(self,tipoRecomendacion):
        Recomendaciones._ventanaElegirCiudad = tk.Tk()
        ventana = Recomendaciones._ventanaElegirCiudad
        anchoPantalla = ventana.winfo_screenwidth()
        altoPantalla = ventana.winfo_screenheight()
        ventana.geometry(f'{anchoPantalla}x{altoPantalla}')
        ventana.geometry("+0+0")
        ventana.title("Elegir Ciudad")
        ventana.grid_columnconfigure((0,1), minsize=80)
        labelTitulo = tk.Label(ventana,text="Recomendaciones",font=("arial", 30))
        labelTitulo.grid(row=0,column=2,columnspan=2,pady=20)
        labelSubtitulo = tk.Label(ventana,text="Elige la ciudad: ",font=("arial", 30))
        labelSubtitulo.grid(row=3,column=2,pady=20,padx=20,sticky="E")
        valorDefecto = tk.StringVar(value="Ciudad")
        hoteles = Base.getHoteles()
        ciudades = []
        for hotel in hoteles:
            ciudades.append(hotel.getCiudad())
        combo = ttk.Combobox(ventana,values=ciudades,textvariable=valorDefecto,font=("arial", 30),state="readonly")
        combo.grid(row=3,column=3,sticky="w",pady=20)
        atras = tk.Button(ventana,text="Atras",font=("arial", 30),command=lambda:(Recomendaciones._ventanaElegirCiudad.destroy(),self.inicio()))
        atras.grid(row=4,column=2,pady=50)
        siguiente = tk.Button(ventana,text="Siguiente",font=("arial", 30),command=lambda:self._tipoRecomendacion(tipoRecomendacion))
        siguiente.grid(row=4,column=3,pady=50)
    
    #TODO:Hacer cuadricula con los hoteles que permita ingresar a ver las habitaciones
    def _tipoRecomendacion(self,tipoRecomendacion):
        Recomendaciones._ventanaElegirCiudad.destroy()
        recomendaciones = {}
        if(tipoRecomendacion=="Por preferencias"):
            recomendaciones = self._huesped.recomendacionHotelesPorSimilar()
        else:
            recomendaciones = self._huesped.recomendacionHotelesPorHistorial()
        Recomendaciones._ventanaTipoRecomendacion = tk.Tk() 
        ventana = Recomendaciones._ventanaTipoRecomendacion
        anchoPantalla = ventana.winfo_screenwidth()
        altoPantalla = ventana.winfo_screenheight()
        ventana.geometry(f'{anchoPantalla}x{altoPantalla}')
        ventana.geometry("+0+0")
        ventana.title("Recomendacion")
        ventana.grid_columnconfigure((0,1), minsize=80)
        labelTitulo = tk.Label(ventana,text="Recomendaciones",font=("arial", 30))
        labelTitulo.grid(row=0,column=2,columnspan=2,pady=20)

        
        

    
        
        



