
def insaEstudiante(ma,ms,P):
    listres=[]
    insatisfaccion = 0
    listma = [len(lista) for lista in ma.values()]
    listms = [len(lista1) for lista1 in ms.values()]
    c=0
    while True:
        
        res=(1 - (abs(listma[c]) / abs(listms[c]))) * (P[c] / ((3 * abs(listms[c])) - 1))
        listres.append(res)  
        c+=1
        if len(listres) == len(listms):
            break
    
    suma_general = sum(listres)
    insatisfaccion = suma_general/len(P)
    return insatisfaccion