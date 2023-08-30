# Import Stack
from words import words
import random

# Globals
Current_Word = ""
Player_Guess = ""
Player_Lives = 0
Guesses = []
Word_Array = []
Player_Guess_Array= ["A","E","I","O","U"]

# Functions
def Set_Word():
    Current_Word = words[random.randrange(0,len(words))]
    return Current_Word
def Validate_Word ():
    while True:
        if len(Current_Word) < 4:
            Set_Word()
        else:
            break
def Validate_Guess(Guess):
    if Guess.isalpha() is False:
 
        return False
    else :
        return True
def Compare_Guess(Word, Guess):
    Correct_Guess = 0
    for Letter in Word:
        if Guess.upper() == Letter.upper():
            Player_Guess_Array.append(Letter)
            Correct_Guess += 1 
    Player_Guess_Array.append(Guess)
    if Correct_Guess !=0:
        return True
    else:
        return False
    
def Check_if_Word_Has_Been_Guessed(Word_Array):
    Correct_Letters = 0
    for Letter in Word_Array:
        if Letter != "_":
            Correct_Letters +=1
    if Correct_Letters == len(Word_Array):
        return True
    else:
        return False

        
def Check_Lives(Lives):
    if Lives == 0:
        print ("You Lose")
        print ("The Word was: "+ Current_Word)
        quit()
def Write_Word(Word):
    Word_Array = []
    for Letter in Word:
        if Letter.upper() in Player_Guess_Array:
            Word_Array.append(Letter.upper())
        else:
            Word_Array.append("_")
    return Word_Array


# Call Stack
# Set up

Current_Word = Set_Word()
Validate_Word()
Player_Lives = len(Current_Word)
Word_Array = Write_Word(Current_Word)

# Main Loop
while True:
#Check to See if Player has won
    if Check_if_Word_Has_Been_Guessed(Word_Array)is True:
        print("You Win!")
        print("The Word Was "+str(Current_Word))
        break
    print(Word_Array)
    print("Guessed Letter: "+str(Player_Guess_Array))
    print ("Current Word has " + str(len(Current_Word)) + " Letters")
    print ("Current Lives: " + str(Player_Lives))
    Player_Guess = input("Please Make a Guess: ")

#Validation Loop
    while Validate_Guess(Player_Guess) is False:
        print ("Sorry That is not a Valid Letter")
        Player_Guess = input("Please Make a Guess: ")
        Validate_Guess(Player_Guess)
# Check if Guess is Correct
    if Compare_Guess(Current_Word,Player_Guess) is True:
        print("You Guessed a Letter Correctly")
    else:
        print("You Guessed Incorrectly")
        Player_Lives -= 1
# Final Checks
    Check_Lives(Player_Lives)
    Word_Array = Write_Word(Current_Word)
    
    
   
