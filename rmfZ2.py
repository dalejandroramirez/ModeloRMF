# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 18:44:27 2021

@author: digin
"""
from collections import deque
import numpy as np
class nodo():
    def __init__(self,ubicacion,c,etiqueta):
        self.ubicacion=ubicacion
        self.ValorC=c
        self.etiqueta=etiqueta

def RMF_in_Z2mas(d,h):
    visitados={}
    papa=nodo([0,0],0,np.random.uniform(0,1,1)[0])
    s=deque([papa])
    Cfin=1
    while len(s)!=0:
        nd=s.pop()
        if nd.ValorC>Cfin:
            continue
        visitados[tuple(nd.ubicacion)]=nd.etiqueta
        ubicacionup=[nd.ubicacion[0],nd.ubicacion[1]+1]
        ubicacionrigth=[nd.ubicacion[0]+1,nd.ubicacion[1]]
        up,rigth=tuple(ubicacionup),tuple(ubicacionrigth)
        if up in visitados:
            hijoup=nodo(ubicacionup,nd.ValorC,visitados[up])
        else :
            hijoup=nodo(ubicacionup,nd.ValorC,np.random.uniform(0,1,1)[0])
        if rigth in visitados:
            hijorigth=nodo(ubicacionup,nd.ValorC,visitados[rigth])
        else :
            hijorigth=nodo(ubicacionup,nd.ValorC,np.random.uniform(0,1,1)[0])
        if nd.valorC<round(nd.etiqueta-hijoup.etiqueta,3):
                    hijoup.valorC=round(nd.etiqueta - hijos[j].etiqueta,3)
        else:
            hijoup.ValorC=round(hijoup.ValorC,3)
        if nd.valorC<round(nd.etiqueta-hijorigth.etiqueta,3):
                    hijorigth.valorC=round(nd.etiqueta - hijorigth.etiqueta,3)
        else:
            hijorigth.ValorC=round(hijorigth.ValorC,3)
            
            
            
        
RMF_in_Z2mas(2, 10)
    
    
     
    