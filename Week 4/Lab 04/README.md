# a.  
Write a short program called `ascii.py` in which you ask a user to enter a string, then you iterate over that string, and for each character in that string, you print what it is, and its ASCII decimal value.  
For example, if a user enters: `TCSS 142`, your output should be:  
```
The ASCII value of T is: 84  
The ASCII value of C is: 67  
The ASCII value of S is: 83  
The ASCII value of S is: 83  
The ASCII value of   is: 32  
The ASCII value of 1 is: 49  
The ASCII value of 4 is: 52  
The ASCII value of 2 is: 50
```

# b.  
Use nested if statements to solve the following problem:  
Write a programnamed `Octants.py` that asks the user to enter three real numbers `x`, `y`, and `z` that represent coordinates of a point in a 3d space.  
Based on the input, the program prints the octant for that point.  
If one of the coordinates is a zero, you need to print a message that the point lies on an axis or a plane and does not belong to any of the octants.  
Example: (`x`, `y`, `z`):  
```
(5, 120, -6) prints octant 5  
(-6, 5, -90) prints octant 6  
(0, 90, 0) prints point lies on an axis or a plane and does not belong to any of the octants.  
(0, 90, 90) prints point lies on an axis or a plane and does not belong to any of the octants.  
```
To help you visualize this, the views of a 3d space and octant numbering are provided below.  
<img src="https://upload.wikimedia.org/wikipedia/commons/6/60/Octant_numbers.svg" width="450" alt="Multi-colored coordinate grid with roman numerals I through VII, excluding VI as it is obscured in the far lower left.">
<img src="https://mathworld.wolfram.com/images/eps-gif/Octant_800.gif" width="500" alt="coordinate grid with intersection x/y/z planes as different colors. Each octant is represented by a set of positive and negative signs.">
