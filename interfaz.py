import tkinter
from tkinter import ttk

ventana = tkinter.Tk()
ventana.title("sasayat¿a s")

#titulo
titulo = ttk.Label(ventana,text="ponga el codigo", font="Papyrus")
titulo.pack(pady= 10, padx= 10)

entrada_texto = ttk.Entry(ventana, font="Papyrus")
entrada_texto.pack(pady=10, padx=10)

btn_buscar= ttk.Button(ventana, text= "enter")
btn_buscar.pack(pady=10, padx=10)

desc_error= ttk.Label(ventana, text= "error", font="Papyrus")
desc_error.pack(pady=10, padx=10)

ventana.mainloop()