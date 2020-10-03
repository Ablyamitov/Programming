def zanovo():
	import random
	n = random.randint(0,100)
	for i in range (0,4):
		mb = int(input("Введите предполагаемое число: "))
		if (mb == n):
			print("Поздравляю! Вы угадали")
			k = int(input("Хотите начать сначала? (1 - ДА ): "))
			if (k == 1):
				zanovo()
			else:
				exit(1)
		elif (mb >= n):
			if (i==4):
				break
			else:
				print("Загаданное число меньше")
		elif (mb <= n):
			if (i==4):
				break
			else:
				print("Загаданное число больше")
	print("Вы проиграли. Было загадано:",n)
	k = int(input("Хотите начать сначала? (1 - ДА ): "))
	if (k == 1):
		zanovo()
	else:
		exit(1)
zanovo()


