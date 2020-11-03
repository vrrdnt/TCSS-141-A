# Sorry for the essay below - this lab was confusing, and I want
# to make sure I'm as clear as possible on how each part works!
# NOTE: brackets [] indicate a variable.
# For example, if x = 5 and I mention the value of x,
# I'll write it as [x].

# First, user input is collected with the input() function.
# It's then converted into an integer, using the int() function.
# After that, the result of int(input()) is converted to a range().
# We do this because we want to know the CPI at each step, from 2 to whatever
# our user entered. We have to start at 2, because x times 0 is zero, and x
# times 1 is x. Neither of those are useful to us, when we start the program
# wanting at least double the amount.
user_input = range(2, int(input("Enter the maximum times the 2014 prices: ")) + 1)


# Here, our variables are initialized. To initialize is to declare them, or assign them a value.

# [iteration] represents the number of times the outer while loop below has run.

# [year] starts at 0 because we use it to keep track of the passing years while we wait to find
# double the starting number, 238.25.

# [increase] is 1.025 because this is equal to our rate of increase, 2.5% (0.025) plus 1.
# If [increase] was just 0.025, we would have to add 238.25 (and future increases) back into itself frequently.

# [start] is 238.25, because this is the baseline our program uses.
# The CPI in 2014 is 238.25.

iteration = 2 # Don't want to multiply by 0 or 1.
year = 0
increase = 1.025
start = 238.25


# The outer while loop simply counts the number of times the relevant year has been printed.
# while iteration in user_input means while the value of iteration corresponds with a number in user_input,
# which is currently a range from 2 to the number our user entered, it'll execute the statements inside.
# As soon as iteration exceeds the limit defined by user_input, the while loop won't run.

while iteration in user_input: 

    # [target] is also used here - this is to calculate the max number we're looking for.
    # First, we want to find out what year it'll be when the CPI has doubled.
    # [target], on its first iteration, is equal to 2, because we defined [iteration] as 2, to start.
    # [target] will then evaluate to 476.5.
    # Once the inner while loop has found the number of years it'll take to double the CPI (29),
    # the line at the bottom, iteration += 1 is saying [iteration] is equal to the value of iteration currently plus 1.
    # After the first run, it becomes three, and [target] now evalutes to 238.25 * 3, or 714.75.
    target = 238.25 * iteration
    
    # This inner while loop is what does our math.
    # This loop will run 29 times before it fails due to a false condition. 
    # The condition asks that, as long as [start] is less than or equal to [target], it'll run over and over,
    # running all of the statements inside the loop.
    while start <= target:
    
        # This line below states that [start] becomes 
        # equal to the value of [start] currently, times the value of increase, which is 1.025.
        # On its first run, it evalutes to the following:
        # [start] = 238.25 * 1.025, which equals 244.20625.
        # Additionally, the line after states that [year] becomes equal to
        # the value of [year] currently plus 1. This evalutes to 1 on its first run, 2 on its second, etc.
        # This while loop will continue to repeat as long as [start] is less than or equal to [target].
        # Immediately as [start] is equal to or greater than [target], the while loop breaks,
        # and the current value of [year] is supplied to the print() function at the bottom.
        start *= increase
        year += 1
        
    # This print statement uses the format() method.
    # Where there are braces {} in the string, variables will replace them in order of appearance.
    # The first {} becomes the value of [iteration], the second {} becomes the value of [year], and the third
    # {} becomes the value of 2014 plus [year].
    # On its first run, [iteration] is 2, [year] is 29, and 2014 + [year] is 2043.
    # print() will print the following on its first run:
    # "Consumer prices will be 2 times 2014 prices in 29 years (2043)
    print("Consumer prices will be {} times 2014 prices in {} years ({})".format(iteration, year, 2014 + year))
    
    # Once the print() function executes, [iteration] becomes equal to the value of
    # [iteration] currently plus 1.
    # After the first run, iteration becomes 3, then 4, etc.
    iteration += 1
