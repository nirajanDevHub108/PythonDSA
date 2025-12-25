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

#pattern-6
'''
12345
1234
123
12
1 
line=n
j =n-i+1 to print exact pattern
'''
for i in range(n):
    for j in range(1,n-i+1):
        print(j,end="")
    print()

'''
    *
   ***
  *****
 *******
*********
[4 , 1, 4]
[3 , 3, 3]
[2 , 5, 2]
[1 , 7, 1]
[0 , 9, 0]
 n=5
 space calculation=(n-i-1 )
 i=o 
 5-i-1=4
 i=1
 5-1-1=3
 5-2-1=2
 5-3-1=1
 5-4-1=0

 start caclulation 2*i+1
 j=0
 2*i+1=2*0+1=1
 2*1+1=3
 2*2+1=5
 2*3+1=7
 2*4+1=9
'''
# 1
# 3 5
# 7 9 11
# 13 15 17 19