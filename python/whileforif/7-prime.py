
def is_prime(num):
	if ((num==2) or (num==3)):
		return True
	elif ((num%2==0) or (num<2)):
		return False
	else:
		for i in range(3, int(num**0.5)+1, 2):
			if((n%i)==0):
				return False
		return True

def prime_numbers(limit):
	for i in range(0,limit+1):
		if is_prime(i):
			print (i)


while(1):
	num = int(input("Insira um numero: "))
	prime_numbers(num)
