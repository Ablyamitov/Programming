a = int(input("Введите значение а: "))
b = int(input("Введите значение b: "))
t=a
a=b
b=t
print("a = ",a)
print("b = ",b)

#далее без доп.переменной

a = int(input("Введите значение а: "))
b = int(input("Введите значение b: "))
a,b=b,a
print("a = ",a)
print("b = ",b)