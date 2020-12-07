# Will Swoveland

# Clarification - "def" and functions haven't been covered at this point - please ignore them.
# I defined the function user_ask just so the program repeats infinitely for testing.

# Function gathering input from user and printing an equivalent Roman numeral.
def user_ask():
    user_input = input("Enter a number between 1 and 10: ")
    
    # Run through checks, starting with input verification.
    if user_input.isdigit():
        # Check the lower and upper bounds of valid input.
        if int(user_input) < 1 or int(user_input) > 10:
            print("Error: User input exceeds bounds of acceptable input. Try again.")
            user_ask()
        elif int(user_input) == 1:
            print("I")
        elif int(user_input) == 2:
            print("II")
        elif int(user_input) == 3:
            print("III")
        elif int(user_input) == 4:
            print("IV")
        elif int(user_input) == 5:
            print("V")
        elif int(user_input) == 6:
            print("VI")
        elif int(user_input) == 7:
            print("VII")
        elif int(user_input) == 8:
            print("VIII")
        elif int(user_input) == 9:
            print("IX")
        elif int(user_input) == 10:
            print("X")
    else:
        # Catch any non-integer input.
        print("User input was not an integer. Please try again.")
        user_ask()

# Run user_ask function.
user_ask()
