

def product(lista):
	prod = 1
	for elem in lista:
		prod *= elem
	return prod

def factorial(lista):
	return product(lista)

while(1):
	num = int(input("Insira um numero: "))
	lista = [x for x in range(1,num+1)]
	print ("Fatorial de ",num,"eh: ",factorial(lista))
 
