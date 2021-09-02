import numpy as np
import pandas as pd

#import rmffinal
import Funcion_verificacion as rmffinal




def Exportar_excel_Valor_C():
    """Se va a crear una lista con los valores de C
    ordenados de menos a mayor para para que
    percole"""

    n= int(input("ingrese el numero de intentos que se realizará el proceso:"))

    d =int(input("ingrese el numero de hijos que tendrá cada nivel: "))

    h =int(input("ingrese la altura maxima que tendra el arbol: "))

    X=np.zeros(n+1)
    for i in range(1,n+1):
        X[i]=rmffinal.Funcion_verificacion(d,h)
        #X[i]=rmffinal.Porcentaje_accesibles_nary_RMF_c(d,h)
    X=np.sort(X)
    Y=np.arange(-1/n,1,1/n)
    V={'Valores C' : X }
    df = pd.DataFrame(V, columns = ['Valores C'])
    df.to_excel('C:/Users/digin/Dropbox/Mi PC (DESKTOP-F432S4K)/Documents/Maestria/RMF_archivosexcel/ValorC'+str(h)+'.xlsx','a',index=False,header=False)
    
    
    
    #datos=pd.read_excel(r"C:\Users\digin\Dropbox\Mi PC (DESKTOP-F432S4K)\Desktop\codigos\valoresC.xlsx",header=0)
    #writer=pd.ExcelWriter('/media/daniel/00C240BEC240B9A4/Users/digin/Dropbox/Mi PC (DESKTOP-F432S4K)/Desktop/codigos/Datosexportados/ejemplo.xlsx')
    #df.to_excel('/media/daniel/00C240BEC240B9A4/Users/digin/Dropbox/Mi PC (DESKTOP-F432S4K)/Documents/Maestria/RMF_archivosexcel/ValorC'+str(h)+'.xlsx',"a+",index=False,header=False)
    #df.to_csv('/media/daniel/00C240BEC240B9A4/Users/digin/Dropbox/Mi PC (DESKTOP-F432S4K)/Documents/Maestria/RMF_archivosexcel/ValorC'+str(h)+'.csv',index=False,header=False)
    #print(df)
    #return(len(df))
    #df.to_excel(r"/media/daniel/00C240BEC240B9A4/Users/digin/Dropbox/Mi PC (DESKTOP-F432S4K)/Documents/Maestria/RMF_archivosexcel\valoresC300.xlsx",index=False,header=False)


print(Exportar_excel_Valor_C())