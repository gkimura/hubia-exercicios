
def speed_control(speed):
	if (speed<70):
		print("Ok.")
	else:
		over = speed-70
		points = over/5
		if (points>12):
			print("Licence suspended.")
		else:
			print("Points: ",points)


while(1):
	num = int(input("Insira a velocidade: "))
	speed_control(num)
