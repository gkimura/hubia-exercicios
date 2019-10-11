import functions

def square(x):
	return (x*x)

def even(x):
	return (x%2==0)

list1 = [1,2,3]
list2 = ["a","b","c"]

#functions.zip(list1,list2)
#functions.map(list1, square)
functions.filter(list1, even)

