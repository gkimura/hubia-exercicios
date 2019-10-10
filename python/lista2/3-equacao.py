
while(1):
	print ("Equation: f(x)= a.x2 + b.x + c")
	a = input("Insira um valor para a: ")
	b = input("Insira um valor para b: ")	
	c = input("Insira um valor para c: ")

	delta = (int(b)*int(b))-4*int(a)*int(c)

	if (delta < 0):
		print ("Nenhuma raiz real")
	elif (delta == 0):
		print ("Uma raiz real")
	elif (delta > 0):
		print ("Duas raizes reais")


