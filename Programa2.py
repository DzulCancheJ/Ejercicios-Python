#programa 2 -- programa dos realice una funcion que permita obtener el volumen de una esfera
from math import pi
A=float(input("Ingrese el radio R de la esfera \n"))
def volumen(a):
	result= (4/3)* pi * pow(a,3)
	return result
print("El volumen de la esfera es " + str(volumen(A)))
