def istok():
	rez = 1
	n = int(input("Введите факториал: "))
	if (n==0):
		rez = 1
	elif (n>0):
		for i in range (1,n+1):
			rez*=i
	else:
		print("Нужно ввести неотрицательное число, попробуйте изменить значение")
		istok()
	print(rez)
istok()
