s,l1,r1,l2,r2 = map(int, input("Введите s,l1,r1,l2,r2: ").split())
if ((r1 + r2) < s):
	print(-1)
elif ((l1 + l2) > s):
	print(-1)
else:
	if (l1 + r2 - s == 0):
		print(l1,"",r2)
	elif(l1 + r2 - s<0):
		x = l1 - (l1 + r2 - s)
		print(x,"",r2)
	elif(l1 + r2 - s > 0):
		x = r2 - (l1 + r2 - s)
		print(l1,"",x)