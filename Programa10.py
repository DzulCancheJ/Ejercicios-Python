#programa 10

numero=int(input("Ingresa un numero: "))

def suma(X):
	suma=0
	for x in range(X):
	        resultado = pow(x+1,2)
	        print(x+1,"^2 es:", resultado)
	        suma+=resultado

	print("La suma de los cuadrads es: ", suma)

suma(numero)

