n=5
for i in range(1,n+1):
    for j in range(n):
        print("*",end="")
    print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()

#1
#22
#333
#4444
#55555  
#no of line =n

for i in range(1,n+1):
    for j in range(i):
        print(i,end="")
    print()

# *****
# ****
# ***
# **
# *

#no of line =n pattern -5
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()  



# 1
# 3 5
# 7 9 11
# 13 15 17 19