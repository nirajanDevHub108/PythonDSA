"""
Given two inputs that are stored in variables a and n, 
you need to print a, n times in a single line without space between them.
 Output must have a newline at the end.

Examples:

Input: a = "Hello", n = 5
Output: HelloHelloHelloHelloHello
Explanation: a is printed n=5 times in a single line without space between them
"""
# User function Template for python3
#User function Template for python3

a = input()
n = int(input())
#Write your code below that prints a n times
for i in range (n):
    print(a,end="")
print()