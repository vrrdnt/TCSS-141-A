# From now on, all labs need to be inside functions. While this code
# could be optimized to include specific functions, I don't
# think it's necessary for this file.
# A function is defined by writing def,
# and then naming the function,
# and adding ().
def main():
    
    # Here, we collect user input and store it in a variable called
    # user_input.
    user_input = input("Enter several non-negative integers: ")
    
    # Here, we redefine user_input as the value of user_input currently
    # with any spaces replaced with nothing. This makes it easier for us to check
    # if the integers are sorted.
    user_input = user_input.replace(" ", "")
    
    # Here, we initialize a few variables.
    # num is set to 1, because later on we check if each number is greater than the one before it.
    # If we start it at 0, it's ineffective.
    # sorted is set to True to start, because the while and if loops below only act if
    # the numbers aren't sorted. If the numbers are in order, the variabled sorted
    # stays True.
    num = 1
    sorted = True
    
    # This while loop runs as long as the num variable, which increases by one each time
    # the while loop runs, is less than the length of our user's input.
    while num < len(user_input):
        
        # This checks to make sure each digit is greater than the one before it.
        # If that is ever false (a number is less than or equal to the number before it)
        # sorted is set to False.
        # After that, the variable num has 1 added to its value.
        if int(user_input[num]) < int(user_input[num - 1]):
            sorted = False
        num += 1
          
    # This part is self-explanatory:
    # if sorted is equal to False by the end, print "NOT SORTED".
    # the else part covers sorted being True, so we just write else and print "SORTED".
    # Remember to use two equals signs, because == is the operator for comparison.
    if sorted == False:
        print("NOT SORTED")
    else:
        print("SORTED")

# Run the main function.
main()
