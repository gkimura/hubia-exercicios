import string 

def zip(list1, list2):
	print ([(list1[i], list2[i]) for i in range(len(list1))])


def map(list1,square):
	print ([square(list1[i]) for i in range(len(list1))])
	

def filter(list1, even):
	print ([list1[i] for i in range(len(list1)) if even(list1[i]) == True ])


def triplets(n):
	print([(a,c-a,c) for c in range(2,n) for a in range(1,c//2+1)])

def enumerate(list1):
	print([(i,list1[i]) for i in range(len(list1))])

def two_dimensional_array(d1, d2):
	print([[None]*d2 for i in range(d1)]) 

def parse_csv(file_name):
	f = open(file_name)
	lines = f.readlines()
	print ([[line[:-1].split(',')] for line in lines])

def generalized_parse_csv(file_name, d, c):
	f = open(file_name)
	lines = f.readlines()
	print ([[line[:-1].split(d)] for line in lines if line[0]!=c])

def swap(word,i):
	w = list(word)
	w[i],w[i+1] = w[i+1],w[i]
	return ''.join(w)

def mutate(word):
	letters = string.ascii_lowercase
	# insert character
	mutations = [''.join([word[:i],l,word[i:len(word)]]) for i in range(len(word)) for l in letters]
	# delete character
	mutations.extend([''.join([word[:i],word[i+1:len(word)]]) for i in range(len(word))])
	# replace character
	mutations.extend([''.join([word[:i],l,word[i+1:len(word)]]) for i in range(len(word)) for l in letters])
	# swap 2 consecutive characters
	mutations.extend([swap(word,i) for i in range(len(word)-1)])
	return mutations

def nearly_equal(str1, str2):
	mutations = mutate(str2)
	if str1 in mutations:
		return True
	else:
		return False
		
	

