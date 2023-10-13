def get_pi_num2():
    user_input = int(input("Enter a number: "))
    
    if user_input >= 1000:
        print("Must be a number under 1000.")
    else:
        # Read the contents of the "1000_digs_pi.txt" file
        with open("1000_digs_pi.txt", "r") as pi_file:
            pi_digits = pi_file.read()
            
        if user_input < len(pi_digits):
            selected_digit = pi_digits[user_input]
            print(f"The digit at the {user_input}-th decimal place of Pi is: {selected_digit}")
        else:
            print(f"The requested decimal place is out of range (0-999).")

get_pi_num2()