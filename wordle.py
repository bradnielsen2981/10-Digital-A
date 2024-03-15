import random
orange = "\033[38;5;208m█\033[0m"
green = "\033[92m█\033[0m" # Green
grey = "\033[90m█\033[0m"  # Grey

word_list = ["flask", "crisp", "plumb", "globe", "waltz", "quilt", "vivid", "jolly", "frost", "swoop","graze", "bison", "latch", "mirth", "douse", "pouch", "creek", "swirl", "blimp", "giddy","squat", "chime", "flint", "crane", "plume", "gloom", "wedge", "quack", "vexed", "joust","fable", "swamp", "brisk", "glide", "wrist", "quail", "vowel", "jelly", "frown", "sweep","blaze", "grasp", "blink", "lunar", "dwarf", "proud", "crisp", "plush", "globe", "waltz"]
word = random.choice(word_list)
#word = list(word)
playerword = input("Guess a 5 letter word (type exit to quit): ")
while playerword != word or playerword != 'exit': 
    #for index in range length of guess
        #check to see the if a letter is in the word 
        #check if the letter at the index = the guess letter at the index
    #tell the user how many letters are correct
    #tell the user how many are in correct sequence
    
    playerword = input("Guess a 5 letter word (type exit to quit): ")