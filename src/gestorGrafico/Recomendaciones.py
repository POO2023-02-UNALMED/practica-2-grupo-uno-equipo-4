import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from baseDatos.Base import Base

class Recomendaciones():
    _ventanaElegirTipoRecomendacion = None
    _ventanaElegirCiudad = None
    _ventanaTipoRecomendacion = None
    _tiposHabitaciones = []
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
        labelTitulo = tk.Label(ventana,text="Recomendaciones",font=("arial", 30),fg="red")
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
        labelTitulo = tk.Label(ventana,text="Recomendaciones",font=("arial", 30),fg="red")
        labelTitulo.grid(row=0,column=2,columnspan=2,pady=20)
        labelSubtitulo = tk.Label(ventana,text="Elige la ciudad: ",font=("arial", 30))
        labelSubtitulo.grid(row=3,column=2,pady=20,padx=20,sticky="E")
        hoteles = Base.getHoteles()
        ciudades = []
        for hotel in hoteles:
            ciudad = hotel.getCiudad()
            if ciudad not in ciudades:
                ciudades.append(hotel.getCiudad())
        valorDefectoCiudad = tk.StringVar(value="Ciudad")
        combo = ttk.Combobox(ventana,values=ciudades,textvariable=valorDefectoCiudad,font=("arial", 30),state="readonly")
        combo.grid(row=3,column=3,sticky="w",pady=20)
        atras = tk.Button(ventana,text="Atras",font=("arial", 30),command=lambda:(Recomendaciones._ventanaElegirCiudad.destroy(),self.inicio()))
        atras.grid(row=4,column=2,pady=50)
        siguiente = tk.Button(ventana,text="Siguiente",font=("arial", 30),command=lambda:self._verificacionCiudad(combo.get(),ciudades,tipoRecomendacion))
        siguiente.grid(row=4,column=3,pady=50)
    
    def _verificacionCiudad(self,ciudad,ciudades,tipoRecomendacion):
        if ciudad not in ciudades:
            messagebox.showerror("Error","Elige una ciudad")
        else:
            self._tipoRecomendacion(tipoRecomendacion,ciudad)

    def _tipoRecomendacion(self,tipoRecomendacion,ciudad):
        Recomendaciones._ventanaElegirCiudad.destroy()
        recomendaciones = {}
        if(tipoRecomendacion=="Por preferencias"):
            recomendaciones = self._huesped.recomendacionHotelesPorSimilar(ciudad)
        else:
            recomendaciones = self._huesped.recomendacionHotelesPorHistorial(ciudad)
        Recomendaciones._ventanaTipoRecomendacion = tk.Tk() 
        ventana = Recomendaciones._ventanaTipoRecomendacion
        anchoPantalla = ventana.winfo_screenwidth()
        altoPantalla = ventana.winfo_screenheight()
        ventana.geometry(f'{anchoPantalla}x{altoPantalla}')
        ventana.geometry("+0+0")
        ventana.title("Recomendacion")
        ventana.grid_columnconfigure((0,1), minsize=80)
        labelTitulo = tk.Label(ventana,text="Recomendaciones",font=("arial", 30),fg="red")
        labelTitulo.grid(row=0,column=2,columnspan=2,pady=20)
        posiciones= 2
        for key,values in recomendaciones.items():
            labelHotel = tk.Label(ventana,text=key.getNombre(),font=("arial",30),fg="blue")
            labelHotel.grid(row=posiciones,column=1)
            posiciones +=1
            for value in values:
                labelHabitacion = tk.Label(ventana,text=value.getTipo(),font=("arial",30))
                labelHabitacion.grid(row=posiciones,column=2)
                posiciones+=1
        nuevaRecomendacion = tk.Button(ventana,text="Solicitar nueva recomendación",font=("arial", 30),command=lambda:(Recomendaciones._ventanaTipoRecomendacion.destroy(),self.inicio()))
        nuevaRecomendacion.grid(row=posiciones,column=2,pady=50)
        atras = tk.Button(ventana,text="Atrás",font=("arial", 30))
        atras.grid(row=posiciones,column=3,pady=50,padx=50)

    #Todo: a dónde devuelve?
    def agregarPreferencia(self):
        hoteles = Base.getHoteles()
        nombresHoteles = [hotel.getNombre() for hotel in hoteles]
        ciudades = [hotel.getCiudad() for hotel in hoteles]
        ventana = tk.Tk()
        anchoPantalla = ventana.winfo_screenwidth()
        altoPantalla = ventana.winfo_screenheight()
        ventana.geometry(f'{anchoPantalla}x{altoPantalla}')
        ventana.geometry("+0+0")
        ventana.title("Agregar Preferencia")
        ventana.grid_columnconfigure((0,1), minsize=80)
        labelTitulo = tk.Label(ventana,text="Agregar Preferencia",font=("arial", 30),fg="red")
        labelTitulo.grid(row=0,column=2,columnspan=2,pady=20)
        valorDefectoHotel = tk.StringVar(value="Hotel")
        labelHotel = tk.Label(ventana,text="Escoje un hotel:",font=("arial",30))
        labelHotel.grid(row=2,column=2)
        comboHoteles = ttk.Combobox(ventana,values=nombresHoteles,textvariable=valorDefectoHotel,font=("arial", 30),state="readonly")
        comboHoteles.grid(row=2,column=3,sticky="w",pady=20)
        valorDefectoCiudad = tk.StringVar(value="Ciudad")
        labelCiudad = tk.Label(ventana,text="Escoje un hotel:",font=("arial",30))
        labelCiudad.grid(row=3,column=2)
        comboCiudades = ttk.Combobox(ventana,values=ciudades,textvariable=valorDefectoCiudad,font=("arial", 30),state="readonly")
        comboCiudades.grid(row=3,column=3,sticky="w",pady=20)
        labelHabitacion = tk.Label(ventana,text="Escoje los o el tipo de habitación:",font=("arial",30))
        labelHabitacion.grid(row=4,column=2)
        valorCasillaSimple = tk.IntVar()
        checkboxSimple = tk.Checkbutton(ventana,text="Simple",font=("arial",30),variable=valorCasillaSimple,command=lambda:self._verificarCheckbox(valorCasillaSimple.get(),"simple"))
        checkboxSimple.grid(row=4,column=3)
        valorCasillaDoble = tk.IntVar()
        checkboxDoble = tk.Checkbutton(ventana,text="Doble",font=("arial",30),variable=valorCasillaDoble,command=lambda:self._verificarCheckbox(valorCasillaDoble.get(),"doble"))
        checkboxDoble.grid(row=5,column=3)
        valorCasillaFamiliar = tk.IntVar()
        checkboxFamiliar = tk.Checkbutton(ventana,text="Familiar",font=("arial",30),variable=valorCasillaFamiliar,command=lambda:self._verificarCheckbox(valorCasillaFamiliar.get(),"familiar"))
        checkboxFamiliar.grid(row=6,column=3)
        valorCasillaVipSimple = tk.IntVar()
        checkboxVipSimple = tk.Checkbutton(ventana,text="Vip simple",font=("arial",30),variable=valorCasillaVipSimple,command=lambda:self._verificarCheckbox(valorCasillaVipSimple.get(),"vipsimple"))
        checkboxVipSimple.grid(row=7,column=3)
        valorCasillaVipDoble = tk.IntVar()
        checkboxVipDoble = tk.Checkbutton(ventana,text="Vip doble",font=("arial",30),variable=valorCasillaVipDoble,command=lambda:self._verificarCheckbox(valorCasillaVipDoble.get(),"vipdoble"))
        checkboxVipDoble.grid(row=8,column=3)
        valorCasillaVipFamiliar = tk.IntVar()
        checkboxVipFamiliar = tk.Checkbutton(ventana,text="Vip familiar",font=("arial",30),variable=valorCasillaVipFamiliar,command=lambda:self._verificarCheckbox(valorCasillaVipFamiliar.get(),"vipfamiliar"))
        checkboxVipFamiliar.grid(row=9,column=3)
        nuevaRecomendacion = tk.Button(ventana,text="Agregar preferencia",font=("arial", 30),command=lambda:(self._enviarDatosPreferencia(nombresHoteles,comboHoteles.get(),ciudades,comboCiudades.get()),self._valorInicial(),comboCiudades.set("Ciudad"),comboHoteles.set("Hotel"),valorCasillaSimple.set(0),valorCasillaDoble.set(0),valorCasillaFamiliar.set(0),valorCasillaVipSimple.set(0),valorCasillaVipDoble.set(0),valorCasillaVipFamiliar.set(0)))
        nuevaRecomendacion.grid(row=10,column=2,pady=50)
        atras = tk.Button(ventana,text="Atrás",font=("arial", 30))
        atras.grid(row=10,column=3,pady=50,padx=50)
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


    def _valorInicial(self):
        Recomendaciones._tiposHabitaciones = []

    def _verificarCheckbox(self,valorCasilla,tipoHabitacion):
        if valorCasilla==1:
            Recomendaciones._tiposHabitaciones.append(tipoHabitacion)
        else:
            Recomendaciones._tiposHabitaciones.remove(tipoHabitacion)
        
            

        
        

    
        
        



