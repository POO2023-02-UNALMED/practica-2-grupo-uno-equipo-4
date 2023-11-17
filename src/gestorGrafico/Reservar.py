import tkinter as tk
from tkinter import ttk
from baseDatos.Base import Base
from gestorGrafico.FieldFrame import FieldFrame

class Reservar():
    
    resultadoHotel = None
    enviarFiltroHotel = None
    selectedHotelFilter = None
    p2 = None
    resultados = None
    typestOptions = None
    
    @classmethod
    def reservar(cls, huesped, root):
        
        def seleccionar():
            hotelNom = cls.resultadoHotel.item(cls.resultadoHotel.selection(), "text")
            for i in Base.getHoteles():
                if i.getNombre() == hotelNom:
                    selectedHotel = i
            cls.chooseRoom(selectedHotel, huesped)
        
        def continuarFiltrado(valores):
            if cls.resultadoHotel != None:
                cls.resultadoHotel.destroy()
            
            if cls.enviarFiltroHotel != None:
                cls.enviarFiltroHotel.destroy()
                
            if cls.selectedHotelFilter == 0:
                hoteles = Base.filtrarPorNombre(valores)
            elif cls.selectedHotelFilter == 1:
                hoteles = Base.filtrarPorCiudad(valores)
            else:
                hoteles = []
                for i in Base.getHoteles():
                    hoteles.append(i)
                
                
            cls.resultadoHotel = ttk.Treeview(cls.p2, columns=("Ciudad", "Habitaciones", "Servicios"), selectmode='browse')
            cls.resultadoHotel.pack(pady=2)
            cls.resultadoHotel.heading("#0", text="Nombre")
            cls.resultadoHotel.heading("Ciudad", text="Ciudad")
            cls.resultadoHotel.heading("Habitaciones", text="Habitaciones Desocupadas")
            cls.resultadoHotel.heading("Servicios", text="Servicios")
                        
            if hoteles != None:
                for i in hoteles:
                    c = 0
                    habs = i.getHabitaciones()
                    for j in habs:
                        if not j.getReservada():
                            c += 1
                    cls.resultadoHotel.insert("", tk.END, text=i.getNombre(), values=(i.getCiudad(), c, ",".join(i.getServicios())))
                    cls.enviarFiltroHotel = tk.Button(cls.p2, text="Seleccionar", command=seleccionar)
                    cls.enviarFiltroHotel.pack(pady=2)
            
            

        
        def filtrar():
            if hFiltOptions.get() == hfiltros[0]:
                cls.selectedHotelFilter = 0
                for w in cls.p2.winfo_children() :
                    w.destroy()
                    
                ingreso = FieldFrame("Label", ["Nombre"], "Ingreso", ["Nombre"])
                ingreso.setRoot(cls.p2)
                ingreso.getFrame().pack(pady=10)
                ingreso.setFunc(continuarFiltrado)             
            
               
            elif hFiltOptions.get() == hfiltros[1]:
                cls.selectedHotelFilter = 1
                for w in cls.p2.winfo_children() :
                    w.destroy()
                    
                ingreso = FieldFrame("Label", ["Ciudad"], "Ingreso", ["Ciudad"])
                ingreso.setRoot(cls.p2)
                ingreso.getFrame().pack(pady=10)
                ingreso.setFunc(continuarFiltrado) 
            else:
                for w in cls.p2.winfo_children() :
                    w.destroy()
                    
                cls.selectedHotelFilter = 2
                continuarFiltrado(None)
                
        
        p1 = tk.Frame(root, bg="white")
        p1.pack(expand=True, fill="both")

        
        funcTitle = tk.Label(p1, text="Reservar", font=("Arial", 20), bg="lightgray")
        funcTitle.pack(pady=10)
        
        
        funcDesc = tk.Label(p1, text="Esta funcionalidad permite al huesped reservar una habitación en un hotel en concreto.", font=("Arial", 10),bg="lightgray")
        funcDesc.pack(pady=10)
        
        cls.p2 = tk.Frame(p1, bg="cyan")
        cls.p2.place(anchor="center", relheight=0.7, relwidth=0.8, rely=0.5, relx=0.5)

        cls.p2.rowconfigure(0, weight=1)
        cls.p2.rowconfigure(1, weight=1)
        cls.p2.columnconfigure(0, weight=1)
        cls.p2.columnconfigure(1, weight=1)

        hfiltros = ["Buscar por nombre", "Buscar por ciudad", "Mostrar todos los hoteles"]
        hotelFilt = tk.Label(cls.p2, text="Elija alguna de las siguientes opciones de filtrado")
        hotelFilt.grid(row=0, column=0, sticky="nsew")
        
        hFiltOptions = ttk.Combobox(cls.p2, values=hfiltros, state="readonly")
        hFiltOptions.set("Filtros")
        hFiltOptions.grid(row=0, column=1, padx=10, sticky="nsew")
        
        filtconfirm = tk.Button(cls.p2, text="Confirmar", command=filtrar)
        filtconfirm.grid(row=1, column=0, sticky="nsew")
        
        cls.resultados = tk.Text(p1, background="gray", fg="white", font=("Arial", 20))
        cls.resultados.place(anchor="s", rely=0.997, relx=0.5, relheight=0.1, relwidth=1) 
        
        
    @classmethod
    def chooseRoom(cls, hotel, huesped):
        
        def seleccionar():
            habId = cls.resultadoHotel.item(cls.resultadoHotel.selection(), "text")
            habitaciones = hotel.getHabitaciones()
            for i in habitaciones:
                if i.getId() == habId:
                    selectedRoom = i
            cls.realizarReserva(selectedRoom, huesped)
            
        
        def continuarFiltrado(valores):
            if cls.resultadoHotel != None:
                cls.resultadoHotel.destroy()
            
            if cls.enviarFiltroHotel != None:
                cls.enviarFiltroHotel.destroy()
                
            if cls.selectedHotelFilter == 0:
                habitaciones = Base.filtrarPorId(valores, hotel, huesped)
            elif cls.selectedHotelFilter == 1:
                tipo = cls.typestOptions.get()
                for w in cls.p2.winfo_children() :
                    w.destroy()
                habitaciones = Base.filtrarPorTipo(hotel, tipo)
            else:
                habitaciones = Base.sortRooms(hotel)
                
                
                
            cls.resultadoHotel = ttk.Treeview(cls.p2, columns=("Camas", "Tipo", "Precio", "Calificación", "Reservada"), selectmode='browse')
            cls.resultadoHotel.pack(pady=2)
            cls.resultadoHotel.heading("#0", text="Id")
            cls.resultadoHotel.heading("Tipo", text="Tipo")
            cls.resultadoHotel.heading("Camas", text="Camas")
            cls.resultadoHotel.heading("Precio", text="Precio")
            cls.resultadoHotel.heading("Calificación", text="Calificación")
            cls.resultadoHotel.heading("Reservada", text="Reservada")
            cls.resultadoHotel.column("Camas", width=100, anchor="center")
            cls.resultadoHotel.column("Tipo", width=100, anchor="center")
            cls.resultadoHotel.column("Precio", width=100, anchor="center")
            cls.resultadoHotel.column("Calificación", width=100, anchor="center")
            cls.resultadoHotel.column("Reservada", width=100, anchor="center")
                        
            if habitaciones != None:
                for i in habitaciones:
                    if "vip" in i.getTipo() and not huesped.isVip():
                        continue
                    
                    calHuesped = i.getCalificaciones()
                    calificaciones = list(calHuesped.values())
                    s = 0
                    for k in calificaciones:
                        s += k
                    
                    prom = s/len(calificaciones)

                    
                    cls.resultadoHotel.insert("", tk.END, text=i.getId(), values=(i.getTipo(), i.getNumeroCamas(), i.getPrecio(), prom,i.getReservada()))
                
                cls.enviarFiltroHotel = tk.Button(cls.p2, text="Seleccionar", command=seleccionar)
                cls.enviarFiltroHotel.pack(pady=2)
            
        
        def filtrar():
            def continuarTipo():
                continuarFiltrado(None)
            
            if hFiltOptions.get() == hfiltros[0]:
                cls.selectedHotelFilter = 0
                for w in cls.p2.winfo_children() :
                    w.destroy()
                    
                ingreso = FieldFrame("Label", ["Id"], "Ingreso", ["Id"])
                ingreso.setRoot(cls.p2)
                ingreso.getFrame().pack(pady=10)
                ingreso.setFunc(continuarFiltrado)             
            
               
            elif hFiltOptions.get() == hfiltros[1]:
                cls.selectedHotelFilter = 1
                for w in cls.p2.winfo_children() :
                    w.destroy()
                    
                hTypesVip = ["simple", "doble", "familiar", "simplevip", "doblevip", "familiarvip"]
                hTypes = ["simple", "doble", "familiar"]
                typesFilt = tk.Label(cls.p2, text="Elija alguno de los siguientes tipos de habitación")
                typesFilt.grid(row=0, column=0, sticky="nsew")
                
                if huesped.isVip():
                    cls.typestOptions = ttk.Combobox(cls.p2, values=hTypesVip, state="readonly")
                else:    
                    cls.typestOptions = ttk.Combobox(cls.p2, values=hTypes, state="readonly")
                cls.typestOptions.set("Tipos")
                cls.typestOptions.grid(row=0, column=1, padx=10, sticky="nsew")
                
                typeFiltconfirm = tk.Button(cls.p2, text="Confirmar", command=continuarTipo)
                typeFiltconfirm.grid(row=1, column=0, sticky="nsew")
                
            else:
                for w in cls.p2.winfo_children() :
                    w.destroy()
                    
                cls.selectedHotelFilter = 2
                continuarFiltrado(None)
        
        for w in cls.p2.winfo_children() :
            w.destroy()
            
        cls.resultados.insert(tk.END, f"Se ha seleccionado el hotel con nombre {hotel.getNombre()} y ciudad {hotel.getCiudad()}", "centrado")
        cls.resultados.tag_configure("centrado", justify="center")
        
        hfiltros = ["Buscar por id", "Buscar por tipo", "Mostrar todas las habitaciones"]
        hotelFilt = tk.Label(cls.p2, text="Elija alguna de las siguientes opciones de filtrado")
        hotelFilt.grid(row=0, column=0, sticky="nsew")
        
        hFiltOptions = ttk.Combobox(cls.p2, values=hfiltros, state="readonly")
        hFiltOptions.set("Filtros")
        hFiltOptions.grid(row=0, column=1, padx=10, sticky="nsew")
        
        filtconfirm = tk.Button(cls.p2, text="Confirmar", command=filtrar)
        filtconfirm.grid(row=1, column=0, sticky="nsew")
        
    
    @classmethod
    def realizarReserva(cls, habitacion, huesped):
        for w in cls.p2.winfo_children() :
            w.destroy()
            
        cls.resultados.delete("1.0", tk.END)            
        cls.resultados.insert(tk.END, f"Se ha seleccionado una habitación con Id {habitacion.getId()} y tipo {habitacion.getTipo()}", "centrado")
        cls.resultados.tag_configure("centrado", justify="center")
        
        titleReserva = tk.Label(cls.p2, text="Ingrese las fechas en las que se hospedará")
        titleReserva.pack(pady=10)
        
        # if habitacion.getReservada:
        #     criterios = ["Fecha de inicio actual", "Fecha de salida actual", ""]
        # else:
            
        # datesFrame = FieldFrame("Fechas", )
        