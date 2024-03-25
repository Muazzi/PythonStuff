# bring in all the constants ##
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list
import random

## All
# What do i use to control when the game ends and starts
in_game = False
# How do i keep count of lives
lives = 6
# i should store the stages in a variable
stages = stages
# i need to generate a random word
hangman_word = random.choice(word_list)
# i need a list with "_"
user_list = []
for c in range(len(hangman_word)):
    user_list.append("_")

print(hangman_word)
# show the logo
print(logo)
# begin the loop of the game game ends if its true
while not in_game:
    guess = input("Guess the word!")


    for index, character in enumerate(hangman_word):

        if character == guess:
        # at the index assign that value
            user_list[index] = guess
    if "_" not in user_list:
        print("You win")
        in_game = True
    if guess not in hangman_word:
        lives -= 1
        print(f"Your guess is wrong incorrect , you guessed {guess} , you lose a life , current lives remaining {lives} ")
    print(user_list)
    print(stages[lives])
