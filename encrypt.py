
         #a -> 0
alpha = 'abcdefghijklmnopqrstuvwxyz' #string is a list []

def place_of_letter(letter):
    for place in range(26):
        if letter == alpha[place]:
            return place
    return -1

#cat
shift = 10
message = input("Please enter your message: ")
new_message = ""
for letter in message:
    if letter == " ":
        new_message = new_message + " "
    else:
        place = place_of_letter(letter)
        new_place = (place + shift)%26
        new_letter = alpha[new_place]
        new_message = new_message + new_letter

print(new_message)