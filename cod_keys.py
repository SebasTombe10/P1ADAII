def cod_keys(diccionario):
    asignaturas, dicestudiantes = diccionario
    codigos_asignaturas = {}
    for cod_asignatura in asignaturas.keys():
        codigos_asignaturas[cod_asignatura] = []

    for estudiante, asignaturas_solicitadas in dicestudiantes.items():
        for cod_asignatura, prioridad in asignaturas_solicitadas:
            if cod_asignatura in asignaturas:
                codigos_asignaturas[cod_asignatura].append((estudiante, prioridad))

    return(codigos_asignaturas)