import math 
a = int(input())
b= int(input())
c = int(input())
x1 = 0
x2 = 0
d = b*b-4*a*c
if (a!=0):
	if (d>0):
		x1 = (-b + math.sqrt(d))/(2*a)
		x2 = (-b - math.sqrt(d))/(2*a)
		print("x1 = ",x1, "x2 =",x2)
	elif (d==0):
		x1 = -b/(2*a)
		print("x1 = ",x1)
	else :
		print("Нет корней")
else: 
	x1 = -c/b
	print("x1 = ",x1)
