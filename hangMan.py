import random
import sys
from hangDict import my_diction

#copy dictionary from file.
dict = my_diction
#hangman simulation.
print("||HANGMAN! SAVE THE MAN||")
#hang-man post.
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



#function to print the hidden word.

def printHidden(letter, word, count, randX, foundL):
    new_word = list(word)
    for key,value in enumerate(new_word):
        #if the letter is apart of the print order and hasn't been discovered.
        if key % randX == 0 and value not in foundL:
            print(value, end =" ")
        else:
            if value == letter and letter in foundL:
                print(value, end = " ")
            elif value != letter and value in foundL:
                print(value, end = " ")
            else:
                print("_", end = " ")
    return


#main hang-man calling function to other sub functions.
def hangMan(letter, word, count, randX, found):

    if letter in word and letter != ' ':
        print("Yes! ", letter, " is in the word.")
        manAboutToDie(count)
        printHidden(letter, word, count, randX, found)
    elif letter == ' ':
        print('Spaces dont count...')
    else:
        manAboutToDie(count)
        printHidden(letter, word, count, randX, found)



###CODE FOR GAME.

hangCounter = 0#game counter.
their = ''
randomX = random.randrange(2, 10)#random number for printing order.
discovered = list()#list of discovered letters by user.
screenWord = list()
word = dict[random.randrange(1,82)]

#intinal print loop.
for index, value in enumerate(word):
    #intial letters will be revealed at the start with random mod printing.
    if index % randomX == 0 and value not in discovered:
        print(value, end = " ")
        discovered.append(value)
        screenWord.append(value)
    #if the letter is in discovered but doesn't mod with the randomX.
    elif index % randomX != 0 and value in discovered:
        print(value, end = " ")

    else:
        print("_", end = " ")


print(" \n")
chance = ' '#the users chance to guess the word.
#loop for game.
while hangCounter <=6 and chance!=word:
    print("=========================================")
    #user's guess.
    their = input("Guess a letter and save the man. :")
    print(" \n")

    if their in word and their not in discovered:
        discovered.append(their)
        screenWord.append(their)

        if screenWord == word:
            print("Congrats! You won! all letters have been shown!")
            print("The word is ", word)
            break

        hangMan(their, word, hangCounter, randomX, discovered)

        guess = input("Would you like to guess the word?(yes/no) (penalty:2 parts): ")


        if guess == 'yes' or guess == 'Yes':
            chance = input("What is it?: ")
            chance.lower()

            if chance == word:
                print("You Won!! Congrats!, ", chance, ' was the word.')
                break
            else:
                print(chance, " isn't the word!")
                hangCounter+=2
                print("That's gonna cost you double!")
                manAboutToDie(hangCounter)
        else:
            print("Ok no pressure...")


    elif their in word and their in discovered:
        print("That letter has already been shown.")
    elif their == ' ':
        continue
    else:
        print("Nope! That's gonna cost you...")
        hangCounter+=1
        hangMan(their, word, hangCounter, randomX, discovered)
    if hangCounter >= 6:
        print("He died! The word was..")
        print(word)
        break
