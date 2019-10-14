


def find_anagrams(list1):
	ans= []
	marked = []

	for ind, l1 in enumerate(list1):
		aux = []
		if l1 not in marked:
			aux.append(l1)
			marked.append(l1)
			for l2 in list1[ind+1:]:
				if (l2 not in marked) and (sorted(l1)==sorted(l2)):
					aux.append(l2)
					marked.append(l2)
			ans.append(aux)
	print (ans)		

list1 = ['eat','ate','done','tea','soup','node']
find_anagrams(list1)









