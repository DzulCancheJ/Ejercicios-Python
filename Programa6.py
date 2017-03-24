#Programa 6 Intervalo de la suma de los cubos de los 
# primeros n numeros

numero=int(input("Ingresa un numero: "))

def sumaCubos(x):
	suma=0
	for x in range(x):
	        resultado = pow(x+1,3)
	        print(x+1,"^3 es:", resultado)
	        suma+=resultado

	print("La suma de los cubos es: ", suma)


sumaCubos(numero)