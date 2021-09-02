# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 14:56:05 2021

@author: digin
"""
import pandas as pd


"""se quiere graficar los resultados del proceso RMF Model, se le ingresa un archivo excel o txt"""

def graficar():
    df=pd.read_excel('C:/Users/digin/Dropbox/Mi PC (DESKTOP-F432S4K)/Documents/Maestria/RMF_archivosexcel/ValorC100.xlsx',header=None)
    print(df)

def frecuencia():
    return(0)

print(graficar())