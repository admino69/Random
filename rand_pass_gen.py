#Project: Random password generator
import random

def len_pass():
    while True:
        pass_length = int(input("Enter the length of your password (5+): "))
        if pass_length < 5:
            print("Invalid answer.")
        elif pass_length >= 5:
            break
    return pass_length

password_length = len_pass()

pass_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"

password = "".join(random.choice(pass_letters) for letter in range(password_length))
print(password)