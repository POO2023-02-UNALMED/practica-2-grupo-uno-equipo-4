import tkinter as tk
from tkinter import ttk
from baseDatos.Base import Base
from gestorGrafico.FieldFrame import FieldFrame

class Reservar():
    
    @classmethod
    def reservar(cls, huesped, root):
        
        def filtrar():
            if hFiltOptions.get() == hfiltros[0]:
                Base.filtrarPorNombre()
                ingreso = FieldFrame("Label", ["Nombre"], "Ingreso", ["str"])
                ingreso.setRoot(p2)
                ingreso.pack(pady=10)
                
            elif hFiltOptions.get() == hfiltros[1]:
                Base.filtrarPorCiudad()
            else:
                pass
        
        p1 = tk.Frame(root, bg="white")
        p1.pack(expand=True, fill="both")

        
        funcTitle = tk.Label(p1, text="Reservar", font=("Arial", 20), bg="lightgray")
        funcTitle.pack(pady=10)
        
        
        funcDesc = tk.Label(p1, text="Esta funcionalidad permite al huesped reservar una habitación en un hotel en concreto.", font=("Arial", 10),bg="lightgray")
        funcDesc.pack(pady=10)
        
        p2 = tk.Frame(p1, bg="white")
        p2.place(anchor="center", relheight=0.3, rely=0.5, relx=0.5)

        p2.rowconfigure(0, weight=1)
        p2.rowconfigure(1, weight=1)
        p2.columnconfigure(0, weight=1)
        p2.columnconfigure(1, weight=1)

        hfiltros = ["Buscar por nombre", "Buscar por ciudad", "Mostrar todos los hoteles"]
        hotelFilt = tk.Label(p2, text="Elija alguna de las siguientes opciones de filtrado")
        hotelFilt.grid(row=0, column=0, sticky="nsew")
        
        hFiltOptions = ttk.Combobox(p2, values=hfiltros, state="readonly")
        hFiltOptions.set("Filtros")
        hFiltOptions.grid(row=0, column=1, padx=10, sticky="nsew")
        
        filtconfirm = tk.Button(p2, text="Confirmar", command=filtrar)
        filtconfirm.grid(row=1, column=0, sticky="nsew")
        
        
        

        
        