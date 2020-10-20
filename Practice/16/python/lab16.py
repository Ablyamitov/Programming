k = True
n = int(input("Введите количество билетов: "))
ticket = ""
x = input("Введите билеты").split()
for d in range(len(x)):
    if ((x[d][0] == 'a') and (x[d][4] == '5') and (x[d][5] == '5') and (x[d][6] == '6') and (x[d][7] == '6') and (x[d][8] == '1')):
         a = [x[d]]
         ticket = ticket + a[0] + ' '
         k = False
    else:
         continue
if (k):
    print(-1)
else: print(ticket)
