"""
1.- Implementar el MVC
2.- Paradigma POO
3.- App de escritorio con interfaz gráfica

4 DICIEMBRE:
    1)Controlador:
        1.1 insertar_camionetas()
        1.2 consultar_camionetas()
        1.3 cambiar_camionetas()
        1.4 borrar_camionetas()
    
    Productos entregables:
        **Interacción con la funcionalidad (controlador) de las interfaces anteriores
        **Nombre del commit: "commit_04_12_25"

5 DICIEMBRE:
    1)Controlador:
        1.1 insertar_camiones()
        1.2 consultar_camiones()
        1.3 cambiar_camiones()
        1.4 borrar_camiones()
    
    Productos entregables:
        **Interacción con la funcionalidad (controlador) de las interfaces anteriores
        **Nombre del commit: "commit_05_12_25"

"""
from tkinter import *
from view import view1

class App:
    def __init__(self,ventana):
        vista=view1.View(ventana)
    
if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()
    
