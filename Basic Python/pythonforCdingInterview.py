#tips and trick for coding interview
# 
#  
#1.variable are dynamically typed
n=0
print('n =' , n)

n='abc'
print('n =' , n)

#Multiple assignments
n,m = 0, "abc"
n , m , z = 0.123 , "abc" , True

#Increment
n = n + 1 #allowed
n +=1 #allowed

#None is null (absence of value)
n=4
n=None
print(n)

#if statemnet don't need parantheses or curly braces
n=1
if n > 2:
    n -= 1
elif n == 2:
    n *=2
else:
    n+=2

# paranthesis is needed for multi-line conditions
#and = &&
#or = ||

n,m = 1,2
if ((n > 2 and n != m) or n == m):
    n+=1

#while loops are similiar 
# n=0
# while n < 5:
#     print(n)
#     n += 1


# for loop i = 0 to i =4
for i in range(5):
    print(i)
# for loop i = 2 to i =6
for i in range(2,6):
    print(i)

print('_________________')
#division is decimal by default
print(5/2)

print(5 // 2) # double slash round down the decimal part

print( -3 // 2)#most langauge round towards 0 by default so neg numbers will round down

print(int(-3 / 2)) #workaround for rounding towards zero is to use decimal division and then convert to int