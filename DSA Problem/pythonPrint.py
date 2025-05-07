"""
You are given two variables, a and b. Your task is to print these variables in the following formats:

With space: Print a and b in a single line, separated by a space, followed by a newline.
Without newline: Print a and b separated by a space, but do not end the output with a newline.
With separator: Print a and b separated by a specified separator, followed by a newline.
Without space: Print a and b in a single line, with no spaces between them, followed by a newline."""

#User function Template for python3
a = input()
b = input()
separator = input()[0]

########### Write your code below ###############

# Print with space
print(a + " " + b ,end='\n' )

# Print without newline at the end
print(a + " " + b, end="")

# Print with separator
print(a + separator + b,end='\n')

# Print without space
print(a + b ,end='\n')