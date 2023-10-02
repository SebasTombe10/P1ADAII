from copy import deepcopy
from pathlib import Path

archivillo = "e_3_5_5.roc"

"""ejcupos = {
    "101": 3,
    "102": 4,
    "103": 2,
}
ejsolicitudes = {
    "1001": {"101": 5, "102": 2, "103": 1},
    "1002": {"101": 4, "102": 1, "103": 3},
    "1003": {"102": 3, "103": 2},
    "1004": {"101": 2, "103": 3},
    "1005": {"101": 3, "102": 2, "103": 3},
}
ejmaterias = len(ejcupos)
ejestudiantes = len(ejsolicitudes)"""

sol = {
    "1000": ["101"],
    "1001": ["101", "102"],
    "1002": ["100"],
    "1003": ["102"],
    "1004": ["101"],
} # Solución Óptima de un problema X (manual)

cupos = {}
solicitudes = {}
numero_materias = 0
numero_estudiantes = 0


class rocfile:
    """Tipo de Archivo .ROC"""

    pass


def leer_archivo(archivo: rocfile):
    """Lee archivos .ROC"""
    global cupos, solicitudes, numero_materias, numero_estudiantes

    entrada = open(
        file=(Path(__file__).parent / "Pruebas/{}".format(archivo)),
        mode="r",
        encoding="utf-8",
    )

    numero_materias = int(entrada.readline())

    # Se leen las materias y se les asigna su respectivo cupo
    for linea in range(0, numero_materias):
        linea = entrada.readline()
        linea = linea.split(",")
        cupos[linea[0]] = int(linea[1])

    # Se lee el número de estudiantes
    numero_estudiantes = int(entrada.readline())

    # Se leen los estudiantes
    for estudiante in range(0, numero_estudiantes):
        # Se lee el código de estudiantes y el número de materias solicitadas
        estudiante = entrada.readline()
        estudiante = estudiante.split(",")

        nuevo_estudiante = {}
        numero_materias_estudiante = int(estudiante[1].strip())

        # Se leen las materias solicitadas con su respectiva prioridad
        for solicitud in range(0, numero_materias_estudiante):
            solicitud = entrada.readline()
            solicitud = solicitud.split(",")
            nuevo_estudiante[solicitud[0]] = int(solicitud[1].strip())

        solicitudes[estudiante[0]] = nuevo_estudiante

    entrada.close()
    # print(f"Solicitudes: {solicitudes}")


def escribir_archivo(
    archivo: rocfile, asignaciones: dict, insatisfaccion: float, tipo_algoritmo: str
) -> rocfile:
    """Escribe un archivo .ROC con la solución del problema y su respectivo costo"""
    dato = archivo.split(".")

    salida = open(
        file=(
            Path(__file__).parent
            / "Salidas/{}_{}.{}".format(dato[0], tipo_algoritmo, dato[1])
        ),
        mode="w",
        encoding="utf-8",
    )

    salida.write("Costo" + "\n")
    salida.write(str(insatisfaccion) + "\n")

    for estudiante in asignaciones:
        salida.write(estudiante + "," + str(len(asignaciones[estudiante])) + "\n")

        for asignatura in asignaciones[estudiante]:
            salida.write(asignatura + "\n")


def insatisfaccion_total(
    materias: int, estudiantes: int, cupos: dict, asignaciones: dict, solicitudes: dict
) -> float:
    """Devuelve la insatisfacción total de las asignaciones de los estudiantes"""

    aux_asignaciones = deepcopy(asignaciones)
    aux_cupos = deepcopy(cupos)
    num_estudiantes = len(solicitudes)

    if estudiantes == 0:
        return 0

    if (materias == 0 or len(asignaciones) == 0) and estudiantes > 0:
        return 1

    # Obtenemos al último estudiante y su asignación
    # lista_estudiantes = obtener_lista_estudiantes(aux_asignaciones)
    estudiante = obtener_ultimo_estudiantes(aux_asignaciones)
    asignacion_estudiante = aux_asignaciones[estudiante]
    aux_asignaciones.pop(estudiante)

    # A cada materia le quitamos los cupos asignados al estudiante
    for materia in asignacion_estudiante:
        aux_cupos[materia] -= 1

    return insatisfaccion_total(
        materias, estudiantes - 1, aux_cupos, aux_asignaciones, solicitudes
    ) + (
        insatisfaccion_singular(estudiante, solicitudes, asignaciones) / num_estudiantes
    )


def insatisfaccion_singular(
    estudiante: str, solicitudes: dict, asignaciones: dict
) -> float:
    """Devuelve la insatisfacción de un estudiante según su asignación de materias"""

    solicitud = set(solicitudes[estudiante])
    asignacion = set(asignaciones[estudiante])
    materias_no_asignadas = solicitud - asignacion
    puntos_prioridad = (3 * len(solicitud)) - 1

    # Puntos de prioridad de los cursos no asignados al estudiante
    puntos_no_asignados = 0

    for materia in materias_no_asignadas:
        puntos_no_asignados += solicitudes[estudiante][materia]

    insatisfaccion = (1 - (len(asignacion) / len(solicitud))) * (
        puntos_no_asignados / puntos_prioridad
    )

    return insatisfaccion


def obtener_lista_estudiantes(dicti: dict) -> list:
    """Devuelve una lista con los estudiantes"""
    return list(dicti.keys())


def obtener_ultimo_estudiantes(dicti: dict) -> list:
    """Devuelve el último estudiante"""
    return next(reversed(dicti.keys()))


"""ejsol = {
    "1001": {"101": 3, "102": 2, "103": 2},
    "1002": {"101": 1, "102": 5, "103": 2},
    "1003": {"101": 4, "102": 2, "103": 2},
}"""

leer_archivo(archivillo)
print(numero_materias)
print(numero_estudiantes)
print(cupos)
print(solicitudes)
insat = insatisfaccion_total(
    numero_materias, numero_estudiantes, cupos, sol, solicitudes
)
print(insat)
escribir_archivo(archivillo, sol, insat, "rocPD")
