#Programa 8

numero=int(input("Ingresa un numero: "))

def rango(X):
	for x in range(X):
	        resultado= x+1
	        if (resultado>=20 and resultado<=60):
	            print(resultado)

rango(numero)

