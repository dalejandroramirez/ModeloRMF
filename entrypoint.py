import RMFArbol

def main():
    d=int(input("ingrese el numero de hijos: "))
    h=int(input("ingrese la altura: "))
    f=RMFArbol.Porcentaje_accesibles_nary_RMF_c(d,h)
    return(f)
if __name__=='__main__':
    print(main())
