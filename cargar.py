from tkinter import filedialog

def cargar1():

    # Definimos los tipos de archivo permitidos
    tipos_archivo = [('Archivos', '*.roc')]
    # Abrimos el diálogo para seleccionar el archivo
    ruta_archivo = filedialog.askopenfilename(defaultextension='.roc', filetypes=tipos_archivo )
    
    # Verificamos si se seleccionó un archivo
    if ruta_archivo != '':
        
        # Abrimos el archivo y lo imprimimos en la consola
        with open(ruta_archivo, 'r') as archivo:
            cantidadAsignaturas = archivo.readline()
            asignaturas = []
            while True:
                asignaturas.append(archivo.readline())
                if len(asignaturas) == int(cantidadAsignaturas):
                    break

            cantidadEstudiantes = archivo.readline()
            estudiantes=[]
            estudiante = archivo.readline()
            p_est = estudiante.split(",")
            r_est = (int(p_est[0]),int(p_est[1]))
            
