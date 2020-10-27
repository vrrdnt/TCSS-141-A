# Will Swoveland

# You don't need to import sys - I only did so so that the user can type 'exit' to stop the program.
# Otherwise, it runs infinitely, until you manually crash the program.
import sys

# Again, ignore the function - it just makes the program loop infinitely for testing.
def main():
    user_input = input("Enter a string! type \'exit\' to quit: ")

    if user_input == "exit":
        sys.exit(0)

    # This lab ideally utilizes the 'in' operator, which allows you to iterate over each object in something.
    # In this case, we iterate over each (ch)aracter in the string 'user_input', and print both the character
    # and its equivalent ASCII code, using the ord() function.
    # Don't forget to convert the output of ord() to a string! Otherwise, it'll be an integer.
    for ch in user_input:
        print("ASCII value of " + ch + " is " + str(ord(ch)))

    main()

main()
