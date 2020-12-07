
# 1. Functions 1  
### a.  
Perform a pencil and paper trace of the program given below to determine what the program will print. After you write the trace, copy and paste the program into Python and run it in order to compare the actual run to your paper trace. Create a Word document named `Functions 1.doc` that contains an explanation as to where you went wrong and why.  
```
def main():
    a = 7
    b = 5.555
    c = "Rafel"
    d = "Dathne"
    parameterMystery2(c, b, d, a)
    parameterMystery1(c, a, b, d)
    parameterMystery2(d, c, b, a)
    print(a, b, c, d)
    
def parameterMystery2(one, two, three, four)
    print(one, two, three, four)
    
def parameterMystery1(a, b, c, d)
    print(a, b, c, d)
    a = a.upper()
    b = b * 5
    c = c + 2 ** 3 / 4
    d = d * 3
    print(a, b, c, d)
    parameterMystery2(c, d, b, a)
    
main()
```  
### b.
Download the program `oops.py`. It contains several mistakes that should be fixed. You may have to move variables around, add functions, delete functions, etc. The program should produce the following output:  
```
x = 20.02 and y = 14.0
The value from main is: 23.14069
x = pierce and y = franklin
x = 23.14069 and y = 20.02
z = 5
```  
# 2. Programs with functions  
Write a program named `grades.py`that asks the user to enter five test scores. Assume valid scores will be entered and each number will be entered separately, i.e. you will need 5 variables. The program should display a letter grade for each score and the average test score. Write the following functions in the program:

 - **main** - asks the user to enter five test scores separately, placing them into five float variables. main should then call showScores 5 times passing one of each of the scores each time. When returned from showScores, main should then call calcAverage passing it the 5 scores.
 - **showScores** - receives a single score and prints the score to the console (without starting a new line) and sends the score just printed to printLetterGrade which will print a letter grade on the same line.
 - **printLetterGrade** - accepts a single number as an argument and displays a letter grade for the score based on the following grading scale:  
 
|Score|Letter Grade|
|--|--|
|90 - 100|A|
|80 - 89 |B|
|70 - 79|C|
|60 - 69|D|
|Below 60|F|
 - **calcAverage** - receives the 5 scores as arguments and displays the average of the scores, along with a letter grade equivalent to that average (take advantage of the function printLetterGrade to display the letter by passing it the calculated average).  

Document your file with your name, completion date, and a brief description of the program at the top of the file. Also, add comments before each function describing its purpose and what it expects to receive as parameters.  
  
  Here is a sample run of the program:
  
```
    Enter grade 1: 65
    Enter grade 2: 80
    Enter grade 3: 90
    Enter grade 4: 71
    Enter grade 5: 85
    65 is D
    80 is B
    90 is A
    71 is C
    85 is B
    The average is: 78.2 which is C
```

