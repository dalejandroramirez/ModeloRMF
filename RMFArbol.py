# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 09:53:09 2021

@author: digin
"""
import time
import numpy as np
from collections import deque

def Porcentaje_accesibles_nary_RMF_c(d,h):
        """
        Vamos a modelar un proceso RMF en un d-arry con d hijos
        el cual tendra una altura h, se hara una busqueda
        en profundidad encontrando el c minimo de tal manera que se alcanza
        a percolar y este c minimo se le hace un redondeo de 3 cifras
        significativas para disminuir el tiempo de ejecucion """
        class nodo:
            """El objeto nodo tiene dos propiedades nivel que es la altura
            y el valor c que es el valor con el que va a poder percolar
            """
            def __init__(self,nivel,c):
                self.nivel=nivel
                self.etiqueta=np.random.uniform(0,1,1)[0]
                self.valorC=c
        #np.random.seed(0)   ### estoy fijando el nodo semilla
        papa=nodo(0,0)
        s=deque([papa])
        Cfin=1
        while len(s)!=0:
            nd=s.pop()

            if nd.valorC>=Cfin:
                continue
            hijos=[nodo(nd.nivel+1,nd.valorC) for i in range(d)]
            for j in range(d):
                if nd.valorC<round(nd.etiqueta-hijos[j].etiqueta,3):
                    hijos[j].valorC=round(nd.etiqueta - hijos[j].etiqueta,3)
                if hijos[j].valorC < Cfin :
                    if hijos[j].nivel==h:
                        Cfin=min(hijos[j].valorC,Cfin)
                        continue
                    s.append(hijos[j])
        return(Cfin)



def Ordenar(d,h,N):
    X=[Porcentaje_accesibles_nary_RMF_c(d, h) for i in range(0,N)]
    X.sort()
    return(X)

def Lista_valoresC(d,h,N):
    hora=time.strftime("%H_%M_%S")
    file =open("ValoresC_h_"+str(h)+"_d_"+str(d)+"_hora_"+str(hora)+".txt","w")
    X=Ordenar(d,h,N)
    for i in range(0,N):
        file.write(str(X[i])+"\n")
    file.close()
    return(0)

if __name__=='__main__':
    '''aqui ejecutare los programas'''
    print(__name__)
    print(Porcentaje_accesibles_nary_RMF_c(2,10))
