


""" este algoritmo me dice si existe percolacion o no, es decir,
#retorna una respuesta booleana

#si en el deque existe un individuo con un nivel h entonces returna 1
#de resto sigue intentando percolar y el algoritmo hace una busqueda
#profunda lo que hace que el algitmo sea mas eficiente

"""
import numpy as np
from collections import deque
import matplotlib.pyplot as plt

def ARI2(d,h,p):
    s=deque([[0,np.random.binomial(1,p,1)]])
    while len(s)!=0:
        nivel,aux=s.pop()
        if nivel==h:
            return(1)
        hijos=[nivel+1,np.random.binomial(1,p,d)] #  "1"
        Accesible=(1==hijos[1])
        j=0
        while j<d:  #"2"
            if Accesible[j]==True :
                s.append([hijos[0],hijos[1][j]])
            j=j+1
        if len(s)==0:
            return(0)
"""
Comentarios
1- dado que no se ha llegado hasta el nivel h deseado entonces se generan
los nuevos hijos del nodo que se quito
2- se agregan al deque los nodos que si fueron percolados
"""


###Sacaremos el promedio de percolaciones en una poblacion de tamaño repeticiones
#con un probabilidad de percolacion de pc
# altura h y numero de hijos d

def EsperadoBin(d,h,rep,pc):
    cont=0
    for i in np.linspace(0,1,rep):
       cont=cont+ARI2(d,h,pc)
    return(cont/rep)


##esta funcion me evalua los posibles valores de pc en El binomial model
#da un valor minimo pc en (0,e),el cual es el valor minimo de percolacion
#e : me va a decir que tan grande debe ser el porcentaje de percolaciones
#para considerarlo cero


def GrafBin(d,h,rep,e):
    Y=[]
    j=0
    for pc in np.linspace(0,1,rep):
        Y.append(EsperadoBin(d,h,rep,pc))
    while Y[j]<e:
        j=j+1
    Cmin=np.linspace(0,1,rep)[j]

    plt.title('Binomial Model')
    plt.suptitle("nivel " +str(h)+" con " + str(rep) + " repeticiones")
    plt.xlabel(r'P_c')
    plt.ylabel('E(Percolacion)')
    plt.plot(np.linspace(0,1,rep),Y,'-',label=("Cmin=",round(Cmin,4)))
    plt.axvline(x=Cmin,ymin=-3,ymax=3,ls="dotted")
    plt.legend()
    plt.show()
    return(Cmin)


print(GrafBin(2,100,100,0.001))
