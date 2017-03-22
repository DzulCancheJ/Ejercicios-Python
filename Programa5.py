#--programa 5 rotar una lista de n numeros


lista=int(input("Ingresa un numero (<=0 para terminar): "))
ins = []
while lista > 0:
   ins.append(lista)
   lista=int(input("Ingresa un numero (<=0 para terminar): "))


# Mostramos el resultado*
print("Elementos rotados")
print ("Rotacion",ins)

#creacion de un funcion
def rotate(l, n):
    return l[n:] + l[:n]
    #concatenamos la lista
    #recibe la misma lista cada vez solo toma dependiendo de n dado
    #[3,2,5,7]
    # l[n:] lo que realiza es imprimir despues de la posicion dada
    # l[:n] toma el elemento dado en la posision y va antes 
    #rotacion y= 1  > [2,5,7] + [3] = [2,5,7,3]
    #rotacion y=2 > [5,7] + [3,2] = [5,7,3,2]

x=len(ins) -1
y=1
while  y <= x:
    print ("Rotacion", rotate(ins,y))
    y=y+1
    
    


