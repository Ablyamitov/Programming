#алгоритм такой же, как и в с++, но не понимаю, почему не работает(согласен, код ужасный)???
import random
f = 0
a = 1
check = True
n = int(input())
allpassword = []
password = str(input())
notall=""
size_password = len(password)
notpassword =[size_password]
for i in range (size_password):
	notpassword.append(0)
alll = ""
for i in range (1,size_password+1):
	a*=i
for i in range (size_password):
	for j in range (n):
		notall += password[i]
	notpassword[i] = notall
	notall =""
allpassword =[a]
if(size_password<n):
	for j in range (a):
		check = True
		for i in range (n):
			x = random.randint(0,size_password-1)
			alll += password[x]
		allpassword.append(alll)
		alll = ""
		if (j>0):
			for i in range (j):
				if (allpassword[i]==allpassword[j]):
					check = False
					allpassword[j] =""
					break
				else:
					continue
		for h in range (size_password):
			if (allpassword[j]==notpassword[h]):
				check = False
				allpassword[j]=""
				break
			else:
				continue
		if(check):
			print(allpassword[j])
		else:
			j=j-1
			continue
else:
	for j in range (a):
		check = True
		for i in range (n):
			x = random.randint(0,size_password-1)
			alll+=password[x]
		allpassword[j]=alll
		for h in range(j):
			if (allpassword[j]==notpassword[h]):
				check =False
				allpassword[j] =""
				alll=""
				break
			else:
				continue
			if (check == False):
				break
		if (check == True):
			for t in range (j):
				if (allpassword[t]==allpassword[j]):
					check = False
					allpassword[j]=""
					alll = ""
					break
			if (check == True):
				print(allpassword[j]," ", end="")
				alll = ""
			else:
				j-=1
				continue









