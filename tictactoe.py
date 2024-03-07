import turtle
turtle.bgcolor("black")
turtle_object = turtle.Turtle()
turtle_object.speed(0)
startx = -150
starty = 150

# draw a square
def square(length, column, row):
    turtle_object.goto(startx + column*length, starty - row*length)
    turtle_object.pencolor("white")
    turtle_object.pendown()
    for i in range(4):
        turtle_object.forward(length)
        turtle_object.right(90)
    turtle_object.penup()

                #row 0       #row 1        #row 2
grid = [['_','_','_'],['_','_','_'],['_','_','_']]

for row in range(3):
    for column in range(3):
        square(100, column, row)

input()

# draw a cross

# draw a circle

# draw a grid
# player1 chooses a coordinate and places a cross
# player2 chooses a coordinate and places a nought
# repeat the above until one player has three in a row (horizonatally, vertically or diagonally)

