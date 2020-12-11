# Main function of the program, calls all other functions, prints output, and repeats input process.
def main():
    ask_again = 'y'
    while ask_again.lower() == 'y':

        # Gathers one napier value from the user and converts it to an integer equivalent.
        nap1 = getNapier()
        num1 = convertNapier(nap1)
        # Prints the result of the above operation.
        print("The first number is: {:,}".format(num1))

        # Gathers one napier value from the user and converts it to an integer equivalent.
        nap2 = getNapier()
        num2 = convertNapier(nap2)
        # Prints the result of the above operation.
        print("The second number is: {:,}".format(num2))

        # Gather an arithmetic operator from the user.
        oper = getOperator()
        # Perform the doMath() operation on user-provided values using the operand given.
        result = doMath(num1, num2, oper)
        # Print the result of doMath().
        print("The result is {:,} or {}".format(result, decimalToNapier(result)))

        # Repeat the program if input is 'Y' or 'y'.
        ask_again = input("Do you want to repeat the program? Y/n: ")


# Prompts and reads napier value but does not return anything until the entered data is all alphabetic.
def getNapier():
    # Gather a Napier value from the user.
    nap = input("Enter Napier's number: ")
    # If the input isn't purely alphabetical, ask again.
    while not nap.isalpha():
        nap = input("Something's wrong. Try again.\nEnter Napiers number: ")

    # Return the user's input.
    return nap


# Receives a string that must be a Napier value (already verified in getNapier)
# Returns the integer equivalent of the received Napier value.
def convertNapier(s):
    result = 0
    # For each letter in the Napier value provided, convert the letter to its ASCII code minus the ASCII code of 'a'
    # to get the power 2 will be raised to, following the a = 2^0, b = 2^1, ... z = 2^25 convention.
    for char in s:
        # Set result to the value of the operation described above.
        result += 2 ** (ord(char) - ord('a'))

    # Return the result of the above operation.
    return result


# Nothing is returned until the user enters a +, -, /, or *
# Returns the operator character.
def getOperator():
    # Gather an operand from the user.
    operator = input("Enter the desired arithmetic operation: ")

    # If the operand provided doesn't match the symbols below, report the error and ask again.
    while operator not in ['+', '-', '/', '*']:
        operator = input("Something's wrong. Try again.\nEnter the desired arithmetic operation: ")

    # Return the operand character provided by the user.
    return operator


# Receives 2 integers and a character representing an operator.
# Returns the result of the operator operation on the 2 integers.
def doMath(n1, n2, op):

    # if/elif system that checks which operand the user provided.
    # Returns the value of the specified operation.
    if op == '+':
        return n1 + n2
    elif op == "-":

        # Subtraction using floor division // is tricky, so convert the negative number to a positive one
        # for use by decimalToNapier(). decimalToNapier() will check if the number is negative and handle
        # it accordingly.
        if n1 >= n2:
            return n1 - n2
        elif n2 > n1:
            return -1 * (n2 - n1)
    elif op == "/":
        return n1 / n2
    elif op == "*":
        return n1 * n2


# Receives an integer.
# Returns a string representing a Napier equivalent of the received integer.
# If the napier equivalent exceeds 67,108,863, or abcdefghijklmnopqrstuvwxyz, the z's will be consolidated if > 10
# Otherwise, x z's will be appended to the end of the Napier value.
def decimalToNapier(num):
    binary_str = ""
    negative = False

    # Only do the math if the number isn't 0 - if it is, return a string mimicking an empty string, ""
    if num == 0:

        # If the Napier value is nothing, return a mock-empty string.
        return "\"\""
    else:

        # Check if the provided number is negative. If it is, set a negative flag to True, and make the number positive.
        if num < 0:
            negative = True
            num *= -1

        max_napier = 67108863  # Equal to abcdefghijklmnopqrstuvwxyz in Napier's notation.
        z = 33554432  # The value of one z in Napier's notation
        napier_add = ""

        # if the provided number exceeds abcdefghijklmnopqrstuvwxyz (67108863), use floor division
        # to find the number z will be multiplied by, and set num to the remainder.
        # The z-amount is set to a string that will either print up to ten z's, or consolidate
        # them into a parentheses set in the form of (z*[]) where [] is the z-amount.
        if num > max_napier:
            z_amount = num // z
            num -= z_amount * z
            if z_amount <= 10:
                for z_letter in range(z_amount):
                    napier_add += "z"
            else:
                napier_add = "(z*{})".format(z_amount)

        # While num is not 0, find its binary value. Do this by using floor division and modulo
        # to set bits in a string to 1 or 0.
        while num != 0:
            binary_str += str(num % 2)
            num //= 2

        counter = 0
        napier_str = ""
        # For each bit in the binary string constructed above, use the index of bits "1" to generate an ASCII code.
        # Use ord('a') as a base.
        for bit in binary_str:
            if bit == "1":
                napier_str += chr(counter + ord('a'))
            counter += 1

        # If the result is negative, prepend a '-' to the Napier value. If not, don't.
        # If the Napier value exceeded the max value, append napier_add to the final string.
        # The code starting on line 121 handles the format of what is appended.
        if negative:
            if napier_add:
                return "-{}{}".format(napier_str, napier_add)
            else:
                return "-{}".format(napier_str)
        else:
            if napier_add:
                return "{}{}".format(napier_str, napier_add)
            else:
                return "{}".format(napier_str)


# Call the main function.
main()
