# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 09:53:09 2021

@author: Daniel Alejandro Ramirez Gomez
"""
import time
import numpy as np
from collections import deque

def Minimo_valor_c_arboles_regulares(d,h):
        """
        Vamos a modelar un proceso RMF en un arbo regular con d hijos
        y altura h. haremos busqueda
        en profundidad encontrando el c minimo de tal manera que un
        sea accesible hasta altura h """

        class nodo:

            """El objeto nodo tiene dos propiedades nivel que es la altura
            y el valor c que es el valor con el que va a poder percolar
            """

            def __init__(self,nivel,c):
                self.nivel = nivel
                self.etiqueta = np.random.uniform(0,1,1)[0]
                self.valorC = c
        papa = nodo(0,0)
        s = deque([papa])
        Cfin = 1
        while len(s) != 0:
            nd = s.pop()

            if nd.valorC >= Cfin:
                continue
            hijos = [nodo(nd.nivel + 1,nd.valorC) for i in range(d)]
            for j in range(d):
                if nd.valorC < round(nd.etiqueta - hijos[j].etiqueta,3):
                    hijos[j].valorC = round(nd.etiqueta - hijos[j].etiqueta,3)
                if hijos[j].valorC < Cfin :
                    if hijos[j].nivel == h:
                        Cfin = min(hijos[j].valorC,Cfin)
                        continue
                    s.append(hijos[j])
        return(Cfin)

def Ordenar(d,h,N):
    X = [Minimo_valor_c_arboles_regulares(d, h) for i in range(0,N)]
    X.sort()
    return(X)

def tiempo_ejecucion(h,N):
    count = 0 
    for _ in range(0,N):
        inicio = time.time()
        Minimo_valor_c_arboles_regulares(2,h)
        time.sleep(1)
        fin = time.time()
        count += fin-inicio
    return(count/N)

if __name__=='__main__':
    '''aqui ejecutare los programas'''
    #print("El valor C minimo de percolacion es =", end=' ')
    #print(Minimo_valor_c_arboles_regulares(2,10))
    print(tiempo_ejecucion(500,5))
    print(tiempo_ejecucion(1000,5))
    print(tiempo_ejecucion(2000,5))



#1.29 1.18 1.54 2.17 2.25 1.59 1.74 2.73 3.0 HEAP