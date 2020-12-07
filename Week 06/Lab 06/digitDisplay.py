# From now on, all labs need to be inside functions. While this code
# could be optimized to include specific functions, I don't
# think it's necessary for this file.
# A function is defined by writing def,
# and then naming the function,
# and adding ().
def main():

    # Here, we collect user input and store it in a variable called
    # user_input.
    user_input = input("Enter an integer (Ideally 100+): ")

    # Here, we initialize a few variables.
    # total, which is used to add the even numbers, is set to 0 to start.
    # string is set to an empty string, as we'll be adding to it with each iteration.
    # first is set to True, which I'll explain later.
    total = 0
    string = ""
    first = True

    # Our first if statement just makes sure our user has actually entered something.
    # It'll fail otherwise.
    if int(user_input) != 0:
        
        # This for loop just iterates over every number in our user's input.
        for num in user_input:
            # This if statement checks if each digit is odd or not. If a number is odd,
            # that number modulo 2 will always equal 1. For example, 3 % 2 is 1, because 2 goes
            # into 3 once, with 1 left over. Modulo = division with remainders.
            if int(num) % 2 == 1:
                # Now to explain the first variable bit - it essentially skips the first odd number our user
                # enters. If we omit this, our output will start with a plus sign, which we want to avoid.
                # If our input is 789, the program should print 7+9 on line 1, and 8 on line 2.
                # This if/else statement only runs the if part once, and that's to skip the first odd number.
                # On every iteration after, it'll put a + between each odd number.
                if first == True:
                    first = False
                else:
                    
                    # This just sets the string variable to its current value plus a "+" sign.
                    string += "+"
                # This part adds the odd numbers. 
                # It sets the string variable to its current value plus the current digit the for loop
                # is looking at, passed through str() so it can be placed in a string.
                string += str(num)
            else:
                # This else statement handles even numbers, and it sets the variable total
                # to its current value plus the current number the for loop is looking at.
                total += int(num)

    # This prints the result, once the for loop ends. We use format() to substitute any {} with variables.
    print("{}\n{}".format(string, total))

# Call the main function.
main()
