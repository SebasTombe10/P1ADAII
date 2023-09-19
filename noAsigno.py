def elimtupla(diccionario,clave,tupla):
    listaestudiante = lista(diccionario)
    for estu in listaestudiante:
        #clave_a_eliminar = clave
        tupla_a_eliminar = tupla

        if estu in diccionario:
            lista = diccionario[estu]
            print(lista)
            if tupla_a_eliminar in lista:
                
                print("Tupla eliminada",tupla_a_eliminar[1])

