

def invertdict(d):
	nd = {}
	for x,y in d.items():
		nd[y]=x
	print (nd)


d = {'x':1, 'y':2, 'z':3}
invertdict(d)
