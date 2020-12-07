def main():
    
    # Open text.txt in "read" mode.
    input_file = open("text.txt", "r")
    
    # Read the file into variable file_contents. This and the above line were originally one line, but
    # since input_file immediately became a string, I couldn't close() input_file, leaving it
    # for garbage collection to handle. In this lab, I'll explicitly close the file if I can.
    file_contents = input_file.read()
    
    # Intialize each variable for each part we're keeping track of.
    total_chars = 0
    total_letters = 0
    total_upper = 0
    total_vowels = 0
    
    # For loop iterating over every character in the input file.
    for character in file_contents:
        # Since no conditions need to be met to count a character, just add 1 to the counter.
        total_chars += 1
        
        # Check if the current character is alphabetical. If so, add 1 to the counter.
        if character.isalpha():
            total_letters += 1
            
         # Check if the current character is uppercase. If so, add 1 to the counter.   
        if character.isupper():
            total_upper += 1
        
    # Check if the current character is a vowel (excluding y). If so, add 1 to the counter.          
        if character.lower() == "a" or character.lower() == "e" or character.lower() == "i" or character.lower() == "o" or character.lower() == "u":
            total_vowels += 1
    
    # Close the open file as soon as it isn't needed.
    input_file.close()
    
    # Print the counters.
    print("There are {} characters in this file.\nThere are {} letters in this file.\nThere are {} uppercase letters in this file.\nThere are {} vowels in this file.".format(total_chars, total_letters, total_upper, total_vowels))

main()
