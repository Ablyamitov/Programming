know =["hallo", "klempner", "das", "ist", "fantastisch", "fluggegecheimen"]
all=""
for i in range (len(know)):
    all = all + know[i]
word =list(input("Введите слово: "))
maybe = 1
for i in range (len(word)):
    if (word[i] in all):
    	multi = (all.count(word[i]))/(len(all))
    	maybe *= multi
    else:
        print(0)
        exit()
print(maybe)


