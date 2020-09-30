from tkinter import ttk 
from tkinter import *
import sqlite3

class Gastos:

    
    def __init__ (self, window):
        self.gastos = {"servicios":0, 
                        "viaticos":0,
                        "comida":0,
                        "ropa":0,
                        "otros":0}
        self.valor_servicios = 0
        self.valor_viaticos = 0
        self.valor_comida = 0
        self.valor_ropa = 0
        self.valor_otros = 0
        self.win = window
        self.win.title("Controlador de gastos")
        #creando un frame
        frame = LabelFrame(self.win, text = "Registra tu gasto")
        frame.grid( row = 0, column = 0, columnspan = 3, pady = 20)
        #dia input 
        dia = Label(frame, text = "Dia:")
        dia.grid(row = 1, column = 0)
        self.dia= Entry(frame )
        self.dia.focus()
        self.dia.grid(row =1 , column =1 )
        #mes input 
        mes = Label(frame, text = "Mes:")
        mes.grid(row = 2, column = 0)
        self.mes = Entry(frame )
        self.mes.focus()
        self.mes.grid(row =2 , column =1 )
        #año input 
        año = Label(frame, text = "Año:")
        año.grid(row = 3, column = 0)
        self.año = Entry(frame )
        self.año.focus()
        self.año.grid(row =3 , column =1 )
        #categoria input 
        categoria = Label(frame, text = "Categoria:")
        categoria.grid(row = 4, column = 0)
        self.categoria = Entry(frame )
        self.categoria.focus()
        self.categoria.grid(row =4 , column =1 )
        #valor input 
        valor = Label(frame, text = "Valor:")
        valor.grid(row = 5, column = 0)
        self.valor = Entry(frame )
        self.valor.focus()
        self.valor.grid(row =5 , column =1 )
        #Boton agregar 
        ttk.Button(frame, text = "Agregar", command= self.agregar).grid(row = 6, column = 0, columnspan = 3, sticky = W + E)
      


        #creando la tabla
        self.tree = ttk.Treeview(height = 5, columns = [f"#{n}" for n in range(1, 3)])
        self.tree.grid(row = 9, column = 0, columnspan = 2)
        self.tree.heading("#0", text = "Categoria", anchor = "center")
        self.tree.heading("#1", text = "Valor", anchor = "center")
        self.tree.heading("#2", text = "Porcentaje", anchor = "center")
      
    def agregar (self):
        categoria = self.categoria.get()
        valor = self.valor.get()
        if categoria == "servicios":
            self.valor_servicios += int(valor)
            self.gastos["servicios"] = self.valor_servicios
            
        if categoria == "viaticos":
            self.valor_viaticos += int(valor)
            self.gastos["viaticos"] = self.valor_viaticos
            
        if categoria == "ropa":
            self.valor_ropa += int(valor)
            self.gastos["ropa"] = self.valor_ropa
            
        if categoria == "comida":
            self.valor_comida += int(valor)
            self.gastos["comida"] = self.valor_comida
            
        if categoria == "otros":
            self.valor_otros += int(valor)
            self.gastos["otros"]= self.valor_otros
        
        self.vista()    
            

        
        

        
        
      
    
    def vista (self):
        #limpiando la tabla
        records= self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        #buscando los datos y procesandolos
        self.tree.insert("", 0, text = "servicios", value= (self.gastos["servicios"], (self.gastos["servicios"] * 100)/ (self.gastos["servicios"]+ self.gastos["viaticos"]+ self.gastos["otros"]+ self.gastos["comida"]+ self.gastos["ropa"])))
        self.tree.insert("", 0, text = "viaticos", value= (self.gastos["viaticos"], (self.gastos["viaticos"] * 100)/ (self.gastos["servicios"]+ self.gastos["viaticos"]+ self.gastos["otros"]+ self.gastos["comida"]+ self.gastos["ropa"])))
        self.tree.insert("", 0, text = "ropa", value= (self.gastos["ropa"], (self.gastos["ropa"] * 100)/ (self.gastos["servicios"]+ self.gastos["viaticos"]+ self.gastos["otros"]+ self.gastos["comida"]+ self.gastos["ropa"])))
        self.tree.insert("", 0, text = "comida", value= (self.gastos["comida"],(self.gastos["comida"] * 100)/ (self.gastos["servicios"]+ self.gastos["viaticos"]+ self.gastos["otros"]+ self.gastos["comida"]+ self.gastos["ropa"]) ))
        self.tree.insert("", 0, text = "otros", value= (self.gastos["otros"],(self.gastos["otros"] * 100)/ (self.gastos["servicios"]+ self.gastos["viaticos"]+ self.gastos["otros"]+ self.gastos["comida"]+ self.gastos["ropa"]) ))

        
        





if __name__ == "__main__":
    window = Tk()
    application = Gastos(window)
    window.mainloop()