#Programa 4 Numero mayor de tres numeros
A=int(input("Ingrese un numero\n"))
B=int(input("Ingrese un numero\n"))
C=int(input("Ingrese un numero\n"))

def mayor(a,b,c):
	if ( A > B and A > C or A==B):
	    print("EL numero mayor es: " + str(A))
	elif( B > A and B > C or B==C):
	    print("El numero mayor es: " + str(B))
	else:
	    print("El numero mayor es: " + str(C))


mayor(A,B,C)