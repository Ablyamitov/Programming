def convert():
	print("Введите аримфетическое действие: ")
	a,b,c = map(str, input().split())
	if (b == "+"):
		print(int(a)+int(c))
	elif (b == "-"):
		print(int(a)-int(c))
	elif (b == "*"):
		print(int(a)*int(c))
	elif (b == "/"):
		if (c=="0"):
			print("На 0 делить нельзя, попробуйте изменить значение")
			convert()
		else:
			print(int(a)/int(c))
	else:
		print("Вы ввели неправильный оператор, попробуйте изменить значение")
		convert()
convert()
