#не знаю почему, но код не работает, извините, что такой дурацкий код, по другому никак не умею...
maxPrice = 0
max_counter_v = 1
check_counter = 0
n=int(input())
k = int(input())
counter = []
ifcheck1=[]
check=[]
counter_name=[]
arrPrice=[]
arrV=[]
for i in range(k):
	counter.append(0)
	check.append(0)
	counter_name.append(0)
mmult=[]
arrName=[]
for i in range (k):
	Name,Price,V=input().split()
	Price,V=int(Price), int(V)
	arrName.append(Name)
	arrPrice.append(Price)
	arrV.append(V)
for i in range (k):
	if (n>=arrPrice[i]):
		rePrice  = arrPrice[i]
		c=rePrice
		mult=0
		v_all = 0
		counter_Name = 0
		for rePrice in range (n+1):
			v_all+=arrV[i]
			mult+=arrPrice[i]
			counter_Name+=1
			rePrice+=c
		counter[i]=v_all
		mmult.append(mult)
		counter_name.append(counter_Name)
		continue
	else:
		counter.append(0)
		mmult.append(n)
		continue
for i in range (k):
	if (max_counter_v<=counter[i]):
		max_counter_v = counter[i]
	else:
		continue
for i in range (k):
	if (counter[i]==max_counter_v):
		check[i]+=1
		remember = i
		check_counter = check_counter+2
	else:
		continue
if (check_counter == 1):
	print(arrName[remember]," ",counter_name[remember])
	print(counter[remember])
	print(n-mmult[remember])
elif (check_counter == 0):
	print(-1)
else:
	for i in range (k):
		if (check[i]==1):
			ifcheck1.append(n-arrPrice[i])
		else:
			continue
	for i in range (k):
		if(maxPrice<=ifcheck1[i]):
			maxPrice=ifcheck1
			remember=i
	print(arrName[remember]," ",counter_name[remember])
	print(counter[remember])
	print(n-mmult[remember])



