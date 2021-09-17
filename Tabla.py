import numpy as np
import pandas as pd

#import rmffinal
import Funcion_verificacion as rmffinal
##esta funcion ya es obsoleta viernes 19 septiembre


def Exportar_excel_Valor_C(n=None,d=None,h=None):

    """Se va a crear una lista con los valores de C
    ordenados de menos a mayor para para que
    percole"""
    if n==None:
        n= int(input("ingrese el numero de intentos que se realizará el proceso:"))
    if d==None:
        d =int(input("ingrese el numero de hijos que tendrá cada nivel: "))
    if h==None:
        h =int(input("ingrese la altura maxima que tendra el arbol: "))

    X=np.zeros(n+1)
    for i in range(1,n+1):
        X[i]=rmffinal.Funcion_verificacion(d,h)
        #X[i]=rmffinal.Porcentaje_accesibles_nary_RMF_c(d,h)
    X=np.sort(X)
    #Y=np.arange(-1/n,1,1/n)
    V={'Valores C' : X }
    df = pd.DataFrame(V, columns = ['Valores C'])
    #df.to_excel('C:/Users/digin/Dropbox/Mi PC (DESKTOP-F432S4K)/Documents/Maestria/RMF_archivosexcel/ValorC'+str(h)+'.xlsx','a',index=False,header=False) ##windows
    #df.to_excel('/media/daniel/00C240BEC240B9A4/Users/digin/Dropbox/Mi PC (DESKTOP-F432S4K)/Documents/Maestria/RMF_archivosexcel/ValorC'+str(h)+'.xlsx','a',index=False,header=False) ##linux
    df.to_excel('/media/daniel/00C240BEC240B9A4/Users/digin/Dropbox/Mi PC (DESKTOP-F432S4K)/Documents/Maestria/AlgoritmosRMF/ValorC'+str(h)+'.xlsx','a',index=False,header=False)

if __name__=='__main__':
    print(Exportar_excel_Valor_C(1000,2,2000))
