import functions

def square(x):
	return (x*x)

def even(x):
	return (x%2==0)

list1 = [1,2,3]
list2 = ["a","b","c"]
"""
functions.zip(list1,list2)
functions.map(list1, square)
functions.filter(list1, even)
functions.triplets(5)
functions.enumerate(list2)

d1 = int(input("Insira dimensao 1: "))
d2 = int(input("Insira dimensao 2: "))
functions.two_dimensional_array(d1,d2)

file_name = input("Insira nome de arquivo: ")
#functions.parse_csv(file_name)
d = input("Insira simbolo de separacao: ")
functions.generalized_parse_csv(file_name,d,'#') 

functions.mutate("word")
"""

while(1):
	str1 = input("Insira uma string: ")
	str2 = input("Insira outra stringl: ")
	print(functions.nearly_equal(str1,str2)) 

