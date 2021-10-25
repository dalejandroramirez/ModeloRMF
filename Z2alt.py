import numpy as np
import random



def valorc(nd,etiqueta_hijo):
    """nd es un diccionario con key su ubicacion y argumento (valorc, Etiqueta)"""
    if nd[1]<etiqueta_hijo:
        return(nd[0])
    else: 
        return(nd[1]-etiqueta_hijo)

def Z2alt(h):
    Cfin=1
    h_actual=0
    Papa={(0,0):(0,random.uniform(0,1))}
    Hijos={}
    while h_actual!=h:
        h_actual+=1
        for i in range(0,h_actual+1):
            etiqueta=random.uniform(0,1)
            if i==0 :
                ValorC=round(valorc(Papa[(0,h_actual-1)],etiqueta),3)
                Hijos[(0,h_actual)]=(ValorC,etiqueta)
            elif i==h_actual:
                ValorC=round(valorc(Papa[(h_actual-1,0)],etiqueta),3)
                Hijos[(i,h_actual-i)]=(ValorC,etiqueta)
            elif 0<i and i<h_actual:
                ValorC1=round(valorc(Papa[(i-1,h_actual-i)],etiqueta),3)
                ValorC2=round(valorc(Papa[(i,h_actual-i-1)],etiqueta),3)
                ValorC=min(ValorC1,ValorC2)
                Hijos[(i,h_actual-i)]=(ValorC,etiqueta)
            if h==h_actual:
                Cfin=min(Cfin,ValorC)
        Papa=Hijos
        Hijos={}

    return(Cfin)
            

def Ordenar_z2alt(h,N):
    X=[Z2alt(h) for i in range(0,N)]
    X.sort()
    return(X)

        

Z2alt(10)


