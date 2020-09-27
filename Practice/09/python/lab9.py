def convert():
	h1,znak,m1 = map(str, input("Введите время первого человека: ").split())
	if(0<=int(h1)<=23 and 0<=int(m1)<=59):
		h2,znak,m2 = map(str, input("Введите время второго человека: ").split())
		if(0<=int(h2)<=23 and 0<=int(m2)<=59):
			if (((int(h2)-int(h1) == 0) and (abs(int(m2) - int(m1))<=15)) or ((int(h2)-int(h1) == 1) and ((int(m2)+60-int(m1))<=15))):
				print("Встреча состоится")
			else: 
				print("Встреча не состоится")
		else:
			print("Вы ввели неккоректное время, попробуйте изменить значение")
			convert()
	else:
		print("Вы ввели неккоректное время, попробуйте изменить значение")
		convert()
convert()
