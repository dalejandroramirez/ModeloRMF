import glob2
import os
d=input("Ingrese el numero de hijos: ")
h=input("Ingrese la altura:")

files_names=glob2.glob("ValoresCheap/Arbol_d"+str(d)+"_h"+str(h)+"/*.txt") ##da todos los nombres en esa carpeta
with open("ValoresC"+str(h)+"d"+str(d)+"concte.txt","w") as f:

    for file in files_names:
        with open(file) as infile:
            f.write(infile.read())
