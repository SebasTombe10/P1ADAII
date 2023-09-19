listres=[]
def insaEstudiante(ma,ms,P,cantE):
    res = 1-(ma/ms)*(P/ms)
    listres.append(res)
    print(listres)
def insaGeneral(cantE):
    res = sum(listres)/cantE
    print(res)