import random as rd
import minmax
import cumulative
import unique 
import dups
import group
import sort
import reverse

tam1 = int(input("Insira tamanho de lista: "))
lista = []
for i in range(tam1):
	lista.append(rd.randrange(5))

print("Lista: ", lista)
"""
print("Minimo: ", minmax.min(lista))
print("Maximo: ", minmax.max(lista))
print("Minimo string: ", minmax.min(["am","efg","dec"]))
print("Maximo string: ", minmax.max(["am","efg","dec"]))
print("Reverso: ", reverse.reverse(lista))
print("Soma acumulada: ", cumulative.summ(lista))
print("Produto acumulado: ", cumulative.product(lista))
print("Elementos unicos: ", unique.find_uniques(lista))
print("Numero de duplicatas: ", dups.count_dups(lista))
tam2 = int(input("Insira tamanho dos grupos menores: "))
print("Agrupamento: ",group.group(lista,tam2))

lista_strings = ['python', 'perl', 'java', 'c', 'haskell', 'ruby']
print("Lista: ", lista_strings)
print("Ordenacao por tamanho de string", sort.lensort(lista_strings))
"""
print("Elementos unicos com SET: ",unique.find_uniques_with_set(lista))
