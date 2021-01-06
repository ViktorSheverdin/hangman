# Step 1

from os import system
import random as random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print("For debug: %s" % (chosen_word))
display = ["_" for char in chosen_word]
print(display)
end_of_game = False


while not end_of_game:
    guess = input("Enter your letter: ").lower()
    print(chr(27) + "[2J")
    print("Guessing letter: %s" % (guess))

    for idx, letter in enumerate(chosen_word):
        if letter == guess:
            print("Contains letter: %s" % (guess))
            display[idx] = guess
    if guess not in chosen_word:
        lives -= 1
        print("Letter %s is not in the word" % (guess))
        if lives < 0:
            print("You losse! Gave Over")
            end_of_game = True
            print(stages[0])

            break
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You won!")

    print(stages[lives])
