
def mult35(limit):
	summ = 0
	for i in range(limit+1):
		if((i%3==0)or(i%5==0)):
			summ += i
	return summ

while(1):
	num = int(input("Insira um numero: "))
	print("Soma dos multiplos de 3 e 5: ", mult35(num))
