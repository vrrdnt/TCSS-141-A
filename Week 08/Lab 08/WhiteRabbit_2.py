def main():
    # Ask the user for an input file and output file.
    # Open the former in "read" mode and the latter in "write" mode.
    input_file = open(input("Enter the name of a file with its extension: "), "r")
    output_file = open(input("Enter the the desired name of an output file: "), "w")
    
    # Read the first line of the input file and assign it to a variable we can get the length of later.
    firstLine = input_file.readline()
    
    # Initialize the our character counter with the length of the first line.
    num_char = len(firstLine)
    
    # For loop iterating over each line in the input file.
    for line in input_file.readlines():
    
        # Add the length of the current line to the character counter.
        num_char += len(line)
        
        # Check if the line is longer than the first line using len() and check if it contains p/P/k/K.
        if len(line) > len(firstLine) and "p" in line or "P" in line or "k" in line or "K" in line:
            # Write the current line to the output file if the conditions are True.
            output_file.write(line)
    
    # Close the input file as soon as we don't need it.
    input_file.close()
    
    # Write the total number of characters in the input file as reported by our counter.
    output_file.write("Total number of characters in the input: {}".format(num_char))
    
    # Close the output file as soon as we don't need it.
    output_file.close()
    
main()
