#Word Guessing Game

import random
"""
_____
Rules
Guess the random generated word beetwin 2 and 5 letters
_____
"""

  

start = input("Press [Enter] to begin!")
fhand = open("words_alpha.txt")
words = []
for line in fhand:
    if(len(line.rstrip()) >= 2 and len(line.rstrip()) <= 5):
        words.append(line)
word = str(random.choice(words)).rstrip()

print("Guess the word!")
while True:
    guess = str(input())
    if(guess == word):
        print(f"congratilations!!! you guessed the correct word: {word}")
        break
    elif(guess < word):
        print('guess higher:')
    else:
        print('guess lower:')
    
#end

    
