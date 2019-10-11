

def min(lista):
	minimo = lista[0]
	for elem in lista:
		if (elem<minimo):
			minimo = elem
	return minimo

def max(lista):
	maximo = lista[0]
	for elem in lista:
		if (elem>maximo):
			maximo = elem
	return maximo

