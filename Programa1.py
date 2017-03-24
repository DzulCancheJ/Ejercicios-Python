#programa 1 realice un programa o funcion que permite obtener la media de tres 

A=float(input("ingrese un numero\n"))
B=float(input("ingrese otro numero\n"))
C=float(input("ingrese un nuemero\n"))

def promedio (a,b,c):
	result= (A + B + C)/3
	return result

print("El promedio es " + str(promedio(A,B,C)))
