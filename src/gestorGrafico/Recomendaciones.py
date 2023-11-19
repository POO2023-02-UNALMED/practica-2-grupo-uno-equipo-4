import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from baseDatos.Base import Base
from tkinter import Menu
from gestorGrafico.Usmenu import Usmenu

class Recomendaciones():
    _ventanaElegirCiudad = None
    _ventanaTipoRecomendacion = None
    _tiposHabitaciones = []

    def __init__(self,huesped,root):
        self._huesped = huesped
        self._root = root

    def _ciudades(self,hoteles):
        ciudades = []
        for hotel in hoteles:
            if hotel.getCiudad() not in ciudades:
                ciudades.append(hotel.getCiudad())
        return ciudades
    
    def _hoteles(self,hoteles):
        nombresHoteles = []
        for hotel in hoteles:
            if hotel.getNombre() not in nombresHoteles:
                nombresHoteles.append(hotel.getNombre())
        return nombresHoteles
   

    
    def inicio(self):
        ventana = self._root
        ventana.title("Tipo de recomendacion")
        framePrincipal = tk.Frame(ventana,bg="white")
        framePrincipal.pack(fill=tk.BOTH, expand=True)
        framePrincipal.grid_columnconfigure((0,1), minsize=80)

        labelTitulo = tk.Label(framePrincipal,text="Recomendaciones",font=("Arial", 20), bg="lightgray")
        labelExplicacion = tk.Label(framePrincipal,text="El sistema de recomendaciones permite basado en el tipo que se eliga y la ciudad,proporcionarle al huesped algunos posibles hoteles y habitaciones donde se podría hospedar. Para generar estas recomendaciones se tiene en cuenta el historial de previas reservaciones y/o las preferencias que anteriormente ha agregado a su cuenta como huesped. ",font=("arial", 10),wraplength=ventana.winfo_screenwidth() - 50)
        labelSubtitulo = tk.Label(framePrincipal,text="Elige el tipo de recomendación: ",font=("arial", 10))

        labelTitulo.pack(expand=True)
        labelTitulo.place(relx=0.5, rely=0.06, anchor="center") 
        labelExplicacion.pack(expand=True)
        labelExplicacion.place(relx=0.5,rely=0.13,anchor="center")
        labelSubtitulo.pack(expand=True)
        labelSubtitulo.place(relx=0.4,rely=0.18,anchor="center")

        valorDefecto = tk.StringVar(value="Tipo")
        combo = ttk.Combobox(framePrincipal,values=["Por preferencias","Por historial"],textvariable=valorDefecto,font=("arial", 10),state="readonly")
        combo.pack(expand=True)
        combo.place(relx=0.55,rely=0.18,anchor="center")
        siguiente = tk.Button(framePrincipal,text="Siguiente",command=lambda:self._verificacionTipoRecomendacion(combo.get(),ventana),font=("arial", 10))
        siguiente.pack(expand=True)
        siguiente.place(relx=0.5,rely=0.3,anchor="center")
        ventana.mainloop()

    def _verificacionTipoRecomendacion(self,valor,ventana):
        if(valor!="Por preferencias" and valor!="Por historial"):
            messagebox.showerror("Error","Elige una opción")
        else:
            self._elegirCiudad(valor,ventana)
        
    def _elegirCiudad(self,tipoRecomendacion,ventana):
        ventana.cleanRoot()
        Usmenu.menu(ventana,self._huesped)
        ventana.title("Elegir Ciudad")
        framePrincipal = tk.Frame(ventana,bg="white")
        framePrincipal.pack(fill=tk.BOTH, expand=True)
        framePrincipal.grid_columnconfigure((0,1), minsize=80)
        labelTitulo = tk.Label(framePrincipal,text="Recomendaciones",font=("Arial", 20), bg="lightgray")
        labelTitulo.pack(expand=True)
        labelTitulo.place(relx=0.5, rely=0.06, anchor="center") 
        labelSubtitulo = tk.Label(framePrincipal,text="Elige la ciudad: ",font=("arial", 10))
        labelSubtitulo.pack(expand=True)
        labelSubtitulo.place(relx=0.45,rely=0.18,anchor="center")
        hoteles = Base.getHoteles()
        ciudades = self._ciudades(hoteles)
        valorDefectoCiudad = tk.StringVar(value="Ciudad")
        combo = ttk.Combobox(framePrincipal,values=ciudades,textvariable=valorDefectoCiudad,font=("arial", 10),state="readonly")
        combo.pack(expand=True)
        combo.place(relx=0.55,rely=0.18,anchor="center")
        atras = tk.Button(framePrincipal,text="Atras",font=("arial", 10),command=lambda:(Recomendaciones._ventanaElegirCiudad.destroy(),self.inicio()))
        atras.pack(expand=True)
        atras.place(relx=0.45,rely=0.3,anchor="center")
        siguiente = tk.Button(framePrincipal,text="Siguiente",font=("arial", 10),command=lambda:self._verificacionCiudad(combo.get(),ciudades,tipoRecomendacion,ventana))
        siguiente.pack(expand=True)
        siguiente.place(relx=0.55,rely=0.3,anchor="center")
        ventana.mainloop()
    
    def _verificacionCiudad(self,ciudad,ciudades,tipoRecomendacion,ventana):
        if ciudad not in ciudades:
            messagebox.showerror("Error","Elige una ciudad")
        else:
            self._tipoRecomendacion(tipoRecomendacion,ciudad,ventana)

    def _tipoRecomendacion(self,tipoRecomendacion,ciudad,ventana):
        ventana.cleanRoot()
        Usmenu.menu(ventana,self._huesped)
        recomendaciones = {}
        if(tipoRecomendacion=="Por preferencias"):
            recomendaciones = self._huesped.recomendacionHotelesPorSimilar(ciudad)
        else:
            recomendaciones = self._huesped.recomendacionHotelesPorHistorial(ciudad)
        ventana.title("Recomendacion")
        framePrincipal = tk.Frame(ventana,bg="white")
        framePrincipal.pack(fill=tk.BOTH, expand=True)
        framePrincipal.grid_columnconfigure((0,1), minsize=80)
        labelTitulo = tk.Label(framePrincipal,text="Recomendaciones",font=("Arial", 20), bg="lightgray")
        labelTitulo.grid(row=2,column=2,columnspan=4,pady=20)
        posiciones= 4
        if self._verificarRecomendaciones(recomendaciones):
            for key,values in recomendaciones.items():
                labelHotel = tk.Label(framePrincipal,text=key.getNombre(),font=("arial",10),fg="blue")
                labelHotel.grid(row=posiciones,column=2)
                posiciones +=1
                for value in values:
                    labelHabitacion = tk.Label(framePrincipal,text=value.getTipo(),font=("arial",10))
                    labelHabitacion.grid(row=posiciones,column=3)
                    posiciones+=1
        else:
            labelError = tk.Label(framePrincipal,text="No hay recomendaciones basadas en el tipo escogido",font=("arial",10),fg="red")
            labelError.grid(row=posiciones,column=2)
            posiciones+=1
        ventana.mainloop()

    def _verificarRecomendaciones(self,recomendaciones):
        return recomendaciones!={}

    #Todo: a dónde devuelve?
    def agregarPreferencia(self):
        hoteles = Base.getHoteles()
        nombresHoteles = self._hoteles(hoteles)
        ciudades = self._ciudades(hoteles)
        ventana = self._root
        ventana.title("Agregar Preferencia")
        ventana.state("zoomed")
        framePrincipal = tk.Frame(ventana,bg="white")
        framePrincipal.pack(fill=tk.BOTH, expand=True)
        framePrincipal.grid_columnconfigure((0,1), minsize=80)
        labelTitulo = tk.Label(framePrincipal,text="Agregar Preferencia",font=("Arial", 20), bg="lightgray")
        labelTitulo.pack(expand=True)
        labelTitulo.place(relx=0.5, rely=0.06, anchor="center") 
        valorDefectoHotel = tk.StringVar(value="Hotel")
        labelHotel = tk.Label(framePrincipal,text="Escoje un hotel:",font=("arial",10))
        labelHotel.pack(expand=True)
        labelHotel.place(relx=0.4,rely=0.18,anchor="center")
        comboHoteles = ttk.Combobox(framePrincipal,values=nombresHoteles,textvariable=valorDefectoHotel,font=("arial", 10),state="readonly")
        comboHoteles.pack(expand=True)
        comboHoteles.place(relx=0.55,rely=0.18,anchor="center")
        valorDefectoCiudad = tk.StringVar(value="Ciudad")
        labelCiudad = tk.Label(framePrincipal,text="Escoje un hotel:",font=("arial",10))
        labelCiudad.pack(expand=True)
        labelCiudad.place(relx=0.4,rely=0.25,anchor="center")
        comboCiudades = ttk.Combobox(framePrincipal,values=ciudades,textvariable=valorDefectoCiudad,font=("arial", 10),state="readonly")
        comboCiudades.pack(expand=True)
        comboCiudades.place(relx=0.55,rely=0.25,anchor="center")
        labelHabitacion = tk.Label(framePrincipal,text="Escoje los o el tipo de habitación:",font=("arial",10))
        labelHabitacion.pack(expand=True)
        labelHabitacion.place(relx=0.4,rely=0.32,anchor="center")
        valorCasillaSimple = tk.IntVar()
        checkboxSimple = tk.Checkbutton(framePrincipal,text="Simple",font=("arial",10),variable=valorCasillaSimple,command=lambda:self._verificarCheckbox(valorCasillaSimple.get(),"simple"))
        checkboxSimple.pack(expand=True)
        checkboxSimple.place(relx=0.55,rely=0.32,anchor="center")
        valorCasillaDoble = tk.IntVar()
        checkboxDoble = tk.Checkbutton(framePrincipal,text="Doble",font=("arial",10),variable=valorCasillaDoble,command=lambda:self._verificarCheckbox(valorCasillaDoble.get(),"doble"))
        checkboxDoble.pack(expand=True)
        checkboxDoble.place(relx=0.55,rely=0.35,anchor="center")
        valorCasillaFamiliar = tk.IntVar()
        checkboxFamiliar = tk.Checkbutton(framePrincipal,text="Familiar",font=("arial",10),variable=valorCasillaFamiliar,command=lambda:self._verificarCheckbox(valorCasillaFamiliar.get(),"familiar"))
        checkboxFamiliar.pack(expand=True)
        checkboxFamiliar.place(relx=0.55,rely=0.38,anchor="center")
        valorCasillaVipSimple = tk.IntVar()
        checkboxVipSimple = tk.Checkbutton(framePrincipal,text="Vip simple",font=("arial",10),variable=valorCasillaVipSimple,command=lambda:self._verificarCheckbox(valorCasillaVipSimple.get(),"vipsimple"))
        checkboxVipSimple.pack(expand=True)
        checkboxVipSimple.place(relx=0.55,rely=0.41,anchor="center")
        valorCasillaVipDoble = tk.IntVar()
        checkboxVipDoble = tk.Checkbutton(framePrincipal,text="Vip doble",font=("arial",10),variable=valorCasillaVipDoble,command=lambda:self._verificarCheckbox(valorCasillaVipDoble.get(),"vipdoble"))
        checkboxVipDoble.pack(expand=True)
        checkboxVipDoble.place(relx=0.55,rely=0.44,anchor="center")
        valorCasillaVipFamiliar = tk.IntVar()
        checkboxVipFamiliar = tk.Checkbutton(framePrincipal,text="Vip familiar",font=("arial",10),variable=valorCasillaVipFamiliar,command=lambda:self._verificarCheckbox(valorCasillaVipFamiliar.get(),"vipfamiliar"))
        checkboxVipFamiliar.pack(expand=True)
        checkboxVipFamiliar.place(relx=0.55,rely=0.47,anchor="center")
        agregarPreferencia = tk.Button(framePrincipal,text="Agregar preferencia",font=("arial", 10),command=lambda:(self._enviarDatosPreferencia(nombresHoteles,comboHoteles.get(),ciudades,comboCiudades.get()),self._valorInicial(),comboCiudades.set("Ciudad"),comboHoteles.set("Hotel"),valorCasillaSimple.set(0),valorCasillaDoble.set(0),valorCasillaFamiliar.set(0),valorCasillaVipSimple.set(0),valorCasillaVipDoble.set(0),valorCasillaVipFamiliar.set(0)))
        agregarPreferencia.pack(expand=True)
        agregarPreferencia.place(relx=0.5,rely=0.55,anchor="center")
        ventana.mainloop()

    def _enviarDatosPreferencia(self,hoteles,hotel,ciudades,ciudad):
        verificacion = True
        if hotel not in hoteles:
            messagebox.showerror("Error","Elige un hotel")
            verificacion = False
        if ciudad not in ciudades:
            messagebox.showerror("Error","Elige una ciudad")
            verificacion = False
        if Recomendaciones._tiposHabitaciones==[]:
            messagebox.showerror("Error","Elige al menos un tipo de habitación")
            verificacion = False
        
        if verificacion:
            self._huesped.agregarPreferencias(ciudad,hotel,Recomendaciones._tiposHabitaciones)
            messagebox.showinfo("Info","Preferencia agregada")


    def _valorInicial(self):
        Recomendaciones._tiposHabitaciones = []

    def _verificarCheckbox(self,valorCasilla,tipoHabitacion):
        if valorCasilla==1:
            Recomendaciones._tiposHabitaciones.append(tipoHabitacion)
        else:
            Recomendaciones._tiposHabitaciones.remove(tipoHabitacion)
        
            

        
        

    
        
        



