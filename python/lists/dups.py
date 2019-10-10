def count_dups(lista):
	d = {x:lista.count(x) for x in lista}
	ndups = [x for x in d.values()]
	return ndups


