import os
ncolumns = os.get_terminal_size().columns


def center_align(file_name):

	f = open(file_name)
	lines = f.readlines()
	
	for l in lines:
		print(l.center(ncolumns))

