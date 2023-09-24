from insatisfaccion import insaEstudiante
import copy

def voraz(d):
    # clave cod asig : valor cupo asign
    asignaturas,dicestudiantes = d
    ta = copy.deepcopy(dicestudiantes)
    asignadas = {estudiante: [] for estudiante in dicestudiantes.keys()}
    prioridades = [prioridad for estudiante in dicestudiantes.keys() for _, prioridad in dicestudiantes[estudiante]]
    while True:
        for estudiante in dicestudiantes:
            asignaturas_solicitadas = dicestudiantes[estudiante]
            for codigo,prioridad in asignaturas_solicitadas:
                if prioridad >= max(prioridades):
                    max_prioridad = max(prioridades)
                    prioridades = [0 if p == max_prioridad else p for p in prioridades]  # Reemplaza la prioridad máxima por cero
                    if asignaturas[codigo] > 0:
                        if codigo not in asignadas[estudiante]:
                            asignadas[estudiante].append(codigo)
                            lista_asignatura_solicitada = dicestudiantes[estudiante]
                            lista_asignatura_solicitada.remove((codigo,prioridad))
                            asignaturas[codigo] = asignaturas[codigo]-1
        if all(valor == 0 for valor in asignaturas.values()):break
    suma_prioridad_no_asignadas = []

    for lista_de_tuplas in dicestudiantes.values():
        suma = sum(valor for _, valor in lista_de_tuplas)
        suma_prioridad_no_asignadas.append(suma)

    insaEstudiante(asignadas,ta,suma_prioridad_no_asignadas)
    return asignadas