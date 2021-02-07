import random
from hangDict import words

# copy dictionary from file.
gameWords = words
# hangman simulation.
print("||HANGMAN! SAVE THE MAN||")
# hang-man post.
print("                                        ===")
print("                                        | |")
print("                                        |")
print("                                        |")
print("                                        |")
print("                                       ===")

def manAboutToDie(lives):
    if lives == 0:
        print("                                        ===")
        print("                                        | |")
        print("                                        |")
        print("                                        |")
        print("                                        |")
        print("                                       ===")


    elif lives == 1:
        print("                                        ===")
        print("                                        | |")
        print("                                        |")
        print("                                        |/")
        print("                                        |")
        print("                                       ===")
    elif lives == 2:
        print("                                        ===")
        print("                                        | |")
        print("                                        |")
        print("                                        |/ \\")
        print("                                        |")
        print("                                       ===")
    elif lives == 3:
        print("                                        ===")
        print("                                        | |")
        print("                                        |")
        print("                                        |/ \\")
        print("                                        |/")
        print("                                       ===")
    elif lives == 4:
        print("                                        ===")
        print("                                        | |")
        print("                                        |")
        print("                                        |/ \\")
        print("                                        |/ \\")
        print("                                       ===")
    elif lives == 5:
        print("                                        ===")
        print("                                        | |")
        print("                                        |")
        print("                                         /|\\")
        print("                                        |/ \\")
        print("                                       ===")
    elif lives >= 6:
         print("                                        ===")
         print("                                        | |")
         print("                                        | O")
         print("                                        |/|\\")
         print("                                        |/ \\")
         print("                                       ===")
    else:
        print("Error...")



# function to print the hidden word.

def printHidden(letter, word, count, randX, foundL):
    new_word = list(word)
    for key,value in enumerate(new_word):
        # if the letter is apart of the print order and hasn't been discovered.
        if key % randX == 0 and value not in foundL:
            print(value, end =" ")
        else:
            if value == letter and letter in foundL:
                print(value, end = " ")
            elif value != letter and value in foundL:
                print(value, end = " ")
            else:
                print("_", end = " ")


# main hang-man calling function to other sub functions.
def hangMan(letter, word, count, randX, found):

    if letter in word:
        print("Yes!", letter, "is in the word.")
        manAboutToDie(count)
        printHidden(letter, word, count, randX, found)
   
    elif letter == ' ':
        print('Spaces dont count...')
   
    else:
        manAboutToDie(count)
        printHidden(letter, word, count, randX, found)



### CODE FOR MAIN GAME LOOP. ###

hangCounter = 0 # Eveytime this counter is increased, the man gains a body part.

letter_guess = '' # User's guess. 

randomX = random.randrange(2, 10) # Random number for printing order.

discovered = [] # List of discovered letters by user.
screenLetters = [] # List to keep track of all visible letters on the screen. 

word = gameWords[ random.randrange( 0, len( gameWords ) - 1 ) ] 

# Intinal print loop to show word in form of '_ _ e _ _ '.
for index, value in enumerate(word):

    # Intial letters will be revealed at the start with random mod printing.
    if index % randomX == 0 and value not in discovered:
        print(value, end = " ")
        discovered.append(value)
        screenLetters.append(value)
    # If the letter is in discovered but doesn't mod with the randomX.
    elif index % randomX != 0 and value in discovered:
        print(value, end = " ")
        screenLetters.append(value)

    else:
        print("_", end = " ")
    
print(" \n")
chance = ' ' # The users chance to guess the word.

# Loop that will only break if user guesses right word or runs out of chances.
while hangCounter <= 6 and chance != word:
    print("=========================================")
    # User's guess.
    letter_guess = input("Guess a letter and save the man. :")
    # Input validation to only take in letters. 
    while not letter_guess.isalpha(): 
        letter_guess = input("Spaces, numbers, and multiple letters are invalid input.. Please enter in a letter: ")

    while len(letter_guess) > 1: 
        letter_guess = input("Spaces, numbers, and multiple letters are invalid input.. Please enter in a letter: ")


    print("\n")

    if letter_guess in word and letter_guess not in discovered:
        discovered.append(letter_guess)
        screenLetters.append(letter_guess)


        # Check for duplicates. 
        occur = 0
        for l in word: 
            if letter_guess == l:
                occur += 1

        # If the word contains duplicate letters of the guessed letter, need to append all duplicates.
        if occur > 1: 
            for i in range(occur - 1):
                screenLetters.append(letter_guess)

        # Check if word on screen is equal to game word. 
        letter_count = 0
        for letter in screenLetters:
            if letter in word: 
                letter_count += 1

        # All letters in screenLetters are equal to the game word. 
        if letter_count == len(word):
            hangMan(letter_guess, word, hangCounter, randomX, discovered)
            print("\nCongrats! You won! all letters have been shown!")
            print("The word is", word)
            if hangCounter == 5: 
                print("Man.. that was close.. he was almost hung!!")

            break

        hangMan(letter_guess, word, hangCounter, randomX, discovered)

        print("\nWould you like to guess the word?")
        guess = input("Enter in y for yes or n for no\n(penalty for wrong guess is 2 body parts): ")

        guess = guess.lower()
        while guess != "y" and guess != "n": 
            guess = input("Please enter in either y or n: ")
            guess = guess.lower()


        if guess == 'y':
            chance = input("What is it?: ")
            chance.lower()

            if chance == word:
                print("You Won!! Congrats!,", chance ,"was the word.")
               
                if hangCounter == 5: 
                    print("Man.. that was close.. he was almost hung!!")

                break
            else:
                print(chance, " isn't the word!")
                hangCounter+=2
                print("That's gonna cost you double!")
                manAboutToDie(hangCounter)
        else:
            print("Ok no pressure...")


    elif letter_guess in word and letter_guess in discovered:
        print("That letter has already been shown.")

    else:
        print("Nope! That's gonna cost you...")
        hangCounter+=1
        hangMan(letter_guess, word, hangCounter, randomX, discovered)
    if hangCounter >= 6:
        print("\nHe died! The word was..", word)
        break


