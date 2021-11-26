# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 09:28:04 2021

@author: digin
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import gridspec

#plt.plot(unique,counts)
#'ValoresC1000.txt'

##   capturar nombres en un txt
def Probabilidad_percolacion(nombre_archivo):
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
    return(unique,y)

def Grafica_Acumulado(nombre_archivo,h,color):
    unique,y=Probabilidad_percolacion(nombre_archivo)
    plt.plot(unique,y,"-",label="Altura {}".format(h),color=color)
    plt.xlabel('Valor C critico')
    plt.ylabel('Probabilidad Percolacio')
    plt.title("RMF Models")
    plt.legend()



def Graficar(nombre_archivos,Etiqueta):
    fig=plt.figure(figsize=(4,8))
    #plt.axes([3,0.55,0.3,0.3])
    fig.tight_layout()
    colores=["blue","green","red","black","orange"]
    i=0
    ax=plt.subplot(1,1,1)
    for j in range(0,5):
        x,y=Probabilidad_percolacion(nombre_archivos[i][j])
        if j==4:
            ax.plot(x,y,color=colores[j],linestyle='dotted')
        else:
            ax.plot(x,y,color=colores[j])
    
    plt.legend(['Altura 125','Altura 250','Altura 500','Altura 1000','Altura 2000'])
    plt.xlim(0.0,0.25)  
    plt.ylim(0,0.2)  
    ax.set_xlabel("$C_{min}$ ",fontsize=15)
    ax.set_ylabel("$\Theta_{RMF}($"+str(Etiqueta[i])+")",fontsize=15)
    plt.grid(color='k', linestyle='dotted', linewidth=1)
    plt.show()


if __name__=='__main__':
    
    #Grafica_Acumulado('ValoresCheap/ValoresC500d2concte.txt',"500 heap","g")
    #Grafica_Acumulado('ValoresCheap/ValoresC2000d2concte.txt',"2000 heap","b")
    #Grafica_Acumulado('ValoresCheap/ValoresC1000d2concte.txt',"1000 heap d2","r")
    #Grafica_Acumulado('ValoresCheap/ValoresC1000d3concte.txt',"1000 heap d3","r")
    #Grafica_Acumulado('ValoresC_L2/ValoresC_L2_h500concte.txt',500,"g")
    #Grafica_Acumulado('ValoresC_L2/ValoresC_L2_h1000concte.txt',1000,"r")
    #Grafica_Acumulado('ValoresC_L2/ValoresC_L2_h2000concte.txt',2000,"b")
    #Grafica_Acumulado('ValoresC_L2alt/ValoresC_L2alt_h100concte.txt',100,"b")
    #Grafica_Acumulado('ValoresC_L2alt/ValoresC_L2alt_h500concte.txt',500,"b")
    #Grafica_Acumulado('ValoresC_L2alt/ValoresC_L2alt_h1000concte.txt',1000,"r")
    #Grafica_Acumulado('ValoresC_L2alt/ValoresC_L2alt_h2000concte.txt',2000,"g")
    Etiqueta=["$2$-arry","$3$-arry","$\mathcal{L}_2^{alt}$","$\mathcal{L}_2$"]
    valorescd2=["ValoresCheap/ValoresC125d2concte.txt","ValoresCheap/ValoresC250d2concte.txt","ValoresCheap/ValoresC500d2concte.txt","ValoresCheap/ValoresC1000d2concte.txt","ValoresCheap/ValoresC2000d2concte.txt"]
    valorescd3=["ValoresCheap/ValoresC125d3concte.txt","ValoresCheap/ValoresC100d3concte.txt","ValoresCheap/ValoresC500d3concte.txt","ValoresCheap/ValoresC1000d3concte.txt","ValoresCheap/ValoresC2000d3concte.txt"]
    valorescL2=["ValoresC_L2/ValoresC_L2_h125concte.txt","ValoresC_L2/ValoresC_L2_h250concte.txt","ValoresC_L2/ValoresC_L2_h500concte.txt","ValoresC_L2/ValoresC_L2_h1000concte.txt","ValoresC_L2/ValoresC_L2_h2000concte.txt"]
    valorescL2alt=["ValoresC_L2alt/ValoresC_L2alt_h125concte.txt","ValoresC_L2alt/ValoresC_L2alt_h250concte.txt","ValoresC_L2alt/ValoresC_L2alt_h500concte.txt","ValoresC_L2alt/ValoresC_L2alt_h1000concte.txt","ValoresC_L2alt/ValoresC_L2alt_h2000concte.txt"]
    nombre_archivos=[valorescd2,valorescd3,valorescL2alt,valorescL2]
    Graficar(nombre_archivos,Etiqueta)
    #plt.show()
