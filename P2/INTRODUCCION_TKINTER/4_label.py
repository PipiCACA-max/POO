from tkinter import *

ventana=Tk()
ventana.title("etiquetas")
ventana.geometry("800x600")

#etiquetas
etiqueta1=Label(ventana,text="hola soy una etiqueta")
etiqueta1.pack()
marco1=Frame(ventana,bg="#363333",width=200,height=100)
marco1.pack_propagate(False)
marco1.pack()
etiqueta2=Label(marco1,text="soy otra etiqueta dentro de un marco",bg="#363333")
etiqueta2.pack()

ventana.mainloop()
