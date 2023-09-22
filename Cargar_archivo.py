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
            archivo_dos = archivo.readlines()

            #Diccionario para almacenar las asignaturas y los estudiantes con sus peticiones
            materias = {}
            estudiantes = {}
            
            #Bucle para inicializar el diccionario de las asignaturas
            for i in range(1,(int(archivo_dos[0])+1)):
                materia = archivo_dos[i].split(',')
                materias[materia[0]] = materia[1]
                # print(archivo_dos[i])

            #Cantidad de estudiantes que solicitan materias
            cantEstudiantes = (archivo_dos[int(archivo_dos[0])+1])
            print(cantEstudiantes)
            
            #Contador de prueba
            cont=(int(archivo_dos[0])+2)
            cont_dos= cont
            print("contador: "+str(cont))
            print(type(cont))

            #Bucle para inicializar el diccinario de estudiantes 
            for j in archivo_dos[(int(archivo_dos[0])+2):]:
                estudiante = j.replace("\n", "").split(',')
                estudiantes[estudiante[0]] = estudiante[1]
                
                for k in range(cont+1, ((cont + int(estudiante[1]))+1)):
                    asignaturas = []
                    # asignaturas.append(archivo_dos[cont])
                    # print(archivo_dos[9])
                    cont += 1
                
                estudiantes[estudiante[0]] = asignaturas

            print(estudiantes)
                           

            
            # for line in archivo: 
                 
            