height= float(input("Enter your height in cm: "))
weight= float(input("Enter your weight in kg: "))
calculation= weight/(height/100)**2
print("Your BMI is- ", calculation)
if calculation<= 18.4:
    print("You are underweight")
elif calculation <= 24.9:
    print("You are healthy")
elif calculation <= 29.9:
    print("You are overweight")
elif calculation<= 34.9:
    print("You are severly overweight")
elif calculation<= 39.9:
    print("You are obese")
else:
    print("You are severly obese")