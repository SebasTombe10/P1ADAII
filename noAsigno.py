#en esta funcion sretorna una lista con las prioridades sumandas por estudiante que no fueron asignadas 
def prioridadesNoAsignadas(asignados,diccionario):
    # Eliminar elementos de diccionario que coinciden con elementos de asignados
    for clave, valores_lista1 in asignados.items():
        if clave in diccionario:
            valores_lista2 = diccionario[clave]
            diccionario[clave] = [(m, v) for m, v in valores_lista2 if m not in valores_lista1]
    # Almacena la suma de valores por estudiante
    suma_valores_por_estudiante = {}
    # Recorrer diccionario actualzado para calcular la suma de valores por estudiante
    for estudiante, valores in diccionario.items():
        suma = 0
        for materia, valor in valores:
            if materia.startswith('M'):
                suma += valor
        suma_valores_por_estudiante[estudiante] = suma
    # diccionario en una lista de valores
    lista_suma_valores = list(suma_valores_por_estudiante.values())
    return lista_suma_valores
    

