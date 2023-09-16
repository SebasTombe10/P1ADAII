# Datos de entrada
M = [("M1", 3), ("M2", 4), ("M3", 1)]
E = [("e1", "ms1"), ("e2", "ms2"), ("e3", "ms3"), ("e4", "ms4"), ("e5", "ms5")]
ms1 = [("M1", 5), ("M2", 2), ("M3", 1)]
ms2 = [("M1", 4), ("M2", 1), ("M3", 3)]
ms3 = [("M2", 3), ("M3", 2)]
ms4 = [("M1", 2), ("M3", 3)]
ms5 = [("M1", 3), ("M2", 2), ("M3", 3)]

def voraz():
    # clave cod asig : valor cupo asign
    asignaturas = dict(M)
    #clave cod estudiante : valor conjunto de asig soli
    estudiantes = dict(E)


    asignaturas_prioritarias = {estudiante: sorted(ms, key=lambda x: x[1], reverse=True) for estudiante, ms in zip(estudiantes.keys(), [ms1, ms2, ms3, ms4, ms5])}
    #prioridad más alta entre todos los estudiantes
    prioridad_maxima = max(max(ms, key=lambda x: x[1])[1] for ms in [ms1, ms2, ms3, ms4, ms5])
    # Crear una lista de estudiantes ordenados por prioridad descendente
    estudiantes_ordenados = sorted(estudiantes.keys(), key=lambda estudiante: max(asignaturas_prioritarias[estudiante], key=lambda x: x[1])[1], reverse=True)
    # Inicializar un diccionario de asignación vacío para cada estudiante
    asignacion = {estudiante: [] for estudiante in estudiantes.keys()}
    # Crear una lista con todas las prioridades
    todas_las_prioridades = [prioridad for estudiante in estudiantes.keys() for _, prioridad in asignaturas_prioritarias[estudiante]]
    # Asignar las asignaturas a los estudiantes en orden de prioridad
    band = False
    while band == False:
        cont = -1
        for estudiante in estudiantes_ordenados:
            asignaturas_solicitadas = asignaturas_prioritarias[estudiante]
            for asignatura, prioridad in asignaturas_solicitadas:
                cont = cont + 1
                if prioridad >= max(todas_las_prioridades):
                    todas_las_prioridades[cont] = 0
                    if asignaturas[asignatura] > 0:
                        if asignatura not in asignacion[estudiante]:
                            asignacion[estudiante].append(asignatura)
                            asignaturas[asignatura] -= 1
                else: False
        if asignaturas[asignatura] == 0:
                        band = True
    return asignacion
"""
    # Imprimir la asignación final
    for estudiante, asignaturas_asignadas in asignacion.items():
        print(f"Estudiante {estudiante} recibió las asignaturas: {asignaturas_asignadas}")
"""