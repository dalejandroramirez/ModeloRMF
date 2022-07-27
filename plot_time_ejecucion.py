from cProfile import label
from turtle import color
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import numpy as np

def curva_L2(h):
    return 0.000005*h**2 - 0.000709*h + 1.080569

def curva_L2alt(h):
    return 0.000007*h**2 + 0.000209*h + 0.855804


def curva_heap(h):
    return 0.000001*h**2+0.004108*h+0.802942

def curva_arbol(h):
   return 0.000006*h**2+0.002011*h+0.919197


def curva_heap(h):
    return 0.0009*h+1.35

def curva_arbol(h):
   return 0.000005*h**2+0.003151*h+0.5274



def tiempo_ejecucion_arbol():

    X = [100, 200, 300, 400, 500, 600, 700, 1000, 2000]

    X_bajo = [10, 20, 40, 80, 160]

    T_Heap = [1.29,1.18,1.54,2.17,2.25,1.59,1.74,2.73,3.0]

    T_Heap_bajo = [1.013, 1.027, 1.050, 1.141, 1.465]

    T_Arbol = [1.06,1.44,2.12,2.40,2.95,3.72,5.0,9.08,25.9]

    T_Arbol_bajo = [1.002,1.010,1.035,1.117,1.322]

    L2 = [5.919, 6.509, 9.119, 19.811, 74.153]

    L2alt = [6.959, 7.315, 12.546, 35.739, 140.397]

    plt.scatter(X,T_Heap,marker="v",label = "$\mathbb{T}_2$ con Prioridad")

    plt.scatter(X,T_Arbol,marker="o",label = "$\mathbb{T}_2$ con Profundidad")
    plt.legend()
    plt.xlabel("Altura")
    plt.ylabel("Segundos")
    plt.title("Tiempo de Ejecución")
    x = range(100,2000)
    plt.plot(x,[curva_heap(i) for i in x],"--", color="blue")
    plt.plot(x,[curva_arbol(i) for i in x],"--",color="orange")
    plt.show()

def tiempo_ejecucion_L2():

    X = [125,250,500,1000,2000]

    X_bajo = [10, 20, 40, 80, 160]

    L2 = [1.088, 1.212, 1.766, 4.977, 17.850]

    L2alt = [1.147, 1.365, 2.502, 8.690, 30.928]

    plt.scatter(X, L2, marker="v",label = "$\mathbb{L}^2$")

    plt.scatter(X, L2alt, marker="o",label = "$\mathbb{L}^2_{alt}$")
    plt.legend()
    plt.xlabel("Altura")
    plt.ylabel("Segundos")
    plt.title("Tiempo de Ejecución")
    x = range(125,2000)
    plt.plot(x,[curva_L2(i) for i in x],"--", color="blue")
    plt.plot(x,[curva_L2alt(i) for i in x],"--",color="orange")
    plt.show()

#print(tiempo_ejecucion_L2())
print(tiempo_ejecucion_arbol())

#1.207 1.543 3.275 8.558 26.956 arbol
#1.348 1.911 1.941 6.445 11.849 heap