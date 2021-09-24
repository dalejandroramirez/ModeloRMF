import heaprmfmodel as heapRMF
import RMFArbol
import time

def Lista_valoresC_heap(d,h,N):
    '''Esta funcion crea la lista de los valores de C minimos
    necesarios para percolar usando heapmin'''
    hora=time.strftime("%H_%M_%S")
    file =open("ValoresCheap/ValoresC_h_"+str(h)+"_d_"+str(d)+"_hora_"+str(hora)+"Heapmin"+".txt","w")
    X=heapRMF.Ordenar_Heap(d,h,N)
    for i in range(0,N):
        file.write(str(X[i])+"\n")
    file.close()
    return(0)


def Lista_valoresC(d,h,N):
    '''Crea la lista de valores usando la convergencia lenta'''
    hora=time.strftime("%H_%M_%S")
    file =open("ValoresC_h_"+str(h)+"_d_"+str(d)+"_hora_"+str(hora)+".txt","w")
    X=RMFArbol.Ordenar(d,h,N)
    for i in range(0,N):
        file.write(str(X[i])+"\n")
    file.close()
    return(0)
