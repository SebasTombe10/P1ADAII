from Cargar_archivo import cargar
from voraz import voraz
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text="Cargar datos", command=cargar ).grid(column=1, row=0)
ttk.Button(frm, text="Fuerza Bruta", command=root.destroy).grid(column=1, row=1)
ttk.Button(frm, text="Voraz", command=voraz).grid(column=1, row=2)
ttk.Button(frm, text="Dinamica", command=root.destroy).grid(column=1, row=3)
root.mainloop() 