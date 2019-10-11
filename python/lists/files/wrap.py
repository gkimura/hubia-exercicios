

def wrap(file_name, width):

	f = open(file_name)
	lines = f.readlines()

	for l in lines:
		aux = l
		while (len(aux)>width):
			print (aux[:width])
			aux = aux[width:]
		print (aux)


def wrap(file_name, width):
	
	f = open(file_name)
	lines = f.readlines()

	for l in lines: 
		aux = l 
		while(len(aux)>width):
			
			
		
