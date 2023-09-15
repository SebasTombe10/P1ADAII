from tkinter import filedialog

def cargar():

    # Definimos los tipos de archivo permitidos
    tipos_archivo = [('Archivos', '*.txt')]
    # Abrimos el diálogo para seleccionar el archivo
    ruta_archivo = filedialog.askopenfilename(defaultextension='.txt', filetypes=tipos_archivo )
    
    # Verificamos si se seleccionó un archivo
    if ruta_archivo != '':
        
        # Abrimos el archivo y lo imprimimos en la consola
        with open(ruta_archivo, 'r') as archivo:
            print(archivo)
            