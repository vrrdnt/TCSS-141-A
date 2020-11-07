
# a.  
Write a program called `digitDisplay.py` that asks a user for an **integer**, prints only the *odd* digits contained in the integer on the same line, with each odd digit separated by a plus `+` sign, and then sums up the *even* digits on a new line.    
 
*E.g.* if a user enters `29107`, your program should produce the following output:  
```
9+1+7  
2  
```  
As another example, the input `5386721` should produce:  
```  
5+3+7+1  
16  
```  
It's a bit tricky to place the `+` signs only between the odd digits, and not have a `+` sign on the end.  
  
As a hint, you'll want to build a string that contains the odd digits separated by a `+` sign. You may want to set a `Boolean` variable (**first**) to `True` and a `string` variable (**string**) to an empty string `“”` before the process begins. As you examine each digit, set first to `False` when you encounter the first odd digit. Otherwise, you'll concatenate a `+` sign and the current string variable, and then assign it to the string variable, then concatenate the digit as a string (call the `str()` function passing the odd digit) to the string, and assign the result back to the string. 
  
The basic *pseudocode* is as follows:  
```
Read an integer into a variable named number  
Set total to 0  
Set first to True  
Set a string variable (say s) to an empty string  
While number does not equal zero do the following:  
      Store the least significant digit into a variable name digit  
      If digit is odd:  
        If first is True:  
            Assign False to first  
        Otherwise:  
            Set s to “+” + s  
        Set s to str(digit) + s  
    Otherwise:  
        Add the current digit to the total  
    Reduce the value of number by 10  
Display s  
Display total  
```  
 
# b.  
Write a program called `roundAndSum.py` that continues to perform the following process until the user no longer wants to continue:   
  

 1. Prompts for two integers to be entered at the keyboard and rounds each int value up to the next multiple of 10 if the rightmost digit is 5 or more
 2. Prints the sum of their rounded values. 

NOTE: The number rounds up if the last digit is 5 or more, and rounds down if the last digit is 4 or less. For example, 15 rounds up to 20, and 14 rounds down to 10.
 
The program should perform as follows:  
```  
Enter an Integer: 15  
Enter another Integer: 14  
30  
Do Another? y  
Enter an Integer: 259
Enter another Integer: 112  
370  
Do Another? n  
```  
 
# c.  
Write a program named `ascending.py` that asks the user to enter **non-negative** integers (*integers > -1*) and determines whether or not the numbers entered by the user are sorted in ascending order. You do not know how many numbers will be entered but you know that a *sentinel* value of `-1` will be used to denote the end of the sequence.  
  
Print “SORTED" if the sequence is sorted, print “NOT SORTED" if it is not.  
  
NOTES:  
 - You cannot use a list or a sort method
 - Understand that NON-NEGATIVE means integers greater than -1
 - Assume valid data entry, i.e. do NOT worry about handling invalid input, e.g. non-integers
