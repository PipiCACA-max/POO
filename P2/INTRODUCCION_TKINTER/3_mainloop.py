from tkinter import *

ventana = Tk()

ventana.title("mainloop")
ventana.geometry("800x600")
ventana.resizable(False,False)

marco = Frame(ventana)
marco.config(
    width=600,
    height=400,
    bg="#0AE5F0",
    bd=10,
    border=2,
    relief=RAISED
)
marco.pack(
    pady=100,
    padx=100
    )

ventana.mainloop()