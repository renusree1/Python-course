def add(X,Y):
    return X + Y
def sub(X,Y):
    return X - Y
def multiply(X,Y):
    return X * Y
def divide(X,Y):
    return X / Y

print("Please enter the oparation:")
print("a:- Addition")
print("s:- Subtraction")
print("m:- Multiplication")
print("d:- Division")

choice= str(input("Enter the opration using (a/s/m/d): "))

num1= int(input("Enter your first number: "))
num2= int(input("Enter your second number: "))

if choice == "a" or choice == "A":
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == "s" or choice == "S":
    print(num1, "-", num2, "=", sub(num1, num2))
elif choice == "m" or choice == "M":
    print(num1, "*", num2, "=", multiply(num1, num2)) 
elif choice == "d" or choice == "D":
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Your input is invalid! Pls try again")