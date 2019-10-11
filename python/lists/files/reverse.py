

def reverse_file(file_name):
	
	infile = open(file_name, "r")
	strings = infile.readlines()
	strings.reverse()
	
	for s in strings:
		print (s)	

	infile.close()
	

def reverse_lines(file_name):

	infile = open(file_name, "r")
	strings = infile.readlines()
	
	for s in strings: 
		print (s[::-1])

	infile.close()


	

