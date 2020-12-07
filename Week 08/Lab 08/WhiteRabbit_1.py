def main():
    # Ask the user for an input file and output file.
    # Open the former in "read" mode and the latter in "write" mode.
    input_file = open(input("Enter the name of a file with its extension: "), "r")
    output_file = open(input("Enter the the desired name of an output file: "), "w")
    
    # Initialize a counter with 1 to check the line number. (Skips the first line as it is odd.)
    line_num = 1
    
    # For loop iterating over each line in the input file.
    for line in input_file.readlines():
    
        # Checks if the line number is even
        if line_num % 2 == 0:
        
            # Writes the line to our output file if the condition is True
            output_file.write(line)
            
        # Adds 1 to our line counter
        line_num += 1
        
    # Close the input file as soon as we don't need it.
    input_file.close()
    
    # Write to and immediately close the output file.
    output_file.write("\nTotal number of lines from the input file: {}".format(line_num - 1))
    output_file.close()
    
main()
