# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 14:11:50 2021

@author: digin
"""
import numpy as np
import time
import random
class nodo:
    def __init__(self,nivel,c):
        nodo.etiqueta=np.random.uniform(0,1,1)[0]
        nodo.altura=nivel
        nodo.valorc=c
    def proliferar(self,d):
        import random
        np.random.seed(0)
        hijos=[nodo(0,0) for i in range(d)]
        for nd_hijo in hijos:
            nd_hijo.etiqueta=random.random()
            nd_hijo.valor_c=0
            nd_hijo.altura=self.altura+1
        return hijos
    def mostrar(self):
        print('altura',self.altura,'valor de c',self.valorc,'etiqueta', self.etiqueta,)

class My_Heap:
    def __init__(self):
        self.datos=[]
        self.tamanio=0
        self.Dprecision=3

    def intercambiar(self, i,j):#i y j son índices
         a=self.datos[i]
         self.datos[i]=self.datos[j]
         self.datos[j]=a

    def hijo_izquierdo(self,i):
        if 2*i+1<self.tamanio:
            return 2*i+1
        else:
            return None

    def hijo_derecho(self,i):
        if 2*i+2<self.tamanio:
            return 2*i+2
        else:
            return None

    def padre(self,i):
        if i>0:
            return int((i-1)/2)
        else:
            return None

    def obtener_llave(self,i):
        return (round(self.datos[i].valorc,self.Dprecision),self.datos[i].altura)

    def comparar_llaves(self,i,j): #regresa True si la pioridad de i es mayor que la de j
        llave1=self.obtener_llave(i)
        llave2=self.obtener_llave(j)
        if llave1[0]<llave2[0]:
            return True
        elif llave1[0]>llave2[0]:
            return  False
        elif llave1[1]>llave2[1]:
            return True
        else:
            return False

    def arreglar_desde_abajo(self,i):
        if self.padre(i)!=None:
            if self.comparar_llaves(i,self.padre(i)):
                self.intercambiar(i,self.padre(i))
                self.arreglar_desde_abajo(self.padre(i))

    def agregar(self, dato):
        self.datos.append(dato)
        self.tamanio+=1
        self.arreglar_desde_abajo(self.tamanio-1)

    def mostrar(self):
        print(self.datos)

    def minimo(self):
        return self.datos[0]

    def arreglar_desde_arriba(self,i):
        if self.hijo_izquierdo(i)!=None:
            if self.hijo_derecho(i)==None:
                if self.comparar_llaves(self.hijo_izquierdo(i),i):
                    self.intercambiar(i,self.hijo_izquierdo(i))
                    self.arreglar_desde_arriba(self.hijo_izquierdo(i))
            elif self.comparar_llaves(self.hijo_izquierdo(i),self.hijo_derecho(i)):
                 if self.comparar_llaves(self.hijo_izquierdo(i),i):
                    self.intercambiar(i,self.hijo_izquierdo(i))
                    self.arreglar_desde_arriba(self.hijo_izquierdo(i))
            elif self.comparar_llaves(self.hijo_derecho(i),i):
                self.intercambiar(i,self.hijo_derecho(i))
                self.arreglar_desde_arriba(self.hijo_derecho(i))


    def borrar_minimo(self):
        raiz=self.minimo()
        ultimo=self.datos.pop()
        self.tamanio-=1
        if self.tamanio>0:
            self.datos[0]=ultimo
            self.arreglar_desde_arriba(0)
        return raiz


def Porcentaje_accesibles_nary_RMF_c_Heap(d,h):
        """
        Vamos a modelar un proceso RMF en un d-arry con d hijos
        el cual tendra una altura h, se hara una busqueda
        en profundidad encontrando el c minimo de tal manera que se alcanza
        a percolar y este c minimo se le hace un redondeo de 3 cifras
        significativas para disminuir el tiempo de ejecucion """

        s=My_Heap()
        papa=nodo(0,0)
        s.agregar(papa)
        canta=1
        Cfin=1
        while canta>0:
            nd=s.borrar_minimo()
            canta-=1
            #print(canta)
            if nd.valorc>=Cfin:
                continue
            hijos=nd.proliferar(d)
            for j in range(d):
                hijos[j].valorc=nd.valorc
                if nd.valorc<round(nd.etiqueta-hijos[j].etiqueta,3):
                    hijos[j].valorc=round(nd.etiqueta - hijos[j].etiqueta,3)
                if hijos[j].valorc < Cfin :
                    if hijos[j].altura==h:
                        Cfin=min(hijos[j].valorc,Cfin)
                        continue
                    s.agregar(hijos[j])
                    canta=canta+1
        return(Cfin)

def Ordenar_Heap(d,h,N):
    X=[Porcentaje_accesibles_nary_RMF_c_Heap(d, h) for i in range(0,N)]
    X.sort()
    return(X)


if __name__=='__main__':
    print("El valor C minimo de percolacion es =", end=' ')
    print(Porcentaje_accesibles_nary_RMF_c_Heap(2,3))
