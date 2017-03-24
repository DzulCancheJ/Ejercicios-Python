#Programa 9
import math
a=float(input("ingrese un cateto: "))
b=float(input("ingrese el otro cateto: "))

def calcular(A,B):
	c=math.sqrt((A*A+B*B))
	print(str(c))


calcular(a,b)