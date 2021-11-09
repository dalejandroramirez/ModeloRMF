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
def Grafica_Acumulado(nombre_archivo,h,color):
    '''Se realiza una grafica de ValoresC vs P(percolacion), esta probabilidad de percolacion
       se calcula haciendo el aculumalado de las frecuencias de percolacion con cada valor de C
    '''
    #df = pd.read_csv('ValoresCheap/'+str(nombre_archivo))
    df = pd.read_csv(str(nombre_archivo))
    df=pd.DataFrame(df)
    df=df.sort_index(axis=0, ascending=True)
    (unique, counts) = np.unique(df, return_counts=True) ##retorna un array con los numeros diferentes y sus repeticiones
    N=len(df)
    n=len(unique)
    j=1
    acum=0
    acumulado=[0]*(n+1)
    while j<=n:
        acum=acum+counts[j-1]
        acumulado[j]=acum
        j=j+1
    y=np.array(acumulado)/N
    unique=np.concatenate([[0],unique])
    #y=np.concatenate([[0],y])
    plt.plot(unique,y,"-",label="Altura {}".format(h),color=color)
    plt.xlabel('Valor C critico')
    plt.ylabel('Probabilidad Percolacio')
    plt.title("RMF Models")
    plt.legend()

    return(0)


if __name__=='__main__':
    
    Grafica_Acumulado('ValoresCheap/ValoresC500d2concte.txt',"500 heap","g")
    Grafica_Acumulado('ValoresCheap/ValoresC2000d2concte.txt',"2000 heap","b")
    Grafica_Acumulado('ValoresCheap/ValoresC1000d2concte.txt',"1000 heap d2","r")
    #Grafica_Acumulado('ValoresCheap/ValoresC1000d3concte.txt',"1000 heap d3","r")
    #Grafica_Acumulado('ValoresC_L2/ValoresC_L2_h500concte.txt',500,"g")
    #Grafica_Acumulado('ValoresC_L2/ValoresC_L2_h1000concte.txt',1000,"r")
    #Grafica_Acumulado('ValoresC_L2/ValoresC_L2_h2000concte.txt',2000,"b")
    #Grafica_Acumulado('ValoresC_L2alt/ValoresC_L2alt_h100concte.txt',100,"b")
    #Grafica_Acumulado('ValoresC_L2alt/ValoresC_L2alt_h500concte.txt',500,"b")
    #Grafica_Acumulado('ValoresC_L2alt/ValoresC_L2alt_h1000concte.txt',1000,"r")
    #Grafica_Acumulado('ValoresC_L2alt/ValoresC_L2alt_h2000concte.txt',2000,"g")
    #Grafica_Acumulado('ValoresC_L2alt/Altura1000/ValoresC_h_1000_hora_09_30_15L2.txt',1000,"r")

    plt.show()
