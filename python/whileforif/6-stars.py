
def show_stars(rows):
	for i in range(rows):
		for j in range(i+1):
			print('*', end='')
		print('')

while(1):
	num = int(input("Insira um numero: "))
	show_stars(num)
