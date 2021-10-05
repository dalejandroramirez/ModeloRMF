import Crearlistas
N= int(input("Ingrese el numero de repeticiones: "))
m=int(input("Ingrese el numero de archivos a crear"))
d=int(input("Ingrese el numero de hijos: "))
h=int(input("Ingrese la altura: "))

for i in range(0,m):
    Crearlistas.Lista_valoresC_heap(d,h,N)
    
