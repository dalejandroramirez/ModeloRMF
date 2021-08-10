


## este algoritmo me dice si existe percolacion o no, es decir,
#retorna una respuesta booleana

#si en el deque existe un individuo con un nivel h entonces returna 1
#de resto sigue intentando percolar y el algoritmo hace una busqueda
#profunda lo que hace que el algitmo sea mas eficiente


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
