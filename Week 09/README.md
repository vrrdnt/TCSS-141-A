# Problem statement
For this program, you are to design and implement a calculator for positive integers that uses John Napier's location arithmetic (explained below). The user of your program will enter two numbers, using Napier's notation, and an arithmetic operator. You program is to translate these numerals into Hindu-Arabic decimal numbers, display them, perform desired operations, and finally print the result - in both abbreviated Napier's notation and in Hindu-Arabic decimal notation. The arithmetic operators that your program should recognize are `+`, `-`, `*`, and `/`. These operators are used to perform Python operations of integer addition, subtraction, multiplication, and division (remember, Napier notation only uses integers. That said, all actual operations you will perform are with integers. In particular, division `//`). The program is to be repeated as many times as the user wishes.  

You may not use Python constructs that have not been discussed in class thus far.
# Input
Input to your program will be interactive. Napier used letters to represent successive powers of 2, where a = 2<sup>0</sup>, b = 2<sup>1</sup>, c = 2<sup>2</sup>, d = 2<sup>3</sup>, ... z = 2<sup>25</sup>.  
When converting to a decimal numeral you simply add the digits: 

`abdgkl= 2^0 + 2^1 + 2^3 + 2^6 + 2^10 + 2^11 = 1 + 2 + 8 + 64 + 1024 + 2048 = 3147` 

His location numerals used sign-value notation, in which a number is simply the sum of its digits, where order does not matter, and digits can be repeated, e.g. 
```
abc = cba= bca
abbc = acc = ad
``` 
After each number or an operator is entered, you are to make sure that no illegal characters or arithmetic operators were entered. For numbers, an illegal character is anything that is not a letter. For operators, an illegal character is anything other than one of the four operator characters listed above. When an invalid input occurs, the program is not to crash or exit, but to ask the user for the given value again – until the valid values are entered.
# Output
In addition to printing the decimal values of the two numbers entered by the user, you need to print the result of the operation in both notations. When printing in Napier's notation, make sure you do not repeat letters where a single letter would do, e.g. instead of `abbc`, you should print `ad`. In addition, if the result of your calculation is a 0, the equivalent string would be an empty string which we will not be able to see on the screen, so in such a case print a set of quotes, e.g. `""`. If the result of your calculations is a negative number, print the number with a minus sign in front, e.g. `–abc`.

To represent a given decimal number as a location numeral, express it as a sum of powers of two and then replace each power of two by its corresponding digit (letter). For example, when converting from a decimal number:

`87 = 1 + 2 + 4 + 16 + 64 = 2^0 + 2^1 + 2^2 + 2^4 + 2^6 = abceg`

You may find standard algorithms for converting from decimal to binary useful to achieve this purpose. To convert from a base-10 integer to its base-2 (binary) equivalent, the number is divided by two, and the remainder serves as the least-significant bit. The (integer) result is again divided by two, its remainder is the next least significant bit. This process repeats until the quotient becomes zero. Example: 
```
13 / 2 = 6 R 1
6 / 2 = 3 R 0
3 / 2 = 1 R 1
1 / 2= 0 R 1
```
So `13` in decimal is `1101` in binary which basically tells you to look at letters corresponding to where 1's occurred in the bit stream, which in this case means positions 0, 2, and 3 (reading the bits right to left) = `acd`
# Sample run
```
Enter Napier's number: -ab2
Something is wrong. Try again.
Enter Napier's number: abc
The first number is: 7
Enter Napier's number: he lo
Something is wrong. Try again.
Enter Napier's number: hello
Thesecond number is 20,624
Enter the desired arithmetic operation: #
Something is wrong. Try again.
Enter the desired arithmetic operation: -
The result is -20,617 or -adhmo
Do you want to repeat the program? Enter y for yes, n for no:
```
# Extra credit
Extra credit of 10 points may be earned if your output handles the issue of an excessive number of z’s in the resulting Napier value. This would be beneficial when the resulting string might require millions of characters (most of which would be z’s). Specifically, if the result converted to Napier requires more than 100 z’s, instead use a special notation for the z characters as follows: In parenthesis include a single z followed by an asterisk, followed by an integer representing how many z’s are required. For example, if 532 z’s are required use: `(z*532)` as the resulting Napier value. However, if only 10 z’s are needed, then you should list all 10 z’s (`abzzzzzzzzzz` but, 11 z’s would produce `ab(z*11)`). An example run and resulting output is illustrated below:
```
Enter Napier: zzba
Enter Napier: zzf
Enter operator: *
The numbers are: 67108867 671088964503601976180832
67108867 * 67108896 = 4,503,601,976,180,832 or fg(z*134217798)
Do another?: y
Enter Napier: zz
Enter Napier: zz
Enter operator: *
The numbers are: 67108864 671088644503599627370496
67108864 * 67108864 = 4,503,599,627,370,496 or (z*134217728)
Do another?: y
Enter Napier: z
Enter Napier: cfg
Enter operator: *
The numbers are: 33554432 1003355443200
33554432 * 100 = 3,355,443,200 or (z*100)
Do another?: y
Enter Napier: z
Enter Napier: acfg
Enter operator: *
The numbers are: 33554432 1013388997632
33554432 * 101 = 3,388,997,632 or (z*101)
Do another?: y
Enter Napier: adcgrz
Enter Napier: bd
Enter operator: *
The numbers are: 33685581 10336855810
33685581 * 10 = 336,855,810 or bijsuzzzzzzzzzz
Do another?:y
Enter Napier: adcgrz
Enter Napier: 11
ERROR! Enter Napier: abd
Enter operator: *
The numbers are: 33685581 11370541391
33685581 * 11 = 370,541,391 or abcdgijrsu(z*11)
Do another?:n
```
