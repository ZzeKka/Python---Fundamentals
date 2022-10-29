"""
<random>  ---  number = randomint(1,100) 
<comparisons>  ---  x < y
<f-strings>  ---  f"It is currently {datetime.datetime.now()}"
<for loops>  ---  for i in range(10): print(i*i) 
<input>  ---  input("Enter your name: ")
<enumerate>  ---  for index, item in enumerate('abc'): print(f"{index}: {item}")   
<reversed>  ---  r = reversed('abcd')
"""  
                
#Number Guessing Game 
"""
_______
Rules:
_______
Guess the number (1-100) currectly as quick as possible
"""
from email.mime import base
from random import randint


#Base conversion function
def Base_Change(number,base):
    number_string = ""
    remain = -1
    while number != 0:
        remain = number % base
        if(remain == 10):
            remain = 'A'
        if(remain == 11):
            remain = 'B'
        if(remain == 12):
            remain = 'C'
        if(remain == 13):
            remain = 'D'
        if(remain == 14):
            remain = 'E'
        if(remain == 15):
            remain = 'F'
        number = int(number / base)
        number_string += str(remain)
    return int(number_string[::-1])

start = input("Press Enter to Begin!")
guesses = 10
base = -1

#base choosing
while True:
    base = int(input("Choose a base: "))
    if(base <= 16 and base >= 2):
        break
    
print(f"-> base is now: {base}")
number = Base_Change(randint(1,100),base)
print(number)
print('Guess a number:')
while True:
    guess = int(input())
    if(guess > Base_Change(100,base)or guess < Base_Change(1,base)):
        print("Guess a number beetween 1 and 100")
    elif(guess < number):
        print('guess higher:')
        guesses-=1
    elif(guess > number):
        print('guess lower:')
        guesses-=1
    elif(guesses == 0):
        print(f"The number was {number}, better luck next time!")
        break
    else:
        print(f'Congratilations it was number {number}!!!!')
        break
    


    


    