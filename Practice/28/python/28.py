def checknumber(a,b):
	if (a>1):
		if (a%b == 0):
			return True
	return False

def print_factorization(n: int) ->None:
	checkall = True
	Simple = 2
	while(checkall == True):
		count = 0
		checkCount = checknumber(n, Simple)
		while(checkCount):
			count +=1
			n = n/Simple
			checkCount = checknumber(n, Simple)
		if (count > 0):
			print(Simple, end="")
			if (count > 1):
				print('^',count, end="", sep="")
			if (n>1):
				print('*', end="")
		Simple+=1
		if(n<=1):
			checkall = False

n = int(input())
print_factorization(n)

