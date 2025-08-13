import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(450,450)
polygon= turtle.Turtle()
no_sides= 6
lenght= 60
angle= 360.0/no_sides
for i in range(no_sides):
    polygon.backward(lenght)
    polygon.right(angle)
turtle.done()