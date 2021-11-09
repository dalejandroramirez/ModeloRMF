import glob2
import os
bandera=int(input("ingresa 1 si es el arbol 2 si es L2 y 3 si es L2alt"))
h=input("Ingrese la altura:")
if bandera==1:
    d=input("Ingrese el numero de hijos: ")
    files_names=glob2.glob("ValoresCheap/Arbol_d"+str(d)+"_h"+str(h)+"/*.txt") ##da todos los nombres en esa carpeta
    with open("ValoresC"+str(h)+"d"+str(d)+"concte.txt","w") as f:
        for file in files_names:
            with open(file) as infile:
                f.write(infile.read())
if bandera==2:
    files_names=glob2.glob("ValoresC_L2/Altura"+str(h)+"/*.txt")
    with open("ValoresC_L2_h"+str(h)+"concte.txt","w") as f:
        for file in files_names:
            with open(file) as infile:
                f.write(infile.read())

if bandera==3:
    files_names=glob2.glob("ValoresC_L2alt/Altura"+str(h)+"/*.txt")
    with open("ValoresC_L2alt_h"+str(h)+"concte.txt","w") as f:
        for file in files_names:
            with open(file) as infile:
                f.write(infile.read())
