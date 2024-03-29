# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 09:28:04 2021

@author: digin
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import gridspec

def Probabilidad_percolacion(nombre_archivo):

    df = pd.read_csv(str(nombre_archivo))
    df = pd.DataFrame(df)
    df = df.sort_index(axis=0, ascending=True)
    ##retorna un array con los numeros diferentes y sus repeticiones
    (unique, counts) = np.unique(df, return_counts=True) 
    N = len(df)
    n = len(unique)
    j = 1
    acum = 0
    acumulado = [0]*(n+1)
    while j <= n:
        acum += counts[j-1]
        acumulado[j] = acum
        j += 1
    y = np.array(acumulado)/N
    unique = np.concatenate([[0],unique])
    return(unique,y)


def Graficar(nombre_archivos,Etiqueta):

    fig = plt.figure(figsize=(4,8))
    fig.tight_layout()
    colores = ["blue", "green", "red", "black", "orange"]
    
    i=1


    
    ax = plt.subplot(1,1,1)
    for j in range(0,5):
        x,y = Probabilidad_percolacion(nombre_archivos[i][j])
        if j == 4:
            if i == 1 :
                ax.plot(x[1:], y[1:], color=colores[j], linestyle='dotted')
            else:
                ax.plot(x, y, color = colores[j], linestyle='dotted')
        else:
            ax.plot(x , y , color = colores[j])
    
    plt.legend(['h = 125','h = 250','h = 500','h = 1000','h = 2000'])
    plt.xlim(0.11,0.14)  
    plt.ylim(0,0.1)  
    ax.set_xlabel("Valores de $c$ ",fontsize=15)
    ax.set_ylabel("Proporción de casos \n con altura $h$",fontsize=15)
    plt.title("Aproximación de \n $\Theta_{RMF}\langle$" + str(Etiqueta[i])
                + ",U(0,1),c" "$ \\rangle$ ",fontsize=15)
    plt.grid(color ='k', linestyle='dotted', linewidth=1)
    plt.show()

def periodograma(nombre_archivo):
    i=0
    for j in range(3):
        df = pd.read_csv(str(nombre_archivo[j]))
        df = pd.DataFrame(df)
        df = df.sort_index(axis=0, ascending=True)
        plt.hist(df,bins=40)
    plt.show()

def intervalo_c(nombre_archivo, alpha,N):

    y = Probabilidad_percolacion(nombre_archivo)
    valoresC = y[0]
    probabilidadC = y[1]
    for i in range(N):
        if probabilidadC[i]> alpha:
            print(valoresC[i] , probabilidadC[i])
            break








if __name__ == '__main__':
    
    Etiqueta = ["$\mathbb{T}_2$","$\mathbb{T}_3$","$\mathbb{L}_{alt}^{2}$","$\mathbb{L}^2$"]

    valorescd2 = ["ValoresCheap/ValoresC125d2concte.txt","ValoresCheap/ValoresC250d2concte.txt",
                "ValoresCheap/ValoresC500d2concte.txt","ValoresCheap/ValoresC1000d2concte.txt",
                "ValoresCheap/ValoresC2000d2concte.txt"]
            
    valorescd3 = ["ValoresCheap/ValoresC125d3concte.txt","ValoresCheap/ValoresC250d3concte.txt",
                "ValoresCheap/ValoresC500d3concte.txt","ValoresCheap/ValoresC1000d3concte.txt",
                "ValoresCheap/ValoresC2000d3concte.txt"]

    valorescL2 = ["ValoresC_L2/ValoresC_L2_h125concte.txt","ValoresC_L2/ValoresC_L2_h250concte.txt",
                "ValoresC_L2/ValoresC_L2_h500concte.txt","ValoresC_L2/ValoresC_L2_h1000concte.txt",
                "ValoresC_L2/ValoresC_L2_h2000concte.txt"]
    
    valorescL2alt = ["ValoresC_L2alt/ValoresC_L2alt_h125concte.txt","ValoresC_L2alt/ValoresC_L2alt_h250concte.txt",
                    "ValoresC_L2alt/ValoresC_L2alt_h500concte.txt","ValoresC_L2alt/ValoresC_L2alt_h1000concte.txt",
                    "ValoresC_L2alt/ValoresC_L2alt_h2000concte.txt"]

    nombre_archivos = [valorescd2, valorescd3, valorescL2alt, valorescL2]


    #intervalo_c(nombre_archivos[3][4],0.99,20000)

    Graficar(nombre_archivos, Etiqueta)

