#use indexes to replace the underscore with the letters
#also replace the letter with underscore
import random

guesses = 0
guess_limit = 7
letters = "abcdefghijklmnopqrstuvwxyz"

def random_word():
    categories = {"Fruits": ["Apple", "Orange"],
                "Cars": ["BMW", "Volvo"]}
    random_key = random.choice(list(categories.keys()))
    random_value = random.choice(categories[random_key])
    return random_value

while True:
    def guess_word():
        word = random_word
        user_input = print(input("Guess the word:"))
        if user_input == word:
            print("ok")
        else:
            print("no, try again")

play = print(input('''        
____
|  |
|  O    Guess the secret word before he gets hanged!
| /|\\
| / \\

Would you like to play hangman? Y/N : '''))
if play == "yes" and "y":
    guess_word()
else:
    quit()

print(guess_word())

#def if_letter_in():
