import numpy as np

class FileFunctions:

	def __init__(self, filename):
		self.filep = open(filename,"r")
		self.strings = None
		self.frequence = None
	
	# Texto como lista de strings
	def read_file(self):
		s = []
		for line in self.filep:
			s.extend(line.strip().split(" "))
		self.strings = s

	# Retorna individualmente cada palavra
	# Conta a quantidade de ocorrencia de cada palavra
	def count_frequence(self):
		d = {}
		for word in self.strings:
			if word in d:
				d[word]+=1
			else:
				d[word]=1
		self.frequence = d
 		
	# 10 palavras mais frequentes
	def most_frequent(self, num):
		d = self.frequence()
		return (sorted(d, key=d.get, reverse=True)[:num])

	# Retorna a media e o desvio padrao das ocorrencias
	def mean_std(self):
		dicti = self.frequence		

		total = 0		
		for key in dicti:
			total += dicti[key]
		
		values = [dicti[i] for i in dicti]
		std = np.std(values)

		return total/len(dicti), std

	# Novo arquivo eliminando todas as StopWords do texto
	def delete_stopwords(self,stpw, outfile_name):
		new_strings = []
		for word in self.strings:
			if word not in stpw.stopwords:
				new_strings.append(word)

		outfile = open(outfile_name,"w")
		for word in new_strings:
			outfile.write(word," ")

	# distancia entre duas palavras
	# hamming adaptado
	def distance_words (self, word1, word2):
		dist = 0
		for i in range(min(len(word1),len(word2))):
			if word1[i] != word2[i]:
				dist+=1
		dist += abs(len(word1)-len(word2))
		return dist

		 

class StopWords:
	def __init__(self):
		stopwords = ["a","e","o","as","os","de","para","sem","com"]
			
		

p1 = FileFunctions("test.txt")
p1.read_file()
p1.count_frequence()
print(p1.frequence)

most10 = p1.most_frequent(10)
print("Top 10 most frequent words: ",most10)

mean, std = p1.mean_std()
print("Mean: ",mean," Standard Deviation: ",std)

word1 = input("Insira uma palavra: ")
word2 = input("Insira outra palavra: ")
dist = p1.distance_words(word1,word2)
print("Distancia entre palavras: ",dist)
