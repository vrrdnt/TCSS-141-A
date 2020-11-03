# a.  
The consumer price index (CPI) indicates the average price of a fixed basket of goods and services.  
It is customarily taken as a measure of inflation and is frequently used to adjust pensions.  
The CPI was `9.9` in July 1913 and `238.25` in July 2014.  
This means that `$9.90` in July 1913 had the same purchasing power as `$238.25` in July 2014.  
Assuming that the CPI will rise at `2.5%` per year in the future, in how many years will the CPI at least double from its July 2014 level?  
What year will it be?  
  
Create a program named: `CPi.py` that has the user enter the maximum “times” value to calculate and display 2 times, 3 times,... , up to and including the entered maximum times value. 
Use nested `while` loops to solve the problem; an outer loop to count the times (2-maximumTimes) and an inner loop to calculate the increase in value and years. 
Once you figure it out, show how many years it will take to double it, triple it, quadruple it, and quintuple it, i.e. the outer loop. 
This is the sample run of the program:  
```
Enter maximum times the 2014 prices: 5  
Consumer prices will be 2 times 2014 prices in 29 years ( 2043 )  
Consumer prices will be 3 times 2014 prices in 45 years ( 2059 )  
Consumer prices will be 4 times 2014 prices in 57 years ( 2071 )  
Consumer prices will be 5 times 2014 prices in 66 years ( 2080 )
```

# b.  
Write a program `StrInsert.py` that simulates insert behavior on a string. 
The program takes three inputs: a `character` to be inserted, its `position`, and a `string` into which a character is to be inserted. 
The program prints the new version of the string.  
For example, if the arguments are: `-`, `2`, and `below` then the program prints `be-low`. 
If a position passed to the program is outside of the bounds of the original string (in this case `<0` or `>5`), then print the original string, without any changes  
```
(Note: an insert value of 0 OR the length of the string will add to the start or append to the end.  
T, 3, and can will be canT 
T, 0, and can will be Tcan  
T, 4, and can will be can
```  
No while loops are used to solve this.
