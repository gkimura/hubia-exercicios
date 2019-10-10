
def showNumbers(limit):
	for i in range(limit+1):
		if((i%2)==0):
			print(i," EVEN")
		else:
			print(i," ODD")



while(1):
	num = int(input("Insira um numero: "))
	showNumbers(num)
