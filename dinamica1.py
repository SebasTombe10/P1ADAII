from cod_keys import cod_keys

def dinamica1(diccionario,memo):
    codigos_keys = cod_keys(diccionario)
    asignaturas,estudiantes = diccionario
    for asignatura_indi in asignaturas.items():
        if(diccionario[0][asignatura_indi[0]] == 1):
            clave = ','.join(memo['indefinidos'].keys())
            clave_definidos = ','.join(memo['definidos'].keys())
            if (asignatura_indi[0] not in clave and asignatura_indi[0] not in clave_definidos):
                # Primero, encontramos el valor máximo en el segundo elemento de todas las tuplas
                maximo_valor = max(codigos_keys[asignatura_indi[0]], key=lambda x: x[1])[1]
                # Luego, construimos una lista de todas las tuplas que tienen ese valor máximo
                tuplas_maximas = [tupla for tupla in codigos_keys[asignatura_indi[0]] if tupla[1] == maximo_valor]
                #Si el tamaño es 1 pasamos el que tenga mas prioridad a definidos
                if (len(tuplas_maximas) == 1):
                    memo['definidos'].update({asignatura_indi[0]:tuplas_maximas})
                    asignaturas[asignatura_indi[0]] = asignaturas[asignatura_indi[0]]-len(tuplas_maximas)
                    for remover in codigos_keys[asignatura_indi[0]]:
                        if ((asignatura_indi[0],remover[1]) in estudiantes[remover[0]]):
                            estudiantes[remover[0]].remove((asignatura_indi[0],remover[1]))
                    
                #De lo contrario pasamosla lista de misma prioridad a indefinidos
                else:
                    memo['indefinidos'].update({asignatura_indi[0]:tuplas_maximas})
        #Si la cantidad de cupos es igual a la cantidad de estudiantes solicitantes los pasamos todos
        if(diccionario[0][asignatura_indi[0]] == len(codigos_keys[asignatura_indi[0]])):
            memo['definidos'].update({asignatura_indi[0]:codigos_keys[asignatura_indi[0]]})
            #se modifica el cpo del diccionario asignaturas 
            asignaturas[asignatura_indi[0]] = asignaturas[asignatura_indi[0]]- len(codigos_keys[asignatura_indi[0]])
            for remover in codigos_keys[asignatura_indi[0]]:
                if ((asignatura_indi[0],remover[1]) in estudiantes[remover[0]]):
                    estudiantes[remover[0]].remove((asignatura_indi[0],remover[1]))
            
        if (diccionario[0][asignatura_indi[0]] > 0):
            clave_indefinidos = ','.join(memo['indefinidos'].keys())
            clave_definidos = ','.join(memo['definidos'].keys())
            if (asignatura_indi[0] not in clave_indefinidos and asignatura_indi[0] not in clave_definidos):
                # Primero, encontramos el valor máximo en el segundo elemento de todas las tuplas
                maximo_valor = max(codigos_keys[asignatura_indi[0]], key=lambda x: x[1])[1]
                # Luego, construimos una lista de todas las tuplas que tienen ese valor máximo
                tuplas_maximas = [tupla for tupla in codigos_keys[asignatura_indi[0]] if tupla[1] == maximo_valor]
                if (len(tuplas_maximas) == 1):
                    memo['definidos'].update({asignatura_indi[0]:tuplas_maximas})
                    asignaturas[asignatura_indi[0]] = asignaturas[asignatura_indi[0]]-len(tuplas_maximas)
                    estudiantes[tuplas_maximas[0][0]].remove((asignatura_indi[0],tuplas_maximas[0][1]))
                    
                #De lo contrario pasamosla lista de misma prioridad a indefinidos
                else:
                    memo['indefinidos'].update({asignatura_indi[0]:tuplas_maximas})

    print(memo)
    #print(asignaturas)
    print("---------------------------------------------------")
    print(diccionario)
    print("---------------------------------------------------")
    print(codigos_keys)
    