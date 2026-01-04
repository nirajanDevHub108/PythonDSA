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