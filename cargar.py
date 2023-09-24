from tkinter import filedialog

def cargar():

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
                asigPrincipal = archivo.readline().strip()
                p_asigP = asigPrincipal.split(",")
                r_asigP = (p_asigP[0],p_asigP[1])
                asignaturas.append(r_asigP)
                if len(asignaturas) == int(cantidadAsignaturas):
                    break
            dicAsignaturas = dict(asignaturas)
            cantidadEstudiantes = archivo.readline()
            cs = int(cantidadEstudiantes)
            estudiantes={}
            while True:
                estudiante = archivo.readline()
                p_est = estudiante.split(",")
                r_est = (int(p_est[0]),int(p_est[1]))
                asignaturasSolicitadas = r_est[1]
                codEstudiante = r_est[0]
                listAsignaturas=[]
                while True:
                    asignatura = archivo.readline()
                    p_asig = asignatura.split(",")
                    r_asig = (int(p_asig[0]),int(p_asig[1]))
                    listAsignaturas.append(r_asig)
                    asignaturasSolicitadas = asignaturasSolicitadas-1
                    if asignaturasSolicitadas == 0: break
                estudiantes[codEstudiante] = listAsignaturas
                cs=cs-1
                if cs == 0: break
            print(dicAsignaturas)
            print(estudiantes)
            
