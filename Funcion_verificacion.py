# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 12:38:59 2021

@author: digin
"""

import numpy as np
from collections import deque
import rmffinal as RMF

def Funcion_verificacion(d,h):
    """Verificará su la función Porcentaje_accesible_nary_RMF()() esta bien definida """
    """creare un vector donde se guardaran todas las etiquetas
    de los nodos y con estas etiquetas se correra otro modelo
    el cual en teoria debera devolver el mismo valor de c"""
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
        np.random.seed(0)   ### estoy fijando el nodo semilla
        papa=nodo(0,0)
        s=deque([papa])
        A=[papa.etiqueta]
        Cfin=1

        while len(s)!=0:
            nd=s.pop()
            hijos=[nodo(nd.nivel+1,nd.valorC) for i in range(d)]
            for hijo in hijos:
                A.append(hijo.etiqueta)
            print(nd.valorC)
#"""hasta el momento se creo todos los hijos de nd con
#una etiqueta de 1 para asegurar su percolación, mas
#adelante vamos a modificarla
#"""
            for j in range(d):
                #print(hijos[j].valorC)
                #print(round(nd.etiqueta-hijos[j].etiqueta,3))

                #print(round(nd.valorC,3))

                if nd.valorC<round(nd.etiqueta-hijos[j].etiqueta,3):
                    hijos[j].valorC=round(nd.etiqueta - hijos[j].etiqueta,3)
#"""si no se puede seguir percolando con la etiqueta del papa, entonces
#se actializa por la diferencia que se necesita """
                elif nd.valorC>nd.etiqueta-hijos[j].etiqueta:
                    True
                    #hijos[j].valorC=round(hijos[j].valorC,3)
                if hijos[j].valorC < Cfin :
                    if hijos[j].nivel==h:
                        #print(nd.valorC)
                        Cfin=min(hijos[j].valorC,Cfin)
                        continue
                    nd=hijos[j]
                    s.append(nd)


            #B.append(Cfin)
        return(A,Cfin)
    MM=Porcentaje_accesibles_nary_RMF_c(d, h)
    return(MM)
print(Funcion_verificacion(2,2))
