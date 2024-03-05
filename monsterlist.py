import random
#                0         1        2        3        4     
monsterlist = ['frog','panther','troll','vampire','dragon']
'''for i in range(5):
    print(monsterlist[i])
monsterlist.append('werewolf')
monsterlist.remove('panther')
for m in monsterlist:
    print(m)'''
random_number = random.randint(0,len(monsterlist)-1)
m = monsterlist[random_number]
print("Welcome brave fighter you have encountered a: " + m)
print("Roll above " + str(random_number) + " to defeat the monster!")
input("Press enter to roll")

roll = random.randint(1,6)
print("Your rolled " + str(roll))
if roll > random_number:
    print("You win!")
else:
    print("You dead!")




