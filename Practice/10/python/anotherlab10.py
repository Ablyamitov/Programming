s,l1,r1,l2,r2 = map(int, input("Введите s,l1,r1,l2,r2:  ").split())
x1 = l1
x2 = r2
def first(s,r1,l2,r2,x1,x2):
	if (x1 + x2 == s):
		print(x1,x2)
		return(0)
	else:
		if (x2>l2):
				x2 = x2 - 1
		elif ((x2 == l2) and (x1<r1)):
				x1 = x1 + 1
				x2 = r2
		if ((x1 == r1) and (x2 == r2)):
			if (x1 + x2 == s):
				print(x1, x2)
				return 0
			else:
				print(-1)
				return 1
		first(s,r1,l2,r2,x1,x2)
if(x1 + x2) == s:
    print(x1, x2)
else:
    first(s,r1,l2,r2,x1,x2)




