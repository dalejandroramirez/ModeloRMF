# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 13:55:33 2021

@author: digin
"""

"""El objeto nodo tiene dos propiedades nivel y el
valor c que es el valor con el que va a poder percolar
"""
import pandas as pd
import numpy as np
from collections import deque
import matplotlib.pyplot as plt
def RMF(d,h):
    class nodo:
        def __init__(self,nivel,c):
            self.nivel=nivel
            self.etiqueta=np-random.uniform(0,1,1)[0]
            self.valorC=c
    s=deque([nodo(0,0)])
    c=0
    cfin=1
    while len(s)!=0:
        nd=s.pop()
        hijos=[nodo(nd.nivel+1,1) for i in range(d)]
#"""hasta el momento se creo todos los hijos de nd con
#una etiqueta de 1 para asegurar su percolación, mas
#adelante vamos a modificarla
#"""
        for j in range(d):
            if nd.valorC<round(nd.etiqueta-hijo[j].etiqueta,3):
                hijos[j].valorC=round(nd.etiqueta-hijos[j].etiqueta,3)
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
