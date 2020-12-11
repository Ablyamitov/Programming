import random


def Coutline(a, maxx, remember):
	for remember in range (remember, maxx):
		print(a[remember], end=" ")
	print()


def BozoSort(a, maxx):
	sorted = False
	while(sorted == False):
		x1 = random.randint(0,maxx-1)
		x2 = random.randint(0,maxx-1)

		swap = a[x1]
		a[x1] = a[x2]
		a[x2] = swap

		sorted = True
		for i in range (1,maxx):
			if (a[i-1]<a[i]):
				sorted = False
				break
	return a


n = int(input())
a = list(map(int, input().split()))
line =[]
temp=[]
maxx = 0
remember = 0
t = 0
for i in range (n):
	line.append(a[t])
	t+=1
	maxx+=1
	if (maxx<=5):
		temp = BozoSort(line, maxx)
		Coutline(temp,maxx, remember)
	else:
		remember = maxx - 5
		temp = BozoSort(line, maxx)
		Coutline(temp, maxx, remember)
