# Will Swoveland

# This assignment is weird - I used a lot of shortcuts to achieve the end-result.

s1 = "This"
s2 = "That"

i1 = 123
i2 = -5

# Multi-line for readability. Putting a string in parentheses () allows you to make one continuous string multi-line.
formatted_text = (
"{:>10}" "{:>9}"
"\n"
"{:>6}" "{:>9}"
"\n"
"{:>7}" "{:>9}"
"\n"
"{:06.2f}"
"\n"
"{:>3}")

# Each set of brackets in formatted_text is a placeholder for a variable.
# When I use the format() function below, the variables are supplemented
# sequentially. First s2, then s1, etc.
print(formatted_text.format(s2, s1, i1, i2, s1, s2, i1, i2)) 

d1 = 123.4
d2 = 3.1315926535

# Text is right-justified, with a field width of 10.
print(("{:>10} {:>10}").format(d1, d2))

# Text is right-justified.
print(("{:>} {:>}").format(d1, d2))

# d1 is left-justified with a field width of 15, decimal accuracy of 4.
# d2 is left-justified with a field width of 15, decimal accuracy of 10.
print(("{:<15.4f} {:<15.10f}").format(d1, d2))

# String containing s1 and d1, left-justified with a field width of 2.
print(("{:<2} {:<2}").format(s1, d1))
