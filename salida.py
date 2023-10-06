def salida(data):
    # Nombre del archivo de salida
    archivo_salida = "output.txt"

    # Abre el archivo para escribir
    with open(archivo_salida, "w") as archivo:
        insa = data['Insatisfaccion']
        archivo.write(f"{str(insa[0])}\n")
        data.popitem()
        # Itera a través de las claves y valores del diccionario
        for estudiante, asignaturas in data.items():
            # Escribe el código del estudiante
            archivo.write(f"{estudiante},")
            
            # Escribe la cantidad de asignaturas
            archivo.write(f"{len(asignaturas)}\n")
            
            # Itera a través de las asignaturas
            for asignatura in asignaturas:
                archivo.write(f"{asignatura}\n")
