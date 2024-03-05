# mastermind choose a code of 4 colours (no repeats) from red, green, blue, yellow, white, and black
# player chooses a code of 4 colours from list above
# player receives feedback saying how many are in the mastermind code, how many are in the correct sequence as well
# player repeats the above until they either guess the code or they run out of lives (7)
print("\033c")

playercode = ""
num_lives = 7
mastermindcode = input("Please choose 4 colours from red, green, blue, yellow, white and black with a space between each colour: ")
mastermindcode = mastermindcode.split(" ")
print() # do this 10 times
while playercode != mastermindcode:
    playercode = input("Please choose 4 colours from red, green, blue, yellow, white and black with a space between each colour: ")
    playercode = playercode.split(" ")
    if playercode == mastermindcode:
        print("Well done! You have survived")
        continue
    num_correct = 0
    num_sequence = 0
    for colour in mastermindcode:
        for playercolour in playercode:
            if colour == playercolour:
                num_correct = num_correct + 1
    print("You got this number correct: ", num_correct)
    for index in range(4):
        colour = mastermindcode[index]
        playercolour = playercode[index]
        if colour == playercolour:
            num_sequence = num_sequence + 1
    print("You got this number in the correct sequence:", num_sequence)
    num_lives = num_lives - 1
    if num_lives < 0:
        print("You are a failure and must be executed!")
        break
print("Game over")