listres=[]
def insaEstudiante(ma,ms,P):
    listma = [len(lista) for lista in ma.values()]
    listms = [len(lista1) for lista1 in ms.values()]
    c=0
    while True:
        print(c)
        res = (1-(listma[c]/listms[c]))*(P[c]/listms[c]) 
        listres.append(res)  
        c+=1
        if len(listres) == len(listms):
            break
    
    print(listres)

def insaGeneral(cantE):
    res = sum(listres)/cantE
    print(res)