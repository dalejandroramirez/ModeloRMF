# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 09:28:04 2021

@author: digin
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#plt.plot(unique,counts)
#'ValoresC1000.txt'

##   capturar nombres en un txt
def Grafica_Acumulado(nombre_archivo,h):
    '''Se realiza una grafica de ValoresC vs P(percolacion), esta probabilidad de percolacion
       se calcula haciendo el aculumalado de las frecuencias de percolacion con cada valor de C
    '''
    df = pd.read_csv('ValoresCheap/'+str(nombre_archivo))
    df=pd.DataFrame(df)
    df=df.sort_index(axis=0, ascending=True)
    (unique, counts) = np.unique(df, return_counts=True) ##retorna un array con los numeros diferentes y sus repeticiones
    N=len(df)
    n=len(unique[0:100])
    j=1
    acum=0
    acumulado=[0]*(n+1)
    while j<=n:
        acum=acum+counts[j-1]
        acumulado[j]=acum
        j=j+1
    y=np.array(acumulado)/N
    unique=np.concatenate([[0],unique])
    y=np.concatenate([[0],y])
    plt.plot(unique[0:60],y[0:60],"-",label="Altura {}".format(h),color=str(h))
    plt.xlabel('Valor C critico')
    plt.ylabel('Probabilidad Percolacio')
    plt.title("RMF Models")
    plt.legend()

    return(0)


if __name__=='__main__':
    Grafica_Acumulado('ValoresC100d2concte.txt',100)
    Grafica_Acumulado('ValoresC1000d2concte.txt',1000)
    Grafica_Acumulado('ValoresC10001000.txt',1000)
    plt.show()
