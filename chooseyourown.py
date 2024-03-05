import random

money = 0
key = False
death = False

choice = input("You come across a rock. 1. Pick it up. 2. Leave it be. ")
choice = int(choice)
if choice == 1:
    print("You found a key.")
    if True:
        key = True # variable only exists in its block  
elif choice == 2:
    print("Being careful is important.")

choice = input("You meet a ogre. The ogre asks how old you think he is?")
choice = int(choice)
if choice < 5:
    print("Ogre gets angry and hits you with his club. You die.")
    death = True
elif choice > 70:
    print("Ogre gets angry and hits you with his club. You die.")
    death = True
else:
    print("You run to a doorway!")
    if key:
        print("You put in the key, and go to safety.")
    else:
        print("You should have picked up the rock you loser.")
        print("You dead!")
        death = True    

if death == False:
    choice = input("Inside the room, is a red dragon. 1. Run away. 2. Fight")
    choice = int(choice)
    if choice == 2:
        input("Press enter to roll. You must roll > 3 to live. ")
        roll = random.randint(1,6)
        print("You have rolled a " + str(roll))
        if roll > 3:
            print("You have won a glorius battle. The dragon bows to your supremacy. You will live on legend")
        else:
            print("you should never fight a dragon. You have been burnt to ash. You loser. You dead!!")
    elif choice == 1:
        print("You live to run another day!!")







