# 1. Files and Strings (including if statement(s))
Write a program named `WhiteRabbit_1.py` that takes two filenames from a user –one for input and one for output – and creates a new output file that contains **only** the **even** numbered lines from the input. Finally, it should print the total number of lines in the input file. For example, if the input file contains (use the provided file `input8b.txt` for your input and `output8b.txt` for output):
```
Read them, said the King
The White Rabbit put on his spectacles.
Where shall I begin, please your Majesty? he asked.
Begin at the beginning, the King said gravely,
And go on till you come to the end:
Then stop.
```
Then the output file should be: 
```
The White Rabbit put on his spectacles.
Begin at the beginning, the King said gravely,
Then stop.
Total number of lines from the input file: 6
```
# 2. Files and Strings (including if statement(s))
Use **Save As...** to rename `WhiteRabbit_1.py` to `WhiteRabbit_2.py` and modify the program to perform as follows:

 - Write a program that takes two filenames from a user –one for input and one for output –and creates a new output file that contains ONLY the lines of the input file that are longer than the first line of the input file AND contain the letters `p`, `P`, `k`, `K`.
 - Finally, it should print the total number of characters processed from the input (including newline characters).

For example, if we use `input8b.txt` from above, the output would be (use `output8b-2.txt` for the output file): 
```
The White Rabbit put on his spectacles.
Where shall I begin, please your Majesty? he asked.
Begin at the beginning, the King said gravely,
Total number of characters in the input: 210
```
As a hint for dealing with the length of the first line, use readLine() on the file Object to read the first line before entering a `for line in input1:` loop. This will consume the first line and move the file marker to the start of the second line just prior to entering the for loop. For example, the following gets the length of the first line using a file Object that you named input1:
```
firstLineLength = len(input1.readLine())
```
# 3. Strings and files
Write a program `counting.py` that reads a file named `text.txt` and prints the following to the screen:

 - The number of characters in that file
 - The number of letters in that file
 - The number of uppercase letters in that file
 - The number of vowels in that file


