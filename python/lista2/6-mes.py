meses = ["janeiro","fevereiro","marco","abril","maio", "junho", "julho", "agosto","setembro","outubro", "novembro","dezembro"]
num = input("Insira um numero entre 1 e 12: ")
while(int(num)<1 or int(num)>12):
	num = input("Insira um numero entre 1 e 12: ")

print ("mes: ",meses[int(num)-1])
