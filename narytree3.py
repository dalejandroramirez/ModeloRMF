# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:19:26 2021

@author: digin
"""
import numpy as np
from collections import deque
import matplotlib.pyplot as plt

def ARI3(d,h,p):

    s=deque([[0,np.random.rand(1)]])
    while len(s)!=0:
        nivel,aux=s.pop()

        if nivel==h:
            return(1)
        hijos=[nivel+1,np.random.uniform(0,1,d)]
        #print(aux)
        #print(hijos)
        Accesible=(p>hijos[1])
        #print(Accesible)
        j=0
        while j<d:
            if Accesible[j]==True :
                s.append([hijos[0],round(hijos[1][j],2)])
            j=j+1
        if len(s)==0:
            return(0)
        #print(s)
#print(ARI3(2,10,0.5))




def EsperadoAcces(d,h,rep,pc):
    cont=0
    for i in np.linspace(0,1,rep):
       cont=cont+ARI3(d,h,pc)
    return(cont/rep)


##esta funcion me evalua los posibles valores de pc en El binomial model
#da un valor minimo pc en (0,e),el cual es el valor minimo de percolacion

def GrafAcces(d,h,rep):
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


print(GrafAcces(3,100,100))
#print(GrafAcces(2,100,1000))
#print(GrafAcces(2,100,2000))
