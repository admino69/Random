#Project: Hangman game
#Game: Random questions, like guess the fruits. Also show
#how long the words are. "_ a _ _ _" Maybe with GUI after.
#maybe hints too, and you will lose a guess if u use a hint
import random

print(input('''        
____
|  |
|  O    Guess the secret word before he gets hanged!
| /|\\
| / \\

    
Would you like to play hangman? Y/N : '''))
guesses = 0
guess_limit = 7
letters = "abcdefghijklmnopqrstuvwxyz"

def random_word():
    categories = {"Fruits": ["Apple", "Orange"],
                "Cars": ["BMW", "Volvo"]}
    random_key = random.choice(list(categories.keys()))
    random_value = random.choice(categories[random_key])
    return random_value

print(random_word())