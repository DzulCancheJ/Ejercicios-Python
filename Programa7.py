#Programa 7 Intervalo de cuadrados de n numeros mayores a 100

numero=int(input("Ingresa un numero: "))

def intervalo(X):
	for x in range(X):
	        resultado = pow(x+1,2)
	        if resultado>100:
	            print(x+1,"^2 es:", resultado)

intervalo(numero)