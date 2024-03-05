# FUNCTIONS 
# int() - changes data to an integer
# print() - prints something on screen
# input() - get data from the user as a string
# type() - returns the type of data
# str() - change data to a string

# FUNCTIONS do something 
# FUNCTION function_name()
# colon defines the start of block of code
# tab indicates we are still in the block of code
def heroname(movie, food):
    num = len(movie)
    name = movie + food + str(num) #adds string together
    return name

#Global Variables
m = input("What was the movie you saw? ")
f = input("What was the last food you ate? ")

h = heroname(m,f)
print("Your hero name is: " + h)

# Local variables only exist inside a block of code
# Global variables exist everywhere
