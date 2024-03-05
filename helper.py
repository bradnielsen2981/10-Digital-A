import math #imports the math library
import mylib

print(mylib.cherry)

def add_two_numbers(num1,num2):
    total = num1 + num2
    return total

def hypot(a,b):
    csquared = a*a + b*b
    c = math.sqrt(csquared)
    return c

def area_of_circle(radius):
    area = radius**2 *math.pi
    return area

print(area_of_circle(5))






