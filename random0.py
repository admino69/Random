import math

pi_num = math.pi

def get_pi_num2():
    user_input = int(input("Enter a number: "))
    if user_input >= 15:
        print("Number must be 15 or under 15.")
    else:
        x = round(pi_num, user_input)
        print(x)
    
get_pi_num2()