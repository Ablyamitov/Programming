import math 
def zanovo():
	a = float(input("Введите а: "))
	b= float(input("Введите b: "))
	c = float(input("Введите c: "))
	d = b*b-4*a*c
	if ((a == 0) and (b == 0) and (c == 0)):
		print("Корень - любое число")
	elif (a!=0):
		if ((b == 0) and (c == 0)):
			print("x1 = 0")
		elif (d>0):
			x1 = (-b + math.sqrt(d))/(2*a)
			x2 = (-b - math.sqrt(d))/(2*a)
			print("x1 = ",x1, "x2 =",x2)
		elif (d==0):
			x1 = -b/(2*a)
			print("x1 = ",x1)
		elif (d<0) :
			print("Нет корней")
	elif (a == 0):
		if ((b == 0) and (c != 0)):
			print("Корней нет")
		elif ((b != 0) and (c==0)):
			print("x1 = 0")
		else:
			x1 = -c/b
			print("x1 = ",x1)
	zanovo()
zanovo()
