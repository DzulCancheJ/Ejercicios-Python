#Programa 7 Intervalo de cuadrados de n numeros mayores a 100

numero=int(input("Ingresa un numero: "))
for x in range(numero):
        resultado = pow(x+1,2)
        if resultado>100:
            print(x+1,"^2 es:", resultado)


