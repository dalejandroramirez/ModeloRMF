import glob2
import os
files_names=glob2.glob("ValoresCheap/Arbol_d2_h1000/*.txt") ##da todos los nombres en esa carpeta
with open("ValoresC1000d2concte.txt","w") as f:

    for file in files_names:
        with open(file) as infile:
            f.write(infile.read())
