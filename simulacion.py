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


def Graficar(nombre_archivos,Etiqueta):
    fig=plt.figure(figsize=(4,8))
    #plt.axes([3,0.55,0.3,0.3])
    fig.tight_layout()
    colores=["blue","green","red","black","orange"]
    i=4

    ax=plt.subplot(1,1,1)
    for j in range(0,5):
        x,y=Probabilidad_percolacion(nombre_archivos[i][j])
        if j==4:
            if i==1 and False:
                ax.plot(x[1:],y[1:],color=colores[j],linestyle='dotted')
            else:
                ax.plot(x,y,color=colores[j],linestyle='dotted')
            
        else:
            ax.plot(x,y,color=colores[j])
    
    plt.legend(['125','250','500','1000','2000'])
    plt.xlim(0.0,2)  
    plt.ylim(0,1)  
    ax.set_xlabel("$C_{min}$ ",fontsize=15)
    ax.set_ylabel("$\Theta_{RMF}($"+str(Etiqueta[i])+")",fontsize=15)
    plt.grid(color='k', linestyle='dotted', linewidth=1)
    plt.show()


if __name__=='__main__':
    
    Etiqueta=["$2$-arry???","$3$-arry???","$\mathcal{L}_2^{alt}$","$\mathcal{L}_2$","normal $T_2$","L2 normal"]
    valorecL2normal=["ValoresC_L2/Normal/concatenateL2/ValoresC_L2_h125concteNormal.txt","ValoresC_L2/Normal/concatenateL2/ValoresC_L2_h250concteNormal.txt","ValoresC_L2/Normal/concatenateL2/ValoresC_L2_h500concteNormal.txt","ValoresC_L2/Normal/concatenateL2/ValoresC_L2_h1000concteNormal.txt","ValoresC_L2/Normal/concatenateL2/ValoresC_L2_h2000concteNormal.txt"]
    valorecd2normal=["ValoresCheap/Normal/Concatenate_d2/ValoresC125d2concteNormal.txt","ValoresCheap/Normal/Concatenate_d2/ValoresC250d2concteNormal.txt","ValoresCheap/Normal/Concatenate_d2/ValoresC500d2concteNormal.txt","ValoresCheap/Normal/Concatenate_d2/ValoresC1000d2concteNormal.txt","ValoresCheap/Normal/Concatenate_d2/ValoresC2000d2concteNormal.txt"]
    valorescd2=["ValoresCheap/ValoresC125d2concte.txt","ValoresCheap/ValoresC250d2concte.txt","ValoresCheap/ValoresC500d2concte.txt","ValoresCheap/ValoresC1000d2concte.txt","ValoresCheap/ValoresC2000d2concte.txt"]
    valorescd3=["ValoresCheap/ValoresC125d3concte.txt","ValoresCheap/ValoresC250d3concte.txt","ValoresCheap/ValoresC500d3concte.txt","ValoresCheap/ValoresC1000d3concte.txt","ValoresCheap/ValoresC2000d3concte.txt"]
    valorescL2=["ValoresC_L2/ValoresC_L2_h125concte.txt","ValoresC_L2/ValoresC_L2_h250concte.txt","ValoresC_L2/ValoresC_L2_h500concte.txt","ValoresC_L2/ValoresC_L2_h1000concte.txt","ValoresC_L2/ValoresC_L2_h2000concte.txt"]
    valorescL2alt=["ValoresC_L2alt/ValoresC_L2alt_h125concte.txt","ValoresC_L2alt/ValoresC_L2alt_h250concte.txt","ValoresC_L2alt/ValoresC_L2alt_h500concte.txt","ValoresC_L2alt/ValoresC_L2alt_h1000concte.txt","ValoresC_L2alt/ValoresC_L2alt_h2000concte.txt"]
    nombre_archivos=[valorescd2,valorescd3,valorescL2alt,valorescL2,valorecd2normal,valorecL2normal]
    Graficar(nombre_archivos,Etiqueta)


