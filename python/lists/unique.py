

def find_uniques(lista):
	aux = [lista[0]]
	for elem in lista:
		if elem not in aux: 
			aux.append(elem)
	return aux

def find_uniques_with_set(lista):
	return set(lista)







