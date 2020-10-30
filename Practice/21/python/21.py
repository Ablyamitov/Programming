def BMI(weight: float, height: float) -> float:
    return weight / (height * height / 10000)
def print_BMI(BMI: float) -> float:
    if (BMI < 18.5):
        print("Underweight")
    elif ((BMI >= 18.5) and (BMI < 25)):
        print("Normal")
    elif ((BMI >= 25) and (BMI < 30)):
        print("Overweight")
    else:
        print("Obesity") 
ves, rost = map(float,input().split())
print_BMI(BMI(ves, rost))