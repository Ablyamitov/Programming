k = 0
often_num = 0
red_num = 0
black_num = 0
a = []
k += 1
for i in range (37):
	a.append(0)
x = int(input())
check = False
while ((x >= 0) and (x <= 36)):
	if (check == True):
		x = int(input())
	check = True
	if (x > 0 and x < 13):
		if ((x % 2 == 0 or x==11)and x != 12):
			black_num+=1
		else:
			red_num+=1
	elif (x >= 13 and x <= 24):
		if ((x % 2 == 0 or x == 19 or x == 21 or x == 23) and x!=20 and x!=22 and x!=24):
			red_num+=1
		else:
			black_num+=1
	elif ((x >= 25) and (x <= 36)):
		if ((x % 2 == 0 or x == 25 or x == 27) and x!=26 and x!=28):
			red_num+=1
		else:
			black_num+=1
	a[x] += 1
	if ((x >= 0) and (x <= 36)):
		for i in range (37):
			for j in range (37):
				if (often_num <= a[j]):
					often_num = a[j]
				else:
					continue
			if (a[i] == often_num):
				print(i, end=" ")
		print(sep="")
		for i in range (37):
			if (a[i] == 0):
				print(i,end =" ")
	print(sep="")
	if ((x>=0) and (x<=36)):
		print(red_num ,black_num)
	print(sep="")
exit(0)
