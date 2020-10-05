s,l1,r1,l2,r2 = map(int, input("Введите s,l1,r1,l2,r2: ").split())
x1 = l1
x2 = r2
def poehali():
	if ((x1 + x2 == s) or (x1 + l2 == s)):
		if (x1 + x2 == s):
			print(x1," ",x2)
		else:
			print(x1," ", l2)
	elif (x1 == r1):
		print("-1")
		exit(1)
	elif (x2 == l2):
		x1 = l1 + 1
		l1 = x1
		poehali()
	elif (x2 == r2):
		x2 = r2 - 1
		poehali()
poehali()





