# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 16:58:19 2021

@author: digin
"""

import numpy as np
from collections import deque   ## este deque funciona como una cola
import matplotlib.pyplot as plt

d= int(input("ingrese el numero de hijos que tendrá cada nivel: "))

h =int(input("ingrese la altura maxima que tendra el arbol: "))

p= float(input("Ingrese la probabilidad con la que un vertice es percolado: "))

def ConAryBer(d,h,p):
    ###Este algoritmo devuelve un vector que muestra cuantos caminos sobrevive en cada
    """nivel en un proceso beroullo
    d : es la cantidad de hijos que tiene cada proceso
    h : es la altura que tiene el arbol
    p : es la probabilidad de percolación
    """
    A=np.zeros(h)
    s=deque([[0,list(np.random.binomial(1,p,1))]])
    ## inicialmente estamos en el nivel 0 puede que percole o no

    while len(s)!=0:
        nivel,aux=s.pop()
        if nivel<h:
            hijos=[nivel+1,list(np.random.binomial(1,p,d))]
            j=0
            while j<d:
                if hijos[1][j]==True:
                    A[nivel]+=1
                    s.append([hijos[0],hijos[1]])
                j+=1
    return(A)

print(ConAryBer(d,h,p))
