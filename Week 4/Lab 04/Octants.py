# Will Swoveland

def main():
    user_input = input("Please enter 3 real numbers separated by a comma: ")

    # Remove any spaces from user_input.
    coordinates = user_input.replace(" ", "")

    # Split the string into an array using a comma (,) as a delimiter.
    # This allows us to store each number as a single object.
    # For example, if user_input is "100, 20, 50", it becomes ["100", "20", "50"].
    # This object is called a list (or an array in other languages).
    # We can reference it using coordinates[i], where "i" is a specific index.
    # For our purposes, we'll be using indexes 0 through 2, as there are
    # three numbers.
    
    # A delimiter is a specific character used to split a string.
    # Above, we instructed the user to enter three numbers separated by a comma.
    # If they did so correctly, we can use their commas to separate each coordinate.
    coordinates = coordinates.split(",")
    

    # Check for point on axis or plane
    if '0' in coordinates:
        print("Point lies on an axis or a plane, and does not belong to any octant.")
    else:
        # If user input is good, go ahead
        if int(coordinates[0]) > 0 and int(coordinates[1]) > 0 and int(coordinates[2]) > 0:
            print("Point is in octant 1.")
        elif int(coordinates[0]) < 0 and int(coordinates[1]) > 0 and int(coordinates[2]) > 0:
            print("Point is in octant 2.")
        elif int(coordinates[0]) < 0 and int(coordinates[1]) < 0 and int(coordinates[2]) > 0:
            print("Point is in octant 3.")
        elif int(coordinates[0]) > 0 and int(coordinates[1]) < 0 and int(coordinates[2]) > 0:
            print("Point is in octant 4.")
        elif int(coordinates[0]) > 0 and int(coordinates[1]) > 0 and int(coordinates[2]) < 0:
            print("Point is in octant 5.")
        elif int(coordinates[0]) < 0 and int(coordinates[1]) > 0 and int(coordinates[2]) < 0:
            print("Point is in octant 6.")
        elif int(coordinates[0]) < 0 and int(coordinates[1]) < 0 and int(coordinates[2]) < 0:
            print("Point is in octant 7.")
        elif int(coordinates[0]) > 0 and int(coordinates[1]) < 0 and int(coordinates[2]) < 0:
            print("Point is in octant 8.")
        else:
            print("Something went wrong!")
        # Repeat for easy testing
        main()
    
# Run program
main()
