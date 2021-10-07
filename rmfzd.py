# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 15:28:34 2021

@author: digin
"""
from collections import deque
import numpy as np

class nodo():
    def __init__(self,ubicacion,c,etiqueta):
        self.ubicacion=ubicacion
        self.ValorC=c
        self.etiqueta=etiqueta

def e(i,d):
    ei=np.zeros(d)
    ei[i]=1
    return(ei)


def RMF_in_Zdmas(d,h):
    visitados={}
    papa=nodo(np.zeros(d),0,np.random.uniform(0,1,1)[0])
    s=deque([papa])
    Cfin=1
    while len(s)!=0:
        nd=s.pop()
        if nd.ValorC>Cfin:
            continue
        if tuple(nd.ubicacion) not in visitados:
            visitados[tuple(nd.ubicacion)]=nd.etiqueta
        for i in range(d):
            ubicacion_i=nd.ubicacion+e(i,d)
            if ubicacion_i in visitados:
                hijo_i=nodo(ubicacion_i,nd.ValorC,visitados[ubicacion_i])
            else:
                visitados[ubicacion_i]=np.random.uniform(0,1,1)[0]
                hijo_i=nodo(ubicacion_i,nd.ValorC,visitados[ubicacion_i])

            if nd.ValorC<round(nd.etiqueta-hijo_i.etiqueta,3):
                hijo_i.ValorC=round(nd.etiqueta - hijo_i.etiqueta,3)
            else:
                hijo_i.ValorC=round(hijo_i.ValorC,3)
            if hijo_i.ValorC<Cfin:
                if sum(hijo_i.ubicacion)==h:
                    Cfin=min(hijo_i.ValorC,Cfin)
                    continue
                s.append(hijo_i)
    return(Cfin)




print(RMF_in_Zdmas(5, 10))
