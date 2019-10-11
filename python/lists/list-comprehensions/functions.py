

def zip(list1, list2):
	print ([(list1[i], list2[i]) for i in range(len(list1))])


def map(list1,square):
	print ([square(list1[i]) for i in range(len(list1))])
	

def filter(list1, even):
	print ([list1[i] for i in range(len(list1)) if even(list1[i]) == True ])



