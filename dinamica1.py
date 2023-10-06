from cod_keys import cod_keys

def dinamica1(diccionario,memo):
    
    codigos_keys = cod_keys(diccionario)
    asignaturas,estudiantes = diccionario
   
    for codigo_asignatura in codigos_keys.items():
        codigo, lista_codigos = codigo_asignatura  # Separa la clave y la lista asociada
        for cupo_asignatura in asignaturas.values():
            if len(lista_codigos) == cupo_asignatura:
                memo['definidos'].update({codigo: lista_codigos})
                break
        codigos_keys[codigo] = []
           

                 

  
    print(memo)
        
   
        


 
    