# 1. Lists
## a. Lists I
Download the file `lists1.py` that contains 4 list exercises. You are to follow/replace each comment in that file with the appropriate statement.
## b. Lists II
Write a program called `lists2.py` that asks a user to enter numbers separated by commas, reads in these numbers, and puts them into a list. Then the program asks a user to enter a number to search for. Finally, the program displays how many times the entered number occurred in the list and the percentage of that value in a data set. You are NOT allowed to use a built-in function count –you need to count the number of values on your own. This is the sample run of the program:
```
Enter numbers separated by commas: 1,2,3,4,4,4,5,6,7,8,9,0
Enter a number to look for: 4 
Appeared 3 times 
Constitutes 25% of this data set
```
# 2. Problem solving with lists, strings, and files
Write a program `classGrades.py` that reads a csv data file called `grades.csv` (sample provided) that contains 4 columns: `student last name`, `student first name`, `midterm score`, and `final score`. The program calculates an exam average for each student and rounds it up to an integer (do floating point division and pass the result to the math library ceil function), then it writes the name and the exam average to another csv file called `examScores.csv` (sample provided). You are expected to decompose all operations into various functions.  

Finally, the program prints to the screen the following stats:

 - Names and scores of students within 5 points of the maximum score, e.g if the maximum score is 98, then all the students scoring >= 93 should be printed
 - The number of students that scored in the range 0 –59, 60 –69, 70 –79, 80–89, 90 –100 (to keep track of the ranges, you should set up a list of counters of size 5; when you process a number within the first range, you update location 0, within second range, location 1, etc)

For example, for the provided input file, the program should print the following 13 lines: 
```
Top scorers (max score = 97):
Herrera, Adrian Q., 93
Kline, Celeste P., 94
Lee, Pearl J., 96
Salinas, Taylor Z., 95
Whitfield, Stella W., 97

Grade ranges:
7 students with grades >= 90
10 students with grades >= 80
31 students with grades >= 70
24 students with grades >= 60
28 students with grades < 60
```
