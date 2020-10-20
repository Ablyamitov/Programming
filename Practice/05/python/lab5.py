x_0 = int(input("x_0 = "))
v_0 = int(input("v_0 = "))
t = int(input("t = "))
g = 9.8
a=g
x_t = abs(x_0-(x_0 + v_0 * t - (a*t*t) / 2))
print("Объект преодолеет ",x_t," метров")

x_t = abs(x_0-(x_0 + v_0 * t - 1/2*(a*t*t)))
print("Объект преодолеет ",x_t," метров")