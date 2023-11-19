from abc import ABC, abstractclassmethod
import tkinter as tk
from tkinter import messagebox

from errores.ErrorValores import ErrorValores

#@autor: David Restrepo
class Base(ABC):
    _administradores = []
    _hoteles = []
    _huespedes = []
    _empleados = []

    @classmethod
    def setAdministradores(cls, administradores):
        cls._administradores = administradores

    @classmethod
    def getAdministradores(cls):
        return cls._administradores

    @classmethod
    def addAdministradores(cls, administrador):
        cls._administradores.append(administrador)

    @classmethod
    def setHoteles(cls, hoteles):
        cls._hoteles = hoteles

    @classmethod
    def getHoteles(cls):
        return cls._hoteles

    @classmethod
    def addHoteles(cls, hotel):
        cls._hoteles.append(hotel)

    @classmethod
    def getHuespedes(cls):
        return cls._huespedes

    @classmethod
    def setHuespedes(cls, huespedes):
        cls._huespedes = huespedes

    @classmethod
    def addHuespedes(cls, huesped):
        cls._huespedes.append(huesped)

    @classmethod
    def getEmpleados(cls):
        return cls._empleados

    @classmethod
    def setEmpleados(cls, empleados):
        cls._empleados = empleados

    @classmethod
    def addEmpleados(cls, empleado):
        cls._empleados.append(empleado)
        
    @classmethod
    def filtrarPorNombre(cls, nombre, resultados):
        foundHotel = False
        nom = nombre[0]
        for hotel in cls._hoteles:
            if nom == hotel.getNombre():
                hotelNombre = hotel
                foundHotel = True
        if foundHotel:
            hotels = [hotelNombre]
            resultados.delete("1.0", tk.END)
            return hotels
        else:
            resultados.delete("1.0", tk.END)            
            resultados.insert(tk.END, "El nombre del hotel que ingresó no se encuentra en la base de datos, intente de nuevo", "centrado")
            resultados.tag_configure("centrado", justify="center")
            print("El nombre del hotel que ingresó no se encuentra en la base de datos, intente de nuevo: ", end="")
            return None
            
        
        
                
    @classmethod
    def filtrarPorCiudad(cls, ciudad, resultados):
        
        print(ciudad)
        foundHotel = False
        ciu = ciudad[0]
        hotels = []
        for hotel in cls._hoteles:
            if ciu == hotel.getCiudad():
                hotelNombre = hotel
                hotels.append(hotelNombre)
                foundHotel = True
        if foundHotel:
            resultados.delete("1.0", tk.END)  
            return hotels
        else:
            resultados.delete("1.0", tk.END)            
            resultados.insert(tk.END, "La ciudad del hotel que ingresó no se encuentra en la base de datos, intente de nuevo", "centrado")
            resultados.tag_configure("centrado", justify="center")
            print("La ciudad del hotel que ingresó no se encuentra en la base de datos, intente de nuevo: ", end="")
            return None
        
    
    @classmethod
    def filtrarPorId(cls, identificacion, hotel, huesped, resultados):
        foundHotel = False
        id = identificacion[0]
        habitaciones = hotel.getHabitaciones()
        try:
            id = int(id)
            for hab in habitaciones:
                if int(id) == hab.getId():
                    tipoHab = hab.getTipo()
                    if "vip" in tipoHab and not huesped.isVip():
                        print("No puede acceder a esta habitación, pues no es VIP")
                        foundHotel = False
                    else:    
                        habitacion = hab
                        foundHotel = True
            if foundHotel:
                habs = [habitacion]
                resultados.delete("1.0", tk.END)    
                return habs
            else:
                resultados.delete("1.0", tk.END)            
                resultados.insert(tk.END, "El Id que ingresó no se encuentra en la base de datos, intente de nuevo", "centrado")
                resultados.tag_configure("centrado", justify="center")
                print("El Id que ingresó no se encuentra en la base de datos, intente de nuevo: ", end="")
                return None
        except ValueError:
            print("Error: No se pudo convertir el string a entero")
            er = ErrorValores("Id", "Entero")
            text = er.mostrarMensaje()
            messagebox.showerror("Error", text)    
        
        
    @classmethod
    def filtrarPorTipo(cls, hotel, tipo):
        sortedRooms = cls.sortRooms(hotel)
        habs = []
        for i in sortedRooms:
            if i.getTipo() == tipo:
                habs.append(i)
        return habs
        
    @classmethod
    def sortRooms(cls, hotel):
        
        promHab = {}
        habitaciones = hotel.getHabitaciones()
        
        for j in habitaciones:
            dicCalificaciones = j.getCalificaciones()
            calificaciones = list(dicCalificaciones.values())
            
            s = 0
            for k in calificaciones:
                s += k
            
            prom = s/len(calificaciones)
            promHab[j] = prom
        
        sortedPromHab = dict(sorted(promHab.items(), key=lambda item:item[1], reverse=True))
        sortedRooms = list(sortedPromHab.keys())
        return sortedRooms
                        
                    
                        
                    
                    

                
                    