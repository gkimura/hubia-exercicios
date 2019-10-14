
def valuesort(d):
	keys = d.keys()
	values_sorted = []
	for i in sorted(keys):
		values_sorted.append(d[i])
		
	print(values_sorted)



d = {'x':1,'y':2,'a':3}
valuesort(d)
