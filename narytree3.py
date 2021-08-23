# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:19:26 2021

@author: digin
"""

import numpy as np
from collections import deque
import matplotlib.pyplot as plt

def ARI3(d,h,p):
    """
    En esencia es el mismo algoritmo del ARI2 solamente que correra con funciona
    distribución uniforme y se toma un p fijo tal que si el numero aleatorio es mayor
    que ese p entones va a percolar
    """
    s=deque([[0,np.random.rand(1)]])
    while len(s)!=0:
        nivel,aux=s.pop()

        if nivel==h:
            return(1)
        hijos=[nivel+1,np.random.uniform(0,1,d)]
        Accesible=(p>hijos[1])
        j=0
        while j<d:
            if Accesible[j]==True :
                s.append([hijos[0],round(hijos[1][j],2)])
            j=j+1
        if len(s)==0:
            return(0)

def EsperadoAcces(d,h,rep,pc):
    """Calcula el promedio de caminos percolados en un d-ary con altura h
    en rep repetiones con una probabilidad de percolacion pc
    """
    cont=0
    for i in np.linspace(0,1,rep):
       cont=cont+ARI3(d,h,pc)
    return(cont/rep)



def GrafAcces():
    """Me evalua los posibles valores de pc en El binomial model
    da un valor minimo pc en (0,e),el cual es el valor minimo de percolacion
    """
    d =int(input("ingrese el numero de hijos que tendrá cada nivel: "))
    h =int(input("ingrese la altura maxima que tendra el arbol: "))
    rep= int(input("ingrese el numero de repeticiones que se quiere hacer: "))
    Y=[]
    j=0
    e=0.001
    for pc in np.linspace(0,1,rep):
        Y.append(EsperadoAcces(d,h,rep,pc))
    while Y[j]<e:
        j=j+1
    Cmin=np.linspace(0,1,rep)[j]
    plt.title('Path Accesible')
    plt.suptitle("nivel 100 con 2000 repeticiones")
    plt.xlabel(r'P_c')
    plt.ylabel('E(Percolacion)')
    plt.plot(np.linspace(0,1,rep),Y,'-',label=("Cmin=",round(Cmin,4)))
    plt.axvline(x=Cmin,ymin=-3,ymax=3,ls="dotted")
    plt.legend()
    plt.show()
    return(Cmin)
print(GrafAcces())
#print(GrafAcces(2,100,1000))
#print(GrafAcces(2,100,2000))
