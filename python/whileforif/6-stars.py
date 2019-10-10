
def show_stars(rows):
	for i in range(1,rows+1,1):
		for j in range(i):
			print('*', end='')
		print('')

while(1):
	num = int(input("Insira um numero: "))
	show_stars(num)
