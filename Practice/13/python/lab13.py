import math 
n = int(input("Введите число: "))
if n>1:
	for i in range (2,int(n**0.5)+1):
		if (n%i == 0):
			print("Составное")
			exit()
	print("Простое")