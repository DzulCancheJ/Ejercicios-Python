#programa 10

numero=int(input("Ingresa un numero: "))
suma=0
for x in range(numero):
        resultado = pow(x+1,2)
        print(x+1,"^2 es:", resultado)
        suma+=resultado

print("La suma de los cuadrads es: ", suma)

