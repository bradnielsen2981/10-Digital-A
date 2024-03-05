import turtle
turtle.bgcolor("black")
turtle.colormode(255)
turtle_object = turtle.Turtle()
turtle_object.speed(100)
turtle_object.goto(0,0)
turtle_object.pencolor("white")

def shape(length, num_sides, colour):
    turtle_object.pendown()
    turtle_object.fillcolor(colour)
    turtle_object.begin_fill()
    for count in range(num_sides):
        turtle_object.forward(length)
        angle = int(360/num_sides)
        turtle_object.right(angle)
    turtle_object.penup()
    turtle_object.end_fill()
    return

length = 200   
for a in range(360,0,-1):
    length = length - 5 
    shape(length, 5, ((255-length)%255,0,0))
    turtle_object.right(10)

input()




