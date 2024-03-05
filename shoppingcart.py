print("Hello World")

#creating variables
apple = 2.50    #float        
num_of_apples = 100  #integer - int
out_of_money = False    #boolean (True or False) - bool
message = "The cost is: " #string of character - str
print(type(message))

#print(appl) - Name Error means you referred to a variable that does not exit
num_of_apples = input("How many apples: ")

# cost = num_of_apples*apple - Type Error means you referred to a variable with the wrong data type.
print(type(num_of_apples))


num_of_apples = int(num_of_apples) #changes into an integer

cost = num_of_apples*apple
print(cost)
