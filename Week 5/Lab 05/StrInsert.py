# NOTE: brackets [] indicate a variable.
# For example, if x = 5 and I mention the value of x,
# I'll write it as [x].

# First, user input is collected using the input() function. Whatever the user enters will become the value of [user_input].
user_input = input("Enter a character to be inserted, a position, and a string for a character to be inserted into: ")

# The next three lines essentially split the [user_input] into three parts:
# The character, the position it should go in, and the string for it to be inserted into.
# In the input() function above, I ask the user to separate each piece using a comma.
# An example user input could look like "a,2,bumblebee", and this program should print out "buamblebee"
# IMPORTANT! Counting starts at 0. In the string "bumblebee", the first letter "b" is at position 0.
# the second letter "u" is at position 1.
# In each step, we use the find() function to locate each comma.
# The find() function searches left to right, and stops as soon as it has located the specified character or string.
character_pos = user_input.find(",")

# In the next two, I have to specify a location to start the search for a comma.
# If I don't, it'll just find the first comma twice, and the character, position and string will all equal 
# whatever the user entered for the character.
# A location to start searching is specified by adding a comma in the find() function, and then passing a number.
# In the line below, [character_pos] + 1 will equal 1, which is where our first comma is.
# It'll then search rightwards from next to that comma to the next comma.
position_pos = user_input.find(",", character_pos + 1)

# The same thing is done here, just using the position of the second comma reported by the last find() call.
# To clarify - to "call" is to execute a function, such as find().
string_pos = user_input.find(",", position_pos + 1)

# Here, we assign the actual values to each variable.
# We want [character] to be the letter our user entered - "a" in the example on line 11.
# Next, we want [position] to be the number our user entered - "2" in the example.
# Lastly, we want [string] to be all the rest of our user input. We achieve this by not specifiying an end index
# in the brackets [] next to [user_input].
# Remember - an "index" means an objects position in a list of objects.
# For example, the position of the lowercase letter "L" in "bumblebee" has an index of 4.
character = user_input[ : character_pos]

# We want to convert [position] into a number using the int() function.
# This is because, as seen above, the find and index operators require a number for any kind of
# specific searching or slicing.
position = int(user_input[character_pos + 1 : position_pos])

# We don't specify an end point for the slice operation here - this is because [string] is the last thing our
# user entered, and has a variable end point that depends on what the user enters.
string = user_input[position_pos + 1 : ]

# This if statement makes sure that the value entered for [position] is actually a valid
# index or position in [string]. If the user entered 10 for position,
# but [string] is only 9 characters long ("bumblebee"), the position is invalid.
# In that event, the program just prints whatever the user entered for [string].
if position <= len(string):
    
    # Here we use a print() and format() statement. 
    # Where there are braces {} in the string, variables will replace them in order of appearance.
    # We only have one {} in the print() statement, so only one variable can be passed to it.
    # We set the {} to be equal to the following:
    # [string] (from the beginning to the number given by the user, PLUS
    # the [character] entered by the user, PLUS
    # the rest of [string] from the number our user entered onwards.
    # This gets us a new string with the user-provided character inserted at the specified position.
    print("{}".format(string[ : position] + character + string[position : ]))
else:
    # This just prints whatever the user entered for [string].
    print(string)
