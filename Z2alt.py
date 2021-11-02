import numpy as np
import random



def valorc(nd,etiqueta_hijo):
    """nd es un diccionario con key su ubicacion y argumento (valorc, Etiqueta)"""
    if nd[1]<etiqueta_hijo+nd[0]:
        return(nd[0])
    else: 
        return(nd[1]-etiqueta_hijo)

def L2(h):
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

def padres(i,num_hijos):
    """Busca los papas de el hijo i """
    if i == 0:
        return([0])
    elif i==1:
        return([0,1])
    elif i==num_hijos-2:
        return([num_hijos-4,num_hijos-3])
    elif i==num_hijos-1:
        return([num_hijos-3])
    else:
        return[i-2,i-1,i]

def valorcalt(i,etiqueta_hijo,Papas,num_hijos):
    """Busca el valor C mas pequeño necesario para llevar al hijo i
    entonces primero busca el valor C necesario de los papas
    y luego busca el minimo C necesario para llegar hasta i"""
    ubicacion_papa=padres(i,num_hijos)
    valorc_i=1
    for j in ubicacion_papa:
        if Papas[j][1]< etiqueta_hijo+Papas[j][0]:
            valorc_i=min(Papas[j][0],valorc_i)
        else :
            valorc_i=min(Papas[j][1]-etiqueta_hijo,valorc_i)
    return(valorc_i)

def L2alt(h):
    Cfin=1
    nivel=1
    Papas=[[0,random.uniform(0,1)]]
    Hijos=[]
    while nivel<h:
        num_hijos=2*nivel +1
        if num_hijos==3:
            papa_etiqueta=Papas[0][1]
            random.uniform(0,1)
            etiquetas=[random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)]
            hijo_1=[max(0,papa_etiqueta-etiquetas[0]),etiquetas[0]]
            hijo_2=[max(0,papa_etiqueta-etiquetas[1]),etiquetas[1]]
            hijo_3=[max(0,papa_etiqueta-etiquetas[2]),etiquetas[2]]
            Hijos=[hijo_1,hijo_2,hijo_3]
            Papas=Hijos
            Hijos=[]
            nivel+=1
        else :
            Hijos=[[0,random.uniform(0,1)] for _ in range(0,num_hijos)]
            for i in range(num_hijos):
                Hijos[i][0]=round(valorcalt(i,Hijos[i][1],Papas,num_hijos),3)
            Papas=Hijos
            Hijos=[]
            nivel+=1
        if nivel==h:
            N=len(Papas)
            for j in range(N):
                Cfin=min(Papas[j][0],Cfin)
    return(Cfin)

def Ordenar_L2alt(h,N):
    X=[L2alt(h) for i in range(0,N)]
    X.sort()
    return(X)

def Ordenar_L2(h,N):
    X=[L2(h) for i in range(0,N)]
    X.sort()
    return(X)


if __name__=="__main__":
    pass

        



