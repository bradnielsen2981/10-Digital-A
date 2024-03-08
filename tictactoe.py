import turtle
turtle.bgcolor("black")
turtle_object = turtle.Turtle()
turtle_object.speed(0)
startx = -150
starty = 150 

# draw circle
def circle(length, column, row):
    turtle_object.goto(startx + column*length + 50, starty - row*length - 100)
    turtle_object.pendown()
    turtle_object.pencolor("green")
    turtle_object.pensize(5)
    turtle_object.circle(length/2)
    turtle_object.penup()
    return

#cross function and test it
def cross(length, column, row):
    turtle_object.setheading(0)
    turtle_object.goto(startx + column*length, starty - row*length)
    turtle_object.pendown()
    turtle_object.pencolor("red")
    turtle_object.pensize(5)
    turtle_object.right(45)
    turtle_object.forward(120)
    turtle_object.penup()
    return

# draw a square
def square(length, column, row):
    turtle_object.pensize(2)
    turtle_object.goto(startx + column*length, starty - row*length)
    turtle_object.pencolor("white")
    turtle_object.pendown()
    for i in range(4):
        turtle_object.forward(length)
        turtle_object.right(90)
    turtle_object.penup()

        #row 0 #row 1 #row 2
grid = [['_','_','_'],
        ['_','_','_'],
        ['_','_','_']]

for row in range(3):
    for column in range(3):
        square(100, column, row)


turn = 1
while True:
    move = input("Please type your column and your row separated by a space: ")
    if move == 'exit':
        break
    move = move.split()
    column = int(move[0]) - 1 #1
    row = int(move[1]) - 1 #1
    if grid[row][column] != 0:
        print("square is already taken")
        continue #skip the rest of the loop

    #turn
    grid[row][column] = turn

    win = False
    #horizontal victory
    for row in grid:
        if row[0] == row[1] == row[2]:
            print("Player", turn, "wins!")
            win = True
    #vertical victory
    for c in range(3):
        if grid[0][c] == grid[1][c] == grid[2][c]:
            print("Player", turn, "wins!")
            win = True
    if win:
        break
    if turn == 1:
        cross(100, column, row) #draw a circle
        turn = 2
    elif turn == 2:
        circle(100, column, row)
        turn = 1
    


