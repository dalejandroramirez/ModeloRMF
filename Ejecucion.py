import Crearlistas

bandera = int(input("ingresa 1 si es el arbol 2 si es L2 y 3 si es L2alt"))
N = int(input("Ingrese el numero de repeticiones: "))
m = int(input("Ingrese el numero de archivos a crear"))
if bandera == 1:
    d = int(input("Ingrese el numero de hijos: "))
    
h = int(input("Ingrese la altura: "))

if bandera == 1:
    for i in range(0,m):
        Crearlistas.Lista_valoresC_heap(d,h,N)
elif bandera == 2:
    for i in range(0,m):
        Crearlistas.Lista_valoresC_L2(h,N)
elif bandera == 3:
    for i in range(0,m):
        Crearlistas.Lista_valoresC_L2alt(h,N)