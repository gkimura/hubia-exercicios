
def grep(string, file_name):
	
	infile = open(file_name,"r")
	lines = infile.readlines()

	for l in lines: 
		if l.find(string)!= -1:
			print(l)

		
