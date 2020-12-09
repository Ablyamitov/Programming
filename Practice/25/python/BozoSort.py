import random
import math as m

def BozoSort1(a, check = True):
	sorted = False
	while(sorted == False):
		x1 = random.randint(0,len(a) - 1)
		x2 = random.randint(0,len(a) - 1)

		swap = a[x1]
		a[x1] = a[x2]
		a[x2] = swap

		sorted = True
		if (check):
			for i in range (1,len(a)):
				if (a[i-1]>a[i]):
					sorted = False
					break
		else:
			for i in range (1,len(a)):
				if (a[i-1]<a[i]):
					sorted = False
					break
	return a



def BozoSort2(a,check = True):
	help = []
	for i in range (len(a)):
		for j in range (len(a)):
			help.append(a[i][j])
	return BozoSort1(help, check)



def BozoSort3(first,second,third,check = True):
	three = []
	three.append(first)
	three.append(second)
	three.append(third)
	return BozoSort1(three, check)


n = int(input())
a = list(map(int, input().split()))
temp=[]

#Лист целых чисел
temp = BozoSort1(a)
for i in range (len(temp)):
	print(temp[i], end=" ")
print()


temp = BozoSort1(a,check = False)
for i in range (len(temp)):
	print(temp[i], end=" ")
print()


#Двумерный лист целых чисел
a2 = []
remember = 0
for i in range (int(m.sqrt(n))):
	temp1=[]
	for j in range (int(m.sqrt(n))):
		temp1.append(a[remember])
		remember+=1
	a2.append(temp1)
	if (remember>len(a)):
		break

temp = BozoSort2(a2)
for i in range (len(temp)):
	print(temp[i], end=" ")
print()


temp = BozoSort2(a2, check = False)
for i in range (len(temp)):
	print(temp[i], end=" ")
print()


#Три переменные
first = a[0]
second = a[1]
third = a[2]

temp = BozoSort3(first,second,third)
for i in range (len(temp)):
	print(temp[i], end=" ")
print()


temp = BozoSort3(first,second,third,check = False)
for i in range (len(temp)):
	print(temp[i], end=" ")
