import math
n = int(input("Введите число: "))
x = 0
k=0
while (2**x <= n):
	k=k+1
	x=x+1
print("Количество подходящих чисел х:",k)
