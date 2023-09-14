#Hagamos todas las posibles combinaciones dentro de lo factible
#(Codigo de asignatura, Cupo)
#M={(M1,3),(M2,4),(M3,1)}
#(Codifo del estudiante, conjutno de materias solicitadas)
#E{(e1,ms1)...(en,msn)}
#ms1={(M1,5)(M2,2)(M3,1)} ...
#msn=...
#Tendremos lista de tuplas

#ntrada de los datos
M = [("M1",3),("M2",4),("M3",1)]
E = [("e1","ms1"),("e2","ms2"),("e3","ms3"),("e4","ms4"),("e5","ms5")]
ms1 = [("M1",5),("M2",2),("M3",1)]
ms2 = [("M1",4),("M2",1),("M3",3)]
ms3 = [("M2",3),("M3",2)]
ms4 = [("M1",2),("M3",3)]
ms5 = [("M1",3),("M2",2),("M3",3)]

for cms in E:
    elemento = cms[0]  # Obtiene el primer elemento del par (e.g., "e1")
    sublista = globals()[cms[1]]  # Obtiene la sublista correspondiente (e.g., ms1)
    
    # Imprime el elemento y sus tuplas asociadas
    print(f"Elemento: {elemento}")
    for ms in sublista:
        print(f"Tupla: {ms}")
    


