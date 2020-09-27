import math 
print("Выберите формат ввода")
print("1.Ввод через стороны")
print("2.Ввод через координаты вершин")
k = int(input())
if (k==1):
	print("Введите значение стороны a: ", end="")
	a = float(input())
	if (a<=0):
		print("А НУ БЫСТРО ВВЕДИ ПРАВИЛЬНОЕ ЗНАЧЕНИЕ")
	else:
		print("Введите значение стороны b: ", end="")
		b = float(input())
		if (b<=0):
			print("А НУ БЫСТРО ВВЕДИ ПРАВИЛЬНОЕ ЗНАЧЕНИЕ")
		else :
			print("Введите значение стороны c: ", end="")
			c = float(input())
			if (c<=0):
				print("А НУ БЫСТРО ВВЕДИ ПРАВИЛЬНОЕ ЗНАЧЕНИЕ")
			elif (a+b<c):
				print("А НУ БЫСТРО ВВЕДИ ПРАВИЛЬНОЕ ЗНАЧЕНИЕ")
			else:
				p = (a+b+c)/2
				S = math.sqrt(p*(p-a)*(p-b)*(p-c))
		print("S =", S)
elif (k == 2):
	print ("Введите координату вершины A: ", end="")
	x1,y1 = map(float, input().split())
	print ("Введите координату вершины B: ", end="")
	x2,y2 = map(float, input().split())
	if ((x2 == x1) and (y1==y2)):
		print("А НУ БЫСТРО ВВЕДИ ПРАВИЛЬНОЕ ЗНАЧЕНИЕ")
	else:
		print ("Введите координату вершины C: ", end="")
		x3,y3 = map(float, input().split())
		if (((x3 == x2) and (y3 == y2)) or ((x3 == x1) and (y3 == y1))):
			print("А НУ БЫСТРО ВВЕДИ ПРАВИЛЬНОЕ ЗНАЧЕНИЕ")
		else:
			a = math.sqrt((x2-x1)**2+(y2-y1)**2)
			b = math.sqrt((x3-x2)**2+(y3-y2)**2)
			c = math.sqrt((x3-x1)**2+(y3-y1)**2)
			p = (a+b+c)/2
			S = math.sqrt(p*(p-a)*(p-b)*(p-c))
			print("S =", S)








