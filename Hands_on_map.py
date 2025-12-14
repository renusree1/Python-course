number1= [1, 2, 3]
number2= [4, 5, 6]
result= map(lambda x,y: x+y, number1, number2)
print("Addition of two lists")
print(list(result))

num= [1, 2, 3, 4, 5]
def sq(x):
    return x*x
square= list(map(sq, num))
print("Square of numbers in the list")
print(square)