from insatisfaccion import insaEstudiante
import copy

def voraz(d):
    # clave cod asig : valor cupo asign
    asignaturas,dicestudiantes = d
    ta = copy.deepcopy(dicestudiantes)
    asignadas = {estudiante: [] for estudiante in dicestudiantes.keys()}

        #Los chances que tiene cada estudiante para obtener una asifnatura
    chances = {}
    for estudiantes_chances in dicestudiantes:
            suma = 0
            asignaturas_solicitadas_chances = dicestudiantes[estudiantes_chances]
            for codigo,_ in asignaturas_solicitadas_chances:
                if (codigo in asignaturas):
                    cupo = int(asignaturas[codigo])
                    suma = suma + cupo
            chances.update({estudiantes_chances:suma})
        # Ordenar el diccionario por valores de menor a mayor
    chances_ordenado = dict(sorted(chances.items(), key=lambda item: item[1]))
    for estudiante in chances_ordenado:
            asignaturas_solicitadas = dicestudiantes[estudiante]
            for codigo,prioridad in asignaturas_solicitadas:
                    if asignaturas[codigo] > 0:
                        if codigo not in asignadas[estudiante]:
                            asignadas[estudiante].append(codigo)
                            lista_asignatura_solicitada = dicestudiantes[estudiante]
                            lista_asignatura_solicitada.remove((codigo,prioridad))
                            asignaturas[codigo] = asignaturas[codigo]-1
            
    suma_prioridad_no_asignadas = []

    for lista_de_tuplas in dicestudiantes.values():
        suma = sum(valor for _, valor in lista_de_tuplas)
        suma_prioridad_no_asignadas.append(suma)

    insatisfaccion = insaEstudiante(asignadas,ta,suma_prioridad_no_asignadas)
    asignadas.update({"Insatisfaccion":[str(insatisfaccion)]})
    return asignadas