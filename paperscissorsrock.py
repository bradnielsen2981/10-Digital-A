#repeat the above until player wants to quit
import random
#player choose a move from papers scissors rock
playermove = input("Please choose paper, scissors, or rock. Type exit to finish.")
movelist = ['paper','scissors','rock']

number_games = 0

while playermove != 'exit':

    if playermove not in movelist:
        continue #skips rest of the loop

    #computer choose a random move from paper scissor rock
    randomindex = random.randint(0,2)
    computermove = movelist[randomindex]
    print(computermove)

    #find out who wins
    if computermove == playermove:
        print("Draw")
    elif (computermove == 'rock' and playermove == 'scissors') or (computermove == 'paper' and playermove == 'rock') or (computermove == 'scissors' and playermove == 'paper'):
        print("Computer wins")
    else:
        print("You win")

    playermove = input("Please choose paper, scissors, or rock. Type exit to finish.")

    number_games = number_games + 1
    if number_games == 3:
        break