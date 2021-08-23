# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 13:55:33 2021

@author: digin
"""

import numpy as np
from collections import deque

def Porcentaje_accesibles_nary_RMF_c(d,h):
    """
    Vamos a modelar un proceso RMF en un d-arry con d hijos
    el cual tendra una altura h, se hara una busqueda
    en profundidad encontrando el c minimo de tal manera que se alcanza
    a percolar y este c minimo se le hace un redondeo de 3 cifras
    significativas para disminuir el tiempo de ejecucion
    """
    class nodo:
        """El objeto nodo tiene dos propiedades nivel que es la altura
        y el valor c que es el valor con el que va a poder percolar
        """
        def __init__(self,nivel,c):
            self.nivel=nivel
            self.etiqueta=np.random.uniform(0,1,1)[0]
            self.valorC=c
    s=deque([nodo(0,0)])
    Cfin=1
    while len(s)!=0:
        nd=s.pop()
        hijos=[nodo(nd.nivel+1,1) for i in range(d)]
#"""hasta el momento se creo todos los hijos de nd con
#una etiqueta de 1 para asegurar su percolación, mas
#adelante vamos a modificarla
#"""
        for j in range(d):
            if nd.valorC<round(nd.etiqueta-hijos[j].etiqueta,3):
                hijos[j].valorC=round(nd.etiqueta - hijos[j].etiqueta,3)
#"""si no se puede seguir percolando con la etiqueta del papa, entonces
#se actializa por la diferencia que se necesita """
            elif nd.valorC>nd.etiqueta-hijos[j].etiqueta:
                hijos[j].valorC=round(nd.valorC,3)
            if hijos[j].valorC < Cfin :
                if hijos[j].nivel==h:
                    Cfin=min(nd.valorC,Cfin)
                    continue
                s.append(hijos[j])
    return(Cfin)
