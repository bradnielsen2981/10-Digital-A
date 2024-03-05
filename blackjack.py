#player choose hit to get new card or sit to not receive card
#check how much cards are worth
#repeating until player busts or sits
#dealer get cards after the player and pretty much keeps flipping until the they are equal to the player
import random

def check_value(hand):
    total = 0
    for card in hand:
        if card > 10:
            card = 10
        total = total + card
    if 1 in hand:
        if (total + 10) <= 21:
            total = total + 10
    return total

money = 1000

while money > 0:
    bet = input("How much would you like to bet? ")
    bet = int(bet)
    if bet > money:
        continue

    win = False
    #playerhand
    playerhand = []
    for i in range(2):
        cardnumber = random.randint(1,13)
        playerhand.append(cardnumber)
    print(playerhand)
    value = check_value(playerhand)
    if value == 21:
        win = True

    if win == False:
        response = input("Would you like to hit or sit? ")
        win = True
        while response != 'sit': 
            if response == 'hit':
                cardnumber = random.randint(1,13)
                playerhand.append(cardnumber)
                print(playerhand)
                #check to see what the value of the playerhand is
                value = check_value(playerhand)
                if value > 21:
                    print("Busted")
                    win = False
                    break
            else:
                print("I do not understand")
            response = input("Would you like to hit or sit? ")

        dealervalue = 0
        dealerhand = []
        while dealervalue < value:
            cardnumber = random.randint(1,13)
            dealerhand.append(cardnumber)
            dealervalue = check_value(dealerhand)
            if dealervalue > 21:
                print("Dealer busted! You win")
                win = True
                break
        if dealervalue <= 21:
            win = False
            print("Dealer won!")
        print(dealerhand)

    if win == True:
        money = money + bet
    else:
        money = money - bet


