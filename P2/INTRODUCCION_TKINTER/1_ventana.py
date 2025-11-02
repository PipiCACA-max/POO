"""
TKinter trabaja a traves de interfaces, es una biblioteca de Python que permite crear aplicaciones en python para escritorio
"""
#from tkinter import *
import tkinter as tk

#ventana=Tk()
ventana=tk.Tk()

ventana.title("Mi primera App Grafica en Tkinter")
ventana.geometry("800x600")
ventana.resizable(False,False)
ventana.mainloop() #Metodo que permite tener la ventana abierta e interactuar con ella