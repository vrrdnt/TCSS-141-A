# This lab makes use of the math library (specifically the ceil and floor functions.)
# You can just type "import math", but then you'd have to write math.ceil() and math.floor()
# Not a big deal, but I prefer not to.
from math import ceil, floor

# For some reason I did this lab slightly different - I defined main()
# and had it call the roundAndSum() function below. It still achieves the same thing.
def main():
    roundAndSum()
    
def roundAndSum():
    # Here, cont is initialized as True.
    cont = True
    # The program immediately uses cont. It allows our user to run the program easily again, using input()
    # later.
    while cont:
    
        # Here, we set int_one and int_two to two different user inputs, and then pass them through
        # the int() function to make them integers.
        int_one = int(input("Enter an integer: "))
        int_two = int(input("Enter another integer: "))
        
        # There's two sets of if/else statements below: each one handles each user input.
        # The if condition asks if each integer is greater than equal to five,
        # simulating the conditions for rounding up.
        # If this is false, meaning the integer is less than or equal to four, it moves on to
        # the else condition and its statements.
        if int_one % 10 >= 5:
        
            # This redefines int_one as the product of int_one divided by 10,
            # passed through ceil(), and the multiplied by ten.
            # Since we want to round by ten, we have to do it this way.
            # For example, if a user enters 36, it then becomes 3.6,
            # and then ceil(3.6) which becomes 4, and then 4 * 10, which is 40.
            # ceil(36) would output 36, as ceil() only rounds decimals up.
            int_one = ceil(int_one / 10) * 10
        else:
            # If the integer is less than or equal to for (the conditions for rounding down),
            # the same thing is done like above, but the floor() function is used.
            # Using the example avove, 36 becomes 3.6,
            # which becomes floor(3.6) = 3, 
            # which becomes 30.
            int_one = floor(int_one / 10) * 10
            
        # The same thing is done here as above. This could be optimized into one neat function,
        # and I'll likely lose points for not doing that. Oops!
        if int_two % 10 >= 5:
            int_two = ceil(int_two / 10) * 10
        else:
            int_two = floor(int_two / 10) * 10
            
        # This prints the combined value of our rounded integers.
        print(int_one + int_two)
        
        # This asks if the user wants to try again. The user should enter "y" if they'd like to
        # repeat.
        ask_continue = input("Try another? Enter y to continue, anything else to quit: ")
        
        # If "y" is entered, cont will remain True and the while loop at the top will repeat.
        # If the user enters anything other than "y", cont is set to False, and the 
        # while loop above terminates.
        if ask_continue != "y":
            cont = False

# Call the main function.
main()
