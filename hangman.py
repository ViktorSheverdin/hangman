# Step 1

from os import system
import random as random
from stages import *
from hangman_words import word_list
lives = 6
print(chr(27) + "[2J")
print(logo)
# word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
# print("For debug: %s" % (chosen_word))
display = ["_" for char in chosen_word]
guessed_letters = []
print(display)
end_of_game = False


while not end_of_game:
    guess = input("Enter your letter: ").lower()
    print(chr(27) + "[2J")
    if guess not in guessed_letters:
        guessed_letters.append(guess)
        print("Guessing letter: %s" % (guess))
    else:
        print("You have alredy guessed letter: %s" % (guess))

    for idx, letter in enumerate(chosen_word):
        if letter == guess:
            print("Contains letter: %s" % (guess))
            display[idx] = guess
    if guess not in chosen_word:
        lives -= 1
        print("Letter %s is not in the word" % (guess))
        if lives <= 0:
            print("You lose! \nGave Over")
            print("The word was: %s" % (chosen_word))
            end_of_game = True
            print(stages[0])

            break
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You won!")

    print(stages[lives])
