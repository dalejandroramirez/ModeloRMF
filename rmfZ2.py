# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 18:44:27 2021

@author: digin
"""
import random
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
        if tuple(nd.ubicacion) not in visitados:
            visitados[tuple(nd.ubicacion)]=nd.etiqueta
        ubicacionup=[nd.ubicacion[0],nd.ubicacion[1]+1]
        ubicacionrigth=[nd.ubicacion[0]+1,nd.ubicacion[1]]
        up,rigth=tuple(ubicacionup),tuple(ubicacionrigth)
        if up in visitados:
            hijoup=nodo(ubicacionup,nd.ValorC,visitados[up])
        else :
            visitados[up]=np.random.uniform(0,1,1)[0]
            hijoup=nodo(ubicacionup,nd.ValorC,visitados[up])
        if rigth in visitados:
            hijorigth=nodo(ubicacionrigth,nd.ValorC,visitados[rigth])
        else :
            visitados[rigth]=np.random.uniform(0,1,1)[0]
            hijorigth=nodo(ubicacionrigth,nd.ValorC,visitados[rigth])
        if nd.ValorC<round(nd.etiqueta-hijoup.etiqueta,3):
            hijoup.ValorC=round(nd.etiqueta - hijoup.etiqueta,3)
        else:
            hijoup.ValorC=round(hijoup.ValorC,3)
        if nd.ValorC<round(nd.etiqueta-hijorigth.etiqueta,3):
                    hijorigth.ValorC=round(nd.etiqueta - hijorigth.etiqueta,3)
        else:
            hijorigth.ValorC=round(hijorigth.ValorC,3)
        if hijoup.ValorC<Cfin:
            if (hijoup.ubicacion[0]+hijoup.ubicacion[1]==h) or (hijorigth.ubicacion[0]+hijorigth.ubicacion[1]==h):
                Cfin=min(hijoup.ValorC,Cfin,hijorigth.ValorC)
                continue
            s.append(hijoup)
            s.append(hijorigth)
    return(len(visitados))
    #return(Cfin)
        
if __name__=="__main__":
    for i in range(30,50):
        print(RMF_in_Z2mas(2,i))
        #print(RMF_in_Z2mas(2,i))

    

    
    


def e(i,d):
    ei=np.zeros(d)
    ei[i]=1
    return(ei)




def RMF_in_Zdmas(d,h):
    visitados={}
    random.seed(0)
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
            if tuple(ubicacion_i) in visitados:
                hijo_i=nodo(ubicacion_i,nd.ValorC,visitados[tuple(ubicacion_i)])
            else:
                visitados[tuple(ubicacion_i)]=np.random.uniform(0,1,1)[0]
                hijo_i=nodo(ubicacion_i,nd.ValorC,visitados[tuple(ubicacion_i)])
    
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
        

    
    
     
    