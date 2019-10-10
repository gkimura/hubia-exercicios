
def fizz_buzz(num):
	div3 = ((num%3)==0)
	div5 = ((num%5)==0)
	if(div3 and div5):
		return "FizzBuzz"
	elif (div3):
		return "Fizz"
	elif (div5):
		return "Buzz"
	else:
		return num

while(1):
	num = int(input("Insira um numero: "))
	print(fizz_buzz(num))


