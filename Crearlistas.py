import heaprmfmodel as heapRMF
import RMFArbol
import Z2alt
import time

def Lista_valoresC_heap(d,h,N):
    '''Esta funcion crea la lista de los valores de C minimos
    necesarios para percolar usando heapmin'''
    hora = time.strftime("%H_%M_%S")
    file =open("ValoresCheap/Arbol_d"+str(d)+"_h"+str(h)+"/ValoresC_h_"+str(h)+"_d_"+str(d)+"_hora_"+str(hora)+"Heap"+".txt","w")
    X = heapRMF.Ordenar_Heap(d,h,N)
    for i in range(0,N):
        file.write(str(X[i])+"\n")
    file.close()
    return(0)

def Lista_valoresC(d,h,N):
    '''Crea la lista de valores usando la convergencia lenta'''
    hora = time.strftime("%H_%M_%S")
    file = open("ValoresCheap/ValoresC_h_"+str(h)+"_d_"+str(d)+"_hora_"+str(hora)+"Deque"+".txt","w")
    X = RMFArbol.Ordenar(d,h,N)
    for i in range(0,N):
        file.write(str(X[i])+"\n")
    file.close()
    return(0)

def Lista_valoresC_L2(h,N):
    '''Esta funcion crea la lista de los valores de C minimos
    necesarios para percolar en L2'''
    hora = time.strftime("%H_%M_%S")
    file = open("ValoresC_L2/Altura"+str(h)+"/ValoresC_h_"+str(h)+"_hora_"+str(hora)+"L2"+".txt","w")
    X = Z2alt.Ordenar_L2(h,N)
    for i in range(0,N):
        file.write(str(X[i])+"\n")
    file.close()
    return(0)

def Lista_valoresC_L2alt(h,N):
    '''Esta funcion crea la lista de los valores de C minimos
    necesarios para percolar en L2'''
    hora = time.strftime("%H_%M_%S")
    file = open("ValoresC_L2alt/Altura"+str(h)+"/ValoresC_h_"+str(h)+"_hora_"+str(hora)+"L2"+".txt","w")
    X= Z2alt.Ordenar_L2alt(h,N)
    for i in range(0,N):
        file.write(str(X[i])+"\n")
    file.close()
    return(0)
