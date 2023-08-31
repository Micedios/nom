import tkinter
from tkinter import ttk
import json

with open('errores.json','r') as archivo:
    datos = json.load(archivo)
def obtenerDesc():
    dato_ingresado =  entrada_texto.get()
    for error in datos['errores']:
        if error['codigo'] == dato_ingresado:
            desc_error.config(text=error['desc'])
            break
        else:
            print("dato erroneo")

ventana = tkinter.Tk()
ventana.title("titulooooo")

#titulo
titulo = ttk.Label(ventana,text="ponga el codigo", font="Papyrus")
titulo.pack(pady= 10, padx= 10)

entrada_texto = ttk.Entry(ventana, font="Papyrus")
entrada_texto.pack(pady=10, padx=10)

btn_buscar= ttk.Button(ventana, text= "enter", command=obtenerDesc)
btn_buscar.pack(pady=10, padx=10)

desc_error= ttk.Label(ventana, text= "", font="Papyrus")
desc_error.pack(pady=10, padx=10)

ventana.mainloop()