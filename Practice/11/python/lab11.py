rez = 1
a = float(input("Введите число, которое хотите возвести в степень: "))
step = int(input("Введите степень: "))
if (step == 0):
	rez = 1
elif (step>0):
	for i in range(step):
		rez *=a
elif (step<0):
	step = -step
	for i in range(step):
		rez *= a
	rez = 1/rez
print(rez)

