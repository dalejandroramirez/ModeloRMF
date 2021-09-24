import glob2
import os
files_names=glob2.glob("ValoresCheap/Arbol_d2_h100/*.txt")
print(files_names)
with open("ValoresC100d2concte.txt","w") as f:
    for file in files_names:
        with open(file) as infile:
            f.write(infile.read()+'\n')
            f.sort()
