from tkinter import *

def cambiarTexto():
    mensaje_cambiante.config(
        text="mensaje cambiado"
    )
def mensajeOriginal():
    mensaje_cambiante.config(
        text="texto original"
    )

ventana=Tk()
ventana.title("uso de botones")
ventana.geometry("800x600")

frame_principal=Frame(ventana)
frame_principal.config(
    bg="silver",
    width=800,
    height=50,
    border=2,
    relief=GROOVE
)
frame_principal.pack_propagate(False)
frame_principal.pack(pady=10)

lbl_titulo=Label(frame_principal,text="uso de botones")
lbl_titulo.config(
    bg="silver",
    width=20,
)
lbl_titulo.pack(pady=10)

mensaje_cambiante=Label(ventana,text="texto original")
mensaje_cambiante.pack()

#boton
boton_cambiar=Button(ventana,text="cambiar texto",command=cambiarTexto)
boton_cambiar.pack()

boton_original=Button(ventana,text="regresar a original",command=mensajeOriginal)
boton_original.pack()

ventana.mainloop()
