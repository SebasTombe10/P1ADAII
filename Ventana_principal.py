from Cargar_archivo import cargar1
from cargar import cargar
from rocV import voraz
from dinamica import dinamica
from dinamica1 import dinamica1
from tkinter import *
from tkinter import ttk

# Variable para almacenar los resultados de capROC
resultados_capROC = None

def capROC():
    global resultados_capROC
    resultados_capROC = cargar()
def capVoraz():
    global resultados_capROC
    resVoraz = voraz(resultados_capROC)
    print(resVoraz)
    mostrar_resultados(resVoraz)
def capDinamica():
    memo_escogencias = {'definidos': {}, 'indefinidos': {}}
    resDinamica = dinamica1(resultados_capROC,memo_escogencias)
def mostrar_resultados(resultados):
    resultados_window = Toplevel(root)
    resultados_window.title("Resultados Voraz")
    resultados_tree = ttk.Treeview(resultados_window, columns=("Estudiantes", "Asignatura"))
    resultados_tree.heading("#1", text="Estudiantes")
    resultados_tree.heading("#2", text="Asignatura")
    # Insertar los datos en el Treeview
    
    for e, a in resultados.items():
        asignatura_str = ', '.join(a)
        resultados_tree.insert("", "end", values=(e,asignatura_str))
    
    resultados_tree.pack()
root = Tk()
root.title("ADA II")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text="Cargar datos", command=capROC ).grid(column=1, row=0)
ttk.Button(frm, text="Fuerza Bruta", command=cargar).grid(column=1, row=1)
ttk.Button(frm, text="Voraz", command=capVoraz).grid(column=1, row=2)
ttk.Button(frm, text="Dinamica", command=capDinamica).grid(column=1, row=3)

root.mainloop() 